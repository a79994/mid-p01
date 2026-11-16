#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo auxiliar para geração dos relatórios em PDF de Modelação e Integração de Dados.
Formato académico clássico (Times New Roman 12pt, espaçamento 1,5 no corpo, margens de 2,5 cm).
"""

import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = json.loads((ROOT / "portal_bundle.json").read_text(encoding="utf-8"))

LIVE_URL_GH = "https://mid-p01.vercel.app"
LIVE_URL_VERCEL = LIVE_URL_GH

_db_state = json.loads((ROOT / "database_state.json").read_text(encoding="utf-8"))
TABLES = sorted(_db_state["tables"], key=lambda x: x["num"])

VIEWS_BY_ID = {v["id"]: v for v in BUNDLE["views"]}
QUERIES_BY_ID = {q["query_id"]: q for q in BUNDLE["queries"]}
CODE_BY_ID = {c["id"]: c for c in BUNDLE["code_files"]}
PDFS_LIST = BUNDLE["pdfs"]
TABLE_RECS = BUNDLE["table_records"]

ROMAN = ["i", "ii", "iii", "iv", "v", "vi"]


def clean_academic_str(s: str) -> str:
    """Remove emojis e pontuação artificial (travessões, ponto e vírgula)."""
    if not s:
        return ""
    s = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2190-\u21ff]", "", s)
    s = s.replace("—", ", ").replace("–", "-").replace(";", ",")
    s = s.replace("DMI", "Modelação e Integração de Dados")
    s = s.replace("PDF Oficial Real", "Documento PDF Não Estruturado")
    s = s.replace("PDFs Reais", "Documentos PDF")
    s = s.replace("PDFs reais", "documentos PDF")
    return s.strip()


def plink(route: str, label: str = None) -> str:
    """Hiperligação discreta para o portal web."""
    url = f"{LIVE_URL_GH}/{route}"
    lbl = clean_academic_str(label or f"portal {route}")
    return f'<a class="acad-link" href="{url}" target="_blank">[{html.escape(lbl)}]</a>'


def vlink(route: str, label: str = None) -> str:
    url = f"{LIVE_URL_VERCEL}/{route}"
    lbl = clean_academic_str(label or f"portal {route}")
    return f'<a class="acad-link" href="{url}" target="_blank">[{html.escape(lbl)}]</a>'


def code_excerpt(file_id: str, start_line: int = 1, max_lines: int = 11, fig_num: str = "1.1") -> str:
    c = CODE_BY_ID[file_id]
    lines = c["content"].splitlines()
    sub = lines[start_line - 1 : start_line - 1 + max_lines]
    cleaned_lines = []
    for i, line in enumerate(sub):
        ln = line.replace("—", "-").replace("–", "-").replace("DMI", "MID")
        cleaned_lines.append(f"{start_line + i:03d}  {ln[:92]}")
    numbered = "\n".join(cleaned_lines)
    return (
        f'<div class="fig-caption"><b>Figura {html.escape(fig_num)}.</b> Excerto do ficheiro '
        f'<code>{html.escape(c["path"])}</code> (linhas {start_line} a '
        f'{min(start_line+max_lines-1, c["line_count"])} de {c["line_count"]}) '
        f'{plink("#codigo:" + file_id, "ver ficheiro completo")}</div>'
        f'<pre><code>{html.escape(numbered)}</code></pre>'
    )


def render_table_catalog(tables_subset, tab_num: str, caption: str, max_fields: int = 3) -> str:
    n_rows = len(tables_subset)
    compact = n_rows >= 15
    max_desc = 48 if compact else 68
    row_pad = "1.1px 3px" if compact else "1.8px 3.5px"
    tbl_fs = "6.1pt" if compact else "6.7pt"
    code_fs = "5.9pt" if compact else "6.4pt"
    rows_html = []
    for t in tables_subset:
        tid = t["id"]
        recs = TABLE_RECS.get(tid, [])
        cnt = len(recs) if recs else 8
        flds = ", ".join(f.split(" ")[0] for f in t.get("fields", [])[: (2 if compact else max_fields)])
        desc = clean_academic_str(t.get("description", ""))
        if len(desc) > max_desc:
            desc = desc[: max_desc - 2] + ".."
        rows_html.append(
            f"<tr>"
            f"<td style='padding:{row_pad};text-align:center;'>{t['num']:02d}</td>"
            f"<td style='padding:{row_pad};'><code style='font-size:{code_fs};'>{html.escape(t['name'])}</code> {plink('#tabela:' + tid, 'dados')}</td>"
            f"<td style='padding:{row_pad};'>{html.escape(clean_academic_str(t['label']))}</td>"
            f"<td style='padding:{row_pad};'><code style='font-size:{code_fs};'>{html.escape(t.get('pk', 'id'))}</code> ({html.escape(flds)})</td>"
            f"<td style='padding:{row_pad};text-align:center;'>{cnt}</td>"
            f"<td style='padding:{row_pad};'>{html.escape(desc)}</td>"
            f"</tr>"
        )
    return (
        f'<div class="table-caption"><b>Tabela {html.escape(tab_num)}.</b> {html.escape(clean_academic_str(caption))}</div>'
        f"<table style='table-layout:fixed;font-size:{tbl_fs};line-height:1.03;'><thead><tr>"
        "<th style='width:4%;padding:1.8px 2px;text-align:center;'>N.º</th>"
        "<th style='width:28%;padding:1.8px 3px;'>Identificador da Entidade</th>"
        "<th style='width:18%;padding:1.8px 3px;'>Designação</th>"
        "<th style='width:21%;padding:1.8px 3px;'>Chave Primária e Atributos</th>"
        "<th style='width:5%;padding:1.8px 2px;text-align:center;'>Reg.</th>"
        "<th style='width:24%;padding:1.8px 3px;'>Descrição Funcional</th>"
        "</tr></thead><tbody>" + "".join(rows_html) + "</tbody></table>"
    )


def render_view_box(view_id: str, tab_num: str, max_rows: int = 2) -> str:
    v = VIEWS_BY_ID[view_id]
    code_lines = v["code"].strip().splitlines()[:4]
    code_str = "\n".join(l[:94] for l in code_lines)
    cols = v["columns"][:5]
    ths = "".join(f"<th>{html.escape(str(c))}</th>" for c in cols)
    trs = []
    for r in v["rows"][:max_rows]:
        tds = "".join(f"<td>{html.escape(clean_academic_str(str(r.get(c, '')))[:28])}</td>" for c in cols)
        trs.append(f"<tr>{tds}</tr>")
    return (
        f'<div class="table-caption"><b>Tabela {html.escape(tab_num)}.</b> Vista de base de dados '
        f'<code>{html.escape(v["name"])}</code> ({v["row_count"]} registos) '
        f'{plink("#vistas:" + view_id, "abrir vista")}</div>'
        f'<pre style="margin:1.5pt 0;padding:2.5px 5px;font-size:6.2pt;"><code>{html.escape(code_str)}</code></pre>'
        f'<table style="margin:1.5pt 0 4pt 0;font-size:6.4pt;"><thead><tr>{ths}</tr></thead>'
        f'<tbody>{"".join(trs)}</tbody></table>'
    )


def render_query_box(qid: str, tab_num: str, max_code_lines: int = 5, max_rows: int = 2) -> str:
    q = QUERIES_BY_ID[qid]
    code_lines = q["query_code"].strip().splitlines()[:max_code_lines]
    code_str = "\n".join(l[:94] for l in code_lines)
    out = q["output"]
    cols = list(out[0].keys())[:5] if out else []
    ths = "".join(f"<th>{html.escape(str(c))}</th>" for c in cols)
    trs = []
    for r in out[:max_rows]:
        tds = "".join(f"<td>{html.escape(clean_academic_str(str(r.get(c, '')))[:27])}</td>" for c in cols)
        trs.append(f"<tr>{tds}</tr>")
    title_clean = clean_academic_str(q["title"])
    just_clean = clean_academic_str(q["justification"])[:165]
    return (
        f'<div class="table-caption"><b>Tabela {html.escape(tab_num)}.</b> Consulta {qid} ({html.escape(title_clean)}, '
        f'dificuldade {html.escape(clean_academic_str(q["difficulty_pt"]).lower())}, {html.escape(clean_academic_str(q["responsible"]))}) '
        f'{plink("#queries:" + qid, "ver resultado")}</div>'
        f'<div class="sub-note">{html.escape(just_clean)}</div>'
        f'<pre style="margin:1.5pt 0;padding:2.5px 5px;font-size:6.1pt;"><code>{html.escape(code_str)}</code></pre>'
        f'<table style="margin:1.5pt 0 4pt 0;font-size:6.3pt;"><thead><tr>{ths}</tr></thead>'
        f'<tbody>{"".join(trs)}</tbody></table>'
    )


BASE_CSS = """
@page {
  size: A4 portrait;
  margin: 25mm 25mm 25mm 25mm;
}
* { box-sizing: border-box; }
body {
  font-family: "Times New Roman", Times, "Liberation Serif", Georgia, serif;
  font-size: 12pt;
  line-height: 1.5;
  color: #000000;
  background: #ffffff;
  margin: 0;
  padding: 0;
}
.pdf-page {
  width: 100%;
  height: 245mm;
  max-height: 245mm;
  overflow: hidden;
  page-break-after: always;
  break-after: page;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.pdf-page:last-child {
  page-break-after: auto;
  break-after: auto;
}
.page-body {
  flex: 1;
  overflow: hidden;
}
.page-topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 0.5pt solid #444444;
  padding-bottom: 2px;
  margin-bottom: 6px;
  font-size: 8pt;
  line-height: 1.0;
  color: #222222;
  font-style: italic;
}
.page-footbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-top: 0.5pt solid #444444;
  padding-top: 2px;
  margin-top: 4px;
  font-size: 9pt;
  line-height: 1.0;
  color: #000000;
}
h1 {
  font-family: "Times New Roman", Times, serif;
  font-size: 13pt;
  font-weight: 700;
  color: #000000;
  border-bottom: 0.8pt solid #000000;
  padding-bottom: 2px;
  margin: 0 0 5pt 0;
  line-height: 1.15;
  text-transform: uppercase;
}
h2 {
  font-family: "Times New Roman", Times, serif;
  font-size: 11pt;
  font-weight: 700;
  color: #000000;
  margin: 5pt 0 2.5pt 0;
  line-height: 1.1;
}
h3 {
  font-family: "Times New Roman", Times, serif;
  font-size: 10pt;
  font-weight: 700;
  color: #000000;
  margin: 3.5pt 0 1.5pt 0;
  line-height: 1.1;
}
p {
  font-family: "Times New Roman", Times, serif;
  font-size: 12pt;
  line-height: 1.5;
  margin: 0 0 4pt 0;
  text-align: justify;
  text-indent: 0;
}
ul, ol {
  margin: 0 0 4pt 0;
  padding-left: 18px;
}
li {
  font-size: 10.5pt;
  line-height: 1.2;
  margin-bottom: 2pt;
  text-align: justify;
}
.table-caption, .fig-caption {
  font-size: 8.5pt;
  line-height: 1.1;
  color: #000000;
  margin: 3pt 0 1.5pt 0;
}
.sub-note {
  font-size: 8pt;
  line-height: 1.1;
  color: #111111;
  margin: 1.5pt 0;
  text-align: justify;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5pt 0 4.5pt 0;
  font-size: 7pt;
  line-height: 1.08;
  border-top: 1pt solid #000000;
  border-bottom: 1pt solid #000000;
}
th {
  background: #f2f2f2;
  color: #000000;
  font-weight: 700;
  text-align: left;
  padding: 2.5px 4px;
  border-bottom: 0.8pt solid #000000;
  border-right: 0.4pt solid #888888;
}
th:last-child { border-right: none; }
td {
  padding: 2px 4px;
  border-bottom: 0.4pt solid #cccccc;
  border-right: 0.4pt solid #cccccc;
  vertical-align: top;
  overflow-wrap: anywhere;
  word-break: break-word;
}
td:last-child { border-right: none; }
code {
  font-family: "Courier New", Courier, monospace;
  font-size: 7pt;
  color: #000000;
  overflow-wrap: anywhere;
  word-break: break-word;
}
pre {
  background: #fafafa;
  color: #000000;
  border: 0.5pt solid #666666;
  padding: 3.5px 6px;
  font-family: "Courier New", Courier, monospace;
  font-size: 6.4pt;
  line-height: 1.1;
  margin: 2pt 0 4pt 0;
  overflow: hidden;
  white-space: pre-wrap;
}
pre code { background: transparent; color: #000000; padding: 0; }
.acad-link {
  color: #000066;
  text-decoration: underline;
  font-size: 7pt;
  font-weight: normal;
}
/* Classic Dotted Table of Contents (Índice Tradicional) */
.toc-container {
  margin: 2pt 0 6pt 0;
}
.toc-row {
  display: flex;
  align-items: baseline;
  font-family: "Times New Roman", Times, serif;
  font-size: 8.6pt;
  line-height: 1.22;
  margin-bottom: 1pt;
}
.toc-row.toc-chap {
  font-weight: 700;
  margin-top: 2pt;
}
.toc-row.toc-sub {
  padding-left: 14px;
  font-weight: normal;
  font-size: 8.2pt;
}
.toc-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.toc-dots {
  flex: 1;
  border-bottom: 0.6pt dotted #333333;
  margin: 0 5px;
  height: 0.75em;
}
.toc-page {
  font-weight: 700;
  white-space: nowrap;
  min-width: 16px;
  text-align: right;
}
"""


def _toc_line(title: str, page: str, is_sub: bool = False) -> str:
    cls = "toc-row toc-sub" if is_sub else "toc-row toc-chap"
    return (
        f'<div class="{cls}">'
        f'<span class="toc-title">{html.escape(title)}</span>'
        f'<span class="toc-dots"></span>'
        f'<span class="toc-page">{html.escape(page)}</span>'
        f'</div>'
    )


def build_ualg_pretextual_4pages(student_name: str, partner_name: str, subtitle_focus: str) -> list:
    """
    Constrói as 4 páginas pré-textuais (i, ii, iii, iv) para a entrega unificada de 30 páginas.
    """
    is_afonso = "Afonso" in student_name
    subtopic_label = "Portugal" if is_afonso else "China"

    p_i = f"""
    <div style="text-align:center;height:224mm;display:flex;flex-direction:column;justify-content:space-between;padding:10px 4px;">
      <div>
        <div style="font-size:14pt;font-weight:700;text-transform:uppercase;letter-spacing:0.5px;">UNIVERSIDADE DO ALGARVE</div>
        <div style="font-size:11.5pt;font-weight:700;text-transform:uppercase;margin-top:4px;">FACULDADE DE CIÊNCIAS E TECNOLOGIA</div>
        <div style="font-size:10pt;margin-top:2px;">Departamento de Engenharia Eletrónica e Informática</div>
      </div>

      <div style="margin:18px 0;">
        <div style="font-size:14pt;font-weight:700;line-height:1.35;text-transform:uppercase;">
          MODELAÇÃO DE FONTES DE DADOS HETEROGÉNEAS NO COMÉRCIO BILATERAL ENTRE PORTUGAL E A CHINA
        </div>
        <div style="font-size:11pt;font-style:italic;margin-top:10px;line-height:1.3;">
          {html.escape(clean_academic_str(subtitle_focus))}
        </div>
      </div>

      <div style="margin:10px 0;">
        <div style="font-size:12pt;font-weight:700;">{html.escape(student_name.upper())}</div>
        <div style="font-size:9.5pt;margin-top:3px;">Trabalho desenvolvido em grupo com {html.escape(partner_name)}</div>
        <div style="font-size:10pt;margin-top:14px;line-height:1.35;">
          Relatório do Projeto P1 elaborado no âmbito da Unidade Curricular de<br>
          <b>Modelação e Integração de Dados</b><br>
          <b>Mestrado em Engenharia Informática</b>
        </div>
        <div style="font-size:10pt;margin-top:12px;line-height:1.35;">
          Trabalho efetuado sob a orientação da<br>
          <b>Professora Doutora Paula Cristina Negrão Ventura Martins</b>
        </div>
      </div>

      <div style="font-size:8.5pt;text-align:left;border-top:0.6pt solid #000;border-bottom:0.6pt solid #000;padding:5px 0;line-height:1.25;">
        <b>Portal Web Interativo do Projeto</b><br>
        Endereço online <a class="acad-link" href="{LIVE_URL_GH}/">{LIVE_URL_GH}/</a><br>
        Secções interativas {plink('#pilares', '116 Entidades')} {plink('#vistas', '15 Vistas BD')} {plink('#queries', '12 Consultas')} {plink('#pdfs', '19 Documentos PDF')} {plink('#codigo', 'Código-Fonte')}
      </div>

      <div style="font-size:11pt;font-weight:700;text-transform:uppercase;">
        FARO<br>2026
      </div>
    </div>
    """

    p_ii = f"""
    <h1>Declaração de Autoria do Trabalho</h1>
    <p><b>Título do Trabalho.</b> <i>Modelação de Fontes de Dados Heterogéneas no Comércio Bilateral entre Portugal e a China ({html.escape(clean_academic_str(subtitle_focus))}).</i></p>
    <p>Declaro ser o autor deste trabalho, que é original e inédito. Autores e trabalhos consultados estão devidamente citados no texto e constam da listagem de referências incluída.</p>
    <p><i>Declaration of authorship of work. I declare I am the author of this work, which is original and unpublished. The sources consulted have been duly cited in the text and included in the list of references.</i></p>

    <h1>Direitos de Autor e Copyright</h1>
    <p><b>Copyright em nome de {html.escape(student_name)}, Universidade do Algarve.</b></p>
    <p>A Universidade do Algarve reserva para si o direito, em conformidade com o disposto no Código do Direito de Autor e dos Direitos Conexos, de arquivar, reproduzir e publicar a obra, independentemente do meio utilizado, bem como de a divulgar através de repositórios científicos e de admitir a sua cópia e distribuição para fins meramente educacionais ou de investigação e não comerciais, conquanto seja dado o devido crédito ao autor e editor.</p>
    <p><i>Copyright on behalf of {html.escape(student_name)}, the University of Algarve. The University of Algarve reserves the right to, in accordance with the provisions of the Copyright Law and Code, archive, reproduce, and publish this work in any medium, as well as to disseminate this work through academic repositories and allow it to be copied and distributed for educational, research, and non-commercial purposes, while ensuring credit is given to the work’s author and publisher.</i></p>
    """

    p_iii = f"""
    <h1>Agradecimentos</h1>
    <p>Agradecemos à Professora Doutora Paula Cristina Negrão Ventura Martins pelo acompanhamento e pelas indicações dadas nas aulas da unidade curricular de Modelação e Integração de Dados do Mestrado em Engenharia Informática da Universidade do Algarve.</p>

    <h1>Sumário</h1>
    <p>Este relatório descreve o trabalho realizado para a primeira entrega (P1) da unidade curricular de Modelação e Integração de Dados sobre o comércio bilateral de importações e exportações entre Portugal e a República Popular da China. Para cobrir as onze fases operacionais de uma transação internacional, desde os fornecedores de matérias-primas, árvores de fabrico e cartas de crédito até às declarações pré-chegada, operações portuárias, trânsito aduaneiro, controlos sanitários, taxas anti-dumping e ajustamento carbónico, modelámos 116 entidades distribuídas por quatro fontes de dados heterogéneas. No subtópico de Portugal (Afonso Bitoque, 58 entidades), a Fonte A1 implementa 39 coleções documentais em MongoDB e a Fonte A2 reúne 19 documentos PDF não estruturados (criados a partir de dados públicos reais visto que os processos aduaneiros originais são sigilosos) convertidos para SQLite. No subtópico da China (David Rodrigues, 58 entidades), a Fonte D1 implementa 38 tabelas relacionais em Terceira Forma Normal (3FN) e a Fonte D2 organiza 20 contentores XML validados por esquema XSD, acompanhados por 15 vistas e 12 consultas.</p>
    <p><b>Palavras-chave.</b> Integração Virtual de Dados, Fontes Heterogéneas, Comércio Portugal e China, Bases Documentais e Extração de Texto, Modelo Relacional em 3FN e XML.</p>

    <h1>Abstract</h1>
    <p>This report describes the work developed for the first assignment (P1) of the Data Modelling and Integration course unit on bilateral trade between Portugal and the People’s Republic of China. To cover the eleven operational stages of international trade, ranging from raw material suppliers, bills of materials, and letters of credit to pre-arrival declarations, port terminal operations, customs transit, sanitary controls, countervailing duties, and carbon border adjustments, we modelled 116 entities across four heterogeneous data sources. In the Portugal subtopic (Afonso Bitoque, 58 entities), Source A1 implements 39 MongoDB document collections and Source A2 contains 19 unstructured PDF documents (created by us from real public data since actual customs files are confidential) extracted into SQLite. In the China subtopic (David Rodrigues, 58 entities), Source D1 implements 38 relational tables in Third Normal Form (3NF) and Source D2 models 20 XML containers validated by XSD, accompanied by 15 database views and 12 queries.</p>
    <p><b>Keywords.</b> Virtual Data Integration, Heterogeneous Data Sources, Portugal and China Trade, Document Databases and Text Extraction, 3NF Relational Modelling and XML.</p>
    """

    toc_items = [
        _toc_line("Declaração de Autoria e Direitos de Autor", "ii"),
        _toc_line("Agradecimentos, Sumário e Abstract", "iii"),
        _toc_line("Índice Geral e Lista de Siglas e Abreviaturas", "iv"),
        _toc_line("Capítulo 1. Introdução, Contextualização e Fases do Comércio Bilateral", "1"),
        _toc_line("Capítulo 2. Glossário Técnico, Identificadores Comuns e Casos de Uso", "2"),
        _toc_line("Capítulo 3. Subtópico Portugal, Fontes A1 (MongoDB) e A2 (Documentos PDF)", "3"),
        _toc_line("3.1 Fonte A1 em MongoDB (Coleções 01 a 85) e Script Gerador", "3", is_sub=True),
        _toc_line("3.2 Fonte A2 (19 Documentos PDF Não Estruturados e Extração para SQLite)", "5", is_sub=True),
        _toc_line("Capítulo 4. Subtópico China, Fontes D1 (SQL 3FN) e D2 (Contentores XML)", "6"),
        _toc_line("4.1 Fonte D1 Relacional em 3FN (Tabelas 33 a 108) e Esquema DDL", "6", is_sub=True),
        _toc_line("4.2 Fonte D2 (20 Contentores XML e Validação por Esquema XSD)", "8", is_sub=True),
        _toc_line("Capítulo 5. Análise de Heterogeneidade, Controlo de Qualidade e Vistas", "9"),
        _toc_line("5.1 Matriz de Heterogeneidade para P2 e Validação das 4 Fontes", "9", is_sub=True),
        _toc_line("5.2 Catálogo Geral das 15 Vistas de Base de Dados", "10", is_sub=True),
        _toc_line("Capítulo 6. Consultas Representativas (Q01 a Q12) e Trabalho de Grupo", "11"),
        _toc_line("6.1 Consultas Locais e Federadas (Q01 a Q12) e Distribuição de Tarefas", "11", is_sub=True),
        _toc_line(f"Capítulo 7. Parte Individual ({student_name}), Subtópico {subtopic_label}", "14"),
        _toc_line(f"Capítulo 8. Modelação e Catálogo da Fonte Principal de {subtopic_label}", "15"),
        _toc_line(f"Capítulo 9. Implementação do Código e Segunda Fonte de {subtopic_label}", "19"),
        _toc_line(f"Capítulo 10. Vistas da Base de Dados do Subtópico {subtopic_label}", "21"),
        _toc_line(f"Capítulo 11. Consultas Locais e Federadas do Subtópico {subtopic_label}", "23"),
        _toc_line("Capítulo 12. Testes de Validação, Conclusão e Referências Bibliográficas", "26"),
    ]

    p_iv = f"""
    <h1>Índice Geral</h1>
    <div class="toc-container">
      {"".join(toc_items)}
    </div>

    <h2>Lista de Siglas e Abreviaturas</h2>
    <table>
      <thead><tr><th style="width:16%">Sigla</th><th style="width:36%">Designação Completa</th><th style="width:48%">Descrição no Domínio do Trabalho</th></tr></thead>
      <tbody>
        <tr><td>3FN</td><td>Terceira Forma Normal Relacional</td><td>Normalização aplicada às 38 tabelas SQL da Fonte D1 da China.</td></tr>
        <tr><td>ADT e NCTS</td><td>Armazém de Depósito Temporário e Trânsito</td><td>Regimes aduaneiros suspensivos europeus antes da introdução em livre prática.</td></tr>
        <tr><td>AT e STADA</td><td>Autoridade Tributária e Aduaneira e STADA</td><td>Sistema eletrónico português de processamento das declarações DAU e H7.</td></tr>
        <tr><td>CBAM e ETS</td><td>Mecanismo de Ajustamento Carbónico Fronteiriço</td><td>Instrumentos europeus de tributação de emissões de carbono na importação e transporte marítimo.</td></tr>
        <tr><td>CIF e FOB</td><td>Cost Insurance and Freight e Free On Board</td><td>Incoterms 2020 usados na valoração aduaneira em Portugal (CIF EUR) e na China (FOB CNY).</td></tr>
        <tr><td>CIFER e CIQ</td><td>China Import Food Enterprise Registration</td><td>Registo sanitário chinês obrigatório para exportadores portugueses de vinho, azeite e cortiça.</td></tr>
        <tr><td>EORI e USCC</td><td>Registo de Operador Europeu e Código Chinês</td><td>Chaves únicas de identificação das empresas em Portugal (EORI) e na China (USCC 18 dígitos).</td></tr>
        <tr><td>GACC e MOFCOM</td><td>Alfândega da China e Ministério do Comércio</td><td>Autoridades chinesas responsáveis pelo desalfandegamento e pelas licenças de exportação.</td></tr>
        <tr><td>ICS2 e JUL</td><td>Import Control System 2 e Janela Única Logística</td><td>Sistemas de segurança pré-embarque europeu e de gestão portuária em Sines e Leixões.</td></tr>
        <tr><td>Jin e Wan</td><td>Unidades Chinesas de Massa e de Capital</td><td>Unidades tradicionais onde 1 Jin equivale a 0,5 kg e 1 Wan equivale a 10.000 CNY.</td></tr>
        <tr><td>TARIC e HS6</td><td>Pauta Integrada das Comunidades Europeias</td><td>Classificação pautal a 10 dígitos ligada à pauta chinesa através da raiz comum de 6 dígitos HS6.</td></tr>
      </tbody>
    </table>
    """
    return [p_i, p_ii, p_iii, p_iv]


def build_ualg_pretextual_2pages(student_name: str, subtitle_focus: str) -> list:
    """
    Constrói as 2 páginas pré-textuais (i, ii) para os relatórios de 15 páginas.
    """
    p_i = f"""
    <div style="text-align:center;height:224mm;display:flex;flex-direction:column;justify-content:space-between;padding:10px 4px;">
      <div>
        <div style="font-size:14pt;font-weight:700;text-transform:uppercase;">UNIVERSIDADE DO ALGARVE</div>
        <div style="font-size:11.5pt;font-weight:700;text-transform:uppercase;margin-top:4px;">FACULDADE DE CIÊNCIAS E TECNOLOGIA</div>
        <div style="font-size:10pt;margin-top:2px;">Departamento de Engenharia Eletrónica e Informática</div>
      </div>

      <div style="margin:18px 0;">
        <div style="font-size:14pt;font-weight:700;line-height:1.35;text-transform:uppercase;">
          MODELAÇÃO DE FONTES DE DADOS HETEROGÉNEAS NO COMÉRCIO BILATERAL ENTRE PORTUGAL E A CHINA
        </div>
        <div style="font-size:11pt;font-style:italic;margin-top:10px;line-height:1.3;">
          {html.escape(clean_academic_str(subtitle_focus))}
        </div>
      </div>

      <div style="margin:10px 0;">
        <div style="font-size:12pt;font-weight:700;">{html.escape(student_name.upper())}</div>
        <div style="font-size:10pt;margin-top:14px;line-height:1.35;">
          Relatório do Projeto P1 elaborado no âmbito da Unidade Curricular de<br>
          <b>Modelação e Integração de Dados</b><br>
          <b>Mestrado em Engenharia Informática</b>
        </div>
        <div style="font-size:10pt;margin-top:12px;line-height:1.35;">
          Trabalho efetuado sob a orientação da<br>
          <b>Professora Doutora Paula Cristina Negrão Ventura Martins</b>
        </div>
      </div>

      <div style="font-size:8.5pt;text-align:left;border-top:0.6pt solid #000;border-bottom:0.6pt solid #000;padding:5px 0;line-height:1.25;">
        <b>Portal Web Interativo do Projeto</b><br>
        Endereço online <a class="acad-link" href="{LIVE_URL_GH}/">{LIVE_URL_GH}/</a>
      </div>

      <div style="font-size:11pt;font-weight:700;text-transform:uppercase;">FARO<br>2026</div>
    </div>
    """

    toc_compact = [
        _toc_line("Declaração de Autoria, Direitos de Autor, Sumário e Abstract", "ii"),
        _toc_line("1. Enquadramento, Arquitetura de Dados e Modelação das Fontes", "1"),
        _toc_line("2. Catálogo Técnico das Entidades, Esquemas Formais e Povoamento", "3"),
        _toc_line("3. Implementação do Código Gerador e Estruturação de Dados", "6"),
        _toc_line("4. Vistas de Base de Dados (SQL e MongoDB)", "8"),
        _toc_line("5. Consultas Locais e Federadas (Q01 a Q12)", "10"),
        _toc_line("6. Testes de Validação, Referências Bibliográficas e Declaração de IA", "13"),
    ]

    p_ii = f"""
    <h1>Declaração de Autoria, Sumário, Abstract e Índice</h1>
    <p><b>Declaração de Autoria do Trabalho.</b> Declaro ser o autor deste trabalho, que é original e inédito. Autores e trabalhos consultados estão devidamente citados no texto e constam da listagem de referências incluída.</p>
    <p><b>Copyright em nome de {html.escape(student_name)}, Universidade do Algarve.</b> A Universidade do Algarve reserva para si o direito, em conformidade com o disposto no Código do Direito de Autor e dos Direitos Conexos, de arquivar, reproduzir e publicar a obra, independentemente do meio utilizado, bem como de a divulgar através de repositórios científicos e de admitir a sua cópia e distribuição para fins meramente educacionais ou de investigação e não comerciais, conquanto seja dado o devido crédito ao autor e editor.</p>
    <p><b>Sumário.</b> Este relatório apresenta o projeto P1 da unidade curricular de Modelação e Integração de Dados sobre o comércio bilateral entre Portugal e a China, composto por 116 entidades em quatro fontes heterogéneas (39 coleções MongoDB e 19 documentos PDF não estruturados criados a partir de dados públicos reais e extraídos para SQLite em Portugal, e 38 tabelas relacionais em 3FN e 20 contentores XML validados por XSD na China), 15 vistas de base de dados, 12 consultas (Q01 a Q12) e um portal web interativo. <b>Palavras-chave.</b> Integração Virtual de Dados, Fontes Heterogéneas, Comércio Portugal e China, MongoDB e SQLite, SQL 3FN e XML.</p>
    <p><b>Abstract.</b> This report presents Project P1 for the Data Modelling and Integration course unit on bilateral trade between Portugal and China, featuring 116 entities across four heterogeneous sources (39 MongoDB collections and 19 unstructured PDFs created from real public data and extracted into SQLite for Portugal, plus 38 3NF SQL tables and 20 XSD-validated XML containers for China), 15 database views, 12 queries, and an interactive web portal. <b>Keywords.</b> Virtual Data Integration, Heterogeneous Data Sources, Portugal and China Trade, MongoDB and SQLite, 3NF SQL and XML.</p>
    <h2>Índice Geral</h2>
    <div class="toc-container">
      {"".join(toc_compact)}
    </div>
    """
    return [p_i, p_ii]


def sanitize_html_fragment(frag: str) -> str:
    """
    Remove emojis e substitui travessões, ponto e vírgula e dois pontos a meio de frase.
    """
    frag = re.sub(r"[\U00010000-\U0010ffff\u2600-\u27bf\u2190-\u21ff]", "", frag)
    frag = frag.replace("DMI", "Modelação e Integração de Dados")
    frag = re.sub(
        r'<div class="callout"[^>]*>\s*<div class="callout-title"[^>]*>(.*?)</div>\s*<p[^>]*>(.*?)</p>\s*</div>',
        r"<p><b>\1.</b> \2</p>",
        frag,
        flags=re.S,
    )
    frag = re.sub(r'<div class="callout"[^>]*>(.*?)</div>', r"<div>\1</div>", frag, flags=re.S)
    frag = re.sub(r'<div class="callout-title"[^>]*>(.*?)</div>', r"<p><b>\1.</b></p>", frag, flags=re.S)

    parts = re.split(r"(<[^>]+>)", frag)
    in_code = False
    for i, part in enumerate(parts):
        if i % 2 == 1:
            low = part.lower()
            if low.startswith("<pre") or low.startswith("<code"):
                in_code = True
            elif low.startswith("</pre") or low.startswith("</code"):
                in_code = False
        else:
            if not in_code:
                txt = html.unescape(part)
                txt = txt.replace(" — ", ". ").replace("—", ", ").replace("–", "-")
                txt = txt.replace(";", ",")
                txt = re.sub(r"(?<!http)(?<!https):\s+", ". ", txt)
                parts[i] = html.escape(txt, quote=False)
    return "".join(parts)


def wrap_ualg_document(pre_pages: list, body_pages: list, doc_title: str, top_left: str) -> str:
    out_pages = []
    total_all = len(pre_pages) + len(body_pages)
    top_left_clean = clean_academic_str(top_left)

    for idx, body in enumerate(pre_pages):
        roman_num = ROMAN[idx]
        body_clean = sanitize_html_fragment(body)
        topbar = (
            f'<div class="page-topbar">'
            f'<span>{html.escape(top_left_clean)}</span>'
            f'<span>Portal Web <a class="acad-link" href="{LIVE_URL_GH}/">mid-p01.vercel.app</a></span>'
            f'</div>'
        )
        footbar = (
            f'<div class="page-footbar">'
            f'<span>Universidade do Algarve, Mestrado em Engenharia Informática, Modelação e Integração de Dados (2026/2027)</span>'
            f'<span>{roman_num}</span>'
            f'</div>'
        )
        out_pages.append(
            f'<div class="pdf-page">'
            f'<div class="page-body">{topbar}{body_clean}</div>'
            f'{footbar}'
            f'</div>'
        )

    for idx, body in enumerate(body_pages, start=1):
        body_clean = sanitize_html_fragment(body)
        topbar = (
            f'<div class="page-topbar">'
            f'<span>{html.escape(top_left_clean)}</span>'
            f'<span>Portal Web <a class="acad-link" href="{LIVE_URL_GH}/">mid-p01.vercel.app</a></span>'
            f'</div>'
        )
        footbar = (
            f'<div class="page-footbar">'
            f'<span>Universidade do Algarve, Mestrado em Engenharia Informática, Modelação e Integração de Dados (2026/2027)</span>'
            f'<span>{idx}</span>'
            f'</div>'
        )
        out_pages.append(
            f'<div class="pdf-page">'
            f'<div class="page-body">{topbar}{body_clean}</div>'
            f'{footbar}'
            f'</div>'
        )

    assert len(out_pages) == total_all
    return (
        f"<!DOCTYPE html><html lang='pt'><head><meta charset='UTF-8'>"
        f"<title>{html.escape(clean_academic_str(doc_title))}</title><style>{BASE_CSS}</style></head>"
        f"<body>{''.join(out_pages)}</body></html>"
    )


def render_html_to_pdf(html_str: str, html_path: Path, pdf_path: Path) -> int:
    html_path.parent.mkdir(parents=True, exist_ok=True)
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html_str, encoding="utf-8")
    cmd = [
        "/usr/bin/chromium",
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path.resolve()}",
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    info = subprocess.check_output(["pdfinfo", str(pdf_path)], text=True)
    for line in info.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":")[1].strip())
    return -1
