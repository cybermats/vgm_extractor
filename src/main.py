import argparse

# Press the green button in the gutter to run the script.
import contextlib
import functools
import json
import sys

import vgm.core
from vgm.ym2151 import state, config
from typing import Dict


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


def extract_tracts(s, track_filename):
    channel_iters = [iter(s.key_presses(ch)) for ch in range(8)]
    channel_notes: Dict[int, vgm.ym2151.state.Note] = {}
    for idx, it in enumerate(channel_iters):
        try:
            note = next(it)
            channel_notes[idx] = note
        except StopIteration:
            pass
    with smart_open(track_filename, "w") as fo:
        fo.write("Samples")
        for i in range(8):
            fo.write(f", Channel {i}")
        fo.write("\n")
        while len(channel_notes):
            samples = [n.sample for n in channel_notes.values()]
            current_sample = min(samples)
            cells = [current_sample]
            for ch in range(8):
                if (
                    ch not in channel_notes
                    or channel_notes[ch].sample != current_sample
                ):
                    cells.append("")
                else:
                    cells.append(channel_notes[ch])
                    try:
                        note = next(channel_iters[ch])
                        channel_notes[ch] = note
                    except StopIteration:
                        del channel_notes[ch]

            fo.write(",".join([str(c) for c in cells]))
            fo.write("\n")


def extract_instruments(instr_filename, s):
    js = json.dumps(s.configs, cls=config.ConfigEncoder, indent="\t")
    with smart_open(instr_filename, "w") as fo:
        fo.write(js)
        fo.write("\n")


def process_vgm_file(cmds):
    s = state.State()

    # curr_sample = 0
    # ticks = {}

    for cmd in cmds:
        if isinstance(cmd, config.YM2151Command):
            s.apply(cmd)
        elif isinstance(cmd, vgm.core.WaitCommand):
            s.beat(cmd.samples)
    #         curr_sample += cmd.samples
    #         ticks[curr_sample] = 1
    #
    # corr = []
    # off_start = 2000
    # off_end = 7000
    # for shift in range(off_start, off_end):
    #     diff = set()
    #     for key in ticks.keys():
    #         diff.add(key + shift)
    #         if key in diff:
    #             diff.remove(key)
    #         else:
    #             diff.add(key)
    #
    #     c = len(diff)
    #     corr.append(c)
    #     if shift % 1000 == 0:
    #         print(shift)
    #
    # with open("corr.csv", "w") as f:
    #     f.write("Offset,Correlation,Delay,TPM,BPM\n")
    #     f.write(
    #         "\n".join(
    #             [
    #                 f"{idx+off_start},{c},{(idx+off_start)/44100},{60/((idx+off_start)/44100)},{15/((idx+off_start)/44100)}"
    #                 for (idx, c) in enumerate(corr)
    #             ]
    #         )
    #     )
    return s


def main(vgm_filename: str, instr_filename: str, track_filename: str):
    with smart_open(vgm_filename, "rb") as f:
        print("Opening file: {}".format(args.file))
        cmds = vgm.core.reader(f)

        s = process_vgm_file(cmds)

        extract_instruments(instr_filename, s)

        extract_tracts(s, track_filename)


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
