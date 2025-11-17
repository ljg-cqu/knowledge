# Requirement Analysis Q&A Generator (Minimal Viable)

Generate 4-6 decision-critical Q&As for requirement analysis with minimal viable coverage for informed decisions and actions.

## Scope & Success Criteria

**Purpose**: Analyze decision-critical requirement scenarios (blocks decision or creates material risk) with limited time  
**Audience**: BA, PM, Architect, DevOps, Security (≥5 core roles)  
**Output**: 4-6 Q&As × 3-4 phases × 2-3 viewpoints × 3-4 quality perspectives | Decision Criticality Framework | Quantified impact | Citations  
**Success**: 12/12 validation PASS | 25% F / 50% I / 25% A difficulty | Decision-critical only (blocks decision, creates risk, affects ≥2 roles, requires 1-6mo action, quantified impact) | 4-6h effort

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 4-6 (25% F / 50% I / 25% A) |
| **Length** | 120-200 words |
| **Components** | Scenario context → Decision Criticality → Impact → Stakeholders → Decision → Action |
| **Citations** | ≥1 per Q&A |
| **Artifacts/Cluster** | ≥2 diagrams + ≥1 table (60% reduction) |

## Coverage (3-4 Decision-Critical Phases × 2-3 Viewpoints)

### 3-4 Decision-Critical Lifecycle Phases

1. **Requirements & Discovery** (Blocks decision): Elicitation gaps | NFR misses | Scope creep | Acceptance criteria clarity
2. **Architecture & Design** (Creates risk): Integration feasibility | Performance budgets | Threat landscape | Compliance gaps
3. **Testing & Quality** (Affects ≥2 roles): Quality gates | Acceptance criteria | Test coverage | Defect escape risk
4. **Operations & Observability** (Requires action): SLO/monitoring gaps | Observability blind spots | Incident response readiness

### 2-3 Decision-Critical Viewpoints

1. **Technical**: Architecture feasibility | Integration risks | Data modeling gaps | API contract changes
2. **Business/Market**: Scope/prioritization impact | ROI/resource allocation | Competitive requirements | Market fit risk
3. **Regulation/Compliance**: Compliance deadline changes | Data residency shifts | Audit gaps | Regulatory threat

### 3-4 Decision-Critical Quality Perspectives (NFR)

1. **Performance**: Threshold changes (p95/p99 latency, rps targets) | Bottleneck discovery | Budget overruns
2. **Security**: Threat landscape shifts | Vulnerability patterns | Compliance requirement changes
3. **Reliability**: Failure scenario discovery | MTTR/MTBF target changes | Error budget exhaustion
4. **Observability** (optional): Monitoring gap discovery | MTTD/SNR threshold changes | Tracing coverage gaps

## ≥5 Core Stakeholder Roles (Decision-Critical)

| Role | Primary Concerns |
|------|------------------|
| **BA** | Elicitation gaps | Acceptance criteria clarity | Scope creep risk |
| **PM** | Prioritization impact | ROI/resource allocation | Market fit risk |
| **Architect** | Integration feasibility | NFR feasibility | Technology risk |
| **DevOps** | Deployment/infrastructure impact | Scaling strategy | Automation gaps |
| **Security** | Threat landscape shifts | Compliance gaps | Data classification changes |

## Content Standards (Decision-Critical Requirement Scenarios)

**Decision Criticality Framework**: Every Q&A must satisfy ≥1 criterion:
- **Blocks Decision**: Directly impacts requirement prioritization, go/no-go, or strategic pivot
- **Creates Risk**: Material threat (scope creep, compliance gap, integration failure, performance regression)
- **Affects ≥2 Roles**: Multi-stakeholder impact (BA + PM, Architect + DevOps, etc.)
- **Requires Action**: 1-6mo action window (not speculative)
- **Quantified Impact**: Requirement coverage %, NFR threshold change, compliance deadline, integration risk score

