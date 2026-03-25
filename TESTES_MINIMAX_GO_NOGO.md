# Testes MiniMax GO/NO-GO

# Análise GO/NO-GO — Indexador Híbrido de Auditoria

---

## 1. Padrões de Falha Não Identificados

**Padrão 1: Assimetria de recall numérico vs. semântico**

Os 14 números-chave que falham não são aleatórios. Observe o padrão:

| Categoria | Taxa de Falha | Possível Causa Raiz |
|-----------|---------------|---------------------|
| Métricas percentuais (68.7%, 45.92%, 90.62%, 92.36%) | 4/4 falhou | Chunking quebra contexto numérico |
| Quantidades absolutas (632, 138, 646, 742mil) | 4/4 falhou | FAISS não rankeia bem números isolados |
| Códigos/categorias (e-mails, CNAE, Leaflet) | 4/4 falhou | Caracteres especiais ignorados no BM25 |

**Isso não é um bug — é uma limitação estrutural do chunking.** Os chunks provavelmente cortam o contexto e não preservam que "632 municípios" está no mesmo contexto que o restante da afirmação.

**Padrão 2: Cross-battery contamination**

A falha de task_type (doc/query idênticos no teste controlado) provavelmente contamina parte dos resultados densos de B2.

**Padrão 3: Omissão de teste**

Nenhum teste valida se o sistema sabe que não sabe. Não há validação robusta de "não encontrado" versus "resultado plausível mas errado".

---

## 2. A taxa de aprovação é confiável?

**Não. Três vieses graves:**

**Viés 1: B3 inflou a média**

17/17 em peça específica mede rastreabilidade, não qualidade semântica do ranking para revisão factual ampla.

**Viés 2: Tests de rastreabilidade vs. accuracy**

B3+B6 passam muito bem, mas não resolvem a integridade numérica de B2.

**Viés 3: Validação interna vs. ground truth externo**

Os testes refletem o conhecimento prévio do conjunto, o que é bom para debug mas não suficiente como validação de produção autônoma.

**Estimativa do parecer:** a taxa real de sucesso em produção parece mais próxima de 55-60% do que de 72,7%.

---

## 3. Probabilidade de funcionar 4 horas sem supervisão

**15-25%.**

Razões:
- 36,4% de sucesso em integridade numérica significa falha em muitos números centrais.
- Um relatório de auditoria com números faltando ou errados é pior que não ter relatório.
- A falha no contraditório é particularmente perigosa para revisão sem supervisão.

---

## 4. A ÚNICA coisa que eu mudaria antes de dar GO

**Adicionar um passo de extração numérica pós-recuperação.**

Fluxo sugerido:
1. Receber top-20 chunks do pipeline atual.
2. Fazer regex dos padrões numéricos relevantes.
3. Cruzar com a lista de números-chave conhecidos.
4. Se o número-chave estiver num chunk fora do top-5, aplicar override auditável no ranking.
5. Registrar `boost_numerico=true` em log.

O motivo: corrige o maior gargalo sem desmontar o que já funciona bem em rastreabilidade e busca cruzada.

---

## 5. Decisão Final

## NO-GO

### Justificativa

**1.** A taxa de 72,7% é ilusória porque uma parcela grande dos testes mede rastreabilidade, não confiabilidade factual.

**2.** A falha de 63,6% em integridade numérica é crítica para o caso de uso: 14 números-chave essenciais não aparecem com prioridade suficiente.

**3.** Rodar 4 horas sem supervisão amplifica o risco de produzir um relatório aparentemente sólido, mas com suporte factual incompleto ou incorreto.

### Ação mínima para reconsiderar GO

Implementar o passo de extração numérica, rerodar pelo menos a bateria 2 e exigir algo próximo de 15/22 antes de liberar a revisão noturna.
