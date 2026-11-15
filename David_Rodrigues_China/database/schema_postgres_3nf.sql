-- ============================================================================
-- UNIVERSIDADE DO ALGARVE - MSc in Informatics Engineering (2026/2027)
-- Course: Data Modelling and Integration (DMI) - Project P1
-- Student: David Rodrigues (Subtopic: China Industrial, Customs & Logistics)
-- Source D1: Structured Relational Database (PostgreSQL / SQL 3NF)
-- Description: Complete DDL Schema for 20 Normalized Relational Tables (3NF)
-- ============================================================================

PRAGMA foreign_keys = ON;

-- 33. cn_provinces_prefectures_cities
CREATE TABLE IF NOT EXISTS cn_provinces_prefectures_cities (
    admin_division_code_gb CHAR(6) PRIMARY KEY,
    province_name_en VARCHAR(100) NOT NULL,
    province_name_zh VARCHAR(100) NOT NULL,
    city_prefecture_name_en VARCHAR(100) NOT NULL,
    economic_macro_region VARCHAR(80) NOT NULL CHECK (
        economic_macro_region IN (
            'Pearl River Delta / Greater Bay Area',
            'Yangtze River Delta',
            'Bohai Economic Rim',
            'Western China',
            'Central China',
            'Special Administrative Region'
        )
    ),
    gdp_billion_cny NUMERIC(14,2) NOT NULL CHECK (gdp_billion_cny > 0),
    export_share_pct NUMERIC(5,2) NOT NULL CHECK (export_share_pct >= 0 AND export_share_pct <= 100),
    average_industrial_wage_cny NUMERIC(10,2) NOT NULL CHECK (average_industrial_wage_cny > 0)
);

-- 34. cn_special_economic_ftz_zones
CREATE TABLE IF NOT EXISTS cn_special_economic_ftz_zones (
    zone_id INTEGER PRIMARY KEY,
    zone_code VARCHAR(25) NOT NULL UNIQUE,
    zone_name_en VARCHAR(150) NOT NULL,
    admin_division_code_gb CHAR(6) NOT NULL,
    zone_type VARCHAR(60) NOT NULL CHECK (
        zone_type IN (
            'Special Economic Zone',
            'Pilot FTZ',
            'Comprehensive Bonded Zone',
            'Cross-Border E-Commerce Pilot Zone',
            'Lusophone In-Depth Cooperation Zone'
        )
    ),
    corporate_tax_rate_pct NUMERIC(5,2) NOT NULL CHECK (corporate_tax_rate_pct >= 0 AND corporate_tax_rate_pct <= 35),
    vat_export_rebate_bonus_pct NUMERIC(5,2) NOT NULL DEFAULT 0.00,
    established_date DATE NOT NULL,
    FOREIGN KEY (admin_division_code_gb) REFERENCES cn_provinces_prefectures_cities(admin_division_code_gb)
);

-- 35. cn_enterprises_manufacturers
-- Note on Semantic Heterogeneity: registered_capital_wan_cny is expressed in "Wan" (1 Wan = 10,000 CNY)
CREATE TABLE IF NOT EXISTS cn_enterprises_manufacturers (
    uscc_code CHAR(18) PRIMARY KEY,
    customs_cr_code_10 CHAR(10) NOT NULL UNIQUE,
    company_name_en VARCHAR(200) NOT NULL,
    company_name_zh VARCHAR(200) NOT NULL,
    ownership_type VARCHAR(50) NOT NULL CHECK (
        ownership_type IN (
            'SOE - State-Owned Enterprise',
            'Private Domestic',
            'Sino-Foreign Joint Venture',
            'Publicly Listed Tech Giant',
            'WFOE'
        )
    ),
    industry_code_gbt4754 CHAR(4) NOT NULL,
    admin_division_code_gb CHAR(6) NOT NULL,
    zone_id INTEGER,
    registered_capital_wan_cny NUMERIC(14,2) NOT NULL CHECK (registered_capital_wan_cny > 0),
    aeo_customs_tier VARCHAR(40) NOT NULL CHECK (
        aeo_customs_tier IN ('Advanced Certified AEO', 'General Certified AEO', 'General Enterprise', 'Discredited')
    ),
    incorporation_date DATE NOT NULL,
    FOREIGN KEY (admin_division_code_gb) REFERENCES cn_provinces_prefectures_cities(admin_division_code_gb),
    FOREIGN KEY (zone_id) REFERENCES cn_special_economic_ftz_zones(zone_id)
);

-- 36. cn_factory_production_facilities
CREATE TABLE IF NOT EXISTS cn_factory_production_facilities (
    facility_id INTEGER PRIMARY KEY,
    uscc_code CHAR(18) NOT NULL,
    facility_name VARCHAR(180) NOT NULL,
    admin_division_code_gb CHAR(6) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL,
    floor_area_sqm INTEGER NOT NULL CHECK (floor_area_sqm > 0),
    workforce_count INTEGER NOT NULL CHECK (workforce_count > 0),
    annual_capacity_units BIGINT NOT NULL CHECK (annual_capacity_units > 0),
    iso9001_certified BOOLEAN NOT NULL DEFAULT 1,
    iso14001_certified BOOLEAN NOT NULL DEFAULT 1,
    cifer_gacc_food_reg_no VARCHAR(35),
    grid_carbon_intensity_kgco2_kwh NUMERIC(6,4) NOT NULL,
    FOREIGN KEY (uscc_code) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (admin_division_code_gb) REFERENCES cn_provinces_prefectures_cities(admin_division_code_gb)
);

