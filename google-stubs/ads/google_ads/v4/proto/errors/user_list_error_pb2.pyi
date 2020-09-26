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

class UserListErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    UserListErrorValue = typing___NewType("UserListErrorValue", builtin___int)
    type___UserListErrorValue = UserListErrorValue
    UserListError: _UserListError
    class _UserListError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            UserListErrorEnum.UserListErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(UserListErrorEnum.UserListErrorValue, 0)
        UNKNOWN = typing___cast(UserListErrorEnum.UserListErrorValue, 1)
        EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 2
        )
        CONCRETE_TYPE_REQUIRED = typing___cast(UserListErrorEnum.UserListErrorValue, 3)
        CONVERSION_TYPE_ID_REQUIRED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 4
        )
        DUPLICATE_CONVERSION_TYPES = typing___cast(
            UserListErrorEnum.UserListErrorValue, 5
        )
        INVALID_CONVERSION_TYPE = typing___cast(UserListErrorEnum.UserListErrorValue, 6)
        INVALID_DESCRIPTION = typing___cast(UserListErrorEnum.UserListErrorValue, 7)
        INVALID_NAME = typing___cast(UserListErrorEnum.UserListErrorValue, 8)
        INVALID_TYPE = typing___cast(UserListErrorEnum.UserListErrorValue, 9)
        CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND = typing___cast(
            UserListErrorEnum.UserListErrorValue, 10
        )
        INVALID_USER_LIST_LOGICAL_RULE_OPERAND = typing___cast(
            UserListErrorEnum.UserListErrorValue, 11
        )
        NAME_ALREADY_USED = typing___cast(UserListErrorEnum.UserListErrorValue, 12)
        NEW_CONVERSION_TYPE_NAME_REQUIRED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 13
        )
        CONVERSION_TYPE_NAME_ALREADY_USED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 14
        )
        OWNERSHIP_REQUIRED_FOR_SET = typing___cast(
            UserListErrorEnum.UserListErrorValue, 15
        )
        USER_LIST_MUTATE_NOT_SUPPORTED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 16
        )
        INVALID_RULE = typing___cast(UserListErrorEnum.UserListErrorValue, 17)
        INVALID_DATE_RANGE = typing___cast(UserListErrorEnum.UserListErrorValue, 27)
        CAN_NOT_MUTATE_SENSITIVE_USERLIST = typing___cast(
            UserListErrorEnum.UserListErrorValue, 28
        )
        MAX_NUM_RULEBASED_USERLISTS = typing___cast(
            UserListErrorEnum.UserListErrorValue, 29
        )
        CANNOT_MODIFY_BILLABLE_RECORD_COUNT = typing___cast(
            UserListErrorEnum.UserListErrorValue, 30
        )
        APP_ID_NOT_SET = typing___cast(UserListErrorEnum.UserListErrorValue, 31)
        USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST = typing___cast(
            UserListErrorEnum.UserListErrorValue, 32
        )
        ADVERTISER_NOT_WHITELISTED_FOR_USING_UPLOADED_DATA = typing___cast(
            UserListErrorEnum.UserListErrorValue, 33
        )
        RULE_TYPE_IS_NOT_SUPPORTED = typing___cast(
            UserListErrorEnum.UserListErrorValue, 34
        )
        CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND = typing___cast(
            UserListErrorEnum.UserListErrorValue, 35
        )
        CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS = typing___cast(
            UserListErrorEnum.UserListErrorValue, 36
        )
    UNSPECIFIED = typing___cast(UserListErrorEnum.UserListErrorValue, 0)
    UNKNOWN = typing___cast(UserListErrorEnum.UserListErrorValue, 1)
    EXTERNAL_REMARKETING_USER_LIST_MUTATE_NOT_SUPPORTED = typing___cast(
        UserListErrorEnum.UserListErrorValue, 2
    )
    CONCRETE_TYPE_REQUIRED = typing___cast(UserListErrorEnum.UserListErrorValue, 3)
    CONVERSION_TYPE_ID_REQUIRED = typing___cast(UserListErrorEnum.UserListErrorValue, 4)
    DUPLICATE_CONVERSION_TYPES = typing___cast(UserListErrorEnum.UserListErrorValue, 5)
    INVALID_CONVERSION_TYPE = typing___cast(UserListErrorEnum.UserListErrorValue, 6)
    INVALID_DESCRIPTION = typing___cast(UserListErrorEnum.UserListErrorValue, 7)
    INVALID_NAME = typing___cast(UserListErrorEnum.UserListErrorValue, 8)
    INVALID_TYPE = typing___cast(UserListErrorEnum.UserListErrorValue, 9)
    CAN_NOT_ADD_LOGICAL_LIST_AS_LOGICAL_LIST_OPERAND = typing___cast(
        UserListErrorEnum.UserListErrorValue, 10
    )
    INVALID_USER_LIST_LOGICAL_RULE_OPERAND = typing___cast(
        UserListErrorEnum.UserListErrorValue, 11
    )
    NAME_ALREADY_USED = typing___cast(UserListErrorEnum.UserListErrorValue, 12)
    NEW_CONVERSION_TYPE_NAME_REQUIRED = typing___cast(
        UserListErrorEnum.UserListErrorValue, 13
    )
    CONVERSION_TYPE_NAME_ALREADY_USED = typing___cast(
        UserListErrorEnum.UserListErrorValue, 14
    )
    OWNERSHIP_REQUIRED_FOR_SET = typing___cast(UserListErrorEnum.UserListErrorValue, 15)
    USER_LIST_MUTATE_NOT_SUPPORTED = typing___cast(
        UserListErrorEnum.UserListErrorValue, 16
    )
    INVALID_RULE = typing___cast(UserListErrorEnum.UserListErrorValue, 17)
    INVALID_DATE_RANGE = typing___cast(UserListErrorEnum.UserListErrorValue, 27)
    CAN_NOT_MUTATE_SENSITIVE_USERLIST = typing___cast(
        UserListErrorEnum.UserListErrorValue, 28
    )
    MAX_NUM_RULEBASED_USERLISTS = typing___cast(
        UserListErrorEnum.UserListErrorValue, 29
    )
    CANNOT_MODIFY_BILLABLE_RECORD_COUNT = typing___cast(
        UserListErrorEnum.UserListErrorValue, 30
    )
    APP_ID_NOT_SET = typing___cast(UserListErrorEnum.UserListErrorValue, 31)
    USERLIST_NAME_IS_RESERVED_FOR_SYSTEM_LIST = typing___cast(
        UserListErrorEnum.UserListErrorValue, 32
    )
    ADVERTISER_NOT_WHITELISTED_FOR_USING_UPLOADED_DATA = typing___cast(
        UserListErrorEnum.UserListErrorValue, 33
    )
    RULE_TYPE_IS_NOT_SUPPORTED = typing___cast(UserListErrorEnum.UserListErrorValue, 34)
    CAN_NOT_ADD_A_SIMILAR_USERLIST_AS_LOGICAL_LIST_OPERAND = typing___cast(
        UserListErrorEnum.UserListErrorValue, 35
    )
    CAN_NOT_MIX_CRM_BASED_IN_LOGICAL_LIST_WITH_OTHER_LISTS = typing___cast(
        UserListErrorEnum.UserListErrorValue, 36
    )
    type___UserListError = UserListError
    def __init__(self,) -> None: ...

type___UserListErrorEnum = UserListErrorEnum
