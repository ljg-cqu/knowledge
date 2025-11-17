# Startup & Formation Intelligence Q&A Generator

Use this as a self-contained prompt for an LLM to generate 4–6 decision-critical Q&As from recent startup news. Supports decisions on market entry, fundraising, product-market fit, and early GTM for founders and investors.

## Context & Scope

- **Cadence**: Bi-weekly, 4–6h effort. Valid for 2 weeks from generation date; include generation and expiry dates.
- **Domain**: Formation-stage startups (pre-seed–Series A) and corporate new-market initiatives.
- **Stakeholders**: Founder/CEO, CFO, Investor (angel/VC/PE), VP Sales, Product Lead.
- **Decision Horizon**: 6–18 months. Ignore intraday noise and long-term speculation unless blocking near-term decisions.
- **Assumptions**: Readers know basic metrics (ARR, CAC, LTV, TAM/SAM, burn, runway); need decision-ready synthesis.
- **Constraints**: Scannable in ≤30 minutes; avoid generic how-to content.
- **Usage**: Self-contained prompt; provide domain/geography, news period, stage/scale, runway/constraints, and ≥2 primary roles when calling LLM.

**Freshness Thresholds** (category-adaptive):

- **HV** (Market/Competition/Partnerships): ≥85% <1mo (≥30% in 1–3d), ≥95% <2mo, 100% ≤4mo
- **MV** (Funding/VC/Business Models/Talent/Macro): ≥70% <2mo (≥20% in 1–3d), ≥90% <3mo, 100% ≤6mo
- **LT** (Regulatory/Compliance): ≥50% <3mo, ≥75% <6mo, 100% ≤12mo (≤20% at 12–18mo if enduring)
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo
- **Validity**: 2 weeks; re-validate beyond expiry.

**Scope**: Decision-critical news only—funding, market entry, competition, business models/pricing, GTM, regulatory, partnerships, talent, macro shocks.

**Exclude**: Technical details, infrastructure, hype, rumors, trivial updates, stale news, mature-org optimization.

**News Categories** (each Q covers ≥2):

1. Market/Competition
2. Funding/VC
3. Business Models & GTM
4. Regulatory/Compliance
5. Partnerships/Ecosystem
6. Talent/Labor
7. Economic/Macro

**News Relevance** (must meet Recency + ≥1):

- Lifecycle impact: ≥2 phases or cross-phase.
- Stakeholder breadth: ≥3 roles or multi-role decision.
- Decision urgency: Action in 1–6 months or strategy change.
- Strategic significance: Alters fundraising, market, or competition.
- Quantified impact: Meaningful numbers (market size, funding, valuation, CAC, burn, etc.).

**Decision Criticality** (include if ≥1):

1. Blocks Decision: Impacts go/no-go on entry, product/GTM, fundraising, hiring.
2. Creates Risk: Increases failure risk (cash, competition, regulatory, talent).
3. Affects ≥2 Roles: Trade-offs across roles.
4. Requires Action: Decision/adjustment in 1–6 months.
5. Quantified Impact: Tied to hard numbers.

## Requirements

- **Q&A**: 4–6 total; ~150 words each; 100% news-triggered; ≥1 citation each, ≥30% with ≥2.
- **Phases** (3–4, 1–2 Q each): Market Research & Validation, Fundraising (Pre-seed–Series A), Product–Market Fit, GTM & Early Growth.
- **Category Coverage (min)**: Funding ≥50%, Market ≥40%, Business/GTM ≥40%, Talent ≥25%.
- **Decision Criticality**: 100% satisfy ≥1 criterion.
- **Stakeholders**: All 5 core roles across Q-set; each Q covers ≥2 roles.
- **References**: G≥8 (terms used), N≥4–5 (fresh), M≥2–3, F≥2–3, R≥2, O≥1–2, A≥6.
- **Visuals**: ≥2 diagrams + ≥1 table.
- **Quality Gates** (fail any = fix):

  1. Decision Criticality: 100% ≥1 criterion.
  2. News: 100% ≥1 fresh source; no PR/rumors.
  3. Impact: 100% ≥2 phases + ≥2 roles + quantified metrics.
  4. Decision: 100% explicit decision, rationale, timeline.
  5. Sources: ≥3 types; ≤50% from one; valid URLs.
  6. Actionability: 100% concrete.

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

- **Record generation date (YYYY-MM-DD)** and compute all news ages from it.

