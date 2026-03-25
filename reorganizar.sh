#!/usr/bin/env bash
# =============================================================================
# Script de Reorganização — CAF-FINAL
# TC 011.073/2025-0 — Qualidade de Dados do CAF
#
# REGRAS:
# - NÃO deleta nada — move para subpastas organizadas
# - Renomeia com padrão pecaXXX_descricao_curta.ext
# - Cria README.md em cada pasta
# - Preserva arquivos originais
# =============================================================================

set -euo pipefail

BASE="/sessions/vigilant-relaxed-cannon/mnt/CAF-FINAL"
cd "$BASE"

echo "=== PASSO 1: Criar nova estrutura de pastas ==="

mkdir -p 00_CONTEXTO
mkdir -p 01_RELATORIO_V2
mkdir -p 02_FONTE_VERDADE
mkdir -p 03_RELATORIO_V1
mkdir -p 04_PECAS_EVIDENCIA/ACH01_documental
mkdir -p 04_PECAS_EVIDENCIA/ACH02_geoespacial
mkdir -p 04_PECAS_EVIDENCIA/ACH03_cadastral
mkdir -p 04_PECAS_EVIDENCIA/ACH04_metadados
mkdir -p 04_PECAS_EVIDENCIA/TRANSVERSAIS
mkdir -p 04_PECAS_EVIDENCIA/txt_extraido
mkdir -p 05_PECAS_TRAMITACAO/pre_relatorio
mkdir -p 05_PECAS_TRAMITACAO/pos_relatorio
mkdir -p 06_NORMAS_CRITERIOS/legislacao
mkdir -p 06_NORMAS_CRITERIOS/iso_referenciais
mkdir -p 06_NORMAS_CRITERIOS/nat_tcu
mkdir -p 07_MODELOS_TCU
mkdir -p _artefatos_latex

echo "Pastas criadas."

echo ""
echo "=== PASSO 2: Mover seções do Relatório V2 ==="

# 00_CONTEXTO
cp PHASE3_MOUNTING_REPORT/RESUMO_EXECUTIVO_V2.md 00_CONTEXTO/
cp PHASE3_MOUNTING_REPORT/VISAO_GERAL_V2.md 00_CONTEXTO/

# 01_RELATORIO_V2
cp PHASE3_MOUNTING_REPORT/INTRODUCAO_V2.md 01_RELATORIO_V2/
cp PHASE3_MOUNTING_REPORT/ACH01_V2.md 01_RELATORIO_V2/
cp PHASE3_MOUNTING_REPORT/ACH02_V2.md 01_RELATORIO_V2/
cp PHASE3_MOUNTING_REPORT/ACH03_V2.md 01_RELATORIO_V2/
cp PHASE3_MOUNTING_REPORT/ACH04_V2.md 01_RELATORIO_V2/

echo "Relatório V2 movido."

echo ""
echo "=== PASSO 3: Mover Fonte de Verdade ==="

cp PECAS_A_INSERIR/PECA170_MATRIZ_DE_ACHADOS_CAF.md 02_FONTE_VERDADE/
cp PECAS_A_INSERIR/PECA170_MATRIZ_DE_ACHADOS_CAF.docx 02_FONTE_VERDADE/
cp PECAS_A_INSERIR/PECA169_codex_anexo_comentarios_gestor_v2.md 02_FONTE_VERDADE/

echo "Fonte de verdade movida."

echo ""
echo "=== PASSO 4: Mover Relatório V1 ==="

cp RELATORIO_ATUAL_PECA_141/relatorio_v1.md 03_RELATORIO_V1/
cp RELATORIO_ATUAL_PECA_141/relatorio_v1.docx 03_RELATORIO_V1/
cp RELATORIO_ATUAL_PECA_141/CODEX_UPGRADED_V1_FINDINGS.md 03_RELATORIO_V1/

echo "Relatório V1 movido."

echo ""
echo "=== PASSO 5: Mover e renomear peças de EVIDÊNCIA por achado ==="

PE="PECAS_EXISTENTES"

