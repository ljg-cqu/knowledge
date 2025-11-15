# Startup & Formation Intelligence Q&A Generator

Generate 18–22 Q&As analyzing industry news across 7 categories, 6 business lifecycle phases, 12 stakeholder roles—transforming news into actionable intelligence for founders, investors, market entrants.

**Target**: 1-2 days | Bi-weekly | Funding/Market (medium-velocity) + Regulatory/Macro (long-tail)

**Scope**: Market entry, competitive positioning, fundraising, business model validation, GTM strategy, team formation.

**MECE Position**: Covers all functions (technical, commercial, product, financial, strategic) during **formation stage only** (pre-seed → Series A), software and non-software industries. Formation-stage decisions require cross-functional integration.

**For Established Organizations**: Not for ongoing operational optimization in mature organizations—use specialized prompts (Product & Market Intelligence, Technical Operations, Commercial Operations, Financial & Economic, Strategic & Innovation).

**Freshness Guarantee** (category-adaptive thresholds):
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

### Quantitative Floors

**Q&A**: 18-22 total | 3-4 per phase | 200-350w | 100% news-driven | ≥85% ≥1 cite, ≥40% ≥2 cites | Each covers ≥2 categories + impact + decision

**Business Lifecycle Phases** (6, 3-4 Q each): (1) Market Research & Validation, (2) Incorporation & Legal Setup, (3) Fundraising (Pre-seed → Series A+), (4) Product-Market Fit, (5) GTM & Growth, (6) Scaling & Expansion

**Category Coverage**: Market 85%, Funding 70% (≥30% specific fundraising rounds/valuations/exits), Business/GTM 65%, Regulatory 40%, Partnerships 75%, Talent 45% (≥20% org dynamics: hiring/layoffs/exec moves), Macro 50%

**Decision Framework** (100%): Impact (≥2 phases, ≥2 roles, quantified) + Decision (Enter/Pursue/Build/Wait/Defer/Pass/Avoid + rationale + alts) + Action Plan (immediate/short/medium)

**Stakeholders** (≥9/12): Founder/CEO, Co-founder, CFO, Investor (Angel/VC/PE), Board Member, Advisor, VP Sales, VP Marketing, Product Lead, Legal/Compliance, HR/Talent Lead, Finance/Controller

**References** (build before Q&A): G≥15 (100% business terms/acronyms/concepts with analogies/formulas), N≥10, M≥6, F≥6, R≥5, O≥5 (org dynamics), A≥18 (APA 7th+tag)

**Visuals**: ≥10 diagrams + ≥5 tables

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

1. **News**: 100% cite ≥1 item per freshness guarantee; 0% marketing/rumors
2. **Impact**: 100% specify ≥2 phases + ≥2 roles + quantified (market sizing, funding, customer economics)
3. **Decision**: 100% decision + rationale + timeline + success criteria + metrics
4. **Sources**: ≥5 types, max 35%/type; per phase ≥1 news + ≥1 market analysis; 100% URLs valid, [Ref: ID] resolve
5. **Coverage**: ≥9/12 roles; categories per floors
6. **Actionability**: 100% concrete steps + timelines; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation

**Record generation date (YYYY-MM-DD)—all news ages calculated from this date.**

1. **Identify Domain**: Industry/market + date (e.g., "Fintech Q3-Q4 2024")

