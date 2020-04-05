# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.resources.merchant_center_link_pb2 import (
    MerchantCenterLink as google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ListMerchantCenterLinksRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMerchantCenterLinksRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMerchantCenterLinksRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id"]) -> None: ...
global___ListMerchantCenterLinksRequest = ListMerchantCenterLinksRequest

class ListMerchantCenterLinksResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def merchant_center_links(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink]: ...

    def __init__(self,
        *,
        merchant_center_links : typing___Optional[typing___Iterable[google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMerchantCenterLinksResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMerchantCenterLinksResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"merchant_center_links",b"merchant_center_links"]) -> None: ...
global___ListMerchantCenterLinksResponse = ListMerchantCenterLinksResponse

class GetMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetMerchantCenterLinkRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetMerchantCenterLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
global___GetMerchantCenterLinkRequest = GetMerchantCenterLinkRequest

class MutateMerchantCenterLinkRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text

    @property
    def operation(self) -> global___MerchantCenterLinkOperation: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        operation : typing___Optional[global___MerchantCenterLinkOperation] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateMerchantCenterLinkRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateMerchantCenterLinkRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"customer_id",b"customer_id",u"operation",b"operation"]) -> None: ...
global___MutateMerchantCenterLinkRequest = MutateMerchantCenterLinkRequest

class MerchantCenterLinkOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove = ... # type: typing___Text

    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...

    @property
    def update(self) -> google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink: ...

    def __init__(self,
        *,
        update_mask : typing___Optional[google___protobuf___field_mask_pb2___FieldMask] = None,
        update : typing___Optional[google___ads___googleads___v2___resources___merchant_center_link_pb2___MerchantCenterLink] = None,
        remove : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MerchantCenterLinkOperation: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MerchantCenterLinkOperation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"operation",b"operation",u"remove",b"remove",u"update",b"update",u"update_mask",b"update_mask"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"operation",b"operation"]) -> typing_extensions___Literal["update","remove"]: ...
global___MerchantCenterLinkOperation = MerchantCenterLinkOperation

class MutateMerchantCenterLinkResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def result(self) -> global___MutateMerchantCenterLinkResult: ...

    def __init__(self,
        *,
        result : typing___Optional[global___MutateMerchantCenterLinkResult] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateMerchantCenterLinkResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateMerchantCenterLinkResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"result",b"result"]) -> None: ...
global___MutateMerchantCenterLinkResponse = MutateMerchantCenterLinkResponse

class MutateMerchantCenterLinkResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> MutateMerchantCenterLinkResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> MutateMerchantCenterLinkResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"resource_name",b"resource_name"]) -> None: ...
global___MutateMerchantCenterLinkResult = MutateMerchantCenterLinkResult
