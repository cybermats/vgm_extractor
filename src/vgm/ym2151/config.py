import copy
import json
from enum import Enum, IntFlag, Flag
from json import JSONEncoder
from typing import Any, List, Dict

from vgm.command import VgmCommand, VgmCommandType


class Waveform(Enum):
    SAW = 0
    SQUARE = 1
    TRIANGLE = 2
    NOISE = 3

    def repr_json(self):
        return self.name


class Operators(Flag):
    MOD1 = 1
    CAR1 = 2
    MOD2 = 4
    CAR2 = 8

    def repr_json(self):
        o = []
        if self & Operators.MOD1:
            o.append(Operators.MOD1.name)
        if self & Operators.CAR1:
            o.append(Operators.CAR1.name)
        if self & Operators.MOD2:
            o.append(Operators.MOD2.name)
        if self & Operators.CAR2:
            o.append(Operators.CAR2.name)
        return "|".join(o)


class BaseConfig:
    def __init__(self, other=None) -> None:
        self.waveform: Waveform = Waveform.SAW if not other else other.waveform
        self.lfo: int = 0 if not other else other.lfo
        self.amp_md: int = 0 if not other else other.amp_md
        self.phs_md: int = 0 if not other else other.phs_md

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, BaseConfig):
            return (
                self.lfo == other.lfo
                and self.phs_md == other.phs_md
                and self.amp_md == other.amp_md
                and self.waveform == other.waveform
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return BaseConfig(self)

    def repr_json(self):
        return self.__dict__


class OperatorConfig:
    def __init__(self, other=None) -> None:
        self.total_level: int = 0 if not other else other.total_level
        self.attack_rate: int = 0 if not other else other.attack_rate
        self.first_decay_rate: int = 0 if not other else other.first_decay_rate
        self.first_decay_level: int = 0 if not other else other.first_decay_level
        self.second_decay_rate: int = 0 if not other else other.second_decay_rate
        self.release_rate: int = 0 if not other else other.release_rate
        self.key_scale: int = 0 if not other else other.key_scale
        self.multiply: int = 0 if not other else other.multiply
        self.first_detune: int = 0 if not other else other.first_detune
        self.second_detune: int = 0 if not other else other.second_detune
        self.ase: bool = False if not other else other.ase

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

    def repr_json(self):
        return {
            "tl": self.total_level,
            "ar": self.attack_rate,
            "d1r": self.first_decay_rate,
            "d1l": self.first_decay_level,
            "d2r": self.second_decay_rate,
            "rr": self.release_rate,
            "ks": self.key_scale,
            "mul": self.multiply,
            "dt1": self.first_detune,
            "dt2": self.second_detune,
            "ase": self.ase,
        }


class NoteConfig:
    def __init__(self, other=None) -> None:
        self.right: bool = False if not other else other.right
        self.left: bool = False if not other else other.left
        self.octave: int = 0 if not other else other.octave
        self.note: int = 0 if not other else other.note
        self.key_fraction: int = 0 if not other else other.key_fraction

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, NoteConfig):
            return (
                self.right == other.right
                and self.left == other.left
                and self.octave == other.octave
                and self.note == other.note
                and self.key_fraction == other.key_fraction
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return NoteConfig(self)

    def repr_json(self):
        return {
            "right": self.right,
            "left": self.left,
            "octave": self.octave,
            "note": self.note,
            "key_fraction": self.key_fraction,
        }


class ChannelConfig:
    def __init__(self, other=None) -> None:
        self.operators: List[OperatorConfig] = (
            [] if not other else copy.deepcopy(other.operators)
        )

        self.fb: int = 0 if not other else other.fb
        self.ams: int = 0 if not other else other.ams
        self.pms: int = 0 if not other else other.pms
        self.connection: int = 0 if not other else other.connection
        self.noise: bool = False if not other else other.noise
        self.noise_freq: int = 0 if not other else other.noise_freq

        if not other:
            for dev in range(4):
                self.operators.append(OperatorConfig())

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ChannelConfig):
            return (
                self.fb == other.fb
                and self.connection == other.connection
                and self.ams == other.ams
                and self.pms == other.pms
                and self.operators == other.operators
                and self.noise == other.noise
                and self.noise_freq == other.noise_freq
            )
        return NotImplemented

    # noinspection PyArgumentList
    def __deepcopy__(self, _) -> object:
        return ChannelConfig(self)

    def repr_json(self):
        return {
            "feedback": self.fb,
            "connection": self.connection,
            "ams": self.ams,
            "pms": self.pms,
            "noise": self.noise,
            "noise_freq": self.noise_freq,
            "m1": self.operators[0],
            "c1": self.operators[2],
            "m2": self.operators[1],
            "c2": self.operators[3],
        }


class Config:
    def __init__(
        self,
        id: int,
        base: BaseConfig = BaseConfig(),
        channel: ChannelConfig = ChannelConfig(),
        operators: Operators = 0,
    ):
        self._id = id
        self._base = base
        self._operators: Operators = operators
        self._channel = channel

    def __getattr__(self, item):
        if item == "lfo":
            return self._base.lfo
        if item == "phs_md":
            return self._base.phs_md
        if item == "amp_md":
            return self._base.amp_md
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

    def repr_json(self) -> Dict:
        return {
            "id": self._id,
            "base": self._base,
            "operators": self._operators,
            "channel": self._channel,
        }


class ConfigEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if hasattr(o, "repr_json"):
            return o.repr_json()
        else:
            return json.JSONEncoder.default(self, o)


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
