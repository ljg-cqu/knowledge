# Product & Market Intelligence News Q&A Generator

Generate 4–6 decision-critical Q&As from recent product and market news for post-PMF organizations.

**Setup**: Fill contextual placeholders (`[Domain]`, `[Period]`, generation date, product, competitors, priorities) then paste into LLM.

**Cadence**: Bi-weekly | Valid 2 weeks from generation date

**Freshness** (age from generation date):
- **High-Velocity** (Competitive, Pricing): Majority <1mo, none >4mo
- **Medium-Velocity** (Strategy, Research): Majority <2mo, none >6mo

**Scope**: Decision-critical product news—competitive features, pricing, strategic pivots, customer research.

**Exclude**: Technical ops, sales execution, finance (except pricing), long-term R&D, rumors, marketing fluff.

## I. Framework

**Context Inputs**:
- Product, business model, value proposition
- Target customers and regions
- Company stage and scale
- 3–7 key competitors
- Strategic priorities and constraints

**Decision Criticality** (include news if ≥1 met):
1. **Blocks Decision**: Impacts roadmap, go/no-go, or pivot
2. **Creates Risk**: Competitive threat, churn signal, pricing pressure
3. **Multi-Stakeholder**: Affects ≥2 core roles
4. **Action Required**: 1-6mo window
5. **Quantified Impact**: Adoption %, pricing $, market share, churn

**Categories** (cover majority):
1. **Competitive**: Launches, updates, parity gaps
2. **Pricing**: Changes, model shifts, packaging
3. **Strategy**: Pivots, expansions, partnerships
4. **Research**: Adoption, churn, usage trends

**Answer Structure**: News (what, when, why) → Impact (quantified, multi-phase, multi-role) → Decision (rec + rationale) → Timeline (immediate/short-term)

## II. Requirements

**Q&A**: 4-6 total | 1-2 per phase | All news-driven with citations | Each has category, impact, decision

**Phases** (cover 3-4): Discovery, Design, Launch, Growth

**Category Balance**: Emphasize Competitive & Pricing; include Strategy & Research

**Stakeholders** (≥5): CPO/VP Product, PM, Product Marketing, Competitive Intel, Eng Lead, others as relevant

**References**: Glossary (key terms), News (≥5, per freshness), Competitive/Pricing/Research (≥2 each), Academic/Industry (as needed, APA format)

**Visuals**: ≥2 (diagrams, matrices, tables in Mermaid/Markdown)

**Quality Gates**:
1. **Criticality**: All Q&As meet ≥1 Decision Criticality criterion
2. **Sources**: Fresh, diverse, primary preferred; no rumors/marketing fluff
3. **Impact**: Quantified, multi-phase (≥2), multi-role (≥2)
4. **Decisions**: Actionable recommendation + rationale + timeline
5. **Completeness**: All terms in glossary, valid URLs, concrete actions

## III. Execution

### Step 1: News Discovery & Curation

1. **Record** generation date (YYYY-MM-DD) and define domain/product category
2. **Search**: Prioritize recent news (<1wk first); use diverse sources (Product Hunt, TechCrunch, changelogs, pricing pages, research reports)
3. **Curate** ≥10 items meeting: freshness thresholds, criticality criteria, category balance, high specificity
4. **Allocate**: Distribute across 4-6 questions covering 3-4 phases and all categories

### Step 2: Build References

**Format**: G# (glossary: term, def, analogy) | N# (news: title, source, date, category, URL) | C/P/R# (competitive/pricing/research: details, URL) | A# (academic: APA 7th)

**Citation**: `[Ref: N1][n1]` in text, `[n1]: URL` at end

**Glossary**: Plain language, analogies, numeric examples for all terms used

### Step 3: Generate Q&A

**Pattern**: "[News] implications for [Phase]+[Roles]?"

**Structure**:
1. **News**: What, when, why, category `[Ref: N#][n#]`
2. **Impact**: Multi-phase (≥2), quantified
3. **Stakeholders**: Multi-role (≥2), concerns, actions
4. **Decision**: Build/Prioritize/Monitor/Defer/Ignore + rationale
5. **Action**: Immediate (0-2wk) + Short (2wk-2mo) + owner
6. **Links**: `[n1]: URL`

**Avoid**: Generic claims, hype, speculation, stale/unattributed content

