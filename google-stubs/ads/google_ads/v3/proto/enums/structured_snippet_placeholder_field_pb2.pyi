# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class StructuredSnippetPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    StructuredSnippetPlaceholderFieldValue = typing___NewType(
        "StructuredSnippetPlaceholderFieldValue", builtin___int
    )
    type___StructuredSnippetPlaceholderFieldValue = (
        StructuredSnippetPlaceholderFieldValue
    )
    StructuredSnippetPlaceholderField: _StructuredSnippetPlaceholderField
    class _StructuredSnippetPlaceholderField(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue,
            0,
        )
        UNKNOWN = typing___cast(
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue,
            1,
        )
        HEADER = typing___cast(
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue,
            2,
        )
        SNIPPETS = typing___cast(
            StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue,
            3,
        )
    UNSPECIFIED = typing___cast(
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue, 0
    )
    UNKNOWN = typing___cast(
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue, 1
    )
    HEADER = typing___cast(
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue, 2
    )
    SNIPPETS = typing___cast(
        StructuredSnippetPlaceholderFieldEnum.StructuredSnippetPlaceholderFieldValue, 3
    )
    type___StructuredSnippetPlaceholderField = StructuredSnippetPlaceholderField
    def __init__(self,) -> None: ...

type___StructuredSnippetPlaceholderFieldEnum = StructuredSnippetPlaceholderFieldEnum
