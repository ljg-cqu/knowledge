# System Analysis Q&A Generator

Generate 30-35 system analysis Q&As covering 8 lifecycle phases × 5 viewpoints × 5 perspectives.

**Scope**: Production-grade systems (>10K rps, >1TB data, multi-team, distributed, regulated)  
**Output**: Q&As with multi-viewpoint analysis, quantified metrics, ≥2 alternatives, diagrams, citations  
**Success**: 24/24 validation PASS | All 10 stakeholder roles | All 8 phases × 5 viewpoints × 5 perspectives

---

# Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total Count** | 30-35 |
| **Difficulty Mix** | 20% Foundational (concepts) / 40% Intermediate (analysis) / 40% Advanced (synthesis) |
| **Answer Length** | 200-350 words (diagrams/tables excluded) |
| **Components** | Context → analysis framework → viewpoints → perspectives → metrics → trade-offs |
| **Citations** | ≥1 each; ≥2 for complex; ≥3 for regulatory/business |
| **Per Cluster** | Analysis framework diagram + viewpoint matrix + perspective metrics + comparison table |

## Coverage Framework

**8 Lifecycle Phases**: Requirements & Discovery | Architecture & Design | Development | Testing & Quality | Deployment & Release | Operations & Observability | Maintenance & Support | Evolution & Governance

**5 Viewpoints (MECE)**: Technical | Ecosystem | Business/Market | Regulatory/Compliance | Operational

**5 Perspectives**: Performance | Security | Reliability | Decentralization | Transparency

## Content Standards

**Flow**: Stakeholder needs → Viewpoints → Perspectives → Metrics → Recommendations  
**Coverage**: ≥3 viewpoints + ≥3 perspectives per Q&A  
**Quantification**: Concrete metrics required (✅ "5x velocity, +40-60% cost, +20-50ms latency" ❌ "enables scalability")  
**Context**: Team size (<10/10-50/>50) | Scale (<100/100-10K/>10K rps; <1TB/1-100TB/>100TB) | Lifecycle (greenfield/modernization/scaling/compliance) | Maturity (POC/MVP/production/mission-critical)  
**Stakeholders**: Primary + secondary specified (BA/PM/Arch/Dev/QA/DevOps/Security/Data/SRE/Leadership)  
**Balance**: ≥2 alternatives with matrix; assumptions/limitations/risks explicit; tag `[Consensus]`/`[Context-dependent]`/`[Emerging]`/`[Controversial]`  
**Precision**: Inline definitions; consistent taxonomy; evidence-based claims with citations

## Artifacts & Analysis Tools

**System Analysis Framework Mapping**:

| Lifecycle Phase | Primary Viewpoint | Key Diagrams | Analysis Tools | Metrics |
|-----------------|-------------------|--------------|----------------|---------|
| Requirements & Discovery | Business/Market | BMC, Value Proposition Canvas, User Journey, Event Storming | SWOT, Porter's Five Forces, Kano Model | Market size, User acquisition cost, Conversion rate |
| Architecture & Design | Technical | C4 (Context/Container/Component), Sequence, Deployment, ERD | ADR, ATAM, STRIDE, Quality Attribute Scenarios | Performance budgets, Cost estimates, CVSS scores |
| Development | Technical/Operational | Component, Class, Data Flow, Git branching | Code quality tools, SAST, Dependency analysis | Cyclomatic complexity, Coverage, Tech debt ratio |
| Testing & Quality | Technical/Operational | Test pyramid, Behavior flow, Performance profile | Test strategy matrix, Risk-based testing | Pass rate, Coverage, Defect density, p95 latency |
| Deployment & Release | Operational | Deployment pipeline, Environment topology, Rollback plan | Blue/green, Canary, Feature flags | DORA metrics, MTTR, Change failure rate |
| Operations & Observability | Operational/Technical | SLO dashboard, Tracing, Alert topology, Capacity plan | Prometheus, Grafana, Distributed tracing | SLO %, Error budget, MTTD, MTTR |
| Maintenance & Support | Operational/Regulatory | Vulnerability timeline, Patch management, Incident retrospective | CVE tracking, License compliance, Change log | Vuln SLA, Dependency age, Incident frequency |
| Evolution & Governance | Business/Regulatory | Migration roadmap, Tech debt register, Compliance matrix | RFC process, CAB, Tech radar, Fitness functions | Debt %, Migration risk score, Compliance % |

