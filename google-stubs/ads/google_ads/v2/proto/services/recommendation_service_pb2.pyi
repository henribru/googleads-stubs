# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.extensions_pb2 import (
    CallFeedItem as google___ads___googleads___v2___common___extensions_pb2___CallFeedItem,
    CalloutFeedItem as google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem,
    SitelinkFeedItem as google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem,
)

from google.ads.google_ads.v2.proto.enums.keyword_match_type_pb2 import (
    KeywordMatchTypeEnum as google___ads___googleads___v2___enums___keyword_match_type_pb2___KeywordMatchTypeEnum,
)

from google.ads.google_ads.v2.proto.resources.ad_pb2 import (
    Ad as google___ads___googleads___v2___resources___ad_pb2___Ad,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status

from typing import (
    Iterable as typing___Iterable,
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

class GetRecommendationRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetRecommendationRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___GetRecommendationRequest = GetRecommendationRequest

class ApplyRecommendationRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ...  # type: typing___Text
    partial_failure = ...  # type: builtin___bool
    @property
    def operations(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___ApplyRecommendationOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[global___ApplyRecommendationOperation]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyRecommendationRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
        ],
    ) -> None: ...

global___ApplyRecommendationRequest = ApplyRecommendationRequest

class ApplyRecommendationOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CampaignBudgetParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def new_budget_amount_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            new_budget_amount_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.CampaignBudgetParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.CampaignBudgetParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "new_budget_amount_micros", b"new_budget_amount_micros"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "new_budget_amount_micros", b"new_budget_amount_micros"
            ],
        ) -> None: ...
    global___CampaignBudgetParameters = CampaignBudgetParameters
    class TextAdParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def ad(self) -> google___ads___googleads___v2___resources___ad_pb2___Ad: ...
        def __init__(
            self,
            *,
            ad: typing___Optional[
                google___ads___googleads___v2___resources___ad_pb2___Ad
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.TextAdParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.TextAdParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions___Literal["ad", b"ad"]
        ) -> builtin___bool: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["ad", b"ad"]
        ) -> None: ...
    global___TextAdParameters = TextAdParameters
    class KeywordParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        match_type = (
            ...
        )  # type: google___ads___googleads___v2___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchType
        @property
        def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            ad_group: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            match_type: typing___Optional[
                google___ads___googleads___v2___enums___keyword_match_type_pb2___KeywordMatchTypeEnum.KeywordMatchType
            ] = None,
            cpc_bid_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.KeywordParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.KeywordParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "ad_group", b"ad_group", "cpc_bid_micros", b"cpc_bid_micros"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "ad_group",
                b"ad_group",
                "cpc_bid_micros",
                b"cpc_bid_micros",
                "match_type",
                b"match_type",
            ],
        ) -> None: ...
    global___KeywordParameters = KeywordParameters
    class TargetCpaOptInParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def target_cpa_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        @property
        def new_campaign_budget_amount_micros(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            target_cpa_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
            new_campaign_budget_amount_micros: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.TargetCpaOptInParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.TargetCpaOptInParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "new_campaign_budget_amount_micros",
                b"new_campaign_budget_amount_micros",
                "target_cpa_micros",
                b"target_cpa_micros",
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "new_campaign_budget_amount_micros",
                b"new_campaign_budget_amount_micros",
                "target_cpa_micros",
                b"target_cpa_micros",
            ],
        ) -> None: ...
    global___TargetCpaOptInParameters = TargetCpaOptInParameters
    class CalloutExtensionParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def callout_extensions(
            self
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem
        ]: ...
        def __init__(
            self,
            *,
            callout_extensions: typing___Optional[
                typing___Iterable[
                    google___ads___googleads___v2___common___extensions_pb2___CalloutFeedItem
                ]
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.CalloutExtensionParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.CalloutExtensionParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "callout_extensions", b"callout_extensions"
            ],
        ) -> None: ...
    global___CalloutExtensionParameters = CalloutExtensionParameters
    class CallExtensionParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def call_extensions(
            self
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___ads___googleads___v2___common___extensions_pb2___CallFeedItem
        ]: ...
        def __init__(
            self,
            *,
            call_extensions: typing___Optional[
                typing___Iterable[
                    google___ads___googleads___v2___common___extensions_pb2___CallFeedItem
                ]
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.CallExtensionParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.CallExtensionParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "call_extensions", b"call_extensions"
            ],
        ) -> None: ...
    global___CallExtensionParameters = CallExtensionParameters
    class SitelinkExtensionParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def sitelink_extensions(
            self
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem
        ]: ...
        def __init__(
            self,
            *,
            sitelink_extensions: typing___Optional[
                typing___Iterable[
                    google___ads___googleads___v2___common___extensions_pb2___SitelinkFeedItem
                ]
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.SitelinkExtensionParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.SitelinkExtensionParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "sitelink_extensions", b"sitelink_extensions"
            ],
        ) -> None: ...
    global___SitelinkExtensionParameters = SitelinkExtensionParameters
    class MoveUnusedBudgetParameters(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def budget_micros_to_move(
            self
        ) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            budget_micros_to_move: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> ApplyRecommendationOperation.MoveUnusedBudgetParameters: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> ApplyRecommendationOperation.MoveUnusedBudgetParameters: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "budget_micros_to_move", b"budget_micros_to_move"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "budget_micros_to_move", b"budget_micros_to_move"
            ],
        ) -> None: ...
    global___MoveUnusedBudgetParameters = MoveUnusedBudgetParameters

    resource_name = ...  # type: typing___Text
    @property
    def campaign_budget(
        self
    ) -> global___ApplyRecommendationOperation.CampaignBudgetParameters: ...
    @property
    def text_ad(self) -> global___ApplyRecommendationOperation.TextAdParameters: ...
    @property
    def keyword(self) -> global___ApplyRecommendationOperation.KeywordParameters: ...
    @property
    def target_cpa_opt_in(
        self
    ) -> global___ApplyRecommendationOperation.TargetCpaOptInParameters: ...
    @property
    def callout_extension(
        self
    ) -> global___ApplyRecommendationOperation.CalloutExtensionParameters: ...
    @property
    def call_extension(
        self
    ) -> global___ApplyRecommendationOperation.CallExtensionParameters: ...
    @property
    def sitelink_extension(
        self
    ) -> global___ApplyRecommendationOperation.SitelinkExtensionParameters: ...
    @property
    def move_unused_budget(
        self
    ) -> global___ApplyRecommendationOperation.MoveUnusedBudgetParameters: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign_budget: typing___Optional[
            global___ApplyRecommendationOperation.CampaignBudgetParameters
        ] = None,
        text_ad: typing___Optional[
            global___ApplyRecommendationOperation.TextAdParameters
        ] = None,
        keyword: typing___Optional[
            global___ApplyRecommendationOperation.KeywordParameters
        ] = None,
        target_cpa_opt_in: typing___Optional[
            global___ApplyRecommendationOperation.TargetCpaOptInParameters
        ] = None,
        callout_extension: typing___Optional[
            global___ApplyRecommendationOperation.CalloutExtensionParameters
        ] = None,
        call_extension: typing___Optional[
            global___ApplyRecommendationOperation.CallExtensionParameters
        ] = None,
        sitelink_extension: typing___Optional[
            global___ApplyRecommendationOperation.SitelinkExtensionParameters
        ] = None,
        move_unused_budget: typing___Optional[
            global___ApplyRecommendationOperation.MoveUnusedBudgetParameters
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyRecommendationOperation: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyRecommendationOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "apply_parameters",
            b"apply_parameters",
            "call_extension",
            b"call_extension",
            "callout_extension",
            b"callout_extension",
            "campaign_budget",
            b"campaign_budget",
            "keyword",
            b"keyword",
            "move_unused_budget",
            b"move_unused_budget",
            "sitelink_extension",
            b"sitelink_extension",
            "target_cpa_opt_in",
            b"target_cpa_opt_in",
            "text_ad",
            b"text_ad",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "apply_parameters",
            b"apply_parameters",
            "call_extension",
            b"call_extension",
            "callout_extension",
            b"callout_extension",
            "campaign_budget",
            b"campaign_budget",
            "keyword",
            b"keyword",
            "move_unused_budget",
            b"move_unused_budget",
            "resource_name",
            b"resource_name",
            "sitelink_extension",
            b"sitelink_extension",
            "target_cpa_opt_in",
            b"target_cpa_opt_in",
            "text_ad",
            b"text_ad",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "apply_parameters", b"apply_parameters"
        ],
    ) -> typing_extensions___Literal[
        "campaign_budget",
        "text_ad",
        "keyword",
        "target_cpa_opt_in",
        "callout_extension",
        "call_extension",
        "sitelink_extension",
        "move_unused_budget",
    ]: ...

