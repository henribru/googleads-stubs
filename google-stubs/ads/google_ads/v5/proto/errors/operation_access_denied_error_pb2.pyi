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

class OperationAccessDeniedErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    OperationAccessDeniedErrorValue = typing___NewType(
        "OperationAccessDeniedErrorValue", builtin___int
    )
    type___OperationAccessDeniedErrorValue = OperationAccessDeniedErrorValue
    OperationAccessDeniedError: _OperationAccessDeniedError
    class _OperationAccessDeniedError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 0
        )
        UNKNOWN = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 1
        )
        ACTION_NOT_PERMITTED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 2
        )
        CREATE_OPERATION_NOT_PERMITTED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 3
        )
        REMOVE_OPERATION_NOT_PERMITTED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 4
        )
        UPDATE_OPERATION_NOT_PERMITTED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 5
        )
        MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 6
        )
        OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 7
        )
        CREATE_AS_REMOVED_NOT_PERMITTED = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 8
        )
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 9
        )
        OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 10
        )
        MUTATE_NOT_PERMITTED_FOR_CUSTOMER = typing___cast(
            OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 11
        )
    UNSPECIFIED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 0
    )
    UNKNOWN = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 1
    )
    ACTION_NOT_PERMITTED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 2
    )
    CREATE_OPERATION_NOT_PERMITTED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 3
    )
    REMOVE_OPERATION_NOT_PERMITTED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 4
    )
    UPDATE_OPERATION_NOT_PERMITTED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 5
    )
    MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 6
    )
    OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 7
    )
    CREATE_AS_REMOVED_NOT_PERMITTED = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 8
    )
    OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 9
    )
    OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 10
    )
    MUTATE_NOT_PERMITTED_FOR_CUSTOMER = typing___cast(
        OperationAccessDeniedErrorEnum.OperationAccessDeniedErrorValue, 11
    )
    type___OperationAccessDeniedError = OperationAccessDeniedError
    def __init__(self,) -> None: ...

type___OperationAccessDeniedErrorEnum = OperationAccessDeniedErrorEnum