**Cross-Cutting Analysis** (Ecosystem/Business/Regulatory):

| Viewpoint | Diagrams | Frameworks | Metrics |
|-----------|----------|------------|---------|
| Ecosystem | Integration/Dependency/Network maps | Platform, API-first, Standards | Integration count, API latency, Adoption % |
| Business/Market | BMC, Lean Canvas, Positioning | Blue Ocean, Disruptive Innovation, Land/Expand | Revenue, CAC, LTV, Market share, Growth |
| Regulatory | Data flow, Consent, Audit trail | GDPR matrix, SOC 2, Industry regs | Compliance score, Audit findings, Breach risk |

**Perspective Metrics** (Formula | Target):

- **Performance**: `Latency_p95 = percentile(duration, 0.95)` <300ms | `Throughput = requests/time` ≥10K rps | `Resource_Efficiency = throughput/(CPU+Mem+Net)` maximize
- **Security**: `CVSS_Score = Base×Temporal×Environmental` <7.0 | `Attack_Surface = Endpoints+AuthBoundaries` minimize | `MTTR_Security = PatchTime` ≤7d
- **Reliability**: `Availability = Uptime/(Uptime+Downtime)×100%` ≥99.9% | `MTTR = Downtime/Incidents` ≤30min | `Durability = 1-(Lost/Total)` ≥11-9s
- **Decentralization**: `Nakamoto_Coef = min(n) controls >50%` ≥7 | `Trust = HonestNodes/Total` ≤33% | `Censorship_Resistance = 1-CentralPoints` >90%
- **Transparency**: `Audit_Coverage = Auditable/Total×100%` ≥95% | `Observability = (Metrics+Logs+Traces)/3` ≥80% | `Lineage = Traced/Total` ≥90%

