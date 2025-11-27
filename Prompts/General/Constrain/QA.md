# Constraint-Aware Professional Domain Q&A Generator

Generate 25-30 Q&As for senior/expert roles with constraint analysis across 8 categories, 10 stakeholder roles, 8 lifecycle phases.

## Context & Success Criteria

**Audience**: Senior practitioners (5+ years), domain experts, strategic decision-makers.

**Scope**: 6 dimensions × 8 constraint categories × 10 stakeholders × 8 lifecycle phases.

**Scale**: 25-30 Q&As; 10-15min/question.

**Timeline**: Assessment (3-4h) or self-study; immediate use.

**Assumptions**: Complex domain-specific systems (scale/impact/risk appropriate to industry), relevant tools/methods/frameworks.

**Stakeholders**: Domain roles vary by industry (e.g., Software: BA, PM, Architect, Developer, QA, DevOps; Healthcare: Clinician, Administrator, Compliance Officer; Finance: Risk Manager, Trader, Analyst).

**Output**: 25-30 Q&As (20/40/40% F/I/A), domain artifacts (10-30 lines: code/formulas/processes/diagrams), quantified trade-offs (≥2), ≥1 citation each.

**Difficulty**: **F**=execution/implementation, **I**=strategy/trade-offs, **A**=portfolio/vision/P&L.

**Success**: 25/25 validation checks PASS, 8/8 criteria met, G≥20, T≥5, L≥6, C≥12.

**Decision-Criticality** (include if ≥1 criterion satisfied):
- **Blocks Decision**: Impacts strategic approach, constraint resolution, or trade-off choices
- **Creates Risk**: Material threat (constraint violations, performance/quality breaches, budget overruns, compliance/safety gaps)
- **Affects ≥2 Stakeholder Roles**: Multi-functional impact (e.g., Operations + Finance, Strategy + Compliance)
- **Requires Action**: 1-6mo implementation window (not theoretical)
- **Quantified Impact**: Measurable constraint metrics (KPI %, cost $, resource utilization %, compliance/safety deadlines, throughput)

---

# Domain Adaptation Guide

This framework is designed for cross-domain applicability. To adapt for your specific industry:

## 1. Define Your Domain Context
- **Industry**: Specify sector (Software, Healthcare, Manufacturing, Finance, Education, etc.)
- **Scale Indicators**: Replace "10K rps, 1TB data" with domain-appropriate metrics (e.g., patients/day, units/hour, transactions/second, students/class)
- **Tools/Methods**: Identify domain-standard frameworks, technologies, methodologies

## 2. Customize Stakeholders
Map 10 stakeholder categories to your domain roles:
- **Software**: BA, PM, Architect, Developer, QA, DevOps, Security, Data Engineer, SRE, Tech Lead
- **Healthcare**: Clinician, Administrator, Compliance Officer, Patient Advocate, Lab Manager, IT Support, Quality Assurance, Finance, Risk Manager, Clinical Lead
- **Manufacturing**: Production Manager, Quality Inspector, Process Engineer, Maintenance, Supply Chain, Safety Officer, Finance, Plant Manager, R&D, Operations Lead
- **Finance**: Trader, Risk Manager, Compliance, Analyst, Portfolio Manager, Operations, Technology, Auditor, Product Manager, Business Lead

## 3. Adapt Artifacts
Replace code with domain-appropriate deliverables:
- **Software**: Code, APIs, configurations, schemas
- **Healthcare**: Clinical protocols, care pathways, safety checklists, dosage calculations
- **Manufacturing**: Process flows, quality control plans, production schedules, formulas
- **Finance**: Risk models, pricing formulas, trading algorithms, compliance frameworks
- **General**: Workflows, decision trees, calculations, procedures, standards

## 4. Customize Constraints
Ensure constraint examples reflect your domain:
- **Technical**: Domain-specific infrastructure/equipment/platforms
- **Compliance**: Relevant regulations (GDPR, HIPAA, SOX, FDA, ISO standards)
- **Operational**: Domain-appropriate KPIs (uptime, yield, accuracy, response time)

---

# Coverage Requirements