# --- ACH-01: Documentação comprobatória ---
ACH01="04_PECAS_EVIDENCIA/ACH01_documental"
cp "$PE/peca103_adequacao_funcional_b89deb70-8b93-41fb-90ed-eb3ec3760849.pdf" "$ACH01/peca103_adequacao_funcional_docs.pdf"
cp "$PE/peca104_documentos_dimensao_area.pdf" "$ACH01/peca104_documentos_dimensao_area.pdf"
cp "$PE/peca105_analise_dimensao_area.pdf" "$ACH01/peca105_analise_dimensao_area.pdf"
cp "$PE/peca106_papel_trabalho_resolucao_dpi.pdf" "$ACH01/peca106_pt_resolucao_dpi.pdf"
cp "$PE/peca107_papel_trabalho_análise_quatro_modulos.pdf" "$ACH01/peca107_pt_analise_quatro_modulos.pdf"
cp "$PE/peca109_pt_analise_dimensao_area_versao_final.pdf" "$ACH01/peca109_pt_dimensao_area_final.pdf"
cp "$PE/peca140_nota_tecnica_atualizacao_populacao.pdf" "$ACH01/peca140_nota_tecnica_populacao.pdf"

# --- ACH-02: Integridade geoespacial ---
ACH02="04_PECAS_EVIDENCIA/ACH02_geoespacial"
cp "$PE/peca110_PT-01_filtro_uf_ativa_achadoII.pdf" "$ACH02/peca110_PT01_filtro_uf_ativa.pdf"
cp "$PE/peca111_PT-02_dimensionamento_leaflet_achadoII.pdf" "$ACH02/peca111_PT02_dimensionamento_leaflet.pdf"
cp "$PE/peca112_PT-03_Dimensionamento_CAF3_achadoII.pdf" "$ACH02/peca112_PT03_dimensionamento_caf3.pdf"
cp "$PE/peca113_PT-04_Extracao_Amostral_achadoII.pdf" "$ACH02/peca113_PT04_extracao_amostral.pdf"
cp "$PE/peca114_PT-05_Deteccao_Algoritmica_achadoII.pdf" "$ACH02/peca114_PT05_deteccao_algoritmica.pdf"
cp "$PE/peca115_PT-06_Analise_Precisao_achadoII.pdf" "$ACH02/peca115_PT06_analise_precisao.pdf"
cp "$PE/peca116_PT-07_Consistencia_Municipal_achadoII.pdf" "$ACH02/peca116_PT07_consistencia_municipal.pdf"
cp "$PE/peca117_PT-08_Duplicacoes_Espaciais_achadoII.pdf" "$ACH02/peca117_PT08_duplicacoes_espaciais.pdf"
cp "$PE/peca118_PT-09_Analise_Temporal_Leaflet_achadoII.pdf" "$ACH02/peca118_PT09_analise_temporal_leaflet.pdf"
cp "$PE/peca119_PT-10_Analise_Temporal_CAF30_achadoII.pdf" "$ACH02/peca119_PT10_analise_temporal_caf30.pdf"
cp "$PE/peca120_PT-11_Validacao_Temporal_Estratos_Equiv_achadoII.pdf" "$ACH02/peca120_PT11_validacao_temporal.pdf"
cp "$PE/peca121_PT-12_Areas_Municipais_Impossiveis_achadoII.pdf" "$ACH02/peca121_PT12_areas_municipais_impossiveis.pdf"
cp "$PE/peca122_MC_MASTER_INDEX_achadoII.pdf" "$ACH02/peca122_MC_master_index_ach02.pdf"

# --- ACH-03: Qualidade dos dados cadastrais ---
ACH03="04_PECAS_EVIDENCIA/ACH03_cadastral"
cp "$PE/peca123_pt_salvador_populacao_total.pdf" "$ACH03/peca123_pt_salvador_populacao.pdf"
cp "$PE/peca124_pt01_capacidade_civil.pdf" "$ACH03/peca124_PT01_capacidade_civil.pdf"
cp "$PE/peca125_pt02_dados_contato.pdf" "$ACH03/peca125_PT02_dados_contato.pdf"
cp "$PE/peca126_pt03_renda_outliers.pdf" "$ACH03/peca126_PT03_renda_outliers.pdf"
cp "$PE/peca127_pt04_cnaes_pj.pdf" "$ACH03/peca127_PT04_cnaes_pj.pdf"
cp "$PE/peca128_mc_master_index.pdf" "$ACH03/peca128_mc_master_index_ach03.pdf"
cp "$PE/peca128_mc_master_index.md" "$ACH03/peca128_mc_master_index_ach03.md"
cp "$PE/peca129_scripts_PT01_LABCONTAS_SQLServer.pdf" "$ACH03/peca129_scripts_labcontas.pdf"
cp "$PE/peca130_pt_outliers_renda.pdf" "$ACH03/peca130_pt_outliers_renda.pdf"
cp "$PE/peca131_pt_capacidade_civil.pdf" "$ACH03/peca131_pt_capacidade_civil.pdf"
cp "$PE/peca132_mc_index_achado04.pdf" "$ACH03/peca132_mc_index_achado04.pdf"

