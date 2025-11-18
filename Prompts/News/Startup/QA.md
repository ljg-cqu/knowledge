# Startup & Formation Intelligence Q&A Generator

**Purpose**: Generate 4–6 decision-critical Q&As from startup news to support formation-stage (pre-seed–Series A) decisions on market entry, fundraising strategy, product-market fit, and early GTM.

**Target Output**: Self-contained document with news-driven insights, quantified impacts, multi-stakeholder perspectives, explicit recommendations, and actionable timelines. Valid for 2 weeks from generation.

## Table of Contents
- [Context & Scope](#context--scope)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality Examples](#question-quality-examples)
- [Output Format](#output-format)

## Context & Scope

- **Cadence**: Bi-weekly, valid 2 weeks from generation.
- **Domain**: Formation-stage startups (pre-seed–Series A) and new-market initiatives.
- **Stakeholders**: Founder/CEO, CFO, Investor, VP Sales, Product Lead.
- **Decision Horizon**: 6–18 months.
- **Usage**: Specify domain/geography, news period, stage, and primary roles.

**Freshness by Category** (age = time from news publication to generation date):
- **High-Velocity** (Market/Competition/Partnerships): <2mo (news changes rapidly, older data unreliable)
- **Medium-Velocity** (Funding/VC/Business/Talent/Macro): <3mo (trends evolve quarterly)
- **Long-Term** (Regulatory/Compliance): <6mo (changes slowly, longer validity)

**News Categories**: Market/Competition | Funding/VC | Business Models & GTM | Regulatory/Compliance | Partnerships/Ecosystem | Talent/Labor | Economic/Macro

**Priority Categories**:
- **Critical**: Funding/VC, Market/Competition, Business Models & GTM
- **Important**: Regulatory/Compliance, Partnerships/Ecosystem
- **Optional**: Talent/Labor, Economic/Macro (unless material impact)

**Include**: Funding, market entry, competition, pricing/GTM, regulatory changes, partnerships, talent shifts, macro shocks with quantified impact.

**Exclude**: Technical details, infrastructure, hype, rumors, trivial updates, mature-org optimization.

**Decision Criticality** (each Q meets ≥1):
1. Blocks go/no-go decision (e.g., market entry, fundraising start)
2. Creates material risk (≥10% impact on runway, valuation, or market position)
3. Affects ≥2 roles with conflicting priorities requiring explicit trade-offs
4. Requires action in 1–6 months with resource commitment
5. Has quantified impact (specific metrics: $, %, timeline)

## Requirements

- **Q&A**: 4–6 total; 120–200 words each (measured by word count); ≥1 citation per Q.
- **Phases**: Cover 3–4 phases: Market Research & Validation | Fundraising | Product–Market Fit | GTM & Early Growth.
- **Category Coverage**: ≥50% from Critical categories (Funding, Market, Business/GTM); remaining from Important/Optional.
- **Stakeholders**: All 5 core roles across Q-set; each Q addresses ≥2 roles.
- **References**: Mix of glossary (G#), news (N#), market reports (M#), funding (F#), research (R#), org/talent (O#), and APA citations (A#).
- **Visuals**: ≥2 diagrams + ≥1 table.
- **Quality Gates** (fail document if any gate fails):
  1. **Decision-critical**: Each Q meets ≥1 criticality criterion (verify against criteria 1-5)
  2. **Fresh sources**: 100% within category freshness thresholds; 0 PR/rumors (verify dates)
  3. **Multi-dimensional**: Each Q spans ≥2 phases/roles (count) + ≥3 quantified metrics ($, %, dates)
  4. **Actionable**: Each Q has ≥2 options compared + explicit recommendation + timeline (<2wk, 2wk–2mo) + owner assigned
  5. **Diverse sources**: ≥3 distinct source types across Q-set (count G/N/M/F/R/O/A)

## Execution

### Step 1: News Discovery & Curation

**Setup**: Record generation date (YYYY-MM-DD). Specify domain (sector, geography, period, stage).

**Search Queries** (use quotation marks for exact phrases):
- **Funding**: `"[sector] seed funding"`, `"[sector] series A"`, `"[sector] raised $"`
- **Market/Competition**: `"[sector] competitor"`, `"[sector] acquisition"`, `"[sector] market entry"`
- **Business/GTM**: `"[sector] pricing"`, `"[sector] PLG"`, `"[sector] GTM strategy"`
- **Talent**: `"[sector] layoffs"`, `"[sector] hiring"`, `"[sector] team"`
- **Regulatory**: `"[sector] regulatory"`, `"[sector] compliance"`, `"[sector] policy"`
- **Timeframe**: Start with 1–3d recent; expand to 7–14d if insufficient; verify dates meet freshness thresholds.

**Trusted Sources**:
- **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch
- **Market/Business**: Gartner, Forrester, a16z, First Round Review, Lenny's Newsletter, SaaStr
- **Regulatory/Macro**: Official sites, major newspapers, central banks
- **Talent**: LinkedIn Economic Graph, Carta, Layoffs.fyi
- **Avoid**: PR releases, rumors, unsourced content

**Curate** (select 6–10 news items for 4–6 Qs):
- Freshness: Each meets category threshold (verify publication date)
- Criticality: Each satisfies ≥1 of 5 criteria (map to specific criterion)
- Specifics: Each includes ≥2 quantified data points (dates, $amounts, %, valuations, metrics)
- Multi-stakeholder: Each relevant to ≥2 of 5 roles (list roles affected)
- Category balance: ≥50% from Critical categories (Funding, Market, Business/GTM)

**Plan**: Map 4–6 Qs across 3–4 phases and all 5 core roles (use matrix: Q × Phase × Roles).

### Step 2: Build References

**Reference Types** (≥3 types across Q-set):
- **G#**: Glossary - term | definition (plain language) | analogy | decision context
- **N#**: News - title | source | date (YYYY-MM-DD) | category | URL
- **M#**: Market report - topic | firm | date | key metrics ($, %) | URL
- **F#**: Funding - company | round | amount $ | valuation $ | date | URL
- **R#**: Research - topic | firm | date | key findings (quantified) | URL
- **O#**: Org/talent - company | event type | date | impact | URL
- **A#**: APA 7th citation | [tag: primary/secondary/data]

**Citation**: Use Markdown links: `[Ref: N1][n1]` in text; `[n1]: URL` at end.

**Glossary**: Include only terms used in Q&As with plain-language definition, analogy, and decision context.

### Step 3: Generate Q&A

**Question Patterns**:
- "[Funding news] implications for burn/runway and fundraising strategy?"
- "Market entry given [competitor raise/acquisition]?"
- "[Macro/regulatory change]: hiring and cash plan response?"
- "[News]: Enter now, wait, or pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation.

**Structure** (120–200 words total):
1. **News** (1-2 sentences): What happened, when (date), category `[Ref: N#][n#]`
2. **Impact** (2-3 sentences): Span ≥2 phases + ≥3 quantified metrics (TAM/SAM $X, funding $Y, burn rate Z%, runway Nmo, valuation $V)
3. **Stakeholders** (2-3 sentences): **[Role 1]**: concerns + action; **[Role 2]**: concerns + action
4. **Decision** (2-3 sentences): Compare ≥2 options (e.g., Enter vs Wait vs Pass) with costs/risks/benefits; explicit recommendation + measurable success targets (metric = target by date)
5. **Action** (2-3 bullets): **Immediate (0–2wk)**: task [Owner]; **Short (2wk–2mo)**: task [Owner]
6. **Assumptions & Risks** (1-2 sentences): Critical assumptions; material risks (≥10% impact); revisit trigger (condition + date)
7. **Links**: `[n1]: URL` (bottom of section)

### Step 4: Visuals

**Types**: Market maps, funding timelines, decision trees, burn/runway scenarios, valuation comparables.

**Format**: Mermaid diagrams for flows/timelines; Markdown tables for comparisons.

### Step 5: Validate

**Completeness Checks** (verify counts):
- Phases: 3–4 distinct phases across Q-set (list)
- Roles: All 5 roles present (Founder, CFO, Investor, VP Sales, Product Lead)
- Citations: Every Q has ≥1 citation; ≥3 types across set (count G/N/M/F/R/O/A)
- Glossary: All terms in Qs defined (term | definition | analogy | context)
- Visuals: ≥2 diagrams + ≥1 table present

**Quality Checks** (verify against gates):
- Freshness: Verify each source date meets category threshold (High <2mo, Medium <3mo, Long <6mo)
- Criticality: Each Q maps to ≥1 of 5 criteria (list which)
- Multi-dimensional: Each Q spans ≥2 phases/roles + ≥3 quantified metrics ($, %, dates)
- Actionable: Each Q compares ≥2 options + recommendation + timeline + owner
- Diverse: ≥3 source types across Q-set (count)
- No placeholders: Search for "TBD", "TODO", "[X]", generic examples

**Metadata** (verify presence): Generation date (YYYY-MM-DD) + expiry date (generation + 14d)

## Validation Checklist

| Check | Criteria | Target | Status |
|-------|----------|--------|--------|
| **Freshness** | All sources meet category thresholds (High-Velocity <2mo, Medium <3mo, Long-Term <6mo) | 100% | ☐ |
| **Coverage** | 4–6 Qs (count) across 3–4 phases (count), all 5 roles (list) | 4–6 / 3–4 / 5 | ☐ |
| **Criticality** | All Qs meet ≥1 criterion (list which for each Q) | 100% | ☐ |
| **Impact** | All Qs span ≥2 phases/roles (count) + metrics ($, %, dates) present | 100% | ☐ |
| **Decisions** | All Qs have ≥2 options compared + explicit recommendation + timeline | 100% | ☐ |
| **Citations** | All Qs have ≥1 citation; ≥3 source types across Q-set (G/N/M/F/R/O/A) | 100% / ≥3 | ☐ |
| **Glossary** | All terms in Qs defined with analogy + context | 100% | ☐ |
| **Visuals** | Diagram count ≥2; table count ≥1 | 2+ / 1+ | ☐ |
| **Word Count** | Each Q between 120–200 words (measure with wc) | 120–200 | ☐ |
| **Metadata** | Generation date (YYYY-MM-DD) + expiry date (date + 14d) present | Both | ☐ |

## Question Quality Examples

**✓ Good** (specific news + date + quantified + decision-focused + multi-stakeholder):
- "Series A funding down 35% (Nov 2024): impact on burn rate and fundraising strategy?" → News trigger, quantified (35%), decision (fundraising), roles (Founder+CFO)
- "Competitor $50M raise (Oct 2024): market entry timing?" → News trigger, quantified ($50M), decision (timing), roles (Founder+Product Lead)
- "Fed rate 5.5% (Dec 2024): runway and hiring implications?" → News trigger, quantified (5.5%), decision (runway/hiring), roles (CFO+Founder)

**✗ Bad** (generic, no news trigger, no metrics, single dimension):
- "How does fundraising work?" → No news trigger, definitional, not decision-focused
- "What is TAM?" → Definitional, not linked to news/decision
- "Should we start a company?" → Too generic, no news trigger, no specifics, not formation-stage relevant

## Output Format

### Document Structure

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## 1. Executive Summary
- **Domain/Period/Coverage**: Sector | geography | news period (dates) | stage | primary roles
- **Top Insights**: 2–3 high-impact findings: **[News event (date)]** → Impact (quantified) → Decision (explicit recommendation)
- **Dashboard**: Quick reference table with columns: Phase | News (date) | Criticality criterion | Decision | Timeline (0–2wk / 2wk–2mo)

## 2. Questions by Phase
### Q#: [Specific News Question with Date]
**Phase**: [Phase] | **Roles**: [Role 1, Role 2] | **Criticality**: [Criterion #] | **Word Count**: 120–200

**News** (1-2 sentences): What happened, when (YYYY-MM-DD), category [Ref: N#][n#]

**Impact** (2-3 sentences): Phase 1 impact (metric $X / Y%) + Phase 2 impact (metric $A / B%) + ≥3 quantified metrics total (TAM/SAM, funding, burn rate, runway, valuation)

**Stakeholders** (2-3 sentences): **[Role 1]**: concern | action + **[Role 2]**: concern | action

**Decision** (2-3 sentences): Option A (cost $X, risk Y%) vs Option B (cost $A, risk B%) → **Recommendation**: [Enter/Wait/Pass] because [rationale] → **Success targets**: metric ≥ target by date

**Action** (2-3 bullets):
- **Immediate (0–2wk)**: task description [Owner]
- **Short (2wk–2mo)**: task description [Owner]

**Assumptions & Risks** (1-2 sentences): Assumes [assumption 1, 2]; risks (≥10% impact): [risk 1, 2]; revisit if [trigger condition] by [date]

[n#]: URL
---

## 3. References (≥3 types across Q-set)
**G#. [Term]**: Definition (plain language) | Analogy | Decision context
**N#. [News Title]** (Source, YYYY-MM-DD): Summary | Category | URL
**M#. [Market Report Topic]** (Firm, YYYY-MM-DD): Key metrics ($X, Y%) | URL
**F#. [Company Funding]** (Company, YYYY-MM-DD): Round | Amount $X | Valuation $Y | URL
**R#. [Research Topic]** (Firm, YYYY-MM-DD): Key findings (quantified) | URL
**O#. [Org/Talent Event]** (Company, YYYY-MM-DD): Event type | Impact | URL
**A#. [Citation]**: APA 7th format | [Tag: primary/secondary/data]

## 4. Visuals (≥2 diagrams + ≥1 table)
### Diagram 1: [Type - e.g., Funding Timeline, Market Map, Decision Tree]
```mermaid
[Mermaid diagram code]
```

### Diagram 2: [Type]
```mermaid
[Mermaid diagram code]
```

### Table 1: [Title - e.g., Option Comparison, Valuation Comparables]
| Column 1 | Column 2 (quantified) | Column 3 (quantified) |
|----------|----------------------|----------------------|
| Row data | $X, Y% | metric |

## 5. Validation
[Completed checklist]
```
