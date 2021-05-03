from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate, XmlTime


@dataclass
class AnalogFilterDevicePreset:
    device_slot: Optional["AnalogFilterDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class AnalogFilterDeviceModel(Enum):
    VALUE_2_P_K35 = "2P K35"
    VALUE_2_P_MOOG = "2P Moog"
    VALUE_4_P_MOOG = "4P Moog"
    VALUE_4_P_DIODE = "4P Diode"


class AnalogFilterDeviceOversamplingFactor(Enum):
    VALUE_1X = "1x"
    VALUE_2X = "2x"
    VALUE_4X = "4x"
    VALUE_8X = "8x"


class AudioPluginDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class AudioPluginDevicePreset:
    device_slot: Optional["AudioPluginDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class AudioPluginDeviceParameterChunkType(Enum):
    CHUNK = "Chunk"
    PARAMETER_BAG = "ParameterBag"


class AudioPluginDevicePluginType(Enum):
    AU = "AU"
    VST = "VST"
    VST3 = "VST3"
    LADSPA = "LADSPA"
    DSSI = "DSSI"


@dataclass
class BusCompressorDevicePreset:
    device_slot: Optional["BusCompressorDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CabinetSimulatorDevicePreset:
    device_slot: Optional["CabinetSimulatorDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Chorus2DevicePreset:
    device_slot: Optional["Chorus2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ChorusDevicePreset:
    device_slot: Optional["ChorusDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Comb2DevicePreset:
    device_slot: Optional["Comb2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class Comb2NoteFilterDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class CombDevicePreset:
    device_slot: Optional["CombDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompressorDevicePreset:
    device_slot: Optional["CompressorDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConvolverDevicePreset:
    device_slot: Optional["ConvolverDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CrossoverDevicePreset:
    device_slot: Optional["CrossoverDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class CrossoverDeviceCrossoverType(Enum):
    LR2 = "LR2"
    LR4 = "LR4"
    LR8 = "LR8"
    FAST_FIR = "Fast FIR"
    STEEP_FIR = "Steep FIR"


@dataclass
class DcOffsetDevicePreset:
    device_slot: Optional["DcOffsetDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DelayDevicePreset:
    device_slot: Optional["DelayDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DigitalFilterDevicePreset:
    device_slot: Optional["DigitalFilterDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class DigitalFilterDeviceModel(Enum):
    BIQUAD = "Biquad"
    BUTTERWORTH_4N = "Butterworth 4n"
    BUTTERWORTH_8N = "Butterworth 8n"
    CHEBYSHEV_4N = "Chebyshev 4n"
    CHEBYSHEV_8N = "Chebyshev 8n"


class DigitalFilterDeviceOversamplingFactor(Enum):
    VALUE_1X = "1x"
    VALUE_2X = "2x"
    VALUE_4X = "4x"
    VALUE_8X = "8x"


@dataclass
class Distortion2DevicePreset:
    device_slot: Optional["Distortion2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DistortionDevicePreset:
    device_slot: Optional["DistortionDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DooferDevicePreset:
    device_slot: Optional["DooferDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class DooferMacroParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


class DooferParameterMappingScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class EnvelopePlayMode(Enum):
    POINTS = "Points"
    LINES = "Lines"
    CURVES = "Curves"


class EnvelopePolarity(Enum):
    UNIPOLAR = "Unipolar"
    BIPOLAR = "Bipolar"


@dataclass
class Eq10DevicePreset:
    device_slot: Optional["Eq10Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class Eq10DeviceInputMode(Enum):
    L = "L"
    R = "R"
    L_R = "L-R"
    L_R_1 = "L+R"


class Eq10DeviceVisualizationMode(Enum):
    GRAPH_ONLY = "Graph Only"
    SLIDERS_ONLY = "Sliders Only"
    FULL_DISPLAY = "Full Display"


@dataclass
class Eq5DevicePreset:
    device_slot: Optional["Eq5Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class Eq5DeviceInputMode(Enum):
    L = "L"
    R = "R"
    L_R = "L-R"
    L_R_1 = "L+R"


class Eq5DeviceVisualizationMode(Enum):
    GRAPH_ONLY = "Graph Only"
    SLIDERS_ONLY = "Sliders Only"
    FULL_DISPLAY = "Full Display"


@dataclass
class ExciterDevicePreset:
    device_slot: Optional["ExciterDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class ExciterDeviceVisibleBand(Enum):
    LOW = "Low"
    MID = "Mid"
    HIGH = "High"


@dataclass
class Filter1DevicePreset:
    device_slot: Optional["Filter1Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Filter2DevicePreset:
    device_slot: Optional["Filter2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Filter3DevicePreset:
    device_slot: Optional["Filter3Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class Filter3DeviceModel(Enum):
    VALUE_24D_B_4_POLE = "24dB 4Pole"
    VALUE_24D_B_MOOG = "24dB Moog"
    BUTTERWORTH_4N = "Butterworth 4n"
    BUTTERWORTH_8N = "Butterworth 8n"


class FilterDeviceIsActiveParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


class FilterDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class FilterDistortionDevicePreset:
    device_slot: Optional["FilterDistortionDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Flanger2DevicePreset:
    device_slot: Optional["Flanger2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FlangerDevicePreset:
    device_slot: Optional["FlangerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FormulaMetaDevicePreset:
    device_slot: Optional["FormulaMetaDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GainerDevicePreset:
    device_slot: Optional["GainerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Gate2DevicePreset:
    device_slot: Optional["Gate2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GateDevicePreset:
    device_slot: Optional["GateDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GlobalSongData:
    beats_per_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "BeatsPerMin",
            "type": "Element",
        },
    )
    lines_per_beat: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinesPerBeat",
            "type": "Element",
        },
    )
    ticks_per_line: Optional[int] = field(
        default=None,
        metadata={
            "name": "TicksPerLine",
            "type": "Element",
        },
    )
    signature_numerator: Optional[int] = field(
        default=None,
        metadata={
            "name": "SignatureNumerator",
            "type": "Element",
        },
    )
    signature_denominator: Optional[int] = field(
        default=None,
        metadata={
            "name": "SignatureDenominator",
            "type": "Element",
        },
    )
    metronome_beats_per_bar: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetronomeBeatsPerBar",
            "type": "Element",
        },
    )
    metronome_lines_per_beat: Optional[int] = field(
        default=None,
        metadata={
            "name": "MetronomeLinesPerBeat",
            "type": "Element",
        },
    )
    shuffle_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShuffleIsActive",
            "type": "Element",
        },
    )
    shuffle_amounts: Optional["GlobalSongData.ShuffleAmounts"] = field(
        default=None,
        metadata={
            "name": "ShuffleAmounts",
            "type": "Element",
        },
    )
    octave: Optional[int] = field(
        default=None,
        metadata={
            "name": "Octave",
            "type": "Element",
        },
    )
    loop_coeff: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopCoeff",
            "type": "Element",
        },
    )
    song_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SongName",
            "type": "Element",
        },
    )
    artist: Optional[str] = field(
        default=None,
        metadata={
            "name": "Artist",
            "type": "Element",
        },
    )
    song_comments: Optional["GlobalSongData.SongComments"] = field(
        default=None,
        metadata={
            "name": "SongComments",
            "type": "Element",
        },
    )
    show_song_comments_after_loading: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowSongCommentsAfterLoading",
            "type": "Element",
        },
    )
    show_used_automations_only: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowUsedAutomationsOnly",
            "type": "Element",
        },
    )
    follow_automations: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FollowAutomations",
            "type": "Element",
        },
    )
    sample_offset_compatibility_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleOffsetCompatibilityMode",
            "type": "Element",
        },
    )
    pitch_effects_compatibility_mode: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PitchEffectsCompatibilityMode",
            "type": "Element",
        },
    )
    global_track_headroom: Optional[float] = field(
        default=None,
        metadata={
            "name": "GlobalTrackHeadroom",
            "type": "Element",
        },
    )
    playback_engine_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "PlaybackEngineVersion",
            "type": "Element",
        },
    )
    render_selection_name_counter: Optional[int] = field(
        default=None,
        metadata={
            "name": "RenderSelectionNameCounter",
            "type": "Element",
        },
    )
    record_sample_name_counter: Optional[int] = field(
        default=None,
        metadata={
            "name": "RecordSampleNameCounter",
            "type": "Element",
        },
    )
    new_sample_name_counter: Optional[int] = field(
        default=None,
        metadata={
            "name": "NewSampleNameCounter",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class ShuffleAmounts:
        shuffle_amount: List[int] = field(
            default_factory=list,
            metadata={
                "name": "ShuffleAmount",
                "type": "Element",
            },
        )

    @dataclass
    class SongComments:
        song_comment: List[str] = field(
            default_factory=list,
            metadata={
                "name": "SongComment",
                "type": "Element",
            },
        )


@dataclass
class GroupTrackMixerDevicePreset:
    device_slot: Optional["GroupTrackMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class HydraDevicePreset:
    device_slot: Optional["HydraDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class HydraDeviceOut1Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut2Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut3Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut4Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut5Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut6Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut7Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut8Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class HydraDeviceOut9Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


@dataclass
class InstrumentAutomationDevicePreset:
    device_slot: Optional["InstrumentAutomationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class InstrumentGlobalPropertiesQuantize(Enum):
    NONE_VALUE = "None"
    LINE = "Line"
    BEAT = "Beat"
    BAR = "Bar"


class InstrumentGlobalPropertiesScale(Enum):
    NONE_VALUE = "None"
    NATURAL_MAJOR = "Natural Major"
    NATURAL_MINOR = "Natural Minor"
    PENTATONIC_MAJOR = "Pentatonic Major"
    PENTATONIC_MINOR = "Pentatonic Minor"
    PENTATONIC_EGYPTIAN = "Pentatonic Egyptian"
    BLUES_MAJOR = "Blues Major"
    BLUES_MINOR = "Blues Minor"
    WHOLE_TONE = "Whole Tone"
    AUGMENTED = "Augmented"
    PROMETHEUS = "Prometheus"
    TRITONE = "Tritone"
    HARMONIC_MAJOR = "Harmonic Major"
    HARMONIC_MINOR = "Harmonic Minor"
    MELODIC_MINOR = "Melodic Minor"
    ALL_MINOR = "All Minor"
    DORIAN = "Dorian"
    PHRYGIAN = "Phrygian"
    PHRYGIAN_DOMINANT = "Phrygian Dominant"
    LYDIAN = "Lydian"
    LYDIAN_AUGMENTED = "Lydian Augmented"
    MIXOLYDIAN = "Mixolydian"
    LOCRIAN = "Locrian"
    LOCRIAN_MAJOR = "Locrian Major"
    SUPER_LOCRIAN = "Super Locrian"
    NEAPOLITAN_MAJOR = "Neapolitan Major"
    NEAPOLITAN_MINOR = "Neapolitan Minor"
    ROMANIAN_MINOR = "Romanian Minor"
    SPANISH_GYPSY = "Spanish Gypsy"
    HUNGARIAN_GYPSY = "Hungarian Gypsy"
    ENIGMATIC = "Enigmatic"
    OVERTONE = "Overtone"
    DIMINISHED_HALF = "Diminished Half"
    DIMINISHED_WHOLE = "Diminished Whole"
    SPANISH_EIGHT_TONE = "Spanish Eight-Tone"
    NINE_TONE_SCALE = "Nine-Tone Scale"


class InstrumentGlobalPropertiesScaleKey(Enum):
    C = "C"
    C_1 = "C#"
    D = "D"
    D_1 = "D#"
    E = "E"
    F = "F"
    F_1 = "F#"
    G = "G"
    G_1 = "G#"
    A = "A"
    A_1 = "A#"
    B = "B"


@dataclass
class InstrumentMacroDevicePreset:
    device_slot: Optional["InstrumentMacroDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class InstrumentMacroParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


class InstrumentMidiGeneratorBankOrder(Enum):
    MSB_LSB = "MSB, LSB"
    LSB_MSB = "LSB, MSB"


class InstrumentMidiGeneratorInstrumentType(Enum):
    EXT_MIDI = "ext. MIDI"
    LINE_IN_RET = "LineIn Ret"
    INT_MIDI = "int. MIDI"


@dataclass
class InstrumentMidiInputProperties:
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceName",
            "type": "Element",
        },
    )
    channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
        },
    )
    note_range_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteRangeStart",
            "type": "Element",
        },
    )
    note_range_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteRangeEnd",
            "type": "Element",
        },
    )
    assigned_track: Optional[int] = field(
        default=None,
        metadata={
            "name": "AssignedTrack",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class InstrumentParameterMappingDestChainType(Enum):
    MODULATION_SET = "ModulationSet"
    SAMPLE_DSP = "SampleDSP"


class InstrumentParameterMappingScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class InstrumentPhraseGeneratorPlaybackMode(Enum):
    OFF = "Off"
    SELECTIVE = "Selective"
    KEYMAP = "Keymap"


class InstrumentPhraseTriggerOptionsKeyTracking(Enum):
    NONE_VALUE = "None"
    TRANSPOSE = "Transpose"
    OFFSET = "Offset"


class InstrumentPluginRoutingMixMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


class InstrumentSampleGeneratorKeyzoneOverlappingMode(Enum):
    PLAY_ALL = "Play All"
    CYCLE = "Cycle"
    RANDOM = "Random"


@dataclass
class KeyTrackingDevicePreset:
    device_slot: Optional["KeyTrackingDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class KeyTrackingDeviceDestScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class KeyTrackingDeviceKeyTrackingMode(Enum):
    CLAMP = "Clamp"
    SOFT = "Soft"
    OCTAVE = "Octave"


@dataclass
class LfoDevicePreset:
    device_slot: Optional["LfoDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LineInDevicePreset:
    device_slot: Optional["LineInDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class LineInDeviceInputChannelMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


class LineInDeviceInputLatencyMode(Enum):
    LIVE_RECORDING_MODE = "Live Recording Mode"
    MIDI_RETURN_MODE = "MIDI Return Mode"


@dataclass
class Lofi2DevicePreset:
    device_slot: Optional["Lofi2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LofiDevicePreset:
    device_slot: Optional["LofiDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MasterTrackMixerDevicePreset:
    device_slot: Optional["MasterTrackMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MaximizerDevicePreset:
    device_slot: Optional["MaximizerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MetaMixerDevicePreset:
    device_slot: Optional["MetaMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class MetaMixerDeviceDestScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


@dataclass
class MidiCcdevicePreset:
    class Meta:
        name = "MidiCCDevicePreset"

    device_slot: Optional["MidiCcdevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class MidiControlDeviceFilterDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class MidiControlDevicePreset:
    device_slot: Optional["MidiControlDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class MidiControlDeviceControllerType0(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType1(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType10(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType11(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType12(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType13(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType14(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType15(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType16(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType17(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType18(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType19(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType2(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType20(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType21(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType22(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType23(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType24(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType25(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType26(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType27(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType28(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType29(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType3(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType30(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType31(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType32(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType33(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType34(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType4(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType5(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType6(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType7(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType8(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


class MidiControlDeviceControllerType9(Enum):
    PB = "PB"
    CP = "CP"
    CC = "CC"
    PRG = "Prg"


@dataclass
class MidiInputRoutingTable:
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MidiMappingControllerMode(Enum):
    ABSOLUTE_7_BIT = "Absolute 7 bit"
    RELATIVE_SIGNED_BIT = "Relative signed bit"
    RELATIVE_SIGNED_BIT_2 = "Relative signed bit 2"
    RELATIVE_BIN_OFFSET = "Relative bin offset"
    RELATIVE_TWO_S_COMP = "Relative two's comp"


class MidiMappingMappingMode(Enum):
    CONTROLLERS = "Controllers"
    NOTES = "Notes"


class MidiMappingNoteMode(Enum):
    TRIGGER = "Trigger"
    GATE = "Gate"
    VALUE = "Value"


@dataclass
class MixerEqDevicePreset:
    device_slot: Optional["MixerEqDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class MixerEqDeviceInputMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


@dataclass
class MultitapDevicePreset:
    device_slot: Optional["MultitapDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class NoteColumnStatesNoteColumnState1(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class NoteColumnStatesNoteColumnState2(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class NoteColumnStatesNoteColumnState3(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class NoteColumnStatesNoteColumnState4(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class NoteColumnStatesNoteColumnState5(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


@dataclass
class OscMapper:
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PatternLineEffectColumnNode:
    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PatternLineNoteColumnNode:
    note: Optional[str] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        },
    )
    instrument: Optional[str] = field(
        default=None,
        metadata={
            "name": "Instrument",
            "type": "Element",
        },
    )
    volume: Optional[str] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    panning: Optional[str] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    delay: Optional[str] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    effect_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectNumber",
            "type": "Element",
        },
    )
    effect_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectValue",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PatternSequenceEntry:
    pattern: Optional[int] = field(
        default=None,
        metadata={
            "name": "Pattern",
            "type": "Element",
        },
    )
    is_section_start: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSectionStart",
            "type": "Element",
        },
    )
    section_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SectionName",
            "type": "Element",
        },
    )
    muted_tracks: Optional["PatternSequenceEntry.MutedTracks"] = field(
        default=None,
        metadata={
            "name": "MutedTracks",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MutedTracks:
        muted_track: List[int] = field(
            default_factory=list,
            metadata={
                "name": "MutedTrack",
                "type": "Element",
            },
        )


@dataclass
class PatternSequenceSelection:
    cursor_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "CursorPos",
            "type": "Element",
        },
    )
    range_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "RangePos",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PdcTestDelayDevicePreset:
    device_slot: Optional["PdcTestDelayDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Phaser2DevicePreset:
    device_slot: Optional["Phaser2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PhaserDevicePreset:
    device_slot: Optional["PhaserDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RecordManager:
    linked_track_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedTrackIndex",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class RenoiseInstrumentActiveGeneratorTab(Enum):
    SAMPLES = "Samples"
    PLUGIN = "Plugin"
    EXT_MIDI = "Ext Midi"


@dataclass
class RenoiseSongScriptingToolData:
    class Meta:
        name = "RenoiseSong.ScriptingToolData"

    tool_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolId",
            "type": "Element",
        },
    )
    data: Optional[str] = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class RenoiseSongLastSoloedOutMode(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class RepeaterDeviceDivisorParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class RepeaterDevicePreset:
    device_slot: Optional["RepeaterDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Reverb2DevicePreset:
    device_slot: Optional["Reverb2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Reverb3DevicePreset:
    device_slot: Optional["Reverb3Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ReverbDevicePreset:
    device_slot: Optional["ReverbDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RewireInDevicePreset:
    device_slot: Optional["RewireInDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class RewireInDeviceChannelMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


@dataclass
class RingMod2DevicePreset:
    device_slot: Optional["RingMod2Device"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class RingMod2NoteFilterDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class RingModDevicePreset:
    device_slot: Optional["RingModDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleAhdsrModulationDevicePreset:
    device_slot: Optional["SampleAhdsrModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleAhdsrModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleAhdsrModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleAutoAmpModulationDevicePreset:
    device_slot: Optional["SampleAutoAmpModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleAutoAmpModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleAutoAmpModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleCompatibilityModulationDevicePreset:
    device_slot: Optional["SampleCompatibilityModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleCompatibilityModulationDeviceEnvelopeLoopMode(Enum):
    OFF = "Off"
    FORWARD = "Forward"
    BACKWARD = "Backward"
    PING_PONG = "PingPong"


class SampleCompatibilityModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleCompatibilityModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleEnvelopeModulationDevicePreset:
    device_slot: Optional["SampleEnvelopeModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleEnvelopeModulationDeviceLoopMode(Enum):
    OFF = "Off"
    FORWARD = "Forward"
    BACKWARD = "Backward"
    PING_PONG = "PingPong"


class SampleEnvelopeModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleEnvelopeModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleFaderModulationDevicePreset:
    device_slot: Optional["SampleFaderModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleFaderModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleFaderModulationDeviceScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class SampleFaderModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleKeyTrackingModulationDevicePreset:
    device_slot: Optional["SampleKeyTrackingModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleKeyTrackingModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleKeyTrackingModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleLfoModulationDevicePreset:
    device_slot: Optional["SampleLfoModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleLfoModulationDeviceMode(Enum):
    SIN = "Sin"
    SAW = "Saw"
    PULSE = "Pulse"
    RANDOM = "Random"


class SampleLfoModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleLfoModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleMixerDevicePreset:
    device_slot: Optional["SampleMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleModulationDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class SampleOperandModulationDevicePreset:
    device_slot: Optional["SampleOperandModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleOperandModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleOperandModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleSliceMarker:
    sample_position: Optional[int] = field(
        default=None,
        metadata={
            "name": "SamplePosition",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleSplitMap:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class SampleSplitMappingLayer(Enum):
    NOTE_ON_LAYER = "Note-On Layer"
    NOTE_OFF_LAYER = "Note-Off Layer"
    DISABLED_LAYER = "Disabled Layer"


@dataclass
class SampleStepperModulationDevicePreset:
    device_slot: Optional["SampleStepperModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleStepperModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleStepperModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


@dataclass
class SampleVelocityTrackingModulationDevicePreset:
    device_slot: Optional["SampleVelocityTrackingModulationDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SampleVelocityTrackingModulationDeviceMode(Enum):
    CLAMP = "Clamp"
    SCALE = "Scale"


class SampleVelocityTrackingModulationDeviceOperator(Enum):
    VALUE = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"


class SampleVelocityTrackingModulationDeviceTarget(Enum):
    VOLUME = "Volume"
    PANNING = "Panning"
    PITCH = "Pitch"
    CUTOFF = "Cutoff"
    RESONANCE = "Resonance"
    DRIVE = "Drive"


class SampleBeatSyncMode(Enum):
    REPITCH = "Repitch"
    TIME_STRETCH_PERCUSSION = "Time-Stretch (Percussion)"
    TIME_STRETCH_TEXTURE = "Time-Stretch (Texture)"


class SampleInterpolationMode(Enum):
    NONE_VALUE = "None"
    LINEAR = "Linear"
    CUBIC = "Cubic"
    SINC = "Sinc"


class SampleLoopMode(Enum):
    OFF = "Off"
    FORWARD = "Forward"
    BACKWARD = "Backward"
    PING_PONG = "PingPong"


class SampleNewNoteAction(Enum):
    CUT = "Cut"
    NOTE_OFF = "NoteOff"
    NONE_VALUE = "None"


class SampleSelectedChannel(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


@dataclass
class SendDevicePreset:
    device_slot: Optional["SendDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SendTrackMixerDevicePreset:
    device_slot: Optional["SendTrackMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SequencerGroupTrackState(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class SequencerMasterTrackState(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class SequencerSendTrackState(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


class SequencerTrackState(Enum):
    ACTIVE = "Active"
    OFF = "Off"
    MUTE = "Mute"


@dataclass
class ShaperDevicePreset:
    device_slot: Optional["ShaperDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SideChainDevicePreset:
    device_slot: Optional["SideChainDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignalFollowerDevicePreset:
    device_slot: Optional["SignalFollowerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class SignalFollowerDeviceDestScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class SignalFollowerDeviceInputMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


@dataclass
class StereoExpanderDevicePreset:
    device_slot: Optional["StereoExpanderDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class StereoExpanderDeviceMonoMixMode(Enum):
    L = "L"
    R = "R"
    L_R = "L+R"


class StutterBufferDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class StutterDevicePreset:
    device_slot: Optional["StutterDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class StutterDivisorDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class TrackMixerDevicePreset:
    device_slot: Optional["TrackMixerDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class TrackVolumeDeviceParameterVisualization(Enum):
    DONT_SHOW = "Dont Show"
    DEVICE_ONLY = "Device only"
    MIXER_AND_DEVICE = "Mixer and Device"


@dataclass
class VelocityDevicePreset:
    device_slot: Optional["VelocityDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class VelocityDeviceDestScaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


@dataclass
class XypadDevicePreset:
    class Meta:
        name = "XYPadDevicePreset"

    device_slot: Optional["XypadDevice"] = field(
        default=None,
        metadata={
            "name": "DeviceSlot",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDevicePreset",
        metadata={
            "type": "Attribute",
        },
    )


class XypadDeviceOut1Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


class XypadDeviceOut2Scaling(Enum):
    LOG_FAST = "Log Fast"
    LOG_SLOW = "Log Slow"
    LINEAR = "Linear"
    EXP_SLOW = "Exp Slow"
    EXP_FAST = "Exp Fast"


@dataclass
class DooferParameterMapping:
    dest_device_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DestDeviceIndex",
            "type": "Element",
        },
    )
    dest_parameter_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DestParameterIndex",
            "type": "Element",
        },
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    scaling: Optional[DooferParameterMappingScaling] = field(
        default=None,
        metadata={
            "name": "Scaling",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Envelope:
    play_mode: Optional[EnvelopePlayMode] = field(
        default=None,
        metadata={
            "name": "PlayMode",
            "type": "Element",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
        },
    )
    value_quantum: Optional[float] = field(
        default=None,
        metadata={
            "name": "ValueQuantum",
            "type": "Element",
        },
    )
    polarity: Optional[EnvelopePolarity] = field(
        default=None,
        metadata={
            "name": "Polarity",
            "type": "Element",
        },
    )
    points: Optional["Envelope.Points"] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Points:
        point: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Point",
                "type": "Element",
            },
        )


@dataclass
class InstrumentMidiGenerator:
    channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
        },
    )
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceName",
            "type": "Element",
        },
    )
    instrument_type: Optional[InstrumentMidiGeneratorInstrumentType] = field(
        default=None,
        metadata={
            "name": "InstrumentType",
            "type": "Element",
        },
    )
    delay: Optional[int] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    program: Optional[int] = field(
        default=None,
        metadata={
            "name": "Program",
            "type": "Element",
        },
    )
    bank: Optional[int] = field(
        default=None,
        metadata={
            "name": "Bank",
            "type": "Element",
        },
    )
    bank_order: Optional[InstrumentMidiGeneratorBankOrder] = field(
        default=None,
        metadata={
            "name": "BankOrder",
            "type": "Element",
        },
    )
    transpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentParameterMapping:
    dest_chain_type: Optional[InstrumentParameterMappingDestChainType] = field(
        default=None,
        metadata={
            "name": "DestChainType",
            "type": "Element",
        },
    )
    dest_chain_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DestChainIndex",
            "type": "Element",
        },
    )
    dest_device_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DestDeviceIndex",
            "type": "Element",
        },
    )
    dest_parameter_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DestParameterIndex",
            "type": "Element",
        },
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    scaling: Optional[InstrumentParameterMappingScaling] = field(
        default=None,
        metadata={
            "name": "Scaling",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentPhraseTriggerOptions:
    base_note: Optional[int] = field(
        default=None,
        metadata={
            "name": "BaseNote",
            "type": "Element",
        },
    )
    key_tracking: Optional[InstrumentPhraseTriggerOptionsKeyTracking] = field(
        default=None,
        metadata={
            "name": "KeyTracking",
            "type": "Element",
        },
    )
    loop: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Loop",
            "type": "Element",
        },
    )
    loop_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopStart",
            "type": "Element",
        },
    )
    loop_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopEnd",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentPluginRouting:
    enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Enabled",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    mix_mode: Optional[InstrumentPluginRoutingMixMode] = field(
        default=None,
        metadata={
            "name": "MixMode",
            "type": "Element",
        },
    )
    auto_assign: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoAssign",
            "type": "Element",
        },
    )
    assigned_track: Optional[int] = field(
        default=None,
        metadata={
            "name": "AssignedTrack",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MidiMapping:
    mapping_mode: Optional[MidiMappingMappingMode] = field(
        default=None,
        metadata={
            "name": "MappingMode",
            "type": "Element",
        },
    )
    controller_mode: Optional[MidiMappingControllerMode] = field(
        default=None,
        metadata={
            "name": "ControllerMode",
            "type": "Element",
        },
    )
    note_mode: Optional[MidiMappingNoteMode] = field(
        default=None,
        metadata={
            "name": "NoteMode",
            "type": "Element",
        },
    )
    channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
        },
    )
    ccnumber_or_note: Optional[int] = field(
        default=None,
        metadata={
            "name": "CCNumberOrNote",
            "type": "Element",
        },
    )
    min: Optional[float] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[float] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PatternLineNode:
    note_columns: Optional["PatternLineNode.NoteColumns"] = field(
        default=None,
        metadata={
            "name": "NoteColumns",
            "type": "Element",
        },
    )
    effect_columns: Optional["PatternLineNode.EffectColumns"] = field(
        default=None,
        metadata={
            "name": "EffectColumns",
            "type": "Element",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class NoteColumns:
        note_column: List[PatternLineNoteColumnNode] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumn",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class EffectColumns:
        effect_column: List[PatternLineEffectColumnNode] = field(
            default_factory=list,
            metadata={
                "name": "EffectColumn",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PatternSequence:
    current_position: Optional[int] = field(
        default=None,
        metadata={
            "name": "CurrentPosition",
            "type": "Element",
        },
    )
    sequence_entries: Optional["PatternSequence.SequenceEntries"] = field(
        default=None,
        metadata={
            "name": "SequenceEntries",
            "type": "Element",
        },
    )
    sequence_selection: Optional[PatternSequenceSelection] = field(
        default=None,
        metadata={
            "name": "SequenceSelection",
            "type": "Element",
        },
    )
    loop_selection: Optional[PatternSequenceSelection] = field(
        default=None,
        metadata={
            "name": "LoopSelection",
            "type": "Element",
        },
    )
    pattern_name_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatternNameWidth",
            "type": "Element",
        },
    )
    pattern_matrix_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatternMatrixWidth",
            "type": "Element",
        },
    )
    pattern_slot_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatternSlotHeight",
            "type": "Element",
        },
    )
    pattern_slot_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "PatternSlotWidth",
            "type": "Element",
        },
    )
    highlite_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "HighliteStep",
            "type": "Element",
        },
    )
    highlite_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "HighliteOffset",
            "type": "Element",
        },
    )
    keep_sequence_sorted: Optional[bool] = field(
        default=None,
        metadata={
            "name": "KeepSequenceSorted",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class SequenceEntries:
        sequence_entry: List[PatternSequenceEntry] = field(
            default_factory=list,
            metadata={
                "name": "SequenceEntry",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SampleSplitMapping:
    layer: Optional[SampleSplitMappingLayer] = field(
        default=None,
        metadata={
            "name": "Layer",
            "type": "Element",
        },
    )
    base_note: Optional[int] = field(
        default=None,
        metadata={
            "name": "BaseNote",
            "type": "Element",
        },
    )
    note_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteStart",
            "type": "Element",
        },
    )
    note_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteEnd",
            "type": "Element",
        },
    )
    map_key_to_pitch: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MapKeyToPitch",
            "type": "Element",
        },
    )
    velocity_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "VelocityStart",
            "type": "Element",
        },
    )
    velocity_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "VelocityEnd",
            "type": "Element",
        },
    )
    map_velocity_to_volume: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MapVelocityToVolume",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AudioPluginDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[AudioPluginDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["AudioPluginDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Comb2NoteFilterDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[Comb2NoteFilterDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["Comb2NoteFilterDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class DooferMacroParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[DooferMacroParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["DooferMacroParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    mappings: Optional["DooferMacroParameter.Mappings"] = field(
        default=None,
        metadata={
            "name": "Mappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Mappings:
        mapping: List[DooferParameterMapping] = field(
            default_factory=list,
            metadata={
                "name": "Mapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class FilterDeviceIsActiveParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[FilterDeviceIsActiveParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["FilterDeviceIsActiveParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class FilterDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[FilterDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["FilterDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class InstrumentMacroParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[InstrumentMacroParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["InstrumentMacroParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    mappings: Optional["InstrumentMacroParameter.Mappings"] = field(
        default=None,
        metadata={
            "name": "Mappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Mappings:
        mapping: List[InstrumentParameterMapping] = field(
            default_factory=list,
            metadata={
                "name": "Mapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class InstrumentPhrase:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    lines: Optional["InstrumentPhrase.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    autoseek: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Autoseek",
            "type": "Element",
        },
    )
    lines_per_beat: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinesPerBeat",
            "type": "Element",
        },
    )
    shuffle_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShuffleIsActive",
            "type": "Element",
        },
    )
    shuffle_amounts: Optional["InstrumentPhrase.ShuffleAmounts"] = field(
        default=None,
        metadata={
            "name": "ShuffleAmounts",
            "type": "Element",
        },
    )
    number_of_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    visible_note_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisibleNoteColumns",
            "type": "Element",
        },
    )
    visible_effect_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisibleEffectColumns",
            "type": "Element",
        },
    )
    note_column_names: Optional["InstrumentPhrase.NoteColumnNames"] = field(
        default=None,
        metadata={
            "name": "NoteColumnNames",
            "type": "Element",
        },
    )
    note_column_states: Optional["InstrumentPhrase.NoteColumnStates"] = field(
        default=None,
        metadata={
            "name": "NoteColumnStates",
            "type": "Element",
        },
    )
    instrument_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InstrumentColumnIsVisible",
            "type": "Element",
        },
    )
    volume_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolumeColumnIsVisible",
            "type": "Element",
        },
    )
    panning_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanningColumnIsVisible",
            "type": "Element",
        },
    )
    delay_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelayColumnIsVisible",
            "type": "Element",
        },
    )
    sample_effects_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleEffectsColumnIsVisible",
            "type": "Element",
        },
    )
    trigger_options: Optional[InstrumentPhraseTriggerOptions] = field(
        default=None,
        metadata={
            "name": "TriggerOptions",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        line: List[PatternLineNode] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )

    @dataclass
    class ShuffleAmounts:
        shuffle_amount: List[int] = field(
            default_factory=list,
            metadata={
                "name": "ShuffleAmount",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnNames:
        note_column_name: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnName",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnStates:
        note_column_state: List[NoteColumnStatesNoteColumnState1] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnState",
                "type": "Element",
            },
        )


@dataclass
class InstrumentPhraseMapping:
    phrase_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "PhraseIndex",
            "type": "Element",
        },
    )
    note_range_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteRangeStart",
            "type": "Element",
        },
    )
    note_range_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "NoteRangeEnd",
            "type": "Element",
        },
    )
    trigger_options: Optional[InstrumentPhraseTriggerOptions] = field(
        default=None,
        metadata={
            "name": "TriggerOptions",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MidiActionMappings:
    action: Optional[str] = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
        },
    )
    midi_mappings: Optional["MidiActionMappings.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class MidiControlDeviceFilterDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[
        MidiControlDeviceFilterDeviceParameterVisualization
    ] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional[
        "MidiControlDeviceFilterDeviceParameter.MidiMappings"
    ] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class NonContinuesDeviceParameter:
    midi_mappings: Optional["NonContinuesDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PatternTrackEnvelope:
    device_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DeviceIndex",
            "type": "Element",
        },
    )
    parameter_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterIndex",
            "type": "Element",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RepeaterDeviceDivisorParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[RepeaterDeviceDivisorParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["RepeaterDeviceDivisorParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RepeaterMidiTriggerParameter:
    midi_mappings: Optional["RepeaterMidiTriggerParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class RingMod2NoteFilterDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[RingMod2NoteFilterDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["RingMod2NoteFilterDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class Sample:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
        },
    )
    file_modification_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FileModificationDate",
            "type": "Element",
        },
    )
    file_modification_day_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "FileModificationDayTime",
            "type": "Element",
        },
    )
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    panning: Optional[float] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    transpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    finetune: Optional[int] = field(
        default=None,
        metadata={
            "name": "Finetune",
            "type": "Element",
        },
    )
    beat_sync_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BeatSyncIsActive",
            "type": "Element",
        },
    )
    beat_sync_mode: Optional[SampleBeatSyncMode] = field(
        default=None,
        metadata={
            "name": "BeatSyncMode",
            "type": "Element",
        },
    )
    beat_sync_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "BeatSyncLines",
            "type": "Element",
        },
    )
    one_shot_trigger: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OneShotTrigger",
            "type": "Element",
        },
    )
    new_note_action: Optional[SampleNewNoteAction] = field(
        default=None,
        metadata={
            "name": "NewNoteAction",
            "type": "Element",
        },
    )
    oversample: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Oversample",
            "type": "Element",
        },
    )
    interpolation_mode: Optional[SampleInterpolationMode] = field(
        default=None,
        metadata={
            "name": "InterpolationMode",
            "type": "Element",
        },
    )
    auto_seek: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoSeek",
            "type": "Element",
        },
    )
    auto_fade: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoFade",
            "type": "Element",
        },
    )
    loop_mode: Optional[SampleLoopMode] = field(
        default=None,
        metadata={
            "name": "LoopMode",
            "type": "Element",
        },
    )
    loop_release: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LoopRelease",
            "type": "Element",
        },
    )
    loop_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopStart",
            "type": "Element",
        },
    )
    loop_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopEnd",
            "type": "Element",
        },
    )
    slice_markers: Optional["Sample.SliceMarkers"] = field(
        default=None,
        metadata={
            "name": "SliceMarkers",
            "type": "Element",
        },
    )
    single_slice_trigger_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SingleSliceTriggerEnabled",
            "type": "Element",
        },
    )
    is_alias: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAlias",
            "type": "Element",
        },
    )
    mute_group_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "MuteGroupIndex",
            "type": "Element",
        },
    )
    modulation_set_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ModulationSetIndex",
            "type": "Element",
        },
    )
    device_chain_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "DeviceChainIndex",
            "type": "Element",
        },
    )
    mapping: Optional[SampleSplitMapping] = field(
        default=None,
        metadata={
            "name": "Mapping",
            "type": "Element",
        },
    )
    display_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayStart",
            "type": "Element",
        },
    )
    display_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayLength",
            "type": "Element",
        },
    )
    selection_range_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectionRangeStart",
            "type": "Element",
        },
    )
    selection_range_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectionRangeEnd",
            "type": "Element",
        },
    )
    selected_channel: Optional[SampleSelectedChannel] = field(
        default=None,
        metadata={
            "name": "SelectedChannel",
            "type": "Element",
        },
    )
    vzoom_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "VZoomFactor",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class SliceMarkers:
        slice_marker: List[SampleSliceMarker] = field(
            default_factory=list,
            metadata={
                "name": "SliceMarker",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SampleModulationDeviceNonContinousParameter:
    midi_mappings: Optional[
        "SampleModulationDeviceNonContinousParameter.MidiMappings"
    ] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SampleModulationDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[SampleModulationDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["SampleModulationDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class StutterBufferDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[StutterBufferDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["StutterBufferDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class StutterDivisorDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[StutterDivisorDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["StutterDivisorDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class TrackVolumeDeviceParameter:
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    visualization: Optional[TrackVolumeDeviceParameterVisualization] = field(
        default=None,
        metadata={
            "name": "Visualization",
            "type": "Element",
        },
    )
    midi_mappings: Optional["TrackVolumeDeviceParameter.MidiMappings"] = field(
        default=None,
        metadata={
            "name": "MidiMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class MidiMappings:
        midi_mapping: List[MidiMapping] = field(
            default_factory=list,
            metadata={
                "name": "MidiMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class AnalogFilterDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[AnalogFilterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[AnalogFilterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oversampling_factor: Optional[AnalogFilterDeviceOversamplingFactor] = field(
        default=None,
        metadata={
            "name": "OversamplingFactor",
            "type": "Element",
        },
    )
    model: Optional[AnalogFilterDeviceModel] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resonance",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Drive",
            "type": "Element",
        },
    )
    show_response_view: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowResponseView",
            "type": "Element",
        },
    )
    response_view_max_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "ResponseViewMaxGain",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="AnalogFilterDevice",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class AudioPluginDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[AudioPluginDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[AudioPluginDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    active_program: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveProgram",
            "type": "Element",
        },
    )
    plugin_type: Optional[AudioPluginDevicePluginType] = field(
        default=None,
        metadata={
            "name": "PluginType",
            "type": "Element",
        },
    )
    plugin_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "PluginIdentifier",
            "type": "Element",
        },
    )
    plugin_display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PluginDisplayName",
            "type": "Element",
        },
    )
    plugin_short_display_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "PluginShortDisplayName",
            "type": "Element",
        },
    )
    plugin_editor_window_position: Optional[str] = field(
        default=None,
        metadata={
            "name": "PluginEditorWindowPosition",
            "type": "Element",
        },
    )
    parameter_chunk_type: Optional[AudioPluginDeviceParameterChunkType] = field(
        default=None,
        metadata={
            "name": "ParameterChunkType",
            "type": "Element",
        },
    )
    parameter_chunk: Optional[str] = field(
        default=None,
        metadata={
            "name": "ParameterChunk",
            "type": "Element",
            "required": True,
        },
    )
    parameters: Optional["AudioPluginDevice.Parameters"] = field(
        default=None,
        metadata={
            "name": "Parameters",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="AudioPluginDevice",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Parameters:
        parameter: List[AudioPluginDeviceParameter] = field(
            default_factory=list,
            metadata={
                "name": "Parameter",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class BusCompressorDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[BusCompressorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[BusCompressorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    ratio: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Element",
        },
    )
    attack: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    make_up: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MakeUp",
            "type": "Element",
        },
    )
    knee: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Knee",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="BusCompressorDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CabinetSimulatorDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[CabinetSimulatorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[CabinetSimulatorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    cabinet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cabinet",
            "type": "Element",
        },
    )
    routing: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Routing",
            "type": "Element",
        },
    )
    distortion: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Distortion",
            "type": "Element",
        },
    )
    wet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
        },
    )
    dry: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
        },
    )
    stereo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Stereo",
            "type": "Element",
        },
    )
    gain0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain0",
            "type": "Element",
        },
    )
    gain1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain1",
            "type": "Element",
        },
    )
    gain2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain2",
            "type": "Element",
        },
    )
    gain3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain3",
            "type": "Element",
        },
    )
    gain4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain4",
            "type": "Element",
        },
    )
    frequency0: Optional[float] = field(
        default=None,
        metadata={
            "name": "Frequency0",
            "type": "Element",
        },
    )
    frequency1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Frequency1",
            "type": "Element",
        },
    )
    frequency2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Frequency2",
            "type": "Element",
        },
    )
    frequency3: Optional[float] = field(
        default=None,
        metadata={
            "name": "Frequency3",
            "type": "Element",
        },
    )
    frequency4: Optional[float] = field(
        default=None,
        metadata={
            "name": "Frequency4",
            "type": "Element",
        },
    )
    band_width0: Optional[float] = field(
        default=None,
        metadata={
            "name": "BandWidth0",
            "type": "Element",
        },
    )
    band_width1: Optional[float] = field(
        default=None,
        metadata={
            "name": "BandWidth1",
            "type": "Element",
        },
    )
    band_width2: Optional[float] = field(
        default=None,
        metadata={
            "name": "BandWidth2",
            "type": "Element",
        },
    )
    band_width3: Optional[float] = field(
        default=None,
        metadata={
            "name": "BandWidth3",
            "type": "Element",
        },
    )
    band_width4: Optional[float] = field(
        default=None,
        metadata={
            "name": "BandWidth4",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="CabinetSimulatorDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Chorus2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Chorus2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Chorus2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
        },
    )
    depth: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    dry_wet_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryWetMix",
            "type": "Element",
        },
    )
    dephase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dephase",
            "type": "Element",
        },
    )
    reset: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Reset",
            "type": "Element",
        },
    )
    filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterFreq",
            "type": "Element",
        },
    )
    filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterResonance",
            "type": "Element",
        },
    )
    filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterDrive",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Chorus2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ChorusDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[ChorusDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[ChorusDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    lfo_rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LfoRate",
            "type": "Element",
        },
    )
    lfo_depth: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LfoDepth",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    dry_wet_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryWetMix",
            "type": "Element",
        },
    )
    phase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
        },
    )
    filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterFreq",
            "type": "Element",
        },
    )
    filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterResonance",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="ChorusDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Comb2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Comb2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Comb2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    note: Optional[Comb2NoteFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        },
    )
    transpose: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    dry_wet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryWet",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Comb2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CombDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[CombDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[CombDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    wet_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetOut",
            "type": "Element",
        },
    )
    dry_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryOut",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="CombDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompressorDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[CompressorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[CompressorDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    log_threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LogThreshold",
            "type": "Element",
        },
    )
    ratio: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Element",
        },
    )
    attack: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="CompressorDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ConvolverDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[ConvolverDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[ConvolverDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Element",
        },
    )
    start: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
        },
    )
    length: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
        },
    )
    resample: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resample",
            "type": "Element",
        },
    )
    pre_delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PreDelay",
            "type": "Element",
        },
    )
    color: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    dry: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
        },
    )
    wet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
        },
    )
    stereo: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Stereo",
            "type": "Element",
        },
    )
    impulse_data_left: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImpulseDataLeft",
            "type": "Element",
            "required": True,
        },
    )
    impulse_data_right: Optional[str] = field(
        default=None,
        metadata={
            "name": "ImpulseDataRight",
            "type": "Element",
            "required": True,
        },
    )
    impulse_data_sample_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImpulseDataSampleRate",
            "type": "Element",
        },
    )
    sample_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleName",
            "type": "Element",
        },
    )
    sample_directory_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "SampleDirectoryPath",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="ConvolverDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CrossoverDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[CrossoverDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[CrossoverDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    out1_send_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1SendAmount",
            "type": "Element",
        },
    )
    out1_dest_send_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestSendTrack",
            "type": "Element",
        },
    )
    out1_mute_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Out1MuteSource",
            "type": "Element",
        },
    )
    out2_send_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2SendAmount",
            "type": "Element",
        },
    )
    out2_dest_send_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestSendTrack",
            "type": "Element",
        },
    )
    out2_mute_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Out2MuteSource",
            "type": "Element",
        },
    )
    out3_send_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3SendAmount",
            "type": "Element",
        },
    )
    out3_dest_send_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3DestSendTrack",
            "type": "Element",
        },
    )
    out3_mute_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Out3MuteSource",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    apply_post_volume: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApplyPostVolume",
            "type": "Element",
        },
    )
    graph_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GraphVisible",
            "type": "Element",
        },
    )
    low_frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LowFrequency",
            "type": "Element",
        },
    )
    high_frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "HighFrequency",
            "type": "Element",
        },
    )
    crossover_type: Optional[CrossoverDeviceCrossoverType] = field(
        default=None,
        metadata={
            "name": "CrossoverType",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="CrossoverDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DcOffsetDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[DcOffsetDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[DcOffsetDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    dcoffset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DCOffset",
            "type": "Element",
        },
    )
    auto_dc: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AutoDC",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="DcOffsetDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DelayDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[DelayDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[DelayDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    ldelay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LDelay",
            "type": "Element",
        },
    )
    rdelay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RDelay",
            "type": "Element",
        },
    )
    lfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LFeedback",
            "type": "Element",
        },
    )
    rfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RFeedback",
            "type": "Element",
        },
    )
    track_send: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "TrackSend",
            "type": "Element",
        },
    )
    line_sync: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LineSync",
            "type": "Element",
        },
    )
    lset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LSetSyncedDelay",
            "type": "Element",
        },
    )
    rset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RSetSyncedDelay",
            "type": "Element",
        },
    )
    ltap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LTapPan",
            "type": "Element",
        },
    )
    rtap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RTapPan",
            "type": "Element",
        },
    )
    mute_dry_signal: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MuteDrySignal",
            "type": "Element",
        },
    )
    lsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LSyncTime",
            "type": "Element",
        },
    )
    rsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RSyncTime",
            "type": "Element",
        },
    )
    lsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LSyncOffset",
            "type": "Element",
        },
    )
    rsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RSyncOffset",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="DelayDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DigitalFilterDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[DigitalFilterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[DigitalFilterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oversampling_factor: Optional[DigitalFilterDeviceOversamplingFactor] = field(
        default=None,
        metadata={
            "name": "OversamplingFactor",
            "type": "Element",
        },
    )
    model: Optional[DigitalFilterDeviceModel] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    q: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
        },
    )
    ripple: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ripple",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    show_response_view: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowResponseView",
            "type": "Element",
        },
    )
    response_view_max_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "ResponseViewMaxGain",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="DigitalFilterDevice",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Distortion2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Distortion2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Distortion2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oversample: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Oversample",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Drive",
            "type": "Element",
        },
    )
    tone: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tone",
            "type": "Element",
        },
    )
    wet_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetOut",
            "type": "Element",
        },
    )
    dry_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryOut",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="Distortion2Device",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class DistortionDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[DistortionDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[DistortionDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    lp_or_clamp: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LpOrClamp",
            "type": "Element",
        },
    )
    wet_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetOut",
            "type": "Element",
        },
    )
    dry_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryOut",
            "type": "Element",
        },
    )
    gate_or_filter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "GateOrFilter",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="DistortionDevice",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Eq10Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Eq10DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Eq10DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    input_mode: Optional[Eq10DeviceInputMode] = field(
        default=None,
        metadata={
            "name": "InputMode",
            "type": "Element",
        },
    )
    max_visualized_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxVisualizedGain",
            "type": "Element",
        },
    )
    gain0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain0",
            "type": "Element",
        },
    )
    gain1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain1",
            "type": "Element",
        },
    )
    gain2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain2",
            "type": "Element",
        },
    )
    gain3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain3",
            "type": "Element",
        },
    )
    gain4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain4",
            "type": "Element",
        },
    )
    gain5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain5",
            "type": "Element",
        },
    )
    gain6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain6",
            "type": "Element",
        },
    )
    gain7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain7",
            "type": "Element",
        },
    )
    gain8: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain8",
            "type": "Element",
        },
    )
    gain9: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain9",
            "type": "Element",
        },
    )
    frequency0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency0",
            "type": "Element",
        },
    )
    frequency1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency1",
            "type": "Element",
        },
    )
    frequency2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency2",
            "type": "Element",
        },
    )
    frequency3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency3",
            "type": "Element",
        },
    )
    frequency4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency4",
            "type": "Element",
        },
    )
    frequency5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency5",
            "type": "Element",
        },
    )
    frequency6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency6",
            "type": "Element",
        },
    )
    frequency7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency7",
            "type": "Element",
        },
    )
    frequency8: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency8",
            "type": "Element",
        },
    )
    frequency9: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency9",
            "type": "Element",
        },
    )
    band_width0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth0",
            "type": "Element",
        },
    )
    band_width1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth1",
            "type": "Element",
        },
    )
    band_width2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth2",
            "type": "Element",
        },
    )
    band_width3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth3",
            "type": "Element",
        },
    )
    band_width4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth4",
            "type": "Element",
        },
    )
    band_width5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth5",
            "type": "Element",
        },
    )
    band_width6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth6",
            "type": "Element",
        },
    )
    band_width7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth7",
            "type": "Element",
        },
    )
    band_width8: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth8",
            "type": "Element",
        },
    )
    band_width9: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth9",
            "type": "Element",
        },
    )
    visualization_mode: Optional[Eq10DeviceVisualizationMode] = field(
        default=None,
        metadata={
            "name": "VisualizationMode",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Eq10Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Eq5Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Eq5DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Eq5DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    input_mode: Optional[Eq5DeviceInputMode] = field(
        default=None,
        metadata={
            "name": "InputMode",
            "type": "Element",
        },
    )
    max_visualized_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxVisualizedGain",
            "type": "Element",
        },
    )
    gain0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain0",
            "type": "Element",
        },
    )
    gain1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain1",
            "type": "Element",
        },
    )
    gain2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain2",
            "type": "Element",
        },
    )
    gain3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain3",
            "type": "Element",
        },
    )
    gain4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain4",
            "type": "Element",
        },
    )
    frequency0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency0",
            "type": "Element",
        },
    )
    frequency1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency1",
            "type": "Element",
        },
    )
    frequency2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency2",
            "type": "Element",
        },
    )
    frequency3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency3",
            "type": "Element",
        },
    )
    frequency4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency4",
            "type": "Element",
        },
    )
    band_width0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth0",
            "type": "Element",
        },
    )
    band_width1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth1",
            "type": "Element",
        },
    )
    band_width2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth2",
            "type": "Element",
        },
    )
    band_width3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth3",
            "type": "Element",
        },
    )
    band_width4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BandWidth4",
            "type": "Element",
        },
    )
    visualization_mode: Optional[Eq5DeviceVisualizationMode] = field(
        default=None,
        metadata={
            "name": "VisualizationMode",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Eq5Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ExciterDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[ExciterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[ExciterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    low_frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LowFrequency",
            "type": "Element",
        },
    )
    high_frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "HighFrequency",
            "type": "Element",
        },
    )
    visible_band: Optional[ExciterDeviceVisibleBand] = field(
        default=None,
        metadata={
            "name": "VisibleBand",
            "type": "Element",
        },
    )
    band1_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Mode",
            "type": "Element",
        },
    )
    band1_sharpness1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Sharpness1",
            "type": "Element",
        },
    )
    band1_amount1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Amount1",
            "type": "Element",
        },
    )
    band1_sharpness2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Sharpness2",
            "type": "Element",
        },
    )
    band1_amount2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Amount2",
            "type": "Element",
        },
    )
    band1_sharpness3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Sharpness3",
            "type": "Element",
        },
    )
    band1_amount3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band1Amount3",
            "type": "Element",
        },
    )
    band2_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Mode",
            "type": "Element",
        },
    )
    band2_sharpness1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Sharpness1",
            "type": "Element",
        },
    )
    band2_amount1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Amount1",
            "type": "Element",
        },
    )
    band2_sharpness2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Sharpness2",
            "type": "Element",
        },
    )
    band2_amount2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Amount2",
            "type": "Element",
        },
    )
    band2_sharpness3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Sharpness3",
            "type": "Element",
        },
    )
    band2_amount3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band2Amount3",
            "type": "Element",
        },
    )
    band3_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Mode",
            "type": "Element",
        },
    )
    band3_sharpness1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Sharpness1",
            "type": "Element",
        },
    )
    band3_amount1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Amount1",
            "type": "Element",
        },
    )
    band3_sharpness2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Sharpness2",
            "type": "Element",
        },
    )
    band3_amount2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Amount2",
            "type": "Element",
        },
    )
    band3_sharpness3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Sharpness3",
            "type": "Element",
        },
    )
    band3_amount3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Band3Amount3",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="ExciterDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Filter1Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Filter1DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Filter1DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resonance",
            "type": "Element",
        },
    )
    innertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Innertia",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="Filter1Device",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Filter2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Filter2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Filter2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resonance",
            "type": "Element",
        },
    )
    innertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Innertia",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    limit_moog_filter_output: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LimitMoogFilterOutput",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="Filter2Device",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class Filter3Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Filter3DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Filter3DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )
    q: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Q",
            "type": "Element",
        },
    )
    gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    model: Optional[Filter3DeviceModel] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="Filter3Device",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class FilterDistortionDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[FilterDistortionDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[FilterDistortionDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oversample: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Oversample",
            "type": "Element",
        },
    )
    filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Drive",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resonance",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FilterDistortionDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Flanger2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Flanger2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Flanger2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
        },
    )
    amplitude: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amplitude",
            "type": "Element",
        },
    )
    feed_back: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FeedBack",
            "type": "Element",
        },
    )
    delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    dephase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dephase",
            "type": "Element",
        },
    )
    reset: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Reset",
            "type": "Element",
        },
    )
    filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterFreq",
            "type": "Element",
        },
    )
    filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterResonance",
            "type": "Element",
        },
    )
    filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterDrive",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Flanger2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FlangerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[FlangerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[FlangerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
        },
    )
    amplitude: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amplitude",
            "type": "Element",
        },
    )
    feed_back: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FeedBack",
            "type": "Element",
        },
    )
    delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    dephase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dephase",
            "type": "Element",
        },
    )
    filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterFreq",
            "type": "Element",
        },
    )
    filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "FilterResonance",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FlangerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FormulaMetaDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[FormulaMetaDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[FormulaMetaDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    formula_paragraphs: Optional["FormulaMetaDevice.FormulaParagraphs"] = field(
        default=None,
        metadata={
            "name": "FormulaParagraphs",
            "type": "Element",
        },
    )
    functions_paragraphs: Optional["FormulaMetaDevice.FunctionsParagraphs"] = field(
        default=None,
        metadata={
            "name": "FunctionsParagraphs",
            "type": "Element",
        },
    )
    input_name_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputNameA",
            "type": "Element",
        },
    )
    input_name_b: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputNameB",
            "type": "Element",
        },
    )
    input_name_c: Optional[str] = field(
        default=None,
        metadata={
            "name": "InputNameC",
            "type": "Element",
        },
    )
    editor_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EditorVisible",
            "type": "Element",
        },
    )
    input_a: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputA",
            "type": "Element",
        },
    )
    input_b: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputB",
            "type": "Element",
        },
    )
    input_c: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputC",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="FormulaMetaDevice",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class FormulaParagraphs:
        formula_paragraph: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FormulaParagraph",
                "type": "Element",
            },
        )

    @dataclass
    class FunctionsParagraphs:
        functions_paragraph: List[str] = field(
            default_factory=list,
            metadata={
                "name": "FunctionsParagraph",
                "type": "Element",
            },
        )


