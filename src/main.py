import argparse

# Press the green button in the gutter to run the script.

import vgm.core
from extractors import extract_tracks, extract_instruments
from tools import smart_open
from vgm.ym2151 import state, config


def process_vgm_file(cmds):
    st = state.State()

    for cmd in cmds:
        if isinstance(cmd, config.YM2151Command):
            st.apply(cmd)
        elif isinstance(cmd, vgm.core.WaitCommand):
            st.beat(cmd.samples)

    return st


def main(
    vgm_filename: str,
    instr_filename: str,
    track_filename: str,
    ticks_per_note: int = None,
):
    with smart_open(vgm_filename, "rb") as f:
        print("Opening file: {}".format(args.file))
        cmds = vgm.core.reader(f)

        s = process_vgm_file(cmds)

        if not ticks_per_note:
            print("Calculating Ticks Per Note", end="")
            ticks_per_note = s.ticks_per_note(show_progress=True)

        print(f"Ticks per Note: {ticks_per_note}")
        if instr_filename:
            extract_instruments(instr_filename, s)

        if track_filename:
            extract_tracks(s, track_filename, ticks_per_note)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VGM Extractor")
    parser.add_argument(
        "file", metavar="file", type=str, help="vgm file for extraction"
    )
    parser.add_argument(
        "-i", "--instrument", type=str, help="Output file for instruments"
    )
    parser.add_argument("-t", "--track", type=str, help="Output file for tracks")
    parser.add_argument(
        "-tn",
        "--ticks-per-note",
        type=int,
        help="Specify Ticks per Note instead of calculating it.",
    )

    args = parser.parse_args()

    main(args.file, args.instrument, args.track, args.ticks_per_note)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
