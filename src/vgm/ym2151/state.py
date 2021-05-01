import copy
import typing
from typing import List, Union
from vgm.ym2151.config import (
    Waveform,
    ChannelConfig,
    BaseConfig,
    Config,
    YM2151Command,
    Operators,
    NoteConfig,
)
from vgm.ym2151.note import Note


class State:
    def __init__(self) -> None:
        self._channel_key_presses: List[List[Note]] = []
        self._channel_configs: List[ChannelConfig] = []
        self._note_configs: List[NoteConfig] = []
        self._current_base_config = BaseConfig()
        self.configs: List[Config] = []
        self._samples = 0

        for i in range(8):
            self._channel_key_presses.append([])
            self._channel_configs.append(ChannelConfig())
            self._note_configs.append(NoteConfig())

    def __getattr__(self, item: str) -> Union[int, bool, Waveform]:
        return getattr(self._current_base_config, item)

    def apply(self, cmd: YM2151Command) -> None:
        channel = cmd.reg & 0x07
        operator = (cmd.reg >> 3) & 0x03

        # Key On/Off
        if cmd.reg == 0x08:
            op = Operators((cmd.value >> 3) & 0xF)
            ch = cmd.value & 0x07
            config_id: int = next(
                (
                    i
                    for (i, c) in enumerate(self.configs)
                    if c.compare(
                        self._current_base_config, self._channel_configs[ch], op
                    )
                ),
                len(self.configs),
            )

            if len(self.configs) == config_id:
                if op:
                    self.configs.append(
                        Config(
                            config_id,
                            copy.deepcopy(self._current_base_config),
                            copy.deepcopy(self._channel_configs[ch]),
                            op,
                        )
                    )
                    self._current_base_config = copy.deepcopy(self._current_base_config)
                else:
                    config_id = -1

            note = Note(config_id, self._note_configs[ch], self._samples)
            self._channel_key_presses[cmd.value & 0x7].append(note)

        # Noise Enable, Noise Frequency
        elif cmd.reg == 0x0F:
            self._current_base_config.noise = (cmd.value & (1 << 7)) > 0
            self._current_base_config.noise_freq = cmd.value & 0x1F

        # LFO - Low Frequency Oscillator
        elif cmd.reg == 0x18:
            self._current_base_config.lfo = cmd.value

        # Phase and Amplitude Modulation
        elif cmd.reg == 0x19:
            if cmd.value & (1 << 7) > 0:
                self._current_base_config.phs_md = cmd.value & 0x7F
            else:
                self._current_base_config.amp_md = cmd.value

        # Control output & Waveform Select
        elif cmd.reg == 0x1B:
            self._current_base_config.waveform = Waveform(cmd.value & 0x3)

        elif cmd.reg & 0xF8 == 0x20:
            self._note_configs[channel].right = (cmd.value & (1 << 7)) > 0
            self._note_configs[channel].left = (cmd.value & (1 << 6)) > 0
            self._channel_configs[channel].fb = (cmd.value >> 3) & 0x07
            self._channel_configs[channel].connection = cmd.value & 0x07

        elif cmd.reg & 0xF8 == 0x28:
            self._note_configs[channel].octave = (cmd.value >> 4) & 0x07
            self._note_configs[channel].note = cmd.value & 0x0F

        elif cmd.reg & 0xF8 == 0x30:
            self._note_configs[channel].key_fraction = (cmd.value >> 2) & 0x3F
        elif cmd.reg & 0xF8 == 0x38:
            self._channel_configs[channel].pms = (cmd.value >> 4) & 0x07
            self._channel_configs[channel].ams = cmd.value & 0x03

        elif cmd.reg & 0xE0 == 0x40:
            self._channel_configs[channel].operators[operator].first_detune = (
                cmd.value >> 4
            ) & 0x07
            self._channel_configs[channel].operators[operator].multiply = (
                cmd.value & 0x0F
            )

        elif cmd.reg & 0xE0 == 0x60:
            self._channel_configs[channel].operators[operator].total_level = (
                cmd.value & 0x7F
            )
        elif cmd.reg & 0xE0 == 0x80:
            self._channel_configs[channel].operators[operator].key_scale = (
                cmd.value >> 6
            ) & 0x3
            self._channel_configs[channel].operators[operator].attack_rate = (
                cmd.value & 0x1F
            )
        elif cmd.reg & 0xE0 == 0xA0:
            self._channel_configs[channel].operators[operator].ase = (
                cmd.value & 0x80
            ) > 0
            self._channel_configs[channel].operators[operator].first_decay_rate = (
                cmd.value & 0x1F
            )
        elif cmd.reg & 0xE0 == 0xC0:
            self._channel_configs[channel].operators[operator].second_detune = (
                cmd.value >> 6
            ) & 0x03
            self._channel_configs[channel].operators[operator].second_decay_rate = (
                cmd.value & 0x0F
            )
        elif cmd.reg & 0xE0 == 0xE0:
            self._channel_configs[channel].operators[operator].first_decay_level = (
                cmd.value >> 4
            ) & 0x0F
            self._channel_configs[channel].operators[operator].release_rate = (
                cmd.value & 0x0F
            )

    def key_presses(self, ch: int) -> typing.List[Note]:
        return self._channel_key_presses[ch]

    def channel_config(self, ch: int):
        return self._channel_configs[ch]

    def beat(self, samples):
        self._samples += samples
