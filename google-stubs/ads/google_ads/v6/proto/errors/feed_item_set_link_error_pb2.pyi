# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FeedItemSetLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    FeedItemSetLinkErrorValue = typing___NewType(
        "FeedItemSetLinkErrorValue", builtin___int
    )
    type___FeedItemSetLinkErrorValue = FeedItemSetLinkErrorValue
    FeedItemSetLinkError: _FeedItemSetLinkError
    class _FeedItemSetLinkError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 0
        )
        UNKNOWN = typing___cast(FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 1)
        FEED_ID_MISMATCH = typing___cast(
            FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 2
        )
        NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET = typing___cast(
            FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 3
        )
    UNSPECIFIED = typing___cast(FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 0)
    UNKNOWN = typing___cast(FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 1)
    FEED_ID_MISMATCH = typing___cast(
        FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 2
    )
    NO_MUTATE_ALLOWED_FOR_DYNAMIC_SET = typing___cast(
        FeedItemSetLinkErrorEnum.FeedItemSetLinkErrorValue, 3
    )
    type___FeedItemSetLinkError = FeedItemSetLinkError
    def __init__(self,) -> None: ...

type___FeedItemSetLinkErrorEnum = FeedItemSetLinkErrorEnum