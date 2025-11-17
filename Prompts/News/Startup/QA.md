# Startup & Formation Intelligence Q&A Generator

Generate 4–6 decision-critical Q&As from startup news for market entry, fundraising, product-market fit, and early GTM decisions.

## Context & Scope

- **Cadence**: Bi-weekly, valid 2 weeks from generation.
- **Domain**: Formation-stage startups (pre-seed–Series A) and new-market initiatives.
- **Stakeholders**: Founder/CEO, CFO, Investor, VP Sales, Product Lead.
- **Decision Horizon**: 6–18 months.
- **Usage**: Specify domain/geography, news period, stage, and primary roles.

**Freshness by Category**:
- **High-Velocity** (Market/Competition/Partnerships): <2mo preferred
- **Medium-Velocity** (Funding/VC/Business/Talent/Macro): <3mo acceptable
- **Long-Term** (Regulatory/Compliance): <6mo acceptable

**News Categories**: Market/Competition | Funding/VC | Business Models & GTM | Regulatory/Compliance | Partnerships/Ecosystem | Talent/Labor | Economic/Macro

**Include**: Funding, market entry, competition, pricing/GTM, regulatory changes, partnerships, talent shifts, macro shocks with quantified impact.

**Exclude**: Technical details, infrastructure, hype, rumors, trivial updates, mature-org optimization.

**Decision Criticality** (each Q meets ≥1):
1. Blocks go/no-go decision
2. Creates material risk
3. Affects ≥2 roles with trade-offs
4. Requires action in 1–6 months
5. Has quantified impact

## Requirements

