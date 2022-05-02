import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ConversionActionCategoryEnum(proto.Message):
    class ConversionActionCategory(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        DEFAULT: int
        PAGE_VIEW: int
        PURCHASE: int
        SIGNUP: int
        DOWNLOAD: int
        ADD_TO_CART: int
        BEGIN_CHECKOUT: int
        SUBSCRIBE_PAID: int
        PHONE_CALL_LEAD: int
        IMPORTED_LEAD: int
        SUBMIT_LEAD_FORM: int
        BOOK_APPOINTMENT: int
        REQUEST_QUOTE: int
        GET_DIRECTIONS: int
        OUTBOUND_CLICK: int
        CONTACT: int
        ENGAGEMENT: int
        STORE_VISIT: int
        STORE_SALE: int
        QUALIFIED_LEAD: int
        CONVERTED_LEAD: int
