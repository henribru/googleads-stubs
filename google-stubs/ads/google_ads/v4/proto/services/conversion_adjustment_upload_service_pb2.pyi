"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v4.proto.enums.conversion_adjustment_type_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.wrappers_pb2
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class UploadConversionAdjustmentsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    CONVERSION_ADJUSTMENTS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    partial_failure: builtins.bool = ...
    validate_only: builtins.bool = ...
    @property
    def conversion_adjustments(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ConversionAdjustment
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        conversion_adjustments: typing.Optional[
            typing.Iterable[global___ConversionAdjustment]
        ] = ...,
        partial_failure: builtins.bool = ...,
        validate_only: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "conversion_adjustments",
            b"conversion_adjustments",
            "customer_id",
            b"customer_id",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

global___UploadConversionAdjustmentsRequest = UploadConversionAdjustmentsRequest

class UploadConversionAdjustmentsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def partial_failure_error(self) -> google.rpc.status_pb2.Status: ...
    @property
    def results(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ConversionAdjustmentResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing.Optional[google.rpc.status_pb2.Status] = ...,
        results: typing.Optional[
            typing.Iterable[global___ConversionAdjustmentResult]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "partial_failure_error", b"partial_failure_error", "results", b"results"
        ],
    ) -> None: ...

global___UploadConversionAdjustmentsResponse = UploadConversionAdjustmentsResponse

class ConversionAdjustment(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONVERSION_ACTION_FIELD_NUMBER: builtins.int
    ADJUSTMENT_DATE_TIME_FIELD_NUMBER: builtins.int
    ADJUSTMENT_TYPE_FIELD_NUMBER: builtins.int
    RESTATEMENT_VALUE_FIELD_NUMBER: builtins.int
    GCLID_DATE_TIME_PAIR_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    adjustment_type: google.ads.google_ads.v4.proto.enums.conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType.V = (
        ...
    )
    @property
    def conversion_action(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def adjustment_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def restatement_value(self) -> global___RestatementValue: ...
    @property
    def gclid_date_time_pair(self) -> global___GclidDateTimePair: ...
    @property
    def order_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        conversion_action: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        adjustment_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        adjustment_type: google.ads.google_ads.v4.proto.enums.conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType.V = ...,
        restatement_value: typing.Optional[global___RestatementValue] = ...,
        gclid_date_time_pair: typing.Optional[global___GclidDateTimePair] = ...,
        order_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
            "restatement_value",
            b"restatement_value",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "adjustment_type",
            b"adjustment_type",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
            "restatement_value",
            b"restatement_value",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "conversion_identifier", b"conversion_identifier"
        ],
    ) -> typing_extensions.Literal["gclid_date_time_pair", "order_id"]: ...

global___ConversionAdjustment = ConversionAdjustment

class RestatementValue(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ADJUSTED_VALUE_FIELD_NUMBER: builtins.int
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    @property
    def adjusted_value(self) -> google.protobuf.wrappers_pb2.DoubleValue: ...
    @property
    def currency_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        adjusted_value: typing.Optional[google.protobuf.wrappers_pb2.DoubleValue] = ...,
        currency_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "adjusted_value", b"adjusted_value", "currency_code", b"currency_code"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "adjusted_value", b"adjusted_value", "currency_code", b"currency_code"
        ],
    ) -> None: ...

global___RestatementValue = RestatementValue

class GclidDateTimePair(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    GCLID_FIELD_NUMBER: builtins.int
    CONVERSION_DATE_TIME_FIELD_NUMBER: builtins.int
    @property
    def gclid(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def conversion_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        gclid: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        conversion_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "conversion_date_time", b"conversion_date_time", "gclid", b"gclid"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "conversion_date_time", b"conversion_date_time", "gclid", b"gclid"
        ],
    ) -> None: ...

global___GclidDateTimePair = GclidDateTimePair

class ConversionAdjustmentResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CONVERSION_ACTION_FIELD_NUMBER: builtins.int
    ADJUSTMENT_DATE_TIME_FIELD_NUMBER: builtins.int
    ADJUSTMENT_TYPE_FIELD_NUMBER: builtins.int
    GCLID_DATE_TIME_PAIR_FIELD_NUMBER: builtins.int
    ORDER_ID_FIELD_NUMBER: builtins.int
    adjustment_type: google.ads.google_ads.v4.proto.enums.conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType.V = (
        ...
    )
    @property
    def conversion_action(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def adjustment_date_time(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def gclid_date_time_pair(self) -> global___GclidDateTimePair: ...
    @property
    def order_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        conversion_action: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        adjustment_date_time: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        adjustment_type: google.ads.google_ads.v4.proto.enums.conversion_adjustment_type_pb2.ConversionAdjustmentTypeEnum.ConversionAdjustmentType.V = ...,
        gclid_date_time_pair: typing.Optional[global___GclidDateTimePair] = ...,
        order_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "adjustment_type",
            b"adjustment_type",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal[
            "conversion_identifier", b"conversion_identifier"
        ],
    ) -> typing_extensions.Literal["gclid_date_time_pair", "order_id"]: ...

global___ConversionAdjustmentResult = ConversionAdjustmentResult
