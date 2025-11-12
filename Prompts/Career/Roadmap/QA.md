# Software System Construction Lifecycle Interview Q&A Generator

Generate 30-35 interview Q&A pairs demonstrating end-to-end lifecycle expertise.

## Scope

**Audience**: Architects (5+ yrs), Engineering Managers, SREs, Technical Leaders
**Output**: 30-35 Q&As across 8 phases with quantified metrics, RACI, ≥2 alternatives, citations
**Success**: 21/21 validation PASS
**Context**: Production distributed systems (>10K rps, >1TB data), 10-100 engineers, cloud-native, regulated (GDPR/SOC 2/HIPAA)

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total** | 30-35 (20% F / 40% I / 40% A difficulty) |
| **Answer** | 200-400 words: Context → Approach → Stakeholders → Deliverables → Metrics → Trade-offs |
| **Citations** | ≥1 each (≥2 complex) |
| **Per Phase** | Diagram + RACI + Criteria + Metrics |

## Coverage (8 Phases, 3-5 Q&As Each)

1. **Requirements & Discovery**: Problem validation, NFRs, risk assessment, DOR (Q1-Q4)
2. **Architecture & Design**: Solution design, ADRs, threat modeling, capacity planning (Q5-Q9)
3. **Development**: Code quality, security, collaboration, CI/CD (Q10-Q13)
4. **Testing & Quality**: Test strategy, automation, NFR validation, defect management (Q14-Q17)
5. **Deployment & Release**: Release automation, rollback, DORA metrics, zero downtime (Q18-Q21)
6. **Operations & Observability**: SLOs, monitoring, incident response, capacity (Q22-Q25)
7. **Maintenance & Support**: Vulnerability management, performance tuning, license compliance (Q26-Q29)
8. **Evolution & Governance**: Technical debt, migrations, change management, fitness functions (Q30-Q35)

## Content Standards

**Traceability**: Business goals → NFRs → Design → Code → Tests → Metrics → Feedback
**Quantified**: Use concrete metrics (✅ "DOR: 100% NFR traceability, p95 <300ms" ❌ "Complete stories")
**Context**: Team (<10/10-50/>50), Scale (<1K/1K-10K/>10K rps), Data (<1TB/1-100TB/>100TB), Maturity (greenfield/scale-up/legacy)
**Stakeholders**: 9 roles (BA, PM, Arch, Dev, QA, DevOps, Sec, SRE, Lead); RACI per phase; escalation paths
**Language**: Define terms inline, consistent terminology, concrete metrics, minimal jargon

## Artifacts

**Phase-Deliverable-Metric Mapping**:

| Phase | Diagram Type | Key Deliverable | Success Metric Formula |
|-------|-------------|-----------------|------------------------|
| Requirements | Context map, Event storming | PRD, NFR catalog | `Completeness = Stories with NFR / Total × 100%` |
| Architecture | C4 (L1-L3), Sequence | SAD, ADRs, threat model | `Coverage = ADRs / Decisions × 100%` |
| Development | Git flow, Package structure | Working software, CI | `Quality = (1 - Defects/KLOC) × Coverage%` |
| Testing | Test pyramid, Coverage | Test reports, defects | `Pass Rate = Passed / Total × 100%` |
| Deployment | Pipeline, Deployment topology | Release pipeline, runbooks | `DORA Lead Time = Commit to Deploy (hours)` |
| Operations | Service topology, Dashboards | SLOs, runbooks, alerts | `Availability = Uptime / Total × 100%` |
| Maintenance | Dependency graph, Vuln trends | Patches, performance reports | `Vuln SLA = Resolved ≤SLA / Total × 100%` |
| Evolution | Migration roadmap, Debt trends | Roadmap, debt register, RFCs | `Debt Reduction = (Debt₀ - Debt₁) / Debt₀ × 100%` |

**Format**: Mermaid (<120 nodes, phase-appropriate); Deliverables (templates + criteria); Metrics (formula + vars + target + frequency); RACI (matrix + escalation)
**Patterns**: DDD, ADRs, STRIDE, Performance Budgets, Quality Gates, Blue/Green, SLO/Error Budget, Strangler Fig, Feature Flags

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥15 | Terms + phase mapping (e.g., "DOR: Definition of Ready. Phase: Requirements. Related: NFR, Criteria") |
| **Tools** | ≥8 | Valid URL, ≤18mo old, phase, pricing, adoption |
| **Literature** | ≥8 | Authoritative (Bass, Forsgren, Beyer, Skelton, Evans, Richardson, Kleppmann, Humble) |
| **Citations** | ≥15 | APA 7th, 60%[EN]/30%[ZH]/10%other (±10%) |

