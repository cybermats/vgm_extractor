from typing import List


class Pattern:
    class PatternTrack:
        pass

    class PatternMasterTrack(PatternTrack):
        pass

    class PatternSendTack(PatternTrack):
        pass

    def __init__(self):
        self.tracks: List[Pattern.PatternTrack] = [Pattern.PatternTrack()]
        self.master_tracks: List[Pattern.PatternMasterTrack] = [
            Pattern.PatternMasterTrack()
        ]
        self.send_tracks: List[Pattern.PatternSendTack] = [Pattern.PatternSendTack()]


class PatternPool:
    def __init__(self):
        self.patterns: List[Pattern] = [Pattern()]
