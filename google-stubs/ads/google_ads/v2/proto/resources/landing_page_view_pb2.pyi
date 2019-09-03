# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class LandingPageView(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    @property
    def unexpanded_final_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        unexpanded_final_url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> LandingPageView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"unexpanded_final_url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",u"unexpanded_final_url"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"unexpanded_final_url",b"unexpanded_final_url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name",u"unexpanded_final_url",b"unexpanded_final_url"]) -> None: ...
