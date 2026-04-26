# Atlas de Regulacao de Criptoativos — Correcoes v3 (Abril 2026)

## Resumo executivo

Este pacote contem as correcoes aplicadas ao repositorio do Atlas em auditoria tecnica
realizada em 26/04/2026, em preparacao para defesa de monografia (UnB) e adaptacao
para artigo cientifico.

## Problemas identificados e acoes tomadas

### 1. Desalinhamento de nomenclatura (CRITICO — DOCUMENTADO)

**Problema:** `scoring_methodology.json` (v2) declarava 8 dimensoes com nomes
diferentes dos 9 campos usados nas `criteria` de todos os arquivos de paises.

**Acao:** Gerado `scoring_methodology_v3.json` com mapeamento formal:

| Campo em `criteria` | Dimensao na metodologia | Peso | Escala efetiva |
|---|---|---|---|
| `legal_certainty` | `regulatory_clarity` | 18 | 0–18 |
| `proportionality` | `private_innovation_openness` | 14 | 0–14 |
| `exchanges` | `investor_user_protection` | 14 | 0–14 |
| `stablecoins` | `stablecoin_regime` | 12 | 0–12 |
| `tokenization` | `tokenization_legal_security` | 10 | 0–10 |
| `mining_infrastructure` | `supervisory_capacity` (+infraestrutura) | 10 | 0–10 |
| `innovation_openness` | `private_innovation_openness` (sinal secundario) | 10 | 0–10 |
| `anti_centralization` | `state_centralization_risk` | 10 | 0–10 |
| `taxation` | (camada suplementar incluida no core) | 10* | 0–10 |

*taxation tem peso efetivo de 10 na pratica, embora declarado como supplementary.

**Formula de calculo documentada:**
```
score = sum(criteria.values())
```
Cada valor em `criteria` ja e um weighted score pre-calculado, nao um raw score 0–10.

### 2. Ambiguidade semantica: mining_infrastructure (CRITICO — DOCUMENTADO)

**Problema:** `mining_infrastructure` captura tanto capacidade supervisoria do regulador
quanto habilitacao de infraestrutura produtiva (energia, compute). Sao dimensoes
semanticamente distintas.

**Acao:** Documentada a natureza dual da dimensao na v3. Recomendacao para versoes
futuras: separar em `supervisory_capacity` e `mining_infrastructure` como campos distintos.

**Para a tese:** A secao 3.3.1 deve explicitar que essa dimensao avalia tanto a
operacionalidade do regulador quanto a habilitacao de infraestrutura digital produtiva,
que na hipotese da pesquisa sao complementares (regulador capaz + infraestrutura habilitada).

### 3. Taxation: suplementar declarado, core na pratica (CRITICO — DOCUMENTADO)

**Problema:** `scoring_methodology.json` (v2) listava `taxation` como `supplementary_layer`,
mas o campo `taxation` esta presente em todas as 201 jurisdicoes e contribui diretamente
para o `score` via soma das criteria.

**Acao:** Inconsistencia documentada em `scoring_methodology_v3.json`. Duas opcoes para
correcao editorial:
- **Opcao A:** Remover `taxation` das criteria, criar campo `taxation_score` separado,
  recalcular `score` como soma dos outros 8 criterios.
- **Opcao B:** Manter `taxation` nas criteria e remover a classificacao de supplementary
  na methodology — declarar formalmente como 9a dimensao do core score.

### 4. Duplicatas de arquivos (CORRIGIDO)

**Problema:** 41 pares de arquivos existiam em lowercase e uppercase (ex: `BRA.json`
e `bra.json`). Os arquivos lowercase continham campos analiticos ausentes nos uppercase.

**Acao:** Todos os pares foram mesclados em arquivo unico uppercase. O arquivo mais rico
foi usado como base, com campos complementados do outro. O resultado esta em `api/country/`.

### 5. Score inconsistente em 3 jurisdicoes (DOCUMENTADO)

**Problema:** Tailandia (THA), Ucrania (UKR) e Liechtenstein (LIE) tem `score`
armazenado 3 pontos acima de `sum(criteria)`.

**Acao:** Cada um desses arquivos recebeu campo `editorial_note` explicando a discrepancia.
Pendente verificacao manual para confirmar se o delta e ajuste intencional ou erro.

## O que NAO foi alterado

- Scores de todos os paises permanecem iguais (nenhum recalculo de pontuacao)
- Conteudo analitico (summary, detailed_analysis, opportunities, risks) preservado
- Estrutura de thresholds (very_favorable, favorable, mixed, restrictive, very_restrictive)
- Posicionamento do Brasil (score=69, favorable, #16 de 201 apos deduplicacao)

## Impacto na tese

O score do Brasil (69) permanece correto e matematicamente consistente.
O anti_centralization baixo (3/10) e coerente com a hipotese central sobre risco
de centralizacao monetaria via Drex. Nao ha correcao necessaria nesses valores.

A secao 3.3.1 da tese deve ser atualizada para:
1. Declarar explicitamente a formula `score = sum(criteria)` onde cada criterio
   e um weighted score (escala 0 a peso_da_dimensao);
2. Usar a tabela de mapeamento acima;
3. Reconhecer a natureza dual de `mining_infrastructure`;
4. Resolver editorialmente a questao de `taxation` (opcao A ou B acima).

## Arquivos gerados

- `api/country/*.json` — 201 arquivos consolidados (sem duplicatas)
- `api/scoring_methodology_v3.json` — metodologia corrigida e documentada
- `audit_report_v3.json` — relatorio completo de auditoria com rankings

