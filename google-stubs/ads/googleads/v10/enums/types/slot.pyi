import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class SlotEnum(proto.Message):
    class Slot(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        SEARCH_SIDE: int
        SEARCH_TOP: int
        SEARCH_OTHER: int
        CONTENT: int
        SEARCH_PARTNER_TOP: int
        SEARCH_PARTNER_OTHER: int
        MIXED: int
