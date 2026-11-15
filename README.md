# Projeto P1: Integração de Dados no Comércio Bilateral Portugal-China

**Unidade Curricular:** Modelação e Integração de Dados (Data Modelling and Integration)  
**Ano Letivo:** 2026/2027  
**Programa de Estudos:** Mestrado em Engenharia Informática  
**Equipa:** Afonso Bitoque (79925) e David Rodrigues (79994)

Este repositório contém a documentação, modelos e artefactos da fase inicial (Projeto P1), focada na conceção e implementação de fontes de dados heterogéneas.

## Descrição do Domínio

O domínio de aplicação foca-se nas transações comerciais de importação e exportação de mercadorias entre Portugal (inserido no mercado único da União Europeia) e a República Popular da China. O ecossistema modela o abismo regulatório, cambial e tarifário entre dois blocos económicos assimétricos. O projeto resolve o desafio de mapear a cadeia de custódia física, documental e financeira das mercadorias, lidando com diferentes regimes políticos, sistemas de classificação aduaneira (TARIC vs. HS Chinês) e infraestruturas financeiras.

## Objetivos do Projeto

O objetivo principal desta fase é desenhar e implementar as fontes de dados locais que ditarão os alicerces para a integração virtual no Projeto P2. Os objetivos específicos incluem:

- Desenhar modelos concetuais, lógicos e físicos para sistemas díspares que operam de forma autónoma.
- Analisar a qualidade da informação recolhida ou gerada.
- Documentar antecipadamente a heterogeneidade estrutural, sintática e semântica existente entre os ecossistemas europeu e asiático.

## Partes Interessadas

A identificação das partes interessadas e a formulação dos requisitos foram estabelecidas com base nas necessidades reais deste domínio:

- **Autoridades Aduaneiras e Fiscais (AT em Portugal e GACC na China):** Necessitam de auditar o valor estatístico das mercadorias e validar a conformidade com as regras de origem e barreiras técnicas.
- **Operadores Económicos (Importadores e Exportadores):** Procuram prever custos aduaneiros (Landed Cost) e gerir os pagamentos.
- **Instituições Financeiras:** Emitem garantias (como Cartas de Crédito) e gerem a flutuação cambial (EUR/CNY).
- **Operadores Logísticos e Despachantes:** Responsáveis pela submissão do processo aduaneiro e transporte físico.

## Requisitos do Utilizador

Os requisitos do sistema ditam as necessidades de informação que serão futuramente convertidas em consultas representativas de dificuldade simples, intermédia e complexa:

- **Mapeamento Tarifário:** O sistema deve permitir a tradução estrutural entre os códigos HS internacionais de 6 dígitos, as extensões europeias de 10 dígitos e as extensões chinesas de 13 dígitos.
- **Rastreabilidade Documental:** É obrigatório associar cada transação a um *dossier* que contenha faturas, conhecimentos de embarque (*Bill of Lading*) e certificados técnicos exigidos.
- **Conformidade Financeira:** O sistema tem de suportar o cálculo de direitos aduaneiros baseados em taxas de câmbio diárias e registar instrumentos de *Trade Finance*.

## Arquitetura e Fontes de Dados Heterogéneas

Para satisfazer as restrições arquitetónicas, cada membro do grupo aborda um subtópico complementar através de duas fontes de dados, garantindo a utilização de diferentes tecnologias de gestão de dados.

### Ecossistema da China Continental (David Rodrigues - 79994)

Responsável pelo núcleo transacional governamental e catálogos dinâmicos asiáticos.

- **Fonte 1 - Estruturada (PostgreSQL):** Base de dados relacional para a Pauta Aduaneira Nacional, taxas de *Export Tax Rebate*, sistema financeiro e o rigoroso registo de operadores económicos (USCC).
- **Fonte 2 - Semi-estruturada (MongoDB):** Base de dados NoSQL documental para acolher especificações técnicas variáveis, relatórios de qualidade e catálogos de produtos de exportação chineses.

### Ecossistema Portugal / União Europeia (Afonso Bitoque - 79925)

Responsável pela infraestrutura de *compliance* legal europeia e consumo de dados comunitários.

- **Fonte 3 - Semi-estruturada (JSON / APIs):** Armazenamento em JSON para simular o consumo de dados abertos (*datasets*) de entidades europeias, focando-se na pauta integrada TARIC e no histórico de taxas de câmbio do Banco Central Europeu.
- **Fonte 4 - Não Estruturada (Armazenamento Bruto):** Repositório local base (sistema de ficheiros) para o arquivo de texto não estruturado, contendo o texto legal dos Tratados Bilaterais e das diretivas comunitárias da União Europeia.

---

## Portal Web Interativo e Entregáveis Finais (P1)

- **Portal Web Interativo (GitHub Pages):** [https://a79994.github.io/mid-p01/](https://a79994.github.io/mid-p01/)
- **Entregáveis Unificados (30 páginas):**
  - `ENTREGA_UNICA_AFONSO_BITOQUE_P1.pdf`
  - `ENTREGA_UNICA_DAVID_RODRIGUES_P1.pdf`
- **Entregáveis Compactos e Individuais (15 páginas):**
  - `ENTREGA_UNICA_15PAG_AFONSO_BITOQUE_P1.pdf`
  - `ENTREGA_UNICA_15PAG_DAVID_RODRIGUES_P1.pdf`
  - `report/P1_RELATORIO_TECNICO_MID_2026_2027.pdf`
  - `Afonso_Bitoque_Portugal/report/P1_RELATORIO_INDIVIDUAL_AFONSO_PORTUGAL.pdf`
  - `David_Rodrigues_China/report/P1_RELATORIO_INDIVIDUAL_DAVID_CHINA.pdf`
