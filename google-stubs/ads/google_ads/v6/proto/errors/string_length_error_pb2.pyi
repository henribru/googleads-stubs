"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class StringLengthErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _StringLengthError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            StringLengthError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = StringLengthErrorEnum.StringLengthError.V(0)
        UNKNOWN = StringLengthErrorEnum.StringLengthError.V(1)
        EMPTY = StringLengthErrorEnum.StringLengthError.V(4)
        TOO_SHORT = StringLengthErrorEnum.StringLengthError.V(2)
        TOO_LONG = StringLengthErrorEnum.StringLengthError.V(3)
    class StringLengthError(metaclass=_StringLengthError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = StringLengthErrorEnum.StringLengthError.V(0)
    UNKNOWN = StringLengthErrorEnum.StringLengthError.V(1)
    EMPTY = StringLengthErrorEnum.StringLengthError.V(4)
    TOO_SHORT = StringLengthErrorEnum.StringLengthError.V(2)
    TOO_LONG = StringLengthErrorEnum.StringLengthError.V(3)
    def __init__(
        self,
    ) -> None: ...

global___StringLengthErrorEnum = StringLengthErrorEnum
