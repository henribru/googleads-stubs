# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.custom_interest_member_type_pb2 import (
    CustomInterestMemberTypeEnum as google___ads___googleads___v2___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum,
)

from google.ads.google_ads.v2.proto.enums.custom_interest_status_pb2 import (
    CustomInterestStatusEnum as google___ads___googleads___v2___enums___custom_interest_status_pb2___CustomInterestStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.custom_interest_type_pb2 import (
    CustomInterestTypeEnum as google___ads___googleads___v2___enums___custom_interest_type_pb2___CustomInterestTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class CustomInterest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    status = (
        ...
    )  # type: google___ads___googleads___v2___enums___custom_interest_status_pb2___CustomInterestStatusEnum.CustomInterestStatus
    type = (
        ...
    )  # type: google___ads___googleads___v2___enums___custom_interest_type_pb2___CustomInterestTypeEnum.CustomInterestType
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def members(
        self
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        global___CustomInterestMember
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___custom_interest_status_pb2___CustomInterestStatusEnum.CustomInterestStatus
        ] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___custom_interest_type_pb2___CustomInterestTypeEnum.CustomInterestType
        ] = None,
        description: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        members: typing___Optional[
            typing___Iterable[global___CustomInterestMember]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CustomInterest: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomInterest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "description", b"description", "id", b"id", "name", b"name"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "description",
            b"description",
            "id",
            b"id",
            "members",
            b"members",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "type",
            b"type",
        ],
    ) -> None: ...

global___CustomInterest = CustomInterest

class CustomInterestMember(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    member_type = (
        ...
    )  # type: google___ads___googleads___v2___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum.CustomInterestMemberType
    @property
    def parameter(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        member_type: typing___Optional[
            google___ads___googleads___v2___enums___custom_interest_member_type_pb2___CustomInterestMemberTypeEnum.CustomInterestMemberType
        ] = None,
        parameter: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CustomInterestMember: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CustomInterestMember: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["parameter", b"parameter"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "member_type", b"member_type", "parameter", b"parameter"
        ],
    ) -> None: ...

global___CustomInterestMember = CustomInterestMember
