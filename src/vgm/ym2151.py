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


_CONFIG_ATTRIBUTE_NAMES: dict[str, Union[int, bool, Waveform]] = {
    "noise": False,
    "noise_freq": 0,
    "lfo": 0,
    "phs_md": 0,
    "amp_md": 0,
    "ct1": False,
    "ct2": False,
    "waveform": Waveform.SAW,
}


class Config:
    def __init__(self) -> None:
        self._attributes = copy.deepcopy(_CONFIG_ATTRIBUTE_NAMES)

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Config):
            return self._attributes == other._attributes
        return NotImplemented

    def __getattr__(self, item: str) -> Union[int, bool, Waveform]:
        if item in _CONFIG_ATTRIBUTE_NAMES:
            return self._attributes[item]
        raise AttributeError(item)

    def __setattr__(self, key: str, value: Any) -> None:
        if key in _CONFIG_ATTRIBUTE_NAMES:
            self._attributes[key] = value
        else:
            object.__setattr__(self, key, value)

    # noinspection PyArgumentList
    def __deepcopy__(self, memo: Dict = None) -> object:
        if memo is None:
            memo = {}
        attr = copy.deepcopy(self._attributes, memo)
        cp = Config()
        cp._attributes = attr
        return cp


class State:
    def __init__(self) -> None:
        self.channels: List[List[Note]] = []
        for i in range(8):
            self.channels.append([])
        self.configs: List[Config] = []

        self.current_config = Config()

    def __getattr__(self, item: str) -> Union[int, bool, Waveform]:
        return getattr(self.current_config, item)

    def apply(self, cmd: YM2151Command) -> None:
        if cmd.reg == 0x0F:
            if cmd.value > 0x20:
                self.current_config.noise = True
            self.current_config.noise_freq = cmd.value & 0x1F

        elif cmd.reg == 0x18:
            self.current_config.lfo = cmd.value

        elif cmd.reg == 0x19:
            if cmd.value & (1 << 7) > 0:
                self.current_config.phs_md = cmd.value & 0x7F
            else:
                self.current_config.amp_md = cmd.value
        elif cmd.reg == 0x1B:
            self.current_config.ct1 = (cmd.value & (1 << 6)) > 0
            self.current_config.ct2 = (cmd.value & (1 << 7)) > 0

            self.current_config.waveform = Waveform(cmd.value & 0x3)

        elif cmd.reg == 0x08:
            config_id: int = next(
                (i for (i, c) in enumerate(self.configs) if c == self.current_config),
                len(self.configs),
            )

            if len(self.configs) == config_id:
                self.configs.append(self.current_config)
                self.current_config = copy.deepcopy(self.current_config)

            note = Note(config_id)
            self.channels[cmd.value & 0x7].append(note)

    def channel(self, ch: int) -> typing.List[Note]:
        return self.channels[ch]
