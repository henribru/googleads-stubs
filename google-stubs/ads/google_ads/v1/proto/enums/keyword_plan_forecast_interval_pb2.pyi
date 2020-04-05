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


class KeywordPlanForecastIntervalEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class KeywordPlanForecastInterval(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(cls, name: builtin___str) -> 'KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval': ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List['KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval']: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[builtin___str, 'KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval']]: ...
        UNSPECIFIED = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 0)
        UNKNOWN = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 1)
        NEXT_WEEK = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 3)
        NEXT_MONTH = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 4)
        NEXT_QUARTER = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 5)
    UNSPECIFIED = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 0)
    UNKNOWN = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 1)
    NEXT_WEEK = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 3)
    NEXT_MONTH = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 4)
    NEXT_QUARTER = typing___cast('KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval', 5)
    global___KeywordPlanForecastInterval = KeywordPlanForecastInterval


    def __init__(self,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> KeywordPlanForecastIntervalEnum: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> KeywordPlanForecastIntervalEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
global___KeywordPlanForecastIntervalEnum = KeywordPlanForecastIntervalEnum
