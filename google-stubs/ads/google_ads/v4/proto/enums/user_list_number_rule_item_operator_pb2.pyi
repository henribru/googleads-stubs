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

class UserListNumberRuleItemOperatorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _UserListNumberRuleItemOperator(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            UserListNumberRuleItemOperator.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = (
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(0)
        )
        UNKNOWN = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(1)
        GREATER_THAN = (
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(2)
        )
        GREATER_THAN_OR_EQUAL = (
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(3)
        )
        EQUALS = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(4)
        NOT_EQUALS = (
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(5)
        )
        LESS_THAN = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(
            6
        )
        LESS_THAN_OR_EQUAL = (
            UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(7)
        )
    class UserListNumberRuleItemOperator(metaclass=_UserListNumberRuleItemOperator):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(0)
    UNKNOWN = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(1)
    GREATER_THAN = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(
        2
    )
    GREATER_THAN_OR_EQUAL = (
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(3)
    )
    EQUALS = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(4)
    NOT_EQUALS = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(5)
    LESS_THAN = UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(6)
    LESS_THAN_OR_EQUAL = (
        UserListNumberRuleItemOperatorEnum.UserListNumberRuleItemOperator.V(7)
    )
    def __init__(
        self,
    ) -> None: ...

global___UserListNumberRuleItemOperatorEnum = UserListNumberRuleItemOperatorEnum
