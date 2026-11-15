#!/usr/bin/env python3
"""
=============================================================================
UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
Modelação e Integração de Dados (DMI) - Projeto P1
Script de Demonstração e Visualização de VISTAS (SQL Views)
Autores: Afonso Bitoque (Portugal) & David Rodrigues (China)
=============================================================================
Permite inspecionar as Vistas das bases de dados em modo tabular no terminal,
ou preparar a demonstração para a professora em software tradicional
(DBeaver, DB Browser for SQLite, MongoDB Compass, VS Code).
=============================================================================
"""

import sys
import sqlite3
from pathlib import Path

CHINA_DB = Path(__file__).resolve().parent / "David_Rodrigues_China/data/relational_db/china_gacc_mofcom_3nf.sqlite"
PORTUGAL_DB = Path(__file__).resolve().parent / "Afonso_Bitoque_Portugal/data/ai_structured_output/afonso_ai_structured_warehouse.sqlite"

def format_ascii_table(rows, headers, max_col_width=32):
    if not rows:
        return "  (Sem registos a apresentar)"
    col_widths = [len(h) for h in headers]
    for r in rows:
        for i, val in enumerate(r):
            s = str(val if val is not None else "-")
            col_widths[i] = max(col_widths[i], min(len(s), max_col_width))

    sep_top = "  ┌─" + "─┬─".join("─" * w for w in col_widths) + "─┐"
    sep_mid = "  ├─" + "─┼─".join("─" * w for w in col_widths) + "─┤"
    sep_bot = "  └─" + "─┴─".join("─" * w for w in col_widths) + "─┘"

    header_line = "  │ " + " │ ".join(f"{h[:w]:<{w}}" for h, w in zip(headers, col_widths)) + " │"
    out_lines = [sep_top, header_line, sep_mid]

    for r in rows:
        cells = []
        for val, w in zip(r, col_widths):
            s = str(val if val is not None else "-")
            if len(s) > w:
                s = s[:w - 1] + "…"
            cells.append(f"{s:<{w}}")
        out_lines.append("  │ " + " │ ".join(cells) + " │")
    out_lines.append(sep_bot)
    return "\n".join(out_lines)

def list_and_show_views(target_view=None, limit=10):
    print("=" * 115)
    print("📊 VISTAS SQL (DATABASE VIEWS) DISPONÍVEIS PARA DEMONSTRAÇÃO E SOFTWARE TRADICIONAL")
    print("=" * 115)

    databases = [
        ("🇨🇳 SUBTÓPICO CHINA — David Rodrigues (Relacional 3FN / SQLite)", CHINA_DB),
        ("🇵🇹 SUBTÓPICO PORTUGAL — Afonso Bitoque (Warehouse IA / SQLite)", PORTUGAL_DB),
    ]

    found_any = False
    for db_title, db_path in databases:
        if not db_path.exists():
            print(f"❌ Base de dados não encontrada: {db_path}")
            continue

        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        views = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='view' ORDER BY name").fetchall()]

        print(f"\n📂 {db_title}")
        print(f"   Ficheiro: {db_path}")
        print(f"   Total de Vistas Ativas: {len(views)}")
        print("   " + "─" * 105)

        for idx, v in enumerate(views, 1):
            cur.execute(f"SELECT count(*) FROM {v}")
            cnt = cur.fetchone()[0]

            cur.execute(f"PRAGMA table_info({v})")
            cols = [c[1] for c in cur.fetchall()]

            print(f"   [{idx:02d}] 👁️  {v:<45} │ {cnt:4d} registos │ {len(cols):2d} colunas: ({', '.join(cols[:4])}...)")

            if target_view and (target_view.lower() == "all" or target_view.lower() == v.lower()):
                found_any = True
                cur.execute(f"SELECT * FROM {v} LIMIT {limit}")
                rows = cur.fetchall()
                print(f"\n      🔎 AMOSTRA DA VISTA '{v}' ({min(len(rows), limit)} de {cnt} registos):")
                print(format_ascii_table(rows, cols, max_col_width=28))
                print()

        conn.close()

    print("\n" + "=" * 115)
    print("💡 COMO MOSTRAR ESTAS VISTAS À PROFESSORA EM SOFTWARE TRADICIONAL:")
    print("=" * 115)
    print("1. 🗄️  DB BROWSER FOR SQLITE (Recomendado para SQLite):")
    print("   - Abrir o DB Browser -> 'Abrir Base de Dados' -> Escolher:")
    print(f"     • {CHINA_DB}")
    print(f"     • {PORTUGAL_DB}")
    print("   - Clicar na pasta 'Views' ou no separador 'Navegar Dados' -> Selecionar qualquer vista no dropdown!")
    print("")
    print("2. 🐬 DBEAVER COMMUNITY (Universal Database Tool):")
    print("   - 'Nova Ligação' -> SQLite -> Apontar para os ficheiros .sqlite acima.")
    print("   - Expandir a árvore: Databases -> Views -> Duplo clique em qualquer vista para ver a grelha de dados!")
    print("")
    print("3. 🍃 MONGODB COMPASS (Para a Base NoSQL de Portugal):")
    print("   - Carregar as 39 coleções e correr no terminal: mongosh pt_comercio_internacional database/mongo_create_views.js")
    print("   - No Compass, as vistas aparecem no menu lateral esquerdo com um ícone de 'Olho'!")
    print("")
    print("4. 💻 VISUAL STUDIO CODE / ANTIGRAVITY IDE:")
    print("   - Com a extensão 'SQLite Viewer', basta clicar nos ficheiros .sqlite no explorador de ficheiros!")
    print("=" * 115)

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    list_and_show_views(target_view=arg)
