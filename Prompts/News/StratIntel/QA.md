# Strategic Intelligence & Market Research News Q&A Generator (Minimal Viable)

Generate 6–8 decision-critical Q&As from recent industry news—minimal viable tracking for strategic decisions with limited time.

**Cadence**: Monthly | 4-6h effort | **Expires**: 4 weeks from generation

**Scope**: Decision-critical strategic news only—research breakthroughs, policy/regulatory shifts, market trends, ESG mandates affecting strategy. Excludes tactical features, daily operations, sales execution, routine finance, speculation.

**Freshness** (category-adaptive):
- **HV** (Research/Innovation/Consumer/Analysis): ≥80% <2mo (≥25% 1-7d), ≥95% <3mo, 100% ≤6mo
- **MV** (Policy/Cross-Industry): ≥65% <3mo (≥15% 1-14d), ≥85% <6mo, 100% ≤9mo
- **LT** (ESG/Cultural): ≥50% <6mo, ≥75% <12mo, 100% ≤18mo
- **Overall**: ≥65% <3mo, ≥80% <6mo, ≥90% <9mo, 100% ≤18mo
- **Validity**: 4 weeks; re-validate if >2mo

## I. Context & Scope

**Audience**: C-suite, strategy teams, corporate dev, research leaders (core roles only).

**Decision Criticality Framework** (include if ≥1 criterion met):
1. **Blocks Decision**: Directly impacts R&D investment, M&A, strategic pivot, or market entry
2. **Creates Risk**: Material threat to competitive position, regulatory compliance, or ESG standing
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (CEO + CSO, CRO + CIO, etc.)
4. **Requires Action**: 3-24mo action window (not speculative)
5. **Quantified Impact**: TAM/CAGR, funding $, policy $, ESG targets, market share

**Categories** (4, each Q covers ≥1):
1. **Research & Innovation**: Breakthroughs, patents, funding, TRL progression affecting R&D roadmap
2. **Policy & Regulatory**: Legislation, trade, tax, compliance affecting operations/strategy
3. **Market & Consumer**: Adoption trends, TAM shifts, generational changes affecting positioning
4. **Industry Analysis**: M&A, consolidation, benchmarks, analyst reports affecting competitive strategy

**Relevance** (≥2 required, Recency mandatory):
1. **Recency** (mandatory per freshness)
2. **Strategic Impact**: Long-term positioning, R&D, market strategy
3. **Horizon Breadth**: ≥2 horizons OR cross-horizon
4. **Stakeholder Breadth**: ≥3 roles OR multi-role
5. **Decision Urgency**: 3-24mo OR planning cycles
6. **Quantified**: Market/consumer/policy/ESG/funding metrics
7. **Trend Significance**: Confirms/refutes thesis, shifts trajectory

**Answer Structure** (200-300w): News (what, when, why) + impact (quantified, ≥2 horizons, ≥2 roles) + decision (Invest/Monitor/Pivot/Prepare/Delay/Ignore + rationale) + timeline (S/M/L). Projections only if sourced.

## II. Requirements

**Q&A**: 6-8 total | 1-2/horizon | 200-300w | 100% news-driven | ≥85% ≥1 cite, ≥30% ≥2 cites | ≥1 category + impact + decision

**Horizons** (3-4, 1-2 Q each): Short (6-18mo), Medium (18-36mo), Long (3-5yr), (Optional: Transformational 5-10yr if decision-critical)

**Category Coverage** (min): Research ≥40%, Policy ≥30%, Market ≥30%, Industry ≥25% (optional)

**Decision Criticality** (100%): Each Q must satisfy ≥1 of 5 criteria (Blocks/Risk/Roles/Action/Quantified)

**Stakeholders** (≥5/11): CEO, CSO, CRO, CIO, VP Corp Dev (core roles only)

**References** (build before Q&A): G≥10 (100% terms used), N≥5-6 (per freshness), A≥3 (academic), P≥2 (policy), I≥3 (industry), R≥10 (APA 7th+tag)

**Visuals**: ≥2 diagrams + ≥1 table

**Quality Gates** (fail ANY = stop):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified)
2. **News**: 100% cite ≥1 per freshness; 0% hype/speculation
3. **Impact**: 100% ≥2 horizons + ≥2 roles + quantified (TAM/CAGR/$, policy $, market share)
4. **Decision**: 100% decision + rationale + timeline
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
   - ✅ Age per freshness
   - ✅ Whitelist OR primary source
   - ✅ Satisfies ≥1 Decision Criticality criterion
   - ✅ Specific details (dates, names, numbers, metrics)
   - ✅ Not marketing/rumors

4. **Verify**: Check decision criticality; if fail, retry earlier tiers

5. **Allocate**: 6-8 Q × 3-4 horizons (1-2 each) × 4 categories (≥1/Q) × ≥5 roles

### Step 2: Build References (Minimal)

**Format**: G# (term, def+analogy, context) | N# (news, source, date, cat, URL) | A# (academic) | P# (policy) | I# (industry) | R# (APA 7th+tag)

**Citation**: Markdown reference links: `[Ref: N1][n1]` in text, `[n1]: URL` at answer end

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
1. **News** (~40w): What, when, why, cat `[Ref: N#][n#]`
2. **Impact** (~80w): ≥2 horizons + quantified (CAGR/TAM/$, policy $, market share, funding)
3. **Stakeholders** (~50w): ≥2 roles + concerns + actions
4. **Decision** (~70w): Invest/Monitor/Pivot/Prepare/Delay/Ignore + rationale + criteria
5. **Action** (~30w): S/M/L (6-18mo/18-36mo/3-5yr) + owner
6. **Links**: Define at end: `[n1]: URL`

**Self-Check**: Age OK | Decision Criticality ✓ | ≥2 horizons | ≥2 roles | Decision clear | 200-300w | Quantified | ≥1 cite | 0% hype | 100% actionable | All terms in glossary

### Step 4: Visuals (≥2 diagrams + ≥1 table)

**Types**: Horizon timelines, TAM/CAGR curves, 2×2 matrices, decision trees, policy roadmaps

**Format**: Mermaid, Markdown tables

### Step 5: Final Checks

**Refs**: 100% resolve | Age OK | Complete | G≥10 (100% terms used) | N≥5-6 | A≥3 | P≥2 | I≥3 | R≥10

**Decision**: 100% decision + rationale + criteria + timeline

**Stakeholders**: ≥5 roles | Actions + authority

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Quantitative**: Floors met | Glossary 100% | 3-4 horizons | Categories per % | ≥5 roles | Citations OK | 5 word samples 200-300w | Visuals OK | Decision 100% | Timeline 100% | **Age per freshness**

**Qualitative**: News per freshness, 0% hype | Decision Criticality 100% | Impact 100% ≥2 horizons+roles+quantified | Decision 100% | Source diversity ≥3 types | Per-horizon ≥1 news+analysis | Links valid | Quantified 100% | Actionable 100% | Evidence 100% | Search documented

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
| | **Age Dist** | <1mo__%(1-7d__%) 1-3mo__% 3-6mo__% | Per header | | INFO |
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
| 4 | Transform | 1-2 | Policy, Market | [Top] | CEO, Board |
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
