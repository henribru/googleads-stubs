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

class SitelinkPlaceholderFieldEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _SitelinkPlaceholderField(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            SitelinkPlaceholderField.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(0)
        UNKNOWN = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(1)
        TEXT = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(2)
        LINE_1 = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(3)
        LINE_2 = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(4)
        FINAL_URLS = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(5)
        FINAL_MOBILE_URLS = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(6)
        TRACKING_URL = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(7)
        FINAL_URL_SUFFIX = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(8)
    class SitelinkPlaceholderField(metaclass=_SitelinkPlaceholderField):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(0)
    UNKNOWN = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(1)
    TEXT = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(2)
    LINE_1 = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(3)
    LINE_2 = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(4)
    FINAL_URLS = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(5)
    FINAL_MOBILE_URLS = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(6)
    TRACKING_URL = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(7)
    FINAL_URL_SUFFIX = SitelinkPlaceholderFieldEnum.SitelinkPlaceholderField.V(8)
    def __init__(
        self,
    ) -> None: ...

global___SitelinkPlaceholderFieldEnum = SitelinkPlaceholderFieldEnum
