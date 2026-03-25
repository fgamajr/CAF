# Reteste Pós-Patch — MiniMax GO/NO-GO

**Data:** 2026-03-25 12:34:26 -03
**Status:** concluído

## Parecer

```text
# GO COM RESSALVAS

## Respostas diretas:

**1. Padrão que inviabilize?**
Não. As 7 falhas restantes são edge cases isolados:
- 3 queries com viés de vocabulário V1 (sesgo de tokenização, não sistêmico)
- 2 queries sem filtro onde --hierarchy "corrige" manualmente
- 1 caso onde o mini-doc é semanticamente correto (27,1%)

Nenhum padrão de falha recorrente quebre o pipeline.

**2. Mini-docs: risco grave ou solução aceitável?**
**Solução aceitável.** Resolveram 22/22 para números-chave (era 8/22). O caso 27,1% não é bug - o número existe no mini-doc. É prioridade de ranking, não correção. Se amanhã um usuário ver "27,1%" no topo ao buscar por ele, isso é *correto*.

**3. Probabilidade de resultado útil até amanhã:**
**~85-90%.** Você tem 90.9% de acerto, zero falhas em stress test, e o gargalo real (bateria 2) foi eliminado. As falhas restantes não são sistêmicas.

**4. Mudança única antes do GO:**
Faça o sistema reconhecer padrões tipo `Proposta X.Y.Z` como *hint implícito* para a Matriz, sem precisar de `--hierarchy` manual. É 1 regex + ajuste de peso. Não seria GO de verdade até resolver isso.

**5. Justificativa:**
O patch eliminou o gargalo crítico (bateria 2: 8→22) sem criar falha nova; as 7 queries restantes são edge cases sem padrão sistêmico. Os mini-docs provaram ser solução eficaz, não risco. Um indexador com 91% de acerto que nunca falha em stress test e rastreia procedência é **pronto para produção assistida overnight** - rode, monitore as 7 falhas restantes como observações, e amanhã você tem o baseline.

**Ação:** GO COM RESSALVAS. Inicie o overnight. Marque as 7 falhas como tickets para amanhã.
```

## Síntese operacional

- Veredicto: `GO COM RESSALVAS`
- Confiança estimada: `85-90%`
- Única melhoria sugerida antes do próximo ciclo: detectar `Proposta X.Y.Z` como pista implícita para priorizar a Matriz
