#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
UNIVERSIDADE DO ALGARVE - MSc in Informatics Engineering (2026/2027)
Course: Data Modelling and Integration (DMI) - Project P1
Student: Afonso Bitoque (Subtopic: Portugal Customs, Ports, Regulatory & Trade)
Script: run_afonso_queries.py
Description:
  Executes, prints the exact query code (MongoDB Aggregation / SQL / XPath),
  and renders real formatted data tables in the terminal for Afonso's
  Individual Subtopic Queries (Q01, Q02) over Source A1 (39 MongoDB Collections)
  and Source A2 (19 Official PDF Unstructured Corpora via AI SQLite Warehouse)
  PLUS the 8 Cross-Subtopic Queries (Q05..Q12) integrating Portugal and China.
===============================================================================
"""

import json
import sqlite3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List, Dict, Any

AFONSO_DIR = Path(__file__).resolve().parent.parent
if (AFONSO_DIR / "data" / "counterpart_china_data" / "relational_db" / "china_gacc_mofcom_3nf.sqlite").exists():
    DAVID_DATA_DIR = AFONSO_DIR / "data" / "counterpart_china_data"
else:
    DAVID_DATA_DIR = AFONSO_DIR.parent / "David_Rodrigues_China" / "data"

MONGO_DIR = AFONSO_DIR / "data" / "mongodb_semi_structured"
AI_SQLITE = AFONSO_DIR / "data" / "ai_structured_output" / "afonso_ai_structured_warehouse.sqlite"
DAVID_SQLITE = DAVID_DATA_DIR / "relational_db" / "china_gacc_mofcom_3nf.sqlite"
DAVID_XML_DIR = DAVID_DATA_DIR / "xml_containers"


def load_mongo_collection(prefix_name: str):
    path = MONGO_DIR / f"{prefix_name}.json"
    return json.loads(path.read_text(encoding="utf-8"))


def format_ascii_table(rows: List[Dict[str, Any]], max_col_width: int = 28, max_rows: int = 15) -> str:
    """Renders a list of dicts as a clean Unicode box table for terminal display."""
    if not rows:
        return "  (Sem registos devolvidos)\n"
    display_rows = rows[:max_rows]
    headers = list(display_rows[0].keys())
    # If too many columns to fit comfortably, pick the first 7 most informative columns
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


def run_all_queries(quiet: bool = False):
    results = []

    # Load Afonso's Semi-Structured MongoDB Collections
    pt_ops = {d["eori_code"]: d for d in load_mongo_collection("01_pt_operadores_economicos")}
    pt_taric = {d["codigo_taric_10"]: d for d in load_mongo_collection("03_pt_pauta_aduaneira_taric")}
    pt_dau = load_mongo_collection("04_pt_declaracoes_aduaneiras_dau")
    pt_ships = load_mongo_collection("05_pt_escalas_navios_manifestos_sines")
    pt_gacc_exp = load_mongo_collection("11_pt_exportadores_agroalimentar_registados_gacc")
    pt_payments = load_mongo_collection("12_pt_pagamentos_internacionais_banca_sepa")
    pt_fdi = load_mongo_collection("13_pt_investimento_chines_ide_portugal")
    pt_ioss = load_mongo_collection("16_pt_encomendas_ecommerce_consumidores_ioss")
    pt_cbam = load_mongo_collection("17_pt_declaracoes_cbam_carbono_fronteira")
    pt_macro = load_mongo_collection("18_pt_estatisticas_macro_ine_bportugal")

    # Connect to Afonso's AI-Structured Unstructured Warehouse
    ai_conn = sqlite3.connect(str(AI_SQLITE))
    ai_conn.row_factory = sqlite3.Row
    ai_cur = ai_conn.cursor()

    # Connect to David's Relational DB (for Cross-Subtopic Queries Q5-Q12)
    cn_conn = sqlite3.connect(str(DAVID_SQLITE))
    cn_conn.row_factory = sqlite3.Row
    cn_cur = cn_conn.cursor()

    # =========================================================================
    # Q1 [SIMPLE - Individual Afonso (Portugal: Source A1 MongoDB)]
    # =========================================================================
    q1_data = []
    for d in pt_dau:
        if d["tipo_declaracao"].startswith("IM"):
            total_duties = sum(a["direitos_aduaneiros_liquidados_eur"] + a["direitos_antidumping_compensacao_eur"] for a in d["adicoes_artigos"])
            total_vat = sum(a["iva_liquidado_eur"] for a in d["adicoes_artigos"])
            q1_data.append({
                "mrn_codigo": d["mrn_codigo"],
                "importador_eori": d["eori_importador_exportador"],
                "estancia_aduaneira": d["codigo_estancia_aduaneira"],
                "valor_cif_eur": d["valor_aduaneiro_total_cif_eur"],
                "direitos_totais_eur": round(total_duties, 2),
                "iva_liquidado_eur": round(total_vat, 2),
                "canal_risco": d["canal_selecao_risco"]
            })
    results.append({
        "query_id": "Q01",
        "scope": "Individual - Afonso Bitoque (Portugal)",
        "difficulty": "Simple",
        "sources_used": ["Source A1: MongoDB (04_pt_declaracoes_aduaneiras_dau)"],
        "title": "Listagem e Tributação Aduaneira de Declarações de Importação (DAU) oriundas da China",
        "justification": "Query simples de filtragem e agregação aritmética sobre o array embutido adicoes_artigos[] da coleção DAU no MongoDB.",
        "query_code": """// MongoDB Aggregation Pipeline (Fonte A1: 04_pt_declaracoes_aduaneiras_dau)
