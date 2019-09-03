# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.extension_setting_device_pb2 import (
    ExtensionSettingDeviceEnum as google___ads___googleads___v1___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum,
)

from google.ads.google_ads.v1.proto.enums.extension_type_pb2 import (
    ExtensionTypeEnum as google___ads___googleads___v1___enums___extension_type_pb2___ExtensionTypeEnum,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class AdGroupExtensionSetting(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    extension_type = ... # type: google___ads___googleads___v1___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionType.ClosedValueType
    device = ... # type: google___ads___googleads___v1___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum.ExtensionSettingDevice.ClosedValueType

    @property
    def ad_group(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def extension_feed_items(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        extension_type : typing___Optional[google___ads___googleads___v1___enums___extension_type_pb2___ExtensionTypeEnum.ExtensionType.ClosedValueType] = None,
        ad_group : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        extension_feed_items : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        device : typing___Optional[google___ads___googleads___v1___enums___extension_setting_device_pb2___ExtensionSettingDeviceEnum.ExtensionSettingDevice.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AdGroupExtensionSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",u"device",u"extension_feed_items",u"extension_type",u"resource_name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ad_group",b"ad_group",u"device",b"device",u"extension_feed_items",b"extension_feed_items",u"extension_type",b"extension_type",u"resource_name",b"resource_name"]) -> None: ...
