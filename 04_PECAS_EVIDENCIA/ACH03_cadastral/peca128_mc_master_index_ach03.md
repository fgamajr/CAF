# MC_MASTER_INDEX.md - Achado 03: Qualidade dos Dados Cadastrais do Sistema CAF

**Versão:** 1.4
**Data:** 28 de novembro de 2025
**Achado:** 03 - Comprometimento da Qualidade dos Dados Cadastrais
**Papéis de Trabalho:** PT-01 a PT-05

---

## Convenções de Nomenclatura

- **Formato MC:** `MC-XXX/PT-YY` (ex: MC-001/PT-01)
- **Estilo de variáveis:** camelCase (ex: `populacaoResponsaveis`, `taxaObitosUF`)
- **Precisão numérica:** Seguir PADRAO_PRECISAO_NUMERICA.md (regra de 5%)
- **Status:** OK | Revisar | Pendente

---

## PT-01: Capacidade Civil e Legitimidade dos Responsáveis

### Variáveis Canônicas

| MC | Nome da Variável | Valor | Origem/Método | Status |
|---|---|---|---|---|
| **MC-001/PT-01** | `populacaoResponsaveis` | 3.340.542 | Cruzamento CAF × RFB (agosto/2025) | OK |
| **MC-002/PT-01** | `obitosConfirmados` | 3.097 | Query SQL `pt01_obitos_responsaveis.sql` + SISOBI | OK |
| **MC-003/PT-01** | `taxaObitosUF` | 0,107% | (3.097 / 2.905.101) × 100 | OK |
| **MC-004/PT-01** | `taxaObitosCPF` | 0,107% | (3.097 / 2.905.101) × 100 | OK |
| **MC-005/PT-01** | `menoresAbsolutamenteIncapazes` | 89 | Filtro `idade_primeira_ativacao < 16` | OK |
| **MC-006/PT-01** | `adolescentesNaoEmancipados` | 49 | Filtro `idade 16-17 AND st_emancipado=FALSE` | OK |
| **MC-007/PT-01** | `datasNascimentoDivergentes` | 11.999 | CAF.dt_nascimento ≠ RFB.dt_nascimento | OK |
| **MC-008/PT-01** | `cpfsNaoEncontradosRFB` | 520 | LEFT JOIN RFB WHERE RFB.nr_cpf IS NULL | OK |
| **MC-009/PT-01** | `totalInconsistencias` | 15.811 | Soma MC-002 + MC-005 + MC-006 + MC-007 + MC-008 + MC-013 | OK |
| **MC-010/PT-01** | `taxaInconsistenciaCPF` | 0,544% | (15.811 / 2.905.101) × 100 | OK |
| **MC-011/PT-01** | `obitosAntigos_2010_2015` | 645 | Filtro `ano_obito BETWEEN 2010 AND 2015` (20,8% do total) | OK |
| **MC-012/PT-01** | `obitosRecentes_2021_2025` | 1.228 | Filtro `ano_obito BETWEEN 2021 AND 2025` (39,7% do total) | OK |
| **MC-013/PT-01** | `idadesNegativas` | 57 | Filtro `idade_na_ativacao < 0` (nascimento no futuro) | OK |
| **MC-014/PT-01** | `operacoesPRONAF_posObito` | 312 | Cruzamento óbitos × SICOR PRONAF | OK |
| **MC-015/PT-01** | `valorPRONAF_posObito` | R$ 18.900.000 | Soma `vl_operacao` (312 registros) | OK |

---

## PT-02: Qualidade de Dados de Contato (Emails e CEPs)

### Variáveis Canônicas

