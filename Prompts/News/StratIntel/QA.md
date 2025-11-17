# Strategic Intelligence & Market Research News Q&A Generator (Minimal Viable)

Generate 6–8 decision-critical Q&As from recent industry news—minimal viable tracking for strategic decisions with limited time.

**Cadence**: Monthly | 4-6h effort | **Expires**: 4 weeks from generation

**Scope**: Decision-critical strategic news only—research breakthroughs, policy/regulatory shifts, market trends, ESG mandates affecting strategy. Excludes tactical features, daily operations, sales execution, routine finance, speculation.

**Freshness** (category-adaptive):
- **HV** (Research/Innovation/Consumer/Analysis): ≥80% <2mo (≥25% 1-7d), ≥95% <3mo, 100% ≤6mo
- **MV** (Policy/Cross-Industry): ≥65% <3mo (≥15% 1-14d), ≥85% <6mo, 100% ≤9mo
- **LT** (ESG/Cultural): ≥50% <6mo, ≥75% <12mo, 100% ≤18mo
- **Overall**: ≥65% <3mo, ≥80% <6mo, ≥90% <9mo, 100% ≤18mo
- **Validity**: 4 weeks; re-validate if used beyond 4 weeks

## How the LLM should use this file

- **Role**: Act as a strategic intelligence and market research analyst for a post-PMF organization.
- **Inputs (fill before running)**:
  - Domain and segment (e.g., EV batteries in NA/EU, global AI infra, consumer fintech in APAC).
  - Period under review (e.g., last 4 weeks, Q4 2025).
  - Organization profile: size, stage, regions, main products, current strategic bets.
  - Baseline strategic metrics: R&D spend %, core TAM and current share, growth rates, ESG ratings/targets, key regulatory exposures.
  - Existing strategy hypotheses or theses to test (e.g., "solid-state by 2030", "carbon price stays < $X").
  - Stakeholders and their goals (11 core roles; add others as relevant): CEO, CSO, CRO, CIO, CFO, VP Corp Dev, Chief Sustainability Officer, Head of Strategy, Head of Market Research, Head of ESG, Board.
  - Constraints: capital envelope, risk appetite, regulatory boundaries, execution capacity.
- **Objective**: Using only the instructions in this file (no other prompt files), produce:
  - An executive summary and horizon coverage overview.
  - 6–8 Q&As that satisfy all requirements below.
  - Glossary and reference sections (G, N, A, P, I, R) with citations.
  - At least 2 diagram descriptions and 1 table in Markdown.
  - A completed validation report with quantitative and qualitative checks.
- **Output expectations**:
  - Respect the word counts, horizons, category floors, and freshness thresholds.
  - Focus only on strategically meaningful news that meets the decision criticality framework.
  - Prefer concrete numbers, formulas, and thresholds over vague language.
  - Cover multiple stakeholder viewpoints and explicitly describe trade-offs, risks, and limitations.
  - Provide clear recommendations, action paths, and success metrics that can be monitored.
  - Use structured Markdown (headings, bullets, tables, diagrams, reference links) for high scanability.

## II. Requirements

**Q&A**: 6-8 total | 1-2/horizon | 200-300w | 100% news-driven | 100% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Horizons** (3-4, 1-2 Q each): Short (6-18mo), Medium (18-36mo), Long (3-5yr), (Optional: Transformational 5-10yr if decision-critical)

**Category Coverage** (min): Research ≥40%, Policy ≥30%, Market ≥30%, Industry ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/11): CEO, CSO, CRO, CIO, CFO, VP Corp Dev (core roles only)

**References** (build before Q&A): G≥10 (100% terms used), N≥5-6 (per freshness), A≥3 (academic), P≥2 (policy), I≥3 (industry), R≥10 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% hype/speculation
3. **Impact**: 100% ≥2 horizons + ≥2 roles + quantified (TAM/CAGR/$, policy $, market share)
4. **Decision**: 100% decision + rationale + criteria + timeline
5. **Sources**: ≥3 types, max 50%/type; 100% URLs valid
6. **Actionable**: 100% concrete; 0% abstract

## III. Execution

### Step 1: News Discovery & Curation (Minimal)

**Record generation date (YYYY-MM-DD)—calculate all news ages from this.**

1. **Domain**: Industry/market/sector + period

2. **Search** (≥12-15 candidates, tiered):

   **Tier 1** (1-7d, search first): `"[Domain] breakthrough|research|policy|M&A|market"` + 1-7d

   **Tier 2** (7-30d if insufficient): Same + 7-30d

   **Tier 3** (1-3mo if still insufficient): Same + 1-3mo

   **Sources** (whitelist, prioritize):
   - **Research**: arXiv, Nature, Science, IEEE, universities, NSF
   - **Policy**: Congress.gov, Federal Register, OECD, WTO, think tanks (Brookings, CSIS)
   - **Market**: Pew, McKinsey, Gartner, Forrester, IDC, analyst reports
   - **Industry**: CB Insights, HBR, Bloomberg, FT, Economist
   - **Avoid**: Marketing, PR fluff, rumors, speculation, clickbait

   **Tools**: Perplexity ("past week"), ChatGPT ("latest"), Google (`after:DATE`), Scholar

