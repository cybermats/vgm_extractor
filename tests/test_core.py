import io
from unittest import TestCase

import vgm.command
import vgm.core
from tests import test_core_data

DATA = test_core_data.get_data()


class TestCore(TestCase):
    def test_reader_none(self):
        with self.assertRaises(AttributeError):
            vgm.core.reader(None)

    def test_reader_not_vgm(self):
        f = io.BytesIO(b"foobar")
        r = vgm.core.reader(f)
        self.assertIsNone(r)

    def test_reader_vgm_header_100(self):
        buffer = DATA["simple_100"]
        f = io.BytesIO(buffer)
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        self.assertEqual(r.size(), len(buffer))
        self.assertEqual(r.version, 100)
        self.assertEqual(r.data_start, 0x40)
        self.assertTrue(r.supports("ym2151"))
        self.assertEqual(r.clock("ym2151"), 0x03)

    def test_reader_vgm_header_100_none(self):
        buffer = DATA["simple_100_none"]
        f = io.BytesIO(buffer)
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        self.assertEqual(r.size(), len(buffer))
        self.assertEqual(r.version, 100)
        self.assertEqual(r.data_start, 0x40)
        self.assertFalse(r.supports("ym2151"))
        self.assertEqual(r.clock("ym2151"), 0x0)

    def test_reader_vgm_header_101(self):
        buffer = DATA["simple_101"]
        f = io.BytesIO(buffer)
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        self.assertEqual(r.size(), len(buffer))
        self.assertEqual(r.version, 101)
        self.assertEqual(r.data_start, 0x40)
        self.assertTrue(r.supports("ym2151"))
        self.assertEqual(r.clock("ym2151"), 0x03)

    def test_reader_vgm_header_110(self):
        buffer = DATA["simple_110"]
        f = io.BytesIO(buffer)
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        self.assertEqual(r.size(), len(buffer))
        self.assertEqual(r.version, 110)
        self.assertEqual(r.data_start, 0x40)
        self.assertTrue(r.supports("ym2151"))
        self.assertEqual(r.clock("ym2151"), 0x0B)

    def test_reader_vgm_header_150(self):
        buffer = DATA["simple_150"]
        f = io.BytesIO(buffer)
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        self.assertEqual(r.size(), len(buffer))
        self.assertEqual(r.version, 150)
        self.assertEqual(r.data_start, 0x80)

    def test_reader_vgm_header_compressed(self):
        f = io.BytesIO(DATA["compressed"])
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)

    def test_vgm_commands(self):
        f = io.BytesIO(DATA["all_commands"])
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        counter = 0
        for idx, cmd in enumerate(r):
            self.assertEqual(cmd.command_id, idx)
            counter += 1
        self.assertEqual(counter, 256)

    def test_vgm_waits(self):
        f = io.BytesIO(DATA["waits"])
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        it = iter(r)
        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 0)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 0x201)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 735)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 882)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 1)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 2)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 16)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.EOS)

    def test_vgm_simple_ym2151(self):
        f = io.BytesIO(DATA["simple_ym2151"])
        r = vgm.core.reader(f)
        self.assertIsNotNone(r)
        it = iter(r)
        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 0)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.YM2151)
        self.assertEqual(cmd.reg, 0xAA)
        self.assertEqual(cmd.value, 0xDD)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 0x201)

        cmd = next(it)
        self.assertEqual(cmd.command_type, None)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.WAIT)
        self.assertEqual(cmd.samples, 735)

        cmd = next(it)
        self.assertEqual(cmd.command_type, vgm.command.VgmCommandType.EOS)

    def test__read32(self):
        self.assertEqual(vgm.core._read32(io.BytesIO(b"\x12\x34\x56\x78")), 0x78563412)

    def test__read32_short(self):
        with self.assertRaises(EOFError):
            vgm.core._read32(io.BytesIO(b"\x12"))

    def test__read16(self):
        self.assertEqual(vgm.core._read16(io.BytesIO(b"\x12\x34")), 0x3412)

    def test__read16_short(self):
        with self.assertRaises(EOFError):
            vgm.core._read16(io.BytesIO(b""))

    def test__read8(self):
        self.assertEqual(vgm.core._read8(io.BytesIO(b"\x12")), 0x12)

    def test__read8_short(self):
        with self.assertRaises(EOFError):
            vgm.core._read8(io.BytesIO(b""))

    def test__read_bcd(self):
        self.assertEqual(vgm.core._readBCD(io.BytesIO(b"\x12\x34\x56\x78")), 12345678)

    def test__read_bcd_short(self):
        with self.assertRaises(EOFError):
            vgm.core._readBCD(io.BytesIO(b"\x12\x34"))