2. **Web Search** (≥35-45 candidates, tiered):

   **Tier 1 - Daily/Breaking** (1-3 days, search first):
   - Market: `"[Domain] market entry|expansion|launch|competitor"` + past 1-3d
   - Funding: `"[Domain] raised|funding|Series A|seed|valuation"` + past 1-3d
   - Competition: `"[Domain] acquisition|merger|market share"` + past 1-3d
   - Ecosystem: `"[Domain] partnership|integration|platform launch"` + past 1-3d
   - Business Model: `"[Domain] pricing|GTM|PLG|enterprise"` + past 1-3d

   **Tier 2 - Recent** (7-14 days if T1 insufficient):
   - All HV: Same queries + past 7-14d

   **Tier 3 - Backfill** (2-4 weeks if T1+T2 insufficient):
   - HV: Same queries + past 2-4wks
   - MV/LT: `"[Domain] VC trends|down round|IPO|regulatory filing|compliance"` + past 2-6mo

   **Tier 1.5 - Org Dynamics** (1-7 days, parallel with T1, target 5-7):
   - Hiring: `"[Competitor] hiring|recruiting|team expansion|acqui-hire"` + past 1-7d
   - Layoffs: `"[Competitor] layoffs|restructuring|workforce cuts"` + past 1-7d
   - Fundraising: `"[Competitor] raised|Series A|B|C|seed|valuation|down round|bridge"` + past 1-7d
   - Leadership: `"[Competitor] CEO|CFO|CTO|VP Sales|VP Marketing|joined|departed"` + past 1-7d
   - Exits: `"[Domain] acquisition|IPO|acqui-hire|M&A"` + past 1-7d

   **Source Whitelist**:
   - **Funding/VC**: Crunchbase, PitchBook, CB Insights, TechCrunch, VentureBeat, The Information, Axios Pro Rata, StrictlyVC, Term Sheet
   - **Market/Competition**: Gartner, Forrester, IDC, CB Insights market maps, G2 category reports, analyst blogs
   - **Business/GTM**: First Round Review, a16z, Sequoia, NFX, Reforge, Lenny's Newsletter, SaaStr
   - **Regulatory**: SEC filings, regulator sites (FDA/FCC/CFPB), legal blogs (Cooley, Wilson Sonsini)
   - **Macro/Economic**: WSJ, FT, Bloomberg, The Economist, Fed, McKinsey/BCG/Bain
   - **Talent**: LinkedIn Economic Graph, Carta, Levels.fyi, Glassdoor, Pave
   - **News Aggregators**: HN, Reddit r/startups, Twitter/X (verified founders/VCs)
   - **Org Dynamics**: Crunchbase, PitchBook, Layoffs.fyi, LinkedIn, AngelList, company press releases, SEC filings
   - **Avoid**: PR aggregators, SEO farms, unverified social

   **Search Tools** (real-time indexing):
   - Perplexity AI: "past week"/"past month" in query
   - ChatGPT Search: "latest"/"recent" in query
   - Google: `after:YYYY-MM-DD` operator
   - Crunchbase: Filter by date, funding type
   - PitchBook: Search by quarter, industry

   **Age Distribution Target**:
   - HV (Market/Competition/Partnerships): <1mo ≥85% (1-3d ≥30%), 1-2mo ≥10%, 2-4mo ≤5%
   - MV (Funding/VC/Business/Talent/Macro): <2mo ≥70% (1-3d ≥20%), 2-3mo ≥20%, 3-6mo ≤10%
   - LT (Regulatory): <3mo ≥50%, 3-6mo ≥25%, 6-12mo ≤20%, 12-18mo ≤5%
   - Overall: <1mo ≥50%, 1-2mo ≥25%, 2-4mo ≥12%, 4-6mo ≥8%, 6-12mo ≤4%, 12-18mo ≤1%

3. **Curate & Validate** (≥24: Market ≥7, Funding ≥5, Business/GTM ≥4, Reg ≥3, Partnerships ≥4, Talent ≥3, Macro ≥3, Org Dynamics ≥5):
   - ✅ Age per freshness guarantee
   - ✅ Source from whitelist OR verified primary
   - ✅ Meets ≥2 relevance criteria
   - ✅ Not marketing/rumors/trivial
   - ✅ Specific details (dates, amounts, market sizes, valuations, headcounts)

4. **Verify Distribution**: Count by category/age; if fails freshness guarantee, return to Step 2 earlier tiers

5. **Allocate**: 18-22 Q across 6 phases (3-4 each), 7 categories (≥2 per Q), 12 roles (≥9 total)

6. **Refresh**: Not required (bi-weekly cadence keeps news fresh)

### Step 2: Build References (before Q&A)

**Format**: G# (term, def with analogy/formula, context) | N# (news, source, date, category, impact, URL) | M# (market report, findings, sizing, URL) | F# (funding, round details, valuation, URL) | R# (research, firm, date, insights, URL) | O# (org event: hiring/layoff/financing/leadership/exit, company, details, implication, URL) | A# (APA 7th+tag)

**Citation Style**: Markdown reference-style links: `[Ref: N1][n1]` in text, define `[n1]: URL` at answer end.

**Floors**: G≥15 (100% business terms/acronyms/metrics/concepts), N≥10 (100% URLs+dates), M≥6, F≥6, R≥5, O≥5, A≥18

