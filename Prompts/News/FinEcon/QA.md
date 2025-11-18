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

- **Problem**: Finance leadership needs decision-critical insights from fragmented financial news
- **Cadence**: Bi-weekly; valid 2 weeks (state generation/expiry dates)
- **Domain**: Financial/economic news affecting capital structure, liquidity, M&A, risk/compliance
- **Audience**: CFO, VP Finance, Treasurer, Corp Dev, FP&A (assumes core finance literacy)
- **Horizon**: 1–6 month decisions; exclude intraday moves and long-term speculation
- **Org Scale**: Mid-to-large enterprises ($100M+ revenue or $50M+ annual finance decisions)
- **Resources**: ~2-4h per cycle for analyst/AI-assisted research
- **Format**: Scannable in ≤30 minutes

**Freshness**: Prioritize recent news (<2mo preferred, <4mo acceptable, ≤9mo maximum). High-velocity topics (capital markets, macro) require fresher sources than medium-velocity (M&A, treasury).

**Decision Criticality** (each Q must meet ≥1):
1. Impacts capital allocation, capital structure, M&A execution, or liquidity
2. Creates material risk to financial stability, compliance, or cash flow
3. Affects ≥2 stakeholder roles
4. Requires near-term action (1-6mo)
5. Has quantified impact (WACC%, $amounts, multiples, IRR)

**Decision Cycles** (cover ≥3): Finance decision domains requiring distinct workflows
1. **Capital Allocation**: Investment decisions, project prioritization, capex/opex trade-offs
2. **Liquidity/Cash**: Working capital, cash runway, debt servicing
3. **M&A/Corp Dev**: Acquisitions, divestitures, strategic partnerships
4. **Risk/Compliance**: Regulatory, financial risk (FX/interest rate), internal controls

**News Categories** (cover ≥3):
1. **Capital Markets/Rates**: Rate changes, equity valuations, credit spreads
2. **Macro Trends**: GDP/CPI/unemployment, recession signals, sector shifts
3. **M&A/Corp Dev**: Transactions, valuations, strategic implications
4. **Treasury/FX**: Currency volatility, liquidity stress, debt refinancing

**Exclude**: Operations, product strategy, early-stage fundraising, rumors, educational content.

## II. Requirements

**Output**: 4-6 Q&As covering ≥3 decision cycles + ≥3 news categories

**Per Q&A**: 120-200 words | ≥1 news citation | Quantified impact | ≥2 stakeholder roles | Decision with ≥2 alternatives

**References**: ≥6 total (prioritize news; include M&A/treasury/research as relevant)

**Visuals**: ≥2 diagrams (Mermaid) + ≥1 table

## III. Execution

### Step 1: News Discovery
Record generation date (YYYY-MM-DD). Search ≥10 candidates (1-14d preferred).

**Sources**: Fed/ECB, WSJ, Bloomberg, FT, Reuters (markets); BLS/BEA (macro); MergerMarket (M&A); research reports. Avoid rumors/PR.

**Curate**: Select 4-6 items meeting decision criticality (Section I). Rank by: (1) quantified financial impact, (2) urgency (<2mo), (3) multi-cycle effects.

### Step 2: Build References
**Format**: G# (term, definition) | N# (news, source, date, URL) | M# (M&A deal, date, URL) | T# (treasury instrument, date, URL) | R# (research, author, year, URL)

**Citations**: `[Ref: N1][n1]` in text, `[n1]: [Source] (YYYY-MM-DD) URL` at end. Verify figures against primary sources; label estimates/projections with "est.", "proj.", or "assumes X".

**Recency**: News <2mo (preferred), <4mo (acceptable), ≤9mo (max). Research from 2023+.

**Glossary**: Define technical terms not in core finance literacy (e.g., WACC, DCF → known; emerging terms → define). Use plain language definitions.

### Step 3: Generate Q&A
**Question**: "[Specific News] implications for [Cycle]?"

