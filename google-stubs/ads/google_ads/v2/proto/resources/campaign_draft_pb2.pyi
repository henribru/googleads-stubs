# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.campaign_draft_status_pb2 import (
    CampaignDraftStatusEnum as google___ads___googleads___v2___enums___campaign_draft_status_pb2___CampaignDraftStatusEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
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

class CampaignDraft(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    status = (
        ...
    )  # type: google___ads___googleads___v2___enums___campaign_draft_status_pb2___CampaignDraftStatusEnum.CampaignDraftStatus
    @property
    def draft_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def base_campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def draft_campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def has_experiment_running(
        self
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def long_running_operation(
        self
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        draft_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        base_campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        draft_campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___campaign_draft_status_pb2___CampaignDraftStatusEnum.CampaignDraftStatus
        ] = None,
        has_experiment_running: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        long_running_operation: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CampaignDraft: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CampaignDraft: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "base_campaign",
            b"base_campaign",
            "draft_campaign",
            b"draft_campaign",
            "draft_id",
            b"draft_id",
            "has_experiment_running",
            b"has_experiment_running",
            "long_running_operation",
            b"long_running_operation",
            "name",
            b"name",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "base_campaign",
            b"base_campaign",
            "draft_campaign",
            b"draft_campaign",
            "draft_id",
            b"draft_id",
            "has_experiment_running",
            b"has_experiment_running",
            "long_running_operation",
            b"long_running_operation",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

global___CampaignDraft = CampaignDraft