**Glossary Requirements**:
- **Coverage**: ALL business terms/acronyms (TAM, LTV, CAC, ARR, MRR, ACV, etc.), metrics (burn rate, runway, valuation multiples), concepts (PLG, land-and-expand, down round, bridge financing, etc.). Prioritize specialized/VC/legal terms.
- **Clarity**: Plain language definitions (avoid circular jargon). Define term before using in definition.
- **Analogies**: Real-world comparisons (e.g., "TAM is total ocean size; SAM is fishable part; SOM is fish you catch this year").
- **Formulas**: Include calculations (e.g., "LTV = ARPU × (1 / Churn Rate)", "Burn Multiple = Net Burn / Net New ARR").
- **Context**: Why term matters in startup context. Connect to funding, growth, or competitive impact.
- **Examples**: Concrete numbers (e.g., "$50M ARR at 5x = $250M valuation").

**News Entry**: **Title** (Source, MM/DD/YYYY): Summary | Cat | Age: X d/mo | Impact | Stakeholders | URL | Justification if HV >1mo OR Reg >6mo

### Step 2.5: Opportunistic Refresh (optional)

**Trigger** (refresh ONLY if):
1. Major funding (>$100M) or unicorn in 24-48h affecting ≥3 Qs
2. Significant market entry/acquisition affecting domain

**Actions**: Quick search (24-48h) → Add 1-2 items (mark "BREAKING") → Adjust 1-2 Qs → Document

**Default**: Skip (bi-weekly keeps fresh)

### Step 3: Generate Q&A (batch 4-5, self-check each)

**Before Starting**: Review glossary (G1-G15+). Track ALL business terms/acronyms/metrics/concepts used. After each batch, verify 100% defined with analogies/formulas. Add missing immediately.

**Question Patterns**: "[News] implications for [Phase] and [Roles]?" | "Market entry given [News]?" | "[Funding News]: What it means for [Phase]?" | "[News A] vs [News B] across [Segments]?" | "[Trend] + [Projection]: prepare for [Impact]?" | "Should [Founder/Investor] [Enter/Wait/Pass] given [News]?"

**Avoid**: Generic "What is X?", tech implementation, operational tooling, unattributed speculation, stale news

**Answer Structure** (200-350w):
1. **News** (~50w): What, when, who, why, category `[Ref: N#][n#], [Ref: M#][m#], [Ref: F#][f#]`
2. **Impact** (~90w): ≥2 phases + quantified (market size, funding, customer economics, burn rate, runway, valuation, TAM/SAM)
3. **Stakeholders** (~60w): ≥2 roles + concerns + actions + authority (include Founder/CEO/Investor for strategic)
4. **Decision** (~70w): Enter/Pursue/Build/Wait/Defer/Pass/Avoid + rationale + 1-2 alts + success criteria (traction, funding milestones, acquisition)
5. **Action** (~50w): Immediate (0-2wks), Short (2wks-2mo) with owner + deliverable
6. **Projections** (opt ~30w): "[Source] projects [outcome] by [time] with [confidence]. Impact: [ranges]" `[Ref: R#][r#]`
7. **Link Definitions**: At end: `[n1]: URL`, `[m1]: URL`
8. **Artifacts**: 1-2 diagrams/tables

**Batch Self-Check**: News age ✓ | ≥2 phases | ≥2 roles | Decision clear | 200-350w | Quantified | ≥3/5 ≥2 cites | Artifact | Timeline | 0% hype | 100% actionable | Projections attributed+confident+timed | **All terms in glossary with analogies/formulas**

### Step 4: Create Visuals (≥10 diagrams + ≥5 tables, ≥60% referenced)

**Types**: Market maps, competitive positioning, funding timelines, TAM/SAM/SOM funnels, decision trees, stakeholder tables, burn rate scenarios, valuation comparisons, GTM channel matrices, roadmaps

**Format**: Mermaid (flowcharts/timelines/quadrants), Markdown tables (funding, sizing, economics, burn rate), 2×2 matrices (positioning, attractiveness)

### Step 5: Final Checks

**References**: 100% [Ref: ID] resolve | All news age ✓ | Fields complete | APA tags | G≥15 (100% terms with analogies/formulas) | N≥10 (7 cats) | M≥6 | F≥6 | R≥5 | O≥5 | A≥18 (45-65% news, 20-30% reports)

