# Strategic Intelligence & Market Research News Q&A Generator

Generate 4–6 decision-critical Q&As from recent industry news for strategic decisions.

**Cadence**: Monthly | 4-6h | **Validity**: 4 weeks

**Scope**: Research breakthroughs, policy/regulatory shifts, market trends, ESG mandates. Excludes tactical features, operations, speculation.

**Freshness**:
- **HV** (Research/Innovation): ≥70% <2mo, 100% ≤6mo
- **MV** (Policy/Cross-Industry): ≥60% <3mo, 100% ≤9mo
- **LT** (ESG/Cultural): ≥50% <6mo, 100% ≤18mo
- **Overall**: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo

## How to Use

**Inputs**:
- Domain, segment, period (e.g., EV batteries NA/EU, Q3-Q4'24)
- Org profile: size, stage, regions, products, strategic bets
- Baseline metrics: R&D spend %, TAM, share, growth, ESG, regulatory exposures
- Strategy hypotheses to test
- Stakeholders: CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Head of Market Research, Head of ESG, Board
- Constraints: capital, risk appetite, regulatory, capacity

**Output**:
- Executive summary with horizon coverage
- 4–6 Q&As satisfying requirements
- References (G, N, A, P, I, R) with citations
- ≥1 diagram, ≥1 table
- Validation report

## II. Requirements

**Q&A**: 4-6 total | 1-2/horizon | 150-250w | 100% news-driven | ≥1 cite | ≥1 category + impact + decision

**Horizons** (3-4 covered, 1-2 Q each): Short (6-18mo), Medium (18-36mo), Long (3-5yr), Transformational (5-10yr, optional)

**Category Balance**: Each Q tagged with ≥1 category (Research, Policy, Market, Industry). Across all Q&As: Research ≥1, Policy ≥1, Market ≥1, Industry ≥1

**Decision Criticality** (100%): Each Q satisfies ≥1 criterion: Blocks investment/pivot | Material risk/opportunity | Multi-stakeholder tension | Requires action within horizon | Quantifiable impact

**Stakeholders** (≥4 addressed): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Head of Market Research, Head of ESG, Board

**References**: G≥5 (terms used), N≥3-4 (news per freshness), A≥2 (academic), P≥1 (policy), I≥2 (industry), R≥5 (consolidated APA 7th)

**Visuals**: ≥1 diagram + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Criticality**: 100% satisfy ≥1 criterion
2. **Evidence**: 100% cite ≥1 source per freshness; 0% speculation
3. **Impact**: 100% quantified (TAM/CAGR/$, share, etc.) + ≥2 horizons + ≥2 roles
4. **Decision**: 100% recommendation + rationale + success metrics + timeline
5. **Sources**: ≥3 types, max 50%/type, 100% URLs valid
6. **Action**: 100% concrete next steps with owners; 0% abstract

## III. Execution

### Step 1: News Discovery

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

**Search** (≥8-10 candidates, tiered by recency):
- Tier 1 (1-7d), Tier 2 (7-30d), Tier 3 (1-3mo)
- Query: `"[Domain] breakthrough|research|policy|M&A|market"`
- **Sources**: arXiv, Nature, Science, IEEE (Research) | Congress.gov, Federal Register, OECD (Policy) | McKinsey, Gartner, Forrester (Market) | CB Insights, Bloomberg, FT (Industry)
- Avoid: Marketing, rumors, speculation

**Curate** (≥8 candidates: Research ≥3, Policy ≥2, Market ≥2, Industry ≥1):
- Age per freshness rules
- Whitelist OR primary source
- Satisfies ≥1 Decision Criticality criterion
- Specific details (dates, numbers)

### Step 2: Build References

**G# (Glossary)**: Term (Acronym) | Definition + analogy | Context | Example (only terms actually used)

**N# (News)**: Title (Source, MM/DD) | Summary | Cat | URL | Criticality

**A/P/I# (Academic/Policy/Industry)**: Title (Date) | Findings/Impact | URL

**R# (Consolidated)**: APA 7th format with [Tag]

**Citation**: Use `[Ref: N1][n1]` and `[n1]: URL`

### Step 3: Generate Q&A

**Pattern**: "[News trigger] → [Strategic decision]?" (e.g., "Nature solid-state 3x (Oct '24): R&D investment?")

**Structure** (150-250w):
1. **News** (~30w): What, when, why [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified (CAGR/TAM/$)
3. **Stakeholders** (~40w): ≥2 roles with concerns, actions
4. **Decision** (~50w): Recommendation | Rationale | Success metrics
5. **Action** (~20w): S/M/L steps, owners, metrics
6. **Links**: [n1]: URL

### Step 4: Visuals

Create ≥1 diagram (Mermaid: timeline/matrix) + ≥1 table (Markdown)

### Step 5: Validate

**Check all**: Floors met | Glossary 100% used terms | 3-4 horizons | Categories balanced | ≥4 roles | Word count 150-250w | Quantified impact | Citations valid | Decisions concrete | Freshness rules met | 0 speculation

Submit only if ALL quality gates pass.

## IV. Validation Checklist

| # | Check | Criteria | Result | Status |
|---|-------|----------|--------|--------|
| 1 | **Freshness** | Overall: ≥60% <3mo, ≥75% <6mo, 100% ≤18mo | __% <3mo | PASS/FAIL |
| 2 | **Floors** | G≥5, N≥3-4, A≥2, P≥1, I≥2, R≥5, Q=4-6 | G:__ N:__ A:__ P:__ I:__ R:__ Q:__ | PASS/FAIL |
| 3 | **Glossary** | 100% terms used | __%terms | PASS/FAIL |
| 4 | **Horizons** | 3-4 covered (1-2Q each) | __/3-4 | PASS/FAIL |
| 5 | **Categories** | Each ≥1: Res, Pol, Mkt, Ind | R:__ P:__ M:__ I:__ | PASS/FAIL |
| 6 | **Roles** | ≥4 addressed | __/11 | PASS/FAIL |
| 7 | **Criticality** | 100% satisfy ≥1 criterion | __%  | PASS/FAIL |
| 8 | **Impact** | 100% ≥2h+≥2r+quantified | __% | PASS/FAIL |
| 9 | **Decision** | 100% recommendation+rationale+metrics | __% | PASS/FAIL |
| 10 | **Citations** | 100% ≥1cite, 100% URLs valid | __% | PASS/FAIL |
| 11 | **Word Count** | 100% within 150-250w | __% | PASS/FAIL |
| 12 | **Visuals** | ≥1 diagram + ≥1 table | diag:__ tab:__ | PASS/FAIL |
| | **Meta** | Generated: __ | Expires: [+4wk] | INFO |
| | **OVERALL** | All checks PASS | | PASS/FAIL |

**Question Quality**:
- **✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?"
- **✗ Bad**: "How does ESG work?" (no news) | "Invest in AI?" (no trigger) | "Competitor feature launch" (tactical)

## VI. Output Format

### A. TOC

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Horizon Coverage (3-4 horizons)
3. Questions by Horizon: Short (Q1-Q2) | Medium (Q3-Q4) | Long (Q5-Q6)
4. References: G (G1-G5) | N (N1-N4) | A (A1-A2) | P (P1) | I (I1-I2) | R (R1-R5)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
**Domain**: [Industry] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Horizon | News | Decision | Timeline]

**Roles**: [4+ roles] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]
```

### C. Horizon Overview

| # | Horizon | Count | Categories | News | Roles |
|---|---------|-------|------------|------|-------|
| 1 | Short | 1-2 | Research, Policy | [Top] | CEO, CSO |
| 2 | Medium | 1-2 | Market, Industry | [Top] | CSO, CRO |
| 3 | Long | 1-2 | Research, Industry | [Top] | CEO, CRO |
| | **Total** | **4-6** | **4** | **4+** | **≥4** |

### D. Q&A Template

```markdown
### Q#: [News Question + Horizon + Roles]

