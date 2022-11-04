from typing import Any

import proto

from google.ads.googleads.v12.common.types.policy import PolicyTopicEntry
from google.ads.googleads.v12.enums.types.asset_field_type import AssetFieldTypeEnum
from google.ads.googleads.v12.enums.types.asset_performance_label import (
    AssetPerformanceLabelEnum,
)
from google.ads.googleads.v12.enums.types.policy_approval_status import (
    PolicyApprovalStatusEnum,
)
from google.ads.googleads.v12.enums.types.policy_review_status import (
    PolicyReviewStatusEnum,
)
from google.ads.googleads.v12.enums.types.served_asset_field_type import (
    ServedAssetFieldTypeEnum,
)

class AdGroupAdAssetPolicySummary(proto.Message):
    policy_topic_entries: list[PolicyTopicEntry]
    review_status: PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_topic_entries: list[PolicyTopicEntry] = ...,
        review_status: PolicyReviewStatusEnum.PolicyReviewStatus = ...,
        approval_status: PolicyApprovalStatusEnum.PolicyApprovalStatus = ...
    ) -> None: ...

class AdGroupAdAssetView(proto.Message):
    resource_name: str
    ad_group_ad: str
    asset: str
    field_type: AssetFieldTypeEnum.AssetFieldType
    enabled: bool
    policy_summary: AdGroupAdAssetPolicySummary
    performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel
    pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        ad_group_ad: str = ...,
        asset: str = ...,
        field_type: AssetFieldTypeEnum.AssetFieldType = ...,
        enabled: bool = ...,
        policy_summary: AdGroupAdAssetPolicySummary = ...,
        performance_label: AssetPerformanceLabelEnum.AssetPerformanceLabel = ...,
        pinned_field: ServedAssetFieldTypeEnum.ServedAssetFieldType = ...
    ) -> None: ...
