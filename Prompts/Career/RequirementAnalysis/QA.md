# Requirement Analysis Interview Q&A Generator

Generate 30-35 interview Q&As for requirement analysis across all lifecycle phases, stakeholders, viewpoints, and quality perspectives.

## Scope & Success Criteria

**Audience**: BA, PM, Architect, Developer, QA/SET, DevOps, Security, Data Engineer, SRE, Leadership (10 roles)  
**Output**: 30-35 Q&As × 8 phases × 6 viewpoints × 10 quality perspectives | Elicitation techniques | Quantified NFRs | ≥2 alternatives | Citations  
**Success**: 23/23 validation PASS | 15/45/40% F/I/A difficulty | Production-grade (>10K rps, >1TB, multi-team, cloud-native, regulated) | Cross-functional (10-100 engineers) | Polyglot (Go/Java/Python/TS) | Compliance (GDPR/HIPAA/SOC2) | Blockchain/distributed systems

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 30-35 (15% F / 45% I / 40% A) |
| **Length** | 150-350 words |
| **Components** | Viewpoint → Technique → Stakeholders → NFR → Trade-offs → Validation |
| **Citations** | ≥1 (≥2 complex) |
| **Artifacts/Cluster** | Diagram + Template + Comparison + Metrics |

## Coverage (8 Lifecycle Phases × 6 Viewpoints)

### 8 Lifecycle Phases

1. **Requirements & Discovery**: Problem validation | Domain modeling | NFR definition | Risk assessment | Data classification
2. **Architecture & Design**: Solution design | ADRs | Threat modeling | Performance budgets | Capacity planning
3. **Development**: Implementation standards | Code quality | Observability instrumentation
4. **Testing & Quality**: Test strategy | Quality gates | Defect management | Acceptance validation
5. **Deployment & Release**: Release planning | Automation | Rollback | Blue/green
6. **Operations & Observability**: SLO management | Incident response | Capacity planning | Monitoring
7. **Maintenance & Support**: Patching | Tuning | Technical debt | Compliance updates
8. **Evolution & Governance**: Roadmap | Migration | Continuous improvement | Change control

### 6 Viewpoints (MECE)

1. **Technical**: Architecture | Stack | Integration | Data modeling | API design
2. **Ecosystem**: Partner integrations | Third-party APIs | OSS dependencies | Vendor landscape | Network effects
3. **Business/Market**: Revenue models | Pricing | Competitive positioning | Market fit | Customer segments
4. **Regulation/Compliance**: GDPR/HIPAA/SOC2/PCI-DSS | Data residency | Audit | Consent management
5. **Organization/Team**: Conway's Law | Team topology | Collaboration | Skills | Communication
6. **Process/Governance**: Methodology | Change management | Decision frameworks | Approvals

### 10 Quality Perspectives (NFR)

1. **Performance**: Throughput (rps) | Latency (p50/p95/p99) | CPU/Memory | Response time
2. **Security**: AuthN/AuthZ | Encryption (rest/transit) | Vulnerability mgmt | Secrets
3. **Reliability**: Error rates | Fault tolerance | Retry | Circuit breakers | MTTR
4. **Availability**: Uptime (SLO %) | Redundancy | DR (RTO/RPO) | Failover | Health checks
5. **Scalability**: H/V scaling | Partitioning/Sharding | Load distribution | Bottlenecks
6. **Decentralization**: Node distribution | Consensus | Topology | Validators | Stake distribution
7. **Trust**: BFT | Cryptographic guarantees | Validator incentives | Slashing
8. **Transparency**: Audit trails | Public verifiability | Provenance | Immutable logs | On-chain governance
9. **Maintainability**: Code quality | Tech debt | Documentation | Onboarding time
10. **Observability**: Metrics | Logging | Tracing | Alerting | Dashboards

## 10 Stakeholder Roles

