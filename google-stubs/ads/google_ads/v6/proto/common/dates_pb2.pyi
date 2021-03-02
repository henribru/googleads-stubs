# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class DateRange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start_date: typing___Text = ...
    end_date: typing___Text = ...
    def __init__(
        self,
        *,
        start_date: typing___Optional[typing___Text] = None,
        end_date: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "end_date",
            b"end_date",
            "start_date",
            b"start_date",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "end_date",
            b"end_date",
            "start_date",
            b"start_date",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_end_date", b"_end_date"]
    ) -> typing_extensions___Literal["end_date"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_start_date", b"_start_date"]
    ) -> typing_extensions___Literal["start_date"]: ...

type___DateRange = DateRange