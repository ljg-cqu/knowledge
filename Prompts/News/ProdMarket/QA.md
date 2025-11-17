# Product & Market Intelligence News Q&A Generator

Generate 4–6 decision-critical Q&As, visuals, and validation report from recent product and market news.

**Setup**: Fill contextual placeholders (`[Domain]`, `[Period]`, roles, generation date, product, stage, region, competitors, priorities) then paste entire prompt into LLM.

**Cadence**: Bi-weekly | 4–6h analysis | Valid 2 weeks from generation date

**Freshness** (age from generation date):
- **High-Velocity** (Competitive, Pricing): ≥85% <1mo (≥30% <1wk), 100% ≤4mo
- **Medium-Velocity** (Strategy, Research): ≥70% <2mo (≥20% <1wk), 100% ≤6mo
- **Overall**: ≥75% <2mo, ≥90% <4mo, 100% ≤9mo

**Scope**: Decision-critical product news only—competitive features, pricing shifts, strategic pivots, customer research. For post-PMF organizations.

**Exclude**: Technical implementation, sales execution, corporate finance (except pricing), long-term R&D, rumors, marketing fluff, stale news.

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

**Categories** (each Q covers ≥1):
1. **Competitive Features**: Launches, updates, parity gaps, deprecations
2. **Pricing & Monetization**: Pricing changes, model shifts, packaging
3. **Product Strategy**: Pivots, expansions, build/buy/partner decisions
4. **Customer Research** (optional): Adoption signals, churn patterns, usage trends

**Answer Structure**: News (what, when, why) + impact (quantified, ≥2 phases, ≥2 roles) + decision (Build/Prioritize/Monitor/Defer/Ignore + rationale) + timeline (immediate/short). Projections only if sourced.

## II. Requirements

**Q&A**: 4-6 total | 1-2/phase | 100% news-driven | 100% ≥1 cite | ≥1 category + impact + decision per Q

**Phases** (3-4, 1-2 Q each): Discovery, Design, Launch, Growth

**Category Distribution**: Competitive ≥40%, Pricing ≥25%, Strategy ≥25%, Research ≥15%

**Decision Criticality** (100%): Each Q satisfies ≥1 criterion.

**Stakeholders** (≥5): CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead

**References**: G≥8 (100% terms used), N≥5 (per freshness), C≥2, P≥2, R≥2, A≥6 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion
2. **News**: 100% cite ≥1 per freshness; 0% marketing/rumors
3. **Impact**: 100% ≥2 phases + ≥2 roles + quantified
4. **Decision**: 100% decision + rationale + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionability**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation

Record generation date (YYYY-MM-DD)—calculate all news ages from this.

1. **Domain**: Define industry/product category + date

2. **Search** (≥10 candidates, tiered):
   - **Tier 1**: Focus on <1wk news first
   - **Tier 2**: Expand to <1mo if needed
   - **Sources**: Competitive (Product Hunt, TechCrunch, changelogs); Pricing (pricing pages, Archive.org); Strategy (newsletters, blogs); Research (reports, analytics firms)

3. **Curate** (≥10 items: Competitive ≥4, Pricing ≥2, Strategy ≥2, Research ≥2):
   - Meets freshness thresholds
   - Primary sources preferred
   - Satisfies ≥1 Decision Criticality criterion
   - Specific details (not vague)
   - High impact potential

4. **Verify**: Confirm each meets criticality criteria

5. **Allocate**: Distribute news across 4-6 questions covering 3-4 phases and all categories; avoid duplicates

### Step 2: Build References

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | C# (competitive, feature, URL) | P# (pricing, model, URL) | R# (research, findings, URL) | A# (APA 7th+tag)

**Citation**: `[Ref: N1][n1]` in text, `[n1]: URL` at end

**Quality**: Prefer primary sources; cross-check summaries

**Glossary** (terms used): Plain language, 1–2 analogies, why matters, numeric example

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Criterion

### Step 3: Generate Q&A

**Pattern**: "[News] implications for [Phase]+[Roles]?"

**Avoid**: Generic, hype, unattributed, stale, speculation

**Structure**:
1. **News**: What, when, why, cat `[Ref: N#][n#]`
2. **Impact**: ≥2 phases + quantified
3. **Stakeholders**: ≥2 roles + concerns + actions
4. **Decision**: Build/Prioritize/Monitor/Defer/Ignore + rationale + criteria
5. **Action**: Immediate (0-2wk) + Short (2wk-2mo) + owner
6. **Links**: `[n1]: URL`

**Self-Check**: Freshness, criticality, ≥2 phases/roles, quantified, actionable, terms in glossary

