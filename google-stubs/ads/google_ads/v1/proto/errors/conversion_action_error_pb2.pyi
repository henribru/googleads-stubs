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


class ConversionActionErrorEnum(google___protobuf___message___Message):
    class ConversionActionError(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['DUPLICATE_NAME'],typing_extensions___Literal['DUPLICATE_APP_ID'],typing_extensions___Literal['TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD'],typing_extensions___Literal['BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION'],typing_extensions___Literal['DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED'],typing_extensions___Literal['DATA_DRIVEN_MODEL_EXPIRED'],typing_extensions___Literal['DATA_DRIVEN_MODEL_STALE'],typing_extensions___Literal['DATA_DRIVEN_MODEL_UNKNOWN']]
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
        DUPLICATE_NAME: typing_extensions___Literal[2]
        DUPLICATE_APP_ID: typing_extensions___Literal[3]
        TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD: typing_extensions___Literal[4]
        BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION: typing_extensions___Literal[5]
        DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED: typing_extensions___Literal[6]
        DATA_DRIVEN_MODEL_EXPIRED: typing_extensions___Literal[7]
        DATA_DRIVEN_MODEL_STALE: typing_extensions___Literal[8]
        DATA_DRIVEN_MODEL_UNKNOWN: typing_extensions___Literal[9]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    DUPLICATE_NAME: typing_extensions___Literal[2]
    DUPLICATE_APP_ID: typing_extensions___Literal[3]
    TWO_CONVERSION_ACTIONS_BIDDING_ON_SAME_APP_DOWNLOAD: typing_extensions___Literal[4]
    BIDDING_ON_SAME_APP_DOWNLOAD_AS_GLOBAL_ACTION: typing_extensions___Literal[5]
    DATA_DRIVEN_MODEL_WAS_NEVER_GENERATED: typing_extensions___Literal[6]
    DATA_DRIVEN_MODEL_EXPIRED: typing_extensions___Literal[7]
    DATA_DRIVEN_MODEL_STALE: typing_extensions___Literal[8]
    DATA_DRIVEN_MODEL_UNKNOWN: typing_extensions___Literal[9]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConversionActionErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
