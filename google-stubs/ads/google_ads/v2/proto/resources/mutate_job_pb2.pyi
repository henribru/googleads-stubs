# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.mutate_job_status_pb2 import (
    MutateJobStatusEnum as google___ads___googleads___v2___enums___mutate_job_status_pb2___MutateJobStatusEnum,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class MutateJob(google___protobuf___message___Message):
    class MutateJobMetadata(google___protobuf___message___Message):

        @property
        def creation_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        @property
        def completion_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        @property
        def estimated_completion_ratio(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

        @property
        def operation_count(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        @property
        def executed_operation_count(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

        def __init__(self,
            *,
            creation_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            completion_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            estimated_completion_ratio : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
            operation_count : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            executed_operation_count : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> MutateJob.MutateJobMetadata: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"completion_date_time",u"creation_date_time",u"estimated_completion_ratio",u"executed_operation_count",u"operation_count"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"completion_date_time",u"creation_date_time",u"estimated_completion_ratio",u"executed_operation_count",u"operation_count"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"completion_date_time",b"completion_date_time",u"creation_date_time",b"creation_date_time",u"estimated_completion_ratio",b"estimated_completion_ratio",u"executed_operation_count",b"executed_operation_count",u"operation_count",b"operation_count"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"completion_date_time",b"completion_date_time",u"creation_date_time",b"creation_date_time",u"estimated_completion_ratio",b"estimated_completion_ratio",u"executed_operation_count",b"executed_operation_count",u"operation_count",b"operation_count"]) -> None: ...

    resource_name = ... # type: typing___Text
    status = ... # type: google___ads___googleads___v2___enums___mutate_job_status_pb2___MutateJobStatusEnum.MutateJobStatus.ClosedValueType

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def next_add_sequence_token(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def metadata(self) -> MutateJob.MutateJobMetadata: ...

    @property
    def long_running_operation(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        next_add_sequence_token : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        metadata : typing___Optional[MutateJob.MutateJobMetadata] = None,
        status : typing___Optional[google___ads___googleads___v2___enums___mutate_job_status_pb2___MutateJobStatusEnum.MutateJobStatus.ClosedValueType] = None,
        long_running_operation : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> MutateJob: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"id",u"long_running_operation",u"metadata",u"next_add_sequence_token"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",u"long_running_operation",u"metadata",u"next_add_sequence_token",u"resource_name",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"id",b"id",u"long_running_operation",b"long_running_operation",u"metadata",b"metadata",u"next_add_sequence_token",b"next_add_sequence_token"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"long_running_operation",b"long_running_operation",u"metadata",b"metadata",u"next_add_sequence_token",b"next_add_sequence_token",u"resource_name",b"resource_name",u"status",b"status"]) -> None: ...
