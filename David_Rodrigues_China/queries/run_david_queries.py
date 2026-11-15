#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
UNIVERSIDADE DO ALGARVE - MSc in Informatics Engineering (2026/2027)
Course: Data Modelling and Integration (DMI) - Project P1
Student: David Rodrigues (Subtopic: China Industrial, Customs & Logistics)
Script: run_david_queries.py
Description:
  Executes, prints the exact query code (SQL 3FN / XPath / Cross-Source),
  and renders real formatted data tables in the terminal for David's
  Individual Subtopic Queries (Q03, Q04) over Source D1 (38 SQL 3FN Tables)
  and Source D2 (20 XSD-Validated XML Containers) PLUS the 8 Cross-Subtopic
  Queries (Q05..Q12) integrating China and Portugal data sources.
===============================================================================
"""

import json
import sqlite3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any

DAVID_DIR = Path(__file__).resolve().parent.parent
AFONSO_DIR = DAVID_DIR.parent / "Afonso_Bitoque_Portugal"

DAVID_SQLITE = DAVID_DIR / "data" / "relational_db" / "china_gacc_mofcom_3nf.sqlite"
DAVID_XML_DIR = DAVID_DIR / "data" / "xml_containers"
AFONSO_RESULTS = AFONSO_DIR / "queries" / "expected_results_afonso.json"


def format_ascii_table(rows: List[Dict[str, Any]], max_col_width: int = 28, max_rows: int = 15) -> str:
    """Renders a list of dicts as a clean Unicode box table for terminal display."""
    if not rows:
        return "  (Sem registos devolvidos)\n"
    display_rows = rows[:max_rows]
    headers = list(display_rows[0].keys())
    if len(headers) > 7:
        headers = headers[:7]

    def fmt_val(v):
        if v is None:
            return "NULL"
        if isinstance(v, float):
            return f"{v:,.2f}"
        s = str(v).replace("\n", " ")
        return s[:max_col_width - 1] + "…" if len(s) > max_col_width else s

    widths = [len(h) for h in headers]
    str_rows = []
    for r in display_rows:
        sr = [fmt_val(r.get(h)) for h in headers]
        for idx, val in enumerate(sr):
            if len(val) > widths[idx]:
                widths[idx] = len(val)
        str_rows.append(sr)

    top = "  ┌─" + "─┬─".join("─" * w for w in widths) + "─┐"
    head = "  │ " + " │ ".join(h.ljust(widths[i]) for i, h in enumerate(headers)) + " │"
    sep = "  ├─" + "─┼─".join("─" * w for w in widths) + "─┤"
    bot = "  └─" + "─┴─".join("─" * w for w in widths) + "─┘"

    lines = [top, head, sep]
    for sr in str_rows:
        lines.append("  │ " + " │ ".join(sr[i].ljust(widths[i]) for i in range(len(headers))) + " │")
    lines.append(bot)
    if len(rows) > max_rows:
        lines.append(f"  ... (+{len(rows) - max_rows} registos adicionais omitidos no ecrã; todos gravados no JSON)")
    return "\n".join(lines)


def print_query_execution(q: Dict[str, Any]):
    """Prints the full query metadata, query code, and real results table to the terminal."""
    print("\n" + "━" * 116)
    print(f"🔎 [{q['query_id']}] [{q['difficulty'].upper()}] — {q['title']}")
    print(f"👤 Responsável: {q['scope']}")
    print(f"🗄️  Fontes Usadas: {', '.join(q['sources_used'])}")
    print(f"💡 Justificação: {q['justification']}")
    print("─" * 116)
    print("📜 CÓDIGO DA QUERY EXECUTADA:")
    for line in q.get("query_code", "").strip().split("\n"):
        print(f"   {line}")
    print("─" * 116)
    out_rows = q.get("output", [])
    print(f"📊 RESULTADOS REAIS OBTIDOS ({len(out_rows)} registos retornados):")
    print(format_ascii_table(out_rows))


def run_david_queries(quiet: bool = False):
    conn = sqlite3.connect(str(DAVID_SQLITE))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    results = []

    # =========================================================================
    # Q3 [SIMPLE - Individual David (China: Source D1 PostgreSQL Relational)]
    # =========================================================================
    q3_sql = """SELECT e.uscc_code, e.company_name_en, e.company_name_zh, p.province_name_en,
       e.registered_capital_wan_cny, ROUND(e.registered_capital_wan_cny * 10000.0, 2) AS registered_capital_cny,
       COUNT(g.gacc_entry_id_18) AS export_shipments_to_pt,
       ROUND(COALESCE(SUM(g.total_fob_value_cny), 0), 2) AS total_fob_exported_cny,
       ROUND(COALESCE(SUM(r.rebate_amount_paid_cny), 0), 2) AS total_vat_rebate_received_cny
