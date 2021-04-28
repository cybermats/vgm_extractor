import argparse

# Press the green button in the gutter to run the script.

import vgm.core

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VGM Extractor")
    parser.add_argument(
        "file", metavar="file", type=str, help="vgm file for extraction"
    )

    args = parser.parse_args()

    vgm.core.reader(args.file)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
