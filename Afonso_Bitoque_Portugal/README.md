# Pacote Oficial de Submissão P1 — Afonso Bitoque (Portugal — 58 Entidades)
**Unidade Curricular:** Modelação e Integração de Dados (14741095) — Mestrado em Engenharia Informática (2026/2027)  
**Faculdade de Ciências e Tecnologia, Universidade do Algarve**  
**Docente Coordenadora:** Prof.ª Doutora Paula Cristina Negrão Ventura Martins  
**Autor:** Afonso Bitoque (Subtópico Portugal)  
**Parceiro de Grupo:** David Rodrigues (Subtópico China)  

---

## 🇵🇹 1. O Meu Subtópico (Portugal — 58 Entidades)
Neste pacote entrego o trabalho que desenvolvi para o subtópico de **Portugal e União Europeia** no nosso projeto sobre o comércio bilateral com a China. Modelei, implementei e populei **58 entidades do lado de Portugal**, divididas por duas fontes heterogéneas:

1. **Fonte A1 — Base de Dados Semi-Estruturada (MongoDB / JSON — 39 Coleções):**
   - Pasta: `data/mongodb_semi_structured/` (`01` a `18` e `65` a `85`)
   - Esquemas formais JSON Schema: `models/mongodb_json_schemas.json`
   - O que modela:
     - **Núcleo Base (`01`–`18`):** Operadores económicos (EORI `PT5...`, NIF, OEA), portos APS Sines e APDL Leixões, pauta TARIC a 10 dígitos, declarações DAU com arrays de adições, escalas marítimas, comboios Yiwu–Entroncamento, carga aérea, entrepostos, transporte e-Fatura, fiscalização CE ASAE, registo CIFER de vinhos/azeite/cortiça, pagamentos SEPA/SWIFT UETR, IDE chinês em Portugal, incentivos AICEP, retalho, e-commerce IOSS, declarações CBAM e estatísticas INE.
     - **Expansão Fim-a-Fim (`65`–`85`):** Rastreabilidade agro-florestal (`65`), lotes de engarrafamento/rolhagem (`66`), Cartas de Crédito SWIFT MT700 (`67`), seguros de crédito COSEC (`68`), Despachantes Oficiais CDO (`69`), sobrestadias *Demurrage & Detention* (`70`), emissões marítimas EU ETS/MRV (`71`), declarações sumárias ICS2/ENS (`72`), Janela Única Logística JUL (`73`), trânsito NCTS T1/T2 (`74`), Armazéns de Depósito Temporário ADT (`75`), controlos sanitários TRACES NT CHED (`76`), impostos especiais EMCS/IEC (`77`), conformidade química REACH/RoHS/SCIP (`78`), medidas anti-dumping UE (`79`), contingentes pautais (`80`), cauções aduaneiras AT (`81`), Informações Pautais Vinculativas IPV/BTI (`82`), auditorias pós-desembaraço AT (`83`), declarações simplificadas e-commerce STADA H7 (`84`) e logística inversa/reembolsos (`85`).
2. **Fonte A2 — Base de Dados Não Estruturada (Texto Livre & OCR) + Motor de IA (19 Corpora):**
   - Pasta: `data/unstructured_corpus/` (`19` a `32` e `86` a `90`: autos da ASAE/DGAV, apreensões de contrafação da AT, certificados OCR, contratos em prosa, logs de frio IoT, fichas químicas MSDS UN3480, cartas de protesto marítimo *Sea Protest*, audiências prévias da AT, traduções de rótulos para mandarim e relatórios de *Due Diligence* KYC).
   - O meu motor de IA: `src/ai_custom_studio.py` e `src/ai_unstructured_to_structured_engine.py` (com NER determinístico e integração opcional com Google Gemini).
   - Base SQLite estruturada pela IA: `data/ai_structured_output/afonso_ai_structured_warehouse.sqlite` (**19 tabelas estruturadas + 1 Grafo de Conhecimento Mestre**).

---

## 📂 2. Estrutura do Meu Pacote de Entrega

```text
entrega_p1_afonso/
├── report/
│   ├── P1_RELATORIO_TECNICO_DMI_2026_2027.pdf         # Relatório Técnico de Grupo (Afonso & David)
│   ├── P1_RELATORIO_INDIVIDUAL_AFONSO_PORTUGAL.pdf    # O meu Relatório Individual (Subtópico Portugal)
│   └── P1_REPORT_AFONSO_COMPLETO.md                   # Fonte Markdown do meu relatório individual
├── src/
│   ├── build_afonso_portugal_db.py                    # Script que gera as minhas 58 entidades de Portugal
│   ├── afonso_expanded_data.py                        # Dados reais das novas coleções (65-85) e textos (86-90)
│   ├── ai_unstructured_to_structured_engine.py        # Pipeline de IA que estrutura os 19 corpora no SQLite
│   └── ai_custom_studio.py                            # Motor de IA com NER e suporte a Gemini
├── data/
│   ├── mongodb_semi_structured/                       # As minhas 39 coleções JSON do MongoDB
│   ├── unstructured_corpus/                           # Os meus 19 corpora de texto livre / OCR / MSDS
│   ├── ai_structured_output/                          # Base SQLite de IA (19 tabelas + Grafo) e JSON
│   └── counterpart_china_data/                        # Dados espelho da China (58 entidades) para queries cruzadas
├── database/
│   ├── setup_and_reset.sh                             # Script de reset e reconstrução das minhas bases
│   └── mongodb_import_init.js                         # Script de importação para MongoDB
├── models/
│   ├── mongodb_json_schemas.json                      # JSON Schemas das minhas coleções
│   └── MODELS_AND_HETEROGENEITY_SPEC.md               # Especificação dos modelos e heterogeneidades
├── queries/
│   ├── run_afonso_queries.py                          # Executa as minhas queries (Q01, Q02 + Q05..Q12)
│   └── expected_results_afonso.json                   # Resultados esperados
├── AI_DECLARATION.md                                  # Declaração de uso de IA (Secção 6.2)
├── README.md                                          # Este guia
└── test_submission_afonso.sh                          # Script de validação automática da minha entrega
```

---

## ⚡ 3. Como Testar a Minha Entrega

### 1. Correr o Teste de Verificação Automática:
```bash
chmod +x test_submission_afonso.sh
./test_submission_afonso.sh
```

### 2. Executar as Minhas Queries (Q01, Q02 e Q05 a Q12):
```bash
python3 queries/run_afonso_queries.py
```
