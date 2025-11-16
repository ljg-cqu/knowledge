# Value Assessment Q&A Generator (Minimal Viable)

Generate **6–12 decision-critical Q&As** for informed value decisions with limited time. Minimal viable value assessment: blocks decisions or creates material risk.

## I. Context

**Purpose**: Assess decision-critical value creation/measurement/optimization across lifecycle for ≥5 core stakeholders (PM, Architect, Developer, SRE, Leadership).

**Terms**: Floor=minimum threshold (≥) | Gate=fail-stop checkpoint | Difficulty: F=execution | I=strategy/trade-offs | A=portfolio/P&L | Value Types: Business, User, Technical, Organizational, Strategic, Risk

**Scope**: Decision-critical scenarios only (blocks decision or creates material risk). **Exclude**: Niche/legacy, orthogonal/nice-to-have, already covered, speculative.

**Cadence**: On-demand | **Effort**: 4–6h per cycle | **Validity**: Evergreen (refresh annually or when business context changes)

**Assumptions**: LLM knows frameworks (NPV, ROI, TCO, Value Stream Mapping, WSJF); 10–15min per question.

**Limitations**: Scenarios require customization; measurement context-dependent; stakeholder priorities conflict.

## II. Requirements

### Decision Criticality Framework (NEW - MANDATORY)

**Include if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts investment go/no-go, resource allocation, or strategic pivot (e.g., $1M+ investment, team scaling, tech stack change)
- **Creates Risk**: Material threat (financial loss >10%, opportunity cost, strategic misalignment, velocity impact >20%)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (CFO + Architect, PM + DevOps, etc.)
- **Requires Action**: 1–6mo action window (not speculative)
- **Quantified Impact**: NPV $, ROI %, velocity %, cost/benefit ratio, adoption %

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative

### Floors (Minimum Thresholds)

| Category | Requirement |
|----------|-------------|
| **Q&A** | **6–12** \| 25%F/50%I/25%A \| 150–250 words/answer \| Each: ≥2 value types+stakeholders |
| **Lifecycle Phases** | 3–4 decision-critical only (Design, Development, Deployment, Operations) |
| **Citations** | ≥70% have ≥1; ≥30% have ≥2 \| EN 50–70%, ZH 20–40%, Other 5–15% |
| **Value Types** | Each Q&A: ≥2 of 6 |
| **Stakeholders** | ≥5 core roles (PM, Architect, Developer, SRE, Leadership); each Q&A ≥2 |
| **References** | Glossary ≥8 \| Tools ≥4 \| Literature ≥5 (≥1 ZH) \| Citations ≥8 APA 7th |
| **Visuals** | ≥1 diagram+table per Q&A (compressed) |
| **Decision Criticality** | 100% of Q&As satisfy ≥1 criterion |

### Gates (Fail-Stop)

**Any failure**: stop, fix, re-validate ALL

| # | Gate | Criteria | Mitigation |
|---|------|----------|------------|
| 1 | **Decision Criticality** | 100% of Q&As satisfy ≥1 criterion | Rewrite/replace non-critical |
| 2 | **Recency** | ≥50% from last 3yrs | Flag outdated with caveats |
| 3 | **Source Diversity** | ≥3 types; no type >40% | Expand research |
| 4 | **Link Validation** | 100% URLs accessible/archived | Archive/replace |
| 5 | **Cross-Reference** | 100% [Ref: ID] resolve; no orphans | Fix broken |
| 6 | **Quantified Impact** | 100% Q&As have quantified metrics | Add metrics |

## III. Execution

### Step 1: Plan Allocation

Distribute **6–12 Q&As** across 3–4 decision-critical lifecycle phases (25%F/50%I/25%A). Ensure ≥5 core stakeholders; each Q&A ≥2 value types + ≥1 Decision Criticality criterion.

**Example** (8): Design (2) + Development (2) + Deployment (2) + Operations (2) = 2F/4I/2A

### Step 2: Build References (BEFORE Q&A, then run Gates 1–6)

