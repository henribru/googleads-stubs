# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.resources.billing_setup_pb2 import (
    BillingSetup as google___ads___googleads___v1___resources___billing_setup_pb2___BillingSetup,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetBillingSetupRequest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetBillingSetupRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateBillingSetupRequest(google___protobuf___message___Message):
    customer_id = ... # type: typing___Text

    @property
    def operation(self) -> BillingSetupOperation: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operation : typing___Optional[BillingSetupOperation] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateBillingSetupRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operation"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operation",b"operation"]) -> None: ...

class BillingSetupOperation(google___protobuf___message___Message):
    remove = ... # type: typing___Text

    @property
    def create(self) -> google___ads___googleads___v1___resources___billing_setup_pb2___BillingSetup: ...

    def __init__(self,
        *,
        create : typing___Optional[google___ads___googleads___v1___resources___billing_setup_pb2___BillingSetup] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BillingSetupOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["create","remove"]: ...

class MutateBillingSetupResponse(google___protobuf___message___Message):

    @property
    def result(self) -> MutateBillingSetupResult: ...

    def __init__(self,
        *,
        result : typing___Optional[MutateBillingSetupResult] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateBillingSetupResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> None: ...

class MutateBillingSetupResult(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateBillingSetupResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
