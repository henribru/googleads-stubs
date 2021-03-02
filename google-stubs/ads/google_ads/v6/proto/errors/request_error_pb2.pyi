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

class RequestErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    RequestErrorValue = typing___NewType("RequestErrorValue", builtin___int)
    type___RequestErrorValue = RequestErrorValue
    RequestError: _RequestError
    class _RequestError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            RequestErrorEnum.RequestErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(RequestErrorEnum.RequestErrorValue, 0)
        UNKNOWN = typing___cast(RequestErrorEnum.RequestErrorValue, 1)
        RESOURCE_NAME_MISSING = typing___cast(RequestErrorEnum.RequestErrorValue, 3)
        RESOURCE_NAME_MALFORMED = typing___cast(RequestErrorEnum.RequestErrorValue, 4)
        BAD_RESOURCE_ID = typing___cast(RequestErrorEnum.RequestErrorValue, 17)
        INVALID_CUSTOMER_ID = typing___cast(RequestErrorEnum.RequestErrorValue, 16)
        OPERATION_REQUIRED = typing___cast(RequestErrorEnum.RequestErrorValue, 5)
        RESOURCE_NOT_FOUND = typing___cast(RequestErrorEnum.RequestErrorValue, 6)
        INVALID_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestErrorValue, 7)
        EXPIRED_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestErrorValue, 8)
        INVALID_PAGE_SIZE = typing___cast(RequestErrorEnum.RequestErrorValue, 22)
        REQUIRED_FIELD_MISSING = typing___cast(RequestErrorEnum.RequestErrorValue, 9)
        IMMUTABLE_FIELD = typing___cast(RequestErrorEnum.RequestErrorValue, 11)
        TOO_MANY_MUTATE_OPERATIONS = typing___cast(
            RequestErrorEnum.RequestErrorValue, 13
        )
        CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = typing___cast(
            RequestErrorEnum.RequestErrorValue, 14
        )
        CANNOT_MODIFY_FOREIGN_FIELD = typing___cast(
            RequestErrorEnum.RequestErrorValue, 15
        )
        INVALID_ENUM_VALUE = typing___cast(RequestErrorEnum.RequestErrorValue, 18)
        DEVELOPER_TOKEN_PARAMETER_MISSING = typing___cast(
            RequestErrorEnum.RequestErrorValue, 19
        )
        LOGIN_CUSTOMER_ID_PARAMETER_MISSING = typing___cast(
            RequestErrorEnum.RequestErrorValue, 20
        )
        VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = typing___cast(
            RequestErrorEnum.RequestErrorValue, 21
        )
        CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS = typing___cast(
            RequestErrorEnum.RequestErrorValue, 29
        )
        CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS = typing___cast(
            RequestErrorEnum.RequestErrorValue, 30
        )
        INCONSISTENT_RETURN_SUMMARY_ROW_VALUE = typing___cast(
            RequestErrorEnum.RequestErrorValue, 31
        )
        TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED = typing___cast(
            RequestErrorEnum.RequestErrorValue, 32
        )
        RPC_DEADLINE_TOO_SHORT = typing___cast(RequestErrorEnum.RequestErrorValue, 33)
    UNSPECIFIED = typing___cast(RequestErrorEnum.RequestErrorValue, 0)
    UNKNOWN = typing___cast(RequestErrorEnum.RequestErrorValue, 1)
    RESOURCE_NAME_MISSING = typing___cast(RequestErrorEnum.RequestErrorValue, 3)
    RESOURCE_NAME_MALFORMED = typing___cast(RequestErrorEnum.RequestErrorValue, 4)
    BAD_RESOURCE_ID = typing___cast(RequestErrorEnum.RequestErrorValue, 17)
    INVALID_CUSTOMER_ID = typing___cast(RequestErrorEnum.RequestErrorValue, 16)
    OPERATION_REQUIRED = typing___cast(RequestErrorEnum.RequestErrorValue, 5)
    RESOURCE_NOT_FOUND = typing___cast(RequestErrorEnum.RequestErrorValue, 6)
    INVALID_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestErrorValue, 7)
    EXPIRED_PAGE_TOKEN = typing___cast(RequestErrorEnum.RequestErrorValue, 8)
    INVALID_PAGE_SIZE = typing___cast(RequestErrorEnum.RequestErrorValue, 22)
    REQUIRED_FIELD_MISSING = typing___cast(RequestErrorEnum.RequestErrorValue, 9)
    IMMUTABLE_FIELD = typing___cast(RequestErrorEnum.RequestErrorValue, 11)
    TOO_MANY_MUTATE_OPERATIONS = typing___cast(RequestErrorEnum.RequestErrorValue, 13)
    CANNOT_BE_EXECUTED_BY_MANAGER_ACCOUNT = typing___cast(
        RequestErrorEnum.RequestErrorValue, 14
    )
    CANNOT_MODIFY_FOREIGN_FIELD = typing___cast(RequestErrorEnum.RequestErrorValue, 15)
    INVALID_ENUM_VALUE = typing___cast(RequestErrorEnum.RequestErrorValue, 18)
    DEVELOPER_TOKEN_PARAMETER_MISSING = typing___cast(
        RequestErrorEnum.RequestErrorValue, 19
    )
    LOGIN_CUSTOMER_ID_PARAMETER_MISSING = typing___cast(
        RequestErrorEnum.RequestErrorValue, 20
    )
    VALIDATE_ONLY_REQUEST_HAS_PAGE_TOKEN = typing___cast(
        RequestErrorEnum.RequestErrorValue, 21
    )
    CANNOT_RETURN_SUMMARY_ROW_FOR_REQUEST_WITHOUT_METRICS = typing___cast(
        RequestErrorEnum.RequestErrorValue, 29
    )
    CANNOT_RETURN_SUMMARY_ROW_FOR_VALIDATE_ONLY_REQUESTS = typing___cast(
        RequestErrorEnum.RequestErrorValue, 30
    )
    INCONSISTENT_RETURN_SUMMARY_ROW_VALUE = typing___cast(
        RequestErrorEnum.RequestErrorValue, 31
    )
    TOTAL_RESULTS_COUNT_NOT_ORIGINALLY_REQUESTED = typing___cast(
        RequestErrorEnum.RequestErrorValue, 32
    )
    RPC_DEADLINE_TOO_SHORT = typing___cast(RequestErrorEnum.RequestErrorValue, 33)
    type___RequestError = RequestError
    def __init__(self,) -> None: ...

type___RequestErrorEnum = RequestErrorEnum