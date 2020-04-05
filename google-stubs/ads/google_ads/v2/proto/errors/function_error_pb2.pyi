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

class FunctionErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FunctionError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "FunctionErrorEnum.FunctionError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["FunctionErrorEnum.FunctionError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "FunctionErrorEnum.FunctionError"]
        ]: ...
        UNSPECIFIED = typing___cast("FunctionErrorEnum.FunctionError", 0)
        UNKNOWN = typing___cast("FunctionErrorEnum.FunctionError", 1)
        INVALID_FUNCTION_FORMAT = typing___cast("FunctionErrorEnum.FunctionError", 2)
        DATA_TYPE_MISMATCH = typing___cast("FunctionErrorEnum.FunctionError", 3)
        INVALID_CONJUNCTION_OPERANDS = typing___cast(
            "FunctionErrorEnum.FunctionError", 4
        )
        INVALID_NUMBER_OF_OPERANDS = typing___cast("FunctionErrorEnum.FunctionError", 5)
        INVALID_OPERAND_TYPE = typing___cast("FunctionErrorEnum.FunctionError", 6)
        INVALID_OPERATOR = typing___cast("FunctionErrorEnum.FunctionError", 7)
        INVALID_REQUEST_CONTEXT_TYPE = typing___cast(
            "FunctionErrorEnum.FunctionError", 8
        )
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER = typing___cast(
            "FunctionErrorEnum.FunctionError", 9
        )
        INVALID_FUNCTION_FOR_PLACEHOLDER = typing___cast(
            "FunctionErrorEnum.FunctionError", 10
        )
        INVALID_OPERAND = typing___cast("FunctionErrorEnum.FunctionError", 11)
        MISSING_CONSTANT_OPERAND_VALUE = typing___cast(
            "FunctionErrorEnum.FunctionError", 12
        )
        INVALID_CONSTANT_OPERAND_VALUE = typing___cast(
            "FunctionErrorEnum.FunctionError", 13
        )
        INVALID_NESTING = typing___cast("FunctionErrorEnum.FunctionError", 14)
        MULTIPLE_FEED_IDS_NOT_SUPPORTED = typing___cast(
            "FunctionErrorEnum.FunctionError", 15
        )
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA = typing___cast(
            "FunctionErrorEnum.FunctionError", 16
        )
        INVALID_ATTRIBUTE_NAME = typing___cast("FunctionErrorEnum.FunctionError", 17)
    UNSPECIFIED = typing___cast("FunctionErrorEnum.FunctionError", 0)
    UNKNOWN = typing___cast("FunctionErrorEnum.FunctionError", 1)
    INVALID_FUNCTION_FORMAT = typing___cast("FunctionErrorEnum.FunctionError", 2)
    DATA_TYPE_MISMATCH = typing___cast("FunctionErrorEnum.FunctionError", 3)
    INVALID_CONJUNCTION_OPERANDS = typing___cast("FunctionErrorEnum.FunctionError", 4)
    INVALID_NUMBER_OF_OPERANDS = typing___cast("FunctionErrorEnum.FunctionError", 5)
    INVALID_OPERAND_TYPE = typing___cast("FunctionErrorEnum.FunctionError", 6)
    INVALID_OPERATOR = typing___cast("FunctionErrorEnum.FunctionError", 7)
    INVALID_REQUEST_CONTEXT_TYPE = typing___cast("FunctionErrorEnum.FunctionError", 8)
    INVALID_FUNCTION_FOR_CALL_PLACEHOLDER = typing___cast(
        "FunctionErrorEnum.FunctionError", 9
    )
    INVALID_FUNCTION_FOR_PLACEHOLDER = typing___cast(
        "FunctionErrorEnum.FunctionError", 10
    )
    INVALID_OPERAND = typing___cast("FunctionErrorEnum.FunctionError", 11)
    MISSING_CONSTANT_OPERAND_VALUE = typing___cast(
        "FunctionErrorEnum.FunctionError", 12
    )
    INVALID_CONSTANT_OPERAND_VALUE = typing___cast(
        "FunctionErrorEnum.FunctionError", 13
    )
    INVALID_NESTING = typing___cast("FunctionErrorEnum.FunctionError", 14)
    MULTIPLE_FEED_IDS_NOT_SUPPORTED = typing___cast(
        "FunctionErrorEnum.FunctionError", 15
    )
    INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA = typing___cast(
        "FunctionErrorEnum.FunctionError", 16
    )
    INVALID_ATTRIBUTE_NAME = typing___cast("FunctionErrorEnum.FunctionError", 17)
    global___FunctionError = FunctionError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FunctionErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FunctionErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___FunctionErrorEnum = FunctionErrorEnum
