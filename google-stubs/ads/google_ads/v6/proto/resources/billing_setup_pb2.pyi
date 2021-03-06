"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.enums.billing_setup_status_pb2
import google.ads.google_ads.v6.proto.enums.time_type_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BillingSetup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class PaymentsAccountInfo(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: builtins.int
        PAYMENTS_ACCOUNT_NAME_FIELD_NUMBER: builtins.int
        PAYMENTS_PROFILE_ID_FIELD_NUMBER: builtins.int
        PAYMENTS_PROFILE_NAME_FIELD_NUMBER: builtins.int
        SECONDARY_PAYMENTS_PROFILE_ID_FIELD_NUMBER: builtins.int
        payments_account_id: typing.Text = ...
        payments_account_name: typing.Text = ...
        payments_profile_id: typing.Text = ...
        payments_profile_name: typing.Text = ...
        secondary_payments_profile_id: typing.Text = ...
        def __init__(
            self,
            *,
            payments_account_id: typing.Text = ...,
            payments_account_name: typing.Text = ...,
            payments_profile_id: typing.Text = ...,
            payments_profile_name: typing.Text = ...,
            secondary_payments_profile_id: typing.Text = ...,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions.Literal[
                "_payments_account_id",
                b"_payments_account_id",
                "_payments_account_name",
                b"_payments_account_name",
                "_payments_profile_id",
                b"_payments_profile_id",
                "_payments_profile_name",
                b"_payments_profile_name",
                "_secondary_payments_profile_id",
                b"_secondary_payments_profile_id",
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
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "_payments_account_id",
                b"_payments_account_id",
                "_payments_account_name",
                b"_payments_account_name",
                "_payments_profile_id",
                b"_payments_profile_id",
                "_payments_profile_name",
                b"_payments_profile_name",
                "_secondary_payments_profile_id",
                b"_secondary_payments_profile_id",
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
        @typing.overload
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_payments_account_id", b"_payments_account_id"
            ],
        ) -> typing_extensions.Literal["payments_account_id"]: ...
        @typing.overload
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_payments_account_name", b"_payments_account_name"
            ],
        ) -> typing_extensions.Literal["payments_account_name"]: ...
        @typing.overload
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_payments_profile_id", b"_payments_profile_id"
            ],
        ) -> typing_extensions.Literal["payments_profile_id"]: ...
        @typing.overload
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_payments_profile_name", b"_payments_profile_name"
            ],
        ) -> typing_extensions.Literal["payments_profile_name"]: ...
        @typing.overload
        def WhichOneof(
            self,
            oneof_group: typing_extensions.Literal[
                "_secondary_payments_profile_id", b"_secondary_payments_profile_id"
            ],
        ) -> typing_extensions.Literal["secondary_payments_profile_id"]: ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    PAYMENTS_ACCOUNT_FIELD_NUMBER: builtins.int
    PAYMENTS_ACCOUNT_INFO_FIELD_NUMBER: builtins.int
    START_DATE_TIME_FIELD_NUMBER: builtins.int
    START_TIME_TYPE_FIELD_NUMBER: builtins.int
    END_DATE_TIME_FIELD_NUMBER: builtins.int
    END_TIME_TYPE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    id: builtins.int = ...
    status: google.ads.google_ads.v6.proto.enums.billing_setup_status_pb2.BillingSetupStatusEnum.BillingSetupStatus.V = (
        ...
    )
    payments_account: typing.Text = ...
    start_date_time: typing.Text = ...
    start_time_type: google.ads.google_ads.v6.proto.enums.time_type_pb2.TimeTypeEnum.TimeType.V = (
        ...
    )
    end_date_time: typing.Text = ...
    end_time_type: google.ads.google_ads.v6.proto.enums.time_type_pb2.TimeTypeEnum.TimeType.V = (
        ...
    )
    @property
    def payments_account_info(self) -> global___BillingSetup.PaymentsAccountInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: builtins.int = ...,
        status: google.ads.google_ads.v6.proto.enums.billing_setup_status_pb2.BillingSetupStatusEnum.BillingSetupStatus.V = ...,
        payments_account: typing.Text = ...,
        payments_account_info: typing.Optional[
            global___BillingSetup.PaymentsAccountInfo
        ] = ...,
        start_date_time: typing.Text = ...,
        start_time_type: google.ads.google_ads.v6.proto.enums.time_type_pb2.TimeTypeEnum.TimeType.V = ...,
        end_date_time: typing.Text = ...,
        end_time_type: google.ads.google_ads.v6.proto.enums.time_type_pb2.TimeTypeEnum.TimeType.V = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_id",
            b"_id",
            "_payments_account",
            b"_payments_account",
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
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_id",
            b"_id",
            "_payments_account",
            b"_payments_account",
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
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_id", b"_id"]
    ) -> typing_extensions.Literal["id"]: ...
    @typing.overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "_payments_account", b"_payments_account"
        ],
    ) -> typing_extensions.Literal["payments_account"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["end_time", b"end_time"]
    ) -> typing_extensions.Literal["end_date_time", "end_time_type"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["start_time", b"start_time"]
    ) -> typing_extensions.Literal["start_date_time", "start_time_type"]: ...

global___BillingSetup = BillingSetup
