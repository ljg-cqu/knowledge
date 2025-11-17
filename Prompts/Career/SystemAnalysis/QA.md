# System Analysis Q&A Generator (Minimal Viable)

Generate **4-6 decision-critical system analysis Q&As** for informed decision-making with limited time.

**Scope**: Production-grade systems (>10K rps, >1TB data, multi-team, distributed, regulated)
**Output**: Decision-critical Q&As with multi-viewpoint analysis, quantified metrics, ≥2 alternatives, diagrams, citations
**Success**: 12/12 validation PASS | ≥5 core stakeholder roles | 4-5 decision-critical phases × viewpoints × perspectives
**Cadence**: Bi-weekly | Effort: 4-6 hours | Expires: 2 weeks from generation

---

# Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total Count** | **4-6** (60% reduction) |
| **Difficulty Mix** | 25% Foundational / 50% Intermediate / 25% Advanced |
| **Answer Length** | 150-250 words (diagrams/tables excluded) |
| **Components** | Context → analysis framework → ≥3 viewpoints → ≥3 perspectives → quantified metrics → trade-offs |
| **Citations** | ≥1 each; ≥2 for complex; ≥3 for regulatory/business |
| **Per Q&A** | Analysis framework diagram + viewpoint matrix + perspective metrics + comparison table |

## Coverage Framework (Decision-Critical Only)

**4-5 Lifecycle Phases** (decision-critical): Architecture & Design | Development | Deployment & Release | Operations & Observability | Evolution & Governance (skip Requirements, Testing, Maintenance unless decision-critical)

**5 Viewpoints (MECE)**: Technical | Ecosystem | Business/Market | Regulatory/Compliance | Operational

**5 Perspectives**: Performance | Security | Reliability | Decentralization | Transparency

## Decision Criticality Framework (NEW)

**Include if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts architecture go/no-go, infrastructure investment, or strategic pivot
- **Creates Risk**: Material threat (performance degradation, security breach, compliance violation, cost overrun >10%)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (Architect + DevOps, Dev + SRE, etc.)
- **Requires Action**: 1-6mo action window (not speculative)
- **Quantified Impact**: Latency ms, throughput rps, cost %, availability %, compliance score

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered

## Content Standards

**Flow**: Stakeholder needs → Viewpoints → Perspectives → Metrics → Recommendations
**Coverage**: ≥3 viewpoints + ≥3 perspectives per Q&A
**Quantification**: Concrete metrics required (✅ "5x velocity, +40-60% cost, +20-50ms latency" ❌ "enables scalability")
**Context**: Team size (<10/10-50/>50) | Scale (<100/100-10K/>10K rps; <1TB/1-100TB/>100TB) | Lifecycle (greenfield/modernization/scaling/compliance) | Maturity (POC/MVP/production/mission-critical)
**Stakeholders**: ≥5 core roles (Architect, Developer, DevOps/SRE, Security, Leadership)
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

## References (Proportional 60% Reduction)

| Component | Min | Requirements |
|-----------|-----|-------------|
| **Glossary** | ≥10 | Only terms used in Q&As (Technical 30%, Business 25%, Ecosystem 15%, Regulatory 15%, Operational 15%) |
| **Tools** | ≥6 | ≥1 per viewpoint category (Technical/Business/Ecosystem/Regulatory/Operational); URL valid, update ≤18mo |
| **Frameworks** | ≥5 | Decision-critical frameworks (STRIDE, ATAM, C4, DORA, Blue Ocean) |
| **Literature** | ≥6 | Canonical references only (Evans, Fowler, Forsgren, Osterwalder, Kim/Mauborgne, GDPR) |
| **Citations** | ≥8 | APA 7th, 60% [EN] / 30% [ZH] / 10% other (±10%); ≥30% business/regulatory |

**Quality**: ≥50% last 3yr | ≥70% modern systems | ≥4 types (books/papers/standards/frameworks) | <20% single source | ≥40% non-technical | All 4-5 decision-critical phases covered | 100% valid links

---

# Generation Process

## 1. Plan Structure

Select 1-2 topic clusters (2-3 Q&As each, 4-6 total) covering 4-5 decision-critical phases. Assign difficulty (1F/2I/1A per cluster = 25/50/25% overall). Map ≥5 core stakeholders per Q&A. Apply Decision Criticality Framework.

**Verify**: 4-6 Q&As | 25/50/25% F/I/A (±5%) | 4-5 decision-critical phases (≥1 Q&A each) | All 5 viewpoints (≥20% each) | All 5 perspectives (≥60% Q&As cover ≥3) | ≥5 core stakeholders (≥1 Q&A per role as primary) | 100% decision-critical

## 2. Build References

