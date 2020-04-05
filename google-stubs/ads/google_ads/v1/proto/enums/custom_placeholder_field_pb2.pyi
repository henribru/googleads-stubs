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

class CustomPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CustomPlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "CustomPlaceholderFieldEnum.CustomPlaceholderField": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls
        ) -> typing___List["CustomPlaceholderFieldEnum.CustomPlaceholderField"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "CustomPlaceholderFieldEnum.CustomPlaceholderField"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 0
        )
        UNKNOWN = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 1)
        ID = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 2)
        ID2 = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 3)
        ITEM_TITLE = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 4
        )
        ITEM_SUBTITLE = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 5
        )
        ITEM_DESCRIPTION = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 6
        )
        ITEM_ADDRESS = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 7
        )
        PRICE = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 8)
        FORMATTED_PRICE = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 9
        )
        SALE_PRICE = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 10
        )
        FORMATTED_SALE_PRICE = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 11
        )
        IMAGE_URL = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 12
        )
        ITEM_CATEGORY = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 13
        )
        FINAL_URLS = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 14
        )
        FINAL_MOBILE_URLS = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 15
        )
        TRACKING_URL = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 16
        )
        CONTEXTUAL_KEYWORDS = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 17
        )
        ANDROID_APP_LINK = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 18
        )
        SIMILAR_IDS = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 19
        )
        IOS_APP_LINK = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 20
        )
        IOS_APP_STORE_ID = typing___cast(
            "CustomPlaceholderFieldEnum.CustomPlaceholderField", 21
        )
    UNSPECIFIED = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 0)
    UNKNOWN = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 1)
    ID = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 2)
    ID2 = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 3)
    ITEM_TITLE = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 4)
    ITEM_SUBTITLE = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 5
    )
    ITEM_DESCRIPTION = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 6
    )
    ITEM_ADDRESS = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 7)
    PRICE = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 8)
    FORMATTED_PRICE = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 9
    )
    SALE_PRICE = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 10)
    FORMATTED_SALE_PRICE = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 11
    )
    IMAGE_URL = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 12)
    ITEM_CATEGORY = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 13
    )
    FINAL_URLS = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 14)
    FINAL_MOBILE_URLS = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 15
    )
    TRACKING_URL = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 16
    )
    CONTEXTUAL_KEYWORDS = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 17
    )
    ANDROID_APP_LINK = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 18
    )
    SIMILAR_IDS = typing___cast("CustomPlaceholderFieldEnum.CustomPlaceholderField", 19)
    IOS_APP_LINK = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 20
    )
    IOS_APP_STORE_ID = typing___cast(
        "CustomPlaceholderFieldEnum.CustomPlaceholderField", 21
    )
    global___CustomPlaceholderField = CustomPlaceholderField
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CustomPlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___CustomPlaceholderFieldEnum = CustomPlaceholderFieldEnum
