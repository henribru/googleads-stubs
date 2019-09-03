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


class ExtensionTypeEnum(google___protobuf___message___Message):
    class ExtensionType(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['NONE'],typing_extensions___Literal['APP'],typing_extensions___Literal['CALL'],typing_extensions___Literal['CALLOUT'],typing_extensions___Literal['MESSAGE'],typing_extensions___Literal['PRICE'],typing_extensions___Literal['PROMOTION'],typing_extensions___Literal['SITELINK'],typing_extensions___Literal['STRUCTURED_SNIPPET'],typing_extensions___Literal['LOCATION'],typing_extensions___Literal['AFFILIATE_LOCATION']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13]]
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
        NONE: typing_extensions___Literal[2]
        APP: typing_extensions___Literal[3]
        CALL: typing_extensions___Literal[4]
        CALLOUT: typing_extensions___Literal[5]
        MESSAGE: typing_extensions___Literal[6]
        PRICE: typing_extensions___Literal[7]
        PROMOTION: typing_extensions___Literal[8]
        SITELINK: typing_extensions___Literal[10]
        STRUCTURED_SNIPPET: typing_extensions___Literal[11]
        LOCATION: typing_extensions___Literal[12]
        AFFILIATE_LOCATION: typing_extensions___Literal[13]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    NONE: typing_extensions___Literal[2]
    APP: typing_extensions___Literal[3]
    CALL: typing_extensions___Literal[4]
    CALLOUT: typing_extensions___Literal[5]
    MESSAGE: typing_extensions___Literal[6]
    PRICE: typing_extensions___Literal[7]
    PROMOTION: typing_extensions___Literal[8]
    SITELINK: typing_extensions___Literal[10]
    STRUCTURED_SNIPPET: typing_extensions___Literal[11]
    LOCATION: typing_extensions___Literal[12]
    AFFILIATE_LOCATION: typing_extensions___Literal[13]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ExtensionTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
