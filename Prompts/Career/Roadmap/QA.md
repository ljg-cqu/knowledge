---
last_updated: 2025-11-18
status: Reviewed
owner: ljg-cqu
---

# Software Roadmap & Evolution Q&A Generator

Generate 3 decision-critical Q&As for informed roadmap decisions.

**Problem**: Hallucinations in roadmap decisions, incomplete analysis of tech shifts, ambiguous choices leading to delays or scalability issues.
**Scope**: Architectural evolution, technology adoption, strategic pivots in production distributed systems.

**Constraints**: Basic software engineering knowledge required; focus on decision-critical aspects.
**Assumptions**: Decisions materially affect roadmap.
**Context**: Typical production systems; adapt scale/constraints.
**Timeline**: Adapt to roadmap cycles.
**Stakeholders**: Architect, Dev Lead, SRE, Engineering Manager, DevOps.
**Resources**: Tools like Mermaid, GitHub, Prometheus.

**Key Terms**:
- **Decision-Critical**: Satisfies ≥1 criterion (see Content Standards).
- **Q&A**: Pair with context, impact, stakeholders, decision, action.
- **ADR**: Record documenting choices/consequences.
- **Difficulty Levels**:
  - **F** = Foundational (execution-level tasks)
  - **I** = Intermediate (strategy/trade-offs)
  - **A** = Advanced (portfolio/vision/P&L)

**Purpose and Output**: Analyze evolution, tech decisions, shifts affecting roadmap. Generate 3 Q&As across 3 phases with quantified impact, criteria, trade-offs.
**Success**: All validation checks pass; 100% decision-critical.

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total** | 3 (1 F / 1 I / 1 A) |
| **Answer** | 100-200 words: Context/Trigger → Impact → Stakeholders → Decision → Action |
| **Citations** | ≥1 per Q&A |
| **Artifacts** | Per phase: diagram + metrics; decision matrix for major trade-offs |
| **Decision Criticality** | 100% satisfy ≥1 criterion: Blocks/Risk/Roles/Evolving/Quantified |

## Coverage (3 Decision-Critical Phases, 1 Q&A Each)

1. **Architecture & Design**: Major tech decisions, ADRs, design pattern evolution (Q1)
2. **Development & Quality**: Code quality evolution, testing strategy shifts, CI/CD improvements (Q2)
3. **Operations & Scalability**: SLO changes, capacity planning, reliability improvements (Q3)

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

**Format**: Mermaid (<80 nodes, decision-focused); decision matrix when comparing options; metrics (formula + target + frequency)
**Patterns**: ADRs, STRIDE (threat modeling), SLO/Error Budget, Strangler Fig, Feature Flags, Blue/Green

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥4 | Terms + phase mapping (only decision-critical terms used in Q&As) |
| **Tools** | ≥3 | Actively maintained, valid URL, decision-critical only (ADR, roadmap, metrics tools) |
| **References** | ≥4 | APA 7th; prefer recent sources; all decision-critical |

**Quality**: Prefer recent publications; mix of architecture/DevOps/SRE sources; ≥3 resource types; <50% from any single source; 100% valid links

---

# Generation Process

1. **Plan Structure**: Identify decision-critical topics, select 1 Q&A per phase (total 3), assign difficulty levels, map stakeholders.
2. **Build References**: Create glossary (≥4 terms), tools (≥3), references (≥4, APA 7th).
3. **Write Q&As**: Craft decision-focused questions and 100-200 word answers with citations, quantified impact, alternatives.
4. **Create Artifacts**: Generate Mermaid diagrams and metrics per phase; add decision matrices for trade-offs.
5. **Link References**: Populate and validate all references.
6. **Validate**: Ensure all checks pass (counts, criticality, citations, language, recency, links, word count, quantified impact, phase coverage, stakeholders, matrices, artifacts).
7. **Final Review**: Confirm decision-first, clarity, accuracy, completeness.

**Failure Handling**: If any check fails, document, fix, re-validate until all pass.

---

# Output Template