**Structure** (120-200 words total):
1. **News** (~25w): What happened, when, why it matters [Ref: N#][n#]
2. **Impact** (~50w): ≥2 cycles + quantified metrics (%, $, multiple, IRR); explicit causal links ("X causes Y because Z"). Order: critical first.
3. **Stakeholders** (~35w): **[Primary]**: Concerns + actions | **[Secondary]**: Concerns + actions. Order: primary decision-maker first.
4. **Decision** (~50w): **Recommended**: [Option] - benefits, costs, risks, criteria | **Alternative**: [Option] - benefits, costs, risks
5. **Action** (~20w): **Critical (0-2wk)**: [Step] - [Owner] | **Important (2wk-2mo)**: [Step] - [Owner]
6. Links: [n1]: [Source] (YYYY-MM-DD) URL

### Step 4: Add Visuals
**Diagrams** (≥2): Mermaid flowcharts (decision trees, WACC/DCF calculation flows), sequence diagrams (timeline for actions), or scenario comparisons.

**Tables** (≥1): Decision comparison matrix (columns: Option, Benefits, Costs, Risks, Timeline), impact summary (columns: Cycle, Metric, Current, Target), or stakeholder action tracker (columns: Role, Action, Timeline, Priority).

### Step 5: Self-Review
Before finalizing, verify:
- **Calculations**: Cross-check metrics (WACC%, IRR, multiples) against sources
- **Citations**: Confirm dates, source names, URLs are accurate and recent
- **Logic**: Check for contradictions between recommendations
- **Completeness**: All Q&As have News/Impact/Stakeholders/Decision/Action
- **Uncertainties**: Flag estimates, projections, or assumptions explicitly

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

**Generated**: [YYYY-MM-DD] | **Expires**: [YYYY-MM-DD] | **Scan Time**: ≤30min

## Executive Summary
**Coverage**: [X] Q&As across [Y] decision cycles, [Z] news categories

**Key Insights** (priority-ordered):
1. **[Critical insight]**: [Decision] by [Timeline] - [Primary stakeholder]
2. **[Important insight]**: [Decision] by [Timeline] - [Primary stakeholder]
3. **[Notable insight]**: [Decision] by [Timeline] - [Primary stakeholder]

**Action Dashboard**:
| Cycle | News Event | Decision | Critical Action | Owner | Deadline |
|-------|------------|----------|-----------------|-------|----------|
| ... | ... | ... | ... | ... | ... |

## Questions by Cycle
[Organized by: Capital Allocation | Liquidity/Cash | M&A/Corp Dev | Risk/Compliance]

## References
**Glossary**: [G#: Term - Definition]
**News**: [N#: Source (YYYY-MM-DD) URL]
**M&A**: [M#: Deal (YYYY-MM-DD) URL]
**Treasury**: [T#: Instrument (YYYY-MM-DD) URL]
**Research**: [R#: Author (Year) URL]

## Validation
[Include validation table from Section IV with actual values]
```

### Q&A Template
```markdown
### Q#: [Specific News Event] implications for [Decision Cycle]?

**Cycle**: [Capital Allocation/Liquidity/M&A/Risk] | **Roles**: [Primary, Secondary] | **Criticality**: [Criterion #]

**News** (~25w): [What happened], [when], [why it matters] [Ref: N#][n#]

**Impact** (~50w): 
- **[Cycle 1]**: [Quantified metric change] because [causal mechanism]
- **[Cycle 2]**: [Quantified metric change] because [causal mechanism]
Order: critical first. Use specific numbers (%, $, multiples, bps, IRR).

**Stakeholders** (~35w): 
- **[Primary Role]**: [Specific concerns] → [Required actions]
- **[Secondary Role]**: [Specific concerns] → [Required actions]

**Decision** (~50w): 
- **Recommended**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z], Criteria: [When to choose]
- **Alternative**: [Option] - Benefits: [X], Costs: [Y], Risks: [Z]

**Action** (~20w): 
- **Critical (0-2wk)**: [Specific step] - [Owner role]
- **Important (2wk-2mo)**: [Specific step] - [Owner role]

[n1]: [Source Name] (YYYY-MM-DD) URL
---
