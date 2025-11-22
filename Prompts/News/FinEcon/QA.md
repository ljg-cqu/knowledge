# Financial & Economic News Intelligence Q&A Generator

## Table of Contents
- [I. Context & Scope](#i-context--scope)
- [II. Requirements](#ii-requirements)
- [III. Execution](#iii-execution)
- [IV. Validation](#iv-validation)
- [V. Question Quality](#v-question-quality)
- [VI. Output Format](#vi-output-format)

## I. Context & Scope

**Problem**: Finance leadership ($100M+ revenue, $50M+ finance decisions) needs decision-critical insights from fragmented financial/economic news for capital allocation and risk decisions.

**Scope**: Generate 4-6 Q&As from financial/economic news (capital structure, liquidity, M&A, risk/compliance) for CFO, VP Finance, Treasurer, Corp Dev, FP&A. Bi-weekly | Valid 2wk | Scannable ≤30min | 2-4h/cycle. **Horizon**: 1-6mo (exclude <1mo tactical, >6mo speculation). **Freshness**: <2mo preferred, <4mo acceptable, ≤9mo max (high-velocity topics require <2mo).

**Criticality Criteria** (≥1 required): Impacts capital allocation/structure/M&A/liquidity OR creates material risk (financial stability, compliance, cash flow) with 1-6mo action AND quantified impact (WACC%, $, multiples, IRR).

**Decision Cycles** (≥3 of 4): Capital Allocation (investment, project prioritization, capex/opex) | Liquidity/Cash (working capital, runway, debt servicing) | M&A/Corp Dev (acquisitions, divestitures, partnerships) | Risk/Compliance (regulatory, FX/interest rate risk, controls).

**News Categories** (≥3 of 4): Capital Markets/Rates (rate changes, equity valuations, credit spreads) | Macro Trends (GDP/CPI/unemployment, recession signals, sector shifts) | M&A/Corp Dev (transactions, valuations) | Treasury/FX (currency volatility, liquidity stress, refinancing).

**Exclude**: Operations, product strategy, fundraising, rumors, educational content.

## II. Requirements

**Output**: 4-6 Q&As (150-200w each) | ≥3 decision cycles + ≥3 news categories | ≥6 references (prioritize news; include M&A/treasury/research) | ≥2 Mermaid diagrams + ≥1 table.

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD). Search ≥10 candidates from Fed/ECB, WSJ, Bloomberg, FT, Reuters (markets), BLS/BEA (macro), MergerMarket (M&A), research. Avoid rumors/PR. Select 4-6 meeting criticality, ranked by: (1) quantified impact, (2) urgency, (3) multi-cycle effects.

### Step 2: Build References

**Format**: G# (term, definition) | N# (news, source, date, URL) | M# (M&A, date, URL) | T# (treasury, date, URL) | R# (research, author, year, URL). **Citations**: `[Ref: N1][n1]` in text, `[n1]: [Source] (YYYY-MM-DD) URL` at end. Verify figures; label estimates ("est.", "proj.", "assumes X"). Research 2023+. Define non-core terms in glossary.

### Step 3: Generate Q&A

**Question**: "[Specific News] implications for [Cycle]?". **Structure** (150-200w): News (~30w: what, when, why [Ref: N#][n#]) | Impact (~60w: ≥2 cycles + quantified metrics - %, $, multiple, IRR, bps - with explicit causal links "X causes Y because Z") | Stakeholders (~40w: Primary/Secondary with concerns → actions) | Decision (~50w: Recommended option - benefits/costs/risks/criteria, Alternative option - benefits/costs/risks) | Action (~20w: Critical 0-2wk [Step - Owner], Important 2wk-2mo [Step - Owner]) | Links: [n#]: [Source] (YYYY-MM-DD) URL.

### Step 4: Add Visuals (Inline Placement)

**Principle**: Embed visuals immediately after relevant text to avoid reader navigation.

**Placement Logic**:
- **Decision comparisons**: Table directly after Decision text showing options/costs/benefits
- **WACC/DCF flows**: Diagram after Impact section explaining capital structure
- **Timeline scenarios**: Sequence diagram inline with timeline-dependent decisions
- **Impact summaries**: Table after Impact section with cycle/metric breakdowns

**Minimum**: ≥2 diagrams (Mermaid: flowcharts for decision trees/WACC/DCF, sequence diagrams for timelines, scenario comparisons) + ≥1 table, all placed inline within Q&A sections (not grouped separately)

### Step 5: Self-Review

Verify calculations (WACC%, IRR, multiples), citations (dates, URLs, recency), logic (no contradictions), completeness (News/Impact/Stakeholders/Decision/Action), uncertainties flagged ("est.", "proj.", "assumes X").

## IV. Validation

| Check | Criteria | Target | Status |
|-------|----------|--------|--------|
| **Freshness** | News recency | ≥50% <2mo, all ≤9mo | PASS/FAIL |
| **Coverage** | Cycles + Categories | ≥3 cycles, ≥3 categories | PASS/FAIL |
| **Output** | Q&A count | 4-6 Q&As | PASS/FAIL |
| **Per Q&A** | Content | 150-200w, ≥1 citation, ≥2 roles, ≥2 alternatives+action | PASS/FAIL |
| **References** | Total citations | ≥6 (news prioritized) | PASS/FAIL |
| **Visuals** | Diagrams + Tables | ≥2 diagrams (Mermaid), ≥1 table | PASS/FAIL |
| **Meta** | Generation/Expiry | Start: [YYYY-MM-DD], Expires: [+2wk] | INFO |

## V. Question Quality

**Good** (news-driven, decision-critical, quantified):
- "Fed 50bps cut (Sept 2024): refinancing implications?"
- "USD/EUR volatility +15% (Q4 2024): hedging strategy?"
- "Salesforce/Slack $27.7B (12x revenue): valuation benchmark?"

**Bad**:
- "How does WACC work?" (educational)
- "Should we raise debt?" (no trigger)
- "Fed rate decision" (no quantification)

## VI. Output Format

### Document Structure

```markdown
# Financial & Economic Intelligence Q&A ([Period])

**Generated**: [YYYY-MM-DD] | **Expires**: [YYYY-MM-DD] | **Scan**: ≤30min

## Executive Summary
**Coverage**: [X] Q&As | [Y] cycles | [Z] categories

**Key Insights**:
1. **Critical**: [Decision] by [Timeline] - [Owner]
2. **Important**: [Decision] by [Timeline] - [Owner]
3. **Notable**: [Decision] by [Timeline] - [Owner]

**Action Dashboard**:
| Cycle | News | Decision | Critical Action | Owner | Deadline |
|-------|------|----------|-----------------|-------|----------|

## Questions by Cycle
[Group by: Capital Allocation | Liquidity/Cash | M&A/Corp Dev | Risk/Compliance]

## References
**Glossary**: G#: Term - Definition
**News**: N#: Source (YYYY-MM-DD) URL
**M&A**: M#: Deal (YYYY-MM-DD) URL
**Treasury**: T#: Instrument (YYYY-MM-DD) URL
**Research**: R#: Author (Year) URL

## Validation
[Table from Section IV with actual PASS/FAIL]
```

### Q&A Structure

```markdown
### Q#: [News Event] implications for [Cycle]?

**Cycle**: [Capital Allocation/Liquidity/M&A/Risk] | **Roles**: [Primary, Secondary] | **Criticality**: [#]

**News** (~25w): [What, when, why] [Ref: N#][n#]

**Impact** (~50w): 
- **[Cycle 1]**: [Quantified change] because [mechanism]
- **[Cycle 2]**: [Quantified change] because [mechanism]

| Cycle | Metric | Current | Target | Change | Mechanism |
|-------|--------|---------|--------|--------|-----------|
| [Optional: Impact summary table if ≥3 cycles affected] | | | | | |

```mermaid
[Optional: WACC/DCF flow diagram if explaining capital structure impact]
graph LR
A[Rate Change] --> B[WACC Impact] --> C[NPV Effect]
```

**Stakeholders** (~35w): 
- **[Primary]**: [Concerns] → [Actions]
- **[Secondary]**: [Concerns] → [Actions]

**Decision** (~50w): 
- **Recommended**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z], Criteria: [When]
- **Alternative**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z]

| Option | Cost | Benefit | Risk | Criteria | Timeline |
|--------|------|---------|------|----------|----------|
| Recommended | [$] | [metric] | [prob/impact] | [when] | [Xmo] |
| Alternative | [$] | [metric] | [prob/impact] | [when] | [Xmo] |

**Action** (~20w): 
- **Critical (0-2wk)**: [Step] - [Owner]
- **Important (2wk-2mo)**: [Step] - [Owner]

```mermaid
[Optional: Timeline sequence if showing phased actions]
sequenceDiagram
Note over Owner: Critical Actions (0-2wk)
Note over Owner: Important Actions (2wk-2mo)
```

[n1]: [Source] (YYYY-MM-DD) URL
---
```