-- 37. cn_hs_tariff_schedule_gacc
-- Note on Semantic Heterogeneity: hs_code_10_cn uses Chinese 10-digit GACC nomenclature;
-- first 6 digits (hs_code_6_wco) link to Portuguese/EU TARIC 10-digit codes.
CREATE TABLE IF NOT EXISTS cn_hs_tariff_schedule_gacc (
    hs_code_10_cn CHAR(10) PRIMARY KEY,
    hs_code_6_wco CHAR(6) NOT NULL,
    ciq_code_13 CHAR(13) NOT NULL,
    commodity_name_zh VARCHAR(200) NOT NULL,
    commodity_name_en VARCHAR(200) NOT NULL,
    statutory_unit_cn VARCHAR(25) NOT NULL,
    mfn_import_duty_pct NUMERIC(5,2) NOT NULL CHECK (mfn_import_duty_pct >= 0),
    export_duty_pct NUMERIC(5,2) NOT NULL DEFAULT 0.00,
    vat_standard_rate_pct NUMERIC(5,2) NOT NULL CHECK (vat_standard_rate_pct IN (0.00, 9.00, 13.00)),
    export_vat_rebate_rate_pct NUMERIC(5,2) NOT NULL CHECK (export_vat_rebate_rate_pct >= 0 AND export_vat_rebate_rate_pct <= 17),
    regulatory_condition_codes VARCHAR(20) NOT NULL
);