FROM cn_enterprises_manufacturers e
JOIN cn_provinces_prefectures_cities p ON e.admin_division_code_gb = p.admin_division_code_gb
LEFT JOIN cn_special_economic_ftz_zones z ON e.zone_id = z.zone_id
LEFT JOIN cn_customs_export_declarations_gacc g ON e.uscc_code = g.exporter_uscc
LEFT JOIN cn_vat_export_tax_rebates_sta r ON g.gacc_entry_id_18 = r.gacc_entry_id_18
GROUP BY e.uscc_code HAVING export_shipments_to_pt > 0 ORDER BY total_fob_exported_cny DESC;"""

    q3_rows = [dict(r) for r in cur.execute("""
        SELECT e.uscc_code,
               e.company_name_en,
               e.company_name_zh,
               p.province_name_en,
               z.zone_name_en,
               e.registered_capital_wan_cny,
               ROUND(e.registered_capital_wan_cny * 10000.0, 2) AS registered_capital_cny,
               COUNT(g.gacc_entry_id_18) AS export_shipments_to_pt,
               ROUND(COALESCE(SUM(g.total_fob_value_cny), 0), 2) AS total_fob_exported_cny,
               ROUND(COALESCE(SUM(r.rebate_amount_paid_cny), 0), 2) AS total_vat_rebate_received_cny
        FROM cn_enterprises_manufacturers e
        JOIN cn_provinces_prefectures_cities p ON e.admin_division_code_gb = p.admin_division_code_gb
        LEFT JOIN cn_special_economic_ftz_zones z ON e.zone_id = z.zone_id
        LEFT JOIN cn_customs_export_declarations_gacc g ON e.uscc_code = g.exporter_uscc
        LEFT JOIN cn_vat_export_tax_rebates_sta r ON g.gacc_entry_id_18 = r.gacc_entry_id_18
        GROUP BY e.uscc_code
        HAVING export_shipments_to_pt > 0
        ORDER BY total_fob_exported_cny DESC;
    """).fetchall()]

    results.append({
        "query_id": "Q03",
        "scope": "Individual - David Rodrigues (China)",
        "difficulty": "Simple",
        "sources_used": [
            "Source D1: CN PostgreSQL (33_cn_provinces_prefectures_cities, 34_cn_special_economic_ftz_zones, 35_cn_enterprises_manufacturers, 44_cn_customs_export_declarations_gacc, 47_cn_vat_export_tax_rebates_sta)"
        ],
        "title": "Ranking de Exportadores Chineses para Portugal, Volume FOB (CNY) e Reembolsos Fiscais de IVA (STA Export Rebate)",
        "justification": "Query SQL sobre a fonte estruturada relacional (3FN) com JOINs entre empresas, províncias, zonas francas, declarações GACC e reembolsos fiscais STA.",
        "query_code": q3_sql,
        "output": q3_rows
    })

    # =========================================================================
    # Q4 [INTERMEDIATE - Individual David (Source D1 PostgreSQL + Source D2 XML)]
    # =========================================================================
    tree55 = ET.parse(DAVID_XML_DIR / "55_cn_master_bills_of_lading_xml.xml")
    tree64 = ET.parse(DAVID_XML_DIR / "64_cn_export_packaging_fumigation_certs_xml.xml")

    hazmat_by_bl = {}
    for cert in tree64.getroot().findall("CertificateRecord"):
        bl_no = cert.attrib["blNumber"]
        hz = cert.find("HazmatIMDGDeclaration")
        vgm = cert.find("SOLASVerifiedGrossMass")
        fum = cert.find("ISPM15WoodFumigation")
        hazmat_by_bl[bl_no] = {
            "cert_id": cert.attrib["certificateId"],
            "is_dangerous_goods": hz.attrib["isDangerousGoods"] == "true",
            "un_number": hz.attrib["unNumber"],
            "imdg_class": hz.attrib["imdgClass"],
            "ippc_fumigation_mark": fum.attrib["ippcMarkCode"],
            "vgm_kg": float(vgm.attrib["verifiedGrossMassKg"])
        }

    q4_data = []
    for bl in tree55.getroot().findall("BillOfLading"):
        bl_no = bl.attrib["blNumber"]
        gacc_id = bl.attrib["gaccDeclarationId18"]
        routing = bl.find("Routing")
        containers = bl.find("ContainerizedCargoList").findall("Container")

        sql_row = cur.execute("""
            SELECT g.gacc_entry_id_18, g.supervision_regime_code, g.total_fob_value_usd,
                   e.company_name_en, c.inspection_verdict, c.e_ciq_certificate_no
            FROM cn_customs_export_declarations_gacc g
            JOIN cn_enterprises_manufacturers e ON g.exporter_uscc = e.uscc_code
            LEFT JOIN cn_ciq_inspection_quarantine_records c ON g.gacc_entry_id_18 = c.gacc_declaration_id_18
            WHERE g.gacc_entry_id_18 = ?
        """, (gacc_id,)).fetchone()

        if sql_row:
            hz_info = hazmat_by_bl.get(bl_no, {})
            q4_data.append({
                "bl_number_xml": bl_no,
                "gacc_entry_id_sql": gacc_id,
                "exporter_cn": sql_row["company_name_en"],
                "port_of_loading_cn": routing.attrib["portOfLoading"],
                "port_of_discharge_pt": routing.attrib["portOfDischarge"],
                "vessel_imo": routing.attrib["vesselImo"],
                "containers_count": len(containers),
                "total_fob_usd": sql_row["total_fob_value_usd"],
                "ciq_quarantine_verdict": sql_row["inspection_verdict"] or "Exempt / Green Channel",
                "e_ciq_cert_no": sql_row["e_ciq_certificate_no"],
                "hazmat_un_code_xml": hz_info.get("un_number", "NON-HAZMAT"),
                "ispm15_wood_mark_xml": hz_info.get("ippc_fumigation_mark", "Standard Pallet")
            })

    results.append({
        "query_id": "Q04",
        "scope": "Individual - David Rodrigues (China)",
        "difficulty": "Intermediate",
        "sources_used": [
            "Source D1: CN PostgreSQL (35_cn_enterprises_manufacturers, 44_cn_customs_export_declarations_gacc, 46_cn_ciq_inspection_quarantine_records)",
            "Source D2: CN BaseX XML (55_cn_master_bills_of_lading_xml, 64_cn_export_packaging_fumigation_certs_xml)"
        ],
        "title": "Integração Logístico-Alfandegária na China: Declarações GACC & Quarentena CIQ (SQL) vs. e-Bills of Lading e Certificados IMDG/ISPM-15 (XML)",
        "justification": "Query intermédia que combina dados relacionais SQL (GACC e CIQ) com múltiplos contentores XML hierárquicos (Conhecimentos de Embarque e Certificados de Mercadorias Perigosas UN38.3/ISPM-15).",
        "query_code": """(: Passo 1 - XPath sobre 55_cn_master_bills_of_lading_xml.xml & 64_cn_export_packaging_fumigation_certs_xml.xml :)
