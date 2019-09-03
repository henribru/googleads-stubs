# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class FunctionErrorEnum(google___protobuf___message___Message):
    class FunctionError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['INVALID_FUNCTION_FORMAT'],typing_extensions___Literal['DATA_TYPE_MISMATCH'],typing_extensions___Literal['INVALID_CONJUNCTION_OPERANDS'],typing_extensions___Literal['INVALID_NUMBER_OF_OPERANDS'],typing_extensions___Literal['INVALID_OPERAND_TYPE'],typing_extensions___Literal['INVALID_OPERATOR'],typing_extensions___Literal['INVALID_REQUEST_CONTEXT_TYPE'],typing_extensions___Literal['INVALID_FUNCTION_FOR_CALL_PLACEHOLDER'],typing_extensions___Literal['INVALID_FUNCTION_FOR_PLACEHOLDER'],typing_extensions___Literal['INVALID_OPERAND'],typing_extensions___Literal['MISSING_CONSTANT_OPERAND_VALUE'],typing_extensions___Literal['INVALID_CONSTANT_OPERAND_VALUE'],typing_extensions___Literal['INVALID_NESTING'],typing_extensions___Literal['MULTIPLE_FEED_IDS_NOT_SUPPORTED'],typing_extensions___Literal['INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA'],typing_extensions___Literal['INVALID_ATTRIBUTE_NAME']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13],typing_extensions___Literal[14],typing_extensions___Literal[15],typing_extensions___Literal[16],typing_extensions___Literal[17]]
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: ClosedValueType) -> str: ...
        @classmethod
        def Value(cls, name: ClosedKeyType) -> ClosedValueType: ...
        @classmethod
        def keys(cls) -> typing___List[ClosedKeyType]: ...
        @classmethod
        def values(cls) -> typing___List[ClosedValueType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[ClosedKeyType, ClosedValueType]]: ...
        UNSPECIFIED: typing_extensions___Literal[0]
        UNKNOWN: typing_extensions___Literal[1]
        INVALID_FUNCTION_FORMAT: typing_extensions___Literal[2]
        DATA_TYPE_MISMATCH: typing_extensions___Literal[3]
        INVALID_CONJUNCTION_OPERANDS: typing_extensions___Literal[4]
        INVALID_NUMBER_OF_OPERANDS: typing_extensions___Literal[5]
        INVALID_OPERAND_TYPE: typing_extensions___Literal[6]
        INVALID_OPERATOR: typing_extensions___Literal[7]
        INVALID_REQUEST_CONTEXT_TYPE: typing_extensions___Literal[8]
        INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: typing_extensions___Literal[9]
        INVALID_FUNCTION_FOR_PLACEHOLDER: typing_extensions___Literal[10]
        INVALID_OPERAND: typing_extensions___Literal[11]
        MISSING_CONSTANT_OPERAND_VALUE: typing_extensions___Literal[12]
        INVALID_CONSTANT_OPERAND_VALUE: typing_extensions___Literal[13]
        INVALID_NESTING: typing_extensions___Literal[14]
        MULTIPLE_FEED_IDS_NOT_SUPPORTED: typing_extensions___Literal[15]
        INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: typing_extensions___Literal[16]
        INVALID_ATTRIBUTE_NAME: typing_extensions___Literal[17]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    INVALID_FUNCTION_FORMAT: typing_extensions___Literal[2]
    DATA_TYPE_MISMATCH: typing_extensions___Literal[3]
    INVALID_CONJUNCTION_OPERANDS: typing_extensions___Literal[4]
    INVALID_NUMBER_OF_OPERANDS: typing_extensions___Literal[5]
    INVALID_OPERAND_TYPE: typing_extensions___Literal[6]
    INVALID_OPERATOR: typing_extensions___Literal[7]
    INVALID_REQUEST_CONTEXT_TYPE: typing_extensions___Literal[8]
    INVALID_FUNCTION_FOR_CALL_PLACEHOLDER: typing_extensions___Literal[9]
    INVALID_FUNCTION_FOR_PLACEHOLDER: typing_extensions___Literal[10]
    INVALID_OPERAND: typing_extensions___Literal[11]
    MISSING_CONSTANT_OPERAND_VALUE: typing_extensions___Literal[12]
    INVALID_CONSTANT_OPERAND_VALUE: typing_extensions___Literal[13]
    INVALID_NESTING: typing_extensions___Literal[14]
    MULTIPLE_FEED_IDS_NOT_SUPPORTED: typing_extensions___Literal[15]
    INVALID_FUNCTION_FOR_FEED_WITH_FIXED_SCHEMA: typing_extensions___Literal[16]
    INVALID_ATTRIBUTE_NAME: typing_extensions___Literal[17]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FunctionErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
