from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

_M = TypeVar("_M")

class HotelPlaceholderFieldEnum(proto.Message):
    class HotelPlaceholderField(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        PROPERTY_ID = 2
        PROPERTY_NAME = 3
        DESTINATION_NAME = 4
        DESCRIPTION = 5
        ADDRESS = 6
        PRICE = 7
        FORMATTED_PRICE = 8
        SALE_PRICE = 9
        FORMATTED_SALE_PRICE = 10
        IMAGE_URL = 11
        CATEGORY = 12
        STAR_RATING = 13
        CONTEXTUAL_KEYWORDS = 14
        FINAL_URLS = 15
        FINAL_MOBILE_URLS = 16
        TRACKING_URL = 17
        ANDROID_APP_LINK = 18
        SIMILAR_PROPERTY_IDS = 19
        IOS_APP_LINK = 20
        IOS_APP_STORE_ID = 21
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
