# Software Roadmap & Evolution Q&A Generator (Minimal Viable)

Generate 6-8 decision-critical Q&As for informed roadmap decisions with minimal time investment.

**Problem**: Hallucinations in roadmap decisions, incomplete analysis of tech shifts, ambiguous choices leading to delays or scalability issues.
**Scope**: Architectural evolution, technology adoption, strategic pivots in production distributed systems.

**Constraints**: Engineering knowledge assumed; focus on decision-critical aspects.
**Assumptions**: Stakeholders provide context; decisions materially affect roadmap.
**Context**: Typical production systems; adapt scale/constraints.
**Timeline**: Adapt to roadmap cycles; typical effort 4-6h; benefits accumulate.
**Stakeholders**: Architect, Dev Lead, SRE, Engineering Manager, DevOps.
**Resources**: Mermaid, GitHub, Prometheus; prefer no-cost.

**Key Terms**:
- **Decision-Critical**: Satisfies ≥1 criterion (see Content Standards).
- **Q&A**: Pair with context, impact, stakeholders, decision, action.
- **ADR**: Record documenting choices/consequences.

**Purpose**: Analyze evolution, tech decisions, shifts affecting roadmap.
**Output**: 6-8 Q&As across 3-4 phases with quantified impact, criteria, trade-offs.
**Success**: 12/12 validation PASS; 100% decision-critical.

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total** | 6-8 (25% F / 50% I / 25% A) |
| **Answer** | 150-250 words: Context/Trigger → Impact → Stakeholders → Decision → Action |
| **Citations** | ≥1 per Q&A |
| **Artifacts** | Per phase: diagram + metrics; decision matrix for major trade-offs |
| **Decision Criticality** | 100% satisfy ≥1 criterion: Blocks/Risk/Roles/Evolving/Quantified |

## Coverage (3-4 Decision-Critical Phases, 1-2 Q&As Each)

1. **Architecture & Design**: Major tech decisions, ADRs, design pattern evolution (Q1-Q2)
2. **Development & Quality**: Code quality evolution, testing strategy shifts, CI/CD improvements (Q3-Q4)
3. **Operations & Scalability**: SLO changes, capacity planning, reliability improvements (Q5-Q6)
4. **Evolution & Governance**: Technical debt, migrations, architectural shifts (Q7-Q8)

## Content Standards

**Decision Criticality**: Every Q&A must satisfy ≥1 criterion:
- **Blocks Decision**: Directly impacts architecture roadmap, tech stack choice, strategic pivot
- **Creates Risk**: Material threat (technical debt, scalability limit, compliance gap)
- **Affects ≥2 Stakeholders**: Multi-team impact (Architect + SRE, Dev Lead + DevOps)
- **Actively Evolving**: Tech/market/regulatory changes in past 3-6 months
- **Quantified Impact**: Adoption %, performance gain, cost reduction, velocity improvement

**Quantified**: Concrete metrics (✅ "Monolith→microservices: 40% deployment time ↓, 3-month roadmap" ❌ "Scale better")
**Context**: State concrete scales (for example, team 10-100 engineers, 100–100K rps, 1–100TB data, scale-up or legacy); adjust ranges to match your system
**Stakeholders**: ≥5 core roles (Architect, Dev Lead, SRE, DevOps, Engineering Manager); decision makers explicit
**Language**: Define terms inline, consistent terminology, concrete metrics, minimal jargon

## Artifacts

| Phase | Diagram Type | Key Deliverable | Success Metric Formula |
|-------|-------------|-----------------|------------------------|
| Architecture & Design | C4 (L1-L2), Decision tree | ADRs, tech roadmap | `Adoption = Teams using / Total × 100%` |
| Development & Quality | CI/CD pipeline, Quality gates | Testing strategy, tooling | `Quality Velocity = Defects ↓ / Velocity ↑ × 100%` |
| Operations & Scalability | Service topology, SLO dashboard | Capacity plan, runbooks | `Reliability = Uptime / Target × 100%` |
| Evolution & Governance | Migration roadmap, Debt trends | Roadmap, debt register | `Debt Reduction = (Debt₀ - Debt₁) / Debt₀ × 100%` |

