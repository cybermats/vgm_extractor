import copy
from unittest import TestCase

import vgm.ym2151
import vgm.ym2151.config
from vgm.ym2151.config import create, Waveform, BaseConfig, Operators
from vgm.ym2151.state import State


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
        self.assertListEqual(self.state.key_presses(0), [])
        self.assertEqual(self.state.key_presses(1), [])
        self.state.apply(create(0x08, 0x00))
        self.assertEqual(len(self.state.key_presses(0)), 1)
        self.assertListEqual(self.state.key_presses(1), [])
        self.assertEqual(len(self.state.configs), 1)

    def test_apply_key_on_simple(self):
        self.assertEqual(len(self.state.configs), 0)
        self.state.apply(create(0x08, (1 << 3) | 5))
        self.assertEqual(len(self.state.key_presses(5)), 1)
        self.assertListEqual(self.state.key_presses(0), [])
        self.assertEqual(self.state.key_presses(5)[0].config_id, 0)
        self.assertEqual(len(self.state.configs), 1)

    def test_apply_key_on_simple_multiple_samples(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.key_presses(5)), 1)
        self.assertEqual(self.state.key_presses(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x18, 0x55))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.key_presses(5)), 2)
        self.assertEqual(self.state.key_presses(5)[1].config_id, 1)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)

        self.state.apply(create(0x0F, (1 << 7)))
        self.state.apply(create(0x08, (1 << 3) | 3))

        self.assertEqual(len(self.state.configs), 3)
        self.assertEqual(len(self.state.key_presses(3)), 1)
        self.assertEqual(self.state.key_presses(3)[0].config_id, 2)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[0].noise, False)
        self.assertEqual(self.state.configs[1].lfo, 0x55)
        self.assertEqual(self.state.configs[1].noise, False)
        self.assertEqual(self.state.configs[2].lfo, 0x55)
        self.assertEqual(self.state.configs[2].noise, True)

    def test_apply_key_on_single_sample_many_notes(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.key_presses(5)), 1)
        self.assertEqual(self.state.key_presses(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.key_presses(5)), 2)
        self.assertEqual(self.state.key_presses(5)[1].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

    def test_apply_key_on_reuse_sample_many_notes(self):
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.key_presses(5)), 1)
        self.assertEqual(self.state.key_presses(5)[0].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)

        self.state.apply(create(0x18, 0x55))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.key_presses(5)), 2)
        self.assertEqual(self.state.key_presses(5)[1].config_id, 1)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)

        self.state.apply(create(0x18, 0x0))
        self.state.apply(create(0x08, (1 << 3) | 5))

        self.assertEqual(len(self.state.configs), 2)
        self.assertEqual(len(self.state.key_presses(5)), 3)
        self.assertEqual(self.state.key_presses(5)[2].config_id, 0)
        self.assertEqual(self.state.configs[0].lfo, 0)
        self.assertEqual(self.state.configs[1].lfo, 0x55)

    def test_apply_channel_control_left_right_single_channel(self):
        ch = 0
        fb = 5
        cxn = 7
        self.assertFalse(self.state.channel_config(ch).right)
        self.assertFalse(self.state.channel_config(ch).left)
        self.assertEqual(self.state.channel_config(ch).fb, 0)
        self.assertEqual(self.state.channel_config(ch).connection, 0)
        self.state.apply(create(0x20 | ch, (1 << 7) | (fb << 3) | cxn))
        self.assertTrue(self.state.channel_config(ch).right)
        self.assertFalse(self.state.channel_config(ch).left)
        self.assertEqual(self.state.channel_config(ch).fb, fb)
        self.assertEqual(self.state.channel_config(ch).connection, cxn)

        self.state.apply(create(0x20 | ch, (1 << 6)))
        self.assertFalse(self.state.channel_config(ch).right)
        self.assertTrue(self.state.channel_config(ch).left)
        self.assertEqual(self.state.channel_config(ch).fb, 0)
        self.assertEqual(self.state.channel_config(ch).connection, 0)

    def test_apply_channel_control_left_right_multiple_channels(self):
        ch = 1
        self.assertFalse(self.state.channel_config(ch).right)
        self.assertFalse(self.state.channel_config(ch).left)
        self.state.apply(create(0x20 | ch, (1 << 7)))
        self.assertTrue(self.state.channel_config(ch).right)
        self.assertFalse(self.state.channel_config(ch).left)
        ch = 2
        self.state.apply(create(0x20 | ch, (1 << 6)))
        self.assertFalse(self.state.channel_config(ch).right)
        self.assertTrue(self.state.channel_config(ch).left)

        self.assertTrue(self.state.channel_config(1).right)
        self.assertFalse(self.state.channel_config(1).left)

    def test_apply_key_code(self):
        ch = 2
        octave = 3
        note = 4
        self.assertEqual(self.state.channel_config(ch).octave, 0)
        self.assertEqual(self.state.channel_config(ch).note, 0)
        self.state.apply(create(0x28 | ch, octave << 4 | note))
        self.assertEqual(self.state.channel_config(ch).octave, octave)
        self.assertEqual(self.state.channel_config(ch).note, note)

    def test_apply_key_fraction(self):
        ch = 2
        kf = 63
        self.assertEqual(self.state.channel_config(ch).key_fraction, 0)
        self.state.apply(create(0x30 | ch, kf << 2))
        self.assertEqual(self.state.channel_config(ch).key_fraction, kf)

    def test_apply_phase_amp_mod_sens(self):
        ch = 2
        pms = 6
        ams = 3
        self.assertEqual(self.state.channel_config(ch).pms, 0)
        self.assertEqual(self.state.channel_config(ch).ams, 0)
        self.state.apply(create(0x38 | ch, (pms << 4) | ams))
        self.assertEqual(self.state.channel_config(ch).pms, pms)
        self.assertEqual(self.state.channel_config(ch).ams, ams)

    def assert_single_field(
        self, reg_address: int, reg_value: int, field_name: str, expected_value: int
    ):
        all_names = list(vars(vgm.ym2151.config.OperatorConfig()).keys())
        self.assertTrue(field_name in all_names)
        for ch in range(8):
            for dev in range(4):
                for pre in range(dev):
                    for field in all_names:
                        actual = getattr(
                            self.state.channel_config(ch).operators[pre], field
                        )
                        expected = 0
                        if field == field_name:
                            expected = expected_value
                        self.assertEqual(actual, expected)

                self.state.apply(create(reg_address | dev << 3 | ch, reg_value))

                for field in all_names:
                    actual = getattr(
                        self.state.channel_config(ch).operators[dev], field
                    )
                    expected = 0
                    if field == field_name:
                        expected = expected_value
                    self.assertEqual(actual, expected)

                for post in range(dev + 1, 4):
                    for field in all_names:
                        actual = getattr(
                            self.state.channel_config(ch).operators[post], field
                        )
                        expected = 0
                        self.assertEqual(actual, expected)

            for dev in range(4):
                for pre in range(dev):
                    for field in all_names:
                        actual = getattr(
                            self.state.channel_config(ch).operators[pre], field
                        )
                        expected = 0
                        self.assertEqual(actual, expected)

                self.state.apply(create(reg_address | dev << 3 | ch, 0))

                for field in all_names:
                    actual = getattr(
                        self.state.channel_config(ch).operators[dev], field
                    )
                    expected = 0
                    self.assertEqual(actual, expected)

                for post in range(dev + 1, 4):
                    for field in all_names:
                        actual = getattr(
                            self.state.channel_config(ch).operators[post], field
                        )
                        expected = 0
                        if field == field_name:
                            expected = expected_value
                        self.assertEqual(actual, expected)

    def test_apply_dt1_mul(self):
        reg = 0x40
        first_detune = 6
        multiply = 15
        self.assert_single_field(reg, first_detune << 4, "first_detune", first_detune)
        self.assert_single_field(reg, multiply, "multiply", multiply)

    def test_apply_tl(self):
        reg = 0x60
        total_level = 6
        self.assert_single_field(reg, total_level, "total_level", total_level)

    def test_apply_eg_attack(self):
        reg = 0x80
        key_scale = 3
        attack_rate = 31
        self.assert_single_field(reg, key_scale << 6, "key_scale", key_scale)
        self.assert_single_field(reg, attack_rate, "attack_rate", attack_rate)

    def test_apply_eg_decay_1(self):
        reg = 0xA0
        ase = 1
        first_decay_rate = 31
        self.assert_single_field(reg, (1 << 7) if ase else 0, "ase", ase)

        self.assert_single_field(
            reg, first_decay_rate, "first_decay_rate", first_decay_rate
        )

    def test_apply_eg_decay_2(self):
        reg = 0xC0
        second_detune = 3
        second_decay_rate = 15
        self.assert_single_field(
            reg, second_detune << 6, "second_detune", second_detune
        )

        self.assert_single_field(
            reg, second_decay_rate, "second_decay_rate", second_decay_rate
        )

    def test_apply_eg_decay_level_release_rate(self):
        reg = 0xE0
        first_decay_level = 15
        release_rate = 15
        self.assert_single_field(
            reg, first_decay_level << 4, "first_decay_level", first_decay_level
        )

        self.assert_single_field(reg, release_rate, "release_rate", release_rate)