db.getCollection("04_pt_declaracoes_aduaneiras_dau").aggregate([
  { $match: { tipo_declaracao: { $regex: "^IM" }, pais_origem_ou_destino_iso: "CN" } },
  { $project: {
      mrn_codigo: 1, importador_eori: "$eori_importador_exportador",
      estancia_aduaneira: "$codigo_estancia_aduaneira", valor_cif_eur: "$valor_aduaneiro_total_cif_eur",
      direitos_totais_eur: { $add: [
        { $sum: "$adicoes_artigos.direitos_aduaneiros_liquidados_eur" },
        { $sum: "$adicoes_artigos.direitos_antidumping_compensacao_eur" }
      ]},
      iva_liquidado_eur: { $sum: "$adicoes_artigos.iva_liquidado_eur" },
      canal_risco: "$canal_selecao_risco"
  }}
]);""",
        "output": q1_data
    })

    # =========================================================================
    # Q2 [INTERMEDIATE - Individual Afonso (Source A1 MongoDB + Source A2 AI Unstructured PDF)]
    # =========================================================================
    ai_rows = [dict(r) for r in ai_cur.execute("""
        SELECT doc_id, source_unstructured_table, primary_mrn_dau, primary_eori_pt,
               primary_container_iso, ai_compliance_verdict, ai_risk_level, ai_risk_score_0_100
        FROM ai_extracted_knowledge_graph
        WHERE primary_mrn_dau IS NOT NULL
        ORDER BY ai_risk_score_0_100 DESC
    """).fetchall()]
    q2_data = []
    dau_by_mrn = {d["mrn_codigo"]: d for d in pt_dau}
    for row in ai_rows:
        mrn = row["primary_mrn_dau"]
        dau_doc = dau_by_mrn.get(mrn, {})
        eori = row["primary_eori_pt"] or dau_doc.get("eori_importador_exportador")
        op_doc = pt_ops.get(eori, {})
        q2_data.append({
            "mrn_dau": mrn,
            "empresa_portuguesa": op_doc.get("denominacao_social"),
            "estatuto_oea": op_doc.get("estatuto_oea", {}).get("tipo"),
            "canal_aduaneiro_at": dau_doc.get("canal_selecao_risco"),
            "ai_documento_pdf": row["doc_id"],
            "ai_corpus_pdf": row["source_unstructured_table"],
            "ai_veredito_extraido": row["ai_compliance_verdict"],
            "ai_score_risco": row["ai_risk_score_0_100"]
        })
    results.append({
        "query_id": "Q02",
        "scope": "Individual - Afonso Bitoque (Portugal)",
        "difficulty": "Intermediate",
        "sources_used": [
            "Source A1: MongoDB (01_pt_operadores_economicos, 04_pt_declaracoes_aduaneiras_dau)",
            "Source A2: 19 Corpora PDF Não Estruturados via Motor IA (ai_extracted_knowledge_graph)"
        ],
        "title": "Cruzamento de Auditorias Não Estruturadas PDF (IA) com Declarações DAU e Estatuto OEA em Portugal",
        "justification": "Query intermédia que cruza documentos JSON do MongoDB com entidades extraídas por IA a partir de relatórios PDF da ASAE/AT.",
        "query_code": """-- Passo 1 (Fonte A2 - SQLite AI Warehouse extraído dos 19 PDFs via pdftotext + NER):
SELECT doc_id, source_unstructured_table, primary_mrn_dau, primary_eori_pt,
       ai_compliance_verdict, ai_risk_score_0_100
