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

class FeedAttributeTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedAttributeTypeValue = typing___NewType("FeedAttributeTypeValue", builtin___int)
    type___FeedAttributeTypeValue = FeedAttributeTypeValue
    FeedAttributeType: _FeedAttributeType
    class _FeedAttributeType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedAttributeTypeEnum.FeedAttributeTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 0)
        UNKNOWN = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 1)
        INT64 = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 2)
        DOUBLE = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 3)
        STRING = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 4)
        BOOLEAN = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 5)
        URL = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 6)
        DATE_TIME = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 7)
        INT64_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 8)
        DOUBLE_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 9)
        STRING_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 10)
        BOOLEAN_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 11)
        URL_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 12)
        DATE_TIME_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 13)
        PRICE = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 14)
    UNSPECIFIED = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 0)
    UNKNOWN = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 1)
    INT64 = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 2)
    DOUBLE = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 3)
    STRING = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 4)
    BOOLEAN = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 5)
    URL = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 6)
    DATE_TIME = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 7)
    INT64_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 8)
    DOUBLE_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 9)
    STRING_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 10)
    BOOLEAN_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 11)
    URL_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 12)
    DATE_TIME_LIST = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 13)
    PRICE = typing___cast(FeedAttributeTypeEnum.FeedAttributeTypeValue, 14)
    type___FeedAttributeType = FeedAttributeType
    def __init__(self,) -> None: ...

type___FeedAttributeTypeEnum = FeedAttributeTypeEnum
