# Operations & Supply Chain News Intelligence Q&A

## TOC
[Framework](#framework) | [Requirements](#requirements) | [Execution](#execution) | [Validation](#validation) | [Quick Check](#quick-check-30s)

---

## Purpose
Generate 4–6 decision-critical Q&As from recent industry news for operations leaders. Use web search; self-contained.

**Context**: Operations leaders need timely, actionable intelligence on supply chain events that require decisions within 6mo. Problem: fragmented news sources, unclear impact. Constraint: limit to decision-critical topics (blocks decisions, creates risk >5%, affects ≥2 stakeholders). Resources: 4–6h/mo effort. Scale: typically 1M+ users or $500K+ annual operations budget. Target: reduce decision time 30-40%, improve risk detection 40-50%.

**Cadence**: Monthly

**Key Terms**:
- **Decision-critical**: News requiring action within 6mo or creating risk/disruption >5% impact
- **Supply chain cycles**: Source (procurement) → Make (production) → Deliver (logistics) → Enable (safety/compliance)
- **MECE**: Mutually Exclusive, Collectively Exhaustive coverage

**Scope**: Supply disruptions, supplier risk, cost shocks, regulatory/safety changes, capacity constraints.

**Exclusions**: R&D, marketing, incremental improvements, rumors.

**Freshness**: Majority <2mo; disruptions <1mo; regulatory <6mo.

**Decision Criticality** (≥1 required, priority labeled):
1. **Critical**: Blocks decisions (sourcing, capacity, suppliers)
2. **Critical**: Creates risk (disruptions, incidents, cost shocks >5%)
3. **Important**: Affects multiple stakeholders
4. **Important**: Requires action within 6mo
5. **Important**: Quantified impact

---

## Framework

**Stakeholders**: COO, VP Supply Chain, Plant Manager, Procurement Head, Quality Lead.

**Cycles**: Source → Make → Deliver → Enable (safety, compliance).

**Categories**: Logistics Disruptions | Supplier Risk | Manufacturing & Capacity | Safety & Compliance

---

## Requirements

**Output**: 4–6 Q&As, 200–300 words each, news-driven, cited.

**Coverage**: Address all 4 cycles; emphasize Logistics and Supplier Risk; engage multiple stakeholders.

**References**: Glossary, News sources (diverse, ≥3 types), valid URLs.

**Visuals**: ≥2 diagrams + ≥1 table.

---

## Execution

### 1. Discovery & Curation
**Search**: Find candidates from authoritative sources (verify current year):
- Trade media: Supply Chain Dive (2024+), Logistics Management (2024+), IndustryWeek (2024+)
- Consulting: McKinsey Supply Chain Insights (2024+), Gartner Supply Chain Top 25 (2024+)
- Regulatory: OSHA.gov (official announcements), FDA.gov (compliance updates)
- Industry: CSCMP's Supply Chain Quarterly (2024+), ASCM publications (2024+)

**Curate**: 
- Prefer primary sources (company announcements, regulatory bodies, official reports) over secondary reporting
- Cover ≥3 source types, multiple categories
- Each Q&A must meet ≥1 criticality criterion
- Verify freshness: majority <2mo, disruptions <1mo, regulatory <6mo
- Include specific, quantified details from sources

**Record**: Date (YYYY-MM-DD), domain, news title/source/date, summary, category, URL, criticality criterion.

### 2. Build References
**Glossary**: Define terms in plain language with analogies (e.g., "Just-in-time inventory: ordering supplies only when needed, like a restaurant buying fresh ingredients daily"). Include only terms used in Q&As.

**Citations**: Use [Ref: N#][n#] inline. Format: [n#]: Source Title. Publication/Organization (Date: YYYY-MM-DD). URL (Accessed: YYYY-MM-DD). Flag uncertainties (e.g., "impact estimated pending official data").

### 3. Generate Q&A Structure
1. ### Qn: Question
2. #### News: What/when/why; cite source with date [Ref: N#][n#]
3. #### Impact: Consequences across cycles, quantified metrics (cost, time, capacity, risk %)
4. #### Stakeholders: Roles affected, specific concerns and actions required
5. #### Options & Decision: 
   - ≥2 alternatives with costs/benefits/risks
   - Recommendation (Adopt/Investigate/Defer/Avoid) with rationale
   - Trade-offs and limitations/counterarguments
   - Timeline with milestones
6. #### Actions: 
   - Next steps (owners, deadlines: 2wk/2mo/6mo)
   - Success criteria: measurable targets (baseline → target, measurement method)
7. #### References: [n#]: Full citation format per §2

### 4. Visuals
Add ≥2 diagrams (Mermaid: risk heatmap, decision tree, impact matrix) + ≥1 comparison table (alternatives, pros/cons, costs).

### 5. Verification
**Self-review**: Before finalizing, verify each item:
- ☐ **Accuracy**: Facts verified against primary sources; version/date confirmed
- ☐ **Evidence**: URLs valid and accessible (test each link)
- ☐ **Precision**: Calculations/metrics accurate; formulas correct
- ☐ **Logic**: No contradictions between Q&As; reasoning sound
- ☐ **Consistency**: Terminology matches glossary; formatting uniform
- ☐ **Criticality**: Each Q&A meets ≥1 criterion; priority labeled
- ☐ **Uncertainty**: Unknowns/estimates flagged explicitly
- ☐ **Completeness**: All requirements met per Validation checklist

---

## Validation

| Check | Criteria | Status |
|-------|----------|--------|
| Count & Length | 4-6 Q&As, 200-300w each | ☐ |
| Freshness | Majority <2mo; disruptions <1mo; regulatory <6mo | ☐ |
| Coverage | All 4 cycles (Source/Make/Deliver/Enable), ≥2 stakeholders per Q&A | ☐ |
| Criticality | Each Q&A ≥1 criterion; priority labeled (Critical/Important) | ☐ |
| Impact | Multi-cycle/role, quantified metrics (cost, time, capacity, risk %) | ☐ |
| Decision | ≥2 alternatives with costs/benefits/risks, recommendation with rationale, limitations | ☐ |
| Actions | Owners assigned, deadlines specified (2wk/2mo/6mo), success criteria (baseline→target) | ☐ |
| References | Glossary (terms used), diverse sources (≥3 types), valid URLs with dates, uncertainties flagged | ☐ |
| Visuals | ≥2 diagrams, ≥1 comparison table | ☐ |
| Verification | Self-review checklist completed (Execution §5): all items checked | ☐ |

**Meta**: Generated: ___ (YYYY-MM-DD) | Age distribution: <1mo __%  1-2mo __%  2-6mo __%

---

## Quick Check (30s)

**Before finalizing:**

☐ **Self-contained**: Complete context; no missing dependencies  
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance  
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth  
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility  
☐ Logic | ☐ Risk/Value | ☐ Fairness  
☐ Structure | ☐ Consistency | ☐ TOC  
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria