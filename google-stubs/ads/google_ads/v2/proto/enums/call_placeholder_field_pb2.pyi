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


class CallPlaceholderFieldEnum(google___protobuf___message___Message):
    class CallPlaceholderField(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['PHONE_NUMBER'],typing_extensions___Literal['COUNTRY_CODE'],typing_extensions___Literal['TRACKED'],typing_extensions___Literal['CONVERSION_TYPE_ID'],typing_extensions___Literal['CONVERSION_REPORTING_STATE']]
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
        PHONE_NUMBER: typing_extensions___Literal[2]
        COUNTRY_CODE: typing_extensions___Literal[3]
        TRACKED: typing_extensions___Literal[4]
        CONVERSION_TYPE_ID: typing_extensions___Literal[5]
        CONVERSION_REPORTING_STATE: typing_extensions___Literal[6]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    PHONE_NUMBER: typing_extensions___Literal[2]
    COUNTRY_CODE: typing_extensions___Literal[3]
    TRACKED: typing_extensions___Literal[4]
    CONVERSION_TYPE_ID: typing_extensions___Literal[5]
    CONVERSION_REPORTING_STATE: typing_extensions___Literal[6]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CallPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
