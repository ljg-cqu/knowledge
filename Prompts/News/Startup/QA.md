# Startup & Formation Intelligence Q&A Generator

**Purpose**: Generate 4–6 decision-critical Q&As from startup news to support formation-stage (pre-seed to Series A: <$10M raised, <50 employees, <18mo runway) decisions on market entry, fundraising strategy, product-market fit, and early GTM.

**Target Output**: Self-contained document with news-driven insights, quantified impacts, multi-stakeholder perspectives, explicit recommendations, and actionable timelines. Valid for 2 weeks from generation.

**Rationale for Specifications**: 4-6 Qs (balances comprehensiveness and readability); 120-200 words per Q (sufficient depth without overwhelming); bi-weekly updates (align with startup decision velocity).

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

**Freshness by Category** (age = time from news publication to generation date; rationale: balance recency with decision relevance):
- **High-Velocity** (Market/Competition/Partnerships): <2mo (market dynamics change rapidly; older data risks stale insights)
- **Medium-Velocity** (Funding/VC/Business/Talent/Macro): <3mo (trends evolve quarterly; captures funding cycle patterns)
- **Long-Term** (Regulatory/Compliance): <6mo (policy changes slowly; implementation timelines longer)

**News Categories** (MECE: each news item belongs to exactly one):
1. **Market/Competition**: Market size changes, competitor moves, acquisitions
2. **Funding/VC**: Funding rounds, investor trends, valuations
3. **Business Models & GTM**: Pricing, PLG, sales strategies, channels
4. **Regulatory/Compliance**: Policy changes, legal requirements
5. **Partnerships/Ecosystem**: Strategic partnerships, platform changes
6. **Talent/Labor**: Hiring trends, layoffs, compensation
7. **Economic/Macro**: Interest rates, GDP, inflation, sector-wide shocks

**Priority Categories**:
- **Critical**: Funding/VC, Market/Competition, Business Models & GTM
- **Important**: Regulatory/Compliance, Partnerships/Ecosystem
- **Optional**: Talent/Labor, Economic/Macro (unless material impact ≥10%)

**Include**: Funding, market entry, competition, pricing/GTM, regulatory changes, partnerships, talent shifts, macro shocks with quantified impact.

**Exclude**: Technical details, infrastructure, hype, rumors, trivial updates, mature-org optimization.

**Decision Criticality** (each Q meets ≥1):
1. Blocks go/no-go decision (e.g., market entry, fundraising start)
2. Creates material risk (≥10% impact on runway, valuation, or market position)
3. Affects ≥2 roles with conflicting priorities requiring explicit trade-offs
4. Requires action in 1–6 months with resource commitment
5. Has quantified impact (specific metrics: $, %, timeline)

## Requirements

