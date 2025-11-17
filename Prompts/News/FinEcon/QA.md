# Financial & Economic News Intelligence Q&A Generator

Generate 4–6 decision-critical Q&As from recent financial/economic news to support capital allocation and risk decisions for finance leadership.

## I. Context & Scope

- **Cadence**: Bi-weekly; 4–6 Q&As per run; valid 2 weeks (state generation and expiry dates).
- **Domain**: Financial/economic news materially affecting capital structure, liquidity, M&A, risk/compliance.
- **Stakeholders**: CFO, VP Finance, Treasurer, Corp Dev, FP&A.
- **Horizon**: 1–6 month decision window; exclude intraday moves and >6 month speculation.
- **Reader**: Assumes core finance knowledge (WACC, IRR, NPV); no tutorials.
- **Format**: Scannable in ≤30 minutes.

**Freshness**: Prioritize recent news (≥70% <2mo, ≥85% <4mo, 100% ≤9mo). High-velocity topics (capital markets, macro) require fresher sources than medium-velocity (M&A, treasury).

**Scope**: Include only decision-critical news—rate changes, M&A deals, macro shifts, treasury/FX moves, compliance deadlines.

**Exclude**: Operations, sales, product strategy, early-stage fundraising, marketing, rumors, stale news, educational overviews.

**Decision Criticality** (each Q must meet ≥1):
1. Blocks capital allocation, debt/equity structure, M&A go/no-go, or liquidity decisions
2. Creates material risk to financial stability, compliance, credit rating, or cash flow
3. Affects ≥2 core roles
4. Requires 1-6mo action (not speculative)
5. Has quantified impact (WACC %, liquidity $, valuation multiple, tax $, cash flow $, IRR)

**Categories** (cover 3-4):
1. **Capital Markets/Rates**: Rate changes, equity valuations, credit spreads affecting WACC/refinancing
2. **Macro Trends**: GDP/CPI/unemployment, recession signals, sector trends affecting assumptions
3. **M&A/Corp Dev**: Transactions, valuations, multiples affecting strategy
4. **Treasury/FX**: Currency volatility, liquidity stress, debt refinancing affecting cash position

## II. Requirements

**Q&A Structure**: 4-6 total | 1-2 per cycle | 120-200 words | All news-driven with ≥1 citation | Category + quantified impact + decision

**Cycles** (cover 3-4): Capital Allocation, Liquidity/Cash, M&A/Corp Dev, Risk/Compliance

**Category Coverage**: Capital Markets/Rates ≥50%, Macro ≥40%, M&A ≥40%, Treasury/FX ≥25%

**Stakeholders**: Include ≥5 roles (CFO, VP Finance, Treasurer, Corp Dev, FP&A, etc.)

**References**: Glossary (terms used), News (≥4), M&A (≥2), Treasury (≥2), Research (≥2), Total (≥6)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (must pass all):
1. Decision Criticality: 100% meet ≥1 criterion
2. Citations: 100% ≥1 valid citation; 0% rumors
3. Impact: 100% cover ≥2 cycles + ≥2 roles + quantified metrics
4. Decision: 100% include decision + rationale + timeline
5. Actionability: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery

Record generation date (YYYY-MM-DD) for age calculations. Search ≥10-15 candidates prioritizing recent (1-7d, then 7-14d).

**Sources**: Fed/ECB, WSJ, Bloomberg, FT, Reuters (markets); BLS/BEA (macro); MergerMarket (M&A); McKinsey, S&P (research). Avoid rumors/PR.

**Curate**: Select items meeting freshness, decision criticality (≥1 criterion), ≥2 roles relevance. Allocate 4-6 Q&As across 3-4 cycles, 3-4 categories, ≥5 roles.

### Step 2: Build References

**Format**: G# (term, definition, analogy) | N# (news, source, date, URL) | M# (M&A, companies, valuation, URL) | T# (treasury, instrument, URL) | R# (research, findings, URL)

**Citations**: `[Ref: N1][n1]` in text, `[n1]: URL` at end. Verify figures; label estimates.

**Glossary**: Include only terms used; plain language; analogies for complex concepts.

### Step 3: Generate Q&A

**Question Pattern**: "[Specific News] implications for [Cycle]?" Avoid generic/speculative questions.

