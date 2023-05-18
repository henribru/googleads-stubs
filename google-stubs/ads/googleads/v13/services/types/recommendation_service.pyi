from collections.abc import MutableSequence
from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v13.common.types.extensions import (
    CallFeedItem,
    CalloutFeedItem,
    SitelinkFeedItem,
)
from google.ads.googleads.v13.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v13.resources.types.ad import Ad
from google.ads.googleads.v13.resources.types.asset import Asset

class ApplyRecommendationOperation(proto.Message):
    class AdAssetApplyParameters(proto.Message):
        class ApplyScope(proto.Enum):
            UNSPECIFIED = 0
            UNKNOWN = 1
            CUSTOMER = 2
            CAMPAIGN = 3
        new_assets: MutableSequence[Asset]
        existing_assets: MutableSequence[str]
        scope: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            new_assets: MutableSequence[Asset] = ...,
            existing_assets: MutableSequence[str] = ...,
            scope: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope = ...
        ) -> None: ...

    class CallAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...

    class CallExtensionParameters(proto.Message):
        call_extensions: MutableSequence[CallFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            call_extensions: MutableSequence[CallFeedItem] = ...
        ) -> None: ...

    class CalloutAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...

    class CalloutExtensionParameters(proto.Message):
        callout_extensions: MutableSequence[CalloutFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            callout_extensions: MutableSequence[CalloutFeedItem] = ...
        ) -> None: ...

    class CampaignBudgetParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            new_budget_amount_micros: int = ...
        ) -> None: ...

    class ForecastingSetTargetRoasParameters(proto.Message):
        target_roas: float
        campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_roas: float = ...,
            campaign_budget_amount_micros: int = ...
        ) -> None: ...

    class KeywordParameters(proto.Message):
        ad_group: str
        match_type: KeywordMatchTypeEnum.KeywordMatchType
        cpc_bid_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad_group: str = ...,
            match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
            cpc_bid_micros: int = ...
        ) -> None: ...

    class MoveUnusedBudgetParameters(proto.Message):
        budget_micros_to_move: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            budget_micros_to_move: int = ...
        ) -> None: ...

    class RaiseTargetCpaBidTooLowParameters(proto.Message):
        target_multiplier: float
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_multiplier: float = ...
        ) -> None: ...

    class ResponsiveSearchAdAssetParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            updated_ad: Ad = ...
        ) -> None: ...

    class ResponsiveSearchAdImproveAdStrengthParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            updated_ad: Ad = ...
        ) -> None: ...

    class ResponsiveSearchAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...
        ) -> None: ...

    class SitelinkAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...

    class SitelinkExtensionParameters(proto.Message):
        sitelink_extensions: MutableSequence[SitelinkFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            sitelink_extensions: MutableSequence[SitelinkFeedItem] = ...
        ) -> None: ...

    class TargetCpaOptInParameters(proto.Message):
        target_cpa_micros: int
        new_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_cpa_micros: int = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...

    class TargetRoasOptInParameters(proto.Message):
        target_roas: float
        new_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_roas: float = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...

    class TextAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...
        ) -> None: ...

    class UseBroadMatchKeywordParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            new_budget_amount_micros: int = ...
        ) -> None: ...
    resource_name: str
    campaign_budget: ApplyRecommendationOperation.CampaignBudgetParameters
    text_ad: ApplyRecommendationOperation.TextAdParameters
    keyword: ApplyRecommendationOperation.KeywordParameters
    target_cpa_opt_in: ApplyRecommendationOperation.TargetCpaOptInParameters
    target_roas_opt_in: ApplyRecommendationOperation.TargetRoasOptInParameters
    callout_extension: ApplyRecommendationOperation.CalloutExtensionParameters
    call_extension: ApplyRecommendationOperation.CallExtensionParameters
    sitelink_extension: ApplyRecommendationOperation.SitelinkExtensionParameters
    move_unused_budget: ApplyRecommendationOperation.MoveUnusedBudgetParameters
    responsive_search_ad: ApplyRecommendationOperation.ResponsiveSearchAdParameters
    use_broad_match_keyword: ApplyRecommendationOperation.UseBroadMatchKeywordParameters
    responsive_search_ad_asset: ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters
    responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters
    raise_target_cpa_bid_too_low: ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters
    forecasting_set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters
    callout_asset: ApplyRecommendationOperation.CalloutAssetParameters
    call_asset: ApplyRecommendationOperation.CallAssetParameters
    sitelink_asset: ApplyRecommendationOperation.SitelinkAssetParameters
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        campaign_budget: ApplyRecommendationOperation.CampaignBudgetParameters = ...,
        text_ad: ApplyRecommendationOperation.TextAdParameters = ...,
        keyword: ApplyRecommendationOperation.KeywordParameters = ...,
        target_cpa_opt_in: ApplyRecommendationOperation.TargetCpaOptInParameters = ...,
        target_roas_opt_in: ApplyRecommendationOperation.TargetRoasOptInParameters = ...,
        callout_extension: ApplyRecommendationOperation.CalloutExtensionParameters = ...,
        call_extension: ApplyRecommendationOperation.CallExtensionParameters = ...,
        sitelink_extension: ApplyRecommendationOperation.SitelinkExtensionParameters = ...,
        move_unused_budget: ApplyRecommendationOperation.MoveUnusedBudgetParameters = ...,
        responsive_search_ad: ApplyRecommendationOperation.ResponsiveSearchAdParameters = ...,
        use_broad_match_keyword: ApplyRecommendationOperation.UseBroadMatchKeywordParameters = ...,
        responsive_search_ad_asset: ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters = ...,
        responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters = ...,
        raise_target_cpa_bid_too_low: ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters = ...,
        forecasting_set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters = ...,
        callout_asset: ApplyRecommendationOperation.CalloutAssetParameters = ...,
        call_asset: ApplyRecommendationOperation.CallAssetParameters = ...,
        sitelink_asset: ApplyRecommendationOperation.SitelinkAssetParameters = ...
    ) -> None: ...

class ApplyRecommendationRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ApplyRecommendationOperation]
    partial_failure: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[ApplyRecommendationOperation] = ...,
        partial_failure: bool = ...
    ) -> None: ...

class ApplyRecommendationResponse(proto.Message):
    results: MutableSequence[ApplyRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[ApplyRecommendationResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...

class ApplyRecommendationResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class DismissRecommendationRequest(proto.Message):
    class DismissRecommendationOperation(proto.Message):
        resource_name: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            resource_name: str = ...
        ) -> None: ...
    customer_id: str
    operations: MutableSequence[
        DismissRecommendationRequest.DismissRecommendationOperation
    ]
    partial_failure: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: MutableSequence[
            DismissRecommendationRequest.DismissRecommendationOperation
        ] = ...,
        partial_failure: bool = ...
    ) -> None: ...

class DismissRecommendationResponse(proto.Message):
    class DismissRecommendationResult(proto.Message):
        resource_name: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            resource_name: str = ...
        ) -> None: ...
    results: MutableSequence[DismissRecommendationResponse.DismissRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: MutableSequence[
            DismissRecommendationResponse.DismissRecommendationResult
        ] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...