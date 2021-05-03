from typing import List


class PatternSequence:
    class SequenceEntry:
        pass

    def __init__(self):
        self.sequence_entries: List[PatternSequence.SequenceEntry] = [
            PatternSequence.SequenceEntry()
        ]
