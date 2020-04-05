# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.frequency_cap_event_type_pb2 import (
    FrequencyCapEventTypeEnum as google___ads___googleads___v1___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.frequency_cap_level_pb2 import (
    FrequencyCapLevelEnum as google___ads___googleads___v1___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum,
)

from google.ads.google_ads.v1.proto.enums.frequency_cap_time_unit_pb2 import (
    FrequencyCapTimeUnitEnum as google___ads___googleads___v1___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
)

from typing import (
    Optional as typing___Optional,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class FrequencyCapEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def key(self) -> global___FrequencyCapKey: ...

    @property
    def cap(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

    def __init__(self,
        *,
        key : typing___Optional[global___FrequencyCapKey] = None,
        cap : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FrequencyCapEntry: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FrequencyCapEntry: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cap",b"cap",u"key",b"key"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cap",b"cap",u"key",b"key"]) -> None: ...
global___FrequencyCapEntry = FrequencyCapEntry

class FrequencyCapKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    level = ... # type: google___ads___googleads___v1___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum.FrequencyCapLevel
    event_type = ... # type: google___ads___googleads___v1___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum.FrequencyCapEventType
    time_unit = ... # type: google___ads___googleads___v1___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit

    @property
    def time_length(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

    def __init__(self,
        *,
        level : typing___Optional[google___ads___googleads___v1___enums___frequency_cap_level_pb2___FrequencyCapLevelEnum.FrequencyCapLevel] = None,
        event_type : typing___Optional[google___ads___googleads___v1___enums___frequency_cap_event_type_pb2___FrequencyCapEventTypeEnum.FrequencyCapEventType] = None,
        time_unit : typing___Optional[google___ads___googleads___v1___enums___frequency_cap_time_unit_pb2___FrequencyCapTimeUnitEnum.FrequencyCapTimeUnit] = None,
        time_length : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> FrequencyCapKey: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> FrequencyCapKey: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"time_length",b"time_length"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"event_type",b"event_type",u"level",b"level",u"time_length",b"time_length",u"time_unit",b"time_unit"]) -> None: ...
global___FrequencyCapKey = FrequencyCapKey
