from enum import Enum, auto


class VgmCommandType(Enum):
    WAIT = auto()
    EOS = auto()
    YM2151 = auto()


class VgmCommand:
    command_type = None
    command_id = 0

    def __init__(self, cmd_id: int, payload: bytes = None):
        self.command_id = cmd_id
        self.payload = payload


class EOSCommand(VgmCommand):
    command_type = VgmCommandType.EOS


class WaitCommand(VgmCommand):
    command_type = VgmCommandType.WAIT

    def __init__(self, cmd_id, samples=None):
        super().__init__(cmd_id)
        self.samples = samples
        if cmd_id // 16 == 7:
            self.samples = cmd_id % 16 + 1
