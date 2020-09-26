# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.common.policy_pb2 import (
    PolicyTopicEntry as google___ads___googleads___v5___common___policy_pb2___PolicyTopicEntry,
)

from google.ads.google_ads.v5.proto.enums.asset_field_type_pb2 import (
    AssetFieldTypeEnum as google___ads___googleads___v5___enums___asset_field_type_pb2___AssetFieldTypeEnum,
)

from google.ads.google_ads.v5.proto.enums.asset_performance_label_pb2 import (
    AssetPerformanceLabelEnum as google___ads___googleads___v5___enums___asset_performance_label_pb2___AssetPerformanceLabelEnum,
)

from google.ads.google_ads.v5.proto.enums.policy_approval_status_pb2 import (
    PolicyApprovalStatusEnum as google___ads___googleads___v5___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum,
)

from google.ads.google_ads.v5.proto.enums.policy_review_status_pb2 import (
    PolicyReviewStatusEnum as google___ads___googleads___v5___enums___policy_review_status_pb2___PolicyReviewStatusEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdGroupAdAssetView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    field_type: google___ads___googleads___v5___enums___asset_field_type_pb2___AssetFieldTypeEnum.AssetFieldTypeValue = ...
    enabled: builtin___bool = ...
    performance_label: google___ads___googleads___v5___enums___asset_performance_label_pb2___AssetPerformanceLabelEnum.AssetPerformanceLabelValue = ...
    @property
    def ad_group_ad(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def asset(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def policy_summary(self) -> type___AdGroupAdAssetPolicySummary: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group_ad: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        asset: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        field_type: typing___Optional[
            google___ads___googleads___v5___enums___asset_field_type_pb2___AssetFieldTypeEnum.AssetFieldTypeValue
        ] = None,
        enabled: typing___Optional[builtin___bool] = None,
        policy_summary: typing___Optional[type___AdGroupAdAssetPolicySummary] = None,
        performance_label: typing___Optional[
            google___ads___googleads___v5___enums___asset_performance_label_pb2___AssetPerformanceLabelEnum.AssetPerformanceLabelValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_enabled",
            b"_enabled",
            "ad_group_ad",
            b"ad_group_ad",
            "asset",
            b"asset",
            "enabled",
            b"enabled",
            "policy_summary",
            b"policy_summary",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_enabled",
            b"_enabled",
            "ad_group_ad",
            b"ad_group_ad",
            "asset",
            b"asset",
            "enabled",
            b"enabled",
            "field_type",
            b"field_type",
            "performance_label",
            b"performance_label",
            "policy_summary",
            b"policy_summary",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_enabled", b"_enabled"]
    ) -> typing_extensions___Literal["enabled"]: ...

type___AdGroupAdAssetView = AdGroupAdAssetView

class AdGroupAdAssetPolicySummary(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    review_status: google___ads___googleads___v5___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatusValue = ...
    approval_status: google___ads___googleads___v5___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatusValue = ...
    @property
    def policy_topic_entries(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v5___common___policy_pb2___PolicyTopicEntry
    ]: ...
    def __init__(
        self,
        *,
        policy_topic_entries: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v5___common___policy_pb2___PolicyTopicEntry
            ]
        ] = None,
        review_status: typing___Optional[
            google___ads___googleads___v5___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatusValue
        ] = None,
        approval_status: typing___Optional[
            google___ads___googleads___v5___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatusValue
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "approval_status",
            b"approval_status",
            "policy_topic_entries",
            b"policy_topic_entries",
            "review_status",
            b"review_status",
        ],
    ) -> None: ...

type___AdGroupAdAssetPolicySummary = AdGroupAdAssetPolicySummary
