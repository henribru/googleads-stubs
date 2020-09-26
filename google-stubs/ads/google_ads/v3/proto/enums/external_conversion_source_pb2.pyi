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

class ExternalConversionSourceEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ExternalConversionSourceValue = typing___NewType(
        "ExternalConversionSourceValue", builtin___int
    )
    type___ExternalConversionSourceValue = ExternalConversionSourceValue
    ExternalConversionSource: _ExternalConversionSource
    class _ExternalConversionSource(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ExternalConversionSourceEnum.ExternalConversionSourceValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 0
        )
        UNKNOWN = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 1
        )
        WEBPAGE = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 2
        )
        ANALYTICS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 3
        )
        UPLOAD = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 4
        )
        AD_CALL_METRICS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 5
        )
        WEBSITE_CALL_METRICS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 6
        )
        STORE_VISITS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 7
        )
        ANDROID_IN_APP = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 8
        )
        IOS_IN_APP = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 9
        )
        IOS_FIRST_OPEN = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 10
        )
        APP_UNSPECIFIED = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 11
        )
        ANDROID_FIRST_OPEN = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 12
        )
        UPLOAD_CALLS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 13
        )
        FIREBASE = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 14
        )
        CLICK_TO_CALL = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 15
        )
        SALESFORCE = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 16
        )
        STORE_SALES_CRM = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 17
        )
        STORE_SALES_PAYMENT_NETWORK = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 18
        )
        GOOGLE_PLAY = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 19
        )
        THIRD_PARTY_APP_ANALYTICS = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 20
        )
        GOOGLE_ATTRIBUTION = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 21
        )
        STORE_SALES_DIRECT = typing___cast(
            ExternalConversionSourceEnum.ExternalConversionSourceValue, 22
        )
    UNSPECIFIED = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 0
    )
    UNKNOWN = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 1
    )
    WEBPAGE = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 2
    )
    ANALYTICS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 3
    )
    UPLOAD = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 4
    )
    AD_CALL_METRICS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 5
    )
    WEBSITE_CALL_METRICS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 6
    )
    STORE_VISITS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 7
    )
    ANDROID_IN_APP = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 8
    )
    IOS_IN_APP = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 9
    )
    IOS_FIRST_OPEN = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 10
    )
    APP_UNSPECIFIED = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 11
    )
    ANDROID_FIRST_OPEN = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 12
    )
    UPLOAD_CALLS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 13
    )
    FIREBASE = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 14
    )
    CLICK_TO_CALL = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 15
    )
    SALESFORCE = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 16
    )
    STORE_SALES_CRM = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 17
    )
    STORE_SALES_PAYMENT_NETWORK = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 18
    )
    GOOGLE_PLAY = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 19
    )
    THIRD_PARTY_APP_ANALYTICS = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 20
    )
    GOOGLE_ATTRIBUTION = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 21
    )
    STORE_SALES_DIRECT = typing___cast(
        ExternalConversionSourceEnum.ExternalConversionSourceValue, 22
    )
    type___ExternalConversionSource = ExternalConversionSource
    def __init__(self,) -> None: ...

type___ExternalConversionSourceEnum = ExternalConversionSourceEnum
