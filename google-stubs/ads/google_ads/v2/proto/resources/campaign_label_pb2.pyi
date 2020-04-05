# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class CampaignLabel(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    @property
    def campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def label(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        campaign : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        label : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CampaignLabel: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CampaignLabel: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"campaign",b"campaign",u"label",b"label"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"campaign",b"campaign",u"label",b"label",u"resource_name",b"resource_name"]) -> None: ...
global___CampaignLabel = CampaignLabel
