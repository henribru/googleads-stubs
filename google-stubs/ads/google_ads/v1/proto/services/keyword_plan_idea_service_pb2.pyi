# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.keyword_plan_common_pb2 import (
    KeywordPlanHistoricalMetrics as google___ads___googleads___v1___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics,
)

from google.ads.google_ads.v1.proto.enums.keyword_plan_network_pb2 import (
    KeywordPlanNetworkEnum as google___ads___googleads___v1___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GenerateKeywordIdeasRequest(google___protobuf___message___Message):
    customer_id = ... # type: typing___Text
    keyword_plan_network = ... # type: google___ads___googleads___v1___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetwork.ClosedValueType

    @property
    def language(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def geo_target_constants(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def keyword_and_url_seed(self) -> KeywordAndUrlSeed: ...

    @property
    def keyword_seed(self) -> KeywordSeed: ...

    @property
    def url_seed(self) -> UrlSeed: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        language : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        geo_target_constants : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        keyword_plan_network : typing___Optional[google___ads___googleads___v1___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetwork.ClosedValueType] = None,
        keyword_and_url_seed : typing___Optional[KeywordAndUrlSeed] = None,
        keyword_seed : typing___Optional[KeywordSeed] = None,
        url_seed : typing___Optional[UrlSeed] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GenerateKeywordIdeasRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"keyword_and_url_seed",u"keyword_seed",u"language",u"seed",u"url_seed"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"geo_target_constants",u"keyword_and_url_seed",u"keyword_plan_network",u"keyword_seed",u"language",u"seed",u"url_seed"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"keyword_and_url_seed",b"keyword_and_url_seed",u"keyword_seed",b"keyword_seed",u"language",b"language",u"seed",b"seed",u"url_seed",b"url_seed"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"geo_target_constants",b"geo_target_constants",u"keyword_and_url_seed",b"keyword_and_url_seed",u"keyword_plan_network",b"keyword_plan_network",u"keyword_seed",b"keyword_seed",u"language",b"language",u"seed",b"seed",u"url_seed",b"url_seed"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"seed",b"seed"]) -> typing_extensions___Literal["keyword_and_url_seed","keyword_seed","url_seed"]: ...

class KeywordAndUrlSeed(google___protobuf___message___Message):

    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def keywords(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keywords : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordAndUrlSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keywords",u"url"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keywords",b"keywords",u"url",b"url"]) -> None: ...

class KeywordSeed(google___protobuf___message___Message):

    @property
    def keywords(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        keywords : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"keywords"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"keywords",b"keywords"]) -> None: ...

class UrlSeed(google___protobuf___message___Message):

    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UrlSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"url"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> None: ...

class GenerateKeywordIdeaResponse(google___protobuf___message___Message):

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GenerateKeywordIdeaResult]: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[GenerateKeywordIdeaResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GenerateKeywordIdeaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"results"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"results",b"results"]) -> None: ...

class GenerateKeywordIdeaResult(google___protobuf___message___Message):

    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def keyword_idea_metrics(self) -> google___ads___googleads___v1___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics: ...

    def __init__(self,
        *,
        text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keyword_idea_metrics : typing___Optional[google___ads___googleads___v1___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GenerateKeywordIdeaResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",u"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",u"text"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",b"keyword_idea_metrics",u"text",b"text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",b"keyword_idea_metrics",u"text",b"text"]) -> None: ...
