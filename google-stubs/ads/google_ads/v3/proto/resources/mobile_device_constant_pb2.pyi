# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.enums.mobile_device_type_pb2 import (
    MobileDeviceTypeEnum as google___ads___googleads___v3___enums___mobile_device_type_pb2___MobileDeviceTypeEnum,
)

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

class MobileDeviceConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    type = (
        ...
    )  # type: google___ads___googleads___v3___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceType
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def manufacturer_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def operating_system_name(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        manufacturer_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        operating_system_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v3___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceType
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MobileDeviceConstant: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MobileDeviceConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "manufacturer_name",
            b"manufacturer_name",
            "name",
            b"name",
            "operating_system_name",
            b"operating_system_name",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "id",
            b"id",
            "manufacturer_name",
            b"manufacturer_name",
            "name",
            b"name",
            "operating_system_name",
            b"operating_system_name",
            "resource_name",
            b"resource_name",
            "type",
            b"type",
        ],
    ) -> None: ...

global___MobileDeviceConstant = MobileDeviceConstant