Create: Glossary ≥10 (Tech 30%, Biz 25%, Eco 15%, Reg 15%, Ops 15%) | Tools ≥6 (≥1/viewpoint, URL/date) | Frameworks ≥5 (STRIDE/ATAM/C4/DORA/Blue Ocean) | Literature ≥6 (canonical only) | Citations ≥8 (APA 7th, 60/30/10% EN/ZH/Other, ≥30% biz/reg)

**Verify**: G≥10, T≥6, F≥5, L≥6, A≥8 | 60/30/10% lang (±10%) | All 5 viewpoints | ≥50% last 3yr, ≥70% modern, ≥30% biz/market | ≥4 types, <20% single source, ≥40% non-tech | 100% valid URLs

## 3. Write Q&As

**Structure** (100% decision-critical): Lifecycle phase + stakeholder(s) + viewpoint(s) + perspective(s) context + Decision Criticality justification

**Each Answer** (150-250 words): Context (needs/phase/system) → Framework (which viewpoints & why) → Multi-viewpoint assessment (≥3 of: Technical/Business/Ecosystem/Regulatory/Operational with quantified metrics) → Multi-perspective evaluation (≥3 of: Performance/Security/Reliability/Decentralization/Transparency) → Comparison matrix (≥2 alternatives: Approach/Technical/Business/Regulatory/Operational/Use When/Stakeholder Impact) → Recommendations (context-specific, thresholds, criteria) → Risks/Limitations (assumptions/trade-offs/boundaries) → Citations (≥1 foundational, ≥2 intermediate, ≥3 advanced/biz/reg)

**Validate Every Q&A**: 150-250 words | ≥3 viewpoints | ≥3 perspectives with metrics | ≥5 core stakeholders | Citations formatted | Comparison table ≥2 alternatives | Quantified insights | Decision Criticality justified

## 4. Create Artifacts

**Per Q&A** (4/4 required): Framework diagram (Mermaid <120 nodes, matches phase/viewpoint: BMC/C4/Data flow/Integration map) | Viewpoint matrix (Technical/Ecosystem/Business/Regulatory/Operational columns) | Perspective metrics (≥3: metric/formula/variables/baseline/target/measurement) | Comparison matrix (≥2 alternatives: Approach/Technical/Business/Regulatory/Operational/Use When/Stakeholder Impact)

**Verify**: All Q&As 4/4 artifacts | Diagrams render | Tables formatted | Metrics complete | Stakeholder impact included | All linked to Q&As

## 5. Link References

Populate all sections (G/T/F/L/A). Extract all `[Ref: ID]` from Q&As. Verify 100% exist. Remove orphans. Validate all URLs.

**Verify**: G≥10, T≥6, F≥5, L≥6, A≥8 | 100% `[Ref: ID]` resolved | 0 broken URLs | 60/30/10% lang (±10%) | All 5 viewpoints | No orphans

## 6. Validate (12 Streamlined Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥10, T≥6, F≥5, L≥6, A≥8, Q=4-6 (25/50/25%) |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified) |
| 3 | Citations | ≥70% Q&As ≥1; ≥40% ≥2; ≥20% ≥3 |
| 4 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 5 | Recency | ≥50% last 3yr; ≥70% modern; ≥30% business |
| 6 | Links | 100% valid URLs |
| 7 | Word count | All Q&As: 150-250 words |
| 8 | Insights | 100% quantified (no generic claims) |
| 9 | Lifecycle coverage | 4-5 decision-critical phases (≥1 Q&A each) |
| 10 | Viewpoint/Perspective | All 5 viewpoints + all 5 perspectives; ≥60% Q&As cover ≥3 each |
| 11 | Stakeholder coverage | ≥5 core roles (≥1 Q&A per role as primary) |
| 12 | Artifacts & Review | 100% Q&As have 4/4 artifacts; 6/6 review criteria PASS |

**Protocol**: ANY fail → STOP → Fix → Re-validate ALL 12 → Iterate until 12/12 PASS

## 7. Final Review (6/6 Required)

1. **Clarity**: Logical structure | Consistent multi-domain terminology | Inline definitions | Clear stakeholder context
2. **Accuracy**: Verifiable facts with citations | Diagrams render | Valid formulas | Correct framework applications
3. **Completeness**: 4-5 decision-critical phases + 5 viewpoints + 5 perspectives + ≥5 core stakeholders | G≥10, T≥6, F≥5, L≥6, A≥8, Q=4-6 | 12/12 PASS
4. **Balance**: ≥3 viewpoints/perspectives per Q&A | ≥2 alternatives + stakeholder impact | Explicit assumptions/limitations/risks | Tagged consensus
5. **Practicality**: Actionable guidance | Stakeholder-specific recommendations | Measurable outcomes with thresholds | Context-specific criteria
6. **Decision-Criticality**: Every Q&A blocks decision or creates material risk | Quantified impact | 1-6mo action window | Multi-stakeholder (≥2 roles)

