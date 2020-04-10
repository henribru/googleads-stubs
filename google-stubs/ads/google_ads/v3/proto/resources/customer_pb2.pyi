# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v3.proto.enums.customer_pay_per_conversion_eligibility_failure_reason_pb2 import (
    CustomerPayPerConversionEligibilityFailureReasonEnum as google___ads___googleads___v3___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from google.protobuf.wrappers_pb2 import (
    BoolValue as google___protobuf___wrappers_pb2___BoolValue,
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

class Customer(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ...  # type: typing___Text
    pay_per_conversion_eligibility_failure_reasons = (
        ...
    )  # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[google___ads___googleads___v3___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason]
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def descriptive_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def time_zone(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def tracking_url_template(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def final_url_suffix(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def auto_tagging_enabled(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def has_partners_badge(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def manager(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def test_account(self) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def call_reporting_setting(self) -> global___CallReportingSetting: ...
    @property
    def conversion_tracking_setting(self) -> global___ConversionTrackingSetting: ...
    @property
    def remarketing_setting(self) -> global___RemarketingSetting: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        descriptive_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        currency_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        time_zone: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        tracking_url_template: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        final_url_suffix: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        auto_tagging_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        has_partners_badge: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        manager: typing___Optional[google___protobuf___wrappers_pb2___BoolValue] = None,
        test_account: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        call_reporting_setting: typing___Optional[global___CallReportingSetting] = None,
        conversion_tracking_setting: typing___Optional[
            global___ConversionTrackingSetting
        ] = None,
        remarketing_setting: typing___Optional[global___RemarketingSetting] = None,
        pay_per_conversion_eligibility_failure_reasons: typing___Optional[
            typing___Iterable[
                google___ads___googleads___v3___enums___customer_pay_per_conversion_eligibility_failure_reason_pb2___CustomerPayPerConversionEligibilityFailureReasonEnum.CustomerPayPerConversionEligibilityFailureReason
            ]
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Customer: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> Customer: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
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

global___Customer = Customer

class CallReportingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def call_reporting_enabled(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def call_conversion_reporting_enabled(
        self,
    ) -> google___protobuf___wrappers_pb2___BoolValue: ...
    @property
    def call_conversion_action(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        call_reporting_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        call_conversion_reporting_enabled: typing___Optional[
            google___protobuf___wrappers_pb2___BoolValue
        ] = None,
        call_conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CallReportingSetting: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> CallReportingSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
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
            "call_conversion_action",
            b"call_conversion_action",
            "call_conversion_reporting_enabled",
            b"call_conversion_reporting_enabled",
            "call_reporting_enabled",
            b"call_reporting_enabled",
        ],
    ) -> None: ...

global___CallReportingSetting = CallReportingSetting

class ConversionTrackingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def conversion_tracking_id(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def cross_account_conversion_tracking_id(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        conversion_tracking_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        cross_account_conversion_tracking_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ConversionTrackingSetting: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ConversionTrackingSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_tracking_id",
            b"conversion_tracking_id",
            "cross_account_conversion_tracking_id",
            b"cross_account_conversion_tracking_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_tracking_id",
            b"conversion_tracking_id",
            "cross_account_conversion_tracking_id",
            b"cross_account_conversion_tracking_id",
        ],
    ) -> None: ...

global___ConversionTrackingSetting = ConversionTrackingSetting

class RemarketingSetting(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def google_global_site_tag(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        google_global_site_tag: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RemarketingSetting: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> RemarketingSetting: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "google_global_site_tag", b"google_global_site_tag"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "google_global_site_tag", b"google_global_site_tag"
        ],
    ) -> None: ...

global___RemarketingSetting = RemarketingSetting