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

class SitelinkPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class SitelinkPlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 0
        )
        UNKNOWN = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 1
        )
        TEXT = typing___cast("SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 2)
        LINE_1 = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 3
        )
        LINE_2 = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 4
        )
        FINAL_URLS = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 5
        )
        FINAL_MOBILE_URLS = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 6
        )
        TRACKING_URL = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 7
        )
        FINAL_URL_SUFFIX = typing___cast(
            "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 8
        )
    UNSPECIFIED = typing___cast(
        "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 0
    )
    UNKNOWN = typing___cast("SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 1)
    TEXT = typing___cast("SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 2)
    LINE_1 = typing___cast("SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 3)
    LINE_2 = typing___cast("SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 4)
    FINAL_URLS = typing___cast(
        "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 5
    )
    FINAL_MOBILE_URLS = typing___cast(
        "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 6
    )
    TRACKING_URL = typing___cast(
        "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 7
    )
    FINAL_URL_SUFFIX = typing___cast(
        "SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField", 8
    )
    global___SitelinkPlaceholderField = SitelinkPlaceholderField
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SitelinkPlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> SitelinkPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___SitelinkPlaceholderFieldEnum = SitelinkPlaceholderFieldEnum