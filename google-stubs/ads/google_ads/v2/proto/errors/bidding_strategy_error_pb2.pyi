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


class BiddingStrategyErrorEnum(google___protobuf___message___Message):
    class BiddingStrategyError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['DUPLICATE_NAME'],typing_extensions___Literal['CANNOT_CHANGE_BIDDING_STRATEGY_TYPE'],typing_extensions___Literal['CANNOT_REMOVE_ASSOCIATED_STRATEGY'],typing_extensions___Literal['BIDDING_STRATEGY_NOT_SUPPORTED'],typing_extensions___Literal['INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6]]
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
        DUPLICATE_NAME: typing_extensions___Literal[2]
        CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: typing_extensions___Literal[3]
        CANNOT_REMOVE_ASSOCIATED_STRATEGY: typing_extensions___Literal[4]
        BIDDING_STRATEGY_NOT_SUPPORTED: typing_extensions___Literal[5]
        INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: typing_extensions___Literal[6]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    DUPLICATE_NAME: typing_extensions___Literal[2]
    CANNOT_CHANGE_BIDDING_STRATEGY_TYPE: typing_extensions___Literal[3]
    CANNOT_REMOVE_ASSOCIATED_STRATEGY: typing_extensions___Literal[4]
    BIDDING_STRATEGY_NOT_SUPPORTED: typing_extensions___Literal[5]
    INCOMPATIBLE_BIDDING_STRATEGY_AND_BIDDING_STRATEGY_GOAL_TYPE: typing_extensions___Literal[6]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BiddingStrategyErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
