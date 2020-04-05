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

class InteractionEventTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class InteractionEventType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "InteractionEventTypeEnum.InteractionEventType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls
        ) -> typing___List["InteractionEventTypeEnum.InteractionEventType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "InteractionEventTypeEnum.InteractionEventType"
            ]
        ]: ...
        UNSPECIFIED = typing___cast("InteractionEventTypeEnum.InteractionEventType", 0)
        UNKNOWN = typing___cast("InteractionEventTypeEnum.InteractionEventType", 1)
        CLICK = typing___cast("InteractionEventTypeEnum.InteractionEventType", 2)
        ENGAGEMENT = typing___cast("InteractionEventTypeEnum.InteractionEventType", 3)
        VIDEO_VIEW = typing___cast("InteractionEventTypeEnum.InteractionEventType", 4)
        NONE = typing___cast("InteractionEventTypeEnum.InteractionEventType", 5)
    UNSPECIFIED = typing___cast("InteractionEventTypeEnum.InteractionEventType", 0)
    UNKNOWN = typing___cast("InteractionEventTypeEnum.InteractionEventType", 1)
    CLICK = typing___cast("InteractionEventTypeEnum.InteractionEventType", 2)
    ENGAGEMENT = typing___cast("InteractionEventTypeEnum.InteractionEventType", 3)
    VIDEO_VIEW = typing___cast("InteractionEventTypeEnum.InteractionEventType", 4)
    NONE = typing___cast("InteractionEventTypeEnum.InteractionEventType", 5)
    global___InteractionEventType = InteractionEventType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InteractionEventTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> InteractionEventTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___InteractionEventTypeEnum = InteractionEventTypeEnum
