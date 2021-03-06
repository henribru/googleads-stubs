"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.common.dates_pb2
import google.ads.google_ads.v6.proto.enums.keyword_plan_forecast_interval_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class KeywordPlan(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    FORECAST_PERIOD_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    id: builtins.int = ...
    name: typing.Text = ...
    @property
    def forecast_period(self) -> global___KeywordPlanForecastPeriod: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        id: builtins.int = ...,
        name: typing.Text = ...,
        forecast_period: typing.Optional[global___KeywordPlanForecastPeriod] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_id",
            b"_id",
            "_name",
            b"_name",
            "forecast_period",
            b"forecast_period",
            "id",
            b"id",
            "name",
            b"name",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_id",
            b"_id",
            "_name",
            b"_name",
            "forecast_period",
            b"forecast_period",
            "id",
            b"id",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_id", b"_id"]
    ) -> typing_extensions.Literal["id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_name", b"_name"]
    ) -> typing_extensions.Literal["name"]: ...

global___KeywordPlan = KeywordPlan

class KeywordPlanForecastPeriod(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DATE_INTERVAL_FIELD_NUMBER: builtins.int
    DATE_RANGE_FIELD_NUMBER: builtins.int
    date_interval: google.ads.google_ads.v6.proto.enums.keyword_plan_forecast_interval_pb2.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval.V = (
        ...
    )
    @property
    def date_range(
        self,
    ) -> google.ads.google_ads.v6.proto.common.dates_pb2.DateRange: ...
    def __init__(
        self,
        *,
        date_interval: google.ads.google_ads.v6.proto.enums.keyword_plan_forecast_interval_pb2.KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval.V = ...,
        date_range: typing.Optional[
            google.ads.google_ads.v6.proto.common.dates_pb2.DateRange
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "date_interval",
            b"date_interval",
            "date_range",
            b"date_range",
            "interval",
            b"interval",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "date_interval",
            b"date_interval",
            "date_range",
            b"date_range",
            "interval",
            b"interval",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["interval", b"interval"]
    ) -> typing_extensions.Literal["date_interval", "date_range"]: ...

global___KeywordPlanForecastPeriod = KeywordPlanForecastPeriod