# --- ACH-04: Gestão de metadados ---
ACH04="04_PECAS_EVIDENCIA/ACH04_metadados"
cp "$PE/peca133_pt_ambiguidade_temporal.pdf" "$ACH04/peca133_pt_ambiguidade_temporal.pdf"
cp "$PE/peca134_pt_cobertura_dicionario.pdf" "$ACH04/peca134_pt_cobertura_dicionario.pdf"
cp "$PE/peca135_pt_qualidade_semantica.pdf" "$ACH04/peca135_pt_qualidade_semantica.pdf"
cp "$PE/peca136_pt_unidades_medida.pdf" "$ACH04/peca136_pt_unidades_medida.pdf"

# --- TRANSVERSAIS ---
TRANS="04_PECAS_EVIDENCIA/TRANSVERSAIS"
cp "$PE/peca75_dicionario_dados_caf.pdf" "$TRANS/peca075_dicionario_dados_caf.pdf"
cp "$PE/peca76_modelo_entidade_relacionamento.pdf" "$TRANS/peca076_modelo_entidade_relacionamento.pdf"
cp "$PE/peca77_especificacoes_ambiente_caf.pdf" "$TRANS/peca077_especificacoes_ambiente_caf.pdf"
cp "$PE/peca78_regras_negocio_caf_33ead8fe-0330-4190-9ddf-f3bd8b8acb62.pdf" "$TRANS/peca078_regras_negocio_caf.pdf"
cp "$PE/peca108_PortariaMDAn19.pdf" "$TRANS/peca108_portaria_mda_19_2025.pdf"

# --- Normas como peças ---
cp "$PE/peca79_resolucao_conarq_c76d74c2-802d-470f-8b73-d3d7b8e2b8fe.pdf" "$TRANS/peca079_resolucao_conarq.pdf"
cp "$PE/peca80_lei_11326_2006_b89deb70-8b93-41fb-90ed-eb3ec3760849.pdf" "$TRANS/peca080_lei_11326_2006.pdf"
cp "$PE/peca81_decreto_9064_2017.pdf" "$TRANS/peca081_decreto_9064_2017.pdf"
cp "$PE/peca82_ISO_8000_parte_2.pdf" "$TRANS/peca082_iso_8000_2.pdf"
cp "$PE/peca83_ISO_19157_2023_parte_1.pdf" "$TRANS/peca083_iso_19157_1.pdf"
cp "$PE/peca84_ISO_11179_2023_parte_1.pdf" "$TRANS/peca084_iso_11179_1.pdf"
cp "$PE/peca85_ISO_IEC_25012_2018.pdf" "$TRANS/peca085_iso_25012.pdf"
cp "$PE/peca86_cap_13_damadmbok.pdf" "$TRANS/peca086_cap13_damadmbok.pdf"
cp "$PE/peca137_mcr_bacen.pdf" "$TRANS/peca137_mcr_bacen.pdf"
cp "$PE/peca138_autodiagnostico_2024.pdf" "$TRANS/peca138_autodiagnostico_2024.pdf"
cp "$PE/peca139_PFIS AudQualidadeDados Rurais e Ambientais (3).pdf" "$TRANS/peca139_pfis_qualidade_dados_rurais.pdf"

echo "Peças de evidência movidas."

echo ""
echo "=== PASSO 6: Mover peças de TRAMITAÇÃO ==="

