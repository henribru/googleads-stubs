import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionOriginEnum(proto.Message):
    class ConversionOrigin(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        WEBSITE: int
        GOOGLE_HOSTED: int
        APP: int
        CALL_FROM_ADS: int
        STORE: int
        YOUTUBE_HOSTED: int
