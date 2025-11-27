# Strategic Roadmap & Evolution Q&A Generator

Generate 3 decision-critical Q&As for informed roadmap decisions across any industry or domain.

> **Cross-Industry Application**: This framework applies to software, manufacturing, healthcare, finance, education, logistics, retail, construction, and more. Adapt terminology, metrics, and stakeholders to your specific domain while maintaining the decision-critical focus and structured approach.

**Problem**: Hallucinations in roadmap decisions, incomplete analysis of strategic shifts, ambiguous choices leading to delays, inefficiencies, or scalability issues.

**Scope**: Strategic evolution, process optimization, technology/methodology adoption, operational pivots in any industry (software, manufacturing, healthcare, finance, education, logistics, etc.).

**Scale**: 3 Q&As (1 F / 1 I / 1 A); 10-15min/question.

**Timeline**: Roadmap cycles (quarterly/annual); adapt to planning windows.

**Stakeholders**: Domain leaders, operational managers, specialists, executives, cross-functional teams (≥5 core roles).

**Constraints**: Basic domain knowledge; decision-critical only; 100-200 words/answer.

**Assumptions**: Decisions materially affect roadmap; operational systems (10-100 team members, measurable throughput/capacity metrics, relevant scale indicators).

**Resources**: Domain-appropriate tools (visualization, decision documentation, monitoring, automation, collaboration platforms).

**Success**: All validations pass (12/12); 100% decision-critical; ≥1 citation per Q&A; G≥4, T≥3, R≥4.

**Key Terms**:
- **Decision-Critical**: Satisfies ≥1 criterion (see Content Standards).
- **Q&A**: Pair with context, impact, stakeholders, decision, action.
- **Decision Record (DR)**: Document capturing choices, rationale, and consequences.
- **Difficulty Levels**:
  - **F** = Foundational (execution-level tasks)
  - **I** = Intermediate (strategy/trade-offs)
  - **A** = Advanced (portfolio/vision/P&L)

**Purpose and Output**: Analyze evolution, strategic decisions, shifts affecting roadmap. Generate 3 Q&As across 3 phases with quantified impact, criteria, trade-offs.
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

1. **Strategy & Design**: Major strategic decisions, design choices, methodology evolution, structural changes (Q1)
2. **Execution & Quality**: Process optimization, quality assurance evolution, workflow improvements, standards implementation (Q2)
3. **Operations & Scale**: Performance targets, capacity planning, reliability improvements, resource optimization (Q3)

## Content Standards

**Decision Criticality**: Every Q&A must satisfy ≥1 criterion:
- **Blocks Decision**: Directly impacts strategic roadmap, methodology choice, structural pivot, resource allocation
- **Creates Risk**: Material threat (process debt, capacity limits, compliance gaps, quality issues, safety concerns)
- **Affects ≥2 Stakeholders**: Multi-team/department impact (cross-functional dependencies)
- **Actively Evolving**: Technology/market/regulatory/competitive changes in past 3-6 months
- **Quantified Impact**: Adoption %, performance gain, cost reduction, efficiency improvement, quality metrics

**Quantified**: Concrete metrics (✅ "Manual→automated: 40% processing time ↓, 3-month implementation" ❌ "Works better")
**Context**: State concrete scales (team size 10-100, throughput metrics, capacity indicators, growth stage); adjust to match your domain
**Stakeholders**: ≥5 core roles from domain (functional leaders, specialists, managers, executives); decision makers explicit
**Language**: Define terms inline, consistent terminology, concrete metrics, minimal jargon

## Artifacts

| Phase | Diagram Type | Key Deliverable | Success Metric Formula |
|-------|-------------|-----------------|------------------------|
| Strategy & Design | Process flow, Decision tree, Structure diagram | Decision records, strategic roadmap | `Adoption = Units using / Total × 100%` |
| Execution & Quality | Workflow diagram, Quality gates, Process maps | Quality framework, standards, procedures | `Quality Efficiency = Defects ↓ / Output ↑ × 100%` |
| Operations & Scale | System topology, Performance dashboard, Resource maps | Capacity plan, operational procedures | `Performance = Actual / Target × 100%` |

**Format**: Visual diagrams (<80 nodes, decision-focused); decision matrix when comparing options; metrics (formula + target + frequency)
**Patterns**: Decision records, risk assessment frameworks, performance targets, incremental migration, staged rollouts, A/B testing, pilot programs

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥4 | Terms + phase mapping (only decision-critical terms used in Q&As) |
| **Tools** | ≥3 | Actively maintained, valid URL, decision-critical only (decision documentation, roadmap, metrics, collaboration tools) |
| **References** | ≥4 | APA 7th; prefer recent sources; all decision-critical |