# Pré-relatório
PRE="05_PECAS_TRAMITACAO/pre_relatorio"
cp "$PE/peca4-comunicacao-fiscalizacao.pdf" "$PRE/peca004_oficio_0132_audti_comunicacao.pdf"
cp "$PE/peca33_30ef9bec-74b4-4f2a-b6b2-e3697f97f97a.pdf" "$PRE/peca033_oficio_sei_98265_mgi.pdf"
cp "$PE/peca46_Ofício 0001492025 - AudTI.pdf" "$PRE/peca046_oficio_000149_audti.pdf"
cp "$PE/peca49_OFÍCIO-MDA N_114_2025_AECI-MDA_MDA.pdf" "$PRE/peca049_oficio_mda_114_aeci.pdf"
cp "$PE/peca51_OFÍCIO - MDA N 831_2025_SAF-MDA_MDA.pdf" "$PRE/peca051_oficio_mda_831_saf.pdf"
cp "$PE/peca56_Ofício 000192_2025 - AudTI.pdf" "$PRE/peca056_oficio_000192_audti.pdf"
cp "$PE/peca58_OFÍCIO - MDA N 130_2025_AECI-MDA_MDA.pdf" "$PRE/peca058_oficio_mda_130_aeci.pdf"
cp "$PE/peca59_DESPACHO-MDA N 196_2025_DCAF-MDA_MDA.pdf" "$PRE/peca059_despacho_mda_196_dcaf.pdf"
cp "$PE/peca60_OFÍCIO N 59_2025_CGINOV_STI_SE_MAPA.pdf" "$PRE/peca060_oficio_59_cginov_mapa.pdf"
cp "$PE/peca61_ Encaminhamento de Dados de Acesso – Processo SEI n 55000012930_2025-64.pdf" "$PRE/peca061_encaminhamento_dados_acesso_sei.pdf"
# Peças 62-64 são duplicatas de 58-60 — manter mas sinalizar
cp "$PE/peca62_OFÍCIO - MDA N 130_2025_AECI-MDA_MDA.pdf" "$PRE/peca062_oficio_mda_130_aeci_DUP58.pdf"
cp "$PE/peca63_DESPACHO-MDA N 196_2025_DCAF-MDA_MDA.pdf" "$PRE/peca063_despacho_mda_196_dcaf_DUP59.pdf"
cp "$PE/peca64_OFÍCIO N 59_2025_CGINOV_STI_SE_MAPA.pdf" "$PRE/peca064_oficio_59_cginov_mapa_DUP60.pdf"
cp "$PE/peca65_email de Encaminhamento de Dados de Acesso – Processo SEI n 55000012930_2025-64.pdf" "$PRE/peca065_email_encaminhamento_dados_acesso_sei.pdf"
cp "$PE/peca66_Ofício 000356_2025 - AudTI.pdf" "$PRE/peca066_oficio_000356_audti.pdf"
cp "$PE/peca68_OFÍCIO - MDA N 164_2025_AECI-MDA_MDA.pdf" "$PRE/peca068_oficio_mda_164_aeci.pdf"
cp "$PE/peca69_OFÍCIO - MDA N 969_2025_SPOA-MDA_MDA.pdf" "$PRE/peca069_oficio_mda_969_spoa.pdf"
cp "$PE/peca70_OFÍCIO N 76_2025_CGDSD_STI_SE_MAPA.pdf" "$PRE/peca070_oficio_76_cgdsd_mapa.pdf"
cp "$PE/peca71_ata_reuniao_apresentacao_equipe_01_07_2025.pdf" "$PRE/peca071_ata_reuniao_apresentacao_20250701.pdf"
cp "$PE/peca72_ata_reuniao_abertura_03_07_2025.pdf" "$PRE/peca072_ata_reuniao_abertura_20250703.pdf"
cp "$PE/peca73_ata_reuniao_trabalho_07_10_2025.pdf" "$PRE/peca073_ata_reuniao_trabalho_20251007.pdf"
cp "$PE/peca74_ata_reuniao_encerramento_21_10_2025.pdf" "$PRE/peca074_ata_reuniao_encerramento_20251021.pdf"

