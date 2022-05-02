import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class UserListSizeRangeEnum(proto.Message):
    class UserListSizeRange(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        LESS_THAN_FIVE_HUNDRED: int
        LESS_THAN_ONE_THOUSAND: int
        ONE_THOUSAND_TO_TEN_THOUSAND: int
        TEN_THOUSAND_TO_FIFTY_THOUSAND: int
        FIFTY_THOUSAND_TO_ONE_HUNDRED_THOUSAND: int
        ONE_HUNDRED_THOUSAND_TO_THREE_HUNDRED_THOUSAND: int
        THREE_HUNDRED_THOUSAND_TO_FIVE_HUNDRED_THOUSAND: int
        FIVE_HUNDRED_THOUSAND_TO_ONE_MILLION: int
        ONE_MILLION_TO_TWO_MILLION: int
        TWO_MILLION_TO_THREE_MILLION: int
        THREE_MILLION_TO_FIVE_MILLION: int
        FIVE_MILLION_TO_TEN_MILLION: int
        TEN_MILLION_TO_TWENTY_MILLION: int
        TWENTY_MILLION_TO_THIRTY_MILLION: int
        THIRTY_MILLION_TO_FIFTY_MILLION: int
        OVER_FIFTY_MILLION: int
