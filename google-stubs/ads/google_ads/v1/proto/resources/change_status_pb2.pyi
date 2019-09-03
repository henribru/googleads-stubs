# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.change_status_operation_pb2 import (
    ChangeStatusOperationEnum as google___ads___googleads___v1___enums___change_status_operation_pb2___ChangeStatusOperationEnum,
)

from google.ads.google_ads.v1.proto.enums.change_status_resource_type_pb2 import (
    ChangeStatusResourceTypeEnum as google___ads___googleads___v1___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum,
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


class ChangeStatus(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    resource_type = ... # type: google___ads___googleads___v1___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum.ChangeStatusResourceType.ClosedValueType
    resource_status = ... # type: google___ads___googleads___v1___enums___change_status_operation_pb2___ChangeStatusOperationEnum.ChangeStatusOperation.ClosedValueType

    @property
    def last_change_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group_ad(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def campaign_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def feed_item(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group_feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def campaign_feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad_group_bid_modifier(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        last_change_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        resource_type : typing___Optional[google___ads___googleads___v1___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum.ChangeStatusResourceType.ClosedValueType] = None,
        campaign : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        resource_status : typing___Optional[google___ads___googleads___v1___enums___change_status_operation_pb2___ChangeStatusOperationEnum.ChangeStatusOperation.ClosedValueType] = None,
        ad_group_ad : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_group_criterion : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        campaign_criterion : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        feed : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        feed_item : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_group_feed : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        campaign_feed : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad_group_bid_modifier : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ChangeStatus: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group",u"ad_group_ad",u"ad_group_bid_modifier",u"ad_group_criterion",u"ad_group_feed",u"campaign",u"campaign_criterion",u"campaign_feed",u"feed",u"feed_item",u"last_change_date_time"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",u"ad_group_ad",u"ad_group_bid_modifier",u"ad_group_criterion",u"ad_group_feed",u"campaign",u"campaign_criterion",u"campaign_feed",u"feed",u"feed_item",u"last_change_date_time",u"resource_name",u"resource_status",u"resource_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"ad_group_ad",b"ad_group_ad",u"ad_group_bid_modifier",b"ad_group_bid_modifier",u"ad_group_criterion",b"ad_group_criterion",u"ad_group_feed",b"ad_group_feed",u"campaign",b"campaign",u"campaign_criterion",b"campaign_criterion",u"campaign_feed",b"campaign_feed",u"feed",b"feed",u"feed_item",b"feed_item",u"last_change_date_time",b"last_change_date_time"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"ad_group_ad",b"ad_group_ad",u"ad_group_bid_modifier",b"ad_group_bid_modifier",u"ad_group_criterion",b"ad_group_criterion",u"ad_group_feed",b"ad_group_feed",u"campaign",b"campaign",u"campaign_criterion",b"campaign_criterion",u"campaign_feed",b"campaign_feed",u"feed",b"feed",u"feed_item",b"feed_item",u"last_change_date_time",b"last_change_date_time",u"resource_name",b"resource_name",u"resource_status",b"resource_status",u"resource_type",b"resource_type"]) -> None: ...