| Role | Primary Concerns |
|------|------------------|
| **BA** | Elicitation completeness \| Acceptance criteria \| Traceability \| Stakeholder alignment |
| **PM** | Business value \| User needs \| Market fit \| Prioritization \| Roadmap |
| **Architect** | NFR feasibility \| Integration constraints \| Technology choices \| Boundaries |
| **Developer** | Implementation clarity \| API contracts \| Data schemas \| Error handling |
| **QA/SET** | Testability \| Measurable criteria \| Quality metrics \| Automation scope |
| **DevOps** | Deployment requirements \| Infrastructure \| Automation \| Scaling strategy |
| **Security** | Threat landscape \| Compliance gaps \| Data classification \| Attack surface |
| **Data Engineer** | Data sources \| Quality requirements \| Schema evolution \| Pipeline SLAs |
| **SRE** | SLO targets \| Failure scenarios \| Capacity planning \| Runbooks |
| **Leadership** | Business alignment \| Risk tolerance \| Resource allocation \| ROI |

## Content Standards

**Traceability**: Goal → FR → NFR → Criteria → Validation → Metrics  
**Quantified NFRs**: ✅ "p95 <300ms @ 10K rps, 4c/8GB" ❌ "Fast"  
**Context Thresholds**: Team (<10 / 10-50 / >50) | Scale (<100 / 100-10K / >10K rps) | Data (<100GB / 100GB-10TB / >10TB) | Compliance (Low/Med/High) | Decentralization (None/Partial/Full)  
**Balance**: ≥2 approaches + table | Assumptions/limitations | Tags: `[Consensus]`/`[Context-dependent]`/`[Emerging]`  
**Precision**: INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable) | Measurable NFRs | Clear criteria

---

# Elicitation Techniques

## Core Techniques by Viewpoint

| Viewpoint | Techniques | Artifacts | Stakeholders |
|-----------|------------|-----------|--------------|
| **Technical** | Event storming \| API workshops \| Data modeling | C4 \| OpenAPI \| ERD | Architects \| Developers \| Data Engineers |
| **Ecosystem** | Partner interviews \| Integration mapping \| Dependency analysis | Integration diagrams \| API contracts \| SLAs | Business \| Architects \| Third-parties |
| **Business/Market** | Value proposition canvas \| Competitive analysis \| Pricing workshops | BMC \| SWOT \| Market sizing | PM \| Execs \| Finance |
| **Regulation** | Compliance checklists \| Data classification \| Audit reviews | DFD \| Consent flows \| Audit trails | Legal \| Compliance \| Security |
| **Organization** | Team topology \| Skills assessment \| Collaboration analysis | Org charts \| RACI \| Communication maps | Managers \| HR \| Leads |
| **Process** | Process mapping \| Decision logs \| Retrospectives | BPMN \| ADR \| Governance policies | PM \| Architects \| Leadership |

## Best Practices

**Required**: Multi-stakeholder workshops (≥3 perspectives) | Quantifiable criteria (100% NFRs) | Prototype validation (≥80% UX) | Risk assessment (P×I) | Assumption logging | Traceability matrix  
**Prohibited**: Single-source requirements | Vague criteria | Missing NFRs | Undocumented assumptions | No owners

---

# Artifacts & Supporting Materials

## Requirement Artifact Mapping

| Phase | Diagrams | Templates | Metrics |
|-------|----------|-----------|---------|
| **Requirements** | Event storming \| Domain model \| Context map | PRD \| User stories (Gherkin) \| NFR catalog | DOR % \| NFR coverage % |
| **Architecture** | C4 (L1-L4) \| Sequence \| ERD \| Threat model | SAD \| ADR \| API specs (OpenAPI) | ADR coverage \| Threat CVSS |
| **Development** | Component \| Data flow | Coding standards \| PR template | Code coverage % \| Cyclomatic complexity |
| **Testing** | Test pyramid \| Coverage heatmap | Test plan \| Defect template | Pass rate % \| Defect density |
| **Deployment** | Pipeline \| Blue/green | Runbook \| Rollback plan | Deployment freq \| Change failure % |
| **Operations** | Dashboard \| Alert topology | SLO definition \| Incident template | SLO compliance % \| MTTR |
| **Maintenance** | Dependency graph \| Debt heatmap | Patch policy \| Escalation matrix | Vulnerability SLA % \| Debt % |
| **Evolution** | Roadmap \| Migration phases | RFC template \| Change policy | Migration success % \| Governance % |

