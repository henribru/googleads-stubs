# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.placement_type_pb2 import (
    PlacementTypeEnum as google___ads___googleads___v1___enums___placement_type_pb2___PlacementTypeEnum,
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GroupPlacementView(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    placement_type = ... # type: google___ads___googleads___v1___enums___placement_type_pb2___PlacementTypeEnum.PlacementType.ClosedValueType

    @property
    def placement(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def display_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def target_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        placement : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        display_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        target_url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        placement_type : typing___Optional[google___ads___googleads___v1___enums___placement_type_pb2___PlacementTypeEnum.PlacementType.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GroupPlacementView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"display_name",u"placement",u"target_url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"display_name",u"placement",u"placement_type",u"resource_name",u"target_url"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"display_name",b"display_name",u"placement",b"placement",u"target_url",b"target_url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"display_name",b"display_name",u"placement",b"placement",u"placement_type",b"placement_type",u"resource_name",b"resource_name",u"target_url",b"target_url"]) -> None: ...
