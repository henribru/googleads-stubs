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


class CampaignFeedErrorEnum(google___protobuf___message___Message):
    class CampaignFeedError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE'],typing_extensions___Literal['CANNOT_CREATE_FOR_REMOVED_FEED'],typing_extensions___Literal['CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED'],typing_extensions___Literal['CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED'],typing_extensions___Literal['INVALID_PLACEHOLDER_TYPE'],typing_extensions___Literal['MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8]]
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
        FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: typing_extensions___Literal[2]
        CANNOT_CREATE_FOR_REMOVED_FEED: typing_extensions___Literal[4]
        CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: typing_extensions___Literal[5]
        CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: typing_extensions___Literal[6]
        INVALID_PLACEHOLDER_TYPE: typing_extensions___Literal[7]
        MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: typing_extensions___Literal[8]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    FEED_ALREADY_EXISTS_FOR_PLACEHOLDER_TYPE: typing_extensions___Literal[2]
    CANNOT_CREATE_FOR_REMOVED_FEED: typing_extensions___Literal[4]
    CANNOT_CREATE_ALREADY_EXISTING_CAMPAIGN_FEED: typing_extensions___Literal[5]
    CANNOT_MODIFY_REMOVED_CAMPAIGN_FEED: typing_extensions___Literal[6]
    INVALID_PLACEHOLDER_TYPE: typing_extensions___Literal[7]
    MISSING_FEEDMAPPING_FOR_PLACEHOLDER_TYPE: typing_extensions___Literal[8]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CampaignFeedErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
