# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.merchant_center_link_status_pb2 import (
    MerchantCenterLinkStatusEnum as google___ads___googleads___v1___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class MerchantCenterLink(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v1___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def merchant_center_account_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        merchant_center_account_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status : typing___Optional[google___ads___googleads___v1___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatus.ClosedValueType] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MerchantCenterLink: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"id",u"merchant_center_account_name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"merchant_center_account_name",u"resource_name",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"merchant_center_account_name",b"merchant_center_account_name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"merchant_center_account_name",b"merchant_center_account_name",u"resource_name",b"resource_name",u"status",b"status"]) -> None: ...
