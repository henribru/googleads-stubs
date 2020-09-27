from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    Optional,
    Sequence,
    Tuple,
    Union,
)

import grpc  # type: ignore
from google.api_core.client_options import ClientOptions  # type: ignore
from google.api_core.gapic_v1.client_info import ClientInfo  # type: ignore
from google.api_core.retry import Retry  # type: ignore
from google.auth.credentials import Credentials  # type: ignore
from google.longrunning import operations_pb2 as operations_pb2
from google.oauth2 import service_account as service_account  # type: ignore
from google.protobuf import empty_pb2 as empty_pb2, wrappers_pb2 as wrappers_pb2

from google.ads.google_ads.v2.proto.resources import (
    account_budget_pb2 as account_budget_pb2,
    account_budget_proposal_pb2 as account_budget_proposal_pb2,
    ad_group_ad_asset_view_pb2 as ad_group_ad_asset_view_pb2,
    ad_group_ad_label_pb2 as ad_group_ad_label_pb2,
    ad_group_ad_pb2 as ad_group_ad_pb2,
    ad_group_audience_view_pb2 as ad_group_audience_view_pb2,
    ad_group_bid_modifier_pb2 as ad_group_bid_modifier_pb2,
    ad_group_criterion_label_pb2 as ad_group_criterion_label_pb2,
    ad_group_criterion_pb2 as ad_group_criterion_pb2,
    ad_group_criterion_simulation_pb2 as ad_group_criterion_simulation_pb2,
    ad_group_extension_setting_pb2 as ad_group_extension_setting_pb2,
    ad_group_feed_pb2 as ad_group_feed_pb2,
    ad_group_label_pb2 as ad_group_label_pb2,
    ad_group_pb2 as ad_group_pb2,
    ad_group_simulation_pb2 as ad_group_simulation_pb2,
    ad_parameter_pb2 as ad_parameter_pb2,
    ad_pb2 as ad_pb2,
    ad_schedule_view_pb2 as ad_schedule_view_pb2,
    age_range_view_pb2 as age_range_view_pb2,
    asset_pb2 as asset_pb2,
    bidding_strategy_pb2 as bidding_strategy_pb2,
    billing_setup_pb2 as billing_setup_pb2,
    campaign_audience_view_pb2 as campaign_audience_view_pb2,
    campaign_bid_modifier_pb2 as campaign_bid_modifier_pb2,
    campaign_budget_pb2 as campaign_budget_pb2,
    campaign_criterion_pb2 as campaign_criterion_pb2,
    campaign_criterion_simulation_pb2 as campaign_criterion_simulation_pb2,
    campaign_draft_pb2 as campaign_draft_pb2,
    campaign_experiment_pb2 as campaign_experiment_pb2,
    campaign_extension_setting_pb2 as campaign_extension_setting_pb2,
    campaign_feed_pb2 as campaign_feed_pb2,
    campaign_label_pb2 as campaign_label_pb2,
    campaign_pb2 as campaign_pb2,
    campaign_shared_set_pb2 as campaign_shared_set_pb2,
    carrier_constant_pb2 as carrier_constant_pb2,
    change_status_pb2 as change_status_pb2,
    click_view_pb2 as click_view_pb2,
    conversion_action_pb2 as conversion_action_pb2,
    custom_interest_pb2 as custom_interest_pb2,
    customer_client_link_pb2 as customer_client_link_pb2,
    customer_client_pb2 as customer_client_pb2,
    customer_extension_setting_pb2 as customer_extension_setting_pb2,
    customer_feed_pb2 as customer_feed_pb2,
    customer_label_pb2 as customer_label_pb2,
    customer_manager_link_pb2 as customer_manager_link_pb2,
    customer_negative_criterion_pb2 as customer_negative_criterion_pb2,
    customer_pb2 as customer_pb2,
    detail_placement_view_pb2 as detail_placement_view_pb2,
    display_keyword_view_pb2 as display_keyword_view_pb2,
    distance_view_pb2 as distance_view_pb2,
    domain_category_pb2 as domain_category_pb2,
    dynamic_search_ads_search_term_view_pb2 as dynamic_search_ads_search_term_view_pb2,
    expanded_landing_page_view_pb2 as expanded_landing_page_view_pb2,
    extension_feed_item_pb2 as extension_feed_item_pb2,
    feed_item_pb2 as feed_item_pb2,
    feed_item_target_pb2 as feed_item_target_pb2,
)
from google.ads.google_ads.v2.proto.services import (
    account_budget_proposal_service_pb2 as account_budget_proposal_service_pb2,
    account_budget_proposal_service_pb2_grpc as account_budget_proposal_service_pb2_grpc,
    account_budget_service_pb2 as account_budget_service_pb2,
    account_budget_service_pb2_grpc as account_budget_service_pb2_grpc,
    ad_group_ad_asset_view_service_pb2 as ad_group_ad_asset_view_service_pb2,
    ad_group_ad_asset_view_service_pb2_grpc as ad_group_ad_asset_view_service_pb2_grpc,
    ad_group_ad_label_service_pb2 as ad_group_ad_label_service_pb2,
    ad_group_ad_label_service_pb2_grpc as ad_group_ad_label_service_pb2_grpc,
    ad_group_ad_service_pb2 as ad_group_ad_service_pb2,
    ad_group_ad_service_pb2_grpc as ad_group_ad_service_pb2_grpc,
    ad_group_audience_view_service_pb2 as ad_group_audience_view_service_pb2,
    ad_group_audience_view_service_pb2_grpc as ad_group_audience_view_service_pb2_grpc,
    ad_group_bid_modifier_service_pb2 as ad_group_bid_modifier_service_pb2,
    ad_group_bid_modifier_service_pb2_grpc as ad_group_bid_modifier_service_pb2_grpc,
    ad_group_criterion_label_service_pb2 as ad_group_criterion_label_service_pb2,
    ad_group_criterion_label_service_pb2_grpc as ad_group_criterion_label_service_pb2_grpc,
    ad_group_criterion_service_pb2 as ad_group_criterion_service_pb2,
    ad_group_criterion_service_pb2_grpc as ad_group_criterion_service_pb2_grpc,
    ad_group_criterion_simulation_service_pb2 as ad_group_criterion_simulation_service_pb2,
    ad_group_criterion_simulation_service_pb2_grpc as ad_group_criterion_simulation_service_pb2_grpc,
    ad_group_extension_setting_service_pb2 as ad_group_extension_setting_service_pb2,
    ad_group_extension_setting_service_pb2_grpc as ad_group_extension_setting_service_pb2_grpc,
    ad_group_feed_service_pb2 as ad_group_feed_service_pb2,
    ad_group_feed_service_pb2_grpc as ad_group_feed_service_pb2_grpc,
    ad_group_label_service_pb2 as ad_group_label_service_pb2,
    ad_group_label_service_pb2_grpc as ad_group_label_service_pb2_grpc,
    ad_group_service_pb2 as ad_group_service_pb2,
    ad_group_service_pb2_grpc as ad_group_service_pb2_grpc,
    ad_group_simulation_service_pb2 as ad_group_simulation_service_pb2,
    ad_group_simulation_service_pb2_grpc as ad_group_simulation_service_pb2_grpc,
    ad_parameter_service_pb2 as ad_parameter_service_pb2,
    ad_parameter_service_pb2_grpc as ad_parameter_service_pb2_grpc,
    ad_schedule_view_service_pb2 as ad_schedule_view_service_pb2,
    ad_schedule_view_service_pb2_grpc as ad_schedule_view_service_pb2_grpc,
    ad_service_pb2 as ad_service_pb2,
    ad_service_pb2_grpc as ad_service_pb2_grpc,
    age_range_view_service_pb2 as age_range_view_service_pb2,
    age_range_view_service_pb2_grpc as age_range_view_service_pb2_grpc,
    asset_service_pb2 as asset_service_pb2,
    asset_service_pb2_grpc as asset_service_pb2_grpc,
    bidding_strategy_service_pb2 as bidding_strategy_service_pb2,
    bidding_strategy_service_pb2_grpc as bidding_strategy_service_pb2_grpc,
    billing_setup_service_pb2 as billing_setup_service_pb2,
    billing_setup_service_pb2_grpc as billing_setup_service_pb2_grpc,
    campaign_audience_view_service_pb2 as campaign_audience_view_service_pb2,
    campaign_audience_view_service_pb2_grpc as campaign_audience_view_service_pb2_grpc,
    campaign_bid_modifier_service_pb2 as campaign_bid_modifier_service_pb2,
    campaign_bid_modifier_service_pb2_grpc as campaign_bid_modifier_service_pb2_grpc,
    campaign_budget_service_pb2 as campaign_budget_service_pb2,
    campaign_budget_service_pb2_grpc as campaign_budget_service_pb2_grpc,
    campaign_criterion_service_pb2 as campaign_criterion_service_pb2,
    campaign_criterion_service_pb2_grpc as campaign_criterion_service_pb2_grpc,
    campaign_criterion_simulation_service_pb2 as campaign_criterion_simulation_service_pb2,
    campaign_criterion_simulation_service_pb2_grpc as campaign_criterion_simulation_service_pb2_grpc,
    campaign_draft_service_pb2 as campaign_draft_service_pb2,
    campaign_draft_service_pb2_grpc as campaign_draft_service_pb2_grpc,
    campaign_experiment_service_pb2 as campaign_experiment_service_pb2,
    campaign_experiment_service_pb2_grpc as campaign_experiment_service_pb2_grpc,
    campaign_extension_setting_service_pb2 as campaign_extension_setting_service_pb2,
    campaign_extension_setting_service_pb2_grpc as campaign_extension_setting_service_pb2_grpc,
    campaign_feed_service_pb2 as campaign_feed_service_pb2,
    campaign_feed_service_pb2_grpc as campaign_feed_service_pb2_grpc,
    campaign_label_service_pb2 as campaign_label_service_pb2,
    campaign_label_service_pb2_grpc as campaign_label_service_pb2_grpc,
    campaign_service_pb2 as campaign_service_pb2,
    campaign_service_pb2_grpc as campaign_service_pb2_grpc,
    campaign_shared_set_service_pb2 as campaign_shared_set_service_pb2,
    campaign_shared_set_service_pb2_grpc as campaign_shared_set_service_pb2_grpc,
    carrier_constant_service_pb2 as carrier_constant_service_pb2,
    carrier_constant_service_pb2_grpc as carrier_constant_service_pb2_grpc,
    change_status_service_pb2 as change_status_service_pb2,
    change_status_service_pb2_grpc as change_status_service_pb2_grpc,
    click_view_service_pb2 as click_view_service_pb2,
    click_view_service_pb2_grpc as click_view_service_pb2_grpc,
    conversion_action_service_pb2 as conversion_action_service_pb2,
    conversion_action_service_pb2_grpc as conversion_action_service_pb2_grpc,
    conversion_adjustment_upload_service_pb2 as conversion_adjustment_upload_service_pb2,
    conversion_adjustment_upload_service_pb2_grpc as conversion_adjustment_upload_service_pb2_grpc,
    conversion_upload_service_pb2 as conversion_upload_service_pb2,
    conversion_upload_service_pb2_grpc as conversion_upload_service_pb2_grpc,
    custom_interest_service_pb2 as custom_interest_service_pb2,
    custom_interest_service_pb2_grpc as custom_interest_service_pb2_grpc,
    customer_client_link_service_pb2 as customer_client_link_service_pb2,
    customer_client_link_service_pb2_grpc as customer_client_link_service_pb2_grpc,
    customer_client_service_pb2 as customer_client_service_pb2,
    customer_client_service_pb2_grpc as customer_client_service_pb2_grpc,
    customer_extension_setting_service_pb2 as customer_extension_setting_service_pb2,
    customer_extension_setting_service_pb2_grpc as customer_extension_setting_service_pb2_grpc,
    customer_feed_service_pb2 as customer_feed_service_pb2,
    customer_feed_service_pb2_grpc as customer_feed_service_pb2_grpc,
    customer_label_service_pb2 as customer_label_service_pb2,
    customer_label_service_pb2_grpc as customer_label_service_pb2_grpc,
    customer_manager_link_service_pb2 as customer_manager_link_service_pb2,
    customer_manager_link_service_pb2_grpc as customer_manager_link_service_pb2_grpc,
    customer_negative_criterion_service_pb2 as customer_negative_criterion_service_pb2,
    customer_negative_criterion_service_pb2_grpc as customer_negative_criterion_service_pb2_grpc,
    customer_service_pb2 as customer_service_pb2,
    customer_service_pb2_grpc as customer_service_pb2_grpc,
    detail_placement_view_service_pb2 as detail_placement_view_service_pb2,
    detail_placement_view_service_pb2_grpc as detail_placement_view_service_pb2_grpc,
    display_keyword_view_service_pb2 as display_keyword_view_service_pb2,
    display_keyword_view_service_pb2_grpc as display_keyword_view_service_pb2_grpc,
    distance_view_service_pb2 as distance_view_service_pb2,
    distance_view_service_pb2_grpc as distance_view_service_pb2_grpc,
    domain_category_service_pb2 as domain_category_service_pb2,
    domain_category_service_pb2_grpc as domain_category_service_pb2_grpc,
    dynamic_search_ads_search_term_view_service_pb2 as dynamic_search_ads_search_term_view_service_pb2,
    dynamic_search_ads_search_term_view_service_pb2_grpc as dynamic_search_ads_search_term_view_service_pb2_grpc,
    expanded_landing_page_view_service_pb2 as expanded_landing_page_view_service_pb2,
    expanded_landing_page_view_service_pb2_grpc as expanded_landing_page_view_service_pb2_grpc,
    extension_feed_item_service_pb2 as extension_feed_item_service_pb2,
    extension_feed_item_service_pb2_grpc as extension_feed_item_service_pb2_grpc,
    feed_item_service_pb2 as feed_item_service_pb2,
    feed_item_service_pb2_grpc as feed_item_service_pb2_grpc,
    feed_item_target_service_pb2 as feed_item_target_service_pb2,
    feed_item_target_service_pb2_grpc as feed_item_target_service_pb2_grpc,
)
from google.ads.google_ads.v2.services import (
    enums as enums,
    feed_item_target_service_client_config as feed_item_target_service_client_config,
)
from google.ads.google_ads.v2.services.transports import (
    feed_item_target_service_grpc_transport as feed_item_target_service_grpc_transport,
)
from google.ads.google_ads.v2.types import FeedItemTarget

