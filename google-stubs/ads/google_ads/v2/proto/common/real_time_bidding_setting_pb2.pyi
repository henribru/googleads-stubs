# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
)

from typing import (
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class RealTimeBiddingSetting(google___protobuf___message___Message):

    @property
    def opt_in(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    def __init__(self,
        *,
        opt_in : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RealTimeBiddingSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"opt_in"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"opt_in"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"opt_in",b"opt_in"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"opt_in",b"opt_in"]) -> None: ...