**Structure** (120-200 words):
1. **News** (~25w): What, when, why, category [Ref: N#][n#]
2. **Impact** (~50w): ≥2 cycles + quantified metrics (WACC%, liquidity$, etc.); explicit causal links
3. **Stakeholders** (~35w): ≥2 roles + concerns/actions
4. **Decision & Alternatives** (~50w): Contrast ≥2 options (benefits/costs/risks); recommend with criteria
5. **Action** (~20w): Immediate (0-2wk) + short (2wk-2mo) steps + owners
6. Links: [n1]: URL

**Self-Check**: Meets criticality/cycles/roles; 120-200 words; ≥1 citation; actionable; terms in glossary.

### Step 4: Add Visuals & Validate

≥2 diagrams (Mermaid flows for WACC/DCF, scenario analyses) + ≥1 table. Verify all references/decisions/timelines meet requirements.

## IV. Validation Report

| Check | Criteria | Status |
|-------|----------|--------|
| **Freshness** | ≥70% <2mo, ≥85% <4mo, 100% ≤9mo | PASS/FAIL |
| **References** | G (terms used), N≥4, M≥2, T≥2, R≥2, Total≥6 | PASS/FAIL |
| **Cycles** | 3-4 cycles, 1-2 Q each, total 4-6 | PASS/FAIL |
| **Categories** | Markets≥50%, Macro≥40%, M&A≥40%, Treasury≥25% | PASS/FAIL |
| **Roles** | ≥5 stakeholders | PASS/FAIL |
| **Criticality** | 100% meet ≥1 criterion | PASS/FAIL |
| **Impact** | 100% ≥2 cycles + ≥2 roles + quantified | PASS/FAIL |
| **Decision** | 100% decision + rationale + timeline | PASS/FAIL |
| **Citations** | 100% ≥1 valid citation | PASS/FAIL |
| **Words** | 100% in 120-200w range | PASS/FAIL |
| **Visuals** | ≥2 diagrams, ≥1 table | PASS/FAIL |
| **Meta** | Start: [Date], Expires: [+2wk] | INFO |
| **OVERALL** | All checks PASS | PASS/FAIL |

## V. Question Quality

**Good Questions** (news-driven, decision-critical, cycle-specific, multi-stakeholder, quantified, timely, actionable):
- "Fed 50bps rate cut (Sept 2024): refinancing implications?"
- "USD/EUR volatility +15% (Q4 2024): hedging strategy?"
- "Salesforce acquires Slack $27.7B (12x revenue): valuation benchmark?"

**Bad Questions** (avoid):
- "How does WACC work?" (no news)
- "What is M&A?" (educational)
- "Should we raise debt?" (no trigger)
- "Fed announced rate decision" (no specifics)

## VI. Output Format

### A. Structure

```markdown
# [Domain] Financial & Economic Intelligence Q&A ([Period])

## Contents
1. Executive Summary
2. Questions by Cycle: Capital Allocation | Liquidity | M&A/Corp Dev | Risk/Compliance
3. References: Glossary | News | M&A | Treasury | Research
4. Validation
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Sector] | **Period**: [Dates] | **Coverage**: [# items, categories]

**Key Insights**: [2-3 high-impact news items with decisions and timelines]

**Dashboard**: [Table: Cycle | News | Decision | Timeline]

**Stakeholders**: [Roles] | **References**: [Counts by type]
```

### C. Q&A Template

```markdown
### Q#: [Specific News Question + Cycle]

**Cycle**: [Cycle] | **Roles**: [Primary, Secondary] | **Categories**: [Covered] | **Criticality**: [Criterion met]

**News** (~25w): What, when, why, category [Ref: N#][n#]

**Impact** (~50w): **Cycles** (≥2) with explicit causal links | **Quantified**: WACC%/Liquidity$/Valuation/Tax$/Cash flow$/IRR

**Stakeholders** (~35w): **[Role 1]**: Concerns + actions | **[Role 2]**: Concerns + actions

**Decision & Alternatives** (~50w): **Options**: Contrast ≥2 (Execute/Defer/Hedge/Monitor/Avoid) with benefits/costs/risks | **Recommendation**: Choice + rationale + success criteria

**Action** (~20w): **Immediate (0-2wk)**: Steps + owner | **Short-term (2wk-2mo)**: Steps + owner

[n1]: URL
---