### Step 4: Create Visuals

≥2 diagrams/matrices + ≥1 table in Mermaid or Markdown

### Step 5: Validate

Check: Reference requirements, Q count (4-6), phase coverage (3-4), category balance, stakeholders (≥5), all citations present, freshness met, impact quantified, decisions actionable, no placeholders, valid URLs

### Step 6: Submit

Complete TOC, glossary with all terms, passing all quality gates

## IV. Validation Report

| Check | Criteria | Result | Status |
|-------|----------|--------|--------|
| **Freshness** | HV majority <1mo, MV majority <2mo | | ☐ PASS |
| **References** | G (terms), N≥5, C/P/R≥2 each | | ☐ PASS |
| **Q&A Count** | 4-6 total | | ☐ PASS |
| **Phase Coverage** | 3-4 phases, 1-2 Q each | | ☐ PASS |
| **Category Balance** | Competitive & Pricing emphasized | | ☐ PASS |
| **Stakeholders** | ≥5 roles | | ☐ PASS |
| **Criticality** | All Q&As meet ≥1 criterion | | ☐ PASS |
| **Impact** | All quantified, multi-phase, multi-role | | ☐ PASS |
| **Decisions** | All have rec + rationale + timeline | | ☐ PASS |
| **Citations** | All Q&As cited | | ☐ PASS |
| **Visuals** | ≥2 diagrams + ≥1 table | | ☐ PASS |
| **Completeness** | No placeholders, all URLs valid | | ☐ PASS |
| **Meta** | Gen: `____` | Expires: `[+2wk]` | INFO |

## V. Question Quality

**Good Questions**: News-driven | Decision-critical | Lifecycle-specific | Multi-stakeholder | Quantified | Actionable

**✓ Examples**: "Notion AI 40% adoption (Oct'24)—roadmap impact?" | "Linear 3→2 tier pricing (Sep'24): response?" | "Competitor ↑20% pricing (Nov'24): strategy?"

**✗ Avoid**: Generic theory | No news trigger | Tech ops focus | Vague impact

## VI. Output Format

### A. TOC

```markdown
# [Domain] Product & Market Intelligence Q&A ([Period])

1. Executive Summary (Insights | Dashboard)
2. Phase Coverage
3. Questions by Phase
4. References (G | N | C | P | R | A)
5. Validation
```

### B. Executive Summary

**Domain**: [Category] | **Period**: [Date range] | **Roles**: [5+ roles]

**Top Insights** (2-3): [Date]: [News] → [Impact] → [Decision] → [Timeline]

**Dashboard**:
| Phase | News | Decision | Timeline |
|-------|------|----------|----------|
| ... | ... | ... | ... |

### C. Phase Overview

| Phase | Count | Categories | Primary Roles |
|-------|-------|------------|---------------|
| Discovery | 1-2 | Competitive, Strategy | PM, Intel |
| Design | 1-2 | Strategy, Research | PM, Eng Lead |
| Launch | 1-2 | Competitive, Pricing | PM, Marketing |
| Growth | 1-2 | Pricing, Research | PM, Analyst |

### D. Q&A Template

```markdown
### Q#: [News Question + Phase]

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Category**: [Cat] | **Criticality**: [Criterion]

**News**: What, when, why [Ref: N#][n#]

**Impact**: Phases affected (≥2), quantified impact (adoption %, pricing $, market %, churn)

**Stakeholders**: 
- **[Role 1]**: Concerns + actions
- **[Role 2]**: Concerns + actions

**Decision**: 
- **Options**: [2+ options]
- **Recommendation**: Build/Prioritize/Monitor/Defer/Ignore
- **Rationale**: Why + success criteria

**Action**: 
- **Immediate (0-2wk)**: [Actions + owner]
- **Short (2wk-2mo)**: [Actions + owner]

[n1]: URL
---
```

### E. Reference Formats

- **G#. Term**: Definition, analogy, context, example
- **N#. News**: Title (Source, MM/DD), summary, category, URL
- **C#. Competitive**: Competitor feature (Source, Date), details, URL
- **P#. Pricing**: Company pricing (Source, Date), model, URL
- **R#. Research**: Title (Firm, Date), findings, URL
- **A#. Academic**: [Tag] Author/Org (YYYY, Mon DD). *Title*. URL
