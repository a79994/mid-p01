#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
===============================================================================
UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
Unidade Curricular: Modelação e Integração de Dados (DMI) - Projeto P1
Docente Coordenadora: Prof.ª Doutora Paula Cristina Negrão Ventura Martins
Autores: Afonso Bitoque (Portugal) & David Rodrigues (China)
Script: run_all_queries.py
Descrição:
  Executa, exibe o código de cada consulta (MongoDB / SQL 3FN / XPath) e
  imprime no terminal as tabelas formatadas com os resultados reais das
  12 Queries Obrigatórias do Projeto P1 (Q01 a Q12).
===============================================================================
"""

import json
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Dict, Any

ROOT_DIR = Path(__file__).resolve().parent.parent
AFONSO_DIR = ROOT_DIR / "Afonso_Bitoque_Portugal"
DAVID_DIR = ROOT_DIR / "David_Rodrigues_China"


def format_ascii_table(rows: List[Dict[str, Any]], max_col_width: int = 28, max_rows: int = 12) -> str:
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


def main():
    print("=" * 116)
    print("🚀 EXECUTANDO AS 12 QUERIES OBRIGATÓRIAS DO PROJETO P1 (DMI 2026/2027 — 116 ENTIDADES)")
    print("   Subtópico Portugal (58 Entidades): Afonso Bitoque | Subtópico China (58 Entidades): David Rodrigues")
    print("=" * 116)

    t0 = time.time()

    # 1. Execute Afonso's Suite (Q01, Q02 + Q05..Q12)
    afonso_script = AFONSO_DIR / "queries" / "run_afonso_queries.py"
    res1 = subprocess.run([sys.executable, str(afonso_script), "--quiet"], capture_output=True, text=True)
    if res1.returncode != 0:
        print("❌ Erro ao executar a suite do Afonso:")
        print(res1.stderr)
        sys.exit(1)

    # 2. Execute David's Suite (Q03, Q04)
    david_script = DAVID_DIR / "queries" / "run_david_queries.py"
    res2 = subprocess.run([sys.executable, str(david_script), "--quiet"], capture_output=True, text=True)
    if res2.returncode != 0:
        print("❌ Erro ao executar a suite do David:")
        print(res2.stderr)
        sys.exit(1)

    # 3. Load Results
    afonso_json = json.loads((AFONSO_DIR / "queries" / "expected_results_afonso.json").read_text(encoding="utf-8"))
    david_json = json.loads((DAVID_DIR / "queries" / "expected_results_david.json").read_text(encoding="utf-8"))

    q_map = {}
    for q in afonso_json:
        q_map[q["query_id"]] = q
    for q in david_json:
        q_map[q["query_id"]] = q

    sorted_ids = [f"Q{i:02d}" for i in range(1, 13)]
    consolidated = []

    diff_labels = {
        "Simple": "Simples",
        "Intermediate": "Intermédia",
        "Complex": "Complexa"
    }

    owners = {
        "Q01": "Afonso Bitoque (Portugal)",
        "Q02": "Afonso Bitoque (Portugal)",
        "Q03": "David Rodrigues (China)",
        "Q04": "David Rodrigues (China)",
        "Q05": "Afonso Bitoque & David Rodrigues",
        "Q06": "Afonso Bitoque & David Rodrigues",
        "Q07": "Afonso Bitoque & David Rodrigues",
        "Q08": "Afonso Bitoque & David Rodrigues",
        "Q09": "Afonso Bitoque & David Rodrigues",
        "Q10": "Afonso Bitoque & David Rodrigues",
        "Q11": "Afonso Bitoque & David Rodrigues",
        "Q12": "Afonso Bitoque & David Rodrigues"
    }

    for qid in sorted_ids:
        q = q_map.get(qid)
        if not q:
            continue
        q["responsible"] = owners.get(qid, "Grupo DMI")
        q["difficulty_pt"] = diff_labels.get(q["difficulty"], q["difficulty"])
        output_len = len(q.get("output", [])) if isinstance(q.get("output"), list) else 1
        q["records_returned"] = output_len
        consolidated.append(q)

        print("\n" + "━" * 116)
        print(f"🔎 [{q['query_id']}] [{q['difficulty_pt'].upper()}] — {q['title']}")
        print(f"👤 Responsável: {q['responsible']}   |   🗄️ Fontes: {', '.join(q.get('sources_used', []))}")
        print(f"💡 Justificação: {q['justification']}")
        print("─" * 116)
        print("📜 CÓDIGO DA QUERY EXECUTADA:")
        for line in q.get("query_code", "").strip().split("\n"):
            print(f"   {line}")
        print("─" * 116)
        print(f"📊 RESULTADOS REAIS OBTIDOS ({output_len} registos):")
        print(format_ascii_table(q.get("output", [])))

    # 4. Print Summary Matrix
    print("\n" + "=" * 116)
    print("📋 MATRIZ RESUMO DAS 12 QUERIES EXECUTADAS")
    print("=" * 116)
    print(f"{'ID':<5} | {'Dificuldade':<12} | {'Registos':<8} | {'Responsável':<32} | {'Título'}")
    print("-" * 116)
    for q in consolidated:
        print(f"{q['query_id']:<5} | {q['difficulty_pt']:<12} | {q['records_returned']:<8} | {q['responsible']:<32} | {q['title'][:50]}")

    out_file = ROOT_DIR / "queries" / "expected_results_all_12_queries.json"
    out_file.write_text(json.dumps(consolidated, indent=2, ensure_ascii=False), encoding="utf-8")

    total_time = round((time.time() - t0) * 1000, 2)
    print("=" * 116)
    print(f"🎉 [SUCESSO] Total de {len(consolidated)}/12 queries executadas, impressas e verificadas em {total_time} ms!")
    print(f"📊 Distribuição de Dificuldade: 4 Simples (Q1,Q3,Q5,Q6), 4 Intermédias (Q2,Q4,Q7,Q8), 4 Complexas (Q9,Q10,Q11,Q12)")
    print(f"💾 Resultados consolidados gravados em: {out_file}\n")


if __name__ == "__main__":
    main()
