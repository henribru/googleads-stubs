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

class AppUrlOperatingSystemTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AppUrlOperatingSystemType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            AppUrlOperatingSystemType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(0)
        UNKNOWN = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(1)
        IOS = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(2)
        ANDROID = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(3)
    class AppUrlOperatingSystemType(metaclass=_AppUrlOperatingSystemType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(0)
    UNKNOWN = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(1)
    IOS = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(2)
    ANDROID = AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType.V(3)
    def __init__(
        self,
    ) -> None: ...

global___AppUrlOperatingSystemTypeEnum = AppUrlOperatingSystemTypeEnum
