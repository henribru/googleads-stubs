# @generated by mypy-protobuf.  Do not edit manually!
import sys
from google.ads.google_ads.v5.proto.enums.customer_pay_per_conversion_eligibility_failure_reason_pb2 import (
    CustomerPayPerConversionEligibilityFailureReasonEnum as google___ads___googleads___v5___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from typing_extensions import Literal as typing_extensions___Literal

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class Customer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    descriptive_name: typing___Text = ...
    currency_code: typing___Text = ...
    time_zone: typing___Text = ...
    tracking_url_template: typing___Text = ...
    final_url_suffix: typing___Text = ...
    auto_tagging_enabled: builtin___bool = ...
    has_partners_badge: builtin___bool = ...
    manager: builtin___bool = ...
    test_account: builtin___bool = ...
    pay_per_conversion_eligibility_failure_reasons: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        google___ads___googleads___v5___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue
    ] = ...
    optimization_score: builtin___float = ...
    @property
    def call_reporting_setting(self) -> type___CallReportingSetting: ...
    @property
    def conversion_tracking_setting(self) -> type___ConversionTrackingSetting: ...
    @property
    def remarketing_setting(self) -> type___RemarketingSetting: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        descriptive_name: typing___Optional[typing___Text] = None,
        currency_code: typing___Optional[typing___Text] = None,
        time_zone: typing___Optional[typing___Text] = None,
        tracking_url_template: typing___Optional[typing___Text] = None,
        final_url_suffix: typing___Optional[typing___Text] = None,
        auto_tagging_enabled: typing___Optional[builtin___bool] = None,
        has_partners_badge: typing___Optional[builtin___bool] = None,
        manager: typing___Optional[builtin___bool] = None,
        test_account: typing___Optional[builtin___bool] = None,
        call_reporting_setting: typing___Optional[type___CallReportingSetting] = None,
        conversion_tracking_setting: typing___Optional[
            type___ConversionTrackingSetting
        ] = None,
        remarketing_setting: typing___Optional[type___RemarketingSetting] = None,
        pay_per_conversion_eligibility_failure_reasons: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v5___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReasonValue
            ]
        ] = None,
        optimization_score: typing___Optional[builtin___float] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_auto_tagging_enabled",
            b"_auto_tagging_enabled",
            "_currency_code",
            b"_currency_code",
            "_descriptive_name",
            b"_descriptive_name",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_has_partners_badge",
            b"_has_partners_badge",
            "_id",
            b"_id",
            "_manager",
            b"_manager",
            "_optimization_score",
            b"_optimization_score",
            "_test_account",
            b"_test_account",
            "_time_zone",
            b"_time_zone",
            "_tracking_url_template",
            b"_tracking_url_template",
            "auto_tagging_enabled",
            b"auto_tagging_enabled",
            "call_reporting_setting",
            b"call_reporting_setting",
            "conversion_tracking_setting",
            b"conversion_tracking_setting",
            "currency_code",
            b"currency_code",
            "descriptive_name",
            b"descriptive_name",
            "final_url_suffix",
            b"final_url_suffix",
            "has_partners_badge",
            b"has_partners_badge",
            "id",
            b"id",
            "manager",
            b"manager",
            "optimization_score",
            b"optimization_score",
            "remarketing_setting",
            b"remarketing_setting",
            "test_account",
            b"test_account",
            "time_zone",
            b"time_zone",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_auto_tagging_enabled",
            b"_auto_tagging_enabled",
            "_currency_code",
            b"_currency_code",
            "_descriptive_name",
            b"_descriptive_name",
            "_final_url_suffix",
            b"_final_url_suffix",
            "_has_partners_badge",
            b"_has_partners_badge",
            "_id",
            b"_id",
            "_manager",
            b"_manager",
            "_optimization_score",
            b"_optimization_score",
            "_test_account",
            b"_test_account",
            "_time_zone",
            b"_time_zone",
            "_tracking_url_template",
            b"_tracking_url_template",
            "auto_tagging_enabled",
            b"auto_tagging_enabled",
            "call_reporting_setting",
            b"call_reporting_setting",
            "conversion_tracking_setting",
            b"conversion_tracking_setting",
            "currency_code",
            b"currency_code",
            "descriptive_name",
            b"descriptive_name",
            "final_url_suffix",
            b"final_url_suffix",
            "has_partners_badge",
            b"has_partners_badge",
            "id",
            b"id",
            "manager",
            b"manager",
            "optimization_score",
            b"optimization_score",
            "pay_per_conversion_eligibility_failure_reasons",
            b"pay_per_conversion_eligibility_failure_reasons",
            "remarketing_setting",
            b"remarketing_setting",
            "resource_name",
            b"resource_name",
            "test_account",
            b"test_account",
            "time_zone",
            b"time_zone",
            "tracking_url_template",
            b"tracking_url_template",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_auto_tagging_enabled", b"_auto_tagging_enabled"
        ],
    ) -> typing_extensions___Literal["auto_tagging_enabled"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_currency_code", b"_currency_code"],
    ) -> typing_extensions___Literal["currency_code"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_descriptive_name", b"_descriptive_name"
        ],
    ) -> typing_extensions___Literal["descriptive_name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_final_url_suffix", b"_final_url_suffix"
        ],
    ) -> typing_extensions___Literal["final_url_suffix"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_has_partners_badge", b"_has_partners_badge"
        ],
    ) -> typing_extensions___Literal["has_partners_badge"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_manager", b"_manager"]
    ) -> typing_extensions___Literal["manager"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_optimization_score", b"_optimization_score"
        ],
    ) -> typing_extensions___Literal["optimization_score"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_test_account", b"_test_account"],
    ) -> typing_extensions___Literal["test_account"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_time_zone", b"_time_zone"]
    ) -> typing_extensions___Literal["time_zone"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_tracking_url_template", b"_tracking_url_template"
        ],
    ) -> typing_extensions___Literal["tracking_url_template"]: ...

