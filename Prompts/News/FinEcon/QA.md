# Financial & Economic News Intelligence Q&A Generator

**Purpose:** Generate 4–6 decision-critical Q&As from recent financial/economic news for finance leadership capital allocation and risk decisions.

## Table of Contents
- [I. Context & Scope](#i-context--scope)
- [II. Requirements](#ii-requirements)
- [III. Execution](#iii-execution)
- [IV. Validation](#iv-validation)
- [V. Question Quality](#v-question-quality)
- [VI. Output Format](#vi-output-format)

## I. Context & Scope

- **Problem**: Finance leadership needs decision-critical insights from fragmented financial news
- **Cadence**: Bi-weekly; valid 2wk (state generation/expiry dates)
- **Domain**: Financial/economic news affecting capital structure, liquidity, M&A, risk/compliance
- **Audience**: CFO, VP Finance, Treasurer, Corp Dev, FP&A
- **Horizon**: 1–6mo decisions; exclude <1mo tactical moves and >6mo speculation
- **Org Scale**: $100M+ revenue or $50M+ annual finance decisions
- **Resources**: 2-4h per cycle (analyst/AI-assisted)
- **Format**: Scannable ≤30min
- **Freshness**: News <2mo (preferred), <4mo (acceptable), ≤9mo (max); high-velocity topics (capital markets, macro) require fresher sources

**Decision Criticality** (each Q must meet ≥1):
1. Impacts capital allocation, capital structure, M&A, or liquidity
2. Creates material risk (financial stability, compliance, cash flow)
3. Requires action within 1-6mo
4. Has quantified impact (WACC%, $, multiples, IRR)

**Decision Cycles** (cover ≥3):
1. **Capital Allocation**: Investment decisions, project prioritization, capex/opex
2. **Liquidity/Cash**: Working capital, cash runway, debt servicing
3. **M&A/Corp Dev**: Acquisitions, divestitures, partnerships
4. **Risk/Compliance**: Regulatory, FX/interest rate risk, controls

**News Categories** (cover ≥3):
1. **Capital Markets/Rates**: Rate changes, equity valuations, credit spreads
2. **Macro Trends**: GDP/CPI/unemployment, recession signals, sector shifts
3. **M&A/Corp Dev**: Transactions, valuations, implications
4. **Treasury/FX**: Currency volatility, liquidity stress, refinancing

**Exclude**: Operations, product strategy, fundraising, rumors, educational content.

## II. Requirements

**Output**: 4-6 Q&As | ≥3 decision cycles + ≥3 news categories | 120-200w per Q&A

**References**: ≥6 total (prioritize news; include M&A/treasury/research)

**Visuals**: ≥2 Mermaid diagrams + ≥1 table

## III. Execution

### Step 1: News Discovery
Record generation date (YYYY-MM-DD). Search ≥10 candidates; select 4-6 meeting decision criticality.

**Sources**: Fed/ECB, WSJ, Bloomberg, FT, Reuters (markets); BLS/BEA (macro); MergerMarket (M&A); research. Avoid rumors/PR.

**Rank by**: (1) quantified impact, (2) urgency, (3) multi-cycle effects

### Step 2: Build References
**Format**: G# (term, definition) | N# (news, source, date, URL) | M# (M&A, date, URL) | T# (treasury, date, URL) | R# (research, author, year, URL)

**Citations**: `[Ref: N1][n1]` in text, `[n1]: [Source] (YYYY-MM-DD) URL` at end. Verify figures; label estimates ("est.", "proj.", "assumes X"). Research 2023+.

**Glossary**: Define non-core terms.

### Step 3: Generate Q&A
**Question**: "[Specific News] implications for [Cycle]?"

**Structure** (120-200w total):
1. **News** (~25w): What, when, why [Ref: N#][n#]
2. **Impact** (~50w): ≥2 cycles + quantified metrics (%, $, multiple, IRR, bps); explicit causal links ("X causes Y because Z")
3. **Stakeholders** (~35w): **Primary**: Concerns → actions | **Secondary**: Concerns → actions
4. **Decision** (~50w): **Recommended**: [Option] - benefits, costs, risks, criteria | **Alternative**: [Option] - benefits, costs, risks
5. **Action** (~20w): **Critical (0-2wk)**: [Step] - [Owner] | **Important (2wk-2mo)**: [Step] - [Owner]
6. Links: [n#]: [Source] (YYYY-MM-DD) URL

### Step 4: Add Visuals
**Diagrams** (≥2): Mermaid flowcharts (decision trees, WACC/DCF), sequence diagrams (timelines), scenario comparisons.

**Tables** (≥1): Decision matrix (Option, Benefits, Costs, Risks, Timeline), impact summary (Cycle, Metric, Current, Target), or action tracker (Role, Action, Timeline, Priority).

### Step 5: Self-Review
Verify: calculations (WACC%, IRR, multiples), citations (dates, URLs, recency), logic (no contradictions), completeness (News/Impact/Stakeholders/Decision/Action), uncertainties flagged (prefix with "est.", "proj.", "assumes X" for estimates/projections/assumptions).

## IV. Validation

| Check | Criteria | Target | Status |
|-------|----------|--------|--------|
| **Freshness** | News recency | ≥50% <2mo, all ≤9mo | PASS/FAIL |
| **Coverage** | Cycles + Categories | ≥3 cycles, ≥3 categories | PASS/FAIL |
| **Output** | Q&A count | 4-6 Q&As | PASS/FAIL |
| **Per Q&A** | Content requirements | 120-200w, ≥1 citation, ≥2 roles, decision (≥2 alternatives)+action | PASS/FAIL |
| **References** | Total citations | ≥6 (news prioritized) | PASS/FAIL |
| **Visuals** | Diagrams + Tables | ≥2 diagrams (Mermaid), ≥1 table | PASS/FAIL |
| **Meta** | Generation/Expiry | Start: [YYYY-MM-DD], Expires: [+2wk] | INFO |

## V. Question Quality

**Good** (news-driven, decision-critical, quantified):
- "Fed 50bps cut (Sept 2024): refinancing implications?"
- "USD/EUR volatility +15% (Q4 2024): hedging strategy?"
- "Salesforce/Slack $27.7B (12x revenue): valuation benchmark?"

**Bad** (avoid):
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

**Stakeholders** (~35w): 
- **[Primary]**: [Concerns] → [Actions]
- **[Secondary]**: [Concerns] → [Actions]

**Decision** (~50w): 
- **Recommended**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z], Criteria: [When]
- **Alternative**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z]

**Action** (~20w): 
- **Critical (0-2wk)**: [Step] - [Owner]
- **Important (2wk-2mo)**: [Step] - [Owner]

[n1]: [Source] (YYYY-MM-DD) URL
---
