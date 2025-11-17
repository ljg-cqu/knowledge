# Commercial Operations News Intelligence Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent commercial news—minimal viable tracking for informed decisions with limited time.

**Target**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Sales, Marketing): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (CS, RevOps, Competitive): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical commercial news only—sales execution, marketing ops, customer success, RevOps, GTM, competitive intel. For post-PMF organizations.

**Exclude**: Technical implementation, product strategy/pricing research, corporate finance (except GTM pricing), long-term strategy, rumors, marketing fluff, stale news, nice-to-have trends.

**How the LLM should use this file**

 - **Role**: Act as a Commercial Operations news intelligence analyst for a post-PMF company.
 - **Inputs (fill before running)**:
   - Domain and vertical (e.g., B2B SaaS, fintech, region).
   - Period (e.g., last 2 weeks, Q4 2024).
   - Company context: size, stage, regions, primary GTM motions, main products, average contract value.
   - Baseline metrics: recent pipeline $, win rate, CAC, LTV, GRR/NRR, churn, key conversion rates.
   - Stakeholders and their goals: CRO, VP Sales, VP Marketing, VP CS, RevOps analyst, others as relevant.
   - Constraints: budget, hiring limits, regulatory or contractual boundaries.
 - **Objective**: Using only the instructions in this file (no other prompt files), produce:
   - An executive summary.
   - A stage coverage overview.
   - 4–6 Q&As that satisfy all requirements below.
   - Glossary and reference sections (G, N, P, M, R, A) with citations.
   - At least 2 diagram descriptions and 1 table in Markdown.
   - A completed validation report.
 - **Output expectations**:
   - Respect word counts and freshness thresholds.
   - Focus on high-impact news that meets the decision criticality framework.
   - Prefer concrete numbers, formulas, and thresholds over vague language.
   - Cover multiple stakeholder viewpoints and explicitly describe trade-offs, risks, and limitations.

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts quota strategy, GTM pivot, or revenue model
2. **Creates Risk**: Material competitive threat, churn signal, or CAC/LTV pressure
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (Sales + RevOps, Marketing + CS, etc.)
4. **Requires Action**: 1-6mo action window (not speculative)
5. **Quantified Impact**: Revenue $, pipeline $, conversion %, retention %, or efficiency gain

**Categories** (3-4, each Q covers ≥1):
1. **Sales Performance & Pipeline**: Win rates, quota attainment, pipeline velocity, sales cycle changes
2. **Marketing Performance & Attribution**: CAC, conversion rates, campaign effectiveness, attribution model shifts
3. **Customer Success & Retention**: Churn, NRR, expansion, retention tactics affecting revenue
4. **Revenue Operations & Analytics** (optional): RevOps tools, analytics platforms, data infrastructure affecting decisions

**Answer Structure** (120–200 words): News (what, when, why) + impact (quantified, ≥2 stages, ≥2 roles) + decision options (compare at least two choices such as Adopt/Test/Scale/Defer/Avoid with rationale, risks, trade-offs, and limitations) + timeline (immediate/short) + success metrics (baseline vs target and how to measure). Projections only if backed by citations and clearly flagged as estimates.

## II. Requirements

### Minimums

**Q&A**: 4-6 total | 1-2/stage | 120-200w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Stages** (3-4, 1-2 Q each): Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization (skip Market Research, Lead Qual, Onboarding unless decision-critical)

**Category Coverage** (min): Sales ≥50%, Marketing ≥40%, CS ≥40%, RevOps ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/13): CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst (core roles only)

**References** (build before Q&A): G≥8 (100% terms used), N≥4-5 (per freshness), P≥2 (platforms), M≥1-2 (methodologies), R≥2 (reports), A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 stages + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Domain**: Industry/vertical + period (e.g., "B2B SaaS GTM Q4 2024")

2. **Search** (≥10-15 candidates, tiered):

   **Tier 1** (1-3d, search first): `"[Domain] {sales performance|pipeline|quota|win rate|marketing|CAC|conversion|campaign|churn|retention|NPS|expansion|competitive|win/loss|market share}"` + 1-3d

   **Tier 2** (7-14d if insufficient): Same + 7-14d

   **Sources** (whitelist, prioritize):
   - **Sales/Marketing**: SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot
   - **CS/RevOps**: Gainsight, RevOps Co-op, Winning by Design
   - **Competitive**: G2, Gartner, Forrester, competitor changelogs
   - **Avoid**: PR fluff, rumors, listicles, speculation

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Product Hunt

3. **Curate** (≥10-15 candidates: Sales ≥4, Marketing ≥3, CS ≥2, RevOps ≥2, Competitive ≥2):
   - Age per freshness
   - Whitelist OR primary source
   - Satisfies ≥1 Decision Criticality criterion
   - Specific details (dates, names, numbers, metrics)
   - Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 4-6 Q × 3-4 stages (1-2 each) × 3-4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | P# (platform, model, URL) | M# (methodology, application, URL) | R# (report, findings, URL) | A# (APA 7th+tag)

