# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class OperationAccessDeniedErrorEnum(google___protobuf___message___Message):
    class OperationAccessDeniedError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['ACTION_NOT_PERMITTED'],typing_extensions___Literal['CREATE_OPERATION_NOT_PERMITTED'],typing_extensions___Literal['REMOVE_OPERATION_NOT_PERMITTED'],typing_extensions___Literal['UPDATE_OPERATION_NOT_PERMITTED'],typing_extensions___Literal['MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT'],typing_extensions___Literal['OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE'],typing_extensions___Literal['CREATE_AS_REMOVED_NOT_PERMITTED'],typing_extensions___Literal['OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE'],typing_extensions___Literal['OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE'],typing_extensions___Literal['MUTATE_NOT_PERMITTED_FOR_CUSTOMER']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11]]
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: ClosedValueType) -> str: ...
        @classmethod
        def Value(cls, name: ClosedKeyType) -> ClosedValueType: ...
        @classmethod
        def keys(cls) -> typing___List[ClosedKeyType]: ...
        @classmethod
        def values(cls) -> typing___List[ClosedValueType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[ClosedKeyType, ClosedValueType]]: ...
        UNSPECIFIED: typing_extensions___Literal[0]
        UNKNOWN: typing_extensions___Literal[1]
        ACTION_NOT_PERMITTED: typing_extensions___Literal[2]
        CREATE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[3]
        REMOVE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[4]
        UPDATE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[5]
        MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: typing_extensions___Literal[6]
        OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: typing_extensions___Literal[7]
        CREATE_AS_REMOVED_NOT_PERMITTED: typing_extensions___Literal[8]
        OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: typing_extensions___Literal[9]
        OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: typing_extensions___Literal[10]
        MUTATE_NOT_PERMITTED_FOR_CUSTOMER: typing_extensions___Literal[11]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    ACTION_NOT_PERMITTED: typing_extensions___Literal[2]
    CREATE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[3]
    REMOVE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[4]
    UPDATE_OPERATION_NOT_PERMITTED: typing_extensions___Literal[5]
    MUTATE_ACTION_NOT_PERMITTED_FOR_CLIENT: typing_extensions___Literal[6]
    OPERATION_NOT_PERMITTED_FOR_CAMPAIGN_TYPE: typing_extensions___Literal[7]
    CREATE_AS_REMOVED_NOT_PERMITTED: typing_extensions___Literal[8]
    OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE: typing_extensions___Literal[9]
    OPERATION_NOT_PERMITTED_FOR_AD_GROUP_TYPE: typing_extensions___Literal[10]
    MUTATE_NOT_PERMITTED_FOR_CUSTOMER: typing_extensions___Literal[11]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> OperationAccessDeniedErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
