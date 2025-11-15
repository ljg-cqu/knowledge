# Financial & Economic News Intelligence Q&A Generator

Generate 15–20 Q&As transforming recent financial/economic news into actionable intelligence across 6 categories, 6 planning cycles, 11 stakeholder roles.

## Scope & Constraints

**Domain**: Corporate finance, treasury, capital markets, M&A, macro trends, compliance. Organizations with structured financial planning (all sizes, all industries).

**Exclude**: Technical operations, commercial/sales execution, product strategy, early-stage fundraising, marketing, unverified rumors, stale news (HV >4mo, MV >6mo).

**Freshness** (category-adaptive):
- **HV** (Capital Markets, Macro): ≥75% <1mo (≥25% 1-7d), ≥90% <2mo, 100% ≤4mo
- **MV** (M&A, Treasury, Reporting): ≥65% <2mo (≥15% 1-14d), ≥85% <3mo, 100% ≤6mo
- **Overall**: ≥70% <2mo, ≥85% <4mo, 100% ≤6mo
- **Validity**: Expires 4 weeks; re-validate if >2mo

**Categories** (6, each Q covers ≥2):
1. **Capital Markets/Rates**: Rate changes (Fed/ECB/BoE/BoJ), equity (IPO/valuations), credit (spreads/covenants), capital raising (debt/equity terms), yields (LIBOR/SOFR)
2. **Macro Trends**: Indicators (GDP/CPI/unemployment/PMI), recession signals, sector trends, commodities, trade policy, regional divergence
3. **M&A/Corp Dev**: Transactions/valuations, consolidation, divestitures, deal structures, multiples, partnerships, CVC
4. **Treasury/FX**: Currency volatility, FX hedging, cash/working capital, debt refinancing, credit facilities, liquidity stress, counterparty risk
5. **Reporting/Compliance**: Standards (ASC 606/842, IFRS), SEC disclosure, tax law, SOX, audit governance, revenue recognition
6. **IR/Capital Structure**: Activism, earnings guidance, allocation (dividends/buybacks/M&A), ratings, convertible debt, secondaries

**News Relevance** (≥2 required, Recency mandatory):
1. Recency per freshness guarantee
2. Planning Cycle Impact (≥2 cycles)
3. Stakeholder Breadth (≥3 roles)
4. Decision Urgency (1-6mo)
5. Financial Significance (capital/liquidity/assumptions shift)
6. Quantified Impact (measurable financial metrics)

**Answer Format** (250-400w): News summary (age per guarantee) → Financial impact (≥2 cycles, ≥2 roles, quantified) → Decision (Execute/Hedge/Defer/Monitor/Avoid) → Action timeline (immediate/short/medium) → Optional projections (source, confidence, scenarios).

## Requirements

### Floors

**Q&A**: 15-20 | 2-3/cycle | 250-400w | 100% news-driven (≥1 per freshness) | ≥80% ≥1 cite, ≥35% ≥2 cites | ≥2 categories + impact + decision

**Cycles** (6, 2-3 Q each): (1) Annual Budgeting, (2) Quarterly Forecasting, (3) Capital Allocation, (4) Liquidity/Cash, (5) M&A/Corp Dev, (6) Risk/Compliance

**Category Coverage**: Capital Markets/Rates 80%, Macro 70%, M&A 60%, Treasury/FX 75%, Compliance 55%, IR/Capital 65%

**Decision** (100%): Impact (≥2 cycles, ≥2 roles, quantified: WACC/liquidity/valuation/tax/cash flow) + Decision (Execute/Hedge/Defer/Monitor/Avoid + rationale + alternatives) + Action (immediate/short/medium)

**Stakeholders** (≥8/11): CFO, VP Finance, Treasurer, Controller, Corp Dev, IR, FP&A, Tax Director, M&A Analyst, Risk Officer, Board Finance

**References** (build before Q&A): G≥20 (100% terms/acronyms with formulas), N≥12, E≥8, M≥6, F≥6, R≥6, A≥20 (APA 7th)

**Visuals**: ≥8 diagrams + ≥4 tables

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

1. **News**: 100% cite ≥1 per freshness; 0% rumors
2. **Impact**: 100% ≥2 cycles + ≥2 roles + quantified
3. **Decision**: 100% with rationale + timeline + criteria + metrics (NPV/IRR/payback/WACC)
4. **Sources**: ≥5 types, max 35%/type; ≥1 news + ≥1 analysis/cycle; 100% URLs valid
5. **Coverage**: ≥8/11 roles; categories per floors
6. **Actionability**: 100% concrete + timelines + owners; 0% abstract

## Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)**—all ages from this date.

1. **Domain**: Industry/sector + period (e.g., "Enterprise Tech Finance Q3-Q4 2024")

2. **Search** (≥30-40 candidates, tiered):
   - **T1 (1-7d)**: Rates, markets, macro, FX, M&A queries
   - **T2 (7-14d)**: HV categories if T1 insufficient
   - **T3 (2-4wk/2-3mo)**: HV/MV backfill if T1+T2 insufficient

   **Queries**: `"Fed|ECB rate decision"`, `"interest rates|yield curve"`, `"GDP|CPI|unemployment"`, `"USD|EUR currency volatility"`, `"[Domain] acquisition|merger"`

   **Sources**: Central banks (Fed/ECB/BoE/BoJ, BIS), Economic data (BLS/BEA/ISM), Capital markets (WSJ/Bloomberg/FT/Reuters), M&A (MergerMarket/PitchBook), Financial news (WSJ/FT/Bloomberg), Accounting/Tax (FASB/IRS/Deloitte/PwC), Treasury/FX (Treasury Today/Bloomberg FX), IR (NIRI), Research (McKinsey/BCG/Bain), Credit (S&P/Moody's/Fitch), Regulatory (SEC/FASB/IASB). **Avoid**: Promotional, rumors, clickbait.

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:YYYY-MM-DD`), Bloomberg Terminal, Fed Watch

   **Age Target**: HV <1mo ≥75% (1-7d ≥25%), MV <2mo ≥65% (1-14d ≥15%), Overall <2mo ≥70%

3. **Curate** (≥20: Capital Markets ≥6, Macro ≥5, M&A ≥4, Treasury ≥4, Compliance ≥3, IR ≥3):
   - ✅ Age per freshness | ✅ Whitelist OR primary source | ✅ ≥2 relevance criteria | ✅ 0% rumors | ✅ Specific details

4. **Verify**: Count by category/age; if fails, return to T1-T3

5. **Allocate**: 15-20 Q across 6 cycles (2-3 each), 6 categories (≥2/Q), 11 roles (≥8 total)

6. **Cadence**: Monthly refresh

### Step 2: Build References (before Q&A)

**Format**: G# (term, def+analogy/formula, context) | N# (news, source, date, category, impact, URL, justification if HV >1mo/MV >3mo) | E# (indicator, source, date, reading, trend, implication, URL) | M# (deal, companies, valuation, multiple, URL) | F# (instrument, terms, pricing, use, URL) | R# (research, firm, date, findings, URL) | A# (APA 7th)

**Citation**: `[Ref: N1][n1]` in text, `[n1]: URL` at end

**Floors**: G≥20 (100% terms/acronyms/metrics), N≥12 (100% URLs+dates), E≥8, M≥6, F≥6, R≥6, A≥20

**Glossary** (100% coverage): ALL terms (EBITDA/DCF/WACC/IRR/NPV/EPS/LIBOR/SOFR/ASC 606), metrics (debt/equity, coverage ratios), concepts (yield curve inversion, covenant-lite, convertible notes, accretive/dilutive) | Plain language, real-world analogies, formulas with calculations, decision context, concrete examples

### Step 2.5: Opportunistic Refresh (optional, default: skip)

**Trigger**: Major policy (Fed >50bps, tax law, crisis) OR M&A (>$1B, consolidation) in 24-48h affecting ≥3 Qs

**Actions**: Quick search → Add 1-2 "BREAKING" → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 3-4, self-check each)

**Pre-check**: Review glossary (G1-G20+). Track ALL terms. Verify 100% defined with formulas. Add missing immediately.

**Question Patterns**: "[Rate News] implications for [Cycle] and [Roles]?" | "[Macro News]: impact on [Planning]?" | "[M&A Deal]: valuation lessons for [Corp Dev]?" | "[FX News]+[Projection]: hedging strategies?"

**Avoid**: Generic "What is X?", commercial/GTM, technical, speculation, stale news

**Answer** (250-400w):
1. **News** (~60w): What, when, who, why, category + `[Ref: N#][n#], [E#][e#]`
2. **Impact** (~110w): ≥2 cycles + quantified (WACC %, liquidity $, valuation multiple, tax $, cash flow $, IRR)
3. **Stakeholders** (~70w): ≥2 roles + concerns + actions + authority (CFO for strategic)
4. **Decision** (~90w): Execute/Hedge/Defer/Monitor/Avoid + rationale + 1-2 alternatives + criteria (NPV, IRR, payback, WACC, debt/equity targets)
5. **Action** (~60w): Immediate (0-2wk), Short (2wk-2mo), Medium (2-6mo) + owner + deliverable
6. **Projections** (opt ~40w): "[Source] projects [outcome] by [time] with [confidence]. Scenarios: best/base/worst [ranges]" + `[Ref: R#][r#]`
7. **Links**: Define at end: `[n1]: URL`, `[e1]: URL`
8. **Artifacts**: 1-2 diagrams/tables

**Self-Check**: Age ✓ | ≥2 cycles ✓ | ≥2 roles ✓ | Decision ✓ | 250-400w ✓ | Quantified ✓ | ≥2/4 ≥2 cites ✓ | Artifact ✓ | Timeline ✓ | 0% speculation ✓ | 100% actionable ✓ | Projections attributed+scenarios+timed ✓ | **Terms in glossary+formulas ✓**

### Step 4: Create Visuals (≥8 diagrams + ≥4 tables, ≥60% referenced)

**Types**: WACC/DCF models, capital structure, M&A valuations, scenario analyses (best/base/worst), liquidity waterfalls, covenant tracking, FX exposure, tax optimization, economic trends

**Format**: Mermaid (trees/waterfalls), Markdown tables (calculations, scenarios, indicators, multiples)

### Step 5: Final Checks

**References**: 100% [Ref: ID] resolve | News age ✓ | Fields complete | APA tags | G≥20 (100% terms+formulas) | N≥12 (6 cats) | E≥8 | M≥6 | F≥6 | R≥6 | A≥20 (40-60% news/economic, 25-35% research)

**Decision**: 100% decision + rationale + alternatives + criteria + timeline + metrics (NPV/IRR/WACC/payback)

**Stakeholders**: ≥8/11 roles | Actions + authority | Cross-role | CFO/Board for strategic

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors ✓ (G≥20, N≥12, E≥8, M≥6, F≥6, R≥6, A≥20, Q=15-20) | Glossary (100% terms, ≥60% formulas) | 6 cycles (2-3 Q each) | Categories (Markets 80%, Macro 70%, M&A 60%, Treasury 75%, Compliance 55%, IR 65%) | Stakeholders ≥8/11 | Citations (100% ≥1 news, ≥80% ≥1 cite, ≥35% ≥2) | Distribution (News 40-60%, Research 25-35%, Other 15-25%) | Words (5 samples 250-400) | Visuals (≥60% ref, ≥8 diagrams, ≥4 tables) | Decision 100% (+ metrics) | Timeline 100% | **Age per freshness**

**Qualitative**: News (per freshness, 0% speculation) | Impact (100% ≥2 cycles + ≥2 roles + quantified) | Decision (100% Execute/Hedge/Defer/Monitor/Avoid + alts + criteria) | Source diversity (≥5 types, max 35%) | Per-cycle (≥1 news + ≥1 analysis) | Links (100% valid) | Cross-refs (100% resolve) | Quantified (100% measurable) | Actionable (100% concrete, 0% abstract) | Anti-speculation (0% rumors, 100% verified) | Projections (100% attributed + scenarios + confidence + time) | Search doc (queries, sources, count)

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | **Glossary complete (100% terms, ≥60% formulas, 100% reader-friendly)** | TOC (6 cycles, Q ranges) | 0 placeholders | ≥8 diagrams + ≥4 tables | 100% cite ≥1 news | 100% impact (≥2 cycles, ≥2 roles, quantified + metrics) | 100% decision (+ rationale + metrics) | 100% timeline | Categories per thresholds | ≥8/11 roles | **Freshness met** | 0% speculation, 100% verified | Projections attributed+scenarios+confident+timed | URLs valid | **Dates (generation + expiration [+4wks])** | Search queries + sources documented

## Validation Report

Use Step 6 criteria. Fill table:

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __% <1mo (1-7d: __%), __% <2mo, __% ≤4mo \| MV: __% <2mo (1-14d: __%), __% <3mo, __% ≤6mo \| Overall: __% <2mo, __% <4mo, __% ≤6mo | Per guarantee | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ E:__ M:__ F:__ R:__ A:__ Q:__ | ≥20, ≥12, ≥8, ≥6, ≥6, ≥6, ≥20, 15-20 | | PASS/FAIL |
| 2a | **Glossary** | __% terms defined; __% with formulas; __% unfamiliar covered | 100%; ≥60%; 100% | | PASS/FAIL |
| 3 | **Cycles** | Cycles __/6 (2-3 Q each); total Q __ | 6/6; 15-20 | | PASS/FAIL |
| 4 | **Categories** | Markets __%, Macro __%, M&A __%, Treasury __%, Compliance __%, IR __% | ≥80%, ≥70%, ≥60%, ≥75%, ≥55%, ≥65% | | PASS/FAIL |
| 5 | **Stakeholders** | Roles __/11 | ≥8 | | PASS/FAIL |
| 6 | **Impact** | __% ≥2 cycles + ≥2 roles + quantified | 100% | | PASS/FAIL |
| 7 | **Decision** | __% decision + rationale + alts + criteria + metrics | 100% | | PASS/FAIL |
| 8 | **Timelines** | __% immediate/short/medium + owners | 100% | | PASS/FAIL |
| 9 | **Citations** | __% ≥1 news; __% ≥1 cite; __% ≥2 cites | 100%; ≥80%; ≥35% | | PASS/FAIL |
| 10 | **Distribution** | News __%, Research __%, Other __% | 40-60%, 25-35%, 15-25% | | PASS/FAIL |
| 11 | **Diversity** | Types __; max %/type __ | ≥5; ≤35% | | PASS/FAIL |
| 12 | **Per-Cycle** | __/6 cycles ≥1 news + ≥1 analysis | 6/6 | | PASS/FAIL |
| 13 | **Words** | 5 samples: __% 250-400w | 100% | | PASS/FAIL |
| 14 | **Visuals** | __% ref; diagrams __; tables __ | ≥60%; ≥8; ≥4 | | PASS/FAIL |
| 15 | **Quantified** | __% measurable financial impact | 100% | | PASS/FAIL |
| 16 | **Links** | __% URLs valid | 100% | | PASS/FAIL |
| 17 | **Cross-Refs** | __% [Ref: ID] resolve | 100% | | PASS/FAIL |
| 18 | **Actionable** | __% concrete; __% abstract | 100%; 0% | | PASS/FAIL |
| 19 | **Projections** | If used: __% attributed; __% scenarios; __% confident; __% timed | 100%; 100%; 100%; 100% | | PASS/FAIL |
| 20 | **Search** | Queries: Y/N \| Whitelist: Y/N \| Candidates: __ \| Accept: __% | Y; Y; ≥30; 55-75% | | PASS/FAIL |
| | **Metadata** | Start: __ \| End: __ \| Expires: [+4wks] \| Refresh: Y/N (__) | | INFO |
| | **Age Dist** | <1mo __% (1-7d __%, 8-21d __%, 22-30d __%) \| 1-2mo __% \| 2-4mo __% \| 4-6mo __% \| HV __%, MV __% | Per guarantee | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## Question Quality (fails ≥3/11 = rewrite)

**Criteria**: News-driven (per freshness) | Cycle-specific (1-2 cycles, clear impact) | Multi-stakeholder (≥2 roles) | Multi-category (≥2 types) | Decision-focused | Quantified impact | Cross-cycle aware | Timely urgency | Alternative-aware (1-2 strategies) | Evidence-based | Actionable | Forward-looking (projections+scenarios)

**✓ Good**: 
- "Fed 50bps rate cut (Sept 2024): debt refinancing and capital structure implications?"
- "USD/EUR volatility +15% (Q4 2024): FX hedging for international revenue?"
- "Salesforce acquires Slack $27.7B (12x revenue): M&A valuation benchmarks for SaaS?"
- "Inflation 3.2% vs Fed 2% target (Nov 2024): budgeting and cost structure impact?"
- "ASC 842 deadline (2025): compliance readiness for Controller?"

**✗ Bad**: "How does WACC work?" (no news) | "What is M&A?" (overview) | "Should we raise debt?" (no trigger) | "Gong pipeline velocity" (commercial ops)

## Output Format

### A. TOC
```markdown
# [Domain] Financial & Economic Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Overview | Insights | Dashboard)
2. Cycle Coverage (6 cycles × 6 categories matrix)
3. Questions by Cycle: Annual Planning (Q1-Q3) | Quarterly Forecast (Q4-Q6) | Capital Allocation (Q7-Q9) | Liquidity (Q10-Q12) | M&A/Corp Dev (Q13-Q15) | Risk/Compliance (Q16-Q20)
4. References: G (G1-G25+) | N (N1-N15+) | E (E1-E10+) | M (M1-M8+) | F (F1-F8+) | R (R1-R8+) | A (A1-A25+)
5. Validation Report (20 checks)
```

### B. Executive Summary
```markdown
## Executive Summary

**Domain**: [Industry/Sector] | **Period**: [Q3-Q4 2024] | **Coverage**: [# items, 6 categories]

**News**: Capital Markets ([#]: top 2-3+dates) | Macro ([#]: top 2) | M&A ([#]: top 1-2) | Treasury ([#]: top 1-2) | Compliance ([#]: top 1) | IR ([#]: top 1)

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (repeat 2-3 high-impact)

**Dashboard**: [Table: Cycle | News | Action | Impact | Timeline]

**Roles**: [9-10+counts] | **Refs**: G=[#] N=[#] E=[#] M=[#] F=[#] R=[#] A=[#]
```

### C. Cycle Overview
| # | Cycle | Range | Count | Categories | News | Roles | Artifacts |
|---|-------|-------|-------|------------|------|-------|-----------|
| 1 | Annual Planning | Q1-Q3 | 2-3 | Macro, Compliance, IR | [Top] | CFO, FP&A, Board | 2D+1T |
| 2 | Quarterly Forecast | Q4-Q6 | 2-3 | Macro, Markets, M&A | [Top] | CFO, FP&A, Controller | 2D+1T |
| 3 | Capital Allocation | Q7-Q9 | 2-3 | Markets, M&A, IR | [Top] | CFO, Corp Dev, Board | 2D+1T |
| 4 | Liquidity | Q10-Q12 | 2-3 | Treasury/FX, Markets | [Top] | CFO, Treasurer, Risk | 1D+1T |
| 5 | M&A/Corp Dev | Q13-Q15 | 2-3 | M&A, Markets, Macro | [Top] | CFO, Corp Dev, M&A Analyst | 2D+1T |
| 6 | Risk/Compliance | Q16-Q20 | 2-3 | Compliance, Treasury, Macro | [Top] | CFO, Controller, Tax, Risk | 1D+1T |
| | **Total** | | **15-20** | **All 6** | **12+** | **≥8/11** | **≥8D+≥4T** |

Legend: D=Diagrams, T=Tables

### D. Q&A Format
```markdown
### Q#: [News Question + Cycle + Roles + Decision]

**Cycle**: [Cycle] | **Roles**: [Primary, Secondary] | **Cats**: [✓✓] | **Decision**: Y

**News** (~60w): What, when, who, why, category [Ref: N#][n#], [E#][e#]

**Impact** (~110w): **Cycles** (≥2) | **Quantified**: WACC [%] | Liquidity [$] | Valuation [Multiple/EV] | Tax [$] | Cash Flow [$] | IRR [%] | NPV [$] | Payback [mo]

**Stakeholders** (~70w): **[Role 1]**: Concerns, actions, authority | **[Role 2]**: Concerns, actions, authority

**Decision** (~90w): **Rec**: Execute/Hedge/Defer/Monitor/Avoid | **Rationale**: [Why] | **Alts**: [1-2 options] | **Success**: [NPV, IRR, payback, WACC target, debt/equity, liquidity threshold]

**Action** (~60w): **Immed (0-2wk)**: [Actions+owner] | **Short (2wk-2mo)**: [Actions+owner] | **Medium (2-6mo)**: [Actions+owner]

**Projections** (opt ~40w): [Source] projects [outcome] by [time] with [confidence]. Scenarios: Best [+X%], Base [Y%], Worst [-Z%] [Ref: R#][r#]

**Artifacts**: [Type: WACC calc, DCF model, scenario analysis, liquidity waterfall, covenant tracker, FX exposure map]

<!-- Link Definitions -->
[n1]: https://source-url-for-n1
[e1]: https://source-url-for-e1
[r1]: https://source-url-for-r1

---
