# Startup & Formation Intelligence Q&A Generator

Self-contained prompt for LLMs to generate 4–6 decision-critical Q&As from startup news. Supports market entry, fundraising, product-market fit, and early GTM decisions.

## Context & Scope

- **Cadence**: Bi-weekly, 4–6h effort. Valid 2 weeks from generation date.
- **Domain**: Formation-stage startups (pre-seed–Series A) and corporate new-market initiatives.
- **Stakeholders**: Founder/CEO, CFO, Investor (angel/VC/PE), VP Sales, Product Lead.
- **Decision Horizon**: 6–18 months.
- **Assumptions**: Readers know basic startup metrics (ARR, CAC, LTV, TAM/SAM, burn, runway).
- **Usage**: Provide domain/geography, news period, stage, and ≥2 primary roles when calling LLM.

**Freshness Thresholds**:
- **HV** (Market/Competition/Partnerships): ≥85% <1mo, ≥95% <2mo
- **MV** (Funding/VC/Business Models/Talent/Macro): ≥70% <2mo, ≥90% <3mo
- **LT** (Regulatory/Compliance): ≥50% <3mo, ≥75% <6mo
- **Overall**: ≥70% <2mo, ≥85% <4mo

**News Categories** (each Q covers ≥2): Market/Competition | Funding/VC | Business Models & GTM | Regulatory/Compliance | Partnerships/Ecosystem | Talent/Labor | Economic/Macro

**Include**: Funding, market entry, competition, business models/pricing, GTM, regulatory, partnerships, talent, macro shocks with quantified impact.

**Exclude**: Technical details, infrastructure, hype, rumors, trivial updates, mature-org optimization.

**Decision Criticality** (each Q must meet ≥1):
1. Blocks go/no-go decision (entry, product/GTM, fundraising, hiring)
2. Creates risk (cash, competition, regulatory, talent)
3. Affects ≥2 roles with trade-offs
4. Requires action in 1–6 months
5. Quantified impact

## Requirements

- **Q&A**: 4–6 total; 120–200w each; ≥1 citation each (≥30% with ≥2 citations).
- **Phases** (3–4, 1–2 Q each): Market Research & Validation | Fundraising | Product–Market Fit | GTM & Early Growth.
- **Category Coverage**: Funding ≥50%, Market ≥40%, Business/GTM ≥40%, Talent ≥25%.
- **Stakeholders**: All 5 core roles across Q-set; each Q covers ≥2 roles.
- **References**: G≥6, N≥4, M≥2, F≥2, R≥2, O≥1, A≥6 (scale with Q count).
- **Visuals**: ≥2 diagrams + ≥1 table.
- **Quality Gates** (fail = fix):
  1. Decision Criticality: 100% meet ≥1 criterion
  2. News: Fresh sources only; no PR/rumors
  3. Impact: ≥2 phases + ≥2 roles + quantified metrics
  4. Decision: Explicit decision + rationale + timeline
  5. Sources: ≥3 types; ≤50% from one type
  6. Actionability: 100% concrete actions

## Execution

### Step 1: News Discovery & Curation

**Setup**: Record generation date (YYYY-MM-DD). Specify domain (sector, geography, period, stage).

**Search** (10–15 candidates):
- **Tier 1 (1–3d)**: `"[sector] seed|series A funding"` | `"[sector] pricing|PLG|GTM"` | `"[sector] competitor raise|acquisition"` | `"[sector] layoffs|hiring"` | `"[sector] regulatory"`
- **Tier 2 (7–14d)**: Same queries if Tier 1 insufficient

**Sources**:
- **Funding**: Crunchbase, PitchBook, CB Insights, TechCrunch
- **Market/Business**: Gartner, Forrester, a16z, First Round Review, Lenny's Newsletter, SaaStr
- **Regulatory/Macro**: Official sites, major newspapers, central banks
- **Talent**: LinkedIn Economic Graph, Carta, Layoffs.fyi
- **Avoid**: PR, rumors, unsourced content

**Curate** (10–15: Funding ≥4, Market ≥3, Business/GTM ≥2, Talent ≥2): Meets freshness, from whitelist, satisfies ≥1 criticality criterion, contains specifics (dates, amounts, valuations), relevant to ≥2 roles, cross-checked.

**Allocate**: Plan 4–6 Qs across 3–4 phases, categories, and all 5 core roles.

### Step 2: Build References

