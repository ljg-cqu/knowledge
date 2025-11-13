# Value Assessment Q&A Generator

Generate 25–30 scenario-based questions testing value judgment across system lifecycle with multi-stakeholder perspectives, evidence-based answers, and visual artifacts.

## I. Context

**Purpose**: Assess value creation/measurement/optimization across lifecycle (Requirements → Evolution) for 9+ stakeholders (Business/BA, PM, Architect, Developer, QA, DevOps, Security, Data, SRE, Leadership).

**Terms**: Floor=minimum threshold (≥) | Gate=fail-stop checkpoint | Difficulty: F=execution | I=strategy/trade-offs | A=portfolio/P&L | Value Types: Business, User, Technical, Organizational, Strategic, Risk

**Scope**: Short/long-term, tangible/intangible, all perspectives. **Exclude**: Single-phase/stakeholder focus, trivia, recall-only.

**Assumptions**: LLM knows frameworks (NPV, ROI, TCO, Value Stream Mapping, WSJF, Kano); 10-15min per question.

**Limitations**: Scenarios require customization; measurement context-dependent; stakeholder priorities conflict.

## II. Requirements

### Floors (Minimum Thresholds)

| Category | Requirement |
|----------|-------------|
| **Q&A** | 25–30 \| 20%F/40%I/40%A (±5%) \| 150–300 words/answer \| Each: ≥2 value types+stakeholders |
| **Topics (MECE)** | Requirements/Design/Development/Testing/Deployment/Operations/Maintenance/Evolution (3–4 each) \| Cross-Lifecycle (4–5) |
| **Citations** | ≥70% have ≥1; ≥30% have ≥2 \| EN 50–70%, ZH 20–40%, Other 5–15% |
| **Value Types** | Each phase: ≥4 of 6 |
| **Stakeholders** | ≥8 total; each Q&A ≥2 |
| **References** | Glossary ≥15 \| Tools ≥8 \| Literature ≥8 (≥2 ZH: 俞军/梁宁/苏杰) \| Citations ≥15 APA 7th |
| **Visuals** | Per phase: ≥1 diagram+table (8+8 min) \| Cross-lifecycle: ≥2 value flow diagrams |
| **Scaling** | >30 Q&A: multiply reference floors by 1.5× |

### Gates (Fail-Stop)

**Any failure**: stop, fix, re-validate ALL

| # | Gate | Criteria | Mitigation |
|---|------|----------|------------|
| 1 | **Recency** | ≥50% from last 3yrs (≥70% AI/ML/platform) | Flag outdated with caveats |
| 2 | **Source Diversity** | ≥3 types; no type >25% | Expand research |
| 3 | **Per-Topic Evidence** | Each: ≥2 authoritative+1 tool | Add missing |
| 4 | **Tool Completeness** | Pricing, users, update (≤18mo), ≥3 integrations | Complete/replace |
| 5 | **Link Validation** | 100% URLs accessible/archived | Archive/replace |
| 6 | **Cross-Reference** | 100% [Ref: ID] resolve; no orphans | Fix broken |

## III. Execution

### Step 1: Plan Allocation

Distribute 25–30 Q&A across 9 topics (20%F/40%I/40%A ±5%). Mix difficulties; ensure ≥8 stakeholders; each Q&A ≥2 value types.

**Example** (28): 8 phases × 3 + Cross-Lifecycle × 4 = 6F/11I/11A

### Step 2: Build References (BEFORE Q&A, then run Gates 1–6)

| Type | Count | Required | ID |
|------|-------|----------|-----|
| **Glossary** | ≥15 | Term, definition, measurement, stakeholder, lifecycle, limitations | G1... |
| **Tools** | ≥8 | Category, pricing, users, update (≤18mo), ≥3 integrations, metrics, stakeholders, lifecycle, URL | T1... |
| **Literature** | ≥8 (≥2 ZH) | Author, title, year, summary, frameworks, lifecycle | L1... |
| **Citations** | ≥15 | APA 7th+[EN]/[ZH]/[Other]; ≥50% from last 3yrs | A1... |

