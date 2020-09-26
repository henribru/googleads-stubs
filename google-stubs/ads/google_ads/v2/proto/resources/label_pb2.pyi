# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v2.proto.common.text_label_pb2 import (
    TextLabel as google___ads___googleads___v2___common___text_label_pb2___TextLabel,
)

from google.ads.google_ads.v2.proto.enums.label_status_pb2 import (
    LabelStatusEnum as google___ads___googleads___v2___enums___label_status_pb2___LabelStatusEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Label(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v2___enums___label_status_pb2___LabelStatusEnum.LabelStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def text_label(
        self,
    ) -> google___ads___googleads___v2___common___text_label_pb2___TextLabel: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___label_status_pb2___LabelStatusEnum.LabelStatusValue
        ] = None,
        text_label: typing___Optional[
            google___ads___googleads___v2___common___text_label_pb2___TextLabel
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "id", b"id", "name", b"name", "text_label", b"text_label"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "text_label",
            b"text_label",
        ],
    ) -> None: ...

type___Label = Label