**Quantified Impact**: ✅ "NFR threshold change: p95 latency <300ms → <200ms" ❌ "Performance improved"
**Review cadence**: Review and refresh scenarios and references at least every 12-18 months or whenever requirement practices, architecture, or regulatory context change materially.
**Traceability**: Scenario context → Decision Criticality → Impact → Stakeholder action → Metric

---

# Decision-Critical Requirement Analysis

## Scenario Selection Strategy (Mandatory, ≥10-15 candidates)

**Tier 1 - Active/Blocking** (≥50% of candidates): Scenarios blocking current decisions or creating immediate risk  
**Tier 2 - Emerging** (≤30% of candidates): Emerging patterns or evolving requirements  
**Tier 3 - Foundational** (≤20% of candidates): Foundational concepts with high adoption barriers

**Scenario Sources**: Production systems | Stakeholder interviews | Architecture reviews | Compliance audits | Integration assessments

## Best Practices

**Required**: Decision Criticality Framework applied to every Q&A | Quantified impact (coverage %, threshold change, risk score) | Multi-stakeholder validation (≥2 roles) | Actionable guidance (1-6mo timeline)  
**Prohibited**: Speculation | Vendor marketing | Single-source scenarios | Vague impact | No decision criteria

---

# Minimal Viable Artifacts (60% Reduction)

## Decision-Critical Artifact Mapping

| Phase/Viewpoint | Diagrams | Impact Table | Metrics |
|-----------------|----------|--------------|---------|
| **Requirements & Discovery** | Elicitation gap heatmap | Scope impact (coverage %, risk score) | DOR % | NFR coverage % |
| **Architecture & Design** | Integration risk matrix | Feasibility impact (effort, risk) | Integration SLA % | Threat CVSS |
| **Testing & Quality** | Quality gate flow | Defect escape risk | Pass rate % | Coverage % |
| **Operations & Observability** | SLO/monitoring gap map | Observability impact (MTTD, SNR) | SLO compliance % | MTTD |

## Decision-Critical Quality Artifacts

| Quality | Diagram | Impact Metric | Threshold |
|---------|---------|---------------|-----------|
| **Performance** | Latency breakdown | Threshold change (p95/p99) | <300ms → <200ms |
| **Security** | Threat model (STRIDE) | Vulnerability count | 0 Critical |
| **Reliability** | Failure tree | MTTR/MTBF change | <30min MTTR |
| **Observability** | Tracing coverage map | MTTD/SNR change | <5min MTTD |

---

# Minimal Viable Generation Process (4-6h, On-Demand)

## 1. Scenario Selection & Analysis (1-2h)

**Actions**: Identify candidates (Tier 1: Active/Blocking, Tier 2: Emerging, Tier 3: Foundational) → ≥10-15 scenarios → Apply Decision Criticality Framework → Select 4-6 decision-critical Q&As  
**Checks**: ≥50% Tier 1 | ≥1 criterion per Q&A | Quantified impact | Multi-stakeholder validation

## 2. Build References (30-45 min)

**Actions**: Glossary (≥8 terms) | Tools (≥3: decision-critical only) | Literature (≥6: canonical only) | Citations (≥6 APA 7th)  
**Checks**: G≥8, T≥3, L≥6, C≥6 | 100% valid URLs | ≥2 citations ≤10yr old (recent practice), others canonical

## 3. Write Q&As (2-3h)

**Each Q&A** (120-200w): Scenario context → Decision Criticality (≥1 criterion) → Impact (quantified) → Stakeholders (≥2 roles) → Decision (go/no-go + rationale) → Action (0-2wk, 2wk-2mo) | ≥1 citation  
**Validate/5**: Word count (120-200) | Citations (≥1) | Decision Criticality (≥1 criterion) | Impact (quantified) | Actionability (timeline + owner)

## 4. Create Artifacts (30-45 min)

**Per Q&A**: ≥2 diagrams (decision tree, risk matrix, impact flow) + ≥1 table (impact assessment, decision matrix, stakeholder actions)  
**Checks**: All render | Tables formatted | Diagrams <80 nodes