**Quality**: ≥50% last 3yr (≥70% DevOps/SRE); ≥3 types, <25% single source; peer-reviewed; 100% valid links

---

# Generation Process

## 1. Plan Structure
**Actions**: Select 3-5 Q&As/phase → Allocate 30-35 total → Assign 20/40/40% F/I/A → Map stakeholders
**Checks**: 30-35 total; 20/40/40% F/I/A (±5%); 8 phases (3-5 each); 9 roles balanced

## 2. Build References
**Actions**: Glossary (≥15, phase-mapped) → Tools (≥8, URL/phase/≤18mo/pricing) → Literature (≥8 books) → Citations (≥15 APA 7th)
**Checks**: G≥15, T≥8, L≥8, A≥15; 60/30/10% EN/ZH/Other (±10%); ≥50% recent (≥70% DevOps/SRE); ≥3 types, <25% single; 100% valid URLs; 8 phases covered

## 3. Write Q&As
**Questions**: ≥70% scenario-based ("How/When/Compare..."); avoid definitions unless foundational
**Answers**: 200-400 words; ≥1 citation (≥2 complex); Context → Approach → Stakeholders → Deliverables → Metrics → Trade-offs → Limits; quantified; ≥2 alternatives + table; phase dependencies
**Validate Every 5**: Word count, citations, stakeholders, quantified, traceability, practicality

## 4. Create Artifacts
**Per Phase**: Mermaid (<120 nodes) + RACI (9 roles) + Criteria (5-10) + Metrics (≥2: formula + vars + target + frequency)
**Checks**: 8 phases complete; diagrams render; RACI has R/A; criteria measurable; formulas valid

## 5. Link References
**Actions**: Populate sections → Extract `[Ref: ID]` → Verify IDs → Map tools → Validate URLs → Remove orphans
**Checks**: G≥15, T≥8, L≥8, A≥15; 100% resolved; 0 broken; 60/30/10%; tools in ≥6 phases; no orphans

## 6. Validate (21 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥15, T≥8, L≥8, A≥15, Q=30-35 (20/40/40%) |
| 2 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 4 | Recency | ≥50% last 3yr (≥70% DevOps/SRE) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 200-400 |
| 9 | Quantified | 100% have measurable criteria |
| 10 | Phase coverage | All 8 phases 3-5 Q&As |
| 11 | Stakeholders | ≥80% cover ≥3 roles |
| 12 | RACI | 100% phases have matrix |
| 13 | Deliverables | ≥90% link to templates |
| 14 | Metrics | ≥80% have formulas |
| 15 | Traceability | ≥80% trace to NFRs |
| 16 | Diagrams | ≥90% phases have diagram |
| 17 | Trade-offs | ≥70% have ≥2 alternatives |
| 18 | Dependencies | ≥60% mention phase dependencies |
| 19 | Scenarios | ≥70% scenario-based |
| 20 | Tools | ≥8, mapped to ≥6 phases |
| 21 | Review | 6/6 criteria (see §7) |

**Failure**: ANY fail → STOP → Document → Fix → Re-validate ALL → Iterate until 21/21 PASS

## 7. Final Review (6 Criteria, All PASS)
1. **Clarity**: Logical lifecycle flow; consistent terms; explicit dependencies
2. **Accuracy**: Verifiable metrics; realistic RACI; current tools/practices
3. **Completeness**: 8 phases (3-5 each); minimums met; 21/21 PASS
4. **Balance**: ≥2 alternatives + table; multi-stakeholder; quantified trade-offs
5. **Practicality**: Actionable deliverables; measurable criteria; realistic timelines
6. **Self-Correction**: No gaps, redundancies, inconsistencies, orphans

**Submit**: 21/21 PASS + 6/6 criteria
**High-Risk**: RACI conflicts, metric formulas, phase dependencies, URLs

---

# Output Template

