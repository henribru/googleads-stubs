# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.keyword_plan_competition_level_pb2 import (
    KeywordPlanCompetitionLevelEnum as google___ads___googleads___v2___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
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

class KeywordPlanHistoricalMetrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    competition = (
        ...
    )  # type: google___ads___googleads___v2___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
    @property
    def avg_monthly_searches(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        avg_monthly_searches: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        competition: typing___Optional[
            google___ads___googleads___v2___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevel
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> KeywordPlanHistoricalMetrics: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> KeywordPlanHistoricalMetrics: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "avg_monthly_searches", b"avg_monthly_searches"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "avg_monthly_searches",
            b"avg_monthly_searches",
            "competition",
            b"competition",
        ],
    ) -> None: ...

global___KeywordPlanHistoricalMetrics = KeywordPlanHistoricalMetrics
