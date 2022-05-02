import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class FeedItemSetErrorEnum(proto.Message):
    class FeedItemSetError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        FEED_ITEM_SET_REMOVED: int
        CANNOT_CLEAR_DYNAMIC_FILTER: int
        CANNOT_CREATE_DYNAMIC_FILTER: int
        INVALID_FEED_TYPE: int
        DUPLICATE_NAME: int
        WRONG_DYNAMIC_FILTER_FOR_FEED_TYPE: int
        DYNAMIC_FILTER_INVALID_CHAIN_IDS: int