**Format**: Mermaid (<80 nodes, decision-focused); decision matrix when comparing options; metrics (formula + target + frequency)
**Patterns**: ADRs, STRIDE (threat modeling), SLO/Error Budget, Strangler Fig, Feature Flags, Blue/Green

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥8 | Terms + phase mapping (only decision-critical terms used in Q&As) |
| **Tools** | ≥5 | Actively maintained, valid URL, decision-critical only (ADR, roadmap, metrics tools) |
| **Literature** | ≥6 | Canonical references (Bass, Forsgren, Beyer, Skelton, Kleppmann, Richardson) |
| **Citations** | ≥8 | APA 7th; aim for ≥2 languages (e.g., EN + ZH); all decision-critical |

**Quality**: ≥50% published in last 10 years; mix of architecture/DevOps/SRE sources; ≥3 resource types; <50% from any single source; 100% valid links

---

# Generation Process

## 1. Plan Structure
**Actions**: Identify decision-critical roadmap topics → Select 1-2 Q&As/phase → Allocate 6-8 total → Assign 25/50/25% F/I/A → Map ≥5 core stakeholders
**Checks**: 6-8 total; 25/50/25% F/I/A (±5%); 3-4 phases (1-2 each); ≥5 core roles; 100% decision-critical

## 2. Build References
**Actions**: Glossary (≥8, decision-critical only) → Tools (≥5, URL/phase, actively maintained) → Literature (≥6 canonical) → Citations (≥8 APA 7th)
**Checks**: G≥8, T≥5, L≥6, A≥8; aim for ≥2 languages (e.g., EN + ZH); ≥50% published in last 10 years; mix of architecture/DevOps/SRE sources; ≥3 resource types; <50% from any single source; 100% valid URLs

## 3. Write Q&As
**Questions**: Decision-focused ("How to decide on...", "When to migrate...", "Compare..."); scenario-based
**Answers**: 150-250 words; ≥1 citation; Context/Trigger → Impact → Stakeholders → Decision → Action; quantified; ≥2 alternatives; decision criteria explicit
**Validate Every 2**: Word count, citations, decision criticality, quantified impact, stakeholder clarity

## 4. Create Artifacts
**Per Phase**: Mermaid diagram (<80 nodes, decision-focused) + Metrics (≥2: formula + target + frequency); add a decision matrix (≥2 alternatives × ≥5 criteria) for major trade-off decisions
**Checks**: 3-4 phases complete; diagrams render; metrics clear; any decision matrices have measurable criteria and valid formulas

## 5. Link References
**Actions**: Populate sections → Extract `[Ref: ID]` → Verify IDs → Validate URLs → Remove orphans
**Checks**: G≥8, T≥5, L≥6, A≥8; 100% resolved; 0 broken; language mix per References; no orphans

## 6. Validate (12 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥8, T≥5, L≥6, A≥8, Q=6-8 (25/50/25%) |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion: Blocks/Risk/Roles/Evolving/Quantified |
| 3 | Citations | 100% Q&As ≥1 citation |
| 4 | Language | Aim for ≥2 languages (e.g., EN + ZH); avoid relying on a single language |
| 5 | Recency & Mix | ≥50% published in last 10 years; mix of architecture, DevOps, and SRE sources |
| 6 | Links | 100% valid |
| 7 | Word count | All Q&As: 150-250 words |
| 8 | Quantified Impact | 100% have measurable metrics + targets |
| 9 | Phase coverage | All 3-4 phases covered (1-2 Q&As each) |
| 10 | Stakeholders | ≥80% cover ≥2 core roles |
| 11 | Decision Matrices | Major trade-off decisions use a matrix (≥2 alternatives × ≥5 criteria) |
| 12 | Artifacts | ≥90% phases have diagram + metrics |

**Failure**: ANY fail → STOP → Document → Fix → Re-validate ALL → Iterate until 12/12 PASS

## 7. Final Review (4 Criteria, All PASS)
1. **Decision-First**: Every Q&A blocks a decision or creates material risk; 100% decision-critical
2. **Clarity**: Clear trigger (scenario/change) → impact → decision → action; consistent terms; explicit decision criteria
3. **Accuracy**: Verifiable metrics; realistic alternatives; current tools/practices; valid URLs
4. **Completeness**: 6-8 Q&As across 3-4 phases; minimums met; 12/12 PASS

