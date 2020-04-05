# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
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


class BidModifierSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def points(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___BidModifierSimulationPoint]: ...

    def __init__(self,
        *,
        points : typing___Optional[typing___Iterable[global___BidModifierSimulationPoint]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BidModifierSimulationPointList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BidModifierSimulationPointList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"points",b"points"]) -> None: ...
global___BidModifierSimulationPointList = BidModifierSimulationPointList

class CpcBidSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def points(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___CpcBidSimulationPoint]: ...

    def __init__(self,
        *,
        points : typing___Optional[typing___Iterable[global___CpcBidSimulationPoint]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CpcBidSimulationPointList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CpcBidSimulationPointList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"points",b"points"]) -> None: ...
global___CpcBidSimulationPointList = CpcBidSimulationPointList

class CpvBidSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def points(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___CpvBidSimulationPoint]: ...

    def __init__(self,
        *,
        points : typing___Optional[typing___Iterable[global___CpvBidSimulationPoint]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CpvBidSimulationPointList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CpvBidSimulationPointList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"points",b"points"]) -> None: ...
global___CpvBidSimulationPointList = CpvBidSimulationPointList

class TargetCpaSimulationPointList(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def points(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___TargetCpaSimulationPoint]: ...

    def __init__(self,
        *,
        points : typing___Optional[typing___Iterable[global___TargetCpaSimulationPoint]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetCpaSimulationPointList: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetCpaSimulationPointList: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"points",b"points"]) -> None: ...
global___TargetCpaSimulationPointList = TargetCpaSimulationPointList

class BidModifierSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def bid_modifier(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def biddable_conversions(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def biddable_conversions_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def parent_biddable_conversions(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def parent_biddable_conversions_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def parent_clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def parent_cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def parent_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def parent_top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def parent_required_budget_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        bid_modifier : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        biddable_conversions : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        biddable_conversions_value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        clicks : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        top_slot_impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        parent_biddable_conversions : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        parent_biddable_conversions_value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        parent_clicks : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        parent_cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        parent_impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        parent_top_slot_impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        parent_required_budget_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BidModifierSimulationPoint: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> BidModifierSimulationPoint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bid_modifier",b"bid_modifier",u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"impressions",b"impressions",u"parent_biddable_conversions",b"parent_biddable_conversions",u"parent_biddable_conversions_value",b"parent_biddable_conversions_value",u"parent_clicks",b"parent_clicks",u"parent_cost_micros",b"parent_cost_micros",u"parent_impressions",b"parent_impressions",u"parent_required_budget_micros",b"parent_required_budget_micros",u"parent_top_slot_impressions",b"parent_top_slot_impressions",u"top_slot_impressions",b"top_slot_impressions"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bid_modifier",b"bid_modifier",u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"impressions",b"impressions",u"parent_biddable_conversions",b"parent_biddable_conversions",u"parent_biddable_conversions_value",b"parent_biddable_conversions_value",u"parent_clicks",b"parent_clicks",u"parent_cost_micros",b"parent_cost_micros",u"parent_impressions",b"parent_impressions",u"parent_required_budget_micros",b"parent_required_budget_micros",u"parent_top_slot_impressions",b"parent_top_slot_impressions",u"top_slot_impressions",b"top_slot_impressions"]) -> None: ...
global___BidModifierSimulationPoint = BidModifierSimulationPoint

class CpcBidSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def biddable_conversions(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def biddable_conversions_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        cpc_bid_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        biddable_conversions : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        biddable_conversions_value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        clicks : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        top_slot_impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CpcBidSimulationPoint: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CpcBidSimulationPoint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"cpc_bid_micros",b"cpc_bid_micros",u"impressions",b"impressions",u"top_slot_impressions",b"top_slot_impressions"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"cpc_bid_micros",b"cpc_bid_micros",u"impressions",b"impressions",u"top_slot_impressions",b"top_slot_impressions"]) -> None: ...
global___CpcBidSimulationPoint = CpcBidSimulationPoint

class CpvBidSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def cpv_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def views(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        cpv_bid_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        views : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CpvBidSimulationPoint: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CpvBidSimulationPoint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cost_micros",b"cost_micros",u"cpv_bid_micros",b"cpv_bid_micros",u"impressions",b"impressions",u"views",b"views"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cost_micros",b"cost_micros",u"cpv_bid_micros",b"cpv_bid_micros",u"impressions",b"impressions",u"views",b"views"]) -> None: ...
global___CpvBidSimulationPoint = CpvBidSimulationPoint

class TargetCpaSimulationPoint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def target_cpa_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def biddable_conversions(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def biddable_conversions_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def clicks(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def cost_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def top_slot_impressions(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    def __init__(self,
        *,
        target_cpa_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        biddable_conversions : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        biddable_conversions_value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        clicks : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        cost_micros : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        top_slot_impressions : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetCpaSimulationPoint: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetCpaSimulationPoint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"impressions",b"impressions",u"target_cpa_micros",b"target_cpa_micros",u"top_slot_impressions",b"top_slot_impressions"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"biddable_conversions",b"biddable_conversions",u"biddable_conversions_value",b"biddable_conversions_value",u"clicks",b"clicks",u"cost_micros",b"cost_micros",u"impressions",b"impressions",u"target_cpa_micros",b"target_cpa_micros",u"top_slot_impressions",b"top_slot_impressions"]) -> None: ...
global___TargetCpaSimulationPoint = TargetCpaSimulationPoint
