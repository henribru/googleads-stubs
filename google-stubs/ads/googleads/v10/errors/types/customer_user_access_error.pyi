import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class CustomerUserAccessErrorEnum(proto.Message):
    class CustomerUserAccessError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        INVALID_USER_ID: int
        REMOVAL_DISALLOWED: int
        DISALLOWED_ACCESS_ROLE: int
        LAST_ADMIN_USER_OF_SERVING_CUSTOMER: int
        LAST_ADMIN_USER_OF_MANAGER: int
