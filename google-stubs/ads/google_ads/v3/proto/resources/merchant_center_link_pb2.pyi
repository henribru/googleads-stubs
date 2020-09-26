# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v3.proto.enums.merchant_center_link_status_pb2 import (
    MerchantCenterLinkStatusEnum as google___ads___googleads___v3___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum,
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

class MerchantCenterLink(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v3___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def merchant_center_account_name(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        merchant_center_account_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v3___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "id", b"id", "merchant_center_account_name", b"merchant_center_account_name"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "merchant_center_account_name",
            b"merchant_center_account_name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

type___MerchantCenterLink = MerchantCenterLink
