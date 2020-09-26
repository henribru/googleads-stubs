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

class BiddingErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    BiddingErrorValue = typing___NewType("BiddingErrorValue", builtin___int)
    type___BiddingErrorValue = BiddingErrorValue
    BiddingError: _BiddingError
    class _BiddingError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            BiddingErrorEnum.BiddingErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(BiddingErrorEnum.BiddingErrorValue, 0)
        UNKNOWN = typing___cast(BiddingErrorEnum.BiddingErrorValue, 1)
        BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 2
        )
        CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 7
        )
        INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 10
        )
        INVALID_BIDDING_STRATEGY_TYPE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 14
        )
        INVALID_BID = typing___cast(BiddingErrorEnum.BiddingErrorValue, 17)
        BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 18
        )
        CONVERSION_TRACKING_NOT_ENABLED = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 19
        )
        NOT_ENOUGH_CONVERSIONS = typing___cast(BiddingErrorEnum.BiddingErrorValue, 20)
        CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 21
        )
        CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 23
        )
        BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 24
        )
        PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 25
        )
        PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 26
        )
        BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 27
        )
        BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 28
        )
        BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 29
        )
        BID_TOO_SMALL = typing___cast(BiddingErrorEnum.BiddingErrorValue, 30)
        BID_TOO_BIG = typing___cast(BiddingErrorEnum.BiddingErrorValue, 31)
        BID_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 32
        )
        INVALID_DOMAIN_NAME = typing___cast(BiddingErrorEnum.BiddingErrorValue, 33)
        NOT_COMPATIBLE_WITH_PAYMENT_MODE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 34
        )
        NOT_COMPATIBLE_WITH_BUDGET_TYPE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 35
        )
        NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE = typing___cast(
            BiddingErrorEnum.BiddingErrorValue, 36
        )
    UNSPECIFIED = typing___cast(BiddingErrorEnum.BiddingErrorValue, 0)
    UNKNOWN = typing___cast(BiddingErrorEnum.BiddingErrorValue, 1)
    BIDDING_STRATEGY_TRANSITION_NOT_ALLOWED = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 2
    )
    CANNOT_ATTACH_BIDDING_STRATEGY_TO_CAMPAIGN = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 7
    )
    INVALID_ANONYMOUS_BIDDING_STRATEGY_TYPE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 10
    )
    INVALID_BIDDING_STRATEGY_TYPE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 14
    )
    INVALID_BID = typing___cast(BiddingErrorEnum.BiddingErrorValue, 17)
    BIDDING_STRATEGY_NOT_AVAILABLE_FOR_ACCOUNT_TYPE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 18
    )
    CONVERSION_TRACKING_NOT_ENABLED = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 19
    )
    NOT_ENOUGH_CONVERSIONS = typing___cast(BiddingErrorEnum.BiddingErrorValue, 20)
    CANNOT_CREATE_CAMPAIGN_WITH_BIDDING_STRATEGY = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 21
    )
    CANNOT_TARGET_CONTENT_NETWORK_ONLY_WITH_CAMPAIGN_LEVEL_POP_BIDDING_STRATEGY = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 23
    )
    BIDDING_STRATEGY_NOT_SUPPORTED_WITH_AD_SCHEDULE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 24
    )
    PAY_PER_CONVERSION_NOT_AVAILABLE_FOR_CUSTOMER = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 25
    )
    PAY_PER_CONVERSION_NOT_ALLOWED_WITH_TARGET_CPA = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 26
    )
    BIDDING_STRATEGY_NOT_ALLOWED_FOR_SEARCH_ONLY_CAMPAIGNS = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 27
    )
    BIDDING_STRATEGY_NOT_SUPPORTED_IN_DRAFTS_OR_EXPERIMENTS = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 28
    )
    BIDDING_STRATEGY_TYPE_DOES_NOT_SUPPORT_PRODUCT_TYPE_ADGROUP_CRITERION = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 29
    )
    BID_TOO_SMALL = typing___cast(BiddingErrorEnum.BiddingErrorValue, 30)
    BID_TOO_BIG = typing___cast(BiddingErrorEnum.BiddingErrorValue, 31)
    BID_TOO_MANY_FRACTIONAL_DIGITS = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 32
    )
    INVALID_DOMAIN_NAME = typing___cast(BiddingErrorEnum.BiddingErrorValue, 33)
    NOT_COMPATIBLE_WITH_PAYMENT_MODE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 34
    )
    NOT_COMPATIBLE_WITH_BUDGET_TYPE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 35
    )
    NOT_COMPATIBLE_WITH_BIDDING_STRATEGY_TYPE = typing___cast(
        BiddingErrorEnum.BiddingErrorValue, 36
    )
    type___BiddingError = BiddingError
    def __init__(self,) -> None: ...

type___BiddingErrorEnum = BiddingErrorEnum
