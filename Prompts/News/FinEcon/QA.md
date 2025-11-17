# Financial & Economic News Intelligence Q&A Generator

Use this specification as a single, self-contained prompt for an LLM to generate 4–6 decision-critical Q&As from recent financial and economic news. The goal is to support fast, high-quality capital allocation and risk decisions for finance leadership.

## I. Context & Scope

- **Cadence**: Bi-weekly; 4–6 Q&As per run; valid 2 weeks from generation (state gen and expiry dates).
- **Domain**: Financial/economic news materially affecting corporate finance (capital structure, liquidity, M&A, risk/compliance).
- **Stakeholders**: CFO, VP Finance, Treasurer, Corp Dev, FP&A; answers must be understandable and actionable.
- **Horizon**: Org-level decisions within a 1–6 month window; ignore intraday moves and >6 month speculation unless they block near-term decisions.
- **Reader**: Assumes familiarity with core finance (WACC, IRR, NPV); provide decision-ready synthesis, not tutorials.
- **Format**: Scannable in ≤30 minutes by senior leaders; avoid redundancy and generic explanations.

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Capital Markets, Macro): ≥80% <1mo (≥25% 1–7d), ≥90% <2mo, 100% ≤4mo
- **Medium-Velocity** (M&A, Treasury, Reporting): ≥65% <2mo (≥15% 1–7d), ≥85% <3mo, 100% ≤6mo
- **Overall**: ≥70% <2mo, ≥85% <4mo, 100% ≤9mo

**Scope**: Include only decision-critical financial news—rate changes, M&A deals, macro shifts, treasury/FX moves, and compliance deadlines that satisfy the Decision Criticality Framework.

**Exclude**: Technical operations, commercial/sales execution, product strategy, early-stage fundraising, marketing, unverified rumors, stale news, nice-to-have trends, and educational overviews not tied to a specific news trigger.

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts capital allocation, debt/equity structure, M&A go/no-go, liquidity crisis
2. **Creates Risk**: Material threat to financial stability, regulatory compliance, credit rating, cash flow
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (CFO + Treasurer, CFO + Corp Dev, etc.)
4. **Requires Action**: 1-6mo action window (not speculative)
5. **Quantified Impact**: WACC %, liquidity $, valuation multiple, tax $, cash flow $, IRR

**Categories** (3-4, each Q covers ≥1):
1. **Capital Markets/Rates**: Rate changes (Fed/ECB/BoE/BoJ), equity valuations, credit spreads affecting WACC/refinancing
2. **Macro Trends**: Indicators (GDP/CPI/unemployment), recession signals, sector trends affecting assumptions
3. **M&A/Corp Dev**: Transactions, valuations, multiples affecting strategy
4. **Treasury/FX** (optional): Currency volatility, liquidity stress, debt refinancing affecting cash position

**Answer Structure** (120-200 words): News (what, when, why) + impact (quantified, ≥2 cycles, ≥2 roles) + decision (Execute/Hedge/Defer/Monitor/Avoid + rationale) + timeline (immediate/short). Projections only if sourced.

## II. Requirements

**Q&A**: 4-6 total | 1-2 per cycle | 120-200 words | 100% news-driven | 100% ≥1 citation; ≥30% ≥2 citations | ≥1 category + quantified impact + decision

**Cycles** (3-4, 1-2 Q each): Capital Allocation, Liquidity/Cash, M&A/Corp Dev, Risk/Compliance

**Category Coverage** (min): Capital Markets/Rates ≥50%, Macro ≥40%, M&A ≥40%, Treasury/FX ≥25%

**Decision Criticality** (100%): Each Q must satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5): CFO, VP Finance, Treasurer, Corp Dev, FP&A

**References**: G≥8 (all terms used), N≥4-5, M≥2-3, T≥2, R≥2, A≥6

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail any = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion
2. **News**: 100% ≥1 citation per freshness; 0% rumors/speculation
3. **Impact**: 100% ≥2 cycles + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% valid URLs
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation

Record generation date (YYYY-MM-DD) for age calculations.

1. Define domain and period (e.g., "Tech Finance Q4 2024").

2. Search for ≥10-15 candidates using tiered approach:
   - Tier 1 (1-7d): Key terms like "Fed rate decision", "GDP/CPI", "[Sector] acquisition".
   - Tier 2 (7-14d if needed): Expand search.

   Sources: Prioritize Fed/ECB, WSJ, Bloomberg, FT, Reuters for markets; BLS/BEA for macro; MergerMarket for M&A; research from McKinsey, S&P. Avoid rumors/PR.

   Tools: Perplexity, ChatGPT, Google with date filters.

