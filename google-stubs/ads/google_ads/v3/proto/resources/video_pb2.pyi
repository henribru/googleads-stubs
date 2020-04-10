# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class Video(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    @property
    def id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def channel_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def duration_millis(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def title(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        channel_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        duration_millis: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        title: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Video: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Video: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "channel_id",
            b"channel_id",
            "duration_millis",
            b"duration_millis",
            "id",
            b"id",
            "title",
            b"title",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "channel_id",
            b"channel_id",
            "duration_millis",
            b"duration_millis",
            "id",
            b"id",
            "resource_name",
            b"resource_name",
            "title",
            b"title",
        ],
    ) -> None: ...

global___Video = Video