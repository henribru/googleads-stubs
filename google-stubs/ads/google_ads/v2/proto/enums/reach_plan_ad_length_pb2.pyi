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

class ReachPlanAdLengthEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ReachPlanAdLength(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "ReachPlanAdLengthEnum.ReachPlanAdLength": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["ReachPlanAdLengthEnum.ReachPlanAdLength"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "ReachPlanAdLengthEnum.ReachPlanAdLength"]
        ]: ...
        UNSPECIFIED = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 0)
        UNKNOWN = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 1)
        SIX_SECONDS = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 2)
        FIFTEEN_OR_TWENTY_SECONDS = typing___cast(
            "ReachPlanAdLengthEnum.ReachPlanAdLength", 3
        )
        TWENTY_SECONDS_OR_MORE = typing___cast(
            "ReachPlanAdLengthEnum.ReachPlanAdLength", 4
        )
    UNSPECIFIED = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 0)
    UNKNOWN = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 1)
    SIX_SECONDS = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 2)
    FIFTEEN_OR_TWENTY_SECONDS = typing___cast(
        "ReachPlanAdLengthEnum.ReachPlanAdLength", 3
    )
    TWENTY_SECONDS_OR_MORE = typing___cast("ReachPlanAdLengthEnum.ReachPlanAdLength", 4)
    global___ReachPlanAdLength = ReachPlanAdLength
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ReachPlanAdLengthEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ReachPlanAdLengthEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ReachPlanAdLengthEnum = ReachPlanAdLengthEnum
