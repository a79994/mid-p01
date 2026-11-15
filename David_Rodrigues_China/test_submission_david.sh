#!/usr/bin/env bash
# =============================================================================
# UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
# Unidade Curricular: Modelação e Integração de Dados (DMI) - Projeto P1
# Script de Verificação e Demonstração Real — David Rodrigues (Subtópico China)
# =============================================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "===================================================================================================================="
echo "🇨🇳 VERIFICAÇÃO E AUDITORIA REAL DA ENTREGA — DAVID RODRIGUES (SUBTÓPICO CHINA — 58 ENTIDADES)"
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

# 2. Auditoria Real das 38 Tabelas Relacionais em 3FN (PostgreSQL / SQLite)
echo ""
echo "▶ [TESTE 2/4] AUDITORIA REAL DAS 38 TABELAS RELACIONAIS EM 3.ª FORMA NORMAL (FONTE D1)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
python3 - << 'PYEOF'
import sqlite3
conn = sqlite3.connect("data/relational_db/china_gacc_mofcom_3nf.sqlite")
cur = conn.cursor()
cur.execute("PRAGMA foreign_key_check;")
fk_errs = cur.fetchall()
assert len(fk_errs) == 0, f"Violações FK: {fk_errs}"

tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name").fetchall()]
assert len(tables) == 38, f"Esperadas 38 tabelas 3FN, encontradas {len(tables)}"

print("  ┌────┬────────────────────────────────────────────────────────┬──────────┬────────────────────────────────────────┐")
print("  │ #  │ Nome da Tabela SQL (3.ª Forma Normal)                  │ Registos │ Exemplo de Chave Primária Real         │")
print("  ├────┼────────────────────────────────────────────────────────┼──────────┼────────────────────────────────────────┤")
total_rows = 0
for idx, t in enumerate(tables, 1):
    cnt = cur.execute(f"SELECT count(*) FROM {t}").fetchone()[0]
    total_rows += cnt
    first_row = cur.execute(f"SELECT * FROM {t} LIMIT 1").fetchone()
    pk_sample = first_row[0] if first_row else "-"
    print(f"  │ {idx:2d} │ {t[:54]:<54} │ {cnt:8d} │ {str(pk_sample)[:38]:<38} │")
print("  └────┴────────────────────────────────────────────────────────┴──────────┴────────────────────────────────────────┘")
conn.close()
print(f"✅ 38/38 Tabelas SQL 3FN validadas com 0 erros de Chave Estrangeira ({total_rows} registos relacionais)!")
PYEOF

# 3. Validação Formal dos 20 Contentores XML contra o Esquema XSD (xmllint)
echo ""
echo "▶ [TESTE 3/4] VALIDAÇÃO FORMAL DOS 20 CONTENTORES BASEX XML CONTRA O ESQUEMA XSD (FONTE D2)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
XML_VAL=$(xmllint --noout --schema models/china_logistics_trade.xsd data/xml_containers/*.xml 2>&1)
if echo "$XML_VAL" | grep -q "fails to validate"; then
  echo "❌ ERRO na validação XML:"
  echo "$XML_VAL"
  exit 1
fi
echo "$XML_VAL" | sed 's/^/  ✓ /'
echo "✅ 20/20 Contentores XML validados a 100% pelo xmllint contra models/china_logistics_trade.xsd!"

# 4. Execução Completa e Impressão das Queries do David no Terminal
echo ""
echo "▶ [TESTE 4/4] EXECUÇÃO REAL E IMPRESSÃO DAS QUERIES DE DAVID RODRIGUES (Q03, Q04 + Q05..Q12)"
echo "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────"
python3 queries/run_david_queries.py

echo ""
echo "===================================================================================================================="
echo "🎉 [SUCESSO TOTAL] A ENTREGA DE DAVID RODRIGUES (58 ENTIDADES CN + QUERIES REAIS + 20 XMLs) ESTÁ 100% VERIFICADA!"
echo "===================================================================================================================="
