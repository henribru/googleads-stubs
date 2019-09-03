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


class ResourceCountLimitExceededErrorEnum(google___protobuf___message___Message):
    class ResourceCountLimitExceededError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['ACCOUNT_LIMIT'],typing_extensions___Literal['CAMPAIGN_LIMIT'],typing_extensions___Literal['ADGROUP_LIMIT'],typing_extensions___Literal['AD_GROUP_AD_LIMIT'],typing_extensions___Literal['AD_GROUP_CRITERION_LIMIT'],typing_extensions___Literal['SHARED_SET_LIMIT'],typing_extensions___Literal['MATCHING_FUNCTION_LIMIT'],typing_extensions___Literal['RESPONSE_ROW_LIMIT_EXCEEDED'],typing_extensions___Literal['RESOURCE_LIMIT']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10]]
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
        ACCOUNT_LIMIT: typing_extensions___Literal[2]
        CAMPAIGN_LIMIT: typing_extensions___Literal[3]
        ADGROUP_LIMIT: typing_extensions___Literal[4]
        AD_GROUP_AD_LIMIT: typing_extensions___Literal[5]
        AD_GROUP_CRITERION_LIMIT: typing_extensions___Literal[6]
        SHARED_SET_LIMIT: typing_extensions___Literal[7]
        MATCHING_FUNCTION_LIMIT: typing_extensions___Literal[8]
        RESPONSE_ROW_LIMIT_EXCEEDED: typing_extensions___Literal[9]
        RESOURCE_LIMIT: typing_extensions___Literal[10]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    ACCOUNT_LIMIT: typing_extensions___Literal[2]
    CAMPAIGN_LIMIT: typing_extensions___Literal[3]
    ADGROUP_LIMIT: typing_extensions___Literal[4]
    AD_GROUP_AD_LIMIT: typing_extensions___Literal[5]
    AD_GROUP_CRITERION_LIMIT: typing_extensions___Literal[6]
    SHARED_SET_LIMIT: typing_extensions___Literal[7]
    MATCHING_FUNCTION_LIMIT: typing_extensions___Literal[8]
    RESPONSE_ROW_LIMIT_EXCEEDED: typing_extensions___Literal[9]
    RESOURCE_LIMIT: typing_extensions___Literal[10]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ResourceCountLimitExceededErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