## Quality Perspective Artifacts

| Quality | Diagrams | Criteria | Thresholds |
|---------|----------|----------|------------|
| **Performance** | Flamegraph \| Latency breakdown | p95 \| Throughput (rps) \| CPU % | <300ms \| >10K rps \| <60% CPU |
| **Security** | Threat model (STRIDE) \| Auth flow | Attack surface \| Vulnerability count | 0 Critical \| <5 High \| CVSS <7.0 |
| **Reliability** | Failure tree \| Retry flow | Error % \| MTBF \| Recovery % | <0.1% \| >720h \| >95% |
| **Availability** | Redundancy \| Failover | Uptime % \| MTTR \| RTO/RPO | ≥99.9% \| <30min \| <1h |
| **Scalability** | Scaling strategy \| Sharding | Scalability factor \| Linear % | 10x \| >80% |
| **Decentralization** | Topology \| Consensus flow | Nakamoto coefficient \| Validators | >7 \| >100 |
| **Trust** | BFT model \| Incentive structure | Byzantine % \| Crypto strength | <33% \| 256-bit min |
| **Transparency** | Audit trail \| Verification flow | Audit % \| Verifiability % | 100% \| >95% |
| **Maintainability** | Clean arch layers \| Dependency graph | Cyclomatic complexity \| Debt % | Mean <10 \| <15% |
| **Observability** | Tracing \| Metric topology | Coverage % \| MTTD \| SNR | >90% \| <5min \| >80% |

## Requirement Patterns

**FR**: User Story "As [role], I want [feature] so that [benefit]" | Acceptance "Given [context] When [action] Then [outcome]" | Edge Cases: Happy path + ≥3 errors  
**NFR**: Performance "[Metric] [op] [threshold] @ [load] with [resources]" | Security "[Control] SHALL [action] to prevent [threat]" | Availability "[Service] SHALL maintain [uptime %] with [redundancy]"  
**Constraints**: Regulatory "MUST comply with [regulation] [section] by [date]" | Integration "SHALL integrate via [protocol] with [system] using [format]" | Technology "SHALL use [tech] [version] due to [rationale]"

---

# Generation Process

## 1. Plan Structure

**Actions**: Select 10-12 clusters (8 phases × 6 viewpoints) → Allocate 30-35 Q&As (5/15/14) → Verify MECE  
**Checks**: 30-35 total | 15/45/40% F/I/A (±5%) | All 8 phases | All 6 viewpoints | ≥5 quality perspectives | No overlap

## 2. Build References

**Actions**: Glossary (≥25 terms + relationships) | Tools (≥10: URL, update ≤18mo, pricing, adoption) | Literature (≥12 + relevance) | Citations (≥12 APA 7th)  
**Checks**: G≥25, T≥10, L≥12, C≥12 | 60/30/10% EN/ZH/Other (±10%) | ≥50% <3yr | ≥3 types, <25% single | 100% valid URLs

## 3. Write Q&As

**Questions**: ≥70% scenario-based ("How/What/Compare") | Avoid pure recall unless foundational  
**Each Answer**: 150-350 words | ≥1 citation (≥2 advanced) | Viewpoint → Technique → Stakeholders → NFR → Trade-offs → Validation | Quantified NFRs | ≥2 alternatives + table | Assumptions/limitations  
**Validate/5**: Word count | Citations | Technique clarity | Traceability | Question type | Quantified NFRs

## 4. Create Artifacts

**Per Cluster**: Mermaid diagram (event storming/C4/BPMN) + Requirement template (FR/NFR/Constraint) + Comparison table (≥2: Technique/Stakeholders/Outputs/Use When) + Metric formula (formula + variables + target)  
**Checks**: All 4/4 | Diagrams render | Templates complete | Tables formatted | Formulas valid

## 5. Link References

**Actions**: Populate sections → Extract `[Ref: ID]` → Verify IDs exist → Remove orphans → Validate URLs  
**Checks**: G≥25, T≥10, L≥12, C≥12 | 100% `[Ref: ID]` resolved | 0 broken links | 60/30/10% EN/ZH/Other | No orphans

