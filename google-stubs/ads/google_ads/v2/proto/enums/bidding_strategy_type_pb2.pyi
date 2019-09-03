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


class BiddingStrategyTypeEnum(google___protobuf___message___Message):
    class BiddingStrategyType(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['COMMISSION'],typing_extensions___Literal['ENHANCED_CPC'],typing_extensions___Literal['MANUAL_CPC'],typing_extensions___Literal['MANUAL_CPM'],typing_extensions___Literal['MANUAL_CPV'],typing_extensions___Literal['MAXIMIZE_CONVERSIONS'],typing_extensions___Literal['MAXIMIZE_CONVERSION_VALUE'],typing_extensions___Literal['PAGE_ONE_PROMOTED'],typing_extensions___Literal['PERCENT_CPC'],typing_extensions___Literal['TARGET_CPA'],typing_extensions___Literal['TARGET_CPM'],typing_extensions___Literal['TARGET_IMPRESSION_SHARE'],typing_extensions___Literal['TARGET_OUTRANK_SHARE'],typing_extensions___Literal['TARGET_ROAS'],typing_extensions___Literal['TARGET_SPEND']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[16],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[13],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[5],typing_extensions___Literal[12],typing_extensions___Literal[6],typing_extensions___Literal[14],typing_extensions___Literal[15],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9]]
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
        COMMISSION: typing_extensions___Literal[16]
        ENHANCED_CPC: typing_extensions___Literal[2]
        MANUAL_CPC: typing_extensions___Literal[3]
        MANUAL_CPM: typing_extensions___Literal[4]
        MANUAL_CPV: typing_extensions___Literal[13]
        MAXIMIZE_CONVERSIONS: typing_extensions___Literal[10]
        MAXIMIZE_CONVERSION_VALUE: typing_extensions___Literal[11]
        PAGE_ONE_PROMOTED: typing_extensions___Literal[5]
        PERCENT_CPC: typing_extensions___Literal[12]
        TARGET_CPA: typing_extensions___Literal[6]
        TARGET_CPM: typing_extensions___Literal[14]
        TARGET_IMPRESSION_SHARE: typing_extensions___Literal[15]
        TARGET_OUTRANK_SHARE: typing_extensions___Literal[7]
        TARGET_ROAS: typing_extensions___Literal[8]
        TARGET_SPEND: typing_extensions___Literal[9]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    COMMISSION: typing_extensions___Literal[16]
    ENHANCED_CPC: typing_extensions___Literal[2]
    MANUAL_CPC: typing_extensions___Literal[3]
    MANUAL_CPM: typing_extensions___Literal[4]
    MANUAL_CPV: typing_extensions___Literal[13]
    MAXIMIZE_CONVERSIONS: typing_extensions___Literal[10]
    MAXIMIZE_CONVERSION_VALUE: typing_extensions___Literal[11]
    PAGE_ONE_PROMOTED: typing_extensions___Literal[5]
    PERCENT_CPC: typing_extensions___Literal[12]
    TARGET_CPA: typing_extensions___Literal[6]
    TARGET_CPM: typing_extensions___Literal[14]
    TARGET_IMPRESSION_SHARE: typing_extensions___Literal[15]
    TARGET_OUTRANK_SHARE: typing_extensions___Literal[7]
    TARGET_ROAS: typing_extensions___Literal[8]
    TARGET_SPEND: typing_extensions___Literal[9]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BiddingStrategyTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