3. **Curate** (≥12-15 candidates: Research ≥4, Policy ≥3, Market ≥3, Industry ≥2):
   - Age per freshness
   - Whitelist OR primary source
   - Satisfies ≥1 Decision Criticality criterion
   - Specific details (dates, names, numbers, metrics)
   - Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 6-8 Q × 3-4 horizons (1-2 each) × 4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | A# (academic) | P# (policy) | I# (industry) | R# (APA 7th+tag)

**Citation**: Use Markdown reference links such as `[Ref: N1 – Source, 2025][n1]` in the answer body and `[n1]: URL` at the end. Prefer authoritative and recent sources (official policy portals, leading journals, central banks, major analyst firms). When older or secondary material is used, label it explicitly and avoid treating it as decisive. For every important numeric claim (for example CAGR, TAM, policy budgets, ESG scores, market share), attach at least one supporting reference where feasible and flag approximations or back-of-envelope estimates.

**Floors**: G≥10 (100% terms used), N≥5-6, A≥3, P≥2, I≥3, R≥10

**Glossary** (only terms used in Q&As):
- **Coverage**: Only terms/acronyms used (TAM, CAGR, TRL, IRR, NPV, etc.)
- **Clarity**: Plain language, avoid jargon
- **Analogies**: 1-2 real-world comparisons per term
- **Context**: Why it matters for decisions
- **Examples**: Real numbers

**News Entry**: **Title** (Source, MM/DD): Summary | Cat | URL | Decision Criticality criterion

### Step 2.5: Refresh (optional)

**Trigger**: Nobel/Nature/$100M+ research OR major legislation/$1B+ policy OR ESG regulation affecting ≥3 Qs
**Action**: Quick search → 1-3 items ("BREAKING") → Adjust 1-2 Qs
**Default**: Skip (monthly sufficient)

### Step 3: Generate Q&A (batch 2-3, self-check each)

**Before**: Review glossary. Track ALL terms used.

**Patterns**: "[Research] → [R&D] investment?" | "[Policy] → [Compliance] timeline?" | "[Market] shift → [Positioning]?" | "[M&A] → [Competitive] strategy?"

**Avoid**: Tactical, daily ops, speculation, hype, unattributed claims, stale news

**Structure** (200-300w):
1. **News** (~40w): What, when, why, category, and at least one reference tag (for example `[Ref: N1][n1]`).
2. **Impact** (~80w): At least two horizons plus quantified effects (CAGR/TAM/$, policy $, market share, funding, ESG scores, NPV/IRR where relevant) with units and baselines.
3. **Stakeholders** (~50w): At least two roles (for example CEO, CSO, CRO, CIO, VP Corp Dev, CSO/ESG) with specific concerns, trade-offs, and candidate actions.
4. **Decision** (~70w): Compare at least two options (Invest/Monitor/Pivot/Prepare/Delay/Ignore) and make the reasoning explicit: benefits, costs, risks, and conditions where each option is appropriate, noting key uncertainties and limitations.
5. **Action** (~30w): S/M/L (6–18mo/18–36mo/3–5yr) next steps, owners, and 2–3 success metrics with target values and measurement approach.
6. **Links**: Define all reference links at the end of the answer, for example `[n1]: URL`.

**Self-Check**: Age OK | Decision criticality satisfied | ≥2 horizons | ≥2 roles | ≥2 options compared | Risks, trade-offs, and limitations stated | Reasoning coherent and non-contradictory | 200–300w | Metrics quantified with units and baselines | ≥1 citation (prefer recent) | Reference links present and valid | 0% hype | 100% actionable | All terms covered in glossary | Calculations and percentages cross-checked | Uncertainties and assumptions explicitly flagged

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Horizon timelines, TAM/CAGR curves, 2×2 matrices, decision trees, policy roadmaps

**Format**: Mermaid, Markdown tables

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥10 (100% terms used) | N≥5-6 | A≥3 | P≥2 | I≥3 | R≥10

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary covers 100% of terms | 3–4 horizons represented | Category percentage targets respected | ≥5 roles used across Q&As | Citations present for all news items | Sample of 5 answers within 200–300 words | Visuals count (diagrams and tables) satisfied | Every Q&A includes a decision and timeline | **All items meet freshness rules**

