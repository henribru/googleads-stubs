"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.enums.shared_set_status_pb2
import google.ads.google_ads.v4.proto.enums.shared_set_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class SharedSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    MEMBER_COUNT_FIELD_NUMBER: builtins.int
    REFERENCE_COUNT_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    type: google.ads.google_ads.v4.proto.enums.shared_set_type_pb2.SharedSetTypeEnum.SharedSetType.V = (
        ...
    )
    status: google.ads.google_ads.v4.proto.enums.shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus.V = (
        ...
    )
    @property
    def id(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def member_count(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    @property
    def reference_count(self) -> google.protobuf.wrappers_pb2.Int64Value: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        type: google.ads.google_ads.v4.proto.enums.shared_set_type_pb2.SharedSetTypeEnum.SharedSetType.V = ...,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        status: google.ads.google_ads.v4.proto.enums.shared_set_status_pb2.SharedSetStatusEnum.SharedSetStatus.V = ...,
        member_count: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        reference_count: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "member_count",
            b"member_count",
            "name",
            b"name",
            "reference_count",
            b"reference_count",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "member_count",
            b"member_count",
            "name",
            b"name",
            "reference_count",
            b"reference_count",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "type",
            b"type",
        ],
    ) -> None: ...

global___SharedSet = SharedSet
