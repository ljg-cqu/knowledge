# Strategic Intelligence & Market Research News Q&A Generator (Minimal Viable)

Generate 4–6 decision-critical Q&As from recent industry news—minimal viable tracking for strategic decisions with limited time.

**Cadence**: Monthly | 4-6h effort | **Expires**: 4 weeks from generation

**Scope**: Decision-critical strategic news only—research breakthroughs, policy/regulatory shifts, market trends, ESG mandates affecting strategy. Excludes tactical features, daily operations, sales execution, routine finance, speculation.

**Freshness** (category-adaptive):
- **HV** (Research/Innovation/Consumer/Analysis): ≥70% <2mo, ≥90% <3mo, 100% ≤6mo
- **MV** (Policy/Cross-Industry): ≥60% <3mo, ≥80% <6mo, 100% ≤9mo
- **LT** (ESG/Cultural): ≥50% <6mo, ≥70% <12mo, 100% ≤18mo
- **Overall**: ≥60% <3mo, ≥75% <6mo, ≥85% <9mo, 100% ≤18mo
- **Validity**: 4 weeks; re-validate if used beyond 4 weeks

## How the LLM should use this file

- **Role**: Act as a strategic intelligence and market research analyst for a post-PMF organization.
- **Inputs (fill before running)**:
  - Domain and segment (e.g., EV batteries in NA/EU).
  - Period under review (e.g., last 4 weeks).
  - Organization profile: size, stage, regions, main products, current strategic bets.
  - Baseline strategic metrics: R&D spend %, core TAM and current share, growth rates, ESG ratings/targets, key regulatory exposures.
  - Existing strategy hypotheses or theses to test (e.g., "solid-state by 2030").
  - Stakeholders and their goals (11 core roles; add others as relevant): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Head of Market Research, Head of ESG, Board.
  - Constraints: capital envelope, risk appetite, regulatory boundaries, execution capacity.
- **Objective**: Using only this file, produce:
  - Executive summary and horizon coverage overview.
  - 4–6 Q&As that satisfy all requirements below.
  - Glossary and reference sections (G, N, A, P, I, R) with citations.
  - At least 1 diagram and 1 table in Markdown.
  - Completed validation report with quantitative and qualitative checks.
- **Output expectations**:
  - Respect word counts, horizons, category floors, and freshness thresholds.
  - Focus on strategically meaningful news meeting decision criticality.
  - Prefer concrete numbers over vague language.
  - Cover multiple stakeholder viewpoints, trade-offs, risks, limitations.
  - Provide clear recommendations, action paths, success metrics.
  - Use structured Markdown for scanability.

## II. Requirements

**Q&A**: 4-6 total | 1-2/horizon | 150-250w | 100% news-driven | 100% ≥1 cite | ≥1 category + impact + decision

**Horizons** (3-4, 1-2 Q each): Short (6-18mo), Medium (18-36mo), Long (3-5yr), (Optional: Transformational 5-10yr if decision-critical)

**Category Coverage** (min): Research ≥40%, Policy ≥30%, Market ≥30%, Industry ≥25%

**Decision Criticality** (100%): Each Q satisfies ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥4/11): CEO, CSO, CRO, CIO, CFO, VP Corp Dev (core roles only)

**References** (build before Q&A): G≥5 (100% terms used), N≥3-4 (per freshness), A≥2 (academic), P≥1 (policy), I≥2 (industry), R≥5 (APA 7th+tag)

**Visuals**: ≥1 diagram + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion
2. **News**: 100% cite ≥1 per freshness; 0% hype/speculation
3. **Impact**: 100% ≥2 horizons + ≥2 roles + quantified (TAM/CAGR/$, policy $, market share)
4. **Decision**: 100% decision + rationale + criteria + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionable**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation

**Record generation date (YYYY-MM-DD)—calculate ages from this.**

1. **Domain**: Industry/market/sector + period

2. **Search** (≥8-10 candidates, tiered):

   **Tier 1** (1-7d): `"[Domain] breakthrough|research|policy|M&A|market"` + 1-7d

   **Tier 2** (7-30d if insufficient): Same + 7-30d

   **Tier 3** (1-3mo if still insufficient): Same + 1-3mo

   **Sources** (whitelist):
   - **Research**: arXiv, Nature, Science, IEEE, universities
   - **Policy**: Congress.gov, Federal Register, OECD, WTO, think tanks
   - **Market**: McKinsey, Gartner, Forrester, IDC
   - **Industry**: CB Insights, Bloomberg, FT
   - **Avoid**: Marketing, rumors, speculation

   **Tools**: Perplexity, ChatGPT, Google, Scholar

