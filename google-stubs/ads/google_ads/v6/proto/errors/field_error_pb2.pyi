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

class FieldErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _FieldError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[FieldError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = FieldErrorEnum.FieldError.V(0)
        UNKNOWN = FieldErrorEnum.FieldError.V(1)
        REQUIRED = FieldErrorEnum.FieldError.V(2)
        IMMUTABLE_FIELD = FieldErrorEnum.FieldError.V(3)
        INVALID_VALUE = FieldErrorEnum.FieldError.V(4)
        VALUE_MUST_BE_UNSET = FieldErrorEnum.FieldError.V(5)
        REQUIRED_NONEMPTY_LIST = FieldErrorEnum.FieldError.V(6)
        FIELD_CANNOT_BE_CLEARED = FieldErrorEnum.FieldError.V(7)
        BLOCKED_VALUE = FieldErrorEnum.FieldError.V(9)
    class FieldError(metaclass=_FieldError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = FieldErrorEnum.FieldError.V(0)
    UNKNOWN = FieldErrorEnum.FieldError.V(1)
    REQUIRED = FieldErrorEnum.FieldError.V(2)
    IMMUTABLE_FIELD = FieldErrorEnum.FieldError.V(3)
    INVALID_VALUE = FieldErrorEnum.FieldError.V(4)
    VALUE_MUST_BE_UNSET = FieldErrorEnum.FieldError.V(5)
    REQUIRED_NONEMPTY_LIST = FieldErrorEnum.FieldError.V(6)
    FIELD_CANNOT_BE_CLEARED = FieldErrorEnum.FieldError.V(7)
    BLOCKED_VALUE = FieldErrorEnum.FieldError.V(9)
    def __init__(
        self,
    ) -> None: ...

global___FieldErrorEnum = FieldErrorEnum