## 6 Dimensions (4-6 Q&As each)
1. **Structure/Organization**: Decomposition, modularity, coupling, boundaries, hierarchy, roles
2. **Process/Flow**: Workflows, sequences, orchestration, dependencies, error/exception handling, timing
3. **Quality/Performance**: Standards, efficiency, scalability, reliability, risk management, security/safety
4. **Resources/Assets**: Management of capital/data/knowledge/materials, allocation, optimization, lifecycle
5. **Integration/Interfaces**: Internal/external interactions, protocols, communication channels, partnerships
6. **Evolution/Change**: Transformation, improvement, adaptation, debt management, migration, innovation

## 8 Constraint Categories (≥3/Q&A, all 8 overall)

| Category | Examples |
|----------|----------|
| **Technical** | Infrastructure capacity, equipment specs, technology platforms, legacy systems, versions, tooling limitations |
| **Resource** | Deadlines, budget ($X/period), team size/skills, materials, space, energy, capital availability |
| **Business** | Pricing models, unit economics, market share, competitive positioning, service levels, revenue targets |
| **Organizational** | Stakeholder roles, workflows, policies, standards, risk appetite, governance, decision authority |
| **Compliance** | Regulations (GDPR, HIPAA, SOX, FDA, ISO), audit requirements, certifications, safety standards, reporting |
| **Operational** | KPIs/SLOs, uptime targets, throughput, capacity limits, maintenance windows, quality metrics, headroom |
| **Ecosystem** | Vendor dependencies, supplier constraints, partner capabilities, talent availability, market maturity |
| **Lifecycle** | Phase-specific constraints: Initiation→Planning→Execution→Testing→Deployment→Operations→Maintenance→Evolution |

## 10 Stakeholder Categories (≥2/Q&A, all 10 overall)
Domain-specific roles from these categories:
1. **Strategy**: Leadership, Product/Program Management, Portfolio Management
2. **Analysis**: Business/Domain Analysts, Requirements Specialists, Data Analysts
3. **Design**: Architects, Designers, Subject Matter Experts
4. **Execution**: Practitioners, Implementers, Specialists (varies by industry)
5. **Quality**: QA, Inspectors, Auditors, Validators
6. **Operations**: Operations teams, Support, Maintenance
7. **Security/Compliance**: Security officers, Compliance managers, Risk managers
8. **Resources**: Finance, HR, Procurement, Resource managers
9. **Reliability**: SRE, Continuity planners, Performance engineers
10. **Integration**: Technical leads, Cross-functional coordinators, Partnership managers

---

# Content Standards

## Q&A Structure (150-300 words)
1. **Header**: Difficulty | Dimension | Phase | Stakeholders
2. **Key Insight**: Quantified trade-off (1 sentence)
3. **Constraints**: ≥3 categories with magnitudes
4. **Body**: Context → Approach/Method → Trade-offs → Metrics → Assumptions → Stakeholder impact
5. **Artifact**: 10-30 lines domain-specific (code/formulas/process flows/decision trees) with validation + optimizations
6. **Metrics**: Formula | Variables | Target | Constraint impact
7. **Trade-offs**: ≥2 alternatives (Approach | Pros | Cons | Resources | Budget | Business | Tag)
8. **Citations**: ≥1 (≥2 for advanced)

## Quality Standards
- **Traceability**: Requirements → Constraints → Approach/Method → Artifact → Metrics
- **Quantified Trade-offs**: ✅ "Method A: 10x throughput, +35% cost, +40% complexity" ❌ "more complex"
- **Context Precision**: Specify magnitudes (e.g., "20 FTE, $5K/mo, 99.9% target, ISO cert, 8-person team, 4mo")
- **Balanced Analysis**: ≥2 alternatives; explicit assumptions/limitations; [Consensus]/[Context]/[Emerging] tags
- **Precise Language**: Define terms inline; consistent terminology; concrete metrics ("95th percentile"); minimal jargon
- **Domain Patterns**: Reference established methods/frameworks/standards relevant to the domain (varies by industry)

## References (G≥20 | T≥5 | L≥6 | C≥12)

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | 20 | Domain terms + relationships; cover all 8 categories + 10 stakeholder categories |
| **Tools** | 5 | Valid URL, updated ≤18mo, pricing/availability |
| **Literature** | 6 | Authoritative sources: seminal works, industry standards, recognized domain experts |
| **Citations** | 12 | APA 7th; 60% EN/30% ZH/10% other; ≥50% last 3yr; 100% valid URLs |

---

# Generation Process

## 1. Plan
- Allocate 25-30 Q&As across 6 dimensions (20/40/40% F/I/A)
- Map 8 constraints + 10 stakeholders + 8 phases
- Verify MECE: no gaps/overlap

