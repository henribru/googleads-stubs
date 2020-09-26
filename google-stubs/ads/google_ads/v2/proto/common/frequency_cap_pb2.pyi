# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v2.proto.enums.frequency_cap_event_type_pb2 import (
    FrequencyCapEventTypeEnum as google___ads___googleads___v2___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum,
)

from google.ads.google_ads.v2.proto.enums.frequency_cap_level_pb2 import (
    FrequencyCapLevelEnum as google___ads___googleads___v2___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum,
)

from google.ads.google_ads.v2.proto.enums.frequency_cap_time_unit_pb2 import (
    FrequencyCapTimeUnitEnum as google___ads___googleads___v2___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
)

from typing import Optional as typing___Optional

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class FrequencyCapEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def key(self) -> type___FrequencyCapKey: ...
    @property
    def cap(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    def __init__(
        self,
        *,
        key: typing___Optional[type___FrequencyCapKey] = None,
        cap: typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["cap", b"cap", "key", b"key"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["cap", b"cap", "key", b"key"]
    ) -> None: ...

type___FrequencyCapEntry = FrequencyCapEntry

class FrequencyCapKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    level: google___ads___googleads___v2___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum.FrequencyCapLevelValue = ...
    event_type: google___ads___googleads___v2___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue = ...
    time_unit: google___ads___googleads___v2___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum.FrequencyCapTimeUnitValue = ...
    @property
    def time_length(self) -> google___protobuf___wrappers_pb2___Int32Value: ...
    def __init__(
        self,
        *,
        level: typing___Optional[
            google___ads___googleads___v2___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum.FrequencyCapLevelValue
        ] = None,
        event_type: typing___Optional[
            google___ads___googleads___v2___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum.FrequencyCapEventTypeValue
        ] = None,
        time_unit: typing___Optional[
            google___ads___googleads___v2___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum.FrequencyCapTimeUnitValue
        ] = None,
        time_length: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["time_length", b"time_length"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "event_type",
            b"event_type",
            "level",
            b"level",
            "time_length",
            b"time_length",
            "time_unit",
            b"time_unit",
        ],
    ) -> None: ...

type___FrequencyCapKey = FrequencyCapKey
