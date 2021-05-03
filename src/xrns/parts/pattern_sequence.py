from typing import List


class PatternSequence:
    class SequenceEntry:
        def __init__(self, pattern: int = None):
            self.pattern = pattern

    def __init__(self):
        self.sequence_entries: List[PatternSequence.SequenceEntry] = []

    def add_pattern(self, pattern: int):
        self.sequence_entries.append(PatternSequence.SequenceEntry(pattern))
