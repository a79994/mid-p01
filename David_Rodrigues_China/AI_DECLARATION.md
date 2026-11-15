# Declaração de Uso de Inteligência Artificial Generativa (Secção 6.2)
**Unidade Curricular:** Modelação e Integração de Dados (DMI) — Mestrado em Engenharia Informática (2026/2027)  
**Instituição:** Faculdade de Ciências e Tecnologia, Universidade do Algarve  
**Docente Coordenadora:** Prof.ª Doutora Paula Cristina Negrão Ventura Martins  
**Autor da Entrega:** David Rodrigues (Subtópico China — 58 Entidades: 38 Tabelas SQL em 3FN + 20 Contentores BaseX XML com XSD)  
**Parceiro de Grupo:** Afonso Bitoque (Subtópico Portugal — 58 Entidades)  

---

## 1. Como Utilizei a Inteligência Artificial no Meu Trabalho
Em cumprimento da **Secção 6.2 do Enunciado**, eu, **David Rodrigues**, declaro de forma transparente como recorri a ferramentas de Inteligência Artificial durante o desenvolvimento deste projeto, garantindo sempre que todas as decisões de modelação das minhas **58 entidades da China**, o esquema relacional em 3.ª Forma Normal, o esquema XSD e as queries foram pensados, revistos e validados por mim e pelo meu colega Afonso Bitoque.

---

## 2. Ferramentas Utilizadas, Finalidade e Validação Humana

| Ferramenta / Componente | Para Que a Usei | Peso no Trabalho | Como Fiz a Validação Humana |
| :--- | :--- | :--- | :--- |
| **Assistente de Programação (Pair-Programming)** | Apoio na geração mais rápida de código repetitivo para popular as minhas 38 tabelas SQL em 3FN e os 20 contentores XML com dados reais pesquisados (GACC, MOFCOM, STA, SAMR, COSCO, BYD, CATL) e escrita do script de teste (`test_submission_david.sh`). | ~30% de apoio na escrita de scripts auxiliares. | Corri validações formais (`PRAGMA foreign_key_check` nas 38 tabelas SQL e `xmllint --noout --schema` nos 20 contentores XML) e verifiquei manualmente os cálculos das minhas queries individuais (Q03 e Q04) e cruzadas (Q05 a Q12). |
| **Google Gemini (`gemini-3.8-flash` / `2.5-flash`)** | Usado no módulo *Estúdio IA* desenvolvido no projeto para estruturar documentos textuais que cruzam com os identificadores `USCC` e `GACC` das minhas bases da China. | ~20% do pipeline de IA do grupo. | Validei que os códigos `USCC` de 18 caracteres e números de *Bill of Lading* extraídos batem certo com as minhas tabelas relacionais e contentores XML. |

---

## 3. Compromisso de Autoria
Eu, **David Rodrigues**, confirmo que conheço a fundo todo o código, o esquema relacional 3FN das 38 tabelas, o esquema XSD dos 20 contentores XML e as queries que entrego, e estou totalmente preparado para os explicar e demonstrar na discussão oral.

Faro, Novembro de 2026.

**David Rodrigues** (em grupo com **Afonso Bitoque**)
