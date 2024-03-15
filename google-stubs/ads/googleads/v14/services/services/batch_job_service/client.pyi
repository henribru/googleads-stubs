import types
from typing import Dict, MutableSequence, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    operation,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v14.services.services.batch_job_service import pagers
from google.ads.googleads.v14.services.types import (
    batch_job_service,
    google_ads_service,
)

from .transports.base import BatchJobServiceTransport

class BatchJobServiceClientMeta(type):
    def get_transport_class(
        cls, label: str | None = None
    ) -> type[BatchJobServiceTransport]: ...

class BatchJobServiceClient(metaclass=BatchJobServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json = from_service_account_file
    @property
    def transport(self) -> BatchJobServiceTransport: ...
    def __enter__(self) -> BatchJobServiceClient: ...
    def __exit__(
        self,
        type: type[BaseException] | None,
        value: BaseException | None,
        traceback: types.TracebackType | None,
    ) -> None: ...
    @staticmethod
    def accessible_bidding_strategy_path(
        customer_id: str, bidding_strategy_id: str
    ) -> str: ...
    @staticmethod
    def parse_accessible_bidding_strategy_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_path(customer_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_ad_path(customer_id: str, ad_group_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_ad_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_ad_label_path(
        customer_id: str, ad_group_id: str, ad_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_asset_path(
        customer_id: str, ad_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_bid_modifier_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_bid_modifier_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_customizer_path(
        customer_id: str,
        ad_group_id: str,
        criterion_id: str,
        customizer_attribute_id: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_customizer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_label_path(
        customer_id: str, ad_group_id: str, criterion_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_customizer_path(
        customer_id: str, ad_group_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_customizer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_extension_setting_path(
        customer_id: str, ad_group_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_extension_setting_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_feed_path(customer_id: str, ad_group_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_feed_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_group_label_path(
        customer_id: str, ad_group_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def ad_parameter_path(
        customer_id: str, ad_group_id: str, criterion_id: str, parameter_index: str
    ) -> str: ...
    @staticmethod
    def parse_ad_parameter_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_group_path(customer_id: str, asset_group_id: str) -> str: ...
    @staticmethod
    def parse_asset_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_group_asset_path(
        customer_id: str, asset_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_group_listing_group_filter_path(
        customer_id: str, asset_group_id: str, listing_group_filter_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_listing_group_filter_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_group_signal_path(
        customer_id: str, asset_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_signal_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_set_path(customer_id: str, asset_set_id: str) -> str: ...
    @staticmethod
    def parse_asset_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def asset_set_asset_path(
        customer_id: str, asset_set_id: str, asset_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_set_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def audience_path(customer_id: str, audience_id: str) -> str: ...
    @staticmethod
    def parse_audience_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def batch_job_path(customer_id: str, batch_job_id: str) -> str: ...
    @staticmethod
    def parse_batch_job_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def bidding_data_exclusion_path(
        customer_id: str, seasonality_event_id: str
    ) -> str: ...
    @staticmethod
    def parse_bidding_data_exclusion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def bidding_seasonality_adjustment_path(
        customer_id: str, seasonality_event_id: str
    ) -> str: ...
    @staticmethod
    def parse_bidding_seasonality_adjustment_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def bidding_strategy_path(customer_id: str, bidding_strategy_id: str) -> str: ...
    @staticmethod
    def parse_bidding_strategy_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_asset_path(
        customer_id: str, campaign_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_asset_set_path(
        customer_id: str, campaign_id: str, asset_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_asset_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_bid_modifier_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_bid_modifier_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_conversion_goal_path(
        customer_id: str, campaign_id: str, category: str, source: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_conversion_goal_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_criterion_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_customizer_path(
        customer_id: str, campaign_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_customizer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_draft_path(
        customer_id: str, base_campaign_id: str, draft_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_draft_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_extension_setting_path(
        customer_id: str, campaign_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_extension_setting_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_feed_path(customer_id: str, campaign_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_campaign_feed_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_group_path(customer_id: str, campaign_group_id: str) -> str: ...
    @staticmethod
    def parse_campaign_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_label_path(
        customer_id: str, campaign_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def campaign_shared_set_path(
        customer_id: str, campaign_id: str, shared_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_shared_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def combined_audience_path(customer_id: str, combined_audience_id: str) -> str: ...
    @staticmethod
    def parse_combined_audience_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_custom_variable_path(
        customer_id: str, conversion_custom_variable_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_custom_variable_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_goal_campaign_config_path(
        customer_id: str, campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_goal_campaign_config_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_path(
        customer_id: str, conversion_value_rule_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_set_path(
        customer_id: str, conversion_value_rule_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def custom_conversion_goal_path(customer_id: str, goal_id: str) -> str: ...
    @staticmethod
    def parse_custom_conversion_goal_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_asset_path(
        customer_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_asset_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_conversion_goal_path(
        customer_id: str, category: str, source: str
    ) -> str: ...
    @staticmethod
    def parse_customer_conversion_goal_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_customizer_path(
        customer_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_customizer_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_extension_setting_path(
        customer_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_extension_setting_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_customer_feed_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_label_path(customer_id: str, label_id: str) -> str: ...
    @staticmethod
    def parse_customer_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customer_negative_criterion_path(
        customer_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_negative_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def customizer_attribute_path(
        customer_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_customizer_attribute_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def experiment_path(customer_id: str, trial_id: str) -> str: ...
    @staticmethod
    def parse_experiment_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def experiment_arm_path(
        customer_id: str, trial_id: str, trial_arm_id: str
    ) -> str: ...
    @staticmethod
    def parse_experiment_arm_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def extension_feed_item_path(customer_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_extension_feed_item_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_feed_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_item_path(customer_id: str, feed_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_feed_item_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_item_set_path(
        customer_id: str, feed_id: str, feed_item_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_item_set_link_path(
        customer_id: str, feed_id: str, feed_item_set_id: str, feed_item_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_link_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_item_target_path(
        customer_id: str,
        feed_id: str,
        feed_item_id: str,
        feed_item_target_type: str,
        feed_item_target_id: str,
    ) -> str: ...
    @staticmethod
    def parse_feed_item_target_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def feed_mapping_path(
        customer_id: str, feed_id: str, feed_mapping_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_mapping_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def geo_target_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_geo_target_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def keyword_plan_path(customer_id: str, keyword_plan_id: str) -> str: ...
    @staticmethod
    def parse_keyword_plan_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def keyword_plan_ad_group_path(
        customer_id: str, keyword_plan_ad_group_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def keyword_plan_ad_group_keyword_path(
        customer_id: str, keyword_plan_ad_group_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_keyword_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def keyword_plan_campaign_path(
        customer_id: str, keyword_plan_campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def keyword_plan_campaign_keyword_path(
        customer_id: str, keyword_plan_campaign_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_keyword_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def label_path(customer_id: str, label_id: str) -> str: ...
    @staticmethod
    def parse_label_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def language_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_language_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def media_file_path(customer_id: str, media_file_id: str) -> str: ...
    @staticmethod
    def parse_media_file_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def mobile_app_category_constant_path(mobile_app_category_id: str) -> str: ...
    @staticmethod
    def parse_mobile_app_category_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def remarketing_action_path(
        customer_id: str, remarketing_action_id: str
    ) -> str: ...
    @staticmethod
    def parse_remarketing_action_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def shared_criterion_path(
        customer_id: str, shared_set_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_shared_criterion_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def shared_set_path(customer_id: str, shared_set_id: str) -> str: ...
    @staticmethod
    def parse_shared_set_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def smart_campaign_setting_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_smart_campaign_setting_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def topic_constant_path(topic_id: str) -> str: ...
    @staticmethod
    def parse_topic_constant_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def user_interest_path(customer_id: str, user_interest_id: str) -> str: ...
    @staticmethod
    def parse_user_interest_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def user_list_path(customer_id: str, user_list_id: str) -> str: ...
    @staticmethod
    def parse_user_list_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials | None = None,
        transport: str | BatchJobServiceTransport | None = None,
        client_options: client_options_lib.ClientOptions | dict | None = None,
        client_info: gapic_v1.client_info.ClientInfo = ...,
    ) -> None: ...
    def mutate_batch_job(
        self,
        request: batch_job_service.MutateBatchJobRequest | dict | None = None,
        *,
        customer_id: str | None = None,
        operation: batch_job_service.BatchJobOperation | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> batch_job_service.MutateBatchJobResponse: ...
    def list_batch_job_results(
        self,
        request: batch_job_service.ListBatchJobResultsRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> pagers.ListBatchJobResultsPager: ...
    def run_batch_job(
        self,
        request: batch_job_service.RunBatchJobRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> operation.Operation: ...
    def add_batch_job_operations(
        self,
        request: batch_job_service.AddBatchJobOperationsRequest | dict | None = None,
        *,
        resource_name: str | None = None,
        sequence_token: str | None = None,
        mutate_operations: MutableSequence[google_ads_service.MutateOperation]
        | None = None,
        retry: retries.Retry | gapic_v1.method._MethodDefault = ...,
        timeout: float | object = ...,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> batch_job_service.AddBatchJobOperationsResponse: ...
