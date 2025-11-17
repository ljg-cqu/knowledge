# Product & Market Intelligence News Q&A Generator

Use this template as a single, self-contained LLM prompt to generate 4–6 decision-critical Q&As, visuals, and a validation report from recent product and market news.

**How to use**:
1. Fill contextual placeholders in the Output Format (`[Domain]`, `[Period]`, roles, generation date) and set product, stage, region, target segment, key competitors, and priorities.
2. Paste this entire prompt into the LLM with those context values.
3. Instruct the LLM to strictly follow all requirements, execution steps, and the output format.

**Cadence & Effort**: Bi-weekly | 4–6h equivalent analysis effort | **Validity**: Results valid for 2 weeks from generation date.

**Freshness** (all news must meet these age thresholds):
- **High-Velocity** (Competitive, Pricing): ≥85% <1mo (≥30% 1-3d), ≥95% <2mo, 100% ≤4mo
- **Medium-Velocity** (Strategy, Research): ≥70% <2mo (≥20% 1-3d), ≥90% <3mo, 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical product news only—competitive features, pricing shifts, strategic pivots, customer research. For post-PMF organizations.

**Exclude**: Technical implementation, sales execution, corporate finance (except pricing), long-term R&D, rumors, marketing fluff, stale news, nice-to-have trends.

## I. Framework

**Context Inputs** (set before running):
- Product, business model, and main value proposition.
- Target customers/segments and regions.
- Company stage and scale (post-PMF, revenue/user band, team size).
- Competitive set (3–7 key competitors).
- Strategic priorities.
- Key constraints and risk tolerance.

**Decision Criticality** (include if ≥1 criterion met):
1. **Blocks Decision**: Impacts roadmap prioritization, go/no-go, or strategic pivot.
2. **Creates Risk**: Material competitive threat, churn signal, or pricing pressure.
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact.
4. **Requires Action**: 1-6mo action window.
5. **Quantified Impact**: Adoption %, pricing $, market share, or churn signal.

**Categories** (3-4, each Q covers ≥1):
1. **Competitive Features**: Launches, updates, parity gaps, deprecations.
2. **Pricing & Monetization**: Pricing changes, model shifts, packaging.
3. **Product Strategy**: Pivots, expansions, build/buy/partner decisions.
4. **Customer Research** (optional): Adoption signals, churn patterns, usage trends.

**Answer Structure**: News (what, when, why) + impact (quantified, ≥2 phases, ≥2 roles) + decision (Build/Prioritize/Monitor/Defer/Ignore + rationale) + timeline (immediate/short). Projections only if sourced.

## II. Requirements

**Q&A**: 4-6 total | 1-2/phase | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision | No generic theory—focus on decisions and actions.

**Phases** (3-4, 1-2 Q each): Discovery, Design, Launch, Growth.

**Category Coverage** (min): Competitive ≥50%, Pricing ≥40%, Strategy ≥40%, Research ≥25%.

**Decision Criticality** (100%): Each Q satisfies ≥1 criterion.

**Stakeholders** (≥5): CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead.

**References**: G≥8 (100% terms used), N≥4-5 (per freshness), C≥2-3, P≥2, R≥2, A≥6 (APA 7th+tag).

**Visuals**: ≥2 diagrams + ≥1 table.

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion.
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors.
3. **Impact**: 100% ≥2 phases + ≥2 roles + quantified.
4. **Decision**: 100% decision + rationale + timeline.
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid.
6. **Actionability**: 100% concrete; 0% abstract.

## III. Execution

### Step 1: News Discovery & Curation

Record generation date (YYYY-MM-DD)—calculate all news ages from this.

1. **Domain**: Define industry/product category + date.

2. **Search** (≥10–15 candidates, tiered):
   - **Tier 1 (1–3d)**: `"[Competitor/Domain] launched|pricing|strategy"` + 1–3d.
   - **Tier 2 (7–14d)**: Same if Tier 1 insufficient.
   - **Sources**: Competitive (Product Hunt, TechCrunch, changelogs); Pricing (ProfitWell, sites, Archive.org); Strategy (newsletters, blogs); Research (Pendo, Amplitude, reports). Avoid fluff, rumors.
   - **Tools**: Perplexity, ChatGPT, Google, Product Hunt.

3. **Curate** (≥10–15: Competitive ≥4, Pricing ≥2, Strategy ≥2, Research ≥2):
   - Meets freshness.
   - From whitelist/primary sources.
   - Satisfies ≥1 Decision Criticality.
   - Specific details.
   - High impact.

4. **Verify**: Check criticality; retry if needed.

5. **Allocate**: 4–6 Q × 3–4 phases × 3–4 categories × ≥5 roles; avoid duplicates.

### Step 2: Build References

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | C# (competitive, feature, URL) | P# (pricing, model, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: `[Ref: N1][n1]` in text, `[n1]: URL` at end.

**Quality**: Prefer primary sources; cross-check summaries.

**Floors**: G≥8, N≥4-5, C≥2-3, P≥2, R≥2, A≥6.