- **Q&A**: 4–6 total; 120–200 words each (count with `wc -w`); ≥1 citation per Q.
- **Phases**: Cover 3–4 phases: Market Research & Validation | Fundraising | Product–Market Fit | GTM & Early Growth.
- **Category Coverage**: ≥50% from Critical categories (Funding, Market, Business/GTM); remaining from Important/Optional.
- **Stakeholders**: All 5 core roles across Q-set; each Q addresses ≥2 roles.
- **References**: Mix of glossary (G#), news (N#), market reports (M#), funding (F#), research (R#), org/talent (O#), APA citations (A#); ≥3 types across Q-set.
- **Visuals**: ≥2 diagrams + ≥1 table.
- **Quality Gates** (fail document if any fails; verify before finalizing):
  1. **Decision-critical**: Each Q maps to ≥1 of 5 criticality criteria (§Context & Scope)
  2. **Fresh sources**: 100% meet category thresholds (High <2mo, Medium <3mo, Long <6mo); 0 PR/rumors
  3. **Multi-dimensional**: Each Q spans ≥2 phases/roles + ≥3 quantified metrics ($, %, dates)
  4. **Actionable**: Each Q compares ≥2 options + explicit recommendation + timeline + owner
  5. **Diverse sources**: ≥3 distinct reference types (G/N/M/F/R/O/A)

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
- **G#**: Glossary - term | definition (plain language, <30 words) | analogy (concrete example) | decision context (when/why it matters)
- **N#**: News - title | source | date (YYYY-MM-DD) | category | URL
- **M#**: Market report - topic | firm | date | key metrics ($, %) | URL
- **F#**: Funding - company | round | amount $ | valuation $ | date | URL
- **R#**: Research - topic | firm | date | key findings (quantified) | URL
- **O#**: Org/talent - company | event type | date | impact | URL
- **A#**: APA 7th citation | [tag: primary/secondary/data]

**Citation Format**: Use Markdown links: `[Ref: N1][n1]` in text; `[n1]: URL` at document end.

**Glossary Policy**: Include ONLY terms actually used in Q&As that require definition (e.g., "PLG", "burn multiple", "CAC payback"). Define in plain language accessible to all 5 stakeholder roles. Exclude terms with common business meaning (e.g., "revenue", "customer").

### Step 3: Generate Q&A

**Question Patterns** (specific news trigger + date + decision focus):
- "[Funding news with specific data] (YYYY-MM-DD): implications for burn/runway and fundraising strategy?"
- "Market entry given [competitor $Xm raise/acquisition] (YYYY-MM-DD)?"
- "[Macro/regulatory change with quantified impact] (YYYY-MM-DD): hiring and cash plan response?"
- "[Specific news event] (YYYY-MM-DD): Enter now, wait, or pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation, redundancy across Qs.

**Concision Requirements**: State each concept once; reference it thereafter; eliminate filler words ("basically", "essentially", "in order to"); use active voice; combine related points.

**Structure** (120–200 words total):
1. **News** (1-2 sentences): What happened, when (YYYY-MM-DD), category `[Ref: N#][n#]`
2. **Impact** (2-3 sentences): Span ≥2 phases + ≥3 quantified metrics (TAM/SAM $X, funding $Y, burn rate Z%, runway Nmo, valuation $V); cite sources for all metrics
3. **Stakeholders** (2-3 sentences): **[Role 1]**: concerns + action; **[Role 2]**: concerns + action (ensure conflicting priorities are explicit if present)
4. **Decision** (2-3 sentences): 
   - Compare ≥2 options (e.g., Enter vs Wait vs Pass) with explicit trade-offs: costs ($X vs $Y), risks (% probability, impact severity), benefits (quantified outcomes)
   - State when each option is appropriate (conditions favoring each)
   - Explicit recommendation with reasoning ("Recommend X because Y, given assumptions A and B")
   - Measurable success targets (metric ≥ target by date)
5. **Action** (2-3 bullets): **Immediate (0–2wk)**: task [Owner]; **Short (2wk–2mo)**: task [Owner]
6. **Assumptions & Risks** (1-2 sentences): Critical assumptions (what must be true); material risks (≥10% impact on runway/valuation/position); revisit trigger (specific condition + date)
7. **Links**: `[n1]: URL` (bottom of section)

**Balanced Analysis Requirements**: Each Decision section must present trade-offs and limitations; avoid one-sided recommendations; specify when NOT to pursue the recommended option (counterindications).

### Step 4: Visuals

**Types**: Market maps, funding timelines, decision trees, burn/runway scenarios, valuation comparables.

**Format**: Mermaid diagrams for flows/timelines; Markdown tables for comparisons.

### Step 5: Self-Review & Validate

**Self-Review Process** (mandatory before validation):
1. **Fact-check**: Verify all dates, amounts ($), percentages (%), valuations against original sources; flag uncertainties ("estimated", "reported", "unconfirmed")
2. **Contradictions**: Check for conflicting recommendations or data across Qs
3. **Calculations**: Verify derived metrics (burn rate, runway, multiples) with explicit formulas
4. **Terminology**: Ensure consistent term usage; all technical terms in glossary
5. **Placeholders**: Search for "TBD", "TODO", "[X]", "YYYY", "example.com"; replace or remove

**Completeness Checks** (verify counts; document in validation table):
- Phases: 3–4 distinct phases across Q-set (list which)
- Roles: All 5 roles present (Founder, CFO, Investor, VP Sales, Product Lead)
- Citations: Every Q has ≥1 citation; ≥3 types across set (count G/N/M/F/R/O/A)
- Glossary: All terms used in Qs that need definition are defined (term | definition | analogy | context)
- Visuals: ≥2 diagrams + ≥1 table present and referenced in text

**Quality Gates** (verify; fail document if any gate fails):
1. Freshness: Each source meets category threshold (verify publication date vs generation date)
2. Criticality: Each Q maps to ≥1 of 5 criteria (list which criterion for each Q)
3. Multi-dimensional: Each Q spans ≥2 phases/roles (count) + ≥3 quantified metrics ($, %, dates) present
4. Actionable: Each Q compares ≥2 options (with costs/risks) + explicit recommendation + timeline (<2wk, 2wk–2mo) + owner
5. Diverse: ≥3 source types across Q-set (count by type: G/N/M/F/R/O/A)

**Metadata** (verify presence): Generation date (YYYY-MM-DD) + expiry date (generation date + 14d)

## Validation Checklist

| Check | Criteria | Target | Evidence | Status |
|-------|----------|--------|----------|--------|
| **Self-Review** | Facts verified, contradictions checked, calculations confirmed, terminology consistent, no placeholders | 5/5 steps completed | [List steps completed] | ☐ |
| **Freshness** | All sources meet category thresholds (verify each source date) | 100% | [List sources with dates: N1 (2024-11-03), M1 (2024-10-15)...] | ☐ |
| **Coverage** | 4–6 Qs across 3–4 phases, all 5 roles | 4–6 / 3–4 / 5 | [Q count: X; Phases: A,B,C; Roles: all present] | ☐ |
| **Criticality** | Each Q maps to ≥1 of 5 criteria | 100% | [Q1→criterion 2, Q2→criterion 1+4...] | ☐ |
| **Multi-dimensional** | Each Q spans ≥2 phases/roles + ≥3 metrics | 100% | [Q1: 2 phases, 2 roles, 4 metrics ($, %, date, metric)] | ☐ |
| **Actionable** | Each Q compares ≥2 options + recommendation + timeline + owner | 100% | [Q1: 2 options compared, rec: Enter, timeline: 0-2wk, owner: CEO] | ☐ |
| **Diverse** | ≥3 source types across Q-set | ≥3 | [Count: G=2, N=4, M=1, F=2, total types=4] | ☐ |
| **Glossary** | Terms needing definition are defined | 100% | [Terms defined: PLG, burn multiple, CAC payback] | ☐ |
| **Visuals** | ≥2 diagrams + ≥1 table, referenced in text | 2+ / 1+ | [Diagram count: X; Table count: Y; refs confirmed] | ☐ |
| **Word Count** | Each Q: 120–200 words (`wc -w`) | 120–200 | [Q1: 145w, Q2: 167w...] | ☐ |
| **Metadata** | Generation + expiry dates present | Both | [Gen: YYYY-MM-DD; Exp: YYYY-MM-DD] | ☐ |

**Instructions**: Fill "Evidence" column with specific data; check "Status" only when criterion met with evidence.

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
- **Generation**: Date (YYYY-MM-DD) | **Expires**: Date (generation + 14d) | **Valid For**: Formation-stage (<$10M raised, <50 employees)
- **Domain/Period/Coverage**: Sector | geography | news period (start to end dates) | stage | primary roles addressed
- **Top Insights** (2–3 high-impact findings with explicit recommendations):
  - **[News event (YYYY-MM-DD)]** → Impact: [quantified metric $X or Y%] → **Decision**: [Enter/Wait/Pass] by [date] | **Owner**: [Role]
- **Dashboard** (quick reference):

| Phase | News (date) | Criticality | Decision | Timeline | Owner |
|-------|-------------|-------------|----------|----------|-------|
| [Phase] | [Event] (YYYY-MM-DD) | [Criterion #] | [Rec] | [0-2wk/2wk-2mo] | [Role] |

## 2. Questions by Phase
### Q#: [Specific News Question with Date]
**Phase**: [Phase] | **Roles**: [Role 1, Role 2] | **Criticality**: [Criterion #] | **Word Count**: 120–200

**News** (1-2 sentences): What happened, when (YYYY-MM-DD), category [Ref: N#][n#]; flag if uncertain (estimated/reported/unconfirmed)

**Impact** (2-3 sentences): Phase 1 impact (metric $X / Y% [Ref: M#]) + Phase 2 impact (metric $A / B%) + ≥3 quantified metrics total (TAM/SAM, funding, burn rate, runway, valuation); cite all metrics

**Stakeholders** (2-3 sentences): **[Role 1]**: concern | action + **[Role 2]**: concern | action; make trade-offs explicit if priorities conflict

**Decision** (2-3 sentences): 
- Option A (cost $X, risk Y%, benefit Z) vs Option B (cost $A, risk B%, benefit C) → **Trade-offs**: [explicit comparison]
- **When Option A**: [conditions]; **When Option B**: [conditions]; **Avoid if**: [counterindications]
- **Recommendation**: [Enter/Wait/Pass] because [rationale citing data] given [assumptions]
- **Success targets**: metric ≥ target by date

**Action** (2-3 bullets; concrete tasks with tools/methods):
- **Immediate (0–2wk)**: [Specific task with method/tool] [Owner: specific role]
  - Example: "Model 3 burn scenarios in spreadsheet (base/optimistic/pessimistic)" [Owner: CFO]
- **Short (2wk–2mo)**: [Specific task with method/tool] [Owner: specific role]
  - Example: "Complete 10 customer discovery calls using Mom Test framework" [Owner: Product Lead]

**Assumptions & Risks** (1-2 sentences): Assumes [assumption 1, 2] hold; risks (≥10% impact): [risk 1 (probability X%), risk 2 (probability Y%)]; revisit if [specific trigger condition] by [YYYY-MM-DD]

[n#]: URL "Source Title (Date)"
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
[Completed checklist with evidence filled in]

---

## Quick Check (Before Finalizing)

**Self-contained & Complete** (verify all present):
☐ Context: Domain, period, stage, stakeholders defined  
☐ Clarity: All technical terms in glossary with definitions  
☐ Precision: All metrics quantified ($, %, dates); formulas shown  
☐ Relevance: Only decision-critical news; no tangential content

**Scope Coverage** (verify counts):
☐ MECE: Each news in exactly 1 category; no gaps in phase coverage  
☐ Sufficiency: All 5 roles addressed; all dimensions (what/why/how/when/who) covered  
☐ Breadth: ≥2 stakeholder perspectives per Q with explicit trade-offs  
☐ Depth: Specific tools/methods in Action items; concrete implementation details

**Quality Standards** (verify each Q):
☐ Significance: Focus on Critical/Important categories (≥50% Critical)  
☐ Priority: Critical items first; timeline labeled (0-2wk, 2wk-2mo)  
☐ Concision: No repeated concepts; active voice; 120-200 words per Q  
☐ Accuracy: All dates/amounts verified against sources; uncertainties flagged  
☐ Credibility: All sources cited with dates; ≥3 reference types across Q-set  
☐ Logic: Trade-offs explicit; recommendations have reasoning  
☐ Risk/Value: ≥2 options compared with costs/risks/benefits per Q  
☐ Fairness: Counterindications stated; when NOT to pursue option specified

**Format & Validation** (verify structure):
☐ Structure: TOC, headings (H2/H3), lists, tables, diagrams present  
☐ Consistency: Uniform formatting; predictable Q structure  
☐ Evidence: All citations with source+date+URL; evidence column filled  
☐ Verification: Self-review completed (5 steps); contradictions checked  
☐ Practicality: Actions include specific tools/methods/commands  
☐ Success Criteria: Measurable targets (metric ≥ value by date) per Q

**Final Checks**:
☐ Generation date + expiry date present  
☐ No placeholders (TBD, TODO, [X], YYYY, example.com)  
☐ Word count verified per Q (use `wc -w`)  
☐ All Quality Gates passed (see Requirements §Quality Gates)
```