- **Domain**: Specify sector/vertical, geography, period, and stage (e.g., “B2B SaaS, US/EU, Q3–Q4 2024, Seed–Series A”).

- **Search** (≥10–15 candidates, tiered):

  - **Tier 1 (1–3d, search first)**:  
    `"[sector] seed OR series A funding"`  
    `"[sector] pricing|PLG|enterprise sales|GTM"`  
    `"[sector] competitor raise|acquisition|market entry"`  
    `"[sector] layoffs|hiring|exec change"`  
    `"[sector] regulatory|license|tax incentive"`  

  - **Tier 2 (7–14d)**: Same queries with 7–14d filters if Tier 1 is insufficient.

- **Sources** (whitelist, prioritize):

  - **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch.  
  - **Market/Business Models**: Gartner, Forrester, CB Insights market maps, a16z, First Round Review, Lenny’s Newsletter, SaaStr, credible founder/investor blogs.  
  - **Regulatory/Macro**: Official regulator/government sites, major newspapers, central bank/government releases.  
  - **Talent/Org**: LinkedIn Economic Graph, Carta, Layoffs.fyi, reputable press on hiring/layoffs and executive moves.  
  - **Avoid**: PR fluff, rumor sites, listicles without sources, generic think pieces with no data.

- **Curate** (≥10–15 candidates: Funding ≥4, Market ≥3, Business/GTM ≥2, Talent ≥2):

  - Meets Freshness thresholds.  
  - From whitelist or primary source.  
  - Satisfies ≥1 Decision Criticality criterion.  
  - Contains specific details (dates, round type, amounts, valuations, pricing changes, headcount).  
  - Relevant to ≥2 roles.

- **Verify**:

  - Check decision criticality and basic factual accuracy.  
  - Cross-check key metrics (round size, valuation, layoffs, macro figures) against at least one secondary source when available.  
  - If a candidate fails, replace it from earlier tiers.

- **Allocate**:

  - Plan 4–6 Qs across 3–4 phases (1–2 each), 3–4 categories (≥1 per Q), and all 5 core roles (plus any additional roles as needed).

### Step 2: Build References (Minimal)

- **Format**:  
  `G#` (term, definition + analogy, context)  
  `N#` (news, source, date, category, URL)  
  `M#` (market report, sizing, URL)  
  `F#` (funding, round, amount, valuation, URL)  
  `R#` (research, findings, URL)  
  `O#` (org/talent event: hiring/layoff/financing/leadership/exit, company, URL)  
  `A#` (APA 7th citation + tag).

- **Citation**: Markdown reference links: `[Ref: N1][n1]` in text; `[n1]: URL` at answer end.

- **Floors**: G≥8, N≥4–5, M≥2–3, F≥2–3, R≥2, O≥1–2, A≥6.

- **Glossary**: Only terms/acronyms used in Q&As (e.g., TAM, SAM, CAC, LTV, ARR, burn rate, runway, valuation multiples), each with a plain-language definition, 1–2 real-world analogies, why it matters for decisions, and at least one numeric example.

- **News Entry**:  
  `Title (Source, MM/DD): Summary | Category | URL | Decision-Critical criterion`

### Step 2.5: Opportunistic Refresh (optional, default: skip)

- **Trigger** (refresh only if):

  1. Major funding (e.g., >$100M) or new unicorn in 24–48h affecting ≥3 Qs.  
  2. Significant market entry/acquisition/regulatory change affecting the domain.

- **Actions**: Quick 24–48h search → add 1–2 “BREAKING” items → adjust 1–2 Qs → document in report.

### Step 3: Generate Q&A (batch 2–3; self-check each)

- **Before**: Review glossary and references. Track all terms used.

- **Patterns**:  
  - “[Funding news] implications for burn/runway and fundraising strategy?”  
  - “Market entry given [competitor raise/acquisition]?”  
  - “[Macro/regulatory change]: hiring and cash plan response?”  
  - “[News]: Enter now, wait, or pass?”

- **Avoid**: Generic questions, hype, unattributed claims, stale news, speculation.

