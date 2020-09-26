# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
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

class CustomerClient(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    @property
    def client_customer(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def hidden(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def level(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def time_zone(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def test_account(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def manager(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def descriptive_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        client_customer: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        hidden: typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        level: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        time_zone: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        test_account: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        manager: typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        descriptive_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        currency_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "client_customer",
            b"client_customer",
            "currency_code",
            b"currency_code",
            "descriptive_name",
            b"descriptive_name",
            "hidden",
            b"hidden",
            "id",
            b"id",
            "level",
            b"level",
            "manager",
            b"manager",
            "test_account",
            b"test_account",
            "time_zone",
            b"time_zone",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "client_customer",
            b"client_customer",
            "currency_code",
            b"currency_code",
            "descriptive_name",
            b"descriptive_name",
            "hidden",
            b"hidden",
            "id",
            b"id",
            "level",
            b"level",
            "manager",
            b"manager",
            "resource_name",
            b"resource_name",
            "test_account",
            b"test_account",
            "time_zone",
            b"time_zone",
        ],
    ) -> None: ...

type___CustomerClient = CustomerClient
