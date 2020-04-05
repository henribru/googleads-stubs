# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

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


class FeedItemQualityDisapprovalReasonEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FeedItemQualityDisapprovalReason(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason']]: ...
        UNSPECIFIED = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 0)
        UNKNOWN = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 1)
        PRICE_TABLE_REPETITIVE_HEADERS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 2)
        PRICE_TABLE_REPETITIVE_DESCRIPTION = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 3)
        PRICE_TABLE_INCONSISTENT_ROWS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 4)
        PRICE_DESCRIPTION_HAS_PRICE_QUALIFIERS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 5)
        PRICE_UNSUPPORTED_LANGUAGE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 6)
        PRICE_TABLE_ROW_HEADER_TABLE_TYPE_MISMATCH = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 7)
        PRICE_TABLE_ROW_HEADER_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 8)
        PRICE_TABLE_ROW_DESCRIPTION_NOT_RELEVANT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 9)
        PRICE_TABLE_ROW_DESCRIPTION_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 10)
        PRICE_TABLE_ROW_HEADER_DESCRIPTION_REPETITIVE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 11)
        PRICE_TABLE_ROW_UNRATEABLE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 12)
        PRICE_TABLE_ROW_PRICE_INVALID = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 13)
        PRICE_TABLE_ROW_URL_INVALID = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 14)
        PRICE_HEADER_OR_DESCRIPTION_HAS_PRICE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 15)
        STRUCTURED_SNIPPETS_HEADER_POLICY_VIOLATED = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 16)
        STRUCTURED_SNIPPETS_REPEATED_VALUES = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 17)
        STRUCTURED_SNIPPETS_EDITORIAL_GUIDELINES = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 18)
        STRUCTURED_SNIPPETS_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 19)
    UNSPECIFIED = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 0)
    UNKNOWN = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 1)
    PRICE_TABLE_REPETITIVE_HEADERS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 2)
    PRICE_TABLE_REPETITIVE_DESCRIPTION = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 3)
    PRICE_TABLE_INCONSISTENT_ROWS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 4)
    PRICE_DESCRIPTION_HAS_PRICE_QUALIFIERS = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 5)
    PRICE_UNSUPPORTED_LANGUAGE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 6)
    PRICE_TABLE_ROW_HEADER_TABLE_TYPE_MISMATCH = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 7)
    PRICE_TABLE_ROW_HEADER_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 8)
    PRICE_TABLE_ROW_DESCRIPTION_NOT_RELEVANT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 9)
    PRICE_TABLE_ROW_DESCRIPTION_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 10)
    PRICE_TABLE_ROW_HEADER_DESCRIPTION_REPETITIVE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 11)
    PRICE_TABLE_ROW_UNRATEABLE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 12)
    PRICE_TABLE_ROW_PRICE_INVALID = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 13)
    PRICE_TABLE_ROW_URL_INVALID = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 14)
    PRICE_HEADER_OR_DESCRIPTION_HAS_PRICE = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 15)
    STRUCTURED_SNIPPETS_HEADER_POLICY_VIOLATED = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 16)
    STRUCTURED_SNIPPETS_REPEATED_VALUES = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 17)
    STRUCTURED_SNIPPETS_EDITORIAL_GUIDELINES = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 18)
    STRUCTURED_SNIPPETS_HAS_PROMOTIONAL_TEXT = typing___cast('FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason', 19)
    global___FeedItemQualityDisapprovalReason = FeedItemQualityDisapprovalReason


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemQualityDisapprovalReasonEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FeedItemQualityDisapprovalReasonEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___FeedItemQualityDisapprovalReasonEnum = FeedItemQualityDisapprovalReasonEnum
