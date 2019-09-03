# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.policy_pb2 import (
    PolicyTopicEntry as google___ads___googleads___v2___common___policy_pb2___PolicyTopicEntry,
)

from google.ads.google_ads.v2.proto.enums.ad_group_ad_status_pb2 import (
    AdGroupAdStatusEnum as google___ads___googleads___v2___enums___ad_group_ad_status_pb2___AdGroupAdStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.ad_strength_pb2 import (
    AdStrengthEnum as google___ads___googleads___v2___enums___ad_strength_pb2___AdStrengthEnum,
)

from google.ads.google_ads.v2.proto.enums.policy_approval_status_pb2 import (
    PolicyApprovalStatusEnum as google___ads___googleads___v2___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.policy_review_status_pb2 import (
    PolicyReviewStatusEnum as google___ads___googleads___v2___enums___policy_review_status_pb2___PolicyReviewStatusEnum,
)

from google.ads.google_ads.v2.proto.resources.ad_pb2 import (
    Ad as google___ads___googleads___v2___resources___ad_pb2___Ad,
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


class AdGroupAd(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v2___enums___ad_group_ad_status_pb2___AdGroupAdStatusEnum.AdGroupAdStatus.ClosedValueType
    ad_strength = ... # type: google___ads___googleads___v2___enums___ad_strength_pb2___AdStrengthEnum.AdStrength.ClosedValueType

    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def ad(self) -> google___ads___googleads___v2___resources___ad_pb2___Ad: ...

    @property
    def policy_summary(self) -> AdGroupAdPolicySummary: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        status : typing___Optional[google___ads___googleads___v2___enums___ad_group_ad_status_pb2___AdGroupAdStatusEnum.AdGroupAdStatus.ClosedValueType] = None,
        ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ad : typing___Optional[google___ads___googleads___v2___resources___ad_pb2___Ad] = None,
        policy_summary : typing___Optional[AdGroupAdPolicySummary] = None,
        ad_strength : typing___Optional[google___ads___googleads___v2___enums___ad_strength_pb2___AdStrengthEnum.AdStrength.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupAd: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad",u"ad_group",u"policy_summary"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad",u"ad_group",u"ad_strength",u"policy_summary",u"resource_name",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad",b"ad",u"ad_group",b"ad_group",u"policy_summary",b"policy_summary"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad",b"ad",u"ad_group",b"ad_group",u"ad_strength",b"ad_strength",u"policy_summary",b"policy_summary",u"resource_name",b"resource_name",u"status",b"status"]) -> None: ...

class AdGroupAdPolicySummary(google___protobuf___message___Message):
    review_status = ... # type: google___ads___googleads___v2___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatus.ClosedValueType
    approval_status = ... # type: google___ads___googleads___v2___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatus.ClosedValueType

    @property
    def policy_topic_entries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___common___policy_pb2___PolicyTopicEntry]: ...

    def __init__(self,
        *,
        policy_topic_entries : typing___Optional[typing___Iterable[google___ads___googleads___v2___common___policy_pb2___PolicyTopicEntry]] = None,
        review_status : typing___Optional[google___ads___googleads___v2___enums___policy_review_status_pb2___PolicyReviewStatusEnum.PolicyReviewStatus.ClosedValueType] = None,
        approval_status : typing___Optional[google___ads___googleads___v2___enums___policy_approval_status_pb2___PolicyApprovalStatusEnum.PolicyApprovalStatus.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupAdPolicySummary: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"approval_status",u"policy_topic_entries",u"review_status"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"approval_status",b"approval_status",u"policy_topic_entries",b"policy_topic_entries",u"review_status",b"review_status"]) -> None: ...