```markdown
## Contents
[TOC: Phase Overview | Q&As by Phase | Cross-Cutting | References | Validation]

## Phase Overview
| Phase | Focus | Q&A Range | Count | Key Stakeholders | Entry Criteria | Exit Criteria |
| 1. Requirements & Discovery | Problem validation | Q1-Q4 | 4 | BA(R), PM(A), Arch(C) | Business case approved | DOR passed |
[All 8 phases, 30-35 total, stakeholder distribution]

---

## Phase 1: Requirements & Discovery

**Overview**: [2-3 sentences: goal, challenges, success indicators]
**Deliverables**: PRD, NFR catalog, risk register, domain model, DOR checklist
**Stakeholders**: BA (R), PM (A), Architect (C), QA/Security/Data (C)

### Q1: [How/When/Compare scenario question]
**Difficulty**: [F/I/A] | **Phase**: Requirements & Discovery

**Key Insight**: [Quantified criterion or trade-off in one sentence]

**Answer**: [200-400 words: Context → Approach (roles) → Deliverables (criteria) → Metrics → Trade-offs (alternatives) → Limits] [≥1 citation [Ref: A1]]

**RACI Matrix**:
| Role | Responsibility | Actions |
| BA | Responsible | Facilitate workshops, document requirements |
| PM | Accountable | Approve scope, prioritize, resolve conflicts |
| Architect | Consulted | Validate feasibility, identify technical risks |
[All relevant roles for this question]

**Success Criteria**:
- [ ] 100% stories have NFR traceability
- [ ] All NFRs measurable with thresholds
- [ ] Risk register complete (P×I scored)
- [ ] DOR checklist validated by PM/Arch/QA
- [ ] Data classification covers all entities

**Metrics**:
| Metric | Formula | Variables | Target | Frequency |
| Completeness | `NFR Stories / Total × 100%` | NFR Stories, Total | 100% | Per sprint |
| Risk Coverage | `Scored Risks / Total × 100%` | Scored, Total | 100% | Weekly |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Stakeholders |
| Waterfall Discovery | Comprehensive upfront | Slow, inflexible | Regulated, fixed scope | PM, Legal |
| Lean Discovery | Fast iteration | Risk of rework | Greenfield, uncertain | PM, Dev |
[≥2 alternatives with quantified pros/cons]

**Phase Diagram** (per phase):
```mermaid
[Diagram type appropriate for phase: Context Map, Event Storming, C4, etc.]
[<120 nodes, clear labels, phase-specific notation]
```

---

## Cross-Cutting Dimensions
**Overview**: Multi-phase concerns requiring coordinated stakeholders

### Structural Evolution
[Architecture evolution across phases 1-8]

### Quality Assurance
[Quality from requirements through operations]

### Data Management
[Data lifecycle from classification through archival]

---

## References

### Glossary (≥15)
**G1. ADR (Architecture Decision Record)** [EN] – Phase: Architecture
Markdown doc: context, options, trade-offs, consequences. Enables traceability. **Related**: SAD, Technical Debt

**G2. DOR (Definition of Ready)** [EN] – Phase: Requirements
Checklist: user stories ready (criteria, NFRs, dependencies clear). **Related**: DoD, NFR

**G3. DORA Metrics** [EN] – Phase: Deployment
4 metrics: deploy frequency, lead time, failure rate, MTTR. **Related**: DevOps, CI/CD

**G4. SLO (Service Level Objective)** [EN] – Phase: Operations
Target for SLI (e.g., 99.9% uptime, p95 <300ms). Error budget basis. **Related**: SLI, SLA

**G5. STRIDE** [EN] – Phase: Architecture
Threat model: Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Privilege Escalation. **Related**: Security

[G6-G15: NFR, RACI, Bounded Context, Event Storming, Blue/Green, Strangler Fig, Feature Toggle, Technical Debt, CAB, RFC]

### Tools (≥8)
**T1. Mermaid** [EN] – All | Text diagrams (flowchart, C4, ERD) | 2024-10 | Free | 100M+ repos | https://mermaid.js.org
**T2. GitHub Actions** [EN] – Dev, Deploy | CI/CD automation | 2024-11 | Free/paid | 90M+ users | https://github.com/features/actions
**T3. Terraform** [EN] – Arch, Deploy, Ops | IaC (multi-cloud) | 2024-10 | Free/Ent | 10K+ orgs | https://www.terraform.io
**T4. Prometheus** [EN] – Ops | Metrics, PromQL, alerts | 2024-10 | Free | CNCF | https://prometheus.io
**T5. Grafana** [EN] – Ops | Dashboards, visualization | 2024-11 | Free/Cloud/Ent | 20M+ users | https://grafana.com
[T6-T8: OpenAPI, SonarQube, Snyk]

### Literature (≥8)
**L1.** Bass et al. (2021). *Software Architecture in Practice* (4th ed.). [EN] | Ph 2,8: ADRs, evaluation, debt
**L2.** Forsgren et al. (2018). *Accelerate*. IT Revolution. [EN] | Ph 5,6,8: DORA metrics, performance
**L3.** Beyer et al. (2016). *Site Reliability Engineering*. O'Reilly. [EN] | Ph 6,7: SLOs, error budgets, incident response
**L4.** Skelton & Pais (2019). *Team Topologies*. IT Revolution. [EN] | Ph 1,2,8: Conway's Law, cognitive load
**L5.** Evans (2003). *Domain-Driven Design*. Addison-Wesley. [EN] | Ph 1,2: Bounded contexts, event storming
**L6.** Richardson (2018). *Microservices Patterns*. Manning. [EN] | Ph 2,3,4: Decomposition, data, observability
**L7.** Kleppmann (2017). *Designing Data-Intensive Applications*. O'Reilly. [EN] | Ph 2,4,6,7: Replication, consistency
**L8.** Humble & Farley (2010). *Continuous Delivery*. Addison-Wesley. [EN] | Ph 3,4,5: Pipelines, testing

### Citations (≥15, APA 7th, 60/30/10%)
**A1.** Bass et al. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. [EN]
**A2.** Forsgren et al. (2018). *Accelerate*. IT Revolution. [EN]
**A3.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly. [EN]
**A4.** Skelton & Pais (2019). *Team topologies*. IT Revolution. [EN]
**A5.** Evans (2003). *Domain-driven design*. Addison-Wesley. [EN]
**A6.** Richardson (2018). *Microservices patterns*. Manning. [EN]
**A7.** Kleppmann (2017). *Designing data-intensive applications*. O'Reilly. [EN]
**A8.** Humble & Farley (2010). *Continuous delivery*. Addison-Wesley. [EN]
**A9.** Newman (2021). *Building microservices* (2nd ed.). O'Reilly. [EN]
**A10.** 周志明 (2021). *凤凰架构*. 机械工业出版社. [ZH]
**A11.** Kim et al. (2018). *The unicorn project*. IT Revolution. [EN]
**A12.** 张逸 (2019). *架构整洁之道实战*. 电子工业出版社. [ZH]
**A13.** Nygard (2018). *Release it!* (2nd ed.). Pragmatic Bookshelf. [EN]
**A14.** Vernon (2013). *Implementing domain-driven design*. Addison-Wesley. [EN]
**A15.** Fowler (2002). *Patterns of enterprise application architecture*. Addison-Wesley. [EN]

---

## Validation Report
| # | Check | Target | Result | Status |
| 1 | Counts | G≥15, T≥8, L≥8, A≥15, Q=30-35 | G:X, T:Y, L:Z, A:W, Q:N | PASS/FAIL |
| 2 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 | X% ≥1, Y% ≥2 | PASS/FAIL |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) | EN:X%, ZH:Y%, Other:Z% | PASS/FAIL |
| 4 | Recency | ≥50% last 3yr (≥70% DevOps/SRE) | X% recent, Y% DevOps | PASS/FAIL |
| 5 | Diversity | ≥3 types; <25% single | X types, Y% max source | PASS/FAIL |
| 6 | Links | 100% valid | X% valid | PASS/FAIL |
| 7 | Cross-refs | 100% resolved | X% resolved | PASS/FAIL |
| 8 | Word count | Sample 5: 200-400 | [Range] | PASS/FAIL |
| 9 | Quantified | 100% have measurable criteria | X% quantified | PASS/FAIL |
| 10 | Phase coverage | All 8 phases 3-5 Q&As | [Distribution] | PASS/FAIL |
| 11 | Stakeholders | ≥80% cover ≥3 roles | X% multi-role | PASS/FAIL |
| 12 | RACI | 100% phases have matrix | X/8 complete | PASS/FAIL |
| 13 | Deliverables | ≥90% link to templates | X% linked | PASS/FAIL |
| 14 | Metrics | ≥80% have formulas | X% with formulas | PASS/FAIL |
| 15 | Traceability | ≥80% trace to NFRs | X% traceable | PASS/FAIL |
| 16 | Diagrams | ≥90% phases have diagram | X/8 complete | PASS/FAIL |
| 17 | Trade-offs | ≥70% have ≥2 alternatives | X% with ≥2 | PASS/FAIL |
| 18 | Dependencies | ≥60% mention phase dependencies | X% with deps | PASS/FAIL |
| 19 | Scenarios | ≥70% scenario-based | X% scenarios | PASS/FAIL |
| 20 | Tools | ≥8, mapped to ≥6 phases | X tools, Y phases | PASS/FAIL |
| 21 | Review | 6/6 criteria | X/6 PASS | PASS/FAIL |

**Overall**: [X/21 PASS - need 21/21]
**Issues**: [Failures]
**Remediation**: [Actions]
**Notes**: [Observations]
```

