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

class AdGroupAdStatusEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdGroupAdStatus(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AdGroupAdStatus.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AdGroupAdStatusEnum.AdGroupAdStatus.V(0)
        UNKNOWN = AdGroupAdStatusEnum.AdGroupAdStatus.V(1)
        ENABLED = AdGroupAdStatusEnum.AdGroupAdStatus.V(2)
        PAUSED = AdGroupAdStatusEnum.AdGroupAdStatus.V(3)
        REMOVED = AdGroupAdStatusEnum.AdGroupAdStatus.V(4)
    class AdGroupAdStatus(metaclass=_AdGroupAdStatus):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AdGroupAdStatusEnum.AdGroupAdStatus.V(0)
    UNKNOWN = AdGroupAdStatusEnum.AdGroupAdStatus.V(1)
    ENABLED = AdGroupAdStatusEnum.AdGroupAdStatus.V(2)
    PAUSED = AdGroupAdStatusEnum.AdGroupAdStatus.V(3)
    REMOVED = AdGroupAdStatusEnum.AdGroupAdStatus.V(4)
    def __init__(
        self,
    ) -> None: ...

global___AdGroupAdStatusEnum = AdGroupAdStatusEnum
