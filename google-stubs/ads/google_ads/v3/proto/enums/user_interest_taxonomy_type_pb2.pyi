# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UserInterestTaxonomyTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UserInterestTaxonomyTypeValue = typing___NewType(
        "UserInterestTaxonomyTypeValue", builtin___int
    )
    type___UserInterestTaxonomyTypeValue = UserInterestTaxonomyTypeValue
    UserInterestTaxonomyType: _UserInterestTaxonomyType
    class _UserInterestTaxonomyType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 0
        )
        UNKNOWN = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 1
        )
        AFFINITY = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 2
        )
        IN_MARKET = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 3
        )
        MOBILE_APP_INSTALL_USER = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 4
        )
        VERTICAL_GEO = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 5
        )
        NEW_SMART_PHONE_USER = typing___cast(
            UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 6
        )
    UNSPECIFIED = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 0
    )
    UNKNOWN = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 1
    )
    AFFINITY = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 2
    )
    IN_MARKET = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 3
    )
    MOBILE_APP_INSTALL_USER = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 4
    )
    VERTICAL_GEO = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 5
    )
    NEW_SMART_PHONE_USER = typing___cast(
        UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeValue, 6
    )
    type___UserInterestTaxonomyType = UserInterestTaxonomyType
    def __init__(self,) -> None: ...

type___UserInterestTaxonomyTypeEnum = UserInterestTaxonomyTypeEnum