---

# Example Question Patterns

## Foundational (20%)
- "Essential deliverables for Requirements & Discovery?"
- "Define DOR and its role preventing blockers."
- "DORA framework metrics?"

## Intermediate (40%)
- "Balance upfront design vs iterative discovery for regulated fintech?"
- "Establish SLOs: stakeholder inputs, resolve conflicts?"
- "Compare monolith vs microservices deployment (20 engineers, 5K rps)?"

## Advanced (40%)
- "Monolith to microservices migration (50 engineers, 100K users, zero downtime): sequencing, coordination, risks, metrics?"
- "40% test debt, 25% failure rate: 2-quarter remediation (org, tools, metrics, improvements)?"
- "Platform centralization vs embedded SREs (100 engineers): costs, velocity, criteria?"

---

# Quality Gates

## Phase Completion (Per Phase)
**Requirements**: [ ] 100% NFR traceability [ ] Measurable NFRs [ ] Risk register (P×I) [ ] DOR validated [ ] Data classified
**Architecture**: [ ] ADR coverage [ ] Performance budgets [ ] Threat model (no High) [ ] Fitness functions [ ] Capacity plan
**Development**: [ ] Lint: 0 errors [ ] ≥80% unit, ≥60% integration [ ] Complexity ≤10 [ ] 0 critical secrets, 0 SAST High [ ] 100% PRs <24h
**Testing**: [ ] ≥95% pass [ ] 100% contract tests [ ] p95 ≤ target [ ] 0 Crit/High vulns [ ] WCAG AA
**Deployment**: [ ] Lead time ≤1d [ ] Deploy ≥daily [ ] Failure ≤15% [ ] MTTR ≤1h [ ] Rollback <5min
**Operations**: [ ] ≥99.9% uptime [ ] MTTR ≤30min (SEV-1) [ ] Error budget enforced [ ] ≥99% backup [ ] 100% runbooks
**Maintenance**: [ ] Vuln: Crit ≤7d, High ≤30d [ ] Deps <6mo [ ] 0 unapproved licenses [ ] Regressions ≤10% [ ] 100% SLA
**Evolution**: [ ] ≥10% debt reduction/quarter [ ] 0 SEV-1 migrations [ ] 100% CAB approval [ ] 100% RFCs [ ] 100% fitness

## Content Quality (Generation)
- [ ] Scenario-based (How/When/Compare) [ ] 200-400 words [ ] ≥1 citation (≥2 complex)
- [ ] Quantified criteria [ ] ≥2 alternatives + table [ ] RACI (R/A clear) [ ] Criteria checklist
- [ ] ≥2 metric formulas [ ] Appropriate diagram [ ] Tools in ≥6 phases [ ] Valid links
- [ ] 60/30/10% EN/ZH/Other (±10%) [ ] ≥50% last 3yr (≥70% DevOps/SRE) [ ] No orphans/redundancy

---

**Template Version**: 1.0
**Last Updated**: 2025-11-13
**Maintained By**: Career Development Team
**Review Cadence**: Quarterly

**Change Log**:
- 2025-11-13: Initial version, adapted from Software System Construction Lifecycle Roadmap handbook, 8-phase coverage with quantified criteria and stakeholder focus