-- 38. cn_products_industrial_catalog
-- Note on Semantic Heterogeneity: unit_weight_jin is in Chinese Jin (1 Jin = 0.5 kg)
CREATE TABLE IF NOT EXISTS cn_products_industrial_catalog (
    product_sku_cn VARCHAR(35) PRIMARY KEY,
    manufacturer_uscc CHAR(18) NOT NULL,
    facility_id INTEGER NOT NULL,
    hs_code_10_cn CHAR(10) NOT NULL,
    model_designation VARCHAR(150) NOT NULL,
    technical_category VARCHAR(80) NOT NULL,
    unit_weight_jin NUMERIC(12,3) NOT NULL CHECK (unit_weight_jin > 0),
    unit_volume_cbm NUMERIC(10,4) NOT NULL CHECK (unit_volume_cbm > 0),
    ex_works_cost_cny NUMERIC(14,2) NOT NULL CHECK (ex_works_cost_cny > 0),
    fob_reference_price_usd NUMERIC(14,2) NOT NULL CHECK (fob_reference_price_usd > 0),
    contains_lithium_hazmat_class VARCHAR(20),
    embedded_carbon_kgco2_per_unit NUMERIC(12,3) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (manufacturer_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (facility_id) REFERENCES cn_factory_production_facilities(facility_id),
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 39. cn_ccc_compulsory_certifications
CREATE TABLE IF NOT EXISTS cn_ccc_compulsory_certifications (
    ccc_certificate_no CHAR(16) PRIMARY KEY,
    product_sku_cn VARCHAR(35) NOT NULL,
    applicant_uscc CHAR(18) NOT NULL,
    issuing_body VARCHAR(60) NOT NULL,
    gb_standard_applied VARCHAR(60) NOT NULL,
    issue_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    certification_status VARCHAR(25) NOT NULL CHECK (
        certification_status IN ('Valid', 'Suspended', 'Revoked', 'Pending Renewal')
    ),
    eu_ce_equivalent_claimed BOOLEAN NOT NULL DEFAULT 1,
    FOREIGN KEY (product_sku_cn) REFERENCES cn_products_industrial_catalog(product_sku_cn),
    FOREIGN KEY (applicant_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 40. cn_mofcom_trade_licenses_quotas
CREATE TABLE IF NOT EXISTS cn_mofcom_trade_licenses_quotas (
    license_no_mofcom VARCHAR(28) PRIMARY KEY,
    holder_uscc CHAR(18) NOT NULL,
    hs_code_10_cn CHAR(10) NOT NULL,
    license_direction VARCHAR(40) NOT NULL CHECK (
        license_direction IN (
            'Export Control Dual-Use',
            'Strategic EV & Battery Export License',
            'Automatic Import License',
            'Agricultural Tariff Quota'
        )
    ),
    destination_or_origin_country_iso CHAR(3) NOT NULL DEFAULT 'PRT',
    authorized_quantity_metric_tons NUMERIC(12,3) NOT NULL CHECK (authorized_quantity_metric_tons > 0),
    authorized_value_usd NUMERIC(14,2) NOT NULL CHECK (authorized_value_usd > 0),
    valid_from DATE NOT NULL,
    valid_until DATE NOT NULL,
    port_of_clearance_limit VARCHAR(60) NOT NULL,
    FOREIGN KEY (holder_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 41. cn_b2b_commercial_contracts
CREATE TABLE IF NOT EXISTS cn_b2b_commercial_contracts (
    contract_no_cn VARCHAR(32) PRIMARY KEY,
    chinese_party_uscc CHAR(18) NOT NULL,
    portuguese_counterparty_eori VARCHAR(20) NOT NULL,
    portuguese_counterparty_name VARCHAR(200) NOT NULL,
    trade_direction VARCHAR(25) NOT NULL CHECK (trade_direction IN ('CN_EXPORT_TO_PT', 'CN_IMPORT_FROM_PT')),
    signing_date DATE NOT NULL,
    incoterm_2020 CHAR(3) NOT NULL CHECK (incoterm_2020 IN ('FOB', 'CIF', 'CFR', 'CIP', 'EXW', 'DDP', 'FCA', 'DAP')),
    contract_currency CHAR(3) NOT NULL CHECK (contract_currency IN ('CNY', 'USD', 'EUR')),
    total_contract_amount NUMERIC(15,2) NOT NULL CHECK (total_contract_amount > 0),
    payment_terms_code VARCHAR(30) NOT NULL,
    dispute_arbitration_center VARCHAR(60) NOT NULL,
    FOREIGN KEY (chinese_party_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 42. cn_commercial_invoices
CREATE TABLE IF NOT EXISTS cn_commercial_invoices (
    invoice_no VARCHAR(32) PRIMARY KEY,
    contract_no_cn VARCHAR(32) NOT NULL,
    issue_date DATE NOT NULL,
    seller_uscc CHAR(18) NOT NULL,
    buyer_pt_eori VARCHAR(20) NOT NULL,
    invoice_currency CHAR(3) NOT NULL CHECK (invoice_currency IN ('CNY', 'USD', 'EUR')),
    subtotal_goods_value NUMERIC(14,2) NOT NULL CHECK (subtotal_goods_value > 0),
    international_freight_value NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    marine_insurance_value NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    total_invoice_value NUMERIC(14,2) NOT NULL CHECK (total_invoice_value >= subtotal_goods_value),
    pboc_exchange_rate_to_cny NUMERIC(10,6) NOT NULL,
    FOREIGN KEY (contract_no_cn) REFERENCES cn_b2b_commercial_contracts(contract_no_cn)
);

-- 43. cn_commercial_invoice_lines
CREATE TABLE IF NOT EXISTS cn_commercial_invoice_lines (
    invoice_line_id INTEGER PRIMARY KEY,
    invoice_no VARCHAR(32) NOT NULL,
    line_number SMALLINT NOT NULL,
    product_sku_cn VARCHAR(35),
    hs_code_10_cn CHAR(10) NOT NULL,
    item_description_en VARCHAR(255) NOT NULL,
    quantity_units NUMERIC(12,2) NOT NULL CHECK (quantity_units > 0),
    net_weight_jin NUMERIC(12,3) NOT NULL CHECK (net_weight_jin > 0),
    gross_weight_jin NUMERIC(12,3) NOT NULL CHECK (gross_weight_jin >= net_weight_jin),
    unit_price_fob NUMERIC(12,4) NOT NULL CHECK (unit_price_fob > 0),
    line_total_amount NUMERIC(14,2) NOT NULL CHECK (line_total_amount > 0),
    batch_lot_number VARCHAR(40) NOT NULL,
    FOREIGN KEY (invoice_no) REFERENCES cn_commercial_invoices(invoice_no),
    FOREIGN KEY (product_sku_cn) REFERENCES cn_products_industrial_catalog(product_sku_cn),
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 44. cn_customs_export_declarations_gacc
-- Note on Syntactic Heterogeneity: declaration_date_epoch is stored as Unix Epoch seconds (BIGINT)
CREATE TABLE IF NOT EXISTS cn_customs_export_declarations_gacc (
    gacc_entry_id_18 CHAR(18) PRIMARY KEY,
    invoice_no VARCHAR(32) NOT NULL,
    exporter_uscc CHAR(18) NOT NULL,
    customs_port_code_cn CHAR(4) NOT NULL,
    declaration_date_epoch BIGINT NOT NULL,
    supervision_regime_code CHAR(4) NOT NULL,
    transport_mode_code VARCHAR(20) NOT NULL,
    bill_of_lading_or_waybill_no VARCHAR(35) NOT NULL,
    vessel_imo_or_train_no VARCHAR(30) NOT NULL,
    port_of_discharge_unlocode CHAR(5) NOT NULL,
    total_fob_value_cny NUMERIC(14,2) NOT NULL CHECK (total_fob_value_cny > 0),
    total_fob_value_usd NUMERIC(14,2) NOT NULL CHECK (total_fob_value_usd > 0),
    clearance_channel VARCHAR(35) NOT NULL CHECK (
        clearance_channel IN ('Released Automatically', 'Doc Review', 'Physical Inspection')
    ),
    FOREIGN KEY (invoice_no) REFERENCES cn_commercial_invoices(invoice_no),
    FOREIGN KEY (exporter_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 45. cn_customs_import_declarations_gacc
CREATE TABLE IF NOT EXISTS cn_customs_import_declarations_gacc (
    gacc_import_id_18 CHAR(18) PRIMARY KEY,
    importer_cn_uscc CHAR(18) NOT NULL,
    portuguese_exporter_nif_eori VARCHAR(20) NOT NULL,
    portuguese_cifer_reg_no VARCHAR(35),
    hs_code_10_cn CHAR(10) NOT NULL,
    port_of_loading_pt CHAR(5) NOT NULL,
    customs_entry_port_cn CHAR(4) NOT NULL,
    bill_of_lading_no VARCHAR(35) NOT NULL,
    cif_value_cny NUMERIC(14,2) NOT NULL CHECK (cif_value_cny > 0),
    import_tariff_paid_cny NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    consumption_tax_paid_cny NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    vat_import_paid_cny NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    declaration_date DATE NOT NULL,
    FOREIGN KEY (importer_cn_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 46. cn_ciq_inspection_quarantine_records
CREATE TABLE IF NOT EXISTS cn_ciq_inspection_quarantine_records (
    ciq_inspection_id VARCHAR(28) PRIMARY KEY,
    gacc_declaration_id_18 CHAR(18) NOT NULL,
    inspection_direction VARCHAR(35) NOT NULL CHECK (
        inspection_direction IN ('Outbound Export Inspection', 'Inbound Import Quarantine')
    ),
    ciq_bureau_branch VARCHAR(60) NOT NULL,
    sample_lab_test_code VARCHAR(35) NOT NULL,
    pesticide_or_heavy_metal_ppm NUMERIC(8,4) NOT NULL DEFAULT 0.0000,
    wood_packaging_ispm15_compliant BOOLEAN NOT NULL DEFAULT 1,
    chinese_labeling_compliant BOOLEAN NOT NULL DEFAULT 1,
    e_ciq_certificate_no VARCHAR(35) NOT NULL UNIQUE,
    inspection_verdict VARCHAR(45) NOT NULL CHECK (
        inspection_verdict IN (
            'Pass - Certificate Issued',
            'Quarantine Treatment Required',
            'Labeling Rectification Ordered',
            'Rejected - Return to Portugal/Destroy'
        )
    ),
    inspection_timestamp TIMESTAMP NOT NULL
);

-- 47. cn_vat_export_tax_rebates_sta
CREATE TABLE IF NOT EXISTS cn_vat_export_tax_rebates_sta (
    rebate_claim_id VARCHAR(28) PRIMARY KEY,
    gacc_entry_id_18 CHAR(18) NOT NULL,
    exporter_uscc CHAR(18) NOT NULL,
    fapiao_tax_invoice_no VARCHAR(32) NOT NULL UNIQUE,
    eligible_fob_amount_cny NUMERIC(14,2) NOT NULL CHECK (eligible_fob_amount_cny > 0),
    applied_rebate_rate_pct NUMERIC(5,2) NOT NULL,
    rebate_amount_paid_cny NUMERIC(14,2) NOT NULL CHECK (rebate_amount_paid_cny >= 0),
    sta_approval_status VARCHAR(30) NOT NULL CHECK (
        sta_approval_status IN ('Approved & Credited', 'Under Audit', 'Denied')
    ),
    payout_date DATE NOT NULL,
    FOREIGN KEY (gacc_entry_id_18) REFERENCES cn_customs_export_declarations_gacc(gacc_entry_id_18),
    FOREIGN KEY (exporter_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 48. cn_fx_settlements_pboc_safe
CREATE TABLE IF NOT EXISTS cn_fx_settlements_pboc_safe (
    safe_verification_no VARCHAR(32) PRIMARY KEY,
    swift_uetr_or_cips_id VARCHAR(45) NOT NULL UNIQUE,
    invoice_no VARCHAR(32) NOT NULL,
    chinese_entity_uscc CHAR(18) NOT NULL,
    portuguese_entity_nif VARCHAR(15) NOT NULL,
    chinese_bank_name VARCHAR(80) NOT NULL,
    settlement_channel VARCHAR(25) NOT NULL CHECK (
        settlement_channel IN ('SWIFT_EUR', 'SWIFT_USD', 'CIPS_DIRECT_RMB')
    ),
    original_currency CHAR(3) NOT NULL CHECK (original_currency IN ('EUR', 'USD', 'CNY')),
    settled_foreign_amount NUMERIC(14,2) NOT NULL CHECK (settled_foreign_amount > 0),
    settled_rmb_cny_amount NUMERIC(14,2) NOT NULL CHECK (settled_rmb_cny_amount > 0),
    pboc_central_parity_rate NUMERIC(10,6) NOT NULL,
    settlement_date DATE NOT NULL,
    FOREIGN KEY (invoice_no) REFERENCES cn_commercial_invoices(invoice_no),
    FOREIGN KEY (chinese_entity_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 49. cn_cargo_insurance_policies_sinosure
CREATE TABLE IF NOT EXISTS cn_cargo_insurance_policies_sinosure (
    policy_no_cn VARCHAR(32) PRIMARY KEY,
    insurer_company VARCHAR(60) NOT NULL,
    contract_no_cn VARCHAR(32) NOT NULL,
    gacc_entry_id_18 CHAR(18),
    policy_type VARCHAR(45) NOT NULL CHECK (
        policy_type IN ('Marine All Risks ICC-A', 'Export Credit Risk SINOSURE', 'Railway Transit Risk')
    ),
    insured_value_usd NUMERIC(14,2) NOT NULL CHECK (insured_value_usd > 0),
    premium_paid_cny NUMERIC(12,2) NOT NULL CHECK (premium_paid_cny > 0),
    claim_filed BOOLEAN NOT NULL DEFAULT 0,
    claim_payout_cny NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (contract_no_cn) REFERENCES cn_b2b_commercial_contracts(contract_no_cn),
    FOREIGN KEY (gacc_entry_id_18) REFERENCES cn_customs_export_declarations_gacc(gacc_entry_id_18)
);

-- 50. cn_state_industrial_subsidies
CREATE TABLE IF NOT EXISTS cn_state_industrial_subsidies (
    subsidy_grant_id INTEGER PRIMARY KEY,
    recipient_uscc CHAR(18) NOT NULL,
    granting_authority VARCHAR(100) NOT NULL,
    program_category VARCHAR(60) NOT NULL,
    fiscal_year SMALLINT NOT NULL CHECK (fiscal_year BETWEEN 2020 AND 2030),
    subsidy_amount_cny NUMERIC(14,2) NOT NULL CHECK (subsidy_amount_cny > 0),
    disbursement_date DATE NOT NULL,
    FOREIGN KEY (recipient_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 51. cn_outward_fdi_approvals_ndrc
CREATE TABLE IF NOT EXISTS cn_outward_fdi_approvals_ndrc (
    ndrc_approval_code VARCHAR(32) PRIMARY KEY,
    chinese_investor_uscc CHAR(18) NOT NULL,
    target_pt_company_nif VARCHAR(15) NOT NULL,
    target_pt_company_name VARCHAR(150) NOT NULL,
    investment_mode VARCHAR(45) NOT NULL CHECK (
        investment_mode IN ('M&A Equity Acquisition', 'Greenfield Gigafactory', 'Joint Venture', 'Port Terminal Concession')
    ),
    approved_outflow_usd NUMERIC(15,2) NOT NULL CHECK (approved_outflow_usd > 0),
    approved_outflow_cny NUMERIC(15,2) NOT NULL CHECK (approved_outflow_cny > 0),
    bri_strategic_priority VARCHAR(60) NOT NULL,
    approval_date DATE NOT NULL,
    FOREIGN KEY (chinese_investor_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 52. cn_green_manufacturing_esg_audits
CREATE TABLE IF NOT EXISTS cn_green_manufacturing_esg_audits (
    audit_record_id INTEGER PRIMARY KEY,
    facility_id INTEGER NOT NULL,
    reporting_year SMALLINT NOT NULL,
    annual_coal_power_mwh NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    annual_renewable_power_mwh NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    scope1_direct_emissions_tco2 NUMERIC(12,3) NOT NULL,
    scope2_indirect_emissions_tco2 NUMERIC(12,3) NOT NULL,
    carbon_tax_paid_in_china_cny_per_ton NUMERIC(8,2) NOT NULL DEFAULT 0.00,
    verified_by_cnas_body VARCHAR(100) NOT NULL,
    FOREIGN KEY (facility_id) REFERENCES cn_factory_production_facilities(facility_id)
);

-- ============================================================================
-- EXPANDED GRANULAR END-TO-END TABLES (TABLES 91 TO 108)
-- Upstream Traceability, UCP600 Trade Finance, NVOCC Packing, Processing Trade,
-- AEO MRA, Dual-Use Controls, CCPIT Origin, MOFCOM Quotas & Post-Clearance
-- ============================================================================

-- 91. cn_raw_materials_tier2_suppliers
CREATE TABLE IF NOT EXISTS cn_raw_materials_tier2_suppliers (
    supplier_tier2_id VARCHAR(28) PRIMARY KEY,
    supplier_uscc CHAR(18) NOT NULL UNIQUE,
    supplier_name_en VARCHAR(180) NOT NULL,
    admin_division_code_gb CHAR(6) NOT NULL,
    raw_material_category VARCHAR(80) NOT NULL CHECK (
        raw_material_category IN (
            'Battery Grade Lithium Carbonate',
            'Anode Spherical Graphite',
            'Cathode LFP Precursor',
            'Solar Grade Polysilicon',
            'Rare Earth Neodymium Magnets',
            'Automotive Grade Steel Coil'
        )
    ),
    mine_or_refinery_location VARCHAR(150) NOT NULL,
    annual_supply_capacity_tons NUMERIC(12,2) NOT NULL CHECK (annual_supply_capacity_tons > 0),
    eu_battery_passport_verified BOOLEAN NOT NULL DEFAULT 1,
    carbon_footprint_kgco2_per_kg NUMERIC(8,3) NOT NULL,
    FOREIGN KEY (admin_division_code_gb) REFERENCES cn_provinces_prefectures_cities(admin_division_code_gb)
);

-- 92. cn_production_lots_batch_genealogy
CREATE TABLE IF NOT EXISTS cn_production_lots_batch_genealogy (
    batch_lot_number VARCHAR(40) PRIMARY KEY,
    product_sku_cn VARCHAR(35) NOT NULL,
    facility_id INTEGER NOT NULL,
    supplier_tier2_id VARCHAR(28) NOT NULL,
    production_timestamp_start TIMESTAMP NOT NULL,
    production_shift_code VARCHAR(20) NOT NULL,
    units_manufactured INTEGER NOT NULL CHECK (units_manufactured > 0),
    eol_quality_pass_rate_pct NUMERIC(5,2) NOT NULL CHECK (eol_quality_pass_rate_pct BETWEEN 0 AND 100),
    serial_range_prefix VARCHAR(45) NOT NULL,
    FOREIGN KEY (product_sku_cn) REFERENCES cn_products_industrial_catalog(product_sku_cn),
    FOREIGN KEY (facility_id) REFERENCES cn_factory_production_facilities(facility_id),
    FOREIGN KEY (supplier_tier2_id) REFERENCES cn_raw_materials_tier2_suppliers(supplier_tier2_id)
);

-- 93. cn_bill_of_materials_bom_structures
CREATE TABLE IF NOT EXISTS cn_bill_of_materials_bom_structures (
    bom_component_id VARCHAR(30) PRIMARY KEY,
    product_sku_cn VARCHAR(35) NOT NULL,
    supplier_tier2_id VARCHAR(28) NOT NULL,
    component_name_en VARCHAR(150) NOT NULL,
    component_hs6_code CHAR(6) NOT NULL,
    quantity_per_unit_jin NUMERIC(10,3) NOT NULL CHECK (quantity_per_unit_jin > 0),
    domestic_value_added_share_pct NUMERIC(5,2) NOT NULL CHECK (domestic_value_added_share_pct BETWEEN 0 AND 100),
    critical_raw_material_flag BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (product_sku_cn) REFERENCES cn_products_industrial_catalog(product_sku_cn),
    FOREIGN KEY (supplier_tier2_id) REFERENCES cn_raw_materials_tier2_suppliers(supplier_tier2_id)
);

-- 94. cn_letters_of_credit_ucp600_swift
CREATE TABLE IF NOT EXISTS cn_letters_of_credit_ucp600_swift (
    lc_number_swift VARCHAR(32) PRIMARY KEY,
    contract_no_cn VARCHAR(32) NOT NULL,
    issuing_bank_bic VARCHAR(15) NOT NULL,
    advising_bank_bic VARCHAR(15) NOT NULL,
    applicant_eori_or_uscc VARCHAR(25) NOT NULL,
    beneficiary_uscc_or_eori VARCHAR(25) NOT NULL,
    lc_currency CHAR(3) NOT NULL CHECK (lc_currency IN ('EUR', 'USD', 'CNY')),
    lc_face_amount NUMERIC(15,2) NOT NULL CHECK (lc_face_amount > 0),
    swift_mt_type VARCHAR(15) NOT NULL CHECK (swift_mt_type IN ('MT700 Issue', 'MT707 Amend', 'MT710 Advise')),
    latest_shipment_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    ucp600_confirmation_status VARCHAR(30) NOT NULL CHECK (
        ucp600_confirmation_status IN ('Confirmed Irrevocable', 'Unconfirmed Irrevocable', 'Transferable LC')
    ),
    FOREIGN KEY (contract_no_cn) REFERENCES cn_b2b_commercial_contracts(contract_no_cn)
);

-- 95. cn_lc_documentary_presentations_discrepancies
CREATE TABLE IF NOT EXISTS cn_lc_documentary_presentations_discrepancies (
    presentation_id VARCHAR(30) PRIMARY KEY,
    lc_number_swift VARCHAR(32) NOT NULL,
    invoice_no VARCHAR(32) NOT NULL,
    presented_bl_or_awb VARCHAR(35) NOT NULL,
    presentation_date DATE NOT NULL,
    discrepancy_found BOOLEAN NOT NULL DEFAULT 0,
    discrepancy_description VARCHAR(200) NOT NULL,
    mt750_advice_status VARCHAR(40) NOT NULL CHECK (
        mt750_advice_status IN ('Clean Presentation - Honored', 'Discrepant - Waived by Applicant', 'Under Bank Examination')
    ),
    settlement_maturity_date DATE NOT NULL,
    FOREIGN KEY (lc_number_swift) REFERENCES cn_letters_of_credit_ucp600_swift(lc_number_swift),
    FOREIGN KEY (invoice_no) REFERENCES cn_commercial_invoices(invoice_no)
);

-- 96. cn_hk_macao_offshore_trading_intermediaries
CREATE TABLE IF NOT EXISTS cn_hk_macao_offshore_trading_intermediaries (
    offshore_trade_id VARCHAR(30) PRIMARY KEY,
    intermediary_reg_no VARCHAR(30) NOT NULL,
    intermediary_name VARCHAR(180) NOT NULL,
    jurisdiction_sar VARCHAR(25) NOT NULL CHECK (
        jurisdiction_sar IN ('Hong Kong SAR', 'Macao SAR', 'Hengqin Offshore Zone')
    ),
    mainland_manufacturer_uscc CHAR(18) NOT NULL,
    contract_no_cn VARCHAR(32) NOT NULL,
    onshore_settlement_cny NUMERIC(15,2) NOT NULL CHECK (onshore_settlement_cny > 0),
    offshore_invoiced_eur_usd NUMERIC(15,2) NOT NULL CHECK (offshore_invoiced_eur_usd > 0),
    cnh_offshore_clearing_bank VARCHAR(100) NOT NULL,
    FOREIGN KEY (mainland_manufacturer_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (contract_no_cn) REFERENCES cn_b2b_commercial_contracts(contract_no_cn)
);

-- 97. cn_freight_forwarders_nvocc_customs_brokers
CREATE TABLE IF NOT EXISTS cn_freight_forwarders_nvocc_customs_brokers (
    broker_forwarder_id VARCHAR(28) PRIMARY KEY,
    broker_uscc CHAR(18) NOT NULL UNIQUE,
    company_name_en VARCHAR(180) NOT NULL,
    gacc_broker_license_no VARCHAR(30) NOT NULL,
    mot_nvocc_registration_no VARCHAR(30) NOT NULL,
    primary_port_unlocode CHAR(5) NOT NULL,
    aeo_broker_tier VARCHAR(35) NOT NULL CHECK (
        aeo_broker_tier IN ('Advanced Certified Broker', 'General Certified Broker')
    ),
    active_poa_clients_count INTEGER NOT NULL CHECK (active_poa_clients_count > 0)
);

-- 98. cn_packing_lists_pallet_carton_details
CREATE TABLE IF NOT EXISTS cn_packing_lists_pallet_carton_details (
    packing_list_id VARCHAR(32) PRIMARY KEY,
    invoice_no VARCHAR(32) NOT NULL,
    broker_forwarder_id VARCHAR(28) NOT NULL,
    packaging_unit_type VARCHAR(40) NOT NULL CHECK (
        packaging_unit_type IN (
            'Fumigated Euro Pallet ISPM-15',
            'Heavy Duty Steel Skid',
            'Export Corrugated Master Carton',
            'Reefer Insulated Wine Case',
            'Bulk Kraft Pulp Bale'
        )
    ),
    total_pallets_or_skids INTEGER NOT NULL CHECK (total_pallets_or_skids > 0),
    total_packages_cartons INTEGER NOT NULL CHECK (total_packages_cartons > 0),
    total_net_weight_jin NUMERIC(14,3) NOT NULL CHECK (total_net_weight_jin > 0),
    total_gross_weight_jin NUMERIC(14,3) NOT NULL CHECK (total_gross_weight_jin >= total_net_weight_jin),
    total_volume_cbm NUMERIC(10,3) NOT NULL CHECK (total_volume_cbm > 0),
    shipping_marks_stencil VARCHAR(180) NOT NULL,
    FOREIGN KEY (invoice_no) REFERENCES cn_commercial_invoices(invoice_no),
    FOREIGN KEY (broker_forwarder_id) REFERENCES cn_freight_forwarders_nvocc_customs_brokers(broker_forwarder_id)
);

-- 99. cn_processing_trade_manuals_handbook
CREATE TABLE IF NOT EXISTS cn_processing_trade_manuals_handbook (
    e_manual_handbook_no CHAR(12) PRIMARY KEY,
    operating_enterprise_uscc CHAR(18) NOT NULL,
    zone_id INTEGER NOT NULL,
    supervision_mode_code CHAR(4) NOT NULL CHECK (supervision_mode_code IN ('0615', '0214', '5034', '1234')),
    imported_raw_material_hs10 CHAR(10) NOT NULL,
    exported_finished_product_hs10 CHAR(10) NOT NULL,
    unit_consumption_ratio NUMERIC(8,4) NOT NULL CHECK (unit_consumption_ratio > 0),
    bonded_duty_suspended_cny NUMERIC(14,2) NOT NULL CHECK (bonded_duty_suspended_cny >= 0),
    verification_writeoff_status VARCHAR(35) NOT NULL CHECK (
        verification_writeoff_status IN ('Active Open Manual', 'Verified & Written Off', 'Pending Bonded Balancing')
    ),
    FOREIGN KEY (operating_enterprise_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (zone_id) REFERENCES cn_special_economic_ftz_zones(zone_id),
    FOREIGN KEY (exported_finished_product_hs10) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 100. cn_gacc_aeo_mutual_recognition_registry
CREATE TABLE IF NOT EXISTS cn_gacc_aeo_mutual_recognition_registry (
    aeo_mra_certificate_no VARCHAR(32) PRIMARY KEY,
    chinese_enterprise_uscc CHAR(18) NOT NULL,
    eu_partner_eori_pt VARCHAR(20) NOT NULL,
    mra_agreement_code VARCHAR(30) NOT NULL DEFAULT 'CN-EU-AEO-MRA-2014',
    reduced_inspection_rate_pct NUMERIC(5,2) NOT NULL CHECK (reduced_inspection_rate_pct BETWEEN 0 AND 20),
    priority_clearance_lane BOOLEAN NOT NULL DEFAULT 1,
    last_gacc_reaudit_date DATE NOT NULL,
    valid_until_date DATE NOT NULL,
    FOREIGN KEY (chinese_enterprise_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 101. cn_export_control_dual_use_mofcom_permits
CREATE TABLE IF NOT EXISTS cn_export_control_dual_use_mofcom_permits (
    dual_use_permit_no VARCHAR(32) PRIMARY KEY,
    exporter_uscc CHAR(18) NOT NULL,
    gacc_entry_id_18 CHAR(18) NOT NULL,
    control_list_item_code VARCHAR(25) NOT NULL,
    controlled_substance_or_tech VARCHAR(150) NOT NULL,
    end_user_pt_eori VARCHAR(20) NOT NULL,
    end_use_statement_verified BOOLEAN NOT NULL DEFAULT 1,
    approval_authority VARCHAR(80) NOT NULL,
    issue_date DATE NOT NULL,
    FOREIGN KEY (exporter_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (gacc_entry_id_18) REFERENCES cn_customs_export_declarations_gacc(gacc_entry_id_18)
);

-- 102. cn_preferential_certificates_of_origin_ccpit
CREATE TABLE IF NOT EXISTS cn_preferential_certificates_of_origin_ccpit (
    co_certificate_no VARCHAR(32) PRIMARY KEY,
    gacc_entry_id_18 CHAR(18) NOT NULL,
    exporter_uscc CHAR(18) NOT NULL,
    co_type VARCHAR(45) NOT NULL CHECK (
        co_type IN ('Non-Preferential CO CCPIT', 'GACC General Certificate of Origin', 'Macao CEPA Origin Certificate')
    ),
    origin_criterion VARCHAR(35) NOT NULL CHECK (
        origin_criterion IN ('WO - Wholly Obtained', 'PE - Produced Exclusively', 'PSR - Substantial Transformation')
    ),
    regional_value_content_pct NUMERIC(5,2) NOT NULL CHECK (regional_value_content_pct BETWEEN 0 AND 100),
    issuing_chamber_branch VARCHAR(100) NOT NULL,
    qr_verification_hash VARCHAR(64) NOT NULL,
    FOREIGN KEY (gacc_entry_id_18) REFERENCES cn_customs_export_declarations_gacc(gacc_entry_id_18),
    FOREIGN KEY (exporter_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 103. cn_customs_tariff_quotas_antidumping_mofcom
CREATE TABLE IF NOT EXISTS cn_customs_tariff_quotas_antidumping_mofcom (
    measure_record_id VARCHAR(30) PRIMARY KEY,
    hs_code_10_cn CHAR(10) NOT NULL,
    gacc_import_id_18 CHAR(18) NOT NULL,
    mofcom_announcement_no VARCHAR(40) NOT NULL,
    measure_type VARCHAR(55) NOT NULL CHECK (
        measure_type IN (
            'EU Pork Anti-Dumping Investigation Deposit',
            'EU Brandy Provisional Security Deposit',
            'Agricultural Tariff Rate Quota TRQ',
            'MFN Standard Zero Measure'
        )
    ),
    applicable_deposit_or_quota_rate_pct NUMERIC(5,2) NOT NULL CHECK (applicable_deposit_or_quota_rate_pct >= 0),
    security_deposit_collected_cny NUMERIC(14,2) NOT NULL DEFAULT 0.00,
    cooperating_exporter_pt_eori VARCHAR(20) NOT NULL,
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn),
    FOREIGN KEY (gacc_import_id_18) REFERENCES cn_customs_import_declarations_gacc(gacc_import_id_18)
);

-- 104. cn_customs_tax_guarantees_consolidated_bonds
CREATE TABLE IF NOT EXISTS cn_customs_tax_guarantees_consolidated_bonds (
    guarantee_bond_no VARCHAR(32) PRIMARY KEY,
    enterprise_uscc CHAR(18) NOT NULL,
    guarantor_bank_or_insurer VARCHAR(100) NOT NULL,
    guarantee_mode VARCHAR(50) NOT NULL CHECK (
        guarantee_mode IN ('Consolidated Monthly Taxation Bond', 'Transit Customs Bond', 'Anti-Dumping Provisional Security Bond')
    ),
    bond_limit_cny NUMERIC(15,2) NOT NULL CHECK (bond_limit_cny > 0),
    utilized_amount_cny NUMERIC(15,2) NOT NULL CHECK (utilized_amount_cny >= 0),
    beneficiary_customs_district CHAR(4) NOT NULL,
    expiry_date DATE NOT NULL,
    FOREIGN KEY (enterprise_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 105. cn_advance_rulings_classification_valuation_gacc
CREATE TABLE IF NOT EXISTS cn_advance_rulings_classification_valuation_gacc (
    ruling_decision_no VARCHAR(32) PRIMARY KEY,
    applicant_uscc CHAR(18) NOT NULL,
    ruling_category VARCHAR(45) NOT NULL CHECK (
        ruling_category IN ('Tariff Classification HS10', 'Origin Determination', 'Customs Valuation Methodology')
    ),
    confirmed_hs_code_10_cn CHAR(10) NOT NULL,
    product_commercial_description VARCHAR(200) NOT NULL,
    issuing_gacc_customs_house VARCHAR(80) NOT NULL,
    effective_date DATE NOT NULL,
    valid_for_years SMALLINT NOT NULL DEFAULT 3,
    FOREIGN KEY (applicant_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code),
    FOREIGN KEY (confirmed_hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 106. cn_post_clearance_audits_anti_smuggling_gacc
CREATE TABLE IF NOT EXISTS cn_post_clearance_audits_anti_smuggling_gacc (
    pca_audit_case_no VARCHAR(32) PRIMARY KEY,
    audited_enterprise_uscc CHAR(18) NOT NULL,
    target_declaration_id_18 CHAR(18) NOT NULL,
    audit_bureau_division VARCHAR(80) NOT NULL,
    audit_focus_area VARCHAR(60) NOT NULL CHECK (
        audit_focus_area IN (
            'Transfer Pricing & Royalties Valuation',
            'Export VAT Rebate Authenticity',
            'HS Code Misclassification Check',
            'CIFER Cold-Chain Traceability'
        )
    ),
    audit_outcome VARCHAR(45) NOT NULL CHECK (
        audit_outcome IN ('Compliant - No Adjustment', 'Supplementary Tax Assessed', 'Voluntary Disclosure Accepted')
    ),
    supplementary_tax_or_fine_cny NUMERIC(12,2) NOT NULL DEFAULT 0.00,
    audit_closing_date DATE NOT NULL,
    FOREIGN KEY (audited_enterprise_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);

-- 107. cn_excise_consumption_tax_sta
CREATE TABLE IF NOT EXISTS cn_excise_consumption_tax_sta (
    consumption_tax_id VARCHAR(30) PRIMARY KEY,
    gacc_import_id_18 CHAR(18) NOT NULL,
    hs_code_10_cn CHAR(10) NOT NULL,
    taxable_category_zh_en VARCHAR(100) NOT NULL,
    ad_valorem_rate_pct NUMERIC(5,2) NOT NULL CHECK (ad_valorem_rate_pct >= 0),
    specific_duty_per_unit_cny NUMERIC(8,2) NOT NULL DEFAULT 0.00,
    assessed_consumption_tax_cny NUMERIC(12,2) NOT NULL CHECK (assessed_consumption_tax_cny >= 0),
    sta_tax_receipt_no VARCHAR(35) NOT NULL UNIQUE,
    FOREIGN KEY (gacc_import_id_18) REFERENCES cn_customs_import_declarations_gacc(gacc_import_id_18),
    FOREIGN KEY (hs_code_10_cn) REFERENCES cn_hs_tariff_schedule_gacc(hs_code_10_cn)
);

-- 108. cn_ipr_customs_protection_recordations
CREATE TABLE IF NOT EXISTS cn_ipr_customs_protection_recordations (
    ipr_recordation_no VARCHAR(30) PRIMARY KEY,
    right_holder_uscc_or_eori VARCHAR(25) NOT NULL,
    brand_or_patent_name VARCHAR(120) NOT NULL,
    ipr_type VARCHAR(45) NOT NULL CHECK (
        ipr_type IN ('Registered Trademark CNIPA', 'Invention Patent CNIPA', 'Geographical Indication GI Douro/Porto')
    ),
    cnipa_registration_no VARCHAR(35) NOT NULL,
    authorized_exporters_importers_list VARCHAR(255) NOT NULL,
    border_enforcement_status VARCHAR(35) NOT NULL CHECK (
        border_enforcement_status IN ('Active Border Protection', 'Detention Triggered', 'White-Listed Authorized Channel')
    ),
    valid_until_date DATE NOT NULL
);

-- Indexes for high-performance query execution and P2 Virtual Data Integration joins
CREATE INDEX IF NOT EXISTS idx_cn_hs_wco6 ON cn_hs_tariff_schedule_gacc(hs_code_6_wco);
CREATE INDEX IF NOT EXISTS idx_cn_contracts_pt_eori ON cn_b2b_commercial_contracts(portuguese_counterparty_eori);
CREATE INDEX IF NOT EXISTS idx_cn_export_bl ON cn_customs_export_declarations_gacc(bill_of_lading_or_waybill_no);
CREATE INDEX IF NOT EXISTS idx_cn_import_bl ON cn_customs_import_declarations_gacc(bill_of_lading_no);
CREATE INDEX IF NOT EXISTS idx_cn_fx_uetr ON cn_fx_settlements_pboc_safe(swift_uetr_or_cips_id);
CREATE INDEX IF NOT EXISTS idx_cn_fdi_pt_nif ON cn_outward_fdi_approvals_ndrc(target_pt_company_nif);
CREATE INDEX IF NOT EXISTS idx_cn_lc_contract ON cn_letters_of_credit_ucp600_swift(contract_no_cn);
CREATE INDEX IF NOT EXISTS idx_cn_packing_inv ON cn_packing_lists_pallet_carton_details(invoice_no);
CREATE INDEX IF NOT EXISTS idx_cn_aeo_pt_eori ON cn_gacc_aeo_mutual_recognition_registry(eu_partner_eori_pt);
