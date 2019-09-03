# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.extensions_pb2 import (
    CallFeedItem as google___ads___googleads___v1___common___extensions_pb2___CallFeedItem,
    CalloutFeedItem as google___ads___googleads___v1___common___extensions_pb2___CalloutFeedItem,
    SitelinkFeedItem as google___ads___googleads___v1___common___extensions_pb2___SitelinkFeedItem,
)

from google.ads.google_ads.v1.proto.enums.keyword_match_type_pb2 import (
    KeywordMatchTypeEnum as google___ads___googleads___v1___enums___keyword_match_type_pb2___KeywordMatchTypeEnum,
)

from google.ads.google_ads.v1.proto.resources.ad_pb2 import (
    Ad as google___ads___googleads___v1___resources___ad_pb2___Ad,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from google.rpc.status_pb2 import (
    Status as google___rpc___status_pb2___Status,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetRecommendationRequest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class ApplyRecommendationRequest(google___protobuf___message___Message):
    customer_id = ... # type: typing___Text
    partial_failure = ... # type: bool

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ApplyRecommendationOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[ApplyRecommendationOperation]] = None,
        partial_failure : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operations",u"partial_failure"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations",u"partial_failure",b"partial_failure"]) -> None: ...

class ApplyRecommendationOperation(google___protobuf___message___Message):
    class CampaignBudgetParameters(google___protobuf___message___Message):

        @property
        def new_budget_amount_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        def __init__(self,
            *,
            new_budget_amount_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.CampaignBudgetParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"new_budget_amount_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"new_budget_amount_micros"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"new_budget_amount_micros",b"new_budget_amount_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"new_budget_amount_micros",b"new_budget_amount_micros"]) -> None: ...

    class TextAdParameters(google___protobuf___message___Message):

        @property
        def ad(self) -> google___ads___googleads___v1___resources___ad_pb2___Ad: ...

        def __init__(self,
            *,
            ad : typing___Optional[google___ads___googleads___v1___resources___ad_pb2___Ad] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.TextAdParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"ad"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"ad"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"ad",b"ad"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"ad",b"ad"]) -> None: ...

    class KeywordParameters(google___protobuf___message___Message):
        match_type = ... # type: google___ads___googleads___v1___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchType.ClosedValueType

        @property
        def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        @property
        def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        def __init__(self,
            *,
            ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            match_type : typing___Optional[google___ads___googleads___v1___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchType.ClosedValueType] = None,
            cpc_bid_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.KeywordParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"ad_group",u"cpc_bid_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",u"cpc_bid_micros",u"match_type"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"cpc_bid_micros",b"cpc_bid_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"cpc_bid_micros",b"cpc_bid_micros",u"match_type",b"match_type"]) -> None: ...

    class TargetCpaOptInParameters(google___protobuf___message___Message):

        @property
        def target_cpa_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        @property
        def new_campaign_budget_amount_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        def __init__(self,
            *,
            target_cpa_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            new_campaign_budget_amount_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.TargetCpaOptInParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"new_campaign_budget_amount_micros",u"target_cpa_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"new_campaign_budget_amount_micros",u"target_cpa_micros"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"new_campaign_budget_amount_micros",b"new_campaign_budget_amount_micros",u"target_cpa_micros",b"target_cpa_micros"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"new_campaign_budget_amount_micros",b"new_campaign_budget_amount_micros",u"target_cpa_micros",b"target_cpa_micros"]) -> None: ...

    class CalloutExtensionParameters(google___protobuf___message___Message):

        @property
        def callout_extensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___extensions_pb2___CalloutFeedItem]: ...

        def __init__(self,
            *,
            callout_extensions : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___extensions_pb2___CalloutFeedItem]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.CalloutExtensionParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"callout_extensions"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"callout_extensions",b"callout_extensions"]) -> None: ...

    class CallExtensionParameters(google___protobuf___message___Message):

        @property
        def call_extensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___extensions_pb2___CallFeedItem]: ...

        def __init__(self,
            *,
            call_extensions : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___extensions_pb2___CallFeedItem]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.CallExtensionParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"call_extensions"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"call_extensions",b"call_extensions"]) -> None: ...

    class SitelinkExtensionParameters(google___protobuf___message___Message):

        @property
        def sitelink_extensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___extensions_pb2___SitelinkFeedItem]: ...

        def __init__(self,
            *,
            sitelink_extensions : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___extensions_pb2___SitelinkFeedItem]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.SitelinkExtensionParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"sitelink_extensions"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"sitelink_extensions",b"sitelink_extensions"]) -> None: ...

    class MoveUnusedBudgetParameters(google___protobuf___message___Message):

        @property
        def budget_micros_to_move(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        def __init__(self,
            *,
            budget_micros_to_move : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ApplyRecommendationOperation.MoveUnusedBudgetParameters: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"budget_micros_to_move"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"budget_micros_to_move"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"budget_micros_to_move",b"budget_micros_to_move"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"budget_micros_to_move",b"budget_micros_to_move"]) -> None: ...

    resource_name = ... # type: typing___Text

    @property
    def campaign_budget(self) -> ApplyRecommendationOperation.CampaignBudgetParameters: ...

    @property
    def text_ad(self) -> ApplyRecommendationOperation.TextAdParameters: ...

    @property
    def keyword(self) -> ApplyRecommendationOperation.KeywordParameters: ...

    @property
    def target_cpa_opt_in(self) -> ApplyRecommendationOperation.TargetCpaOptInParameters: ...

    @property
    def callout_extension(self) -> ApplyRecommendationOperation.CalloutExtensionParameters: ...

    @property
    def call_extension(self) -> ApplyRecommendationOperation.CallExtensionParameters: ...

    @property
    def sitelink_extension(self) -> ApplyRecommendationOperation.SitelinkExtensionParameters: ...

    @property
    def move_unused_budget(self) -> ApplyRecommendationOperation.MoveUnusedBudgetParameters: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        campaign_budget : typing___Optional[ApplyRecommendationOperation.CampaignBudgetParameters] = None,
        text_ad : typing___Optional[ApplyRecommendationOperation.TextAdParameters] = None,
        keyword : typing___Optional[ApplyRecommendationOperation.KeywordParameters] = None,
        target_cpa_opt_in : typing___Optional[ApplyRecommendationOperation.TargetCpaOptInParameters] = None,
        callout_extension : typing___Optional[ApplyRecommendationOperation.CalloutExtensionParameters] = None,
        call_extension : typing___Optional[ApplyRecommendationOperation.CallExtensionParameters] = None,
        sitelink_extension : typing___Optional[ApplyRecommendationOperation.SitelinkExtensionParameters] = None,
        move_unused_budget : typing___Optional[ApplyRecommendationOperation.MoveUnusedBudgetParameters] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyRecommendationOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"apply_parameters",u"call_extension",u"callout_extension",u"campaign_budget",u"keyword",u"move_unused_budget",u"sitelink_extension",u"target_cpa_opt_in",u"text_ad"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"apply_parameters",u"call_extension",u"callout_extension",u"campaign_budget",u"keyword",u"move_unused_budget",u"resource_name",u"sitelink_extension",u"target_cpa_opt_in",u"text_ad"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"apply_parameters",b"apply_parameters",u"call_extension",b"call_extension",u"callout_extension",b"callout_extension",u"campaign_budget",b"campaign_budget",u"keyword",b"keyword",u"move_unused_budget",b"move_unused_budget",u"sitelink_extension",b"sitelink_extension",u"target_cpa_opt_in",b"target_cpa_opt_in",u"text_ad",b"text_ad"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"apply_parameters",b"apply_parameters",u"call_extension",b"call_extension",u"callout_extension",b"callout_extension",u"campaign_budget",b"campaign_budget",u"keyword",b"keyword",u"move_unused_budget",b"move_unused_budget",u"resource_name",b"resource_name",u"sitelink_extension",b"sitelink_extension",u"target_cpa_opt_in",b"target_cpa_opt_in",u"text_ad",b"text_ad"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"apply_parameters",b"apply_parameters"]) -> typing_extensions___Literal["campaign_budget","text_ad","keyword","target_cpa_opt_in","callout_extension","call_extension","sitelink_extension","move_unused_budget"]: ...