## 6. Validate (23 Checks)

| # | Check | Target | # | Check | Target |
|---|-------|--------|---|-------|--------|
| 1 | Counts | G≥25, T≥10, L≥12, C≥12, Q=30-35 | 13 | Artifacts | ≥90% clusters 4/4 |
| 2 | Citations | ≥70% ≥1; ≥30% ≥2 | 14 | Techniques | ≥80% elicitation |
| 3 | Language | 60/30/10% EN/ZH/Other | 15 | Metrics | ≥60% formulas |
| 4 | Recency | ≥50% <3yr | 16 | Templates | ≥80% examples |
| 5 | Diversity | ≥3 types; <25% single | 17 | Syntax | 100% valid |
| 6 | Links | 100% valid | 18 | Formulas | 100% valid |
| 7 | Cross-refs | 100% resolved | 19 | Lifecycle | All 8 phases |
| 8 | Word count | Sample 5: 150-350 | 20 | Viewpoints | All 6 viewpoints |
| 9 | NFRs | 100% quantified | 21 | Quality | ≥5/10 perspectives |
| 10 | Per-topic | ≥2 sources + ≥1 tool | 22 | Stakeholders | ≥8/10 roles |
| 11 | Traceability | ≥80% req→criteria | 23 | Review | 6/6 criteria (§7) |
| 12 | Question type | ≥70% scenario | | | |

**Failure**: ANY fail → STOP → Document → Fix → Re-validate ALL → Iterate → 23/23 PASS

## 7. Final Review

**6 Criteria (All PASS)**: Clarity (logical structure, consistent terms, inline definitions) | Accuracy (verifiable facts, valid techniques, sound metrics) | Completeness (8 phases × 6 viewpoints, minimums met, 23/23 PASS) | Balance (≥2 approaches + table, assumptions/limitations, tagged consensus) | Practicality (actionable guidance, measurable NFRs, testable criteria) | Self-Correction (no redundancy/inconsistencies/gaps/orphans)  
**Submit**: 23/23 PASS + 6/6 criteria  
**High-Risk**: NFR quantification | URLs | Cross-refs `[Ref: ID]`

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Phase × Viewpoint | Range | Count | Difficulty |
| [Title] | [Phase] × [Viewpoint] | Q1-Q4 | 4 | 1F/2I/1A |
[10-12 clusters, 30-35 total, 15/45/40% F/I/A]

---

## Topic 1: [Title - Phase × Viewpoint]
**Overview**: [1-2 sentences: phase, viewpoint, quality perspectives]

### Q1: [How/What/Compare scenario question]
**[F/I/A]** | **Phase**: [Phase] | **Viewpoint**: [Viewpoint] | **Quality**: [Perspectives]  
**Key**: [Technique + quantified NFR threshold]

**Answer** [150-350w]: Context → Technique → Stakeholders (≥2) → NFR (quantified) → Trade-offs → Validation [≥1 [Ref: C1]]

**Elicitation**: [Technique description]

**Stakeholders**: | Role | Concerns | Input | [BA/PM/Arch/etc]

**Template** (per cluster):
```gherkin
As [role] I want [feature] So that [benefit]
[Metric] SHALL [op] [threshold] @ [load] with [resources]
Given [context] When [action] Then [outcome] And [measurable]
```

**Diagram** (per cluster): ```mermaid [Event storming/C4/BPMN/Sequence/ERD] ```

**NFR Metrics**: | Quality | Metric | Formula | Target |

**Trade-offs** (≥2): | Approach | Stakeholders | Outputs | Effort | Use When | Tag |

---

## References

### Glossary (≥25)
**G1. [Term]** [EN/ZH/Other]: [Definition]. **Related**: [Terms]

### Tools (≥10)
**T1. [Tool]** [Tag]: [Purpose]. **Updated**: [YYYY-MM] | **Pricing**: [Type] | **Adoption**: [Metrics] | **URL**: [Link]

### Literature (≥12)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag]: [Relevance to requirement analysis]

### Citations (≥12, APA 7th, 60/30/10%)
**C1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report
| # | Check | Target | Result | Status | [23 rows - see §6]
| 1 | Counts | G≥25, T≥10, L≥12, C≥12, Q=30-35 | G:X, T:Y... | PASS/FAIL |

