import copy
import typing
from enum import Enum
from typing import Union, List, Any, Dict

from vgm.command import VgmCommandType, VgmCommand


class YM2151Command(VgmCommand):
    command_type = VgmCommandType.YM2151

    def __init__(self, cmd_id, reg: int, value: int) -> None:
        super().__init__(cmd_id)
        self.reg = reg
        self.value = value


def create(reg: int, value: int) -> YM2151Command:
    return YM2151Command(0x54, reg, value)


class Note:
    def __init__(self, config_id: int) -> None:
        self.config_id = config_id


class Waveform(Enum):
    SAW = 0
    SQUARE = 1
    TRIANGLE = 2
    NOISE = 3


class BaseConfig:
    def __init__(self, other=None) -> None:
        self.noise: bool = False if not other else other.noise
        self.noise_freq: int = 0 if not other else other.noise_freq
        self.lfo: int = 0 if not other else other.lfo
        self.phs_md: int = 0 if not other else other.phs_md
        self.amp_md: int = 0 if not other else other.amp_md
        self.ct1: bool = False if not other else other.ct1
        self.ct2: bool = False if not other else other.ct2
        self.waveform: Waveform = Waveform.SAW if not other else other.waveform

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, BaseConfig):
            return (
                self.noise == other.noise
                and self.noise_freq == other.noise_freq
                and self.lfo == other.lfo
                and self.phs_md == other.phs_md
                and self.amp_md == other.amp_md
                and self.ct1 == other.ct1
                and self.ct2 == other.ct2
                and self.waveform == other.waveform
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return BaseConfig(self)


class OperatorConfig:
    def __init__(self, other=None) -> None:
        self.first_detune: int = 0 if not other else other.first_detune
        self.second_detune: int = 0 if not other else other.second_detune
        self.multiply: int = 0 if not other else other.multiply
        self.total_level: int = 0 if not other else other.total_level
        self.key_scale: int = 0 if not other else other.key_scale
        self.attack_rate: int = 0 if not other else other.attack_rate
        self.ase: bool = False if not other else other.ase
        self.first_decay_rate: int = 0 if not other else other.first_decay_rate
        self.second_decay_rate: int = 0 if not other else other.second_decay_rate
        self.first_decay_level: int = 0 if not other else other.first_decay_level
        self.release_rate: int = 0 if not other else other.release_rate

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, OperatorConfig):
            return (
                self.first_detune == other.first_detune
                and self.second_detune == other.second_detune
                and self.multiply == other.multiply
                and self.total_level == other.total_level
                and self.key_scale == other.key_scale
                and self.attack_rate == other.attack_rate
                and self.ase == other.ase
                and self.first_decay_rate == other.first_decay_rate
                and self.second_decay_rate == other.second_decay_rate
                and self.first_decay_level == other.first_decay_level
                and self.release_rate == other.release_rate
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return OperatorConfig(self)


class ChannelConfig:
    def __init__(self, other=None) -> None:
        self.right: bool = False if not other else other.right
        self.left: bool = False if not other else other.left
        self.fb: int = 0 if not other else other.fb
        self.connection: int = 0 if not other else other.connection
        self.octave: int = 0 if not other else other.octave
        self.note: int = 0 if not other else other.note
        self.key_fraction: int = 0 if not other else other.key_fraction
        self.ams: int = 0 if not other else other.ams
        self.pms: int = 0 if not other else other.pms
        self.operators: List[OperatorConfig] = [] if not other else other.operators
        if not other:
            for dev in range(4):
                self.operators.append(OperatorConfig())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ChannelConfig):
            return (
                self.right == other.right
                and self.left == other.left
                and self.fb == other.fb
                and self.connection == other.connection
                and self.octave == other.octave
                and self.note == other.note
                and self.key_fraction == other.key_fraction
                and self.ams == other.ams
                and self.pms == other.pms
                and self.operators == other.operators
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return ChannelConfig(self)


class State:
    def __init__(self) -> None:
        self._channel_key_presses: List[List[Note]] = []
        self._channel_configs: List[ChannelConfig] = []
        self._current_base_config = BaseConfig()
        self.configs: List[BaseConfig] = []

        for i in range(8):
            self._channel_key_presses.append([])
            self._channel_configs.append(ChannelConfig())

    def __getattr__(self, item: str) -> Union[int, bool, Waveform]:
        return getattr(self._current_base_config, item)

    def apply(self, cmd: YM2151Command) -> None:
        channel = cmd.reg & 0x07
        operator = (cmd.reg >> 3) & 0x03

        # Key On/Off
        if cmd.reg == 0x08:
            config_id: int = next(
                (
                    i
                    for (i, c) in enumerate(self.configs)
                    if c == self._current_base_config
                ),
                len(self.configs),
            )

            if len(self.configs) == config_id:
                self.configs.append(self._current_base_config)
                self._current_base_config = copy.deepcopy(self._current_base_config)

            note = Note(config_id)
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
            self._current_base_config.ct1 = (cmd.value & (1 << 6)) > 0
            self._current_base_config.ct2 = (cmd.value & (1 << 7)) > 0

            self._current_base_config.waveform = Waveform(cmd.value & 0x3)

        elif cmd.reg & 0xF8 == 0x20:
            self._channel_configs[channel].right = (cmd.value & (1 << 7)) > 0
            self._channel_configs[channel].left = (cmd.value & (1 << 6)) > 0
            self._channel_configs[channel].fb = (cmd.value >> 3) & 0x07
            self._channel_configs[channel].connection = cmd.value & 0x07

        elif cmd.reg & 0xF8 == 0x28:
            self._channel_configs[channel].octave = (cmd.value >> 4) & 0x07
            self._channel_configs[channel].note = cmd.value & 0x0F

        elif cmd.reg & 0xF8 == 0x30:
            self._channel_configs[channel].key_fraction = (cmd.value >> 2) & 0x3F
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
