# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v3.proto.resources.payments_account_pb2 import (
    PaymentsAccount as google___ads___googleads___v3___resources___payments_account_pb2___PaymentsAccount,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ListPaymentsAccountsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    def __init__(
        self, *, customer_id: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["customer_id", b"customer_id"]
    ) -> None: ...

type___ListPaymentsAccountsRequest = ListPaymentsAccountsRequest

class ListPaymentsAccountsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def payments_accounts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v3___resources___payments_account_pb2___PaymentsAccount
    ]: ...
    def __init__(
        self,
        *,
        payments_accounts: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v3___resources___payments_account_pb2___PaymentsAccount
            ]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "payments_accounts", b"payments_accounts"
        ],
    ) -> None: ...

type___ListPaymentsAccountsResponse = ListPaymentsAccountsResponse
