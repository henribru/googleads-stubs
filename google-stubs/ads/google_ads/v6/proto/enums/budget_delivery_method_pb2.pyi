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

class BudgetDeliveryMethodEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _BudgetDeliveryMethod(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BudgetDeliveryMethod.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(0)
        UNKNOWN = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(1)
        STANDARD = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(2)
        ACCELERATED = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(3)
    class BudgetDeliveryMethod(metaclass=_BudgetDeliveryMethod):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(0)
    UNKNOWN = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(1)
    STANDARD = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(2)
    ACCELERATED = BudgetDeliveryMethodEnum.BudgetDeliveryMethod.V(3)
    def __init__(
        self,
    ) -> None: ...

global___BudgetDeliveryMethodEnum = BudgetDeliveryMethodEnum
