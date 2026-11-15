-- =============================================================================
-- UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
-- Modelação e Integração de Dados (DMI) - Projeto P1
-- Subtópico Portugal: Vistas SQL do Warehouse Extraído por IA
-- Autor: Afonso Bitoque
-- =============================================================================

-- 1. Vista de Auditoria Global de Conformidade e Risco Aduaneiro (Grafo de Conhecimento IA)
DROP VIEW IF EXISTS vw_auditoria_ia_conformidade_global;
CREATE VIEW vw_auditoria_ia_conformidade_global AS
SELECT 
    doc_id,
    source_unstructured_table AS corpus_origem,
    primary_eori_pt AS operador_eori_pt,
    primary_mrn_dau AS declaracao_mrn_dau,
    primary_taric_10 AS pauta_taric_10,
    primary_cifer_gacc AS registo_cifer_china,
    primary_vessel_imo AS navio_imo,
    primary_amount_eur AS montante_eur,
    ai_compliance_verdict AS veredito_conformidade_ia,
    ai_risk_level AS nivel_risco,
    ai_risk_score_0_100 AS pontuacao_risco_ia,
    ROUND(ai_confidence * 100.0, 1) AS confianca_modelo_pct
FROM ai_extracted_knowledge_graph;

-- 2. Vista de Sinistros e Incidentes Marítimos em Alto-Mar e no Porto de Sines
DROP VIEW IF EXISTS vw_incidentes_maritimos_e_avarias_ia;
CREATE VIEW vw_incidentes_maritimos_e_avarias_ia AS
SELECT 
    g.doc_id,
    g.source_unstructured_table AS categoria_documento,
    g.primary_vessel_imo AS navio_imo,
    g.primary_port_unlocode AS porto_afetado,
    g.primary_amount_eur AS prejuizo_estimado_eur,
    g.ai_compliance_verdict AS parecer_ia,
    g.ai_risk_score_0_100 AS risco_pontuacao
FROM ai_extracted_knowledge_graph g
WHERE g.source_unstructured_table IN (
    'pt_unstruct_diarios_bordo_incidentes_maritimos_aps',
    'pt_unstruct_cartas_protesto_maritimo_sea_protest',
    'pt_unstruct_participacoes_sinistros_seguradoras'
);

-- 3. Vista de Ações de Fiscalização Alimentar/Aduaneira (ASAE / DGAV / AT Apreensões)
DROP VIEW IF EXISTS vw_fiscalizacao_asae_dgav_e_apreensoes;
CREATE VIEW vw_fiscalizacao_asae_dgav_e_apreensoes AS
SELECT 
    g.doc_id,
    g.primary_eori_pt AS operador_alvo_eori,
    g.primary_mrn_dau AS mrn_apreendido,
    g.primary_taric_10 AS mercadoria_taric,
    g.ai_compliance_verdict AS decisao_autoridade,
    g.ai_risk_score_0_100 AS gravidade_infracao_score
FROM ai_extracted_knowledge_graph g
WHERE g.source_unstructured_table IN (
    'pt_unstruct_relatorios_inspecao_asae_dgav',
    'pt_unstruct_autos_apreensao_contrafacao_at',
    'pt_unstruct_oficios_notificacoes_audiencia_previa_at'
);

-- 4. Vista de Certificados de Origem Fitossanitários OCR e Barreiras Sanitárias CIFER
DROP VIEW IF EXISTS vw_certificados_fitossanitarios_ocr_taric;
CREATE VIEW vw_certificados_fitossanitarios_ocr_taric AS
SELECT 
    g.doc_id,
    g.primary_eori_pt AS exportador_nacional_eori,
    g.primary_cifer_gacc AS registo_cifer_gacc_china,
    g.primary_taric_10 AS codigo_pautal_taric,
    g.ai_compliance_verdict AS validacao_admissibilidade_china,
    g.ai_risk_score_0_100 AS score_risco_barreira_sanitaria
FROM ai_extracted_knowledge_graph g
WHERE g.source_unstructured_table IN (
    'pt_unstruct_certificados_origem_fitossanitarios_ocr',
    'pt_unstruct_traducoes_rotulagem_mandarim_gacc'
);

-- 5. Vista de Telemetria IoT dos Contentores Reefer e Ruptura da Cadeia de Frio
DROP VIEW IF EXISTS vw_telemetria_iot_cadeia_frio_risco;
CREATE VIEW vw_telemetria_iot_cadeia_frio_risco AS
SELECT 
    g.doc_id,
    g.primary_container_iso AS contentor_reefer_iso,
    g.primary_vessel_imo AS navio_transportador_imo,
    g.max_temperature_recorded_c AS temp_maxima_registada_celsius,
    CASE 
        WHEN g.max_temperature_recorded_c > -15.0 THEN 'ALERTA_RUPTURA_CADEIA_FRIO'
        ELSE 'TEMPERATURA_CONTROLADA_OK'
    END AS estado_cadeia_refrigeracao,
    g.ai_compliance_verdict AS conformidade_sensorica,
    g.ai_risk_score_0_100 AS probabilidade_perda_carga
FROM ai_extracted_knowledge_graph g
WHERE g.source_unstructured_table = 'pt_unstruct_logs_telemetria_iot_cadeia_frio';

-- 6. Vista do Dossier Diplomático, Inteligência de Mercado e Investimento Bilateral
DROP VIEW IF EXISTS vw_dossier_diplomatico_e_investimento_aicep;
CREATE VIEW vw_dossier_diplomatico_e_investimento_aicep AS
SELECT 
    g.doc_id,
    g.source_unstructured_table AS tipo_relatorio,
    g.primary_amount_eur AS valor_investimento_eur,
    g.ai_compliance_verdict AS enquadramento_estrategico,
    g.tfidf_keywords_json AS palavras_chave_relevantes
FROM ai_extracted_knowledge_graph g
WHERE g.source_unstructured_table IN (
    'pt_unstruct_tratados_memorandos_diplomaticos_mneg',
    'pt_unstruct_relatorios_inteligencia_mercado_aicep',
    'pt_unstruct_atas_reunioes_camara_comercio_ccilc',
    'pt_unstruct_auditorias_sustentabilidade_esg_fornecedores'
);