@dataclass
class GainerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[GainerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[GainerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    lphase_invert: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LPhaseInvert",
            "type": "Element",
        },
    )
    rphase_invert: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RPhaseInvert",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="GainerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Gate2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Gate2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Gate2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    attack: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    hold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Hold",
            "type": "Element",
        },
    )
    release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    floor: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        },
    )
    listen_to_side_chain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ListenToSideChain",
            "type": "Element",
        },
    )
    side_chain_hp_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SideChainHpFreq",
            "type": "Element",
        },
    )
    side_chain_lp_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SideChainLpFreq",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    mix_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MixMode",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="Gate2Device",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class GateDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[GateDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[GateDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    attack_in_ms: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AttackInMs",
            "type": "Element",
        },
    )
    hold_in_ms: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "HoldInMs",
            "type": "Element",
        },
    )
    release_in_ms: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ReleaseInMs",
            "type": "Element",
        },
    )
    gated_volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "GatedVolume",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="GateDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GroupTrackMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[GroupTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[GroupTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    surround: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Surround",
            "type": "Element",
        },
    )
    post_panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostPanning",
            "type": "Element",
        },
    )
    post_volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostVolume",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="GroupTrackMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class HydraDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[HydraDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[HydraDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    visible_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisiblePages",
            "type": "Element",
        },
    )
    input_value: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputValue",
            "type": "Element",
        },
    )
    out1_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestTrack",
            "type": "Element",
        },
    )
    out1_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestEffect",
            "type": "Element",
        },
    )
    out1_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestParameter",
            "type": "Element",
        },
    )
    out1_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1Min",
            "type": "Element",
        },
    )
    out1_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1Max",
            "type": "Element",
        },
    )
    out1_scaling: Optional[HydraDeviceOut1Scaling] = field(
        default=None,
        metadata={
            "name": "Out1Scaling",
            "type": "Element",
        },
    )
    out2_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestTrack",
            "type": "Element",
        },
    )
    out2_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestEffect",
            "type": "Element",
        },
    )
    out2_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestParameter",
            "type": "Element",
        },
    )
    out2_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2Min",
            "type": "Element",
        },
    )
    out2_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2Max",
            "type": "Element",
        },
    )
    out2_scaling: Optional[HydraDeviceOut2Scaling] = field(
        default=None,
        metadata={
            "name": "Out2Scaling",
            "type": "Element",
        },
    )
    out3_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3DestTrack",
            "type": "Element",
        },
    )
    out3_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3DestEffect",
            "type": "Element",
        },
    )
    out3_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3DestParameter",
            "type": "Element",
        },
    )
    out3_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3Min",
            "type": "Element",
        },
    )
    out3_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out3Max",
            "type": "Element",
        },
    )
    out3_scaling: Optional[HydraDeviceOut3Scaling] = field(
        default=None,
        metadata={
            "name": "Out3Scaling",
            "type": "Element",
        },
    )
    out4_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out4DestTrack",
            "type": "Element",
        },
    )
    out4_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out4DestEffect",
            "type": "Element",
        },
    )
    out4_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out4DestParameter",
            "type": "Element",
        },
    )
    out4_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out4Min",
            "type": "Element",
        },
    )
    out4_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out4Max",
            "type": "Element",
        },
    )
    out4_scaling: Optional[HydraDeviceOut4Scaling] = field(
        default=None,
        metadata={
            "name": "Out4Scaling",
            "type": "Element",
        },
    )
    out5_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out5DestTrack",
            "type": "Element",
        },
    )
    out5_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out5DestEffect",
            "type": "Element",
        },
    )
    out5_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out5DestParameter",
            "type": "Element",
        },
    )
    out5_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out5Min",
            "type": "Element",
        },
    )
    out5_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out5Max",
            "type": "Element",
        },
    )
    out5_scaling: Optional[HydraDeviceOut5Scaling] = field(
        default=None,
        metadata={
            "name": "Out5Scaling",
            "type": "Element",
        },
    )
    out6_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out6DestTrack",
            "type": "Element",
        },
    )
    out6_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out6DestEffect",
            "type": "Element",
        },
    )
    out6_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out6DestParameter",
            "type": "Element",
        },
    )
    out6_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out6Min",
            "type": "Element",
        },
    )
    out6_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out6Max",
            "type": "Element",
        },
    )
    out6_scaling: Optional[HydraDeviceOut6Scaling] = field(
        default=None,
        metadata={
            "name": "Out6Scaling",
            "type": "Element",
        },
    )
    out7_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out7DestTrack",
            "type": "Element",
        },
    )
    out7_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out7DestEffect",
            "type": "Element",
        },
    )
    out7_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out7DestParameter",
            "type": "Element",
        },
    )
    out7_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out7Min",
            "type": "Element",
        },
    )
    out7_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out7Max",
            "type": "Element",
        },
    )
    out7_scaling: Optional[HydraDeviceOut7Scaling] = field(
        default=None,
        metadata={
            "name": "Out7Scaling",
            "type": "Element",
        },
    )
    out8_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out8DestTrack",
            "type": "Element",
        },
    )
    out8_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out8DestEffect",
            "type": "Element",
        },
    )
    out8_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out8DestParameter",
            "type": "Element",
        },
    )
    out8_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out8Min",
            "type": "Element",
        },
    )
    out8_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out8Max",
            "type": "Element",
        },
    )
    out8_scaling: Optional[HydraDeviceOut8Scaling] = field(
        default=None,
        metadata={
            "name": "Out8Scaling",
            "type": "Element",
        },
    )
    out9_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out9DestTrack",
            "type": "Element",
        },
    )
    out9_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out9DestEffect",
            "type": "Element",
        },
    )
    out9_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out9DestParameter",
            "type": "Element",
        },
    )
    out9_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out9Min",
            "type": "Element",
        },
    )
    out9_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out9Max",
            "type": "Element",
        },
    )
    out9_scaling: Optional[HydraDeviceOut9Scaling] = field(
        default=None,
        metadata={
            "name": "Out9Scaling",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="HydraDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentAutomationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[InstrumentAutomationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[InstrumentAutomationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    parameter_number0: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber0",
            "type": "Element",
        },
    )
    parameter_value0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue0",
            "type": "Element",
        },
    )
    parameter_number1: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber1",
            "type": "Element",
        },
    )
    parameter_value1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue1",
            "type": "Element",
        },
    )
    parameter_number2: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber2",
            "type": "Element",
        },
    )
    parameter_value2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue2",
            "type": "Element",
        },
    )
    parameter_number3: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber3",
            "type": "Element",
        },
    )
    parameter_value3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue3",
            "type": "Element",
        },
    )
    parameter_number4: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber4",
            "type": "Element",
        },
    )
    parameter_value4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue4",
            "type": "Element",
        },
    )
    parameter_number5: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber5",
            "type": "Element",
        },
    )
    parameter_value5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue5",
            "type": "Element",
        },
    )
    parameter_number6: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber6",
            "type": "Element",
        },
    )
    parameter_value6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue6",
            "type": "Element",
        },
    )
    parameter_number7: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber7",
            "type": "Element",
        },
    )
    parameter_value7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue7",
            "type": "Element",
        },
    )
    parameter_number8: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber8",
            "type": "Element",
        },
    )
    parameter_value8: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue8",
            "type": "Element",
        },
    )
    parameter_number9: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber9",
            "type": "Element",
        },
    )
    parameter_value9: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue9",
            "type": "Element",
        },
    )
    parameter_number10: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber10",
            "type": "Element",
        },
    )
    parameter_value10: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue10",
            "type": "Element",
        },
    )
    parameter_number11: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber11",
            "type": "Element",
        },
    )
    parameter_value11: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue11",
            "type": "Element",
        },
    )
    parameter_number12: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber12",
            "type": "Element",
        },
    )
    parameter_value12: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue12",
            "type": "Element",
        },
    )
    parameter_number13: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber13",
            "type": "Element",
        },
    )
    parameter_value13: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue13",
            "type": "Element",
        },
    )
    parameter_number14: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber14",
            "type": "Element",
        },
    )
    parameter_value14: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue14",
            "type": "Element",
        },
    )
    parameter_number15: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber15",
            "type": "Element",
        },
    )
    parameter_value15: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue15",
            "type": "Element",
        },
    )
    parameter_number16: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber16",
            "type": "Element",
        },
    )
    parameter_value16: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue16",
            "type": "Element",
        },
    )
    parameter_number17: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber17",
            "type": "Element",
        },
    )
    parameter_value17: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue17",
            "type": "Element",
        },
    )
    parameter_number18: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber18",
            "type": "Element",
        },
    )
    parameter_value18: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue18",
            "type": "Element",
        },
    )
    parameter_number19: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber19",
            "type": "Element",
        },
    )
    parameter_value19: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue19",
            "type": "Element",
        },
    )
    parameter_number20: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber20",
            "type": "Element",
        },
    )
    parameter_value20: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue20",
            "type": "Element",
        },
    )
    parameter_number21: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber21",
            "type": "Element",
        },
    )
    parameter_value21: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue21",
            "type": "Element",
        },
    )
    parameter_number22: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber22",
            "type": "Element",
        },
    )
    parameter_value22: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue22",
            "type": "Element",
        },
    )
    parameter_number23: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber23",
            "type": "Element",
        },
    )
    parameter_value23: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue23",
            "type": "Element",
        },
    )
    parameter_number24: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber24",
            "type": "Element",
        },
    )
    parameter_value24: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue24",
            "type": "Element",
        },
    )
    parameter_number25: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber25",
            "type": "Element",
        },
    )
    parameter_value25: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue25",
            "type": "Element",
        },
    )
    parameter_number26: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber26",
            "type": "Element",
        },
    )
    parameter_value26: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue26",
            "type": "Element",
        },
    )
    parameter_number27: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber27",
            "type": "Element",
        },
    )
    parameter_value27: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue27",
            "type": "Element",
        },
    )
    parameter_number28: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber28",
            "type": "Element",
        },
    )
    parameter_value28: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue28",
            "type": "Element",
        },
    )
    parameter_number29: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber29",
            "type": "Element",
        },
    )
    parameter_value29: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue29",
            "type": "Element",
        },
    )
    parameter_number30: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber30",
            "type": "Element",
        },
    )
    parameter_value30: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue30",
            "type": "Element",
        },
    )
    parameter_number31: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber31",
            "type": "Element",
        },
    )
    parameter_value31: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue31",
            "type": "Element",
        },
    )
    parameter_number32: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber32",
            "type": "Element",
        },
    )
    parameter_value32: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue32",
            "type": "Element",
        },
    )
    parameter_number33: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber33",
            "type": "Element",
        },
    )
    parameter_value33: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue33",
            "type": "Element",
        },
    )
    parameter_number34: Optional[int] = field(
        default=None,
        metadata={
            "name": "ParameterNumber34",
            "type": "Element",
        },
    )
    parameter_value34: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue34",
            "type": "Element",
        },
    )
    linked_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedInstrument",
            "type": "Element",
        },
    )
    visible_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisiblePages",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="InstrumentAutomationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentGlobalProperties:
    macro0: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro0",
            "type": "Element",
        },
    )
    macro1: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro1",
            "type": "Element",
        },
    )
    macro2: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro2",
            "type": "Element",
        },
    )
    macro3: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro3",
            "type": "Element",
        },
    )
    macro4: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro4",
            "type": "Element",
        },
    )
    macro5: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro5",
            "type": "Element",
        },
    )
    macro6: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro6",
            "type": "Element",
        },
    )
    macro7: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro7",
            "type": "Element",
        },
    )
    pitchbend_macro: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "PitchbendMacro",
            "type": "Element",
        },
    )
    modulation_wheel_macro: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "ModulationWheelMacro",
            "type": "Element",
        },
    )
    channel_pressure_macro: Optional[InstrumentMacroParameter] = field(
        default=None,
        metadata={
            "name": "ChannelPressureMacro",
            "type": "Element",
        },
    )
    macros_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MacrosVisible",
            "type": "Element",
        },
    )
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    transpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    scale: Optional[InstrumentGlobalPropertiesScale] = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
        },
    )
    scale_key: Optional[InstrumentGlobalPropertiesScaleKey] = field(
        default=None,
        metadata={
            "name": "ScaleKey",
            "type": "Element",
        },
    )
    quantize: Optional[InstrumentGlobalPropertiesQuantize] = field(
        default=None,
        metadata={
            "name": "Quantize",
            "type": "Element",
        },
    )
    monophonic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monophonic",
            "type": "Element",
        },
    )
    monophonic_glide: Optional[int] = field(
        default=None,
        metadata={
            "name": "MonophonicGlide",
            "type": "Element",
        },
    )
    comments: Optional["InstrumentGlobalProperties.Comments"] = field(
        default=None,
        metadata={
            "name": "Comments",
            "type": "Element",
        },
    )
    show_comments_after_loading: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowCommentsAfterLoading",
            "type": "Element",
        },
    )
    beats_per_min: Optional[float] = field(
        default=None,
        metadata={
            "name": "BeatsPerMin",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Comments:
        comment: List[str] = field(
            default_factory=list,
            metadata={
                "name": "Comment",
                "type": "Element",
            },
        )


@dataclass
class InstrumentMacroDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[InstrumentMacroDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[InstrumentMacroDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    parameter_value0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue0",
            "type": "Element",
        },
    )
    parameter_value1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue1",
            "type": "Element",
        },
    )
    parameter_value2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue2",
            "type": "Element",
        },
    )
    parameter_value3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue3",
            "type": "Element",
        },
    )
    parameter_value4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue4",
            "type": "Element",
        },
    )
    parameter_value5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue5",
            "type": "Element",
        },
    )
    parameter_value6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue6",
            "type": "Element",
        },
    )
    parameter_value7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ParameterValue7",
            "type": "Element",
        },
    )
    pitchbend_value: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PitchbendValue",
            "type": "Element",
        },
    )
    modulation_value: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ModulationValue",
            "type": "Element",
        },
    )
    channel_pressure_value: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ChannelPressureValue",
            "type": "Element",
        },
    )
    phrase_programm_value: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PhraseProgrammValue",
            "type": "Element",
        },
    )
    linked_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedInstrument",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="InstrumentMacroDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class InstrumentPhraseMap:
    mappings: Optional["InstrumentPhraseMap.Mappings"] = field(
        default=None,
        metadata={
            "name": "Mappings",
            "type": "Element",
        },
    )
    selected_mapping_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedMappingIndex",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Mappings:
        mapping: List[InstrumentPhraseMapping] = field(
            default_factory=list,
            metadata={
                "name": "Mapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class KeyTrackingDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[KeyTrackingDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[KeyTrackingDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    src_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "SrcInstrument",
            "type": "Element",
        },
    )
    dest_scaling: Optional[KeyTrackingDeviceDestScaling] = field(
        default=None,
        metadata={
            "name": "DestScaling",
            "type": "Element",
        },
    )
    key_tracking_mode: Optional[KeyTrackingDeviceKeyTrackingMode] = field(
        default=None,
        metadata={
            "name": "KeyTrackingMode",
            "type": "Element",
        },
    )
    key_tracking_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "KeyTrackingMin",
            "type": "Element",
        },
    )
    key_tracking_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "KeyTrackingMax",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    dest_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMin",
            "type": "Element",
        },
    )
    dest_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMax",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="KeyTrackingDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LfoDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[LfoDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[LfoDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    amplitude: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amplitude",
            "type": "Element",
        },
    )
    offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
        },
    )
    frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )
    type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    reset: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Reset",
            "type": "Element",
        },
    )
    custom_envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "CustomEnvelope",
            "type": "Element",
        },
    )
    custom_envelope_one_shot: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CustomEnvelopeOneShot",
            "type": "Element",
        },
    )
    use_adjusted_envelope_length: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseAdjustedEnvelopeLength",
            "type": "Element",
        },
    )
    type_attribute: str = field(
        init=False,
        default="LfoDevice",
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


@dataclass
class LineInDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[LineInDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[LineInDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    input_channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "InputChannel",
            "type": "Element",
        },
    )
    input_channel_mode: Optional[LineInDeviceInputChannelMode] = field(
        default=None,
        metadata={
            "name": "InputChannelMode",
            "type": "Element",
        },
    )
    input_latency_mode: Optional[LineInDeviceInputLatencyMode] = field(
        default=None,
        metadata={
            "name": "InputLatencyMode",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="LineInDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Lofi2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Lofi2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Lofi2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    bits: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Bits",
            "type": "Element",
        },
    )
    rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
        },
    )
    noise: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Noise",
            "type": "Element",
        },
    )
    wet_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetOut",
            "type": "Element",
        },
    )
    dry_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryOut",
            "type": "Element",
        },
    )
    interpolate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Interpolate",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Lofi2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class LofiDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[LofiDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[LofiDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    bit_crunsh: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BitCrunsh",
            "type": "Element",
        },
    )
    quality: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Quality",
            "type": "Element",
        },
    )
    noise: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Noise",
            "type": "Element",
        },
    )
    wet_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetOut",
            "type": "Element",
        },
    )
    dry_out: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryOut",
            "type": "Element",
        },
    )
    interpolate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Interpolate",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="LofiDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MasterTrackMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MasterTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MasterTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    surround: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Surround",
            "type": "Element",
        },
    )
    post_panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostPanning",
            "type": "Element",
        },
    )
    post_volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostVolume",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    auto_dc_correction: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoDcCorrection",
            "type": "Element",
        },
    )
    soft_clipping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SoftClipping",
            "type": "Element",
        },
    )
    auto_gain: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoGain",
            "type": "Element",
        },
    )
    bpm_automator: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "BpmAutomator",
            "type": "Element",
        },
    )
    lpb_automator: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LpbAutomator",
            "type": "Element",
        },
    )
    tpl_automator: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "TplAutomator",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MasterTrackMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MaximizerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MaximizerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MaximizerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    input_gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputGain",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    transient_release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "TransientRelease",
            "type": "Element",
        },
    )
    long_term_release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LongTermRelease",
            "type": "Element",
        },
    )
    ceiling: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ceiling",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MaximizerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MetaMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MetaMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MetaMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    dest_scaling: Optional[MetaMixerDeviceDestScaling] = field(
        default=None,
        metadata={
            "name": "DestScaling",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    dest_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMin",
            "type": "Element",
        },
    )
    dest_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMax",
            "type": "Element",
        },
    )
    input_a: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputA",
            "type": "Element",
        },
    )
    input_b: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputB",
            "type": "Element",
        },
    )
    input_c: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "InputC",
            "type": "Element",
        },
    )
    weight_a: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WeightA",
            "type": "Element",
        },
    )
    weight_b: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WeightB",
            "type": "Element",
        },
    )
    weight_c: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WeightC",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MetaMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MidiCcdevice:
    class Meta:
        name = "MidiCCDevice"

    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MidiCcdevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MidiCcdevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    controller_value0: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue0",
            "type": "Element",
        },
    )
    controller_number0: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber0",
            "type": "Element",
        },
    )
    controller_name0: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName0",
            "type": "Element",
        },
    )
    controller_value1: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue1",
            "type": "Element",
        },
    )
    controller_number1: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber1",
            "type": "Element",
        },
    )
    controller_name1: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName1",
            "type": "Element",
        },
    )
    controller_value2: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue2",
            "type": "Element",
        },
    )
    controller_number2: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber2",
            "type": "Element",
        },
    )
    controller_name2: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName2",
            "type": "Element",
        },
    )
    controller_value3: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue3",
            "type": "Element",
        },
    )
    controller_number3: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber3",
            "type": "Element",
        },
    )
    controller_name3: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName3",
            "type": "Element",
        },
    )
    controller_value4: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue4",
            "type": "Element",
        },
    )
    controller_number4: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber4",
            "type": "Element",
        },
    )
    controller_name4: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName4",
            "type": "Element",
        },
    )
    controller_value5: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue5",
            "type": "Element",
        },
    )
    controller_number5: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber5",
            "type": "Element",
        },
    )
    controller_name5: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName5",
            "type": "Element",
        },
    )
    controller_value6: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue6",
            "type": "Element",
        },
    )
    controller_number6: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber6",
            "type": "Element",
        },
    )
    controller_name6: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName6",
            "type": "Element",
        },
    )
    controller_value7: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue7",
            "type": "Element",
        },
    )
    controller_number7: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber7",
            "type": "Element",
        },
    )
    controller_name7: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName7",
            "type": "Element",
        },
    )
    controller_value8: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue8",
            "type": "Element",
        },
    )
    controller_number8: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber8",
            "type": "Element",
        },
    )
    controller_name8: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName8",
            "type": "Element",
        },
    )
    controller_value9: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue9",
            "type": "Element",
        },
    )
    controller_number9: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber9",
            "type": "Element",
        },
    )
    controller_name9: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName9",
            "type": "Element",
        },
    )
    controller_value10: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue10",
            "type": "Element",
        },
    )
    controller_number10: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber10",
            "type": "Element",
        },
    )
    controller_name10: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName10",
            "type": "Element",
        },
    )
    controller_value11: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue11",
            "type": "Element",
        },
    )
    controller_number11: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber11",
            "type": "Element",
        },
    )
    controller_name11: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName11",
            "type": "Element",
        },
    )
    controller_value12: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue12",
            "type": "Element",
        },
    )
    controller_number12: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber12",
            "type": "Element",
        },
    )
    controller_name12: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName12",
            "type": "Element",
        },
    )
    controller_value13: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue13",
            "type": "Element",
        },
    )
    controller_number13: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber13",
            "type": "Element",
        },
    )
    controller_name13: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName13",
            "type": "Element",
        },
    )
    linked_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedInstrument",
            "type": "Element",
        },
    )
    visible_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisiblePages",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MidiCCDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MidiControlDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MidiControlDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MidiControlDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    controller_value0: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue0",
            "type": "Element",
        },
    )
    controller_number0: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber0",
            "type": "Element",
        },
    )
    controller_name0: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName0",
            "type": "Element",
        },
    )
    controller_type0: Optional[MidiControlDeviceControllerType0] = field(
        default=None,
        metadata={
            "name": "ControllerType0",
            "type": "Element",
        },
    )
    controller_value1: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue1",
            "type": "Element",
        },
    )
    controller_number1: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber1",
            "type": "Element",
        },
    )
    controller_name1: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName1",
            "type": "Element",
        },
    )
    controller_type1: Optional[MidiControlDeviceControllerType1] = field(
        default=None,
        metadata={
            "name": "ControllerType1",
            "type": "Element",
        },
    )
    controller_value2: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue2",
            "type": "Element",
        },
    )
    controller_number2: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber2",
            "type": "Element",
        },
    )
    controller_name2: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName2",
            "type": "Element",
        },
    )
    controller_type2: Optional[MidiControlDeviceControllerType2] = field(
        default=None,
        metadata={
            "name": "ControllerType2",
            "type": "Element",
        },
    )
    controller_value3: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue3",
            "type": "Element",
        },
    )
    controller_number3: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber3",
            "type": "Element",
        },
    )
    controller_name3: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName3",
            "type": "Element",
        },
    )
    controller_type3: Optional[MidiControlDeviceControllerType3] = field(
        default=None,
        metadata={
            "name": "ControllerType3",
            "type": "Element",
        },
    )
    controller_value4: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue4",
            "type": "Element",
        },
    )
    controller_number4: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber4",
            "type": "Element",
        },
    )
    controller_name4: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName4",
            "type": "Element",
        },
    )
    controller_type4: Optional[MidiControlDeviceControllerType4] = field(
        default=None,
        metadata={
            "name": "ControllerType4",
            "type": "Element",
        },
    )
    controller_value5: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue5",
            "type": "Element",
        },
    )
    controller_number5: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber5",
            "type": "Element",
        },
    )
    controller_name5: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName5",
            "type": "Element",
        },
    )
    controller_type5: Optional[MidiControlDeviceControllerType5] = field(
        default=None,
        metadata={
            "name": "ControllerType5",
            "type": "Element",
        },
    )
    controller_value6: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue6",
            "type": "Element",
        },
    )
    controller_number6: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber6",
            "type": "Element",
        },
    )
    controller_name6: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName6",
            "type": "Element",
        },
    )
    controller_type6: Optional[MidiControlDeviceControllerType6] = field(
        default=None,
        metadata={
            "name": "ControllerType6",
            "type": "Element",
        },
    )
    controller_value7: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue7",
            "type": "Element",
        },
    )
    controller_number7: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber7",
            "type": "Element",
        },
    )
    controller_name7: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName7",
            "type": "Element",
        },
    )
    controller_type7: Optional[MidiControlDeviceControllerType7] = field(
        default=None,
        metadata={
            "name": "ControllerType7",
            "type": "Element",
        },
    )
    controller_value8: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue8",
            "type": "Element",
        },
    )
    controller_number8: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber8",
            "type": "Element",
        },
    )
    controller_name8: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName8",
            "type": "Element",
        },
    )
    controller_type8: Optional[MidiControlDeviceControllerType8] = field(
        default=None,
        metadata={
            "name": "ControllerType8",
            "type": "Element",
        },
    )
    controller_value9: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue9",
            "type": "Element",
        },
    )
    controller_number9: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber9",
            "type": "Element",
        },
    )
    controller_name9: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName9",
            "type": "Element",
        },
    )
    controller_type9: Optional[MidiControlDeviceControllerType9] = field(
        default=None,
        metadata={
            "name": "ControllerType9",
            "type": "Element",
        },
    )
    controller_value10: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue10",
            "type": "Element",
        },
    )
    controller_number10: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber10",
            "type": "Element",
        },
    )
    controller_name10: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName10",
            "type": "Element",
        },
    )
    controller_type10: Optional[MidiControlDeviceControllerType10] = field(
        default=None,
        metadata={
            "name": "ControllerType10",
            "type": "Element",
        },
    )
    controller_value11: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue11",
            "type": "Element",
        },
    )
    controller_number11: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber11",
            "type": "Element",
        },
    )
    controller_name11: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName11",
            "type": "Element",
        },
    )
    controller_type11: Optional[MidiControlDeviceControllerType11] = field(
        default=None,
        metadata={
            "name": "ControllerType11",
            "type": "Element",
        },
    )
    controller_value12: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue12",
            "type": "Element",
        },
    )
    controller_number12: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber12",
            "type": "Element",
        },
    )
    controller_name12: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName12",
            "type": "Element",
        },
    )
    controller_type12: Optional[MidiControlDeviceControllerType12] = field(
        default=None,
        metadata={
            "name": "ControllerType12",
            "type": "Element",
        },
    )
    controller_value13: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue13",
            "type": "Element",
        },
    )
    controller_number13: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber13",
            "type": "Element",
        },
    )
    controller_name13: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName13",
            "type": "Element",
        },
    )
    controller_type13: Optional[MidiControlDeviceControllerType13] = field(
        default=None,
        metadata={
            "name": "ControllerType13",
            "type": "Element",
        },
    )
    controller_value14: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue14",
            "type": "Element",
        },
    )
    controller_number14: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber14",
            "type": "Element",
        },
    )
    controller_name14: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName14",
            "type": "Element",
        },
    )
    controller_type14: Optional[MidiControlDeviceControllerType14] = field(
        default=None,
        metadata={
            "name": "ControllerType14",
            "type": "Element",
        },
    )
    controller_value15: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue15",
            "type": "Element",
        },
    )
    controller_number15: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber15",
            "type": "Element",
        },
    )
    controller_name15: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName15",
            "type": "Element",
        },
    )
    controller_type15: Optional[MidiControlDeviceControllerType15] = field(
        default=None,
        metadata={
            "name": "ControllerType15",
            "type": "Element",
        },
    )
    controller_value16: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue16",
            "type": "Element",
        },
    )
    controller_number16: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber16",
            "type": "Element",
        },
    )
    controller_name16: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName16",
            "type": "Element",
        },
    )
    controller_type16: Optional[MidiControlDeviceControllerType16] = field(
        default=None,
        metadata={
            "name": "ControllerType16",
            "type": "Element",
        },
    )
    controller_value17: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue17",
            "type": "Element",
        },
    )
    controller_number17: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber17",
            "type": "Element",
        },
    )
    controller_name17: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName17",
            "type": "Element",
        },
    )
    controller_type17: Optional[MidiControlDeviceControllerType17] = field(
        default=None,
        metadata={
            "name": "ControllerType17",
            "type": "Element",
        },
    )
    controller_value18: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue18",
            "type": "Element",
        },
    )
    controller_number18: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber18",
            "type": "Element",
        },
    )
    controller_name18: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName18",
            "type": "Element",
        },
    )
    controller_type18: Optional[MidiControlDeviceControllerType18] = field(
        default=None,
        metadata={
            "name": "ControllerType18",
            "type": "Element",
        },
    )
    controller_value19: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue19",
            "type": "Element",
        },
    )
    controller_number19: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber19",
            "type": "Element",
        },
    )
    controller_name19: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName19",
            "type": "Element",
        },
    )
    controller_type19: Optional[MidiControlDeviceControllerType19] = field(
        default=None,
        metadata={
            "name": "ControllerType19",
            "type": "Element",
        },
    )
    controller_value20: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue20",
            "type": "Element",
        },
    )
    controller_number20: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber20",
            "type": "Element",
        },
    )
    controller_name20: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName20",
            "type": "Element",
        },
    )
    controller_type20: Optional[MidiControlDeviceControllerType20] = field(
        default=None,
        metadata={
            "name": "ControllerType20",
            "type": "Element",
        },
    )
    controller_value21: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue21",
            "type": "Element",
        },
    )
    controller_number21: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber21",
            "type": "Element",
        },
    )
    controller_name21: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName21",
            "type": "Element",
        },
    )
    controller_type21: Optional[MidiControlDeviceControllerType21] = field(
        default=None,
        metadata={
            "name": "ControllerType21",
            "type": "Element",
        },
    )
    controller_value22: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue22",
            "type": "Element",
        },
    )
    controller_number22: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber22",
            "type": "Element",
        },
    )
    controller_name22: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName22",
            "type": "Element",
        },
    )
    controller_type22: Optional[MidiControlDeviceControllerType22] = field(
        default=None,
        metadata={
            "name": "ControllerType22",
            "type": "Element",
        },
    )
    controller_value23: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue23",
            "type": "Element",
        },
    )
    controller_number23: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber23",
            "type": "Element",
        },
    )
    controller_name23: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName23",
            "type": "Element",
        },
    )
    controller_type23: Optional[MidiControlDeviceControllerType23] = field(
        default=None,
        metadata={
            "name": "ControllerType23",
            "type": "Element",
        },
    )
    controller_value24: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue24",
            "type": "Element",
        },
    )
    controller_number24: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber24",
            "type": "Element",
        },
    )
    controller_name24: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName24",
            "type": "Element",
        },
    )
    controller_type24: Optional[MidiControlDeviceControllerType24] = field(
        default=None,
        metadata={
            "name": "ControllerType24",
            "type": "Element",
        },
    )
    controller_value25: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue25",
            "type": "Element",
        },
    )
    controller_number25: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber25",
            "type": "Element",
        },
    )
    controller_name25: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName25",
            "type": "Element",
        },
    )
    controller_type25: Optional[MidiControlDeviceControllerType25] = field(
        default=None,
        metadata={
            "name": "ControllerType25",
            "type": "Element",
        },
    )
    controller_value26: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue26",
            "type": "Element",
        },
    )
    controller_number26: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber26",
            "type": "Element",
        },
    )
    controller_name26: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName26",
            "type": "Element",
        },
    )
    controller_type26: Optional[MidiControlDeviceControllerType26] = field(
        default=None,
        metadata={
            "name": "ControllerType26",
            "type": "Element",
        },
    )
    controller_value27: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue27",
            "type": "Element",
        },
    )
    controller_number27: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber27",
            "type": "Element",
        },
    )
    controller_name27: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName27",
            "type": "Element",
        },
    )
    controller_type27: Optional[MidiControlDeviceControllerType27] = field(
        default=None,
        metadata={
            "name": "ControllerType27",
            "type": "Element",
        },
    )
    controller_value28: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue28",
            "type": "Element",
        },
    )
    controller_number28: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber28",
            "type": "Element",
        },
    )
    controller_name28: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName28",
            "type": "Element",
        },
    )
    controller_type28: Optional[MidiControlDeviceControllerType28] = field(
        default=None,
        metadata={
            "name": "ControllerType28",
            "type": "Element",
        },
    )
    controller_value29: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue29",
            "type": "Element",
        },
    )
    controller_number29: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber29",
            "type": "Element",
        },
    )
    controller_name29: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName29",
            "type": "Element",
        },
    )
    controller_type29: Optional[MidiControlDeviceControllerType29] = field(
        default=None,
        metadata={
            "name": "ControllerType29",
            "type": "Element",
        },
    )
    controller_value30: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue30",
            "type": "Element",
        },
    )
    controller_number30: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber30",
            "type": "Element",
        },
    )
    controller_name30: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName30",
            "type": "Element",
        },
    )
    controller_type30: Optional[MidiControlDeviceControllerType30] = field(
        default=None,
        metadata={
            "name": "ControllerType30",
            "type": "Element",
        },
    )
    controller_value31: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue31",
            "type": "Element",
        },
    )
    controller_number31: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber31",
            "type": "Element",
        },
    )
    controller_name31: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName31",
            "type": "Element",
        },
    )
    controller_type31: Optional[MidiControlDeviceControllerType31] = field(
        default=None,
        metadata={
            "name": "ControllerType31",
            "type": "Element",
        },
    )
    controller_value32: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue32",
            "type": "Element",
        },
    )
    controller_number32: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber32",
            "type": "Element",
        },
    )
    controller_name32: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName32",
            "type": "Element",
        },
    )
    controller_type32: Optional[MidiControlDeviceControllerType32] = field(
        default=None,
        metadata={
            "name": "ControllerType32",
            "type": "Element",
        },
    )
    controller_value33: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue33",
            "type": "Element",
        },
    )
    controller_number33: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber33",
            "type": "Element",
        },
    )
    controller_name33: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName33",
            "type": "Element",
        },
    )
    controller_type33: Optional[MidiControlDeviceControllerType33] = field(
        default=None,
        metadata={
            "name": "ControllerType33",
            "type": "Element",
        },
    )
    controller_value34: Optional[MidiControlDeviceFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ControllerValue34",
            "type": "Element",
        },
    )
    controller_number34: Optional[int] = field(
        default=None,
        metadata={
            "name": "ControllerNumber34",
            "type": "Element",
        },
    )
    controller_name34: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControllerName34",
            "type": "Element",
        },
    )
    controller_type34: Optional[MidiControlDeviceControllerType34] = field(
        default=None,
        metadata={
            "name": "ControllerType34",
            "type": "Element",
        },
    )
    linked_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "LinkedInstrument",
            "type": "Element",
        },
    )
    visible_pages: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisiblePages",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MidiControlDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MidiMapper:
    action_mappings: Optional["MidiMapper.ActionMappings"] = field(
        default=None,
        metadata={
            "name": "ActionMappings",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class ActionMappings:
        action_mapping: List[MidiActionMappings] = field(
            default_factory=list,
            metadata={
                "name": "ActionMapping",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class MixerEqDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MixerEqDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MixerEqDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    input_mode: Optional[MixerEqDeviceInputMode] = field(
        default=None,
        metadata={
            "name": "InputMode",
            "type": "Element",
        },
    )
    max_visualized_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "MaxVisualizedGain",
            "type": "Element",
        },
    )
    low_gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LowGain",
            "type": "Element",
        },
    )
    mid_gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MidGain",
            "type": "Element",
        },
    )
    mid_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MidFreq",
            "type": "Element",
        },
    )
    mid_q: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MidQ",
            "type": "Element",
        },
    )
    hi_gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "HiGain",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MixerEqDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class MultitapDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[MultitapDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[MultitapDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panic: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panic",
            "type": "Element",
        },
    )
    visible_tap: Optional[int] = field(
        default=None,
        metadata={
            "name": "VisibleTap",
            "type": "Element",
        },
    )
    visible_panel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisiblePanel",
            "type": "Element",
        },
    )
    mute_dry_signal: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "MuteDrySignal",
            "type": "Element",
        },
    )
    tap1_delay_left: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1DelayLeft",
            "type": "Element",
        },
    )
    tap1_delay_right: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1DelayRight",
            "type": "Element",
        },
    )
    tap1_input_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1InputAmount",
            "type": "Element",
        },
    )
    tap1_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1Amount",
            "type": "Element",
        },
    )
    tap1_lfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LFeedback",
            "type": "Element",
        },
    )
    tap1_rfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1RFeedback",
            "type": "Element",
        },
    )
    tap1_invert_feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1InvertFeedback",
            "type": "Element",
        },
    )
    tap1_previous_tap_input: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1PreviousTapInput",
            "type": "Element",
        },
    )
    tap1_left_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LeftTapPan",
            "type": "Element",
        },
    )
    tap1_right_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1RightTapPan",
            "type": "Element",
        },
    )
    tap1_filter_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1FilterMode",
            "type": "Element",
        },
    )
    tap1_filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1FilterType",
            "type": "Element",
        },
    )
    tap1_filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1FilterFreq",
            "type": "Element",
        },
    )
    tap1_filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1FilterResonance",
            "type": "Element",
        },
    )
    tap1_filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1FilterDrive",
            "type": "Element",
        },
    )
    tap1_line_sync: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LineSync",
            "type": "Element",
        },
    )
    tap1_lset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LSetSyncedDelay",
            "type": "Element",
        },
    )
    tap1_rset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1RSetSyncedDelay",
            "type": "Element",
        },
    )
    tap1_lsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LSyncTime",
            "type": "Element",
        },
    )
    tap1_rsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1RSyncTime",
            "type": "Element",
        },
    )
    tap1_lsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1LSyncOffset",
            "type": "Element",
        },
    )
    tap1_rsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap1RSyncOffset",
            "type": "Element",
        },
    )
    tap2_delay_left: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2DelayLeft",
            "type": "Element",
        },
    )
    tap2_delay_right: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2DelayRight",
            "type": "Element",
        },
    )
    tap2_input_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2InputAmount",
            "type": "Element",
        },
    )
    tap2_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2Amount",
            "type": "Element",
        },
    )
    tap2_lfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LFeedback",
            "type": "Element",
        },
    )
    tap2_rfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2RFeedback",
            "type": "Element",
        },
    )
    tap2_invert_feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2InvertFeedback",
            "type": "Element",
        },
    )
    tap2_previous_tap_input: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2PreviousTapInput",
            "type": "Element",
        },
    )
    tap2_left_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LeftTapPan",
            "type": "Element",
        },
    )
    tap2_right_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2RightTapPan",
            "type": "Element",
        },
    )
    tap2_filter_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2FilterMode",
            "type": "Element",
        },
    )
    tap2_filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2FilterType",
            "type": "Element",
        },
    )
    tap2_filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2FilterFreq",
            "type": "Element",
        },
    )
    tap2_filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2FilterResonance",
            "type": "Element",
        },
    )
    tap2_filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2FilterDrive",
            "type": "Element",
        },
    )
    tap2_line_sync: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LineSync",
            "type": "Element",
        },
    )
    tap2_lset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LSetSyncedDelay",
            "type": "Element",
        },
    )
    tap2_rset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2RSetSyncedDelay",
            "type": "Element",
        },
    )
    tap2_lsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LSyncTime",
            "type": "Element",
        },
    )
    tap2_rsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2RSyncTime",
            "type": "Element",
        },
    )
    tap2_lsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2LSyncOffset",
            "type": "Element",
        },
    )
    tap2_rsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap2RSyncOffset",
            "type": "Element",
        },
    )
    tap3_delay_left: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3DelayLeft",
            "type": "Element",
        },
    )
    tap3_delay_right: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3DelayRight",
            "type": "Element",
        },
    )
    tap3_input_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3InputAmount",
            "type": "Element",
        },
    )
    tap3_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3Amount",
            "type": "Element",
        },
    )
    tap3_lfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LFeedback",
            "type": "Element",
        },
    )
    tap3_rfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3RFeedback",
            "type": "Element",
        },
    )
    tap3_invert_feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3InvertFeedback",
            "type": "Element",
        },
    )
    tap3_previous_tap_input: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3PreviousTapInput",
            "type": "Element",
        },
    )
    tap3_left_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LeftTapPan",
            "type": "Element",
        },
    )
    tap3_right_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3RightTapPan",
            "type": "Element",
        },
    )
    tap3_filter_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3FilterMode",
            "type": "Element",
        },
    )
    tap3_filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3FilterType",
            "type": "Element",
        },
    )
    tap3_filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3FilterFreq",
            "type": "Element",
        },
    )
    tap3_filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3FilterResonance",
            "type": "Element",
        },
    )
    tap3_filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3FilterDrive",
            "type": "Element",
        },
    )
    tap3_line_sync: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LineSync",
            "type": "Element",
        },
    )
    tap3_lset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LSetSyncedDelay",
            "type": "Element",
        },
    )
    tap3_rset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3RSetSyncedDelay",
            "type": "Element",
        },
    )
    tap3_lsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LSyncTime",
            "type": "Element",
        },
    )
    tap3_rsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3RSyncTime",
            "type": "Element",
        },
    )
    tap3_lsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3LSyncOffset",
            "type": "Element",
        },
    )
    tap3_rsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap3RSyncOffset",
            "type": "Element",
        },
    )
    tap4_delay_left: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4DelayLeft",
            "type": "Element",
        },
    )
    tap4_delay_right: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4DelayRight",
            "type": "Element",
        },
    )
    tap4_input_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4InputAmount",
            "type": "Element",
        },
    )
    tap4_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4Amount",
            "type": "Element",
        },
    )
    tap4_lfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LFeedback",
            "type": "Element",
        },
    )
    tap4_rfeedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4RFeedback",
            "type": "Element",
        },
    )
    tap4_invert_feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4InvertFeedback",
            "type": "Element",
        },
    )
    tap4_previous_tap_input: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4PreviousTapInput",
            "type": "Element",
        },
    )
    tap4_left_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LeftTapPan",
            "type": "Element",
        },
    )
    tap4_right_tap_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4RightTapPan",
            "type": "Element",
        },
    )
    tap4_filter_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4FilterMode",
            "type": "Element",
        },
    )
    tap4_filter_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4FilterType",
            "type": "Element",
        },
    )
    tap4_filter_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4FilterFreq",
            "type": "Element",
        },
    )
    tap4_filter_resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4FilterResonance",
            "type": "Element",
        },
    )
    tap4_filter_drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4FilterDrive",
            "type": "Element",
        },
    )
    tap4_line_sync: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LineSync",
            "type": "Element",
        },
    )
    tap4_lset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LSetSyncedDelay",
            "type": "Element",
        },
    )
    tap4_rset_synced_delay: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4RSetSyncedDelay",
            "type": "Element",
        },
    )
    tap4_lsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LSyncTime",
            "type": "Element",
        },
    )
    tap4_rsync_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4RSyncTime",
            "type": "Element",
        },
    )
    tap4_lsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4LSyncOffset",
            "type": "Element",
        },
    )
    tap4_rsync_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Tap4RSyncOffset",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="MultitapDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PatternTrackAutomation:
    envelopes: Optional["PatternTrackAutomation.Envelopes"] = field(
        default=None,
        metadata={
            "name": "Envelopes",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Envelopes:
        envelope: List[PatternTrackEnvelope] = field(
            default_factory=list,
            metadata={
                "name": "Envelope",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PdcTestDelayDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[PdcTestDelayDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[PdcTestDelayDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    delay_in_ms: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DelayInMs",
            "type": "Element",
        },
    )
    report_latency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ReportLatency",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PdcTestDelayDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Phaser2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Phaser2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Phaser2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    floor: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        },
    )
    ceilling: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ceilling",
            "type": "Element",
        },
    )
    rate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    depth: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    dephase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dephase",
            "type": "Element",
        },
    )
    reset: Optional[NonContinuesDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Reset",
            "type": "Element",
        },
    )
    stages: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Stages",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Phaser2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class PhaserDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[PhaserDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[PhaserDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    ceilling: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ceilling",
            "type": "Element",
        },
    )
    floor: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Floor",
            "type": "Element",
        },
    )
    lforate: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LFORate",
            "type": "Element",
        },
    )
    depth: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
        },
    )
    feedback: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Feedback",
            "type": "Element",
        },
    )
    phase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
        },
    )
    stages: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Stages",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PhaserDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RepeaterDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[RepeaterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[RepeaterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
        },
    )
    divisor: Optional[RepeaterDeviceDivisorParameter] = field(
        default=None,
        metadata={
            "name": "Divisor",
            "type": "Element",
        },
    )
    hold: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Hold",
            "type": "Element",
        },
    )
    sync_mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SyncMode",
            "type": "Element",
        },
    )
    midi_trigger0: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger0",
            "type": "Element",
        },
    )
    midi_trigger1: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger1",
            "type": "Element",
        },
    )
    midi_trigger2: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger2",
            "type": "Element",
        },
    )
    midi_trigger3: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger3",
            "type": "Element",
        },
    )
    midi_trigger4: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger4",
            "type": "Element",
        },
    )
    midi_trigger5: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger5",
            "type": "Element",
        },
    )
    midi_trigger6: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger6",
            "type": "Element",
        },
    )
    midi_trigger7: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger7",
            "type": "Element",
        },
    )
    midi_trigger8: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger8",
            "type": "Element",
        },
    )
    midi_trigger9: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger9",
            "type": "Element",
        },
    )
    midi_trigger10: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger10",
            "type": "Element",
        },
    )
    midi_trigger11: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger11",
            "type": "Element",
        },
    )
    midi_trigger12: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger12",
            "type": "Element",
        },
    )
    midi_trigger13: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger13",
            "type": "Element",
        },
    )
    midi_trigger14: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger14",
            "type": "Element",
        },
    )
    midi_trigger15: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger15",
            "type": "Element",
        },
    )
    midi_trigger16: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger16",
            "type": "Element",
        },
    )
    midi_trigger17: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger17",
            "type": "Element",
        },
    )
    midi_trigger18: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger18",
            "type": "Element",
        },
    )
    midi_trigger19: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger19",
            "type": "Element",
        },
    )
    midi_trigger20: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger20",
            "type": "Element",
        },
    )
    midi_trigger21: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger21",
            "type": "Element",
        },
    )
    midi_trigger22: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger22",
            "type": "Element",
        },
    )
    midi_trigger23: Optional[RepeaterMidiTriggerParameter] = field(
        default=None,
        metadata={
            "name": "MidiTrigger23",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="RepeaterDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Reverb2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Reverb2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Reverb2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    quality_setup: Optional[int] = field(
        default=None,
        metadata={
            "name": "QualitySetup",
            "type": "Element",
        },
    )
    reverb_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ReverbTime",
            "type": "Element",
        },
    )
    lpfilter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LPFilter",
            "type": "Element",
        },
    )
    pre_delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PreDelay",
            "type": "Element",
        },
    )
    dry_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryMix",
            "type": "Element",
        },
    )
    send: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Send",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Reverb2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Reverb3Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[Reverb3DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[Reverb3DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    reverb_time: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ReverbTime",
            "type": "Element",
        },
    )
    pre_delay: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PreDelay",
            "type": "Element",
        },
    )
    lpfilter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LPFilter",
            "type": "Element",
        },
    )
    lpgain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LPGain",
            "type": "Element",
        },
    )
    color: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    width: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
        },
    )
    pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Pan",
            "type": "Element",
        },
    )
    wet_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "WetMix",
            "type": "Element",
        },
    )
    dry_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryMix",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="Reverb3Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ReverbDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[ReverbDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[ReverbDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    send: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Send",
            "type": "Element",
        },
    )
    room_size: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "RoomSize",
            "type": "Element",
        },
    )
    width: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
        },
    )
    damp: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Damp",
            "type": "Element",
        },
    )
    dry_mix: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryMix",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="ReverbDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RewireInDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[RewireInDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[RewireInDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "DeviceName",
            "type": "Element",
        },
    )
    channel_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ChannelIndex",
            "type": "Element",
        },
    )
    channel_mode: Optional[RewireInDeviceChannelMode] = field(
        default=None,
        metadata={
            "name": "ChannelMode",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="RewireInDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RingMod2Device:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[RingMod2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[RingMod2DevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oscillator_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "OscillatorType",
            "type": "Element",
        },
    )
    note: Optional[RingMod2NoteFilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Note",
            "type": "Element",
        },
    )
    transpose: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    dry_wet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DryWet",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="RingMod2Device",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RingModDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[RingModDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[RingModDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    oscillator_type: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "OscillatorType",
            "type": "Element",
        },
    )
    frequency: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )
    amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    phase: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
        },
    )
    inertia: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Inertia",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="RingModDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleAhdsrModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleAhdsrModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleAhdsrModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleAhdsrModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleAhdsrModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    attack: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    hold: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Hold",
            "type": "Element",
        },
    )
    decay: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    sustain: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Sustain",
            "type": "Element",
        },
    )
    release: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    attack_scaling: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AttackScaling",
            "type": "Element",
        },
    )
    decay_scaling: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DecayScaling",
            "type": "Element",
        },
    )
    release_scaling: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ReleaseScaling",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleAhdsrModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleAutoAmpModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleAutoAmpModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleAutoAmpModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleAutoAmpModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleAutoAmpModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    attack: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    release: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    amount: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleAutoAmpModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleCompatibilityModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleCompatibilityModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleCompatibilityModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleCompatibilityModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleCompatibilityModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    envelope_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnvelopeIsActive",
            "type": "Element",
        },
    )
    envelope_sustain_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "EnvelopeSustainIsActive",
            "type": "Element",
        },
    )
    envelope_sustain_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "EnvelopeSustainPos",
            "type": "Element",
        },
    )
    envelope_loop_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "EnvelopeLoopStart",
            "type": "Element",
        },
    )
    envelope_loop_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "EnvelopeLoopEnd",
            "type": "Element",
        },
    )
    envelope_loop_mode: Optional[
        SampleCompatibilityModulationDeviceEnvelopeLoopMode
    ] = field(
        default=None,
        metadata={
            "name": "EnvelopeLoopMode",
            "type": "Element",
        },
    )
    envelope_decay: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "EnvelopeDecay",
            "type": "Element",
        },
    )
    envelope_nodes: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "EnvelopeNodes",
            "type": "Element",
        },
    )
    lfo1_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "Lfo1Mode",
            "type": "Element",
        },
    )
    lfo1_dephase: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo1Dephase",
            "type": "Element",
        },
    )
    lfo1_frequency: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo1Frequency",
            "type": "Element",
        },
    )
    lfo1_amplitude: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo1Amplitude",
            "type": "Element",
        },
    )
    lfo2_mode: Optional[int] = field(
        default=None,
        metadata={
            "name": "Lfo2Mode",
            "type": "Element",
        },
    )
    lfo2_dephase: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo2Dephase",
            "type": "Element",
        },
    )
    lfo2_frequency: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo2Frequency",
            "type": "Element",
        },
    )
    lfo2_amplitude: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Lfo2Amplitude",
            "type": "Element",
        },
    )
    auto_amp_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoAmpIsActive",
            "type": "Element",
        },
    )
    auto_amp_attack: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AutoAmpAttack",
            "type": "Element",
        },
    )
    auto_amp_release: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AutoAmpRelease",
            "type": "Element",
        },
    )
    auto_amp_amount: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "AutoAmpAmount",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleCompatibilityModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleEnvelopeModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleEnvelopeModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleEnvelopeModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleEnvelopeModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleEnvelopeModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    sustain_is_active: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SustainIsActive",
            "type": "Element",
        },
    )
    sustain_pos: Optional[int] = field(
        default=None,
        metadata={
            "name": "SustainPos",
            "type": "Element",
        },
    )
    loop_start: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopStart",
            "type": "Element",
        },
    )
    loop_end: Optional[int] = field(
        default=None,
        metadata={
            "name": "LoopEnd",
            "type": "Element",
        },
    )
    loop_mode: Optional[SampleEnvelopeModulationDeviceLoopMode] = field(
        default=None,
        metadata={
            "name": "LoopMode",
            "type": "Element",
        },
    )
    decay: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Decay",
            "type": "Element",
        },
    )
    nodes: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Nodes",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleEnvelopeModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleFaderModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleFaderModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleFaderModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleFaderModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleFaderModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    scaling: Optional[SampleFaderModulationDeviceScaling] = field(
        default=None,
        metadata={
            "name": "Scaling",
            "type": "Element",
        },
    )
    from_value: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
        },
    )
    to: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
        },
    )
    duration: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
        },
    )
    delay: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleFaderModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleKeyTrackingModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleKeyTrackingModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleKeyTrackingModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleKeyTrackingModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleKeyTrackingModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    min: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleKeyTrackingModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleLfoModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleLfoModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleLfoModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleLfoModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleLfoModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    mode: Optional[SampleLfoModulationDeviceMode] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
        },
    )
    frequency: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Frequency",
            "type": "Element",
        },
    )
    amplitude: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Amplitude",
            "type": "Element",
        },
    )
    dephase: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dephase",
            "type": "Element",
        },
    )
    delay: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Delay",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleLfoModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    post_panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostPanning",
            "type": "Element",
        },
    )
    post_volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostVolume",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleMixerModulationDevice:
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    volume: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    pitch: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Pitch",
            "type": "Element",
        },
    )
    pitch_modulation_range: Optional[float] = field(
        default=None,
        metadata={
            "name": "PitchModulationRange",
            "type": "Element",
        },
    )
    cutoff: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Cutoff",
            "type": "Element",
        },
    )
    resonance: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Resonance",
            "type": "Element",
        },
    )
    drive: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Drive",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleMixerModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleOperandModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleOperandModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleOperandModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleOperandModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleOperandModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    value: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleOperandModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleStepperModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleStepperModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleStepperModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleStepperModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleStepperModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    step_amount: Optional[int] = field(
        default=None,
        metadata={
            "name": "StepAmount",
            "type": "Element",
        },
    )
    reset: Optional[SampleModulationDeviceNonContinousParameter] = field(
        default=None,
        metadata={
            "name": "Reset",
            "type": "Element",
        },
    )
    nodes: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Nodes",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleStepperModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SampleVelocityTrackingModulationDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SampleVelocityTrackingModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SampleVelocityTrackingModulationDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    target: Optional[SampleVelocityTrackingModulationDeviceTarget] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
        },
    )
    operator: Optional[SampleVelocityTrackingModulationDeviceOperator] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
        },
    )
    bipolar: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Bipolar",
            "type": "Element",
        },
    )
    tempo_synced: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TempoSynced",
            "type": "Element",
        },
    )
    min: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Min",
            "type": "Element",
        },
    )
    max: Optional[SampleModulationDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Max",
            "type": "Element",
        },
    )
    mode: Optional[SampleVelocityTrackingModulationDeviceMode] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SampleVelocityTrackingModulationDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SendDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SendDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SendDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    send_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SendAmount",
            "type": "Element",
        },
    )
    send_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SendPan",
            "type": "Element",
        },
    )
    dest_send_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestSendTrack",
            "type": "Element",
        },
    )
    mute_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MuteSource",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    apply_post_volume: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ApplyPostVolume",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SendDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SendTrackMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SendTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SendTrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    surround: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Surround",
            "type": "Element",
        },
    )
    post_panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostPanning",
            "type": "Element",
        },
    )
    post_volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostVolume",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SendTrackMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ShaperDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[ShaperDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[ShaperDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    threshold: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Threshold",
            "type": "Element",
        },
    )
    ratio: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Ratio",
            "type": "Element",
        },
    )
    attack: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    gain: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="ShaperDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SideChainDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SideChainDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SideChainDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    mute_source: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MuteSource",
            "type": "Element",
        },
    )
    send_amount: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SendAmount",
            "type": "Element",
        },
    )
    send_pan: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SendPan",
            "type": "Element",
        },
    )
    dest_chain_index: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestChainIndex",
            "type": "Element",
        },
    )
    dest_effect_index: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffectIndex",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SideChainDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SignalFollowerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[SignalFollowerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[SignalFollowerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    dest_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMin",
            "type": "Element",
        },
    )
    dest_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMax",
            "type": "Element",
        },
    )
    dest_offset: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestOffset",
            "type": "Element",
        },
    )
    attack: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Attack",
            "type": "Element",
        },
    )
    release: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Release",
            "type": "Element",
        },
    )
    sensitivity: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Sensitivity",
            "type": "Element",
        },
    )
    dest_scaling: Optional[SignalFollowerDeviceDestScaling] = field(
        default=None,
        metadata={
            "name": "DestScaling",
            "type": "Element",
        },
    )
    lp_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "LpFreq",
            "type": "Element",
        },
    )
    hp_freq: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "HpFreq",
            "type": "Element",
        },
    )
    input_mode: Optional[SignalFollowerDeviceInputMode] = field(
        default=None,
        metadata={
            "name": "InputMode",
            "type": "Element",
        },
    )
    look_ahead: Optional[float] = field(
        default=None,
        metadata={
            "name": "LookAhead",
            "type": "Element",
        },
    )
    listen_to_input: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ListenToInput",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SignalFollowerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StereoExpanderDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[StereoExpanderDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[StereoExpanderDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    mono_mix_mode: Optional[StereoExpanderDeviceMonoMixMode] = field(
        default=None,
        metadata={
            "name": "MonoMixMode",
            "type": "Element",
        },
    )
    stereo_width: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "StereoWidth",
            "type": "Element",
        },
    )
    surround_width: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "SurroundWidth",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="StereoExpanderDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class StutterDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[StutterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[StutterDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    divisor: Optional[StutterDivisorDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Divisor",
            "type": "Element",
        },
    )
    buffer: Optional[StutterBufferDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Buffer",
            "type": "Element",
        },
    )
    wet: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Wet",
            "type": "Element",
        },
    )
    dry: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Dry",
            "type": "Element",
        },
    )
    mode: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="StutterDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TrackMixerDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[TrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[TrackMixerDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Panning",
            "type": "Element",
        },
    )
    volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    surround: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Surround",
            "type": "Element",
        },
    )
    post_panning: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostPanning",
            "type": "Element",
        },
    )
    post_volume: Optional[TrackVolumeDeviceParameter] = field(
        default=None,
        metadata={
            "name": "PostVolume",
            "type": "Element",
        },
    )
    smooth_parameter_changes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SmoothParameterChanges",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="TrackMixerDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class VelocityDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[VelocityDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[VelocityDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    src_instrument: Optional[int] = field(
        default=None,
        metadata={
            "name": "SrcInstrument",
            "type": "Element",
        },
    )
    dest_scaling: Optional[VelocityDeviceDestScaling] = field(
        default=None,
        metadata={
            "name": "DestScaling",
            "type": "Element",
        },
    )
    velocity_min: Optional[int] = field(
        default=None,
        metadata={
            "name": "VelocityMin",
            "type": "Element",
        },
    )
    velocity_max: Optional[int] = field(
        default=None,
        metadata={
            "name": "VelocityMax",
            "type": "Element",
        },
    )
    dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestTrack",
            "type": "Element",
        },
    )
    dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestEffect",
            "type": "Element",
        },
    )
    dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestParameter",
            "type": "Element",
        },
    )
    dest_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMin",
            "type": "Element",
        },
    )
    dest_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "DestMax",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="VelocityDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class XypadDevice:
    class Meta:
        name = "XYPadDevice"

    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[XypadDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[XypadDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    sliders_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SlidersVisible",
            "type": "Element",
        },
    )
    reset_on_release: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ResetOnRelease",
            "type": "Element",
        },
    )
    reset_snap_back_value_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "ResetSnapBackValueX",
            "type": "Element",
        },
    )
    reset_snap_back_value_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "ResetSnapBackValueY",
            "type": "Element",
        },
    )
    value_x: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ValueX",
            "type": "Element",
        },
    )
    value_y: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "ValueY",
            "type": "Element",
        },
    )
    out1_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestTrack",
            "type": "Element",
        },
    )
    out1_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestEffect",
            "type": "Element",
        },
    )
    out1_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1DestParameter",
            "type": "Element",
        },
    )
    out1_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1Min",
            "type": "Element",
        },
    )
    out1_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out1Max",
            "type": "Element",
        },
    )
    out1_scaling: Optional[XypadDeviceOut1Scaling] = field(
        default=None,
        metadata={
            "name": "Out1Scaling",
            "type": "Element",
        },
    )
    out2_dest_track: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestTrack",
            "type": "Element",
        },
    )
    out2_dest_effect: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestEffect",
            "type": "Element",
        },
    )
    out2_dest_parameter: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2DestParameter",
            "type": "Element",
        },
    )
    out2_min: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2Min",
            "type": "Element",
        },
    )
    out2_max: Optional[FilterDeviceParameter] = field(
        default=None,
        metadata={
            "name": "Out2Max",
            "type": "Element",
        },
    )
    out2_scaling: Optional[XypadDeviceOut2Scaling] = field(
        default=None,
        metadata={
            "name": "Out2Scaling",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="XYPadDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DooferFilterDeviceChain:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    devices: Optional["DooferFilterDeviceChain.Devices"] = field(
        default=None,
        metadata={
            "name": "Devices",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Devices:
        analog_filter_device: List[AnalogFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "AnalogFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        audio_plugin_device: List[AudioPluginDevice] = field(
            default_factory=list,
            metadata={
                "name": "AudioPluginDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        bus_compressor_device: List[BusCompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "BusCompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        cabinet_simulator_device: List[CabinetSimulatorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CabinetSimulatorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus2_device: List[Chorus2Device] = field(
            default_factory=list,
            metadata={
                "name": "Chorus2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus_device: List[ChorusDevice] = field(
            default_factory=list,
            metadata={
                "name": "ChorusDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        comb2_device: List[Comb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Comb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        comb_device: List[CombDevice] = field(
            default_factory=list,
            metadata={
                "name": "CombDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        compressor_device: List[CompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        convolver_device: List[ConvolverDevice] = field(
            default_factory=list,
            metadata={
                "name": "ConvolverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        crossover_device: List[CrossoverDevice] = field(
            default_factory=list,
            metadata={
                "name": "CrossoverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        dc_offset_device: List[DcOffsetDevice] = field(
            default_factory=list,
            metadata={
                "name": "DcOffsetDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        delay_device: List[DelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "DelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        digital_filter_device: List[DigitalFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "DigitalFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion2_device: List[Distortion2Device] = field(
            default_factory=list,
            metadata={
                "name": "Distortion2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion_device: List[DistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "DistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        doofer_device: List["DooferDevice"] = field(
            default_factory=list,
            metadata={
                "name": "DooferDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        eq10_device: List[Eq10Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq10Device",
                "type": "Element",
                "sequential": True,
            },
        )
        eq5_device: List[Eq5Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq5Device",
                "type": "Element",
                "sequential": True,
            },
        )
        exciter_device: List[ExciterDevice] = field(
            default_factory=list,
            metadata={
                "name": "ExciterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        filter1_device: List[Filter1Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter1Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter2_device: List[Filter2Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter3_device: List[Filter3Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter_distortion_device: List[FilterDistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "FilterDistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger2_device: List[Flanger2Device] = field(
            default_factory=list,
            metadata={
                "name": "Flanger2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger_device: List[FlangerDevice] = field(
            default_factory=list,
            metadata={
                "name": "FlangerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        formula_meta_device: List[FormulaMetaDevice] = field(
            default_factory=list,
            metadata={
                "name": "FormulaMetaDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gainer_device: List[GainerDevice] = field(
            default_factory=list,
            metadata={
                "name": "GainerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gate2_device: List[Gate2Device] = field(
            default_factory=list,
            metadata={
                "name": "Gate2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        gate_device: List[GateDevice] = field(
            default_factory=list,
            metadata={
                "name": "GateDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        hydra_device: List[HydraDevice] = field(
            default_factory=list,
            metadata={
                "name": "HydraDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_automation_device: List[InstrumentAutomationDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentAutomationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_macro_device: List[InstrumentMacroDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentMacroDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        key_tracking_device: List[KeyTrackingDevice] = field(
            default_factory=list,
            metadata={
                "name": "KeyTrackingDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lfo_device: List[LfoDevice] = field(
            default_factory=list,
            metadata={
                "name": "LfoDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        line_in_device: List[LineInDevice] = field(
            default_factory=list,
            metadata={
                "name": "LineInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi2_device: List[Lofi2Device] = field(
            default_factory=list,
            metadata={
                "name": "Lofi2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi_device: List[LofiDevice] = field(
            default_factory=list,
            metadata={
                "name": "LofiDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        maximizer_device: List[MaximizerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MaximizerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        meta_mixer_device: List[MetaMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MetaMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_ccdevice: List[MidiCcdevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiCCDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_control_device: List[MidiControlDevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiControlDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        mixer_eq_device: List[MixerEqDevice] = field(
            default_factory=list,
            metadata={
                "name": "MixerEqDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        multitap_device: List[MultitapDevice] = field(
            default_factory=list,
            metadata={
                "name": "MultitapDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        pdc_test_delay_device: List[PdcTestDelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "PdcTestDelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser2_device: List[Phaser2Device] = field(
            default_factory=list,
            metadata={
                "name": "Phaser2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser_device: List[PhaserDevice] = field(
            default_factory=list,
            metadata={
                "name": "PhaserDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        repeater_device: List[RepeaterDevice] = field(
            default_factory=list,
            metadata={
                "name": "RepeaterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb2_device: List[Reverb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb3_device: List[Reverb3Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb_device: List[ReverbDevice] = field(
            default_factory=list,
            metadata={
                "name": "ReverbDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        rewire_in_device: List[RewireInDevice] = field(
            default_factory=list,
            metadata={
                "name": "RewireInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod2_device: List[RingMod2Device] = field(
            default_factory=list,
            metadata={
                "name": "RingMod2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod_device: List[RingModDevice] = field(
            default_factory=list,
            metadata={
                "name": "RingModDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        send_device: List[SendDevice] = field(
            default_factory=list,
            metadata={
                "name": "SendDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        shaper_device: List[ShaperDevice] = field(
            default_factory=list,
            metadata={
                "name": "ShaperDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        side_chain_device: List[SideChainDevice] = field(
            default_factory=list,
            metadata={
                "name": "SideChainDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        signal_follower_device: List[SignalFollowerDevice] = field(
            default_factory=list,
            metadata={
                "name": "SignalFollowerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stereo_expander_device: List[StereoExpanderDevice] = field(
            default_factory=list,
            metadata={
                "name": "StereoExpanderDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stutter_device: List[StutterDevice] = field(
            default_factory=list,
            metadata={
                "name": "StutterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        velocity_device: List[VelocityDevice] = field(
            default_factory=list,
            metadata={
                "name": "VelocityDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        xypad_device: List[XypadDevice] = field(
            default_factory=list,
            metadata={
                "name": "XYPadDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class InstrumentPhraseGenerator:
    playback_sync: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlaybackSync",
            "type": "Element",
        },
    )
    playback_mode: Optional[InstrumentPhraseGeneratorPlaybackMode] = field(
        default=None,
        metadata={
            "name": "PlaybackMode",
            "type": "Element",
        },
    )
    selected_phrase_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedPhraseIndex",
            "type": "Element",
        },
    )
    phrases: Optional["InstrumentPhraseGenerator.Phrases"] = field(
        default=None,
        metadata={
            "name": "Phrases",
            "type": "Element",
        },
    )
    phrase_map: Optional[InstrumentPhraseMap] = field(
        default=None,
        metadata={
            "name": "PhraseMap",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Phrases:
        phrase: List[InstrumentPhrase] = field(
            default_factory=list,
            metadata={
                "name": "Phrase",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class InstrumentPluginGenerator:
    channel: Optional[int] = field(
        default=None,
        metadata={
            "name": "Channel",
            "type": "Element",
        },
    )
    transpose: Optional[int] = field(
        default=None,
        metadata={
            "name": "Transpose",
            "type": "Element",
        },
    )
    volume: Optional[float] = field(
        default=None,
        metadata={
            "name": "Volume",
            "type": "Element",
        },
    )
    output_routings: Optional["InstrumentPluginGenerator.OutputRoutings"] = field(
        default=None,
        metadata={
            "name": "OutputRoutings",
            "type": "Element",
        },
    )
    midi_output_routing_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "MidiOutputRoutingIndex",
            "type": "Element",
        },
    )
    auto_suspend: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AutoSuspend",
            "type": "Element",
        },
    )
    alias_instrument_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "AliasInstrumentIndex",
            "type": "Element",
        },
    )
    alias_fx_indices: Optional[str] = field(
        default=None,
        metadata={
            "name": "AliasFxIndices",
            "type": "Element",
        },
    )
    plugin_device: Optional[AudioPluginDevice] = field(
        default=None,
        metadata={
            "name": "PluginDevice",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class OutputRoutings:
        output_routing: List[InstrumentPluginRouting] = field(
            default_factory=list,
            metadata={
                "name": "OutputRouting",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PatternGroupTrack:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    lines: Optional["PatternGroupTrack.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
        },
    )
    alias_pattern_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "AliasPatternIndex",
            "type": "Element",
        },
    )
    color_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ColorEnabled",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    automations: Optional[PatternTrackAutomation] = field(
        default=None,
        metadata={
            "name": "Automations",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PatternGroupTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        line: List[PatternLineNode] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )


@dataclass
class PatternMasterTrack:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    lines: Optional["PatternMasterTrack.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
        },
    )
    alias_pattern_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "AliasPatternIndex",
            "type": "Element",
        },
    )
    color_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ColorEnabled",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    automations: Optional[PatternTrackAutomation] = field(
        default=None,
        metadata={
            "name": "Automations",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PatternMasterTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        line: List[PatternLineNode] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )


@dataclass
class PatternSendTrack:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    lines: Optional["PatternSendTrack.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
        },
    )
    alias_pattern_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "AliasPatternIndex",
            "type": "Element",
        },
    )
    color_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ColorEnabled",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    automations: Optional[PatternTrackAutomation] = field(
        default=None,
        metadata={
            "name": "Automations",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PatternSendTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        line: List[PatternLineNode] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )


@dataclass
class PatternTrack:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    lines: Optional["PatternTrack.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
        },
    )
    alias_pattern_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "AliasPatternIndex",
            "type": "Element",
        },
    )
    color_enabled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ColorEnabled",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    automations: Optional[PatternTrackAutomation] = field(
        default=None,
        metadata={
            "name": "Automations",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="PatternTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Lines:
        line: List[PatternLineNode] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )


@dataclass
class SampleModulationSet:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    devices: Optional["SampleModulationSet.Devices"] = field(
        default=None,
        metadata={
            "name": "Devices",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    filter_type: Optional[int] = field(
        default=None,
        metadata={
            "name": "FilterType",
            "type": "Element",
        },
    )
    filter_bank_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "FilterBankVersion",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Devices:
        sample_ahdsr_modulation_device: List[SampleAhdsrModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleAhdsrModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_auto_amp_modulation_device: List[SampleAutoAmpModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleAutoAmpModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_compatibility_modulation_device: List[
            SampleCompatibilityModulationDevice
        ] = field(
            default_factory=list,
            metadata={
                "name": "SampleCompatibilityModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_envelope_modulation_device: List[SampleEnvelopeModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleEnvelopeModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_fader_modulation_device: List[SampleFaderModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleFaderModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_key_tracking_modulation_device: List[
            SampleKeyTrackingModulationDevice
        ] = field(
            default_factory=list,
            metadata={
                "name": "SampleKeyTrackingModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_lfo_modulation_device: List[SampleLfoModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleLfoModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_mixer_modulation_device: List[SampleMixerModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleMixerModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_operand_modulation_device: List[SampleOperandModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleOperandModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_stepper_modulation_device: List[SampleStepperModulationDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleStepperModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_velocity_tracking_modulation_device: List[
            SampleVelocityTrackingModulationDevice
        ] = field(
            default_factory=list,
            metadata={
                "name": "SampleVelocityTrackingModulationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class DooferDevice:
    custom_device_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "CustomDeviceName",
            "type": "Element",
        },
    )
    is_maximized: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsMaximized",
            "type": "Element",
        },
    )
    is_selected: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSelected",
            "type": "Element",
        },
    )
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    run_time_preset_a: Optional[DooferDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetA",
            "type": "Element",
        },
    )
    run_time_preset_b: Optional[DooferDevicePreset] = field(
        default=None,
        metadata={
            "name": "RunTimePresetB",
            "type": "Element",
        },
    )
    is_active: Optional[FilterDeviceIsActiveParameter] = field(
        default=None,
        metadata={
            "name": "IsActive",
            "type": "Element",
        },
    )
    macro0: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro0",
            "type": "Element",
        },
    )
    macro1: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro1",
            "type": "Element",
        },
    )
    macro2: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro2",
            "type": "Element",
        },
    )
    macro3: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro3",
            "type": "Element",
        },
    )
    macro4: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro4",
            "type": "Element",
        },
    )
    macro5: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro5",
            "type": "Element",
        },
    )
    macro6: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro6",
            "type": "Element",
        },
    )
    macro7: Optional[DooferMacroParameter] = field(
        default=None,
        metadata={
            "name": "Macro7",
            "type": "Element",
        },
    )
    num_active_macros: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumActiveMacros",
            "type": "Element",
        },
    )
    show_devices: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ShowDevices",
            "type": "Element",
        },
    )
    device_chain: Optional[DooferFilterDeviceChain] = field(
        default=None,
        metadata={
            "name": "DeviceChain",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="DooferDevice",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Pattern:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    number_of_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfLines",
            "type": "Element",
        },
    )
    tracks: Optional["Pattern.Tracks"] = field(
        default=None,
        metadata={
            "name": "Tracks",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Tracks:
        pattern_track: List[PatternTrack] = field(
            default_factory=list,
            metadata={
                "name": "PatternTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        pattern_group_track: List[PatternGroupTrack] = field(
            default_factory=list,
            metadata={
                "name": "PatternGroupTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        pattern_master_track: List[PatternMasterTrack] = field(
            default_factory=list,
            metadata={
                "name": "PatternMasterTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        pattern_send_track: List[PatternSendTrack] = field(
            default_factory=list,
            metadata={
                "name": "PatternSendTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class PatternPool:
    highlite_step: Optional[int] = field(
        default=None,
        metadata={
            "name": "HighliteStep",
            "type": "Element",
        },
    )
    default_pattern_length: Optional[int] = field(
        default=None,
        metadata={
            "name": "DefaultPatternLength",
            "type": "Element",
        },
    )
    patterns: Optional["PatternPool.Patterns"] = field(
        default=None,
        metadata={
            "name": "Patterns",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Patterns:
        pattern: List[Pattern] = field(
            default_factory=list,
            metadata={
                "name": "Pattern",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SampleFilterDeviceChain:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    devices: Optional["SampleFilterDeviceChain.Devices"] = field(
        default=None,
        metadata={
            "name": "Devices",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    routing_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RoutingIndex",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Devices:
        analog_filter_device: List[AnalogFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "AnalogFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        audio_plugin_device: List[AudioPluginDevice] = field(
            default_factory=list,
            metadata={
                "name": "AudioPluginDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        bus_compressor_device: List[BusCompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "BusCompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        cabinet_simulator_device: List[CabinetSimulatorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CabinetSimulatorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus2_device: List[Chorus2Device] = field(
            default_factory=list,
            metadata={
                "name": "Chorus2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus_device: List[ChorusDevice] = field(
            default_factory=list,
            metadata={
                "name": "ChorusDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        comb2_device: List[Comb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Comb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        comb_device: List[CombDevice] = field(
            default_factory=list,
            metadata={
                "name": "CombDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        compressor_device: List[CompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        convolver_device: List[ConvolverDevice] = field(
            default_factory=list,
            metadata={
                "name": "ConvolverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        crossover_device: List[CrossoverDevice] = field(
            default_factory=list,
            metadata={
                "name": "CrossoverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        dc_offset_device: List[DcOffsetDevice] = field(
            default_factory=list,
            metadata={
                "name": "DcOffsetDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        delay_device: List[DelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "DelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        digital_filter_device: List[DigitalFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "DigitalFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion2_device: List[Distortion2Device] = field(
            default_factory=list,
            metadata={
                "name": "Distortion2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion_device: List[DistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "DistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        doofer_device: List[DooferDevice] = field(
            default_factory=list,
            metadata={
                "name": "DooferDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        eq10_device: List[Eq10Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq10Device",
                "type": "Element",
                "sequential": True,
            },
        )
        eq5_device: List[Eq5Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq5Device",
                "type": "Element",
                "sequential": True,
            },
        )
        exciter_device: List[ExciterDevice] = field(
            default_factory=list,
            metadata={
                "name": "ExciterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        filter1_device: List[Filter1Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter1Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter2_device: List[Filter2Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter3_device: List[Filter3Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter_distortion_device: List[FilterDistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "FilterDistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger2_device: List[Flanger2Device] = field(
            default_factory=list,
            metadata={
                "name": "Flanger2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger_device: List[FlangerDevice] = field(
            default_factory=list,
            metadata={
                "name": "FlangerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        formula_meta_device: List[FormulaMetaDevice] = field(
            default_factory=list,
            metadata={
                "name": "FormulaMetaDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gainer_device: List[GainerDevice] = field(
            default_factory=list,
            metadata={
                "name": "GainerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gate2_device: List[Gate2Device] = field(
            default_factory=list,
            metadata={
                "name": "Gate2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        gate_device: List[GateDevice] = field(
            default_factory=list,
            metadata={
                "name": "GateDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        hydra_device: List[HydraDevice] = field(
            default_factory=list,
            metadata={
                "name": "HydraDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_automation_device: List[InstrumentAutomationDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentAutomationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_macro_device: List[InstrumentMacroDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentMacroDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        key_tracking_device: List[KeyTrackingDevice] = field(
            default_factory=list,
            metadata={
                "name": "KeyTrackingDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lfo_device: List[LfoDevice] = field(
            default_factory=list,
            metadata={
                "name": "LfoDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        line_in_device: List[LineInDevice] = field(
            default_factory=list,
            metadata={
                "name": "LineInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi2_device: List[Lofi2Device] = field(
            default_factory=list,
            metadata={
                "name": "Lofi2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi_device: List[LofiDevice] = field(
            default_factory=list,
            metadata={
                "name": "LofiDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        maximizer_device: List[MaximizerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MaximizerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        meta_mixer_device: List[MetaMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MetaMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_ccdevice: List[MidiCcdevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiCCDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_control_device: List[MidiControlDevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiControlDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        mixer_eq_device: List[MixerEqDevice] = field(
            default_factory=list,
            metadata={
                "name": "MixerEqDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        multitap_device: List[MultitapDevice] = field(
            default_factory=list,
            metadata={
                "name": "MultitapDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        pdc_test_delay_device: List[PdcTestDelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "PdcTestDelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser2_device: List[Phaser2Device] = field(
            default_factory=list,
            metadata={
                "name": "Phaser2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser_device: List[PhaserDevice] = field(
            default_factory=list,
            metadata={
                "name": "PhaserDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        repeater_device: List[RepeaterDevice] = field(
            default_factory=list,
            metadata={
                "name": "RepeaterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb2_device: List[Reverb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb3_device: List[Reverb3Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb_device: List[ReverbDevice] = field(
            default_factory=list,
            metadata={
                "name": "ReverbDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        rewire_in_device: List[RewireInDevice] = field(
            default_factory=list,
            metadata={
                "name": "RewireInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod2_device: List[RingMod2Device] = field(
            default_factory=list,
            metadata={
                "name": "RingMod2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod_device: List[RingModDevice] = field(
            default_factory=list,
            metadata={
                "name": "RingModDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        sample_mixer_device: List[SampleMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "SampleMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        send_device: List[SendDevice] = field(
            default_factory=list,
            metadata={
                "name": "SendDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        shaper_device: List[ShaperDevice] = field(
            default_factory=list,
            metadata={
                "name": "ShaperDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        side_chain_device: List[SideChainDevice] = field(
            default_factory=list,
            metadata={
                "name": "SideChainDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        signal_follower_device: List[SignalFollowerDevice] = field(
            default_factory=list,
            metadata={
                "name": "SignalFollowerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stereo_expander_device: List[StereoExpanderDevice] = field(
            default_factory=list,
            metadata={
                "name": "StereoExpanderDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stutter_device: List[StutterDevice] = field(
            default_factory=list,
            metadata={
                "name": "StutterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        velocity_device: List[VelocityDevice] = field(
            default_factory=list,
            metadata={
                "name": "VelocityDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        xypad_device: List[XypadDevice] = field(
            default_factory=list,
            metadata={
                "name": "XYPadDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class TrackFilterDeviceChain:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    devices: Optional["TrackFilterDeviceChain.Devices"] = field(
        default=None,
        metadata={
            "name": "Devices",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Devices:
        analog_filter_device: List[AnalogFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "AnalogFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        audio_plugin_device: List[AudioPluginDevice] = field(
            default_factory=list,
            metadata={
                "name": "AudioPluginDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        bus_compressor_device: List[BusCompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "BusCompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        cabinet_simulator_device: List[CabinetSimulatorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CabinetSimulatorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus2_device: List[Chorus2Device] = field(
            default_factory=list,
            metadata={
                "name": "Chorus2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        chorus_device: List[ChorusDevice] = field(
            default_factory=list,
            metadata={
                "name": "ChorusDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        comb2_device: List[Comb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Comb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        comb_device: List[CombDevice] = field(
            default_factory=list,
            metadata={
                "name": "CombDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        compressor_device: List[CompressorDevice] = field(
            default_factory=list,
            metadata={
                "name": "CompressorDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        convolver_device: List[ConvolverDevice] = field(
            default_factory=list,
            metadata={
                "name": "ConvolverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        crossover_device: List[CrossoverDevice] = field(
            default_factory=list,
            metadata={
                "name": "CrossoverDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        dc_offset_device: List[DcOffsetDevice] = field(
            default_factory=list,
            metadata={
                "name": "DcOffsetDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        delay_device: List[DelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "DelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        digital_filter_device: List[DigitalFilterDevice] = field(
            default_factory=list,
            metadata={
                "name": "DigitalFilterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion2_device: List[Distortion2Device] = field(
            default_factory=list,
            metadata={
                "name": "Distortion2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        distortion_device: List[DistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "DistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        doofer_device: List[DooferDevice] = field(
            default_factory=list,
            metadata={
                "name": "DooferDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        eq10_device: List[Eq10Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq10Device",
                "type": "Element",
                "sequential": True,
            },
        )
        eq5_device: List[Eq5Device] = field(
            default_factory=list,
            metadata={
                "name": "Eq5Device",
                "type": "Element",
                "sequential": True,
            },
        )
        exciter_device: List[ExciterDevice] = field(
            default_factory=list,
            metadata={
                "name": "ExciterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        filter1_device: List[Filter1Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter1Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter2_device: List[Filter2Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter3_device: List[Filter3Device] = field(
            default_factory=list,
            metadata={
                "name": "Filter3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        filter_distortion_device: List[FilterDistortionDevice] = field(
            default_factory=list,
            metadata={
                "name": "FilterDistortionDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger2_device: List[Flanger2Device] = field(
            default_factory=list,
            metadata={
                "name": "Flanger2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        flanger_device: List[FlangerDevice] = field(
            default_factory=list,
            metadata={
                "name": "FlangerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        formula_meta_device: List[FormulaMetaDevice] = field(
            default_factory=list,
            metadata={
                "name": "FormulaMetaDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gainer_device: List[GainerDevice] = field(
            default_factory=list,
            metadata={
                "name": "GainerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        gate2_device: List[Gate2Device] = field(
            default_factory=list,
            metadata={
                "name": "Gate2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        gate_device: List[GateDevice] = field(
            default_factory=list,
            metadata={
                "name": "GateDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        group_track_mixer_device: List[GroupTrackMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "GroupTrackMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        hydra_device: List[HydraDevice] = field(
            default_factory=list,
            metadata={
                "name": "HydraDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_automation_device: List[InstrumentAutomationDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentAutomationDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        instrument_macro_device: List[InstrumentMacroDevice] = field(
            default_factory=list,
            metadata={
                "name": "InstrumentMacroDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        key_tracking_device: List[KeyTrackingDevice] = field(
            default_factory=list,
            metadata={
                "name": "KeyTrackingDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lfo_device: List[LfoDevice] = field(
            default_factory=list,
            metadata={
                "name": "LfoDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        line_in_device: List[LineInDevice] = field(
            default_factory=list,
            metadata={
                "name": "LineInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi2_device: List[Lofi2Device] = field(
            default_factory=list,
            metadata={
                "name": "Lofi2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        lofi_device: List[LofiDevice] = field(
            default_factory=list,
            metadata={
                "name": "LofiDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        master_track_mixer_device: List[MasterTrackMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MasterTrackMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        maximizer_device: List[MaximizerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MaximizerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        meta_mixer_device: List[MetaMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "MetaMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_ccdevice: List[MidiCcdevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiCCDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        midi_control_device: List[MidiControlDevice] = field(
            default_factory=list,
            metadata={
                "name": "MidiControlDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        mixer_eq_device: List[MixerEqDevice] = field(
            default_factory=list,
            metadata={
                "name": "MixerEqDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        multitap_device: List[MultitapDevice] = field(
            default_factory=list,
            metadata={
                "name": "MultitapDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        pdc_test_delay_device: List[PdcTestDelayDevice] = field(
            default_factory=list,
            metadata={
                "name": "PdcTestDelayDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser2_device: List[Phaser2Device] = field(
            default_factory=list,
            metadata={
                "name": "Phaser2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        phaser_device: List[PhaserDevice] = field(
            default_factory=list,
            metadata={
                "name": "PhaserDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        repeater_device: List[RepeaterDevice] = field(
            default_factory=list,
            metadata={
                "name": "RepeaterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb2_device: List[Reverb2Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb3_device: List[Reverb3Device] = field(
            default_factory=list,
            metadata={
                "name": "Reverb3Device",
                "type": "Element",
                "sequential": True,
            },
        )
        reverb_device: List[ReverbDevice] = field(
            default_factory=list,
            metadata={
                "name": "ReverbDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        rewire_in_device: List[RewireInDevice] = field(
            default_factory=list,
            metadata={
                "name": "RewireInDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod2_device: List[RingMod2Device] = field(
            default_factory=list,
            metadata={
                "name": "RingMod2Device",
                "type": "Element",
                "sequential": True,
            },
        )
        ring_mod_device: List[RingModDevice] = field(
            default_factory=list,
            metadata={
                "name": "RingModDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        send_device: List[SendDevice] = field(
            default_factory=list,
            metadata={
                "name": "SendDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        send_track_mixer_device: List[SendTrackMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "SendTrackMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        shaper_device: List[ShaperDevice] = field(
            default_factory=list,
            metadata={
                "name": "ShaperDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        side_chain_device: List[SideChainDevice] = field(
            default_factory=list,
            metadata={
                "name": "SideChainDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        signal_follower_device: List[SignalFollowerDevice] = field(
            default_factory=list,
            metadata={
                "name": "SignalFollowerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stereo_expander_device: List[StereoExpanderDevice] = field(
            default_factory=list,
            metadata={
                "name": "StereoExpanderDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        stutter_device: List[StutterDevice] = field(
            default_factory=list,
            metadata={
                "name": "StutterDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        track_mixer_device: List[TrackMixerDevice] = field(
            default_factory=list,
            metadata={
                "name": "TrackMixerDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        velocity_device: List[VelocityDevice] = field(
            default_factory=list,
            metadata={
                "name": "VelocityDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        xypad_device: List[XypadDevice] = field(
            default_factory=list,
            metadata={
                "name": "XYPadDevice",
                "type": "Element",
                "sequential": True,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class InstrumentSampleGenerator:
    samples: Optional["InstrumentSampleGenerator.Samples"] = field(
        default=None,
        metadata={
            "name": "Samples",
            "type": "Element",
        },
    )
    selected_sample_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedSampleIndex",
            "type": "Element",
        },
    )
    modulation_sets: Optional["InstrumentSampleGenerator.ModulationSets"] = field(
        default=None,
        metadata={
            "name": "ModulationSets",
            "type": "Element",
        },
    )
    selected_modulation_set_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedModulationSetIndex",
            "type": "Element",
        },
    )
    device_chains: Optional["InstrumentSampleGenerator.DeviceChains"] = field(
        default=None,
        metadata={
            "name": "DeviceChains",
            "type": "Element",
        },
    )
    selected_device_chain_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedDeviceChainIndex",
            "type": "Element",
        },
    )
    keyzone_overlapping_mode: Optional[
        InstrumentSampleGeneratorKeyzoneOverlappingMode
    ] = field(
        default=None,
        metadata={
            "name": "KeyzoneOverlappingMode",
            "type": "Element",
        },
    )
    split_map: Optional[SampleSplitMap] = field(
        default=None,
        metadata={
            "name": "SplitMap",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class Samples:
        sample: List[Sample] = field(
            default_factory=list,
            metadata={
                "name": "Sample",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class ModulationSets:
        modulation_set: List[SampleModulationSet] = field(
            default_factory=list,
            metadata={
                "name": "ModulationSet",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class DeviceChains:
        device_chain: List[SampleFilterDeviceChain] = field(
            default_factory=list,
            metadata={
                "name": "DeviceChain",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


@dataclass
class SequencerGroupTrack:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color_blend: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlend",
            "type": "Element",
        },
    )
    state: Optional[SequencerGroupTrackState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
        },
    )
    soloed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Soloed",
            "type": "Element",
        },
    )
    note_column_states: Optional["SequencerGroupTrack.NoteColumnStates"] = field(
        default=None,
        metadata={
            "name": "NoteColumnStates",
            "type": "Element",
        },
    )
    note_column_names: Optional["SequencerGroupTrack.NoteColumnNames"] = field(
        default=None,
        metadata={
            "name": "NoteColumnNames",
            "type": "Element",
        },
    )
    number_of_visible_note_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleNoteColumns",
            "type": "Element",
        },
    )
    number_of_visible_effect_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleEffectColumns",
            "type": "Element",
        },
    )
    volume_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolumeColumnIsVisible",
            "type": "Element",
        },
    )
    panning_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanningColumnIsVisible",
            "type": "Element",
        },
    )
    delay_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelayColumnIsVisible",
            "type": "Element",
        },
    )
    sample_effect_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleEffectColumnIsVisible",
            "type": "Element",
        },
    )
    track_routing: Optional[int] = field(
        default=None,
        metadata={
            "name": "TrackRouting",
            "type": "Element",
        },
    )
    group_nesting_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroupNestingLevel",
            "type": "Element",
        },
    )
    track_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "TrackDelay",
            "type": "Element",
        },
    )
    collapsed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Collapsed",
            "type": "Element",
        },
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
        },
    )
    filter_devices: Optional[TrackFilterDeviceChain] = field(
        default=None,
        metadata={
            "name": "FilterDevices",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SequencerGroupTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class NoteColumnStates:
        note_column_state: List[NoteColumnStatesNoteColumnState1] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnState",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnNames:
        note_column_name: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnName",
                "type": "Element",
            },
        )


@dataclass
class SequencerMasterTrack:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color_blend: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlend",
            "type": "Element",
        },
    )
    state: Optional[SequencerMasterTrackState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
        },
    )
    soloed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Soloed",
            "type": "Element",
        },
    )
    note_column_states: Optional["SequencerMasterTrack.NoteColumnStates"] = field(
        default=None,
        metadata={
            "name": "NoteColumnStates",
            "type": "Element",
        },
    )
    note_column_names: Optional["SequencerMasterTrack.NoteColumnNames"] = field(
        default=None,
        metadata={
            "name": "NoteColumnNames",
            "type": "Element",
        },
    )
    number_of_visible_note_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleNoteColumns",
            "type": "Element",
        },
    )
    number_of_visible_effect_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleEffectColumns",
            "type": "Element",
        },
    )
    volume_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolumeColumnIsVisible",
            "type": "Element",
        },
    )
    panning_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanningColumnIsVisible",
            "type": "Element",
        },
    )
    delay_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelayColumnIsVisible",
            "type": "Element",
        },
    )
    sample_effect_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleEffectColumnIsVisible",
            "type": "Element",
        },
    )
    track_routing: Optional[int] = field(
        default=None,
        metadata={
            "name": "TrackRouting",
            "type": "Element",
        },
    )
    group_nesting_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroupNestingLevel",
            "type": "Element",
        },
    )
    track_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "TrackDelay",
            "type": "Element",
        },
    )
    collapsed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Collapsed",
            "type": "Element",
        },
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
        },
    )
    filter_devices: Optional[TrackFilterDeviceChain] = field(
        default=None,
        metadata={
            "name": "FilterDevices",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SequencerMasterTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class NoteColumnStates:
        note_column_state: List[NoteColumnStatesNoteColumnState1] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnState",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnNames:
        note_column_name: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnName",
                "type": "Element",
            },
        )


@dataclass
class SequencerSendTrack:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color_blend: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlend",
            "type": "Element",
        },
    )
    state: Optional[SequencerSendTrackState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
        },
    )
    soloed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Soloed",
            "type": "Element",
        },
    )
    note_column_states: Optional["SequencerSendTrack.NoteColumnStates"] = field(
        default=None,
        metadata={
            "name": "NoteColumnStates",
            "type": "Element",
        },
    )
    note_column_names: Optional["SequencerSendTrack.NoteColumnNames"] = field(
        default=None,
        metadata={
            "name": "NoteColumnNames",
            "type": "Element",
        },
    )
    number_of_visible_note_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleNoteColumns",
            "type": "Element",
        },
    )
    number_of_visible_effect_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleEffectColumns",
            "type": "Element",
        },
    )
    volume_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolumeColumnIsVisible",
            "type": "Element",
        },
    )
    panning_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanningColumnIsVisible",
            "type": "Element",
        },
    )
    delay_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelayColumnIsVisible",
            "type": "Element",
        },
    )
    sample_effect_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleEffectColumnIsVisible",
            "type": "Element",
        },
    )
    track_routing: Optional[int] = field(
        default=None,
        metadata={
            "name": "TrackRouting",
            "type": "Element",
        },
    )
    group_nesting_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroupNestingLevel",
            "type": "Element",
        },
    )
    track_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "TrackDelay",
            "type": "Element",
        },
    )
    collapsed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Collapsed",
            "type": "Element",
        },
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
        },
    )
    filter_devices: Optional[TrackFilterDeviceChain] = field(
        default=None,
        metadata={
            "name": "FilterDevices",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SequencerSendTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class NoteColumnStates:
        note_column_state: List[NoteColumnStatesNoteColumnState1] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnState",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnNames:
        note_column_name: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnName",
                "type": "Element",
            },
        )


@dataclass
class SequencerTrack:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    color: Optional[str] = field(
        default=None,
        metadata={
            "name": "Color",
            "type": "Element",
        },
    )
    color_blend: Optional[float] = field(
        default=None,
        metadata={
            "name": "ColorBlend",
            "type": "Element",
        },
    )
    state: Optional[SequencerTrackState] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
        },
    )
    soloed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Soloed",
            "type": "Element",
        },
    )
    note_column_states: Optional["SequencerTrack.NoteColumnStates"] = field(
        default=None,
        metadata={
            "name": "NoteColumnStates",
            "type": "Element",
        },
    )
    note_column_names: Optional["SequencerTrack.NoteColumnNames"] = field(
        default=None,
        metadata={
            "name": "NoteColumnNames",
            "type": "Element",
        },
    )
    number_of_visible_note_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleNoteColumns",
            "type": "Element",
        },
    )
    number_of_visible_effect_columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfVisibleEffectColumns",
            "type": "Element",
        },
    )
    volume_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VolumeColumnIsVisible",
            "type": "Element",
        },
    )
    panning_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PanningColumnIsVisible",
            "type": "Element",
        },
    )
    delay_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DelayColumnIsVisible",
            "type": "Element",
        },
    )
    sample_effect_column_is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SampleEffectColumnIsVisible",
            "type": "Element",
        },
    )
    track_routing: Optional[int] = field(
        default=None,
        metadata={
            "name": "TrackRouting",
            "type": "Element",
        },
    )
    group_nesting_level: Optional[int] = field(
        default=None,
        metadata={
            "name": "GroupNestingLevel",
            "type": "Element",
        },
    )
    track_delay: Optional[float] = field(
        default=None,
        metadata={
            "name": "TrackDelay",
            "type": "Element",
        },
    )
    collapsed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Collapsed",
            "type": "Element",
        },
    )
    visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Visible",
            "type": "Element",
        },
    )
    filter_devices: Optional[TrackFilterDeviceChain] = field(
        default=None,
        metadata={
            "name": "FilterDevices",
            "type": "Element",
        },
    )
    type: str = field(
        init=False,
        default="SequencerTrack",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class NoteColumnStates:
        note_column_state: List[NoteColumnStatesNoteColumnState1] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnState",
                "type": "Element",
            },
        )

    @dataclass
    class NoteColumnNames:
        note_column_name: List[str] = field(
            default_factory=list,
            metadata={
                "name": "NoteColumnName",
                "type": "Element",
            },
        )


@dataclass
class RenoiseInstrument:
    selected_preset_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetName",
            "type": "Element",
        },
    )
    selected_preset_library: Optional[str] = field(
        default=None,
        metadata={
            "name": "SelectedPresetLibrary",
            "type": "Element",
        },
    )
    selected_preset_is_modified: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SelectedPresetIsModified",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    copy_into_new_sample_name_counter: Optional[int] = field(
        default=None,
        metadata={
            "name": "CopyIntoNewSampleNameCounter",
            "type": "Element",
        },
    )
    copy_into_new_instrument_name_counter: Optional[int] = field(
        default=None,
        metadata={
            "name": "CopyIntoNewInstrumentNameCounter",
            "type": "Element",
        },
    )
    global_properties: Optional[InstrumentGlobalProperties] = field(
        default=None,
        metadata={
            "name": "GlobalProperties",
            "type": "Element",
        },
    )
    midi_input_properties: Optional[InstrumentMidiInputProperties] = field(
        default=None,
        metadata={
            "name": "MidiInputProperties",
            "type": "Element",
        },
    )
    phrase_generator: Optional[InstrumentPhraseGenerator] = field(
        default=None,
        metadata={
            "name": "PhraseGenerator",
            "type": "Element",
        },
    )
    sample_generator: Optional[InstrumentSampleGenerator] = field(
        default=None,
        metadata={
            "name": "SampleGenerator",
            "type": "Element",
        },
    )
    plugin_generator: Optional[InstrumentPluginGenerator] = field(
        default=None,
        metadata={
            "name": "PluginGenerator",
            "type": "Element",
        },
    )
    midi_generator: Optional[InstrumentMidiGenerator] = field(
        default=None,
        metadata={
            "name": "MidiGenerator",
            "type": "Element",
        },
    )
    active_generator_tab: Optional[RenoiseInstrumentActiveGeneratorTab] = field(
        default=None,
        metadata={
            "name": "ActiveGeneratorTab",
            "type": "Element",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class RenoiseSong:
    global_song_data: Optional[GlobalSongData] = field(
        default=None,
        metadata={
            "name": "GlobalSongData",
            "type": "Element",
        },
    )
    scripting_tool_data: Optional["RenoiseSong.ScriptingToolData"] = field(
        default=None,
        metadata={
            "name": "ScriptingToolData",
            "type": "Element",
        },
    )
    record_manager: Optional[RecordManager] = field(
        default=None,
        metadata={
            "name": "RecordManager",
            "type": "Element",
        },
    )
    midi_mapper: Optional[MidiMapper] = field(
        default=None,
        metadata={
            "name": "MidiMapper",
            "type": "Element",
        },
    )
    osc_mapper: Optional[OscMapper] = field(
        default=None,
        metadata={
            "name": "OscMapper",
            "type": "Element",
        },
    )
    instruments: Optional["RenoiseSong.Instruments"] = field(
        default=None,
        metadata={
            "name": "Instruments",
            "type": "Element",
        },
    )
    selected_instrument_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedInstrumentIndex",
            "type": "Element",
        },
    )
    midi_input_routing: Optional[MidiInputRoutingTable] = field(
        default=None,
        metadata={
            "name": "MidiInputRouting",
            "type": "Element",
        },
    )
    tracks: Optional["RenoiseSong.Tracks"] = field(
        default=None,
        metadata={
            "name": "Tracks",
            "type": "Element",
        },
    )
    selected_track_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "SelectedTrackIndex",
            "type": "Element",
        },
    )
    spectrum_track_display_a: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpectrumTrackDisplayA",
            "type": "Element",
        },
    )
    spectrum_track_display_b: Optional[int] = field(
        default=None,
        metadata={
            "name": "SpectrumTrackDisplayB",
            "type": "Element",
        },
    )
    pattern_pool: Optional[PatternPool] = field(
        default=None,
        metadata={
            "name": "PatternPool",
            "type": "Element",
        },
    )
    pattern_sequence: Optional[PatternSequence] = field(
        default=None,
        metadata={
            "name": "PatternSequence",
            "type": "Element",
        },
    )
    last_soloed_out_mode: Optional[RenoiseSongLastSoloedOutMode] = field(
        default=None,
        metadata={
            "name": "LastSoloedOutMode",
            "type": "Element",
        },
    )
    doc_version: int = field(
        init=False,
        default=65,
        metadata={
            "type": "Attribute",
        },
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass
    class ScriptingToolData:
        scripting_tool_data_item: List[RenoiseSongScriptingToolData] = field(
            default_factory=list,
            metadata={
                "name": "ScriptingToolDataItem",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Instruments:
        instrument: List[RenoiseInstrument] = field(
            default_factory=list,
            metadata={
                "name": "Instrument",
                "type": "Element",
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )

    @dataclass
    class Tracks:
        sequencer_track: List[SequencerTrack] = field(
            default_factory=list,
            metadata={
                "name": "SequencerTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        sequencer_group_track: List[SequencerGroupTrack] = field(
            default_factory=list,
            metadata={
                "name": "SequencerGroupTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        sequencer_master_track: List[SequencerMasterTrack] = field(
            default_factory=list,
            metadata={
                "name": "SequencerMasterTrack",
                "type": "Element",
                "sequential": False,
            },
        )
        sequencer_send_track: List[SequencerSendTrack] = field(
            default_factory=list,
            metadata={
                "name": "SequencerSendTrack",
                "type": "Element",
                "sequential": True,
            },
        )
        type: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
