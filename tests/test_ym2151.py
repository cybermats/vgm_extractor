from unittest import TestCase

from vgm.ym2151 import YM2151State, create


class TestYM2151State(TestCase):
    def setUp(self) -> None:
        self.state = YM2151State()

    def test_apply(self):
        cmd = create(0, 0)
        self.state.apply(cmd)

    def test_apply_noise_enable(self):
        cmd = create(0x0F, 0b10000000)
        self.assertFalse(self.state.noise)
        self.state.apply(cmd)
        self.assertTrue(self.state.noise)

    def test_apply_noise_freq(self):
        freq = 0x1F
        cmd = create(0x0F, freq)
        self.assertFalse(self.state.noise)
        self.assertEqual(self.state.noise_freq, 0)
        self.state.apply(cmd)
        self.assertFalse(self.state.noise)
        self.assertEqual(self.state.noise_freq, freq)

    def test_apply_lfo(self):
        freq = 0xAA
        cmd = create(0x18, freq)
        self.assertEqual(self.state.lfo, 0)
        self.state.apply(cmd)
        self.assertEqual(self.state.lfo, freq)

    def test_apply_phs_md(self):
        depth = 0x55
        cmd = create(0x19, depth + 0x80)
        self.assertEqual(self.state.phs_md, 0)
        self.state.apply(cmd)
        self.assertEqual(self.state.phs_md, depth)

    def test_apply_amp_md(self):
        depth = 0x55
        cmd = create(0x19, depth)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, 0)
        self.state.apply(cmd)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, depth)

    def test_apply_ctrl_output(self):
        self.assertFalse(self.state.ct1)
        self.assertFalse(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)

        self.state.apply(create(0x1B, 1 << 7))
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 6) | (1 << 7)))

        self.assertTrue(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 6)))

        self.assertTrue(self.state.ct1)
        self.assertFalse(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 7) | 2))
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.TRIANGLE)

    def test_apply_mix(self):
        self.state.apply(create(0x0F, 0xFF))
        self.assertTrue(self.state.noise)
        self.assertEqual(self.state.noise_freq, 0x1F)

        self.assertEqual(self.state.lfo, 0)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, 0)
        self.assertFalse(self.state.ct1)
        self.assertFalse(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 7)))

        self.assertTrue(self.state.noise)
        self.assertEqual(self.state.noise_freq, 0x1F)

        self.assertEqual(self.state.lfo, 0)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, 0)
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, YM2151State.Waveform.SAW)
