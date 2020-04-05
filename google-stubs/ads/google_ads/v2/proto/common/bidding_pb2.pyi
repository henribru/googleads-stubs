# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.page_one_promoted_strategy_goal_pb2 import (
    PageOnePromotedStrategyGoalEnum as google___ads___googleads___v2___enums___page_one_promoted_strategy_goal_pb2___PageOnePromotedStrategyGoalEnum,
)

from google.ads.google_ads.v2.proto.enums.target_impression_share_location_pb2 import (
    TargetImpressionShareLocationEnum as google___ads___googleads___v2___enums___target_impression_share_location_pb2___TargetImpressionShareLocationEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import Optional as typing___Optional, Union as typing___Union

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class Commission(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def commission_rate_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        commission_rate_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Commission: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Commission: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "commission_rate_micros", b"commission_rate_micros"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "commission_rate_micros", b"commission_rate_micros"
        ],
    ) -> None: ...

global___Commission = Commission

class EnhancedCpc(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> EnhancedCpc: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> EnhancedCpc: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___EnhancedCpc = EnhancedCpc

class ManualCpc(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def enhanced_cpc_enabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        enhanced_cpc_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ManualCpc: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ManualCpc: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "enhanced_cpc_enabled", b"enhanced_cpc_enabled"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "enhanced_cpc_enabled", b"enhanced_cpc_enabled"
        ],
    ) -> None: ...

global___ManualCpc = ManualCpc

class ManualCpm(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ManualCpm: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ManualCpm: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ManualCpm = ManualCpm

class ManualCpv(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ManualCpv: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ManualCpv: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ManualCpv = ManualCpv

class MaximizeConversions(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MaximizeConversions: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MaximizeConversions: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___MaximizeConversions = MaximizeConversions

class MaximizeConversionValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_roas(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    def __init__(
        self,
        *,
        target_roas: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MaximizeConversionValue: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MaximizeConversionValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["target_roas", b"target_roas"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["target_roas", b"target_roas"]
    ) -> None: ...

global___MaximizeConversionValue = MaximizeConversionValue

class PageOnePromoted(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    strategy_goal = (
        ...
    )  # type: google___ads___googleads___v2___enums___page_one_promoted_strategy_goal_pb2___PageOnePromotedStrategyGoalEnum.PageOnePromotedStrategyGoal
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def only_raise_cpc_bids(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def raise_cpc_bid_when_budget_constrained(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def raise_cpc_bid_when_quality_score_is_low(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        strategy_goal: typing___Optional[
            google___ads___googleads___v2___enums___page_one_promoted_strategy_goal_pb2___PageOnePromotedStrategyGoalEnum.PageOnePromotedStrategyGoal
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        only_raise_cpc_bids: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        raise_cpc_bid_when_budget_constrained: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        raise_cpc_bid_when_quality_score_is_low: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PageOnePromoted: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> PageOnePromoted: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "bid_modifier",
            b"bid_modifier",
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "only_raise_cpc_bids",
            b"only_raise_cpc_bids",
            "raise_cpc_bid_when_budget_constrained",
            b"raise_cpc_bid_when_budget_constrained",
            "raise_cpc_bid_when_quality_score_is_low",
            b"raise_cpc_bid_when_quality_score_is_low",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "bid_modifier",
            b"bid_modifier",
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "only_raise_cpc_bids",
            b"only_raise_cpc_bids",
            "raise_cpc_bid_when_budget_constrained",
            b"raise_cpc_bid_when_budget_constrained",
            "raise_cpc_bid_when_quality_score_is_low",
            b"raise_cpc_bid_when_quality_score_is_low",
            "strategy_goal",
            b"strategy_goal",
        ],
    ) -> None: ...

global___PageOnePromoted = PageOnePromoted

class TargetCpa(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_cpa_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpc_bid_floor_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        target_cpa_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpc_bid_floor_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetCpa: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetCpa: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "cpc_bid_floor_micros",
            b"cpc_bid_floor_micros",
            "target_cpa_micros",
            b"target_cpa_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "cpc_bid_floor_micros",
            b"cpc_bid_floor_micros",
            "target_cpa_micros",
            b"target_cpa_micros",
        ],
    ) -> None: ...

global___TargetCpa = TargetCpa

class TargetCpm(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetCpm: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetCpm: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___TargetCpm = TargetCpm

class TargetImpressionShare(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    location = (
        ...
    )  # type: google___ads___googleads___v2___enums___target_impression_share_location_pb2___TargetImpressionShareLocationEnum.TargetImpressionShareLocation
    @property
    def location_fraction_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        location: typing___Optional[
            google___ads___googleads___v2___enums___target_impression_share_location_pb2___TargetImpressionShareLocationEnum.TargetImpressionShareLocation
        ] = None,
        location_fraction_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetImpressionShare: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetImpressionShare: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "location_fraction_micros",
            b"location_fraction_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "location",
            b"location",
            "location_fraction_micros",
            b"location_fraction_micros",
        ],
    ) -> None: ...

global___TargetImpressionShare = TargetImpressionShare

class TargetOutrankShare(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_outrank_share_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int32Value: ...
    @property
    def competitor_domain(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def only_raise_cpc_bids(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def raise_cpc_bid_when_quality_score_is_low(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        target_outrank_share_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
        competitor_domain: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        only_raise_cpc_bids: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        raise_cpc_bid_when_quality_score_is_low: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetOutrankShare: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetOutrankShare: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "competitor_domain",
            b"competitor_domain",
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "only_raise_cpc_bids",
            b"only_raise_cpc_bids",
            "raise_cpc_bid_when_quality_score_is_low",
            b"raise_cpc_bid_when_quality_score_is_low",
            "target_outrank_share_micros",
            b"target_outrank_share_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "competitor_domain",
            b"competitor_domain",
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "only_raise_cpc_bids",
            b"only_raise_cpc_bids",
            "raise_cpc_bid_when_quality_score_is_low",
            b"raise_cpc_bid_when_quality_score_is_low",
            "target_outrank_share_micros",
            b"target_outrank_share_micros",
        ],
    ) -> None: ...

global___TargetOutrankShare = TargetOutrankShare

class TargetRoas(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_roas(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpc_bid_floor_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        target_roas: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpc_bid_floor_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetRoas: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetRoas: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "cpc_bid_floor_micros",
            b"cpc_bid_floor_micros",
            "target_roas",
            b"target_roas",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "cpc_bid_floor_micros",
            b"cpc_bid_floor_micros",
            "target_roas",
            b"target_roas",
        ],
    ) -> None: ...

global___TargetRoas = TargetRoas

class TargetSpend(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def target_spend_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        target_spend_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetSpend: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> TargetSpend: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "target_spend_micros",
            b"target_spend_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "target_spend_micros",
            b"target_spend_micros",
        ],
    ) -> None: ...

global___TargetSpend = TargetSpend

class PercentCpc(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def cpc_bid_ceiling_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def enhanced_cpc_enabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    def __init__(
        self,
        *,
        cpc_bid_ceiling_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        enhanced_cpc_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PercentCpc: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> PercentCpc: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "enhanced_cpc_enabled",
            b"enhanced_cpc_enabled",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_ceiling_micros",
            b"cpc_bid_ceiling_micros",
            "enhanced_cpc_enabled",
            b"enhanced_cpc_enabled",
        ],
    ) -> None: ...

global___PercentCpc = PercentCpc