## 5. Link References (15 min)

**Actions**: Extract `[Ref: ID]` → Verify IDs exist → Validate URLs  
**Checks**: 100% `[Ref: ID]` resolved | 0 broken links

## 6. Validate (12 Checks, Streamlined)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | Q=4-6, G≥8, T≥3, L≥6, C≥6 |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion |
| 3 | Citations | ≥70% Q&As have ≥1; mix of canonical + ≥2 citations ≤10yr |
| 4 | Review | All Q&As and references reviewed in last 18mo |
| 5 | Links | 100% valid |
| 6 | Word count | Sample 3: 120-200 |
| 7 | Impact | 100% quantified |
| 8 | Stakeholders | ≥2 roles per Q&A |
| 9 | Decision | 100% have go/no-go criteria |
| 10 | Action | 100% have timeline + owner |
| 11 | Artifacts | ≥2 diagrams + ≥1 table per Q&A |
| 12 | Overall | 12/12 PASS |

**Failure**: ANY fail → Document → Fix → Re-validate → Iterate → 12/12 PASS

## 7. Final Review (3 Criteria)

**Criteria (All PASS)**: Clarity (decision-critical focus, consistent terms) | Accuracy (verifiable scenarios and sources, sound impact, valid metrics) | Actionability (go/no-go criteria, timeline, owner)
**Submit**: 12/12 PASS + 3/3 criteria  
**High-Risk**: Decision Criticality | Quantified impact | Timeline/owner

---

# Output Template (Minimal Viable)

```markdown
## Contents
[TOC: Decision-Critical Q&As | References | Validation]

## Decision-Critical Q&As (4-6 Total)

| # | Scenario | Phase | Viewpoint | Criticality | Roles | Range |
|---|----------|-------|-----------|-------------|-------|-------|
| 1 | [Scenario title] | [Phase] | [Viewpoint] | [Blocks/Risk/Roles/Action/Quantified] | [≥2] | Q1 |
[4-6 rows, 25% F / 50% I / 25% A]

---

## Q1: [Decision-Critical Requirement Scenario]
**[F/I/A]** | **Phase**: [Phase] | **Viewpoint**: [Viewpoint] | **Quality**: [Perspectives]  
**Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified] | **Justification**: [Why included]

**Answer** [120-200w]:
- **Scenario Context** (~25w): What, why, scope, stakeholders
- **Decision Criticality** (~30w): Which criterion satisfied + impact scope
- **Impact** (~40w): Quantified (%, $, timeline, risk score) + affected phases/roles
- **Stakeholders** (~30w): ≥2 roles, concerns, required actions
- **Decision** (~40w): Go/no-go criteria + rationale + success targets
- **Action** (~15w): Immediate (0-2wk) + short-term (2wk-2mo) + owner

[≥1 [Ref: C1]]

**Impact Assessment**:
| Dimension | Current | Change | Impact | Timeline |
| [Metric] | [Baseline] | [New] | [Risk/Opportunity] | [1-6mo] |

**Stakeholder Actions**:
| Role | Concern | Action | Owner | Deadline |
| [BA/PM/Arch/etc] | [Concern] | [Action] | [Owner] | [Date] |

**Diagram**: ```mermaid [Decision tree / Risk matrix / Impact flow] ```

---

## References

### Glossary (≥8)
**G1. [Term]** [EN/ZH/Other]: [Definition]. **Related**: [Terms]

### Tools (≥3, Decision-Critical)
**T1. [Tool]** [Tag]: [Purpose]. **Updated**: [YYYY-MM] | **URL**: [Link]

### Literature (≥6, Canonical)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag]: [Relevance]

### Citations (≥6, APA 7th, canonical + ≥2 ≤10yr)
**C1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report (12 Checks)
| # | Check | Target | Result | Status |
| 1 | Counts | Q=4-6, G≥8, T≥3, L≥6, C≥6 | [X] | PASS/FAIL |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion | [X] | PASS/FAIL |
| 3 | Citations | ≥70% ≥1; mix of canonical + ≥2 citations ≤10yr | [X] | PASS/FAIL |
| 4 | Review | All Q&As and references reviewed in last 18mo | [X] | PASS/FAIL |
| 5 | Links | 100% valid | [X] | PASS/FAIL |
| 6 | Word count | Sample 3: 120-200 | [X] | PASS/FAIL |
| 7 | Impact | 100% quantified | [X] | PASS/FAIL |
| 8 | Stakeholders | ≥2 roles per Q&A | [X] | PASS/FAIL |
| 9 | Decision | 100% have go/no-go criteria | [X] | PASS/FAIL |
| 10 | Action | 100% have timeline + owner | [X] | PASS/FAIL |
| 11 | Artifacts | ≥2 diagrams + ≥1 table per Q&A | [X] | PASS/FAIL |
| 12 | Overall | 12/12 PASS | [X] | PASS/FAIL |

**Overall**: [X/12 PASS - need 12/12] | **Issues**: [Failures] | **Remediation**: [Actions]
```