**Overall**: [X/23 PASS - need 23/23] | **Issues**: [Failures] | **Remediation**: [Actions]
```

---

# Reference Examples

## Glossary

**G1. INVEST** [EN]: Independent, Negotiable, Valuable, Estimable, Small, Testable user story quality  
**G2. NFR** [EN]: Non-Functional Requirements (performance, security, reliability, scalability)  
**G3. DOR** [EN]: Definition of Ready checklist (criteria, dependencies, sizing)  
**G4. Event Storming** [EN]: Collaborative domain modeling via events/commands/aggregates. **Related**: DDD  
**G5. STRIDE** [EN]: Threat model (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation)  
**G6. C4 Model** [EN]: Architecture diagrams L1-L4 (Context, Container, Component, Code)  
**G7. Bounded Context** [EN]: DDD model boundary with ubiquitous language. **Related**: Context Map  
**G8. ADR** [EN]: Architecture Decision Record (context, options, consequences)  
**G9. SLO** [EN]: Service Level Objective (e.g., 99.9% availability). Drives error budget  
**G10. MTTR** [EN]: Mean Time To Repair. Target: <30min SEV-1  
**G11. RTO/RPO** [EN]: Recovery Time/Point Objective (max downtime/data loss)  
**G12. BFT** [EN]: Byzantine Fault Tolerance (<33% malicious). **Related**: PBFT  
**G13. Nakamoto Coefficient** [EN]: Min entities to disrupt (>50% stake/hash). Target: >7  
**G14. CVSS** [EN]: Vulnerability severity 0.0-10.0 (Low/Med/High/Critical)  
**G15. Cyclomatic Complexity** [EN]: Code complexity via paths. Target: mean <10  
**G16. Technical Debt** [EN]: Shortcuts impeding work. Target: <15% codebase  
**G17. RACI** [EN]: Responsible, Accountable, Consulted, Informed ownership  
**G18. Context Map** [EN]: DDD context relationships (shared kernel, customer/supplier)  
**G19. Quality Attribute Scenario** [EN]: NFR test (stimulus → artifact → env → response → measure)  
**G20. DORA Metrics** [EN]: Deployment freq, lead time, change failure, MTTR. Elite: daily, <1d, <15%, <1h  
**G21. Conway's Law** [EN]: System structure mirrors org communication  
**G22. Gherkin** [EN]: BDD Given/When/Then. Tools: Cucumber, SpecFlow  
**G23. Event Sourcing** [EN]: State as event log. Enables audit, temporal queries. Pairs with CQRS  
**G24. CQRS** [EN]: Separate write/read models. +Scalability, +Complexity  
**G25. Zero-Trust** [EN]: "Never trust, always verify". **Related**: Defense-in-Depth  
**G26. Ubiquitous Language** [EN]: Shared domain vocabulary (business + technical)  
**G27. Aggregate** [EN]: Consistency boundary (root + entities/VOs). **Related**: Repository  
**G28. PRD** [EN]: Product Requirements Document (goals, features, metrics, constraints)  
**G29. Traceability Matrix** [EN]: Links requirements → design → code → tests  
**G30. Fit Criteria** [EN]: Measurable acceptance thresholds (Volere template)

## Tools

**T1. Mermaid** [EN]: Text diagrams (flowchart, sequence, C4, ERD) | 2024-10 | Free/OSS | https://mermaid.js.org  
**T2. EventStorming** [EN]: Collaborative modeling workshops (post-it, DDD) | Free | https://www.eventstorming.com  
**T3. Strategyzer** [EN]: Value proposition, BMC design | 2024-09 | Freemium | https://www.strategyzer.com  
**T4. OpenAPI** [EN]: REST API spec, codegen, contract testing | 2024-11 | Free/OSS | https://www.openapis.org  
**T5. Cucumber** [EN]: BDD Given/When/Then framework | 2024-10 | Free/OSS | https://cucumber.io  
**T6. Jira/Confluence** [EN]: Requirement tracking, traceability | 2024-11 | Paid | 100K+ orgs | https://www.atlassian.com  
**T7. draw.io** [EN]: C4, UML, BPMN, flowcharts | 2024-10 | Free/OSS | https://www.diagrams.net  
**T8. OWASP Threat Dragon** [EN]: STRIDE threat modeling | 2024-08 | Free/OSS | https://owasp.org/www-project-threat-dragon  
**T9. ArchUnit** [EN]: Architecture fitness (Java/Kotlin) | 2024-09 | Free/OSS | https://www.archunit.org  
**T10. SonarQube** [EN]: Code quality, tech debt, security | 2024-11 | Freemium | 400K+ | https://www.sonarqube.org  
**T11. Prometheus** [EN]: Metrics, alerting (CNCF) | 2024-10 | Free/OSS | https://prometheus.io  
**T12. Grafana** [EN]: Dashboards, multi-source viz | 2024-11 | Freemium | 10M+ | https://grafana.com

## Literature

**L1. Wiegers & Beatty (2013). *Software Requirements* (3rd). Microsoft Press** [EN]: Elicitation, NFR spec, traceability, validation  
**L2. Leffingwell & Widrig (2003). *Managing Software Requirements*. Addison-Wesley** [EN]: Management, change control, traceability  
**L3. Evans (2003). *Domain-Driven Design*. Addison-Wesley** [EN]: Domain modeling, ubiquitous language, bounded contexts  
**L4. Bass et al. (2021). *Software Architecture in Practice* (4th). Addison-Wesley** [EN]: NFR scenarios, QAW, ATAM  
**L5. Osterwalder & Pigneur (2010). *Business Model Generation*. Wiley** [EN]: BMC, value proposition, stakeholder mapping  
**L6. Robertson & Robertson (2012). *Mastering Requirements Process* (3rd). Addison-Wesley** [EN]: Volere, fit criteria, reuse  
**L7. Cohn (2004). *User Stories Applied*. Addison-Wesley** [EN]: INVEST, splitting, acceptance criteria, estimation  
**L8. Kim et al. (2016). *DevOps Handbook*. IT Revolution** [EN]: Deployment requirements, feature flags, observability  
**L9. Beyer et al. (2016). *Site Reliability Engineering*. O'Reilly** [EN]: SLO, error budgets, toil, capacity planning  
**L10. Shostack (2014). *Threat Modeling*. Wiley** [EN]: STRIDE, security requirements elicitation  
**L11. Kleppmann (2017). *Designing Data-Intensive Applications*. O'Reilly** [EN]: Data requirements, consistency, partitioning  
**L12. Vernon (2013). *Implementing DDD*. Addison-Wesley** [EN]: Context mapping, aggregates, event sourcing  
**L13. 张在旺 (2018). *软件需求工程* (第2版). 清华** [ZH]: Requirements engineering, Chinese practices  
**L14. Skelton & Pais (2019). *Team Topologies*. IT Revolution** [EN]: Org requirements, Conway's Law, interaction modes

## Citations

**C1.** Wiegers & Beatty (2013). *Software requirements* (3rd). Microsoft Press [EN]  
**C2.** Evans (2003). *Domain-driven design*. Addison-Wesley [EN]  
**C3.** Bass, Clements & Kazman (2021). *Software architecture in practice* (4th). Addison-Wesley [EN]  
**C4.** Osterwalder & Pigneur (2010). *Business model generation*. Wiley [EN]  
**C5.** Robertson & Robertson (2012). *Mastering requirements process* (3rd). Addison-Wesley [EN]  
**C6.** Cohn (2004). *User stories applied*. Addison-Wesley [EN]  
**C7.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly [EN]  
**C8.** Kleppmann (2017). *Designing data-intensive applications*. O'Reilly [EN]  
**C9.** Vernon (2013). *Implementing domain-driven design*. Addison-Wesley [EN]  
**C10.** Skelton & Pais (2019). *Team topologies*. IT Revolution [EN]  
**C11.** 张在旺 (2018). *软件需求工程* (第2版). 清华大学出版社 [ZH]  
**C12.** Shostack (2014). *Threat modeling: Designing for security*. Wiley [EN]

---
