-- =============================================================================
-- UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
-- Modelação e Integração de Dados (DMI) - Projeto P1
-- Subtópico China: Vistas SQL Relacionais (Views em 3.ª Forma Normal)
-- Autor: David Rodrigues
-- =============================================================================

-- 1. Vista de Desalfandegamento Aduaneiro de Exportação da China para Portugal
DROP VIEW IF EXISTS vw_desalfandegamento_exportacao_china;
CREATE VIEW vw_desalfandegamento_exportacao_china AS
SELECT 
    d.gacc_entry_id_18,
    date(d.declaration_date_epoch, 'unixepoch') AS data_declaracao,
    e.company_name_zh AS exportador_nome_zh,
    e.company_name_en AS exportador_nome_en,
    d.exporter_uscc,
    i.buyer_pt_eori,
    d.customs_port_code_cn,
    d.port_of_discharge_unlocode,
    d.transport_mode_code,
    d.vessel_imo_or_train_no,
    d.supervision_regime_code,
    d.clearance_channel,
    d.total_fob_value_cny,
    d.total_fob_value_usd,
    i.total_invoice_value,
    i.invoice_currency,
    COALESCE(r.rebate_amount_paid_cny, 0) AS reembolso_iva_sta_cny,
    COALESCE(r.sta_approval_status, 'NÃO_SUBMETIDO') AS estado_reembolso_iva
FROM cn_customs_export_declarations_gacc d
JOIN cn_enterprises_manufacturers e ON d.exporter_uscc = e.uscc_code
JOIN cn_commercial_invoices i ON d.invoice_no = i.invoice_no
LEFT JOIN cn_vat_export_tax_rebates_sta r ON d.gacc_entry_id_18 = r.gacc_entry_id_18;

-- 2. Vista da Balança Comercial Bilateral (Fluxo Exportação China -> PT e Importação China <- PT)
DROP VIEW IF EXISTS vw_balanca_comercial_bilateral_cn_pt;
CREATE VIEW vw_balanca_comercial_bilateral_cn_pt AS
SELECT 
    'EXPORT_CN_TO_PT' AS fluxo_direcao,
    d.gacc_entry_id_18 AS id_declaracao,
    date(d.declaration_date_epoch, 'unixepoch') AS data_operacao,
    d.exporter_uscc AS operador_origem,
    e.company_name_en AS operador_origem_nome,
    i.buyer_pt_eori AS operador_destino,
    d.port_of_discharge_unlocode AS porto_destino,
    d.total_fob_value_usd AS valor_fob_usd,
    d.total_fob_value_cny AS valor_cny,
    d.clearance_channel AS canal_despacho
FROM cn_customs_export_declarations_gacc d
JOIN cn_enterprises_manufacturers e ON d.exporter_uscc = e.uscc_code
JOIN cn_commercial_invoices i ON d.invoice_no = i.invoice_no

UNION ALL

SELECT 
    'IMPORT_CN_FROM_PT' AS fluxo_direcao,
    imp.gacc_import_id_18 AS id_declaracao,
    imp.declaration_date AS data_operacao,
    imp.portuguese_exporter_nif_eori AS operador_origem,
    'Exportador Nacional (Vinho/Cortiça/Azeite)' AS operador_origem_nome,
    imp.importer_cn_uscc AS operador_destino,
    imp.customs_entry_port_cn AS porto_destino,
    ROUND(imp.cif_value_cny / 7.22, 2) AS valor_fob_usd,
    imp.cif_value_cny AS valor_cny,
    'GREEN_CUSTOMS_CLEARANCE' AS canal_despacho
FROM cn_customs_import_declarations_gacc imp;

