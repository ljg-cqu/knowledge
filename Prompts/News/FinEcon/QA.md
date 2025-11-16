# Financial & Economic News Intelligence Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent financial/economic news—minimal viable tracking for informed decisions with limited time.

**Cadence**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Capital Markets, Macro): ≥85% <1mo (≥30% 1-7d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (M&A, Treasury, Reporting): ≥70% <2mo (≥20% 1-7d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical financial news only—rate changes, M&A deals, macro shifts, treasury/FX moves, compliance deadlines. For CFO/FP&A/Treasury teams.

**Exclude**: Technical operations, commercial/sales execution, product strategy, early-stage fundraising, marketing, unverified rumors, stale news, nice-to-have trends.

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

**Answer Structure** (120-200w): News (what, when, why) + impact (quantified, ≥2 cycles, ≥2 roles) + decision (Execute/Hedge/Defer/Monitor/Avoid + rationale) + timeline (immediate/short). Projections only if sourced.

## II. Requirements

**Q&A**: 4-6 total | 1-2/cycle | 120-200w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Cycles** (3-4, 1-2 Q each): Capital Allocation, Liquidity/Cash, M&A/Corp Dev, Risk/Compliance (skip Annual Budgeting, Quarterly Forecasting unless decision-critical)

**Category Coverage** (min): Capital Markets/Rates ≥50%, Macro ≥40%, M&A ≥40%, Treasury/FX ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/11): CFO, VP Finance, Treasurer, Corp Dev, FP&A (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), M≥2-3 (M&A), T≥2 (Treasury), R≥2 (research), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% rumors/speculation
3. **Impact**: 100% ≥2 cycles + ≥2 roles + quantified (WACC%, liquidity$, valuation multiple, tax$, cash flow$, IRR)
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)**—calculate all news ages from this.

1. **Domain**: Financial/economic sector + period (e.g., "Tech Finance Q4 2024")

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-7d, search first): `"Fed|ECB rate decision"`, `"interest rates|yield curve"`, `"GDP|CPI|unemployment"`, `"[Sector] acquisition|merger"` + 1-7d
   
   **Tier 2** (7-14d if insufficient): Same + 7-14d

   **Sources** (whitelist, prioritize):
   - **Capital Markets**: Fed/ECB/BoE/BoJ, WSJ, Bloomberg, FT, Reuters
   - **Macro**: BLS, BEA, ISM, central bank reports
   - **M&A**: MergerMarket, PitchBook, company announcements
   - **Treasury/FX**: Bloomberg FX, Treasury Today, central bank reports
   - **Research**: McKinsey, BCG, Bain, S&P, Moody's, Fitch
   - **Avoid**: PR fluff, rumors, speculation, clickbait

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Bloomberg Terminal

3. **Curate** (≥10-15 candidates: Capital Markets ≥4, Macro ≥3, M&A ≥2, Treasury ≥2):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, names, numbers, metrics)
   - ✅ Not rumors/speculation
   - ✅ Relevant to ≥2 roles

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 3-4 cycles (1-2 each) × 3-4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | M# (M&A, companies, valuation, URL) | T# (treasury, instrument, terms, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥8 (100% terms used), N≥4-5, M≥2-3, T≥2, R≥2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (WACC, IRR, NPV, EBITDA, DCF, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

### Step 2.5: Opportunistic Refresh (optional, default: skip)

**Trigger**: Major policy (Fed >50bps, tax law, crisis) OR M&A (>$1B, consolidation) in 24-48h affecting ≥3 Qs

**Actions**: Quick search → Add 1-2 "BREAKING" → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[Rate News] implications for [Cycle]+[Roles]?" | "[Macro News]: impact on [Planning]?" | "[M&A Deal]: valuation implications?" | "[FX News]: hedging strategy?"

**Avoid**: Generic questions, speculation, stale news, unattributed claims

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 cycles + quantified (WACC%, liquidity$, valuation multiple, tax$, cash flow$, IRR)
3. **Stakeholders** (~35w): ≥2 roles + concerns + actions
4. **Decision** (~50w): Execute/Hedge/Defer/Monitor/Avoid + rationale + criteria
5. **Action** (~20w): Immediate (0-2wk), Short (2wk-2mo) + owner
6. **Links**: Define at end: `[n1]: URL`

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 cycles | ≥2 roles | Decision clear | 120-200w | Quantified | ≥1 cite | 0% speculation | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: WACC/DCF models, M&A valuations, scenario analyses (best/base/worst), liquidity waterfalls, decision trees

**Format**: Mermaid (flows), Markdown tables (data)

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥8 (100% terms used) | N≥4-5 | M≥2-3 | T≥2 | R≥2 | A≥6

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 cycles | Categories per % | ≥5 roles | Citations OK | 5 word samples 120-200w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% speculation | Decision Criticality 100% | Impact 100% ≥2 cycles+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-cycle ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

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
3. Questions by Cycle: Capital Allocation (Q1-Q2) | Liquidity (Q3-Q4) | M&A/Corp Dev (Q5-Q6) | Risk/Compliance (Q7-Q8)
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

**Impact** (~50w): **Cycles** (≥2) | **Quantified**: WACC% | Liquidity$ | Valuation multiple | Tax$ | Cash flow$ | IRR

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Execute/Hedge/Defer/Monitor/Avoid | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n1]: URL
---