---

# Reference Examples (Decision-Critical Only)

## Glossary (≥8)

**G1. Decision Criticality** [EN]: Framework for prioritizing requirement scenarios and changes: Blocks decision, Creates risk, Affects ≥2 roles, Requires 1-6mo action, Quantified impact
**G2. NFR** [EN]: Non-Functional Requirements (performance, security, reliability, scalability, observability)
**G3. SLO** [EN]: Service Level Objective (e.g., 99.9% availability). Drives error budget  
**G4. STRIDE** [EN]: Threat model (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation)  
**G5. RACI** [EN]: Responsible, Accountable, Consulted, Informed ownership  
**G6. Scope Creep** [EN]: Uncontrolled expansion of requirements. Risk: budget/timeline overrun  
**G7. Integration Risk** [EN]: Feasibility/compatibility threat from third-party dependencies  
**G8. Acceptance Criteria** [EN]: Measurable conditions for requirement completion (INVEST: Testable)

## Tools (≥3, Decision-Critical)

**T1. Mermaid** [EN]: Text diagrams (decision trees, risk matrices, impact flows) | 2024-10 | Free/OSS | https://mermaid.js.org  
**T2. Jira/Confluence** [EN]: Requirement tracking, impact assessment, decision logging | 2024-11 | Paid | https://www.atlassian.com  
**T3. OWASP Threat Dragon** [EN]: STRIDE threat modeling for security requirements | 2024-08 | Free/OSS | https://owasp.org/www-project-threat-dragon

## Literature (≥6, Canonical)

**L1. Wiegers & Beatty (2013). *Software Requirements* (3rd). Microsoft Press** [EN]: Elicitation, NFR spec, traceability  
**L2. Bass et al. (2021). *Software Architecture in Practice* (4th). Addison-Wesley** [EN]: NFR scenarios, quality attributes  
**L3. Beyer et al. (2016). *Site Reliability Engineering*. O'Reilly** [EN]: SLO, error budgets, observability requirements  
**L4. Shostack (2014). *Threat Modeling*. Wiley** [EN]: STRIDE, security requirements  
**L5. Cohn (2004). *User Stories Applied*. Addison-Wesley** [EN]: INVEST, acceptance criteria  
**L6. Kleppmann (2017). *Designing Data-Intensive Applications*. O'Reilly** [EN]: Data requirements, consistency models

## Citations (≥6, APA 7th, ≤2yr)

**C1.** Wiegers & Beatty (2013). *Software requirements* (3rd). Microsoft Press [EN]  
**C2.** Bass, Clements & Kazman (2021). *Software architecture in practice* (4th). Addison-Wesley [EN]  
**C3.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly [EN]  
**C4.** Shostack (2014). *Threat modeling: Designing for security*. Wiley [EN]  
**C5.** Cohn (2004). *User stories applied*. Addison-Wesley [EN]  
**C6.** Kleppmann (2017). *Designing data-intensive applications*. O'Reilly [EN]

---