3. **Curate** (≥8-10 candidates: Research ≥3, Policy ≥2, Market ≥2, Industry ≥1):
   - Age per freshness
   - Whitelist OR primary source
   - Satisfies ≥1 Decision Criticality criterion
   - Specific details (dates, names, numbers)
   - Not marketing/rumors

4. **Verify**: Check decision criticality; retry if fail

5. **Allocate**: 4-6 Q × 3-4 horizons (1-2 each) × 4 categories × ≥4 roles

### Step 2: Build References

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | A# (academic) | P# (policy) | I# (industry) | R# (APA 7th+tag)

**Citation**: Use Markdown links `[Ref: N1][n1]` and `[n1]: URL`. Prefer authoritative recent sources. Flag approximations.

**Floors**: G≥5 (100% terms used), N≥3-4, A≥2, P≥1, I≥2, R≥5

**Glossary** (only terms used):
- Coverage: Only used terms (TAM, CAGR, etc.)
- Clarity: Plain language
- Analogies: 1-2 comparisons
- Context: Why matters for decisions
- Examples: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality

### Step 3: Generate Q&A

**Patterns**: "[Research] → [R&D] investment?" | "[Policy] → [Compliance] timeline?" | "[Market] shift → [Positioning]?"

**Avoid**: Tactical, speculation, hype, stale news

**Structure** (150-250w):
1. **News** (~30w): What, when, why, cat [Ref: N#][n#]
2. **Impact** (~60w): ≥2 horizons + quantified effects (CAGR/TAM/$, etc.)
3. **Stakeholders** (~40w): ≥2 roles with concerns, actions
4. **Decision** (~50w): Compare ≥2 options; rationale, benefits, costs, risks
5. **Action** (~20w): S/M/L next steps, owners, 2-3 success metrics
6. **Links**: [n1]: URL

**Self-Check**: Age OK | Decision criticality | ≥2 horizons | ≥2 roles | ≥2 options | Risks stated | 150-250w | Quantified | ≥1 citation | Links valid | 0% hype | Actionable | Terms in glossary | Uncertainties flagged

### Step 4: Visuals (≥1 diagram + ≥1 table)

**Types**: Horizon timelines, TAM/CAGR curves, 2×2 matrices

**Format**: Mermaid, Markdown tables

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | Floors met

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥4 roles | Actions

### Step 6: Validate (fail ANY = stop, fix, re-run)

**Quantitative**: Floors met | Glossary 100% terms | 3-4 horizons | Category targets | ≥4 roles | Citations present | Sample within 150-250w | Visuals count | Decisions and timelines | Freshness rules

**Qualitative**: News meets freshness, no hype | Q&As meet criteria | Impacts quantified | Decisions compare options | Sources ≥3 types | Links resolve | Quantification plausible | Recommendations concrete | Evidence cited | Uncertainties labelled | Search documented | Checks: calculations, terminology, coherence, metrics

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | Freshness OK | Evidence 100% | URLs valid | Dates (gen + expire=gen+4wks) | Search documented

## IV. Validation Report

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<2mo, __%<3mo \| MV: __%<3mo \| Overall: __%<3mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ A:__ P:__ I:__ R:__ Q:__ | ≥5,≥3-4,≥2,≥1,≥2,≥5,4-6 | | PASS/FAIL |
| 3 | **Glossary** | __%terms | 100% | | PASS/FAIL |
| 4 | **Horizons** | __/3-4 (1-2Q each); total__ | 3-4/3-4;4-6 | | PASS/FAIL |
| 5 | **Categories** | Res__% Pol__% Mkt__% Ind__% | ≥40,30,30,25% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥4 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2h+≥2r+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 3 samples: __%150-250w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥1;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+4wk] | | INFO |
| | **Age Dist** | <1mo__% 1-3mo__% 3-6mo__% 6-9mo__% 9-18mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven | Decision-critical | Lifecycle-specific | Multi-stakeholder | Quantified impact | Timely | Actionable

**✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?" | "Gartner AI $900B 35% CAGR: competitive positioning?"

**✗ Bad**: "How does ESG work?" (no news) | "Invest in AI?" (no trigger) | "Competitor launched feature" (tactical)

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
