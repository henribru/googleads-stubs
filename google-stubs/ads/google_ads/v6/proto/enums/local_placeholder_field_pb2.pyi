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

class LocalPlaceholderFieldEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _LocalPlaceholderField(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            LocalPlaceholderField.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(0)
        UNKNOWN = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(1)
        DEAL_ID = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(2)
        DEAL_NAME = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(3)
        SUBTITLE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(4)
        DESCRIPTION = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(5)
        PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(6)
        FORMATTED_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(7)
        SALE_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(8)
        FORMATTED_SALE_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(9)
        IMAGE_URL = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(10)
        ADDRESS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(11)
        CATEGORY = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(12)
        CONTEXTUAL_KEYWORDS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(13)
        FINAL_URLS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(14)
        FINAL_MOBILE_URLS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(15)
        TRACKING_URL = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(16)
        ANDROID_APP_LINK = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(17)
        SIMILAR_DEAL_IDS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(18)
        IOS_APP_LINK = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(19)
        IOS_APP_STORE_ID = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(20)
    class LocalPlaceholderField(metaclass=_LocalPlaceholderField):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(0)
    UNKNOWN = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(1)
    DEAL_ID = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(2)
    DEAL_NAME = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(3)
    SUBTITLE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(4)
    DESCRIPTION = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(5)
    PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(6)
    FORMATTED_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(7)
    SALE_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(8)
    FORMATTED_SALE_PRICE = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(9)
    IMAGE_URL = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(10)
    ADDRESS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(11)
    CATEGORY = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(12)
    CONTEXTUAL_KEYWORDS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(13)
    FINAL_URLS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(14)
    FINAL_MOBILE_URLS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(15)
    TRACKING_URL = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(16)
    ANDROID_APP_LINK = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(17)
    SIMILAR_DEAL_IDS = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(18)
    IOS_APP_LINK = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(19)
    IOS_APP_STORE_ID = LocalPlaceholderFieldEnum.LocalPlaceholderField.V(20)
    def __init__(
        self,
    ) -> None: ...

global___LocalPlaceholderFieldEnum = LocalPlaceholderFieldEnum