- **Q&A**: 4–6 total; 120–200 words each; ≥1 citation per Q.
- **Phases**: Cover 3–4 phases: Market Research & Validation | Fundraising | Product–Market Fit | GTM & Early Growth.
- **Category Coverage**: Balance across categories; prioritize Funding, Market, Business/GTM.
- **Stakeholders**: All 5 core roles across Q-set; each Q addresses ≥2 roles.
- **References**: Mix of glossary (G#), news (N#), market reports (M#), funding (F#), research (R#), org/talent (O#), and APA citations (A#).
- **Visuals**: ≥2 diagrams + ≥1 table.
- **Quality Gates**:
  1. Decision-critical: Each Q meets ≥1 criticality criterion
  2. Fresh sources: Within category freshness thresholds; no PR/rumors
  3. Multi-dimensional: Each Q spans ≥2 phases/roles with quantified metrics
  4. Actionable: Explicit decision + rationale + timeline + concrete actions
  5. Diverse sources: ≥3 source types

## Execution

### Step 1: News Discovery & Curation

**Setup**: Record generation date (YYYY-MM-DD). Specify domain (sector, geography, period, stage).

**Search Queries**:
- `"[sector] seed|series A funding"` | `"[sector] pricing|PLG|GTM"` | `"[sector] competitor raise|acquisition"` | `"[sector] layoffs|hiring"` | `"[sector] regulatory"`
- Start with recent items (1–3d); expand to 7–14d if needed.

**Trusted Sources**:
- **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch
- **Market/Business**: Gartner, Forrester, a16z, First Round Review, Lenny's Newsletter, SaaStr
- **Regulatory/Macro**: Official sites, major newspapers, central banks
- **Talent**: LinkedIn Economic Graph, Carta, Layoffs.fyi
- **Avoid**: PR releases, rumors, unsourced content

**Curate**: Select items that meet freshness thresholds, satisfy ≥1 criticality criterion, contain specifics (dates, amounts, valuations), and are relevant to ≥2 roles. Balance across Funding, Market, Business/GTM, and Talent categories.

**Plan**: Map 4–6 Qs across 3–4 phases and all 5 core roles.

### Step 2: Build References

**Types**:
- **G#**: Glossary (term, definition + analogy, context)
- **N#**: News (source, date, category, URL)
- **M#**: Market report (sizing, URL)
- **F#**: Funding (round, amount, valuation, URL)
- **R#**: Research (findings, URL)
- **O#**: Org/talent event (company, URL)
- **A#**: APA 7th citation + tag

**Citation**: Use Markdown links: `[Ref: N1][n1]` in text; `[n1]: URL` at end.

**Glossary**: Include only terms used in Q&As with plain-language definition, analogy, and decision context.

### Step 3: Generate Q&A

**Question Patterns**:
- "[Funding news] implications for burn/runway and fundraising strategy?"
- "Market entry given [competitor raise/acquisition]?"
- "[Macro/regulatory change]: hiring and cash plan response?"
- "[News]: Enter now, wait, or pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation.

**Structure** (120–200 words):
1. **News**: What, when, why, category `[Ref: N#][n#]`
2. **Impact**: Span ≥2 phases with quantified metrics (market size, funding, burn, runway, valuation)
3. **Stakeholders**: **[Role 1]** and **[Role 2]** concerns + actions
4. **Decision**: Compare ≥2 options (Enter vs Wait vs Pass) with costs/risks/benefits; recommend with success targets
5. **Action**: **Immediate (0–2wk)** and **Short (2wk–2mo)** tasks + owner
6. **Assumptions & Risks**: Critical assumptions, material risks, when to revisit
7. **Links**: `[n1]: URL`

### Step 4: Visuals

**Types**: Market maps, funding timelines, decision trees, burn/runway scenarios, valuation comparables.

**Format**: Mermaid diagrams for flows/timelines; Markdown tables for comparisons.

### Step 5: Validate

**Completeness**: 3–4 phases covered | All 5 roles addressed | Citations present | Glossary complete | Visuals included (≥2 diagrams + ≥1 table)

**Quality**: Fresh sources per thresholds | All Qs meet criticality criteria | Multi-dimensional impact (≥2 phases/roles + quantified) | Actionable decisions with rationale | Diverse sources (≥3 types) | No placeholders

**Metadata**: Generation date + expiry (2 weeks)

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| **Freshness** | Sources meet category thresholds | ☐ |
| **Coverage** | 4–6 Qs across 3–4 phases, all 5 roles | ☐ |
| **Criticality** | All Qs meet ≥1 criterion | ☐ |
| **Impact** | All Qs span ≥2 phases/roles with quantified metrics | ☐ |
| **Decisions** | All Qs have decision + rationale + timeline | ☐ |
| **Citations** | All Qs cited; diverse sources (≥3 types) | ☐ |
| **Glossary** | Terms defined with analogies | ☐ |
| **Visuals** | ≥2 diagrams + ≥1 table | ☐ |
| **Word Count** | 120–200 words per Q | ☐ |
| **Metadata** | Generation date + 2-week expiry | ☐ |

## Question Quality Examples

**✓ Good**:
- "Series A funding down 35% (Nov 2024): impact on burn rate and fundraising strategy?"
- "Competitor $50M raise (Oct 2024): market entry timing?"
- "Fed rate 5.5% (Dec 2024): runway and hiring implications?"

**✗ Bad**:
- "How does fundraising work?" (no news trigger)
- "What is TAM?" (definitional, not decision-focused)
- "Should we start a company?" (too generic)

## Output Format

### Document Structure

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## 1. Executive Summary
- **Domain/Period/Coverage**: Key metadata
- **Top Insights**: 2–3 high-impact findings (News → Impact → Decision)
- **Dashboard**: Quick reference table (Phase | News | Decision | Timeline)

## 2. Questions by Phase
### Q#: [News Question]
**Phase**: [Phase] | **Roles**: [Role 1, Role 2] | **Criticality**: [Criterion]

**News**: Event summary with citation [Ref: N#][n#]

**Impact**: Cross-phase effects with quantified metrics (TAM/SAM, funding, burn, runway, valuation)

**Stakeholders**: **[Role 1]** and **[Role 2]** concerns + actions

**Decision**: Recommendation (Enter/Wait/Pass) | Rationale | Success targets

**Action**: **Immediate (0–2wk)** and **Short (2wk–2mo)** tasks with owners

**Assumptions & Risks**: Key assumptions | Material risks | Revisit triggers

[n#]: URL
---

## 3. References
**G#. Term**: Definition | Analogy | Context
**N#. News Title** (Source, Date): Summary | Category | URL
**M#. Market Report** (Firm, Date): Sizing | URL
**F#. Funding Event** (Company, Date): Round | Amount | Valuation | URL
**R#. Research** (Firm, Date): Findings | URL
**O#. Org/Talent Event** (Company, Date): Event | URL
**A#. Citation** (APA 7th): Full citation [Tag]

## 4. Visuals
[Diagrams and tables]

## 5. Validation
[Completed checklist]
```
