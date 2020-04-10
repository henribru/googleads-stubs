# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class BillingSetupErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BillingSetupError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "BillingSetupErrorEnum.BillingSetupError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["BillingSetupErrorEnum.BillingSetupError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "BillingSetupErrorEnum.BillingSetupError"]
        ]: ...
        UNSPECIFIED = typing___cast("BillingSetupErrorEnum.BillingSetupError", 0)
        UNKNOWN = typing___cast("BillingSetupErrorEnum.BillingSetupError", 1)
        CANNOT_USE_EXISTING_AND_NEW_ACCOUNT = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 2
        )
        CANNOT_REMOVE_STARTED_BILLING_SETUP = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 3
        )
        CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 4
        )
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 5
        )
        INVALID_PAYMENTS_ACCOUNT = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 6
        )
        BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 7
        )
        INVALID_START_TIME_TYPE = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 8
        )
        THIRD_PARTY_ALREADY_HAS_BILLING = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 9
        )
        BILLING_SETUP_IN_PROGRESS = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 10
        )
        NO_SIGNUP_PERMISSION = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 11
        )
        CHANGE_OF_BILL_TO_IN_PROGRESS = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 12
        )
        PAYMENTS_PROFILE_NOT_FOUND = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 13
        )
        PAYMENTS_ACCOUNT_NOT_FOUND = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 14
        )
        PAYMENTS_PROFILE_INELIGIBLE = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 15
        )
        PAYMENTS_ACCOUNT_INELIGIBLE = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 16
        )
        CUSTOMER_NEEDS_INTERNAL_APPROVAL = typing___cast(
            "BillingSetupErrorEnum.BillingSetupError", 17
        )
    UNSPECIFIED = typing___cast("BillingSetupErrorEnum.BillingSetupError", 0)
    UNKNOWN = typing___cast("BillingSetupErrorEnum.BillingSetupError", 1)
    CANNOT_USE_EXISTING_AND_NEW_ACCOUNT = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 2
    )
    CANNOT_REMOVE_STARTED_BILLING_SETUP = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 3
    )
    CANNOT_CHANGE_BILLING_TO_SAME_PAYMENTS_ACCOUNT = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 4
    )
    BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_STATUS = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 5
    )
    INVALID_PAYMENTS_ACCOUNT = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 6
    )
    BILLING_SETUP_NOT_PERMITTED_FOR_CUSTOMER_CATEGORY = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 7
    )
    INVALID_START_TIME_TYPE = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 8
    )
    THIRD_PARTY_ALREADY_HAS_BILLING = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 9
    )
    BILLING_SETUP_IN_PROGRESS = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 10
    )
    NO_SIGNUP_PERMISSION = typing___cast("BillingSetupErrorEnum.BillingSetupError", 11)
    CHANGE_OF_BILL_TO_IN_PROGRESS = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 12
    )
    PAYMENTS_PROFILE_NOT_FOUND = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 13
    )
    PAYMENTS_ACCOUNT_NOT_FOUND = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 14
    )
    PAYMENTS_PROFILE_INELIGIBLE = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 15
    )
    PAYMENTS_ACCOUNT_INELIGIBLE = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 16
    )
    CUSTOMER_NEEDS_INTERNAL_APPROVAL = typing___cast(
        "BillingSetupErrorEnum.BillingSetupError", 17
    )
    global___BillingSetupError = BillingSetupError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BillingSetupErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> BillingSetupErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___BillingSetupErrorEnum = BillingSetupErrorEnum