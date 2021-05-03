from typing import List, Dict


class Pattern:
    class Line:
        def __init__(self, note: str, instrument: str, pan: str):
            self.note: str = note
            self.instrument: str = instrument
            self.pan: str = pan

        def __str__(self):
            return f"{self.note} {self.instrument} {self.pan}"

    class PatternTrack:
        def __init__(self):
            self.lines: Dict[int, Pattern.Line] = {}

    class PatternMasterTrack(PatternTrack):
        pass

    class PatternSendTack(PatternTrack):
        pass

    def __init__(self, tracks: int, lines_per_track: int):
        self.lines_per_track = lines_per_track

        self.tracks: List[Pattern.PatternTrack] = [
            Pattern.PatternTrack() for _ in range(tracks)
        ]
        self.master_tracks: List[Pattern.PatternMasterTrack] = [
            Pattern.PatternMasterTrack()
        ]
        self.send_tracks: List[Pattern.PatternSendTack] = [Pattern.PatternSendTack()]


class PatternPool:
    def __init__(self, tracks: int, lines_per_track: int):
        self.patterns: List[Pattern] = []
        self.tracks = tracks
        self.lines_per_track = lines_per_track

    def add_note(
        self,
        pattern: int,
        channel: int,
        line: int,
        note: str,
        instrument: str,
        pan: str,
    ):
        while pattern >= len(self.patterns):
            self.patterns.append(Pattern(self.tracks, self.lines_per_track))
        self.patterns[pattern].tracks[channel].lines[line] = Pattern.Line(
            note, instrument, pan
        )
