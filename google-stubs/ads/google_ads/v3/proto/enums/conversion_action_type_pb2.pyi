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

class ConversionActionTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ConversionActionType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "ConversionActionTypeEnum.ConversionActionType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["ConversionActionTypeEnum.ConversionActionType"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "ConversionActionTypeEnum.ConversionActionType"
            ]
        ]: ...
        UNSPECIFIED = typing___cast("ConversionActionTypeEnum.ConversionActionType", 0)
        UNKNOWN = typing___cast("ConversionActionTypeEnum.ConversionActionType", 1)
        AD_CALL = typing___cast("ConversionActionTypeEnum.ConversionActionType", 2)
        CLICK_TO_CALL = typing___cast(
            "ConversionActionTypeEnum.ConversionActionType", 3
        )
        GOOGLE_PLAY_DOWNLOAD = typing___cast(
            "ConversionActionTypeEnum.ConversionActionType", 4
        )
        GOOGLE_PLAY_IN_APP_PURCHASE = typing___cast(
            "ConversionActionTypeEnum.ConversionActionType", 5
        )
        UPLOAD_CALLS = typing___cast("ConversionActionTypeEnum.ConversionActionType", 6)
        UPLOAD_CLICKS = typing___cast(
            "ConversionActionTypeEnum.ConversionActionType", 7
        )
        WEBPAGE = typing___cast("ConversionActionTypeEnum.ConversionActionType", 8)
        WEBSITE_CALL = typing___cast("ConversionActionTypeEnum.ConversionActionType", 9)
    UNSPECIFIED = typing___cast("ConversionActionTypeEnum.ConversionActionType", 0)
    UNKNOWN = typing___cast("ConversionActionTypeEnum.ConversionActionType", 1)
    AD_CALL = typing___cast("ConversionActionTypeEnum.ConversionActionType", 2)
    CLICK_TO_CALL = typing___cast("ConversionActionTypeEnum.ConversionActionType", 3)
    GOOGLE_PLAY_DOWNLOAD = typing___cast(
        "ConversionActionTypeEnum.ConversionActionType", 4
    )
    GOOGLE_PLAY_IN_APP_PURCHASE = typing___cast(
        "ConversionActionTypeEnum.ConversionActionType", 5
    )
    UPLOAD_CALLS = typing___cast("ConversionActionTypeEnum.ConversionActionType", 6)
    UPLOAD_CLICKS = typing___cast("ConversionActionTypeEnum.ConversionActionType", 7)
    WEBPAGE = typing___cast("ConversionActionTypeEnum.ConversionActionType", 8)
    WEBSITE_CALL = typing___cast("ConversionActionTypeEnum.ConversionActionType", 9)
    global___ConversionActionType = ConversionActionType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ConversionActionTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ConversionActionTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ConversionActionTypeEnum = ConversionActionTypeEnum