# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v2.proto.enums.manager_link_status_pb2 import (
    ManagerLinkStatusEnum as google___ads___googleads___v2___enums___manager_link_status_pb2___ManagerLinkStatusEnum,
)

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

class CustomerClientLink(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v2___enums___manager_link_status_pb2___ManagerLinkStatusEnum.ManagerLinkStatusValue = ...
    @property
    def client_customer(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def manager_link_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def hidden(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        client_customer: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        manager_link_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___manager_link_status_pb2___ManagerLinkStatusEnum.ManagerLinkStatusValue
        ] = None,
        hidden: typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "client_customer",
            b"client_customer",
            "hidden",
            b"hidden",
            "manager_link_id",
            b"manager_link_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "client_customer",
            b"client_customer",
            "hidden",
            b"hidden",
            "manager_link_id",
            b"manager_link_id",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

type___CustomerClientLink = CustomerClientLink