# Pós-relatório (contraditório)
POS="05_PECAS_TRAMITACAO/pos_relatorio"
cp "$PE/PECA142_417ffa70-e6ca-4e95-87b8-ecbe44ef7598.pdf" "$POS/peca142_pronunciamento_subunidade_audti.pdf"
cp "$PE/PECA143_f0db14d5-544d-4cc7-9e76-a6396af098bb.pdf" "$POS/peca143_pronunciamento_unidade_audti.pdf"
cp "$PE/PECA144_2112260a-7e1d-4030-bb03-a0421abb6b3e.pdf" "$POS/peca144_oficio_4045_seproc_diligencia.pdf"
cp "$PE/PECA145_a1e6d198-a410-4981-9faf-a1efb2cecc95.pdf" "$POS/peca145_termo_ciencia_conecta_tcu.pdf"
cp "$PE/PECA146_a4725580-0fc4-4fb2-a7ff-c8334ebc45c9.pdf" "$POS/peca146_oficio_28_aeci_prorrogacao.pdf"
cp "$PE/PECA147_5ba9b46c-7103-4208-b676-2d786a1d6546.pdf" "$POS/peca147_despacho_prorrogacao_prazo.pdf"
cp "$PE/PECA148_5222b52c-44cc-4d64-87f5-91c33f37c430.pdf" "$POS/peca148_oficio_aeci_encaminhamento.pdf"
cp "$PE/PECA149_1577c261-fc39-453b-a21b-b4e04b24f716.pdf" "$POS/peca149_oficio_dcaf_manifestacao.pdf"
cp "$PE/PECA150_5b1299d3-89a3-45c1-8162-b7f25b81ce46.pdf" "$POS/peca150_relatorio_tecnico_dcaf_76p.pdf"
cp "$PE/PECA151_467145c7-8218-43f7-9e86-f6a1855f98da.pdf" "$POS/peca151_oficio_aeci_acordao_885.pdf"
cp "$PE/PECA152_e5bbcc39-6e22-4641-9787-0f9a98090567.pdf" "$POS/peca152_caf_em_numeros_32p.pdf"
cp "$PE/PECA153_c8039635-e67c-4382-82c6-e7ca85a69016.pdf" "$POS/peca153_organograma_dcaf_20p.pdf"
cp "$PE/PECA154_06fe444a-fb2b-488b-9b01-75f4d54011dc.pdf" "$POS/peca154_nota_tecnica_cgti_tic.pdf"
cp "$PE/PECA155_5206d838-fe92-48e9-897a-c5a7440e2a10.pdf" "$POS/peca155_etp_contratacao_tic_81p.pdf"
cp "$PE/PECA156_3e723048-4587-4e70-bbca-03eb968e275b.pdf" "$POS/peca156_relatorio_monitoramento_caf.pdf"
cp "$PE/PECA157_64b09371-d838-441f-9e9d-909952f42a39.pdf" "$POS/peca157_nota_tecnica_ted_ufes.pdf"
cp "$PE/PECA158_5e826027-d3db-4aa3-8ad3-310315bc6299.pdf" "$POS/peca158_plano_trabalho_ted_ufes.pdf"
cp "$PE/PECA159_ef2d8c1d-f638-4c71-b406-9816abf115c2.pdf" "$POS/peca159_contrato_dataprev.pdf"
cp "$PE/PECA160_b1ec4ff1-8659-40d0-9838-535baff712ee.pdf" "$POS/peca160_oficio_spoa_incidentes_tic.pdf"
cp "$PE/PECA161_dcb721d5-02b6-4ddf-b286-79943a362b28.pdf" "$POS/peca161_memoria_tecnica_doc121.pdf"
cp "$PE/PECA162_05f48235-7176-412f-88cf-fc647b9ee7eb.pdf" "$POS/peca162_apresentacao_caf_governanca.pdf"
cp "$PE/PECA163_c43e9fb1-3fc6-481e-b107-abafcac0e6d4.pdf" "$POS/peca163_anexo_tecnico_achado01.pdf"
# Peça 164 — ausente do acervo
cp "$PE/PECA165_8c85f34f-8d97-496a-b68c-56eeed2334f7.pdf" "$POS/peca165_nota_tecnica_cafweb.pdf"
cp "$PE/PECA166_2d24187f-dd7d-4984-ab74-c359e8d0c243.pdf" "$POS/peca166_memoria_tecnica_doc105.pdf"
cp "$PE/PECA167_434aa822-d880-47e8-a7e5-3d7d02a277f3.pdf" "$POS/peca167_termo_recebimento_area_validation.pdf"
cp "$PE/PECA168_241b881b-4c93-49c2-b9f2-875166525765.pdf" "$POS/peca168_termo_recebimento_inflacao_municipal.pdf"

# Inventários existentes
cp "$PE/inventario_pecas_comentarios.md" "05_PECAS_TRAMITACAO/inventario_pecas_comentarios.md"
cp "$PE/inventario_pecas_para_docx.md" "05_PECAS_TRAMITACAO/inventario_pecas_para_docx.md"

echo "Peças de tramitação movidas."

echo ""
echo "=== PASSO 7: Mover textos extraídos ==="

