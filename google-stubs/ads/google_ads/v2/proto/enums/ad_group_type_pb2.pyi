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

class AdGroupTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AdGroupType(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> "AdGroupTypeEnum.AdGroupType": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["AdGroupTypeEnum.AdGroupType"]: ...
        @classmethod
        def items(
            cls
        ) -> typing___List[
            typing___Tuple[builtin___str, "AdGroupTypeEnum.AdGroupType"]
        ]: ...
        UNSPECIFIED = typing___cast("AdGroupTypeEnum.AdGroupType", 0)
        UNKNOWN = typing___cast("AdGroupTypeEnum.AdGroupType", 1)
        SEARCH_STANDARD = typing___cast("AdGroupTypeEnum.AdGroupType", 2)
        DISPLAY_STANDARD = typing___cast("AdGroupTypeEnum.AdGroupType", 3)
        SHOPPING_PRODUCT_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 4)
        HOTEL_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 6)
        SHOPPING_SMART_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 7)
        VIDEO_BUMPER = typing___cast("AdGroupTypeEnum.AdGroupType", 8)
        VIDEO_TRUE_VIEW_IN_STREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 9)
        VIDEO_TRUE_VIEW_IN_DISPLAY = typing___cast("AdGroupTypeEnum.AdGroupType", 10)
        VIDEO_NON_SKIPPABLE_IN_STREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 11)
        VIDEO_OUTSTREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 12)
        SEARCH_DYNAMIC_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 13)
        SHOPPING_COMPARISON_LISTING_ADS = typing___cast(
            "AdGroupTypeEnum.AdGroupType", 14
        )
    UNSPECIFIED = typing___cast("AdGroupTypeEnum.AdGroupType", 0)
    UNKNOWN = typing___cast("AdGroupTypeEnum.AdGroupType", 1)
    SEARCH_STANDARD = typing___cast("AdGroupTypeEnum.AdGroupType", 2)
    DISPLAY_STANDARD = typing___cast("AdGroupTypeEnum.AdGroupType", 3)
    SHOPPING_PRODUCT_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 4)
    HOTEL_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 6)
    SHOPPING_SMART_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 7)
    VIDEO_BUMPER = typing___cast("AdGroupTypeEnum.AdGroupType", 8)
    VIDEO_TRUE_VIEW_IN_STREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 9)
    VIDEO_TRUE_VIEW_IN_DISPLAY = typing___cast("AdGroupTypeEnum.AdGroupType", 10)
    VIDEO_NON_SKIPPABLE_IN_STREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 11)
    VIDEO_OUTSTREAM = typing___cast("AdGroupTypeEnum.AdGroupType", 12)
    SEARCH_DYNAMIC_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 13)
    SHOPPING_COMPARISON_LISTING_ADS = typing___cast("AdGroupTypeEnum.AdGroupType", 14)
    global___AdGroupType = AdGroupType
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupTypeEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AdGroupTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___AdGroupTypeEnum = AdGroupTypeEnum
