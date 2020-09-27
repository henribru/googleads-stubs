# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ConversionActionCategoryEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionActionCategoryValue = typing___NewType(
        "ConversionActionCategoryValue", builtin___int
    )
    type___ConversionActionCategoryValue = ConversionActionCategoryValue
    ConversionActionCategory: _ConversionActionCategory
    class _ConversionActionCategory(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionActionCategoryEnum.ConversionActionCategoryValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 0
        )
        UNKNOWN = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 1
        )
        DEFAULT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 2
        )
        PAGE_VIEW = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 3
        )
        PURCHASE = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 4
        )
        SIGNUP = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 5
        )
        LEAD = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 6
        )
        DOWNLOAD = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 7
        )
        ADD_TO_CART = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 8
        )
        BEGIN_CHECKOUT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 9
        )
        SUBSCRIBE_PAID = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 10
        )
        PHONE_CALL_LEAD = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 11
        )
        IMPORTED_LEAD = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 12
        )
        SUBMIT_LEAD_FORM = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 13
        )
        BOOK_APPOINTMENT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 14
        )
        REQUEST_QUOTE = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 15
        )
        GET_DIRECTIONS = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 16
        )
        OUTBOUND_CLICK = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 17
        )
        CONTACT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 18
        )
        ENGAGEMENT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 19
        )
        STORE_VISIT = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 20
        )
        STORE_SALE = typing___cast(
            ConversionActionCategoryEnum.ConversionActionCategoryValue, 21
        )
    UNSPECIFIED = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 0
    )
    UNKNOWN = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 1
    )
    DEFAULT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 2
    )
    PAGE_VIEW = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 3
    )
    PURCHASE = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 4
    )
    SIGNUP = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 5
    )
    LEAD = typing___cast(ConversionActionCategoryEnum.ConversionActionCategoryValue, 6)
    DOWNLOAD = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 7
    )
    ADD_TO_CART = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 8
    )
    BEGIN_CHECKOUT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 9
    )
    SUBSCRIBE_PAID = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 10
    )
    PHONE_CALL_LEAD = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 11
    )
    IMPORTED_LEAD = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 12
    )
    SUBMIT_LEAD_FORM = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 13
    )
    BOOK_APPOINTMENT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 14
    )
    REQUEST_QUOTE = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 15
    )
    GET_DIRECTIONS = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 16
    )
    OUTBOUND_CLICK = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 17
    )
    CONTACT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 18
    )
    ENGAGEMENT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 19
    )
    STORE_VISIT = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 20
    )
    STORE_SALE = typing___cast(
        ConversionActionCategoryEnum.ConversionActionCategoryValue, 21
    )
    type___ConversionActionCategory = ConversionActionCategory
    def __init__(self,) -> None: ...

type___ConversionActionCategoryEnum = ConversionActionCategoryEnum