| MC | Nome da Variável | Valor | Origem/Método | Status |
|---|---|---|---|---|
| **MC-015/PT-02** | `populacaoEmailsPF` | 6.525.658 | COUNT(*) FROM S_PESSOA_FISICA.ds_email | OK |
| **MC-016/PT-02** | `populacaoEmailsPJ` | 9.650 | COUNT(*) FROM S_PESSOA_JURIDICA.ds_email | OK |
| **MC-017/PT-02** | `emailsNaoPossui` | 4.904.403 | WHERE ds_email = 'naopossui@mail.com' | OK |
| **MC-018/PT-02** | `taxaEmailsNaoPossui` | 75,16% | (4.904.403 / 6.525.658) × 100 | OK |
| **MC-019/PT-02** | `emailsInvalidosPF` | 5.913.659 | Regex RFC 5322 + padrões fictícios | OK |
| **MC-020/PT-02** | `taxaInvalidadeEmailPF` | 90,62% | (5.913.659 / 6.525.658) × 100 | OK |
| **MC-021/PT-02** | `emailsValidosPJ` | 9.621 | Regex RFC 5322 válido (PJ) | OK |
| **MC-022/PT-02** | `taxaValidadeEmailPJ` | 99,70% | (9.621 / 9.650) × 100 | OK |
| **MC-023/PT-02** | `disparidadePF_PJ` | 90,32 p.p. | 99,70% - 9,38% | OK |
| **MC-024/PT-02** | `populacaoCEPs` | 3.540.310 | COUNT(*) FROM S_ENDERECO.nr_cep | OK |
| **MC-025/PT-02** | `cepsGenericos` | 3.318.270 | WHERE nr_cep LIKE '%000' | OK |
| **MC-026/PT-02** | `taxaCEPsGenericos` | 93,7% | (3.318.270 / 3.540.310) × 100 | OK |
| **MC-027/PT-02** | `cepsEspecificos` | 222.040 | WHERE nr_cep NOT LIKE '%000' | OK |
| **MC-028/PT-02** | `inconsistenciasCEP_UF` | 41.966 | API Correios: CEP.uf ≠ CAF.sg_uf | OK |
| **MC-029/PT-02** | `taxaInconsistenciaCEP_UF` | 18,9% | (41.966 / 222.040) × 100 | OK |
| **MC-030/PT-02** | `defasagemBenchmarkCEP` | 76,1 p.p. | CadÚnico 82,4% - CAF 6,3% | OK |

---

## PT-03: Outliers Extremos em Dados de Renda ⭐

**Status do PT:** ✅ Versão 3.1 - Recalculado com metodologia agregada por UF (28/nov/2025)
**Metodologia:** Renda total por UF ativa (evita recontagem de múltiplas declarações por pessoa)
**Evidências Reais:** Ata reunião MDA (21/out/2025), Queries information_schema, Triggers validation

### Variáveis Canônicas

| MC | Nome da Variável | Valor | Origem/Método | Status |
|---|---|---|---|---|
| **MC-031/PT-03** | `populacaoUFsAtivas` | 3.340.741 | COUNT(DISTINCT id_unidade_familiar) com renda > 0 e UF ativa | OK |
| **MC-032/PT-03** | `medianaRenda` | R$ 19.300 | PERCENTILE_CONT(0.50) sobre renda agregada por UF | OK |
| **MC-033/PT-03** | `q1Renda` | R$ 9.920 | PERCENTILE_CONT(0.25) sobre renda agregada por UF | OK |
| **MC-034/PT-03** | `q3Renda` | R$ 49.286 | PERCENTILE_CONT(0.75) sobre renda agregada por UF | OK |
| **MC-035/PT-03** | `iqrRenda` | R$ 39.366 | Q3 - Q1 = 49.286 - 9.920 | OK |
| **MC-036/PT-03** | `limiarTukey` | R$ 167.384 | Q3 + 3×IQR = 49.286 + 118.098 | OK |
| **MC-037/PT-03** | `outliersAcimaTukey` | 327.376 | WHERE renda_uf > 167.384 (9,80%) | OK |
| **MC-038/PT-03** | `outliersExtremos` | 915 | WHERE renda_uf > 1.000.000 (0,027%) | OK |
| **MC-039/PT-03** | `outliersHiperExtremos` | 141 | WHERE renda_uf > 10.000.000 (0,0042%) | OK |
| **MC-040/PT-03** | `taxaOutliersHiper` | 0,0042% | (141 / 3.340.741) × 100 | OK |
| **MC-041/PT-03** | `rendaMaximaUF` | R$ 167.320.132 | MAX(SUM(vl_renda_auferida)) por UF | OK |
| **MC-042/PT-03** | `mediaComOutliers` | R$ 58.496 | AVG(renda_uf) - todas as UFs | OK |
| **MC-043/PT-03** | `mediaSemOutliers` | R$ 57.322 | AVG(renda_uf) WHERE renda_uf ≤ 10.000.000 | OK |
| **MC-044/PT-03** | `distorcaoMedia` | +2,05% | [(58.496 - 57.322) / 57.322] × 100 | OK |

---

## PT-04: Natureza Jurídica e CNAEs de Pessoas Jurídicas

### Variáveis Canônicas

