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

class ContentLabelTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ContentLabelType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "ContentLabelTypeEnum.ContentLabelType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["ContentLabelTypeEnum.ContentLabelType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "ContentLabelTypeEnum.ContentLabelType"]
        ]: ...
        UNSPECIFIED = typing___cast("ContentLabelTypeEnum.ContentLabelType", 0)
        UNKNOWN = typing___cast("ContentLabelTypeEnum.ContentLabelType", 1)
        SEXUALLY_SUGGESTIVE = typing___cast("ContentLabelTypeEnum.ContentLabelType", 2)
        BELOW_THE_FOLD = typing___cast("ContentLabelTypeEnum.ContentLabelType", 3)
        PARKED_DOMAIN = typing___cast("ContentLabelTypeEnum.ContentLabelType", 4)
        GAME = typing___cast("ContentLabelTypeEnum.ContentLabelType", 5)
        JUVENILE = typing___cast("ContentLabelTypeEnum.ContentLabelType", 6)
        PROFANITY = typing___cast("ContentLabelTypeEnum.ContentLabelType", 7)
        TRAGEDY = typing___cast("ContentLabelTypeEnum.ContentLabelType", 8)
        VIDEO = typing___cast("ContentLabelTypeEnum.ContentLabelType", 9)
        VIDEO_RATING_DV_G = typing___cast("ContentLabelTypeEnum.ContentLabelType", 10)
        VIDEO_RATING_DV_PG = typing___cast("ContentLabelTypeEnum.ContentLabelType", 11)
        VIDEO_RATING_DV_T = typing___cast("ContentLabelTypeEnum.ContentLabelType", 12)
        VIDEO_RATING_DV_MA = typing___cast("ContentLabelTypeEnum.ContentLabelType", 13)
        VIDEO_NOT_YET_RATED = typing___cast("ContentLabelTypeEnum.ContentLabelType", 14)
        EMBEDDED_VIDEO = typing___cast("ContentLabelTypeEnum.ContentLabelType", 15)
        LIVE_STREAMING_VIDEO = typing___cast(
            "ContentLabelTypeEnum.ContentLabelType", 16
        )
        SOCIAL_ISSUES = typing___cast("ContentLabelTypeEnum.ContentLabelType", 17)
    UNSPECIFIED = typing___cast("ContentLabelTypeEnum.ContentLabelType", 0)
    UNKNOWN = typing___cast("ContentLabelTypeEnum.ContentLabelType", 1)
    SEXUALLY_SUGGESTIVE = typing___cast("ContentLabelTypeEnum.ContentLabelType", 2)
    BELOW_THE_FOLD = typing___cast("ContentLabelTypeEnum.ContentLabelType", 3)
    PARKED_DOMAIN = typing___cast("ContentLabelTypeEnum.ContentLabelType", 4)
    GAME = typing___cast("ContentLabelTypeEnum.ContentLabelType", 5)
    JUVENILE = typing___cast("ContentLabelTypeEnum.ContentLabelType", 6)
    PROFANITY = typing___cast("ContentLabelTypeEnum.ContentLabelType", 7)
    TRAGEDY = typing___cast("ContentLabelTypeEnum.ContentLabelType", 8)
    VIDEO = typing___cast("ContentLabelTypeEnum.ContentLabelType", 9)
    VIDEO_RATING_DV_G = typing___cast("ContentLabelTypeEnum.ContentLabelType", 10)
    VIDEO_RATING_DV_PG = typing___cast("ContentLabelTypeEnum.ContentLabelType", 11)
    VIDEO_RATING_DV_T = typing___cast("ContentLabelTypeEnum.ContentLabelType", 12)
    VIDEO_RATING_DV_MA = typing___cast("ContentLabelTypeEnum.ContentLabelType", 13)
    VIDEO_NOT_YET_RATED = typing___cast("ContentLabelTypeEnum.ContentLabelType", 14)
    EMBEDDED_VIDEO = typing___cast("ContentLabelTypeEnum.ContentLabelType", 15)
    LIVE_STREAMING_VIDEO = typing___cast("ContentLabelTypeEnum.ContentLabelType", 16)
    SOCIAL_ISSUES = typing___cast("ContentLabelTypeEnum.ContentLabelType", 17)
    global___ContentLabelType = ContentLabelType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ContentLabelTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ContentLabelTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ContentLabelTypeEnum = ContentLabelTypeEnum
