// =============================================================================
// UNIVERSIDADE DO ALGARVE - Mestrado em Engenharia Informática (2026/2027)
// Modelação e Integração de Dados (DMI) - Projeto P1
// Subtópico Portugal: Vistas MongoDB (db.createView para MongoDB Compass)
// Autor: Afonso Bitoque
// =============================================================================
// Como executar no mongosh ou terminal:
//   mongosh pt_comercio_internacional database/mongo_create_views.js
// No MongoDB Compass:
//   As vistas aparecem na barra lateral com um ícone de 'Olho / Vista'
// =============================================================================

// 1. Vista de Resumo das Declarações de Importação DAU (Origem China)
db.createView(
  "vw_resumo_importacoes_china_dau",
  "04_pt_declaracoes_aduaneiras_dau",
  [
    {
      $match: {
        tipo_declaracao: { $regex: "^IM" },
        pais_origem_ou_destino_iso: "CN"
      }
    },
    {
      $project: {
        mrn_codigo: 1,
        data_aceitacao: "$data_aceitacao_aduana",
        estancia_aduaneira: "$estancia_aduaneira_codigo",
        importador_eori: "$entidades_envolvidas.importador_destinatario.eori",
        importador_nome: "$entidades_envolvidas.importador_destinatario.nome",
        regime_aduaneiro: "$regime_aduaneiro_codigo",
        incoterm: "$condicoes_entrega_incoterm.termo",
        valor_aduaneiro_eur: "$valores_tributaveis_totais.total_valor_aduaneiro_eur",
        total_impostos_pagos_eur: {
          $sum: [
            "$impostos_e_direitos_apurados.direitos_aduaneiros_totais_eur",
            "$impostos_e_direitos_apurados.iva_aduaneiro_total_eur",
            "$impostos_e_direitos_apurados.taxas_especiais_e_antidumping_eur"
          ]
        },
        num_artigos: { $size: { $ifNull: ["$adicoes_artigos", []] } }
      }
    },
    { $sort: { data_aceitacao: -1 } }
  ]
);

// 2. Vista de Rastreabilidade e Auditoria de Risco de Operadores Económicos
db.createView(
  "vw_auditoria_operadores_risco_pt",
  "01_pt_operadores_economicos",
  [
    {
      $project: {
        eori_code: 1,
        nif_pt: 1,
        razao_social: 1,
        estatuto_oea: "$estatuto_operador_economico_autorizado.tipo_certificacao",
        setor_atividade: "$cae_atividade_economica_principal.designacao",
        nivel_risco_aduaneiro: "$perfil_risco_aduaneiro.classificacao_nivel",
        canal_habitual: "$perfil_risco_aduaneiro.canal_selecao_habitual",
        historico_infracoes: "$perfil_risco_aduaneiro.historico_infracoes_ultimos_3_anos"
      }
    },
    { $sort: { nivel_risco_aduaneiro: -1 } }
  ]
);

// 3. Vista de Movimentação Portuária e Escalas em Sines
db.createView(
  "vw_escalas_porto_sines_resumo",
  "05_pt_escalas_navios_manifestos_sines",
  [
    {
      $project: {
        numero_escala: "$numero_escala_jul",
        navio_nome: "$dados_navio.nome_embarcacao",
        imo: "$dados_navio.numero_imo",
        porto_origem: "$rota_viagem.porto_origem_unlocode",
        porto_procedencia: "$rota_viagem.porto_anterior_unlocode",
        data_chegada: "$operacoes_cais.data_hora_atracacao",
        teus_descarregados: "$manifesto_carga_maritima.totais_carga.total_teus_descarregados",
        contentores_inspecionados: "$controlo_aduaneiro_escala.total_contentores_selecionados_raio_x",
        atraso_dias: "$operacoes_cais.dias_atraso_registados"
      }
    },
    { $sort: { data_chegada: -1 } }
  ]
);

print("✅ [MONGODB COMPASS VIEWS CRIADAS] 3 vistas criadas na base de dados MongoDB!");
