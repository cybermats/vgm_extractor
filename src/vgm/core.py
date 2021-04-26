import gzip
import io
import logging
import struct
import typing

from vgm.command import VgmCommand, WaitCommand, EOSCommand
from vgm.ym2151 import YM2151Command


def _read32(file: typing.BinaryIO) -> int:
    b = file.read(4)
    if b is None or len(b) != 4:
        raise EOFError
    return struct.unpack("I", b)[0]


def _read16(file: typing.BinaryIO) -> int:
    b = file.read(2)
    if b is None or len(b) != 2:
        raise EOFError
    return struct.unpack("H", b)[0]


def _read8(file: typing.BinaryIO) -> int:
    b = file.read(1)
    if b is None or len(b) != 1:
        raise EOFError
    return struct.unpack("B", b)[0]


def _readBCD(file: typing.BinaryIO) -> int:
    b = file.read(4)
    if b is None or len(b) != 4:
        raise EOFError
    o = 0
    for item in b:
        for val in (item >> 4, item & 0x0F):
            o *= 10
            o += val

    return o


class Vgm:
    data_start = 0x40
    clocks = {}

    def __init__(self, f: typing.BinaryIO):
        self.file = f
        self.eof_offset = _read32(self.file)
        self.version = _readBCD(self.file)
        _read32(self.file)
        self.clocks["ym2413"] = _read32(self.file)
        self.file.seek(0x30, io.SEEK_SET)
        self.clocks["ym2151"] = _read32(self.file)
        if self.version < 110:
            self.clocks["ym2151"] = self.clocks["ym2413"]

        if self.version >= 150:
            self.data_start = 0x34 + _read32(self.file)

        self.file.seek(self.data_start, io.SEEK_SET)
        return

    def size(self) -> int:
        return self.eof_offset + 4

    def supports(self, chip: str) -> bool:
        return chip in self.clocks and self.clocks[chip] > 0

    def clock(self, chip: str) -> int:
        return self.clocks[chip]

    def __iter__(self):
        return self

    def __next__(self):
        cmd = self.file.read(1)
        if cmd is None or len(cmd) == 0:
            raise StopIteration
        return command(cmd[0], self.file)


def command(cmd_id: int, f: typing.BinaryIO) -> VgmCommand:
    if (
        (cmd_id < 0x30)
        or (cmd_id == 0x60)
        or (0x64 <= cmd_id <= 0x65)
        or (0x69 == cmd_id)
        or (0x80 <= cmd_id < 0x90)
        or (0x96 <= cmd_id < 0xA0)
    ):
        return VgmCommand(cmd_id)

    if 30 <= cmd_id < 0x40:
        return VgmCommand(cmd_id, f.read(1))
    elif cmd_id < 0x4F:
        return VgmCommand(cmd_id, f.read(2))
    elif cmd_id < 0x51:
        return VgmCommand(cmd_id, f.read(1))
    elif cmd_id < 0x54:
        return VgmCommand(cmd_id, f.read(2))
    elif cmd_id == 0x54:
        reg = _read8(f)
        value = _read8(f)
        return YM2151Command(cmd_id, reg, value)
    elif cmd_id < 0x60:
        return VgmCommand(cmd_id, f.read(2))
    elif cmd_id == 0x61:
        return WaitCommand(cmd_id, _read16(f))
    elif cmd_id == 0x62:
        return WaitCommand(cmd_id, 735)
    elif cmd_id == 0x63:
        return WaitCommand(cmd_id, 882)
    elif cmd_id == 0x66:
        return EOSCommand(cmd_id, 882)
    elif cmd_id == 0x67:
        buffer = f.read(6)
        # Pad to handle uint on aligned boundaries?
        (tt, ss) = struct.unpack("<xBI", buffer)
        tt = tt
        ss = ss
        return VgmCommand(cmd_id, f.read(ss))
    elif cmd_id == 0x68:
        buffer = f.read(11)
        (cc, ooB, ooH, ddB, ddH, ssB, ssH) = struct.unpack("<xBBHBHBH", buffer)
        cc = cc
        oo = (ooH * 256) + ooB
        dd = (ddH * 256) + ddB
        ss = (ssH * 256) + ssB
        return VgmCommand(cmd_id, f.read(ss))
    elif cmd_id < 0x80:
        return WaitCommand(cmd_id)
    elif cmd_id < 0x92:
        return VgmCommand(cmd_id, f.read(4))
    elif cmd_id == 0x92:
        return VgmCommand(cmd_id, f.read(5))
    elif cmd_id == 0x93:
        return VgmCommand(cmd_id, f.read(10))
    elif cmd_id == 0x94:
        return VgmCommand(cmd_id, f.read(1))
    elif cmd_id == 0x95:
        return VgmCommand(cmd_id, f.read(4))
    elif cmd_id < 0xC0:
        return VgmCommand(cmd_id, f.read(2))
    elif cmd_id < 0xE0:
        return VgmCommand(cmd_id, f.read(3))
    else:
        return VgmCommand(cmd_id, f.read(4))


def reader(vgmfile: typing.BinaryIO) -> typing.Optional[Vgm]:
    logging.info(f"opening {vgmfile}")
    header = vgmfile.read(4)

    if header[:2] == b"\x1f\x8b":
        vgmfile.seek(0)
        vgmfile = gzip.open(vgmfile, "rb")
        header = vgmfile.read(4)

    if header != b"Vgm ":
        return None
    return Vgm(vgmfile)