**Qualitative**: News items meet freshness thresholds and avoid hype | Every Q&A meets decision criticality criteria | Impacts cover ≥2 horizons and ≥2 roles and are quantified | Decisions compare alternatives with rationale and criteria | Sources span at least three types | Each horizon has at least one news+analysis pair | Links resolve correctly | Quantification is consistent and plausible | Recommendations are concrete and implementable | Evidence is explicitly cited and uncertainty is labelled | Search process is documented | Final pass checks calculations, terminology consistency, reasoning coherence, and success metrics

### Step 7: Submit

**Checklist** (all YES): Validations PASS | Floors met | Glossary complete (100% terms, ≥50% analogies) | TOC complete | 0 placeholders | Visuals OK | Citations OK | Impact OK | Decision OK | Timeline OK | Categories OK | Roles OK | **Freshness OK** | Evidence 100% | URLs valid | **Dates (gen + expire=gen+4wks)** | Search documented

## IV. Validation Report (Minimal)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | **Freshness** | HV: __%<2mo (1-7d:__%), __%<3mo \| MV: __%<3mo (1-14d:__%) \| Overall: __%<3mo | Per header | | PASS/FAIL |
| 2 | **Floors** | G:__ N:__ A:__ P:__ I:__ R:__ Q:__ | ≥10,≥5-6,≥3,≥2,≥3,≥10,6-8 | | PASS/FAIL |
| 3 | **Glossary** | __%terms; __%analogies | 100%;≥50% | | PASS/FAIL |
| 4 | **Horizons** | __/3-4 (1-2Q each); total__ | 3-4/3-4;6-8 | | PASS/FAIL |
| 5 | **Categories** | Res__% Pol__% Mkt__% Ind__% | ≥40,30,30,25% | | PASS/FAIL |
| 6 | **Roles** | __/11 | ≥5 | | PASS/FAIL |
| 7 | **Decision Criticality** | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 8 | **Impact** | __% ≥2h+≥2r+quantified | 100% | | PASS/FAIL |
| 9 | **Decision** | __% decision+rationale+criteria | 100% | | PASS/FAIL |
| 10 | **Citations** | __%≥1cite | 100% | | PASS/FAIL |
| 11 | **Words** | 5 samples: __%200-300w | 100% | | PASS/FAIL |
| 12 | **Visuals** | diag__; tab__ | ≥2;≥1 | | PASS/FAIL |
| | **Meta** | Start:__ End:__ Expires:[+4wk] | | INFO |
| | **Age Dist** | <1mo__%(1-7d__%) 1-3mo__% 3-6mo__% 6-9mo__% 9-18mo__% | Per header | | INFO |
| | **OVERALL** | All checks | All PASS | | PASS/FAIL |

## V. Question Quality (≥2 fails of 7 = rewrite)

**Criteria**: News-driven (per freshness) | Decision-critical (≥1 criterion) | Lifecycle-specific (1-2 horizons) | Multi-stakeholder (≥2 roles) | Quantified impact | Timely | Actionable

**✓ Good**: "Nature solid-state 3x (Oct '24): R&D investment?" | "CBAM $120B 2026-34: supply chain strategy?" | "Gartner AI $900B 35% CAGR: competitive positioning?" | "M&A consolidation (Nov '24): acquisition target?"

**✗ Bad**: "How does ESG work?" (no news) | "What is CAGR?" (overview) | "Invest in AI?" (no trigger) | "Latest research" (no decision) | "Competitor launched feature" (tactical)

## VI. Output Format (Minimal)

### A. TOC

```markdown
# [Domain] Strategic Intelligence Q&A ([Period])

## Contents
1. Executive Summary (Insights | Dashboard)
2. Horizon Coverage (3-4 horizons)
3. Questions by Horizon: Short (Q1-Q2) | Medium (Q3-Q4) | Long (Q5-Q6) | Transformational (Q7-Q8)
4. References: G (G1-G10) | N (N1-N6) | A (A1-A3) | P (P1-P2) | I (I1-I3) | R (R1-R10)
5. Validation (12 checks)
```

### B. Executive Summary

```markdown
**Domain**: [Industry] | **Period**: [Q3-Q4'24] | **Coverage**: [# items, 4 cats]

**Insights**: 1. [News] ([Date]): [Impact] → [Decision] → [Timeline] (2 high-impact)

**Dashboard**: [Table: Horizon | News | Decision | Timeline]

**Roles**: [5+ roles] | **Refs**: G=[#] N=[#] A=[#] P=[#] I=[#] R=[#]
```

### C. Horizon Overview

| # | Horizon | Count | Categories | News | Roles |
|---|---------|-------|------------|------|-------|
| 1 | Short | 1-2 | Research, Policy | [Top] | CEO, CSO |
| 2 | Medium | 1-2 | Market, Industry | [Top] | CSO, CRO, CIO |
| 3 | Long | 1-2 | Research, Industry | [Top] | CEO, CRO, Board |
| 4 | Transformational | 1-2 | Policy, Market | [Top] | CEO, Board |
| | **Total** | **6-8** | **4** | **6+** | **≥5** |