-- 3. Vista de Inspeções Sanitárias e Fitossanitárias CIQ/GACC e Conformidade CIFER
DROP VIEW IF EXISTS vw_inspecoes_sanitarias_ciq_cifer;
CREATE VIEW vw_inspecoes_sanitarias_ciq_cifer AS
SELECT 
    ciq.ciq_inspection_id,
    ciq.gacc_declaration_id_18,
    ciq.inspection_direction,
    ciq.ciq_bureau_branch,
    ciq.sample_lab_test_code,
    ciq.pesticide_or_heavy_metal_ppm,
    CASE WHEN ciq.wood_packaging_ispm15_compliant = 1 THEN 'CONFORME_ISPM15' ELSE 'NÃO_CONFORME' END AS embalagem_madeira_ispm15,
    CASE WHEN ciq.chinese_labeling_compliant = 1 THEN 'ROTULAGEM_CONFORME' ELSE 'ROTULAGEM_IRREGULAR' END AS rotulagem_mandarim_gacc,
    ciq.e_ciq_certificate_no,
    ciq.inspection_verdict
FROM cn_ciq_inspection_quarantine_records ciq;

-- 4. Vista de Liquidação Cambial Bancária Transfronteiriça PBOC/SAFE (SWIFT & CIPS)
DROP VIEW IF EXISTS vw_liquidacao_cambial_forex_safe;
CREATE VIEW vw_liquidacao_cambial_forex_safe AS
SELECT 
    fx.safe_verification_no,
    fx.swift_uetr_or_cips_id,
    fx.invoice_no,
    ent.company_name_en AS empresa_chinesa_nome,
    fx.chinese_entity_uscc,
    fx.portuguese_entity_nif,
    fx.chinese_bank_name,
    fx.settlement_channel,
    fx.original_currency,
    fx.settled_foreign_amount,
    fx.settled_rmb_cny_amount,
    fx.pboc_central_parity_rate,
    fx.settlement_date
FROM cn_fx_settlements_pboc_safe fx
JOIN cn_enterprises_manufacturers ent ON fx.chinese_entity_uscc = ent.uscc_code;

-- 5. Vista de Operadores Económicos Chineses AEO e Acordo de Reconhecimento Mútuo MRA com a UE
DROP VIEW IF EXISTS vw_operadores_economicos_aeo_confianca;
CREATE VIEW vw_operadores_economicos_aeo_confianca AS
SELECT 
    ent.uscc_code,
    ent.customs_cr_code_10,
    ent.company_name_zh,
    ent.company_name_en,
    ent.ownership_type,
    ent.aeo_customs_tier,
    ent.registered_capital_wan_cny,
    COALESCE(mra.aeo_mra_certificate_no, 'NÃO_APLICÁVEL') AS certificado_mra_eu_pt,
    COALESCE(mra.eu_partner_eori_pt, '-') AS parceiro_pt_privilegiado,
    COALESCE(mra.reduced_inspection_rate_pct, 0) AS taxa_inspecao_reduzida_pct,
    COALESCE(mra.priority_clearance_lane, 0) AS canal_verde_prioritario
FROM cn_enterprises_manufacturers ent
LEFT JOIN cn_gacc_aeo_mutual_recognition_registry mra ON ent.uscc_code = mra.chinese_enterprise_uscc;

-- 6. Vista de Auditorias Industriais ESG e Descarbonização CBAM
DROP VIEW IF EXISTS vw_auditoria_esg_cbam_descarbonizacao;
CREATE VIEW vw_auditoria_esg_cbam_descarbonizacao AS
SELECT 
    audit.audit_record_id,
    fac.facility_name,
    ent.company_name_en AS empresa_titular,
    audit.reporting_year,
    audit.annual_renewable_power_mwh,
    audit.annual_coal_power_mwh,
    ROUND((audit.annual_renewable_power_mwh * 100.0) / (audit.annual_renewable_power_mwh + audit.annual_coal_power_mwh), 1) AS percentagem_energia_verde,
    audit.scope1_direct_emissions_tco2,
    audit.scope2_indirect_emissions_tco2,
    audit.carbon_tax_paid_in_china_cny_per_ton,
    audit.verified_by_cnas_body
FROM cn_green_manufacturing_esg_audits audit
JOIN cn_factory_production_facilities fac ON audit.facility_id = fac.facility_id
JOIN cn_enterprises_manufacturers ent ON fac.uscc_code = ent.uscc_code;
