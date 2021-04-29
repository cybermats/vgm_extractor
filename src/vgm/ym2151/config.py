import copy
from enum import Enum, IntFlag
from typing import Any, List

from vgm.command import VgmCommand, VgmCommandType


class Waveform(Enum):
    SAW = 0
    SQUARE = 1
    TRIANGLE = 2
    NOISE = 3


class Operators(IntFlag):
    CAR2 = 1
    MOD2 = 2
    CAR1 = 4
    MOD1 = 8


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
        self.operators: List[OperatorConfig] = (
            [] if not other else copy.deepcopy(other.operators)
        )
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
                #                and self.octave == other.octave
                #                and self.note == other.note
                #                and self.key_fraction == other.key_fraction
                and self.ams == other.ams
                and self.pms == other.pms
                and self.operators == other.operators
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return ChannelConfig(self)


class Config:
    def __init__(
        self,
        base: BaseConfig = BaseConfig(),
        channel: ChannelConfig = ChannelConfig(),
        operators: Operators = 0,
    ):
        self._base = base
        self._operators: Operators = operators
        self._channel = channel

    def __getattr__(self, item):
        if item == "noise":
            return self._base.noise
        if item == "noise_freq":
            return self._base.noise_freq
        if item == "lfo":
            return self._base.lfo
        if item == "phs_md":
            return self._base.phs_md
        if item == "amp_md":
            return self._base.amp_md
        if item == "ct1":
            return self._base.ct1
        if item == "ct2":
            return self._base.ct2
        if item == "waveform":
            return self._base.waveform
        if item == "enabled_operators":
            return self._operators

        return getattr(self._channel, item)

    def compare(self, base: BaseConfig, channel: ChannelConfig, operators: Operators):
        return (
            self._base == base
            and self._channel == channel
            and self._operators == operators
        )


class YM2151Command(VgmCommand):
    command_type = VgmCommandType.YM2151

    def __init__(self, cmd_id, reg: int, value: int) -> None:
        super().__init__(cmd_id)
        self.reg = reg
        self.value = value

    def __str__(self) -> str:
        return f"YM2151Command(Reg: {hex(self.reg)}, Data: {hex(self.value)})"


def create(reg: int, value: int) -> YM2151Command:
    return YM2151Command(0x54, reg, value)
