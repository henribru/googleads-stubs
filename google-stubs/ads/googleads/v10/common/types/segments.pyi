import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.common.types import criteria as criteria

__protobuf__: Incomplete

class Segments(proto.Message):
    ad_destination_type: Incomplete
    ad_network_type: Incomplete
    budget_campaign_association_status: Incomplete
    click_type: Incomplete
    conversion_action: Incomplete
    conversion_action_category: Incomplete
    conversion_action_name: Incomplete
    conversion_adjustment: Incomplete
    conversion_attribution_event_type: Incomplete
    conversion_lag_bucket: Incomplete
    conversion_or_adjustment_lag_bucket: Incomplete
    date: Incomplete
    day_of_week: Incomplete
    device: Incomplete
    external_conversion_source: Incomplete
    geo_target_airport: Incomplete
    geo_target_canton: Incomplete
    geo_target_city: Incomplete
    geo_target_country: Incomplete
    geo_target_county: Incomplete
    geo_target_district: Incomplete
    geo_target_metro: Incomplete
    geo_target_most_specific_location: Incomplete
    geo_target_postal_code: Incomplete
    geo_target_province: Incomplete
    geo_target_region: Incomplete
    geo_target_state: Incomplete
    hotel_booking_window_days: Incomplete
    hotel_center_id: Incomplete
    hotel_check_in_date: Incomplete
    hotel_check_in_day_of_week: Incomplete
    hotel_city: Incomplete
    hotel_class: Incomplete
    hotel_country: Incomplete
    hotel_date_selection_type: Incomplete
    hotel_length_of_stay: Incomplete
    hotel_rate_rule_id: Incomplete
    hotel_rate_type: Incomplete
    hotel_price_bucket: Incomplete
    hotel_state: Incomplete
    hour: Incomplete
    interaction_on_this_extension: Incomplete
    keyword: Incomplete
    month: Incomplete
    month_of_year: Incomplete
    partner_hotel_id: Incomplete
    placeholder_type: Incomplete
    product_aggregator_id: Incomplete
    product_bidding_category_level1: Incomplete
    product_bidding_category_level2: Incomplete
    product_bidding_category_level3: Incomplete
    product_bidding_category_level4: Incomplete
    product_bidding_category_level5: Incomplete
    product_brand: Incomplete
    product_channel: Incomplete
    product_channel_exclusivity: Incomplete
    product_condition: Incomplete
    product_country: Incomplete
    product_custom_attribute0: Incomplete
    product_custom_attribute1: Incomplete
    product_custom_attribute2: Incomplete
    product_custom_attribute3: Incomplete
    product_custom_attribute4: Incomplete
    product_item_id: Incomplete
    product_language: Incomplete
    product_merchant_id: Incomplete
    product_store_id: Incomplete
    product_title: Incomplete
    product_type_l1: Incomplete
    product_type_l2: Incomplete
    product_type_l3: Incomplete
    product_type_l4: Incomplete
    product_type_l5: Incomplete
    quarter: Incomplete
    recommendation_type: Incomplete
    search_engine_results_page_type: Incomplete
    search_term_match_type: Incomplete
    slot: Incomplete
    conversion_value_rule_primary_dimension: Incomplete
    webpage: Incomplete
    week: Incomplete
    year: Incomplete
    sk_ad_network_conversion_value: Incomplete
    sk_ad_network_user_type: Incomplete
    sk_ad_network_ad_event_type: Incomplete
    sk_ad_network_source_app: Incomplete
    sk_ad_network_attribution_credit: Incomplete
    asset_interaction_target: Incomplete

class Keyword(proto.Message):
    ad_group_criterion: Incomplete
    info: Incomplete

class BudgetCampaignAssociationStatus(proto.Message):
    campaign: Incomplete
    status: Incomplete

class AssetInteractionTarget(proto.Message):
    asset: Incomplete
    interaction_on_this_asset: Incomplete

class SkAdNetworkSourceApp(proto.Message):
    sk_ad_network_source_app_id: Incomplete
