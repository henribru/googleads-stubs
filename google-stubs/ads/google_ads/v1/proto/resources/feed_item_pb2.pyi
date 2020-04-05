# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.custom_parameter_pb2 import (
    CustomParameter as google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter,
)

from google.ads.google_ads.v1.proto.common.feed_common_pb2 import (
    Money as google___ads___googleads___v1___common___feed_common_pb2___Money,
)

from google.ads.google_ads.v1.proto.common.policy_pb2 import (
    PolicyTopicEntry as google___ads___googleads___v1___common___policy_pb2___PolicyTopicEntry,
)

from google.ads.google_ads.v1.proto.enums.feed_item_quality_approval_status_pb2 import (
    FeedItemQualityApprovalStatusEnum as google___ads___googleads___v1___enums___feed_item_quality_approval_status_pb2___FeedItemQualityApprovalStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.feed_item_quality_disapproval_reason_pb2 import (
    FeedItemQualityDisapprovalReasonEnum as google___ads___googleads___v1___enums___feed_item_quality_disapproval_reason_pb2___FeedItemQualityDisapprovalReasonEnum,
)

from google.ads.google_ads.v1.proto.enums.feed_item_status_pb2 import (
    FeedItemStatusEnum as google___ads___googleads___v1___enums___feed_item_status_pb2___FeedItemStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.feed_item_validation_status_pb2 import (
    FeedItemValidationStatusEnum as google___ads___googleads___v1___enums___feed_item_validation_status_pb2___FeedItemValidationStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.geo_targeting_restriction_pb2 import (
    GeoTargetingRestrictionEnum as google___ads___googleads___v1___enums___geo_targeting_restriction_pb2___GeoTargetingRestrictionEnum,
)

from google.ads.google_ads.v1.proto.enums.policy_approval_status_pb2 import (
    PolicyApprovalStatusEnum as google___ads___googleads___v1___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.policy_review_status_pb2 import (
    PolicyReviewStatusEnum as google___ads___googleads___v1___enums___policy_review_status_pb2___PolicyReviewStatusEnum,
)

from google.ads.google_ads.v1.proto.errors.feed_item_validation_error_pb2 import (
    FeedItemValidationErrorEnum as google___ads___googleads___v1___errors___feed_item_validation_error_pb2___FeedItemValidationErrorEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

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

class FeedItem(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    geo_targeting_restriction = (
        ...
    )  # type: google___ads___googleads___v1___enums___geo_targeting_restriction_pb2___GeoTargetingRestrictionEnum.GeoTargetingRestriction
    status = (
        ...
    )  # type: google___ads___googleads___v1___enums___feed_item_status_pb2___FeedItemStatusEnum.FeedItemStatus
    @property
    def feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def start_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def attribute_values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___FeedItemAttributeValue
    ]: ...
    @property
    def url_custom_parameters(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter
    ]: ...
    @property
    def policy_infos(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___FeedItemPlaceholderPolicyInfo
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        feed: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        attribute_values: typing___Optional[
            typing___Iterable[global___FeedItemAttributeValue]
        ] = None,
        geo_targeting_restriction: typing___Optional[
            google___ads___googleads___v1___enums___geo_targeting_restriction_pb2___GeoTargetingRestrictionEnum.GeoTargetingRestriction
        ] = None,
        url_custom_parameters: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v1___common___custom_parameter_pb2___CustomParameter
            ]
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v1___enums___feed_item_status_pb2___FeedItemStatusEnum.FeedItemStatus
        ] = None,
        policy_infos: typing___Optional[
            typing___Iterable[global___FeedItemPlaceholderPolicyInfo]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItem: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItem: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "end_date_time",
            b"end_date_time",
            "feed",
            b"feed",
            "id",
            b"id",
            "start_date_time",
            b"start_date_time",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "attribute_values",
            b"attribute_values",
            "end_date_time",
            b"end_date_time",
            "feed",
            b"feed",
            "geo_targeting_restriction",
            b"geo_targeting_restriction",
            "id",
            b"id",
            "policy_infos",
            b"policy_infos",
            "resource_name",
            b"resource_name",
            "start_date_time",
            b"start_date_time",
            "status",
            b"status",
            "url_custom_parameters",
            b"url_custom_parameters",
        ],
    ) -> None: ...

global___FeedItem = FeedItem

class FeedItemAttributeValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def feed_attribute_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def integer_value(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def boolean_value(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def string_value(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def double_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def price_value(
        self,
    ) -> google___ads___googleads___v1___common___feed_common_pb2___Money: ...
    @property
    def integer_values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___Int64Value
    ]: ...
    @property
    def boolean_values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___BoolValue
    ]: ...
    @property
    def string_values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def double_values(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___DoubleValue
    ]: ...
    def __init__(
        self,
        *,
        feed_attribute_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        integer_value: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        boolean_value: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        string_value: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        double_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        price_value: typing___Optional[
            google___ads___googleads___v1___common___feed_common_pb2___Money
        ] = None,
        integer_values: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___Int64Value]
        ] = None,
        boolean_values: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___BoolValue]
        ] = None,
        string_values: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        double_values: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___DoubleValue]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemAttributeValue: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemAttributeValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "boolean_value",
            b"boolean_value",
            "double_value",
            b"double_value",
            "feed_attribute_id",
            b"feed_attribute_id",
            "integer_value",
            b"integer_value",
            "price_value",
            b"price_value",
            "string_value",
            b"string_value",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "boolean_value",
            b"boolean_value",
            "boolean_values",
            b"boolean_values",
            "double_value",
            b"double_value",
            "double_values",
            b"double_values",
            "feed_attribute_id",
            b"feed_attribute_id",
            "integer_value",
            b"integer_value",
            "integer_values",
            b"integer_values",
            "price_value",
            b"price_value",
            "string_value",
            b"string_value",
            "string_values",
            b"string_values",
        ],
    ) -> None: ...

