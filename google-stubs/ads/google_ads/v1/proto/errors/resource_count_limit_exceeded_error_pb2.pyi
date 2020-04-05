# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

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


class ResourceCountLimitExceededErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ResourceCountLimitExceededError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError']]: ...
        UNSPECIFIED = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 0)
        UNKNOWN = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 1)
        ACCOUNT_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 2)
        CAMPAIGN_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 3)
        ADGROUP_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 4)
        AD_GROUP_AD_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 5)
        AD_GROUP_CRITERION_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 6)
        SHARED_SET_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 7)
        MATCHING_FUNCTION_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 8)
        RESPONSE_ROW_LIMIT_EXCEEDED = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 9)
    UNSPECIFIED = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 0)
    UNKNOWN = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 1)
    ACCOUNT_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 2)
    CAMPAIGN_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 3)
    ADGROUP_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 4)
    AD_GROUP_AD_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 5)
    AD_GROUP_CRITERION_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 6)
    SHARED_SET_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 7)
    MATCHING_FUNCTION_LIMIT = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 8)
    RESPONSE_ROW_LIMIT_EXCEEDED = typing___cast('ResourceCountLimitExceededErrorEnum.ResourceCountLimitExceededError', 9)
    global___ResourceCountLimitExceededError = ResourceCountLimitExceededError


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ResourceCountLimitExceededErrorEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ResourceCountLimitExceededErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___ResourceCountLimitExceededErrorEnum = ResourceCountLimitExceededErrorEnum
