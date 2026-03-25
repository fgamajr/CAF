# 04_PECAS_EVIDENCIA

**Evidências organizadas por achado. Fonte de fatos para narrativa em 01_RELATORIO_V2.**

## Propósito

Contém todas as peças de evidência física e análise, organizadas por tipo de achado. Use para fundamentar narrativa, extrair citações e validar conclusões.

## Estrutura de Subpastas

### Por Achado
| Subfolder | PEÇAS | Descrição |
|-----------|-------|-----------|
| ACH01_documental | 103-109, 140 | Qualidade estrutural: perfil de campos, preenchimento, validação |
| ACH02_geoespacial | 110-122 | Consistência espacial: geocodificação, limites administrativos |
| ACH03_cadastral | 123-132 | Integridade: duplicatas, relacionamentos, histórico |
| ACH04_metadados | 133-136 | Qualidade de metadados: documentação, rastreabilidade |

### Evidências Transversais
- **Subpasta**: TRANSVERSAIS
- **PEÇAS**: 75-86, 108, 137-139 (servem múltiplos achados)
- **Uso**: Consulte quando evidência é citada por mais de um achado

### Texto Extraído
- **Subpasta**: txt_extraido/
- **Conteúdo**: Texto raw extraído de PDFs (OCR/parsing)
- **Uso**: Busca de palavras-chave, análise de conteúdo

## Tabela PEÇA → ACHADO → CONTEÚDO

```
PEÇA 75-86   → Transversais
PEÇA 103-109 → ACH01 (documental)
PEÇA 108     → ACH01 + Transversais
PEÇA 110-122 → ACH02 (geoespacial)
PEÇA 123-132 → ACH03 (cadastral)
PEÇA 133-136 → ACH04 (metadados)
PEÇA 137-139 → Transversais
PEÇA 140     → ACH01 (documental)
```

## Como Usar

### Para Redatores
1. Identifique achado (ACH01-04) em que está trabalhando
2. Navegue para subfolder correspondente
3. Extraia fatos, números, exemplos para suportar narrativa
4. Cite PEÇA e página ao referenciar

### Para Validadores
1. Leia seção em `01_RELATORIO_V2/`
2. Rastreie cada citação para respectiva PEÇA em subpastas
3. Verifique acurácia e contexto original

## Aviso

Peças transversais (75-86, 108, 137-139) podem ser citadas por múltiplos achados. Verifique contexto completo antes de usar.
