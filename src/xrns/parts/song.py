from typing import List, Optional

from xrns.parts.globals import Globals
from xrns.parts.instrument import Instrument
from xrns.parts.pattern import PatternPool
from xrns.parts.pattern_sequence import PatternSequence
from xrns.parts.track import Tracks


class Song:
    def __init__(
        self, *, tracks: int = 8, instruments: int = 1, lines_per_track: int = 64
    ):
        self.globals: Globals = Globals()
        self.instruments: List[Instrument] = [Instrument()] * instruments
        self.tracks: Tracks = Tracks(tracks)
        self.pattern_pool: PatternPool = PatternPool(tracks, lines_per_track)
        self.pattern_sequence: PatternSequence = PatternSequence()
