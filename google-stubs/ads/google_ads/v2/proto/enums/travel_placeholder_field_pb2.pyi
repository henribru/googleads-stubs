# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class TravelPlaceholderFieldEnum(google___protobuf___message___Message):
    class TravelPlaceholderField(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['DESTINATION_ID'],typing_extensions___Literal['ORIGIN_ID'],typing_extensions___Literal['TITLE'],typing_extensions___Literal['DESTINATION_NAME'],typing_extensions___Literal['ORIGIN_NAME'],typing_extensions___Literal['PRICE'],typing_extensions___Literal['FORMATTED_PRICE'],typing_extensions___Literal['SALE_PRICE'],typing_extensions___Literal['FORMATTED_SALE_PRICE'],typing_extensions___Literal['IMAGE_URL'],typing_extensions___Literal['CATEGORY'],typing_extensions___Literal['CONTEXTUAL_KEYWORDS'],typing_extensions___Literal['DESTINATION_ADDRESS'],typing_extensions___Literal['FINAL_URL'],typing_extensions___Literal['FINAL_MOBILE_URLS'],typing_extensions___Literal['TRACKING_URL'],typing_extensions___Literal['ANDROID_APP_LINK'],typing_extensions___Literal['SIMILAR_DESTINATION_IDS'],typing_extensions___Literal['IOS_APP_LINK'],typing_extensions___Literal['IOS_APP_STORE_ID']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5],typing_extensions___Literal[6],typing_extensions___Literal[7],typing_extensions___Literal[8],typing_extensions___Literal[9],typing_extensions___Literal[10],typing_extensions___Literal[11],typing_extensions___Literal[12],typing_extensions___Literal[13],typing_extensions___Literal[14],typing_extensions___Literal[15],typing_extensions___Literal[16],typing_extensions___Literal[17],typing_extensions___Literal[18],typing_extensions___Literal[19],typing_extensions___Literal[20],typing_extensions___Literal[21]]
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: ClosedValueType) -> str: ...
        @classmethod
        def Value(cls, name: ClosedKeyType) -> ClosedValueType: ...
        @classmethod
        def keys(cls) -> typing___List[ClosedKeyType]: ...
        @classmethod
        def values(cls) -> typing___List[ClosedValueType]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[ClosedKeyType, ClosedValueType]]: ...
        UNSPECIFIED: typing_extensions___Literal[0]
        UNKNOWN: typing_extensions___Literal[1]
        DESTINATION_ID: typing_extensions___Literal[2]
        ORIGIN_ID: typing_extensions___Literal[3]
        TITLE: typing_extensions___Literal[4]
        DESTINATION_NAME: typing_extensions___Literal[5]
        ORIGIN_NAME: typing_extensions___Literal[6]
        PRICE: typing_extensions___Literal[7]
        FORMATTED_PRICE: typing_extensions___Literal[8]
        SALE_PRICE: typing_extensions___Literal[9]
        FORMATTED_SALE_PRICE: typing_extensions___Literal[10]
        IMAGE_URL: typing_extensions___Literal[11]
        CATEGORY: typing_extensions___Literal[12]
        CONTEXTUAL_KEYWORDS: typing_extensions___Literal[13]
        DESTINATION_ADDRESS: typing_extensions___Literal[14]
        FINAL_URL: typing_extensions___Literal[15]
        FINAL_MOBILE_URLS: typing_extensions___Literal[16]
        TRACKING_URL: typing_extensions___Literal[17]
        ANDROID_APP_LINK: typing_extensions___Literal[18]
        SIMILAR_DESTINATION_IDS: typing_extensions___Literal[19]
        IOS_APP_LINK: typing_extensions___Literal[20]
        IOS_APP_STORE_ID: typing_extensions___Literal[21]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    DESTINATION_ID: typing_extensions___Literal[2]
    ORIGIN_ID: typing_extensions___Literal[3]
    TITLE: typing_extensions___Literal[4]
    DESTINATION_NAME: typing_extensions___Literal[5]
    ORIGIN_NAME: typing_extensions___Literal[6]
    PRICE: typing_extensions___Literal[7]
    FORMATTED_PRICE: typing_extensions___Literal[8]
    SALE_PRICE: typing_extensions___Literal[9]
    FORMATTED_SALE_PRICE: typing_extensions___Literal[10]
    IMAGE_URL: typing_extensions___Literal[11]
    CATEGORY: typing_extensions___Literal[12]
    CONTEXTUAL_KEYWORDS: typing_extensions___Literal[13]
    DESTINATION_ADDRESS: typing_extensions___Literal[14]
    FINAL_URL: typing_extensions___Literal[15]
    FINAL_MOBILE_URLS: typing_extensions___Literal[16]
    TRACKING_URL: typing_extensions___Literal[17]
    ANDROID_APP_LINK: typing_extensions___Literal[18]
    SIMILAR_DESTINATION_IDS: typing_extensions___Literal[19]
    IOS_APP_LINK: typing_extensions___Literal[20]
    IOS_APP_STORE_ID: typing_extensions___Literal[21]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> TravelPlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
