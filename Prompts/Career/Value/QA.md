# Value Assessment Q&A Generator (Minimal Viable)

Generate **4–8 decision-critical Q&As** for informed value decisions with limited time. Minimal viable: blocks decisions or creates material risk.

## Context

**Problem**: Poor value assessments lead to bad decisions (e.g., over-investing in low-ROI projects, underestimating technical debt). Need structured Q&A to evaluate value across 6 dimensions: business, user, technical, organizational, strategic, risk.

**Scope**: Decision-critical scenarios only (e.g., ≥$100K impact or ≥20% velocity change; adjustable). Focus: software engineering lifecycle (design, development, deployment, operations).

**Constraints**: ~10–15min per Q&A; self-contained.

**Assumptions**: Stakeholders have conflicting priorities; measurements context-dependent.

**Scale**: Individual to 50+ team decisions; 4-8 Q&A sets.

**Timeline**: On-demand; 4-6h effort; refresh annually.

**Stakeholders**: PM, Architect, Developer, SRE/DevOps, CFO.

**Resources**: Capable LLM; optional online access.

**Terms**:
- **Floor**: Min threshold (≥).
- **Gate**: Fail-stop checkpoint (100% compliance).
- **Difficulty**: F=execution, I=strategy, A=portfolio.
- **Value Types** (MECE): Business, User, Technical, Organizational, Strategic, Risk.
- **Decision Criticality**: Meets ≥1 criterion (below).

**Limitations**: Balances conflicts; context-dependent; excludes speculation; customize domains.

## Requirements

### Decision Criticality Framework (MANDATORY)

**Include if ≥1 criterion is satisfied**:
- **Blocks Decision**: Directly impacts investment go/no-go, resource allocation, or strategic/roadmap pivot.
- **Creates Risk**: Material threat (e.g., financial loss >10%, major opportunity cost, strategic misalignment, or velocity impact >20%).
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (CFO + Architect, PM + DevOps, etc.).
- **Requires Action**: 1–6mo action window (not speculative).
- **Quantified Impact**: Clear metrics (NPV $, ROI %, velocity %, cost/benefit ratio, adoption %).

**Exclude if**: Niche/legacy (<5% adoption), orthogonal/nice-to-have, already covered, speculative.

### Floors (Minimum Thresholds)

| Category | Requirement |
|----------|-------------|
| **Q&A** | **4–8** \| Balanced difficulty \| Each: ≥2 value types+stakeholders \| ~150 words/answer |
| **Lifecycle Phases** | 3–4 decision-critical only (Design, Development, Deployment, Operations) |
| **Citations** | ≥50% have ≥1; ≥20% have ≥2 \| Diverse sources (EN majority, some ZH/other) |
| **Value Types** | Each Q&A: ≥2 of 6 |
| **Stakeholders** | ≥4 core roles (PM, Architect, Developer, SRE); each Q&A ≥2 |
| **References** | Glossary ≥4 \| Tools ≥2 \| Literature ≥3 (≥1 ZH) \| Citations ≥4 APA 7th |
| **Visuals** | ≥1 diagram+table per Q&A (compressed) |
| **Decision Criticality** | 100% of Q&As satisfy ≥1 criterion |

### Gates (Fail-Stop)

**Any failure**: stop, fix, re-validate ALL

| # | Gate | Criteria | Mitigation |
|---|------|----------|------------|
| 1 | **Decision Criticality** | 100% of Q&As satisfy ≥1 criterion | Rewrite/replace non-critical |
| 2 | **Recency** | ≥50% of references from last 3yrs | Flag outdated with caveats |
| 3 | **Source Diversity** | ≥3 types; no type >40% | Expand research |
| 4 | **Link Validation** | 100% URLs accessible/archived | Archive/replace |
| 5 | **Cross-Reference** | 100% [Ref: ID] resolve; no orphans | Fix broken |
| 6 | **Quantified Impact** | 100% Q&As have quantified metrics | Add metrics |

## Execution

### Step 1: Plan Allocation

Distribute **4–8 Q&As** across 3–4 phases (balanced difficulty). ≥4 stakeholders; each Q&A ≥2 value types + ≥1 criticality criterion.

**Example** (6): Design (2) + Development (2) + Deployment (1) + Operations (1) = balanced F/I/A

### Step 2: Build References (BEFORE Q&A, then run Gates 1–6)