global___ApplyRecommendationOperation = ApplyRecommendationOperation

class ApplyRecommendationResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def results(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___ApplyRecommendationResult
    ]: ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[global___ApplyRecommendationResult]
        ] = None,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyRecommendationResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyRecommendationResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
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

global___ApplyRecommendationResponse = ApplyRecommendationResponse

class ApplyRecommendationResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ApplyRecommendationResult: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ApplyRecommendationResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___ApplyRecommendationResult = ApplyRecommendationResult

class DismissRecommendationRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class DismissRecommendationOperation(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        resource_name = ...  # type: typing___Text
        def __init__(
            self, *, resource_name: typing___Optional[typing___Text] = None
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> DismissRecommendationRequest.DismissRecommendationOperation: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> DismissRecommendationRequest.DismissRecommendationOperation: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal["resource_name", b"resource_name"],
        ) -> None: ...
    global___DismissRecommendationOperation = DismissRecommendationOperation

    customer_id = ...  # type: typing___Text
    partial_failure = ...  # type: builtin___bool
    @property
    def operations(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___DismissRecommendationRequest.DismissRecommendationOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[
                global___DismissRecommendationRequest.DismissRecommendationOperation
            ]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DismissRecommendationRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> DismissRecommendationRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
        ],
    ) -> None: ...

global___DismissRecommendationRequest = DismissRecommendationRequest

class DismissRecommendationResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class DismissRecommendationResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        resource_name = ...  # type: typing___Text
        def __init__(
            self, *, resource_name: typing___Optional[typing___Text] = None
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> DismissRecommendationResponse.DismissRecommendationResult: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> DismissRecommendationResponse.DismissRecommendationResult: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal["resource_name", b"resource_name"],
        ) -> None: ...
    global___DismissRecommendationResult = DismissRecommendationResult
    @property
    def results(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___DismissRecommendationResponse.DismissRecommendationResult
    ]: ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[
                global___DismissRecommendationResponse.DismissRecommendationResult
            ]
        ] = None,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DismissRecommendationResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> DismissRecommendationResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
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

global___DismissRecommendationResponse = DismissRecommendationResponse
