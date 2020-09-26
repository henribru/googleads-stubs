# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class HotelPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    HotelPlaceholderFieldValue = typing___NewType(
        "HotelPlaceholderFieldValue", builtin___int
    )
    type___HotelPlaceholderFieldValue = HotelPlaceholderFieldValue
    HotelPlaceholderField: _HotelPlaceholderField
    class _HotelPlaceholderField(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 0
        )
        UNKNOWN = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 1)
        PROPERTY_ID = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 2
        )
        PROPERTY_NAME = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 3
        )
        DESTINATION_NAME = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 4
        )
        DESCRIPTION = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 5
        )
        ADDRESS = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 6)
        PRICE = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 7)
        FORMATTED_PRICE = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 8
        )
        SALE_PRICE = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 9
        )
        FORMATTED_SALE_PRICE = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 10
        )
        IMAGE_URL = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 11
        )
        CATEGORY = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 12
        )
        STAR_RATING = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 13
        )
        CONTEXTUAL_KEYWORDS = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 14
        )
        FINAL_URLS = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 15
        )
        FINAL_MOBILE_URLS = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 16
        )
        TRACKING_URL = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 17
        )
        ANDROID_APP_LINK = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 18
        )
        SIMILAR_PROPERTY_IDS = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 19
        )
        IOS_APP_LINK = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 20
        )
        IOS_APP_STORE_ID = typing___cast(
            HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 21
        )
    UNSPECIFIED = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 0)
    UNKNOWN = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 1)
    PROPERTY_ID = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 2)
    PROPERTY_NAME = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 3
    )
    DESTINATION_NAME = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 4
    )
    DESCRIPTION = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 5)
    ADDRESS = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 6)
    PRICE = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 7)
    FORMATTED_PRICE = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 8
    )
    SALE_PRICE = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 9)
    FORMATTED_SALE_PRICE = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 10
    )
    IMAGE_URL = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 11)
    CATEGORY = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 12)
    STAR_RATING = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 13
    )
    CONTEXTUAL_KEYWORDS = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 14
    )
    FINAL_URLS = typing___cast(HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 15)
    FINAL_MOBILE_URLS = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 16
    )
    TRACKING_URL = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 17
    )
    ANDROID_APP_LINK = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 18
    )
    SIMILAR_PROPERTY_IDS = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 19
    )
    IOS_APP_LINK = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 20
    )
    IOS_APP_STORE_ID = typing___cast(
        HotelPlaceholderFieldEnum.HotelPlaceholderFieldValue, 21
    )
    type___HotelPlaceholderField = HotelPlaceholderField
    def __init__(self,) -> None: ...

type___HotelPlaceholderFieldEnum = HotelPlaceholderFieldEnum