```markdown
## Contents
[TOC: Phase Overview | Q&As by Phase | Cross-Cutting | References | Validation]

## Phase Overview
| Phase | Focus | Q&A Range | Count | Key Stakeholders | Decision Trigger |
|-------|-------|-----------|-------|------------------|------------------|
| Architecture & Design | Tech decisions, ADRs | Q1 | 1 | Architect, Dev Lead, SRE | New tech adoption, design pattern shift |
| Development & Quality | Code quality, testing | Q2 | 1 | Dev Lead, QA Lead, DevOps | Testing strategy evolution, CI/CD improvement |
| Operations & Scalability | SLOs, capacity | Q3 | 1 | SRE, DevOps, Architect | SLO change, capacity limit, reliability gap |

---

## Phase 1: Architecture & Design

**Overview**: Major technology decisions, architectural patterns, and design evolution affecting system roadmap
**Decision Trigger**: New tech adoption, design pattern shift, or architectural risk
**Stakeholders**: Architect (R), Dev Lead (A), SRE (C), Engineering Manager (C)

[Repeat Q&A structure for each Q&A in this phase]

---

## References

### Glossary (≥4)
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



### Tools (≥5)
**T1. Mermaid** [EN] – Architecture, Evolution | Text diagrams (C4, flowchart, decision trees) | 2024-10 | Free | https://mermaid.js.org
**T2. ADR GitHub Template** [EN] – Architecture | ADR generation, storage, versioning | 2024-09 | Free | https://github.com/adr/madr
**T3. Prometheus** [EN] – Operations | Metrics, PromQL, alerts, SLO tracking | 2024-10 | Free | https://prometheus.io
**T4. Grafana** [EN] – Operations | Dashboards, SLO visualization, alerting | 2024-11 | Free/Cloud/Ent | https://grafana.com
**T5. Terraform** [EN] – Architecture, Evolution | IaC (multi-cloud), capacity planning | 2024-10 | Free/Ent | https://www.terraform.io

### References (≥4, APA 7th, multi-language mix)
**R1.** Bass et al. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. [EN] | ADRs, evaluation, technical debt
**R2.** Forsgren et al. (2018). *Accelerate*. IT Revolution. [EN] | DORA metrics, deployment, performance
**R3.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly. [EN] | SLOs, error budgets, reliability
**R4.** Skelton & Pais (2019). *Team topologies*. IT Revolution. [EN] | Conway's Law, organizational design
**R5.** 周志明 (2021). *凤凰架构*. 机械工业出版社. [ZH] | Architecture patterns, evolution
**R6.** 张逸 (2019). *架构整洁之道实战*. 电子工业出版社. [ZH] | Clean architecture implementation

---

## Validation Report
| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Counts | G≥4, T≥3, R≥4, Q=3 (1/1/1) | G:X, T:Y, R:Z, Q:N | PASS/FAIL |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion | X% decision-critical | PASS/FAIL |
| 3 | Citations | 100% Q&As ≥1 citation | X% cited | PASS/FAIL |
| 4 | Language | Use clear, consistent terminology | [Check] | PASS/FAIL |
| 5 | Recency & Mix | Prefer recent sources; mix of architecture/DevOps/SRE sources | X% recent, Y% DevOps/SRE | PASS/FAIL |
| 6 | Links | 100% valid | X% valid | PASS/FAIL |
| 7 | Word count | All Q&As: 100-200 words | [Range] | PASS/FAIL |
| 8 | Quantified Impact | 100% have measurable metrics + targets | X% quantified | PASS/FAIL |
| 9 | Phase coverage | All 3 phases covered (1 Q&A each) | [Distribution] | PASS/FAIL |
| 10 | Stakeholders | ≥80% cover ≥2 core roles | X% multi-role | PASS/FAIL |
| 11 | Decision Matrices | Major trade-off decisions use a matrix (≥2 alternatives × ≥5 criteria) | X% with matrix | PASS/FAIL |
| 12 | Artifacts | ≥90% phases have diagram + metrics | X/3 complete | PASS/FAIL |

**Overall**: [X/12 PASS - need 12/12]
**Issues**: [Failures]
**Remediation**: [Actions]
**Notes**: [Observations]
```

---

**Template Version**: 2.1
**Last Updated**: 2025-11-16
**Maintained By**: Career Development Team
**Review Cadence**: Quarterly (roadmap cycles)



