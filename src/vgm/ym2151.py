from enum import Enum, auto

from vgm.command import VgmCommandType, VgmCommand


class YM2151Command(VgmCommand):
    command_type = VgmCommandType.YM2151

    def __init__(self, cmd_id, reg, value):
        super().__init__(cmd_id)
        self.reg = reg
        self.value = value


def create(reg: int, value: int) -> YM2151Command:
    return YM2151Command(0x54, reg, value)


class YM2151State:
    class Waveform(Enum):
        SAW = 0
        SQUARE = 1
        TRIANGLE = 2
        NOISE = 3

    noise = None
    noise_freq = 0
    lfo = 0
    phs_md = 0
    amp_md = 0
    ct1 = None
    ct2 = None
    waveform = Waveform.SAW

    def apply(self, cmd: YM2151Command):
        if cmd.reg == 0x0F:
            if cmd.value > 0x20:
                self.noise = True
            self.noise_freq = cmd.value & 0x1F

        elif cmd.reg == 0x18:
            self.lfo = cmd.value

        elif cmd.reg == 0x19:
            if cmd.value & (1 << 7) > 0:
                self.phs_md = cmd.value & 0x7F
            else:
                self.amp_md = cmd.value
        elif cmd.reg == 0x1B:
            self.ct1 = (cmd.value & (1 << 6)) > 0
            self.ct2 = (cmd.value & (1 << 7)) > 0

            self.waveform = YM2151State.Waveform(cmd.value & 0x3)
