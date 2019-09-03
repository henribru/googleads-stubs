# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.operating_system_version_operator_type_pb2 import (
    OperatingSystemVersionOperatorTypeEnum as google___ads___googleads___v1___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
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


class OperatingSystemVersionConstant(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    operator_type = ... # type: google___ads___googleads___v1___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def os_major_version(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

    @property
    def os_minor_version(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        os_major_version : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        os_minor_version : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        operator_type : typing___Optional[google___ads___googleads___v1___enums___operating_system_version_operator_type_pb2___OperatingSystemVersionOperatorTypeEnum.OperatingSystemVersionOperatorType.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> OperatingSystemVersionConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"id",u"name",u"os_major_version",u"os_minor_version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"name",u"operator_type",u"os_major_version",u"os_minor_version",u"resource_name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"os_major_version",b"os_major_version",u"os_minor_version",b"os_minor_version"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name",u"operator_type",b"operator_type",u"os_major_version",b"os_major_version",u"os_minor_version",b"os_minor_version",u"resource_name",b"resource_name"]) -> None: ...
