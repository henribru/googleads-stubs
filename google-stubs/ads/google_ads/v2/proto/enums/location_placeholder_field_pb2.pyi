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


class LocationPlaceholderFieldEnum(google___protobuf___message___Message):
    class LocationPlaceholderField(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['BUSINESS_NAME'],typing_extensions___Literal['ADDRESS_LINE_1'],typing_extensions___Literal['ADDRESS_LINE_2'],typing_extensions___Literal['CITY'],typing_extensions___Literal['PROVINCE'],typing_extensions___Literal['POSTAL_CODE'],typing_extensions___Literal['COUNTRY_CODE'],typing_extensions___Literal['PHONE_NUMBER']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9]]
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
        BUSINESS_NAME: typing_extensions___Literal[2]
        ADDRESS_LINE_1: typing_extensions___Literal[3]
        ADDRESS_LINE_2: typing_extensions___Literal[4]
        CITY: typing_extensions___Literal[5]
        PROVINCE: typing_extensions___Literal[6]
        POSTAL_CODE: typing_extensions___Literal[7]
        COUNTRY_CODE: typing_extensions___Literal[8]
        PHONE_NUMBER: typing_extensions___Literal[9]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    BUSINESS_NAME: typing_extensions___Literal[2]
    ADDRESS_LINE_1: typing_extensions___Literal[3]
    ADDRESS_LINE_2: typing_extensions___Literal[4]
    CITY: typing_extensions___Literal[5]
    PROVINCE: typing_extensions___Literal[6]
    POSTAL_CODE: typing_extensions___Literal[7]
    COUNTRY_CODE: typing_extensions___Literal[8]
    PHONE_NUMBER: typing_extensions___Literal[9]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LocationPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
