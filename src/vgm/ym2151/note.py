import typing

from vgm.ym2151.config import NoteConfig


_NOTE_LOOKUP: typing.Dict = {
    0: "C#",
    1: "D ",
    2: "D#",
    3: "D?",
    4: "E ",
    5: "F ",
    6: "F#",
    7: "F?",
    8: "G",
    9: "G#",
    10: "A ",
    11: "A?",
    12: "A#",
    13: "B ",
    14: "C ",
    15: "C?",
}


class Note:
    def __init__(self, config_id: int, note_config: NoteConfig, sample: int) -> None:
        self.config_id: int = config_id
        self.right: bool = note_config.right
        self.left: bool = note_config.left
        self.octave: int = note_config.octave
        self.note: int = note_config.note
        self.key_fraction: int = note_config.key_fraction
        self.sample: int = sample

    def __str__(self):
        if self.config_id < 0:
            return "Key Off"
        note = _NOTE_LOOKUP[self.note]
        kf = ""
        if self.key_fraction > 1:
            kf = "-{:02.0f}".format(self.key_fraction * 1.6)
        pan = ""
        if not self.right or not self.left:
            pan = "Pan {}".format("R" if self.right else "L")
        return f"{note}-{self.octave}{kf} [{self.config_id}] {pan}"
