# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CustomerClient(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

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

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        client_customer : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        hidden : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        level : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        time_zone : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        test_account : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        manager : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        descriptive_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        currency_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomerClient: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"client_customer",u"currency_code",u"descriptive_name",u"hidden",u"id",u"level",u"manager",u"test_account",u"time_zone"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"client_customer",u"currency_code",u"descriptive_name",u"hidden",u"id",u"level",u"manager",u"resource_name",u"test_account",u"time_zone"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"client_customer",b"client_customer",u"currency_code",b"currency_code",u"descriptive_name",b"descriptive_name",u"hidden",b"hidden",u"id",b"id",u"level",b"level",u"manager",b"manager",u"test_account",b"test_account",u"time_zone",b"time_zone"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"client_customer",b"client_customer",u"currency_code",b"currency_code",u"descriptive_name",b"descriptive_name",u"hidden",b"hidden",u"id",b"id",u"level",b"level",u"manager",b"manager",u"resource_name",b"resource_name",u"test_account",b"test_account",u"time_zone",b"time_zone"]) -> None: ...
