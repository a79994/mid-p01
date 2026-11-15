# Declaração de Uso de Inteligência Artificial Generativa (Secção 6.2)
**Unidade Curricular:** Modelação e Integração de Dados (DMI) — Mestrado em Engenharia Informática (2026/2027)  
**Instituição:** Faculdade de Ciências e Tecnologia, Universidade do Algarve  
**Docente Coordenadora:** Prof.ª Doutora Paula Cristina Negrão Ventura Martins  
**Autor da Entrega:** Afonso Bitoque (Subtópico Portugal — 58 Entidades: 39 Coleções MongoDB + 19 Corpora de Texto / Tabelas SQLite IA)  
**Parceiro de Grupo:** David Rodrigues (Subtópico China — 58 Entidades)  

---

## 1. Como Utilizei a Inteligência Artificial no Meu Trabalho
Em cumprimento da **Secção 6.2 do Enunciado**, eu, **Afonso Bitoque**, declaro de forma transparente como recorri a ferramentas de Inteligência Artificial durante o desenvolvimento deste projeto, garantindo sempre que todas as decisões de modelação das minhas **58 entidades de Portugal**, os JSON Schemas, o pipeline de extração e as queries foram pensados, revistos e validados por mim e pelo meu colega David Rodrigues.

---

## 2. Ferramentas Utilizadas, Finalidade e Validação Humana

| Ferramenta / Componente | Para Que a Usei | Peso no Trabalho | Como Fiz a Validação Humana |
| :--- | :--- | :--- | :--- |
| **Google Gemini (`gemini-3.8-flash` / `2.5-flash`)** | Integrado como opção interativa no meu módulo *Estúdio IA* (`src/ai_custom_studio.py`) para testar a extração de entidades aduaneiras a partir dos 19 documentos de texto não estruturado de Portugal (autos da ASAE, fichas químicas MSDS, cartas de protesto marítimo e audiências prévias da AT). | ~20% do pipeline de IA (chamada opcional via API). | Revi manualmente os campos extraídos, validei os formatos com expressões regulares (`MRN`, `EORI`, `USCC`, `TARIC`) e verifiquei a consistência antes de gravar na base SQLite `afonso_ai_structured_warehouse.sqlite`. |
| **Assistente de Programação (Pair-Programming)** | Apoio na geração mais rápida de código repetitivo para popular as minhas 39 coleções MongoDB e 19 corpora de texto com dados reais pesquisados (INE, AICEP, TARIC, APS Sines) e escrita do script de teste (`test_submission_afonso.sh`). | ~30% de apoio na escrita de scripts auxiliares. | Validei todos os ficheiros JSON, testei as 19 tabelas do Warehouse SQLite e verifiquei manualmente os resultados das minhas queries individuais (Q01 e Q02) e cruzadas (Q05 a Q12). |
| **Motor Heurístico Local (Python Puro — NER)** | Motor determinístico que programei localmente sem dependências externas para garantir que a estruturação dos 19 textos livres funciona 100% offline. | 100% código local do projeto. | Testei documento a documento nos 19 corpora de Portugal, confirmando 100% de precisão na extração das chaves de ligação com o MongoDB e com as bases da China. |

---

## 3. Compromisso de Autoria
Eu, **Afonso Bitoque**, confirmo que conheço a fundo todo o código, os esquemas das minhas 58 entidades de Portugal e as queries que entrego, e estou totalmente preparado para os explicar e demonstrar na discussão oral.

Faro, Novembro de 2026.

**Afonso Bitoque** (em grupo com **David Rodrigues**)
