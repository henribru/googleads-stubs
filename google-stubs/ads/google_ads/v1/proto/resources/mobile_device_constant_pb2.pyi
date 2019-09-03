# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.mobile_device_type_pb2 import (
    MobileDeviceTypeEnum as google___ads___googleads___v1___enums___mobile_device_type_pb2___MobileDeviceTypeEnum,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
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


class MobileDeviceConstant(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    type = ... # type: google___ads___googleads___v1___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceType.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def manufacturer_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def operating_system_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        manufacturer_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        operating_system_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___mobile_device_type_pb2___MobileDeviceTypeEnum.MobileDeviceType.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MobileDeviceConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"id",u"manufacturer_name",u"name",u"operating_system_name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"manufacturer_name",u"name",u"operating_system_name",u"resource_name",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"manufacturer_name",b"manufacturer_name",u"name",b"name",u"operating_system_name",b"operating_system_name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"manufacturer_name",b"manufacturer_name",u"name",b"name",u"operating_system_name",b"operating_system_name",u"resource_name",b"resource_name",u"type",b"type"]) -> None: ...
