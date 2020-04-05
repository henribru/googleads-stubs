# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.budget_delivery_method_pb2 import (
    BudgetDeliveryMethodEnum as google___ads___googleads___v1___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum,
)

from google.ads.google_ads.v1.proto.enums.budget_period_pb2 import (
    BudgetPeriodEnum as google___ads___googleads___v1___enums___budget_period_pb2___BudgetPeriodEnum,
)

from google.ads.google_ads.v1.proto.enums.budget_status_pb2 import (
    BudgetStatusEnum as google___ads___googleads___v1___enums___budget_status_pb2___BudgetStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.budget_type_pb2 import (
    BudgetTypeEnum as google___ads___googleads___v1___enums___budget_type_pb2___BudgetTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

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


class CampaignBudget(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v1___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatus
    delivery_method = ... # type: google___ads___googleads___v1___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethod
    period = ... # type: google___ads___googleads___v1___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriod
    type = ... # type: google___ads___googleads___v1___enums___budget_type_pb2___BudgetTypeEnum.BudgetType

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
    def has_recommended_budget(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    @property
    def recommended_budget_amount_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def recommended_budget_estimated_change_weekly_clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def recommended_budget_estimated_change_weekly_cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def recommended_budget_estimated_change_weekly_interactions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def recommended_budget_estimated_change_weekly_views(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        amount_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        total_amount_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        status : typing___Optional[google___ads___googleads___v1___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatus] = None,
        delivery_method : typing___Optional[google___ads___googleads___v1___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethod] = None,
        explicitly_shared : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        reference_count : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        has_recommended_budget : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        recommended_budget_amount_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        period : typing___Optional[google___ads___googleads___v1___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriod] = None,
        recommended_budget_estimated_change_weekly_clicks : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        recommended_budget_estimated_change_weekly_cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        recommended_budget_estimated_change_weekly_interactions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        recommended_budget_estimated_change_weekly_views : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___budget_type_pb2___BudgetTypeEnum.BudgetType] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CampaignBudget: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CampaignBudget: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"amount_micros",b"amount_micros",u"explicitly_shared",b"explicitly_shared",u"has_recommended_budget",b"has_recommended_budget",u"id",b"id",u"name",b"name",u"recommended_budget_amount_micros",b"recommended_budget_amount_micros",u"recommended_budget_estimated_change_weekly_clicks",b"recommended_budget_estimated_change_weekly_clicks",u"recommended_budget_estimated_change_weekly_cost_micros",b"recommended_budget_estimated_change_weekly_cost_micros",u"recommended_budget_estimated_change_weekly_interactions",b"recommended_budget_estimated_change_weekly_interactions",u"recommended_budget_estimated_change_weekly_views",b"recommended_budget_estimated_change_weekly_views",u"reference_count",b"reference_count",u"total_amount_micros",b"total_amount_micros"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"amount_micros",b"amount_micros",u"delivery_method",b"delivery_method",u"explicitly_shared",b"explicitly_shared",u"has_recommended_budget",b"has_recommended_budget",u"id",b"id",u"name",b"name",u"period",b"period",u"recommended_budget_amount_micros",b"recommended_budget_amount_micros",u"recommended_budget_estimated_change_weekly_clicks",b"recommended_budget_estimated_change_weekly_clicks",u"recommended_budget_estimated_change_weekly_cost_micros",b"recommended_budget_estimated_change_weekly_cost_micros",u"recommended_budget_estimated_change_weekly_interactions",b"recommended_budget_estimated_change_weekly_interactions",u"recommended_budget_estimated_change_weekly_views",b"recommended_budget_estimated_change_weekly_views",u"reference_count",b"reference_count",u"resource_name",b"resource_name",u"status",b"status",u"total_amount_micros",b"total_amount_micros",u"type",b"type"]) -> None: ...
global___CampaignBudget = CampaignBudget