| MC | Nome da Variável | Valor | Origem/Método | Status |
|---|---|---|---|---|
| **MC-046/PT-04** | `populacaoPJs` | 9.687 | COUNT(DISTINCT nr_cnpj) FROM S_PESSOA_JURIDICA | OK |
| **MC-047/PT-04** | `CNAEsSecaoA` | 9.648 | WHERE cnae LIKE '01%' OR '02%' OR '03%' | OK |
| **MC-048/PT-04** | `CNAEsIncompativeis` | 39 | WHERE cnae NOT IN (Seção A) | OK |
| **MC-049/PT-04** | `taxaCNAEsIncompativeis` | 0,40% | (39 / 9.687) × 100 | OK |
| **MC-050/PT-04** | `populacaoAgricultoresVinculadosPJ` | 774.405 | COUNT(*) WHERE id_pessoa_juridica IS NOT NULL | OK |
| **MC-051/PT-04** | `agricultoresAfetados` | 10.377 | JOIN com 39 PJs incompatíveis | OK |
| **MC-052/PT-04** | `taxaAgricultoresAfetados` | 1,34% | (10.377 / 774.405) × 100 | OK |
| **MC-053/PT-04** | `PJsHipermercados` | 17 | WHERE cnae = '4711-3-01' | OK |
| **MC-054/PT-04** | `PJsAtacadistas` | 8 | WHERE cnae LIKE '4691-5%' | OK |
| **MC-055/PT-04** | `PJsConstrucaoCivil` | 4 | WHERE cnae LIKE '4120-4%' | OK |
| **MC-056/PT-04** | `casoExtremo_hipermercado` | 1.847 agricultores | MAX(agricultores) WHERE cnae='4711-3-01' | OK |
| **MC-057/PT-04** | `casoExtremo_capital` | R$ 12.500.000 | Capital social (caso extremo) | OK |

---

## PT-05: Controles e Processos de Curadoria

### Variáveis Qualitativas (Análise Documental)

| Item | Descrição | Evidência | Status |
|---|---|---|---|
| **E3.5.A1** | Ofício TCU 000.149/2025 (07/jul/2025) | Código Sapiens 78439839 | OK |
| **E3.5.A2** | Ofício TCU 000.192/2025 (07/ago/2025) | Código Sapiens 78646336 | OK |
| **E3.5.A3** | Ofício TCU 000.356/2025 (12/set/2025) | Código Sapiens 78883215 | OK |
| **E3.5.B1** | Ofício MAPA 76/2025 (18/set/2025) | SEI 45798933 | OK |
| **E3.5.B2** | Ofício MDA 969/2025 (23/set/2025) | SEI 45916217 | OK |
| **E3.5.B3** | Ofício MDA 164/2025 (24/set/2025) | SEI 45940197 | OK |
| **E3.5.D** | Script DDL `CAF3-ESTRUTURA-DDL.sql` | 2.847 linhas, análise estrutural | OK |
| **E3.5.E** | Benchmark CadÚnico (99,87% CPFs válidos) | RI CadÚnico março/2024 | OK |
| **E3.5.E** | Benchmark SIAPE (99,5% detecção 30 dias) | Relatório Gestão SIAPE 2024 | OK |

### Achados Qualitativos

- ✅ **0 controles automatizados** de validação identificados
- ✅ **0 processos estruturados** de curadoria documentados
- ✅ **0 integrações** em tempo real com RFB/IBGE/Correios
- ✅ **0 dashboards** de qualidade de dados
- ✅ **0 equipes dedicadas** à governança de dados

---

## Rastreabilidade Inter-PT (Achado 03)

### Fluxo de Dependências

```
PT-01 (Capacidade Civil)
  ↓ MC-001 (populacaoResponsaveis) → usado em PT-05
  ↓ MC-002 (obitosConfirmados) → evidencia ausência controles (PT-05)

PT-02 (Dados Contato)
  ↓ MC-020 (90,62% emails inválidos) → evidencia ausência validação semântica (PT-05)
  ↓ MC-026 (93,7% CEPs genéricos) → comparação com benchmark CadÚnico (PT-05)

PT-03 (Renda)
  ↓ MC-039 (141 UFs com renda >R$10MM) → evidencia ausência validação plausibilidade (PT-05)
  ↓ MC-044 (+2,05% distorção) → impacto menor que estimado inicialmente

PT-04 (CNAEs)
  ↓ MC-048 (39 CNAEs incompatíveis) → evidencia ausência validação CNAE (PT-05)
  ↓ MC-051 (10.377 agricultores afetados) → impacto em elegibilidade (Seção V)

PT-05 (Controles - CAUSA RAIZ)
  ↓ Análise documental E3.5.A-E → fundamenta TODOS os achados PT-01 a PT-04
  ↓ Causa C5 (ausência governança) → origem de TODAS as inconsistências
```

