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


class CriterionCategoryLocaleAvailabilityModeEnum(google___protobuf___message___Message):
    class CriterionCategoryLocaleAvailabilityMode(object):
        ClosedKeyType = typing___Union[typing_extensions___Literal['UNSPECIFIED'],typing_extensions___Literal['UNKNOWN'],typing_extensions___Literal['ALL_LOCALES'],typing_extensions___Literal['COUNTRY_AND_ALL_LANGUAGES'],typing_extensions___Literal['LANGUAGE_AND_ALL_COUNTRIES'],typing_extensions___Literal['COUNTRY_AND_LANGUAGE']]
        ClosedValueType = typing___Union[typing_extensions___Literal[0],typing_extensions___Literal[1],typing_extensions___Literal[2],typing_extensions___Literal[3],typing_extensions___Literal[4],typing_extensions___Literal[5]]
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
        ALL_LOCALES: typing_extensions___Literal[2]
        COUNTRY_AND_ALL_LANGUAGES: typing_extensions___Literal[3]
        LANGUAGE_AND_ALL_COUNTRIES: typing_extensions___Literal[4]
        COUNTRY_AND_LANGUAGE: typing_extensions___Literal[5]
    UNSPECIFIED: typing_extensions___Literal[0]
    UNKNOWN: typing_extensions___Literal[1]
    ALL_LOCALES: typing_extensions___Literal[2]
    COUNTRY_AND_ALL_LANGUAGES: typing_extensions___Literal[3]
    LANGUAGE_AND_ALL_COUNTRIES: typing_extensions___Literal[4]
    COUNTRY_AND_LANGUAGE: typing_extensions___Literal[5]


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CriterionCategoryLocaleAvailabilityModeEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
