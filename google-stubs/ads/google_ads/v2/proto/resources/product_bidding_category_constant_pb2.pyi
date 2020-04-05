# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.product_bidding_category_level_pb2 import (
    ProductBiddingCategoryLevelEnum as google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum,
)

from google.ads.google_ads.v2.proto.enums.product_bidding_category_status_pb2 import (
    ProductBiddingCategoryStatusEnum as google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class ProductBiddingCategoryConstant(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    level = (
        ...
    )  # type: google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
    status = (
        ...
    )  # type: google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def product_bidding_category_constant_parent(
        self
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def localized_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        country_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        product_bidding_category_constant_parent: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        level: typing___Optional[
            google___ads___googleads___v2___enums___product_bidding_category_level_pb2___ProductBiddingCategoryLevelEnum.ProductBiddingCategoryLevel
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___product_bidding_category_status_pb2___ProductBiddingCategoryStatusEnum.ProductBiddingCategoryStatus
        ] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        localized_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ProductBiddingCategoryConstant: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ProductBiddingCategoryConstant: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "country_code",
            b"country_code",
            "id",
            b"id",
            "language_code",
            b"language_code",
            "localized_name",
            b"localized_name",
            "product_bidding_category_constant_parent",
            b"product_bidding_category_constant_parent",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "country_code",
            b"country_code",
            "id",
            b"id",
            "language_code",
            b"language_code",
            "level",
            b"level",
            "localized_name",
            b"localized_name",
            "product_bidding_category_constant_parent",
            b"product_bidding_category_constant_parent",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...

global___ProductBiddingCategoryConstant = ProductBiddingCategoryConstant
