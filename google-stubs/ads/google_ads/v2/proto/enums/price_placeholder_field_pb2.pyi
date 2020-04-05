# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

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

class PricePlaceholderFieldEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PricePlaceholderField(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "PricePlaceholderFieldEnum.PricePlaceholderField": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["PricePlaceholderFieldEnum.PricePlaceholderField"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "PricePlaceholderFieldEnum.PricePlaceholderField"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 0
        )
        UNKNOWN = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 1)
        TYPE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 2)
        PRICE_QUALIFIER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 3
        )
        TRACKING_TEMPLATE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 4
        )
        LANGUAGE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 5)
        FINAL_URL_SUFFIX = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 6
        )
        ITEM_1_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 100
        )
        ITEM_1_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 101
        )
        ITEM_1_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 102
        )
        ITEM_1_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 103
        )
        ITEM_1_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 104
        )
        ITEM_1_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 105
        )
        ITEM_2_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 200
        )
        ITEM_2_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 201
        )
        ITEM_2_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 202
        )
        ITEM_2_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 203
        )
        ITEM_2_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 204
        )
        ITEM_2_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 205
        )
        ITEM_3_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 300
        )
        ITEM_3_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 301
        )
        ITEM_3_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 302
        )
        ITEM_3_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 303
        )
        ITEM_3_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 304
        )
        ITEM_3_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 305
        )
        ITEM_4_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 400
        )
        ITEM_4_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 401
        )
        ITEM_4_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 402
        )
        ITEM_4_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 403
        )
        ITEM_4_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 404
        )
        ITEM_4_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 405
        )
        ITEM_5_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 500
        )
        ITEM_5_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 501
        )
        ITEM_5_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 502
        )
        ITEM_5_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 503
        )
        ITEM_5_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 504
        )
        ITEM_5_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 505
        )
        ITEM_6_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 600
        )
        ITEM_6_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 601
        )
        ITEM_6_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 602
        )
        ITEM_6_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 603
        )
        ITEM_6_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 604
        )
        ITEM_6_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 605
        )
        ITEM_7_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 700
        )
        ITEM_7_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 701
        )
        ITEM_7_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 702
        )
        ITEM_7_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 703
        )
        ITEM_7_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 704
        )
        ITEM_7_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 705
        )
        ITEM_8_HEADER = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 800
        )
        ITEM_8_DESCRIPTION = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 801
        )
        ITEM_8_PRICE = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 802
        )
        ITEM_8_UNIT = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 803
        )
        ITEM_8_FINAL_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 804
        )
        ITEM_8_FINAL_MOBILE_URLS = typing___cast(
            "PricePlaceholderFieldEnum.PricePlaceholderField", 805
        )
    UNSPECIFIED = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 0)
    UNKNOWN = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 1)
    TYPE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 2)
    PRICE_QUALIFIER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 3
    )
    TRACKING_TEMPLATE = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 4
    )
    LANGUAGE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 5)
    FINAL_URL_SUFFIX = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 6
    )
    ITEM_1_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 100
    )
    ITEM_1_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 101
    )
    ITEM_1_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 102)
    ITEM_1_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 103)
    ITEM_1_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 104
    )
    ITEM_1_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 105
    )
    ITEM_2_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 200
    )
    ITEM_2_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 201
    )
    ITEM_2_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 202)
    ITEM_2_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 203)
    ITEM_2_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 204
    )
    ITEM_2_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 205
    )
    ITEM_3_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 300
    )
    ITEM_3_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 301
    )
    ITEM_3_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 302)
    ITEM_3_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 303)
    ITEM_3_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 304
    )
    ITEM_3_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 305
    )
    ITEM_4_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 400
    )
    ITEM_4_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 401
    )
    ITEM_4_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 402)
    ITEM_4_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 403)
    ITEM_4_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 404
    )
    ITEM_4_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 405
    )
    ITEM_5_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 500
    )
    ITEM_5_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 501
    )
    ITEM_5_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 502)
    ITEM_5_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 503)
    ITEM_5_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 504
    )
    ITEM_5_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 505
    )
    ITEM_6_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 600
    )
    ITEM_6_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 601
    )
    ITEM_6_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 602)
    ITEM_6_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 603)
    ITEM_6_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 604
    )
    ITEM_6_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 605
    )
    ITEM_7_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 700
    )
    ITEM_7_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 701
    )
    ITEM_7_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 702)
    ITEM_7_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 703)
    ITEM_7_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 704
    )
    ITEM_7_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 705
    )
    ITEM_8_HEADER = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 800
    )
    ITEM_8_DESCRIPTION = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 801
    )
    ITEM_8_PRICE = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 802)
    ITEM_8_UNIT = typing___cast("PricePlaceholderFieldEnum.PricePlaceholderField", 803)
    ITEM_8_FINAL_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 804
    )
    ITEM_8_FINAL_MOBILE_URLS = typing___cast(
        "PricePlaceholderFieldEnum.PricePlaceholderField", 805
    )
    global___PricePlaceholderField = PricePlaceholderField
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PricePlaceholderFieldEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> PricePlaceholderFieldEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___PricePlaceholderFieldEnum = PricePlaceholderFieldEnum