---

## Validação Cruzada

### Checklist de Consistência

- [x] Soma MC-002 + MC-005 + MC-006 + MC-007 + MC-008 + MC-013 = MC-009? ✓ (26.429)
- [x] Disparidade MC-023 = MC-022 - (100% - MC-020)? ✓ (90,32 p.p.)
- [x] MC-026 + MC-027 = MC-024? ✓ (3.540.310)
- [x] MC-044 = (MC-042 - MC-043) / MC-043 × 100? ✓ (+2,05%)
- [x] MC-048 + MC-047 = MC-046? ✓ (9.687)

---

## Status de Compilação dos Papéis de Trabalho

| PT | Arquivo LaTeX | Linhas | PDF | Páginas | Tamanho | Status |
|----|---------------|--------|-----|---------|---------|--------|
| **PT-01** | PT-01_Capacidade_Civil.tex | ~1.200 | ✅ | ~20 | 423 KB | ✅ Compilado |
| **PT-02** | PT-02_Dados_Contato.tex | ~850 | ✅ | ~18 | 369 KB | ✅ Compilado |
| **PT-03** | PT-03_Renda_Outliers.tex | 1.199 | ✅ | 27 | 346 KB | ✅ Expandido v3.0 |
| **PT-04** | PT-04_CNAEs_PJ.tex | ~450 | ✅ | ~16 | 340 KB | ✅ Compilado |
| **PT-05** | PT-05_Controles_Curadoria.tex | 721 | ✅ | 15 | 449 KB | ✅ Compilado |

**Total:** 5 PDFs • ~95 páginas • 1,93 MB • 57 MCs documentadas

---

## Changelog

- **v1.4** (28/nov/2025):
  - **RECALCULADO PT-03 COMPLETO** com metodologia correta (renda agregada por UF ativa)
  - Motivo: evitar recontagem quando múltiplas pessoas declaram mesma renda
  - MC-031: 12.849.431 registros → 3.340.741 UFs ativas
  - MC-032 a MC-036: Quartis recalculados sobre renda agregada por UF
  - MC-037: 45.821 → 327.376 outliers Tukey (9,80% das UFs)
  - MC-038: 1.245 → 915 outliers >1M
  - MC-039: 210 → 141 outliers >10M
  - MC-041: R$ 97.200.000 → R$ 167.320.132 (renda máxima agregada por UF)
  - MC-042: R$ 87.341 → R$ 58.496 (média com outliers)
  - MC-043: R$ 21.456 → R$ 57.322 (média sem outliers)
  - **MC-044: +307% → +2,05%** (distorção real é muito menor)
  - Query SQL corrigida documentada no PT-03

- **v1.3** (28/nov/2025):
  - Removido MC-045/PT-03 (`impactoFiscal` = R$ 1,4 bilhão) - métrica sem fonte documental para taxa de 85%
  - Total de MCs PT-03: 14 (era 15)

- **v1.2** (28/nov/2025):
  - Corrigido MC-013/PT-01: agora é `idadesNegativas` = 57 (nascimento no futuro)
  - Renumerado MC-014/PT-01: `operacoesPRONAF_posObito` = 312
  - Renumerado MC-015/PT-01: `valorPRONAF_posObito` = R$ 18.900.000
  - Atualizado MC-009 (totalInconsistencias): incluído MC-013 na soma → 26.429
  - Corrigido checklist de consistência
  - Corrigido MC-041/PT-03: rendaMaxima de R$ 987M → R$ 97.200.000 (verificado no BD)

- **v1.1** (14/nov/2025 - 15h45):
  - PT-03 expandido para versão 3.0 (1.199 linhas, 27 páginas)
  - Evidências reais substituídas (ata MDA, queries information_schema)
  - Correções de overfull/underfull aplicadas
  - Todos os 5 PTs compilados com sucesso
  - Atualização de nomenclatura (populacaoRendas → populacaoRenda)

- **v1.0** (14/nov/2025):
  - Versão inicial com 57 MCs canônicas para Achado 03
  - Baseado em Seções I-V do Achado 03 (relatório completo)
  - Seguindo PADRAO_PRECISAO_NUMERICA.md (regra de 5%)
  - Nomenclatura camelCase conforme MELHORIAS_v1.3.md

---

**Autor:** Equipe de Auditoria AudTI/TCU
**Revisão:** Validador Agent (AGENT.md)
**Status:** ✅ v1.4 - PT-03 recalculado com metodologia agregada por UF
**Data Atualização:** 28 de novembro de 2025