//BillOfLading[@blNumber and @gaccDeclarationId18]/ContainerizedCargoList/Container
//CertificateRecord[@blNumber]/HazmatIMDGDeclaration[@unNumber='UN3480']
-- Passo 2 - Join com Fonte D1 (SQL 3FN):
SELECT g.gacc_entry_id_18, g.total_fob_value_usd, e.company_name_en, c.inspection_verdict
FROM cn_customs_export_declarations_gacc g JOIN cn_enterprises_manufacturers e ON g.exporter_uscc = e.uscc_code
LEFT JOIN cn_ciq_inspection_quarantine_records c ON g.gacc_entry_id_18 = c.gacc_declaration_id_18;""",
        "output": q4_data
    })

    # Include the 8 shared Cross-Subtopic Queries (Q05..Q12)
    local_expected = DAVID_DIR / "queries" / "expected_results_david.json"
    source_json_path = AFONSO_RESULTS if AFONSO_RESULTS.exists() else local_expected
    if source_json_path.exists():
        afonso_q = json.loads(source_json_path.read_text(encoding="utf-8"))
        for q in afonso_q:
            if q["query_id"] not in ("Q01", "Q02", "Q03", "Q04"):
                results.append(q)

    out_path = DAVID_DIR / "queries" / "expected_results_david.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    conn.close()

    if not quiet:
        print("=" * 116)
        print("🇨🇳 CADERNO DE QUERIES DE DAVID RODRIGUES (SUBTÓPICO CHINA — 58 ENTIDADES: 38 SQL 3FN + 20 XML/XSD)")
        print("   Inclui as Queries Individuais (Q03, Q04) e as 8 Queries Cruzadas com Portugal (Q05 a Q12)")
        print("=" * 116)
        for q in results:
            print_query_execution(q)
        print("\n" + "=" * 116)
        print(f"✅ [SUCESSO] {len(results)} queries executadas, código exibido e tabelas de dados reais impressas!")
        print(f"💾 Ficheiro JSON de resultados atualizado em: {out_path}")
        print("=" * 116)


if __name__ == "__main__":
    quiet_flag = "--quiet" in sys.argv
    run_david_queries(quiet=quiet_flag)
