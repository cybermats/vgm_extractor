from typing import List, Optional


class SequencerTrack:
    def __init__(self, name: Optional[str] = None):
        self.name: Optional[str] = name
        self.state = "Active"
        self.soloed = False


class SequencerMasterTrack(SequencerTrack):
    pass


class SequencerSendTrack(SequencerTrack):
    pass


class Tracks:
    def __init__(self, tracks: int):
        self.tracks: List[SequencerTrack] = [
            SequencerTrack(f"Track {i}") for i in range(tracks)
        ]
        self.master_tracks: List[SequencerMasterTrack] = [SequencerMasterTrack("Mst")]
        self.send_tracks: List[SequencerSendTrack] = [SequencerSendTrack("S01")]
