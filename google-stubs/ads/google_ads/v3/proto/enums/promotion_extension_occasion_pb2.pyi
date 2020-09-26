# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    NewType as typing___NewType,
    cast as typing___cast,
)

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class PromotionExtensionOccasionEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    PromotionExtensionOccasionValue = typing___NewType(
        "PromotionExtensionOccasionValue", builtin___int
    )
    type___PromotionExtensionOccasionValue = PromotionExtensionOccasionValue
    PromotionExtensionOccasion: _PromotionExtensionOccasion
    class _PromotionExtensionOccasion(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 0
        )
        UNKNOWN = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 1
        )
        NEW_YEARS = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 2
        )
        CHINESE_NEW_YEAR = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 3
        )
        VALENTINES_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 4
        )
        EASTER = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 5
        )
        MOTHERS_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 6
        )
        FATHERS_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 7
        )
        LABOR_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 8
        )
        BACK_TO_SCHOOL = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 9
        )
        HALLOWEEN = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 10
        )
        BLACK_FRIDAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 11
        )
        CYBER_MONDAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 12
        )
        CHRISTMAS = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 13
        )
        BOXING_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 14
        )
        INDEPENDENCE_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 15
        )
        NATIONAL_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 16
        )
        END_OF_SEASON = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 17
        )
        WINTER_SALE = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 18
        )
        SUMMER_SALE = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 19
        )
        FALL_SALE = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 20
        )
        SPRING_SALE = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 21
        )
        RAMADAN = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 22
        )
        EID_AL_FITR = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 23
        )
        EID_AL_ADHA = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 24
        )
        SINGLES_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 25
        )
        WOMENS_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 26
        )
        HOLI = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 27
        )
        PARENTS_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 28
        )
        ST_NICHOLAS_DAY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 29
        )
        CARNIVAL = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 30
        )
        EPIPHANY = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 31
        )
        ROSH_HASHANAH = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 32
        )
        PASSOVER = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 33
        )
        HANUKKAH = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 34
        )
        DIWALI = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 35
        )
        NAVRATRI = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 36
        )
        SONGKRAN = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 37
        )
        YEAR_END_GIFT = typing___cast(
            PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 38
        )
    UNSPECIFIED = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 0
    )
    UNKNOWN = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 1
    )
    NEW_YEARS = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 2
    )
    CHINESE_NEW_YEAR = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 3
    )
    VALENTINES_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 4
    )
    EASTER = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 5
    )
    MOTHERS_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 6
    )
    FATHERS_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 7
    )
    LABOR_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 8
    )
    BACK_TO_SCHOOL = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 9
    )
    HALLOWEEN = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 10
    )
    BLACK_FRIDAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 11
    )
    CYBER_MONDAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 12
    )
    CHRISTMAS = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 13
    )
    BOXING_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 14
    )
    INDEPENDENCE_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 15
    )
    NATIONAL_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 16
    )
    END_OF_SEASON = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 17
    )
    WINTER_SALE = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 18
    )
    SUMMER_SALE = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 19
    )
    FALL_SALE = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 20
    )
    SPRING_SALE = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 21
    )
    RAMADAN = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 22
    )
    EID_AL_FITR = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 23
    )
    EID_AL_ADHA = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 24
    )
    SINGLES_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 25
    )
    WOMENS_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 26
    )
    HOLI = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 27
    )
    PARENTS_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 28
    )
    ST_NICHOLAS_DAY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 29
    )
    CARNIVAL = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 30
    )
    EPIPHANY = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 31
    )
    ROSH_HASHANAH = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 32
    )
    PASSOVER = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 33
    )
    HANUKKAH = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 34
    )
    DIWALI = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 35
    )
    NAVRATRI = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 36
    )
    SONGKRAN = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 37
    )
    YEAR_END_GIFT = typing___cast(
        PromotionExtensionOccasionEnum.PromotionExtensionOccasionValue, 38
    )
    type___PromotionExtensionOccasion = PromotionExtensionOccasion
    def __init__(self,) -> None: ...

type___PromotionExtensionOccasionEnum = PromotionExtensionOccasionEnum
