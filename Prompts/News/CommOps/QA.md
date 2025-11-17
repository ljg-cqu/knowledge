# Commercial Operations News Intelligence Q&A Generator

Generate 4–6 (or fewer if insufficient qualifying news) decision-critical Q&As from recent commercial news for informed decisions.

## I. Context & Scope

**Target**: Bi-weekly | 4-6h effort | **Expires**: 2 weeks from generation

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Sales, Marketing): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (CS, RevOps, Competitive): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical commercial news—sales execution, marketing ops, customer success, RevOps, GTM, competitive intel.

**Exclude**: Technical implementation, product strategy/pricing research, corporate finance (except GTM pricing), long-term strategy, rumors, marketing fluff, stale news, nice-to-have trends.

**LLM Role**: Commercial Operations news intelligence analyst.

**Inputs** (fill before running):
- Domain and vertical (e.g., B2B SaaS, fintech, region).
- Period (e.g., last 2 weeks, Q4 2024).
- Company context: size, stage, regions, primary GTM motions, main products, average contract value.
- Baseline metrics: recent pipeline $, win rate, CAC, LTV, GRR/NRR, churn, key conversion rates.
- Stakeholders and goals: CRO, VP Sales, VP Marketing, VP CS, RevOps analyst, others.
- Constraints: budget, hiring limits, regulatory or contractual boundaries.

**Objective**: Produce executive summary, stage coverage overview, 4–6 (or fewer) Q&As, references (G, N, P, M, R, A), ≥2 diagrams + 1 table, validation report.

**Output Expectations**:
- Respect word counts and freshness.
- Focus on high-impact news meeting decision criticality.
- Prefer concrete numbers over vague language.
- Cover multiple viewpoints, trade-offs, risks, limitations.

**Decision Criticality** (≥1 criterion met):
1. **Blocks Decision**: Impacts quota strategy, GTM pivot, revenue model.
2. **Creates Risk**: Competitive threat, churn signal, CAC/LTV pressure.
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact.
4. **Requires Action**: 1-6mo window.
5. **Quantified Impact**: Revenue $, pipeline $, conversion %, retention %, efficiency gain.

**Categories** (3-4, each Q covers ≥1):
1. **Sales Performance & Pipeline**: Win rates, quota attainment, pipeline velocity, sales cycle changes.
2. **Marketing Performance & Attribution**: CAC, conversion rates, campaign effectiveness, attribution shifts.
3. **Customer Success & Retention**: Churn, NRR, expansion, retention tactics.
4. **Revenue Operations & Analytics** (optional): RevOps tools, analytics platforms, data infrastructure.

**Answer Structure** (120–200 words): News (what, when, why) + impact (quantified, ≥2 stages, ≥2 roles) + decision options (compare ≥2 choices with rationale, risks, trade-offs, limitations) + timeline (immediate/short) + success metrics (baseline vs target, measurement). Projections only if cited and flagged as estimates.

## II. Requirements

**Q&A**: 4-6 (or fewer) total | 1-2 per stage | 120-200 words | 100% news-driven | ≥85% with ≥1 citation, ≥30% with ≥2 | Each covers ≥1 category, impact, decision.

**Stages** (3-4, 1-2 Q each): Lead Gen & Demand, Sales & Closing, Retention & Expansion, Analytics & Optimization.

**Category Coverage** (min): Sales ≥50%, Marketing ≥40%, CS ≥40%, RevOps ≥25%.

**Decision Criticality** (100%): Each Q satisfies ≥1 criterion (Blocks/Risk/Roles/Action/Quantified).

**Stakeholders** (≥5): CRO, VP Sales, VP Marketing, VP CS, RevOps Analyst.

**References**: G≥8 (100% terms used), N≥4-5 (per freshness), P≥2, M≥1-2, R≥2, A≥6.

**Visuals**: ≥2 diagrams + ≥1 table.