**Decision**: 100% decision + rationale + alts + success criteria + timeline + metrics

**Stakeholders**: ≥9/12 roles | Specific actions + authority | Cross-role coordination | Founder/Investor for strategic

### Step 6: Run Validations (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors (G≥15, N≥10, M≥6, F≥6, R≥5, O≥5, A≥18, Q=18-22) | Glossary (100% terms, ≥60% analogies/formulas) | 6 phases (3-4 Q each) | Categories (Market 85%, Funding 70% ≥30% rounds, Business 65%, Reg 40%, Partnerships 75%, Talent 45% ≥20% org dynamics, Macro 50%) | Stakeholders ≥9/12 | Citations (100% ≥1 news, ≥85% ≥1 cite, ≥40% ≥2) | Distribution (News 45-65%, Reports 20-30%, Docs 10-20%) | Words (5 samples, 100% 200-350) | Visuals (≥60% ref, ≥10 diagrams, ≥5 tables) | Decision 100% + metrics | Timeline 100% | **News age ✓**

**Qualitative**: News (freshness ✓, 0% marketing) | Impact (100% ≥2 phases + ≥2 roles + quantified) | Decision (100% + alts + criteria) | Source diversity (≥5 types, max 35%) | Per-phase (≥1 news + ≥1 analysis) | Links (100% valid) | Cross-refs (100% resolve) | Quantification (100%) | Actionability (100% concrete, 0% abstract) | Anti-hype (0% marketing, 100% evidence) | Projections (100% attributed, confidence+time) | Web search doc (queries, sources, count)

### Step 7: Submit

**Final Checklist** (all YES): All validations PASS | Floors met | **Glossary complete (100% terms, ≥60% analogies/formulas)** | TOC complete (6 phases, Q ranges) | 0 placeholders | ≥10 diagrams + ≥5 tables | 100% cite ≥1 news | 100% impact (≥2 phases, ≥2 roles, quantified) | 100% decision + rationale + metrics | 100% timeline | 7 categories per thresholds (Funding 70% ≥30% rounds, Talent 45% ≥20% org dynamics) | ≥9/12 roles | **Freshness met** | 0% speculation, 100% evidence | Projections attributed+confident+timed | URLs valid | Balanced | **Gen + expiration dates (start + 2wks)** | Search queries + sources documented

## IV. Validation Report

