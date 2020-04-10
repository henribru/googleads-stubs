# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.resources.custom_interest_pb2 import (
    CustomInterest as google___ads___googleads___v3___resources___custom_interest_pb2___CustomInterest,
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

from google.protobuf.message import Message as google___protobuf___message___Message

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

class GetCustomInterestRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetCustomInterestRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> GetCustomInterestRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___GetCustomInterestRequest = GetCustomInterestRequest

class MutateCustomInterestsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ...  # type: typing___Text
    validate_only = ...  # type: builtin___bool
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___CustomInterestOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[global___CustomInterestOperation]
        ] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateCustomInterestsRequest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MutateCustomInterestsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

global___MutateCustomInterestsRequest = MutateCustomInterestsRequest

class CustomInterestOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v3___resources___custom_interest_pb2___CustomInterest: ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v3___resources___custom_interest_pb2___CustomInterest: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        create: typing___Optional[
            google___ads___googleads___v3___resources___custom_interest_pb2___CustomInterest
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v3___resources___custom_interest_pb2___CustomInterest
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CustomInterestOperation: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomInterestOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "update"]: ...

global___CustomInterestOperation = CustomInterestOperation

class MutateCustomInterestsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___MutateCustomInterestResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing___Optional[
            typing___Iterable[global___MutateCustomInterestResult]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateCustomInterestsResponse: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MutateCustomInterestsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["results", b"results"]
    ) -> None: ...

global___MutateCustomInterestsResponse = MutateCustomInterestsResponse

class MutateCustomInterestResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateCustomInterestResult: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> MutateCustomInterestResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___MutateCustomInterestResult = MutateCustomInterestResult