type___Customer = Customer

class CallReportingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    call_reporting_enabled: builtin___bool = ...
    call_conversion_reporting_enabled: builtin___bool = ...
    call_conversion_action: typing___Text = ...
    def __init__(
        self,
        *,
        call_reporting_enabled: typing___Optional[builtin___bool] = None,
        call_conversion_reporting_enabled: typing___Optional[builtin___bool] = None,
        call_conversion_action: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_call_conversion_action",
            b"_call_conversion_action",
            "_call_conversion_reporting_enabled",
            b"_call_conversion_reporting_enabled",
            "_call_reporting_enabled",
            b"_call_reporting_enabled",
            "call_conversion_action",
            b"call_conversion_action",
            "call_conversion_reporting_enabled",
            b"call_conversion_reporting_enabled",
            "call_reporting_enabled",
            b"call_reporting_enabled",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_call_conversion_action",
            b"_call_conversion_action",
            "_call_conversion_reporting_enabled",
            b"_call_conversion_reporting_enabled",
            "_call_reporting_enabled",
            b"_call_reporting_enabled",
            "call_conversion_action",
            b"call_conversion_action",
            "call_conversion_reporting_enabled",
            b"call_conversion_reporting_enabled",
            "call_reporting_enabled",
            b"call_reporting_enabled",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_call_conversion_action", b"_call_conversion_action"
        ],
    ) -> typing_extensions___Literal["call_conversion_action"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_call_conversion_reporting_enabled", b"_call_conversion_reporting_enabled"
        ],
    ) -> typing_extensions___Literal["call_conversion_reporting_enabled"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_call_reporting_enabled", b"_call_reporting_enabled"
        ],
    ) -> typing_extensions___Literal["call_reporting_enabled"]: ...

type___CallReportingSetting = CallReportingSetting

class ConversionTrackingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    conversion_tracking_id: builtin___int = ...
    cross_account_conversion_tracking_id: builtin___int = ...
    def __init__(
        self,
        *,
        conversion_tracking_id: typing___Optional[builtin___int] = None,
        cross_account_conversion_tracking_id: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_conversion_tracking_id",
            b"_conversion_tracking_id",
            "_cross_account_conversion_tracking_id",
            b"_cross_account_conversion_tracking_id",
            "conversion_tracking_id",
            b"conversion_tracking_id",
            "cross_account_conversion_tracking_id",
            b"cross_account_conversion_tracking_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_conversion_tracking_id",
            b"_conversion_tracking_id",
            "_cross_account_conversion_tracking_id",
            b"_cross_account_conversion_tracking_id",
            "conversion_tracking_id",
            b"conversion_tracking_id",
            "cross_account_conversion_tracking_id",
            b"cross_account_conversion_tracking_id",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_tracking_id", b"_conversion_tracking_id"
        ],
    ) -> typing_extensions___Literal["conversion_tracking_id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_cross_account_conversion_tracking_id",
            b"_cross_account_conversion_tracking_id",
        ],
    ) -> typing_extensions___Literal["cross_account_conversion_tracking_id"]: ...

type___ConversionTrackingSetting = ConversionTrackingSetting

class RemarketingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    google_global_site_tag: typing___Text = ...
    def __init__(
        self, *, google_global_site_tag: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_google_global_site_tag",
            b"_google_global_site_tag",
            "google_global_site_tag",
            b"google_global_site_tag",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_google_global_site_tag",
            b"_google_global_site_tag",
            "google_global_site_tag",
            b"google_global_site_tag",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_google_global_site_tag", b"_google_global_site_tag"
        ],
    ) -> typing_extensions___Literal["google_global_site_tag"]: ...

type___RemarketingSetting = RemarketingSetting
