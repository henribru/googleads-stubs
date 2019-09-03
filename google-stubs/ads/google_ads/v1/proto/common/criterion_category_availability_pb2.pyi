# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.advertising_channel_sub_type_pb2 import (
    AdvertisingChannelSubTypeEnum as google___ads___googleads___v1___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.advertising_channel_type_pb2 import (
    AdvertisingChannelTypeEnum as google___ads___googleads___v1___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.criterion_category_channel_availability_mode_pb2 import (
    CriterionCategoryChannelAvailabilityModeEnum as google___ads___googleads___v1___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum,
)

from google.ads.google_ads.v1.proto.enums.criterion_category_locale_availability_mode_pb2 import (
    CriterionCategoryLocaleAvailabilityModeEnum as google___ads___googleads___v1___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CriterionCategoryAvailability(google___protobuf___message___Message):

    @property
    def channel(self) -> CriterionCategoryChannelAvailability: ...

    @property
    def locale(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CriterionCategoryLocaleAvailability]: ...

    def __init__(self,
        *,
        channel : typing___Optional[CriterionCategoryChannelAvailability] = None,
        locale : typing___Optional[typing___Iterable[CriterionCategoryLocaleAvailability]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CriterionCategoryAvailability: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"channel"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel",u"locale"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"channel",b"channel"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"channel",b"channel",u"locale",b"locale"]) -> None: ...

class CriterionCategoryChannelAvailability(google___protobuf___message___Message):
    availability_mode = ... # type: google___ads___googleads___v1___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode.ClosedValueType
    advertising_channel_type = ... # type: google___ads___googleads___v1___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum.AdvertisingChannelType.ClosedValueType
    advertising_channel_sub_type = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[google___ads___googleads___v1___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType.ClosedValueType]

    @property
    def include_default_channel_sub_type(self) -> google___protobuf___wrappers_pb2___BoolValue: ...

    def __init__(self,
        *,
        availability_mode : typing___Optional[google___ads___googleads___v1___enums___criterion_category_channel_availability_mode_pb2___CriterionCategoryChannelAvailabilityModeEnum.CriterionCategoryChannelAvailabilityMode.ClosedValueType] = None,
        advertising_channel_type : typing___Optional[google___ads___googleads___v1___enums___advertising_channel_type_pb2___AdvertisingChannelTypeEnum.AdvertisingChannelType.ClosedValueType] = None,
        advertising_channel_sub_type : typing___Optional[typing___Iterable[google___ads___googleads___v1___enums___advertising_channel_sub_type_pb2___AdvertisingChannelSubTypeEnum.AdvertisingChannelSubType.ClosedValueType]] = None,
        include_default_channel_sub_type : typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CriterionCategoryChannelAvailability: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"include_default_channel_sub_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"advertising_channel_sub_type",u"advertising_channel_type",u"availability_mode",u"include_default_channel_sub_type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"include_default_channel_sub_type",b"include_default_channel_sub_type"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"advertising_channel_sub_type",b"advertising_channel_sub_type",u"advertising_channel_type",b"advertising_channel_type",u"availability_mode",b"availability_mode",u"include_default_channel_sub_type",b"include_default_channel_sub_type"]) -> None: ...

class CriterionCategoryLocaleAvailability(google___protobuf___message___Message):
    availability_mode = ... # type: google___ads___googleads___v1___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode.ClosedValueType

    @property
    def country_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        availability_mode : typing___Optional[google___ads___googleads___v1___enums___criterion_category_locale_availability_mode_pb2___CriterionCategoryLocaleAvailabilityModeEnum.CriterionCategoryLocaleAvailabilityMode.ClosedValueType] = None,
        country_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        language_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CriterionCategoryLocaleAvailability: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"country_code",u"language_code"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"availability_mode",u"country_code",u"language_code"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"country_code",b"country_code",u"language_code",b"language_code"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"availability_mode",b"availability_mode",u"country_code",b"country_code",u"language_code",b"language_code"]) -> None: ...