**Submit When**: 12/12 PASS + 6/6 criteria | **High-Risk**: Decision Criticality | Stakeholder specification | Metrics validity | URLs | Cross-refs | Framework usage

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Lifecycle Phase | Viewpoint(s) | Perspective(s) | Range | Count | Difficulty |
| [Title] | [Phase] | [Primary + Secondary] | [≥3 Perspectives] | Q1-Q3 | 3 | 1F/1I/1A |
[1-2 clusters, 4-6 total, 4-5 decision-critical phases, all 5 viewpoints, all 5 perspectives, 25/50/25% F/I/A]

---

## Topic 1: [Title] – [Lifecycle Phase]
**Overview**: [1-2 sentences describing analysis scope, primary stakeholder, and key perspectives]

**Stakeholder Focus**: Primary: [Role] | Secondary: [Roles consulted]

### Q1: [Analysis-based question with multi-viewpoint context]
**Difficulty**: [F/I/A] | **Phase**: [Lifecycle] | **Stakeholder**: [Primary Role]

**Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified] – [Justification]

**Key Insight**: [Multi-viewpoint quantified insight in one sentence]

**Answer** (150-250 words):

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

## References (Minimal Viable)

### Glossary (≥10, Multi-Domain)
**G1. [Term]** [EN/ZH/Other] – [Viewpoint: Technical/Business/Ecosystem/Regulatory/Operational]
[Definition]. **Related**: [Terms]. **Used in**: [Lifecycle phases]

### Tools (≥6, Decision-Critical Only)
**T1. [Tool]** [Tag] – [Viewpoint]
**Purpose**: [Desc]. **Updated**: [YYYY-MM]. **URL**: [Link]

### Frameworks (≥5, Decision-Critical Analysis Methods)
**F1. [Framework Name]** [Tag] – [Viewpoint]
**Purpose**: [When to use]. **Key Elements**: [Components]. **Output**: [What it produces]. **Source**: [Official URL]

### Literature (≥6, Canonical References Only)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – [Domain: Technical/Business/Regulatory/Operational]
**Relevance**: [Why]. **Key Concepts**: [Main ideas]

### Citations (≥8, APA 7th, 60/30/10%, ≥30% business/regulatory)
**A1.** Author(s). (Year). *Title*. Source. [EN/ZH/Other]

---

## Validation Report (12 Streamlined Checks)
| # | Check | Target | Result | Status |
| 1 | Counts | G≥10, T≥6, F≥5, L≥6, A≥8, Q=4-6 (25/50/25%) | G:X, T:Y, F:Z... | PASS/FAIL |
| 2 | Decision Criticality | 100% Q&As satisfy ≥1 criterion | X/4-6 | PASS/FAIL |
| 3 | Citations | ≥70% ≥1; ≥40% ≥2; ≥20% ≥3 | X% / Y% / Z% | PASS/FAIL |
| 4 | Language | 60/30/10% EN/ZH/Other (±10%) | X% / Y% / Z% | PASS/FAIL |
| 5 | Recency | ≥50% last 3yr; ≥70% modern; ≥30% business | X% / Y% / Z% | PASS/FAIL |
| 6 | Links | 100% valid URLs | X/Y | PASS/FAIL |
| 7 | Word count | All Q&As: 150-250 words | X-Y avg | PASS/FAIL |
| 8 | Insights | 100% quantified (no generic claims) | X/4-6 | PASS/FAIL |
| 9 | Lifecycle coverage | 4-5 decision-critical phases (≥1 Q&A each) | X/4-5 | PASS/FAIL |
| 10 | Viewpoint/Perspective | All 5 viewpoints + all 5 perspectives; ≥60% Q&As cover ≥3 each | X% / Y% | PASS/FAIL |
| 11 | Stakeholder coverage | ≥5 core roles (≥1 Q&A per role as primary) | X/5 | PASS/FAIL |
| 12 | Artifacts & Review | 100% Q&As have 4/4 artifacts; 6/6 review criteria PASS | X/4-6 | PASS/FAIL |

**Overall**: [X/12 PASS - need 12/12]
**Issues**: [List all failures]
**Remediation**: [Specific actions to fix each failure]

**Coverage Summary**:
- Lifecycle phases: [4-5/4-5 decision-critical covered]
- Viewpoints: Technical X%, Business Y%, Ecosystem Z%, Regulatory W%, Operational V%
- Perspectives: Performance X%, Security Y%, Reliability Z%, Decentralization W%, Transparency V%
- Stakeholders: [≥5/5 core roles with ≥1 Q&A each as primary]
- Decision Criticality: [100% satisfy ≥1 criterion]
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

## Tools (≥6, Decision-Critical; ≥1 per viewpoint: Technical/Business/Ecosystem/Regulatory/Operational)

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

## Frameworks (≥5, Analysis Methods Across Viewpoints)

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

## Citations (≥8, APA 7th, 60/30/10% EN/ZH/Other, ≥30% Business/Regulatory)

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
