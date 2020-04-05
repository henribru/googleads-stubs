# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.account_budget_proposal_status_pb2 import (
    AccountBudgetProposalStatusEnum as google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.account_budget_proposal_type_pb2 import (
    AccountBudgetProposalTypeEnum as google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.spending_limit_type_pb2 import (
    SpendingLimitTypeEnum as google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.time_type_pb2 import (
    TimeTypeEnum as google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
    overload as typing___overload,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class AccountBudgetProposal(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    proposal_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum.AccountBudgetProposalType
    status = (
        ...
    )  # type: google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
    proposed_start_time_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    proposed_end_time_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    approved_end_time_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
    proposed_spending_limit_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType
    approved_spending_limit_type = (
        ...
    )  # type: google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def billing_setup(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def account_budget(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def approved_start_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_purchase_order_number(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_notes(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def creation_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def approval_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_start_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_end_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def approved_end_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def proposed_spending_limit_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def approved_spending_limit_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        billing_setup: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        account_budget: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposal_type: typing___Optional[
            google___ads___googleads___v1___enums___account_budget_proposal_type_pb2___AccountBudgetProposalTypeEnum.AccountBudgetProposalType
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v1___enums___account_budget_proposal_status_pb2___AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus
        ] = None,
        proposed_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        approved_start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposed_purchase_order_number: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposed_notes: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        creation_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        approval_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposed_start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposed_start_time_type: typing___Optional[
            google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
        ] = None,
        proposed_end_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        proposed_end_time_type: typing___Optional[
            google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
        ] = None,
        approved_end_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        approved_end_time_type: typing___Optional[
            google___ads___googleads___v1___enums___time_type_pb2___TimeTypeEnum.TimeType
        ] = None,
        proposed_spending_limit_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        proposed_spending_limit_type: typing___Optional[
            google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType
        ] = None,
        approved_spending_limit_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        approved_spending_limit_type: typing___Optional[
            google___ads___googleads___v1___enums___spending_limit_type_pb2___SpendingLimitTypeEnum.SpendingLimitType
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AccountBudgetProposal: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> AccountBudgetProposal: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "account_budget",
            b"account_budget",
            "approval_date_time",
            b"approval_date_time",
            "approved_end_date_time",
            b"approved_end_date_time",
            "approved_end_time",
            b"approved_end_time",
            "approved_end_time_type",
            b"approved_end_time_type",
            "approved_spending_limit",
            b"approved_spending_limit",
            "approved_spending_limit_micros",
            b"approved_spending_limit_micros",
            "approved_spending_limit_type",
            b"approved_spending_limit_type",
            "approved_start_date_time",
            b"approved_start_date_time",
            "billing_setup",
            b"billing_setup",
            "creation_date_time",
            b"creation_date_time",
            "id",
            b"id",
            "proposed_end_date_time",
            b"proposed_end_date_time",
            "proposed_end_time",
            b"proposed_end_time",
            "proposed_end_time_type",
            b"proposed_end_time_type",
            "proposed_name",
            b"proposed_name",
            "proposed_notes",
            b"proposed_notes",
            "proposed_purchase_order_number",
            b"proposed_purchase_order_number",
            "proposed_spending_limit",
            b"proposed_spending_limit",
            "proposed_spending_limit_micros",
            b"proposed_spending_limit_micros",
            "proposed_spending_limit_type",
            b"proposed_spending_limit_type",
            "proposed_start_date_time",
            b"proposed_start_date_time",
            "proposed_start_time",
            b"proposed_start_time",
            "proposed_start_time_type",
            b"proposed_start_time_type",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "account_budget",
            b"account_budget",
            "approval_date_time",
            b"approval_date_time",
            "approved_end_date_time",
            b"approved_end_date_time",
            "approved_end_time",
            b"approved_end_time",
            "approved_end_time_type",
            b"approved_end_time_type",
            "approved_spending_limit",
            b"approved_spending_limit",
            "approved_spending_limit_micros",
            b"approved_spending_limit_micros",
            "approved_spending_limit_type",
            b"approved_spending_limit_type",
            "approved_start_date_time",
            b"approved_start_date_time",
            "billing_setup",
            b"billing_setup",
            "creation_date_time",
            b"creation_date_time",
            "id",
            b"id",
            "proposal_type",
            b"proposal_type",
            "proposed_end_date_time",
            b"proposed_end_date_time",
            "proposed_end_time",
            b"proposed_end_time",
            "proposed_end_time_type",
            b"proposed_end_time_type",
            "proposed_name",
            b"proposed_name",
            "proposed_notes",
            b"proposed_notes",
            "proposed_purchase_order_number",
            b"proposed_purchase_order_number",
            "proposed_spending_limit",
            b"proposed_spending_limit",
            "proposed_spending_limit_micros",
            b"proposed_spending_limit_micros",
            "proposed_spending_limit_type",
            b"proposed_spending_limit_type",
            "proposed_start_date_time",
            b"proposed_start_date_time",
            "proposed_start_time",
            b"proposed_start_time",
            "proposed_start_time_type",
            b"proposed_start_time_type",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "approved_end_time", b"approved_end_time"
        ],
    ) -> typing_extensions___Literal[
        "approved_end_date_time", "approved_end_time_type"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "approved_spending_limit", b"approved_spending_limit"
        ],
    ) -> typing_extensions___Literal[
        "approved_spending_limit_micros", "approved_spending_limit_type"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "proposed_end_time", b"proposed_end_time"
        ],
    ) -> typing_extensions___Literal[
        "proposed_end_date_time", "proposed_end_time_type"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "proposed_spending_limit", b"proposed_spending_limit"
        ],
    ) -> typing_extensions___Literal[
        "proposed_spending_limit_micros", "proposed_spending_limit_type"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "proposed_start_time", b"proposed_start_time"
        ],
    ) -> typing_extensions___Literal[
        "proposed_start_date_time", "proposed_start_time_type"
    ]: ...

global___AccountBudgetProposal = AccountBudgetProposal
