# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v4.proto.enums.budget_delivery_method_pb2 import (
    BudgetDeliveryMethodEnum as google___ads___googleads___v4___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum,
)

from google.ads.google_ads.v4.proto.enums.budget_period_pb2 import (
    BudgetPeriodEnum as google___ads___googleads___v4___enums___budget_period_pb2___BudgetPeriodEnum,
)

from google.ads.google_ads.v4.proto.enums.budget_status_pb2 import (
    BudgetStatusEnum as google___ads___googleads___v4___enums___budget_status_pb2___BudgetStatusEnum,
)

from google.ads.google_ads.v4.proto.enums.budget_type_pb2 import (
    BudgetTypeEnum as google___ads___googleads___v4___enums___budget_type_pb2___BudgetTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
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
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignBudget(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v4___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatusValue = ...
    delivery_method: google___ads___googleads___v4___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethodValue = ...
    period: google___ads___googleads___v4___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriodValue = ...
    type: google___ads___googleads___v4___enums___budget_type_pb2___BudgetTypeEnum.BudgetTypeValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def amount_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def total_amount_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def explicitly_shared(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def reference_count(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def has_recommended_budget(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def recommended_budget_amount_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def recommended_budget_estimated_change_weekly_clicks(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def recommended_budget_estimated_change_weekly_cost_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def recommended_budget_estimated_change_weekly_interactions(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def recommended_budget_estimated_change_weekly_views(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        amount_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        total_amount_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v4___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatusValue
        ] = None,
        delivery_method: typing___Optional[
            google___ads___googleads___v4___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethodValue
        ] = None,
        explicitly_shared: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        reference_count: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        has_recommended_budget: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        recommended_budget_amount_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        period: typing___Optional[
            google___ads___googleads___v4___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriodValue
        ] = None,
        recommended_budget_estimated_change_weekly_clicks: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        recommended_budget_estimated_change_weekly_cost_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        recommended_budget_estimated_change_weekly_interactions: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        recommended_budget_estimated_change_weekly_views: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v4___enums___budget_type_pb2___BudgetTypeEnum.BudgetTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "amount_micros",
            b"amount_micros",
            "explicitly_shared",
            b"explicitly_shared",
            "has_recommended_budget",
            b"has_recommended_budget",
            "id",
            b"id",
            "name",
            b"name",
            "recommended_budget_amount_micros",
            b"recommended_budget_amount_micros",
            "recommended_budget_estimated_change_weekly_clicks",
            b"recommended_budget_estimated_change_weekly_clicks",
            "recommended_budget_estimated_change_weekly_cost_micros",
            b"recommended_budget_estimated_change_weekly_cost_micros",
            "recommended_budget_estimated_change_weekly_interactions",
            b"recommended_budget_estimated_change_weekly_interactions",
            "recommended_budget_estimated_change_weekly_views",
            b"recommended_budget_estimated_change_weekly_views",
            "reference_count",
            b"reference_count",
            "total_amount_micros",
            b"total_amount_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "amount_micros",
            b"amount_micros",
            "delivery_method",
            b"delivery_method",
            "explicitly_shared",
            b"explicitly_shared",
            "has_recommended_budget",
            b"has_recommended_budget",
            "id",
            b"id",
            "name",
            b"name",
            "period",
            b"period",
            "recommended_budget_amount_micros",
            b"recommended_budget_amount_micros",
            "recommended_budget_estimated_change_weekly_clicks",
            b"recommended_budget_estimated_change_weekly_clicks",
            "recommended_budget_estimated_change_weekly_cost_micros",
            b"recommended_budget_estimated_change_weekly_cost_micros",
            "recommended_budget_estimated_change_weekly_interactions",
            b"recommended_budget_estimated_change_weekly_interactions",
            "recommended_budget_estimated_change_weekly_views",
            b"recommended_budget_estimated_change_weekly_views",
            "reference_count",
            b"reference_count",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "total_amount_micros",
            b"total_amount_micros",
            "type",
            b"type",
        ],
    ) -> None: ...

type___CampaignBudget = CampaignBudget
