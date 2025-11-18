# Financial & Economic News Intelligence Q&A Generator

Generate 4–6 decision-critical Q&As from recent financial/economic news to support capital allocation and risk decisions for finance leadership.

## Table of Contents
- [I. Context & Scope](#i-context--scope)
- [II. Requirements](#ii-requirements)
- [III. Execution](#iii-execution)
- [IV. Validation](#iv-validation)
- [V. Question Quality](#v-question-quality)
- [VI. Output Format](#vi-output-format)

## I. Context & Scope

- **Cadence**: Bi-weekly; valid 2 weeks (state generation/expiry dates)
- **Domain**: Financial/economic news affecting capital structure, liquidity, M&A, risk/compliance
- **Audience**: CFO, VP Finance, Treasurer, Corp Dev, FP&A (assumes core finance literacy)
- **Horizon**: 1–6 month decisions; exclude intraday moves and long-term speculation
- **Format**: Scannable in ≤30 minutes

**Freshness**: Prioritize recent news (<2mo preferred, <4mo acceptable, ≤9mo maximum). High-velocity topics (capital markets, macro) require fresher sources than medium-velocity (M&A, treasury).

**Decision Criticality** (each Q must meet ≥1):
1. Impacts capital allocation, capital structure, M&A execution, or liquidity
2. Creates material risk to financial stability, compliance, or cash flow
3. Affects ≥2 stakeholder roles
4. Requires near-term action (1-6mo)
5. Has quantified impact (WACC%, $amounts, multiples, IRR)

**Categories** (cover ≥3):
1. **Capital Markets/Rates**: Rate changes, equity valuations, credit spreads
2. **Macro Trends**: GDP/CPI/unemployment, recession signals, sector shifts
3. **M&A/Corp Dev**: Transactions, valuations, strategic implications
4. **Treasury/FX**: Currency volatility, liquidity stress, debt refinancing

**Exclude**: Operations, product strategy, early-stage fundraising, rumors, educational content.

## II. Requirements

**Output**: 4-6 Q&As covering ≥3 decision cycles (Capital Allocation, Liquidity/Cash, M&A/Corp Dev, Risk/Compliance)

**Per Q&A**: 120-200 words | ≥1 news citation | Quantified impact | ≥2 stakeholder roles | Decision recommendation

**References**: ≥6 total (prioritize news sources; include M&A deals, treasury instruments, research as relevant)

**Visuals**: ≥2 diagrams + ≥1 table

## III. Execution

### Step 1: News Discovery
Record generation date (YYYY-MM-DD). Search ≥10 candidates prioritizing recent news (1-14d preferred).

**Sources**: Fed/ECB, WSJ, Bloomberg, FT, Reuters (markets); BLS/BEA (macro); MergerMarket (M&A); research reports. Avoid rumors/PR.

**Curate**: Select 4-6 items meeting decision criticality, covering ≥3 cycles and ≥3 categories. Rank by impact: prioritize items with (1) quantified financial impact, (2) near-term urgency (<2mo), (3) multi-cycle effects.

### Step 2: Build References
**Format**: G# (term, definition) | N# (news, source, date, URL) | M# (M&A deal, date, URL) | T# (treasury instrument, date, URL) | R# (research, author, year, URL)

**Citations**: `[Ref: N1][n1]` in text, `[n1]: [Source] (YYYY-MM-DD) URL` at end. Verify figures against primary sources; label estimates/projections explicitly.

**Recency**: News sources <2mo (preferred), <4mo (acceptable), ≤9mo (maximum). Research/reports from 2023+.

**Glossary**: Include only terms used; plain language.

### Step 3: Generate Q&A
**Question**: "[Specific News] implications for [Cycle]?"

**Structure** (120-200 words total, ordered by priority):
1. **News** (~25w): What, when, why [Ref: N#][n#]
2. **Impact** (~50w): ≥2 cycles + quantified metrics; explicit causal links. Order: critical impacts first.
3. **Stakeholders** (~35w): ≥2 roles + concerns/actions. Order: primary decision-maker first.
4. **Decision** (~50w): Contrast ≥2 options (benefits/costs/risks); recommend with criteria. Label: **Recommended**/Alternative.
5. **Action** (~20w): **Critical** (0-2wk) + **Important** (2wk-2mo) steps + owners
6. Links: [n1]: URL

### Step 4: Add Visuals
≥2 diagrams (Mermaid flows for WACC/DCF, scenarios) + ≥1 table.

### Step 5: Self-Review
Before finalizing, verify:
- **Calculations**: Cross-check metrics (WACC%, IRR, multiples) against sources
- **Citations**: Confirm dates, source names, URLs are accurate and recent
- **Logic**: Check for contradictions between recommendations
- **Completeness**: All Q&As have News/Impact/Stakeholders/Decision/Action
- **Uncertainties**: Flag estimates, projections, or assumptions explicitly

## IV. Validation

| Check | Criteria | Status |
|-------|----------|--------|
| **Freshness** | Most <2mo, all ≤9mo | PASS/FAIL |
| **Output** | 4-6 Q&As, ≥3 cycles, ≥3 categories | PASS/FAIL |
| **Per Q&A** | 120-200w, ≥1 citation, ≥2 roles, decision+action | PASS/FAIL |
| **References** | ≥6 total | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | PASS/FAIL |
| **Meta** | Start: [Date], Expires: [+2wk] | INFO |

## V. Question Quality

**Good** (news-driven, decision-critical, quantified):
- "Fed 50bps rate cut (Sept 2024): refinancing implications?"
- "USD/EUR volatility +15% (Q4 2024): hedging strategy?"
- "Salesforce acquires Slack $27.7B (12x revenue): valuation benchmark?"

**Bad** (avoid):
- "How does WACC work?" (educational, no news)
- "Should we raise debt?" (no trigger)
- "Fed announced rate decision" (no specifics/quantification)

## VI. Output Format

### Structure
```markdown
# Financial & Economic Intelligence Q&A ([Period])

## Executive Summary
**Period**: [Dates] | **Coverage**: [# Q&As, cycles, categories]
**Key Insights**: [2-3 high-impact items with decisions/timelines]
**Dashboard**: [Table: Cycle | News | Decision | Timeline]

## Questions by Cycle
[Organized by: Capital Allocation | Liquidity/Cash | M&A/Corp Dev | Risk/Compliance]

## References
[Glossary | News | M&A | Treasury | Research]

## Validation
[Include validation table from Section IV]
```

### Q&A Template
```markdown
### Q#: [Specific News] implications for [Cycle]?

**Cycle**: [Cycle] | **Roles**: [Primary, Secondary] | **Criticality**: [Criterion met]

**News** (~25w): What, when, why [Ref: N#][n#]

**Impact** (~50w): ≥2 cycles + quantified metrics (WACC%/$/multiples/IRR); explicit causal links. Order: critical impacts first.

**Stakeholders** (~35w): **[Primary Role]**: Concerns + actions | **[Secondary Role]**: Concerns + actions

**Decision** (~50w): **Recommended**: [Option] - benefits/costs/risks + rationale | **Alternative**: [Option] - benefits/costs/risks

**Action** (~20w): **Critical (0-2wk)**: Steps + owner | **Important (2wk-2mo)**: Steps + owner

[n1]: [Source] (YYYY-MM-DD) URL
---
