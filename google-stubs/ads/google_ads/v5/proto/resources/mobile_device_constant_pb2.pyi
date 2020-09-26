# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.mobile_device_type_pb2 import (
    MobileDeviceTypeEnum as google___ads___googleads___v5___enums___mobile_device_type_pb2___MobileDeviceTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class MobileDeviceConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    name: typing___Text = ...
    manufacturer_name: typing___Text = ...
    operating_system_name: typing___Text = ...
    type: google___ads___googleads___v5___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceTypeValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        manufacturer_name: typing___Optional[typing___Text] = None,
        operating_system_name: typing___Optional[typing___Text] = None,
        type: typing___Optional[
            google___ads___googleads___v5___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_manufacturer_name",
            b"_manufacturer_name",
            "_name",
            b"_name",
            "_operating_system_name",
            b"_operating_system_name",
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
            "_id",
            b"_id",
            "_manufacturer_name",
            b"_manufacturer_name",
            "_name",
            b"_name",
            "_operating_system_name",
            b"_operating_system_name",
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
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_manufacturer_name", b"_manufacturer_name"
        ],
    ) -> typing_extensions___Literal["manufacturer_name"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_operating_system_name", b"_operating_system_name"
        ],
    ) -> typing_extensions___Literal["operating_system_name"]: ...

type___MobileDeviceConstant = MobileDeviceConstant
