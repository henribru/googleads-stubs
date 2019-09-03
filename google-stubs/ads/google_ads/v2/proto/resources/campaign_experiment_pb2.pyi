# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.campaign_experiment_status_pb2 import (
    CampaignExperimentStatusEnum as google___ads___googleads___v2___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.campaign_experiment_traffic_split_type_pb2 import (
    CampaignExperimentTrafficSplitTypeEnum as google___ads___googleads___v2___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum,
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


class CampaignExperiment(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    traffic_split_type = ... # type: google___ads___googleads___v2___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType.ClosedValueType
    status = ... # type: google___ads___googleads___v2___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum.CampaignExperimentStatus.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def campaign_draft(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def traffic_split_percent(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def experiment_campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def long_running_operation(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        campaign_draft : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        description : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        traffic_split_percent : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        traffic_split_type : typing___Optional[google___ads___googleads___v2___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitType.ClosedValueType] = None,
        experiment_campaign : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status : typing___Optional[google___ads___googleads___v2___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum.CampaignExperimentStatus.ClosedValueType] = None,
        long_running_operation : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        start_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        end_date : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CampaignExperiment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"campaign_draft",u"description",u"end_date",u"experiment_campaign",u"id",u"long_running_operation",u"name",u"start_date",u"traffic_split_percent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"campaign_draft",u"description",u"end_date",u"experiment_campaign",u"id",u"long_running_operation",u"name",u"resource_name",u"start_date",u"status",u"traffic_split_percent",u"traffic_split_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"campaign_draft",b"campaign_draft",u"description",b"description",u"end_date",b"end_date",u"experiment_campaign",b"experiment_campaign",u"id",b"id",u"long_running_operation",b"long_running_operation",u"name",b"name",u"start_date",b"start_date",u"traffic_split_percent",b"traffic_split_percent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"campaign_draft",b"campaign_draft",u"description",b"description",u"end_date",b"end_date",u"experiment_campaign",b"experiment_campaign",u"id",b"id",u"long_running_operation",b"long_running_operation",u"name",b"name",u"resource_name",b"resource_name",u"start_date",b"start_date",u"status",b"status",u"traffic_split_percent",b"traffic_split_percent",u"traffic_split_type",b"traffic_split_type"]) -> None: ...
