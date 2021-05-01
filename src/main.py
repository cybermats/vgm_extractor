import argparse

# Press the green button in the gutter to run the script.
import contextlib
import json
import sys

import vgm.core
from vgm.ym2151 import state, config
from typing import Dict, Set, List


@contextlib.contextmanager
def smart_open(filename: str, mode: str):
    if filename and filename != "-":
        fh = open(filename, mode)
    elif mode.startswith("w"):
        fh = sys.stdout
    elif mode.startswith("r"):
        fh = sys.stdin
    else:
        raise Exception("Unknown mode")

    try:
        yield fh
    finally:
        if fh is not sys.stdout and fh is not sys.stdin:
            fh.close()


def extract_tracks(s, track_filename):
    channel_iters = [iter(s.key_presses(ch)) for ch in range(8)]
    channel_notes: Dict[int, vgm.ym2151.state.Note] = {}
    for idx, it in enumerate(channel_iters):
        try:
            note = next(it)
            channel_notes[idx] = note
        except StopIteration:
            pass

    ticks_per_note = s.ticks_per_note()
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
    js = json.dumps(s.configs, cls=config.ConfigEncoder, indent="\t")
    with smart_open(instr_filename, "w") as fo:
        fo.write(js)
        fo.write("\n")


def process_vgm_file(cmds):
    st = state.State()

    for cmd in cmds:
        if isinstance(cmd, config.YM2151Command):
            st.apply(cmd)
        elif isinstance(cmd, vgm.core.WaitCommand):
            st.beat(cmd.samples)

    return st


def main(vgm_filename: str, instr_filename: str, track_filename: str):
    with smart_open(vgm_filename, "rb") as f:
        print("Opening file: {}".format(args.file))
        cmds = vgm.core.reader(f)

        s = process_vgm_file(cmds)

        extract_instruments(instr_filename, s)

        extract_tracks(s, track_filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VGM Extractor")
    parser.add_argument(
        "file", metavar="file", type=str, help="vgm file for extraction"
    )
    parser.add_argument(
        "-i", "--instrument", type=str, help="Output file for instruments"
    )
    parser.add_argument("-t", "--track", type=str, help="Output file for tracks")

    args = parser.parse_args()

    main(args.file, args.instrument, args.track)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