**Quality Gates** (fail any = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion.
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors.
3. **Impact**: 100% ≥2 stages + ≥2 roles + quantified.
4. **Decision**: 100% with rationale + timeline.
5. **Sources**: ≥3 types, max 50%/type; URLs valid.
6. **Actionability**: 100% concrete; 0% abstract.

## III. Execution

### Step 1: News Discovery & Curation

Record generation date (YYYY-MM-DD)—calculate ages from this.

1. **Domain**: Industry/vertical + period (e.g., "B2B SaaS GTM Q4 2024").

2. **Search** (≥10-15 candidates, tiered):
   - **Tier 1** (1-3d): `"[Domain] {sales performance|pipeline|quota|win rate|marketing|CAC|conversion|campaign|churn|retention|NPS|expansion|competitive|win/loss|market share}"` + 1-3d.
   - **Tier 2** (7-14d if needed): Same + 7-14d.
   - **Sources** (prioritize): SaaStr, Sales Hacker, MarketingProfs, Gong, Salesforce, HubSpot, Gainsight, RevOps Co-op, Winning by Design, G2, Gartner, Forrester.
   - **Tools**: Perplexity, ChatGPT, Google, Product Hunt.

3. **Curate** (≥10-15: Sales ≥4, Marketing ≥3, CS ≥2, RevOps ≥2, Competitive ≥2): Age per freshness, whitelist source, ≥1 criticality criterion, specific details, no rumors.

4. **Verify**: Check criticality; retry if fail.

5. **Allocate**: 4-6 (or fewer) Q across 3-4 stages (1-2 each), categories, ≥5 roles.

### Step 2: Build References

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | P# (platform, model, URL) | M# (methodology, application, URL) | R# (report, findings, URL) | A# (APA 7th+tag).

**Citation**: Markdown links, e.g., `[Ref: N1 – Gong, 2024][n1]`. Prefer recent sources; mark older/uncertain.

**Floors**: G≥8 (100% used), N≥4-5, P≥2, M≥1-2, R≥2, A≥6.

**Glossary** (terms used): Plain language, 1-2 analogies, context, examples.

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Criticality.

### Step 2.5: Opportunistic Refresh (optional)

For breaking news (24-48h) affecting ≥3 Qs: Quick search → Add 1-2 "BREAKING" → Adjust 1-2 Qs → Document.

### Step 3: Generate Q&A

Review glossary; track terms.

**Patterns**: "[News] implications for [Stage]+[Roles]?" etc.

**Avoid**: Generic, hype, unattributed, stale, speculation.

**Structure** (120-200w):
1. **News** (~25w): What, when, why, cat [Ref].
2. **Impact** (~50w): ≥2 stages + quantified (include baselines/targets).
3. **Stakeholders** (~35w): ≥2 roles + concerns/actions; note differences.
4. **Decision** (~50w): Compare ≥2 options (rationale, risks, trade-offs, uncertainties).
5. **Action** (~20w): Immediate (0-2wk) + Short (2wk-2mo) actions + owner + 1-3 metrics.

**Self-Check**: Freshness/criticality ✓ | ≥2 stages/roles | ≥2 options | 120-200w | quantified | ≥1 cite | actionable | terms in glossary | no contradictions | uncertainties flagged.

### Step 4: Visuals

≥2 diagrams (Mermaid) + ≥1 table. Types: funnels, pipelines, cohorts, matrices.

### Step 5: Final Checks

Refs resolved, age OK, floors met, decisions/timelines/actions for ≥5 roles.

### Step 6: Validate

**Quantitative**: Floors | Glossary 100% | Stages | Categories % | Roles | Citations | Words | Visuals | Decision/Timeline | Age.

**Qualitative**: Freshness | Criticality 100% | Impact 100% | Decision 100% | Sources ≥3 types | Per-stage news | Links valid | Quantified/Actionable 100% | Evidence 100% | Search documented | Self-review.

### Step 7: Submit

**Checklist**: Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC | No placeholders | Visuals/Citations/Impact/Decision/Timeline/Categories/Roles/Freshness OK | Evidence 100% | URLs valid | Dates | Search documented.

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<1mo (1-3d:__%), __%<2mo \| MV: __%<2mo (1-3d:__%) \| Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ P:__ M:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2,≥1-2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Stages** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Sales__% Marketing__% CS__% RevOps__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | **Roles** | __/5 | ≥5 | | PASS/FAIL |
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
| 2 | Sales & Closing | 1-2 | Sales, RevOps | [Top] | VP Sales, AE |
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
