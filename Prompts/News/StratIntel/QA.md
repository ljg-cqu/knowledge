# Strategic Intelligence & Market Research News Q&A Generator

**Purpose**: Generate 4-6 decision-critical Q&As from industry news to inform strategic investment, pivot, and risk decisions.

**Cadence**: Monthly | 4-6h | **Validity**: 4 weeks

**Scope**: Research breakthroughs, policy/regulatory shifts, market trends, ESG mandates. Excludes tactical features, operations, speculation.

**Freshness**: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo (from generation date)

**Glossary**: CAGR (Compound Annual Growth Rate), TAM (Total Addressable Market), NPV (Net Present Value), TRL (Technology Readiness Level), ESG (Environmental/Social/Governance), CSO (Chief Strategy Officer), CRO (Chief Research Officer), CIO (Chief Information Officer), IP (Intellectual Property)

## TOC
[I. Inputs & Outputs](#i-inputs--outputs) | [II. Requirements](#ii-requirements) | [III. Execution](#iii-execution) | [IV. Validation](#iv-validation-checklist) | [V. Output Format](#v-output-format) | [VI. Example](#vi-example) | [VII. Use Cases](#vii-use-cases)

## I. Inputs & Outputs

**Inputs**:
- Domain, segment, period
- Org profile: size, stage, regions, products, strategic bets
- Baseline metrics: R&D spend %, TAM, market share, growth rate, ESG exposures
- Strategy hypotheses to test
- Key stakeholders (≥4): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Board
- Constraints: capital, risk appetite, regulatory, capacity

**Outputs**:
- Executive summary with horizon coverage (Short/Medium/Long/Transformational)
- 4-6 Q&As with references, ≥1 diagram, ≥1 table
- Glossary (G≥3) defining acronyms/terms
- Validation report verifying all quality gates

## II. Requirements

**Q&A Structure**: 4-6 total | 150-250w each | News-anchored | ≥1 citation | Decision-critical

**Horizons** (3-4 covered, 1-2Q each):
- Short: 6-18 months | Medium: 18-36 months | Long: 3-5 years | Transformational: 5-10 years (optional)

**Categories** (all 4 covered, each Q tagged with ≥1):
- Research (breakthroughs, tech advances) | Policy (regulations, mandates) | Market (trends, dynamics) | Industry (M&A, partnerships)

**Decision Criticality** (100%): Each Q satisfies ≥1: Blocks investment/pivot | Material risk/opportunity | Multi-stakeholder tension | Action required within horizon | Quantifiable impact

**Stakeholders**: ≥4 roles addressed across all Q&As

**References** (minimum counts):
- G≥3 (Glossary) | N≥3 (News) | A≥2 (Academic) | P≥1 (Policy) | I≥2 (Industry) | R≥5 (APA citations)

**Visuals**: ≥1 diagram (Mermaid) + ≥1 table (Markdown)

**Quality Gates** (all must pass):
1. **Evidence**: Every Q cites ≥1 source with valid URL; zero speculation
2. **Impact**: 100% quantified (CAGR/TAM/$) + ≥2 horizons + ≥2 stakeholder roles
3. **Decision**: 100% include priority label + recommendation + rationale + success metrics; ≥50% compare ≥2 alternatives
4. **Action**: 100% concrete steps with assigned owners; zero abstract recommendations
5. **Limitations**: ≥50% include risks/constraints/when NOT to act

## III. Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

**Search** (8-10 candidates):
- Query pattern: `"[Domain] + [breakthrough|research|policy|M&A|market]"`
- **Sources by category**:
  - Research: arXiv, Nature, Science, IEEE, ACM
  - Policy: Congress.gov, Federal Register, OECD, EU Commission
  - Market: McKinsey, Gartner, Forrester, IDC
  - Industry: CB Insights, Bloomberg, Financial Times, WSJ
- **Avoid**: Marketing content, unverified rumors, speculation

**Curate** (≥8 candidates, all 4 categories):
- Freshness rules met
- Primary/authoritative sources only
- Satisfies ≥1 decision criticality criterion
- Contains concrete details (dates, numbers, quantified impacts)

### Step 2: Build References

Create references for all terms, sources, citations:

- **G#** (Glossary): Term (Acronym) | Definition | Context | Example
- **N#** (News): Title (Source, MM/DD) | Summary | Category | URL | Criticality criterion
- **A/P/I#** (Academic/Policy/Industry): Title (Date) | Key Findings | URL
- **R#** (APA Citations): Full APA 7th format with [Tag]
- **In-text**: Use `[Ref: N1][n1]` with `[n1]: URL` at Q&A end

### Step 3: Generate Q&A

**Pattern**: "[News trigger] → [Strategic decision]?"

**Structure** (150-250w total):
1. **News** (~30w): What, when, why significant [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified metrics (CAGR/TAM/NPV/$)
3. **Stakeholders** (~40w): ≥2 roles with concerns and required actions
4. **Decision** (~50w): Priority (critical/important/optional) | Recommendation | Alternatives (compare ≥2 when applicable) | Rationale | Risks/limits (when NOT to act) | Success metrics
5. **Action** (~20w): Short/Medium/Long steps with owners and metrics
6. **Links**: [n1]: URL

### Step 4: Create Visuals & Validate

**Create**: ≥1 diagram (Mermaid) + ≥1 table (Markdown)

**Validate** (Section IV checklist):
- All 5 Quality Gates
- Coverage: 3-4 horizons, 4 categories, ≥4 roles
- Quantified metrics, 150-250w, freshness, valid URLs

**Submit only if ALL gates pass.**

## IV. Validation Checklist

| # | Check | Criteria | Result |
|---|-------|----------|--------|
| 1 | **Freshness** | ≥60% <3mo, ≥75% <6mo, 100% ≤18mo | __%/<3mo |
| 2 | **Counts** | G≥3, N≥3, A≥2, P≥1, I≥2, R≥5, Q=4-6 | G:__ N:__ A:__ P:__ I:__ R:__ Q:__ |
| 3 | **Coverage** | 3-4 horizons \| 4 categories \| ≥4 roles | H:__ C:__ R:__ |
| 4 | **Quality** | 100% critical \| quantified \| citations \| priority \| actions \| ≥50% alternatives \| ≥50% limitations | __%  |
| 5 | **Word Count** | 100% within 150-250w | __% |
| 6 | **Visuals** | ≥1 diagram + ≥1 table | D:__ T:__ |
| 7 | **Meta** | Generated: __ \| Expires: [+4wk] | |
| 8 | **URLs** | All tested and valid | Pass/Fail |
| 9 | **Calculations** | CAGR, NPV, TAM formulas verified | Pass/Fail |
| 10 | **Consistency** | No contradictions; roles consistent | Pass/Fail |

**Question Quality**:
- **✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?"
- **✗ Bad**: "How does ESG work?" (no news) | "Invest in AI?" (no trigger) | "Competitor feature" (tactical)

## V. Output Format

### A. Structure

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

## 1. Executive Summary
- Top 2 insights with quantified outcomes
- Dashboard table (Horizon | News | Decision | Timeline | Priority)
- Stakeholder roles (≥4)
- Reference counts (G, N, A, P, I, R)

## 2. Horizon Overview
- Table mapping Q&As to horizons

## 3. Q&As by Horizon
- 4-6 Q&As (Short → Transformational)

## 4. References
- G: Glossary (≥3) | N: News (≥3) | A: Academic (≥2) | P: Policy (≥1) | I: Industry (≥2) | R: APA (≥5)

## 5. Validation Report
- Completed checklist from Section IV
```

### B. Executive Summary Template

```markdown
**Domain**: [Industry/Sector] | **Period**: [Q3-Q4'24] | **Coverage**: [# Q&As: Research/Policy/Market/Industry]
**Insights**:
1. [News] ([Date]): [Quantified impact] → [Decision] → [Horizon]
2. [News] ([Date]): [Quantified impact] → [Decision] → [Horizon]
**Dashboard**: [Horizon | News | Decision | Timeline | Priority]
**Roles**: [≥4 stakeholder roles] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]
```

### C. Q&A Template

```markdown
### Q#: [News trigger → Strategic decision]?

**Horizon**: [Short/Medium/Long/Transformational] | **Roles**: [Primary, Secondary] | **Cats**: [Research/Policy/Market/Industry] | **Criticality**: [Criterion]

**News** (~30w): What, when (MM/DD/YY), why significant [Ref: N#][n#]

**Impact** (~60w): ≥2 horizons with quantified metrics
- **[Horizon 1]**: [CAGR/TAM/$/NPV/% numbers]
- **[Horizon 2]**: [CAGR/TAM/$/NPV/% numbers]

**Stakeholders** (~40w): ≥2 roles
- **[Role 1]**: Concern: [X]. Action: [Y with $/timeline]
- **[Role 2]**: Concern: [X]. Action: [Y with $/timeline]

**Decision** (~50w):
- **Priority**: [Critical/Important/Optional]
- **Rec**: [Specific recommendation]
- **Alternatives** (if applicable): (1) [Option 1: cost/benefit] vs (2) [Option 2: cost/benefit]
- **Rationale**: [Why, expected outcomes]
- **Risks/Limits**: [When NOT to act]
- **Success**: [Baseline→target, timeline]

**Action** (~20w):
- **S** (6-18mo): [Role]: [Steps] → [Metric]
- **M** (18-36mo): [Role]: [Steps] → [Metric]
- **L** (3-5yr): [Role]: [Steps] → [Metric]

[n1]: [Full URL]
---
```

### D. Reference Formats

```markdown
**Glossary**
**G#. Term (Acronym)**: [Definition] | Context: [Usage] | Example: [Real usage]

**News Sources**
**N#. Title** (Source, MM/DD/YY): [Summary] | Category: [R/P/M/I] | Criticality: [Criterion] | URL: [URL]

**Academic Papers**
**A#. Title** (Journal, Date): [Key findings] | URL: [DOI/URL]

**Policy Documents**
**P#. Title** (Agency, Date): [Summary and impact] | URL: [URL]

**Industry Reports**
**I#. Title** (Firm, Date): [Key findings with numbers] | URL: [URL]

**APA Citations**
**R#. [Tag]**: Author/Org. (YYYY, Mon DD). *Title*. Publisher. URL
```

## VI. Example

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: Medium, Long | **Roles**: CRO, CSO, CEO | **Cats**: Research | **Criticality**: Blocks R&D investment

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current density), sulfide electrolyte, 1K cycles, TRL 4-5. MIT/Toyota partnership, $50M DOE funding + $1B private investment. 600mi range enables trucking/aviation TAM expansion. [Ref: N1][n1]

**Impact**:
- **Medium (18-36mo)**: R&D pivot triggers IP race. Patent filings +45%. $200M pilot → $2B NPV by '29.
- **Long (3-5yr)**: Market transformation. 600mi range TAM: 15M→60M units (40% CAGR). Carbon -30%. Market share +5-10% = $15B NPV.

**Stakeholders**:
- **CRO**: Concern: TRL 4-5 maturation risk. Action: $200M R&D/3yr, hire 20 PhDs in solid-state electrolytes.
- **CSO**: Concern: IP positioning. Action: M&A evaluation ($1-2B budget), monitor Toyota partnership.
- **CEO**: Concern: $500M capital decision, 5-7yr payback. Action: Approve phased investment with stage-gates, prepare pivot '28-30.

**Decision**: **Priority**: Critical | **Rec**: Invest in R&D + commercialization. Monitor Toyota pilot through '27. | **Alternatives**: (1) Internal R&D $200M/3yr, full IP ownership vs (2) License $100M upfront + 5% royalties | **Rationale**: TRL 4-5 = 5-7yr commercialization. 3x density transformational for long-range. +5-10% share = $15B NPV. | **Risks/Limits**: Sulfide safety concerns, scale-up challenges, supply constraints. Do NOT invest if TRL <4 or Toyota fails by Q2'27. | **Success**: TRL 7 by '27, 200+ patents by '26, 200K units/yr by '30.

**Action**:
- **Short (6-18mo)**: CRO: $50M R&D, 20 PhDs → TRL 5 by Q4'25
- **Medium (18-36mo)**: CRO: $150M pilot → TRL 7 by Q2'27
- **Long (3-5yr)**: CEO: $500M CapEx → 200K units/yr by '30

[n1]: https://nature.com/s41586-024-x

---

## VII. Use Cases

**Applications**:
1. **R&D Roadmaps**: Identify tech investments, assess TRL timelines, prioritize patents
2. **Market Sizing**: Quantify TAM expansion, forecast CAGR, validate business cases
3. **Policy Foresight**: Anticipate regulations (costs, deadlines), assess supply chain risks
4. **ESG Strategy**: Track mandates (carbon targets, reporting), evaluate opportunities
5. **Competitive Positioning**: Monitor M&A, identify partnerships, benchmark developments

**Cadence**: Monthly generation | Quarterly strategy reviews | Annual roadmap planning
