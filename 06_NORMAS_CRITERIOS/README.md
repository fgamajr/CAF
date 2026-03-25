# 06_NORMAS_CRITERIOS

**Referencial normativo e técnico. Legislação, normas ISO, e diretrizes TCU para fundamentação.**

## Propósito

Contém toda a base legal, técnica e metodológica necessária para fundamentar achados. Consulte para validar critérios de auditoria, definições técnicas e fundamentação jurídica.

## Subpastas e Conteúdo

### legislacao/
Marcos legais que definem escopo e autoridade:

| Documento | Ano | Relevância |
|-----------|-----|-----------|
| Lei 11326/2006 | 2006 | Cadastro de Agricultura Familiar - Lei que institui CAF |
| Decreto 9064/2017 | 2017 | Regulamenta Lei 11326 - procedimentos de cadastro |
| Portaria MDA 19/2025 | 2025 | Regulação atual de qualidade de dados CAF |

### iso_referenciais/
Normas técnicas internacionais de qualidade de dados:

| Norma | Foco |
|-------|------|
| ISO 25012 | Data Quality - modelo de qualidade de dados |
| ISO 19157 | Geographic Data Quality - qualidade de dados geoespaciais |
| ISO 11179 | Data Element Metadata - padrão de metadados |
| ISO 8000 | Master Data Quality - integridade e relacionamentos |
| DAMA-DMBOK | Data Management Body of Knowledge - framework prático |

### nat_tcu/
Diretrizes TCU de auditoria operacional:

| Material | Tipo |
|----------|------|
| Manual de Auditoria Operacional | Framework metodológico |
| Checklist NAT | Verificações padrão |
| Termos Oficiais TCU | Glossário de conceitos |
| Manual de Redação TCU | Padrão de escrita normativa |

## Como Usar

### Para Fundamentação de Achados
1. Identifique critério técnico (ex: duplicatas, geocodificação)
2. Consulte ISO correspondente (DAMA-DMBOK para conceito geral)
3. Verifique Lei 11326/2006 e Decretos para autoridade jurídica
4. Use Portaria MDA 19/2025 para regulação atual
5. Cite em narrativa: "conforme ISO 25012, ponto X.Y"

### Para Validação Redacional
1. Leia seção candidata em `01_RELATORIO_V2/`
2. Verifique se critérios estão fundamentados em docs desta pasta
3. Confirme alinhamento com Manual de Redação TCU
4. Valide uso correto de termos oficiais

## Citação Padrão

```
Conforme ISO 25012 (Data Quality Model), item 4.2...
Respaldado por Lei 11326/2006, artigo X...
Conforme Manual de Auditoria Operacional do TCU, página Y...
```

## Aviso

Normas técnicas podem ter intepretações diferentes. Se houver conflito técnico entre duas normas, **PECA170 (Matriz de Achados)** é autoridade final.