3. Curate: ≥10-15 items meeting freshness, whitelist sources, ≥1 criticality criterion, specific details, no rumors, ≥2 roles relevance.

4. Verify criticality; retry if insufficient.

5. Allocate: 4-6 Q&As across 3-4 cycles (1-2 each), 3-4 categories, ≥5 roles.

### Step 2: Build References

Format: G# (term, definition+analogy, context) | N# (news, source, date, category, URL) | M# (M&A, companies, valuation, URL) | T# (treasury, instrument, terms, URL) | R# (research, findings, URL) | A# (APA 7th+tag).

Citations: `[Ref: N1][n1]` in text, `[n1]: URL` at end.

Verification: Use primary sources; verify figures; label estimates.

Floors: G≥8 (all used), N≥4-5, M≥2-3, T≥2, R≥2, A≥6.

Glossary: Terms used only; plain language; 1-2 analogies; context; examples.

### Step 3: Generate Q&A

Review glossary; track terms.

Patterns: News-driven questions like "[Rate News] implications for [Cycle]?"

Avoid: Generic/speculative questions.

Structure (120-200 words):
1. **News** (~25 words): What, when, why, category [Ref: N#][n#].
2. **Impact** (~50 words): ≥2 cycles + quantified metrics; explicit causal links.
3. **Stakeholders** (~35 words): ≥2 roles + concerns/actions; note tensions.
4. **Decision & Alternatives** (~50 words): Contrast ≥2 options (benefits/costs/risks); recommend with criteria/metrics.
5. **Action** (~20 words): Immediate (0-2wk) + short (2wk-2mo) steps + owners.
6. Links: [n1]: URL

Self-Check: Meets age/criticality/cycles/roles; clear decisions; 120-200 words; consistent metrics; ≥1 citation; actionable; coherent; assumptions stated; terms in glossary.

### Step 4: Visuals

≥2 diagrams (e.g., Mermaid flows for WACC/DCF, scenario analyses) + ≥1 table (data).

### Step 5: Final Checks

Ensure refs complete/valid; decisions/timelines/stakeholders meet requirements.

### Step 6: Submit

Checklist: All validations pass; floors met; glossary complete; TOC; no placeholders; visuals/citations OK; freshness/dates documented.

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-7d:__%), __%<2mo \| MV: __%<2mo (1-7d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ M:__ T:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2-3,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Cycles** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Markets__% Macro__% M&A__% Treasury__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2cycles+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%120-200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-7d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Cycle-specific (1-2 cycles) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "Fed 50bps rate cut (Sept 2024): refinancing implications?" | "USD/EUR volatility +15% (Q4 2024): hedging strategy?" | "Salesforce acquires Slack $27.7B (12x revenue): valuation benchmark?" | "Inflation 3.2% vs 2% target (Nov 2024): budgeting impact?" | "ASC 842 deadline (2025): compliance readiness?"

**✗ Bad**: "How does WACC work?" (no news) | "What is M&A?" (overview) | "Should we raise debt?" (no trigger) | "Gong pipeline velocity" (commercial ops) | "Fed announced rate decision" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Financial & Economic Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Cycle Coverage (3-4 cycles)
3. Questions by Cycle: Capital Allocation | Liquidity | M&A/Corp Dev | Risk/Compliance
4. References: G (G1-G8) | N (N1-N5) | M (M1-M3) | T (T1-T2) | R (R1-R2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Sector] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Cycle | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] M=[#] T=[#] R=[#] A=[#]
```

### C. Cycle Overview

| # | Cycle | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Capital Allocation | 1-2 | Markets, M&A | [Top] | CFO, Corp Dev |
| 2 | Liquidity | 1-2 | Treasury/FX, Markets | [Top] | CFO, Treasurer |
| 3 | M&A/Corp Dev | 1-2 | M&A, Macro | [Top] | CFO, Corp Dev |
| 4 | Risk/Compliance | 1-2 | Macro, Treasury | [Top] | CFO, FP&A |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Cycle + Roles]

**Cycle**: [Cycle] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Cycles** (≥2) | **Quantified**: WACC% | Liquidity$ | Valuation multiple | Tax$ | Cash flow$ | IRR. Make causal links explicit.

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same; note any tension between roles.

**Decision & Alternatives** (~50w): **Options**: Briefly contrast at least two options (e.g., Execute now vs Defer/Hedge/Monitor), including benefits, costs, and risks. **Rec**: State recommended option and why. **Success**: Quantified targets (e.g., WACC change, liquidity buffer, covenant headroom).

**Action** (~20w): **Immed (0-2wk)**: Concrete steps + owner | **Short (2wk-2mo)**: Concrete steps + owner

[n1]: URL
---
