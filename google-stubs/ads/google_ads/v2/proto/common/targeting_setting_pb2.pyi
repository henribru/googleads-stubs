# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.targeting_dimension_pb2 import (
    TargetingDimensionEnum as google___ads___googleads___v2___enums___targeting_dimension_pb2___TargetingDimensionEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
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


class TargetingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def target_restrictions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___TargetRestriction]: ...

    def __init__(self,
        *,
        target_restrictions : typing___Optional[typing___Iterable[global___TargetRestriction]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetingSetting: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetingSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"target_restrictions",b"target_restrictions"]) -> None: ...
global___TargetingSetting = TargetingSetting

class TargetRestriction(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    targeting_dimension = ... # type: google___ads___googleads___v2___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimension

    @property
    def bid_only(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    def __init__(self,
        *,
        targeting_dimension : typing___Optional[google___ads___googleads___v2___enums___targeting_dimension_pb2___TargetingDimensionEnum.TargetingDimension] = None,
        bid_only : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetRestriction: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetRestriction: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bid_only",b"bid_only"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bid_only",b"bid_only",u"targeting_dimension",b"targeting_dimension"]) -> None: ...
global___TargetRestriction = TargetRestriction