| Type | Count | Required | ID |
|------|-------|----------|-----|
| **Glossary** | ≥8 | Term, definition, measurement, stakeholder, lifecycle | G1... |
| **Tools** | ≥4 | Category, pricing, users, update (≤18mo), metrics, stakeholders, URL | T1... |
| **Literature** | ≥5 (≥1 ZH) | Author, title, year, summary, frameworks, lifecycle | L1... |
| **Citations** | ≥8 | APA 7th+[EN]/[ZH]/[Other]; ≥50% from last 3yrs | A1... |

**Examples**: Glossary—NPV, ROI, TCO, WSJF, Technical Debt, Value Stream Mapping, Kano Model, Opportunity Cost | Tools—Pendo, Aha!, SonarQube, Kubecost | Literature—Reinertsen, Kim, Cagan (EN); 俞军 (ZH)

### Step 3: Generate Q&A (2–3 at a time, self-check)

**Question**: Decision-critical value scenario with stakeholder tensions (business/technical, short/long-term) | Test ≥2 signals: quantification, trade-offs, alignment, negative value | **Avoid** recall ("What is ROI?") | **Difficulty**: F=execution | I=strategy | A=portfolio | **MANDATORY**: Justify Decision Criticality criterion

**Answer** (150–250 words—streamlined):
1. **Key Insight** (1 sentence): Value tension + decision criticality
2. **Framework** [Ref: G#/A#]
3. **Multi-Value** (≥2): Business/User/Technical/Org/Strategic/Risk + quantification
4. **Multi-Stakeholder** (≥2): Perception/measurement/concerns
5. **Lifecycle**: Creation/realization/decay (brief)
6. **Quantification**: Metrics, methods, sources (quantified)
7. **Trade-offs**: Positive/negative, alternatives (≥2)
8. **Decision Criteria**: Go/no-go thresholds, success targets
9. **Citations**: ≥1 [Ref: ID]
10. **Artifact** *(optional)*: Value matrix/calculation

**Batch Check** (per 2–3): Decision Criticality criterion | ≥2 value signals | 150–250 words | ≥2 value types | ≥2 stakeholders | Quantified | ≥1 cite

### Step 4: Create Visuals (≥1 diagram+table per Q&A)

**By Phase** (decision-critical only):
- **Design**: Architecture value vs. cost, debt impact, trade-off matrix
- **Development**: Quality/velocity trade-off, cost/benefit, stakeholder impact
- **Deployment**: Frequency/value, cost/benefit, risk matrix
- **Operations**: SLO impact, incident cost, efficiency gains

**Practices**: Tables for quantitative (NPV, ROI, cost/benefit) | Diagrams for flows/trade-offs | Include units/currencies | Show positive+negative | Indicate confidence | Cite sources

### Step 5: Populate References

| Type | Format |
|------|--------|
| **Glossary** | **G#. Term** \| Definition \| Measurement \| Stakeholder \| Lifecycle (alphabetize) |
| **Tools** | **T#. Tool** \| Description \| Pricing \| Users \| Update (Q# YYYY) \| Metrics \| URL (group by category) |
| **Literature** | **L#. Author, Title, Year** \| Summary (value, frameworks) \| Lifecycle (group: EN, ZH) |
| **Citations** | **A#. [APA 7th] [Lang]** (sort by ID) |

**Validation**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA tagged

### Step 6: Validate (fail ANY = stop, fix, re-run ALL 12)

See **Section IV** for complete checklist. Key:
- **Floors**: G≥8, T≥4, L≥5, A≥8, Q=6–12, 25%F/50%I/25%A
- **Decision Criticality**: 100% satisfy ≥1 criterion [Blocks/Risk/Roles/Action/Quantified]
- **Citations**: ≥70% have ≥1; ≥30% have ≥2 | EN 50–70%, ZH 20–40%, Other 5–15%
- **Quality**: 100% word count 150–250 | 100% value-concrete + quantified | ≥90% scenario-based
- **Coverage**: ≥5 core stakeholders, each Q&A ≥2 | ≥2 value types per Q&A | 3–4 phases covered
- **Integrity**: 100% links accessible | 100% [Ref: ID] resolve, no orphans

### Step 7: Final Review

**Questions**: Clarity (single ask) | Value focus | Depth (trade-offs) | Realism (stakeholder tension) | Decision-critical (blocks decision or creates risk) | Discriminative (judgment>recall) | Aligned difficulty

**Answers** (sample ≥3): ≥2 value types | ≥2 stakeholders | Quantification | Frameworks+cites | Trade-offs/alternatives | Positive+negative | Decision criteria | Limitations/assumptions

**Submit**: All 12 validations PASS | All 6 gates PASS | TOC with links | No placeholders | Decision Criticality justified for each Q&A

## IV. Validation Report (fill all; ANY fail = stop, fix, re-run ALL 12)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥8, T≥4, L≥5, A≥8, Q:6-12, 25/50/25% | | PASS/FAIL |
| 2 | Decision Criticality| __/__ satisfy ≥1 criterion            | 100% [Blocks/Risk/Roles/Action/Quantified] | | PASS/FAIL |
| 3 | Citations          | __%≥1, __%≥2                          | ≥70%≥1, ≥30%≥2                      | | PASS/FAIL |
| 4 | Language           | EN:__%, ZH:__%, Other:__%             | EN:50-70%, ZH:20-40%, Other:5-15%   | | PASS/FAIL |
| 5 | Recency            | __% from 3yrs                         | ≥50%                                | | PASS/FAIL |
| 6 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 7 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 8 | Word Count         | __ sampled: __ compliant              | 100% (150-250)                      | | PASS/FAIL |
| 9 | Key Insights       | __/__ value-concrete + quantified     | 100% (specific value tension)       | | PASS/FAIL |
| 10| Frameworks         | __/__ value+cited                     | ≥80% value-focused                  | | PASS/FAIL |
| 11| Value Judgment     | __% scenario+value                    | ≥90% value scenario-based           | | PASS/FAIL |
| 12| Stakeholder Cov    | __/5 core roles; Q&A: __/__ ≥2        | ≥5 total; each Q&A ≥2               | | PASS/FAIL |

## V. Question Quality (≥2 failures = rewrite/replace)

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

## VI. Output Structure

### A. Table of Contents
1. Lifecycle Phases Overview | 2. Q&A by Phase (3–4 phases) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Lifecycle Phases Overview

**Summary**: [6–12] total | [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | 3–4 decision-critical phases | ≥2 value types per Q&A | ≥5 core stakeholders

| # | Phase | Range | Count | Mix | Value Types | Stakeholders | Artifacts |
|---|-------|-------|-------|-----|-------------|--------------|-----------|
| 1 | Design | Q1–Q3 | 2–3 | 0–1F/1–2I/1–2A | Tech/Org/Str/Risk | Arch/Dev/SRE | 1 diagram+table |
| 2 | Development | Q4–Q6 | 2–3 | 1F/1–2I/1A | Tech/Org/Risk | Dev/Arch/PM | 1 diagram+table |
| 3 | Deployment | Q7–Q9 | 2–3 | 1F/1I/1A | Org/Risk/Bus | DevOps/SRE/Arch | 1 diagram+table |
| 4 | Operations | Q10–Q12 | 2–3 | 0–1F/1–2I/1A | User/Bus/Risk | SRE/DevOps/PM | 1 diagram+table |
| | **Total** | | **8–12** | **2–4F/4–8I/2–4A** | **≥2 per Q&A** | **≥5 core** | **4–8 total** |

**Legend**: F=execution | I=strategy/trade-offs | A=portfolio/P&L | Bus=Business | User=User | Tech=Technical | Org=Organizational | Str=Strategic | Risk=Risk

### C. Q&A Template

**Phase X: [Phase Name]**

**QX: [Value Scenario Question]**

**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Value Types**: [≥2] | **Stakeholders**: [≥2] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

**Key Insight**: [1 sentence value tension + decision criticality]

**Answer** (150–250 words): Framework [Ref: G#/A#] | Multi-value (≥2 types+quantification) | Multi-stakeholder (≥2 roles) | Lifecycle (brief) | Quantification (metrics, methods, sources) | Trade-offs (≥2 alternatives) | Decision criteria (go/no-go) | ≥1 [Ref: ID]

**Artifact** *(optional)*: Value matrix/calculation/table

### D. References Template

See **Step 5** for formats. Summary:
- **Glossary**: **G#. Term** | Definition | Measurement | Stakeholder | Lifecycle (alphabetize)
- **Tools**: **T#. Tool** | Description | Pricing | Users | Update | Metrics | URL (group by category)
- **Literature**: **L#. Author, Title, Year** | Summary | Lifecycle (group: EN, ZH)
- **Citations**: **A#. [APA 7th] [Lang]** (sort by ID)

|---|-----------|--------|--------|
| 1 | **Clarity**: Single value ask | "Microservices ($500K, 6mo)—assess business/tech/org value?" | "Explain value types" |
| 2 | **Decision Criticality**: Blocks/Risk | "$2M investment blocks roadmap. Allocate: product/debt/platform?" | "Should we invest in platform?" |
| 3 | **Quantification**: Metrics | "Feature: +$2M revenue, -40% velocity. NPV? Payback? Risk?" | "Calculate ROI" |
| 4 | **Realism**: Stakeholder tension | "Sales: $5M customization. Arch: 30% debt. PM: Q4 launch. Assess?" | "What's the value?" |
## VII. Example

**Q1: Architect proposes microservices migration ($800K, 9mo, 5 engineers). PM: roadmap delayed. CFO: ROI justification. DevOps: operational complexity +40%. Assess total value across lifecycle?**

**Difficulty**: A | **Phase**: Design → Development → Operations → Evolution (cross-lifecycle) | **Value Types**: Business, Technical, Organizational, Risk, Strategic | **Stakeholders**: Architect, PM, CFO, DevOps/SRE, Developers

**Key Insight**: Comprehensive value assessment across lifecycle/stakeholders, balancing investment cost (negative) against distributed benefits (positive: technical/organizational/strategic) while navigating conflicting priorities.

**Answer** (262 words):

Apply **Value Stream Mapping** [Ref: G7] + **Total Economic Impact** [Ref: A8] for lifecycle assessment.

**Multi-value analysis**:
- **Business** [Ref: G1]: Costs ($800K migration + $120K/yr ops [Ref: A5]) vs. benefits (30% velocity improvement = ~$400K/yr [Ref: L4]). NPV (3yr, 10%): -$90K → **marginally negative short-term**.
- **Technical** [Ref: G3]: Reduces coupling (2-week → daily deploys [Ref: L6]). Debt reduction $200K (CodeScene [Ref: T8]). Scalability saves ~$80K/yr infrastructure.
- **Organizational** [Ref: G4]: Team autonomy (5 teams vs. 2), -25% coordination [Ref: L1]. Learning cost: 9mo reduced velocity (-30%) = $270K opportunity cost.
- **Risk** [Ref: G6]: Migration risk (1 SEV-1, $150K). Ops risk increases (tracing, observability). Resilience improves (blast radius 20% vs. 100% [Ref: L2]).
- **Strategic** [Ref: G5]: API monetization ($500K/yr potential [Ref: A3]). Competitive positioning: faster time-to-market.

**Stakeholder views**: CFO: negative NPV short-term; Architect: debt reduction+scalability; PM: 3-quarter delay; DevOps: +2 FTE burden; Developers: autonomy.

**Lifecycle flow**: Design creates architecture value [Ref: T7]; Development incurs opportunity cost; Operations realizes efficiency (year 2+); Evolution unlocks strategic optionality.

**Trade-offs**: (1) Migrate now: upfront cost, long-term gain; (2) Delay: compound debt, lose position; (3) Hybrid (strangler [Ref: L3]): slower, lower risk.

**Realization**: Track deployment frequency (DORA [Ref: A12]), velocity, infrastructure costs, MTTR over 24mo.

**Limitations**: Velocity estimate uncertain (±15%); assumes team capability success; API monetization speculative.

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