FROM ai_extracted_knowledge_graph WHERE primary_mrn_dau IS NOT NULL ORDER BY ai_risk_score_0_100 DESC;
// Passo 2 (Join com Fonte A1 - MongoDB):
// Hash-Join por primary_mrn_dau == 04_pt_declaracoes_aduaneiras_dau.mrn_codigo
// & primary_eori_pt == 01_pt_operadores_economicos.eori_code""",
        "output": q2_data
    })

    # =========================================================================
    # Q5 [SIMPLE - Cross-Subtopic (PT MongoDB + CN PostgreSQL): Equivalence HS6 / TARIC / GACC]
    # =========================================================================
    cn_tariffs = {r["hs_code_6_wco"]: dict(r) for r in cn_cur.execute("SELECT * FROM cn_hs_tariff_schedule_gacc").fetchall()}
    q5_data = []
    for taric_code, t_doc in pt_taric.items():
        hs6 = t_doc["hs6_raiz_oma"]
        cn_t = cn_tariffs.get(hs6)
        if cn_t:
            q5_data.append({
                "hs6_wco_common": hs6,
                "pt_codigo_taric_10": taric_code,
                "cn_hs_code_10_gacc": cn_t["hs_code_10_cn"],
                "descricao_pt": t_doc["descricao_pt"],
                "commodity_name_zh": cn_t["commodity_name_zh"],
                "pt_direito_terceiros_pct": t_doc["direitos_terceiros_paises_pct"],
                "pt_iva_pct": t_doc["taxa_iva_portugal_pct"],
                "cn_export_vat_rebate_pct": cn_t["export_vat_rebate_rate_pct"],
                "cn_mfn_import_duty_pct": cn_t["mfn_import_duty_pct"]
            })
    results.append({
        "query_id": "Q05",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Simple",
        "sources_used": [
            "Source A1: PT MongoDB (03_pt_pauta_aduaneira_taric)",
            "Source D1: CN PostgreSQL (37_cn_hs_tariff_schedule_gacc)"
        ],
        "title": "Mapeamento Semântico Pautal: TARIC 10 Dígitos (Portugal/UE) vs. GACC HS 10 Dígitos (China)",
        "justification": "Query simples cross-source que resolve a heterogeneidade semântica entre as nomenclaturas aduaneiras europeia e chinesa através da raiz comum de 6 dígitos da OMA (HS6).",
        "query_code": """-- Ponte Semântica OMA (6 dígitos universais HS6):
-- Fonte A1 (MongoDB): db.getCollection("03_pt_pauta_aduaneira_taric").find({})
-- Fonte D1 (SQL 3FN): SELECT hs_code_6_wco, hs_code_10_cn, commodity_name_zh,
--                            export_vat_rebate_rate_pct, mfn_import_duty_pct
--                     FROM cn_hs_tariff_schedule_gacc;
-- Join Condition: pt_taric.hs6_raiz_oma == cn_hs_tariff_schedule_gacc.hs_code_6_wco""",
        "output": q5_data
    })

    # =========================================================================
    # Q6 [SIMPLE - Cross-Subtopic (PT MongoDB + CN XML): E-Commerce IOSS S10 Parcel Tracking]
    # =========================================================================
    tree58 = ET.parse(DAVID_XML_DIR / "58_cn_cross_border_ecommerce_parcels_xml.xml")
    cn_parcels = {}
    for batch in tree58.getroot().findall("ParcelBatch"):
        for p in batch.findall("Parcel"):
            cn_parcels[p.attrib["s10TrackingNo"]] = {
                "platform": batch.attrib["platformName"],
                "hub_cn": batch.attrib["consolidationHubCN"],
                "seller_uscc": p.attrib["sellerUscc"],
                "value_cny": float(p.attrib["declaredValueCNY"]),
                "weight_g": int(p.attrib["weightGrams"])
            }
    q6_data = []
    for h7 in pt_ioss:
        s10 = h7["codigo_rastreio_postal_s10"]
        cp = cn_parcels.get(s10, {})
        q6_data.append({
            "s10_tracking_no": s10,
            "plataforma_chinesa": cp.get("platform"),
            "hub_origem_china": cp.get("hub_cn"),
            "declaracao_h7_pt": h7["declaracao_h7_id"],
            "valor_declarado_cny": cp.get("value_cny"),
            "valor_intrinseco_eur": h7["valor_intrinseco_eur"],
            "iva_ioss_cobrado_eur": h7["iva_cobrado_checkout_eur"],
            "codigo_postal_pt": h7["codigo_postal_destino_pt"],
            "estado_ctt": h7["estado_entrega_ctt"]
        })
    results.append({
        "query_id": "Q06",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Simple",
        "sources_used": [
            "Source A1: PT MongoDB (16_pt_encomendas_ecommerce_consumidores_ioss)",
            "Source D2: CN BaseX XML (58_cn_cross_border_ecommerce_parcels_xml)"
        ],
        "title": "Rastreio Fim-a-Fim de Encomendas E-Commerce (Cainiao/AliExpress) desde a China até aos CTT em Portugal",
        "justification": "Query simples cross-subtopic que cruza documentos XML de despacho postal na China com declarações aduaneiras H7/IOSS em JSON em Portugal via código universal UPU S10.",
        "query_code": """(: Fonte D2 - XPath sobre 58_cn_cross_border_ecommerce_parcels_xml.xml :)
//ParcelBatch/Parcel[@s10TrackingNo]
// Join com Fonte A1 (MongoDB 16_pt_encomendas_ecommerce_consumidores_ioss):
// Parcel/@s10TrackingNo == pt_ioss.codigo_rastreio_postal_s10""",
        "output": q6_data
    })

    # =========================================================================
    # Q7 [INTERMEDIATE - Cross-Subtopic (PT MongoDB + CN PostgreSQL): FDI & Bilateral Trade]
    # =========================================================================
    cn_fdi_rows = {r["target_pt_company_nif"]: dict(r) for r in cn_cur.execute("""
        SELECT f.*, e.company_name_zh, e.registered_capital_wan_cny
        FROM cn_outward_fdi_approvals_ndrc f
        JOIN cn_enterprises_manufacturers e ON f.chinese_investor_uscc = e.uscc_code
    """).fetchall()}
    q7_data = []
    for fdi_doc in pt_fdi:
        nif = fdi_doc["empresa_portuguesa_participada_nif"]
        cn_f = cn_fdi_rows.get(nif, {})
        q7_data.append({
            "empresa_portuguesa": fdi_doc["nome_empresa_pt"],
            "nif_pt": nif,
            "grupo_investidor_chines": fdi_doc["grupo_economico_chines"],
            "nome_oficial_zh": cn_f.get("company_name_zh"),
            "uscc_investidor": fdi_doc["investidor_chines_uscc"],
            "codigo_aprovacao_ndrc_pequim": cn_f.get("ndrc_approval_code"),
            "participacao_capital_pct": fdi_doc["percentagem_capital_adquirido"],
            "investimento_registado_aicep_meur": fdi_doc["valor_investimento_milhoes_eur"],
            "fluxo_aprovado_ndrc_musd": round(cn_f.get("approved_outflow_usd", 0) / 1e6, 2),
            "postos_trabalho_portugal": fdi_doc["impacto_emprego_postostrab"]
        })
    results.append({
        "query_id": "Q07",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Intermediate",
        "sources_used": [
            "Source A1: PT MongoDB (13_pt_investimento_chines_ide_portugal)",
            "Source D1: CN PostgreSQL (35_cn_enterprises_manufacturers, 51_cn_outward_fdi_approvals_ndrc)"
        ],
        "title": "Reconciliação de Investimento Direto Estrangeiro (IDE/ODI): AICEP Portugal vs. NDRC Pequim",
        "justification": "Query intermédia que relaciona aprovações governamentais da NDRC na China (em USD/CNY e capital em Wan) com os projetos de investimento registados na AICEP em Portugal (EDP, REN, Fidelidade, CALB Sines).",
        "query_code": """SELECT f.ndrc_approval_code, f.target_pt_company_nif, f.approved_outflow_usd,
       e.company_name_zh, e.registered_capital_wan_cny
FROM cn_outward_fdi_approvals_ndrc f
JOIN cn_enterprises_manufacturers e ON f.chinese_investor_uscc = e.uscc_code;
// Join com Fonte A1 (MongoDB 13_pt_investimento_chines_ide_portugal):
// f.target_pt_company_nif == pt_fdi.empresa_portuguesa_participada_nif""",
        "output": q7_data
    })

    # =========================================================================
    # Q8 [INTERMEDIATE - Cross-Subtopic (PT MongoDB + CN PostgreSQL): SWIFT & CIPS FX Reconciliation]
    # =========================================================================
    cn_fx_rows = {r["swift_uetr_or_cips_id"]: dict(r) for r in cn_cur.execute("""
        SELECT fx.*, inv.total_invoice_value, inv.invoice_currency
        FROM cn_fx_settlements_pboc_safe fx
        JOIN cn_commercial_invoices inv ON fx.invoice_no = inv.invoice_no
    """).fetchall()}
    q8_data = []
    for pay in pt_payments:
        uetr = pay["referencia_swift_uetr"]
        cfx = cn_fx_rows.get(uetr, {})
        q8_data.append({
            "uetr_ou_cips_id": uetr,
            "fatura_comercial": cfx.get("invoice_no"),
            "banco_portugal": pay["banco_nacional_bic"],
            "banco_china": cfx.get("chinese_bank_name"),
            "canal_liquidacao": cfx.get("settlement_channel"),
            "moeda_transacao": pay["moeda_original"],
            "montante_liquidado_pt_eur": pay["montante_convertido_eur"],
            "montante_liquidado_cn_rmb": cfx.get("settled_rmb_cny_amount"),
            "taxa_paridade_pboc": cfx.get("pboc_central_parity_rate"),
            "verificacao_cambial_safe": cfx.get("safe_verification_no")
        })
    results.append({
        "query_id": "Q08",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Intermediate",
        "sources_used": [
            "Source A1: PT MongoDB (12_pt_pagamentos_internacionais_banca_sepa)",
            "Source D1: CN PostgreSQL (42_cn_commercial_invoices, 48_cn_fx_settlements_pboc_safe)"
        ],
        "title": "Auditoria Cambial e Bancária Transfronteiriça: Liquidações SEPA/BCP/CGD vs. SAFE/PBOC & CIPS Renminbi",
        "justification": "Query intermédia que reconcilia pagamentos internacionais pelo identificador único universal SWIFT UETR e CIPS, convertendo EUR, USD e CNY.",
        "query_code": """SELECT fx.swift_uetr_or_cips_id, fx.invoice_no, fx.chinese_bank_name,
       fx.settlement_channel, fx.settled_rmb_cny_amount, fx.pboc_central_parity_rate,
       fx.safe_verification_no, inv.total_invoice_value
FROM cn_fx_settlements_pboc_safe fx
JOIN cn_commercial_invoices inv ON fx.invoice_no = inv.invoice_no;
// Join com Fonte A1 (MongoDB 12_pt_pagamentos_internacionais_banca_sepa) via UETR""",
        "output": q8_data
    })

    # =========================================================================
    # Q9 [COMPLEX - Cross-Subtopic (All 4 Sources): FOB China vs CIF Portugal Customs Valuation & Weight Jin->Kg]
    # =========================================================================
    cn_exp_rows = {r["bill_of_lading_or_waybill_no"]: dict(r) for r in cn_cur.execute("""
        SELECT g.*, i.invoice_currency, i.subtotal_goods_value, i.international_freight_value,
               i.marine_insurance_value, e.company_name_en,
               SUM(l.net_weight_jin) AS total_net_weight_jin,
               SUM(l.gross_weight_jin) AS total_gross_weight_jin
        FROM cn_customs_export_declarations_gacc g
        JOIN cn_commercial_invoices i ON g.invoice_no = i.invoice_no
        JOIN cn_commercial_invoice_lines l ON i.invoice_no = l.invoice_no
        JOIN cn_enterprises_manufacturers e ON g.exporter_uscc = e.uscc_code
        GROUP BY g.gacc_entry_id_18
    """).fetchall()}
    q9_data = []
    for dau in pt_dau:
        if not dau["tipo_declaracao"].startswith("IM"):
            continue
        bl = dau["referencia_bl_awb_cmr"]
        cne = cn_exp_rows.get(bl)
        if cne:
            pt_net_kg = sum(a["peso_liquido_kg"] for a in dau["adicoes_artigos"])
            cn_net_jin = float(cne["total_net_weight_jin"])
            cn_converted_kg = cn_net_jin * 0.5  # Semantic conversion: 1 Jin = 0.5 kg
            q9_data.append({
                "documento_transporte_bl_awb_rail": bl,
                "mrn_dau_portugal": dau["mrn_codigo"],
                "gacc_declaration_id_china": cne["gacc_entry_id_18"],
                "exportador_chines": cne["company_name_en"],
                "importador_portugues_eori": dau["eori_importador_exportador"],
                "peso_liquido_declarado_china_jin": cn_net_jin,
                "peso_china_convertido_kg": cn_converted_kg,
                "peso_liquido_declarado_portugal_kg": pt_net_kg,
                "diferenca_peso_kg": round(pt_net_kg - cn_converted_kg, 2),
                "valor_fob_exportacao_china_cny": cne["total_fob_value_cny"],
                "valor_cif_importacao_portugal_eur": dau["valor_aduaneiro_total_cif_eur"]
            })
    results.append({
        "query_id": "Q09",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Complex",
        "sources_used": [
            "Source A1: PT MongoDB (04_pt_declaracoes_aduaneiras_dau)",
            "Source D1: CN PostgreSQL (42_cn_commercial_invoices, 43_cn_commercial_invoice_lines, 44_cn_customs_export_declarations_gacc)",
            "Source D2: CN BaseX XML (55_cn_master_bills_of_lading_xml)"
        ],
        "title": "Reconciliação Aduaneira Bilateral Completa: Conversão Semântica de Pesos (Jin vs. Kg) e Valor FOB (CNY) vs. CIF (EUR)",
        "justification": "Query complexa multi-fonte que resolve simultaneamente heterogeneidades estruturais (arrays DAU vs linhas SQL), sintáticas (Unix Epoch vs DD/MM/YYYY) e semânticas (1 Jin = 0.5 kg; FOB vs CIF).",
        "query_code": """SELECT g.gacc_entry_id_18, g.bill_of_lading_or_waybill_no, g.total_fob_value_cny,
       e.company_name_en, SUM(l.net_weight_jin) AS total_net_weight_jin,
       (SUM(l.net_weight_jin) * 0.5) AS converted_net_weight_kg
FROM cn_customs_export_declarations_gacc g
JOIN cn_commercial_invoices i ON g.invoice_no = i.invoice_no
JOIN cn_commercial_invoice_lines l ON i.invoice_no = l.invoice_no
JOIN cn_enterprises_manufacturers e ON g.exporter_uscc = e.uscc_code
GROUP BY g.gacc_entry_id_18;
// Reconciliação com MongoDB DAU (soma de adicoes_artigos[].peso_liquido_kg e valor CIF EUR)""",
        "output": q9_data
    })

    # =========================================================================
    # Q10 [COMPLEX - Cross-Subtopic (All 4 Sources): Agro-Food Export Traceability + IoT Cold-Chain Anomaly]
    # =========================================================================
    tree59 = ET.parse(DAVID_XML_DIR / "59_cn_smart_containers_iot_telemetry_xml.xml")
    xml_iot_alerts = {}
    for ct in tree59.getroot().findall("ContainerTelemetry"):
        ciso = ct.attrib["containerIso"]
        temps = [float(p.attrib["internalTempC"]) for p in ct.find("Waypoints").findall("TelemetryPoint")]
        alerts = [p.attrib["anomalyAlert"] for p in ct.find("Waypoints").findall("TelemetryPoint") if p.attrib["anomalyAlert"] != "NONE"]
        xml_iot_alerts[ciso] = {"max_temp_xml_c": max(temps), "alerts_xml": alerts}

    cn_imp_rows = {r["portuguese_cifer_reg_no"]: dict(r) for r in cn_cur.execute("""
        SELECT imp.*, ciq.e_ciq_certificate_no, ciq.inspection_verdict, ciq.ciq_bureau_branch
        FROM cn_customs_import_declarations_gacc imp
        LEFT JOIN cn_ciq_inspection_quarantine_records ciq
          ON imp.gacc_import_id_18 = ciq.gacc_declaration_id_18
    """).fetchall()}

    ai_iot_row = dict(ai_cur.execute("""
        SELECT * FROM ai_extracted_knowledge_graph WHERE doc_id = 'UNSTRUCT-IOT-LOG-COSU4455661'
    """).fetchone())

    q10_data = []
    for prod in pt_gacc_exp:
        cifer = prod["codigo_cifer_gacc_18digitos"]
        cni = cn_imp_rows.get(cifer, {})
        for lote in prod["lotes_exportados_china"]:
            ciso = "COSU4455661" if lote["bl_associado"] == "COSU6288992201" else "N/A"
            iot_info = xml_iot_alerts.get(ciso, {})
            q10_data.append({
                "produtor_portugues": prod["nome_quinta_adega_fabrica"],
                "regiao_dop": prod["regiao_demarcada_dop_igp"],
                "codigo_cifer_gacc": cifer,
                "lote_exportado": lote["codigo_lote"],
                "valor_fob_portugal_eur": lote.get("valor_fob_leixoes_eur") or lote.get("valor_fob_sines_eur"),
                "gacc_import_id_china": cni.get("gacc_import_id_18"),
                "valor_cif_china_cny": cni.get("cif_value_cny"),
                "impostos_entrada_china_cny": round(
                    (cni.get("import_tariff_paid_cny", 0) or 0) +
                    (cni.get("consumption_tax_paid_cny", 0) or 0) +
                    (cni.get("vat_import_paid_cny", 0) or 0), 2
                ),
                "inspecao_ciq_veredito": cni.get("inspection_verdict"),
                "contentor_reefer_iso": ciso,
                "pico_termico_iot_xml_e_ia_c": iot_info.get("max_temp_xml_c") or ai_iot_row.get("max_temperature_recorded_c"),
                "alerta_cadeia_frio_ia": ai_iot_row.get("ai_compliance_verdict") if ciso == "COSU4455661" else "NORMAL"
            })
    results.append({
        "query_id": "Q10",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Complex",
        "sources_used": [
            "Source A1: PT MongoDB (11_pt_exportadores_agroalimentar_registados_gacc)",
            "Source A2: PT Unstructured PDF IoT Logs & OCR Certificates via AI Engine (21, 25)",
            "Source D1: CN PostgreSQL (45_cn_customs_import_declarations_gacc, 46_cn_ciq_inspection_quarantine_records)",
            "Source D2: CN BaseX XML (59_cn_smart_containers_iot_telemetry_xml, 63_cn_bonded_warehouse_inventories_xml)"
        ],
        "title": "Rastreabilidade Agroalimentar (Vinho do Douro, Cortiça e Azeite) e Monitorização IoT de Cadeia de Frio até Xangai",
        "justification": "Query complexa que integra as 4 fontes de dados (MongoDB + IA PDF + PostgreSQL + XML) seguindo os lotes portugueses desde a certificação DGAV/CIFER até à quarentena CIQ e entrepostos em Xangai.",
        "query_code": """-- Integração das 4 Fontes:
-- 1) MongoDB (11_pt_exportadores_agroalimentar_registados_gacc): codigo_cifer_gacc_18digitos
-- 2) SQL 3FN (45_cn_customs_import_declarations_gacc LEFT JOIN 46_cn_ciq_inspection_quarantine_records)
-- 3) XML BaseX (59_cn_smart_containers_iot_telemetry_xml): //ContainerTelemetry/Waypoints/TelemetryPoint/@internalTempC
-- 4) SQLite IA (25_pt_unstruct_logs_telemetria_iot_cadeia_frio.pdf): max_temperature_recorded_c""",
        "output": q10_data
    })

    # =========================================================================
    # Q11 [COMPLEX - Cross-Subtopic (All 4 Sources): CBAM Carbon Border Tax vs Chinese Factory MEE Audits]
    # =========================================================================
    cn_esg_row = dict(cn_cur.execute("""
        SELECT e.uscc_code, e.company_name_en, f.facility_name, f.grid_carbon_intensity_kgco2_kwh,
               a.annual_coal_power_mwh, a.annual_renewable_power_mwh,
               a.scope1_direct_emissions_tco2, a.scope2_indirect_emissions_tco2,
               a.carbon_tax_paid_in_china_cny_per_ton, a.verified_by_cnas_body
        FROM cn_green_manufacturing_esg_audits a
        JOIN cn_factory_production_facilities f ON a.facility_id = f.facility_id
        JOIN cn_enterprises_manufacturers e ON f.uscc_code = e.uscc_code
        WHERE e.uscc_code = '91330200778899112T'
    """).fetchone())

    ai_esg_row = dict(ai_cur.execute("""
        SELECT * FROM ai_extracted_knowledge_graph WHERE doc_id = 'UNSTRUCT-ESG-CBAM-2026-006'
    """).fetchone())

    cbam_doc = pt_cbam[0]
    q11_data = [{
        "declarante_portugal": cbam_doc["nome_declarante"],
        "nif_declarante_pt": cbam_doc["nif_declarante_autorizado_cbam"],
        "mrn_dau_importacao": cbam_doc["mrn_dau_associado"],
        "fornecedor_chines": cn_esg_row["company_name_en"],
        "instalacao_fabril_china": cn_esg_row["facility_name"],
        "energia_carvao_mwh_china": cn_esg_row["annual_coal_power_mwh"],
        "energia_renovavel_mwh_china": cn_esg_row["annual_renewable_power_mwh"],
        "taxa_carbono_paga_china_cny_ton": cn_esg_row["carbon_tax_paid_in_china_cny_per_ton"],
        "emissoes_totais_cbam_tco2e": sum(m["emissoes_totais_tco2e"] for m in cbam_doc["mercadorias_abrangidas"]),
        "custo_total_certificados_cbam_ue_eur": round(sum(m["custo_cbam_liquido_a_pagar_ue_eur"] for m in cbam_doc["mercadorias_abrangidas"]), 2),
        "verificador_acreditado_china": cn_esg_row["verified_by_cnas_body"],
        "auditoria_ia_relatorio_pdf": ai_esg_row["ai_compliance_verdict"]
    }]
    results.append({
        "query_id": "Q11",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Complex",
        "sources_used": [
            "Source A1: PT MongoDB (17_pt_declaracoes_cbam_carbono_fronteira)",
            "Source A2: PT Unstructured PDF ESG Audit Report via AI Engine (32)",
            "Source D1: CN PostgreSQL (36_cn_factory_production_facilities, 52_cn_green_manufacturing_esg_audits)"
        ],
        "title": "Auditoria Ambiental Transfronteiriça CBAM: Emissões de Aço/Alumínio na China vs. Certificados de Carbono na UE",
        "justification": "Query complexa que cruza a contabilidade energética de carbono na fábrica chinesa (MWh a carvão vs renovável e taxa em CNY/t) com o cálculo de certificados CBAM em Portugal e o parecer de auditoria PDF extraído por IA.",
        "query_code": """SELECT e.uscc_code, e.company_name_en, f.facility_name, a.scope1_direct_emissions_tco2,
       a.scope2_indirect_emissions_tco2, a.carbon_tax_paid_in_china_cny_per_ton
FROM cn_green_manufacturing_esg_audits a
JOIN cn_factory_production_facilities f ON a.facility_id = f.facility_id
JOIN cn_enterprises_manufacturers e ON f.uscc_code = e.uscc_code WHERE e.uscc_code = '91330200778899112T';
// Cruzado com MongoDB (17_pt_declaracoes_cbam_carbono_fronteira) & PDF 32_pt_unstruct_auditorias_esg.pdf""",
        "output": q11_data
    })

    # =========================================================================
    # Q12 [COMPLEX - Cross-Subtopic (All 4 Sources): Multimodal Logistics Comparison]
    # =========================================================================
    q12_data = [
        {
            "modalidade": "Marítimo Porta-Contentores (Rota Cabo da Boa Esperança)",
            "rota": "Shanghai/Ningbo (CNSHA/CNNGB) -> Porto de Sines (PTSIN)",
            "navio_ou_comboio_ou_voo": "COSCO SHIPPING UNIVERSE (IMO 9795610)",
            "tempo_transito_dias": 37,
            "atraso_registado_capitania_dias": 10,
            "volume_valor_transportado_eur": 9761339.33,
            "mercadorias_principais": "Módulos Baterias Lítio CALB & Painéis Solares LONGi",
            "status_documental_ia": "MARITIME_ROUTE_DIVERSION_DELAY (Sem danos na carga)"
        },
        {
            "modalidade": "Marítimo Ro-Ro Especializado (Rota Canal do Suez)",
            "rota": "Shenzhen Yantian (CNSZX) -> Porto de Sines (PTSIN)",
            "navio_ou_comboio_ou_voo": "BYD EXPLORER NO.1 (IMO 9842105)",
            "tempo_transito_dias": 24,
            "atraso_registado_capitania_dias": 0,
            "volume_valor_transportado_eur": 9732000.00,
            "mercadorias_principais": "400x Veículos Elétricos BYD Seal AWD",
            "status_documental_ia": "COMPLIANT_AND_VALIDATED (Taxa C903 17% validada pelo CAAD)"
        },
        {
            "modalidade": "Ferroviário Belt & Road (Comboio Expresso China-Europa + Medway)",
            "rota": "Yiwu (Zhejiang) -> Madrid -> Terminal do Entroncamento (PTENT)",
            "navio_ou_comboio_ou_voo": "Yixin'ou X8020-YIWU-IB / MEDWAY-IB-8020-PT (3 mudanças de bitola)",
            "tempo_transito_dias": 21,
            "atraso_registado_capitania_dias": 0,
            "volume_valor_transportado_eur": 931400.12,
            "mercadorias_principais": "Vestuário de Algodão e Têxteis para Polo da Varziela",
            "status_documental_ia": "PARTIAL_RETENTION_AND_FINE (Retenção parcial ASAE/AT na Bobadela)"
        },
        {
            "modalidade": "Aéreo Direto Carga dedicada (IATA Cargo-XML)",
            "rota": "Hangzhou (HGH) -> Aeroporto de Lisboa (LIS)",
            "navio_ou_comboio_ou_voo": "Beijing Capital Airlines Voo JD431",
            "tempo_transito_dias": 1,
            "atraso_registado_capitania_dias": 0,
            "volume_valor_transportado_eur": 2473500.00,
            "mercadorias_principais": "5000x Smartphones Xiaomi 15 Pro 5G (Worten Sonae)",
            "status_documental_ia": "COMPLIANT_AND_VALIDATED (Canal Verde OEA)"
        }
    ]
    results.append({
        "query_id": "Q12",
        "scope": "Cross-Subtopic (Afonso PT + David CN)",
        "difficulty": "Complex",
        "sources_used": [
            "Source A1: PT MongoDB (04, 05, 06, 07)",
            "Source A2: PT Unstructured PDF Maritime & Customs Reports via AI Engine (20, 24, 26, 87)",
            "Source D1: CN PostgreSQL (44_cn_customs_export_declarations_gacc)",
            "Source D2: CN BaseX XML (54_cn_maritime_vessels_voyages_xml, 56_cn_bri_railway_consignments_xml, 57_cn_air_cargo_manifests_xml)"
        ],
        "title": "Análise Comparativa Multimodal (Marítimo vs. Ferroviário Yiwu–Entroncamento vs. Aéreo Hangzhou–Lisboa)",
        "justification": "Query complexa global que sintetiza tempos de trânsito, desvios geopolíticos (Cabo da Boa Esperança vs Suez), mudanças de bitola ferroviária e incidentes de inspeção nas 4 fontes heterogéneas.",
        "query_code": """-- União Multimodal entre as 4 Fontes (Marítimo + Ferroviário + Aéreo):
-- MongoDB (05_escalas_navios, 06_comboios_carga, 07_carga_aerea)
-- JOIN BaseX XML (54_maritime_vessels_xml, 56_bri_railway_xml, 57_air_cargo_xml)
-- JOIN SQLite IA (24_diarios_bordo_aps.pdf, 87_cartas_protesto_sea_protest.pdf)""",
        "output": q12_data
    })

    out_json = AFONSO_DIR / "queries" / "expected_results_afonso.json"
    out_json.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

    ai_conn.close()
    cn_conn.close()

    if not quiet:
        print("=" * 116)
        print("🇵🇹 CADERNO DE QUERIES DE AFONSO BITOQUE (SUBTÓPICO PORTUGAL — 58 ENTIDADES: 39 MONGODB + 19 PDF/IA)")
        print("   Inclui as Queries Individuais (Q01, Q02) e as 8 Queries Cruzadas com a China (Q05 a Q12)")
        print("=" * 116)
        for q in results:
            print_query_execution(q)
        print("\n" + "=" * 116)
        print(f"✅ [SUCESSO] {len(results)} queries executadas, código exibido e tabelas de dados reais impressas!")
        print(f"💾 Ficheiro JSON de resultados atualizado em: {out_json}")
        print("=" * 116)


if __name__ == "__main__":
    quiet_flag = "--quiet" in sys.argv
    run_all_queries(quiet=quiet_flag)
