-- =============================================================================
-- CHINA GACC & MOFCOM 3NF RELATIONAL DATABASE DUMP (POSTGRESQL / SQLITE)
-- MSc in Informatics Engineering - Data Modelling & Integration (DMI)
-- Student: David Rodrigues (2026/2027)
-- =============================================================================

BEGIN TRANSACTION;
CREATE TABLE cn_advance_rulings_classification_valuation_gacc (
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
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-SH-2025-0101','91320413MA1M9Y2C4B','Tariff Classification HS10','8507600090','Integrated LFP Liquid-Cooled Prismatic Battery Module with BMS Slave Board','Shanghai Customs Classification Center','2025-06-01',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-SZ-2025-0202','91440300192317458F','Tariff Classification HS10','8703800010','Dual-Motor All-Wheel-Drive Passenger BEV with CTB Blade Battery Architecture','Shenzhen Customs Tariff Division','2025-07-15',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-SH-2025-0303','91110000101123456N','Customs Valuation Methodology','2204210000','Deductive & Transaction Value Ruling for Symington Port Wine Marketing Royalties','Shanghai Customs Valuation Bureau','2025-09-10',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-GZ-2025-0404','91440400MA56LUS01P','Origin Determination','1509200000','Portuguese Alentejo DOP Extra Virgin Olive Oil Bottled for Macao-Hengqin CEPA','Gongbei Customs Origin Office','2025-10-20',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-NB-2025-0505','91350900587527783P','Tariff Classification HS10','8507600090','Containerized 20ft Utility-Scale LFP BESS Outdoor Rack (Classified as Accumulator)','Ningbo Customs Classification Center','2025-11-05',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-SZ-2025-0606','91440300618837699Q','Tariff Classification HS10','8504403090','Three-Phase 100kW String PV Inverter with PID Recovery & Arc-Fault Circuit Interrupter','Shenzhen Customs Tariff Division','2025-12-12',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-QD-2026-0707','91370200163562681G','Origin Determination','4703290000','Wholly Obtained Portuguese Eucalyptus Globulus Bleached Kraft Pulp Bales','Qingdao Customs Tariff & Origin Bureau','2026-01-18',3);
INSERT INTO "cn_advance_rulings_classification_valuation_gacc" VALUES('RUL-GACC-BJ-2026-0808','911100007178071858','Tariff Classification HS10','8607191000','Complete Motorized Metro Bogie Sub-Assembly with Pneumatic Suspension','Beijing Customs Tariff Division','2026-02-05',3);
CREATE TABLE cn_b2b_commercial_contracts (
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
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-001','91320413MA1M9Y2C4B','PT517890123','CALB Portugal - Fábrica de Baterias de Sines, S.A.','CN_EXPORT_TO_PT','2026-01-15','CIF','EUR',18500000,'LC_AT_SIGHT','Macau WTC');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-002','91440300192317458F','PT500234567','Salvador Caetano Auto - Importação e Distribuição, S.A.','CN_EXPORT_TO_PT','2026-01-22','CIF','EUR',28320000,'30_TT_70_BL','CIETAC Beijing');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-003','91610132724912345X','PT500697256','EDP Renováveis & Energia Solar Portugal, S.A.','CN_EXPORT_TO_PT','2026-02-05','FOB','USD',7280000,'LC_AT_SIGHT','SHIAC Shanghai');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-004','91350900587527783P','PT503412890','REN - Redes Energéticas Nacionais, SGPS, S.A.','CN_EXPORT_TO_PT','2026-02-18','CIF','EUR',10260000,'LC_AT_SIGHT','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-005','91110108551385082Q','PT500246810','Worten - Equipamentos para o Lar, S.A. (Grupo Sonae)','CN_EXPORT_TO_PT','2026-03-01','CIP','EUR',4850000,'OA_60_DAYS','SHIAC Shanghai');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-006','91330200778899112T','PT500191827','Mota-Engil Engenharia e Construção, S.A.','CN_EXPORT_TO_PT','2026-03-10','CIF','USD',5425000,'30_TT_70_BL','CIETAC Beijing');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-007','91330782098765432W','PT504998877','Varziela Chinarte - Centro Grossista de Vila do Conde, Lda.','CN_EXPORT_TO_PT','2026-03-18','FOB','CNY',14250000,'30_TT_70_BL','Macau WTC');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-008','91110000101123456N','PT500265432','Symington Family Estates - Vinhos do Douro e Porto, S.A.','CN_IMPORT_FROM_PT','2026-02-12','FOB','EUR',3450000,'LC_AT_SIGHT','Macau WTC');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-009','91110000101123456N','PT500077889','Corticeira Amorim, SGPS, S.A.','CN_IMPORT_FROM_PT','2026-02-25','CIF','EUR',4120000,'OA_60_DAYS','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-010','91440400MA56LUS01P','PT500112233','Sovena Consumer Goods - Azeites de Portugal, S.A.','CN_IMPORT_FROM_PT','2026-03-08','CIF','EUR',2680000,'LC_AT_SIGHT','Macau WTC');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-011','91110000101123456N','PT508112244','Maporal - Matadouro de Porco Alentejano, S.A.','CN_IMPORT_FROM_PT','2026-03-15','CIF','EUR',4200000,'LC_AT_SIGHT','Macau WTC');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-012','91110000101123456N','PT500214890','Sogrape Vinhos, S.A.','CN_IMPORT_FROM_PT','2026-03-22','CIF','EUR',3100000,'LC_AT_SIGHT','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-013','91370200163562681G','PT500055214','The Navigator Company, S.A.','CN_IMPORT_FROM_PT','2026-03-28','CIF','EUR',6500000,'OA_60_DAYS','CIETAC Beijing');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-014','91440300618837699Q','PT500697256','EDP Renováveis, S.A.','CN_EXPORT_TO_PT','2026-04-02','CIF','EUR',4800000,'LC_AT_SIGHT','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-015','91110108551385082Q','PT500246810','Worten - Equipamentos para o Lar, S.A.','CN_EXPORT_TO_PT','2026-04-05','CIP','EUR',6200000,'OA_60_DAYS','SHIAC Shanghai');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-016','91440606190342599T','PT500246810','Worten - Equipamentos para o Lar, S.A.','CN_EXPORT_TO_PT','2026-04-10','CIF','EUR',3800000,'LC_AT_SIGHT','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-017','911100007178071858','PT503412890','REN - Redes Energéticas Nacionais, SGPS, S.A.','CN_EXPORT_TO_PT','2026-04-14','CIF','EUR',8500000,'LC_AT_SIGHT','CAC Lisboa');
INSERT INTO "cn_b2b_commercial_contracts" VALUES('CN-PT-CTR-2026-018','91440300192317458F','PT500234567','Salvador Caetano Auto, S.A.','CN_EXPORT_TO_PT','2026-04-18','CIF','EUR',18500000,'30_TT_70_BL','CIETAC Beijing');
CREATE TABLE cn_bill_of_materials_bom_structures (
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
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-CALB-314-01','CN-SKU-CALB-LFP314','SUP-T2-LI-001','Battery-Grade Lithium Carbonate Li2CO3 Cathode Active Salt','283691',24.5,38.4,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-CALB-314-02','CN-SKU-CALB-LFP314','SUP-T2-LFP-004','Iron Phosphate FePO4 Nano-Crystalline Precursor Powder','283529',68,29.1,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-CALB-314-03','CN-SKU-CALB-LFP314','SUP-T2-GR-003','Coated Spherical Artificial Anode Graphite Powder','380110',36.2,18.5,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-BYD-SEAL-01','CN-SKU-BYD-SEAL-EV','SUP-T2-LFP-004','BYD Blade LFP 82.5kWh Structural Battery Pack Assembly','850760',1120,42,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-BYD-SEAL-02','CN-SKU-BYD-SEAL-EV','SUP-T2-RE-006','Permanent Magnet Synchronous Hairpin Traction Motor 230kW','850153',185,19.8,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-BYD-SEAL-03','CN-SKU-BYD-SEAL-EV','SUP-T2-ST-007','Ultra-High-Strength Hot-Stamped Body-in-White Steel Frame','870829',1420,24.5,0);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-LONGI-PV-01','CN-SKU-LONGI-HIMO7','SUP-T2-SI-005','N-Type HPDC Monocrystalline Silicon Solar Wafers M10','381800',14.8,64.2,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-CATL-ESS-01','CN-SKU-CATL-ENERC','SUP-T2-LI-002','CATL 306Ah LFP Liquid-Cooled Cell Rack Cluster','850760',4850,71.5,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-HW-INV-01','CN-SKU-HW-SUN2000','SUP-T2-RE-006','IGBT Power Module & Neodymium Inductive Reactor Core','850490',62,58,1);
INSERT INTO "cn_bill_of_materials_bom_structures" VALUES('BOM-CRRC-BG-01','CN-SKU-CRRC-BOGIE','SUP-T2-ST-007','Forged Alloy Steel Railway Wheelset & Frame Assembly','860719',9800,82.4,0);
CREATE TABLE cn_cargo_insurance_policies_sinosure (
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
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('SINOSURE-2026-JS-1001','SINOSURE','CN-PT-CTR-2026-001','220120260000108801','Export Credit Risk SINOSURE',7300000,131400,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PICC-MAR-2026-SZ-1002','PICC Property & Casualty','CN-PT-CTR-2026-002','530120260000108802','Marine All Risks ICC-A',11260000,230400,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PINGAN-MAR-2026-ND-1004','Ping An Marine','CN-PT-CTR-2026-004','310120260000108804','Marine All Risks ICC-A',4080000,86400,1,185000);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PICC-RAIL-2026-YW-1007','PICC Property & Casualty','CN-PT-CTR-2026-007','292120260000108807','Railway Transit Risk',1085000,28500,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('SINOSURE-2026-SN-1003','SINOSURE','CN-PT-CTR-2026-003','220120260000108803','Export Credit Risk SINOSURE',4200000,75600,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PICC-MAR-2026-NB-1006','PICC Property & Casualty','CN-PT-CTR-2026-006','310120260000108806','Marine All Risks ICC-A',3200000,68000,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PINGAN-MAR-2026-SZ-1008','Ping An Marine','CN-PT-CTR-2026-014','530120260000108808','Marine All Risks ICC-A',2150000,43000,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('SINOSURE-2026-SZ-1013','SINOSURE','CN-PT-CTR-2026-018','530120260000108813','Export Credit Risk SINOSURE',10200000,183600,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PICC-AIR-2026-BJ-1005','PICC Property & Casualty','CN-PT-CTR-2026-005','010120260000108805','Marine All Risks ICC-A',2850000,39900,0,0);
INSERT INTO "cn_cargo_insurance_policies_sinosure" VALUES('PINGAN-MAR-2026-GZ-1010','Ping An Marine','CN-PT-CTR-2026-016','510120260000108810','Marine All Risks ICC-A',1680000,33600,0,0);
CREATE TABLE cn_ccc_compulsory_certifications (
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
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010907881201','CN-SKU-CALB-LFP314','91320413MA1M9Y2C4B','CQC - China Quality Certification Centre','GB 38031-2020 / UN38.3','2025-01-15','2030-01-14','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2024011101664420','CN-SKU-BYD-SEAL-EV','91440300192317458F','CCAP - China Certification Centre for Automotive','GB 18384-2020 / WVTA EU','2024-06-20','2029-06-19','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010907772103','CN-SKU-CATL-ENERC','91350900587527783P','CQC - China Quality Certification Centre','GB/T 36276-2023','2025-02-10','2030-02-09','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2024010305661004','CN-SKU-LONGI-HIMO7','91610132724912345X','CQC - China Quality Certification Centre','GB/T 9535 / IEC 61215','2024-06-20','2029-06-19','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010907553311','CN-SKU-HW-SUN2000','91440300618837699Q','CQC - China Quality Certification Centre','GB/T 37408 / EN 50549','2025-03-05','2030-03-04','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025011606998812','CN-SKU-XM-15PRO-5G','91110108551385082Q','CQC / SRRC Radio Type Approval','GB 4943.1-2022','2025-01-20','2030-01-19','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2024010805112234','CN-SKU-YW-APPAREL-LOT','91330782098765432W','CQC - China Quality Certification Centre','GB 18401-2010','2024-09-12','2029-09-11','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010907334415','CN-SKU-TRINA-VERTEX','91320400608131370B','CQC - China Quality Certification Centre','IEC 61215 / IEC 61730','2025-02-18','2030-02-17','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010703889922','CN-SKU-MIDEA-SPLIT','91440606190342599T','CQC - China Quality Certification Centre','GB 4706.32-2012 / EN 60335','2025-03-12','2030-03-11','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010703889923','CN-SKU-GREE-SPLIT','91440400192548256N','CQC - China Quality Certification Centre','GB 4706.32 / CE Mark','2025-03-15','2030-03-14','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2025010808554433','CN-SKU-HAIER-TV65','91370200163562681G','CQC - China Quality Certification Centre','GB 8898-2011 / RED Directive','2025-01-25','2030-01-24','Valid',1);
INSERT INTO "cn_ccc_compulsory_certifications" VALUES('2024011101664425','CN-SKU-BYD-ATTO3','91440300192317458F','CCAP - China Center for Automobile Product Certification','GB 18384-2020 / WVTA EU','2024-08-15','2029-08-14','Valid',1);
CREATE TABLE cn_ciq_inspection_quarantine_records (
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
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SH-001088','220120260000108801','Outbound Export Inspection','Shanghai CIQ','LAB-UN383-BAT-01',0.001,1,1,'ECIQ-CN20260320001','Pass - Certificate Issued','2026-03-21 10:30:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SZ-001089','530120260000108802','Outbound Export Inspection','Guangdong Shenzhen CIQ','LAB-EV-SAFETY-02',0.0005,1,1,'ECIQ-CN20260326002','Pass - Certificate Issued','2026-03-26 14:15:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SH-001090','220120260000108803','Outbound Export Inspection','Shanghai CIQ','LAB-PV-IEC-03',0,1,1,'ECIQ-CN20260402003','Pass - Certificate Issued','2026-04-02 09:45:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-NB-001091','310120260000108804','Outbound Export Inspection','Ningbo CIQ','LAB-HAZMAT-ESS-04',0.002,1,1,'ECIQ-CN20260410004','Pass - Certificate Issued','2026-04-10 16:40:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SH-009901','220120261000990001','Inbound Import Quarantine','Shanghai Waigaoqiao CIQ','LAB-WINE-SO2-01',0.012,1,1,'ECIQ-IM20260505101','Pass - Certificate Issued','2026-05-05 09:20:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SH-009902','220120261000990002','Inbound Import Quarantine','Shanghai Waigaoqiao CIQ','LAB-CORK-TCA-02',0.0002,1,1,'ECIQ-IM20260511102','Pass - Certificate Issued','2026-05-11 11:00:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-HQ-009903','530420261000990003','Inbound Import Quarantine','Zhuhai Hengqin CIQ','LAB-OLIVE-ACID-03',0.004,1,1,'ECIQ-IM20260519103','Pass - Certificate Issued','2026-05-19 15:10:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-QD-009905','220120261000990005','Inbound Import Quarantine','Shanghai Cold-Chain CIQ','LAB-SWINE-PCR-05',0.008,1,0,'ECIQ-IM20260527105','Labeling Rectification Ordered','2026-05-27 17:45:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SH-009906','220120261000990006','Inbound Import Quarantine','Shanghai Waigaoqiao CIQ','LAB-WINE-DOURO-06',0.001,1,1,'ECIQ-IM20260529106','Pass - Certificate Issued','2026-05-29 11:30:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-QD-009907','370220261000990007','Inbound Import Quarantine','Qingdao Dagang CIQ','LAB-WOOD-PULP-07',0,1,1,'ECIQ-IM20260531107','Pass - Certificate Issued','2026-05-31 14:20:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-SZ-001092','530120260000108808','Outbound Export Inspection','Shenzhen CIQ','LAB-EMC-5G-08',0,1,1,'ECIQ-CN20260503008','Pass - Certificate Issued','2026-05-03 10:15:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-BJ-001093','010120260000108809','Outbound Export Inspection','Beijing Capital CIQ','LAB-LITHIUM-AIR-09',0.0005,1,1,'ECIQ-CN20260505009','Pass - Certificate Issued','2026-05-05 13:40:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-GZ-001094','510120260000108810','Outbound Export Inspection','Guangzhou Nansha CIQ','LAB-HVAC-FGAS-10',0,1,1,'ECIQ-CN20260507010','Pass - Certificate Issued','2026-05-07 15:20:00');
INSERT INTO "cn_ciq_inspection_quarantine_records" VALUES('CIQ-2026-TJ-001095','010120260000108811','Outbound Export Inspection','Tianjin Port CIQ','LAB-METRO-BOGIE-11',0,1,1,'ECIQ-CN20260509011','Pass - Certificate Issued','2026-05-09 16:00:00');
CREATE TABLE cn_commercial_invoice_lines (
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
INSERT INTO "cn_commercial_invoice_lines" VALUES(1,'INV-CN-2026-8801',1,'CN-SKU-CALB-LFP314','8507600090','CALB L314Ah Zero-Carbon LFP Battery Pack Modules for Sines Assembly',10000,1760000,1840000,612,6120000,'LOT-CALB-2026-03A');
INSERT INTO "cn_commercial_invoice_lines" VALUES(2,'INV-CN-2026-8802',1,'CN-SKU-BYD-SEAL-EV','8703800010','BYD Seal AWD Electric Passenger Vehicles (EU Spec WVTA)',400,1748000,1780000,23600,9440000,'LOT-BYD-2026-03B');
INSERT INTO "cn_commercial_invoice_lines" VALUES(3,'INV-CN-2026-8803',1,'CN-SKU-LONGI-HIMO7','8541430000','LONGi Hi-MO 7 590W Bifacial Solar PV Modules for Alentejo Solar Park',50000,3250000,3420000,72.8,3640000,'LOT-LONGI-2026-04A');
INSERT INTO "cn_commercial_invoice_lines" VALUES(4,'INV-CN-2026-8804',1,'CN-SKU-CATL-ENERC','8507600090','CATL EnerC Plus Grid-Scale Battery Storage Containers for REN Grid',100,680000,710000,34200,3420000,'LOT-CATL-2026-04B');
INSERT INTO "cn_commercial_invoice_lines" VALUES(5,'INV-CN-2026-8805',1,'CN-SKU-XM-15PRO-5G','8517130000','Xiaomi 15 Pro 5G Smartphones PT/EU Retail Packaging',5000,2200,3100,485,2425000,'LOT-XM-2026-04C');
INSERT INTO "cn_commercial_invoice_lines" VALUES(6,'INV-CN-2026-8806',1,'CN-SKU-NB-STEEL-S355','7225409900','Ningbo S355J2 Structural Alloy Steel Plates for Sines Industrial Plant',2000,4000000,4020000,655,1310000,'LOT-NBST-2026-04D');
INSERT INTO "cn_commercial_invoice_lines" VALUES(7,'INV-CN-2026-8806',2,'CN-SKU-NB-ALU-6061','7606125900','Ningbo 6061-T6 Structural Aluminum Sheets (CBAM Regulated)',485.56,971120,985000,2770,1345000,'LOT-NBAL-2026-04E');
INSERT INTO "cn_commercial_invoice_lines" VALUES(8,'INV-CN-2026-8807',1,'CN-SKU-YW-APPAREL-LOT','6204620000','Yiwu Textile & Cotton Apparel Assortment Cartons via BRI Rail',2500,230000,248000,2850,7125000,'LOT-YIWU-2026-04F');
INSERT INTO "cn_commercial_invoice_lines" VALUES(9,'INV-PT-2026-9901',1,NULL,'2204210000','Symington Graham''s 20Y Tawny Port & Douro DOC Reserva Wine 750ml',120000,180000,336000,12.3333,1480000,'LOT-SH-SYM-2026A');
INSERT INTO "cn_commercial_invoice_lines" VALUES(10,'INV-PT-2026-9902',1,NULL,'4504900000','Amorim Natural Cork TwinTop Wine Stoppers Sterile Packed',15000000,135000,144000,0.1233,1850000,'LOT-SH-AMO-2026B');
INSERT INTO "cn_commercial_invoice_lines" VALUES(11,'INV-PT-2026-9903',1,NULL,'1509200000','Oliveira da Serra Extra Virgin Olive Oil Alentejo 750ml Bottles',180000,270000,296000,6.2222,1120000,'LOT-HQ-SOV-2026C');
INSERT INTO "cn_commercial_invoice_lines" VALUES(12,'INV-PT-2026-9905',1,NULL,'0203290090','Maporal Frozen Bone-in & Boneless Iberico Pork Cuts (Belly/Shoulder)',450000,900000,944000,3.5555,1600000,'LOT-TAO-MAP-2026D');
INSERT INTO "cn_commercial_invoice_lines" VALUES(13,'INV-PT-2026-9906',1,NULL,'2204210000','Sogrape Quinta da Leda Douro DOC & Grão Vasco Dão Red Wine 750ml',95000,142500,266000,13.0526,1240000,'LOT-SH-SOG-2026E');
INSERT INTO "cn_commercial_invoice_lines" VALUES(14,'INV-PT-2026-9904',1,NULL,'4703290000','The Navigator Company Bleached Eucalyptus Kraft Pulp (BEKP 500kg Bales)',4000,4000000,4040000,510,2040000,'LOT-QD-NAV-2026F');
INSERT INTO "cn_commercial_invoice_lines" VALUES(15,'INV-CN-2026-8808',1,'CN-SKU-HW-SUN2000','8504403090','Huawei FusionSolar Smart Inverters for EDP Alentejo Solar',800,147200,156000,2225,1780000,'LOT-HW-2026-05A');
INSERT INTO "cn_commercial_invoice_lines" VALUES(16,'INV-CN-2026-8809',1,'CN-SKU-XM-BOOKPRO','8471300000','Xiaomi Book Pro Laptops for Worten Back-to-School Campaign',4000,15200,22400,785,3140000,'LOT-XM-2026-05B');
INSERT INTO "cn_commercial_invoice_lines" VALUES(17,'INV-CN-2026-8810',1,'CN-SKU-MIDEA-SPLIT','8415102100','Midea Inverter Split Heat Pump Air Conditioners',5000,340000,370000,280,1400000,'LOT-MD-2026-05C');
INSERT INTO "cn_commercial_invoice_lines" VALUES(18,'INV-CN-2026-8811',1,'CN-SKU-CRRC-BOGIE','8607191000','CRRC Metro Bogies with Traction Motors for Lisbon Metro Expansion',80,1160000,1190000,50625,4050000,'LOT-CRRC-2026-05D');
INSERT INTO "cn_commercial_invoice_lines" VALUES(19,'INV-CN-2026-8813',1,'CN-SKU-BYD-ATTO3','8703800010','BYD Atto 3 Compact Electric SUVs for Salvador Caetano Distribution',350,1323000,1350000,24800,8680000,'LOT-BYD-2026-05E');
INSERT INTO "cn_commercial_invoice_lines" VALUES(20,'INV-CN-2026-8803',2,'CN-SKU-TRINA-VERTEX','8541430000','Trina Solar 700W Bifacial PV Panels for Hybrid Wind-Solar',20000,1440000,1520000,75,1500000,'LOT-TRN-2026-04G');
INSERT INTO "cn_commercial_invoice_lines" VALUES(21,'INV-CN-2026-8805',2,'CN-SKU-YW-TOYS-LOT','9503002100','Yiwu Intelligence Block Toy Assortment for Sonae Retail',10000,600000,640000,45,450000,'LOT-YW-2026-04H');
INSERT INTO "cn_commercial_invoice_lines" VALUES(22,'INV-CN-2026-8807',2,'CN-SKU-YW-APPAREL-LOT','6204620000','Yiwu Women''s Knitted Apparel B2B Lots via Rail',1500,138000,148000,2850,4275000,'LOT-YIWU-2026-04I');
INSERT INTO "cn_commercial_invoice_lines" VALUES(23,'INV-PT-2026-9901',2,NULL,'2204210000','Symington Cockburn''s Special Reserve Port Wine 750ml',60000,90000,168000,9.5,570000,'LOT-SH-SYM-2026G');
INSERT INTO "cn_commercial_invoice_lines" VALUES(24,'INV-PT-2026-9903',2,NULL,'1509200000','Sovena Andorinha Portuguese Cold-Pressed Olive Oil 500ml',120000,120000,135000,4.25,510000,'LOT-HQ-SOV-2026H');
INSERT INTO "cn_commercial_invoice_lines" VALUES(25,'INV-PT-2026-9905',2,NULL,'0203290090','Maporal Frozen Prime Iberico Pork Loins (Lombo de Porco Preto)',200000,400000,420000,4.1,820000,'LOT-TAO-MAP-2026I');
INSERT INTO "cn_commercial_invoice_lines" VALUES(26,'INV-CN-2026-8801',2,'CN-SKU-CALB-LFP314','8507600090','CALB L314Ah High-Capacity Energy Cell Spare Integration Units',1000,176000,184000,612,612000,'LOT-CALB-2026-03K');
CREATE TABLE cn_commercial_invoices (
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
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8801','CN-PT-CTR-2026-001','2026-03-20','91320413MA1M9Y2C4B','PT517890123','EUR',6120000,145000,18500,6283500,7.82);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8802','CN-PT-CTR-2026-002','2026-03-25','91440300192317458F','PT500234567','EUR',9440000,260000,32000,9732000,7.82);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8803','CN-PT-CTR-2026-003','2026-04-02','91610132724912345X','PT500697256','USD',3640000,0,0,3640000,7.21);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8804','CN-PT-CTR-2026-004','2026-04-10','91350900587527783P','PT503412890','EUR',3420000,88000,12000,3520000,7.835);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8805','CN-PT-CTR-2026-005','2026-04-15','91110108551385082Q','PT500246810','EUR',2425000,42000,6500,2473500,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8806','CN-PT-CTR-2026-006','2026-04-18','91330200778899112T','PT500191827','USD',2655000,95000,11000,2761000,7.22);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8807','CN-PT-CTR-2026-007','2026-04-22','91330782098765432W','PT504998877','CNY',7125000,0,0,7125000,1);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9901','CN-PT-CTR-2026-008','2026-04-05','91110000101123456N','PT500265432','EUR',1480000,38000,4500,1522500,7.83);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9902','CN-PT-CTR-2026-009','2026-04-12','91110000101123456N','PT500077889','EUR',1850000,32000,3800,1885800,7.83);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9903','CN-PT-CTR-2026-010','2026-04-20','91440400MA56LUS01P','PT500112233','EUR',1120000,29000,3200,1152200,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9905','CN-PT-CTR-2026-011','2026-04-24','91110000101123456N','PT508112244','EUR',1600000,45000,5000,1650000,7.835);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9906','CN-PT-CTR-2026-012','2026-04-28','91110000101123456N','PT500214890','EUR',1240000,36000,4000,1280000,7.835);
INSERT INTO "cn_commercial_invoices" VALUES('INV-PT-2026-9904','CN-PT-CTR-2026-013','2026-04-30','91370200163562681G','PT500055214','EUR',2040000,55000,5000,2100000,7.83);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8808','CN-PT-CTR-2026-014','2026-05-02','91440300618837699Q','PT500697256','EUR',1780000,52000,8000,1840000,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8809','CN-PT-CTR-2026-015','2026-05-04','91110108551385082Q','PT500246810','EUR',3140000,52000,8000,3200000,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8810','CN-PT-CTR-2026-016','2026-05-06','91440606190342599T','PT500246810','EUR',1400000,45000,5000,1450000,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8811','CN-PT-CTR-2026-017','2026-05-08','911100007178071858','PT503412890','EUR',4050000,88000,12000,4150000,7.84);
INSERT INTO "cn_commercial_invoices" VALUES('INV-CN-2026-8813','CN-PT-CTR-2026-018','2026-05-12','91440300192317458F','PT500234567','EUR',8680000,240000,30000,8950000,7.84);
CREATE TABLE cn_customs_export_declarations_gacc (
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
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('220120260000108801','INV-CN-2026-8801','91320413MA1M9Y2C4B','2201',1774080000,'0110','2 - Maritime','COSU6288991101','9795610','PTSIN',47858400,6638000,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('530120260000108802','INV-CN-2026-8802','91440300192317458F','5301',1774512000,'0110','2 - Maritime','COSU6288991102','9842105','PTSIN',73820800,10238000,'Doc Review');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('220120260000108803','INV-CN-2026-8803','91610132724912345X','2201',1775116800,'0110','2 - Maritime','COSU6288991103','9795610','PTSIN',26244400,3640000,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('310120260000108804','INV-CN-2026-8804','91350900587527783P','3101',1775808000,'0110','2 - Maritime','COSU6288991104','9795634','PTLEI',26795700,3710000,'Physical Inspection');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('010120260000108805','INV-CN-2026-8805','91110108551385082Q','0101',1776240000,'0110','5 - Air','047-88991105','JD431','PTLIS',19012000,2630000,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('310120260000108806','INV-CN-2026-8806','91330200778899112T','3101',1776499200,'0110','2 - Maritime','COSU6288991106','9795634','PTSIN',19169100,2655000,'Doc Review');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('292120260000108807','INV-CN-2026-8807','91330782098765432W','2921',1776844800,'9710','3 - Rail','CIMSMGS-YW2026-07','X8020-YIWU-IB','PTENT',7125000,986800,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('530120260000108808','INV-CN-2026-8808','91440300618837699Q','5301',1777017600,'0110','2 - Maritime','COSU6288991108','9795646','PTSIN',14425600,1998000,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('010120260000108809','INV-CN-2026-8809','91110108551385082Q','0101',1777276800,'0110','5 - Air','047-88991109','CA1091','PTLIS',25088000,3474800,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('510120260000108810','INV-CN-2026-8810','91440606190342599T','5101',1777449600,'0110','2 - Maritime','COSU6288991110','9795646','PTSIN',11368000,1574500,'Doc Review');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('010120260000108811','INV-CN-2026-8811','911100007178071858','0101',1777708800,'0110','2 - Maritime','COSU6288991111','9795622','PTSIN',32536000,4506300,'Doc Review');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('292120260000108812','INV-CN-2026-8807','91330782098765432W','2921',1777968000,'9710','3 - Rail','CIMSMGS-YW2026-12','X8020-YIWU-MAD','PTLIS',4275000,592000,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('530120260000108813','INV-CN-2026-8813','91440300192317458F','5301',1778140800,'0110','2 - Maritime','COSU6288991113','9842117','PTSIN',70168000,9718500,'Doc Review');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('310120260000108814','INV-CN-2026-8803','91320400608131370B','3101',1778313600,'0110','2 - Maritime','COSU6288991114','9795622','PTSIN',11760000,1628800,'Released Automatically');
INSERT INTO "cn_customs_export_declarations_gacc" VALUES('530120260000108815','INV-CN-2026-8805','91440300755673010C','5301',1778486400,'9610','5 - Air','871-33221100','5Y8911','PTLIS',8250000,1142600,'Released Automatically');
CREATE TABLE cn_customs_import_declarations_gacc (
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
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('220120261000990001','91110000101123456N','PT500265432','CPRT18000102000101','2204210000','PTLEI','2201','COSU6288992201',11921175,1668964.5,1510015.5,1963019.9,'2026-05-04');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('220120261000990002','91110000101123456N','PT500077889','CPRT18009901000202','4504900000','PTLEI','2201','COSU6288992202',14765814,738290.7,0,2015533.61,'2026-05-10');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('530420261000990003','91440400MA56LUS01P','PT500112233','CPRT18000401000303','1509200000','PTSIN','5304','COSU6288992203',9033248,903324.8,0,894291.55,'2026-05-18');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('310120261000990004','91330200778899112T','PT500334455',NULL,'4703290000','PTLEI','3101','COSU6288992204',22450000,0,0,2918500,'2026-05-22');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('220120261000990005','91110000101123456N','PT508112244','CPRT18000101000505','0203290090','PTSIN','2201','COSU6288992205',8420000,673600,0,818424,'2026-05-26');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('220120261000990006','91110000101123456N','PT500214890','CPRT18000102000606','2204210000','PTLEI','2201','COSU6288992206',9722400,1361136,1231494,1600984,'2026-05-29');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('370220261000990007','91370200163562681G','PT500055214','CPRT18000301000707','4703290000','PTSET','3702','COSU6288992207',16443000,0,0,2137590,'2026-05-31');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('530120261000990008','91440300755673010C','PT500876543','CPRT15000104000505','1509200000','PTSIN','5301','COSU6288992202',7250000,725000,0,717750,'2026-06-02');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('220120261000990009','91310000132234561L','PT500123999','CPRT45000106000404','4504900000','PTLEI','2201','COSU6288992207',6500000,325000,0,887250,'2026-06-04');
INSERT INTO "cn_customs_import_declarations_gacc" VALUES('370220261000990010','91110000101123456N','PT502889900','CPRT18000201000505','0203290090','PTSIN','3702','COSU6288992205',11125700,890056,0,1081418.04,'2026-06-06');
CREATE TABLE cn_customs_tariff_quotas_antidumping_mofcom (
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
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-AD-2026-PORK-01','0203290090','220120261000990005','MOFCOM Announcement No. 23 of 2024 (EU Pork Investigation)','EU Pork Anti-Dumping Investigation Deposit',4.9,412580,'PT508112244');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-AD-2026-PORK-02','0203290090','370220261000990010','MOFCOM Announcement No. 23 of 2024 (EU Pork Investigation)','EU Pork Anti-Dumping Investigation Deposit',4.9,545159.3,'PT502889900');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-MFN-2026-WINE-03','2204210000','220120261000990001','GACC Tariff Schedule 2026 (Table & Fortified Wine)','MFN Standard Zero Measure',0,0,'PT500265432');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-MFN-2026-CORK-04','4504900000','220120261000990002','GACC Green Packaging Tariff Reduction 2026','MFN Standard Zero Measure',0,0,'PT500077889');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-TRQ-2026-OLIVE-05','1509200000','530420261000990003','Hengqin Lusophone Foodstuff Facilitation Notice 2026','Agricultural Tariff Rate Quota TRQ',0,0,'PT500112233');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-MFN-2026-PULP-06','4703290000','370220261000990007','GACC Zero-Tariff Raw Wood Pulp Schedule 2026','MFN Standard Zero Measure',0,0,'PT500055214');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-MFN-2026-WINE-07','2204210000','220120261000990006','GACC Tariff Schedule 2026 (Douro DOC Wine)','MFN Standard Zero Measure',0,0,'PT500214890');
INSERT INTO "cn_customs_tariff_quotas_antidumping_mofcom" VALUES('MOF-TRQ-2026-OLIVE-08','1509200000','530120261000990008','GACC Edible Oil Import Monitoring Schedule 2026','Agricultural Tariff Rate Quota TRQ',0,0,'PT500876543');
CREATE TABLE cn_customs_tax_guarantees_consolidated_bonds (
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
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-SH-2026-01','91110000101123456N','Bank of China Shanghai FTZ Branch','Consolidated Monthly Taxation Bond',50000000,14250000,'2201','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-QD-2026-02','91110000101123456N','Agricultural Bank of China Qingdao','Anti-Dumping Provisional Security Bond',15000000,957739.3,'3702','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-HQ-2026-03','91440400MA56LUS01P','Bank of China Zhuhai Hengqin Branch','Consolidated Monthly Taxation Bond',20000000,3850000,'5304','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-NB-2026-04','91330200778899112T','Bank of Communications Ningbo Branch','Consolidated Monthly Taxation Bond',40000000,8120000,'3101','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-QD-2026-05','91370200163562681G','China Construction Bank Qingdao','Consolidated Monthly Taxation Bond',60000000,11400000,'3702','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-SZ-2026-06','91440300755673010C','PICC Property & Casualty Tariff Bond Division','Transit Customs Bond',35000000,6200000,'5301','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-JS-2026-07','91320413MA1M9Y2C4B','Bank of China Changzhou Branch','Transit Customs Bond',80000000,18500000,'2304','2026-12-31');
INSERT INTO "cn_customs_tax_guarantees_consolidated_bonds" VALUES('BOND-GACC-SH-2026-08','91310000132234561L','Industrial Bank Shanghai Head Office','Consolidated Monthly Taxation Bond',30000000,4120000,'2201','2026-12-31');
CREATE TABLE cn_enterprises_manufacturers (
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
INSERT INTO "cn_enterprises_manufacturers" VALUES('91320413MA1M9Y2C4B','3204960012','CALB Group Co., Ltd. (China Aviation Lithium Battery)','中创新航科技集团股份有限公司','Publicly Listed Tech Giant','C384','320400',6,177255,'Advanced Certified AEO','2015-12-08');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440300192317458F','4403160088','BYD Auto Industry Company Limited','比亚迪汽车工业有限公司','Publicly Listed Tech Giant','C361','440300',2,375800,'Advanced Certified AEO','2006-08-03');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91350900587527783P','3509960001','Contemporary Amperex Technology Co., Limited (CATL)','宁德时代新能源科技股份有限公司','Publicly Listed Tech Giant','C384','350900',7,439800,'Advanced Certified AEO','2011-12-16');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91610132724912345X','6101960022','LONGi Green Energy Technology Co., Ltd.','隆基绿能科技股份有限公司','Publicly Listed Tech Giant','C382','610100',8,758200,'Advanced Certified AEO','2000-02-14');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440300618837699Q','4403960001','Huawei Technologies Co., Ltd. (Solar & Digital Power)','华为技术有限公司','Private Domestic','C396','440300',2,4084110,'Advanced Certified AEO','1987-09-15');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91110108551385082Q','1108960055','Xiaomi Communications Co., Ltd.','小米通讯技术有限公司','Publicly Listed Tech Giant','C397','110000',1,320000,'Advanced Certified AEO','2010-08-25');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91330782098765432W','3307960088','Zhejiang China Commodities City Group (Yiwu CCCG)','浙江中国小商品城集团股份有限公司','SOE - State-Owned Enterprise','F513','330782',5,548600,'Advanced Certified AEO','1993-12-28');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91330200778899112T','3302960077','Ningbo Iron & Steel Co., Ltd. (Hanggang Group)','宁波钢铁有限公司','SOE - State-Owned Enterprise','C312','330200',4,1180000,'General Certified AEO','2003-02-18');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91110000101123456N','1101960010','COFCO Corporation (China National Cereals, Oils & Foodstuffs)','中粮集团有限公司','SOE - State-Owned Enterprise','F512','110000',1,1195500,'Advanced Certified AEO','1983-07-06');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440400MA56LUS01P','4404960056','Guangdong-Macao Traditional Chinese Medicine & Lusophone Park','粤澳合作中医药科技产业园开发有限公司','SOE - State-Owned Enterprise','M731','440400',3,250000,'General Certified AEO','2011-11-28');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91310000132209876M','3100960002','COSCO SHIPPING Lines Co., Ltd.','中远海运集装箱运输有限公司','SOE - State-Owned Enterprise','G551','310000',1,2366000,'Advanced Certified AEO','1997-11-11');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91110000100001146K','1101960088','China Three Gorges Corporation (CTG - EDP Strategic Partner)','中国长江三峡集团有限公司','SOE - State-Owned Enterprise','D441','110000',1,21150000,'Advanced Certified AEO','1993-09-27');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91110000710931234R','1101960099','State Grid Corporation of China (SGCC - REN Stakeholder)','国家电网有限公司','SOE - State-Owned Enterprise','D442','110000',1,82950000,'Advanced Certified AEO','2002-12-29');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91310000132234561L','3100960005','Fosun International Limited (Fidelidade & BCP Investor)','复星国际有限公司','Private Domestic','L721','310000',1,895000,'Advanced Certified AEO','1992-11-06');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91320400608131370B','3204960033','Trina Solar Co., Ltd.','天合光能股份有限公司','Publicly Listed Tech Giant','C382','320400',6,217300,'Advanced Certified AEO','1997-12-26');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440606190342599T','4406960021','Midea Group Co., Ltd.','美的集团股份有限公司','Publicly Listed Tech Giant','C385','440600',2,701500,'Advanced Certified AEO','2000-04-07');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440400192548256N','4404960011','Gree Electric Appliances, Inc. of Zhuhai','珠海格力电器股份有限公司','Publicly Listed Tech Giant','C385','440400',3,563100,'Advanced Certified AEO','1989-12-13');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91370200163562681G','3702960015','Haier Smart Home Co., Ltd.','海尔智家股份有限公司','Publicly Listed Tech Giant','C385','370200',10,943800,'Advanced Certified AEO','1994-03-29');
INSERT INTO "cn_enterprises_manufacturers" VALUES('911100007178071858','1101960066','CRRC Corporation Limited (Rolling Stock & Metro Cars)','中国中车股份有限公司','SOE - State-Owned Enterprise','C371','110000',1,2869800,'Advanced Certified AEO','2007-12-28');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91440300755673010C','4403960044','Cainiao Smart Logistics Network (Shenzhen Hub)','深圳市菜鸟供应链管理有限公司','Private Domestic','G599','440300',2,100000,'Advanced Certified AEO','2013-05-28');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91330100716105852F','3301960018','Alibaba (China) Technology Co., Ltd. (AliExpress)','阿里巴巴（中国）网络技术有限公司','Publicly Listed Tech Giant','I642','330100',12,1530000,'Advanced Certified AEO','1999-09-09');
INSERT INTO "cn_enterprises_manufacturers" VALUES('91120000103061234K','1201960005','Tianjin Port (Group) Co., Ltd.','天津港（集团）有限公司','SOE - State-Owned Enterprise','G551','120000',11,1420000,'Advanced Certified AEO','1992-10-18');
CREATE TABLE cn_excise_consumption_tax_sta (
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
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-SH-001','220120261000990001','2204210000','Imported Grape Wine Consumption Tax (进口葡萄酒消费税 10%)',10,0,1510015.5,'STA-CT-3100-2026-990001');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-SH-002','220120261000990006','2204210000','Imported Grape Wine Consumption Tax (进口葡萄酒消费税 10%)',10,0,1231494,'STA-CT-3100-2026-990006');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-SH-003','220120261000990002','4504900000','Exempt Industrial Cork Articles (软木制品免征消费税)',0,0,0,'STA-CT-3100-2026-990002');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-HQ-004','530420261000990003','1509200000','Exempt Edible Olive Oil (食用橄榄油免征消费税)',0,0,0,'STA-CT-4404-2026-990003');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-SH-005','220120261000990005','0203290090','Exempt Frozen Swine Meat (冻猪肉免征消费税)',0,0,0,'STA-CT-3100-2026-990005');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-QD-006','370220261000990007','4703290000','Exempt Wood Pulp Raw Material (木浆免征消费税)',0,0,0,'STA-CT-3702-2026-990007');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-SZ-007','530120261000990008','1509200000','Exempt Edible Olive Oil (食用橄榄油免征消费税)',0,0,0,'STA-CT-4403-2026-990008');
INSERT INTO "cn_excise_consumption_tax_sta" VALUES('CT-STA-2026-QD-008','370220261000990010','0203290090','Exempt Frozen Swine Meat (冻猪肉免征消费税)',0,0,0,'STA-CT-3702-2026-990010');
CREATE TABLE cn_export_control_dual_use_mofcom_permits (
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
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-001','91320413MA1M9Y2C4B','220120260000108801','CN-DU-2024-GRAPHITE-02','Synthetic Spherical Anode Graphite Embedded in LFP Cells','PT517890123',1,'MOFCOM Bureau of Industry, Security, Import & Export Control','2026-03-10');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-002','91440300192317458F','530120260000108802','CN-DU-2025-NDM-05','High-Coercivity Samarium-Cobalt / NdFeB Permanent Traction Magnets','PT500234567',1,'MOFCOM Bureau of Industry, Security, Import & Export Control','2026-03-15');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-003','91350900587527783P','310120260000108804','CN-DU-2025-LFP-CATHODE','High-Compaction Density LFP Cathode Material (>300Wh/kg Tech)','PT503412890',1,'MOFCOM & MIIT Joint Strategic Technology Panel','2026-04-01');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-004','91330200778899112T','310120260000108806','CN-DU-2024-ALLOY-72','High-Tensile Corrosion-Resistant Marine/Offshore Alloy Steel','PT500191827',1,'MOFCOM Zhejiang Provincial Department','2026-04-10');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-005','91440300618837699Q','530120260000108808','CN-DU-2024-GAN-RF09','Gallium Nitride (GaN) High-Frequency Power Amplifier Modules','PT500697256',1,'MOFCOM Bureau of Industry, Security, Import & Export Control','2026-04-22');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-006','911100007178071858','010120260000108811','CN-DU-2025-RAIL-IGBT','High-Voltage Traction Converter Control Units (3300V IGBT)','PT503412890',1,'MOFCOM Beijing Municipal Commission of Commerce','2026-04-30');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-007','91440300192317458F','530120260000108813','CN-DU-2025-NDM-05','Rare-Earth Permanent Magnet Synchronous EV Drive Units','PT500234567',1,'MOFCOM Bureau of Industry, Security, Import & Export Control','2026-05-05');
INSERT INTO "cn_export_control_dual_use_mofcom_permits" VALUES('DUAL-MOFCOM-2026-008','91610132724912345X','220120260000108803','CN-DU-2024-WAFER-INGOT','Large-Diameter Monocrystalline Silicon Ingot Puller Specification','PT500697256',1,'MOFCOM Shaanxi Provincial Commerce Department','2026-03-25');
CREATE TABLE cn_factory_production_facilities (
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
INSERT INTO "cn_factory_production_facilities" VALUES(101,'91320413MA1M9Y2C4B','CALB Changzhou Jintan Zero-Carbon Battery Base','320400',31.7245,119.5821,480000,6200,35000000,1,1,NULL,0.312);
INSERT INTO "cn_factory_production_facilities" VALUES(102,'91440300192317458F','BYD Shenzhen Pingshan New Energy Vehicle MegaPlant','440300',22.6912,114.3541,1120000,18500,500000,1,1,NULL,0.385);
INSERT INTO "cn_factory_production_facilities" VALUES(103,'91350900587527783P','CATL Ningde Zhangwan Lighthouse Battery Plant','350900',26.6853,119.5478,890000,14200,60000000,1,1,NULL,0.275);
INSERT INTO "cn_factory_production_facilities" VALUES(104,'91610132724912345X','LONGi Xi''an Jingwei Hi-MO Solar Module Factory','610100',34.4321,108.9732,410000,5400,18000000,1,1,NULL,0.441);
INSERT INTO "cn_factory_production_facilities" VALUES(105,'91440300618837699Q','Huawei Dongguan Songshan Lake Smart5G & Inverter Campus','440300',22.9231,113.8891,650000,9800,12000000,1,1,NULL,0.351);
INSERT INTO "cn_factory_production_facilities" VALUES(106,'91110108551385082Q','Xiaomi Beijing Changping Dark Smart Factory','110000',40.1125,116.2981,81000,1100,10000000,1,1,NULL,0.398);
INSERT INTO "cn_factory_production_facilities" VALUES(107,'91330782098765432W','Yiwu Futian Consumer Goods Consolidation & Textile Mill','330782',29.3214,120.0982,260000,3100,95000000,1,0,NULL,0.512);
INSERT INTO "cn_factory_production_facilities" VALUES(108,'91330200778899112T','Ningbo Beilun Special Structural Steel & Aluminum Smelter','330200',29.9123,121.8452,540000,4300,1200000,1,1,NULL,0.648);
INSERT INTO "cn_factory_production_facilities" VALUES(109,'91110000101123456N','COFCO Shanghai Waigaoqiao Bonded Cold-Chain Wine Hub','310000',31.3412,121.5891,95000,420,45000000,1,1,'CNSH001928374',0.36);
INSERT INTO "cn_factory_production_facilities" VALUES(110,'91320400608131370B','Trina Solar Changzhou Photovoltaic Cell Gigafactory','320400',31.8123,119.9821,350000,4800,25000000,1,1,NULL,0.325);
INSERT INTO "cn_factory_production_facilities" VALUES(111,'91440606190342599T','Midea Shunde Smart Home & Heat Pump HVAC Plant','440600',22.8123,113.2451,520000,7500,15000000,1,1,NULL,0.345);
INSERT INTO "cn_factory_production_facilities" VALUES(112,'91440400192548256N','Gree Zhuhai Qianshan Inverter & AC Base','440400',22.2512,113.5124,480000,6800,14000000,1,1,NULL,0.352);
INSERT INTO "cn_factory_production_facilities" VALUES(113,'91370200163562681G','Haier Qingdao Sino-German EcoPark Smart Appliance Base','370200',36.0123,120.1823,420000,5100,8000000,1,1,NULL,0.318);
INSERT INTO "cn_factory_production_facilities" VALUES(114,'911100007178071858','CRRC Qingdao Sifang High-Speed & Metro Rolling Stock Plant','370200',36.1824,120.3541,780000,8900,1500,1,1,NULL,0.42);
INSERT INTO "cn_factory_production_facilities" VALUES(115,'91440300755673010C','Cainiao Shenzhen Airport International Cross-Border Gateway','440300',22.6321,113.8124,180000,1900,120000000,1,1,NULL,0.33);
INSERT INTO "cn_factory_production_facilities" VALUES(116,'91440400MA56LUS01P','Hengqin Sino-Lusophone GMP Bio-Pharmaceutical Base','440400',22.1412,113.5412,120000,850,5000000,1,1,'CNGD008819283',0.29);
CREATE TABLE cn_freight_forwarders_nvocc_customs_brokers (
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
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-SINOTRANS-01','91110000710930011X','Sinotrans Limited (China National Foreign Trade Transportation)','GACC-BRK-SH-0001','MOC-NV00001','CNSHA','Advanced Certified Broker',1450);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-COSCO-LOG-02','91310000710928812Y','COSCO SHIPPING Logistics & Supply Chain Co., Ltd.','GACC-BRK-NB-0008','MOC-NV00012','CNNGB','Advanced Certified Broker',1820);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-KUEHNE-SZ-03','91440300607411223Z','Kuehne + Nagel (China) Ltd. Shenzhen Branch','GACC-BRK-SZ-0042','MOC-NV00105','CNSZX','Advanced Certified Broker',940);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-DHL-GLOBAL-04','91310000607299104W','DHL Global Forwarding (China) Co., Ltd.','GACC-BRK-BJ-0019','MOC-NV00088','CNBJS','Advanced Certified Broker',1120);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-YIWU-RAIL-05','91330782558899110V','Yiwu Timex Industrial Investment & BRI Rail Forwarding Co.','GACC-BRK-YW-0102','MOC-NV01822','CNYIW','General Certified Broker',680);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-CAINIAO-CB-06','91440300MA5ECBEC6U','Cainiao Customs Brokerage & Smart Clearance Shenzhen Ltd.','GACC-BRK-SZ-0211','MOC-NV02410','CNSZX','Advanced Certified Broker',3200);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-QINGDAO-PORT-07','91370200163577889T','Qingdao Port International Logistics & Customs Agency Co.','GACC-BRK-QD-0015','MOC-NV00319','CNTAO','Advanced Certified Broker',790);
INSERT INTO "cn_freight_forwarders_nvocc_customs_brokers" VALUES('BRK-CN-MACAO-CTS-08','91440400192599001S','China Travel Service (Macao/Zhuhai) Bonded Customs Brokers','GACC-BRK-ZH-0033','MOC-NV00944','CNZUH','General Certified Broker',340);
CREATE TABLE cn_fx_settlements_pboc_safe (
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
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SH-90001','97ed4827-7b6f-4491-a06f-b548d5a75001','INV-CN-2026-8801','91320413MA1M9Y2C4B','517890123','Bank of China (BOC) Jiangsu Branch','SWIFT_EUR','EUR',6283500,49136970,7.82,'2026-03-28');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SZ-90002','97ed4827-7b6f-4491-a06f-b548d5a75002','INV-CN-2026-8802','91440300192317458F','500234567','ICBC Shenzhen Futian Branch','SWIFT_EUR','EUR',9732000,76104240,7.82,'2026-04-02');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-XA-90003','97ed4827-7b6f-4491-a06f-b548d5a75003','INV-CN-2026-8803','91610132724912345X','500697256','China Construction Bank (CCB) Shaanxi','SWIFT_USD','USD',3640000,26244400,7.21,'2026-04-09');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-ND-90004','97ed4827-7b6f-4491-a06f-b548d5a75004','INV-CN-2026-8804','91350900587527783P','503412890','Bank of China (BOC) Lisbon-Fujian Clearing','SWIFT_EUR','EUR',3520000,27579200,7.835,'2026-04-16');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-BJ-90005','97ed4827-7b6f-4491-a06f-b548d5a75005','INV-CN-2026-8805','91110108551385082Q','500246810','ICBC Beijing Head Office','SWIFT_EUR','EUR',2473500,19392240,7.84,'2026-04-22');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-NB-90006','97ed4827-7b6f-4491-a06f-b548d5a75006','INV-CN-2026-8806','91330200778899112T','500191827','Bank of Communications Ningbo','SWIFT_USD','USD',2761000,19934420,7.22,'2026-04-25');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-YW-90007','CIPS-RMB-20260428-YIWU-PT007','INV-CN-2026-8807','91330782098765432W','504998877','Bank of China Macau / Yiwu CIPS Direct','CIPS_DIRECT_RMB','CNY',7125000,7125000,1,'2026-04-28');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SH-90008','97ed4827-7b6f-4491-a06f-b548d5a75008','INV-PT-2026-9901','91110000101123456N','500265432','Bank of China Shanghai FTZ Branch','SWIFT_EUR','EUR',1522500,11921175,7.83,'2026-05-06');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SH-90009','97ed4827-7b6f-4491-a06f-b548d5a75009','INV-PT-2026-9902','91110000101123456N','500077889','Bank of China Shanghai FTZ Branch','SWIFT_EUR','EUR',1885800,14765814,7.83,'2026-05-12');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-HQ-90010','97ed4827-7b6f-4491-a06f-b548d5a75010','INV-PT-2026-9903','91440400MA56LUS01P','500112233','Bank of China Hengqin Branch','SWIFT_EUR','EUR',1152200,9033248,7.84,'2026-05-18');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-QD-90011','97ed4827-7b6f-4491-a06f-b548d5a75011','INV-PT-2026-9905','91110000101123456N','508112244','Agricultural Bank of China Qingdao','SWIFT_EUR','EUR',1650000,12927750,7.835,'2026-05-22');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SH-90012','97ed4827-7b6f-4491-a06f-b548d5a75012','INV-PT-2026-9904','91370200163562681G','500055214','Bank of Communications Shanghai','SWIFT_EUR','EUR',2100000,16443000,7.83,'2026-05-26');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SZ-90013','97ed4827-7b6f-4491-a06f-b548d5a75013','INV-CN-2026-8808','91440300618837699Q','500697256','ICBC Shenzhen Futian','SWIFT_EUR','EUR',1840000,14425600,7.84,'2026-05-29');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-SZ-90014','97ed4827-7b6f-4491-a06f-b548d5a75014','INV-CN-2026-8813','91440300192317458F','500234567','ICBC Shenzhen Pingshan','SWIFT_EUR','EUR',8950000,70168000,7.84,'2026-06-02');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-BJ-90015','97ed4827-7b6f-4491-a06f-b548d5a75015','INV-CN-2026-8809','91110108551385082Q','500246810','ICBC Beijing Haidian','SWIFT_EUR','EUR',3200000,25088000,7.84,'2026-06-05');
INSERT INTO "cn_fx_settlements_pboc_safe" VALUES('SAFE-2026-GZ-90016','97ed4827-7b6f-4491-a06f-b548d5a75016','INV-CN-2026-8810','91440606190342599T','500246810','Bank of China Shunde','SWIFT_EUR','EUR',1450000,11368000,7.84,'2026-06-08');
CREATE TABLE cn_gacc_aeo_mutual_recognition_registry (
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
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-JS-3204960012','91320413MA1M9Y2C4B','PT517890123','CN-EU-AEO-MRA-2014',0.8,1,'2025-11-10','2028-11-09');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-GD-4403160088','91440300192317458F','PT500234567','CN-EU-AEO-MRA-2014',1.2,1,'2025-09-18','2028-09-17');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-FJ-3509960001','91350900587527783P','PT503412890','CN-EU-AEO-MRA-2014',0.9,1,'2025-10-22','2028-10-21');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-SN-6101960022','91610132724912345X','PT500697256','CN-EU-AEO-MRA-2014',0.75,1,'2025-08-14','2028-08-13');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-BJ-1108960055','91110108551385082Q','PT500246810','CN-EU-AEO-MRA-2014',1.1,1,'2025-12-01','2028-11-30');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-BJ-1101960010','91110000101123456N','PT500265432','CN-EU-AEO-MRA-2014',1,1,'2025-07-19','2028-07-18');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-SH-3100960002','91310000132209876M','PT500077889','CN-EU-AEO-MRA-2014',0.65,1,'2026-01-15','2029-01-14');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-GD-4403960001','91440300618837699Q','PT500697256','CN-EU-AEO-MRA-2014',0.85,1,'2025-06-30','2028-06-29');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-SD-3702960015','91370200163562681G','PT500055214','CN-EU-AEO-MRA-2014',0.95,1,'2025-10-05','2028-10-04');
INSERT INTO "cn_gacc_aeo_mutual_recognition_registry" VALUES('AEO-CN-BJ-1101960066','911100007178071858','PT500191827','CN-EU-AEO-MRA-2014',1.15,1,'2025-11-28','2028-11-27');
CREATE TABLE cn_green_manufacturing_esg_audits (
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
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(1,101,2025,12500,185000,8420.5,3903.5,68.5,'China Quality Certification Centre (CQC-CNAS)');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(2,102,2025,84000,310000,34200,32340,68.5,'SGS-CSTC Standards Technical Services Shenzhen');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(3,103,2025,15000,420000,11200,4125,72,'TÜV Rheinland Greater China / CNAS');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(4,104,2025,62000,195000,21500,27342,65,'CQC Xi''an Carbon Verification Bureau');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(5,108,2025,295000,82000,168400,191160,85,'Sinocarbon Innovation & Investment Co. (CBAM Verifier)');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(6,105,2025,45000,280000,18200,19500,70,'SGS-CSTC Standards Dongguan');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(7,106,2025,38000,165000,14200,16400,68.5,'CQC Beijing Green Building Bureau');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(8,110,2025,48000,210000,16500,19800,68.5,'TÜV NORD China CNAS');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(9,111,2025,92000,180000,42000,45200,65,'China National Accreditation Service (CNAS)');
INSERT INTO "cn_green_manufacturing_esg_audits" VALUES(10,114,2025,185000,95000,82000,91500,75,'CQC Qingdao Industrial Energy Bureau');
CREATE TABLE cn_hk_macao_offshore_trading_intermediaries (
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
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-MO-2026-001','MO-SOE-28891-C','Nam Kwong Lusophone International Trading Co., Ltd.','Macao SAR','91440400MA56LUS01P','CN-PT-CTR-2026-010',9033248,1152200,'Bank of China Macau Branch (RMB Clearing Bank)');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-HK-2026-002','HK-CR-1928374','BYD (H.K.) Co., Limited - Offshore Treasury & Auto Hub','Hong Kong SAR','91440300192317458F','CN-PT-CTR-2026-002',76104240,9732000,'BOCHK Hong Kong Offshore CNH Clearing Center');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-MO-2026-003','MO-COM-88219-A','Macau Legend & COFCO Lusophone Wine Distribution Lda.','Macao SAR','91110000101123456N','CN-PT-CTR-2026-008',11921175,1522500,'BNU Macau / Banco Nacional Ultramarino');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-HQ-2026-004','HQ-FTZ-99102-Z','Hengqin Sino-Portuguese Commodity Clearing Platform Ltd.','Hengqin Offshore Zone','91330782098765432W','CN-PT-CTR-2026-007',7125000,910000,'ICBC Hengqin Free Trade Account (FTN) Center');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-HK-2026-005','HK-CR-2093811','Xiaomi H.K. Limited - Global Supply Chain Treasury','Hong Kong SAR','91110108551385082Q','CN-PT-CTR-2026-005',19392240,2473500,'HSBC Hong Kong Offshore Renminbi Desk');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-MO-2026-006','MO-INV-55412-B','Chung Kiu (Macau) Agri-Food & Cork Import-Export Lda.','Macao SAR','91110000101123456N','CN-PT-CTR-2026-009',14765814,1885800,'Luso International Banking Ltd. (LIB Macau)');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-HK-2026-007','HK-CR-3319022','LONGi Solar Technology (H.K.) Limited','Hong Kong SAR','91610132724912345X','CN-PT-CTR-2026-003',26244400,3640000,'Standard Chartered Bank (HK) CNH Settlement');
INSERT INTO "cn_hk_macao_offshore_trading_intermediaries" VALUES('OFF-HQ-2026-008','HQ-FTZ-77410-M','China-Portugal Green Energy Equipment Leasing (Hengqin) Co.','Hengqin Offshore Zone','91320413MA1M9Y2C4B','CN-PT-CTR-2026-001',49136970,6283500,'Bank of China Hengqin Cross-Border RMB Pool');
CREATE TABLE cn_hs_tariff_schedule_gacc (
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
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8507600090','850760','8507600090999','锂离子蓄电池组 (新能源汽车及储能用)','Lithium-ion electric accumulators (EV & ESS modules)','piece / Jin',6,0,13,9,'B/4');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8541430000','854143','8541430000999','已组装的光伏电池组件 (太阳能电池板)','Photovoltaic cells assembled in modules or panels','piece / Jin',0,0,13,9,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8703800010','870380','8703800010101','仅装有驱动电动机的载人机动车辆 (纯电动汽车)','Motor vehicles propelled solely by electric motor (BEV)','unit / Jin',15,0,13,13,'B/4/O');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8504403090','850440','8504403090999','智能光伏逆变器及变流器','Static converters and smart solar PV inverters','piece / Jin',5,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8517130000','851713','8517130000999','蜂窝网络智能手机','Smartphones for cellular networks (5G)','piece / Jin',0,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8471300000','847130','8471300000999','重量不超过10公斤的便携式数字自动数据处理设备 (笔记本电脑)','Portable automatic data processing machines <= 10kg (Laptops)','piece / Jin',0,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8415102100','841510','8415102100999','分体式变频房间空气调节器 (热泵空调)','Split-system inverter air conditioners (Heat Pumps)','piece / Jin',10,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8528722100','852872','8528722100999','彩色液晶平板智能电视机','Color smart LCD / OLED television receivers','piece / Jin',12,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('6109100000','610910','6109100000999','棉制针织T恤衫、汗衫及马甲','T-shirts, singlets and other vests, knitted of cotton','piece / Jin',10,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('9503002100','950300','9503002100999','塑料制玩偶及拼插积木类智力玩具','Dolls, scale models and plastic construction toy sets','piece / Jin',0,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('7225409900','722540','7225409900999','热轧其他合金钢平板轧材 (CBAM受控钢材)','Flat-rolled alloy steel products, hot-rolled (CBAM scope)','Jin / metric ton',3,0,13,0,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('7606125900','760612','7606125900999','铝合金矩形板、片及带 (CBAM受控铝材)','Aluminum alloy rectangular plates and sheets (CBAM scope)','Jin / metric ton',6,0,13,0,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8479899990','847989','8479899990999','工业多关节机械手及自动装配机器人','Industrial articulated multi-axis robots and assembly arms','piece / Jin',0,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('8607191000','860719','8607191000999','铁道机车及轨道交通客车用转向架总成','Bogies and steerable wheelsets for railway locomotives and metro cars','unit / Jin',2,0,13,9,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('6204620000','620462','6204620000999','棉制女式长裤及工装裤','Women''s or girls'' trousers and shorts of cotton','piece / Jin',8,0,13,13,'B');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('2204210000','220421','2204210000101','装入2升及以下容器的鲜葡萄酿造的酒 (葡萄牙DOC葡萄酒)','Wine of fresh grapes in containers <= 2L (Douro/Alentejo/Port)','liter / bottle',14,0,13,0,'A/B/R');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('1509200000','150920','1509200000102','特级初榨橄榄油 (葡萄牙进口)','Extra virgin olive oil chemically unmodified','Jin / liter',10,0,9,0,'A/B/R');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('4504900000','450490','4504900000105','压制软木塞及天然软木制品','Agglomerated cork stoppers and natural cork articles','Jin / piece',5,0,13,0,'A');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('4703290000','470329','4703290000101','漂白桉木碱木浆 (葡萄牙造纸木浆)','Semi-bleached or bleached non-coniferous eucalyptus wood pulp','Jin / metric ton',0,0,13,0,'A');
INSERT INTO "cn_hs_tariff_schedule_gacc" VALUES('0203290090','020329','0203290090101','冻猪肉 (葡萄牙黑猪及必萨罗猪肉)','Frozen meat of swine (Portuguese Iberico & Bisaro pork)','Jin / kg',8,0,9,0,'A/P/R');
CREATE TABLE cn_ipr_customs_protection_recordations (
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
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-TM-001','PT500265432','GRAHAM''S PORT & SYMINGTON DOURO DOC','Geographical Indication GI Douro/Porto','CNIPA-GI-2019-DOURO01','COFCO Wines & Spirits Import & Export Co., Ltd. (91110000101123456N)','White-Listed Authorized Channel','2034-12-31');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-TM-002','PT500214890','MATEUS ROSÉ & QUINTA DA LEDA SOGRAPE','Registered Trademark CNIPA','CNIPA-TM-11928374','COFCO Wines & Spirits Import & Export Co., Ltd. (91110000101123456N)','White-Listed Authorized Channel','2033-10-15');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-PT-003','PT500077889','AMORIM NATURAL CORK & NDTECH ANTI-TCA','Invention Patent CNIPA','ZL202180019283.4','COFCO Wines & Spirits / Fosun Wine & Spirits Shanghai','Active Border Protection','2035-06-30');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-TM-004','PT500112233','OLIVEIRA DA SERRA & ANDORINHA SOVENA','Registered Trademark CNIPA','CNIPA-TM-22839102','Guangdong-Macao Lusophone Park Trading (91440400MA56LUS01P)','White-Listed Authorized Channel','2032-08-20');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-PT-005','91440300192317458F','BYD BLADE BATTERY & E-PLATFORM 3.0','Invention Patent CNIPA','ZL202010293847.1','Salvador Caetano Auto S.A. Portugal (PT500234567)','White-Listed Authorized Channel','2035-12-31');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-PT-006','91320413MA1M9Y2C4B','CALB CIRRUS ULTRA-LOW CARBON LFP TABLESS CELL','Invention Patent CNIPA','ZL202310887766.5','CALB Portugal S.A. Sines Gigafactory (PT517890123)','White-Listed Authorized Channel','2036-03-15');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2025-TM-007','91110108551385082Q','XIAOMI HYPEROS & MI LOGO','Registered Trademark CNIPA','CNIPA-TM-88371920','Worten Equipamentos para o Lar S.A. (PT500246810)','Active Border Protection','2034-05-01');
INSERT INTO "cn_ipr_customs_protection_recordations" VALUES('IPR-GACC-2026-TM-008','91330782098765432W','LUXURY EUROPEAN FASHION BRAND PROTECTION (YIWU BORDER)','Registered Trademark CNIPA','CNIPA-TM-99001122','Unauthorized Counterfeit Garment Alert on Rail Consignment','Detention Triggered','2031-12-31');
CREATE TABLE cn_lc_documentary_presentations_discrepancies (
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
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-001','LC-BCP-BOC-2026-0001','INV-CN-2026-8801','COSU6288991101','2026-03-25',0,'Zero Discrepancies - Full UCP 600 Art. 14 Compliance','Clean Presentation - Honored','2026-03-28');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-003','LC-CGD-CCB-2026-0003','INV-CN-2026-8803','COSU6288991103','2026-04-06',0,'Zero Discrepancies - eUCP 2.0 Electronic BL Validated','Clean Presentation - Honored','2026-04-09');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-004','LC-BPI-BOC-2026-0004','INV-CN-2026-8804','COSU6288991104','2026-04-13',1,'Minor Typo in Notify Party Postal Code on Packing List (Waived by REN)','Discrepant - Waived by Applicant','2026-04-16');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-008','LC-BOC-BCP-2026-0008','INV-PT-2026-9901','COSU6288992201','2026-05-02',0,'Zero Discrepancies - Symington Port Wine Origin & VI-1 Verified','Clean Presentation - Honored','2026-05-06');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-010','LC-BOC-CGD-2026-0010','INV-PT-2026-9903','COSU6288992203','2026-05-14',0,'Zero Discrepancies - Hengqin FTZ Preferential Clearance','Clean Presentation - Honored','2026-05-18');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-011','LC-ABC-BPI-2026-0011','INV-PT-2026-9905','COSU6288992205','2026-05-19',1,'Bilingual Mandarin Back-Label Font Height < 1.8mm (Rectified in Bond)','Discrepant - Waived by Applicant','2026-05-22');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-012','LC-BOC-BCP-2026-0012','INV-PT-2026-9906','COSU6288992206','2026-05-25',0,'Zero Discrepancies - Full Compliance with UCP 600','Clean Presentation - Honored','2026-05-29');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-014','LC-CGD-ICBC-2026-0014','INV-CN-2026-8808','COSU6288991108','2026-05-26',0,'Zero Discrepancies - Huawei Inverter IEC Certificate Attached','Clean Presentation - Honored','2026-05-29');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-016','LC-BCP-BOC-2026-0016','INV-CN-2026-8810','COSU6288991110','2026-06-04',0,'Zero Discrepancies - Clean On-Board Bill of Lading','Clean Presentation - Honored','2026-06-08');
INSERT INTO "cn_lc_documentary_presentations_discrepancies" VALUES('PRES-DOC-2026-017','LC-HTB-ICBC-2026-0017','INV-CN-2026-8811','COSU6288991111','2026-06-10',0,'Documents Under Final Checking by Haitong Bank Lisbon','Under Bank Examination','2026-06-18');
CREATE TABLE cn_letters_of_credit_ucp600_swift (
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
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BCP-BOC-2026-0001','CN-PT-CTR-2026-001','BCOMPTPLXXX','BKCHCNBJ940','PT517890123','91320413MA1M9Y2C4B','EUR',18500000,'MT700 Issue','2026-06-30','2026-07-21','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-CGD-CCB-2026-0003','CN-PT-CTR-2026-003','CGDIPTPLXXX','PCBCCNBJSAX','PT500697256','91610132724912345X','USD',7280000,'MT700 Issue','2026-05-30','2026-06-15','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BPI-BOC-2026-0004','CN-PT-CTR-2026-004','BBPIPTPLXXX','BKCHCNBJ720','PT503412890','91350900587527783P','EUR',10260000,'MT700 Issue','2026-06-15','2026-06-30','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BOC-BCP-2026-0008','CN-PT-CTR-2026-008','BKCHCNBJ300','BCOMPTPLXXX','91110000101123456N','PT500265432','EUR',3450000,'MT700 Issue','2026-05-15','2026-05-31','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BOC-CGD-2026-0010','CN-PT-CTR-2026-010','BKCHCNBJ45A','CGDIPTPLXXX','91440400MA56LUS01P','PT500112233','EUR',2680000,'MT700 Issue','2026-05-25','2026-06-10','Unconfirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-ABC-BPI-2026-0011','CN-PT-CTR-2026-011','ABOCCNBJ380','BBPIPTPLXXX','91110000101123456N','PT508112244','EUR',4200000,'MT700 Issue','2026-06-05','2026-06-20','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BOC-BCP-2026-0012','CN-PT-CTR-2026-012','BKCHCNBJ300','BCOMPTPLXXX','91110000101123456N','PT500214890','EUR',3100000,'MT707 Amend','2026-06-10','2026-06-25','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-CGD-ICBC-2026-0014','CN-PT-CTR-2026-014','CGDIPTPLXXX','ICBKCNBJSZN','PT500697256','91440300618837699Q','EUR',4800000,'MT700 Issue','2026-06-20','2026-07-05','Confirmed Irrevocable');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-BCP-BOC-2026-0016','CN-PT-CTR-2026-016','BCOMPTPLXXX','BKCHCNBJ400','PT500246810','91440606190342599T','EUR',3800000,'MT700 Issue','2026-06-25','2026-07-10','Transferable LC');
INSERT INTO "cn_letters_of_credit_ucp600_swift" VALUES('LC-HTB-ICBC-2026-0017','CN-PT-CTR-2026-017','ESSIPTPLXXX','ICBKCNBJBJM','PT503412890','911100007178071858','EUR',8500000,'MT700 Issue','2026-07-01','2026-07-15','Confirmed Irrevocable');
CREATE TABLE cn_mofcom_trade_licenses_quotas (
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
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-EX-2026-JS001','91320413MA1M9Y2C4B','8507600090','Strategic EV & Battery Export License','PRT',15000,120000000,'2026-01-01','2026-12-31','Shanghai / Ningbo Ports');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-EX-2026-GD002','91440300192317458F','8703800010','Strategic EV & Battery Export License','PRT',12000,320000000,'2026-01-01','2026-12-31','Shenzhen Yantian / Shekou');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-IM-2026-BJ09101','91110000101123456N','2204210000','Automatic Import License','PRT',2500,18500000,'2026-01-01','2026-12-31','Shanghai / Shenzhen Ports');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-IM-2026-BJ09102','91110000101123456N','0203290090','Agricultural Tariff Quota','PRT',4500,19500000,'2026-01-01','2026-12-31','Shanghai Waigaoqiao Port');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-EX-2026-SN003','91610132724912345X','8541430000','Strategic EV & Battery Export License','PRT',8000,65000000,'2026-01-01','2026-12-31','Shanghai / Qingdao Ports');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-EX-2026-ZJ004','91330200778899112T','7225409900','Export Control Dual-Use','PRT',25000,35000000,'2026-01-01','2026-12-31','Ningbo Zhoushan Port');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-EX-2026-GD005','91440300618837699Q','8504403090','Export Control Dual-Use','PRT',5000,48000000,'2026-01-01','2026-12-31','Shenzhen Shekou Port');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-IM-2026-HQ006','91440400MA56LUS01P','1509200000','Automatic Import License','PRT',3000,15000000,'2026-01-01','2026-12-31','Hengqin Port');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-IM-2026-SH007','91110000101123456N','4504900000','Automatic Import License','PRT',1200,14000000,'2026-01-01','2026-12-31','Shanghai Waigaoqiao Port');
INSERT INTO "cn_mofcom_trade_licenses_quotas" VALUES('MOFCOM-IM-2026-QD008','91370200163562681G','4703290000','Automatic Import License','PRT',80000,48000000,'2026-01-01','2026-12-31','Qingdao Dagang Port');
CREATE TABLE cn_outward_fdi_approvals_ndrc (
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
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2011-BJ-001','91110000100001146K','500697256','EDP - Energias de Portugal, S.A. (21.4% Strategic Stake)','M&A Equity Acquisition',3510000000,22464000000,'Energy Grid & Renewables','2011-12-22');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2012-BJ-002','91110000710931234R','503412890','REN - Redes Energéticas Nacionais, SGPS, S.A. (25% Stake)','M&A Equity Acquisition',512000000,3225600000,'National Transmission Grid','2012-02-02');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2014-SH-003','91310000132234561L','500918273','Fidelidade - Companhia de Seguros, S.A. (85% Stake)','M&A Equity Acquisition',1360000000,8432000000,'Financial Services & Insurance','2014-05-15');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2025-JS-004','91320413MA1M9Y2C4B','517890123','CALB Portugal - Gigafábrica Zero-Carbon de Baterias em Sines (15 GWh)','Greenfield Gigafactory',2160000000,15552000000,'New Energy EV Supply Chain','2025-02-10');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2014-SH-005','91310000132234561L','503112244','Luz Saúde, S.A. (Hospital da Luz Acquisition)','M&A Equity Acquisition',610000000,3782000000,'Healthcare Facilities','2014-10-18');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2016-SH-006','91310000132234561L','500998811','Millennium bcp - Banco Comercial Português (29.95% Stake)','M&A Equity Acquisition',1120000000,6944000000,'Banking & Commercial Finance','2016-11-20');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2020-BJ-007','911100007178071858','500191827','Mota-Engil, SGPS, S.A. (32.4% Strategic Equity Stake)','M&A Equity Acquisition',205000000,1312000000,'Global Construction & Infrastructure','2020-11-27');
INSERT INTO "cn_outward_fdi_approvals_ndrc" VALUES('NDRC-ODI-2023-GD-008','91440300192317458F','509887766','Kora Tech Hub Évora - Advanced Automotive R&D Center','Joint Venture',55000000,396000000,'Automotive Software & R&D','2023-04-12');
CREATE TABLE cn_packing_lists_pallet_carton_details (
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
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8801','INV-CN-2026-8801','BRK-CN-SINOTRANS-01','Heavy Duty Steel Skid',250,10000,1936000,2024000,748,'CALB-SINES-PT // UN3480 LITHIUM // KEEP DRY // C/NO 1-250');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8802','INV-CN-2026-8802','BRK-CN-KUEHNE-SZ-03','Heavy Duty Steel Skid',400,400,1748000,1780000,5680,'BYD-CAETANO-PT // RO-RO DECK LASHING // WVTA EU');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8803','INV-CN-2026-8803','BRK-CN-SINOTRANS-01','Fumigated Euro Pallet ISPM-15',2100,70000,4690000,4940000,5920,'EDP-ALENTEJO-SOLAR // FRAGILE PV GLASS // IPPC CN-61001-HT');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8804','INV-CN-2026-8804','BRK-CN-COSCO-LOG-02','Heavy Duty Steel Skid',100,100,680000,710000,540,'REN-GRID-PORTUGAL // CATL ENERC // UN3480 CLASS 9');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8805','INV-CN-2026-8805','BRK-CN-DHL-GLOBAL-04','Export Corrugated Master Carton',45,15000,602200,643100,1406,'WORTEN-LISBOA // XIAOMI 5G // HIGH VALUE ELECTRONICS');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8806','INV-CN-2026-8806','BRK-CN-COSCO-LOG-02','Heavy Duty Steel Skid',320,2485,4971120,5005000,435.5,'MOTA-ENGIL-SINES // S355 STEEL & 6061 ALU // CBAM CERTIFIED');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-CN-2026-8807','INV-CN-2026-8807','BRK-CN-YIWU-RAIL-05','Export Corrugated Master Carton',160,4000,368000,396000,720,'VARZIELA-PORTUGAL // YIXINOU BRI RAIL // COTTON APPAREL');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-PT-2026-9901','INV-PT-2026-9901','BRK-CN-SINOTRANS-01','Reefer Insulated Wine Case',240,30000,270000,504000,410,'COFCO-SHANGHAI // SYMINGTON DOURO & PORT // REEFER +14C');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-PT-2026-9902','INV-PT-2026-9902','BRK-CN-SINOTRANS-01','Fumigated Euro Pallet ISPM-15',180,3000,135000,144000,380,'AMORIM-CORK-PT // SO2 STERILE // FOOD GRADE STOPPER');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-PT-2026-9903','INV-PT-2026-9903','BRK-CN-MACAO-CTS-08','Reefer Insulated Wine Case',210,25000,390000,431000,365,'HENGQIN-LUSOPHONE // SOVENA EXTRA VIRGIN OLIVE OIL');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-PT-2026-9905','INV-PT-2026-9905','BRK-CN-QINGDAO-PORT-07','Reefer Insulated Wine Case',520,32500,1300000,1364000,890,'MAPORAL-PT // CIFER CPRT18000101000505 // KEEP FROZEN -18C');
INSERT INTO "cn_packing_lists_pallet_carton_details" VALUES('PKL-PT-2026-9904','INV-PT-2026-9904','BRK-CN-QINGDAO-PORT-07','Bulk Kraft Pulp Bale',500,4000,4000000,4040000,2850,'NAVIGATOR-PULP-PT // FSC & EUDR CERTIFIED // QINGDAO PORT');
CREATE TABLE cn_post_clearance_audits_anti_smuggling_gacc (
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
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-SH-001','91320413MA1M9Y2C4B','220120260000108801','Shanghai Customs Enterprise Audit Bureau (Jicha)','Export VAT Rebate Authenticity','Compliant - No Adjustment',0,'2026-05-10');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-SZ-002','91440300192317458F','530120260000108802','Shenzhen Customs Post-Clearance Audit Division','Transfer Pricing & Royalties Valuation','Compliant - No Adjustment',0,'2026-05-18');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-SH-003','91110000101123456N','220120261000990001','Shanghai Waigaoqiao Customs Audit Bureau','Transfer Pricing & Royalties Valuation','Voluntary Disclosure Accepted',42500,'2026-05-28');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-SH-004','91110000101123456N','220120261000990005','Shanghai Port Cold-Chain Supervision Bureau','CIFER Cold-Chain Traceability','Compliant - No Adjustment',0,'2026-06-04');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-YW-005','91330782098765432W','292120260000108807','Hangzhou/Yiwu Customs Audit Division','HS Code Misclassification Check','Supplementary Tax Assessed',18400,'2026-06-08');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-NB-006','91330200778899112T','310120260000108806','Ningbo Customs Industrial Metals Audit Team','Export VAT Rebate Authenticity','Compliant - No Adjustment',0,'2026-06-11');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-HQ-007','91440400MA56LUS01P','530420261000990003','Gongbei/Hengqin Customs Bonded Audit Division','CIFER Cold-Chain Traceability','Compliant - No Adjustment',0,'2026-06-14');
INSERT INTO "cn_post_clearance_audits_anti_smuggling_gacc" VALUES('PCA-GACC-2026-QD-008','91370200163562681G','370220261000990007','Qingdao Customs Enterprise Compliance Bureau','Transfer Pricing & Royalties Valuation','Compliant - No Adjustment',0,'2026-06-16');
CREATE TABLE cn_preferential_certificates_of_origin_ccpit (
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
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26320400101','220120260000108801','91320413MA1M9Y2C4B','Non-Preferential CO CCPIT','PSR - Substantial Transformation',86,'CCPIT Jiangsu Sub-Council (Changzhou)','SHA256-9A8B7C6D5E4F3A2B1C0D9E8F7A6B5C4D');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26440300202','530120260000108802','91440300192317458F','Non-Preferential CO CCPIT','PSR - Substantial Transformation',88.3,'CCPIT Shenzhen Municipal Committee','SHA256-1F2E3D4C5B6A79880796857463524130');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('GACC-CO-26610100303','220120260000108803','91610132724912345X','GACC General Certificate of Origin','PE - Produced Exclusively',94.2,'Xi''an Customs District GACC','SHA256-445566778899AABBCCDDEEFF00112233');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26350900404','310120260000108804','91350900587527783P','Non-Preferential CO CCPIT','PSR - Substantial Transformation',91.5,'CCPIT Fujian Sub-Council (Ningde)','SHA256-77889900112233445566778899AABBCC');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26110100505','010120260000108805','91110108551385082Q','Non-Preferential CO CCPIT','PSR - Substantial Transformation',76.4,'CCPIT Beijing Sub-Council','SHA256-AABBCCDDEEFF00112233445566778899');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('GACC-CO-26330200606','310120260000108806','91330200778899112T','GACC General Certificate of Origin','WO - Wholly Obtained',96,'Ningbo Customs District GACC','SHA256-11223344556677889900AABBCCDDEEFF');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26330700707','292120260000108807','91330782098765432W','Non-Preferential CO CCPIT','PE - Produced Exclusively',98.5,'CCPIT Yiwu Chamber of International Commerce','SHA256-99887766554433221100FFEEDDCCBBAA');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26440300808','530120260000108808','91440300618837699Q','Non-Preferential CO CCPIT','PSR - Substantial Transformation',84,'CCPIT Shenzhen Municipal Committee','SHA256-5566778899AABBCC0011223344556677');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('GACC-CO-26440601010','510120260000108810','91440606190342599T','GACC General Certificate of Origin','PE - Produced Exclusively',92,'Foshan Customs District GACC','SHA256-3344556677889900AABBCCDDEEFF1122');
INSERT INTO "cn_preferential_certificates_of_origin_ccpit" VALUES('CCPIT-CO-26110101111','010120260000108811','911100007178071858','Non-Preferential CO CCPIT','PSR - Substantial Transformation',95.1,'CCPIT Beijing Sub-Council','SHA256-6677889900112233445566778899AABB');
CREATE TABLE cn_processing_trade_manuals_handbook (
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
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C23042600001','91320413MA1M9Y2C4B',6,'0615','2836910000','8507600090',0.1392,6420000,'Active Open Manual');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C53012600002','91440300192317458F',2,'0615','8542319000','8703800010',4,12850000,'Active Open Manual');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C35092600003','91350900587527783P',7,'0615','7410110000','8507600090',0.085,4920000,'Verified & Written Off');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C61012600004','91610132724912345X',8,'5034','2804619000','8541430000',0.225,3180000,'Active Open Manual');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C44032600005','91440300618837699Q',2,'0615','8542399000','8504403090',2,5640000,'Verified & Written Off');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C11012600006','91110108551385082Q',1,'0615','8542319000','8517130000',1,8950000,'Active Open Manual');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C44062600007','91440606190342599T',2,'0214','8414301900','8415102100',1,2150000,'Verified & Written Off');
INSERT INTO "cn_processing_trade_manuals_handbook" VALUES('C37022600008','91370200163562681G',10,'5034','8529909090','8528722100',1,1940000,'Pending Bonded Balancing');
CREATE TABLE cn_production_lots_batch_genealogy (
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
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-CALB-2026-03A','CN-SKU-CALB-LFP314',101,'SUP-T2-LI-001','2026-03-05 08:00:00','SHIFT-JINTAN-A1',10000,99.84,'SN-CALB314-202603A');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-BYD-2026-03B','CN-SKU-BYD-SEAL-EV',102,'SUP-T2-GR-003','2026-03-10 06:00:00','SHIFT-PINGSHAN-B2',400,99.5,'VIN-LC0CE4DC-2026B');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-LONGI-2026-04A','CN-SKU-LONGI-HIMO7',104,'SUP-T2-SI-005','2026-03-20 07:30:00','SHIFT-XIAN-PV1',50000,99.91,'SN-LG590W-202604A');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-CATL-2026-04B','CN-SKU-CATL-ENERC',103,'SUP-T2-LI-002','2026-03-28 08:00:00','SHIFT-NINGDE-L1',100,99.95,'SN-ENERC-202604B');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-XM-2026-04C','CN-SKU-XM-15PRO-5G',106,'SUP-T2-GR-008','2026-04-04 09:00:00','SHIFT-CHANGPING-DARK',5000,99.92,'IMEI-86994006-XM15');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-NBST-2026-04D','CN-SKU-NB-STEEL-S355',108,'SUP-T2-ST-007','2026-04-06 00:00:00','SHIFT-BEILUN-BF2',2000,99.6,'HEAT-NBS355-202604D');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-HW-2026-05A','CN-SKU-HW-SUN2000',105,'SUP-T2-RE-006','2026-04-20 08:00:00','SHIFT-SONGSHAN-S3',800,99.88,'SN-HWSUN2000-202605');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-MD-2026-05C','CN-SKU-MIDEA-SPLIT',111,'SUP-T2-RE-006','2026-04-25 07:00:00','SHIFT-SHUNDE-AC1',5000,99.75,'SN-MIDEA12K-202605');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-CRRC-2026-05D','CN-SKU-CRRC-BOGIE',114,'SUP-T2-ST-007','2026-04-28 08:00:00','SHIFT-SIFANG-BG1',80,100,'SN-CRRC-BOGIE-PT26');
INSERT INTO "cn_production_lots_batch_genealogy" VALUES('LOT-BYD-2026-05E','CN-SKU-BYD-ATTO3',102,'SUP-T2-LFP-004','2026-05-01 06:00:00','SHIFT-PINGSHAN-A3',350,99.71,'VIN-LC0CE4CB-ATTO3');
CREATE TABLE cn_products_industrial_catalog (
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
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-CALB-LFP314','91320413MA1M9Y2C4B',101,'8507600090','CALB L314Ah Zero-Carbon LFP Prismatic Module Pack','Lithium-Ion EV & Grid Storage Battery',176,0.068,4850,680,'UN3480 Class 9',142.5);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-BYD-SEAL-EV','91440300192317458F',102,'8703800010','BYD Seal 82.5kWh AWD Blade Battery Electric Sedan','Battery Electric Vehicle (BEV)',4370,14.2,168000,23600,'UN3171 Class 9',6840);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-CATL-ENERC','91350900587527783P',103,'8507600090','CATL EnerC Plus 306Ah Utility-Scale Liquid Cooled Rack','Grid Energy Storage System (ESS)',6800,5.4,245000,34200,'UN3480 Class 9',8920);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-LONGI-HIMO7','91610132724912345X',104,'8541430000','LONGi Hi-MO 7 Bifacial 590W N-Type Solar PV Panel','Solar Photovoltaic Module',65,0.082,520,72.8,NULL,310);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-HW-SUN2000','91440300618837699Q',105,'8504403090','Huawei FusionSolar SUN2000-100KTL-M2 Smart String Inverter','Three-Phase Solar Inverter',184,0.24,18900,2650,NULL,485);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-XM-15PRO-5G','91110108551385082Q',106,'8517130000','Xiaomi 15 Pro 5G 512GB Leica Optics EU Edition','Consumer Electronics Smartphone',0.44,0.0012,3450,485,'UN3481 Class 9',48.2);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-NB-STEEL-S355','91330200778899112T',108,'7225409900','Ningbo S355J2 Wind-Tower Heavy Structural Alloy Steel Plate (1 Ton)','Heavy Structural Steel (CBAM)',2000,0.128,4680,655,NULL,1980);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-NB-ALU-6061','91330200778899112T',108,'7606125900','Ningbo 6061-T6 Aerospace & EV Battery Tray Aluminum Sheet (1 Ton)','Industrial Aluminum Sheet (CBAM)',2000,0.37,19800,2770,NULL,8450);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-YW-APPAREL-LOT','91330782098765432W',107,'6204620000','Yiwu Export Cotton Garment & Retail Assortment Carton (100 pcs)','Textile & Apparel Wholesale',92,0.18,2850,400,NULL,215);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-TRINA-VERTEX','91320400608131370B',110,'8541430000','Trina Solar Vertex N 700W Bifacial TOPCon PV Module','Solar Photovoltaic Module',72,0.091,580,81.2,NULL,295);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-MIDEA-SPLIT','91440606190342599T',111,'8415102100','Midea All-Easy Pro 12000BTU Inverter A+++ Heat Pump Split AC','HVAC Inverter Air Conditioner',68,0.165,2100,294,'UN3363 Class 9',260);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-GREE-SPLIT','91440400192548256N',112,'8415102100','Gree Amber Elite 3.5kW Ultra-Efficient Split AC','HVAC Inverter Air Conditioner',70,0.17,2250,315,'UN3363 Class 9',275);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-HAIER-TV65','91370200163562681G',113,'8528722100','Haier 65-inch 4K QD-MiniLED Smart Google TV','Consumer Electronics TV',48,0.22,3200,448,NULL,190);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-CRRC-BOGIE','911100007178071858',114,'8607191000','CRRC High-Floor Metro Bogie Set with Traction Motors','Rail Transit Bogie Assembly',14500,12.5,385000,53900,NULL,12500);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-XM-BOOKPRO','91110108551385082Q',106,'8471300000','Xiaomi Book Pro 16 Intel Ultra-7 OLED Slim Laptop','Consumer Electronics Laptop',3.8,0.0085,6200,868,'UN3481 Class 9',85);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-BYD-ATTO3','91440300192317458F',102,'8703800010','BYD Atto 3 60.5kWh Blade Battery Compact Electric SUV','Battery Electric Vehicle (BEV)',3780,13.8,142000,19880,'UN3171 Class 9',5920);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-HW-5G-AAU','91440300618837699Q',105,'8504403090','Huawei 5G Massive MIMO AAU5613 Active Antenna Unit','Telecommunications Equipment',84,0.115,32500,4550,NULL,410);
INSERT INTO "cn_products_industrial_catalog" VALUES('CN-SKU-YW-TOYS-LOT','91330782098765432W',107,'9503002100','Yiwu Educational Plastic Building Block Toy Assortment','Children Educational Toys',60,0.14,1850,259,NULL,110);
CREATE TABLE cn_provinces_prefectures_cities (
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
INSERT INTO "cn_provinces_prefectures_cities" VALUES('310000','Shanghai Municipality','上海市','Shanghai','Yangtze River Delta',4721.87,14.2,14820);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('440300','Guangdong Province','广东省深圳市','Shenzhen','Pearl River Delta / Greater Bay Area',3460.64,18.5,14250);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('440100','Guangdong Province','广东省广州市','Guangzhou','Pearl River Delta / Greater Bay Area',3035.57,11.4,12680);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('440400','Guangdong Province','广东省珠海市','Zhuhai (Hengqin)','Pearl River Delta / Greater Bay Area',423.32,4.1,11950);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('440600','Guangdong Province','广东省佛山市','Foshan (Shunde)','Pearl River Delta / Greater Bay Area',1268.45,9.5,11800);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('330200','Zhejiang Province','浙江省宁波市','Ningbo','Yangtze River Delta',1645.28,9.8,12300);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('330100','Zhejiang Province','浙江省杭州市','Hangzhou','Yangtze River Delta',2005.9,12.4,13100);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('330782','Zhejiang Province','浙江省义乌市','Yiwu (Jinhua)','Yangtze River Delta',205.56,7.6,10850);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('320400','Jiangsu Province','江苏省常州市','Changzhou','Yangtze River Delta',1011.64,8.2,11900);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('320100','Jiangsu Province','江苏省南京市','Nanjing','Yangtze River Delta',1742.14,9.4,12850);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('320500','Jiangsu Province','江苏省苏州市','Suzhou','Yangtze River Delta',2465.34,12.8,13600);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('350900','Fujian Province','福建省宁德市','Ningde','Pearl River Delta / Greater Bay Area',380.73,5.4,10900);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('350200','Fujian Province','福建省厦门市','Xiamen','Pearl River Delta / Greater Bay Area',806.64,5.3,11750);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('610100','Shaanxi Province','陕西省西安市','Xi''an','Western China',1201.08,4.5,10200);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('370200','Shandong Province','山东省青岛市','Qingdao','Bohai Economic Rim',1576.03,6.7,11100);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('110000','Beijing Municipality','北京市','Beijing','Bohai Economic Rim',4376.07,5.8,15400);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('120000','Tianjin Municipality','天津市','Tianjin','Bohai Economic Rim',1673.72,7.2,11600);
INSERT INTO "cn_provinces_prefectures_cities" VALUES('820000','Macao SAR','澳门特别行政区','Macao','Special Administrative Region',345.4,3.8,18500);
CREATE TABLE cn_raw_materials_tier2_suppliers (
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
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-LI-001','91360500716598112A','Ganfeng Lithium Group Co., Ltd. (Jiangxi Refining)','320400','Battery Grade Lithium Carbonate','Xinyu & Yichun Spodumene Refinery, Jiangxi',120000,1,5.42);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-LI-002','91510900206360118B','Tianqi Lithium Corporation (Sichuan Battery Grade)','350900','Battery Grade Lithium Carbonate','Suining & Shehong Lithium Plant, Sichuan',95000,1,5.18);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-GR-003','91440300723041998C','BTR New Material Group Co., Ltd. (Shenzhen Anode)','440300','Anode Spherical Graphite','Guangming High-Tech Park, Shenzhen',180000,1,3.85);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-LFP-004','91320413MA1W88210D','Hunan Yuneng New Energy Battery Material Co., Ltd.','320400','Cathode LFP Precursor','Changzhou Jintan Cathode Industrial Park',210000,1,4.12);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-SI-005','91510100679680114E','Tongwei Solar & Yongxiang Polysilicon Co., Ltd.','610100','Solar Grade Polysilicon','Leshan High-Purity Crystalline Silicon Base',350000,1,8.95);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-RE-006','91150200701465882F','China Northern Rare Earth (Group) High-Tech Co., Ltd.','110000','Rare Earth Neodymium Magnets','Bayan Obo Rare Earth Complex, Baotou',65000,1,11.2);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-ST-007','91310000132200821G','Baoshan Iron & Steel Co., Ltd. (Baosteel Automotive)','310000','Automotive Grade Steel Coil','Baoshan Special Steel Works, Shanghai',850000,1,1.89);
INSERT INTO "cn_raw_materials_tier2_suppliers" VALUES('SUP-T2-GR-008','91310000607388192H','Shanghai Putailai New Energy Technology Co., Ltd.','310000','Anode Spherical Graphite','Pudong Jinqiao Anode Coating Base, Shanghai',140000,1,3.62);
CREATE TABLE cn_special_economic_ftz_zones (
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
INSERT INTO "cn_special_economic_ftz_zones" VALUES(1,'CN-SH-WAIGAOQIAO','Shanghai Waigaoqiao Free Trade Zone','310000','Pilot FTZ',15,2,'2013-09-29');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(2,'CN-GD-QIANHAI','Shenzhen Qianhai Shekou Pilot FTZ','440300','Special Economic Zone',15,1.5,'2015-04-27');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(3,'CN-GD-HENGQIN-MO','Hengqin Guangdong-Macao In-Depth Cooperation Zone','440400','Lusophone In-Depth Cooperation Zone',15,3,'2021-09-17');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(4,'CN-ZJ-NINGBO-CBZ','Ningbo Meishan Comprehensive Bonded Zone','330200','Comprehensive Bonded Zone',20,2,'2010-02-24');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(5,'CN-ZJ-YIWU-CBEC','Yiwu Cross-Border E-Commerce Comprehensive Pilot Zone','330782','Cross-Border E-Commerce Pilot Zone',15,4,'2018-07-24');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(6,'CN-JS-CHANGZHOU-HI','Changzhou National High-Tech Industrial Zone (New Energy)','320400','Pilot FTZ',15,2.5,'2015-01-15');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(7,'CN-FJ-NINGDE-BATT','Ningde Lithium-Ion Battery Special Industrial Zone','350900','Special Economic Zone',15,2.5,'2017-06-01');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(8,'CN-SN-XIAN-LANDPORT','Xi''an International Inland Port Bonded Zone (BRI Rail)','610100','Comprehensive Bonded Zone',15,2,'2014-03-12');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(9,'CN-GD-NANSHA-CBZ','Guangzhou Nansha Comprehensive Bonded Zone','440100','Comprehensive Bonded Zone',15,2,'2020-07-15');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(10,'CN-SD-QINGDAO-FTZ','Qingdao Qianwan Comprehensive Bonded Zone','370200','Comprehensive Bonded Zone',15,2,'2019-08-30');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(11,'CN-TJ-DONGLI-CBZ','Tianjin Port Free Trade Zone (Airport Logistics)','120000','Pilot FTZ',15,2,'2015-04-21');
INSERT INTO "cn_special_economic_ftz_zones" VALUES(12,'CN-ZJ-HANGZHOU-CROSS','Hangzhou Cross-Border E-Commerce Comprehensive Pilot Area','330100','Cross-Border E-Commerce Pilot Zone',15,3.5,'2015-03-07');
CREATE TABLE cn_state_industrial_subsidies (
    subsidy_grant_id INTEGER PRIMARY KEY,
    recipient_uscc CHAR(18) NOT NULL,
    granting_authority VARCHAR(100) NOT NULL,
    program_category VARCHAR(60) NOT NULL,
    fiscal_year SMALLINT NOT NULL CHECK (fiscal_year BETWEEN 2020 AND 2030),
    subsidy_amount_cny NUMERIC(14,2) NOT NULL CHECK (subsidy_amount_cny > 0),
    disbursement_date DATE NOT NULL,
    FOREIGN KEY (recipient_uscc) REFERENCES cn_enterprises_manufacturers(uscc_code)
);
INSERT INTO "cn_state_industrial_subsidies" VALUES(1,'91320413MA1M9Y2C4B','MIIT & Jiangsu Provincial New Energy Fund','EV & Battery Innovation Grant',2025,185000000,'2025-09-15');
INSERT INTO "cn_state_industrial_subsidies" VALUES(2,'91440300192317458F','Shenzhen Municipal NEV Global Expansion Program','EV & Battery Innovation Grant',2025,310000000,'2025-11-20');
INSERT INTO "cn_state_industrial_subsidies" VALUES(3,'91610132724912345X','Shaanxi Clean Tech Manufacturing Upgrade','Photovoltaic Export Support',2025,95000000,'2025-08-10');
INSERT INTO "cn_state_industrial_subsidies" VALUES(4,'91330782098765432W','Yiwu Municipal BRI China-Europe Railway Express Fund','Belt & Road Rail Freight Subsidy',2026,18500000,'2026-02-01');
INSERT INTO "cn_state_industrial_subsidies" VALUES(5,'91330200778899112T','Zhejiang Industrial Decarbonization Fund','Green Factory Upgrade',2026,24000000,'2026-01-18');
INSERT INTO "cn_state_industrial_subsidies" VALUES(6,'91350900587527783P','Fujian Energy Storage Technology Development Grant','Grid Storage R&D Grant',2025,120000000,'2025-10-15');
INSERT INTO "cn_state_industrial_subsidies" VALUES(7,'91320400608131370B','Jiangsu High-Efficiency Photovoltaic Innovation Program','Photovoltaic Export Support',2025,65000000,'2025-07-22');
INSERT INTO "cn_state_industrial_subsidies" VALUES(8,'91440300618837699Q','Guangdong Provincial Smart Grid R&D Incentive','Renewable Electronics Grant',2025,88000000,'2025-12-05');
INSERT INTO "cn_state_industrial_subsidies" VALUES(9,'91440606190342599T','Guangdong Green Appliance Export Decarbonization Subsidy','Eco-Design & Energy Efficiency',2026,32000000,'2026-01-25');
INSERT INTO "cn_state_industrial_subsidies" VALUES(10,'911100007178071858','National Rail Transit Core Technology Breakthrough Special Fund','Rail Traction Systems Innovation',2025,150000000,'2025-06-30');
CREATE TABLE cn_vat_export_tax_rebates_sta (
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
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-001','220120260000108801','91320413MA1M9Y2C4B','FAPIAO-3204-2026-8801',47858400,9,4307256,'Approved & Credited','2026-04-15');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-002','530120260000108802','91440300192317458F','FAPIAO-4403-2026-8802',73820800,13,9596704,'Approved & Credited','2026-04-20');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-003','220120260000108803','91610132724912345X','FAPIAO-6101-2026-8803',26244400,9,2361996,'Approved & Credited','2026-04-28');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-004','310120260000108804','91350900587527783P','FAPIAO-3509-2026-8804',26795700,9,2411613,'Approved & Credited','2026-05-05');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-005','010120260000108805','91110108551385082Q','FAPIAO-1101-2026-8805',19012000,13,2471560,'Approved & Credited','2026-05-10');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-006','310120260000108806','91330200778899112T','FAPIAO-3302-2026-8806',19169100,0,0,'Denied','2026-05-15');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-007','292120260000108807','91330782098765432W','FAPIAO-3307-2026-8807',7125000,13,926250,'Under Audit','2026-05-28');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-008','530120260000108808','91440300618837699Q','FAPIAO-4403-2026-8808',14425600,13,1875328,'Approved & Credited','2026-06-02');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-009','010120260000108809','91110108551385082Q','FAPIAO-1101-2026-8809',25088000,13,3261440,'Approved & Credited','2026-06-05');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-010','510120260000108810','91440606190342599T','FAPIAO-4406-2026-8810',11368000,13,1477840,'Approved & Credited','2026-06-08');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-011','010120260000108811','911100007178071858','FAPIAO-1101-2026-8811',32536000,13,4229680,'Approved & Credited','2026-06-12');
INSERT INTO "cn_vat_export_tax_rebates_sta" VALUES('STA-REB-2026-013','530120260000108813','91440300192317458F','FAPIAO-4403-2026-8813',70168000,13,9121840,'Approved & Credited','2026-06-16');
CREATE INDEX idx_cn_hs_wco6 ON cn_hs_tariff_schedule_gacc(hs_code_6_wco);
CREATE INDEX idx_cn_contracts_pt_eori ON cn_b2b_commercial_contracts(portuguese_counterparty_eori);
CREATE INDEX idx_cn_export_bl ON cn_customs_export_declarations_gacc(bill_of_lading_or_waybill_no);
CREATE INDEX idx_cn_import_bl ON cn_customs_import_declarations_gacc(bill_of_lading_no);
CREATE INDEX idx_cn_fx_uetr ON cn_fx_settlements_pboc_safe(swift_uetr_or_cips_id);
CREATE INDEX idx_cn_fdi_pt_nif ON cn_outward_fdi_approvals_ndrc(target_pt_company_nif);
CREATE INDEX idx_cn_lc_contract ON cn_letters_of_credit_ucp600_swift(contract_no_cn);
CREATE INDEX idx_cn_packing_inv ON cn_packing_lists_pallet_carton_details(invoice_no);
CREATE INDEX idx_cn_aeo_pt_eori ON cn_gacc_aeo_mutual_recognition_registry(eu_partner_eori_pt);
COMMIT;
