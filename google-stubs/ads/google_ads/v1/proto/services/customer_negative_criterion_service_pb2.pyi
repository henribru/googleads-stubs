# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.resources.customer_negative_criterion_pb2 import (
    CustomerNegativeCriterion as google___ads___googleads___v1___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion,
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetCustomerNegativeCriterionRequest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomerNegativeCriterionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateCustomerNegativeCriteriaRequest(google___protobuf___message___Message):
    customer_id = ... # type: typing___Text
    partial_failure = ... # type: bool
    validate_only = ... # type: bool

    @property
    def operations(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CustomerNegativeCriterionOperation]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operations : typing___Optional[typing___Iterable[CustomerNegativeCriterionOperation]] = None,
        partial_failure : typing___Optional[bool] = None,
        validate_only : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerNegativeCriteriaRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operations",u"partial_failure",u"validate_only"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operations",b"operations",u"partial_failure",b"partial_failure",u"validate_only",b"validate_only"]) -> None: ...

class CustomerNegativeCriterionOperation(google___protobuf___message___Message):
    remove = ... # type: typing___Text

    @property
    def create(self) -> google___ads___googleads___v1___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion: ...

    def __init__(self,
        *,
        create : typing___Optional[google___ads___googleads___v1___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomerNegativeCriterionOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["create","remove"]: ...

class MutateCustomerNegativeCriteriaResponse(google___protobuf___message___Message):

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[MutateCustomerNegativeCriteriaResult]: ...

    def __init__(self,
        *,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        results : typing___Optional[typing___Iterable[MutateCustomerNegativeCriteriaResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerNegativeCriteriaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...

class MutateCustomerNegativeCriteriaResult(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateCustomerNegativeCriteriaResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