**Glossary** (terms used): Plain language, 1–2 analogies, why matters, numeric example.

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Criterion.

### Step 3: Generate Q&A

**Patterns**: "[News] implications for [Phase]+[Roles]?" etc.

**Avoid**: Generic, hype, unattributed, stale, speculation.

**Structure**:
1. **News**: What, when, why, cat `[Ref: N#][n#]`
2. **Impact**: ≥2 phases + quantified.
3. **Stakeholders**: ≥2 roles + concerns + actions.
4. **Decision**: Build/Prioritize/Monitor/Defer/Ignore + rationale + criteria.
5. **Action**: Immediate (0-2wk) + Short (2wk-2mo) + owner.
6. **Links**: `[n1]: URL`

**Self-Check**: Freshness, criticality, ≥2 phases/roles/quantified, balanced, consistent, actionable, terms in glossary.

### Step 4: Visuals

**Types**: Matrices, tables, 2×2, trees.

**Format**: Mermaid, Markdown.

### Step 5: Final Checks

Refs complete, floors met, decisions/timelines, coverage, stakeholders.

### Step 6: Validate

Quantitative: Floors, glossary, phases, categories, roles, citations, visuals, decisions, timelines, age.

Qualitative: Freshness, no hype, criticality, impact, decisions, diversity, links, quantified, actionable, evidence, logic.

### Step 7: Submit

Checklist: All validations pass, complete glossary, TOC, no placeholders, OK visuals/citations/impact/decisions/timelines/categories/roles/freshness/evidence/URLs/dates/search.

## IV. Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Freshness | HV: __%<1mo (1-3d:__%), __%<2mo; MV: __%<2mo (1-3d:__%); Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | Floors | G:__ N:__ C:__ P:__ R:__ A:__ Q:__ | ≥8,≥4-5,≥2-3,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | Glossary | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | Phases | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | Categories | Comp__% Pric__% Strat__% Res__% | ≥50,40,40,25% | | PASS/FAIL |
| 6 | Roles | __/5 | ≥5 | | PASS/FAIL |
| 7 | Decision Criticality | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | Impact | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 9 | Decision | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | Citations | __%≥1cite | 100% | | PASS/FAIL |
| 11 | Visuals | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | Meta | Start:__ End:__ Expires:[+2wk] | | INFO |
| | Age Dist | <1mo__%(1-3d__%) 1-2mo__% 2-4mo__% | Per header | | INFO |
| | OVERALL | All checks | All PASS | | PASS/FAIL |

## V. Question Quality

**Criteria**: News-driven | Decision-critical | Lifecycle-specific | Multi-stakeholder | Quantified impact | Timely | Actionable. Rewrite if ≥2 fails.

**✓ Good**: "Notion AI 40% adoption (Oct'24)—roadmap impact?" | "Linear 3→2 tier (Sep'24): response?" | "Competitor pricing ↑20% (Nov'24): strategy?" | "UserTesting: 65% mobile (Nov'24): prioritize?"

**✗ Bad**: "How does PMF work?" (no news) | "What is NPS?" (overview) | "Build AI features?" (no trigger) | "Kubernetes 1.30" (tech ops) | "Competitor launched feature" (no decision)

## VI. Output Format

LLM: Structure output exactly as follows.

### A. TOC

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Discovery (Q1-Q2) | Design (Q3-Q4) | Launch (Q5-Q6) | Growth (Q7-Q8)
4. References: G (G1-G8) | N (N1-N5) | C (C1-C3) | P (P1-P2) | R (R1-R2) | A (A1-A6)
5. Validation (12 checks)
```

### B. Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] C=[#] P=[#] R=[#] A=[#]

### C. Phase Overview

| # | Phase | Count | Categories | News | Roles |
|---|-------|-------|------------|------|-------|
| 1 | Discovery | 1-2 | Competitive, Strategy | [Top] | PM, Intel |
| 2 | Design | 1-2 | Strategy, Research | [Top] | PM, Eng Lead |
| 3 | Launch | 1-2 | Competitive, Pricing | [Top] | PM, Marketing |
| 4 | Growth | 1-2 | Pricing, Research | [Top] | PM, Analyst |
| | **Total** | **4-6** | **3-4** | **4+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase + Roles]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News**: What, when, why, cat [Ref: N#][n#]

**Impact**: **Phases** (≥2) | **Quantified**: Concrete numbers (adoption %, pricing $, market %, churn signal)

**Stakeholders**: **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision**: Compare ≥2 responses, **Rec**: Build/Prioritize/Monitor/Defer/Ignore | **Rationale**: Why | **Success**: Measurable targets (e.g., adoption %, churn %, revenue impact, NPS)

**Action**: **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same; concrete experiments/tools (e.g., price tests, surveys)

[n1]: URL
---
```

### E. Reference Formats

**G#. Term (Acronym)**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL | Criterion

**C#. Competitor Feature** (Source, Date): Details | URL

**P#. Company Pricing** (Source, Date): Model | URL

**R#. Title** (Firm, Date): Findings | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