- **Structure** (120–200w):

  1. **News** (~25w): What, when, why, category `[Ref: N#][n#]`.  
  2. **Impact** (~50w): ≥2 phases + quantified metrics (market size $, funding $, burn, runway, valuation, TAM/SAM), with baseline vs target or scenario ranges where sources allow.  
  3. **Stakeholders** (~35w): **[Role 1]** and **[Role 2]** concerns plus 1–2 concrete actions each.  
  4. **Decision & Alternatives** (~50w): Compare ≥2 realistic options (e.g., Enter now vs Wait 6–12mo vs Pass) with costs, risks, and benefits; state the recommendation and 2–3 measurable success targets (e.g., runway ≥X months, burn multiple ≤Y, probability of next round ≥Z%).  
  5. **Action** (~20w): **Immed (0–2wk)** and **Short (2wk–2mo)**: 1–3 specific tasks + owner each.  
  6. **Assumptions & Risks** (~20w): Critical assumptions, at least one material risk or counterargument, and when to revisit or reverse the decision.  
  7. **Links**: Define at end: `[n1]: URL`.

- **Self-Check (LLM)**:

  Age per freshness | Decision Criticality ✓ | ≥2 phases and ≥2 roles | Alternatives compared | Metrics with explicit targets | Assumptions & risks stated | Logic and numbers consistent | 120–200w | ≥1 citation (prefer ≥2 for high-impact items) | 0% hype/speculation | 100% actionable | All terms appear in the glossary.

### Step 4: Visuals (≥2 diagrams + ≥1 table)

- **Types**: Market maps, funding timelines, decision trees (enter/wait/pass), burn/runway scenario charts, valuation comparables tables.
- **Format**: Mermaid diagrams for flows/timelines; Markdown tables for numeric comparisons.

### Step 5: Final Checks

- **Refs**: 100% resolve; ages OK; floors met: G≥8, N≥4–5, M≥2–3, F≥2–3, R≥2, O≥1–2, A≥6.
- **Decision**: 100% decision + rationale + criteria + timeline.
- **Stakeholders**: All 5 core roles appear across the Q-set (each Q covers ≥2 roles); actions and authority clear.

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

- **Quantitative**: Floors met | Glossary 100% | 3–4 phases | Categories meet % targets | 5/5 core roles covered | Citations OK | 5 word samples 120–200w | Visuals OK | Decision 100% | Timeline 100% | Age per Freshness.

- **Qualitative**: News meets freshness, 0% hype/rumors | Decision Criticality 100% | Impact 100% (≥2 phases+roles+quantified) | Decision 100% | Source diversity ≥3 types | Each phase backed by ≥1 news+analysis | Links valid | Quantification consistent with sources | 100% actionable | Evidence 100% | Search documented.

### Step 7: Submit

- **Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | No placeholders | Visuals, citations, impact, decision, timeline, categories, and roles all OK | **Freshness OK** | Evidence 100% | URLs valid | Generation and expiry dates set (gen + 2 weeks) | Search documented.

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1–3d:__%), __%<2mo \| MV: __%<2mo (1–3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ M:__ F:__ R:__ O:__ A:__ Q:__ | ≥8,≥4–5,≥2–3,≥2–3,≥2,≥1–2,≥6,4–6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%; ≥50% | | PASS/FAIL |
| 4 | **Phases** | __/3–4 (1–2Q each); total__ | 3–4/3–4; 4–6 | | PASS/FAIL |
| 5 | **Categories** | Funding__% Market__% Business__% Talent__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/5 | 5/5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2 phases + 2 roles + quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision + rationale + criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __% ≥1 cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __% 120–200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__ ; tab__ | ≥2; ≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__% (1–3d__%) 1–2mo__% 2–4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 9 = rewrite)

**Criteria**: News-driven (per Freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1–2 phases) | Multi-stakeholder (≥2 roles) | Quantified impact with explicit targets | Comparative (≥2 alternatives with trade-offs) | Assumptions & risks explicit | Timely | Actionable.

**✓ Good**: "Series A funding down 35% (Nov 2024): impact on burn rate?" | "Competitor $50M raise (Oct 2024): market entry strategy?" | "Fed rate 5.5% (Dec 2024): runway implications?" | "Down round trend (Q3 2024): bridge or cut burn?"

**✗ Bad**: "How does fundraising work?" (no news) | "What is TAM?" (overview) | "Should we start?" (no trigger) | "Competitor launched feature" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Market Research (Q1-Q2) | Fundraising (Q3-Q4) | PMF & GTM (Q5-Q6, as needed)
4. References: G (G1-G8) | N (N1-N5) | M (M1-M3) | F (F1-F3) | R (R1-R2) | O (O1-O2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5 core roles (+ others if used)] | **Refs**: G=[#] N=[#] M=[#] F=[#] R=[#] O=[#] A=[#]
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
