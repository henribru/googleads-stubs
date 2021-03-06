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

class ResourceChangeOperationEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ResourceChangeOperation(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            ResourceChangeOperation.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = ResourceChangeOperationEnum.ResourceChangeOperation.V(0)
        UNKNOWN = ResourceChangeOperationEnum.ResourceChangeOperation.V(1)
        CREATE = ResourceChangeOperationEnum.ResourceChangeOperation.V(2)
        UPDATE = ResourceChangeOperationEnum.ResourceChangeOperation.V(3)
        REMOVE = ResourceChangeOperationEnum.ResourceChangeOperation.V(4)
    class ResourceChangeOperation(metaclass=_ResourceChangeOperation):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = ResourceChangeOperationEnum.ResourceChangeOperation.V(0)
    UNKNOWN = ResourceChangeOperationEnum.ResourceChangeOperation.V(1)
    CREATE = ResourceChangeOperationEnum.ResourceChangeOperation.V(2)
    UPDATE = ResourceChangeOperationEnum.ResourceChangeOperation.V(3)
    REMOVE = ResourceChangeOperationEnum.ResourceChangeOperation.V(4)
    def __init__(
        self,
    ) -> None: ...

global___ResourceChangeOperationEnum = ResourceChangeOperationEnum
