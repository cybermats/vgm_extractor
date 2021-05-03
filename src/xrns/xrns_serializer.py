from typing import List, Optional, Iterable, Any

from xrns.parts.song import Song
from xrns.parts.globals import Globals
from xrns.parts.instrument import Instrument
from xrns.parts.track import (
    SequencerTrack,
    SequencerMasterTrack,
    SequencerSendTrack,
    Tracks,
)
from xrns.parts.pattern import PatternPool, Pattern
from xrns.parts.pattern_sequence import PatternSequence
import xrns.xml.song.renoise_song65 as dao


class SerializerConfig:
    def __init__(self):
        self.defaults = True
        self.track_colors = [
            "166,41,41",
            "166,80,41",
            "166,118,41",
            "166,144,41",
            "161,166,41",
            "118,166,47",
            "71,166,47",
            "63,166,106",
        ]
        self.master_track_color = "220,220,220"
        self.send_track_color = "41,166,153"


class XrnsSerializer:
    def __init__(self, config=SerializerConfig()):
        self.config = config

    def render(self, song: Song) -> dao.RenoiseSong:

        global_song_data = self._render_global_song_data(song.globals)

        instruments: dao.RenoiseSong.Instruments = self._render_instruments(
            song.instruments
        )

        tracks: dao.RenoiseSong.Tracks = self._render_tracks(song.tracks)

        pattern_pool: dao.PatternPool = self._render_pattern_pool(song.pattern_pool)

        pattern_sequence: dao.PatternSequence = self._render_pattern_sequence(
            song.pattern_sequence
        )

        return dao.RenoiseSong(
            global_song_data=global_song_data,
            instruments=instruments,
            tracks=tracks,
            pattern_pool=pattern_pool,
            pattern_sequence=pattern_sequence,
        )

    def _render_global_song_data(self, global_song_data: Globals) -> dao.GlobalSongData:
        return dao.GlobalSongData(
            beats_per_min=global_song_data.beats_per_min,
            lines_per_beat=global_song_data.lines_per_beat,
            ticks_per_line=global_song_data.ticks_per_line,
            signature_numerator=global_song_data.signature_numerator,
            signature_denominator=global_song_data.signature_denominator,
            metronome_beats_per_bar=global_song_data.metronome_beats_per_bar,
            metronome_lines_per_beat=global_song_data.metronome_lines_per_beat,
            shuffle_is_active=global_song_data.shuffle_is_active,
            shuffle_amounts=dao.GlobalSongData.ShuffleAmounts(
                shuffle_amount=global_song_data.shuffle_amounts
            ),
            octave=global_song_data.octave,
            loop_coeff=global_song_data.loop_coeff,
            song_name=global_song_data.song_name,
            artist=global_song_data.artist,
        )

    def _render_instruments(
        self, instruments: List[Instrument]
    ) -> dao.RenoiseSong.Instruments:
        return dao.RenoiseSong.Instruments(
            [self._render_instrument(instrument) for instrument in instruments]
        )

    def _render_instrument(self, instrument: Instrument) -> dao.RenoiseInstrument:
        return dao.RenoiseInstrument()

    def _render_tracks(self, tracks: Tracks) -> dao.RenoiseSong.Tracks:
        color_iter = iter(self.config.track_colors)
        seq_track = [self._render_track(track, color_iter) for track in tracks.tracks]
        master_track = [
            self._render_master_track(track) for track in tracks.master_tracks
        ]
        send_track = [self._render_send_track(track) for track in tracks.send_tracks]
        output = dao.RenoiseSong.Tracks(
            sequencer_track=seq_track,
            sequencer_master_track=master_track,
            sequencer_send_track=send_track,
        )
        output.sequencer_master_track = master_track
        return output

    def _render_track(
        self, track: SequencerTrack, color_iter: Iterable[str]
    ) -> dao.SequencerTrack:

        track = dao.SequencerTrack(
            name=track.name,
            color_blend=0,
            state=track.state,
            soloed=track.soloed,
            panning_column_is_visible=True,
            filter_devices=dao.TrackFilterDeviceChain(
                devices=dao.TrackFilterDeviceChain.Devices(
                    track_mixer_device=[dao.TrackMixerDevice()]
                )
            ),
        )

        try:
            track.color = next(color_iter)
        except StopIteration:
            pass

        return track

    def _render_master_track(
        self, track: SequencerMasterTrack
    ) -> dao.SequencerMasterTrack:
        return dao.SequencerMasterTrack(
            name=track.name,
            color=self.config.master_track_color,
            color_blend=0,
            state=track.state,
            soloed=track.soloed,
            filter_devices=dao.TrackFilterDeviceChain(
                devices=dao.TrackFilterDeviceChain.Devices(
                    master_track_mixer_device=[dao.MasterTrackMixerDevice()]
                )
            ),
        )

    def _render_send_track(self, track: SequencerSendTrack) -> dao.SequencerSendTrack:
        return dao.SequencerSendTrack(
            name=track.name,
            color=self.config.send_track_color,
            color_blend=0,
            state=track.state,
            soloed=track.soloed,
            filter_devices=dao.TrackFilterDeviceChain(
                devices=dao.TrackFilterDeviceChain.Devices(
                    send_track_mixer_device=[dao.SendTrackMixerDevice()]
                )
            ),
        )

    def _render_pattern_pool(self, pattern_pool: PatternPool) -> dao.PatternPool:
        return dao.PatternPool(
            patterns=dao.PatternPool.Patterns(
                [self._render_pattern(pattern) for pattern in pattern_pool.patterns]
            )
        )

    def _render_pattern(self, pattern: Pattern) -> dao.Pattern:
        return dao.Pattern(
            tracks=dao.Pattern.Tracks(
                pattern_track=[
                    self._render_pattern_track(track) for track in pattern.tracks
                ],
                pattern_master_track=[
                    self._render_pattern_master_track(track)
                    for track in pattern.master_tracks
                ],
                pattern_send_track=[
                    self._render_pattern_send_track(track)
                    for track in pattern.send_tracks
                ],
            )
        )

    def _render_pattern_track(self, track: Pattern.PatternTrack) -> dao.PatternTrack:
        return dao.PatternTrack(
            lines=dao.PatternTrack.Lines(
                line=[
                    dao.PatternLineNode(
                        index=idx,
                        note_columns=dao.PatternLineNode.NoteColumns(
                            note_column=[
                                dao.PatternLineNoteColumnNode(
                                    note=line.note,
                                    instrument=line.instrument,
                                    panning=line.pan,
                                )
                            ]
                        ),
                    )
                    for idx, line in track.lines.items()
                ]
            )
        )

    def _render_pattern_master_track(
        self, track: Pattern.PatternMasterTrack
    ) -> dao.PatternMasterTrack:
        return dao.PatternMasterTrack()

    def _render_pattern_send_track(
        self, track: Pattern.PatternSendTack
    ) -> dao.PatternSendTrack:
        return dao.PatternSendTrack()

    def _render_pattern_sequence(
        self, pattern_sequence: PatternSequence
    ) -> dao.PatternSequence:
        return dao.PatternSequence(
            sequence_entries=dao.PatternSequence.SequenceEntries(
                [
                    self._render_sequence_entry(entry)
                    for entry in pattern_sequence.sequence_entries
                ]
            )
        )

    def _render_sequence_entry(
        self, entry: PatternSequence.SequenceEntry
    ) -> dao.PatternSequenceEntry:
        return dao.PatternSequenceEntry(pattern=entry.pattern)