**Submit**: 12/12 PASS + 4/4 criteria
**High-Risk**: Decision criticality justification, metric formulas, stakeholder clarity, URLs

---

# Output Template

```markdown
## Contents
[TOC: Phase Overview | Q&As by Phase | Cross-Cutting | References | Validation]

## Phase Overview
| Phase | Focus | Q&A Range | Count | Key Stakeholders | Decision Trigger |
|-------|-------|-----------|-------|------------------|------------------|
| Architecture & Design | Tech decisions, ADRs | Q1-Q2 | 1-2 | Architect, Dev Lead, SRE | New tech adoption, design pattern shift |
| Development & Quality | Code quality, testing | Q3-Q4 | 1-2 | Dev Lead, QA Lead, DevOps | Testing strategy evolution, CI/CD improvement |
| Operations & Scalability | SLOs, capacity | Q5-Q6 | 1-2 | SRE, DevOps, Architect | SLO change, capacity limit, reliability gap |
| Evolution & Governance | Tech debt, migrations | Q7-Q8 | 1-2 | Architect, Engineering Manager, Dev Lead | Debt threshold, migration roadmap, strategic shift |

---

## Phase 1: Architecture & Design

**Overview**: Major technology decisions, architectural patterns, and design evolution affecting system roadmap
**Decision Trigger**: New tech adoption, design pattern shift, or architectural risk
**Stakeholders**: Architect (R), Dev Lead (A), SRE (C), Engineering Manager (C)

### Q1: [How to decide on tech adoption? When to migrate patterns? Compare approaches?]
**Difficulty**: [I/A] | **Phase**: Architecture & Design | **Decision Criticality**: [Blocks/Risk/Roles/Evolving/Quantified]

**Context**: [What scenario/constraint prompted this decision?]

**Answer**: [150-250 words: Context → Impact (quantified) → Stakeholders (roles + concerns) → Decision (alternatives + criteria) → Action (timeline + owner)] [≥1 citation [Ref: A1]]

**Decision Matrix**:
| Criterion | Option A | Option B | Option C | Weight |
|-----------|----------|----------|----------|--------|
| Adoption barrier (effort) | High | Medium | Low | 30% |
| Performance impact | +10% | +5% | +2% | 25% |
| Team expertise | Low | Medium | High | 20% |
| Risk (breaking changes) | High | Medium | Low | 25% |
| **Score** | **X** | **Y** | **Z** | **100%** |

**Metrics**:
| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| Adoption | `Teams using / Total × 100%` | ≥60% in 3mo | Monthly |
| Performance | `Latency / Baseline × 100%` | ≤95% | Per release |

**Phase Diagram**:
```mermaid
[C4 L1-L2 or Decision tree: <80 nodes, decision-focused]
```

---

## References

### Glossary (≥8)
**G1. ADR (Architecture Decision Record)** [EN] – Phase: Architecture & Design
Markdown doc: context, options, trade-offs, consequences. Enables traceability. **Related**: Technical Debt, Decision Matrix

**G2. SLO (Service Level Objective)** [EN] – Phase: Operations & Scalability
Target for SLI (e.g., 99.9% uptime, p95 <300ms). Error budget basis. **Related**: SLI, SLA, Reliability

**G3. Technical Debt** [EN] – Phase: Evolution & Governance
Accumulated shortcuts/deferred work. Quantified: effort to remediate. **Related**: Refactoring, Roadmap

**G4. DORA Metrics** [EN] – Phase: Development & Quality
4 metrics: deploy frequency, lead time, failure rate, MTTR. **Related**: DevOps, CI/CD, Performance

**G5. Strangler Fig** [EN] – Phase: Evolution & Governance
Incremental migration pattern: new system gradually replaces legacy. **Related**: Migration, Risk Mitigation

**G6. Feature Flags** [EN] – Phase: Development & Quality
Runtime toggles: enable/disable features without deployment. **Related**: CI/CD, Blue/Green, Rollback

**G7. Bounded Context** [EN] – Phase: Architecture & Design
DDD: explicit boundary around domain model. **Related**: Microservices, Domain-Driven Design

**G8. Error Budget** [EN] – Phase: Operations & Scalability
Acceptable downtime: SLO target - actual uptime. Guides incident response. **Related**: SLO, Reliability

### Tools (≥5)
**T1. Mermaid** [EN] – Architecture, Evolution | Text diagrams (C4, flowchart, decision trees) | 2024-10 | Free | https://mermaid.js.org
**T2. ADR GitHub Template** [EN] – Architecture | ADR generation, storage, versioning | 2024-09 | Free | https://github.com/adr/madr
**T3. Prometheus** [EN] – Operations | Metrics, PromQL, alerts, SLO tracking | 2024-10 | Free | https://prometheus.io
**T4. Grafana** [EN] – Operations | Dashboards, SLO visualization, alerting | 2024-11 | Free/Cloud/Ent | https://grafana.com
**T5. Terraform** [EN] – Architecture, Evolution | IaC (multi-cloud), capacity planning | 2024-10 | Free/Ent | https://www.terraform.io

### Literature (≥6)
**L1.** Bass et al. (2021). *Software Architecture in Practice* (4th ed.). Addison-Wesley. [EN] | ADRs, evaluation, technical debt
**L2.** Forsgren et al. (2018). *Accelerate*. IT Revolution. [EN] | DORA metrics, deployment, performance
**L3.** Beyer et al. (2016). *Site Reliability Engineering*. O'Reilly. [EN] | SLOs, error budgets, reliability
**L4.** Skelton & Pais (2019). *Team Topologies*. IT Revolution. [EN] | Conway's Law, organizational design
**L5.** Richardson (2018). *Microservices Patterns*. Manning. [EN] | Decomposition, migration patterns
**L6.** Kleppmann (2017). *Designing Data-Intensive Applications*. O'Reilly. [EN] | Scalability, consistency, replication

### Citations (≥8, APA 7th, multi-language mix)
**A1.** Bass et al. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. [EN]
**A2.** Forsgren et al. (2018). *Accelerate*. IT Revolution. [EN]
**A3.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly. [EN]
**A4.** Skelton & Pais (2019). *Team topologies*. IT Revolution. [EN]
**A5.** Richardson (2018). *Microservices patterns*. Manning. [EN]
**A6.** Kleppmann (2017). *Designing data-intensive applications*. O'Reilly. [EN]
**A7.** 周志明 (2021). *凤凰架构*. 机械工业出版社. [ZH]
**A8.** 张逸 (2019). *架构整洁之道实战*. 电子工业出版社. [ZH]
**A9.** ISO/IEC/IEEE 42010:2011. *Systems and software engineering — Architecture description*. International Organization for Standardization. [Other]

---

## Validation Report
| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Counts | G≥8, T≥5, L≥6, A≥8, Q=6-8 (25/50/25%) | G:X, T:Y, L:Z, A:W, Q:N | PASS/FAIL |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion | X% decision-critical | PASS/FAIL |
| 3 | Citations | 100% Q&As ≥1 citation | X% cited | PASS/FAIL |
| 4 | Language | Aim for ≥2 languages (e.g., EN + ZH); avoid relying on a single language | EN:X%, ZH:Y%, Other:Z% | PASS/FAIL |
| 5 | Recency & Mix | ≥50% published in last 10 years; mix of architecture/DevOps/SRE sources | X% recent, Y% DevOps/SRE | PASS/FAIL |
| 6 | Links | 100% valid | X% valid | PASS/FAIL |
| 7 | Word count | All Q&As: 150-250 words | [Range] | PASS/FAIL |
| 8 | Quantified Impact | 100% have measurable metrics + targets | X% quantified | PASS/FAIL |
| 9 | Phase coverage | All 3-4 phases covered (1-2 Q&As each) | [Distribution] | PASS/FAIL |
| 10 | Stakeholders | ≥80% cover ≥2 core roles | X% multi-role | PASS/FAIL |
| 11 | Decision Matrices | Major trade-off decisions use a matrix (≥2 alternatives × ≥5 criteria) | X% with matrix | PASS/FAIL |
| 12 | Artifacts | ≥90% phases have diagram + metrics | X/4 complete | PASS/FAIL |

**Overall**: [X/12 PASS - need 12/12]
**Issues**: [Failures]
**Remediation**: [Actions]
**Notes**: [Observations]
```

---

**Template Version**: 2.0 (Minimal Viable)
**Last Updated**: 2025-11-16
**Maintained By**: Career Development Team
**Review Cadence**: Quarterly (roadmap cycles)


