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


class UserListTypeEnum(google___protobuf___message___Message):
    class UserListType(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['REMARKETING'],typing_extensions___Literal['LOGICAL'],typing_extensions___Literal['EXTERNAL_REMARKETING'],typing_extensions___Literal['RULE_BASED'],typing_extensions___Literal['SIMILAR'],typing_extensions___Literal['CRM_BASED']]
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
        REMARKETING: typing_extensions___Literal[2]
        LOGICAL: typing_extensions___Literal[3]
        EXTERNAL_REMARKETING: typing_extensions___Literal[4]
        RULE_BASED: typing_extensions___Literal[5]
        SIMILAR: typing_extensions___Literal[6]
        CRM_BASED: typing_extensions___Literal[7]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    REMARKETING: typing_extensions___Literal[2]
    LOGICAL: typing_extensions___Literal[3]
    EXTERNAL_REMARKETING: typing_extensions___Literal[4]
    RULE_BASED: typing_extensions___Literal[5]
    SIMILAR: typing_extensions___Literal[6]
    CRM_BASED: typing_extensions___Literal[7]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UserListTypeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