class FeedItemTargetServiceClient:
    SERVICE_ADDRESS: ClassVar[str] = ...
    @classmethod
    def from_service_account_file(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemTargetServiceClient: ...
    @classmethod
    def from_service_account_json(
        cls, filename: str, *args: Any, **kwargs: Any
    ) -> FeedItemTargetServiceClient: ...
    @classmethod
    def feed_item_target_path(cls, customer: Any, feed_item_target: Any) -> str: ...
    transport: Union[
        feed_item_target_service_grpc_transport.FeedItemTargetServiceGrpcTransport,
        Callable[
            [Credentials, type],
            feed_item_target_service_grpc_transport.FeedItemTargetServiceGrpcTransport,
        ],
    ] = ...
    def __init__(
        self,
        transport: Optional[
            Union[
                feed_item_target_service_grpc_transport.FeedItemTargetServiceGrpcTransport,
                Callable[
                    [Credentials, type],
                    feed_item_target_service_grpc_transport.FeedItemTargetServiceGrpcTransport,
                ],
            ]
        ] = ...,
        channel: Optional[grpc.Channel] = ...,
        credentials: Optional[Credentials] = ...,
        client_config: Optional[Dict[str, Any]] = ...,
        client_info: Optional[ClientInfo] = ...,
    ) -> None: ...
    def get_feed_item_target(
        self,
        resource_name: str,
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> FeedItemTarget: ...
    def mutate_feed_item_targets(
        self,
        customer_id: str,
        operations: List[
            Union[Dict[str, Any], feed_item_target_service_pb2.FeedItemTargetOperation]
        ],
        retry: Optional[Retry] = ...,
        timeout: Optional[float] = ...,
        metadata: Optional[Sequence[Tuple[str, str]]] = ...,
    ) -> feed_item_target_service_pb2.MutateFeedItemTargetsResponse: ...
