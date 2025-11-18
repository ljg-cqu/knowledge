# Strategic Intelligence & Market Research News Q&A Generator

Generate 4-6 decision-critical Q&As from recent industry news for strategic decisions.

**Cadence**: Monthly | 4-6h | **Validity**: 4 weeks

**Scope**: Research breakthroughs, policy/regulatory shifts, market trends, ESG mandates. Excludes tactical features, operations, speculation.

**Freshness**: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo

## TOC
[I. Inputs & Outputs](#i-inputs--outputs) | [II. Requirements](#ii-requirements) | [III. Execution](#iii-execution) | [IV. Validation](#iv-validation-checklist) | [V. Output Format](#v-output-format) | [VI. Example](#vi-example) | [VII. Use Cases](#vii-use-cases)

## I. Inputs & Outputs

**Inputs**:
- Domain, segment, period
- Org profile: size, stage, regions, products, strategic bets
- Baseline metrics: R&D spend %, TAM, share, growth, ESG exposures
- Strategy hypotheses to test
- Key stakeholders (≥4): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Board
- Constraints: capital, risk appetite, regulatory, capacity

**Outputs**:
- Executive summary with horizon coverage
- 4-6 Q&As with references, ≥1 diagram, ≥1 table
- Glossary (G≥3) defining acronyms/terms used
- Validation report

## II. Requirements

**Q&A Structure**: 4-6 total | 150-250w each | News-anchored | ≥1 citation | Decision-critical

**Horizons** (3-4 covered, 1-2Q each): Short (6-18mo), Medium (18-36mo), Long (3-5yr), Transformational (5-10yr, optional)

**Categories** (all 4 covered): Research, Policy, Market, Industry (each Q has ≥1, total coverage ≥1 each)

**Decision Criticality** (100%): Each Q satisfies ≥1: Blocks investment/pivot | Material risk/opportunity | Multi-stakeholder tension | Action required within horizon | Quantifiable impact

**Stakeholders**: ≥4 roles addressed across all Q&As

**References**: G≥3 (glossary), N≥3 (news), A≥2 (academic), P≥1 (policy), I≥2 (industry), R≥5 (APA)

**Visuals**: ≥1 diagram + ≥1 table

**Quality Gates** (all must pass):
1. **Evidence**: Every Q cites ≥1 source; 0% speculation; URLs valid
2. **Impact**: 100% quantified + ≥2 horizons + ≥2 roles
3. **Decision**: 100% have recommendation + rationale + priority label (critical/important/optional) + success metrics; ≥50% compare ≥2 alternatives
4. **Action**: 100% concrete steps with owners; 0% abstract
5. **Limitations**: ≥50% include risks, constraints, or when NOT to act

## III. Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

**Search** (8-10 candidates):
- Query: `"[Domain] breakthrough|research|policy|M&A|market"`
- **Sources**: arXiv, Nature, Science, IEEE (Research) | Congress.gov, Federal Register, OECD (Policy) | McKinsey, Gartner, Forrester (Market) | CB Insights, Bloomberg, FT (Industry)
- Avoid: Marketing, rumors, speculation

**Curate** (≥8 candidates covering all 4 categories):
- Meets freshness rules
- Primary/authoritative sources
- Satisfies ≥1 Decision Criticality criterion
- Specific details (dates, numbers, quantified impacts)

### Step 2: Build References

**G#**: Term (Acronym) | Definition | Context | Example (only terms used)
**N#**: Title (Source, MM/DD) | Summary | Category | URL | Criticality
**A/P/I#**: Title (Date) | Findings/Impact | URL
**R#**: APA 7th format with [Tag]
**Citation**: Use `[Ref: N1][n1]` and `[n1]: URL`

### Step 3: Generate Q&A

**Pattern**: "[News trigger] → [Strategic decision]?"

**Structure** (150-250w):
1. **News** (~30w): What, when, why [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified (CAGR/TAM/$)
3. **Stakeholders** (~40w): ≥2 roles with concerns, actions
4. **Decision** (~50w): Priority (critical/important/optional) | Recommendation (compare ≥2 alternatives if applicable) | Rationale | Limitations/risks | Success metrics
5. **Action** (~20w): S/M/L steps, owners, metrics
6. **Links**: [n1]: URL

### Step 4: Visuals & Validation

**Create**: ≥1 diagram (Mermaid) + ≥1 table (Markdown)

**Validate**: Quality gates 1-5 | Coverage (3-4 horizons, 4 categories, ≥4 roles) | Quantified impacts | Word counts | Valid citations | Priority labels | Alternatives (≥50%) | Limitations (≥50%) | Freshness rules | Concrete actions

Submit only if ALL quality gates pass.

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

**Question Quality**:
- **✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?"
- **✗ Bad**: "How does ESG work?" (no news) | "Invest in AI?" (no trigger) | "Competitor feature launch" (tactical)

## V. Output Format

### A. Structure

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

1. Executive Summary (Insights | Dashboard | Roles | References)
2. Horizon Overview (Table)
3. Q&As by Horizon
4. References (G, N, A, P, I, R)
5. Validation
```

### B. Executive Summary

```markdown
**Domain**: [Industry] | **Period**: [Q3-Q4'24] | **Coverage**: [# Q&As, 4 categories]
**Insights**: Top 2 high-impact items: [News] ([Date]): [Impact] → [Decision] → [Timeline]
**Dashboard**: [Table: Horizon | News | Decision | Timeline]
**Roles**: [≥4 roles] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]
```

### C. Q&A Template

```markdown
### Q#: [News trigger → Strategic decision]?

**Horizon**: [H] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Criticality**: [Criterion]

**News** (~30w): What, when, why [Ref: N#][n#]
**Impact** (~60w): ≥2 horizons | Quantified (CAGR/TAM/$)
**Stakeholders** (~40w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same
**Decision** (~50w): **Priority**: [Critical/Important/Optional] | **Rec**: [Action] (compare alternatives if applicable) | **Rationale**: Why | **Risks/Limits**: When NOT to act, constraints | **Success**: Metrics
**Action** (~20w): **S**: [Steps+owner] | **M**: Same | **L**: Same

[n1]: URL
---
```

### D. Reference Formats

```markdown
**G#. Term (Acronym)**: Definition | Context | Example
**N#. Title** (Source, MM/DD): Summary | Category | URL
**A#. Paper** (Date): Findings | URL
**P#. Policy** (Date): Summary | Impact | URL
**I#. Report** (Firm, Date): Key findings | URL
**R#. APA 7th [Tag]**: Author/Org. (YYYY, Mon DD). *Title*. Publisher. URL
```

## VI. Example

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: Medium, Long | **Roles**: CRO, CSO, CEO | **Cats**: Research | **Criticality**: Blocks R&D investment

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current), sulfide, 1K cycles, TRL 4-5. MIT/Toyota partnership, $50M DOE + $1B private. 600mi range enables trucking/aviation TAM.

**Impact**: **M (18-36mo)**: R&D pivot + IP race. Patents +45%. $200M pilot → $2B NPV by '29. **L (3-5yr)**: Market transformation. 600mi TAM: 15M→60M units (40% CAGR). Carbon -30%. Market share +5-10% ($15B).

**Stakeholders**: **CRO**: R&D pivot, $200M/3yr. **CSO**: M&A evaluation ($1-2B). **CEO**: $500M investment decision, potential pivot '28-30.

**Decision**: **Priority**: Critical. | **Rec**: Invest R&D + commercialization; Monitor Toyota '27. Alternative: License technology ($100M vs $200M R&D). | **Rationale**: TRL 4-5 → 5-7yr timeline. 3x improvement transformational. +5-10% share ($15B NPV). | **Risks/Limits**: Scaling challenges, sulfide safety, supply chain. Do NOT invest if TRL <4 or pilot fails by Q2'27. | **Success**: Pilot TRL 7 by '27, 200+ patents by '26, production by '30.

**Action**: **S**: CRO: $50M R&D (20 PhDs) → TRL 5 Q4'25. **M**: CRO: $150M pilot → Q2'27. **L**: CEO: $500M CapEx → 200K units/yr.

[n1]: https://nature.com/s41586-024-x

---

## VII. Use Cases

**R&D roadmaps** | **Market sizing** | **Policy foresight** | **ESG strategy** | **Competitive positioning**
