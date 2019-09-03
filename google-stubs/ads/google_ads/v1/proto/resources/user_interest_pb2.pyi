# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.criterion_category_availability_pb2 import (
    CriterionCategoryAvailability as google___ads___googleads___v1___common___criterion_category_availability_pb2___CriterionCategoryAvailability,
)

from google.ads.google_ads.v1.proto.enums.user_interest_taxonomy_type_pb2 import (
    UserInterestTaxonomyTypeEnum as google___ads___googleads___v1___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UserInterest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    taxonomy_type = ... # type: google___ads___googleads___v1___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType.ClosedValueType

    @property
    def user_interest_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def user_interest_parent(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def launched_to_all(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    @property
    def availabilities(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v1___common___criterion_category_availability_pb2___CriterionCategoryAvailability]: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        taxonomy_type : typing___Optional[google___ads___googleads___v1___enums___user_interest_taxonomy_type_pb2___UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType.ClosedValueType] = None,
        user_interest_id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        user_interest_parent : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        launched_to_all : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        availabilities : typing___Optional[typing___Iterable[google___ads___googleads___v1___common___criterion_category_availability_pb2___CriterionCategoryAvailability]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UserInterest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"launched_to_all",u"name",u"user_interest_id",u"user_interest_parent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"availabilities",u"launched_to_all",u"name",u"resource_name",u"taxonomy_type",u"user_interest_id",u"user_interest_parent"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"launched_to_all",b"launched_to_all",u"name",b"name",u"user_interest_id",b"user_interest_id",u"user_interest_parent",b"user_interest_parent"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"availabilities",b"availabilities",u"launched_to_all",b"launched_to_all",u"name",b"name",u"resource_name",b"resource_name",u"taxonomy_type",b"taxonomy_type",u"user_interest_id",b"user_interest_id",u"user_interest_parent",b"user_interest_parent"]) -> None: ...
