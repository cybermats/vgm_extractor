import gzip
import zipfile

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.serializers.writers import XmlEventWriter

from xrns.parts.song import Song
from xrns.xrns_serializer import XrnsSerializer


def writer(xrnsfile, song):

    xrns = XrnsSerializer()
    xml_song = xrns.render(song)

    config = SerializerConfig(pretty_print=True, encoding="UTF-8", xml_version="1.0")
    serializer = XmlSerializer(config=config)  # , writer=XmlEventWriter)

    rendered = serializer.render(xml_song)

    with zipfile.ZipFile(xrnsfile, mode="w") as zf:
        zf.writestr("Song.xml", rendered)
