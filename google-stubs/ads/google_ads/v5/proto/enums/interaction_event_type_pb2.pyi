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

class InteractionEventTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    InteractionEventTypeValue = typing___NewType(
        "InteractionEventTypeValue", builtin___int
    )
    type___InteractionEventTypeValue = InteractionEventTypeValue
    InteractionEventType: _InteractionEventType
    class _InteractionEventType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            InteractionEventTypeEnum.InteractionEventTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            InteractionEventTypeEnum.InteractionEventTypeValue, 0
        )
        UNKNOWN = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 1)
        CLICK = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 2)
        ENGAGEMENT = typing___cast(
            InteractionEventTypeEnum.InteractionEventTypeValue, 3
        )
        VIDEO_VIEW = typing___cast(
            InteractionEventTypeEnum.InteractionEventTypeValue, 4
        )
        NONE = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 5)
    UNSPECIFIED = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 0)
    UNKNOWN = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 1)
    CLICK = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 2)
    ENGAGEMENT = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 3)
    VIDEO_VIEW = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 4)
    NONE = typing___cast(InteractionEventTypeEnum.InteractionEventTypeValue, 5)
    type___InteractionEventType = InteractionEventType
    def __init__(self,) -> None: ...

type___InteractionEventTypeEnum = InteractionEventTypeEnum