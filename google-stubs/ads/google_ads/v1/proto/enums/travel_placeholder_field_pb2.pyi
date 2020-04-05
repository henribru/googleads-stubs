# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class TravelPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TravelPlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "TravelPlaceholderFieldEnum.TravelPlaceholderField": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["TravelPlaceholderFieldEnum.TravelPlaceholderField"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "TravelPlaceholderFieldEnum.TravelPlaceholderField"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 0
        )
        UNKNOWN = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 1)
        DESTINATION_ID = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 2
        )
        ORIGIN_ID = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 3
        )
        TITLE = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 4)
        DESTINATION_NAME = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 5
        )
        ORIGIN_NAME = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 6
        )
        PRICE = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 7)
        FORMATTED_PRICE = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 8
        )
        SALE_PRICE = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 9
        )
        FORMATTED_SALE_PRICE = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 10
        )
        IMAGE_URL = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 11
        )
        CATEGORY = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 12
        )
        CONTEXTUAL_KEYWORDS = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 13
        )
        DESTINATION_ADDRESS = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 14
        )
        FINAL_URL = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 15
        )
        FINAL_MOBILE_URLS = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 16
        )
        TRACKING_URL = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 17
        )
        ANDROID_APP_LINK = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 18
        )
        SIMILAR_DESTINATION_IDS = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 19
        )
        IOS_APP_LINK = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 20
        )
        IOS_APP_STORE_ID = typing___cast(
            "TravelPlaceholderFieldEnum.TravelPlaceholderField", 21
        )
    UNSPECIFIED = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 0)
    UNKNOWN = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 1)
    DESTINATION_ID = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 2
    )
    ORIGIN_ID = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 3)
    TITLE = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 4)
    DESTINATION_NAME = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 5
    )
    ORIGIN_NAME = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 6)
    PRICE = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 7)
    FORMATTED_PRICE = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 8
    )
    SALE_PRICE = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 9)
    FORMATTED_SALE_PRICE = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 10
    )
    IMAGE_URL = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 11)
    CATEGORY = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 12)
    CONTEXTUAL_KEYWORDS = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 13
    )
    DESTINATION_ADDRESS = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 14
    )
    FINAL_URL = typing___cast("TravelPlaceholderFieldEnum.TravelPlaceholderField", 15)
    FINAL_MOBILE_URLS = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 16
    )
    TRACKING_URL = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 17
    )
    ANDROID_APP_LINK = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 18
    )
    SIMILAR_DESTINATION_IDS = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 19
    )
    IOS_APP_LINK = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 20
    )
    IOS_APP_STORE_ID = typing___cast(
        "TravelPlaceholderFieldEnum.TravelPlaceholderField", 21
    )
    global___TravelPlaceholderField = TravelPlaceholderField
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TravelPlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TravelPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___TravelPlaceholderFieldEnum = TravelPlaceholderFieldEnum