## 2. Build References
- Glossary: 8 categories + 10 stakeholders + relationships
- Tools: URL, updated ≤18mo, pricing
- Literature: Authoritative sources
- Citations: APA 7th, 60/30/10% EN/ZH/Other, ≥50% last 3yr, valid URLs

## 3. Write Q&As (Validate Every 5)
- **Questions**: ≥70% judgment ("How/When/Compare..."); multi-dimensional constraints
- **Checkpoints**: Words 150-300 | Citations | Syntax | Traceability | Quantified | Constraints (≥3/Q&A) | Stakeholders (≥2/Q&A) | Phases | Technical ≥40%

## 4. Artifacts & Links
- Per cluster: Visual models (<120 nodes) + domain artifacts + metrics + trade-offs
- Verify [Ref: ID] resolved, 100% valid URLs

## 5. Final Validation (25/25 PASS)

**Counts**: G≥20 | T≥5 | L≥6 | C≥12 | Q=25-30 (20/40/40%)  
**Quality**: Citations ≥70% | EN 60%/ZH 30%/Other 10% | Recency ≥50% | URLs 100% | Cross-refs 100%  
**Content**: Words 150-300 | Quantified 100% | Judgment ≥70% | Traceability ≥80% | Artifacts ≥90% | Syntax 100%  
**Coverage**: Constraints (≥80% Q&As ≥3) | Stakeholders all 10 | Phases all 8 | Technical ≥40% | Business ≥30% | Ecosystem ≥30%  
**Criteria**: Clarity | Accuracy | Completeness | Balance | Practicality | Self-Correction | Constraint-Awareness | Stakeholder-Awareness

**Failure**: ANY fail → Fix → Re-validate ALL

---

# Templates

## Q&A
```
**Q**: [Judgment question with multi-dimensional constraints]
**Difficulty**: F/I/A | **Dimension**: [1-6] | **Phase**: [Lifecycle] | **Stakeholders**: [≥2]
**Key Insight**: [Quantified trade-off, 1 sentence]
**Constraints**: [≥3 categories with magnitudes]
**Answer** (150-300 words): [Context → Approach/Method → Trade-offs → Metrics → Assumptions → Impact] [Ref: X]
**Artifact** (10-30 lines): [Domain-specific format + validation + optimizations]
**Metrics**: [Formula | Variables | Target | Constraint impact]
**Trade-offs**: | Approach | Pros | Cons | Resources | Budget | Business | Tag |
**Stakeholders**: [≥2 with concerns]
```

## References
- **Glossary** (≥20): Term [EN/ZH] → Definition + Related
- **Tools** (≥5): Name → Purpose | Updated | Pricing | URL
- **Literature** (≥6): Author (Year). Title. Publisher
- **Citations** (≥12): APA 7th, 60/30/10% EN/ZH/Other

## Validation Report
```
**Counts**: G:X/20 | T:X/5 | L:X/6 | C:X/12 | Q:X/25-30 (F:X% I:X% A:X%)
**Quality**: Cites X% | Lang EN:X% ZH:X% | Recent X% | URLs X% | Links X%
**Content**: Words X% | Quantified X% | Judgment X% | Trace X% | Artifacts X% | Syntax X%
**Coverage**: Constraints X% | Stakeholders X% | Phases X% | Tech X% | Biz X% | Eco X%
**Status**: X/25 PASS | X/8 MET | **Issues**: [List] | **Fix**: [Actions]
```

# Example (Software Domain)

> **Note**: This example demonstrates the framework applied to software architecture. Adapt structure, constraints, stakeholders, and artifacts to your specific domain (e.g., Healthcare: patient care workflows; Manufacturing: production line optimization; Finance: risk management models).

## Q: Design high-throughput transaction processing for regulated marketplace under resource/compliance constraints?

**Difficulty**: A | **Dimension**: Structure+Resources | **Phase**: Design, Execution, Operations | **Stakeholders**: Strategy, Design, Execution, Security/Compliance, Reliability, Integration

**Key Insight**: Event-driven separation of concerns achieves 15K transactions/hour (+180% vs baseline), +35ms latency, +40% operational complexity, compliance-verified.

