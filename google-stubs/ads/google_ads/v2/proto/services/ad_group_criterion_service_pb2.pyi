# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.common.policy_pb2 import (
    PolicyViolationKey as google___ads___googleads___v2___common___policy_pb2___PolicyViolationKey,
)

from google.ads.google_ads.v2.proto.resources.ad_group_criterion_pb2 import (
    AdGroupCriterion as google___ads___googleads___v2___resources___ad_group_criterion_pb2___AdGroupCriterion,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.rpc.status_pb2 import (
    Status as google___rpc___status_pb2___Status,
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


class GetAdGroupCriterionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetAdGroupCriterionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetAdGroupCriterionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
global___GetAdGroupCriterionRequest = GetAdGroupCriterionRequest

class MutateAdGroupCriteriaRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text
    partial_failure = ... # type: builtin___bool
    validate_only = ... # type: builtin___bool

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___AdGroupCriterionOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[global___AdGroupCriterionOperation]] = None,
        partial_failure : typing___Optional[builtin___bool] = None,
        validate_only : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateAdGroupCriteriaRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateAdGroupCriteriaRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations",u"partial_failure",b"partial_failure",u"validate_only",b"validate_only"]) -> None: ...
global___MutateAdGroupCriteriaRequest = MutateAdGroupCriteriaRequest

class AdGroupCriterionOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove = ... # type: typing___Text

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def exempt_policy_violation_keys(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___common___policy_pb2___PolicyViolationKey]: ...

    @property
    def create(self) -> google___ads___googleads___v2___resources___ad_group_criterion_pb2___AdGroupCriterion: ...

    @property
    def update(self) -> google___ads___googleads___v2___resources___ad_group_criterion_pb2___AdGroupCriterion: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        exempt_policy_violation_keys : typing___Optional[typing___Iterable[google___ads___googleads___v2___common___policy_pb2___PolicyViolationKey]] = None,
        create : typing___Optional[google___ads___googleads___v2___resources___ad_group_criterion_pb2___AdGroupCriterion] = None,
        update : typing___Optional[google___ads___googleads___v2___resources___ad_group_criterion_pb2___AdGroupCriterion] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AdGroupCriterionOperation: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AdGroupCriterionOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"create",b"create",u"exempt_policy_violation_keys",b"exempt_policy_violation_keys",u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["create","update","remove"]: ...
global___AdGroupCriterionOperation = AdGroupCriterionOperation

class MutateAdGroupCriteriaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[global___MutateAdGroupCriterionResult]: ...

    def __init__(self,
        *,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        results : typing___Optional[typing___Iterable[global___MutateAdGroupCriterionResult]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateAdGroupCriteriaResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateAdGroupCriteriaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...
global___MutateAdGroupCriteriaResponse = MutateAdGroupCriteriaResponse

class MutateAdGroupCriterionResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateAdGroupCriterionResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateAdGroupCriterionResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
global___MutateAdGroupCriterionResult = MutateAdGroupCriterionResult
