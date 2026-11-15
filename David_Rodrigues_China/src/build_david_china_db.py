#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
UNIVERSIDADE DO ALGARVE - MSc in Informatics Engineering (2026/2027)
Course: Data Modelling and Integration (DMI) - Project P1
Student: David Rodrigues (Subtopic: China Industrial, Customs & Logistics)
Script: build_david_china_db.py
Description:
  1. Creates and heavily populates Source D1 (Structured Relational Database -
     20 SQL tables in 3NF) with real and high-fidelity bilateral China-Portugal
     trade, customs, enterprise, and financial data.
  2. Exports a PostgreSQL-compatible SQL dump and a live SQLite3 database.
  3. Generates Source D2 (Semi-Structured XML Database - 12 XML Containers)
     and validates all 12 XML files against models/china_logistics_trade.xsd.
===============================================================================
"""

import os
import sqlite3
import subprocess
import json
import sys
from pathlib import Path

# Add src to path for modular data import
SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import david_sql_data
import david_xml_data

BASE_DIR = SRC_DIR.parent
SCHEMA_SQL_PATH = BASE_DIR / "database" / "schema_postgres_3nf.sql"
SQLITE_DB_PATH = BASE_DIR / "data" / "relational_db" / "china_gacc_mofcom_3nf.sqlite"
SQL_DUMP_PATH = BASE_DIR / "data" / "relational_db" / "china_gacc_mofcom_dump.sql"
XML_DIR = BASE_DIR / "data" / "xml_containers"
XSD_PATH = BASE_DIR / "models" / "china_logistics_trade.xsd"


def build_structured_relational_db():
    """Creates and populates all 20 relational SQL tables (Tables 33 to 52)."""
    SQLITE_DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if SQLITE_DB_PATH.exists():
        SQLITE_DB_PATH.unlink()

    conn = sqlite3.connect(str(SQLITE_DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON;")
    cursor = conn.cursor()

    with open(SCHEMA_SQL_PATH, "r", encoding="utf-8") as f:
        schema_sql = f.read()
    cursor.executescript(schema_sql)

    sql_data = david_sql_data.get_sql_data()

    # 33. cn_provinces_prefectures_cities (8 cols)
    cursor.executemany("INSERT INTO cn_provinces_prefectures_cities VALUES (?,?,?,?,?,?,?,?)", sql_data["provinces"])

    # 34. cn_special_economic_ftz_zones (8 cols)
    cursor.executemany("INSERT INTO cn_special_economic_ftz_zones VALUES (?,?,?,?,?,?,?,?)", sql_data["zones"])

    # 35. cn_enterprises_manufacturers (11 cols)
    cursor.executemany("INSERT INTO cn_enterprises_manufacturers VALUES (?,?,?,?,?,?,?,?,?,?,?)", sql_data["enterprises"])

    # 36. cn_factory_production_facilities (13 cols)
    cursor.executemany("INSERT INTO cn_factory_production_facilities VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["facilities"])

    # 37. cn_hs_tariff_schedule_gacc (11 cols)
    cursor.executemany("INSERT INTO cn_hs_tariff_schedule_gacc VALUES (?,?,?,?,?,?,?,?,?,?,?)", sql_data["hs_codes"])

    # 38. cn_products_industrial_catalog (12 cols)
    cursor.executemany("INSERT INTO cn_products_industrial_catalog VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["products"])

    # 39. cn_ccc_compulsory_certifications (9 cols)
    cursor.executemany("INSERT INTO cn_ccc_compulsory_certifications VALUES (?,?,?,?,?,?,?,?,?)", sql_data["ccc_certs"])

    # 40. cn_mofcom_trade_licenses_quotas (10 cols)
    cursor.executemany("INSERT INTO cn_mofcom_trade_licenses_quotas VALUES (?,?,?,?,?,?,?,?,?,?)", sql_data["mofcom_licenses"])

    # 41. cn_b2b_commercial_contracts (11 cols)
    cursor.executemany("INSERT INTO cn_b2b_commercial_contracts VALUES (?,?,?,?,?,?,?,?,?,?,?)", sql_data["contracts"])

    # 42. cn_commercial_invoices (11 cols)
    cursor.executemany("INSERT INTO cn_commercial_invoices VALUES (?,?,?,?,?,?,?,?,?,?,?)", sql_data["invoices"])

    # 43. cn_commercial_invoice_lines (12 cols)
    cursor.executemany("INSERT INTO cn_commercial_invoice_lines VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["invoice_lines"])

    # 44. cn_customs_export_declarations_gacc (13 cols)
    cursor.executemany("INSERT INTO cn_customs_export_declarations_gacc VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["gacc_exports"])

    # 45. cn_customs_import_declarations_gacc (13 cols)
    cursor.executemany("INSERT INTO cn_customs_import_declarations_gacc VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["gacc_imports"])

    # 46. cn_ciq_inspection_quarantine_records (11 cols)
    cursor.executemany("INSERT INTO cn_ciq_inspection_quarantine_records VALUES (?,?,?,?,?,?,?,?,?,?,?)", sql_data["ciq_records"])

    # 47. cn_vat_export_tax_rebates_sta (9 cols)
    cursor.executemany("INSERT INTO cn_vat_export_tax_rebates_sta VALUES (?,?,?,?,?,?,?,?,?)", sql_data["vat_rebates"])

    # 48. cn_fx_settlements_pboc_safe (12 cols)
    cursor.executemany("INSERT INTO cn_fx_settlements_pboc_safe VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["fx_settlements"])

    # 49. cn_cargo_insurance_policies_sinosure (9 cols)
    cursor.executemany("INSERT INTO cn_cargo_insurance_policies_sinosure VALUES (?,?,?,?,?,?,?,?,?)", sql_data["insurances"])

    # 50. cn_state_industrial_subsidies (7 cols)
    cursor.executemany("INSERT INTO cn_state_industrial_subsidies VALUES (?,?,?,?,?,?,?)", sql_data["subsidies"])

    # 51. cn_outward_fdi_approvals_ndrc (9 cols)
    cursor.executemany("INSERT INTO cn_outward_fdi_approvals_ndrc VALUES (?,?,?,?,?,?,?,?,?)", sql_data["fdi_approvals"])

    # 52. cn_green_manufacturing_esg_audits (9 cols)
    cursor.executemany("INSERT INTO cn_green_manufacturing_esg_audits VALUES (?,?,?,?,?,?,?,?,?)", sql_data["esg_audits"])

    # 91. cn_raw_materials_tier2_suppliers (9 cols)
    cursor.executemany("INSERT INTO cn_raw_materials_tier2_suppliers VALUES (?,?,?,?,?,?,?,?,?)", sql_data["tier2_suppliers"])

    # 92. cn_production_lots_batch_genealogy (9 cols)
    cursor.executemany("INSERT INTO cn_production_lots_batch_genealogy VALUES (?,?,?,?,?,?,?,?,?)", sql_data["production_lots"])

    # 93. cn_bill_of_materials_bom_structures (8 cols)
    cursor.executemany("INSERT INTO cn_bill_of_materials_bom_structures VALUES (?,?,?,?,?,?,?,?)", sql_data["bom_structures"])

    # 94. cn_letters_of_credit_ucp600_swift (12 cols)
    cursor.executemany("INSERT INTO cn_letters_of_credit_ucp600_swift VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", sql_data["letters_of_credit"])

    # 95. cn_lc_documentary_presentations_discrepancies (9 cols)
    cursor.executemany("INSERT INTO cn_lc_documentary_presentations_discrepancies VALUES (?,?,?,?,?,?,?,?,?)", sql_data["lc_presentations"])

    # 96. cn_hk_macao_offshore_trading_intermediaries (9 cols)
    cursor.executemany("INSERT INTO cn_hk_macao_offshore_trading_intermediaries VALUES (?,?,?,?,?,?,?,?,?)", sql_data["offshore_intermediaries"])

    # 97. cn_freight_forwarders_nvocc_customs_brokers (8 cols)
    cursor.executemany("INSERT INTO cn_freight_forwarders_nvocc_customs_brokers VALUES (?,?,?,?,?,?,?,?)", sql_data["freight_forwarders"])

    # 98. cn_packing_lists_pallet_carton_details (10 cols)
    cursor.executemany("INSERT INTO cn_packing_lists_pallet_carton_details VALUES (?,?,?,?,?,?,?,?,?,?)", sql_data["packing_lists"])

    # 99. cn_processing_trade_manuals_handbook (9 cols)
    cursor.executemany("INSERT INTO cn_processing_trade_manuals_handbook VALUES (?,?,?,?,?,?,?,?,?)", sql_data["processing_manuals"])

    # 100. cn_gacc_aeo_mutual_recognition_registry (8 cols)
    cursor.executemany("INSERT INTO cn_gacc_aeo_mutual_recognition_registry VALUES (?,?,?,?,?,?,?,?)", sql_data["aeo_mra_registry"])

    # 101. cn_export_control_dual_use_mofcom_permits (9 cols)
    cursor.executemany("INSERT INTO cn_export_control_dual_use_mofcom_permits VALUES (?,?,?,?,?,?,?,?,?)", sql_data["dual_use_permits"])

    # 102. cn_preferential_certificates_of_origin_ccpit (8 cols)
    cursor.executemany("INSERT INTO cn_preferential_certificates_of_origin_ccpit VALUES (?,?,?,?,?,?,?,?)", sql_data["certificates_of_origin"])

    # 103. cn_customs_tariff_quotas_antidumping_mofcom (8 cols)
    cursor.executemany("INSERT INTO cn_customs_tariff_quotas_antidumping_mofcom VALUES (?,?,?,?,?,?,?,?)", sql_data["mofcom_measures"])

    # 104. cn_customs_tax_guarantees_consolidated_bonds (8 cols)
    cursor.executemany("INSERT INTO cn_customs_tax_guarantees_consolidated_bonds VALUES (?,?,?,?,?,?,?,?)", sql_data["customs_bonds"])

    # 105. cn_advance_rulings_classification_valuation_gacc (8 cols)
    cursor.executemany("INSERT INTO cn_advance_rulings_classification_valuation_gacc VALUES (?,?,?,?,?,?,?,?)", sql_data["advance_rulings"])

    # 106. cn_post_clearance_audits_anti_smuggling_gacc (8 cols)
    cursor.executemany("INSERT INTO cn_post_clearance_audits_anti_smuggling_gacc VALUES (?,?,?,?,?,?,?,?)", sql_data["post_clearance_audits"])

    # 107. cn_excise_consumption_tax_sta (8 cols)
    cursor.executemany("INSERT INTO cn_excise_consumption_tax_sta VALUES (?,?,?,?,?,?,?,?)", sql_data["consumption_taxes"])

    # 108. cn_ipr_customs_protection_recordations (8 cols)
    cursor.executemany("INSERT INTO cn_ipr_customs_protection_recordations VALUES (?,?,?,?,?,?,?,?)", sql_data["ipr_recordations"])

    conn.commit()

    # Generate SQL dump
    with open(SQL_DUMP_PATH, "w", encoding="utf-8") as f_dump:
        f_dump.write("-- =============================================================================\n")
        f_dump.write("-- CHINA GACC & MOFCOM 3NF RELATIONAL DATABASE DUMP (POSTGRESQL / SQLITE)\n")
        f_dump.write("-- MSc in Informatics Engineering - Data Modelling & Integration (DMI)\n")
        f_dump.write("-- Student: David Rodrigues (2026/2027)\n")
        f_dump.write("-- =============================================================================\n\n")
        for line in conn.iterdump():
            f_dump.write(f"{line}\n")

    conn.close()
    print(f"[SQL 3NF OK] Populated 38 Relational Tables -> {SQLITE_DB_PATH} ({SQL_DUMP_PATH})")


def build_semi_structured_xml_containers():
    """Generates all 12 XML Containers (Tables 53 to 64) and validates against XSD."""
    XML_DIR.mkdir(parents=True, exist_ok=True)
    containers = david_xml_data.get_xml_containers()

    xml_files_created = []
    for fname, content in containers.items():
        fpath = XML_DIR / fname
        fpath.write_text(content.strip() + "\n", encoding="utf-8")
        xml_files_created.append(fpath)

    # Validate all 12 XML files against XSD using xmllint
    for xml_path in xml_files_created:
        res = subprocess.run(
            ["xmllint", "--noout", "--schema", str(XSD_PATH), str(xml_path)],
            capture_output=True,
            text=True,
        )
        if res.returncode != 0:
            raise RuntimeError(f"XSD validation failed for {xml_path.name}:\n{res.stderr}")
        print(f"[XSD VALIDATED] {xml_path.name}")

    print(f"[XML CONTAINERS OK] Created and strictly validated {len(xml_files_created)} BaseX XML containers.")


if __name__ == "__main__":
    build_structured_relational_db()
    build_semi_structured_xml_containers()
    print("\n=== DAVID RODRIGUES (CHINA) DATABASES BUILT & VALIDATED SUCCESSFULLY ===")
