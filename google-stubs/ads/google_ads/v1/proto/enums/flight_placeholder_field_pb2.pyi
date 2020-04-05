# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)


builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class FlightPlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FlightPlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'FlightPlaceholderFieldEnum.FlightPlaceholderField': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['FlightPlaceholderFieldEnum.FlightPlaceholderField']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'FlightPlaceholderFieldEnum.FlightPlaceholderField']]: ...
        UNSPECIFIED = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 0)
        UNKNOWN = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 1)
        DESTINATION_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 2)
        ORIGIN_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 3)
        FLIGHT_DESCRIPTION = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 4)
        ORIGIN_NAME = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 5)
        DESTINATION_NAME = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 6)
        FLIGHT_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 7)
        FORMATTED_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 8)
        FLIGHT_SALE_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 9)
        FORMATTED_SALE_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 10)
        IMAGE_URL = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 11)
        FINAL_URLS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 12)
        FINAL_MOBILE_URLS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 13)
        TRACKING_URL = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 14)
        ANDROID_APP_LINK = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 15)
        SIMILAR_DESTINATION_IDS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 16)
        IOS_APP_LINK = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 17)
        IOS_APP_STORE_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 18)
    UNSPECIFIED = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 0)
    UNKNOWN = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 1)
    DESTINATION_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 2)
    ORIGIN_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 3)
    FLIGHT_DESCRIPTION = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 4)
    ORIGIN_NAME = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 5)
    DESTINATION_NAME = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 6)
    FLIGHT_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 7)
    FORMATTED_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 8)
    FLIGHT_SALE_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 9)
    FORMATTED_SALE_PRICE = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 10)
    IMAGE_URL = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 11)
    FINAL_URLS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 12)
    FINAL_MOBILE_URLS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 13)
    TRACKING_URL = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 14)
    ANDROID_APP_LINK = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 15)
    SIMILAR_DESTINATION_IDS = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 16)
    IOS_APP_LINK = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 17)
    IOS_APP_STORE_ID = typing___cast('FlightPlaceholderFieldEnum.FlightPlaceholderField', 18)
    global___FlightPlaceholderField = FlightPlaceholderField


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FlightPlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FlightPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___FlightPlaceholderFieldEnum = FlightPlaceholderFieldEnum
