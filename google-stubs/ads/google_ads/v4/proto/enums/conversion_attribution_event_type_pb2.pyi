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

class ConversionAttributionEventTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ConversionAttributionEventType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ConversionAttributionEventType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = (
            ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(0)
        )
        UNKNOWN = ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(1)
        IMPRESSION = (
            ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(2)
        )
        INTERACTION = (
            ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(3)
        )
    class ConversionAttributionEventType(metaclass=_ConversionAttributionEventType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(0)
    UNKNOWN = ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(1)
    IMPRESSION = ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(2)
    INTERACTION = ConversionAttributionEventTypeEnum.ConversionAttributionEventType.V(3)
    def __init__(
        self,
    ) -> None: ...

global___ConversionAttributionEventTypeEnum = ConversionAttributionEventTypeEnum
