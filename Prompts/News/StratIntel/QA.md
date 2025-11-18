# Strategic Intelligence & Market Research News Q&A Generator

**Purpose**: Generate 4-6 decision-critical Q&As from industry news to inform strategic investment, pivot, and risk decisions.

**Context**: Problem (fragmented news → missed strategic signals), Scale (4-6 Q&As, ≥4 stakeholder roles), Timeline (monthly generation, 4wk validity), Stakeholders (CEO/CSO/CRO/CIO/CFO), Constraints (4-6h effort, authoritative sources only)

**Cadence**: Monthly | 4-6h | **Validity**: 4 weeks

**Scope**: Research breakthroughs, policy/regulatory shifts, market trends, ESG mandates, corporate governance, major litigation/IP disputes. **Excludes**: tactical features, operations, speculation, marketing content, unverified rumors, routine legal matters.

**Freshness**: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo (from generation date)

**Glossary**: CAGR (Compound Annual Growth Rate), TAM (Total Addressable Market), NPV (Net Present Value: `NPV = Σ(Cash Flow_t / (1+r)^t)`), TRL (Technology Readiness Level: 1-9 scale), ESG (Environmental/Social/Governance), CSO (Chief Strategy Officer), CRO (Chief Research Officer), CIO (Chief Information Officer), IP (Intellectual Property), Board Composition (Director mix: independent, executive, diversity), Fiduciary Duty (Legal obligation to act in shareholders' best interests), Material Litigation (Legal disputes with potential significant financial/reputational impact)

## TOC
[I. Inputs & Outputs](#i-inputs--outputs) | [II. Requirements](#ii-requirements) | [III. Execution](#iii-execution) | [IV. Validation](#iv-validation-checklist) | [V. Output Format](#v-output-format) | [VI. Example](#vi-example) | [VII. Use Cases](#vii-use-cases)

## I. Inputs & Outputs

**Inputs**:
- Domain, segment, period, generation date (YYYY-MM-DD)
- Org profile: size, stage, regions, products, strategic bets, baseline metrics (R&D%, TAM, share%, growth%, ESG)
- Strategy hypotheses, constraints (capital, risk, regulatory, capacity)
- Stakeholders (≥4): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Board

**Outputs**:
- Executive summary (horizon coverage: Short/Medium/Long/Transformational)
- 4-6 Q&As (150-250w each, ≥1 citation, ≥1 diagram, ≥1 table total)
- References: G≥3, N≥3, A≥2, P≥1, I≥2, R≥5 (APA)
- Validation report (all quality gates passed)

## II. Requirements

**Coverage** (MECE):
- **Horizons** (3-4): Short (6-18mo) | Medium (18-36mo) | Long (3-5yr) | Transformational (5-10yr, optional) | 1-2Q each
- **Categories** (all 5): Research | Policy/Regulatory | Market/Industry | ESG/Sustainability | Governance/Legal | Each Q tagged ≥1
- **Stakeholders**: ≥4 roles across all Q&As | ≥2 roles per Q
- **Criticality** (100%): Each Q satisfies ≥1: Blocks investment/pivot | Material risk/opportunity | Multi-stakeholder tension | Action required | Quantifiable impact

**Quality Gates** (all pass):
1. **Evidence**: ≥1 source/Q, valid URL, zero speculation
2. **Impact**: 100% quantified (CAGR/TAM/$), ≥2 horizons/Q, ≥2 roles/Q
3. **Decision**: 100% priority + recommendation + rationale + success metrics; ≥50% compare ≥2 alternatives
4. **Action**: 100% concrete steps + owners; ≥50% include risks/when NOT to act
5. **Format**: 100% within 150-250w | ≥1 diagram + ≥1 table total

**References**: G≥3 | N≥3 | A≥2 | P≥1 | I≥2 | R≥5 (APA)

## III. Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

**Search** (8-10 candidates, query: `"[Domain] + [breakthrough|research|policy|M&A|market|governance|litigation]"`):
- **Research**: arXiv, Nature, Science, IEEE, ACM
- **Policy/Regulatory**: Congress.gov, Federal Register, OECD, EU Commission
- **Market/Industry**: McKinsey, Gartner, Forrester, IDC, CB Insights, Bloomberg
- **ESG/Sustainability**: CDP, SASB, GRI, Corporate sustainability reports
- **Governance/Legal**: SEC filings (10-K, DEF 14A), major legal databases, corporate governance news (WSJ, FT, Bloomberg Law)

**Curate** (≥8 candidates, all 5 categories): Freshness met | Primary sources | ≥1 criticality criterion | Concrete details (dates, numbers, impacts)

### Step 2: Build References

- **G#**: Term (Acronym) | Definition | Context | Example
- **N#**: Title (Source, MM/DD/YY) | Summary | Category (R/P/M/E/G: Research/Policy/Market/ESG/Governance) | Criticality | URL
- **A/P/I/L#**: Title (Date) | Key Findings | URL (Academic/Policy/Industry/Legal)
- **R#**: Full APA 7th with [Tag]
- **In-text**: `[Ref: N1][n1]` with `[n1]: URL` at Q&A end

### Step 3: Generate Q&A

**Pattern**: "[News trigger] → [Strategic decision]?" | 150-250w total

1. **News** (~30w): What, when (MM/DD/YY), why significant [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified (CAGR/TAM/NPV/$)
3. **Stakeholders** (~40w): ≥2 roles (concern, action with $/timeline)
4. **Decision** (~50w): Priority | Recommendation | Alternatives (≥2 if applicable) | Rationale | Risks/when NOT to act | Success metrics (baseline→target, timeline)
5. **Action** (~20w): S/M/L steps with owner + metric
6. **Links**: [n#]: URL

### Step 4: Create Visuals & Validate

**Create**: ≥1 Mermaid diagram + ≥1 Markdown table

**Validate** (IV checklist): All 5 Quality Gates | Coverage (3-4 horizons, 4 categories, ≥4 roles) | Metrics quantified | 150-250w | Freshness | Valid URLs

**Submit only if ALL gates pass.**

## IV. Validation Checklist

| # | Check | Criteria | Result |
|---|-------|----------|--------|
| 1 | **Freshness** | ≥60% <3mo, ≥75% <6mo, 100% ≤18mo | __%/<3mo |
| 2 | **Counts** | G≥3, N≥3, A≥2, P≥1, I≥2, R≥5, Q=4-6 | G:__ N:__ A:__ P:__ I:__ R:__ Q:__ |
| 3 | **Coverage** | 3-4 horizons, 5 categories, ≥4 roles | H:__ C:__ R:__ |
| 4 | **Quality** | 100% critical+quantified+citations+priority+actions; ≥50% alternatives+limitations | __% |
| 5 | **Format** | 100% within 150-250w | __%; D:__ T:__ |
| 6 | **Meta** | Generated: __ | Expires: [+4wk] |
| 7 | **Verification** | URLs valid; calculations verified; no contradictions | Pass/Fail |

**Question Quality Examples**:
- **✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain?" | "Major IP lawsuit $500M (Nov '24): IP strategy?"
- **✗ Bad**: "How does ESG work?" (no news) | "Invest in AI?" (no trigger) | "Competitor feature" (tactical) | "Routine contract dispute" (not material)

## V. Output Format

### A. Structure

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

## 1. Executive Summary
**Domain**: [Industry] | **Period**: [Q3-Q4'24] | **Coverage**: [#Q: R/P/M/I]
**Insights** (top 2): [News] ([Date]): [Quantified impact] → [Decision] → [Horizon]
**Dashboard**: [Horizon | News | Decision | Timeline | Priority]
**Roles**: [≥4] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]

## 2. Horizon Overview
[Table: Q# | Horizon(s) | Category | Priority]

## 3. Q&As by Horizon
[4-6 Q&As: Short → Transformational]

## 4. References
G: [≥3] | N: [≥3] | A: [≥2] | P: [≥1] | I: [≥2] | R: [≥5 APA]

## 5. Validation Report
[IV checklist completed]
```

### B. Q&A Template

```markdown
### Q#: [News trigger → Strategic decision]?

**Horizon**: [S/M/L/T] | **Roles**: [≥2] | **Cat**: [R/P/M/I] | **Criticality**: [Criterion]

**News** (~30w): What, when (MM/DD/YY), why significant [Ref: N#][n#]

**Impact** (~60w): ≥2 horizons quantified
- **[H1]**: [CAGR/TAM/$/NPV/%]
- **[H2]**: [CAGR/TAM/$/NPV/%]

**Stakeholders** (~40w): ≥2 roles
- **[Role 1]**: Concern: [X]; Action: [Y, $/timeline]
- **[Role 2]**: Concern: [X]; Action: [Y, $/timeline]

**Decision** (~50w):
- **Priority**: [Critical/Important/Optional]
- **Rec**: [Recommendation]
- **Alternatives** (if applicable): (1) [Option 1: cost/benefit] vs (2) [Option 2]
- **Rationale**: [Why, outcomes]
- **Risks/Limits**: [When NOT to act]
- **Success**: [Baseline→target, timeline]

**Action** (~20w):
- **S** (6-18mo): [Role]: [Steps] → [Metric]
- **M/L** (as applicable): [Role]: [Steps] → [Metric]

[n#]: [URL]
---
```

### C. Reference Formats

```markdown
**G#. Term (Acronym)**: [Definition] | Context: [Usage] | Example: [Example]
**N#. Title** (Source, MM/DD/YY): [Summary] | Cat: [R/P/M/E/G] | Criticality: [X] | URL: [URL]
**A#. Title** (Journal, Date): [Findings] | URL: [DOI/URL]
**P#. Title** (Agency, Date): [Summary+impact] | URL: [URL]
**I#. Title** (Firm, Date): [Findings+numbers] | URL: [URL]
**L#. Title** (Legal Source, Date): [Case/ruling summary] | URL: [URL]
**R#. [Tag]**: Author/Org. (YYYY, Mon DD). *Title*. Publisher. URL
```

## VI. Example

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: M, L | **Roles**: CRO, CSO, CEO | **Cat**: Research | **Criticality**: Blocks R&D investment

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current), sulfide electrolyte, 1K cycles, TRL 4-5. MIT/Toyota, $50M DOE + $1B private. 600mi range enables trucking/aviation TAM. [Ref: N1][n1]

**Impact**:
- **M (18-36mo)**: IP race, patents +45%. $200M pilot → $2B NPV '29.
- **L (3-5yr)**: TAM 15M→60M (40% CAGR), carbon -30%, share +5-10% = $15B NPV.

**Stakeholders**:
- **CRO**: Concern: TRL 4-5 risk; Action: $200M/3yr, 20 PhDs solid-state.
- **CSO**: Concern: IP position; Action: M&A eval ($1-2B), monitor Toyota.
- **CEO**: Concern: $500M, 5-7yr payback; Action: Phased investment+stage-gates, pivot '28-30.

**Decision**:
- **Priority**: Critical
- **Rec**: Invest R&D+commercialization; monitor Toyota '27.
- **Alternatives**: (1) Internal $200M/3yr, full IP vs (2) License $100M+5% royalty
- **Rationale**: TRL 4-5 = 5-7yr. 3x transformational. +5-10% = $15B NPV.
- **Risks/Limits**: Sulfide safety, scale-up, supply. NOT if TRL<4 or Toyota fails Q2'27.
- **Success**: TRL 7 '27, 200+ patents '26, 200K units/yr '30.

**Action**:
- **S** (6-18mo): CRO: $50M, 20 PhDs → TRL 5 Q4'25
- **M** (18-36mo): CRO: $150M → TRL 7 Q2'27
- **L** (3-5yr): CEO: $500M CapEx → 200K/yr '30

[n1]: https://nature.com/s41586-024-x

---

## VII. Use Cases

**Applications**:
1. **R&D Roadmaps**: Tech investments, TRL timelines, patent priority
2. **Market Sizing**: TAM/CAGR forecasts, business case validation
3. **Policy Foresight**: Regulation anticipation (costs, deadlines), supply chain risks
4. **ESG Strategy**: Mandate tracking (carbon, reporting), opportunities
5. **Governance & Legal**: Board composition trends, material litigation risk, IP strategy, fiduciary obligations
6. **Competitive**: M&A monitoring, partnerships, benchmarking

**Cadence**: Monthly generation | Quarterly reviews | Annual planning
