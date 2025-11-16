# Startup & Formation Intelligence Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent industry news—minimal viable tracking for informed decisions with limited time.

**Cadence**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Scope**: Decision-critical startup news only—funding environment, market entry barriers, competitive threats, business model viability, talent/execution risk, macro/regulatory shocks. For founders, investors, early-stage companies.

**MECE Position**: Formation stage only (pre-seed → Series A). Covers decision-blocking scenarios across market, funding, business model, regulatory, talent dimensions.

**For Established Organizations**: Not for ongoing operational optimization in mature organizations—use specialized prompts (ProdMarket.md, TechOps.md, CommOps.md, FinEcon.md, StratIntel.md, OpsSupply.md, PeopleWF.md).

**Freshness** (category-adaptive thresholds):
- **HV** (Market/Competition/Partnerships): ≥85% <1mo (≥30% in 1-3d), ≥95% <2mo, 100% ≤4mo
- **MV** (Funding/VC/Business Models/Talent/Macro): ≥70% <2mo (≥20% in 1-3d), ≥90% <3mo, 100% ≤6mo
- **LT** (Regulatory/Compliance): ≥50% <3mo, ≥75% <6mo, 100% ≤12mo (≤20% at 12-18mo if enduring impact)
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo
- **Validity**: Output expires in 2 weeks; re-validate if >1mo

## I. Context & Scope

**Purpose**: Transform industry news into actionable intelligence across 6 business lifecycle phases and 12 stakeholder roles for startup formation and market entry.

**Target Audience**: Founders, investors, early-stage companies, corporate innovation teams entering new markets.

**Scope**: Market entry barriers/opportunities, competitive landscape, fundraising environment (VC sentiment, valuations, terms), business model innovation, GTM strategies, regulatory barriers, TAM/SAM drivers, ecosystem readiness, macro trends affecting startups.

**Exclude**: Technical implementation details, infrastructure decisions, operational tooling, marketing hype, unverified rumors, trivial updates, stale news per freshness guarantee.

**News Categories** (7 types, each Q covers ≥2):
1. **Market/Competition**: Market entry, competitive moves, consolidation, market sizing (TAM/SAM/SOM), customer trends, industry shifts
2. **Funding/VC**: VC sentiment, valuation multiples, fundraising environment, term sheet standards, fundraising rounds, down rounds, bridge financing, exits/IPOs, acqui-hires
3. **Business Models & GTM**: Pricing strategies, distribution channels, PLG, enterprise vs SMB, vertical vs horizontal, recurring revenue models
4. **Regulatory/Compliance**: Industry regulations, licensing, data privacy (GDPR/CCPA), sector laws, tax incentives
5. **Partnerships/Ecosystem**: Strategic partnerships, platform access, channel partnerships, accelerators, co-marketing, API integrations
6. **Talent/Labor**: Hiring trends, compensation benchmarks, remote work policies, talent hotspots, competitor hiring, layoffs, executive moves, acqui-hires
7. **Economic/Macro**: Interest rates, inflation, recession signals, CapEx cycles, consumer spending, FX

**News Relevance** (must meet ≥2 including Recency):
1. **Recency** (MANDATORY—see freshness guarantee)
2. **Lifecycle Impact**: Affects ≥2 phases OR cross-phase coordination
3. **Stakeholder Breadth**: Relevant to ≥3 roles OR multi-role decisions
4. **Decision Urgency**: Action needed within 1-6mo OR affects strategy
5. **Strategic Significance**: Shifts market landscape, fundraising environment, or competitive positioning
6. **Quantified Impact**: Measurable market size, funding amounts, valuation changes, CAC, burn rate

**Answer Requirements** (200-350w): ≥1 news item + summary + impact (≥2 phases, ≥2 roles, quantified) + decision (Enter/Pursue/Build/Wait/Defer/Pass/Avoid) + action timeline + optional evidence-backed projections (source, confidence, timeframe, ranges, scenarios).

## II. Requirements

**Q&A**: 4-6 total | 1-2/phase | 120-200w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Business Lifecycle Phases** (3-4, 1-2 Q each): Market Research & Validation, Fundraising (Pre-seed → Series A), Product-Market Fit, GTM & Growth (skip Incorporation, Scaling unless decision-critical)

**Category Coverage** (min): Funding ≥50%, Market ≥40%, Business/GTM ≥40%, Talent ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/12): Founder/CEO, CFO, Investor (Angel/VC/PE), VP Sales, Product Lead (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), M≥2-3 (market), F≥2-3 (funding), R≥2 (research), O≥1-2 (org dynamics), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Identify Domain**: Industry/market + date (e.g., "Fintech Q3-Q4 2024")

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-3d, search first): `"[Domain] funding|market entry|competitor|pricing"` + 1-3d

   **Tier 2** (7-14d if insufficient): Same + 7-14d

   **Sources** (whitelist, prioritize):
   - **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch
   - **Market**: Gartner, Forrester, CB Insights market maps, analyst blogs
   - **Business/GTM**: First Round Review, a16z, Lenny's Newsletter, SaaStr
   - **Regulatory**: SEC filings, regulator sites, legal blogs
   - **Talent**: LinkedIn Economic Graph, Carta, Layoffs.fyi
   - **Avoid**: PR fluff, rumors, listicles, speculation

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Crunchbase

