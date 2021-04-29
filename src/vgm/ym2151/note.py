from vgm.ym2151.config import ChannelConfig


class Note:
    def __init__(self, config_id: int, channel_config: ChannelConfig) -> None:
        self.config_id: int = config_id
        self.octave: int = channel_config.octave
        self.note: int = channel_config.note
        self.key_fraction: int = channel_config.key_fraction
