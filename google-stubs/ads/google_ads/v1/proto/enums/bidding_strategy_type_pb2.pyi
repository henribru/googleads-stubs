# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

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

class BiddingStrategyTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class BiddingStrategyType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "BiddingStrategyTypeEnum.BiddingStrategyType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls
        ) -> typing___List["BiddingStrategyTypeEnum.BiddingStrategyType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "BiddingStrategyTypeEnum.BiddingStrategyType"]
        ]: ...
        UNSPECIFIED = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 0)
        UNKNOWN = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 1)
        COMMISSION = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 16)
        ENHANCED_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 2)
        MANUAL_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 3)
        MANUAL_CPM = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 4)
        MANUAL_CPV = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 13)
        MAXIMIZE_CONVERSIONS = typing___cast(
            "BiddingStrategyTypeEnum.BiddingStrategyType", 10
        )
        MAXIMIZE_CONVERSION_VALUE = typing___cast(
            "BiddingStrategyTypeEnum.BiddingStrategyType", 11
        )
        PAGE_ONE_PROMOTED = typing___cast(
            "BiddingStrategyTypeEnum.BiddingStrategyType", 5
        )
        PERCENT_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 12)
        TARGET_CPA = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 6)
        TARGET_CPM = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 14)
        TARGET_IMPRESSION_SHARE = typing___cast(
            "BiddingStrategyTypeEnum.BiddingStrategyType", 15
        )
        TARGET_OUTRANK_SHARE = typing___cast(
            "BiddingStrategyTypeEnum.BiddingStrategyType", 7
        )
        TARGET_ROAS = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 8)
        TARGET_SPEND = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 9)
    UNSPECIFIED = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 0)
    UNKNOWN = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 1)
    COMMISSION = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 16)
    ENHANCED_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 2)
    MANUAL_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 3)
    MANUAL_CPM = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 4)
    MANUAL_CPV = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 13)
    MAXIMIZE_CONVERSIONS = typing___cast(
        "BiddingStrategyTypeEnum.BiddingStrategyType", 10
    )
    MAXIMIZE_CONVERSION_VALUE = typing___cast(
        "BiddingStrategyTypeEnum.BiddingStrategyType", 11
    )
    PAGE_ONE_PROMOTED = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 5)
    PERCENT_CPC = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 12)
    TARGET_CPA = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 6)
    TARGET_CPM = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 14)
    TARGET_IMPRESSION_SHARE = typing___cast(
        "BiddingStrategyTypeEnum.BiddingStrategyType", 15
    )
    TARGET_OUTRANK_SHARE = typing___cast(
        "BiddingStrategyTypeEnum.BiddingStrategyType", 7
    )
    TARGET_ROAS = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 8)
    TARGET_SPEND = typing___cast("BiddingStrategyTypeEnum.BiddingStrategyType", 9)
    global___BiddingStrategyType = BiddingStrategyType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BiddingStrategyTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> BiddingStrategyTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___BiddingStrategyTypeEnum = BiddingStrategyTypeEnum
