# Value Assessment Q&A Generator

Generate **4–8 decision-critical Q&As** for informed value decisions. Minimal viable scope: includes only questions that block decisions or create material risk.

## Context

**Problem**: Poor value assessments lead to bad decisions (over-investing in low-ROI, underestimating technical debt). Structured Q&A evaluates value across 6 dimensions: business, user, technical, organizational, strategic, risk.

**Scope**: Decision-critical scenarios (≥$100K impact or ≥20% velocity change; adjustable). Focus: software engineering lifecycle (design, development, deployment, operations).

**Constraints**: ~10–15min per Q&A; self-contained. **Assumptions**: Conflicting stakeholder priorities; context-dependent measurements. **Scale**: Individual to 50+ team decisions; 4-8 Q&A sets. **Timeline**: On-demand; 4-6h effort; refresh annually. **Stakeholders**: PM, Architect, Developer, SRE/DevOps, CFO. **Resources**: Capable LLM; optional online access.

**Terms**: Floor (min threshold ≥), Gate (fail-stop, 100% compliance), Difficulty (F=execution, I=strategy/trade-offs, A=portfolio/P&L), Value Types (Business, User, Technical, Organizational, Strategic, Risk—MECE), Decision Criticality (meets ≥1 criterion below).

**Limitations**: Balances conflicts; context-dependent; excludes speculation; customize for specific domains.

## Requirements

### Decision Criticality Framework (MANDATORY)

**Include if ≥1 criterion satisfied**: (1) **Blocks Decision** (investment go/no-go, resource allocation, strategic pivot), (2) **Creates Risk** (financial loss >10%, major opportunity cost, strategic misalignment, velocity impact >20%), (3) **Affects ≥2 Core Roles** (CFO+Architect, PM+DevOps, etc.), (4) **Requires Action** (1–6mo window, not speculative), (5) **Quantified Impact** (NPV, ROI, velocity, cost/benefit, adoption %).

**Exclude**: Niche/legacy (<5% adoption), orthogonal/nice-to-have, already covered, speculative.

### Floors (Minimum Thresholds)

| Category | Requirement |
|----------|-------------|
| **Q&A** | **4–8** \| 20% F / 40% I / 40% A \| Each: ≥2 value types+stakeholders \| ~150 words/answer |
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

Distribute **4–8 Q&As** across 3–4 phases (balanced F/I/A). ≥4 stakeholders; each Q&A ≥2 value types + ≥1 criticality criterion. **Example**: 6 Q&As = Design (2) + Development (2) + Deployment (1) + Operations (1)

### Step 2: Build References (BEFORE Q&A, then run Gates 1–6)

| Type | Count | Required | ID |
|------|-------|----------|-----|
| **Glossary** | ≥4 | Term, definition, measurement, stakeholder, lifecycle | G1... |
| **Tools** | ≥2 | Category, pricing, users, update (≤18mo), metrics, stakeholders, URL | T1... |
| **Literature** | ≥3 (≥1 ZH) | Author, title, year, summary, frameworks, lifecycle | L1... |
| **Citations** | ≥4 | APA 7th+[EN]/[ZH]/[Other]; ≥50% from last 3yrs | A1... |

**Examples**:
- **Glossary**: NPV (Net Present Value), ROI (Return on Investment), TCO (Total Cost of Ownership), WSJF (Weighted Shortest Job First)
- **Tools**: Pendo (product analytics, $50K/yr, Q2 2024), SonarQube (code quality, free, Q3 2024)
- **Literature**: Reinertsen (2009) Product Development Flow [EN], Kim (2018) Phoenix Project [EN], 俞军 (2018) 产品方法论 [ZH]
- **Citations**: AWS Well-Architected Framework, OWASP Top 10 (recent primary sources with URLs)

### Step 3: Generate Q&A (2–3 at a time, self-check)

**Question**: Decision-critical scenario with tensions. Test quantification, trade-offs, alignment. Avoid recall. Assign F/I/A. Justify criticality.

