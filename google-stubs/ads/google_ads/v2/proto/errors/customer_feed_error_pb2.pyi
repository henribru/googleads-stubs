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

class CustomerFeedErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomerFeedErrorValue = typing___NewType("CustomerFeedErrorValue", builtin___int)
    type___CustomerFeedErrorValue = CustomerFeedErrorValue
    CustomerFeedError: _CustomerFeedError
    class _CustomerFeedError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomerFeedErrorEnum.CustomerFeedErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(CustomerFeedErrorEnum.CustomerFeedErrorValue, 0)
        UNKNOWN = typing___cast(CustomerFeedErrorEnum.CustomerFeedErrorValue, 1)
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 2
        )
        CANNOT_CREATE_FOR_REMOVED_FEED = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 3
        )
        CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 4
        )
        CANNOT_MODIFY_REMOVED_CUSTOMER_FEED = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 5
        )
        INVALID_PLACEHOLDER_TYPE = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 6
        )
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 7
        )
        PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED = typing___cast(
            CustomerFeedErrorEnum.CustomerFeedErrorValue, 8
        )
    UNSPECIFIED = typing___cast(CustomerFeedErrorEnum.CustomerFeedErrorValue, 0)
    UNKNOWN = typing___cast(CustomerFeedErrorEnum.CustomerFeedErrorValue, 1)
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 2
    )
    CANNOT_CREATE_FOR_REMOVED_FEED = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 3
    )
    CANNOT_CREATE_ALREADY_EXISTING_CUSTOMER_FEED = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 4
    )
    CANNOT_MODIFY_REMOVED_CUSTOMER_FEED = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 5
    )
    INVALID_PLACEHOLDER_TYPE = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 6
    )
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 7
    )
    PLACEHOLDER_TYPE_NOT_ALLOWED_ON_CUSTOMER_FEED = typing___cast(
        CustomerFeedErrorEnum.CustomerFeedErrorValue, 8
    )
    type___CustomerFeedError = CustomerFeedError
    def __init__(self,) -> None: ...

type___CustomerFeedErrorEnum = CustomerFeedErrorEnum
