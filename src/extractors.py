import json
from typing import Dict

import vgm.ym2151
from vgm.ym2151.state import State
import xrns.parts.song
import xrns.parts.pattern
from xrns.writer import writer
from tools import smart_open
from vgm.ym2151 import config


def extract_tracks_to_xrns(s: State, track_filename, ticks_per_note):
    print(f"Writing xrns {track_filename}...")

    song = xrns.parts.song.Song(tracks=8, instruments=len(s.configs))

    channel_count = 8
    sample_freq = 44100
    notes_per_beat = 4
    line_count = 64

    note_length = ticks_per_note / sample_freq
    beat_length = note_length * notes_per_beat
    bpm = 60 / beat_length
    song.globals.beats_per_min = int(bpm)

    for ch in range(channel_count):
        for n in s.key_presses(ch):
            total_row = n.sample // ticks_per_note
            row = total_row % line_count
            pattern = total_row // line_count
            instr = None
            if n.config_id >= 0:
                instr = f"{n.config_id:0>2X}"

            pan = None
            if not n.right or not n.left:
                if n.right:
                    pan = "00"
                else:
                    pan = "F0"

            song.pattern_pool.add_note(pattern, ch, row, n.xrns_note(), instr, pan)

    for p in range(len(song.pattern_pool.patterns)):
        song.pattern_sequence.add_pattern(p)

    with open(track_filename, "wb") as f:
        writer(f, song)


def extract_tracks(s, track_filename, ticks_per_note):
    print(f"Writing tracks to {track_filename}...")
    channel_iters = [iter(s.key_presses(ch)) for ch in range(8)]
    channel_notes: Dict[int, vgm.ym2151.state.Note] = {}
    for idx, it in enumerate(channel_iters):
        try:
            note = next(it)
            channel_notes[idx] = note
        except StopIteration:
            pass

    with smart_open(track_filename, "w") as fo:
        header = ["Samples", "Row", "Pattern", "Total Row", "Fraction"]
        for i in range(8):
            header.append(f"Channel {i+1}")
        fo.write("{}\n".format(",".join(header)))

        channel_count = 8
        line_count = 64
        total_row = 0
        note_row = [""] * channel_count

        while len(channel_notes):
            samples = [n.sample for n in channel_notes.values()]
            current_sample = min(samples)
            current_row = current_sample // ticks_per_note
            if current_row != total_row:
                row = [
                    str(current_sample),
                    str(total_row % line_count),
                    str(total_row // line_count),
                    str(total_row),
                    "{:.2}".format((current_sample / ticks_per_note) % 1),
                ] + note_row
                fo.write(f'{",".join(row)}\n')

                while total_row + 1 < current_row:
                    total_row += 1
                    row = [
                        str(current_sample),
                        str(total_row % line_count),
                        str(total_row // line_count),
                        str(total_row),
                        "{:.2}".format((current_sample / ticks_per_note) % 1),
                    ] + [""] * channel_count
                    fo.write(f'{",".join(row)}\n')

                total_row = current_row
                note_row = [""] * channel_count

            for ch in range(channel_count):
                if (
                    ch in channel_notes
                    and channel_notes[ch].sample // ticks_per_note == current_row
                ):
                    note_row[ch] = str(channel_notes[ch])
                    try:
                        note = next(channel_iters[ch])
                        channel_notes[ch] = note
                    except StopIteration:
                        del channel_notes[ch]


def extract_instruments(instr_filename, s):
    print(f"Writing instruments to {instr_filename}...")
    js = json.dumps(s.configs, cls=config.ConfigEncoder, indent="\t")
    with smart_open(instr_filename, "w") as fo:
        fo.write(js)
        fo.write("\n")