class ApplyRecommendationResponse(google___protobuf___message___Message):

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ApplyRecommendationResult]: ...

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[ApplyRecommendationResult]] = None,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyRecommendationResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...

class ApplyRecommendationResult(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyRecommendationResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class DismissRecommendationRequest(google___protobuf___message___Message):
    class DismissRecommendationOperation(google___protobuf___message___Message):
        resource_name = ... # type: typing___Text

        def __init__(self,
            *,
            resource_name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DismissRecommendationRequest.DismissRecommendationOperation: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

    customer_id = ... # type: typing___Text
    partial_failure = ... # type: bool

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DismissRecommendationRequest.DismissRecommendationOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[DismissRecommendationRequest.DismissRecommendationOperation]] = None,
        partial_failure : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DismissRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operations",u"partial_failure"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations",u"partial_failure",b"partial_failure"]) -> None: ...

class DismissRecommendationResponse(google___protobuf___message___Message):
    class DismissRecommendationResult(google___protobuf___message___Message):
        resource_name = ... # type: typing___Text

        def __init__(self,
            *,
            resource_name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DismissRecommendationResponse.DismissRecommendationResult: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...


    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DismissRecommendationResponse.DismissRecommendationResult]: ...

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[DismissRecommendationResponse.DismissRecommendationResult]] = None,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DismissRecommendationResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...
