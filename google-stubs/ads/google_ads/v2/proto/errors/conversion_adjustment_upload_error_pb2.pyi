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

class ConversionAdjustmentUploadErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ConversionAdjustmentUploadError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls
        ) -> typing___List[
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError"
        ]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[
                builtin___str,
                "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError",
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 0
        )
        UNKNOWN = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 1
        )
        TOO_RECENT_CONVERSION_ACTION = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 2
        )
        INVALID_CONVERSION_ACTION = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 3
        )
        CONVERSION_ALREADY_RETRACTED = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 4
        )
        CONVERSION_NOT_FOUND = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 5
        )
        CONVERSION_EXPIRED = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 6
        )
        ADJUSTMENT_PRECEDES_CONVERSION = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 7
        )
        MORE_RECENT_RESTATEMENT_FOUND = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 8
        )
        TOO_RECENT_CONVERSION = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 9
        )
        CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE = typing___cast(
            "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 10
        )
    UNSPECIFIED = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 0
    )
    UNKNOWN = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 1
    )
    TOO_RECENT_CONVERSION_ACTION = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 2
    )
    INVALID_CONVERSION_ACTION = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 3
    )
    CONVERSION_ALREADY_RETRACTED = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 4
    )
    CONVERSION_NOT_FOUND = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 5
    )
    CONVERSION_EXPIRED = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 6
    )
    ADJUSTMENT_PRECEDES_CONVERSION = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 7
    )
    MORE_RECENT_RESTATEMENT_FOUND = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 8
    )
    TOO_RECENT_CONVERSION = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 9
    )
    CANNOT_RESTATE_CONVERSION_ACTION_THAT_ALWAYS_USES_DEFAULT_CONVERSION_VALUE = typing___cast(
        "ConversionAdjustmentUploadErrorEnum.ConversionAdjustmentUploadError", 10
    )
    global___ConversionAdjustmentUploadError = ConversionAdjustmentUploadError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(
            cls, s: builtin___bytes
        ) -> ConversionAdjustmentUploadErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ConversionAdjustmentUploadErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ConversionAdjustmentUploadErrorEnum = ConversionAdjustmentUploadErrorEnum
