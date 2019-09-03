# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.resources.account_budget_proposal_pb2 import (
    AccountBudgetProposal as google___ads___googleads___v2___resources___account_budget_proposal_pb2___AccountBudgetProposal,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetAccountBudgetProposalRequest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetAccountBudgetProposalRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...

class MutateAccountBudgetProposalRequest(google___protobuf___message___Message):
    customer_id = ... # type: typing___Text
    validate_only = ... # type: bool

    @property
    def operation(self) -> AccountBudgetProposalOperation: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operation : typing___Optional[AccountBudgetProposalOperation] = None,
        validate_only : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAccountBudgetProposalRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",u"operation",u"validate_only"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operation",b"operation",u"validate_only",b"validate_only"]) -> None: ...

class AccountBudgetProposalOperation(google___protobuf___message___Message):
    remove = ... # type: typing___Text

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def create(self) -> google___ads___googleads___v2___resources___account_budget_proposal_pb2___AccountBudgetProposal: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        create : typing___Optional[google___ads___googleads___v2___resources___account_budget_proposal_pb2___AccountBudgetProposal] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AccountBudgetProposalOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove",u"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",u"operation",u"remove",u"update_mask"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove",u"update_mask",b"update_mask"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"create",b"create",u"operation",b"operation",u"remove",b"remove",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["create","remove"]: ...

class MutateAccountBudgetProposalResponse(google___protobuf___message___Message):

    @property
    def result(self) -> MutateAccountBudgetProposalResult: ...

    def __init__(self,
        *,
        result : typing___Optional[MutateAccountBudgetProposalResult] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAccountBudgetProposalResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> None: ...

class MutateAccountBudgetProposalResult(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateAccountBudgetProposalResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
