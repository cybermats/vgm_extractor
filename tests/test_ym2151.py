import copy
from unittest import TestCase

from vgm.ym2151 import State, create, Waveform, Config


class TestYM2151State(TestCase):
    def setUp(self) -> None:
        self.state = State()

    def tearDown(self) -> None:
        self.state = None

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
        self.assertEqual(self.state.waveform, Waveform.SAW)

        self.state.apply(create(0x1B, 1 << 7))
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 6) | (1 << 7)))

        self.assertTrue(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 6)))

        self.assertTrue(self.state.ct1)
        self.assertFalse(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 7) | 2))
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.TRIANGLE)

    def test_apply_mix(self):
        self.state.apply(create(0x0F, 0xFF))
        self.assertTrue(self.state.noise)
        self.assertEqual(self.state.noise_freq, 0x1F)

        self.assertEqual(self.state.lfo, 0)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, 0)
        self.assertFalse(self.state.ct1)
        self.assertFalse(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.SAW)

        self.state.apply(create(0x1B, (1 << 7)))

        self.assertTrue(self.state.noise)
        self.assertEqual(self.state.noise_freq, 0x1F)

        self.assertEqual(self.state.lfo, 0)
        self.assertEqual(self.state.phs_md, 0)
        self.assertEqual(self.state.amp_md, 0)
        self.assertFalse(self.state.ct1)
        self.assertTrue(self.state.ct2)
        self.assertEqual(self.state.waveform, Waveform.SAW)

    def test_apply_key_off(self):
        self.assertEqual(len(self.state.configs), 0)
        self.assertListEqual(self.state.channel(0), [])
        self.assertEqual(self.state.channel(1), [])
        self.state.apply(create(0x08, 0x00))
        self.assertEqual(len(self.state.channel(0)), 1)
        self.assertListEqual(self.state.channel(1), [])
        self.assertEqual(len(self.state.configs), 1)

    def test_apply_key_on_simple(self):
        self.assertEqual(len(self.state.configs), 0)
        self.state.apply(create(0x08, (1 << 3) | 5))
        self.assertEqual(len(self.state.channel(5)), 1)
        self.assertListEqual(self.state.channel(0), [])
        self.assertEqual(self.state.channel(5)[0].config_id, 0)
        self.assertEqual(len(self.state.configs), 1)

    def test_apply_key_on_simple_multiple_samples(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.channel(5)), 1)
        self.assertEqual(self.state.channel(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x18, 0x55))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.channel(5)), 2)
        self.assertEqual(self.state.channel(5)[1].config_id, 1)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)

        self.state.apply(create(0x0F, (1 << 7)))
        self.state.apply(create(0x08, (1 << 3) | 3))

        self.assertEqual(len(self.state.configs), 3)
        self.assertEqual(len(self.state.channel(3)), 1)
        self.assertEqual(self.state.channel(3)[0].config_id, 2)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[0].noise, False)
        self.assertEqual(self.state.configs[1].lfo, 0x55)
        self.assertEqual(self.state.configs[1].noise, False)
        self.assertEqual(self.state.configs[2].lfo, 0x55)
        self.assertEqual(self.state.configs[2].noise, True)

    def test_apply_key_on_single_sample_many_notes(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.channel(5)), 1)
        self.assertEqual(self.state.channel(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.channel(5)), 2)
        self.assertEqual(self.state.channel(5)[1].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

    def test_apply_key_on_reuse_sample_many_notes(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.channel(5)), 1)
        self.assertEqual(self.state.channel(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x18, 0x55))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.channel(5)), 2)
        self.assertEqual(self.state.channel(5)[1].config_id, 1)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)

        self.state.apply(create(0x18, 0x0))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.channel(5)), 3)
        self.assertEqual(self.state.channel(5)[2].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)


class TestConfig(TestCase):
    def test_get_attribute(self):
        cfg = Config()
        self.assertEqual(cfg.lfo, 0)

    def test_set_attribute(self):
        cfg = Config()
        cfg.lfo = 1
        self.assertEqual(cfg.lfo, 1)

    def test_deepcopy(self):
        cfg = Config()
        cp = copy.deepcopy(cfg)

        self.assertEqual(cfg, cp)
        cp.lfo = 1
        self.assertNotEqual(cfg.lfo, cp.lfo)
        self.assertNotEqual(cfg, cp)

    def test_equality(self):
        a = Config()
        a.lfo = 5
        b = Config()
        self.assertNotEqual(a, b)
        b.lfo = 5
        self.assertEqual(a, b)

    def test_equality_with_other(self):
        a = Config()
        self.assertNotEqual(a, 0)
        self.assertNotEqual(a, None)
        self.assertNotEqual(0, a)
        self.assertNotEqual(None, a)

    def test_get_wrong_attribute(self):
        a = Config()
        with self.assertRaises(AttributeError):
            _ = a.foo
