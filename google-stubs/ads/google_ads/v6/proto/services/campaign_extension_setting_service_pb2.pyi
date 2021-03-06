"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.resources.campaign_extension_setting_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCampaignExtensionSettingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___GetCampaignExtensionSettingRequest = GetCampaignExtensionSettingRequest

class MutateCampaignExtensionSettingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    partial_failure: builtins.bool = ...
    validate_only: builtins.bool = ...
    @property
    def operations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___CampaignExtensionSettingOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        operations: typing.Optional[
            typing.Iterable[global___CampaignExtensionSettingOperation]
        ] = ...,
        partial_failure: builtins.bool = ...,
        validate_only: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

global___MutateCampaignExtensionSettingsRequest = MutateCampaignExtensionSettingsRequest

class CampaignExtensionSettingOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    CREATE_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    remove: typing.Text = ...
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def create(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting: ...
    @property
    def update(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting: ...
    def __init__(
        self,
        *,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        create: typing.Optional[
            google.ads.google_ads.v6.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting
        ] = ...,
        update: typing.Optional[
            google.ads.google_ads.v6.proto.resources.campaign_extension_setting_pb2.CampaignExtensionSetting
        ] = ...,
        remove: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["operation", b"operation"]
    ) -> typing_extensions.Literal["create", "update", "remove"]: ...

global___CampaignExtensionSettingOperation = CampaignExtensionSettingOperation

class MutateCampaignExtensionSettingsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def partial_failure_error(self) -> google.rpc.status_pb2.Status: ...
    @property
    def results(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MutateCampaignExtensionSettingResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing.Optional[google.rpc.status_pb2.Status] = ...,
        results: typing.Optional[
            typing.Iterable[global___MutateCampaignExtensionSettingResult]
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

global___MutateCampaignExtensionSettingsResponse = (
    MutateCampaignExtensionSettingsResponse
)

class MutateCampaignExtensionSettingResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___MutateCampaignExtensionSettingResult = MutateCampaignExtensionSettingResult