**Format**:
- `G#` (term, definition + analogy, context)
- `N#` (news, source, date, category, URL)
- `M#` (market report, sizing, URL)
- `F#` (funding, round, amount, valuation, URL)
- `R#` (research, findings, URL)
- `O#` (org/talent event, company, URL)
- `A#` (APA 7th citation + tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text; `[n1]: URL` at answer end.

**Glossary**: Only terms used in Q&As with plain-language definition, 1–2 analogies, decision context, and numeric example.

**News Entry**: `Title (Source, MM/DD): Summary | Category | URL | Criticality criterion`

### Step 3: Generate Q&A

**Patterns**:
- "[Funding news] implications for burn/runway and fundraising strategy?"
- "Market entry given [competitor raise/acquisition]?"
- "[Macro/regulatory change]: hiring and cash plan response?"
- "[News]: Enter now, wait, or pass?"

**Avoid**: Generic questions, hype, unattributed claims, stale news, speculation.

**Structure** (120–200w):
1. **News** (~25w): What, when, why, category `[Ref: N#][n#]`
2. **Impact** (~50w): ≥2 phases + quantified metrics (market size, funding, burn, runway, valuation) with baseline vs target
3. **Stakeholders** (~35w): **[Role 1]** and **[Role 2]** concerns + 1–2 actions each
4. **Decision** (~50w): Compare ≥2 options (Enter vs Wait vs Pass) with costs/risks/benefits; recommend with 2–3 success targets (runway ≥X mo, burn ≤Y, next round prob ≥Z%)
5. **Action** (~20w): **Immed (0–2wk)** and **Short (2wk–2mo)**: 1–3 tasks + owner each
6. **Assumptions & Risks** (~20w): Critical assumptions, ≥1 material risk, when to revisit
7. **Links**: `[n1]: URL`

**Self-Check**: Age per freshness | Criticality ✓ | ≥2 phases+roles | Alternatives compared | Metrics with targets | Assumptions+risks stated | Logic consistent | 120–200w | ≥1 citation | 0% hype | 100% actionable | Terms in glossary

### Step 4: Visuals

**Types**: Market maps, funding timelines, decision trees (enter/wait/pass), burn/runway scenarios, valuation comparables.

**Format**: Mermaid diagrams for flows/timelines; Markdown tables for comparisons.

### Step 5: Validate

**Quantitative**: Reference floors met | Glossary 100% | 3–4 phases | Category % targets | 5/5 roles | Citations OK | Word count 120–200w | Visuals ≥2 diagrams + ≥1 table | Freshness OK

**Qualitative**: Fresh news only | Criticality 100% | Impact 100% (≥2 phases+roles+quantified) | Decision+rationale+timeline 100% | Source diversity ≥3 types | Links valid | 100% actionable | Evidence-backed

**Checklist**: All validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | No placeholders | Generation + expiry dates (gen + 2wk)

## Validation Report

| # | Check | Criteria | Result | Status |
|---|-------|----------|--------|--------|
| 1 | **Freshness** | Per thresholds above | | PASS/FAIL |
| 2 | **Floors** | G≥6 N≥4 M≥2 F≥2 R≥2 O≥1 A≥6 Q:4–6 | | PASS/FAIL |
| 3 | **Glossary** | 100% terms; ≥50% analogies | | PASS/FAIL |
| 4 | **Phases** | 3–4 (1–2Q each); total 4–6 | | PASS/FAIL |
| 5 | **Categories** | Funding≥50% Market≥40% Business≥40% Talent≥25% | | PASS/FAIL |
| 6 | **Roles** | 5/5 core roles | | PASS/FAIL |
| 7 | **Criticality** | 100% meet ≥1 criterion | | PASS/FAIL |
| 8 | **Impact** | 100% ≥2 phases+roles+quantified | | PASS/FAIL |
| 9 | **Decision** | 100% decision+rationale+timeline | | PASS/FAIL |
| 10 | **Citations** | 100% ≥1 cite | | PASS/FAIL |
| 11 | **Words** | 100% 120–200w | | PASS/FAIL |
| 12 | **Visuals** | ≥2 diagrams; ≥1 table | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+2wk] | | INFO |
| | **OVERALL** | All checks PASS | | PASS/FAIL |

## Question Quality

**Criteria**: News-driven (per Freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1–2 phases) | Multi-stakeholder (≥2 roles) | Quantified impact with targets | Comparative (≥2 alternatives) | Assumptions & risks explicit | Timely | Actionable

**✓ Good**: "Series A funding down 35% (Nov 2024): impact on burn rate?" | "Competitor $50M raise (Oct 2024): market entry strategy?" | "Fed rate 5.5% (Dec 2024): runway implications?"

**✗ Bad**: "How does fundraising work?" (no news) | "What is TAM?" (overview) | "Should we start?" (no trigger)

## Output Format

### A. TOC

```markdown
# [Domain] Startup & Market Entry Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Phase Coverage (3-4 phases)
3. Questions by Phase: Market Research | Fundraising | PMF & GTM
4. References: G | N | M | F | R | O | A
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
## Executive Summary

**Domain**: [Category] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 3-4 cats]

**Insights**: [2 high-impact: News (Date) → Impact → Decision → Timeline]

**Dashboard**: [Table: Phase | News | Decision | Timeline]

**Roles**: [5 core roles] | **Refs**: G=[#] N=[#] M=[#] F=[#] R=[#] O=[#] A=[#]
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

**Phase**: [Phase] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Criticality**: [Criterion]

**News** (~25w): What, when, why, cat [Ref: N#][n#]

**Impact** (~50w): **Phases** (≥2) | **Quantified**: Market [$TAM/SAM] | Funding [$] | Burn [$/mo] | Runway [mo] | Valuation [$]

**Stakeholders** (~35w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Enter/Wait/Pass | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **Immed (0-2wk)**: Actions+owner | **Short (2wk-2mo)**: Same

**Assumptions & Risks** (~20w): Assumptions | Risks | Revisit when

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

**O#. Company Event** (Source, MM/DD): Event | Company | URL

**A#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
```
