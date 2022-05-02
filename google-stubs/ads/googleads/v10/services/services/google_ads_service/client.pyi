from typing import Dict, Iterable, Optional, Sequence, Tuple, Type, Union

from _typeshed import Incomplete
from google.api_core import (
    client_options as client_options_lib,
    gapic_v1,
    retry as retries,
)
from google.auth import credentials as ga_credentials

from google.ads.googleads.v10.services.services.google_ads_service import pagers
from google.ads.googleads.v10.services.types import google_ads_service

from .transports.base import GoogleAdsServiceTransport

class GoogleAdsServiceClientMeta(type):
    def get_transport_class(
        cls, label: str = ...
    ) -> Type[GoogleAdsServiceTransport]: ...

class GoogleAdsServiceClient(metaclass=GoogleAdsServiceClientMeta):
    DEFAULT_ENDPOINT: str
    DEFAULT_MTLS_ENDPOINT: Incomplete
    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs): ...
    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs): ...
    from_service_account_json: Incomplete
    @property
    def transport(self) -> GoogleAdsServiceTransport: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback) -> None: ...
    @staticmethod
    def accessible_bidding_strategy_path(
        customer_id: str, bidding_strategy_id: str
    ) -> str: ...
    @staticmethod
    def parse_accessible_bidding_strategy_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def account_budget_path(customer_id: str, account_budget_id: str) -> str: ...
    @staticmethod
    def parse_account_budget_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def account_budget_proposal_path(
        customer_id: str, account_budget_proposal_id: str
    ) -> str: ...
    @staticmethod
    def parse_account_budget_proposal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def account_link_path(customer_id: str, account_link_id: str) -> str: ...
    @staticmethod
    def parse_account_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_path(customer_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_path(customer_id: str, ad_group_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_ad_path(customer_id: str, ad_group_id: str, ad_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_ad_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_ad_asset_combination_view_path(
        customer_id: str,
        ad_group_id: str,
        ad_id: str,
        asset_combination_id_low: str,
        asset_combination_id_high: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_asset_combination_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_ad_asset_view_path(
        customer_id: str, ad_group_id: str, ad_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_asset_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_ad_label_path(
        customer_id: str, ad_group_id: str, ad_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_ad_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_asset_path(
        customer_id: str, ad_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_audience_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_audience_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_bid_modifier_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_bid_modifier_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_customizer_path(
        customer_id: str,
        ad_group_id: str,
        criterion_id: str,
        customizer_attribute_id: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_customizer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_label_path(
        customer_id: str, ad_group_id: str, criterion_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_criterion_simulation_path(
        customer_id: str,
        ad_group_id: str,
        criterion_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_criterion_simulation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_customizer_path(
        customer_id: str, ad_group_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_customizer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_extension_setting_path(
        customer_id: str, ad_group_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_extension_setting_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_feed_path(customer_id: str, ad_group_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_ad_group_feed_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_label_path(
        customer_id: str, ad_group_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_group_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_group_simulation_path(
        customer_id: str,
        ad_group_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_ad_group_simulation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_parameter_path(
        customer_id: str, ad_group_id: str, criterion_id: str, parameter_index: str
    ) -> str: ...
    @staticmethod
    def parse_ad_parameter_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def ad_schedule_view_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_ad_schedule_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def age_range_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_age_range_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_path(customer_id: str, asset_id: str) -> str: ...
    @staticmethod
    def parse_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_field_type_view_path(customer_id: str, field_type: str) -> str: ...
    @staticmethod
    def parse_asset_field_type_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_group_path(customer_id: str, asset_group_id: str) -> str: ...
    @staticmethod
    def parse_asset_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_group_asset_path(
        customer_id: str, asset_group_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_group_listing_group_filter_path(
        customer_id: str, asset_group_id: str, listing_group_filter_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_listing_group_filter_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_group_product_group_view_path(
        customer_id: str, asset_group_id: str, listing_group_filter_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_product_group_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_group_signal_path(
        customer_id: str, asset_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_group_signal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_set_path(customer_id: str, asset_set_id: str) -> str: ...
    @staticmethod
    def parse_asset_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def asset_set_asset_path(
        customer_id: str, asset_set_id: str, asset_id: str
    ) -> str: ...
    @staticmethod
    def parse_asset_set_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def audience_path(customer_id: str, audience_id: str) -> str: ...
    @staticmethod
    def parse_audience_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def batch_job_path(customer_id: str, batch_job_id: str) -> str: ...
    @staticmethod
    def parse_batch_job_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def bidding_data_exclusion_path(
        customer_id: str, seasonality_event_id: str
    ) -> str: ...
    @staticmethod
    def parse_bidding_data_exclusion_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def bidding_seasonality_adjustment_path(
        customer_id: str, seasonality_event_id: str
    ) -> str: ...
    @staticmethod
    def parse_bidding_seasonality_adjustment_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def bidding_strategy_path(customer_id: str, bidding_strategy_id: str) -> str: ...
    @staticmethod
    def parse_bidding_strategy_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def bidding_strategy_simulation_path(
        customer_id: str,
        bidding_strategy_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_bidding_strategy_simulation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def billing_setup_path(customer_id: str, billing_setup_id: str) -> str: ...
    @staticmethod
    def parse_billing_setup_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def call_view_path(customer_id: str, call_detail_id: str) -> str: ...
    @staticmethod
    def parse_call_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_asset_path(
        customer_id: str, campaign_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_asset_set_path(
        customer_id: str, campaign_id: str, asset_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_asset_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_audience_view_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_audience_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_bid_modifier_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_bid_modifier_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_budget_path(customer_id: str, campaign_budget_id: str) -> str: ...
    @staticmethod
    def parse_campaign_budget_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_conversion_goal_path(
        customer_id: str, campaign_id: str, category: str, source: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_conversion_goal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_criterion_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_criterion_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_criterion_simulation_path(
        customer_id: str,
        campaign_id: str,
        criterion_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_campaign_criterion_simulation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_customizer_path(
        customer_id: str, campaign_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_customizer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_draft_path(
        customer_id: str, base_campaign_id: str, draft_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_draft_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_experiment_path(
        customer_id: str, campaign_experiment_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_experiment_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_extension_setting_path(
        customer_id: str, campaign_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_extension_setting_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_feed_path(customer_id: str, campaign_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_campaign_feed_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_group_path(customer_id: str, campaign_group_id: str) -> str: ...
    @staticmethod
    def parse_campaign_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_label_path(
        customer_id: str, campaign_id: str, label_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_shared_set_path(
        customer_id: str, campaign_id: str, shared_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_campaign_shared_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def campaign_simulation_path(
        customer_id: str,
        campaign_id: str,
        type: str,
        modification_method: str,
        start_date: str,
        end_date: str,
    ) -> str: ...
    @staticmethod
    def parse_campaign_simulation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def carrier_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_carrier_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def change_event_path(
        customer_id: str, timestamp_micros: str, command_index: str, mutate_index: str
    ) -> str: ...
    @staticmethod
    def parse_change_event_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def change_status_path(customer_id: str, change_status_id: str) -> str: ...
    @staticmethod
    def parse_change_status_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def click_view_path(customer_id: str, date: str, gclid: str) -> str: ...
    @staticmethod
    def parse_click_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def combined_audience_path(customer_id: str, combined_audience_id: str) -> str: ...
    @staticmethod
    def parse_combined_audience_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_action_path(customer_id: str, conversion_action_id: str) -> str: ...
    @staticmethod
    def parse_conversion_action_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_custom_variable_path(
        customer_id: str, conversion_custom_variable_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_custom_variable_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_goal_campaign_config_path(
        customer_id: str, campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_goal_campaign_config_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_path(
        customer_id: str, conversion_value_rule_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def conversion_value_rule_set_path(
        customer_id: str, conversion_value_rule_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_conversion_value_rule_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def currency_constant_path(code: str) -> str: ...
    @staticmethod
    def parse_currency_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def custom_audience_path(customer_id: str, custom_audience_id: str) -> str: ...
    @staticmethod
    def parse_custom_audience_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def custom_conversion_goal_path(customer_id: str, goal_id: str) -> str: ...
    @staticmethod
    def parse_custom_conversion_goal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_asset_path(
        customer_id: str, asset_id: str, field_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_asset_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_client_path(customer_id: str, client_customer_id: str) -> str: ...
    @staticmethod
    def parse_customer_client_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_client_link_path(
        customer_id: str, client_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_client_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_conversion_goal_path(
        customer_id: str, category: str, source: str
    ) -> str: ...
    @staticmethod
    def parse_customer_conversion_goal_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_customizer_path(
        customer_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_customizer_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_extension_setting_path(
        customer_id: str, extension_type: str
    ) -> str: ...
    @staticmethod
    def parse_customer_extension_setting_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_customer_feed_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_label_path(customer_id: str, label_id: str) -> str: ...
    @staticmethod
    def parse_customer_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_manager_link_path(
        customer_id: str, manager_customer_id: str, manager_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_manager_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_negative_criterion_path(
        customer_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_negative_criterion_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_user_access_path(customer_id: str, user_id: str) -> str: ...
    @staticmethod
    def parse_customer_user_access_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customer_user_access_invitation_path(
        customer_id: str, invitation_id: str
    ) -> str: ...
    @staticmethod
    def parse_customer_user_access_invitation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def custom_interest_path(customer_id: str, custom_interest_id: str) -> str: ...
    @staticmethod
    def parse_custom_interest_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def customizer_attribute_path(
        customer_id: str, customizer_attribute_id: str
    ) -> str: ...
    @staticmethod
    def parse_customizer_attribute_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def detailed_demographic_path(
        customer_id: str, detailed_demographic_id: str
    ) -> str: ...
    @staticmethod
    def parse_detailed_demographic_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def detail_placement_view_path(
        customer_id: str, ad_group_id: str, base64_placement: str
    ) -> str: ...
    @staticmethod
    def parse_detail_placement_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def display_keyword_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_display_keyword_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def distance_view_path(
        customer_id: str, placeholder_chain_id: str, distance_bucket: str
    ) -> str: ...
    @staticmethod
    def parse_distance_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def domain_category_path(
        customer_id: str, campaign_id: str, base64_category: str, language_code: str
    ) -> str: ...
    @staticmethod
    def parse_domain_category_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def dynamic_search_ads_search_term_view_path(
        customer_id: str,
        ad_group_id: str,
        search_term_fingerprint: str,
        headline_fingerprint: str,
        landing_page_fingerprint: str,
        page_url_fingerprint: str,
    ) -> str: ...
    @staticmethod
    def parse_dynamic_search_ads_search_term_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def expanded_landing_page_view_path(
        customer_id: str, expanded_final_url_fingerprint: str
    ) -> str: ...
    @staticmethod
    def parse_expanded_landing_page_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def experiment_path(customer_id: str, trial_id: str) -> str: ...
    @staticmethod
    def parse_experiment_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def experiment_arm_path(
        customer_id: str, trial_id: str, trial_arm_id: str
    ) -> str: ...
    @staticmethod
    def parse_experiment_arm_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def extension_feed_item_path(customer_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_extension_feed_item_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_path(customer_id: str, feed_id: str) -> str: ...
    @staticmethod
    def parse_feed_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_path(customer_id: str, feed_id: str, feed_item_id: str) -> str: ...
    @staticmethod
    def parse_feed_item_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_set_path(
        customer_id: str, feed_id: str, feed_item_set_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_set_link_path(
        customer_id: str, feed_id: str, feed_item_set_id: str, feed_item_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_item_set_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_item_target_path(
        customer_id: str,
        feed_id: str,
        feed_item_id: str,
        feed_item_target_type: str,
        feed_item_target_id: str,
    ) -> str: ...
    @staticmethod
    def parse_feed_item_target_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_mapping_path(
        customer_id: str, feed_id: str, feed_mapping_id: str
    ) -> str: ...
    @staticmethod
    def parse_feed_mapping_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def feed_placeholder_view_path(customer_id: str, placeholder_type: str) -> str: ...
    @staticmethod
    def parse_feed_placeholder_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def gender_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_gender_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def geographic_view_path(
        customer_id: str, country_criterion_id: str, location_type: str
    ) -> str: ...
    @staticmethod
    def parse_geographic_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def geo_target_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_geo_target_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def group_placement_view_path(
        customer_id: str, ad_group_id: str, base64_placement: str
    ) -> str: ...
    @staticmethod
    def parse_group_placement_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def hotel_group_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_hotel_group_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def hotel_performance_view_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_hotel_performance_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def hotel_reconciliation_path(customer_id: str, commission_id: str) -> str: ...
    @staticmethod
    def parse_hotel_reconciliation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def income_range_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_income_range_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_path(customer_id: str, keyword_plan_id: str) -> str: ...
    @staticmethod
    def parse_keyword_plan_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_ad_group_path(
        customer_id: str, keyword_plan_ad_group_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_ad_group_keyword_path(
        customer_id: str, keyword_plan_ad_group_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_ad_group_keyword_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_campaign_path(
        customer_id: str, keyword_plan_campaign_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_plan_campaign_keyword_path(
        customer_id: str, keyword_plan_campaign_keyword_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_plan_campaign_keyword_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_theme_constant_path(
        express_category_id: str, express_sub_category_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_theme_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def keyword_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_keyword_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def label_path(customer_id: str, label_id: str) -> str: ...
    @staticmethod
    def parse_label_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def landing_page_view_path(
        customer_id: str, unexpanded_final_url_fingerprint: str
    ) -> str: ...
    @staticmethod
    def parse_landing_page_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def language_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_language_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def lead_form_submission_data_path(
        customer_id: str, lead_form_user_submission_id: str
    ) -> str: ...
    @staticmethod
    def parse_lead_form_submission_data_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def life_event_path(customer_id: str, life_event_id: str) -> str: ...
    @staticmethod
    def parse_life_event_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def location_view_path(
        customer_id: str, campaign_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_location_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def managed_placement_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_managed_placement_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def media_file_path(customer_id: str, media_file_id: str) -> str: ...
    @staticmethod
    def parse_media_file_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def mobile_app_category_constant_path(mobile_app_category_id: str) -> str: ...
    @staticmethod
    def parse_mobile_app_category_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def mobile_device_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_mobile_device_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def offline_user_data_job_path(
        customer_id: str, offline_user_data_update_id: str
    ) -> str: ...
    @staticmethod
    def parse_offline_user_data_job_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def operating_system_version_constant_path(criterion_id: str) -> str: ...
    @staticmethod
    def parse_operating_system_version_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def paid_organic_search_term_view_path(
        customer_id: str, campaign_id: str, ad_group_id: str, base64_search_term: str
    ) -> str: ...
    @staticmethod
    def parse_paid_organic_search_term_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def parental_status_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_parental_status_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def payments_account_path(customer_id: str, payments_account_id: str) -> str: ...
    @staticmethod
    def parse_payments_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def product_bidding_category_constant_path(
        country_code: str, level: str, id: str
    ) -> str: ...
    @staticmethod
    def parse_product_bidding_category_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def product_group_view_path(
        customer_id: str, adgroup_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_product_group_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def recommendation_path(customer_id: str, recommendation_id: str) -> str: ...
    @staticmethod
    def parse_recommendation_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def remarketing_action_path(
        customer_id: str, remarketing_action_id: str
    ) -> str: ...
    @staticmethod
    def parse_remarketing_action_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def search_term_view_path(
        customer_id: str, campaign_id: str, ad_group_id: str, query: str
    ) -> str: ...
    @staticmethod
    def parse_search_term_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def shared_criterion_path(
        customer_id: str, shared_set_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_shared_criterion_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def shared_set_path(customer_id: str, shared_set_id: str) -> str: ...
    @staticmethod
    def parse_shared_set_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def shopping_performance_view_path(customer_id: str) -> str: ...
    @staticmethod
    def parse_shopping_performance_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def smart_campaign_search_term_view_path(
        customer_id: str, campaign_id: str, query: str
    ) -> str: ...
    @staticmethod
    def parse_smart_campaign_search_term_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def smart_campaign_setting_path(customer_id: str, campaign_id: str) -> str: ...
    @staticmethod
    def parse_smart_campaign_setting_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def third_party_app_analytics_link_path(
        customer_id: str, customer_link_id: str
    ) -> str: ...
    @staticmethod
    def parse_third_party_app_analytics_link_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def topic_constant_path(topic_id: str) -> str: ...
    @staticmethod
    def parse_topic_constant_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def topic_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_topic_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def user_interest_path(customer_id: str, user_interest_id: str) -> str: ...
    @staticmethod
    def parse_user_interest_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def user_list_path(customer_id: str, user_list_id: str) -> str: ...
    @staticmethod
    def parse_user_list_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def user_location_view_path(
        customer_id: str, country_criterion_id: str, is_targeting_location: str
    ) -> str: ...
    @staticmethod
    def parse_user_location_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def video_path(customer_id: str, video_id: str) -> str: ...
    @staticmethod
    def parse_video_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def webpage_view_path(
        customer_id: str, ad_group_id: str, criterion_id: str
    ) -> str: ...
    @staticmethod
    def parse_webpage_view_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_billing_account_path(billing_account: str) -> str: ...
    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_folder_path(folder: str) -> str: ...
    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_organization_path(organization: str) -> str: ...
    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_project_path(project: str) -> str: ...
    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]: ...
    @staticmethod
    def common_location_path(project: str, location: str) -> str: ...
    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]: ...
    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = ...,
        transport: Union[str, GoogleAdsServiceTransport, None] = ...,
        client_options: Optional[client_options_lib.ClientOptions] = ...,
        client_info: gapic_v1.client_info.ClientInfo = ...
    ) -> None: ...
    def search(
        self,
        request: Union[google_ads_service.SearchGoogleAdsRequest, dict] = ...,
        *,
        customer_id: str = ...,
        query: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> pagers.SearchPager: ...
    def search_stream(
        self,
        request: Union[google_ads_service.SearchGoogleAdsStreamRequest, dict] = ...,
        *,
        customer_id: str = ...,
        query: str = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> Iterable[google_ads_service.SearchGoogleAdsStreamResponse]: ...
    def mutate(
        self,
        request: Union[google_ads_service.MutateGoogleAdsRequest, dict] = ...,
        *,
        customer_id: str = ...,
        mutate_operations: Sequence[google_ads_service.MutateOperation] = ...,
        retry: Union[retries.Retry, gapic_v1.method._MethodDefault] = ...,
        timeout: float = ...,
        metadata: Sequence[Tuple[str, str]] = ...
    ) -> google_ads_service.MutateGoogleAdsResponse: ...