**Citation**: Use Markdown reference links with source name and year, for example `[Ref: N1 – Gong, 2024][n1]` in text and `[n1]: URL` at the end. Prefer sources from the last 12 months where possible, and explicitly mark older or uncertain information.

**Floors**: G≥8 (100% terms used), N≥4-5, P≥2, M≥1-2, R≥2, A≥6

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (MQL, SQL, CAC, LTV, NPS, GRR, NRR, pipeline velocity)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 2.5: Opportunistic Refresh (optional, skip default)

**Only for breaking news in last 24-48 hours affecting ≥3 questions.**

**Action**: Quick search → Add 1-2 "BREAKING" items → Adjust 1-2 Qs → Document

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[News] implications for [Stage]+[Roles]?" | "[Metric] improvement per [News]?" | "[Tool Update] impact on [Process]?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 stages + quantified (revenue $, pipeline $, conversion %, retention %, include baseline vs target when possible)
3. **Stakeholders** (~35w): ≥2 roles + concerns + actions; call out where perspectives, incentives, or constraints differ
4. **Decision** (~50w): Compare at least two options (e.g., Adopt vs Test vs Defer/Avoid) with rationale, risks, trade-offs, and when each is appropriate; note key uncertainties
5. **Action** (~20w): Immediate (0-2wk) and Short (2wk-2mo) actions + owner + 1–3 success metrics and how they will be measured

**Self-Check**: Freshness & Decision Criticality ✓ | ≥2 stages & roles | ≥2 options with risks/limits | clear decision & timeline | 120–200w | quantified with units & baselines | ≥1 recent cite | 0% hype, 100% actionable | all terms in glossary | no contradictions across answers | uncertainties flagged

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Conversion funnels, sales pipelines, retention cohorts, 2×2 matrices, benchmarks

**Format**: Mermaid (flows), Markdown tables (data), 2×2 matrices

### Step 5: Final Checks

**Final**: Refs resolved, age OK, floors met (G≥8 with 100% terms, N≥4–5, P≥2, M≥1–2, R≥2, A≥6), every Q has a decision (with rationale, criteria, timeline), and ≥5 roles have clear actions and authority.

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 stages | Categories per % | ≥5 roles | Citations OK | 5 word samples 120-200w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Decision Criticality 100% | Impact 100% ≥2 stages+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-stage ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented | Self-review of calculations, terminology, contradictions, and success metrics completed

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+2wk)** | Search documented

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ P:__ M:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2,≥1-2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Stages** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Sales__% Market__% CS__% RevOps__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/13 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2stages+2roles+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%120-200w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **Age Dist** | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1-2 stages) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "Gong Labs Q3: 12% pipeline velocity—Sales & RevOps response?" | "SaaS Capital: NRR 108% vs our 95%—CS retention tactics?" | "HubSpot pricing ↑15% (Nov'24): GTM strategy?" | "Competitor CAC ↓20% (Oct'24): our response?"

**✗ Bad**: "How does sales work?" (no news) | "What is NPS?" (overview) | "Should we use Salesforce?" (no trigger) | "Competitor launched feature" (no decision)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Commercial Operations Intelligence ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Stage Coverage (3-4 stages)
3. Questions by Stage: Lead Gen (Q1-Q2) | Sales (Q3-Q4) | Retention (Q5-Q6) | Analytics (Q7-Q8)
4. References: G (G1-G8) | N (N1-N5) | P (P1-P2) | M (M1-M2) | R (R1-R2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Stage | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] P=[#] M=[#] R=[#] A=[#]
```

### C. Stage Overview

| # | Stage | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Lead Gen & Demand | 1-2 | Sales, Marketing | [Top] | VP Marketing, Demand Gen |
| 2 | Sales & Closing | 1-2 | Sales, Competitive | [Top] | VP Sales, AE |
| 3 | Retention & Expansion | 1-2 | CS, RevOps | [Top] | VP CS, CSM |
| 4 | Analytics & Optimization | 1-2 | RevOps, Marketing | [Top] | RevOps Analyst, CRO |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Stage + Roles]

**Stage**: [Stage] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Stages** (≥2) | **Quantified**: Revenue $ | Pipeline $ | Conversion % | Retention %

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Adopt/Test/Scale/Defer/Avoid | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

[n1]: URL
---
```

### E. Reference Formats

**G#. Term (Acronym)**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL

**P#. Platform** (Source, Date): Model | URL

**M#. Methodology** (Source, Date): Application | URL

**R#. Title** (Firm, Date): Findings | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
