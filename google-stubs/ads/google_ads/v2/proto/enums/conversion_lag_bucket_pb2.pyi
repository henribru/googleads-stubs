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

class ConversionLagBucketEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    ConversionLagBucketValue = typing___NewType(
        "ConversionLagBucketValue", builtin___int
    )
    type___ConversionLagBucketValue = ConversionLagBucketValue
    ConversionLagBucket: _ConversionLagBucket
    class _ConversionLagBucket(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            ConversionLagBucketEnum.ConversionLagBucketValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(ConversionLagBucketEnum.ConversionLagBucketValue, 0)
        UNKNOWN = typing___cast(ConversionLagBucketEnum.ConversionLagBucketValue, 1)
        LESS_THAN_ONE_DAY = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 2
        )
        ONE_TO_TWO_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 3
        )
        TWO_TO_THREE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 4
        )
        THREE_TO_FOUR_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 5
        )
        FOUR_TO_FIVE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 6
        )
        FIVE_TO_SIX_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 7
        )
        SIX_TO_SEVEN_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 8
        )
        SEVEN_TO_EIGHT_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 9
        )
        EIGHT_TO_NINE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 10
        )
        NINE_TO_TEN_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 11
        )
        TEN_TO_ELEVEN_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 12
        )
        ELEVEN_TO_TWELVE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 13
        )
        TWELVE_TO_THIRTEEN_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 14
        )
        THIRTEEN_TO_FOURTEEN_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 15
        )
        FOURTEEN_TO_TWENTY_ONE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 16
        )
        TWENTY_ONE_TO_THIRTY_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 17
        )
        THIRTY_TO_FORTY_FIVE_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 18
        )
        FORTY_FIVE_TO_SIXTY_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 19
        )
        SIXTY_TO_NINETY_DAYS = typing___cast(
            ConversionLagBucketEnum.ConversionLagBucketValue, 20
        )
    UNSPECIFIED = typing___cast(ConversionLagBucketEnum.ConversionLagBucketValue, 0)
    UNKNOWN = typing___cast(ConversionLagBucketEnum.ConversionLagBucketValue, 1)
    LESS_THAN_ONE_DAY = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 2
    )
    ONE_TO_TWO_DAYS = typing___cast(ConversionLagBucketEnum.ConversionLagBucketValue, 3)
    TWO_TO_THREE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 4
    )
    THREE_TO_FOUR_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 5
    )
    FOUR_TO_FIVE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 6
    )
    FIVE_TO_SIX_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 7
    )
    SIX_TO_SEVEN_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 8
    )
    SEVEN_TO_EIGHT_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 9
    )
    EIGHT_TO_NINE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 10
    )
    NINE_TO_TEN_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 11
    )
    TEN_TO_ELEVEN_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 12
    )
    ELEVEN_TO_TWELVE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 13
    )
    TWELVE_TO_THIRTEEN_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 14
    )
    THIRTEEN_TO_FOURTEEN_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 15
    )
    FOURTEEN_TO_TWENTY_ONE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 16
    )
    TWENTY_ONE_TO_THIRTY_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 17
    )
    THIRTY_TO_FORTY_FIVE_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 18
    )
    FORTY_FIVE_TO_SIXTY_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 19
    )
    SIXTY_TO_NINETY_DAYS = typing___cast(
        ConversionLagBucketEnum.ConversionLagBucketValue, 20
    )
    type___ConversionLagBucket = ConversionLagBucket
    def __init__(self,) -> None: ...

type___ConversionLagBucketEnum = ConversionLagBucketEnum