**Answer** (~150 words): (1) Key Insight (value tension + criticality, 1 sentence), (2) Framework [Ref: G#/A#], (3) Multi-Value (≥2 types + quantification), (4) Multi-Stakeholder (≥2 roles), (5) Lifecycle (brief), (6) Quantification (metrics/methods/sources), (7) Trade-offs (≥2 alternatives), (8) Decision Criteria (thresholds/targets), (9) Citations ≥1 [Ref: ID], (10) Artifact (optional).

**Batch Check**: Criticality | ≥2 signals | Word count | ≥2 types/stakeholders | Quantified | ≥1 cite

### Step 4: Create Visuals (≥1 diagram+table per Q&A)

By phase: Design (value/cost), Development (quality/velocity), Deployment (frequency/risk), Operations (SLO/efficiency). Use tables/diagrams with units, confidence, citations.

### Step 5: Populate References

**Glossary**: G#. Term | Definition | Measurement | Stakeholder | Lifecycle. **Tools**: T#. Tool | Description | Pricing | Users | Update | Metrics | URL. **Literature**: L#. Author, Title, Year | Summary | Lifecycle. **Citations**: A#. [APA 7th] [Lang].

Validate: 100% [Ref: ID] resolve; no orphans; complete fields; G≥4, T≥2, L≥3, A≥4

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**Floors**: G≥4, T≥2, L≥3, A≥4, Q=4–8, balanced | **Decision Criticality**: 100% satisfy ≥1 criterion | **Citations**: ≥50% have ≥1; ≥20% have ≥2 | **Quality**: ~150 words, 100% quantified, ≥90% scenario-based | **Coverage**: ≥4 stakeholders, ≥2 per Q&A, ≥2 value types per Q&A, 3–4 phases | **Integrity**: 100% links accessible, 100% [Ref: ID] resolve

### Step 7: Final Review

**Questions**: Clarity | Value focus | Trade-offs | Stakeholder tension | Decision-critical | Judgment>recall | Aligned difficulty. **Answers** (sample ≥3): ≥2 value types, ≥2 stakeholders, quantified, frameworks+cites, trade-offs, balanced view, decision criteria, limitations. **Submit**: All validations PASS, all gates PASS, TOC, no placeholders, criticality justified.

## Validation Report (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥4, T≥2, L≥3, A≥4, Q:4-8, 20/40/40 | | PASS/FAIL |
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
1. Lifecycle Phases Overview | 2. Q&A by Phase | 3. References | 4. Validation Report

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

See **Step 5** for formats. Alphabetize Glossary, group Tools by category, group Literature by language (EN, ZH), sort Citations by ID.

## Example

**Q1: Architect proposes microservices migration ($800K, 9mo, 5 engineers). PM: roadmap delayed. CFO: ROI justification. DevOps: operational complexity +40%. Assess total value across lifecycle?**

**Difficulty**: A | **Phase**: Design → Development → Operations → Evolution (cross-lifecycle) | **Value Types**: Business, Technical, Organizational, Risk, Strategic | **Stakeholders**: Architect, PM, CFO, DevOps/SRE, Developers

**Key Insight**: Comprehensive value assessment across lifecycle/stakeholders, balancing investment cost (negative) against distributed benefits (positive: technical/organizational/strategic) while navigating conflicting priorities.

**Answer** (~150 words):
Apply **Value Stream Mapping** [Ref: G7] + **Total Economic Impact** [Ref: A8]. **Multi-value**: Business [G1]: $800K+$120K/yr ops vs. $400K/yr velocity gain, NPV (3yr, 10%): -$90K; Technical [G3]: debt -$200K, scalability +$80K/yr; Organizational [G4]: autonomy +25%, velocity -30% ($270K cost); Risk [G6]: migration risk $150K, resilience improves; Strategic [G5]: API $500K/yr potential. **Stakeholders**: CFO: negative NPV; Architect: debt reduction; PM: delay; DevOps: +2 FTE; Developers: autonomy. **Lifecycle**: Design (architecture) → Development (opportunity cost) → Operations (efficiency) → Evolution (strategic gains). **Trade-offs**: Migrate now (cost/gain), delay (compound debt), hybrid (slower/lower risk). **Realization**: DORA metrics, costs, MTTR. **Limitations**: ±15% velocity uncertainty; assumes capability; speculative API value.

**Artifact**:

| Value Type        | Phase        | Metric                    | Year 1      | Year 2      | Year 3      | 3yr NPV (10%) |
|-------------------|--------------|---------------------------|-------------|-------------|-------------|---------------|
| **Business**      | All          | Revenue/Cost              | -$800K      | +$320K      | +$400K      | -$90K         |
| **Technical**     | Design/Ops   | Debt reduction + scaling  | -$270K      | +$200K      | +$280K      | +$140K        |
| **Organizational**| Development  | Team efficiency           | -$100K      | +$150K      | +$150K      | +$165K        |
| **Risk**          | Operations   | Incident cost reduction   | -$150K      | +$100K      | +$120K      | +$35K         |
| **Strategic**     | Evolution    | Platform/API value        | $0          | +$200K      | +$500K      | +$580K        |
| **Total NPV**     |              |                           |             |             |             | **+$830K**    |

**Communication**: CFO: NPV +$830K, breakeven mo 18 | PM: 3Q impact, 30% faster after | Architect: debt -$200K, scalability | DevOps: +2 FTE, resilience [T4] | Developers: autonomy. **Recommendation**: Approve with strangler pattern; $50K observability; 2 DevOps FTE; quarterly tracking. **Confidence**: Medium (velocity ±15%; API adoption uncertain).

## Limitations and Trade-offs

**Trade-offs**: Rigor/speed (↑time ↓errors 30-40%), depth/breadth, precision/accessibility. **Skip for**: Low-stakes (<$100K), rapid (<1h), exploratory, prototyping. **Exclude**: Theory, speculation, edge cases (<5%), unsupported trends. **Metrics**: Directional (±20-30%); heuristics over exact.

