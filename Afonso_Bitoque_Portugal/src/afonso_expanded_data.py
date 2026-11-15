#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expanded End-to-End Granular Collections & Unstructured Corpora for Afonso Bitoque (Portugal).
Adds:
  - 21 New MongoDB Semi-Structured Collections (65 to 85) -> Total 39 MongoDB Collections
  - 5 New Unstructured Text Corpora (86 to 90) -> Total 19 Unstructured Corpora & AI Tables
"""

true = True
false = False
null = None


def get_expanded_mongo_collections():
    c = {}

    # 65. pt_rastreabilidade_origem_agro_florestal (N04: EUDR & GeoJSON Parcel Traceability)
    c["65_pt_rastreabilidade_origem_agro_florestal"] = [
        {
            "_id": "EUDR-PT-2026-001",
            "registo_eudr_ue": "EUDR-DDS-PT-2026-009811",
            "eori_produtor": "PT500077889",
            "nif_produtor": "500077889",
            "empresa_titular": "Corticeira Amorim, SGPS, S.A.",
            "tipo_materia_prima": "Cortiça Natural em Prancha (Quercus suber)",
            "herdade_ou_exploracao": "Herdade da Baliza & Montado de Coruche (Santarém/Évora)",
            "area_hectares": 3420.5,
            "certificacao_florestal": "FSC 100% (FSC-C012345) & PEFC",
            "poligono_geojson_centroide": {"lat": 38.9581, "lon": -8.5264},
            "data_extracao_cortica": "15/07/2025",
            "conformidade_desflorestacao_eudr": "ISENTO_DESFLORESTACAO_VERIFICADO",
            "fatura_exportacao_associada": "INV-PT-2026-9902"
        },
        {
            "_id": "EUDR-PT-2026-002",
            "registo_eudr_ue": "EUDR-DDS-PT-2026-009812",
            "eori_produtor": "PT500055214",
            "nif_produtor": "500055214",
            "empresa_titular": "The Navigator Company, S.A.",
            "tipo_materia_prima": "Madeira de Eucalipto (Eucalyptus globulus) para Pasta BEKP",
            "herdade_ou_exploracao": "Unidades Florestais do Baixo Vouga e Figueira da Foz",
            "area_hectares": 12850.0,
            "certificacao_florestal": "FSC Forest Management & PEFC Portugal",
            "poligono_geojson_centroide": {"lat": 40.1502, "lon": -8.8612},
            "data_extracao_cortica": "10/02/2026",
            "conformidade_desflorestacao_eudr": "ISENTO_DESFLORESTACAO_VERIFICADO",
            "fatura_exportacao_associada": "INV-PT-2026-9904"
        },
        {
            "_id": "EUDR-PT-2026-003",
            "registo_eudr_ue": "IVDP-PARCELA-DOURO-2026-041",
            "eori_produtor": "PT500265432",
            "nif_produtor": "500265432",
            "empresa_titular": "Symington Family Estates - Vinhos, S.A.",
            "tipo_materia_prima": "Uvas de Vinha Letra A (Touriga Nacional & Touriga Franca)",
            "herdade_ou_exploracao": "Quinta dos Malvedos & Quinta do Bomfim (Pinhão / Alijó)",
            "area_hectares": 412.8,
            "certificacao_florestal": "Sustentabilidade Vinhos de Portugal / IVDP",
            "poligono_geojson_centroide": {"lat": 41.1904, "lon": -7.5451},
            "data_extracao_cortica": "22/09/2025",
            "conformidade_desflorestacao_eudr": "ORIGEM_DOP_DOURO_CERTIFICADA",
            "fatura_exportacao_associada": "INV-PT-2026-9901"
        },
        {
            "_id": "EUDR-PT-2026-004",
            "registo_eudr_ue": "DGAV-EXPLORACAO-ALENTEJO-2026-08",
            "eori_produtor": "PT508112244",
            "nif_produtor": "508112244",
            "empresa_titular": "Maporal - Matadouro de Porco Alentejano, S.A.",
            "tipo_materia_prima": "Suínos de Raça Alentejana e Cruzados Criados em Montanheira",
            "herdade_ou_exploracao": "Marca de Exploração DGAV PT-07-REG-441 (Reguengos de Monsaraz)",
            "area_hectares": 1850.0,
            "certificacao_florestal": "Biossegurança Nível A DGAV / Peste Suína Africana Free",
            "poligono_geojson_centroide": {"lat": 38.4251, "lon": -7.5349},
            "data_extracao_cortica": "05/04/2026",
            "conformidade_desflorestacao_eudr": "BIOSSEGURANCA_GACC_VALIDADA",
            "fatura_exportacao_associada": "INV-PT-2026-9905"
        }
    ]

    # 66. pt_lotes_producao_engarrafamento_abate (N05: Bottling & Slaughter Batch Logs)
    c["66_pt_lotes_producao_engarrafamento_abate"] = [
        {
            "_id": "LOTE-PROD-PT-001",
            "codigo_lote_industrial": "LOT-SH-SYM-2026A",
            "eori_produtor": "PT500265432",
            "codigo_cifer_gacc": "CPRT18000102000101",
            "tipo_processamento": "Engarrafamento e Estágio em Cave (Vila Nova de Gaia)",
            "selo_garantia_ivdp_intervalo": "IVDP-AA-900120001 a IVDP-AA-900240000",
            "grau_alcoolico_vol_pct": 20.0,
            "acidez_total_g_l": 4.35,
            "so2_total_mg_l": 82.0,
            "unidades_produzidas": 120000,
            "fatura_associada": "INV-PT-2026-9901",
            "mrn_exportacao_dau": "26PT000140EX009901"
        },
        {
            "_id": "LOTE-PROD-PT-002",
            "codigo_lote_industrial": "LOT-TAO-MAP-2026D",
            "eori_produtor": "PT508112244",
            "codigo_cifer_gacc": "CPRT18000101000505",
            "tipo_processamento": "Abate Sanitário, Desmancha e Ultracongelação em Túnel (-40C)",
            "selo_garantia_ivdp_intervalo": "MARCA-SALUBRIDADE-PT-07-041-CE",
            "grau_alcoolico_vol_pct": 0.0,
            "temperatura_nucleo_congelacao_c": -18.5,
            "teste_pcr_psa_peste_suina": "NEGATIVO_100_PORCENTO",
            "unidades_produzidas": 450000,
            "fatura_associada": "INV-PT-2026-9905",
            "mrn_exportacao_dau": "26PT000395EX009905"
        },
        {
            "_id": "LOTE-PROD-PT-003",
            "codigo_lote_industrial": "LOT-HQ-SOV-2026C",
            "eori_produtor": "PT500112233",
            "codigo_cifer_gacc": "CPRT18000401000303",
            "tipo_processamento": "Extração a Frio e Engarrafamento de Azeite Virgem Extra",
            "selo_garantia_ivdp_intervalo": "LOTE-SOV-BARREIRO-2026-04C",
            "acidez_livre_oleico_pct": 0.19,
            "indice_peroxidos_meq_kg": 6.8,
            "unidades_produzidas": 180000,
            "fatura_associada": "INV-PT-2026-9903",
            "mrn_exportacao_dau": "26PT000395EX009903"
        },
        {
            "_id": "LOTE-PROD-PT-004",
            "codigo_lote_industrial": "LOT-SH-AMO-2026B",
            "eori_produtor": "PT500077889",
            "codigo_cifer_gacc": "CPRT18009901000202",
            "tipo_processamento": "Brocação, Lavação sem Cloro e Triagem Individual NDTech Anti-TCA",
            "selo_garantia_ivdp_intervalo": "SYSTECODE-PREMIUM-CELIEGE-2026",
            "teor_tca_tricloroanisol_ng_l": 0.2,
            "tratamento_superficie": "Parafina e Silicone Alimentar FDA/GB9685",
            "unidades_produzidas": 15000000,
            "fatura_associada": "INV-PT-2026-9902",
            "mrn_exportacao_dau": "26PT000140EX009902"
        }
    ]

    # 67. pt_creditos_documentarios_garantias_bancarias (N09: Portuguese Bank Trade Finance)
    c["67_pt_creditos_documentarios_garantias_bancarias"] = [
        {
            "_id": "TF-PT-BCP-2026-001",
            "referencia_lc_swift": "LC-BCP-BOC-2026-0001",
            "banco_nacional": "Millennium bcp (Banco Comercial Português, S.A.)",
            "swift_bic_nacional": "BCOMPTPLXXX",
            "banco_correspondente_china": "Bank of China Jiangsu Branch (BKCHCNBJ940)",
            "ordenador_ou_beneficiario_pt_eori": "PT517890123",
            "contraparte_china_uscc": "91320413MA1M9Y2C4B",
            "contrato_comercial": "CN-PT-CTR-2026-001",
            "tipo_instrumento_ucp600": "Carta de Crédito Documentário Irrevogável Confirmada à Vista (MT700)",
            "montante_coberto_eur": 18500000.0,
            "cobertura_forward_cambial": "Swap Cambial EUR/CNH Taxa Fixa 7.8200",
            "comissao_abertura_confirmacao_eur": 27750.0,
            "estado_dossier": "ATIVO_LIQUIDACAO_PARCIAL_HONRADA"
        },
        {
            "_id": "TF-PT-CGD-2026-003",
            "referencia_lc_swift": "LC-CGD-CCB-2026-0003",
            "banco_nacional": "Caixa Geral de Depósitos, S.A. (CGD)",
            "swift_bic_nacional": "CGDIPTPLXXX",
            "banco_correspondente_china": "China Construction Bank Shaanxi (PCBCCNBJSAX)",
            "ordenador_ou_beneficiario_pt_eori": "PT500697256",
            "contraparte_china_uscc": "91610132724912345X",
            "contrato_comercial": "CN-PT-CTR-2026-003",
            "tipo_instrumento_ucp600": "Crédito Documentário de Importação Green Trade Finance (MT700)",
            "montante_coberto_eur": 6725000.0,
            "cobertura_forward_cambial": "Forward EUR/USD 1.0825",
            "comissao_abertura_confirmacao_eur": 10087.5,
            "estado_dossier": "LIQUIDADO_SEM_RESERVAS"
        },
        {
            "_id": "TF-PT-BPI-2026-004",
            "referencia_lc_swift": "LC-BPI-BOC-2026-0004",
            "banco_nacional": "Banco BPI, S.A.",
            "swift_bic_nacional": "BBPIPTPLXXX",
            "banco_correspondente_china": "Bank of China Fujian Branch (BKCHCNBJ720)",
            "ordenador_ou_beneficiario_pt_eori": "PT503412890",
            "contraparte_china_uscc": "91350900587527783P",
            "contrato_comercial": "CN-PT-CTR-2026-004",
            "tipo_instrumento_ucp600": "Carta de Crédito Irrevogável + Garantia de Boa Execução 10% (MT760)",
            "montante_coberto_eur": 10260000.0,
            "cobertura_forward_cambial": "N/A - Faturação Direta em EUR",
            "comissao_abertura_confirmacao_eur": 15390.0,
            "estado_dossier": "DISCREPANCIA_MENOR_LEVANTADA_E_PAGO"
        },
        {
            "_id": "TF-PT-HTB-2026-017",
            "referencia_lc_swift": "LC-HTB-ICBC-2026-0017",
            "banco_nacional": "Haitong Bank, S.A. (Sede Lisboa)",
            "swift_bic_nacional": "ESSIPTPLXXX",
            "banco_correspondente_china": "ICBC Beijing Municipal Branch (ICBKCNBJBJM)",
            "ordenador_ou_beneficiario_pt_eori": "PT503412890",
            "contraparte_china_uscc": "911100007178071858",
            "contrato_comercial": "CN-PT-CTR-2026-017",
            "tipo_instrumento_ucp600": "Crédito Documentário Estruturado Luso-Chinês (MT700)",
            "montante_coberto_eur": 8500000.0,
            "cobertura_forward_cambial": "Conta Corrente CIPS RMB Lisboa",
            "comissao_abertura_confirmacao_eur": 12750.0,
            "estado_dossier": "EM_CONFERENCIA_DOCUMENTAL"
        }
    ]

    # 68. pt_seguros_credito_exportacao_cosec (N10: COSEC Export Credit Insurance)
    c["68_pt_seguros_credito_exportacao_cosec"] = [
        {
            "_id": "COSEC-PT-2026-001",
            "numero_apolice_cosec": "COSEC-ALLIANZ-EXP-2026-8801",
            "seguradora_nacional": "COSEC - Companhia de Seguro de Créditos, S.A. (Allianz Trade)",
            "exportador_segurado_eori": "PT500265432",
            "comprador_devedor_china_uscc": "91110000101123456N",
            "fatura_coberta": "INV-PT-2026-9901",
            "limite_credito_aprovado_eur": 5000000.0,
            "percentagem_cobertura_risco_pct": 90.0,
            "premio_seguro_pago_eur": 9135.0,
            "garantia_estado_portugues": true,
            "classificacao_risco_comprador_cn": "Grau 1 - SOE Estatal Chinesa (COFCO)",
            "estado_sinistralidade": "REGULAR_SEM_MORA"
        },
        {
            "_id": "COSEC-PT-2026-002",
            "numero_apolice_cosec": "COSEC-ALLIANZ-EXP-2026-8802",
            "seguradora_nacional": "COSEC - Companhia de Seguro de Créditos, S.A.",
            "exportador_segurado_eori": "PT500077889",
            "comprador_devedor_china_uscc": "91110000101123456N",
            "fatura_coberta": "INV-PT-2026-9902",
            "limite_credito_aprovado_eur": 6000000.0,
            "percentagem_cobertura_risco_pct": 90.0,
            "premio_seguro_pago_eur": 11314.8,
            "garantia_estado_portugues": false,
            "classificacao_risco_comprador_cn": "Grau 1 - Excelente",
            "estado_sinistralidade": "REGULAR_SEM_MORA"
        },
        {
            "_id": "COSEC-PT-2026-003",
            "numero_apolice_cosec": "COSEC-AGRO-EXP-2026-8805",
            "seguradora_nacional": "COSEC / Linha de Apoio Seguro Crédito AICEP",
            "exportador_segurado_eori": "PT508112244",
            "comprador_devedor_china_uscc": "91110000101123456N",
            "fatura_coberta": "INV-PT-2026-9905",
            "limite_credito_aprovado_eur": 4500000.0,
            "percentagem_cobertura_risco_pct": 95.0,
            "premio_seguro_pago_eur": 12375.0,
            "garantia_estado_portugues": true,
            "classificacao_risco_comprador_cn": "Grau 1 - Cobertura Risco Político e Fitossanitário",
            "estado_sinistralidade": "REGULAR_SEM_MORA"
        },
        {
            "_id": "COSEC-PT-2026-004",
            "numero_apolice_cosec": "COSEC-IND-EXP-2026-8804",
            "seguradora_nacional": "COSEC - Companhia de Seguro de Créditos, S.A.",
            "exportador_segurado_eori": "PT500055214",
            "comprador_devedor_china_uscc": "91370200163562681G",
            "fatura_coberta": "INV-PT-2026-9904",
            "limite_credito_aprovado_eur": 10000000.0,
            "percentagem_cobertura_risco_pct": 90.0,
            "premio_seguro_pago_eur": 14700.0,
            "garantia_estado_portugues": false,
            "classificacao_risco_comprador_cn": "Grau 1 - Multinacional Cotada Qingdao",
            "estado_sinistralidade": "REGULAR_SEM_MORA"
        }
    ]

    # 69. pt_transitarios_despachantes_oficiais_cdo (N15: Freight Forwarders & Customs Brokers PT)
    c["69_pt_transitarios_despachantes_oficiais_cdo"] = [
        {
            "_id": "CDO-PT-001",
            "cedula_profissional_cdo": "CDO-PT-1482",
            "eori_representante": "PT500991122",
            "nif_representante": "500991122",
            "nome_sociedade": "Rangel Aduaneira & Logística Global, S.A.",
            "alvara_transitario_imt": "IMT-TRANS-200145",
            "modalidade_representacao_cau": "Representação Direta (Art. 18.º n.º 1 do CAU)",
            "estancias_operacao": ["PTSIN - Sines", "PTLEI - Leixões", "PTLIS - Aeroporto Lisboa"],
            "parceiro_nvocc_china_id": "BRK-CN-SINOTRANS-01",
            "declaracoes_dau_submetidas": ["26PT000395IM008801", "26PT000395IM008802", "26PT000140EX009901"]
        },
        {
            "_id": "CDO-PT-002",
            "cedula_profissional_cdo": "CDO-PT-2109",
            "eori_representante": "PT501223344",
            "nif_representante": "501223344",
            "nome_sociedade": "Garland Transitários & Despachos Aduaneiros, S.A.",
            "alvara_transitario_imt": "IMT-TRANS-199812",
            "modalidade_representacao_cau": "Representação Direta com Garantia Global",
            "estancias_operacao": ["PTLEI - Leixões", "PTSIN - Sines", "PTENT - Entroncamento"],
            "parceiro_nvocc_china_id": "BRK-CN-COSCO-LOG-02",
            "declaracoes_dau_submetidas": ["26PT000140IM008804", "26PT000395IM008806", "26PT000140EX009902"]
        },
        {
            "_id": "CDO-PT-003",
            "cedula_profissional_cdo": "CDO-PT-3390",
            "eori_representante": "PT502334455",
            "nif_representante": "502334455",
            "nome_sociedade": "Orey Shipping & Kuehne+Nagel Portugal, Lda.",
            "alvara_transitario_imt": "IMT-TRANS-200890",
            "modalidade_representacao_cau": "Representação Indireta (Art. 18.º CAU - Solidariamente Responsável)",
            "estancias_operacao": ["PTSIN - Sines", "PTLIS - Lisboa"],
            "parceiro_nvocc_china_id": "BRK-CN-KUEHNE-SZ-03",
            "declaracoes_dau_submetidas": ["26PT000395IM008803", "26PT000510IM008807"]
        },
        {
            "_id": "CDO-PT-004",
            "cedula_profissional_cdo": "CDO-PT-4012",
            "eori_representante": "PT500077568",
            "nif_representante": "500077568",
            "nome_sociedade": "CTT Expresso - Representação Aduaneira E-Commerce IOSS, S.A.",
            "alvara_transitario_imt": "IMT-TRANS-199501",
            "modalidade_representacao_cau": "Representação Indireta Lotes Expresso STADA-H7",
            "estancias_operacao": ["PTLIS - Terminal Carga Aérea Lisboa"],
            "parceiro_nvocc_china_id": "BRK-CN-CAINIAO-CB-06",
            "declaracoes_dau_submetidas": ["26PT000520IM008805"]
        }
    ]

    # 70. pt_sobrestadias_contentores_demurrage_detention (N22: Port Demurrage & Detention)
    c["70_pt_sobrestadias_contentores_demurrage_detention"] = [
        {
            "_id": "DEM-PT-2026-001",
            "fatura_sobrestadia_no": "PSA-SIN-DEM-2026-0411",
            "numero_contentor_iso": "CATU8004401",
            "numero_bl_master": "COSU6288991104",
            "mrn_dau": "26PT000140IM008804",
            "terminal_portuario": "TCL - Terminal de Contentores de Leixões",
            "dias_livres_contratados_free_time": 7,
            "dias_efetivos_permanencia": 10,
            "dias_sobrestadia_faturados": 3,
            "tarifa_diaria_demurrage_eur": 110.0,
            "tarifa_ligacao_eletrica_reefer_eur": 0.0,
            "total_liquidado_eur": 330.0,
            "motivo_retencao": "Canal Vermelho - Vistoria Física Conjunta ASAE, DGEG e Perito de Seguros"
        },
        {
            "_id": "DEM-PT-2026-002",
            "fatura_sobrestadia_no": "PSA-SIN-DEM-2026-0412",
            "numero_contentor_iso": "COSU8001101",
            "numero_bl_master": "COSU6288991101",
            "mrn_dau": "26PT000395IM008801",
            "terminal_portuario": "PSA Sines - Terminal XXI",
            "dias_livres_contratados_free_time": 10,
            "dias_efetivos_permanencia": 4,
            "dias_sobrestadia_faturados": 0,
            "tarifa_diaria_demurrage_eur": 85.0,
            "tarifa_ligacao_eletrica_reefer_eur": 0.0,
            "total_liquidado_eur": 0.0,
            "motivo_retencao": "Saída Rápida Green Lane OEA dentro do período livre"
        },
        {
            "_id": "DEM-PT-2026-003",
            "fatura_sobrestadia_no": "MEDWAY-ENT-DEM-2026-009",
            "numero_contentor_iso": "CRXU9988771",
            "numero_bl_master": "CIMSMGS-YW2026-07",
            "mrn_dau": "26PT000510IM008807",
            "terminal_portuario": "Terminal Ferroviário Bobadela / Entroncamento",
            "dias_livres_contratados_free_time": 5,
            "dias_efetivos_permanencia": 12,
            "dias_sobrestadia_faturados": 7,
            "tarifa_diaria_demurrage_eur": 75.0,
            "tarifa_ligacao_eletrica_reefer_eur": 0.0,
            "total_liquidado_eur": 525.0,
            "motivo_retencao": "Apreensão Parcial e Contagem Física pela Brigada Fiscal GNR/AT"
        },
        {
            "_id": "DEM-PT-2026-004",
            "fatura_sobrestadia_no": "PSA-SIN-DEM-2026-0488",
            "numero_contentor_iso": "COSU8003301",
            "numero_bl_master": "COSU6288991103",
            "mrn_dau": "26PT000395IM008803",
            "terminal_portuario": "PSA Sines - Terminal XXI",
            "dias_livres_contratados_free_time": 10,
            "dias_efetivos_permanencia": 6,
            "dias_sobrestadia_faturados": 0,
            "tarifa_diaria_demurrage_eur": 85.0,
            "tarifa_ligacao_eletrica_reefer_eur": 0.0,
            "total_liquidado_eur": 0.0,
            "motivo_retencao": "Libertação dentro do Free Time para Entreposto Solar Alentejo"
        }
    ]

    # 71. pt_emissoes_maritimas_eu_ets_mrv (N23: EU ETS Maritime & FuelEU MRV)
    c["71_pt_emissoes_maritimas_eu_ets_mrv"] = [
        {
            "_id": "ETS-MAR-PT-2026-001",
            "registo_thetismrv_ue": "THETIS-MRV-2026-PTSIN-9795610",
            "imo_navio": "9795610",
            "nome_navio": "COSCO SHIPPING UNIVERSE",
            "numero_escala_jul": "PTSIN202600412",
            "rota_oceano": "Shanghai (CNSHA) -> Cabo da Boa Esperança -> Sines (PTSIN)",
            "distancia_milhas_nauticas": 13840,
            "combustivel_consumido_ton": 4120.0,
            "emissoes_totais_viagem_tco2": 12830.0,
            "percentagem_abrangida_eu_ets_extra_ue_pct": 50.0,
            "licencas_eua_entregues_ton": 6415.0,
            "custo_ets_imputado_contentores_pt_eur": 477917.5,
            " sobretaxa_ets_por_teu_eur": 42.0
        },
        {
            "_id": "ETS-MAR-PT-2026-002",
            "registo_thetismrv_ue": "THETIS-MRV-2026-PTSIN-9842105",
            "imo_navio": "9842105",
            "nome_navio": "BYD EXPLORER NO.1 (LNG Dual-Fuel PCTC)",
            "numero_escala_jul": "PTSIN202600445",
            "rota_oceano": "Shenzhen Yantian (CNSZX) -> Cabo da Boa Esperança -> Sines (PTSIN)",
            "distancia_milhas_nauticas": 13120,
            "combustivel_consumido_ton": 2480.0,
            "emissoes_totais_viagem_tco2": 6820.0,
            "percentagem_abrangida_eu_ets_extra_ue_pct": 50.0,
            "licencas_eua_entregues_ton": 3410.0,
            "custo_ets_imputado_contentores_pt_eur": 254045.0,
            "sobretaxa_ets_por_teu_eur": 28.5
        },
        {
            "_id": "ETS-MAR-PT-2026-003",
            "registo_thetismrv_ue": "THETIS-MRV-2026-PTLEI-9839131",
            "imo_navio": "9839131",
            "nome_navio": "COSCO SHIPPING SOLAR",
            "numero_escala_jul": "PTLEI202600198",
            "rota_oceano": "Ningbo (CNNGB) -> Sines (PTSIN) -> Leixões (PTLEI)",
            "distancia_milhas_nauticas": 13980,
            "combustivel_consumido_ton": 3950.0,
            "emissoes_totais_viagem_tco2": 12290.0,
            "percentagem_abrangida_eu_ets_extra_ue_pct": 50.0,
            "licencas_eua_entregues_ton": 6145.0,
            "custo_ets_imputado_contentores_pt_eur": 457802.5,
            "sobretaxa_ets_por_teu_eur": 44.0
        }
    ]

    # 72. pt_declaracoes_sumarias_entrada_ics2_ens (N24: EU ICS2 Pre-Arrival Safety ENS)
    c["72_pt_declaracoes_sumarias_entrada_ics2_ens"] = [
        {
            "_id": "ICS2-ENS-PT-2026-001",
            "mrn_ens_ics2": "26PTICS2000395ENS8801",
            "versao_ics2": "ICS2 Release 3 (Maritime & Rail)",
            "submetido_24h_antes_embarque_cn": true,
            "data_hora_submissao_utc": "2026-03-22T06:00:00Z",
            "referencia_bl_ou_awb": "COSU6288991101",
            "eori_transportador": "PT500991122",
            "eori_recetor_portugal": "PT517890123",
            "codigo_hs6_declarado": "850760",
            "primeira_estancia_entrada_ue": "PT000395 (Alfândega Marítima de Sines)",
            "resultado_analise_risco_seguranca": "ASSESSMENT_COMPLETE_PERMIT_TO_LOAD",
            "alerta_dnl_do_not_load": false
        },
        {
            "_id": "ICS2-ENS-PT-2026-002",
            "mrn_ens_ics2": "26PTICS2000395ENS8802",
            "versao_ics2": "ICS2 Release 3 (Maritime Ro-Ro)",
            "submetido_24h_antes_embarque_cn": true,
            "data_hora_submissao_utc": "2026-03-26T04:30:00Z",
            "referencia_bl_ou_awb": "COSU6288991102",
            "eori_transportador": "PT500991122",
            "eori_recetor_portugal": "PT500234567",
            "codigo_hs6_declarado": "870380",
            "primeira_estancia_entrada_ue": "PT000395 (Alfândega Marítima de Sines)",
            "resultado_analise_risco_seguranca": "ASSESSMENT_COMPLETE_PERMIT_TO_LOAD",
            "alerta_dnl_do_not_load": false
        },
        {
            "_id": "ICS2-ENS-PT-2026-003",
            "mrn_ens_ics2": "26PTICS2000520ENS8805",
            "versao_ics2": "ICS2 Release 2 (Air Cargo PLACI)",
            "submetido_24h_antes_embarque_cn": true,
            "data_hora_submissao_utc": "2026-04-15T18:00:00Z",
            "referencia_bl_ou_awb": "047-88991105",
            "eori_transportador": "PT500077568",
            "eori_recetor_portugal": "PT500246810",
            "codigo_hs6_declarado": "851713",
            "primeira_estancia_entrada_ue": "PT000520 (Alfândega Aeroporto de Lisboa)",
            "resultado_analise_risco_seguranca": "PLACI_SECURITY_SCREENED_OK",
            "alerta_dnl_do_not_load": false
        },
        {
            "_id": "ICS2-ENS-PT-2026-004",
            "mrn_ens_ics2": "26PTICS2000140ENS8804",
            "versao_ics2": "ICS2 Release 3 (Maritime Hazmat)",
            "submetido_24h_antes_embarque_cn": true,
            "data_hora_submissao_utc": "2026-04-10T12:00:00Z",
            "referencia_bl_ou_awb": "COSU6288991104",
            "eori_transportador": "PT501223344",
            "eori_recetor_portugal": "PT503412890",
            "codigo_hs6_declarado": "850760",
            "primeira_estancia_entrada_ue": "PT000140 (Alfândega de Leixões)",
            "resultado_analise_risco_seguranca": "RFI_HAZMAT_UN3480_REQUIRED_ON_ARRIVAL",
            "alerta_dnl_do_not_load": false
        }
    ]

    # 73. pt_janela_unica_logistica_jul_operacoes (N25: JUL Port Single Window Dossiers)
    c["73_pt_janela_unica_logistica_jul_operacoes"] = [
        {
            "_id": "JUL-OP-PT-2026-001",
            "id_dossier_jul": "JUL-APS-2026-00412-01",
            "numero_escala_jul": "PTSIN202600412",
            "numero_contentor_iso": "COSU8001101",
            "mrn_dau_associado": "26PT000395IM008801",
            "autorizacoes_entidades": {
                "autoridade_tributaria_at": "LIBERTADO_SAIDA_AUTORIZADA",
                "capitania_porto_am": "CONFORME_SEGURANCA_MARITIMA",
                "policia_maritima_ucf": "TRIPULACAO_E_CARGA_CONTROLADAS",
                "sanidade_fronteiras_dgav": "ISENTO_CONTROLO_VETERINARIO"
            },
            "titulo_saida_gate_out_pin": "PIN-PSA-SIN-994812",
            "modo_evacuacao_porto": "Comboio Bloco Ferroviário Medway para ZILS Sines",
            "timestamp_gate_out": "30/04/2026 15:20"
        },
        {
            "_id": "JUL-OP-PT-2026-002",
            "id_dossier_jul": "JUL-APS-2026-00445-02",
            "numero_escala_jul": "PTSIN202600445",
            "numero_contentor_iso": "BYDU9002201",
            "mrn_dau_associado": "26PT000395IM008802",
            "autorizacoes_entidades": {
                "autoridade_tributaria_at": "LIBERTADO_APOS_CAUCOES_C903",
                "capitania_porto_am": "CONFORME_OPERACAO_RORO",
                "policia_maritima_ucf": "CONFORME",
                "sanidade_fronteiras_dgav": "ISENTO"
            },
            "titulo_saida_gate_out_pin": "PIN-PSA-SIN-995104",
            "modo_evacuacao_porto": "Camiões Porta-Automóveis Rodoviários (e-Fatura)",
            "timestamp_gate_out": "03/05/2026 09:45"
        },
        {
            "_id": "JUL-OP-PT-2026-003",
            "id_dossier_jul": "JUL-APDL-2026-00198-04",
            "numero_escala_jul": "PTLEI202600198",
            "numero_contentor_iso": "CATU8004401",
            "mrn_dau_associado": "26PT000140IM008804",
            "autorizacoes_entidades": {
                "autoridade_tributaria_at": "LIBERTADO_POS_VISTORIA_CANAL_VERMELHO",
                "capitania_porto_am": "VISTORIA_AVARIA_GROSSA_CONCLUIDA",
                "policia_maritima_ucf": "CONFORME",
                "sanidade_fronteiras_dgav": "ISENTO"
            },
            "titulo_saida_gate_out_pin": "PIN-TCL-LEI-772190",
            "modo_evacuacao_porto": "Transporte Especial Pesado para Subestação REN Riba de Ave",
            "timestamp_gate_out": "18/05/2026 11:10"
        }
    ]

    # 74. pt_transito_aduaneiro_ncts_t1_t2 (N26: EU NCTS Phase 5 Customs Transit T1/T2)
    c["74_pt_transito_aduaneiro_ncts_t1_t2"] = [
        {
            "_id": "NCTS-PT-2026-001",
            "mrn_transito_ncts": "26PT000395TR000101",
            "regime_transito": "T1 - Trânsito Externo da União (Mercadoria Não-UE em Suspensão)",
            "estancia_partida": "PT000395 (Alfândega de Sines)",
            "estancia_destino": "PT000140 (Alfândega de Leixões / Entreposto Gaia)",
            "principal_responsavel_eori": "PT500991122",
            "numero_contentor_iso": "COSU8001101",
            "selo_aduaneiro_at": "AT-SELO-SIN-88412",
            "montante_garantia_retida_eur": 450000.0,
            "data_limite_apresentacao": "05/05/2026",
            "mensagem_apuramento_ie045": "APURADO_SEM_DISCREPANCIAS_IE045"
        },
        {
            "_id": "NCTS-PT-2026-002",
            "mrn_transito_ncts": "26PT000395TR000102",
            "regime_transito": "T1 - Trânsito Externo da União",
            "estancia_partida": "PT000395 (Alfândega de Sines)",
            "estancia_destino": "PT000510 (Alfândega do Jardim do Tabaco / Entreposto Azambuja)",
            "principal_responsavel_eori": "PT502334455",
            "numero_contentor_iso": "COSU8003301",
            "selo_aduaneiro_at": "AT-SELO-SIN-88499",
            "montante_garantia_retida_eur": 320000.0,
            "data_limite_apresentacao": "12/05/2026",
            "mensagem_apuramento_ie045": "APURADO_SEM_DISCREPANCIAS_IE045"
        },
        {
            "_id": "NCTS-PT-2026-003",
            "mrn_transito_ncts": "26ES002801TR009912",
            "regime_transito": "T1 - Trânsito Ferroviário Internacional Yiwu-Madrid-Entroncamento",
            "estancia_partida": "ES002801 (Aduana de Madrid Abroñigal)",
            "estancia_destino": "PT000510 (Delegação Aduaneira do Entroncamento)",
            "principal_responsavel_eori": "PT501223344",
            "numero_contentor_iso": "CRXU9988771",
            "selo_aduaneiro_at": "CIMSMGS-SEAL-YW07",
            "montante_garantia_retida_eur": 295000.0,
            "data_limite_apresentacao": "14/05/2026",
            "mensagem_apuramento_ie045": "APURADO_COM_AUTO_INSPECAO_AT"
        }
    ]

    # 75. pt_deposito_temporario_armazens_adt (N27: Temporary Storage Warehouses ADT - 90 Days Limit)
    c["75_pt_deposito_temporario_armazens_adt"] = [
        {
            "_id": "ADT-PT-2026-001",
            "autorizacao_adt_at": "ADT-PT000395-PSA-01",
            "declaracao_adt_id": "DSDT-2026-SIN-008801",
            "operador_armazem": "PSA Sines - Terminal de Contentores, S.A.",
            "numero_contentor_iso": "COSU8001101",
            "numero_bl": "COSU6288991101",
            "data_entrada_adt": "29/04/2026",
            "prazo_maximo_legal_90_dias_cau": "28/07/2026",
            "data_apuramento_por_dau": "30/04/2026",
            "mrn_dau_apuramento": "26PT000395IM008801",
            "estado_adt": "APURADO_DENTRO_DO_PRAZO"
        },
        {
            "_id": "ADT-PT-2026-002",
            "autorizacao_adt_at": "ADT-PT000520-GROUND-02",
            "declaracao_adt_id": "DSDT-2026-LIS-008805",
            "operador_armazem": "Portway / Menzies Aviation Terminal de Carga Lisboa",
            "numero_contentor_iso": "PMC44111CA",
            "numero_bl": "047-88991105",
            "data_entrada_adt": "16/04/2026",
            "prazo_maximo_legal_90_dias_cau": "15/07/2026",
            "data_apuramento_por_dau": "17/04/2026",
            "mrn_dau_apuramento": "26PT000520IM008805",
            "estado_adt": "APURADO_DENTRO_DO_PRAZO"
        },
        {
            "_id": "ADT-PT-2026-003",
            "autorizacao_adt_at": "ADT-PT000140-TCL-03",
            "declaracao_adt_id": "DSDT-2026-LEI-008804",
            "operador_armazem": "Yilport / TCL Leixões",
            "numero_contentor_iso": "CATU8004401",
            "numero_bl": "COSU6288991104",
            "data_entrada_adt": "08/05/2026",
            "prazo_maximo_legal_90_dias_cau": "06/08/2026",
            "data_apuramento_por_dau": "18/05/2026",
            "mrn_dau_apuramento": "26PT000140IM008804",
            "estado_adt": "APURADO_APOS_PERITAGEM"
        }
    ]

    # 76. pt_controlos_fronteiricos_traces_nt_ched (N28: EU TRACES-NT CHED Border Health Certificates)
    c["76_pt_controlos_fronteiricos_traces_nt_ched"] = [
        {
            "_id": "TRACES-CHED-2026-001",
            "numero_ched_traces_nt": "CHEDPP.PT.2026.0004412",
            "tipo_documento_ched": "CHED-PP (Fitossanitário - Embalagens de Madeira ISPM-15)",
            "posto_controlo_fronteirico_pcf": "PCF Porto de Sines (PTSIN1)",
            "autoridade_competente": "DGAV / ICNF - Inspeção Fitossanitária",
            "mrn_dau_associado": "26PT000395IM008801",
            "numero_contentor_iso": "COSU8001101",
            "certificado_origem_china": "CERT-HZ-2026-001 (IPPC CN-32004-HT)",
            "controlo_documental": "SATISFATORIO",
            "controlo_identidade": "SATISFATORIO",
            "controlo_fisico_amostragem": "DISPENSADO_TAXA_REDUZIDA",
            "decisao_final_traces": "VALIDADO_ADMISSIVEL_NO_TERRITORIO_UE"
        },
        {
            "_id": "TRACES-CHED-2026-002",
            "numero_ched_traces_nt": "CHEDPP.PT.2026.0004489",
            "tipo_documento_ched": "CHED-PP (Fitossanitário - Paletes de Painéis Solares)",
            "posto_controlo_fronteirico_pcf": "PCF Porto de Sines (PTSIN1)",
            "autoridade_competente": "DGAV / ICNF",
            "mrn_dau_associado": "26PT000395IM008803",
            "numero_contentor_iso": "COSU8003301",
            "certificado_origem_china": "CERT-PK-2026-003 (IPPC CN-61001-HT)",
            "controlo_documental": "SATISFATORIO",
            "controlo_identidade": "SATISFATORIO",
            "controlo_fisico_amostragem": "SATISFATORIO_SEM_NEMATODO",
            "decisao_final_traces": "VALIDADO_ADMISSIVEL_NO_TERRITORIO_UE"
        },
        {
            "_id": "TRACES-CHED-2026-003",
            "numero_ched_traces_nt": "TRACES.EX.PT.2026.0009905",
            "tipo_documento_ched": "Certificado Sanitário Oficial de Exportação DGAV/TRACES para GACC China",
            "posto_controlo_fronteirico_pcf": "Direção de Serviços de Alimentação e Veterinária do Alentejo / Sines",
            "autoridade_competente": "DGAV Portugal",
            "mrn_dau_associado": "26PT000395EX009905",
            "numero_contentor_iso": "COSU4455665",
            "certificado_origem_china": "CIFER CPRT18000101000505",
            "controlo_documental": "SATISFATORIO",
            "controlo_identidade": "SELO_VETERINARIO_VERIFICADO",
            "controlo_fisico_amostragem": "TESTE_LABORATORIAL_NEGATIVO",
            "decisao_final_traces": "APROVADO_PARA_EXPORTACAO_CHINA"
        }
    ]

    # 77. pt_impostos_especiais_consumo_emcs_iec (N29: EMCS e-AD Excise Duty Suspension for Wine)
    c["77_pt_impostos_especiais_consumo_emcs_iec"] = [
        {
            "_id": "EMCS-PT-2026-001",
            "codigo_arc_emcs": "26PT000140EMCS0009901",
            "tipo_documento_iec": "e-DA (Documento Administrativo Eletrónico em Suspensão de IABA)",
            "estatuto_fiscal_expedidor": "Depositário Autorizado IEC n.º PT001409981",
            "entreposto_fiscal_origem": "Caves Graham's & Symington - Vila Nova de Gaia",
            "eori_exportador": "PT500265432",
            "estancia_aduaneira_saida_ue": "PT000140 (Alfândega de Leixões)",
            "mrn_exportacao_dau": "26PT000140EX009901",
            "volume_hectolitros": 900.0,
            "imposto_iaba_suspenso_eur": 0.0,
            "taxa_promocao_ivdp_paga_eur": 5400.0,
            "notificacao_saida_ie818": "SAIDA_CONFIRMADA_APURAMENTO_IEC_CONCLUIDO"
        },
        {
            "_id": "EMCS-PT-2026-002",
            "codigo_arc_emcs": "26PT000140EMCS0009906",
            "tipo_documento_iec": "e-DA (Documento Administrativo Eletrónico em Suspensão de IABA)",
            "estatuto_fiscal_expedidor": "Depositário Autorizado IEC n.º PT001402210",
            "entreposto_fiscal_origem": "Sogrape Vinhos - Avintes (Vila Nova de Gaia)",
            "eori_exportador": "PT500214890",
            "estancia_aduaneira_saida_ue": "PT000140 (Alfândega de Leixões)",
            "mrn_exportacao_dau": "26PT000140EX009906",
            "volume_hectolitros": 712.5,
            "imposto_iaba_suspenso_eur": 0.0,
            "taxa_promocao_ivdp_paga_eur": 4275.0,
            "notificacao_saida_ie818": "SAIDA_CONFIRMADA_APURAMENTO_IEC_CONCLUIDO"
        }
    ]

    # 78. pt_conformidade_quimica_ambiental_reach_rohs_scip (N30: REACH, RoHS, WEEE & EU Battery Passport)
    c["78_pt_conformidade_quimica_ambiental_reach_rohs_scip"] = [
        {
            "_id": "REACH-BATT-2026-001",
            "passaporte_bateria_ue_id": "EU-BPASS-2026-CALB-L314-SINES01",
            "notificacao_scip_echa": "SCIP-UUID-8812-4490-991A-CALB314",
            "registo_apa_produtor_reee_pilhas": "PT001928-APA-BATERIAS-INDUSTRIAIS",
            "eori_importador": "PT517890123",
            "fabricante_china_uscc": "91320413MA1M9Y2C4B",
            "mrn_dau": "26PT000395IM008801",
            "regulamento_aplicavel": "Regulamento (UE) 2023/1542 (Baterias) & Regulamento REACH 1907/2006",
            "pegada_carbono_ciclo_vida_kgco2_kwh": 45.2,
            "conteudo_reciclado_declarado_pct": {"cobalto": 0.0, "litio": 6.5, "niquel": 0.0, "chumbo": 0.0},
            "conformidade_rohs_metais_pesados": true,
            "entidade_gestora_residuos_pt": "Ecopilhas / Amb3E"
        },
        {
            "_id": "REACH-BATT-2026-002",
            "passaporte_bateria_ue_id": "EU-BPASS-2026-BYD-BLADE-82KWH",
            "notificacao_scip_echa": "SCIP-UUID-7721-3310-882B-BYDSEAL",
            "registo_apa_produtor_reee_pilhas": "PT000412-APA-VEICULOS-ELETRICOS",
            "eori_importador": "PT500234567",
            "fabricante_china_uscc": "91440300192317458F",
            "mrn_dau": "26PT000395IM008802",
            "regulamento_aplicavel": "Regulamento (UE) 2023/1542 & Homologação Europeia WVTA",
            "pegada_carbono_ciclo_vida_kgco2_kwh": 52.8,
            "conteudo_reciclado_declarado_pct": {"cobalto": 0.0, "litio": 5.2, "niquel": 0.0, "chumbo": 0.0},
            "conformidade_rohs_metais_pesados": true,
            "entidade_gestora_residuos_pt": "Valorcar Portugal"
        },
        {
            "_id": "REACH-ELEC-2026-003",
            "passaporte_bateria_ue_id": "ROHS-CE-2026-XIAOMI-15PRO",
            "notificacao_scip_echa": "SCIP-UUID-5519-2201-119C-XM15PRO",
            "registo_apa_produtor_reee_pilhas": "PT000288-APA-EEE-WORTEN",
            "eori_importador": "PT500246810",
            "fabricante_china_uscc": "91110108551385082Q",
            "mrn_dau": "26PT000520IM008805",
            "regulamento_aplicavel": "Diretiva RoHS 2011/65/UE & Diretiva REEE 2012/19/UE",
            "pegada_carbono_ciclo_vida_kgco2_kwh": 48.2,
            "conteudo_reciclado_declarado_pct": {"aluminio_reciclado": 80.0, "ouro_reciclado_placa": 25.0},
            "conformidade_rohs_metais_pesados": true,
            "entidade_gestora_residuos_pt": "ERP Portugal / Electrão"
        }
    ]

    # 79. pt_medidas_defesa_comercial_antidumping_ue (N31: EU Anti-Dumping & Countervailing Duties)
    c["79_pt_medidas_defesa_comercial_antidumping_ue"] = [
        {
            "_id": "AD-CVD-UE-2026-001",
            "regulamento_comissao_europeia": "Regulamento de Execução (UE) 2024/2754 da Comissão",
            "tipo_medida_defesa": "Direito de Compensação Definitivo (Anti-Subsídios sobre BEV da China)",
            "codigo_taric_10": "8703801000",
            "codigo_adicional_taric_empresa": "C903 (Grupo BYD - Produtor Exportador Cooperante)",
            "fabricante_china_uscc": "91440300192317458F",
            "eori_importador_pt": "PT500234567",
            "mrn_dau_liquidado": "26PT000395IM008802",
            "valor_aduaneiro_cif_eur": 9732000.0,
            "taxa_direito_convencional_pct": 10.0,
            "taxa_adicional_antisubsidio_pct": 17.0,
            "montante_antisubsidio_cobrado_at_eur": 1654440.0,
            "taxa_residual_nao_cooperantes_pct": 35.3
        },
        {
            "_id": "AD-CVD-UE-2026-002",
            "regulamento_comissao_europeia": "Regulamento de Execução (UE) 2024/2754 da Comissão",
            "tipo_medida_defesa": "Direito de Compensação Definitivo (2.º Lote BYD Atto 3)",
            "codigo_taric_10": "8703801000",
            "codigo_adicional_taric_empresa": "C903 (Grupo BYD)",
            "fabricante_china_uscc": "91440300192317458F",
            "eori_importador_pt": "PT500234567",
            "mrn_dau_liquidado": "26PT000395IM008813",
            "valor_aduaneiro_cif_eur": 8950000.0,
            "taxa_direito_convencional_pct": 10.0,
            "taxa_adicional_antisubsidio_pct": 17.0,
            "montante_antisubsidio_cobrado_at_eur": 1521500.0,
            "taxa_residual_nao_cooperantes_pct": 35.3
        },
        {
            "_id": "AD-CVD-UE-2026-003",
            "regulamento_comissao_europeia": "Regulamento de Execução (UE) 2021/1784 (Alumínio Laminado Plano)",
            "tipo_medida_defesa": "Direito Anti-Dumping Definitivo sobre Produtos Planos de Alumínio da China",
            "codigo_taric_10": "7606129200",
            "codigo_adicional_taric_empresa": "C684",
            "fabricante_china_uscc": "91330200778899112T",
            "eori_importador_pt": "PT500191827",
            "mrn_dau_liquidado": "26PT000395IM008806",
            "valor_aduaneiro_cif_eur": 1242000.0,
            "taxa_direito_convencional_pct": 7.5,
            "taxa_adicional_antisubsidio_pct": 14.3,
            "montante_antisubsidio_cobrado_at_eur": 177606.0,
            "taxa_residual_nao_cooperantes_pct": 24.6
        }
    ]

    # 80. pt_contingentes_pautais_suspensoes_autonomas (N32: EU Tariff Quotas & Autonomous Suspensions)
    c["80_pt_contingentes_pautais_suspensoes_autonomas"] = [
        {
            "_id": "QUOTA-UE-2026-001",
            "numero_ordem_contingente_ue": "09.2681 (Suspensão Pautal Autónoma Industrial para Fabrico de Baterias EV)",
            "regulamento_conselho_ue": "Regulamento (UE) 2025/2605 do Conselho",
            "eori_beneficiario_pt": "PT517890123",
            "mrn_dau": "26PT000395IM008801",
            "codigo_taric_10": "8507600090",
            "regime_destino_especial_end_use": "Autorização de Destino Especial (End-Use Art. 254.º CAU) - Gigafábrica Sines",
            "taxa_normal_pauta_pct": 2.7,
            "taxa_reduzida_contingente_pct": 0.0,
            "quantidade_pedida_unidades": 10000,
            "poupanca_direitos_aduaneiros_eur": 169654.5,
            "estado_atribuicao_dg_taxud": "CONCEDIDO_INTEGRALMENTE_100_PCT"
        },
        {
            "_id": "QUOTA-UE-2026-002",
            "numero_ordem_contingente_ue": "09.0142 (Contingente OMC Aço Laminado de Construção)",
            "regulamento_conselho_ue": "Regulamento de Salvaguarda do Aço (UE) 2024/1782",
            "eori_beneficiario_pt": "PT500191827",
            "mrn_dau": "26PT000395IM008806",
            "codigo_taric_10": "7225409000",
            "regime_destino_especial_end_use": "Contingente Trimestral First-Come First-Served",
            "taxa_normal_pauta_pct": 25.0,
            "taxa_reduzida_contingente_pct": 0.0,
            "quantidade_pedida_unidades": 2000,
            "poupanca_direitos_aduaneiros_eur": 327500.0,
            "estado_atribuicao_dg_taxud": "CONCEDIDO_DENTRO_QUOTA_LIVRE_SALVAGUARDA"
        }
    ]

    # 81. pt_caucoes_garantias_aduaneiras_at (N33: AT Comprehensive Customs Guarantees & VAT Deferral)
    c["81_pt_caucoes_garantias_aduaneiras_at"] = [
        {
            "_id": "CAUCAO-AT-2026-001",
            "numero_garantia_aduaneira_grn": "26PT000395GRN0001122",
            "titular_eori": "PT517890123",
            "tipo_garantia_cau": "Garantia Global com Redução para 30% do Montante de Referência (Estatuto AEOC Art. 95.º CAU)",
            "entidade_fiadora": "Millennium bcp / Fidelidade Seguros (Seguro-Caução)",
            "montante_referencia_anual_eur": 15000000.0,
            "caucao_efetiva_prestada_eur": 4500000.0,
            "opcao_autoliquidacao_iva_art27_civa": true,
            "iva_diferido_sem_desembolso_imediato_eur": 1484142.84,
            "estado_conta_corrente_stada": "ATIVA_SALDO_DISPONIVEL"
        },
        {
            "_id": "CAUCAO-AT-2026-002",
            "numero_garantia_aduaneira_grn": "26PT000140GRN0003344",
            "titular_eori": "PT500234567",
            "tipo_garantia_cau": "Garantia Global para Desalfandegamento e Pagamento Diferido (30 Dias Art. 110.º CAU)",
            "entidade_fiadora": "Banco BPI, S.A.",
            "montante_referencia_anual_eur": 25000000.0,
            "caucao_efetiva_prestada_eur": 12500000.0,
            "opcao_autoliquidacao_iva_art27_civa": true,
            "iva_diferido_sem_desembolso_imediato_eur": 2842717.2,
            "estado_conta_corrente_stada": "ATIVA_SALDO_DISPONIVEL"
        },
        {
            "_id": "CAUCAO-AT-2026-003",
            "numero_garantia_aduaneira_grn": "26PT000140GRN0005566",
            "titular_eori": "PT500991122",
            "tipo_garantia_cau": "Garantia Global de Representante Aduaneiro para Trânsito NCTS e Depósito Temporário",
            "entidade_fiadora": "Caixa Geral de Depósitos, S.A.",
            "montante_referencia_anual_eur": 10000000.0,
            "caucao_efetiva_prestada_eur": 3000000.0,
            "opcao_autoliquidacao_iva_art27_civa": false,
            "iva_diferido_sem_desembolso_imediato_eur": 0.0,
            "estado_conta_corrente_stada": "ATIVA_SALDO_DISPONIVEL"
        }
    ]

    # 82. pt_informacoes_pautais_vinculativas_ipv_bti (N34: EU Binding Tariff Information BTI / IPV)
    c["82_pt_informacoes_pautais_vinculativas_ipv_bti"] = [
        {
            "_id": "IPV-BTI-PT-2026-001",
            "referencia_decisao_ebti": "PTBTI2025-000891-SINES",
            "tipo_decisao_vinculativa": "IPV / BTI (Informação Pautal Vinculativa - Art. 33.º do CAU)",
            "titular_eori": "PT517890123",
            "autoridade_emissora": "AT - Direção de Serviços de Regulação Aduaneira (Lisboa)",
            "codigo_taric_10_fixado": "8507600090",
            "descricao_tecnica_mercadoria": "Módulo de acumuladores de iões de lítio-ferro-fosfato (LFP) 314Ah com placa de monitorização térmica passiva, sem inversor integrado",
            "regra_geral_interpretativa_aplicada": "RGI 1 e RGI 6 da Nomenclatura Combinada",
            "data_inicio_validade": "15/06/2025",
            "data_fim_validade_3_anos": "14/06/2028",
            "invocada_no_dau_mrn": "26PT000395IM008801"
        },
        {
            "_id": "IPV-BTI-PT-2026-002",
            "referencia_decisao_ebti": "PTBTI2025-001104-REN",
            "tipo_decisao_vinculativa": "IPV / BTI (Informação Pautal Vinculativa)",
            "titular_eori": "PT503412890",
            "autoridade_emissora": "AT - Direção de Serviços de Regulação Aduaneira",
            "codigo_taric_10_fixado": "8507600090",
            "descricao_tecnica_mercadoria": "Contentor marítimo de 20 pés equipado com racks de baterias LFP CATL EnerC Plus e sistema de arrefecimento líquido para armazenamento em rede elétrica",
            "regra_geral_interpretativa_aplicada": "RGI 1, Nota 3 da Secção XVI e RGI 6",
            "data_inicio_validade": "10/09/2025",
            "data_fim_validade_3_anos": "09/09/2028",
            "invocada_no_dau_mrn": "26PT000140IM008804"
        }
    ]

    # 83. pt_controlo_pos_desembaraco_auditorias_at (N35: Post-Clearance Audits & Transfer Pricing AT)
    c["83_pt_controlo_pos_desembaraco_auditorias_at"] = [
        {
            "_id": "PCA-AT-2026-001",
            "ordem_servico_inspecao_at": "OI202600412-DSAFA",
            "unidade_inspetiva": "AT - Direção de Serviços de Antifraude Aduaneira (DSAFA)",
            "fundamento_legal_cau": "Controlo Pós-Desembaraço (Art. 48.º do Código Aduaneiro da União)",
            "operador_auditado_eori": "PT517890123",
            "empresa_mae_china_uscc": "91320413MA1M9Y2C4B",
            "mrn_dau_auditado": "26PT000395IM008801",
            "objeto_auditoria": "Verificação de Preços de Transferência (Art. 70.º n.º 3 al. d) CAU) e inclusão de Royalties de Patente LFP no Valor Aduaneiro",
            "conclusao_relatorio": "REGULAR - Dossier de Preços de Transferência OCDE comprova que a relação especial não influenciou o preço CIF faturado",
            "liquidacao_adicional_direitos_eur": 0.0
        },
        {
            "_id": "PCA-AT-2026-002",
            "ordem_servico_inspecao_at": "OI202600589-DSAFA",
            "unidade_inspetiva": "AT - Divisão Operacional do Norte (Porto)",
            "fundamento_legal_cau": "Controlo Pós-Desembaraço (Art. 48.º e Art. 71.º CAU)",
            "operador_auditado_eori": "PT504998877",
            "empresa_mae_china_uscc": "91330782098765432W",
            "mrn_dau_auditado": "26PT000510IM008807",
            "objeto_auditoria": "Reavaliação do Valor Aduaneiro por subfaturação em 200 caixas de vestuário e omissão de comissões de compra",
            "conclusao_relatorio": "LIQUIDACAO_ADICIONAL_EMITIDA",
            "liquidacao_adicional_direitos_eur": 14820.5
        }
    ]

    # 84. pt_declaracoes_simplificadas_ecommerce_stada_h7 (N36: STADA-H7 Super-Reduced Dataset <150 EUR)
    c["84_pt_declaracoes_simplificadas_ecommerce_stada_h7"] = [
        {
            "_id": "STADA-H7-2026-001",
            "mrn_h7_stada": "26PT000520H70012901",
            "conjunto_dados_cau": "Coluna H7 do Anexo B do Regulamento Delegado (UE) 2015/2446 (Super-Reduzido <= 150 EUR)",
            "declarante_expresso_eori": "PT500077568",
            "codigo_rastreio_postal_s10": "LP00667788901CN",
            "master_awb_aereo": "871-33221100",
            "numero_ioss_validado_vies": "IM5280001234",
            "codigo_hs6_declarado": "851830",
            "valor_intrinseco_remessa_eur": 68.5,
            "isencao_direitos_art23_reg1186": true,
            "iva_pago_no_checkout_ioss": true,
            "canal_selecao_stada_h7": "CANAL_VERDE_DESEMBARACO_AUTOMATICO_EM_VOO"
        },
        {
            "_id": "STADA-H7-2026-002",
            "mrn_h7_stada": "26PT000520H70012902",
            "conjunto_dados_cau": "Coluna H7 do Anexo B do Regulamento Delegado (UE) 2015/2446",
            "declarante_expresso_eori": "PT500077568",
            "codigo_rastreio_postal_s10": "LP00667788902CN",
            "master_awb_aereo": "871-33221100",
            "numero_ioss_validado_vies": "IM5280001234",
            "codigo_hs6_declarado": "910212",
            "valor_intrinseco_remessa_eur": 112.0,
            "isencao_direitos_art23_reg1186": true,
            "iva_pago_no_checkout_ioss": true,
            "canal_selecao_stada_h7": "CANAL_VERDE_DESEMBARACO_AUTOMATICO_EM_VOO"
        },
        {
            "_id": "STADA-H7-2026-003",
            "mrn_h7_stada": "26PT000520H70012905",
            "conjunto_dados_cau": "Coluna H7 do Anexo B do Regulamento Delegado (UE) 2015/2446",
            "declarante_expresso_eori": "PT500077568",
            "codigo_rastreio_postal_s10": "LP00667788905CN",
            "master_awb_aereo": "871-33221100",
            "numero_ioss_validado_vies": "IM5280009988",
            "codigo_hs6_declarado": "620462",
            "valor_intrinseco_remessa_eur": 84.9,
            "isencao_direitos_art23_reg1186": true,
            "iva_pago_no_checkout_ioss": true,
            "canal_selecao_stada_h7": "CANAL_VERDE_DESEMBARACO_AUTOMATICO_EM_VOO"
        }
    ]

    # 85. pt_logistica_inversa_devolucoes_reembolsos_aduaneiros (N37: Reverse Logistics & Duty Refunds)
    c["85_pt_logistica_inversa_devolucoes_reembolsos_aduaneiros"] = [
        {
            "_id": "REV-LOG-PT-2026-001",
            "pedido_reembolso_at_no": "REM-AT-2026-LIS-00412",
            "fundamento_cau": "Art. 116.º e Art. 118.º do CAU (Mercadorias Defeituosas ou Não Conformes com o Contrato)",
            "requerente_eori": "PT500697256",
            "fornecedor_china_uscc": "91440300618837699Q",
            "mrn_importacao_original": "26PT000395IM008808",
            "mrn_reexportacao_devolucao": "26PT000395EX009988",
            "descricao_ocorrencia": "Devolução à fábrica da Huawei em Dongguan de 4 inversores solares SUN2000 para recalibração de firmware sob garantia",
            "direitos_aduaneiros_reembolsados_eur": 1120.0,
            "processo_retorno_china_id": "RET-B2B-2026-003",
            "decisao_at": "DEFERIDO_REEMBOLSO_CREDITADO"
        },
        {
            "_id": "REV-LOG-PT-2026-002",
            "pedido_reembolso_at_no": "REM-AT-2026-CTT-00891",
            "fundamento_cau": "Art. 116.º do CAU & Anulação de Declaração H7 por Devolução de Consumidor no Prazo de 14 Dias",
            "requerente_eori": "PT500077568",
            "fornecedor_china_uscc": "91440300755673010C",
            "mrn_importacao_original": "26PT000520H70012901",
            "mrn_reexportacao_devolucao": "26PT000520EX009991",
            "descricao_ocorrencia": "Consolidação de devoluções de e-commerce no Hub CTT Cabo Ruivo e reexpedição aérea para o entreposto de Shenzhen Qianhai",
            "direitos_aduaneiros_reembolsados_eur": 0.0,
            "processo_retorno_china_id": "RET-CBEC-2026-001",
            "decisao_at": "CREDITO_IVA_IOSS_REGULARIZADO"
        }
    ]

    return c


def get_expanded_unstructured_corpora():
    u = {}

    # 86. pt_unstruct_fichas_dados_seguranca_msds_quimicos (N38: 16-Section CLP/GHS MSDS Safety Data Sheets)
    u["86_pt_unstruct_fichas_dados_seguranca_msds_quimicos"] = [
        {
            "doc_id": "UNSTRUCT-MSDS-CALB-LFP314",
            "corpus_table": "pt_unstruct_fichas_dados_seguranca_msds_quimicos",
            "raw_text": "FICHA DE DADOS DE SEGURANÇA (FDS / MSDS - REGULAMENTO REACH CE 1907/2006 & CLP 1272/2008 - 16 SECÇÕES). Produto: Módulo de Bateria de Iões de Lítio-Ferro-Fosfato CALB L314Ah (TARIC 8507600090). Fabricante: CALB Group Co., Ltd. (USCC 91320413MA1M9Y2C4B). Importador em Portugal: CALB Portugal, S.A. (EORI PT517890123 / NIF 517890123, Porto de Sines PTSIN). Declaração Aduaneira: MRN 26PT000395IM008801, BL COSU6288991101, Contentor COSU8001101, Fatura INV-CN-2026-8801 (6283500.00 EUR). SECÇÃO 2 & 3 (Composição Química): Fosfato de Ferro e Lítio (LiFePO4 CAS 15365-14-7: 42%), Grafite Artificial (CAS 7782-42-5: 24%), Hexafluorofosfato de Lítio (LiPF6 CAS 21324-40-3 em solvente carbonato de etileno). SECÇÃO 9 & 10 (Estabilidade Térmica): Temperatura normal de transporte +21.5C; limiar de fuga térmica (Thermal Runaway) > +195.0C. SECÇÃO 14 (Transporte Marítimo IMDG): Número ONU UN3480, Classe 9, Grupo de Embalagem II, Código de Túnel E, Teste Manual ONU Subsecção 38.3 Aprovado (Certificado CCC 2025010907881201). Resultado da Revisão Química APA/AT: CONFORME E VALIDADO."
        },
        {
            "doc_id": "UNSTRUCT-MSDS-CATL-ENERC",
            "corpus_table": "pt_unstruct_fichas_dados_seguranca_msds_quimicos",
            "raw_text": "FICHA DE DADOS DE SEGURANÇA QUÍMICA E RESPOSTA A EMERGÊNCIAS N.º MSDS-CATL-2026-04. Importador: REN - Redes Energéticas Nacionais (EORI PT503412890). Fabricante: CATL (USCC 91350900587527783P). Referência DAU MRN 26PT000140IM008804, BL COSU6288991104, Contentor CATU8004401 no Porto de Leixões (PTLEI), Fatura INV-CN-2026-8804 (3520000.00 EUR). Mercadoria: Racks estacionários LFP arrefecidos por líquido glicol-água (TARIC 8507600090). Agente extintor recomendado: Água nebulizada em grande caudal ou FM-200. Conformidade integral com o Regulamento REACH e Passaporte Digital Europeu de Baterias."
        }
    ]

    # 87. pt_unstruct_cartas_protesto_maritimo_sea_protest (N39: Captain's Sea Protests & Lloyd's Surveyor Reports)
    u["87_pt_unstruct_cartas_protesto_maritimo_sea_protest"] = [
        {
            "doc_id": "UNSTRUCT-SEAPROTEST-LEIXOES-2026",
            "corpus_table": "pt_unstruct_cartas_protesto_maritimo_sea_protest",
            "raw_text": "CARTA DE PROTESTO DE MAR (NOTE OF SEA PROTEST) & RELATÓRIO DE PERITAGEM LLOYD'S AGENCY PORTO/LEIXÕES. Navio: COSCO SHIPPING SOLAR (IMO: 9839131), Viagem VOY-COSCO-2026-04B, atracado no Porto de Leixões (PTLEI). Comandante: Capt. Zhang Wei. Importador: REN - Redes Energéticas Nacionais (EORI PT503412890 / NIF 503412890). Exportador: CATL (USCC 91350900587527783P). Declaração DAU MRN 26PT000140IM008804, BL COSU6288991104, Contentor CATU8004401, Fatura INV-CN-2026-8804. O Comandante lavra formal Protesto de Mar perante a Capitania do Porto de Leixões declarando que na travessia do Golfo da Biscaia a 14/05/2026 o navio enfrentou ventos de Força 9 Beaufort e vagas de 7.5 metros, causando impacto mecânico na porta exterior do contentor CATU8004401. A peritagem conjunta confirmou temperatura interna estável de +20.8C e integridade total dos módulos (TARIC 8507600090), fixando apenas 23650.00 EUR de reparação estrutural do contentor coberta pelo seguro marítimo."
        },
        {
            "doc_id": "UNSTRUCT-SEAPROTEST-SHANGHAI-WINE",
            "corpus_table": "pt_unstruct_cartas_protesto_maritimo_sea_protest",
            "raw_text": "RELATÓRIO DE VISTORIA DE CADEIA DE FRIO E PROTESTO MARÍTIMO N.º SURVEY-SH-2026-9901. Exportador Português: Symington Family Estates (EORI PT500265432, CIFER CPRT18000102000101). Importador Chinês: COFCO Wines & Spirits (USCC 91110000101123456N). Navio IMO: 9839131, BL COSU6288992201, Contentor Reefer COSU4455661, Fatura INV-PT-2026-9901 (1522500.00 EUR, TARIC 2204218010), Porto CNSHA. Durante a rota pelo Cabo da Boa Esperança registou-se uma excursão térmica temporária de +28.4C durante 35 minutos por falha de disjuntor do gerador reefer. O teste laboratorial enológico em Xangai confirmou ausência de oxidação no Vinho do Porto e Douro DOC."
        }
    ]

    # 88. pt_unstruct_oficios_notificacoes_audiencia_previa_at (N40: AT Customs Prior Hearing & Tariff Dispute Notices)
    u["88_pt_unstruct_oficios_notificacoes_audiencia_previa_at"] = [
        {
            "doc_id": "UNSTRUCT-AT-AUDIENCIA-2026-001",
            "corpus_table": "pt_unstruct_oficios_notificacoes_audiencia_previa_at",
            "raw_text": "OFÍCIO DE NOTIFICAÇÃO PARA AUDIÊNCIA PRÉVIA (ART. 22.º N.º 6 DO CÓDIGO ADUANEIRO DA UNIÃO E ART. 60.º DA LGT) N.º AT-SIN-2026-008802. Emitente: Alfândega Marítima de Sines (PTSIN). Notificada: Salvador Caetano Auto, S.A. (EORI PT500234567 / NIF 500234567). Exportador na Origem: BYD Auto Industry Co., Ltd. (USCC 91440300192317458F). Referência DAU MRN 26PT000395IM008802, BL COSU6288991102, Contentor BYDU9002201, Fatura INV-CN-2026-8802 (9732000.00 EUR, TARIC 8703801000). Notifica-se o importador para, no prazo de 30 dias, apresentar o original autenticado da Declaração de Fabricante Direto exigida pelo Regulamento (UE) 2024/2754 para aplicação do código adicional TARIC C903 (taxa anti-subsídios de 17.0% em vez da taxa residual de 35.3%). Resposta do Operador: Documento apresentado e validado em 02/05/2026; arquivado sem liquidação adicional."
        },
        {
            "doc_id": "UNSTRUCT-AT-AUDIENCIA-2026-002",
            "corpus_table": "pt_unstruct_oficios_notificacoes_audiencia_previa_at",
            "raw_text": "NOTIFICAÇÃO DE LIQUIDAÇÃO ADICIONAL PÓS-DESEMBARAÇO E COIMA ADUANEIRA N.º AT-ENT-2026-008807. Alfândega do Jardim do Tabaco / Delegação do Entroncamento (PTENT). Importador: Varziela Chinarte, Lda. (EORI PT504998877 / NIF 504998877). Exportador: Yiwu CCCG (USCC 91330782098765432W). DAU MRN 26PT000510IM008807, Carta de Porte CIMSMGS-YW2026-07, Contentor CRXU9988771, TARIC 6204623100. Em sede de revisão física e documental foi detetada retenção parcial e aplicação de coima de 18500.00 EUR por divergência quantitativa e contrafação em lote residual."
        }
    ]

    # 89. pt_unstruct_traducoes_rotulagem_mandarim_gacc (N41: Mandarin Back-Label Compliance GB 7718 / GB 2757)
    u["89_pt_unstruct_traducoes_rotulagem_mandarim_gacc"] = [
        {
            "doc_id": "UNSTRUCT-GACC-LABEL-WINE-9901",
            "corpus_table": "pt_unstruct_traducoes_rotulagem_mandarim_gacc",
            "raw_text": "DOSSIER TÉCNICO DE HOMOLOGAÇÃO DE CONTRA-RÓTULO EM MANDARIM (NORMA NACIONAL CHINESA GB 7718-2011 & GB 2757-2012). Exportador Português: Symington Family Estates (EORI PT500265432 / NIF 500265432, Registo CIFER CPRT18000102000101). Importador na China: COFCO Wines & Spirits (USCC 91110000101123456N). Declaração MRN 26PT000140EX009901, Fatura INV-PT-2026-9901 (1522500.00 EUR), BL COSU6288992201, Contentor COSU4455661, TARIC 2204218010, Porto CNSHA. Texto obrigatório aprovado pela CIQ Xangai: Nome do Produto: 格雷厄姆20年陈酿波特酒及杜罗河干红葡萄酒 (Graham's 20Y Tawny Port & Douro DOC); Ingredientes: 葡萄汁, 二氧化硫 (Contém Sulfitos SO2); Grau Alcoólico: 20.0% vol; Aviso de Saúde Obrigatório: 过量饮酒有害健康 (O consumo excessivo de álcool é prejudicial à saúde). Altura mínima dos caracteres chineses verificada: 2.2 mm (>= 1.8 mm exigido). Veredito CIQ: CONFORME E APROVADO."
        },
        {
            "doc_id": "UNSTRUCT-GACC-LABEL-PORK-9905",
            "corpus_table": "pt_unstruct_traducoes_rotulagem_mandarim_gacc",
            "raw_text": "AUTO DE RETIFICAÇÃO DE ROTULAGEM BILINGUE EM ENTREPOSTO FRIGORÍFICO N.º CIQ-LABEL-2026-9905. Exportador: Maporal, S.A. (EORI PT508112244, Registo CIFER CPRT18000101000505). Importador: COFCO Meat (USCC 91110000101123456N). Fatura INV-PT-2026-9905 (1650000.00 EUR), BL COSU6288992205, Contentor COSU4455665, Porto de Sines PTSIN -> CNSHA. Durante a inspeção de entrada em Xangai verificou-se que a etiqueta interna de plástico das embalagens de lombo de porco alentejano congelado (-18.0C) apresentava o número de registo CIFER impresso com 1.5 mm. Foi ordenada retificação de rotulagem no armazém alfandegado sob supervisão da GACC antes da emissão do certificado e-CIQ final."
        }
    ]

    # 90. pt_unstruct_relatorios_due_diligence_sancoes_kyc (N42: Banking KYC, Sanctions Screening & Transfer Pricing)
    u["90_pt_unstruct_relatorios_due_diligence_sancoes_kyc"] = [
        {
            "doc_id": "UNSTRUCT-KYC-BCP-CALB-2026",
            "corpus_table": "pt_unstruct_relatorios_due_diligence_sancoes_kyc",
            "raw_text": "RELATÓRIO DE COMPLIANCE BANCÁRIO, KYC (KNOW YOUR CUSTOMER), TRIAGEM DE SANÇÕES INTERNACIONAIS E PREÇOS DE TRANSFERÊNCIA N.º KYC-BCP-2026-0001. Instituição Financeira: Millennium bcp - Departamento de Compliance de Trade Finance (Lisboa). Operação Analisada: Contrato CN-PT-CTR-2026-001 e Fatura INV-CN-2026-8801 (6283500.00 EUR), DAU MRN 26PT000395IM008801, BL COSU6288991101, Contentor COSU8001101, Porto PTSIN. Entidades Verificadas: Ordenador CALB Portugal, S.A. (EORI PT517890123 / NIF 517890123) e Beneficiário CALB Group Co., Ltd. (USCC 91320413MA1M9Y2C4B, cotada na Bolsa de Hong Kong HKEX: 3931). Triagem nas listas consolidadas de sanções da União Europeia, ONU e OFAC: ZERO OCORRÊNCIAS (CLEAN). Verificação de Bens de Duplo Uso (TARIC 8507600090): Licença MOFCOM validada e Certificado de Utilizador Final Civil na ZILS Sines confirmado. Parecer de Compliance: RISCO BAIXO - OPERAÇÃO APROVADA."
        },
        {
            "doc_id": "UNSTRUCT-KYC-BPI-CATL-2026",
            "corpus_table": "pt_unstruct_relatorios_due_diligence_sancoes_kyc",
            "raw_text": "PARECER DE DUE DILIGENCE BANCÁRIA E BENEFICIÁRIO EFETIVO (RCBE) N.º KYC-BPI-2026-0004. Cliente Nacional: REN - Redes Energéticas Nacionais, SGPS, S.A. (EORI PT503412890 / NIF 503412890). Contraparte Chinesa: Contemporary Amperex Technology Co., Limited (CATL, USCC 91350900587527783P). Contrato CN-PT-CTR-2026-004, Fatura INV-CN-2026-8804 (3520000.00 EUR), DAU MRN 26PT000140IM008804, BL COSU6288991104, Contentor CATU8004401, TARIC 8507600090. Confirma-se conformidade total com a Lei n.º 83/2017 (Prevenção do Branqueamento de Capitais) e rastreabilidade integral via mensagem SWIFT UETR 97ed4827-7b6f-4491-a06f-b548d5a75004."
        }
    ]

    return u
