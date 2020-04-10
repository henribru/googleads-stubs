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

class FeedItemValidationStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedItemValidationStatus(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "FeedItemValidationStatusEnum.FeedItemValidationStatus": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["FeedItemValidationStatusEnum.FeedItemValidationStatus"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "FeedItemValidationStatusEnum.FeedItemValidationStatus"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "FeedItemValidationStatusEnum.FeedItemValidationStatus", 0
        )
        UNKNOWN = typing___cast(
            "FeedItemValidationStatusEnum.FeedItemValidationStatus", 1
        )
        PENDING = typing___cast(
            "FeedItemValidationStatusEnum.FeedItemValidationStatus", 2
        )
        INVALID = typing___cast(
            "FeedItemValidationStatusEnum.FeedItemValidationStatus", 3
        )
        VALID = typing___cast(
            "FeedItemValidationStatusEnum.FeedItemValidationStatus", 4
        )
    UNSPECIFIED = typing___cast(
        "FeedItemValidationStatusEnum.FeedItemValidationStatus", 0
    )
    UNKNOWN = typing___cast("FeedItemValidationStatusEnum.FeedItemValidationStatus", 1)
    PENDING = typing___cast("FeedItemValidationStatusEnum.FeedItemValidationStatus", 2)
    INVALID = typing___cast("FeedItemValidationStatusEnum.FeedItemValidationStatus", 3)
    VALID = typing___cast("FeedItemValidationStatusEnum.FeedItemValidationStatus", 4)
    global___FeedItemValidationStatus = FeedItemValidationStatus
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemValidationStatusEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemValidationStatusEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___FeedItemValidationStatusEnum = FeedItemValidationStatusEnum