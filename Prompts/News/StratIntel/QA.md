# Strategic Intelligence & Market Research News Q&A Generator

**Purpose**: Generate 4-6 decision-critical Q&As from recent industry news to inform strategic investment, pivot, and risk decisions.

**Cadence**: Monthly | 4-6h | **Validity**: 4 weeks

**Scope**: Research breakthroughs, policy/regulatory shifts, market trends, ESG (Environmental/Social/Governance) mandates. Excludes tactical features, operations, speculation.

**Freshness**: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo (calculated from generation date)

## TOC
[I. Inputs & Outputs](#i-inputs--outputs) | [II. Requirements](#ii-requirements) | [III. Execution](#iii-execution) | [IV. Validation](#iv-validation-checklist) | [V. Output Format](#v-output-format) | [VI. Example](#vi-example) | [VII. Use Cases](#vii-use-cases) | [VIII. Pre-Submission Verification](#viii-pre-submission-verification)

## I. Inputs & Outputs

**Inputs**:
- Domain, segment, period
- Org profile: size, stage, regions, products, strategic bets
- Baseline metrics: R&D spend %, TAM (Total Addressable Market), market share, growth rate, ESG exposures
- Strategy hypotheses to test
- Key stakeholders (≥4): CEO, CSO (Chief Strategy Officer), CRO (Chief Research Officer), CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Board
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
- G≥3 (Glossary: acronyms/terms) | N≥3 (News: primary sources) | A≥2 (Academic: papers) | P≥1 (Policy: gov/regulatory) | I≥2 (Industry: reports) | R≥5 (APA formatted citations)

**Visuals**: ≥1 diagram (Mermaid) + ≥1 table (Markdown)

**Quality Gates** (all must pass before submission):
1. **Evidence**: Every Q cites ≥1 source with valid URL; zero speculation
2. **Impact**: 100% quantified (with CAGR/TAM/$) + ≥2 horizons + ≥2 stakeholder roles
3. **Decision**: 100% include priority label + recommendation + rationale + success metrics; ≥50% compare ≥2 alternatives
4. **Action**: 100% concrete steps with assigned owners; zero abstract recommendations
5. **Limitations**: ≥50% include risks/constraints/when NOT to act

## III. Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

**Search** (8-10 candidates):
- Query pattern: `"[Domain] + [breakthrough|research|policy|M&A|market]"`
- **Authoritative sources by category**:
  - Research: arXiv, Nature, Science, IEEE, ACM
  - Policy: Congress.gov, Federal Register, OECD, EU Commission
  - Market: McKinsey, Gartner, Forrester, IDC
  - Industry: CB Insights, Bloomberg, Financial Times, WSJ
- **Avoid**: Marketing content, unverified rumors, speculation without evidence

**Curate** (≥8 candidates covering all 4 categories):
- **Freshness**: Meets ≥60% <3mo, ≥75% <6mo, 100% ≤18mo rules
- **Authority**: Primary/authoritative sources only (no secondary reports without citations)
- **Decision Criticality**: Each satisfies ≥1 criterion (blocks investment/pivot | material risk/opportunity | multi-stakeholder tension | action required within horizon | quantifiable impact)
- **Specificity**: Contains concrete details (exact dates, specific numbers, quantified impacts with units)

### Step 2: Build References

Create references for all terms, sources, and citations:

- **G#** (Glossary): Term (Acronym) | Definition | Context | Example (only terms actually used in Q&As)
- **N#** (News): Title (Source, MM/DD) | Summary | Category tag | URL | Decision Criticality criterion
- **A/P/I#** (Academic/Policy/Industry): Title (Date) | Key Findings/Impact | URL
- **R#** (APA Citations): Full APA 7th format with [Tag]
- **In-text**: Use `[Ref: N1][n1]` format with `[n1]: URL` at Q&A end

### Step 3: Generate Q&A

**Pattern**: "[News trigger] → [Strategic decision]?"

**Structure** (150-250w total):
1. **News** (~30w): What happened, when, why significant [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified metrics (CAGR=Compound Annual Growth Rate, TAM=Total Addressable Market, NPV=Net Present Value, or $ amounts)
3. **Stakeholders** (~40w): ≥2 roles with specific concerns and required actions
4. **Decision** (~50w): Priority level (critical/important/optional) | Recommendation (compare ≥2 alternatives when applicable) | Rationale (why) | Limitations/risks (when NOT to act) | Success metrics
5. **Action** (~20w): Short/Medium/Long-term steps with assigned owners and metrics
6. **Links**: [n1]: URL

### Step 4: Visuals & Validation

**Create**: ≥1 diagram (Mermaid) + ≥1 table (Markdown)

**Validate** (use checklist in Section IV):
- All 5 Quality Gates (Evidence, Impact, Decision, Action, Limitations)
- Coverage requirements (3-4 horizons, 4 categories, ≥4 roles)
- Quantified metrics, word counts (150-250w), freshness rules, valid URLs

**Submit only if ALL quality gates pass.**

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

**Question Quality Examples**:
- **✓ Good** (news-anchored, strategic, decision-critical): "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?"
- **✗ Bad**: "How does ESG work?" (no news anchor) | "Invest in AI?" (no specific trigger) | "Competitor feature launch" (tactical, not strategic)

## V. Output Format

### A. Structure

Final output document structure:

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

## 1. Executive Summary
- Top 2 high-impact insights with quantified outcomes
- Dashboard table (Horizon | News | Decision | Timeline | Priority)
- Stakeholder roles addressed (≥4)
- Reference counts (G, N, A, P, I, R)

## 2. Horizon Overview
- Table mapping Q&As to horizons (Short/Medium/Long/Transformational)

## 3. Q&As by Horizon
- 4-6 Q&As following template in Section V.C
- Organized by horizon (Short first → Transformational last)

## 4. References
- G: Glossary (≥3 terms)
- N: News sources (≥3)
- A: Academic papers (≥2)
- P: Policy documents (≥1)
- I: Industry reports (≥2)
- R: APA citations (≥5)

## 5. Validation Report
- Checklist from Section IV with all fields completed
```

### B. Executive Summary Template

```markdown
**Domain**: [Industry/Sector] | **Period**: [Q3-Q4'24] | **Coverage**: [# Q&As across 4 categories: Research/Policy/Market/Industry]
**Insights**: Top 2 high-impact items with quantified impact:
1. [News title] ([Date]): [Quantified impact] → [Decision type] → [Timeline/Horizon]
2. [News title] ([Date]): [Quantified impact] → [Decision type] → [Timeline/Horizon]
**Dashboard**: [Table with columns: Horizon | News | Decision | Timeline | Priority]
**Roles Addressed**: [List ≥4 stakeholder roles] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]
```

### C. Q&A Template

```markdown
### Q#: [Specific news trigger → Strategic decision question]?

**Horizon**: [Short/Medium/Long/Transformational] | **Roles**: [Primary, Secondary] | **Cats**: [Research/Policy/Market/Industry] | **Criticality**: [Which criterion satisfied]

**News** (~30w): What happened, when (MM/DD/YY), why significant [Ref: N#][n#]

**Impact** (~60w): ≥2 horizons with quantified metrics
- **[Horizon 1]**: [Specific impact with CAGR/TAM/$/NPV/% numbers]
- **[Horizon 2]**: [Specific impact with CAGR/TAM/$/NPV/% numbers]

**Stakeholders** (~40w): ≥2 roles with specific concerns and required actions
- **[Role 1]**: [Specific concerns] → [Required actions with $ amounts/timelines]
- **[Role 2]**: [Specific concerns] → [Required actions with $ amounts/timelines]

**Decision** (~50w):
- **Priority**: [Critical/Important/Optional]
- **Rec**: [Specific recommendation]
- **Alternatives** (if applicable): (1) [Option 1 with cost/benefit] vs (2) [Option 2 with cost/benefit]
- **Rationale**: [Why this recommendation, expected outcomes]
- **Risks/Limits**: [Specific risks, constraints, when NOT to act]
- **Success**: [Measurable outcomes with baseline→target, timeline]

**Action** (~20w):
- **S** (6-18mo): [Role]: [Specific steps] → [Metric/milestone]
- **M** (18-36mo): [Role]: [Specific steps] → [Metric/milestone]
- **L** (3-5yr): [Role]: [Specific steps] → [Metric/milestone]

[n1]: [Full URL]
---
```

### D. Reference Formats

```markdown
**Glossary**
**G#. Term (Acronym)**: [Definition] | Context: [When/how used] | Example: [Real usage]

**News Sources**
**N#. Title** (Source, MM/DD/YY): [Summary] | Category: [Research/Policy/Market/Industry] | Criticality: [Which criterion] | URL: [Full URL]

**Academic Papers**
**A#. Paper Title** (Journal, Date): [Key findings] | URL: [DOI or URL]

**Policy Documents**
**P#. Policy Title** (Agency, Date): [Summary and impact] | URL: [Official URL]

**Industry Reports**
**I#. Report Title** (Firm, Date): [Key findings with numbers] | URL: [Full URL]

**APA Citations**
**R#. [Tag]**: Author/Org. (YYYY, Mon DD). *Title*. Publisher. URL
```

## VI. Example

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: Medium, Long | **Roles**: CRO, CSO, CEO | **Cats**: Research | **Criticality**: Blocks R&D investment

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current density), sulfide electrolyte, 1K cycles, TRL (Technology Readiness Level) 4-5. MIT/Toyota partnership, $50M DOE funding + $1B private investment. 600mi range enables trucking/aviation TAM expansion. [Ref: N1][n1]

**Impact**:
- **Medium (18-36mo)**: R&D pivot triggers IP (Intellectual Property) race. Patent filings +45%. $200M pilot investment → $2B NPV (Net Present Value) by '29.
- **Long (3-5yr)**: Market transformation. 600mi range TAM expands from 15M→60M units (40% CAGR). Carbon emissions -30%. Market share +5-10% worth $15B NPV.

**Stakeholders**:
- **CRO (Chief Research Officer)**: Concern: Technology maturation risk at TRL 4-5. Action: Allocate $200M R&D budget over 3yr, hire 20 PhDs specializing in solid-state electrolytes.
- **CSO (Chief Strategy Officer)**: Concern: Competitive positioning in IP race. Action: Evaluate M&A targets ($1-2B acquisition budget), monitor Toyota partnership developments.
- **CEO**: Concern: $500M capital allocation decision with 5-7yr payback. Action: Approve phased investment with stage-gates, prepare for potential business model pivot '28-30.

**Decision**: **Priority**: Critical | **Rec**: Invest in R&D + commercialization pipeline. Monitor Toyota pilot progress through '27. | **Alternatives**: (1) Internal R&D $200M/3yr with full IP ownership vs (2) License technology $100M upfront with 5% royalties | **Rationale**: TRL 4-5 indicates 5-7yr commercialization timeline. 3x energy density is transformational for long-range applications. Projected +5-10% market share worth $15B NPV. | **Risks/Limits**: Sulfide electrolyte safety concerns, manufacturing scale-up challenges, supply chain constraints. Do NOT invest if TRL drops <4 or Toyota pilot fails by Q2'27. | **Success**: Pilot achieves TRL 7 by '27, file 200+ patents by '26, production capacity 200K units/yr by '30.

**Action**:
- **Short (6-18mo)**: CRO: Allocate $50M R&D, hire 20 PhDs → Achieve TRL 5 by Q4'25
- **Medium (18-36mo)**: CRO: Deploy $150M pilot facility → Demonstrate TRL 7 by Q2'27
- **Long (3-5yr)**: CEO: Commit $500M CapEx for production scale-up → 200K units/yr capacity by '30

[n1]: https://nature.com/s41586-024-x

---

## VII. Use Cases

**Primary applications**:
1. **R&D Roadmaps**: Identify emerging technologies requiring investment, assess TRL progression timelines, prioritize patent filings
2. **Market Sizing**: Quantify TAM expansion from breakthroughs, forecast adoption curves (CAGR), validate business case assumptions
3. **Policy Foresight**: Anticipate regulatory changes (compliance costs, deadlines), assess policy risks to supply chains
4. **ESG Strategy**: Track sustainability mandates (carbon reduction targets, reporting requirements), evaluate ESG investment opportunities
5. **Competitive Positioning**: Monitor M&A activity, identify partnership opportunities, benchmark against industry developments

**Cadence**: Monthly generation | Quarterly strategy reviews | Annual roadmap planning

## VIII. Pre-Submission Verification

Before finalizing output, verify:
- [ ] All URLs tested and valid (no 404s, paywalls documented)
- [ ] Calculations verified (CAGR, NPV, TAM formulas checked)
- [ ] Acronyms defined in Glossary (G≥3) before first use
- [ ] Freshness rules met (≥60% <3mo calculated from generation date)
- [ ] No contradictions between Q&As (cross-check recommendations)
- [ ] Stakeholder roles consistent across document (CEO, CRO, CSO, etc.)
- [ ] All 5 Quality Gates passed (Evidence, Impact, Decision, Action, Limitations)
- [ ] Word counts within 150-250w per Q&A
- [ ] Priority labels present (Critical/Important/Optional) for all Q&As
- [ ] ≥50% of Q&As compare ≥2 alternatives
- [ ] ≥50% of Q&As include explicit limitations/risks
