"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class AccountBudgetProposalErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AccountBudgetProposalError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            AccountBudgetProposalError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(0)
        UNKNOWN = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(1)
        FIELD_MASK_NOT_ALLOWED = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(2)
        )
        IMMUTABLE_FIELD = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(3)
        REQUIRED_FIELD_MISSING = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(4)
        )
        CANNOT_CANCEL_APPROVED_PROPOSAL = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(5)
        )
        CANNOT_REMOVE_UNAPPROVED_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(6)
        )
        CANNOT_REMOVE_RUNNING_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(7)
        )
        CANNOT_END_UNAPPROVED_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(8)
        )
        CANNOT_END_INACTIVE_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(9)
        )
        BUDGET_NAME_REQUIRED = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(10)
        )
        CANNOT_UPDATE_OLD_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(11)
        )
        CANNOT_END_IN_PAST = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(12)
        )
        CANNOT_EXTEND_END_TIME = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(13)
        )
        PURCHASE_ORDER_NUMBER_REQUIRED = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(14)
        )
        PENDING_UPDATE_PROPOSAL_EXISTS = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(15)
        )
        MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(16)
        )
        CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(17)
        )
        SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(18)
        )
        UPDATE_IS_NO_OP = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(
            19
        )
        END_TIME_MUST_FOLLOW_START_TIME = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(20)
        )
        BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(21)
        )
        NOT_AUTHORIZED = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(22)
        INVALID_BILLING_SETUP = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(23)
        )
        OVERLAPS_EXISTING_BUDGET = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(24)
        )
        CANNOT_CREATE_BUDGET_THROUGH_API = (
            AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(25)
        )
    class AccountBudgetProposalError(metaclass=_AccountBudgetProposalError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(0)
    UNKNOWN = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(1)
    FIELD_MASK_NOT_ALLOWED = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(2)
    )
    IMMUTABLE_FIELD = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(3)
    REQUIRED_FIELD_MISSING = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(4)
    )
    CANNOT_CANCEL_APPROVED_PROPOSAL = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(5)
    )
    CANNOT_REMOVE_UNAPPROVED_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(6)
    )
    CANNOT_REMOVE_RUNNING_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(7)
    )
    CANNOT_END_UNAPPROVED_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(8)
    )
    CANNOT_END_INACTIVE_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(9)
    )
    BUDGET_NAME_REQUIRED = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(
        10
    )
    CANNOT_UPDATE_OLD_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(11)
    )
    CANNOT_END_IN_PAST = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(12)
    CANNOT_EXTEND_END_TIME = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(13)
    )
    PURCHASE_ORDER_NUMBER_REQUIRED = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(14)
    )
    PENDING_UPDATE_PROPOSAL_EXISTS = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(15)
    )
    MULTIPLE_BUDGETS_NOT_ALLOWED_FOR_UNAPPROVED_BILLING_SETUP = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(16)
    )
    CANNOT_UPDATE_START_TIME_FOR_STARTED_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(17)
    )
    SPENDING_LIMIT_LOWER_THAN_ACCRUED_COST_NOT_ALLOWED = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(18)
    )
    UPDATE_IS_NO_OP = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(19)
    END_TIME_MUST_FOLLOW_START_TIME = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(20)
    )
    BUDGET_DATE_RANGE_INCOMPATIBLE_WITH_BILLING_SETUP = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(21)
    )
    NOT_AUTHORIZED = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(22)
    INVALID_BILLING_SETUP = AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(
        23
    )
    OVERLAPS_EXISTING_BUDGET = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(24)
    )
    CANNOT_CREATE_BUDGET_THROUGH_API = (
        AccountBudgetProposalErrorEnum.AccountBudgetProposalError.V(25)
    )
    def __init__(
        self,
    ) -> None: ...

global___AccountBudgetProposalErrorEnum = AccountBudgetProposalErrorEnum
