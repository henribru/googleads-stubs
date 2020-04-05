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

class MutateErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class MutateError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "MutateErrorEnum.MutateError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["MutateErrorEnum.MutateError"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "MutateErrorEnum.MutateError"]
        ]: ...
        UNSPECIFIED = typing___cast("MutateErrorEnum.MutateError", 0)
        UNKNOWN = typing___cast("MutateErrorEnum.MutateError", 1)
        RESOURCE_NOT_FOUND = typing___cast("MutateErrorEnum.MutateError", 3)
        ID_EXISTS_IN_MULTIPLE_MUTATES = typing___cast("MutateErrorEnum.MutateError", 7)
        INCONSISTENT_FIELD_VALUES = typing___cast("MutateErrorEnum.MutateError", 8)
        MUTATE_NOT_ALLOWED = typing___cast("MutateErrorEnum.MutateError", 9)
        RESOURCE_NOT_IN_GOOGLE_ADS = typing___cast("MutateErrorEnum.MutateError", 10)
        RESOURCE_ALREADY_EXISTS = typing___cast("MutateErrorEnum.MutateError", 11)
    UNSPECIFIED = typing___cast("MutateErrorEnum.MutateError", 0)
    UNKNOWN = typing___cast("MutateErrorEnum.MutateError", 1)
    RESOURCE_NOT_FOUND = typing___cast("MutateErrorEnum.MutateError", 3)
    ID_EXISTS_IN_MULTIPLE_MUTATES = typing___cast("MutateErrorEnum.MutateError", 7)
    INCONSISTENT_FIELD_VALUES = typing___cast("MutateErrorEnum.MutateError", 8)
    MUTATE_NOT_ALLOWED = typing___cast("MutateErrorEnum.MutateError", 9)
    RESOURCE_NOT_IN_GOOGLE_ADS = typing___cast("MutateErrorEnum.MutateError", 10)
    RESOURCE_ALREADY_EXISTS = typing___cast("MutateErrorEnum.MutateError", 11)
    global___MutateError = MutateError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MutateErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___MutateErrorEnum = MutateErrorEnum