**Quality**: Prefer recent publications; mix of strategic/operational/domain-specific sources; ≥3 resource types; <50% from any single source; 100% valid links

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
| Strategy & Design | Strategic decisions, structural design | Q1 | 1 | Domain leaders, specialists, executives | New methodology adoption, design shift, structural change |
| Execution & Quality | Process optimization, quality standards | Q2 | 1 | Operations managers, quality leads, specialists | Process evolution, standards update, workflow improvement |
| Operations & Scale | Performance targets, capacity planning | Q3 | 1 | Operations leads, resource managers, domain experts | Performance target change, capacity limit, reliability gap |

---

## Phase 1: Strategy & Design

**Overview**: Major strategic decisions, structural design choices, and methodology evolution affecting domain roadmap
**Decision Trigger**: New methodology adoption, design paradigm shift, or strategic risk
**Stakeholders**: Domain Leader (R), Strategy Lead (A), Operations Lead (C), Executive Sponsor (C)

[Repeat Q&A structure for each Q&A in this phase]

---

## References

### Glossary (≥4)
**G1. Decision Record (DR)** [EN] – Phase: Strategy & Design
Document: context, options, trade-offs, consequences. Enables traceability. **Related**: Process Debt, Decision Matrix

**G2. Performance Target** [EN] – Phase: Operations & Scale
Objective for performance indicator (e.g., 95% on-time delivery, <2h response time). Baseline for measurement. **Related**: KPI, SLA, Reliability

**G3. Process Debt** [EN] – Phase: Operations & Scale
Accumulated shortcuts/deferred improvements. Quantified: effort to remediate. **Related**: Optimization, Roadmap

**G4. Performance Metrics** [EN] – Phase: Execution & Quality
Key indicators: throughput, cycle time, error rate, resolution time. **Related**: Operations, Quality, Efficiency

**G5. Incremental Migration** [EN] – Phase: Strategy & Design
Phased transition pattern: new system gradually replaces legacy. **Related**: Change Management, Risk Mitigation

**G6. Pilot Program** [EN] – Phase: Execution & Quality
Limited rollout: test changes in controlled environment before full deployment. **Related**: A/B Testing, Risk Mitigation, Rollback



### Tools (≥5)
**T1. Mermaid** [EN] – Strategy, Operations | Visual diagrams (flowchart, process maps, decision trees) | 2024-10 | Free | https://mermaid.js.org
**T2. Decision Record Templates** [EN] – Strategy | DR generation, storage, versioning | 2024-09 | Free | https://github.com/adr/madr
**T3. Performance Dashboards** [EN] – Operations | Metrics tracking, alerts, performance monitoring (e.g., Tableau, Power BI, Grafana) | 2024-11 | Free/Commercial | Domain-specific
**T4. Process Mapping Tools** [EN] – Execution | Workflow visualization, process optimization (e.g., Lucidchart, Draw.io, Visio) | 2024-10 | Free/Commercial | Domain-specific
**T5. Project Management Platforms** [EN] – All Phases | Planning, tracking, collaboration (e.g., Asana, Jira, Monday.com) | 2024-11 | Free/Commercial | https://asana.com

### References (≥4, APA 7th, multi-language mix)
**R1.** Rumelt, R. (2011). *Good strategy bad strategy*. Crown Business. [EN] | Strategic planning, decision frameworks, execution
**R2.** Goldratt, E. M. (2014). *The goal: A process of ongoing improvement* (3rd ed.). North River Press. [EN] | Process optimization, bottlenecks, throughput
**R3.** Kim, G., Behr, K., & Spafford, G. (2018). *The Phoenix Project*. IT Revolution. [EN] | Operations, flow, improvement patterns
**R4.** Ries, E. (2011). *The lean startup*. Crown Business. [EN] | Innovation, experimentation, validated learning
**R5.** Kahneman, D. (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux. [EN] | Decision-making, cognitive biases, risk assessment
**R6.** 陈春花 (2020). *管理的常识*. 机械工业出版社. [ZH] | Management fundamentals, organizational design, operations

---

## Validation Report
| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Counts | G≥4, T≥3, R≥4, Q=3 (1/1/1) | G:X, T:Y, R:Z, Q:N | PASS/FAIL |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion | X% decision-critical | PASS/FAIL |
| 3 | Citations | 100% Q&As ≥1 citation | X% cited | PASS/FAIL |
| 4 | Language | Use clear, consistent terminology | [Check] | PASS/FAIL |
| 5 | Recency & Mix | Prefer recent sources; mix of strategic/operational/domain-specific sources | X% recent, Y% operational | PASS/FAIL |
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

**Template Version**: 3.0
**Last Updated**: 2025-11-27
**Maintained By**: Strategic Planning Team
**Review Cadence**: Quarterly (roadmap cycles)
**Applicability**: Cross-industry (software, manufacturing, healthcare, finance, education, logistics, etc.)