Use Step 6 validation criteria. Fill table:

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **News Freshness** | HV: __% <1mo (1-3d: __%), __% <2mo, __% ≤4mo \| MV: __% <2mo (1-3d: __%), __% <3mo, __% ≤6mo \| LT: __% <3mo, __% <6mo, __% ≤12mo \| Overall: __% <2mo, __% <4mo, __% <6mo, __% ≤12mo | Per freshness guarantee (see header) | | PASS/FAIL |
| 2 | **Reference Floors** | G:__ N:__ M:__ F:__ R:__ O:__ A:__ Q:__ | ≥15, ≥10, ≥6, ≥6, ≥5, ≥5, ≥18, 18-22 | | PASS/FAIL |
| 2a | **Glossary Coverage** | __% business/funding terms/acronyms/concepts defined; __% with analogies/formulas; __% unfamiliar terms covered | 100%; ≥60%; 100% | | PASS/FAIL |
| 3 | **Lifecycle Coverage** | Phases __/6 (3-4 Q each); total Q __ | 6/6; 18-22 | | PASS/FAIL |
| 4 | **Category Coverage** | Market __%, Funding __%, Business __%, Reg __%, Partnerships __%, Talent __%, Macro __% | ≥85%, ≥70%, ≥65%, ≥40%, ≥75%, ≥45%, ≥50% | | PASS/FAIL |
| 5 | **Stakeholder Coverage** | Roles __/12 | ≥9 | | PASS/FAIL |
| 6 | **Impact** | __% specify ≥2 phases + ≥2 roles + quantified | 100% | | PASS/FAIL |
| 7 | **Decision** | __% decision + rationale + alts | 100% | | PASS/FAIL |
| 8 | **Timelines** | __% immediate/short/medium + owners | 100% | | PASS/FAIL |
| 9 | **Citations** | __% ≥1 news; __% ≥1 cite; __% ≥2 cites | 100%; ≥85%; ≥40% | | PASS/FAIL |
| 10 | **Source Distribution** | News __%, Market/Funding Reports __%, Other __% | 45-65%, 20-30%, 10-20% | | PASS/FAIL |
| 11 | **Source Diversity** | Types __; max %/type __ | ≥5; ≤35% | | PASS/FAIL |
| 12 | **Per-Phase Evidence** | __/6 phases ≥1 news + ≥1 market/funding analysis | 6/6 | | PASS/FAIL |
| 13 | **Word Count** | 5 samples: __% in 200-350w | 100% | | PASS/FAIL |
| 14 | **Visuals** | __% ref artifacts; diagrams __; tables __ | ≥60%; ≥10; ≥5 | | PASS/FAIL |
| 15 | **Quantification** | __% measurable impact | 100% | | PASS/FAIL |
| 16 | **Links** | __% URLs valid | 100% | | PASS/FAIL |
| 17 | **Cross-Refs** | __% [Ref: ID] resolve | 100% | | PASS/FAIL |
| 18 | **Actionability** | __% concrete; __% abstract | 100%; 0% | | PASS/FAIL |
| 19 | **Projections** | If used: __% attributed; __% confident; __% timed; __% scenarios | 100%; 100%; 100%; 100% | | PASS/FAIL |
| 20 | **Search Quality** | Queries: Y/N \| Whitelist: Y/N \| Candidates: __ \| Accept: __% | Y; Y; ≥35; 50-70% | | PASS/FAIL |
| | **Metadata** | Start: __ \| End: __ \| Expires: [+2wks] \| Refresh: Y/N (__) | | INFO |
| | **Age Distribution** | <1mo __% (1-3d __%, 4-14d __%, 15-30d __%) \| 1-2mo __% \| 2-4mo __% \| 4-6mo __% \| 6-12mo __% \| 12-18mo __% \| By category: HV __%, MV __%, LT __% | Per freshness guarantee (see header) | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (fails ≥3 of 11 = rewrite)

**Criteria**: News-driven (freshness ✓) | Lifecycle-specific (1-2 phases, clear impact) | Multi-stakeholder (≥2 roles) | Multi-category (≥2 types) | Decision-focused | Quantified impact | Cross-phase aware | Timely urgency | Alternative-aware (1-2 strategies) | Evidence-based | Actionable | Forward-looking (if projections)

**✓ Good**: 
- "Anthropic $4B Amazon investment (Sept 2024): implications for AI Infrastructure founders fundraising Series A?"
- "Stripe $65B vs Plaid $13B (March 2024): fintech market entry strategies?"
- "Fed rate 5.5% (Dec 2024): impact on seed-stage burn rate and runway for B2B SaaS?"
- "Down round trend Q3 2024 (+35%): bridge financing or cut burn?"
- "EU AI Act (Aug 2026): market entry barriers for US AI startups in Europe?"

**✗ Bad**: "How does fundraising work?" (no news) | "What is TAM?" (overview) | "Should we start?" (no trigger) | "PostgreSQL 17 2x JSON perf" (tech ops)

## VI. Output Format