global___FeedItemAttributeValue = FeedItemAttributeValue

class FeedItemPlaceholderPolicyInfo(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    review_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatus
    approval_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatus
    validation_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___feed_item_validation_status_pb2___FeedItemValidationStatusEnum.FeedItemValidationStatus
    quality_approval_status = (
        ...
    )  # type: google___ads___googleads___v1___enums___feed_item_quality_approval_status_pb2___FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
    quality_disapproval_reasons = (
        ...
    )  # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[google___ads___googleads___v1___enums___feed_item_quality_disapproval_reason_pb2___FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason]
    @property
    def placeholder_type(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    @property
    def feed_mapping_resource_name(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def policy_topic_entries(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___ads___googleads___v1___common___policy_pb2___PolicyTopicEntry
    ]: ...
    @property
    def validation_errors(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___FeedItemValidationError
    ]: ...
    def __init__(
        self,
        *,
        placeholder_type: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
        feed_mapping_resource_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        review_status: typing___Optional[
            google___ads___googleads___v1___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatus
        ] = None,
        approval_status: typing___Optional[
            google___ads___googleads___v1___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatus
        ] = None,
        policy_topic_entries: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v1___common___policy_pb2___PolicyTopicEntry
            ]
        ] = None,
        validation_status: typing___Optional[
            google___ads___googleads___v1___enums___feed_item_validation_status_pb2___FeedItemValidationStatusEnum.FeedItemValidationStatus
        ] = None,
        validation_errors: typing___Optional[
            typing___Iterable[global___FeedItemValidationError]
        ] = None,
        quality_approval_status: typing___Optional[
            google___ads___googleads___v1___enums___feed_item_quality_approval_status_pb2___FeedItemQualityApprovalStatusEnum.FeedItemQualityApprovalStatus
        ] = None,
        quality_disapproval_reasons: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v1___enums___feed_item_quality_disapproval_reason_pb2___FeedItemQualityDisapprovalReasonEnum.FeedItemQualityDisapprovalReason
            ]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemPlaceholderPolicyInfo: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemPlaceholderPolicyInfo: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "feed_mapping_resource_name",
            b"feed_mapping_resource_name",
            "placeholder_type",
            b"placeholder_type",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "approval_status",
            b"approval_status",
            "feed_mapping_resource_name",
            b"feed_mapping_resource_name",
            "placeholder_type",
            b"placeholder_type",
            "policy_topic_entries",
            b"policy_topic_entries",
            "quality_approval_status",
            b"quality_approval_status",
            "quality_disapproval_reasons",
            b"quality_disapproval_reasons",
            "review_status",
            b"review_status",
            "validation_errors",
            b"validation_errors",
            "validation_status",
            b"validation_status",
        ],
    ) -> None: ...

global___FeedItemPlaceholderPolicyInfo = FeedItemPlaceholderPolicyInfo

class FeedItemValidationError(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    validation_error = (
        ...
    )  # type: google___ads___googleads___v1___errors___feed_item_validation_error_pb2___FeedItemValidationErrorEnum.FeedItemValidationError
    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def feed_attribute_ids(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___Int64Value
    ]: ...
    @property
    def extra_info(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        validation_error: typing___Optional[
            google___ads___googleads___v1___errors___feed_item_validation_error_pb2___FeedItemValidationErrorEnum.FeedItemValidationError
        ] = None,
        description: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        feed_attribute_ids: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___Int64Value]
        ] = None,
        extra_info: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FeedItemValidationError: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> FeedItemValidationError: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "description", b"description", "extra_info", b"extra_info"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "description",
            b"description",
            "extra_info",
            b"extra_info",
            "feed_attribute_ids",
            b"feed_attribute_ids",
            "validation_error",
            b"validation_error",
        ],
    ) -> None: ...

global___FeedItemValidationError = FeedItemValidationError
