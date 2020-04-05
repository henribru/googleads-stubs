# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.keyword_plan_common_pb2 import (
    KeywordPlanHistoricalMetrics as google___ads___googleads___v2___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics,
)

from google.ads.google_ads.v2.proto.enums.keyword_plan_network_pb2 import (
    KeywordPlanNetworkEnum as google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum,
)

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
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
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


class GenerateKeywordIdeasRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text
    keyword_plan_network = ... # type: google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetwork

    @property
    def language(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def geo_target_constants(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def keyword_and_url_seed(self) -> global___KeywordAndUrlSeed: ...

    @property
    def keyword_seed(self) -> global___KeywordSeed: ...

    @property
    def url_seed(self) -> global___UrlSeed: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        language : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        geo_target_constants : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        keyword_plan_network : typing___Optional[google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetwork] = None,
        keyword_and_url_seed : typing___Optional[global___KeywordAndUrlSeed] = None,
        keyword_seed : typing___Optional[global___KeywordSeed] = None,
        url_seed : typing___Optional[global___UrlSeed] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateKeywordIdeasRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateKeywordIdeasRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"keyword_and_url_seed",b"keyword_and_url_seed",u"keyword_seed",b"keyword_seed",u"language",b"language",u"seed",b"seed",u"url_seed",b"url_seed"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"geo_target_constants",b"geo_target_constants",u"keyword_and_url_seed",b"keyword_and_url_seed",u"keyword_plan_network",b"keyword_plan_network",u"keyword_seed",b"keyword_seed",u"language",b"language",u"seed",b"seed",u"url_seed",b"url_seed"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"seed",b"seed"]) -> typing_extensions___Literal["keyword_and_url_seed","keyword_seed","url_seed"]: ...
global___GenerateKeywordIdeasRequest = GenerateKeywordIdeasRequest

class KeywordAndUrlSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def keywords(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keywords : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> KeywordAndUrlSeed: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> KeywordAndUrlSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"keywords",b"keywords",u"url",b"url"]) -> None: ...
global___KeywordAndUrlSeed = KeywordAndUrlSeed

class KeywordSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def keywords(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        keywords : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> KeywordSeed: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> KeywordSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"keywords",b"keywords"]) -> None: ...
global___KeywordSeed = KeywordSeed

class UrlSeed(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UrlSeed: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UrlSeed: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"url",b"url"]) -> None: ...
global___UrlSeed = UrlSeed

class GenerateKeywordIdeaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___GenerateKeywordIdeaResult]: ...

    def __init__(self,
        *,
        results : typing___Optional[typing___Iterable[global___GenerateKeywordIdeaResult]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateKeywordIdeaResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateKeywordIdeaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"results",b"results"]) -> None: ...
global___GenerateKeywordIdeaResponse = GenerateKeywordIdeaResponse

class GenerateKeywordIdeaResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def keyword_idea_metrics(self) -> google___ads___googleads___v2___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics: ...

    def __init__(self,
        *,
        text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        keyword_idea_metrics : typing___Optional[google___ads___googleads___v2___common___keyword_plan_common_pb2___KeywordPlanHistoricalMetrics] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GenerateKeywordIdeaResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GenerateKeywordIdeaResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",b"keyword_idea_metrics",u"text",b"text"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"keyword_idea_metrics",b"keyword_idea_metrics",u"text",b"text"]) -> None: ...
global___GenerateKeywordIdeaResult = GenerateKeywordIdeaResult
