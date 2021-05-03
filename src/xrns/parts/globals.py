from typing import List


class Globals:
    def __init__(self):
        self.beats_per_min: int = 120
        self.lines_per_beat: int = 4
        self.ticks_per_line: int = 12
        self.signature_numerator: int = 4
        self.signature_denominator: int = 4
        self.metronome_beats_per_bar: int = 4
        self.metronome_lines_per_beat: int = 0
        self.shuffle_is_active: bool = False
        self.shuffle_amounts: List[int] = [0, 0, 0, 0]
        self.octave: int = 3
        self.loop_coeff: int = 4
        self.song_name: str = "Untitled"
        self.artist: str = "FooBar"
