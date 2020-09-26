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

class DistanceBucketEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    DistanceBucketValue = typing___NewType("DistanceBucketValue", builtin___int)
    type___DistanceBucketValue = DistanceBucketValue
    DistanceBucket: _DistanceBucket
    class _DistanceBucket(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            DistanceBucketEnum.DistanceBucketValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(DistanceBucketEnum.DistanceBucketValue, 0)
        UNKNOWN = typing___cast(DistanceBucketEnum.DistanceBucketValue, 1)
        WITHIN_700M = typing___cast(DistanceBucketEnum.DistanceBucketValue, 2)
        WITHIN_1KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 3)
        WITHIN_5KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 4)
        WITHIN_10KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 5)
        WITHIN_15KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 6)
        WITHIN_20KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 7)
        WITHIN_25KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 8)
        WITHIN_30KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 9)
        WITHIN_35KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 10)
        WITHIN_40KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 11)
        WITHIN_45KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 12)
        WITHIN_50KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 13)
        WITHIN_55KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 14)
        WITHIN_60KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 15)
        WITHIN_65KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 16)
        BEYOND_65KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 17)
        WITHIN_0_7MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 18)
        WITHIN_1MILE = typing___cast(DistanceBucketEnum.DistanceBucketValue, 19)
        WITHIN_5MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 20)
        WITHIN_10MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 21)
        WITHIN_15MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 22)
        WITHIN_20MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 23)
        WITHIN_25MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 24)
        WITHIN_30MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 25)
        WITHIN_35MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 26)
        WITHIN_40MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 27)
        BEYOND_40MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 28)
    UNSPECIFIED = typing___cast(DistanceBucketEnum.DistanceBucketValue, 0)
    UNKNOWN = typing___cast(DistanceBucketEnum.DistanceBucketValue, 1)
    WITHIN_700M = typing___cast(DistanceBucketEnum.DistanceBucketValue, 2)
    WITHIN_1KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 3)
    WITHIN_5KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 4)
    WITHIN_10KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 5)
    WITHIN_15KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 6)
    WITHIN_20KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 7)
    WITHIN_25KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 8)
    WITHIN_30KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 9)
    WITHIN_35KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 10)
    WITHIN_40KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 11)
    WITHIN_45KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 12)
    WITHIN_50KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 13)
    WITHIN_55KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 14)
    WITHIN_60KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 15)
    WITHIN_65KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 16)
    BEYOND_65KM = typing___cast(DistanceBucketEnum.DistanceBucketValue, 17)
    WITHIN_0_7MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 18)
    WITHIN_1MILE = typing___cast(DistanceBucketEnum.DistanceBucketValue, 19)
    WITHIN_5MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 20)
    WITHIN_10MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 21)
    WITHIN_15MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 22)
    WITHIN_20MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 23)
    WITHIN_25MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 24)
    WITHIN_30MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 25)
    WITHIN_35MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 26)
    WITHIN_40MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 27)
    BEYOND_40MILES = typing___cast(DistanceBucketEnum.DistanceBucketValue, 28)
    type___DistanceBucket = DistanceBucket
    def __init__(self,) -> None: ...

type___DistanceBucketEnum = DistanceBucketEnum
