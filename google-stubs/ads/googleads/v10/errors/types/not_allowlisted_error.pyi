import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class NotAllowlistedErrorEnum(proto.Message):
    class NotAllowlistedError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE: int
