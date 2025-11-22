# Startup & Formation Intelligence Q&A Generator

**Purpose**: Generate 4-6 decision-critical Q&As from startup news for formation-stage (pre-seed to Series A: <$10M raised, <50 employees, <18mo runway) decisions on market entry, fundraising, product-market fit, early GTM.

**Output**: Self-contained document with quantified insights, ≥2 alternatives per Q, explicit recommendations, actionable timelines. 150-200w per Q. Valid 14d from generation.

## Table of Contents
- [Context & Scope](#context--scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality Examples](#question-quality-examples)
- [Output Format](#output-format)

## Context & Scope

**Constraints**: Bi-weekly cadence. Formation-stage only (pre-seed–Series A). 6-18mo decision horizon. Valid 14d from generation.

**Stakeholders**: Founder/CEO, CFO, Investor, VP Sales, Product Lead.

**Usage**: Specify domain/geography, news period (start 1-3d, expand to 7-14d), stage, primary roles.

**News Categories** (MECE):
1. **Market/Competition**: Market size, competitor moves, acquisitions (<2mo freshness)
2. **Funding/VC**: Rounds, investor trends, valuations (<3mo)
3. **Business Models & GTM**: Pricing, PLG, sales strategies (<3mo)
4. **Regulatory/Compliance**: Policy, legal requirements (<6mo)
5. **Partnerships/Ecosystem**: Strategic partnerships, platform changes (<2mo)
6. **Economic/Macro**: Interest rates, GDP, inflation (<3mo)

**Priority**: Critical (Funding/VC, Market/Competition, Business/GTM: ≥50% of Qs); Important (Regulatory, Partnerships, Macro: if ≥10% impact on fundraising/runway).

**Include**: Quantified impacts on funding, market entry, competition, pricing/GTM, regulatory changes, partnerships.

**Exclude**: Technical infrastructure, hype, rumors, trivial updates, mature-org optimization.

**Decision Criticality** (≥1):
1. Blocks go/no-go decision
2. ≥10% impact on runway/valuation/position
3. ≥2 roles with conflicting priorities
4. Action required in 1-6mo with resource commitment
5. Quantified impact ($, %, timeline)

## Requirements

- **Q&A**: 4-6 total; 150-200w each; ≥1 citation per Q
- **Phases**: 3-4 of: Market Research & Validation | Fundraising | Product-Market Fit | GTM & Early Growth
- **Categories**: ≥50% Critical (Funding, Market, Business/GTM); remainder Important/Optional
- **Stakeholders**: All 5 roles across Q-set; ≥2 roles per Q
- **References**: ≥3 types from G#/N#/M#/F#/R#/O#/A#
- **Visuals**: ≥2 diagrams + ≥1 table
- **Quality Gates** (fail if any fails):
  1. Decision-critical: Each Q maps to ≥1 of 5 criteria
  2. Fresh: 100% meet category thresholds; 0 PR/rumors
  3. Multi-dimensional: Each Q spans ≥2 phases/roles + ≥3 metrics
  4. Actionable: Each Q has ≥2 options + recommendation + timeline + owner
  5. Diverse: ≥3 reference types

## Execution

### Step 1: News Discovery & Curation

**Setup**: Record generation date (YYYY-MM-DD). Specify domain (sector, geography, period, stage).

**Search Queries**:
- **Funding**: `"[sector] seed funding"`, `"[sector] series A"`, `"[sector] raised $"`
- **Market/Competition**: `"[sector] competitor"`, `"[sector] acquisition"`, `"[sector] market entry"`
- **Business/GTM**: `"[sector] pricing"`, `"[sector] PLG"`, `"[sector] GTM strategy"`
- **Partnerships**: `"[sector] partnership"`, `"[sector] integration"`, `"[sector] ecosystem"`
- **Regulatory**: `"[sector] regulatory"`, `"[sector] compliance"`, `"[sector] policy"`
- **Timeframe**: 1-3d; expand to 7-14d if needed; verify freshness.

**Trusted Sources**:
- **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch
- **Market/Business**: Gartner, Forrester, a16z, First Round Review, Lenny's Newsletter, SaaStr
- **Partnerships**: Official partner blogs, ecosystem platform announcements
- **Regulatory/Macro**: Official sites, major newspapers, central banks
- **Avoid**: PR releases, rumors, unsourced content

**Curate** (6-10 items for 4-6 Qs): Freshness threshold | ≥1 criticality criterion | ≥2 quantified data points | ≥2 roles | ≥50% from Critical categories

**Plan**: Map 4-6 Qs across 3-4 phases and all 5 roles.

### Step 2: Build References

**Reference Types** (≥3 types):
- **G#**: Glossary - term | definition (<30w) | analogy | decision context
- **N#**: News - title | source | date (YYYY-MM-DD) | category | URL
- **M#**: Market report - topic | firm | date | key metrics | URL
- **F#**: Funding - company | round | amount | valuation | date | URL
- **R#**: Research - topic | firm | date | key findings | URL
- **P#**: Partnership - companies | type | date | strategic impact | URL
- **A#**: APA 7th citation | [tag: primary/secondary/data]

**Citation Format**: Markdown links `[Ref: N1][n1]` in text; `[n1]: URL` at end.

**Glossary**: ONLY terms needing definition (e.g., "PLG", "burn multiple"). Plain language. Exclude common terms ("revenue", "customer").

### Step 3: Generate Q&A

**Question Patterns**:
- "[Funding news with specific data] (YYYY-MM-DD): implications for burn/runway and fundraising strategy?"
- "Market entry given [competitor $Xm raise/acquisition] (YYYY-MM-DD)?"
- "[Macro/regulatory change with quantified impact] (YYYY-MM-DD): hiring and cash plan response?"
- "[Specific news event] (YYYY-MM-DD): Enter now, wait, or pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation, redundancy. State each concept once; reference thereafter; use active voice.

**Structure** (150-200w): News (1-2 sentences) → Impact (≥2 phases, ≥3 quantified metrics, cited) → Stakeholders (≥2 roles, conflicting priorities explicit) → Decision (≥2 options with costs/risks/benefits, conditions for each, recommendation with reasoning, success targets) → Action (Immediate 0-2wk + Short 2wk-2mo, with tools and owners) → Assumptions & Risks (critical assumptions, ≥10% impact risks with probabilities, revisit trigger).

### Step 4: Visuals (Inline Placement)

**Principle**: Embed visuals immediately after relevant text to avoid reader navigation.

**Placement Logic**:
- **Market positioning**: Map/matrix after Impact section showing competitive landscape
- **Funding timelines**: Diagram inline when describing runway/fundraising sequence
- **Decision comparisons**: Table directly after Decision text comparing enter/wait/pass options
- **Burn/runway scenarios**: Chart after Impact section with financial metrics
- **Valuation comparables**: Table inline with funding/valuation analysis

**Minimum**: ≥2 diagrams (Mermaid for flows/timelines/decision trees) + ≥1 table (Markdown for comparisons), all placed inline within Q&A sections (not grouped separately)

### Step 5: Self-Review & Validate

**Self-Review**:
1. Fact-check dates, amounts, percentages, valuations; flag uncertainties
2. Check contradictions across Qs
3. Verify calculations with explicit formulas
4. Ensure consistent terminology; all technical terms in glossary
5. Remove placeholders ("TBD", "TODO", "[X]", "YYYY", "example.com")

**Verify**: Phases (3-4) | Roles (all 5) | Citations (≥1 per Q, ≥3 types total) | Glossary (all terms defined) | Visuals (≥2 diagrams + ≥1 table, referenced)

**Quality Gates** (fail if any fails):
1. Freshness: 100% meet category thresholds
2. Criticality: Each Q maps to ≥1 of 5 criteria
3. Multi-dimensional: Each Q spans ≥2 phases/roles + ≥3 metrics
4. Actionable: Each Q has ≥2 options + recommendation + timeline + owner
5. Diverse: ≥3 source types

**Metadata**: Generation (YYYY-MM-DD) + expiry (generation + 14d)

## Validation Checklist

| Check | Target | Evidence | Status |
|-------|--------|----------|--------|
| **Self-Review** | 5/5 steps | [Steps completed] | ☐ |
| **Freshness** | 100% | [Sources + dates] | ☐ |
| **Coverage** | 4-6 Qs, 3-4 phases, 5 roles | [Counts] | ☐ |
| **Criticality** | 100% | [Q→criterion] | ☐ |
| **Multi-dimensional** | 100% | [Phases, roles, metrics per Q] | ☐ |
| **Actionable** | 100% | [Options, rec, timeline, owner per Q] | ☐ |
| **Diverse** | ≥3 types | [Count by type] | ☐ |
| **Glossary** | 100% | [Terms] | ☐ |
| **Visuals** | ≥2 diagrams + ≥1 table | [Counts, refs] | ☐ |
| **Word Count** | 150-200/Q | [Per Q] | ☐ |
| **Metadata** | Gen + exp dates | [Dates] | ☐ |

## Question Quality Examples

**✓ Good**:
- "Series A funding down 35% (Nov 2024): impact on burn rate and fundraising strategy?"
- "Competitor $50M raise (Oct 2024): market entry timing?"

**✗ Bad**:
- "How does fundraising work?"
- "Should we start a company?"

## Output Format

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## 1. Executive Summary
- **Generation**: YYYY-MM-DD | **Expires**: YYYY-MM-DD (generation + 14d) | **Valid For**: Formation-stage (<$10M, <50 employees)
- **Domain/Period/Coverage**: Sector | geography | news period | stage | primary roles
- **Top Insights** (2-3):
  - **[News event (YYYY-MM-DD)]** → Impact: [quantified] → **Decision**: [Rec] by [date] | **Owner**: [Role]
- **Dashboard**:

| Phase | News (date) | Criticality | Decision | Timeline | Owner |
|-------|-------------|-------------|----------|----------|-------|
| [Phase] | [Event] (YYYY-MM-DD) | [Criterion #] | [Rec] | [0-2wk/2wk-2mo] | [Role] |

## 2. Questions by Phase
### Q#: [Specific News Question with Date]
**Phase**: [Phase] | **Roles**: [Role 1, Role 2] | **Criticality**: [Criterion #] | **Word Count**: 150-200

**News** (1-2 sentences): What, when (YYYY-MM-DD), category [Ref: N#][n#]

**Impact** (2-3 sentences): ≥2 phases + ≥3 quantified metrics ($, %, timeline); cite all

| Metric | Baseline | Target | Timeline | Impact |
|--------|----------|--------|----------|--------|
| [Optional: Metrics table if ≥3 financial/runway metrics] | | | | |

```mermaid
[Optional: Funding/runway timeline or burn scenario diagram]
gantt
    title Runway & Fundraising
    section Current
    Burn Rate $50K/mo: done, 0-12mo
    section Target
    Series A $5M: milestone, 12mo
```

**Stakeholders** (2-3 sentences): **[Role 1]**: concern | action + **[Role 2]**: concern | action

**Decision** (2-3 sentences): 
- Option A (cost, risk, benefit) vs Option B (cost, risk, benefit) → **Trade-offs**: [explicit]
- **When A**: [conditions]; **When B**: [conditions]; **Avoid if**: [counterindications]
- **Recommendation**: [Enter/Wait/Pass] because [rationale] given [assumptions]
- **Success targets**: metric ≥ target by date

| Option | Cost | Benefit | Risk | Conditions | Timeline |
|--------|------|---------|------|------------|----------|
| A | [$] | [metric] | [prob%] | [when] | [Xmo] |
| B | [$] | [metric] | [prob%] | [when] | [Xmo] |

**Action** (2-3 bullets):
- **Immediate (0-2wk)**: [Task with tool] [Owner]
- **Short (2wk-2mo)**: [Task with tool] [Owner]

```mermaid
[Optional: Market positioning or competitive landscape diagram]
quadrantChart
    title Market Position
    x-axis Niche --> Broad Market
    y-axis Low Traction --> High Traction
    Competitor A: [0.7, 0.6]
    Us: [0.3, 0.4]
```

**Assumptions & Risks** (1-2 sentences): Assumes [X, Y]; risks (≥10%): [R1 (prob %), R2 (prob %)]; revisit if [trigger] by [YYYY-MM-DD]

[n#]: URL "Source (Date)"
---

## 3. References (≥3 types: G/N/M/F/R/P/A)
[See Step 2 for format]

## 4. Validation
[Completed checklist from Validation Checklist section]

**Note**: All visuals (≥2 diagrams + ≥1 table) should be embedded inline within Q&A sections, not grouped separately.
```