### Step 4: Visuals

**Types**: Matrices, tables, 2×2, trees | **Format**: Mermaid, Markdown

### Step 5: Validate

**Quantitative**: Reference floors (G≥8, N≥5, C≥2, P≥2, R≥2, A≥6), Q count (4-6), phases (3-4), categories, roles (≥5), citations (100% ≥1), visuals (≥2 diag, ≥1 table), decisions/timelines (100%), freshness thresholds

**Qualitative**: No hype/rumors, criticality met, impact quantified, decisions actionable, source diversity, URLs valid

### Step 6: Submit

Complete TOC, glossary (100% terms), no placeholders, all checks pass

## IV. Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Freshness | HV: __%<1mo (<1wk:__%); MV: __%<2mo (<1wk:__%); Overall: __%<2mo | Per header | | PASS/FAIL |
| 2 | Floors | G:__ N:__ C:__ P:__ R:__ A:__ Q:__ | ≥8,≥5,≥2,≥2,≥2,≥6,4-6 | | PASS/FAIL |
| 3 | Glossary | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | Phases | __/__ (1-2Q each); total__ | 3-4;4-6 | | PASS/FAIL |
| 5 | Categories | Comp__% Pric__% Strat__% Res__% | ≥40,25,25,15% | | PASS/FAIL |
| 6 | Roles | __ | ≥5 | | PASS/FAIL |
| 7 | Decision Criticality | __% satisfy ≥1 | 100% | | PASS/FAIL |
| 8 | Impact | __% ≥2phases+2roles+quantified | 100% | | PASS/FAIL |
| 9 | Decision | __% decision+rationale+timeline | 100% | | PASS/FAIL |
| 10 | Citations | __%≥1cite | 100% | | PASS/FAIL |
| 11 | Visuals | diag:__ tab:__ | ≥2;≥1 | | PASS/FAIL |
| | Meta | Gen:__ Expires:[+2wk] | | INFO |
| | Age Dist | <1mo:__% 1-2mo:__% 2-4mo:__% | Per header | | INFO |
| | OVERALL | All checks | All PASS | | PASS/FAIL |

## V. Question Quality

**Criteria**: News-driven | Decision-critical | Lifecycle-specific | Multi-stakeholder | Quantified impact | Actionable | Rewrite if ≥2 fail

**✓ Good**: "Notion AI 40% adoption (Oct'24)—roadmap impact?" | "Linear 3→2 tier (Sep'24): response?" | "Competitor ↑20% pricing (Nov'24): strategy?"

**✗ Bad**: "How does PMF work?" (no news) | "Build AI features?" (no trigger) | "Kubernetes 1.30" (tech ops) | "Competitor launched feature" (no decision)

## VI. Output Format

### A. TOC

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage
3. Questions by Phase (Discovery | Design | Launch | Growth)
4. References (G | N | C | P | R | A)
5. Validation
```

### B. Executive Summary

**Domain**: [Category] | **Period**: [Date range] | **Coverage**: [# items, cats]

**Insights**: 2 highest-impact news with [Date]: [Impact] → [Decision] → [Timeline]

**Dashboard**: Table with Phase | News | Decision | Timeline

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] C=[#] P=[#] R=[#] A=[#]

### C. Phase Overview

| Phase | Count | Categories | Top News | Primary Roles |
|-------|-------|------------|----------|---------------|
| Discovery | 1-2 | Competitive, Strategy | [Title] | PM, Intel |
| Design | 1-2 | Strategy, Research | [Title] | PM, Eng Lead |
| Launch | 1-2 | Competitive, Pricing | [Title] | PM, Marketing |
| Growth | 1-2 | Pricing, Research | [Title] | PM, Analyst |
| **Total** | **4-6** | **3-4** | **5+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Criticality**: [Criterion]

**News**: What, when, why, cat [Ref: N#][n#]

**Impact**: **Phases** (≥2 affected) | **Quantified**: Numbers (adoption %, pricing $, market %, churn signal)

**Stakeholders**: **[Role 1]**: Concerns, actions | **[Role 2]**: Concerns, actions

**Decision**: **Options** (≥2) | **Rec**: Build/Prioritize/Monitor/Defer/Ignore | **Rationale**: Why | **Success**: Measurable targets

**Action**: **Immediate (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Actions+owner

[n1]: URL
---
```

### E. Reference Formats

**G#. Term**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL | Criterion

**C#. Competitor Feature** (Source, Date): Details | URL

**P#. Company Pricing** (Source, Date): Model | URL

**R#. Research Title** (Firm, Date): Findings | URL

**A#. [Tag]**: Author/Org. (YYYY, Mon DD). *Title*. URL
