# Startup & Formation Intelligence Q&A Generator (Minimal Viable)

Use this specification as a single, self-contained prompt for an LLM to generate 4–6 decision-critical Q&As from recent startup/formation news. The goal is to support fast, high-quality decisions on market entry, fundraising, product–market fit, and early GTM for founders and investors.

## I. Context & Scope

- **Cadence & Effort**: Bi-weekly, 4–6h analyst effort. Output valid for 2 weeks from the generation date; always state generation and expiry dates.
- **Domain**: Formation-stage startups (pre-seed–Series A) and corporate new-market initiatives.
- **Stakeholders**: Founder/CEO, CFO, Investor (angel/VC/PE), VP Sales, Product Lead (core roles).
- **Decision Horizon**: 6–18 month runway/planning window. Ignore intraday noise and very long-term speculation unless it blocks a near-term decision.
- **Assumptions**: Readers know basic startup metrics (ARR, CAC, LTV, TAM/SAM, burn, runway) and need decision-ready synthesis, not tutorials.
- **Constraints**: Brief must be scannable in ≤30 minutes; avoid generic startup how-to content.
- **Self-contained usage**: Treat this file as the full prompt; do not rely on previous answers or other files. Put all necessary context into a single LLM call.
- **LLM Call**: When calling the LLM, provide domain/geography, news period, startup stage and scale, runway and key constraints, and primary roles (≥2 of the core roles), and instruct it to follow Sections I–VI and output a Markdown report.

**Freshness** (category-adaptive thresholds):

- **HV** (Market/Competition/Partnerships): ≥85% <1mo (≥30% in 1–3d), ≥95% <2mo, 100% ≤4mo
- **MV** (Funding/VC/Business Models/Talent/Macro): ≥70% <2mo (≥20% in 1–3d), ≥90% <3mo, 100% ≤6mo
- **LT** (Regulatory/Compliance): ≥50% <3mo, ≥75% <6mo, 100% ≤12mo (≤20% at 12–18mo if enduring impact)
- **Overall**: ≥70% <2mo, ≥85% <4mo, ≥95% <6mo, 100% ≤12mo
- **Validity**: 2 weeks from generation (per expiry date in the report); re-validate if used beyond expiry.

**Scope**: Decision-critical startup news only—funding environment, market entry barriers and opportunities, competitive moves, business model & pricing, GTM strategies, regulatory barriers/incentives, partnerships & ecosystem, talent/execution risk, macro shocks.

**Exclude**: Technical implementation details, infrastructure/tooling choices, pure marketing hype, unverified rumors, trivial product updates, stale news outside freshness rules, and mature-organization optimization (for those, use other templates).

**News Categories** (each Q covers ≥2):

1. **Market/Competition**
2. **Funding/VC**
3. **Business Models & GTM**
4. **Regulatory/Compliance**
5. **Partnerships/Ecosystem**
6. **Talent/Labor**
7. **Economic/Macro**

**News Relevance** (must meet Recency + ≥1):

- Lifecycle impact: affects ≥2 phases or cross-phase coordination.
- Stakeholder breadth: relevant to ≥3 roles or a multi-role decision.
- Decision urgency: action needed in 1–6 months or affects strategy.
- Strategic significance: changes fundraising environment, market landscape, or competitive position.
- Quantified impact: meaningful numbers (market size, funding amounts, valuation changes, CAC, burn rate, etc.).

**Decision Criticality Framework** (include news/Q if ≥1):

1. **Blocks Decision**: Directly impacts go/no-go on market entry, major product/GTM bet, fundraising, or key hiring.
2. **Creates Risk**: Materially increases risk of failure (cash crunch, competitive displacement, regulatory/tax shock, execution/talent risk).
3. **Affects ≥2 Roles**: Requires trade-offs across Founder, CFO, Investor, Sales, Product, etc.
4. **Requires Action**: Needs decision/adjustment within 1–6 months.
5. **Quantified Impact**: Tied to hard numbers (funding/valuation, pricing, CAC/LTV, burn/runway, TAM/SAM, headcount, macro indicators).

## II. Requirements

- **Q&A**: 4–6 total; 120–200 words; 100% news-triggered; 100% with ≥1 citation, ≥30% with ≥2.
- **Business Lifecycle Phases** (3–4, 1–2 Q each): Market Research & Validation, Fundraising (Pre-seed–Series A), Product–Market Fit, GTM & Early Growth (skip Incorporation and Scaling unless decisively affected).
- **Category Coverage (min)**: Funding ≥50% of Qs, Market ≥40%, Business/GTM ≥40%, Talent ≥25% (optional, as news allows).
- **Decision Criticality**: 100% of Qs satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified).
- **Stakeholders**: All 5 core roles appear across the Q-set (each Q covers ≥2 roles), with a focus on Founder/CEO, CFO, Investor, VP Sales, Product Lead.
- **References (build before Q&A)**: G≥8 (all terms used), N≥4–5 (per freshness), M≥2–3 (market), F≥2–3 (funding), R≥2 (research), O≥1–2 (org/talent events), A≥6 (APA 7th + tag).
- **Visuals**: ≥2 diagrams + ≥1 table in the final report.
- **Quality Gates** (fail ANY = stop and fix):

  1. **Decision Criticality**: 100% satisfy ≥1 criterion.  
  2. **News**: 100% cite ≥1 source meeting freshness; 0% PR/rumors.  
  3. **Impact**: 100% cover ≥2 phases + ≥2 roles + quantified metrics (market size, funding, burn, runway, valuation, TAM/SAM).  
  4. **Decision**: 100% contain explicit decision, rationale, and timeline.  
  5. **Sources**: ≥3 source types; ≤50% from any one type; all URLs valid.  
  6. **Actionability**: 100% concrete; no vague advice.

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
