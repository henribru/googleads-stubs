# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ContentLabelTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ContentLabelTypeValue = typing___NewType("ContentLabelTypeValue", builtin___int)
    type___ContentLabelTypeValue = ContentLabelTypeValue
    ContentLabelType: _ContentLabelType
    class _ContentLabelType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ContentLabelTypeEnum.ContentLabelTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 0)
        UNKNOWN = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 1)
        SEXUALLY_SUGGESTIVE = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 2
        )
        BELOW_THE_FOLD = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 3)
        PARKED_DOMAIN = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 4)
        JUVENILE = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 6)
        PROFANITY = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 7)
        TRAGEDY = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 8)
        VIDEO = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 9)
        VIDEO_RATING_DV_G = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 10
        )
        VIDEO_RATING_DV_PG = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 11
        )
        VIDEO_RATING_DV_T = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 12
        )
        VIDEO_RATING_DV_MA = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 13
        )
        VIDEO_NOT_YET_RATED = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 14
        )
        EMBEDDED_VIDEO = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 15)
        LIVE_STREAMING_VIDEO = typing___cast(
            ContentLabelTypeEnum.ContentLabelTypeValue, 16
        )
        SOCIAL_ISSUES = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 17)
    UNSPECIFIED = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 0)
    UNKNOWN = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 1)
    SEXUALLY_SUGGESTIVE = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 2)
    BELOW_THE_FOLD = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 3)
    PARKED_DOMAIN = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 4)
    JUVENILE = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 6)
    PROFANITY = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 7)
    TRAGEDY = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 8)
    VIDEO = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 9)
    VIDEO_RATING_DV_G = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 10)
    VIDEO_RATING_DV_PG = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 11)
    VIDEO_RATING_DV_T = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 12)
    VIDEO_RATING_DV_MA = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 13)
    VIDEO_NOT_YET_RATED = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 14)
    EMBEDDED_VIDEO = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 15)
    LIVE_STREAMING_VIDEO = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 16)
    SOCIAL_ISSUES = typing___cast(ContentLabelTypeEnum.ContentLabelTypeValue, 17)
    type___ContentLabelType = ContentLabelType
    def __init__(self,) -> None: ...

type___ContentLabelTypeEnum = ContentLabelTypeEnum