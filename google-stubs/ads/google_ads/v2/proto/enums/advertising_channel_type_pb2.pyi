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


class AdvertisingChannelTypeEnum(google___protobuf___message___Message):
    class AdvertisingChannelType(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['SEARCH'],typing_extensions___Literal['DISPLAY'],typing_extensions___Literal['SHOPPING'],typing_extensions___Literal['HOTEL'],typing_extensions___Literal['VIDEO'],typing_extensions___Literal['MULTI_CHANNEL']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7]]
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
        SEARCH: typing_extensions___Literal[2]
        DISPLAY: typing_extensions___Literal[3]
        SHOPPING: typing_extensions___Literal[4]
        HOTEL: typing_extensions___Literal[5]
        VIDEO: typing_extensions___Literal[6]
        MULTI_CHANNEL: typing_extensions___Literal[7]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    SEARCH: typing_extensions___Literal[2]
    DISPLAY: typing_extensions___Literal[3]
    SHOPPING: typing_extensions___Literal[4]
    HOTEL: typing_extensions___Literal[5]
    VIDEO: typing_extensions___Literal[6]
    MULTI_CHANNEL: typing_extensions___Literal[7]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdvertisingChannelTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