### D. Q&A Template

```markdown
### Q#: [News Question + Horizon + Roles]

**Horizon**: [H] | **Roles**: [Primary, Secondary] | **Cats**: [✓] | **Decision Criticality**: [Criterion]

**News** (~40w): What, when, why, cat [Ref: N#][n#]

**Impact** (~80w): **Horizons** (≥2) | **Quantified**: CAGR/TAM/$, policy $, market share, funding

**Stakeholders** (~50w): **[Role 1]**: Concerns, actions | **[Role 2]**: Same

**Decision** (~70w): **Rec**: Invest/Monitor/Pivot/Prepare/Delay/Ignore | **Rationale**: Why | **Success**: Targets

**Action** (~30w): **S (6-18mo)**: Actions+owner | **M (18-36mo)**: Same | **L (3-5yr)**: Same

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

## VII. Example (format demo—use actual recent news)

### Q1: Nature solid-state 3x (Oct '24): R&D investment?

**Horizon**: Long, Medium | **Roles**: [CRO, CSO, CEO] | **Cats**: [Research] | **Decision Criticality**: [Blocks R&D investment]

**News**: *Nature* 10/15/24: 450 Wh/kg (3x current), sulfide, 1K cycles, TRL 4-5. MIT/Toyota partnership, $50M DOE + $1B private. 600mi range → trucking/aviation TAM.

**Impact**: **M (18-36mo)**: R&D pivot + IP. Patents +45% (Toyota 1.2K, Samsung 900). $200M pilot → $2B NPV by '29. **L (3-5yr)**: Market transformation. 600mi TAM: 15M→60M units (40% CAGR). Carbon -30%. Market share +5-10% ($15B), ESG rating B→A.

**Stakeholders**: **CRO**: R&D pivot decision, $200M/3yr, partnerships. **CSO**: M&A evaluation (QS $1-2B), JV strategy. **CEO**: $500M investment decision, pivot timeline '28-30.

**Decision**: **Invest** R&D + commercialization; **Monitor** Toyota '27, Samsung '29. | **Rationale**: Nature TRL 4-5 → 5-7yr timeline = '29-31. 3x improvement = transformational. +5-10% share ($15B NPV). ESG leadership. Risk: scaling, competition. | **Success Criteria**: Pilot TRL 7 by '27, 200+ patents by '26, 600mi production by '30, ESG A rating by '29.

**Action**: **S (6-18mo)**: CRO: $50M MIT/Stanford R&D (20 PhDs) → TRL 5 Q4'25 | CSO: M&A analysis → target list Q2'25. **M (18-36mo)**: CRO: $150M pilot (10 MWh) → Q2'27 | CSO: M&A/JV ($500M-1B) → Q4'26. **L (3-5yr)**: CEO: $500M CapEx (10 GWh mfg) → 200K units/yr.

[n1]: https://nature.com/s41586-024-x | [a1]: https://techcrunch.com/mit-toyota | [i1]: https://gartner.com/solid-state-2030

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

**Use for**: R&D roadmaps | Market sizing | Policy foresight | ESG strategy | Cross-industry adjacency | Competitive positioning

## IX. Quick Prompt Checklist (before running)

Use this as a final 30–60 second sanity check before asking an LLM to generate Q&As with this file:

- **Self-contained**: All necessary instructions, definitions, and expectations are present in this single prompt; no reliance on other files or prior answers.
- **Context filled**: Domain, period, organization profile, baseline metrics, existing theses, stakeholders, and constraints are specified.
- **Precise & relevant**: The focus is on a small set of strategically important news items, each with clear metrics (TAM/CAGR/$, policy $, ESG scores, market share) and a 3–24 month+ decision window.
- **Complete but MECE**: Horizons (3–4), categories (Research/Policy/Market/Industry), and core roles are all covered with minimal overlap.
- **Multi-perspective & deep**: Each question touches at least two horizons and two roles, with enough detail for implementation (owners, timing, resources).
- **High-signal & concise**: Answers are constrained to 200–300 words, focus on the highest-impact points, and avoid background history unless directly decision-relevant.
- **Evidence-driven**: Sources are authoritative and recent; numeric claims are backed by citations or clearly marked as estimates; uncertainties and limitations are surfaced.
- **Balanced decisions**: At least two options are compared per question with benefits, costs, and risks; counterpoints and downside scenarios are acknowledged.
- **Structured output**: Executive summary, horizon overview, Q&As, references, visuals, and validation report are all requested in clear Markdown structure.
- **Actionable & testable**: For each decision, there are concrete S/M/L actions, owners, and measurable success criteria with baselines and targets.
