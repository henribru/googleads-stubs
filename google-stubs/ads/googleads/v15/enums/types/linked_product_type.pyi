from typing import Any

import proto

class LinkedProductTypeEnum(proto.Message):
    class LinkedProductType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DATA_PARTNER = 2
        GOOGLE_ADS = 3
        HOTEL_CENTER = 7
        MERCHANT_CENTER = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...