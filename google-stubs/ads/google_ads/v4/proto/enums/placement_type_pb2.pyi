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

class PlacementTypeEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _PlacementType(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[PlacementType.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = PlacementTypeEnum.PlacementType.V(0)
        UNKNOWN = PlacementTypeEnum.PlacementType.V(1)
        WEBSITE = PlacementTypeEnum.PlacementType.V(2)
        MOBILE_APP_CATEGORY = PlacementTypeEnum.PlacementType.V(3)
        MOBILE_APPLICATION = PlacementTypeEnum.PlacementType.V(4)
        YOUTUBE_VIDEO = PlacementTypeEnum.PlacementType.V(5)
        YOUTUBE_CHANNEL = PlacementTypeEnum.PlacementType.V(6)
    class PlacementType(metaclass=_PlacementType):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = PlacementTypeEnum.PlacementType.V(0)
    UNKNOWN = PlacementTypeEnum.PlacementType.V(1)
    WEBSITE = PlacementTypeEnum.PlacementType.V(2)
    MOBILE_APP_CATEGORY = PlacementTypeEnum.PlacementType.V(3)
    MOBILE_APPLICATION = PlacementTypeEnum.PlacementType.V(4)
    YOUTUBE_VIDEO = PlacementTypeEnum.PlacementType.V(5)
    YOUTUBE_CHANNEL = PlacementTypeEnum.PlacementType.V(6)
    def __init__(
        self,
    ) -> None: ...

global___PlacementTypeEnum = PlacementTypeEnum