**Constraints**: **Technical**: Limited infrastructure (4-core, 16GB, 500 IOPS) | **Resource**: $8K/mo, 8 specialists, 1 reliability engineer, 4mo | **Business**: $500K/mo throughput, 15% market share, <200ms target | **Compliance**: Industry regulation (HIPAA/SOX/FDA equivalent), audit trail | **Operational**: 99.9% availability | **Ecosystem**: Cloud platform, open-source messaging, legacy system integration

**Answer** (280 words): Separated command/query architecture with event sourcing: commands → append-only audit store, queries → optimized read views (cached). Independent scaling (3 write, 6 read processors) within $8K/mo, <200ms latency [Ref: A2, A7]. Stack: Message broker (encrypted TLS 1.3), transaction log (events), cache layer (reads). Legacy integration via isolation layer + failure protection. Trade-offs: +35ms processing time (vs 2s baseline), +40% operational overhead (team training required), +60% storage ($2.4K/mo). Impact: +$150K/mo capacity, 4mo feasible [Ref: A4]. Metrics: 95th percentile processing 180ms, queries 25ms, utilization 65%, $7.8K/mo. Stakeholder alignment: Compliance (encrypted audit), Reliability (documented procedures), Strategy (timeline), Integration (ROI 18mo). Limits: 5GB/day growth → repartition at 18mo; eventual consistency (<500ms) unsuitable for real-time inventory.

**Artifact** (Implementation pseudo-code):
```
function ProcessTransaction(context, command):
    if not Validator.Validate(command):
        AuditLog.Record(context, "ValidationFailed", command.ID, error)
        return Error("Validation failed")
    
    event = CreateEvent(
        ID: GenerateUniqueID(),
        TransactionID: command.ID,
        Data: Encrypt(command),
        Timestamp: CurrentTime()
    )
    
    if not EventStore.Append(context, event):
        return Error("Event store append failed")
    
    if not MessageBroker.Publish(context, "transactions.created", event):
        Logger.Error("Message publish failed", event.ID, error)
    
    return Success()
```

**Metrics**: 95th percentile: validate(15) + encrypt(10) + append(120) + ack(35) = 180ms | Target <300ms | Resource constraints limit validation, encryption +10ms

**Trade-offs**:
| Approach | Pros | Cons | Resources | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| Separated Architecture | +180% throughput, audit trail | +35ms latency, +40% ops | 65% utilization (3×units), 5GB/day | $7.8K | +$150K/mo, 4mo, <200ms | [Consensus] |
| Integrated System | Simple, 145ms latency | Max 5.5K/hour capacity | 85% utilization (1×unit), 1.5GB/day | $4.5K | $275K/mo ceiling | [Context] |

**Stakeholders**: **Strategy**: 4mo timeline acceptable | **Design**: Balances throughput/complexity/team capability | **Execution**: Training mitigates operational overhead | **Security/Compliance**: Encryption meets requirements | **Reliability**: Failure protection + 30% headroom | **Integration**: ROI 18mo

## Glossary (Domain-Adaptive Examples)
**G1. Modular Design** [EN] – Core isolation via defined interfaces/boundaries. Enables independent change. Related: Separation of Concerns  
**G2. Separation of Concerns** [EN] – Distinct responsibilities for different components/functions. Related: Modularity  
**G3. Audit Trail** [EN] – Immutable record of changes/events. Compliance, traceability, temporal analysis. Related: Event Log  
**G4. Domain Model** [EN] – Representation of domain concepts, relationships, rules. Related: Conceptual Framework  
**G5. Bounded Context** [EN] – Model/process boundary for consistency and clarity. Related: Scope Definition  
**G6. Consistency Boundary** [EN] – Limits within which data/state must be consistent. Related: Transaction Scope  
**G7. Abstraction Layer** [EN] – Interface hiding implementation complexity. Enables substitution. Related: Encapsulation  
**G8. Event** [EN] – Immutable fact/occurrence. Enables decoupling, asynchronous processing. Related: State Change  
**G9. Compensating Action** [EN] – Reversal/mitigation step for long-running processes. Related: Error Recovery  
**G10. Failure Isolation** [EN] – Prevents cascading failures through boundaries/limits. Related: Risk Containment  
**G11. Technical Constraint** [EN] – Infrastructure, equipment, platform, tools, legacy systems. Related: Capability Limits  
**G12. Resource Constraint** [EN] – Time/budget/personnel/materials limits. Deadlines, costs, skills, availability. Related: Capacity  
**G13. Business Constraint** [EN] – Revenue, market, continuity requirements. Pricing, economics, competitive position. Related: Value  
**G14. Organizational Constraint** [EN] – Stakeholder/process/governance structures. Workflows, authority, risk tolerance. Related: Policy  
**G15. Compliance Constraint** [EN] – Legal/regulatory/standards requirements. Certifications, audits, reporting. Related: Governance  
**G16. Operational Constraint** [EN] – Performance/quality targets. KPIs, availability, throughput, capacity headroom. Related: Service Level  
**G17. Ecosystem Constraint** [EN] – External dependencies. Vendor/supplier capabilities, market maturity, talent pool. Related: Environment  
**G18. Lifecycle Constraint** [EN] – Phase-specific limits. Initiation→Planning→Execution→Testing→Deployment→Operations→Maintenance→Evolution. Related: Process Stage  
**G19. Stakeholder** [EN] – Role with interest/influence. Varies by domain: strategy, execution, quality, operations, etc. Related: RACI  
**G20. Lifecycle Phase** [EN] – 8 phases: Initiation→Planning→Execution→Testing→Deployment→Operations→Maintenance→Evolution. Related: Project Stage

