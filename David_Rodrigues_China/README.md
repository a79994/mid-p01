# Pacote Oficial de Submissão P1 — David Rodrigues (China — 58 Entidades)
**Unidade Curricular:** Modelação e Integração de Dados (14741095) — Mestrado em Engenharia Informática (2026/2027)  
**Faculdade de Ciências e Tecnologia, Universidade do Algarve**  
**Docente Coordenadora:** Prof.ª Doutora Paula Cristina Negrão Ventura Martins  
**Autor:** David Rodrigues (Subtópico China)  
**Parceiro de Grupo:** Afonso Bitoque (Subtópico Portugal)  

---

## 🇨🇳 1. O Meu Subtópico (China — 58 Entidades)
Neste pacote entrego o trabalho que desenvolvi para o subtópico da **República Popular da China** no nosso projeto sobre o comércio bilateral com Portugal. Modelei, implementei e populei **58 entidades do lado da China**, divididas por duas fontes heterogéneas:

1. **Fonte D1 — Base de Dados Estruturada Relacional em 3FN (PostgreSQL / SQLite — 38 Tabelas):**
   - Base de dados: `data/relational_db/china_gacc_mofcom_3nf.sqlite` (`33` a `52` e `91` a `108`)
   - DDL SQL oficial: `models/schema_postgres_3nf.sql`
   - O que modela:
     - **Núcleo Base (`33`–`52`):** Divisão administrativa GB/T 2260, Zonas Francas FTZ, fabricantes sob código USCC de 18 caracteres na SAMR, instalações fabris, pauta aduaneira GACC HS de 10 dígitos, catálogo industrial com pesos em *Jin*, certificações CCC, licenças MOFCOM, contratos B2B, faturas Fapiao normalizadas em cabeçalhos e linhas (3FN), declarações GACC de exportação/importação, quarentena CIQ, reembolsos de IVA da STA, liquidações cambiais SAFE/PBOC, apólices Sinosure, subsídios estatais, aprovações de IDE da NDRC e auditorias ESG.
     - **Expansão Industrial e Aduaneira (`91`–`108`):** Fornecedores *Tier-2* de matérias-primas (`91`), árvores de fabrico *Bill of Materials* (`92`), genealogia de lotes fabris (`93`), Cartas de Crédito UCP 600 via SWIFT MT700 (`94`), discrepâncias documentais em L/C (`95`), intermediários *offshore* em Hong Kong e Macau (`96`), transitários NVOCC e *customs brokers* (`97`), *Packing Lists* ao nível da palete (`98`), manuais de *Processing Trade* (`99`), imposto de consumo especial STA sobre vinhos (`100`), licenças *Dual-Use* do MOFCOM (`101`), certificados de origem CCPIT (`102`), registo de reconhecimento mútuo OEA UE–China (`103`), quotas tarifárias e anti-dumping (`104`), cauções fiscais consolidadas GACC (`105`), decisões vinculativas *Advance Rulings* (`106`), auditorias pós-desembaraço e anti-contrabando (`107`) e proteção aduaneira de propriedade intelectual IPR (`108`).
2. **Fonte D2 — Base de Dados Semi-Estruturada (BaseX XML com Esquema XSD — 20 Contentores):**
   - Pasta: `data/xml_containers/` (`53` a `64` e `109` a `116`)
   - Esquema formal XSD: `models/china_logistics_trade.xsd`, validado a 100% com `xmllint`.
   - O que modela: Portos e terminais (`53`), navios e viagens (`54`), *Master Bills of Lading* (`55`), cartas ferroviárias CIM/SMGS Yiwu–Madrid (`56`), manifestos aéreos IATA Cargo-XML (`57`), pacotes postais UPU S10 (`58`), telemetria IoT *reefer* (`59`), especificações técnicas B2B (`60`), feiras Canton Fair/CIIE (`61`), plataforma de Macau (`62`), inventários de entrepostos francos (`63`), certificados de fumigação ISPM-15 (`64`), planos de estiva CLP e peso VGM (`109`), consolidação *House B/L* (`110`), reconciliação *Three-Stream Matching* 9610/1210 (`111`), eventos de *Gate* e pórtico TOS (`112`), transbordo marítimo em hubs (`113`), sobrestadias *Demurrage & Detention* (`114`), logística inversa em Zona Franca (`115`) e códigos sanitários de cadeia de frio (`116`).

---

## 📂 2. Estrutura do Meu Pacote de Entrega

```text
entrega_p1_david/
├── report/
│   ├── P1_RELATORIO_TECNICO_DMI_2026_2027.pdf         # Relatório Técnico de Grupo (Afonso & David)
│   ├── P1_RELATORIO_INDIVIDUAL_DAVID_CHINA.pdf        # O meu Relatório Individual (Subtópico China)
│   └── P1_REPORT_DAVID_COMPLETO.md                    # Fonte Markdown do meu relatório individual
├── src/
│   ├── build_david_china_db.py                        # Script que gera as minhas 58 entidades da China
│   └── david_expanded_data.py                         # Dados reais das novas tabelas SQL (91-108) e XMLs (109-116)
├── data/
│   ├── relational_db/                                 # Base SQLite 3FN (38 tabelas) e dump SQL
│   ├── xml_containers/                                # Os meus 20 contentores XML BaseX validados por XSD
│   └── counterpart_portugal_data/                     # Dados espelho de Portugal (58 entidades) para queries cruzadas
├── database/
│   ├── setup_and_reset.sh                             # Script de reset e reconstrução das minhas bases
│   └── schema_postgres_3nf.sql                        # DDL Relacional completo em 3FN (38 tabelas)
├── models/
│   ├── china_logistics_trade.xsd                      # Esquema formal XSD para os 20 contentores XML
│   ├── schema_postgres_3nf.sql                        # Esquema relacional em 3FN
│   └── MODELS_AND_HETEROGENEITY_SPEC.md               # Especificação dos modelos e heterogeneidades
├── queries/
│   ├── run_david_queries.py                           # Executa as minhas queries (Q03, Q04 + Q05..Q12)
│   └── expected_results_david.json                    # Resultados esperados
├── AI_DECLARATION.md                                  # Declaração de uso de IA (Secção 6.2)
├── README.md                                          # Este guia
└── test_submission_david.sh                           # Script de validação automática da minha entrega
```

---

## ⚡ 3. Como Testar a Minha Entrega

### 1. Correr o Teste de Verificação Automática:
```bash
chmod +x test_submission_david.sh
./test_submission_david.sh
```

### 2. Executar as Minhas Queries (Q03, Q04 e Q05 a Q12):
```bash
python3 queries/run_david_queries.py
```
