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

class CallPlaceholderFieldEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _CallPlaceholderField(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            CallPlaceholderField.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = CallPlaceholderFieldEnum.CallPlaceholderField.V(0)
        UNKNOWN = CallPlaceholderFieldEnum.CallPlaceholderField.V(1)
        PHONE_NUMBER = CallPlaceholderFieldEnum.CallPlaceholderField.V(2)
        COUNTRY_CODE = CallPlaceholderFieldEnum.CallPlaceholderField.V(3)
        TRACKED = CallPlaceholderFieldEnum.CallPlaceholderField.V(4)
        CONVERSION_TYPE_ID = CallPlaceholderFieldEnum.CallPlaceholderField.V(5)
        CONVERSION_REPORTING_STATE = CallPlaceholderFieldEnum.CallPlaceholderField.V(6)
    class CallPlaceholderField(metaclass=_CallPlaceholderField):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = CallPlaceholderFieldEnum.CallPlaceholderField.V(0)
    UNKNOWN = CallPlaceholderFieldEnum.CallPlaceholderField.V(1)
    PHONE_NUMBER = CallPlaceholderFieldEnum.CallPlaceholderField.V(2)
    COUNTRY_CODE = CallPlaceholderFieldEnum.CallPlaceholderField.V(3)
    TRACKED = CallPlaceholderFieldEnum.CallPlaceholderField.V(4)
    CONVERSION_TYPE_ID = CallPlaceholderFieldEnum.CallPlaceholderField.V(5)
    CONVERSION_REPORTING_STATE = CallPlaceholderFieldEnum.CallPlaceholderField.V(6)
    def __init__(
        self,
    ) -> None: ...

global___CallPlaceholderFieldEnum = CallPlaceholderFieldEnum
