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

class AdGroupAdErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AdGroupAdError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AdGroupAdError.V],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AdGroupAdErrorEnum.AdGroupAdError.V(0)
        UNKNOWN = AdGroupAdErrorEnum.AdGroupAdError.V(1)
        AD_GROUP_AD_LABEL_DOES_NOT_EXIST = AdGroupAdErrorEnum.AdGroupAdError.V(2)
        AD_GROUP_AD_LABEL_ALREADY_EXISTS = AdGroupAdErrorEnum.AdGroupAdError.V(3)
        AD_NOT_UNDER_ADGROUP = AdGroupAdErrorEnum.AdGroupAdError.V(4)
        CANNOT_OPERATE_ON_REMOVED_ADGROUPAD = AdGroupAdErrorEnum.AdGroupAdError.V(5)
        CANNOT_CREATE_DEPRECATED_ADS = AdGroupAdErrorEnum.AdGroupAdError.V(6)
        CANNOT_CREATE_TEXT_ADS = AdGroupAdErrorEnum.AdGroupAdError.V(7)
        EMPTY_FIELD = AdGroupAdErrorEnum.AdGroupAdError.V(8)
        RESOURCE_REFERENCED_IN_MULTIPLE_OPS = AdGroupAdErrorEnum.AdGroupAdError.V(9)
        AD_TYPE_CANNOT_BE_PAUSED = AdGroupAdErrorEnum.AdGroupAdError.V(10)
        AD_TYPE_CANNOT_BE_REMOVED = AdGroupAdErrorEnum.AdGroupAdError.V(11)
    class AdGroupAdError(metaclass=_AdGroupAdError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AdGroupAdErrorEnum.AdGroupAdError.V(0)
    UNKNOWN = AdGroupAdErrorEnum.AdGroupAdError.V(1)
    AD_GROUP_AD_LABEL_DOES_NOT_EXIST = AdGroupAdErrorEnum.AdGroupAdError.V(2)
    AD_GROUP_AD_LABEL_ALREADY_EXISTS = AdGroupAdErrorEnum.AdGroupAdError.V(3)
    AD_NOT_UNDER_ADGROUP = AdGroupAdErrorEnum.AdGroupAdError.V(4)
    CANNOT_OPERATE_ON_REMOVED_ADGROUPAD = AdGroupAdErrorEnum.AdGroupAdError.V(5)
    CANNOT_CREATE_DEPRECATED_ADS = AdGroupAdErrorEnum.AdGroupAdError.V(6)
    CANNOT_CREATE_TEXT_ADS = AdGroupAdErrorEnum.AdGroupAdError.V(7)
    EMPTY_FIELD = AdGroupAdErrorEnum.AdGroupAdError.V(8)
    RESOURCE_REFERENCED_IN_MULTIPLE_OPS = AdGroupAdErrorEnum.AdGroupAdError.V(9)
    AD_TYPE_CANNOT_BE_PAUSED = AdGroupAdErrorEnum.AdGroupAdError.V(10)
    AD_TYPE_CANNOT_BE_REMOVED = AdGroupAdErrorEnum.AdGroupAdError.V(11)
    def __init__(
        self,
    ) -> None: ...

global___AdGroupAdErrorEnum = AdGroupAdErrorEnum
