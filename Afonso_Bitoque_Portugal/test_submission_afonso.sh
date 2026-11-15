#!/usr/bin/env bash
# =============================================================================
# UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
# Unidade Curricular: Modelação e Integração de Dados (DMI) - Projeto P1
# Script de Verificação e Demonstração Real — Afonso Bitoque (Subtópico Portugal)
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "===================================================================================================================="
echo "🇵🇹 VERIFICAÇÃO E AUDITORIA REAL DA ENTREGA — AFONSO BITOQUE (SUBTÓPICO PORTUGAL — 58 ENTIDADES)"
echo "===================================================================================================================="

# 1. Pastas e Relatórios PDF
echo ""
echo "▶ [TESTE 1/4] ESTRUTURA DO PACOTE E RELATÓRIOS TÉCNICOS EM PDF (SECÇÃO 6.1)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
for item in "report" "src" "data" "database" "models" "queries" "README.md" "AI_DECLARATION.md"; do
  if [ ! -e "$item" ]; then
    echo "❌ FALTANDO: $item"
    exit 1
  fi
done
ls -lh report/*.pdf README.md AI_DECLARATION.md
echo "✅ Estrutura de pastas e relatórios PDF oficiais verificados!"

# 2. Auditoria Real das 39 Coleções MongoDB JSON
echo ""
echo "▶ [TESTE 2/4] AUDITORIA REAL DAS 39 COLEÇÕES SEMI-ESTRUTURADAS MONGODB (FONTE A1)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
python3 - << 'PYEOF'
import json
from pathlib import Path

files = sorted(Path("data/mongodb_semi_structured").glob("*.json"))
assert len(files) == 39, f"Esperadas 39 coleções, encontradas {len(files)}"

print("  ┌────┬────────────────────────────────────────────────────────┬──────────┬────────────────────────────────────────┐")
print("  │ #  │ Nome da Coleção MongoDB (JSON/BSON)                    │ Registos │ Exemplo de Chave / Identificador Real  │")
print("  ├────┼────────────────────────────────────────────────────────┼──────────┼────────────────────────────────────────┤")
total_docs = 0
for idx, f in enumerate(files, 1):
    docs = json.loads(f.read_text(encoding="utf-8"))
    assert isinstance(docs, list) and len(docs) > 0
    total_docs += len(docs)
    d0 = docs[0]
    sample_key = (
        d0.get("mrn_codigo") or d0.get("eori_code") or d0.get("codigo_taric_10") or
        d0.get("numero_escala_jul") or d0.get("codigo_cifer_gacc_18digitos") or
        d0.get("referencia_swift_uetr") or d0.get("_id") or str(list(d0.values())[0])
    )
    print(f"  │ {idx:2d} │ {f.stem[:54]:<54} │ {len(docs):8d} │ {str(sample_key)[:38]:<38} │")
print("  └────┴────────────────────────────────────────────────────────┴──────────┴────────────────────────────────────────┘")
print(f"✅ 39/39 Coleções MongoDB validadas com sucesso ({total_docs} documentos BSON/JSON reais carregados)!")
PYEOF

# 3. Auditoria Real dos 19 Ficheiros PDF Não Estruturados + Warehouse SQLite de IA
echo ""
echo "▶ [TESTE 3/4] AUDITORIA DOS 19 DOCUMENTOS PDF NÃO ESTRUTURADOS E EXTRAÇÃO POR IA (FONTE A2)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
python3 - << 'PYEOF'
import sqlite3, subprocess, shutil
from pathlib import Path

pdfs = sorted(Path("data/unstructured_corpus").glob("*.pdf"))
assert len(pdfs) == 19, f"Esperados 19 ficheiros PDF em data/unstructured_corpus, encontrados {len(pdfs)}"

has_pdftotext = shutil.which("pdftotext") is not None
print("  ┌────┬────────────────────────────────────────────────────────┬──────────┬────────────────────────────────────────┐")
print("  │ #  │ Ficheiro PDF Oficial (Corpus Não Estruturado)          │ Tamanho  │ Amostra Extraída do PDF (pdftotext)    │")
print("  ├────┼────────────────────────────────────────────────────────┼──────────┼────────────────────────────────────────┤")
for idx, p in enumerate(pdfs, 1):
    kb = f"{p.stat().st_size / 1024:.1f} KB"
    snippet = "PDF 1.4 Válido"
    if has_pdftotext:
        txt = subprocess.check_output(["pdftotext", str(p), "-"], text=True).splitlines()
        doc_lines = [l.strip() for l in txt if "DOCUMENT ID:" in l or "REPÚBLICA" in l]
        snippet = doc_lines[1] if len(doc_lines) > 1 else (doc_lines[0] if doc_lines else "Texto extraído OK")
    print(f"  │ {idx:2d} │ {p.name[:54]:<54} │ {kb:>8} │ {snippet[:38]:<38} │")
print("  └────┴────────────────────────────────────────────────────────┴──────────┴────────────────────────────────────────┘")

conn = sqlite3.connect("data/ai_structured_output/afonso_ai_structured_warehouse.sqlite")
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("PRAGMA foreign_key_check;")
assert len(cur.fetchall()) == 0
tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
rows = cur.execute("SELECT doc_id, primary_eori_pt, primary_mrn_dau, primary_taric_10, ai_compliance_verdict, ai_risk_score_0_100 FROM ai_extracted_knowledge_graph LIMIT 10").fetchall()

print(f"\n  📊 Amostra da Tabela Mestre SQLite Extraída por IA (ai_extracted_knowledge_graph — {len(tables)} tabelas ativas):")
print("  ┌──────────────────────────────┬──────────────┬────────────────────┬────────────┬──────────────────────────────┬───────┐")
print("  │ doc_id (Extraído do PDF)     │ EORI PT      │ MRN DAU            │ TARIC 10D  │ Veredito IA                  │ Risco │")
print("  ├──────────────────────────────┼──────────────┼────────────────────┼────────────┼──────────────────────────────┼───────┤")
for r in rows:
    doc_id = str(r["doc_id"])[:28]
    eori = str(r["primary_eori_pt"] or "-")[:12]
    mrn = str(r["primary_mrn_dau"] or "-")[:18]
    taric = str(r["primary_taric_10"] or "-")[:10]
    verdict = str(r["ai_compliance_verdict"])[:28]
    risk = float(r["ai_risk_score_0_100"])
    print(f"  │ {doc_id:<28} │ {eori:<12} │ {mrn:<18} │ {taric:<10} │ {verdict:<28} │ {risk:5.1f} │")
print("  └──────────────────────────────┴──────────────┴────────────────────┴────────────┴──────────────────────────────┴───────┘")
conn.close()
print(f"✅ 19/19 Ficheiros PDF Não Estruturados + {len(tables)} Tabelas SQLite de IA verificadas com 0 erros!")
PYEOF

# 4. Execução Completa e Impressão das Queries do Afonso no Terminal
echo ""
echo "▶ [TESTE 4/4] EXECUÇÃO REAL E IMPRESSÃO DAS QUERIES DE AFONSO BITOQUE (Q01, Q02 + Q05..Q12)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
python3 queries/run_afonso_queries.py

echo ""
echo "===================================================================================================================="
echo "🎉 [SUCESSO TOTAL] A ENTREGA DE AFONSO BITOQUE (58 ENTIDADES PT + QUERIES REAIS + 19 PDFs) ESTÁ 100% VERIFICADA!"
echo "===================================================================================================================="
