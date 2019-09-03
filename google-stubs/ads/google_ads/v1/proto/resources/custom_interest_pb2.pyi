# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.custom_interest_member_type_pb2 import (
    CustomInterestMemberTypeEnum as google___ads___googleads___v1___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.custom_interest_status_pb2 import (
    CustomInterestStatusEnum as google___ads___googleads___v1___enums___custom_interest_status_pb2___CustomInterestStatusEnum,
)

from google.ads.google_ads.v1.proto.enums.custom_interest_type_pb2 import (
    CustomInterestTypeEnum as google___ads___googleads___v1___enums___custom_interest_type_pb2___CustomInterestTypeEnum,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class CustomInterest(google___protobuf___message___Message):
    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v1___enums___custom_interest_status_pb2___CustomInterestStatusEnum.CustomInterestStatus.ClosedValueType
    type = ... # type: google___ads___googleads___v1___enums___custom_interest_type_pb2___CustomInterestTypeEnum.CustomInterestType.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def members(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CustomInterestMember]: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        status : typing___Optional[google___ads___googleads___v1___enums___custom_interest_status_pb2___CustomInterestStatusEnum.CustomInterestStatus.ClosedValueType] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___custom_interest_type_pb2___CustomInterestTypeEnum.CustomInterestType.ClosedValueType] = None,
        description : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        members : typing___Optional[typing___Iterable[CustomInterestMember]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomInterest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"description",u"id",u"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",u"id",u"members",u"name",u"resource_name",u"status",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"description",b"description",u"id",b"id",u"name",b"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"description",b"description",u"id",b"id",u"members",b"members",u"name",b"name",u"resource_name",b"resource_name",u"status",b"status",u"type",b"type"]) -> None: ...

class CustomInterestMember(google___protobuf___message___Message):
    member_type = ... # type: google___ads___googleads___v1___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum.CustomInterestMemberType.ClosedValueType

    @property
    def parameter(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        member_type : typing___Optional[google___ads___googleads___v1___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum.CustomInterestMemberType.ClosedValueType] = None,
        parameter : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomInterestMember: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"parameter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"member_type",u"parameter"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"parameter",b"parameter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"member_type",b"member_type",u"parameter",b"parameter"]) -> None: ...