### A. TOC Structure

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Overview | Insights | Dashboard)
2. Phase Coverage (6 phases × 7 categories matrix)
3. Questions by Phase: Market Research (Q1-Q4) | Incorporation (Q5-Q7) | Fundraising (Q8-Q11) | PMF (Q12-Q15) | GTM (Q16-Q19) | Scaling (Q20-Q22)
4. References: G (G1-G20+) | N (N1-N12+) | M (M1-M8+) | F (F1-F8+) | R (R1-R6+) | O (O1-O7+) | A (A1-A20+)
5. Validation Report (20 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Market/Industry] | **Period**: [Q3-Q4 2024] | **Coverage**: [# items, 7 categories]

**News**: Market ([#]: top 2-3 + dates) | Funding ([#]: top 2-3) | Business/GTM ([#]: top 1-2) | Reg ([#]: top 1) | Partnerships ([#]: top 1-2) | Talent ([#]: top 1) | Macro ([#]: top 1)

**Insights**: [News] ([Date]): [Impact] → [Decision] → [Timeline] (repeat 2-3 high-impact)

**Dashboard**: [Table: Phase | News | Action | Timeline]

**Roles**: [9-11 with counts] | **Refs**: G=[#] N=[#] M=[#] F=[#] R=[#] O=[#] A=[#]
```

### C. Business Lifecycle Phase Overview Table

| # | Phase | Range | Count | Categories | News | Roles | Artifacts |
|---|-------|-------|-------|------------|------|-------|-----------|
| 1 | Market Research | Q1-Q4 | 3-4 | Market, Competition, Reg, Macro | [Top] | Founder, Advisor, Investor | 2D+1T |
| 2 | Incorporation | Q5-Q7 | 3-4 | Reg, Legal, Funding | [Top] | Founder, Legal, Advisor | 2D+1T |
| 3 | Fundraising | Q8-Q11 | 3-4 | Funding, VC, Macro | [Top] | Founder, CFO, Investor | 2D+1T |
| 4 | Product-Market Fit | Q12-Q15 | 3-4 | Market, Business/GTM, Talent | [Top] | Founder, Product, VP Sales | 2D+1T |
| 5 | GTM & Growth | Q16-Q19 | 3-4 | Business/GTM, Partnerships, Market | [Top] | VP Sales, VP Marketing, Founder | 2D+1T |
| 6 | Scaling | Q20-Q22 | 3-4 | Talent, Partnerships, Macro, Funding | [Top] | CEO, CFO, Board, VP Sales | 2D+1T |
| | **Total** | | **18-22** | **All 7** | **12+** | **≥9/12** | **≥10D+≥5T** |

Legend: D=Diagrams, T=Tables

### D. Q&A Format

```markdown
### Q#: [News Question + Phase + Roles + Decision]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓✓] | **Decision**: Y

**News** (~50w): What, when, who, why, category [Ref: N#][n#], [Ref: M#][m#], [Ref: F#][f#]

**Impact** (~90w): **Phases** (≥2) | **Quantified**: Market [$TAM/SAM/SOM] | Funding [$amounts/valuations] | Customer [LTV/CAC] | Burn Rate [$/mo] | Runway [months] | Valuation [$ or multiples]

**Stakeholders** (~60w): **[Role 1]**: Concerns, actions, authority | **[Role 2]**: Concerns, actions, authority

**Decision** (~70w): **Rec**: Enter/Pursue/Build/Wait/Defer/Pass/Avoid | **Rationale**: [Why] | **Alts**: [1-2 options] | **Success**: [Measurable metrics]

**Action** (~50w): **Immed (0-2wks)**: [Actions+owner] | **Short (2wks-2mo)**: [Actions+owner]

**Projections** (opt ~30w): [Source] projects [outcome] by [time] with [confidence]. Impact: [ranges] [Ref: R#][r#]

**Artifacts**: [Type]

<!-- Link Definitions -->
[n1]: URL
[m1]: URL
[f1]: URL

---
```

### E. Reference Formats

```markdown
## 4. References

### 4.1 Glossary (G1-G20+)
**G#. Term (Acronym)**: Plain-language def | Analogy/Formula | Startup context | Why it matters | Example

**Example**:
- **G1. TAM (Total Addressable Market)**: Total revenue opportunity at 100% market share.
- **G2. LTV (Lifetime Value)**: Total revenue expected from a customer over their relationship.

### 4.2 News (N1-N12+)
**N#. Title** (Source, MM/DD/YYYY): Summary | Cat | Impact (phases, metrics) | Roles | URL

### 4.3 Market Reports (M1-M8+)
**M#. Title** (Firm, Date): Sizing (TAM/SAM/SOM) | Growth rate | Landscape | Trends | Relevance | URL

### 4.4 Funding Sources (F1-F8+)
**F#. Company Funding** (Source, Date): Round (Seed/Series A/B/C) | Amount | Valuation | Lead investor | Use | Impact | URL

### 4.5 Research/Analysis (R1-R6+)
**R#. Title** (Firm, Date): Findings | Projections | Implications | Confidence | Relevance | URL

### 4.6 Organizational Dynamics (O1-O7+)
**O#. Company Event Type** (Source, MM/DD/YYYY): Event (Hiring/Layoff/Financing/Leadership/Exit) | Company | Details | Context | Implication | Impact | URL

### 4.7 Citations (A1-A20+)
**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub/Firm. URL [News/Market Report/Funding/Research/Org]