**Horizon**: [H] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~30w): What, when, why, cat [Ref: N#][n#]

**Impact** (~60w): **Horizons** (≥2) | **Quantified**: CAGR/TAM/$, etc.

**Stakeholders** (~40w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~50w): **Rec**: Invest/Monitor/Pivot/Prepare/Delay/Ignore | **Rationale**: Why | **Success**: Targets

**Action** (~20w): **S (6-18mo)**: Actions+owner | **M (18-36mo)**: Same | **L (3-5yr)**: Same

[n1]: URL
---
```

### E. Reference Formats

```markdown
**G#. Term (Acronym)**: Definition | Analogy | Context | Example

**N#. Title** (Source, MM/DD): Summary | Cat | URL

**A#. Paper** (Date): Findings | URL

**P#. Legislation** (Date): Summary | Impact | URL

**I#. Report** (Firm, Date): TAM/CAGR | Competitive | URL

**R#. APA 7th [Tag]**: Author/Org. YYYY, Mon DD. *Title*. Pub. URL [Tag]
```

## VII. Example (use actual recent news)

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: Long, Medium | **Roles**: CRO, CSO, CEO | **Cats**: Research | **Decision Criticality**: Blocks R&D investment

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current), sulfide, 1K cycles, TRL 4-5. MIT/Toyota partnership, $50M DOE + $1B private. 600mi range → trucking/aviation TAM.

**Impact**: **M (18-36mo)**: R&D pivot + IP. Patents +45%. $200M pilot → $2B NPV by '29. **L (3-5yr)**: Market transformation. 600mi TAM: 15M→60M units (40% CAGR). Carbon -30%. Market share +5-10% ($15B).

**Stakeholders**: **CRO**: R&D pivot, $200M/3yr. **CSO**: M&A evaluation ($1-2B). **CEO**: $500M investment, pivot '28-30.

**Decision**: **Invest** R&D + commercialization; **Monitor** Toyota '27. | **Rationale**: TRL 4-5 → 5-7yr timeline. 3x improvement transformational. +5-10% share ($15B NPV). Risk: scaling. | **Success**: Pilot TRL 7 by '27, 200+ patents by '26, production by '30.

**Action**: **S (6-18mo)**: CRO: $50M R&D (20 PhDs) → TRL 5 Q4'25. **M (18-36mo)**: CRO: $150M pilot → Q2'27. **L (3-5yr)**: CEO: $500M CapEx → 200K units/yr.

[n1]: https://nature.com/s41586-024-x

---

## VIII. Focus Areas

| Area | Strategic Intel |
|------|-----------------|
| **Horizon** | 6mo-10yr (strategy) |
| **Audience** | C-suite, strategy, research |
| **Decisions** | Invest/Monitor/Pivot/Prepare |
| **Metrics** | Market share, CAGR, ESG, NPV |
| **News** | Research, policy, market, industry |
| **Value** | Long-term positioning |

**Use for**: R&D roadmaps | Market sizing | Policy foresight | ESG strategy | Competitive positioning

## IX. Quick Prompt Checklist

- **Self-contained**: All instructions present; no reliance on other files.
- **Context filled**: Domain, period, profile, metrics, theses, stakeholders, constraints specified.
- **Precise & relevant**: Focus on strategically important news with clear metrics and decision window.
- **Complete but MECE**: Horizons, categories, roles covered with minimal overlap.
- **Multi-perspective & deep**: Each question touches ≥2 horizons and roles, with implementation detail.
- **High-signal & concise**: Answers 150-250 words, focus on highest-impact points.
- **Evidence-driven**: Sources authoritative and recent; claims backed or flagged as estimates; uncertainties surfaced.
- **Balanced decisions**: ≥2 options compared with benefits, costs, risks; counterpoints acknowledged.
- **Structured output**: Executive summary, overview, Q&As, references, visuals, validation in Markdown.
- **Actionable & testable**: Concrete S/M/L actions, owners, measurable success criteria with baselines/targets.
