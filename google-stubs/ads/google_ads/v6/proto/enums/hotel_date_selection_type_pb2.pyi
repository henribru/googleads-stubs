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

class HotelDateSelectionTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _HotelDateSelectionType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            HotelDateSelectionType.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(0)
        UNKNOWN = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(1)
        DEFAULT_SELECTION = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(50)
        USER_SELECTED = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(51)
    class HotelDateSelectionType(metaclass=_HotelDateSelectionType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(0)
    UNKNOWN = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(1)
    DEFAULT_SELECTION = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(50)
    USER_SELECTED = HotelDateSelectionTypeEnum.HotelDateSelectionType.V(51)
    def __init__(
        self,
    ) -> None: ...

global___HotelDateSelectionTypeEnum = HotelDateSelectionTypeEnum