TXT="04_PECAS_EVIDENCIA/txt_extraido"
for f in "$PE"/*_texto_com_paginas.txt "$PE"/*_texto.txt; do
    [ -f "$f" ] && cp "$f" "$TXT/"
done

echo "Textos extraídos movidos."

echo ""
echo "=== PASSO 8: Mover Normas e Critérios ==="

NC="NORMAS_CRITERIOS"
# Legislação
cp "$NC/PortariaMDAn19.pdf" "06_NORMAS_CRITERIOS/legislacao/portaria_mda_19_2025.pdf"

# ISOs e referenciais
cp "$NC/ISO_IEC_25012_2008.pdf" "06_NORMAS_CRITERIOS/iso_referenciais/"
cp "$NC/ISO_19157_1_2023.pdf" "06_NORMAS_CRITERIOS/iso_referenciais/"
cp "$NC/ISO_IEC_11179_1_2023.pdf" "06_NORMAS_CRITERIOS/iso_referenciais/"
cp "$NC/ISO_8000_2_2022.pdf" "06_NORMAS_CRITERIOS/iso_referenciais/"
cp "$NC/dama-dmbok-data-management-body-of-knowledge-2nd-edition 1.pdf" "06_NORMAS_CRITERIOS/iso_referenciais/dama_dmbok_2ed.pdf"

# NAT TCU
cp "$NC/Manual_auditoria_operacional_4_edicao.pdf" "06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf"
cp "$NC/manual-de-redacao.pdf" "06_NORMAS_CRITERIOS/nat_tcu/manual_de_redacao.pdf"
cp "$NC/Resolução TCU n° 315_2020.doc" "06_NORMAS_CRITERIOS/nat_tcu/resolucao_tcu_315_2020.doc"
cp "$NC/nat_checklist.md" "06_NORMAS_CRITERIOS/nat_tcu/"
cp "$NC/normas_auditoria_nat_tcu.md" "06_NORMAS_CRITERIOS/nat_tcu/"
cp "$NC/NAT_QUICK_REFERENCE.md" "06_NORMAS_CRITERIOS/nat_tcu/"
cp "$NC/nat_index.json" "06_NORMAS_CRITERIOS/nat_tcu/"
cp "$NC/official_terms.json" "06_NORMAS_CRITERIOS/nat_tcu/"
cp "$NC/modelo_matriz_de_achados.docx" "06_NORMAS_CRITERIOS/nat_tcu/"

echo "Normas movidas."

echo ""
echo "=== PASSO 9: Mover Modelos TCU ==="

cp "MODELOS_RELATORIO_TCU/RELATÓRIO_ Instrucao_Processo_00795120191.pdf" "07_MODELOS_TCU/exemplo_instrucao_processo.pdf"
cp "MODELOS_RELATORIO_TCU/Template Relatório de Auditoria.docx" "07_MODELOS_TCU/template_relatorio_auditoria.docx"

echo "Modelos movidos."

echo ""
echo "=== PASSO 10: Isolar artefatos LaTeX ==="

for ext in aux log out; do
    for f in "$PE"/*."$ext"; do
        [ -f "$f" ] && cp "$f" "_artefatos_latex/"
    done
done
# Também mover os .tex
for f in "$PE"/*.tex; do
    [ -f "$f" ] && cp "$f" "_artefatos_latex/"
done
# E a versão "original" da portaria
cp "$PE/peca108_PortariaMDAn19_original.pdf" "_artefatos_latex/" 2>/dev/null || true

echo "Artefatos LaTeX isolados."

echo ""
echo "=== PASSO 11: Limpar .DS_Store ==="
find . -name ".DS_Store" -delete 2>/dev/null || true

echo "DS_Store removidos."

echo ""
echo "=== REORGANIZAÇÃO COMPLETA ==="
echo ""
echo "Estrutura nova:"
find . -maxdepth 3 -type d | sort | grep -v "PECAS_EXISTENTES\|PHASE3\|RELATORIO_ATUAL\|MODELOS_RELATORIO\|^./NORMAS" | head -30

echo ""
echo "Contagem de arquivos na nova estrutura:"
for d in 00_CONTEXTO 01_RELATORIO_V2 02_FONTE_VERDADE 03_RELATORIO_V1 04_PECAS_EVIDENCIA 05_PECAS_TRAMITACAO 06_NORMAS_CRITERIOS 07_MODELOS_TCU _artefatos_latex; do
    count=$(find "$d" -type f 2>/dev/null | wc -l)
    echo "  $d: $count arquivos"
done

echo ""
echo "NOTA: As pastas originais foram PRESERVADAS."
echo "Após validação, você pode removê-las com:"
echo "  rm -rf PECAS_EXISTENTES PHASE3_MOUNTING_REPORT RELATORIO_ATUAL_PECA_141 NORMAS_CRITERIOS MODELOS_RELATORIO_TCU PECAS_A_INSERIR"
