# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.billing_setup_status_pb2 import (
    BillingSetupStatusEnum as google___ads___googleads___v2___enums___billing_setup_status_pb2___BillingSetupStatusEnum,
)

from google.ads.google_ads.v2.proto.enums.time_type_pb2 import (
    TimeTypeEnum as google___ads___googleads___v2___enums___time_type_pb2___TimeTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
    overload as typing___overload,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class BillingSetup(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class PaymentsAccountInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def payments_account_id(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def payments_account_name(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def payments_profile_id(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def payments_profile_name(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def secondary_payments_profile_id(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        def __init__(
            self,
            *,
            payments_account_id: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            payments_account_name: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            payments_profile_id: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            payments_profile_name: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            secondary_payments_profile_id: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
        ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(
                cls, s: builtin___bytes
            ) -> BillingSetup.PaymentsAccountInfo: ...
        else:
            @classmethod
            def FromString(
                cls,
                s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode],
            ) -> BillingSetup.PaymentsAccountInfo: ...
        def MergeFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def CopyFrom(
            self, other_msg: google___protobuf___message___Message
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "payments_account_id",
                b"payments_account_id",
                "payments_account_name",
                b"payments_account_name",
                "payments_profile_id",
                b"payments_profile_id",
                "payments_profile_name",
                b"payments_profile_name",
                "secondary_payments_profile_id",
                b"secondary_payments_profile_id",
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "payments_account_id",
                b"payments_account_id",
                "payments_account_name",
                b"payments_account_name",
                "payments_profile_id",
                b"payments_profile_id",
                "payments_profile_name",
                b"payments_profile_name",
                "secondary_payments_profile_id",
                b"secondary_payments_profile_id",
            ],
        ) -> None: ...
    global___PaymentsAccountInfo = PaymentsAccountInfo

    resource_name = ...  # type: typing___Text
    status = (
        ...
    )  # type: google___ads___googleads___v2___enums___billing_setup_status_pb2___BillingSetupStatusEnum.BillingSetupStatus
    start_time_type = (
        ...
    )  # type: google___ads___googleads___v2___enums___time_type_pb2___TimeTypeEnum.TimeType
    end_time_type = (
        ...
    )  # type: google___ads___googleads___v2___enums___time_type_pb2___TimeTypeEnum.TimeType
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def payments_account(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def payments_account_info(self) -> global___BillingSetup.PaymentsAccountInfo: ...
    @property
    def start_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        status: typing___Optional[
            google___ads___googleads___v2___enums___billing_setup_status_pb2___BillingSetupStatusEnum.BillingSetupStatus
        ] = None,
        payments_account: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        payments_account_info: typing___Optional[
            global___BillingSetup.PaymentsAccountInfo
        ] = None,
        start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        start_time_type: typing___Optional[
            google___ads___googleads___v2___enums___time_type_pb2___TimeTypeEnum.TimeType
        ] = None,
        end_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_time_type: typing___Optional[
            google___ads___googleads___v2___enums___time_type_pb2___TimeTypeEnum.TimeType
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> BillingSetup: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> BillingSetup: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "end_date_time",
            b"end_date_time",
            "end_time",
            b"end_time",
            "end_time_type",
            b"end_time_type",
            "id",
            b"id",
            "payments_account",
            b"payments_account",
            "payments_account_info",
            b"payments_account_info",
            "start_date_time",
            b"start_date_time",
            "start_time",
            b"start_time",
            "start_time_type",
            b"start_time_type",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "end_date_time",
            b"end_date_time",
            "end_time",
            b"end_time",
            "end_time_type",
            b"end_time_type",
            "id",
            b"id",
            "payments_account",
            b"payments_account",
            "payments_account_info",
            b"payments_account_info",
            "resource_name",
            b"resource_name",
            "start_date_time",
            b"start_date_time",
            "start_time",
            b"start_time",
            "start_time_type",
            b"start_time_type",
            "status",
            b"status",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["end_time", b"end_time"]
    ) -> typing_extensions___Literal["end_date_time", "end_time_type"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["start_time", b"start_time"]
    ) -> typing_extensions___Literal["start_date_time", "start_time_type"]: ...

global___BillingSetup = BillingSetup
