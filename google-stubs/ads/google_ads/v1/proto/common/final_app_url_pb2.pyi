# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.app_url_operating_system_type_pb2 import (
    AppUrlOperatingSystemTypeEnum as google___ads___googleads___v1___enums___app_url_operating_system_type_pb2___AppUrlOperatingSystemTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import Optional as typing___Optional, Union as typing___Union

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class FinalAppUrl(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    os_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___app_url_operating_system_type_pb2___AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        os_type: typing___Optional[
            google___ads___googleads___v1___enums___app_url_operating_system_type_pb2___AppUrlOperatingSystemTypeEnum.AppUrlOperatingSystemType
        ] = None,
        url: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FinalAppUrl: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FinalAppUrl: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["url", b"url"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["os_type", b"os_type", "url", b"url"],
    ) -> None: ...

global___FinalAppUrl = FinalAppUrl
