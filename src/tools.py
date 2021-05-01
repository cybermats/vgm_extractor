import contextlib
import sys


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
