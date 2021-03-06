"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.common.criteria_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class CampaignBidModifier(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    CAMPAIGN_FIELD_NUMBER: builtins.int
    CRITERION_ID_FIELD_NUMBER: builtins.int
    BID_MODIFIER_FIELD_NUMBER: builtins.int
    INTERACTION_TYPE_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    campaign: typing.Text = ...
    criterion_id: builtins.int = ...
    bid_modifier: builtins.float = ...
    @property
    def interaction_type(
        self,
    ) -> google.ads.google_ads.v5.proto.common.criteria_pb2.InteractionTypeInfo: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        campaign: typing.Text = ...,
        criterion_id: builtins.int = ...,
        bid_modifier: builtins.float = ...,
        interaction_type: typing.Optional[
            google.ads.google_ads.v5.proto.common.criteria_pb2.InteractionTypeInfo
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "_bid_modifier",
            b"_bid_modifier",
            "_campaign",
            b"_campaign",
            "_criterion_id",
            b"_criterion_id",
            "bid_modifier",
            b"bid_modifier",
            "campaign",
            b"campaign",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "interaction_type",
            b"interaction_type",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "_bid_modifier",
            b"_bid_modifier",
            "_campaign",
            b"_campaign",
            "_criterion_id",
            b"_criterion_id",
            "bid_modifier",
            b"bid_modifier",
            "campaign",
            b"campaign",
            "criterion",
            b"criterion",
            "criterion_id",
            b"criterion_id",
            "interaction_type",
            b"interaction_type",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_bid_modifier", b"_bid_modifier"]
    ) -> typing_extensions.Literal["bid_modifier"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_campaign", b"_campaign"]
    ) -> typing_extensions.Literal["campaign"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["_criterion_id", b"_criterion_id"]
    ) -> typing_extensions.Literal["criterion_id"]: ...
    @typing.overload
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["criterion", b"criterion"]
    ) -> typing_extensions.Literal["interaction_type"]: ...

global___CampaignBidModifier = CampaignBidModifier