**Examples**: Glossary—NPV, ROI, TCO, WSJF, Technical Debt, Value Stream Mapping | Tools—Pendo, Aha!, SonarQube, CodeScene, Kubecost | Literature—Reinertsen, Kim, Cagan, Forsgren (EN); 俞军, 梁宁, 苏杰 (ZH)

### Step 3: Generate Q&A (5 at a time, self-check)

**Question**: Value scenario with stakeholder tensions, conflicts (business/technical, short/long-term) | Test ≥2 signals: quantification, trade-offs, alignment, negative value, lifecycle optimization | **Avoid** recall ("What is ROI?") | **Difficulty**: F=execution | I=strategy | A=portfolio

**Answer** (150–300 words—ALL required):
1. **Key Insight** (1 sentence): Value tension
2. **Framework** [Ref: G#/A#]
3. **Multi-Value** (≥2): Business/User/Technical/Org/Strategic/Risk+quantification
4. **Multi-Stakeholder** (≥2): Perception/measurement
5. **Lifecycle**: Creation/realization/decay
6. **Quantification**: Metrics, methods, sources
7. **Steps**: Assess, measure, track, optimize
8. **Trade-offs**: Positive/negative, alternatives
9. **Communication**: Per stakeholder
10. **Success Criteria**: Metrics, timeframes
11. **Limitations**: Uncertainty, leakage, delay
12. **Citations**: ≥1 [Ref: ID]
13. **Artifact** *(optional)*: Value stream/matrix/calculation

**Batch Check** (per 5): Scenario | ≥2 value signals | 150–300 words | ≥2 value types | ≥2 stakeholders | Lifecycle aware | ≥3/5 have ≥1 cite (≥1/5 has ≥2)

### Step 4: Create Visuals (≥1 diagram+table per phase)

**By Phase**: Requirements—Value canvas, stakeholder matrix, ROI | Design—Architecture value, debt cost, NFR | Development—Quality trend, delivery, velocity/value | Testing—Quality ROI, defect cost, coverage | Deployment—Frequency/value, release, rollback cost | Operations—SLO impact, incident cost, efficiency | Maintenance—Cost/value, debt ROI, patch | Evolution—Innovation portfolio, migration, capability | Cross-Lifecycle—Value stream, cumulative, stakeholder flow, cost/value (≥2)

**Practices**: Tables for quantitative (ROI, NPV, cost/benefit) | Diagrams for flows | Include units/periods/currencies | Show positive+negative | Indicate confidence | Cite sources

### Step 5: Populate References

| Type | Format |
|------|--------|
| **Glossary** | **G#. Term** \| Definition \| Measurement \| Stakeholder \| Lifecycle \| Limitations (alphabetize) |
| **Tools** | **T#. Tool** \| Description \| Pricing \| Users \| Update (Q# YYYY) \| Integrations (≥3) \| Metrics \| Stakeholder \| Lifecycle \| URL (group by category) |
| **Literature** | **L#. Author, Title, Year** \| Summary (value, frameworks) \| Lifecycle \| Stakeholder (group: EN, ZH) |
| **Citations** | **A#. [APA 7th] [Lang]** (sort by ID) |

**Validation**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA tagged

### Step 6: Validate (fail ANY = stop, fix, re-run ALL 15)

See **Section IV** for complete checklist. Key:
- **Floors**: G≥15, T≥8, L≥8, A≥15, Q=25–30, 20%F/40%I/40%A (±5%)
- **Citations**: ≥70% have ≥1; ≥30% have ≥2 | EN 50–70%, ZH 20–40%, Other 5–15%
- **Quality**: 100% word count 150–300 | 100% value-concrete | ≥80% frameworks value+cited+limits | ≥90% scenario
- **Coverage**: Each phase ≥4 value types | ≥8 stakeholders, each Q&A ≥2 | ≥70% cross-phase | 8/8 phases have ≥2 authoritative+1 tool
- **Integrity**: 100% links accessible | 100% [Ref: ID] resolve, no orphans

### Step 7: Final Review

**Questions**: Clarity (single ask) | Value focus | Depth (trade-offs) | Realism (stakeholder tension) | Lifecycle aware | Discriminative (judgment>recall) | Aligned difficulty

**Answers** (sample ≥5): ≥2 value types | ≥2 stakeholders | Lifecycle | Quantification | Frameworks+cites | Trade-offs/alternatives | Positive+negative | Realization criteria | Limitations/assumptions/uncertainties

**Submit**: All 15 validations PASS | All 6 gates PASS | TOC with links | No placeholders | Balanced perspectives (short/long, business/user/technical, tangible/intangible, creation/risk)

## IV. Validation Report (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥15, T≥8, L≥8, A≥15, Q:25-30, 20/40/40% | | PASS/FAIL |
| 2 | Citations          | __%≥1, __%≥2                          | ≥70%≥1, ≥30%≥2                      | | PASS/FAIL |
| 3 | Language           | EN:__%, ZH:__%, Other:__%             | EN:50-70%, ZH:20-40%, Other:5-15%   | | PASS/FAIL |
| 4 | Recency            | __% from 3yrs (domain: ___)           | ≥50% (≥70% AI/platform)             | | PASS/FAIL |
| 5 | Source Types       | __ types; max __%                     | ≥3 types, max 25%                   | | PASS/FAIL |
| 6 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 7 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 8 | Word Count         | __ sampled: __ compliant              | 100% (150-300)                      | | PASS/FAIL |
| 9 | Key Insights       | __/__ value-concrete                  | 100% (specific value tension)       | | PASS/FAIL |
| 10| Per-Phase Evidence | __/8 (≥2 auth + ≥1 tool)              | 8/8 phases                          | | PASS/FAIL |
| 11| Frameworks         | __/__ value+cited+limits              | ≥80% value-focused                  | | PASS/FAIL |
| 12| Value Judgment     | __% scenario+value                    | ≥90% value scenario-based           | | PASS/FAIL |
| 13| Value Types        | Each phase: __/6 types                | Each phase ≥4                       | | PASS/FAIL |
| 14| Stakeholder Cov    | __/8 stakeholders; Q&A: __/__ ≥2      | ≥8 total; each Q&A ≥2               | | PASS/FAIL |
| 15| Lifecycle Integ    | __% cross-phase value                 | ≥70% multi-phase or flow            | | PASS/FAIL |

## V. Question Quality (≥2 failures = rewrite/replace)

| # | Criterion | ✓ Pass | ✗ Fail |
|---|-----------|--------|--------|
| 1 | **Clarity**: Single value ask | "Quantify: refactoring vs. features?" | "Explain debt + list types" |
| 2 | **Value Signal**: Tests judgment | "Microservices ($500K, 6mo)—assess business/tech/org value?" | "List microservices benefits" |
| 3 | **Depth**: Enables trade-offs | "Allocate $2M: product/debt/platform? Justify across stakeholders" | "Should we invest in platform?" |
| 4 | **Realism**: Stakeholder tension | "Sales wants customization ($5M). Arch: 30% debt. PM: Q4 launch. Assess?" | "Calculate ROI" |
| 5 | **Discriminative**: Judgment>recall | "When does NPV mislead platform value? Supplement with flow metrics?" | "What is NPV?" |
| 6 | **Lifecycle**: Phase/cross-phase | "Design decisions create value how? Trace to deployment/operations" | "What happens in design?" |
| 7 | **Multi-Stakeholder**: ≥2 views | "QA: 30% coverage inadequate. Dev: features urgent. Leadership: value impact?" | "How do PMs measure value?" |
| 8 | **Positive+Negative**: Gains+costs | "Feature adds $2M revenue but 40% velocity drop. Full assessment?" | "What's the ROI?" |
| 9 | **Aligned Difficulty**: Match | F=measurement \| I=trade-offs \| A=portfolio/P&L | Mismatch |

## VI. Output Structure

### A. Table of Contents
1. Lifecycle Phases Overview | 2. Q&A by Phase (8+cross-lifecycle) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Lifecycle Phases Overview

**Summary**: [25–30] total | [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | 8 phases+cross-lifecycle (MECE) | 6 value types | 9+ stakeholders

| # | Phase | Range | Count | Mix | Value Types | Stakeholders | Artifacts |
|---|-------|-------|-------|-----|-------------|--------------|-----------|
| 1 | Requirements | Q1–Q3 | 3 | 1F/1I/1A | Bus/User/Str/Risk | BA/PM/Arch/Lead | 1 diagram+table |
| 2 | Design | Q4–Q6 | 3 | 0F/1I/2A | Tech/Org/Str/Risk | Arch/Dev/SRE | 1 diagram+table |
| 3 | Development | Q7–Q9 | 3 | 1F/1I/1A | Tech/Org/Risk | Dev/Arch/QA | 1 diagram+table |
| 4 | Testing | Q10–12 | 3 | 1F/1I/1A | Tech/Bus/User | QA/Dev/PM | 1 diagram+table |
| 5 | Deployment | Q13–15 | 3 | 1F/1I/1A | Org/Risk/Bus | DevOps/SRE/Arch | 1 diagram+table |
| 6 | Operations | Q16–18 | 3 | 0F/1I/2A | User/Bus/Risk | SRE/DevOps/PM | 1 diagram+table |
| 7 | Maintenance | Q19–21 | 3 | 1F/1I/1A | Tech/Risk/Bus | Dev/Sec/SRE | 1 diagram+table |
| 8 | Evolution | Q22–24 | 3 | 0F/2I/1A | Str/Bus/Org | Arch/PM/Lead | 1 diagram+table |
| 9 | Cross-Lifecycle | Q25–28 | 4 | 1F/2I/1A | All 6 | All 9 | 2 diagrams+2 tables |
| | **Total** | | **28** | **6F/11I/11A** | **All 6** | **All 9** | **10+10** |

**Legend**: F=execution | I=strategy/trade-offs | A=portfolio/P&L | Bus=Business | User=User | Tech=Technical | Org=Organizational | Str=Strategic

### C. Q&A Template

**Phase X: [Phase Name]**

**QX: [Value Scenario Question]**

**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Value Types**: [≥2] | **Stakeholders**: [≥2]

**Key Insight**: [1 sentence value tension]

**Answer** (150–300 words): Framework [Ref: G#/A#] | Multi-value (≥2 types+quantification) | Multi-stakeholder (≥2 roles) | Lifecycle | Quantification (metrics, methods, sources) | Steps | Trade-offs (positive/negative, alternatives) | Communication | Realization criteria | Limitations (uncertainty, leakage) | ≥1 [Ref: ID]

**Artifact** *(optional)*: Value stream/matrix/calculation/table

### D. References Template

See **Step 5** for formats. Summary:
- **Glossary**: **G#. Term** | Definition | Measurement | Stakeholder | Lifecycle | Limitations (alphabetize)
- **Tools**: **T#. Tool** | Description | Pricing | Users | Update | Integrations | Metrics | Stakeholder | Lifecycle | URL (group by category)
- **Literature**: **L#. Author, Title, Year** | Summary | Lifecycle | Stakeholder (group: EN, ZH)
- **Citations**: **A#. [APA 7th] [Lang]** (sort by ID)

## VII. Example

**Q1: Architect proposes microservices migration ($800K, 9 months, 5 engineers). PM says roadmap delayed. CFO asks ROI justification. DevOps says operational complexity +40%. How assess total value across lifecycle?**

**Difficulty**: A | **Phase**: Design → Development → Operations → Evolution (cross-lifecycle) | **Value Types**: Business, Technical, Organizational, Risk, Strategic | **Stakeholders**: Architect, PM, CFO/Leadership, DevOps/SRE, Developers

**Key Insight**: Tests comprehensive value assessment across lifecycle phases and stakeholder perspectives, balancing investment cost (negative value) against distributed benefits (positive value across technical/organizational/strategic dimensions) while navigating conflicting stakeholder priorities.

**Answer** (287 words):

Apply **Value Stream Mapping** [Ref: G7] + **Total Economic Impact framework** [Ref: A8] to assess lifecycle value holistically.

**Multi-value-type analysis**:
- **Business Value** [Ref: G1]: Direct costs ($800K migration + $120K/yr operational increase [Ref: A5]) vs. benefits (faster feature delivery: 30% velocity improvement after stabilization = ~$400K/yr value [Ref: L4]). NPV (3yr, 10% discount): -$90K → **marginally negative short-term**.
- **Technical Value** [Ref: G3]: Reduces deployment coupling (monolith: 2-week cycles → microservices: daily deploys [Ref: L6]). Technical debt reduction valued at $200K (measured via CodeScene debt analysis [Ref: T8]). Scalability ROI: independent scaling saves ~$80K/yr infrastructure vs. over-provisioned monolith.
- **Organizational Value** [Ref: G4]: Team autonomy enables parallel work (5 teams vs. 2 currently), reducing coordination overhead 25% [Ref: L1]. Learning investment: 9 months reduced velocity (-30%) = $270K opportunity cost.
- **Risk Value** [Ref: G6]: Migration risk (1 SEV-1 likely, $150K impact). Operational risk increases (distributed tracing, observability complexity). Resilience improves (failure isolation: blast radius 20% vs. 100% [Ref: L2]).
- **Strategic Value** [Ref: G5]: Platform enables API monetization ($500K/yr potential [Ref: A3]). Competitive positioning: time-to-market improvement.

**Stakeholder perspectives**: CFO sees negative NPV short-term; Architect values technical debt reduction + scalability; PM concerned about roadmap delay (3 quarters); DevOps sees operational burden (+2 FTE); Developers favor autonomy.

**Lifecycle value flow**: Design phase creates architecture value [Ref: T7]; Development incurs opportunity cost; Operations realizes efficiency gains (year 2+); Evolution unlocks strategic optionality.

**Trade-offs**: (1) Migrate now: upfront cost, long-term gain; (2) Delay: compound technical debt, lose competitive position; (3) Hybrid (strangler pattern [Ref: L3]): slower but lower risk.

**Value realization**: Track deployment frequency (DORA [Ref: A12]), team velocity, infrastructure costs, incident MTTR over 24 months.

**Limitations**: Velocity improvement estimate uncertain (±15%); assumes team capability building succeeds; API monetization speculative.

**Artifact**:

| Value Type        | Phase        | Metric                    | Year 1      | Year 2      | Year 3      | 3yr NPV (10%) |
|-------------------|--------------|---------------------------|-------------|-------------|-------------|---------------|
| **Business**      | All          | Revenue/Cost              | -$800K      | +$320K      | +$400K      | -$90K         |
| **Technical**     | Design/Ops   | Debt reduction + scaling  | -$270K      | +$200K      | +$280K      | +$140K        |
| **Organizational**| Development  | Team efficiency           | -$100K      | +$150K      | +$150K      | +$165K        |
| **Risk**          | Operations   | Incident cost reduction   | -$150K      | +$100K      | +$120K      | +$35K         |
| **Strategic**     | Evolution    | Platform/API value        | $0          | +$200K      | +$500K      | +$580K        |
| **Total NPV**     |              |                           |             |             |             | **+$830K**    |

**Stakeholder Communication**:
- **CFO**: 3-year NPV +$830K; breakeven month 18
- **PM**: Roadmap impact 3 quarters, but 30% faster delivery after
- **Architect**: Technical debt reduced $200K, scalability gains
- **DevOps**: +2 FTE needed, but better resilience + observability [Ref: T4]
- **Developers**: Autonomy + modern stack improve satisfaction

**Recommendation**: Approve with strangler pattern phased approach; allocate $50K observability tooling; commit 2 DevOps FTE; track value realization quarterly

**Confidence**: Medium (velocity estimates ±15%; strategic value depends on API adoption)
