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


class MultiplierErrorEnum(google___protobuf___message___Message):
    class MultiplierError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['MULTIPLIER_TOO_HIGH'],typing_extensions___Literal['MULTIPLIER_TOO_LOW'],typing_extensions___Literal['TOO_MANY_FRACTIONAL_DIGITS'],typing_extensions___Literal['MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY'],typing_extensions___Literal['MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING'],typing_extensions___Literal['NO_MULTIPLIER_SPECIFIED'],typing_extensions___Literal['MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET'],typing_extensions___Literal['MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET'],typing_extensions___Literal['MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET'],typing_extensions___Literal['MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID'],typing_extensions___Literal['BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER'],typing_extensions___Literal['MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13]]
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
        MULTIPLIER_TOO_HIGH: typing_extensions___Literal[2]
        MULTIPLIER_TOO_LOW: typing_extensions___Literal[3]
        TOO_MANY_FRACTIONAL_DIGITS: typing_extensions___Literal[4]
        MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY: typing_extensions___Literal[5]
        MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING: typing_extensions___Literal[6]
        NO_MULTIPLIER_SPECIFIED: typing_extensions___Literal[7]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET: typing_extensions___Literal[8]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET: typing_extensions___Literal[9]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET: typing_extensions___Literal[10]
        MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID: typing_extensions___Literal[11]
        BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER: typing_extensions___Literal[12]
        MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH: typing_extensions___Literal[13]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    MULTIPLIER_TOO_HIGH: typing_extensions___Literal[2]
    MULTIPLIER_TOO_LOW: typing_extensions___Literal[3]
    TOO_MANY_FRACTIONAL_DIGITS: typing_extensions___Literal[4]
    MULTIPLIER_NOT_ALLOWED_FOR_BIDDING_STRATEGY: typing_extensions___Literal[5]
    MULTIPLIER_NOT_ALLOWED_WHEN_BASE_BID_IS_MISSING: typing_extensions___Literal[6]
    NO_MULTIPLIER_SPECIFIED: typing_extensions___Literal[7]
    MULTIPLIER_CAUSES_BID_TO_EXCEED_DAILY_BUDGET: typing_extensions___Literal[8]
    MULTIPLIER_CAUSES_BID_TO_EXCEED_MONTHLY_BUDGET: typing_extensions___Literal[9]
    MULTIPLIER_CAUSES_BID_TO_EXCEED_CUSTOM_BUDGET: typing_extensions___Literal[10]
    MULTIPLIER_CAUSES_BID_TO_EXCEED_MAX_ALLOWED_BID: typing_extensions___Literal[11]
    BID_LESS_THAN_MIN_ALLOWED_BID_WITH_MULTIPLIER: typing_extensions___Literal[12]
    MULTIPLIER_AND_BIDDING_STRATEGY_TYPE_MISMATCH: typing_extensions___Literal[13]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MultiplierErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
