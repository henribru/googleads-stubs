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

class LocationGroupRadiusUnitsEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class LocationGroupRadiusUnits(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(
            cls,
        ) -> typing___List["LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[
                builtin___str, "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits"
            ]
        ]: ...
        UNSPECIFIED = typing___cast(
            "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 0
        )
        UNKNOWN = typing___cast(
            "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 1
        )
        METERS = typing___cast(
            "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 2
        )
        MILES = typing___cast(
            "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 3
        )
    UNSPECIFIED = typing___cast(
        "LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 0
    )
    UNKNOWN = typing___cast("LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 1)
    METERS = typing___cast("LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 2)
    MILES = typing___cast("LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits", 3)
    global___LocationGroupRadiusUnits = LocationGroupRadiusUnits
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LocationGroupRadiusUnitsEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> LocationGroupRadiusUnitsEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___LocationGroupRadiusUnitsEnum = LocationGroupRadiusUnitsEnum