class TestConfig(TestCase):
    def test_get_attribute(self):
        cfg = BaseConfig()
        self.assertEqual(cfg.lfo, 0)

    def test_set_attribute(self):
        cfg = BaseConfig()
        cfg.lfo = 1
        self.assertEqual(cfg.lfo, 1)

    def test_deepcopy(self):
        cfg = BaseConfig()
        cp = copy.deepcopy(cfg)

        self.assertEqual(cfg, cp)
        cp.lfo = 1
        self.assertNotEqual(cfg.lfo, cp.lfo)
        self.assertNotEqual(cfg, cp)

    def test_equality(self):
        a = BaseConfig()
        a.lfo = 5
        b = BaseConfig()
        self.assertNotEqual(a, b)
        b.lfo = 5
        self.assertEqual(a, b)

    def test_equality_with_other(self):
        a = BaseConfig()
        self.assertNotEqual(a, 0)
        self.assertNotEqual(a, None)
        self.assertNotEqual(0, a)
        self.assertNotEqual(None, a)

    def test_get_wrong_attribute(self):
        a = BaseConfig()
        with self.assertRaises(AttributeError):
            _ = a.foo


class TestKeyOnSaves(TestCase):
    def setUp(self) -> None:
        self.state = State()

    def tearDown(self) -> None:
        self.state = None

    def test_key_on_full_config(self):
        channel = 1
        operator = 1
        enabled_operator = Operators.CAR1

        # Add noise freq (Basic Config)
        self.state.apply(create(0x0F, 0x1))
        # Add Connection (Channel Config)
        self.state.apply(create(0x20 | channel, 1))
        # Add Phase Multiply (Operator Config)
        self.state.apply(create(0x40 | operator << 3 | channel, 1))

        self.assertEqual(len(self.state.configs), 0)

        # Play note
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 1)

        # Play note again
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 1)
        # Check Noise Freq (Basic Config)
        self.assertEqual(self.state.configs[0].noise_freq, 1)
        # Check Connection (Channel Config)
        self.assertEqual(self.state.configs[0].connection, 1)
        # Check Phase Multiply (Operator Config)
        self.assertEqual(self.state.configs[0].operators[operator].multiply, 1)
        # Check Active Operators (Note Config)
        self.assertEqual(self.state.configs[0].enabled_operators, enabled_operator)

    def test_key_on_old_sample(self):
        channel = 1
        operator = 1
        enabled_operator = Operators.CAR1

        # Play note
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 1)

        # Add noise freq (Basic Config)
        self.state.apply(create(0x0F, 0x1))
        # Add Connection (Channel Config)
        self.state.apply(create(0x20 | channel, 1))
        # Add Phase Multiply (Operator Config)
        self.state.apply(create(0x40 | operator << 3 | channel, 1))

        # Play note with new config
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 2)

        # Add noise freq (Basic Config)
        self.state.apply(create(0x0F, 0x0))
        # Add Connection (Channel Config)
        self.state.apply(create(0x20 | channel, 0))
        # Add Phase Multiply (Operator Config)
        self.state.apply(create(0x40 | operator << 3 | channel, 0))

        # Play note again with old config
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        # Check no new configs stored
        self.assertEqual(len(self.state.configs), 2)

        # Config 0
        # Check Noise Freq (Basic Config)
        self.assertEqual(self.state.configs[0].noise_freq, 0)
        # Check Connection (Channel Config)
        self.assertEqual(self.state.configs[0].connection, 0)
        # Check Phase Multiply (Operator Config)
        self.assertEqual(self.state.configs[0].operators[operator].multiply, 0)
        # Check Active Operators (Note Config)
        self.assertEqual(self.state.configs[0].noise_freq, 0)
        # Config 1
        # Check Noise Freq (Basic Config)
        self.assertEqual(self.state.configs[1].noise_freq, 1)
        # Check Connection (Channel Config)
        self.assertEqual(self.state.configs[1].connection, 1)
        # Check Phase Multiply (Operator Config)
        self.assertEqual(self.state.configs[1].operators[operator].multiply, 1)
        # Check Active Operators (Note Config)
        self.assertEqual(self.state.configs[1].noise_freq, 1)

    def test_key_on_different_notes(self):
        channel = 1
        operator = 1
        enabled_operator = Operators.CAR1

        # Play note
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 1)

        self.assertEqual(len(self.state.key_presses(channel)), 1)
        self.assertEqual(self.state.key_presses(channel)[0].octave, 0)
        self.assertEqual(self.state.key_presses(channel)[0].note, 0)
        self.assertEqual(self.state.key_presses(channel)[0].key_fraction, 0)

        # Set different note
        self.state.apply(create(0x28 | channel, 0x1))

        # Play note with new config
        self.state.apply(create(0x08, enabled_operator << 3 | channel))

        self.assertEqual(len(self.state.configs), 1)
        self.assertEqual(len(self.state.key_presses(channel)), 2)
        self.assertEqual(self.state.key_presses(channel)[0].octave, 0)
        self.assertEqual(self.state.key_presses(channel)[0].note, 0)
        self.assertEqual(self.state.key_presses(channel)[0].key_fraction, 0)
        self.assertEqual(self.state.key_presses(channel)[1].octave, 0)
        self.assertEqual(self.state.key_presses(channel)[1].note, 1)
        self.assertEqual(self.state.key_presses(channel)[1].key_fraction, 0)
