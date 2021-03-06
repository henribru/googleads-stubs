"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.enums.extension_setting_device_pb2
import google.ads.google_ads.v5.proto.enums.extension_type_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CustomerExtensionSetting(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    EXTENSION_TYPE_FIELD_NUMBER: builtins.int
    EXTENSION_FEED_ITEMS_FIELD_NUMBER: builtins.int
    DEVICE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    extension_type: google.ads.google_ads.v5.proto.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.V = (
        ...
    )
    device: google.ads.google_ads.v5.proto.enums.extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice.V = (
        ...
    )
    @property
    def extension_feed_items(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        google.protobuf.wrappers_pb2.StringValue
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        extension_type: google.ads.google_ads.v5.proto.enums.extension_type_pb2.ExtensionTypeEnum.ExtensionType.V = ...,
        extension_feed_items: typing.Optional[
            typing.Iterable[google.protobuf.wrappers_pb2.StringValue]
        ] = ...,
        device: google.ads.google_ads.v5.proto.enums.extension_setting_device_pb2.ExtensionSettingDeviceEnum.ExtensionSettingDevice.V = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "device",
            b"device",
            "extension_feed_items",
            b"extension_feed_items",
            "extension_type",
            b"extension_type",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

global___CustomerExtensionSetting = CustomerExtensionSetting
