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

class NullErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _NullError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NullError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = NullErrorEnum.NullError.V(0)
        UNKNOWN = NullErrorEnum.NullError.V(1)
        NULL_CONTENT = NullErrorEnum.NullError.V(2)
    class NullError(metaclass=_NullError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = NullErrorEnum.NullError.V(0)
    UNKNOWN = NullErrorEnum.NullError.V(1)
    NULL_CONTENT = NullErrorEnum.NullError.V(2)
    def __init__(
        self,
    ) -> None: ...

global___NullErrorEnum = NullErrorEnum
