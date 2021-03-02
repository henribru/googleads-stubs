# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.common.keyword_plan_common_pb2 import (
    KeywordPlanHistoricalMetrics as google___ads___googleads___v6___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics,
)
from google.ads.google_ads.v6.proto.resources.keyword_plan_pb2 import (
    KeywordPlan as google___ads___googleads___v6___resources___keyword_plan_pb2___KeywordPlan,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetKeywordPlanRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetKeywordPlanRequest = GetKeywordPlanRequest

class MutateKeywordPlansRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[type___KeywordPlanOperation]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___MutateKeywordPlansRequest = MutateKeywordPlansRequest

class KeywordPlanOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v6___resources___keyword_plan_pb2___KeywordPlan: ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v6___resources___keyword_plan_pb2___KeywordPlan: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        create: typing___Optional[
            google___ads___googleads___v6___resources___keyword_plan_pb2___KeywordPlan
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v6___resources___keyword_plan_pb2___KeywordPlan
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "update", "remove"]: ...

type___KeywordPlanOperation = KeywordPlanOperation

class MutateKeywordPlansResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateKeywordPlansResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___MutateKeywordPlansResult]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error", "results", b"results"
        ],
    ) -> None: ...

type___MutateKeywordPlansResponse = MutateKeywordPlansResponse

class MutateKeywordPlansResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateKeywordPlansResult = MutateKeywordPlansResult

class GenerateForecastCurveRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan: typing___Text = ...
    def __init__(
        self, *, keyword_plan: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["keyword_plan", b"keyword_plan"]
    ) -> None: ...

type___GenerateForecastCurveRequest = GenerateForecastCurveRequest

class GenerateForecastCurveResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def campaign_forecast_curves(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanCampaignForecastCurve
    ]: ...
    def __init__(
        self,
        *,
        campaign_forecast_curves: typing___Optional[
            typing___Iterable[type___KeywordPlanCampaignForecastCurve]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_forecast_curves", b"campaign_forecast_curves"
        ],
    ) -> None: ...

type___GenerateForecastCurveResponse = GenerateForecastCurveResponse

class GenerateForecastTimeSeriesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan: typing___Text = ...
    def __init__(
        self, *, keyword_plan: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["keyword_plan", b"keyword_plan"]
    ) -> None: ...

type___GenerateForecastTimeSeriesRequest = GenerateForecastTimeSeriesRequest

class GenerateForecastTimeSeriesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def weekly_time_series_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanWeeklyTimeSeriesForecast
    ]: ...
    def __init__(
        self,
        *,
        weekly_time_series_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanWeeklyTimeSeriesForecast]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "weekly_time_series_forecasts", b"weekly_time_series_forecasts"
        ],
    ) -> None: ...

type___GenerateForecastTimeSeriesResponse = GenerateForecastTimeSeriesResponse

class GenerateForecastMetricsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan: typing___Text = ...
    def __init__(
        self, *, keyword_plan: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["keyword_plan", b"keyword_plan"]
    ) -> None: ...

type___GenerateForecastMetricsRequest = GenerateForecastMetricsRequest

class GenerateForecastMetricsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def campaign_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanCampaignForecast
    ]: ...
    @property
    def ad_group_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanAdGroupForecast
    ]: ...
    @property
    def keyword_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanKeywordForecast
    ]: ...
    def __init__(
        self,
        *,
        campaign_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanCampaignForecast]
        ] = None,
        ad_group_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanAdGroupForecast]
        ] = None,
        keyword_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanKeywordForecast]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_forecasts",
            b"ad_group_forecasts",
            "campaign_forecasts",
            b"campaign_forecasts",
            "keyword_forecasts",
            b"keyword_forecasts",
        ],
    ) -> None: ...

type___GenerateForecastMetricsResponse = GenerateForecastMetricsResponse

class KeywordPlanCampaignForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan_campaign: typing___Text = ...
    @property
    def campaign_forecast(self) -> type___ForecastMetrics: ...
    def __init__(
        self,
        *,
        keyword_plan_campaign: typing___Optional[typing___Text] = None,
        campaign_forecast: typing___Optional[type___ForecastMetrics] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "campaign_forecast",
            b"campaign_forecast",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "campaign_forecast",
            b"campaign_forecast",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_keyword_plan_campaign", b"_keyword_plan_campaign"
        ],
    ) -> typing_extensions___Literal["keyword_plan_campaign"]: ...

type___KeywordPlanCampaignForecast = KeywordPlanCampaignForecast

class KeywordPlanAdGroupForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan_ad_group: typing___Text = ...
    @property
    def ad_group_forecast(self) -> type___ForecastMetrics: ...
    def __init__(
        self,
        *,
        keyword_plan_ad_group: typing___Optional[typing___Text] = None,
        ad_group_forecast: typing___Optional[type___ForecastMetrics] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_ad_group",
            b"_keyword_plan_ad_group",
            "ad_group_forecast",
            b"ad_group_forecast",
            "keyword_plan_ad_group",
            b"keyword_plan_ad_group",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_ad_group",
            b"_keyword_plan_ad_group",
            "ad_group_forecast",
            b"ad_group_forecast",
            "keyword_plan_ad_group",
            b"keyword_plan_ad_group",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_keyword_plan_ad_group", b"_keyword_plan_ad_group"
        ],
    ) -> typing_extensions___Literal["keyword_plan_ad_group"]: ...

type___KeywordPlanAdGroupForecast = KeywordPlanAdGroupForecast

class KeywordPlanKeywordForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan_ad_group_keyword: typing___Text = ...
    @property
    def keyword_forecast(self) -> type___ForecastMetrics: ...
    def __init__(
        self,
        *,
        keyword_plan_ad_group_keyword: typing___Optional[typing___Text] = None,
        keyword_forecast: typing___Optional[type___ForecastMetrics] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_ad_group_keyword",
            b"_keyword_plan_ad_group_keyword",
            "keyword_forecast",
            b"keyword_forecast",
            "keyword_plan_ad_group_keyword",
            b"keyword_plan_ad_group_keyword",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_ad_group_keyword",
            b"_keyword_plan_ad_group_keyword",
            "keyword_forecast",
            b"keyword_forecast",
            "keyword_plan_ad_group_keyword",
            b"keyword_plan_ad_group_keyword",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_keyword_plan_ad_group_keyword", b"_keyword_plan_ad_group_keyword"
        ],
    ) -> typing_extensions___Literal["keyword_plan_ad_group_keyword"]: ...

type___KeywordPlanKeywordForecast = KeywordPlanKeywordForecast

class KeywordPlanCampaignForecastCurve(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan_campaign: typing___Text = ...
    @property
    def max_cpc_bid_forecast_curve(
        self,
    ) -> type___KeywordPlanMaxCpcBidForecastCurve: ...
    def __init__(
        self,
        *,
        keyword_plan_campaign: typing___Optional[typing___Text] = None,
        max_cpc_bid_forecast_curve: typing___Optional[
            type___KeywordPlanMaxCpcBidForecastCurve
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
            "max_cpc_bid_forecast_curve",
            b"max_cpc_bid_forecast_curve",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
            "max_cpc_bid_forecast_curve",
            b"max_cpc_bid_forecast_curve",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_keyword_plan_campaign", b"_keyword_plan_campaign"
        ],
    ) -> typing_extensions___Literal["keyword_plan_campaign"]: ...

type___KeywordPlanCampaignForecastCurve = KeywordPlanCampaignForecastCurve

class KeywordPlanMaxCpcBidForecastCurve(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def max_cpc_bid_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanMaxCpcBidForecast
    ]: ...
    def __init__(
        self,
        *,
        max_cpc_bid_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanMaxCpcBidForecast]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "max_cpc_bid_forecasts", b"max_cpc_bid_forecasts"
        ],
    ) -> None: ...

type___KeywordPlanMaxCpcBidForecastCurve = KeywordPlanMaxCpcBidForecastCurve

class KeywordPlanMaxCpcBidForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    max_cpc_bid_micros: builtin___int = ...
    @property
    def max_cpc_bid_forecast(self) -> type___ForecastMetrics: ...
    def __init__(
        self,
        *,
        max_cpc_bid_micros: typing___Optional[builtin___int] = None,
        max_cpc_bid_forecast: typing___Optional[type___ForecastMetrics] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_max_cpc_bid_micros",
            b"_max_cpc_bid_micros",
            "max_cpc_bid_forecast",
            b"max_cpc_bid_forecast",
            "max_cpc_bid_micros",
            b"max_cpc_bid_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_max_cpc_bid_micros",
            b"_max_cpc_bid_micros",
            "max_cpc_bid_forecast",
            b"max_cpc_bid_forecast",
            "max_cpc_bid_micros",
            b"max_cpc_bid_micros",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_max_cpc_bid_micros", b"_max_cpc_bid_micros"
        ],
    ) -> typing_extensions___Literal["max_cpc_bid_micros"]: ...

type___KeywordPlanMaxCpcBidForecast = KeywordPlanMaxCpcBidForecast

class KeywordPlanWeeklyTimeSeriesForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan_campaign: typing___Text = ...
    @property
    def weekly_forecasts(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanWeeklyForecast
    ]: ...
    def __init__(
        self,
        *,
        keyword_plan_campaign: typing___Optional[typing___Text] = None,
        weekly_forecasts: typing___Optional[
            typing___Iterable[type___KeywordPlanWeeklyForecast]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_keyword_plan_campaign",
            b"_keyword_plan_campaign",
            "keyword_plan_campaign",
            b"keyword_plan_campaign",
            "weekly_forecasts",
            b"weekly_forecasts",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_keyword_plan_campaign", b"_keyword_plan_campaign"
        ],
    ) -> typing_extensions___Literal["keyword_plan_campaign"]: ...

type___KeywordPlanWeeklyTimeSeriesForecast = KeywordPlanWeeklyTimeSeriesForecast

class KeywordPlanWeeklyForecast(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    start_date: typing___Text = ...
    @property
    def forecast(self) -> type___ForecastMetrics: ...
    def __init__(
        self,
        *,
        start_date: typing___Optional[typing___Text] = None,
        forecast: typing___Optional[type___ForecastMetrics] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_start_date",
            b"_start_date",
            "forecast",
            b"forecast",
            "start_date",
            b"start_date",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_start_date",
            b"_start_date",
            "forecast",
            b"forecast",
            "start_date",
            b"start_date",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_start_date", b"_start_date"]
    ) -> typing_extensions___Literal["start_date"]: ...

type___KeywordPlanWeeklyForecast = KeywordPlanWeeklyForecast

class ForecastMetrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    impressions: builtin___float = ...
    ctr: builtin___float = ...
    average_cpc: builtin___int = ...
    clicks: builtin___float = ...
    cost_micros: builtin___int = ...
    def __init__(
        self,
        *,
        impressions: typing___Optional[builtin___float] = None,
        ctr: typing___Optional[builtin___float] = None,
        average_cpc: typing___Optional[builtin___int] = None,
        clicks: typing___Optional[builtin___float] = None,
        cost_micros: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_average_cpc",
            b"_average_cpc",
            "_clicks",
            b"_clicks",
            "_cost_micros",
            b"_cost_micros",
            "_ctr",
            b"_ctr",
            "_impressions",
            b"_impressions",
            "average_cpc",
            b"average_cpc",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "ctr",
            b"ctr",
            "impressions",
            b"impressions",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_average_cpc",
            b"_average_cpc",
            "_clicks",
            b"_clicks",
            "_cost_micros",
            b"_cost_micros",
            "_ctr",
            b"_ctr",
            "_impressions",
            b"_impressions",
            "average_cpc",
            b"average_cpc",
            "clicks",
            b"clicks",
            "cost_micros",
            b"cost_micros",
            "ctr",
            b"ctr",
            "impressions",
            b"impressions",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_average_cpc", b"_average_cpc"]
    ) -> typing_extensions___Literal["average_cpc"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_clicks", b"_clicks"]
    ) -> typing_extensions___Literal["clicks"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_cost_micros", b"_cost_micros"]
    ) -> typing_extensions___Literal["cost_micros"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_ctr", b"_ctr"]
    ) -> typing_extensions___Literal["ctr"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_impressions", b"_impressions"]
    ) -> typing_extensions___Literal["impressions"]: ...

type___ForecastMetrics = ForecastMetrics

class GenerateHistoricalMetricsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    keyword_plan: typing___Text = ...
    def __init__(
        self, *, keyword_plan: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["keyword_plan", b"keyword_plan"]
    ) -> None: ...

type___GenerateHistoricalMetricsRequest = GenerateHistoricalMetricsRequest

class GenerateHistoricalMetricsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def metrics(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanKeywordHistoricalMetrics
    ]: ...
    def __init__(
        self,
        *,
        metrics: typing___Optional[
            typing___Iterable[type___KeywordPlanKeywordHistoricalMetrics]
        ] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["metrics", b"metrics"]
    ) -> None: ...

type___GenerateHistoricalMetricsResponse = GenerateHistoricalMetricsResponse

class KeywordPlanKeywordHistoricalMetrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    search_query: typing___Text = ...
    close_variants: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    @property
    def keyword_metrics(
        self,
    ) -> google___ads___googleads___v6___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics: ...
    def __init__(
        self,
        *,
        search_query: typing___Optional[typing___Text] = None,
        close_variants: typing___Optional[typing___Iterable[typing___Text]] = None,
        keyword_metrics: typing___Optional[
            google___ads___googleads___v6___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_search_query",
            b"_search_query",
            "keyword_metrics",
            b"keyword_metrics",
            "search_query",
            b"search_query",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_search_query",
            b"_search_query",
            "close_variants",
            b"close_variants",
            "keyword_metrics",
            b"keyword_metrics",
            "search_query",
            b"search_query",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_search_query", b"_search_query"],
    ) -> typing_extensions___Literal["search_query"]: ...

type___KeywordPlanKeywordHistoricalMetrics = KeywordPlanKeywordHistoricalMetrics