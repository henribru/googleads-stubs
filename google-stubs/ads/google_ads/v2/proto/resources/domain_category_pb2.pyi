# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
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

class DomainCategory(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    @property
    def campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def category(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def domain(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def coverage_fraction(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def category_rank(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def has_children(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def recommended_cpc_bid_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        category: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        domain: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        coverage_fraction: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        category_rank: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        has_children: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        recommended_cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DomainCategory: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> DomainCategory: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "campaign",
            b"campaign",
            "category",
            b"category",
            "category_rank",
            b"category_rank",
            "coverage_fraction",
            b"coverage_fraction",
            "domain",
            b"domain",
            "has_children",
            b"has_children",
            "language_code",
            b"language_code",
            "recommended_cpc_bid_micros",
            b"recommended_cpc_bid_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign",
            b"campaign",
            "category",
            b"category",
            "category_rank",
            b"category_rank",
            "coverage_fraction",
            b"coverage_fraction",
            "domain",
            b"domain",
            "has_children",
            b"has_children",
            "language_code",
            b"language_code",
            "recommended_cpc_bid_micros",
            b"recommended_cpc_bid_micros",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

global___DomainCategory = DomainCategory