3. **Curate** (≥10-15 candidates: Funding ≥4, Market ≥3, Business ≥2, Talent ≥2):
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, amounts, valuations)
   - ✅ Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 3-4 phases (1-2 each) × 3-4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | M# (market report, sizing, URL) | F# (funding, round, valuation, URL) | R# (research, findings, URL) | O# (org event: hiring/layoff/financing/leadership/exit, company, URL) | A# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

**Floors**: G≥8 (100% terms used), N≥4-5, M≥2-3, F≥2-3, R≥2, O≥1-2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (TAM, LTV, CAC, ARR, burn rate, runway, valuation multiples, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 2.5: Opportunistic Refresh (optional)

**Trigger** (refresh ONLY if):
1. Major funding (>$100M) or unicorn in 24-48h affecting ≥3 Qs
2. Significant market entry/acquisition affecting domain

**Actions**: Quick search (24-48h) → Add 1-2 items (mark "BREAKING") → Adjust 1-2 Qs → Document

**Default**: Skip (bi-weekly keeps fresh)

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[News] implications for [Phase]+[Roles]?" | "Market entry given [News]?" | "[Funding News]: response?" | "[News]: Enter/Wait/Pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 phases + quantified (market size $, funding $, burn rate, runway, valuation, TAM/SAM)
3. **Stakeholders** (~35w): ≥2 roles + concerns + actions
4. **Decision** (~50w): Enter/Pursue/Build/Wait/Defer/Pass/Avoid + rationale + criteria
5. **Action** (~20w): Immediate (0-2wk), Short (2wk-2mo) + owner
6. **Links**: Define at end: `[n1]: URL`

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 phases | ≥2 roles | Decision clear | 120-200w | Quantified | ≥1 cite | 0% hype | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Market maps, funding timelines, decision trees, burn rate scenarios, funding/valuation tables

**Format**: Mermaid (flows, timelines), Markdown tables (data), 2×2 matrices

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥8 (100% terms used) | N≥4-5 | M≥2-3 | F≥2-3 | R≥2 | O≥1-2 | A≥6

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 phases | Categories per % | ≥5 roles | Citations OK | 5 word samples 120-200w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Decision Criticality 100% | Impact 100% ≥2 phases+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-phase ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ M:__ F:__ R:__ O:__ A:__ Q:__ | ≥8,≥4-5,≥2-3,≥2-3,≥2,≥1-2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Phases** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Funding__% Market__% Business__% Talent__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/12 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%120-200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1-2 phases) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "Series A funding down 35% (Nov 2024): impact on burn rate?" | "Competitor $50M raise (Oct 2024): market entry strategy?" | "Fed rate 5.5% (Dec 2024): runway implications?" | "Down round trend (Q3 2024): bridge or cut burn?"

**✗ Bad**: "How does fundraising work?" (no news) | "What is TAM?" (overview) | "Should we start?" (no trigger) | "Competitor launched feature" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Market Research (Q1-Q2) | Fundraising (Q3-Q4) | PMF (Q5-Q6) | GTM (Q7-Q8)
4. References: G (G1-G8) | N (N1-N5) | M (M1-M3) | F (F1-F3) | R (R1-R2) | O (O1-O2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] M=[#] F=[#] R=[#] O=[#] A=[#]
```

### C. Phase Overview

| # | Phase | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Market Research | 1-2 | Market, Funding | [Top] | Founder, Investor |
| 2 | Fundraising | 1-2 | Funding, Macro | [Top] | Founder, CFO, Investor |
| 3 | Product-Market Fit | 1-2 | Market, Business | [Top] | Founder, Product Lead |
| 4 | GTM & Growth | 1-2 | Business, Talent | [Top] | Founder, VP Sales |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Phases** (≥2) | **Quantified**: Market [$TAM/SAM] | Funding [$] | Burn rate [$/mo] | Runway [mo] | Valuation [$]

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Enter/Pursue/Build/Wait/Defer/Pass/Avoid | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n1]: URL
---
```

### E. Reference Formats

```markdown
## 4. References

**G#. Term (Acronym)**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL

**M#. Title** (Firm, Date): Sizing (TAM/SAM) | URL

**F#. Company Funding** (Source, Date): Round | Amount | Valuation | URL

**R#. Title** (Firm, Date): Findings | URL

**O#. Company Event** (Source, MM/DD): Event (Hiring/Layoff/Financing/Leadership/Exit) | Company | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
```
