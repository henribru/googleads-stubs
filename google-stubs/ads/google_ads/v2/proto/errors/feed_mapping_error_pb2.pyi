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


class FeedMappingErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedMappingError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'FeedMappingErrorEnum.FeedMappingError': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['FeedMappingErrorEnum.FeedMappingError']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'FeedMappingErrorEnum.FeedMappingError']]: ...
        UNSPECIFIED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 0)
        UNKNOWN = typing___cast('FeedMappingErrorEnum.FeedMappingError', 1)
        INVALID_PLACEHOLDER_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 2)
        INVALID_CRITERION_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 3)
        INVALID_PLACEHOLDER_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 4)
        INVALID_CRITERION_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 5)
        NO_ATTRIBUTE_FIELD_MAPPINGS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 7)
        FEED_ATTRIBUTE_TYPE_MISMATCH = typing___cast('FeedMappingErrorEnum.FeedMappingError', 8)
        CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 9)
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 10)
        MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 11)
        MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 12)
        MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 13)
        UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 14)
        LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 15)
        CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 16)
        INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 17)
        INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 18)
    UNSPECIFIED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 0)
    UNKNOWN = typing___cast('FeedMappingErrorEnum.FeedMappingError', 1)
    INVALID_PLACEHOLDER_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 2)
    INVALID_CRITERION_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 3)
    INVALID_PLACEHOLDER_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 4)
    INVALID_CRITERION_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 5)
    NO_ATTRIBUTE_FIELD_MAPPINGS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 7)
    FEED_ATTRIBUTE_TYPE_MISMATCH = typing___cast('FeedMappingErrorEnum.FeedMappingError', 8)
    CANNOT_OPERATE_ON_MAPPINGS_FOR_SYSTEM_GENERATED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 9)
    MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 10)
    MULTIPLE_MAPPINGS_FOR_CRITERION_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 11)
    MULTIPLE_MAPPINGS_FOR_PLACEHOLDER_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 12)
    MULTIPLE_MAPPINGS_FOR_CRITERION_FIELD = typing___cast('FeedMappingErrorEnum.FeedMappingError', 13)
    UNEXPECTED_ATTRIBUTE_FIELD_MAPPINGS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 14)
    LOCATION_PLACEHOLDER_ONLY_FOR_PLACES_FEEDS = typing___cast('FeedMappingErrorEnum.FeedMappingError', 15)
    CANNOT_MODIFY_MAPPINGS_FOR_TYPED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 16)
    INVALID_PLACEHOLDER_TYPE_FOR_NON_SYSTEM_GENERATED_FEED = typing___cast('FeedMappingErrorEnum.FeedMappingError', 17)
    INVALID_PLACEHOLDER_TYPE_FOR_SYSTEM_GENERATED_FEED_TYPE = typing___cast('FeedMappingErrorEnum.FeedMappingError', 18)
    global___FeedMappingError = FeedMappingError


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedMappingErrorEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FeedMappingErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___FeedMappingErrorEnum = FeedMappingErrorEnum