## Tools (Domain-Adaptive Examples)
> **Note**: Select tools appropriate to your domain. Examples below span multiple disciplines.

**T1. Mermaid** – Visual diagrams from text. Flowcharts, sequences, relationships. 2024-10. Free. https://mermaid.js.org  
**T2. Lucidchart** – Collaborative diagramming. Process flows, org charts, models. 2024-09. Freemium. https://www.lucidchart.com  
**T3. BPMN Tools** – Business process modeling. Workflow standardization. 2024-08. Varies. https://www.bpmn.org  
**T4. Decision Matrix** – Multi-criteria evaluation. Trade-off analysis. 2024-10. Free. https://www.mindtools.com/decision-matrix  
**T5. ADR (Architecture Decision Records)** – Decision log. Rationale capture, traceability. 2024-06. Free. https://adr.github.io

## Literature (Domain-Adaptive Examples)
> **Note**: Replace with authoritative sources from your domain. Examples below demonstrate variety across disciplines.

**L1.** Goldratt (1984). *The Goal*. North River Press – Theory of Constraints, systems thinking (Manufacturing/Operations)  
**L2.** Kahneman (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux – Decision-making, cognitive biases (General)  
**L3.** Kim et al. (2013). *The Phoenix Project*. IT Revolution – Process improvement, constraint management (IT/Operations)  
**L4.** Porter (1985). *Competitive Advantage*. Free Press – Strategy, value chains, trade-offs (Business Strategy)  
**L5.** Ries (2011). *The Lean Startup*. Crown Business – Iteration, validation, resource constraints (Entrepreneurship)  
**L6.** ISO/IEC Standards – Domain-specific standards (e.g., ISO 9001 Quality, ISO 27001 Security, ISO 14001 Environmental)

## Citations (Domain-Adaptive Examples)
> **Note**: Replace with domain-appropriate sources. Maintain language distribution (60% EN/30% ZH/10% Other) and recency (≥50% last 3yr).

**A1.** Goldratt (1984). *The goal: A process of ongoing improvement*. North River Press [EN]  
**A2.** Kim et al. (2013). *The Phoenix Project: A novel about IT, DevOps, and helping your business win*. IT Revolution [EN]  
**A3.** 周爱民 (2021). *架构的本质* (Nature of Architecture). 电子工业出版社 [ZH]  
**A4.** Porter (1985). *Competitive advantage: Creating and sustaining superior performance*. Free Press [EN]  
**A5.** Kahneman (2011). *Thinking, fast and slow*. Farrar, Straus and Giroux [EN]  
**A6.** Ries (2011). *The lean startup*. Crown Business [EN]  
**A7.** ISO (2015). *ISO 9001:2015 Quality management systems*. International Organization for Standardization [EN]  
**A8.** Womack & Jones (1996). *Lean thinking*. Simon & Schuster [EN]  
**A9.** 张逸 (2019). *领域驱动设计实践* (Domain-Driven Design in Practice). 电子工业出版社 [ZH]  
**A10.** Schwaber & Sutherland (2020). *The Scrum guide*. Scrum.org [EN]  
**A11.** PMI (2021). *A guide to the project management body of knowledge (PMBOK)* (7th ed.). Project Management Institute [EN]  
**A12.** 华为 (2020). *华为数字化转型之道* (Huawei's Digital Transformation). 机械工业出版社 [ZH]