| Type | Count | Required | ID |
|------|-------|----------|-----|
| **Glossary** | ≥4 | Term, definition, measurement, stakeholder, lifecycle | G1... |
| **Tools** | ≥2 | Category, pricing, users, update (≤18mo), metrics, stakeholders, URL | T1... |
| **Literature** | ≥3 (≥1 ZH) | Author, title, year, summary, frameworks, lifecycle | L1... |
| **Citations** | ≥4 | APA 7th+[EN]/[ZH]/[Other]; ≥50% from last 3yrs | A1... |

**Examples**:
- **Glossary**: NPV (Net Present Value: future cash flows discounted to present), ROI (Return on Investment: (gain-cost)/cost × 100%), TCO (Total Cost of Ownership: acquisition + operation + maintenance), WSJF (Weighted Shortest Job First: cost of delay / job duration).
- **Tools**: Pendo (product analytics, $50K/yr, 10K users, Q2 2024), SonarQube (code quality, free/open-source, 1M users, Q3 2024).
- **Literature**: Reinertsen, D. (2009). The Principles of Product Development Flow. Celeritas Publishing. [EN, value flow]; Kim, M. (2018). The Phoenix Project. IT Revolution Press. [EN, DevOps value]; 俞军. (2018). 俞军产品方法论. 中信出版社. [ZH, product strategy].
- **Citations**: Cite recent primary sources, e.g., AWS Well-Architected Framework (https://aws.amazon.com/architecture/well-architected/), OWASP Top 10 (https://owasp.org/www-project-top-ten/).

### Step 3: Generate Q&A (2–3 at a time, self-check)

**Question**: Decision-critical scenario with tensions. Test quantification, trade-offs, alignment. Avoid recall. Difficulty: F/I/A. Justify criticality.

**Answer** (~150 words):
1. **Key Insight**: Value tension + criticality (1 sentence)
2. **Framework** [Ref: G#/A#]
3. **Multi-Value** (≥2 types + quantification)
4. **Multi-Stakeholder** (≥2 roles)
5. **Lifecycle** (brief)
6. **Quantification** (metrics/methods/sources)
7. **Trade-offs** (≥2 alternatives)
8. **Decision Criteria** (thresholds/targets)
9. **Citations** ≥1 [Ref: ID]
10. **Artifact** (optional)

**Batch Check**: Criticality | ≥2 signals | Word count | ≥2 types/stakeholders | Quantified | ≥1 cite

### Step 4: Create Visuals (≥1 diagram+table per Q&A)

By phase: Design (value/cost), Development (quality/velocity), Deployment (frequency/risk), Operations (SLO/efficiency). Use tables/diagrams with units, confidence, citations.

### Step 5: Populate References

| Type | Format |
|------|--------|
| **Glossary** | G#. Term | Definition | Measurement | Stakeholder | Lifecycle |
| **Tools** | T#. Tool | Description | Pricing | Users | Update | Metrics | URL |
| **Literature** | L#. Author, Title, Year | Summary | Lifecycle |
| **Citations** | A#. [APA 7th] [Lang] |

Validate: 100% [Ref: ID] resolve; no orphans; complete fields; G≥4, T≥2, L≥3, A≥4

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

See checklist below. Key:
- **Floors**: G≥4, T≥2, L≥3, A≥4, Q=4–8, balanced
- **Decision Criticality**: 100% satisfy ≥1 criterion [Blocks/Risk/Roles/Action/Quantified]
- **Citations**: ≥50% have ≥1; ≥20% have ≥2 | Diverse
- **Quality**: ~150 words | 100% value-concrete + quantified | ≥90% scenario-based
- **Coverage**: ≥4 core stakeholders, each Q&A ≥2 | ≥2 value types per Q&A | 3–4 phases covered
- **Integrity**: 100% links accessible | 100% [Ref: ID] resolve, no orphans

### Step 7: Final Review

**Questions**: Clarity (single ask) | Value focus | Depth (trade-offs) | Realism (stakeholder tension) | Decision-critical (blocks decision or creates risk) | Discriminative (judgment>recall) | Aligned difficulty

**Answers** (sample ≥3): ≥2 value types | ≥2 stakeholders | Quantification | Frameworks+cites | Trade-offs/alternatives | Positive+negative | Decision criteria | Limitations/assumptions

**Submit**: All validations PASS | All gates PASS | TOC with links | No placeholders | Decision Criticality justified for each Q&A

## Validation Report (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥4, T≥2, L≥3, A≥4, Q:4-8, balanced | | PASS/FAIL |
| 2 | Decision Criticality| __/__ satisfy ≥1 criterion            | 100% [Blocks/Risk/Roles/Action/Quantified] | | PASS/FAIL |
| 3 | Citations          | __%≥1, __%≥2                          | ≥50%≥1, ≥20%≥2                      | | PASS/FAIL |
| 4 | Diversity          | Types:__, Recency:__%                 | ≥3 types, ≥50% last 3yrs            | | PASS/FAIL |
| 5 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 6 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 7 | Word Count         | __ sampled: __ compliant              | ~150 words                          | | PASS/FAIL |
| 8 | Key Insights       | __/__ value-concrete + quantified     | 100% (specific value tension)       | | PASS/FAIL |
| 9 | Frameworks         | __/__ value+cited                     | ≥80% value-focused                  | | PASS/FAIL |
| 10| Value Judgment     | __% scenario+value                    | ≥90% value scenario-based           | | PASS/FAIL |
| 11| Stakeholder Cov    | __/4 core roles; Q&A: __/__ ≥2        | ≥4 total; each Q&A ≥2               | | PASS/FAIL |
| 12| Quantified Impact  | __/__ have metrics                    | 100%                                | | PASS/FAIL |

## Question Quality (≥2 failures = rewrite/replace)

| # | Criterion | ✓ Pass | ✗ Fail |
|---|-----------|--------|--------|
| 1 | **Clarity**: Single value ask | "Microservices ($500K, 6mo)—assess business/tech/org value?" | "Explain value types" |
| 2 | **Decision Criticality**: Blocks/Risk | "$2M investment blocks roadmap. Allocate: product/debt/platform?" | "Should we invest in platform?" |
| 3 | **Quantification**: Metrics | "Feature: +$2M revenue, -40% velocity. NPV? Payback? Risk?" | "Calculate ROI" |
| 4 | **Realism**: Stakeholder tension | "Sales: $5M customization. Arch: 30% debt. PM: Q4 launch. Assess?" | "What's the value?" |
| 5 | **Trade-offs**: ≥2 alternatives | "Migrate now (upfront cost, long-term gain) vs. delay (compound debt) vs. hybrid?" | "List pros/cons" |
| 6 | **Lifecycle**: Phase/cross-phase | "Design creates value → realized in ops (year 2+). Timeline? Risks?" | "What happens in design?" |
| 7 | **Multi-Stakeholder**: ≥2 views | "CFO: NPV negative. Arch: debt reduction. PM: delay. DevOps: +2 FTE. Decision?" | "How do PMs measure value?" |
| 8 | **Aligned Difficulty**: Match | F=measurement \| I=trade-offs \| A=portfolio/P&L | Mismatch |

## Output Structure

### A. Table of Contents
1. Lifecycle Phases Overview | 2. Q&A by Phase (3–4 phases) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Lifecycle Phases Overview

**Summary**: [4–8] total | Balanced difficulty | 3–4 decision-critical phases | ≥2 value types per Q&A | ≥4 core stakeholders

| # | Phase | Range | Count | Mix | Value Types | Stakeholders | Artifacts |
|---|-------|-------|-------|-----|-------------|--------------|-----------|
| 1 | Design | Q1–Q3 | 1–2 | Balanced | Tech/Org/Str/Risk | Arch/Dev/SRE | 1 diagram+table |
| 2 | Development | Q4–Q6 | 1–2 | Balanced | Tech/Org/Risk | Dev/Arch/PM | 1 diagram+table |
| 3 | Deployment | Q7–Q9 | 1–2 | Balanced | Org/Risk/Bus | DevOps/SRE/Arch | 1 diagram+table |
| 4 | Operations | Q10–Q12 | 1–2 | Balanced | User/Bus/Risk | SRE/DevOps/PM | 1 diagram+table |
| | **Total** | | **4–8** | **Balanced** | **≥2 per Q&A** | **≥4 core** | **≥1 per Q&A** |

**Legend**: F=execution | I=strategy/trade-offs | A=portfolio/P&L | Bus=Business | User=User | Tech=Technical | Org=Organizational | Str=Strategic | Risk=Risk

### C. Q&A Template

**Phase X: [Phase Name]**

**QX: [Value Scenario Question]**

**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Value Types**: [≥2] | **Stakeholders**: [≥2] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

**Key Insight**: [1 sentence value tension + decision criticality]

**Answer** (~150 words): Framework [Ref: G#/A#] | Multi-value (≥2 types+quantification) | Multi-stakeholder (≥2 roles) | Lifecycle (brief) | Quantification (metrics, methods, sources) | Trade-offs (≥2 alternatives) | Decision criteria (go/no-go) | ≥1 [Ref: ID]

**Artifact** *(optional)*: Value matrix/calculation/table

### D. References Template

See **Step 5** for formats. Summary:
- **Glossary**: **G#. Term** | Definition | Measurement | Stakeholder | Lifecycle (alphabetize)
- **Tools**: **T#. Tool** | Description | Pricing | Users | Update | Metrics | URL (group by category)
- **Literature**: **L#. Author, Title, Year** | Summary | Lifecycle (group: EN, ZH)
- **Citations**: **A#. [APA 7th] [Lang]** (sort by ID)

## Example

**Q1: Architect proposes microservices migration ($800K, 9mo, 5 engineers). PM: roadmap delayed. CFO: ROI justification. DevOps: operational complexity +40%. Assess total value across lifecycle?**

**Difficulty**: A | **Phase**: Design → Development → Operations → Evolution (cross-lifecycle) | **Value Types**: Business, Technical, Organizational, Risk, Strategic | **Stakeholders**: Architect, PM, CFO, DevOps/SRE, Developers

**Key Insight**: Comprehensive value assessment across lifecycle/stakeholders, balancing investment cost (negative) against distributed benefits (positive: technical/organizational/strategic) while navigating conflicting priorities.

**Answer** (~150 words):
Apply **Value Stream Mapping** [Ref: G7] + **Total Economic Impact** [Ref: A8] for lifecycle assessment.

**Multi-value analysis**:
- **Business** [Ref: G1]: Costs $800K + $120K/yr ops vs. 30% velocity gain $400K/yr. NPV (3yr, 10%): -$90K.
- **Technical** [Ref: G3]: Reduces coupling, debt -$200K, scalability +$80K/yr.
- **Organizational** [Ref: G4]: Team autonomy, -25% coordination, but -30% velocity $270K cost.
- **Risk** [Ref: G6]: Migration risk $150K, ops risk up, resilience improves.
- **Strategic** [Ref: G5]: API potential $500K/yr, faster time-to-market.

**Stakeholder views**: CFO: negative NPV; Architect: debt reduction; PM: delay; DevOps: +2 FTE; Developers: autonomy.

**Lifecycle**: Design → architecture value; Development → opportunity cost; Operations → efficiency; Evolution → strategic gains.

**Trade-offs**: Migrate now (cost/gain), delay (debt), hybrid (slower/lower risk).

**Realization**: Track DORA metrics, costs, MTTR.

**Limitations**: ±15% velocity uncertainty; assumes capability; speculative API value.

**Artifact**:

| Value Type        | Phase        | Metric                    | Year 1      | Year 2      | Year 3      | 3yr NPV (10%) |
|-------------------|--------------|---------------------------|-------------|-------------|-------------|---------------|
| **Business**      | All          | Revenue/Cost              | -$800K      | +$320K      | +$400K      | -$90K         |
| **Technical**     | Design/Ops   | Debt reduction + scaling  | -$270K      | +$200K      | +$280K      | +$140K        |
| **Organizational**| Development  | Team efficiency           | -$100K      | +$150K      | +$150K      | +$165K        |
| **Risk**          | Operations   | Incident cost reduction   | -$150K      | +$100K      | +$120K      | +$35K         |
| **Strategic**     | Evolution    | Platform/API value        | $0          | +$200K      | +$500K      | +$580K        |
| **Total NPV**     |              |                           |             |             |             | **+$830K**    |

**Communication**:
- **CFO**: 3yr NPV +$830K; breakeven mo 18
- **PM**: 3-quarter impact, 30% faster after
- **Architect**: Debt -$200K, scalability gains
- **DevOps**: +2 FTE, better resilience+observability [Ref: T4]
- **Developers**: Autonomy+modern stack

**Recommendation**: Approve with strangler pattern; allocate $50K observability; commit 2 DevOps FTE; track quarterly

**Confidence**: Medium (velocity ±15%; strategic value depends on API adoption)

## Quality Attributes

Accurate | Precise | Cited | Complete (MECE) | Actionable | Consistent | Relevant | Balanced | Recent (last 3yrs) | Testable

## Limitations and Trade-offs

**Trade-offs**: Rigor/speed (↑time ↓errors 30-40%), depth/breadth, precision/accessibility.

**Skip for**: Low-stakes (<$100K), rapid (<1h), exploratory, prototyping.

**Exclude**: Theory, speculation, edge cases (<5%), unsupported trends.

**Metrics**: Directional (±20-30%); heuristics over exact.