**Format**: Mermaid diagrams (<120 nodes) | Quantitative tables with "Use When"/"Stakeholder Impact" | Formulas with targets | Framework name + application context

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥25 | Multi-domain terms (Technical 30%, Business 25%, Ecosystem 15%, Regulatory 15%, Operational 15%) with relationships |
| **Tools** | ≥12 | ≥2 per viewpoint category (Technical/Business/Ecosystem/Regulatory/Operational); URL valid, update ≤18mo, pricing, adoption |
| **Frameworks** | ≥8 | Analysis frameworks across viewpoints (SWOT, BMC, STRIDE, ATAM, Porter's, Blue Ocean, DORA, etc.) |
| **Literature** | ≥12 | Multi-domain coverage: Technical (Evans, Fowler, Richardson, Kleppmann), Business (Osterwalder, Kim/Mauborgne, Christensen), Regulatory (GDPR guides, SOC 2), Operational (Forsgren, Beyer) |
| **Citations** | ≥20 | APA 7th, 60% [EN] / 30% [ZH] / 10% other (±10%); ≥30% business/regulatory |

**Quality**: ≥50% last 3yr | ≥70% modern systems | ≥5 types (books/papers/standards/frameworks/reports) | <20% single source | ≥40% non-technical | All viewpoints/perspectives/phases covered | 100% valid links

---

# Generation Process

## 1. Plan Structure

Select 7-8 topic clusters (4-5 Q&As each, 30-35 total) covering all 8 phases. Assign difficulty (1F/2I/2A per cluster = 20/40/40% overall). Map primary/secondary stakeholders per Q&A.

**Verify**: 30-35 Q&As | 20/40/40% F/I/A (±5%) | All 8 phases (≥3 Q&As major) | All 5 viewpoints (≥20% each) | All 5 perspectives (≥60% Q&As cover ≥3) | All 10 stakeholders (≥2 Q&As per role as primary) | No gaps/redundancy

## 2. Build References

Create: Glossary ≥25 (Tech 30%, Biz 25%, Eco 15%, Reg 15%, Ops 15%, with relationships) | Tools ≥12 (≥2/viewpoint, URL/date/pricing/adoption) | Frameworks ≥8 (SWOT/BMC/STRIDE/ATAM/Porter's/Blue Ocean/DORA) | Literature ≥12 (multi-domain) | Citations ≥20 (APA 7th, 60/30/10% EN/ZH/Other, ≥30% biz/reg)

**Verify**: G≥25, T≥12, F≥8, L≥12, A≥20 | 60/30/10% lang (±10%) | All 5 viewpoints | ≥50% last 3yr, ≥70% modern, ≥30% biz/market | ≥5 types, <20% single source, ≥40% non-tech | 100% valid URLs

## 3. Write Q&As

**Structure** (≥70% analysis-based): Lifecycle phase + stakeholder(s) + viewpoint(s) + perspective(s) context

**Each Answer** (200-350 words): Context (needs/phase/system) → Framework (which viewpoints & why) → Multi-viewpoint assessment (≥3 of: Technical/Business/Ecosystem/Regulatory/Operational with quantified metrics) → Multi-perspective evaluation (≥3 of: Performance/Security/Reliability/Decentralization/Transparency) → Comparison matrix (≥2 alternatives: Approach/Technical/Business/Regulatory/Operational/Use When/Stakeholder Impact) → Recommendations (context-specific, thresholds, criteria) → Risks/Limitations (assumptions/trade-offs/boundaries) → Citations (≥1 foundational, ≥2 intermediate, ≥3 advanced/biz/reg)

**Validate Every 5**: 200-350 words | ≥3 viewpoints | ≥3 perspectives with metrics | Primary+secondary stakeholders | Citations formatted | Comparison table ≥2 alternatives | Quantified insights

## 4. Create Artifacts

**Per Cluster** (4/4 required): Framework diagram (Mermaid <120 nodes, matches phase/viewpoint: BMC/C4/Data flow/Integration map) | Viewpoint matrix (Technical/Ecosystem/Business/Regulatory/Operational columns) | Perspective metrics (≥3: metric/formula/variables/baseline/target/measurement) | Comparison matrix (≥2 alternatives: Approach/Technical/Business/Regulatory/Operational/Use When/Stakeholder Impact)

**Verify**: All clusters 4/4 artifacts | Diagrams render | Tables formatted | Metrics complete | Stakeholder impact included | All linked to Q&As

## 5. Link References

Populate all sections (G/T/F/L/A). Extract all `[Ref: ID]` from Q&As. Verify 100% exist. Remove orphans. Validate all URLs.

**Verify**: G≥25, T≥12, F≥8, L≥12, A≥20 | 100% `[Ref: ID]` resolved | 0 broken URLs | 60/30/10% lang (±10%) | All 5 viewpoints | No orphans

## 6. Validate (24 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥25, T≥12, F≥8, L≥12, A≥20, Q=30-35 (20/40/40%) |
| 2 | Citations | ≥70% Q&As ≥1; ≥40% ≥2; ≥20% ≥3 |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 4 | Recency | ≥50% last 3yr; ≥70% modern; ≥30% business |
| 5 | Diversity | ≥5 types; <20% single; ≥40% non-technical |
| 6 | Links | 100% valid URLs |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 200-350 |
| 9 | Insights | 100% quantified (no generic claims) |
| 10 | Lifecycle coverage | All 8 phases (≥3 Q&As major phases) |
| 11 | Viewpoint coverage | All 5 viewpoints (≥20% each) |
| 12 | Perspective coverage | All 5 perspectives; ≥60% Q&As cover ≥3 |
| 13 | Stakeholder coverage | All 10 roles (≥2 Q&As per role as primary) |
| 14 | Multi-viewpoint | ≥80% Q&As cover ≥3 viewpoints |
| 15 | Multi-perspective | ≥60% Q&As evaluate ≥3 perspectives with metrics |
| 16 | Question type | ≥70% analysis-based |
| 17 | Artifacts | 100% clusters have 4/4 artifacts |
| 18 | Viewpoint matrix | ≥90% have multi-viewpoint assessment |
| 19 | Perspective metrics | ≥80% have ≥3 perspective metrics with formulas |
| 20 | Comparison matrix | 100% have ≥2 alternatives with stakeholder impact |
| 21 | Stakeholder specified | 100% specify primary + secondary stakeholders |
| 22 | Domain coverage | All viewpoints in references; all perspectives addressed |
| 23 | Framework usage | ≥70% Q&As apply analysis frameworks |
| 24 | Review | 6/6 criteria (see §7) |

**Protocol**: ANY fail → STOP → Fix → Re-validate ALL 24 → Iterate until 24/24 PASS

## 7. Final Review (6/6 Required)

1. **Clarity**: Logical structure | Consistent multi-domain terminology | Inline definitions | Clear stakeholder context
2. **Accuracy**: Verifiable facts with citations | Diagrams render | Valid formulas | Correct framework applications
3. **Completeness**: All 8 phases + 5 viewpoints + 5 perspectives + 10 stakeholders | G≥25, T≥12, F≥8, L≥12, A≥20, Q=30-35 | 24/24 PASS
4. **Balance**: ≥3 viewpoints/perspectives per Q&A | ≥2 alternatives + stakeholder impact | Explicit assumptions/limitations/risks | Tagged consensus
5. **Practicality**: Actionable guidance | Stakeholder-specific recommendations | Measurable outcomes with thresholds | Context-specific criteria
6. **Rigor**: Multi-domain integration | Quantified trade-offs across viewpoints | Explicit boundaries | Stakeholder impact assessment

**Submit When**: 24/24 PASS + 6/6 criteria | **High-Risk**: Multi-domain coverage | Stakeholder specification | Metrics validity | URLs | Cross-refs | Framework usage

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Lifecycle Phase | Viewpoint(s) | Perspective(s) | Range | Count | Difficulty |
| [Title] | [Phase] | [Primary + Secondary] | [≥3 Perspectives] | Q1-Q4 | 4 | 1F/1I/2A |
[7-8 clusters, 30-35 total, all 8 phases, all 5 viewpoints, all 5 perspectives, 20/40/40% F/I/A]

---

## Topic 1: [Title] – [Lifecycle Phase]
**Overview**: [1-2 sentences describing analysis scope, primary stakeholder, and key perspectives]

**Stakeholder Focus**: Primary: [Role] | Secondary: [Roles consulted]

### Q1: [Analysis-based question with multi-viewpoint context]
**Difficulty**: [F/I/A] | **Phase**: [Lifecycle] | **Stakeholder**: [Primary Role]

**Key Insight**: [Multi-viewpoint quantified insight in one sentence]

**Answer** (200-350 words):

**Context**: [Needs/system/phase constraints]

**Framework**: [Which & why – STRIDE/BMC/ATAM/etc.]

**Viewpoint Assessment** (≥3):
- **Technical**: [Arch/impl/infra + metrics]
- **Business**: [Value/cost/ROI + metrics] (when relevant)
- **Ecosystem**: [Integration/deps/standards + metrics] (when relevant)
- **Regulatory**: [Compliance/audit + scores] (when relevant)
- **Operational**: [Deploy/monitor + SLO/MTTR]

**Perspective Evaluation** (≥3): [Quantified metrics for Performance/Security/Reliability/Decentralization/Transparency]

**Recommendations**: [Context-specific guidance + thresholds + criteria]

**Risks**: [Assumptions/trade-offs/boundaries]

[Citations: ≥1 foundational, ≥2 intermediate, ≥3 advanced/biz/reg]

**Analysis Framework Diagram**:
```mermaid
[Framework visualization: BMC, C4, Data Flow, Integration Map, etc., <120 nodes]
```

**Viewpoint Matrix**:
| Viewpoint | Assessment | Key Metrics | Stakeholder Impact |
| Technical | [Analysis] | [Metrics] | [Impact] |
| Business | [Analysis] | [Metrics] | [Impact] |
| Ecosystem | [Analysis] | [Metrics] | [Impact] |
| Regulatory | [Analysis] | [Metrics] | [Impact] |
| Operational | [Analysis] | [Metrics] | [Impact] |

**Perspective Metrics** (≥3):
| Perspective | Metric | Formula | Variables | Baseline | Target | Measurement Method |
| [Type] | [Name] | [Formula] | [Defs] | [Current] | [Goal] | [How to measure] |

**Comparison Matrix** (≥2 alternatives):
| Approach | Technical | Business | Regulatory | Operational | Use When | Stakeholder Impact |
| [Option 1] | [Pros/Cons] | [ROI/Cost] | [Compliance] | [SLO/MTTR] | [Context] | [Who benefits/affected] |
| [Option 2] | [Pros/Cons] | [ROI/Cost] | [Compliance] | [SLO/MTTR] | [Context] | [Who benefits/affected] |

---

## References

### Glossary (≥25, Multi-Domain)
**G1. [Term]** [EN/ZH/Other] – [Viewpoint: Technical/Business/Ecosystem/Regulatory/Operational]  
[Definition]. **Related**: [Terms]. **Used in**: [Lifecycle phases]

### Tools (≥12, All Viewpoints)
**T1. [Tool]** [Tag] – [Viewpoint]  
**Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Frameworks (≥8, Analysis Methods)
**F1. [Framework Name]** [Tag] – [Viewpoint]  
**Purpose**: [When to use]. **Key Elements**: [Components]. **Output**: [What it produces]. **Source**: [Official URL]

### Literature (≥12, Multi-Domain)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – [Domain: Technical/Business/Regulatory/Operational]  
**Relevance**: [Why]. **Key Concepts**: [Main ideas]

### Citations (≥20, APA 7th, 60/30/10%, ≥30% business/regulatory)
**A1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report
| # | Check | Target | Result | Status |
| 1 | Counts | G≥25, T≥12, F≥8, L≥12, A≥20, Q=30-35 | G:X, T:Y, F:Z... | PASS/FAIL |
| 2 | Citations | ≥70% ≥1; ≥40% ≥2; ≥20% ≥3 | X% / Y% / Z% | PASS/FAIL |
[All 24 checks]

**Overall**: [X/24 PASS - need 24/24]  
**Issues**: [List all failures]  
**Remediation**: [Specific actions to fix each failure]

**Coverage Summary**:
- Lifecycle phases: [8/8 covered]
- Viewpoints: Technical X%, Business Y%, Ecosystem Z%, Regulatory W%, Operational V%
- Perspectives: Performance X%, Security Y%, Reliability Z%, Decentralization W%, Transparency V%
- Stakeholders: [10/10 roles with ≥2 Q&As each as primary]
```

# Reference Examples

## Glossary (Multi-Domain: Technical 30%, Business 25%, Ecosystem 15%, Regulatory 15%, Operational 15%)

**Technical (30%)**:  
**G1. Hexagonal Architecture** [EN] – Technical – Isolates core via ports/adapters. Enables testability, tech independence. Related: DI, Clean Architecture. Used in: Architecture & Design  
**G2. CQRS** [EN] – Technical – Separates commands (writes) from queries (reads). Optimizes scalability. Related: Event Sourcing. Used in: Architecture & Design, Performance  
**G3. Event Sourcing** [EN] – Technical – Stores state as event log. Enables audit, temporal queries. Related: CQRS. Used in: Data, Regulatory  
**G4. Circuit Breaker** [EN] – Technical – Prevents cascading failures. Opens on error threshold. Related: Bulkhead. Used in: Reliability, Operations  
**G5. Service Mesh** [EN] – Technical – Infrastructure layer for service-to-service communication (Istio, Linkerd). Related: Microservices. Used in: Architecture, Security  
**G6. Blue/Green Deployment** [EN] – Technical/Operational – Zero-downtime deployment via parallel environments. Related: Canary. Used in: Deployment & Release  
**G7. Observability** [EN] – Technical/Operational – Ability to understand internal state from external outputs (metrics, logs, traces). Related: Monitoring. Used in: Operations  

**Business (25%)**:  
**G8. Business Model Canvas (BMC)** [EN] – Business – 9-block framework for business model design. Related: Value Proposition Canvas. Used in: Requirements & Discovery  
**G9. Value Proposition** [EN] – Business – Products/services solving customer problems/needs. Related: BMC. Used in: Requirements  
**G10. Customer Acquisition Cost (CAC)** [EN] – Business – Total cost to acquire a customer. Formula: Marketing + Sales / New Customers. Related: LTV. Used in: Business analysis  
**G11. Lifetime Value (LTV)** [EN] – Business – Total revenue from a customer over their lifetime. Related: CAC, LTV:CAC ratio >3:1 healthy. Used in: Business metrics  
**G12. Blue Ocean Strategy** [EN] – Business – Creating uncontested market space vs competing in red ocean. Related: Value Innovation. Used in: Market analysis  
**G13. Network Effects** [EN] – Business/Ecosystem – Value increases with more users (Metcalfe's Law). Related: Platform. Used in: Ecosystem, Market  

**Ecosystem (15%)**:  
**G14. API-First** [EN] – Ecosystem – Design APIs before implementation. Related: Contract-First. Used in: Integration, Architecture  
**G15. Platform Strategy** [EN] – Ecosystem/Business – Multi-sided platform connecting producers/consumers. Related: Network Effects. Used in: Ecosystem, Business  
**G16. Interoperability** [EN] – Ecosystem – Ability of systems to exchange and use data. Related: Standards, APIs. Used in: Integration  
**G17. Vendor Lock-in** [EN] – Ecosystem – Dependence on vendor making switching costly. Related: Multi-cloud, Standards. Used in: Risk, Ecosystem  

**Regulatory (15%)**:  
**G18. GDPR** [EN] – Regulatory – EU General Data Protection Regulation. Related: PII, Consent, Right to Erasure. Used in: Requirements, Compliance  
**G19. PII (Personally Identifiable Information)** [EN] – Regulatory – Data identifying an individual. Related: GDPR, Data Classification. Used in: Security, Compliance  
**G20. Audit Trail** [EN] – Regulatory/Operational – Chronological record of system activities. Related: Compliance, Observability. Used in: Regulatory, Security  
**G21. SOC 2** [EN] – Regulatory – Security/availability audit framework. Related: Compliance, Trust. Used in: Security, Governance  

**Operational (15%)**:  
**G22. SLO (Service Level Objective)** [EN] – Operational – Target for SLI (e.g., 99.9% availability). Related: SLA, Error Budget. Used in: Operations, Testing  
**G23. MTTR (Mean Time To Recovery)** [EN] – Operational – Average time to restore service after incident. Related: MTTD, Availability. Used in: Operations, Reliability  
**G24. DORA Metrics** [EN] – Operational – Four key metrics: deployment frequency, lead time, change failure rate, MTTR. Related: DevOps. Used in: Operations, Evolution  
**G25. Technical Debt** [EN] – Technical/Operational – Cost of rework from quick solutions vs better approaches. Related: Tech Debt Ratio. Used in: Maintenance, Evolution

## Tools (≥2 per viewpoint: Technical/Business/Ecosystem/Regulatory/Operational)

**Technical**:  
**T1. Mermaid** [EN] – Technical – Text-based diagrams (flowchart, sequence, C4, ER). GitHub-native. Updated: 2024-10. Pricing: Free/OSS. Adoption: GitHub official. https://mermaid.js.org  
**T2. Kubernetes** [EN] – Technical – Container orchestration. Declarative YAML. Updated: 2024-11. Pricing: Free/OSS. Adoption: CNCF graduated, 50K+ stars. https://kubernetes.io  
**T3. Terraform** [EN] – Technical/Operational – Infrastructure as Code. Multi-cloud. Updated: 2024-10. Pricing: Free/Enterprise. Adoption: HashiCorp, 40K+ stars. https://www.terraform.io  

**Business**:  
**T4. Strategyzer** [EN] – Business – BMC, Value Proposition Canvas digital tool. Updated: 2024-09. Pricing: Freemium/$49/mo. Adoption: 2M+ users. https://www.strategyzer.com  
**T5. Google Analytics** [EN] – Business – Web analytics, user metrics, conversion tracking. Updated: 2024-11. Pricing: Free/360. Adoption: 30M+ sites. https://analytics.google.com  

**Ecosystem**:  
**T6. OpenAPI** [EN] – Ecosystem – REST API spec. Codegen, contract testing. Updated: 2024-09. Pricing: Free/OSS. Adoption: OAI standard, 20K+ stars. https://www.openapis.org  
**T7. AsyncAPI** [EN] – Ecosystem – Event-driven API spec. Updated: 2024-10. Pricing: Free/OSS. Adoption: Linux Foundation, 3K+ stars. https://www.asyncapi.com  

**Regulatory**:  
**T8. OneTrust** [EN] – Regulatory – Privacy/compliance automation (GDPR, CCPA). Updated: 2024-10. Pricing: Enterprise. Adoption: 12K+ customers. https://www.onetrust.com  
**T9. Vanta** [EN] – Regulatory – SOC 2, ISO 27001 compliance automation. Updated: 2024-11. Pricing: $3K+/yr. Adoption: 5K+ customers. https://www.vanta.com  

**Operational**:  
**T10. Prometheus** [EN] – Operational – Metrics collection, time-series DB. Updated: 2024-10. Pricing: Free/OSS. Adoption: CNCF graduated, 50K+ stars. https://prometheus.io  
**T11. Grafana** [EN] – Operational – Observability dashboards, alerting. Updated: 2024-11. Pricing: Free/Cloud/Enterprise. Adoption: 1M+ active installs. https://grafana.com  
**T12. PagerDuty** [EN] – Operational – Incident response, on-call management. Updated: 2024-11. Pricing: $21+/user/mo. Adoption: 19K+ customers. https://www.pagerduty.com

## Frameworks (≥8, Analysis Methods Across Viewpoints)

**Business Analysis**:  
**F1. Business Model Canvas (BMC)** [EN] – Business – Purpose: Visualize business model in 9 blocks. Key Elements: Value Proposition, Customer Segments, Channels, Revenue Streams, Cost Structure, Key Resources, Activities, Partnerships. Output: One-page business model. Source: https://www.strategyzer.com/library/the-business-model-canvas  
**F2. SWOT Analysis** [EN] – Business – Purpose: Strategic planning via Strengths/Weaknesses/Opportunities/Threats. Output: 2×2 matrix. Source: Albert Humphrey, Stanford (1960s)  
**F3. Porter's Five Forces** [EN] – Business – Purpose: Industry competitiveness analysis. Key Elements: Competitive Rivalry, Supplier Power, Buyer Power, Threat of Substitution, Threat of New Entry. Output: Industry attractiveness assessment. Source: Porter, M. (1979). Harvard Business Review  

**Technical Analysis**:  
**F4. ATAM (Architecture Tradeoff Analysis Method)** [EN] – Technical – Purpose: Evaluate architecture quality attributes. Key Elements: Scenarios, Quality Attributes, Tradeoffs, Risks. Output: Architecture evaluation report. Source: SEI CMU https://insights.sei.cmu.edu/library/atam-method-for-architecture-evaluation/  
**F5. C4 Model** [EN] – Technical – Purpose: Software architecture diagrams at 4 levels. Key Elements: Context, Container, Component, Code. Output: Hierarchical architecture views. Source: Simon Brown https://c4model.com  

**Security/Regulatory Analysis**:  
**F6. STRIDE** [EN] – Security – Purpose: Threat modeling. Key Elements: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege. Output: Threat catalog with mitigations. Source: Microsoft SDL  

**Operational Analysis**:  
**F7. DORA Framework** [EN] – Operational – Purpose: Measure DevOps performance. Key Elements: Deployment Frequency, Lead Time, Change Failure Rate, MTTR. Output: Performance classification (Elite/High/Medium/Low). Source: Forsgren, N. et al. (2018). Accelerate  

**Market Analysis**:  
**F8. Blue Ocean Strategy** [EN] – Business/Market – Purpose: Create uncontested market space. Key Elements: Eliminate-Reduce-Raise-Create grid, Strategy Canvas. Output: Value innovation framework. Source: Kim, W. & Mauborgne, R. (2005). Blue Ocean Strategy

## Literature (Multi-Domain: Technical/Business/Regulatory/Operational)

**Technical**:  
**L1. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** [EN] – Technical – Relevance: Strategic/tactical modeling, ubiquitous language, bounded contexts. Key Concepts: Aggregates, Entities, Value Objects, Repositories  
**L2. Richardson, C. (2018). *Microservices Patterns*. Manning.** [EN] – Technical – Relevance: Decomposition, data, communication patterns with quantified trade-offs. Key Concepts: Saga, API Gateway, CQRS  
**L3. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.** [EN] – Technical – Relevance: Distributed systems: replication, partitioning, transactions, consistency. Key Concepts: CAP, Eventual Consistency  

**Business**:  
**L4. Osterwalder, A. & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** [EN] – Business – Relevance: BMC framework, value proposition design. Key Concepts: 9 building blocks, business model patterns  
**L5. Kim, W. & Mauborgne, R. (2015). *Blue Ocean Strategy* (Expanded). Harvard Business Review Press.** [EN] – Business – Relevance: Creating uncontested markets, value innovation. Key Concepts: Strategy Canvas, Four Actions Framework  
**L6. Christensen, C. (1997). *The Innovator's Dilemma*. Harvard Business Review Press.** [EN] – Business – Relevance: Disruptive innovation theory, market dynamics. Key Concepts: Sustaining vs Disruptive Innovation  

**Operational**:  
**L7. Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate*. IT Revolution.** [EN] – Operational – Relevance: DORA metrics, DevOps research. Key Concepts: Elite performers, deployment frequency, lead time  
**L8. Beyer, B. et al. (2016). *Site Reliability Engineering*. O'Reilly.** [EN] – Operational – Relevance: SLOs, error budgets, incident response. Key Concepts: Toil, SLI/SLO/SLA, Automation  
**L9. Skelton, M. & Pais, M. (2019). *Team Topologies*. IT Revolution.** [EN] – Operational/Technical – Relevance: Team structure, Conway's Law, cognitive load. Key Concepts: Stream-aligned, Platform, Enabling, Complicated Subsystem teams  

**Regulatory/Compliance**:  
**L10. GDPR Official Text. (2018). *General Data Protection Regulation*.** [EN] – Regulatory – Relevance: EU data protection law, compliance requirements. Key Concepts: Consent, Right to Erasure, Data Portability, DPO  
**L11. AICPA. (2021). *SOC 2 Trust Services Criteria*.** [EN] – Regulatory – Relevance: Security, availability, confidentiality audit framework. Key Concepts: Trust Service Principles, Controls  

**Cross-Domain**:  
**L12. Bass, L., Clements, P., & Kazman, R. (2021). *Software Architecture in Practice* (4th). Addison-Wesley.** [EN] – Technical/Operational – Relevance: Quality attributes, architecture evaluation, ATAM. Key Concepts: QAS, ADD, Architecture tactics

## Citations (≥20, APA 7th, 60/30/10% EN/ZH/Other, ≥30% Business/Regulatory)

**Technical (40%)**:  
**A1.** Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley. [EN]  
**A2.** Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning. [EN]  
**A3.** Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly. [EN]  
**A4.** Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley. [EN]  
**A5.** Newman, S. (2021). *Building microservices: Designing fine-grained systems* (2nd ed.). O'Reilly. [EN]  
**A6.** Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns: Designing, building, and deploying messaging solutions*. Addison-Wesley. [EN]  
**A7.** Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. [EN]  
**A8.** 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]

**Business/Market (30%)**:  
**A9.** Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]  
**A10.** Kim, W. C., & Mauborgne, R. (2015). *Blue Ocean Strategy: How to create uncontested market space and make the competition irrelevant* (Expanded ed.). Harvard Business Review Press. [EN]  
**A11.** Christensen, C. M. (1997). *The innovator's dilemma: When new technologies cause great firms to fail*. Harvard Business Review Press. [EN]  
**A12.** Porter, M. E. (1979). How competitive forces shape strategy. *Harvard Business Review*, 57(2), 137-145. [EN]  
**A13.** 陈春花. (2020). *价值共生*. 机械工业出版社. [ZH]  
**A14.** Maurya, A. (2012). *Running Lean: Iterate from Plan A to a plan that works* (2nd ed.). O'Reilly. [EN]

**Operational (20%)**:  
**A15.** Forsgren, N., Humble, J., & Kim, G. (2018). *Accelerate: The science of lean software and DevOps*. IT Revolution. [EN]  
**A16.** Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). *Site reliability engineering: How Google runs production systems*. O'Reilly. [EN]  
**A17.** Skelton, M., & Pais, M. (2019). *Team topologies: Organizing business and technology teams for fast flow*. IT Revolution. [EN]  
**A18.** Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps handbook: How to create world-class agility, reliability, and security in technology organizations*. IT Revolution. [EN]

**Regulatory/Compliance (10%)**:  
**A19.** European Parliament and Council. (2016). *Regulation (EU) 2016/679 (General Data Protection Regulation)*. Official Journal of the European Union. [EN]  
**A20.** AICPA. (2017). *SOC 2®: SOC for service organizations: Trust services criteria*. American Institute of CPAs. [EN]
