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

class ManagerLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ManagerLinkErrorValue = typing___NewType("ManagerLinkErrorValue", builtin___int)
    type___ManagerLinkErrorValue = ManagerLinkErrorValue
    ManagerLinkError: _ManagerLinkError
    class _ManagerLinkError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ManagerLinkErrorEnum.ManagerLinkErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 0)
        UNKNOWN = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 1)
        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 2
        )
        TOO_MANY_MANAGERS = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 3)
        TOO_MANY_INVITES = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 4)
        ALREADY_INVITED_BY_THIS_MANAGER = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 5
        )
        ALREADY_MANAGED_BY_THIS_MANAGER = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 6
        )
        ALREADY_MANAGED_IN_HIERARCHY = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 7
        )
        DUPLICATE_CHILD_FOUND = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 8
        )
        CLIENT_HAS_NO_ADMIN_USER = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 9
        )
        MAX_DEPTH_EXCEEDED = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 10
        )
        CYCLE_NOT_ALLOWED = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 11
        )
        TOO_MANY_ACCOUNTS = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 12
        )
        TOO_MANY_ACCOUNTS_AT_MANAGER = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 13
        )
        NON_OWNER_USER_CANNOT_MODIFY_LINK = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 14
        )
        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS = typing___cast(
            ManagerLinkErrorEnum.ManagerLinkErrorValue, 15
        )
    UNSPECIFIED = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 0)
    UNKNOWN = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 1)
    ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 2
    )
    TOO_MANY_MANAGERS = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 3)
    TOO_MANY_INVITES = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 4)
    ALREADY_INVITED_BY_THIS_MANAGER = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 5
    )
    ALREADY_MANAGED_BY_THIS_MANAGER = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 6
    )
    ALREADY_MANAGED_IN_HIERARCHY = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 7
    )
    DUPLICATE_CHILD_FOUND = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 8)
    CLIENT_HAS_NO_ADMIN_USER = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 9
    )
    MAX_DEPTH_EXCEEDED = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 10)
    CYCLE_NOT_ALLOWED = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 11)
    TOO_MANY_ACCOUNTS = typing___cast(ManagerLinkErrorEnum.ManagerLinkErrorValue, 12)
    TOO_MANY_ACCOUNTS_AT_MANAGER = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 13
    )
    NON_OWNER_USER_CANNOT_MODIFY_LINK = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 14
    )
    SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS = typing___cast(
        ManagerLinkErrorEnum.ManagerLinkErrorValue, 15
    )
    type___ManagerLinkError = ManagerLinkError
    def __init__(self,) -> None: ...

type___ManagerLinkErrorEnum = ManagerLinkErrorEnum
