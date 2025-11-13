# Constraint-Aware Software Architecture Interview Q&A Generator

Generate 25-30 interview Q&As for senior/architect roles with holistic constraint analysis across 8 categories, 10 stakeholder roles, full SDLC phases, and architecture-to-code translation.

## Success Criteria

**Output**: 25-30 Q&As | 25/25 validation PASS | 8/8 review criteria met  
**Audience**: Senior devs (5+ years), architects, 10 stakeholder roles (BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead)  
**Scope**: 6 dimensions × 8 constraint categories × 10 stakeholders × 8 SDLC phases | Production code | Quantified trade-offs (≥2 alternatives) | Authoritative citations  
**Assumptions**: Distributed systems (>10K rps, >1TB data) | Idiomatic Go/Java/Python/TypeScript | Cloud-native | Foundational knowledge (layers, MVC, REST)

---

# Requirements

## Q&A Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 25-30 (20% Foundational / 40% Intermediate / 40% Advanced) |
| **Answer Length** | 150-300 words (code excluded) |
| **Structure** | Pattern → rationale → code → quantified trade-offs → metrics → stakeholder impact |
| **Citations** | ≥1/Q&A; ≥2 for advanced |
| **Per Cluster** | Mermaid diagram (<120 nodes) + code (10-30 lines) + metrics table + trade-offs table (≥2 alternatives) |

## Coverage Dimensions

**6 Dimensions** (4-6 Q&As each):
1. **Structural**: Decomposition, modularity, coupling, boundaries
2. **Behavioral**: Events, state, orchestration, error handling  
3. **Quality**: Performance, scalability, reliability, security
4. **Data**: Persistence, caching, consistency, partitioning
5. **Integration**: APIs, messaging, protocols
6. **Evolution**: Refactoring, migration, technical debt

**8 Constraint Categories** (≥3/Q&A, all 8 overall):

| Category | Examples |
|----------|----------|
| **Technical** | CPU/mem/storage/network limits, platform constraints, legacy APIs, language/framework versions |
| **Resource** | Deadlines, budget ($X/mo), team size/skills, hiring pipeline |
| **Business/Market** | Pricing models, CAC/LTV, market share, competitive SLAs, feature priority |
| **Organizational** | 10 stakeholder roles, approval workflows, architecture standards, risk appetite |
| **Regulatory/Compliance** | GDPR, HIPAA, PCI-DSS, SOC 2, ISO 27001, audit logs, data residency |
| **Operational** | SLOs, RTO/RPO, downtime windows, on-call coverage, 30% capacity headroom |
| **Ecosystem** | Cloud lock-in, SaaS API limits, OSS health, protocol adoption, talent availability |
| **Lifecycle** | Phase-specific constraints across 8 SDLC phases (Requirements→Design→Dev→Testing→Deployment→Operations→Maintenance→Evolution) |

**10 Stakeholder Roles** (≥2/Q&A, all 10 overall): BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

## Content Standards

- **Traceability**: Requirements → Constraints → Pattern → Code → Metrics
- **Quantified Trade-offs**: Concrete metrics only. ✅ "CQRS: 10x read, +20-40ms write, +30% complexity" ❌ "Microservices are complex"
- **Context Precision**: Specify magnitudes (e.g., "4-core CPU, $5K/mo, 99.9% SLA, HIPAA, 8-person team, 4-month deadline")
- **Balanced Analysis**: ≥2 alternatives with table; explicit assumptions/limitations; tag [Consensus]/[Context-dependent]/[Emerging]
- **Precise Language**: Define terms inline; consistent terminology; concrete metrics ("<300ms p95" not "fast"); minimal jargon
- **Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Bulkhead, Event Sourcing, Sharding, Strangler Fig, Feature Toggle, Canary

## Reference Requirements

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥20 | Terms + relationships; includes all 8 constraint categories + 10 stakeholder roles |
| **Tools** | ≥5 | Valid URL, updated ≤18mo, pricing, adoption metrics |
| **Literature** | ≥6 | Authoritative (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann) |
| **Citations** | ≥12 | APA 7th; 60% [EN] / 30% [ZH] / 10% other (±10%); ≥50% last 3yr; 100% valid URLs |

---

# Generation Process

## 1. Plan (5-6 clusters, 25-30 Q&As)
- Allocate 4-6 Q&As/cluster across 6 dimensions (20/40/40% Foundational/Intermediate/Advanced)
- Map all 8 constraint categories + 10 stakeholders + 8 lifecycle phases across Q&As
- Verify MECE coverage, no gaps/overlap

## 2. Build References (Glossary ≥20 | Tools ≥5 | Literature ≥6 | Citations ≥12)
- Glossary: All 8 constraint categories + 10 stakeholder roles + term relationships
- Tools: Valid URL, updated ≤18mo, pricing, adoption metrics
- Literature: Authoritative sources (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann)
- Citations: APA 7th, 60/30/10% [EN]/[ZH]/Other, ≥50% last 3yr, 100% valid URLs

## 3. Write Q&As (Validate Every 5)

**Questions**: ≥70% judgment ("How/When/Compare..."); multi-dimensional constraints (e.g., "Given 4-core CPU, $5K/mo, HIPAA, 4-month deadline...")

**Answer Structure** (150-300 words):
1. Header: Difficulty | Dimension | Phase | Stakeholders
2. Key Insight: Quantified trade-off (1 sentence)
3. Constraints: ≥3 categories with magnitudes
4. Body: Context → Pattern → Quantified trade-offs → Metrics → Assumptions → Stakeholder impact (≥2 roles)
5. Code: 10-30 lines with error handling + constraint optimizations
6. Metrics Table: Formula | Variables | Target | Constraint impact
7. Trade-offs Table: ≥2 alternatives (Approach | Pros | Cons | Hardware/Budget/Business/Ecosystem | Consensus tag)
8. Citations: ≥1 (≥2 for advanced)

**Validation Checkpoints** (Every 5 Q&As): Word count 150-300 | Citations present | Syntax valid | Traceability complete | Judgment questions | Quantified insights | Constraint coverage (≥3/Q&A, all 8 overall) | Stakeholder coverage (≥2/Q&A, all 10 overall) | Lifecycle phases (all 8 overall) | Hardware (≥40% overall)

## 4. Create Artifacts & Resolve Links
- Per cluster: Mermaid diagram (<120 nodes) + code + metrics table + trade-offs table
- Verify all [Ref: ID] resolved, 100% valid URLs, no orphans

## 5. Final Validation (Submit When 25/25 PASS + 8/8 Criteria)

**25 Validation Checks**:
- **Counts**: G≥20 | T≥5 | L≥6 | C≥12 | Q=25-30 (20/40/40% F/I/A)
- **Quality**: Citations ≥70% Q&As | Language 60/30/10% EN/ZH/Other | Recency ≥50% last 3yr | 100% valid URLs | 100% cross-refs resolved
- **Content**: 150-300 words | 100% quantified insights | ≥70% judgment Qs | ≥80% traceability | ≥90% clusters with artifacts | 100% syntax valid
- **Coverage**: All 8 constraints (≥80% Q&As mention ≥3) | All 10 stakeholders (≥2/Q&A) | All 8 phases | Hardware ≥40% | Business ≥30% | Ecosystem ≥30%

**8 Review Criteria**: Clarity | Accuracy | Completeness | Balance (≥2 alternatives) | Practicality | Self-Correction | Constraint-Awareness (quantified multi-dimensional) | Stakeholder-Awareness (≥2/Q&A)

**Failure Protocol**: ANY fail → Fix → Re-validate ALL

---

# Output Templates

## Q&A Format
```
**Q**: [Judgment question with multi-dimensional constraints]

**Difficulty**: F/I/A | **Dimension**: [1-6] | **Phase**: [SDLC phase] | **Stakeholders**: [≥2 roles]

**Key Insight**: [Quantified trade-off, 1 sentence]

**Constraints**: [≥3 categories with magnitudes]

**Answer** (150-300 words): [Context → Pattern → Quantified trade-offs → Metrics → Assumptions → Stakeholder impact] [Ref: X]

**Code** (10-30 lines): [Language with error handling + constraint optimizations]

**Metrics**: [Formula | Variables | Target | Constraint impact]

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Ecosystem | Tag |

**Stakeholders**: [≥2 roles with specific concerns]
```

## References Format
- **Glossary** (≥20): Term [EN/ZH] → Definition + Related terms
- **Tools** (≥5): Name → Purpose | Updated | Pricing | URL
- **Literature** (≥6): Author (Year). Title. Publisher → Relevance
- **Citations** (≥12): APA 7th, 60/30/10% EN/ZH/Other

## Validation Report
```
**Counts**: G:X/20 | T:X/5 | L:X/6 | C:X/12 | Q:X/25-30 (F:X% I:X% A:X%)
**Quality**: Citations X% Q&As | Language EN:X% ZH:X% Other:X% | Recency X% last 3yr | Valid URLs X% | Cross-refs X%
**Content**: Words X% in range | Quantified X% | Judgment Qs X% | Traceability X% | Artifacts X% | Syntax X%
**Coverage**: Constraints X% Q&As ≥3 | Stakeholders X% | Phases X% | Hardware X% | Business X% | Ecosystem X%
**Status**: X/25 PASS | **Criteria**: X/8 MET
**Issues**: [List]
**Remediation**: [Actions]
```

# Reference Examples

## Complete Q&A Example

### Q: How would you design a high-throughput order processing system for a regulated healthcare marketplace under tight hardware and compliance constraints?

**Difficulty**: Advanced | **Dimension**: Structural + Data | **Lifecycle**: Design, Dev, Ops | **Stakeholders**: Arch, Dev, Sec, Data, SRE, Lead

**Key Insight**: Event-driven CQRS achieves 15K rps on 4-core instances (+180% vs monolith) but increases write latency +35ms (p95) and operational complexity +40% while satisfying HIPAA audit requirements.

**Constraints**: **Hardware**: 4-core CPU, 16GB RAM, 500 IOPS SSD | **Budget**: $8K/mo | **Business**: $500K/mo revenue, 15% market share, <200ms competitive SLA | **Compliance**: HIPAA, SOC 2 | **Team**: 8 devs, 1 SRE | **Time**: 4 months | **Ecosystem**: AWS, Kafka OSS, SOAP legacy system | **Operational**: 99.9% availability

**Answer** (280 words): CQRS with event sourcing satisfies multi-dimensional constraints: commands persist to append-only event store (HIPAA audit trail), queries serve from materialized views (cached performance). Enables independent scaling (3 write nodes, 6 read replicas) within $8K/mo budget while maintaining <200ms latency [Ref: A2, A7]. Implementation: Kafka OSS for event backbone (PHI encrypted TLS 1.3), AWS PostgreSQL for event store, Redis for read views. Legacy SOAP integration isolated via anti-corruption layer + circuit breaker. Trade-offs: +35ms write latency acceptable vs 2s baseline; +40% ops complexity mitigated by team Kafka experience; storage +60% ($2.4K/mo) within budget. Business impact: +$150K/mo revenue capacity, 4-month achievable [Ref: A4]. Metrics: p95 write 180ms, reads 25ms, CPU 65% (30% headroom), cost $7.8K/mo. Stakeholder alignment: Security approves encrypted pipeline; SRE accepts complexity with runbooks; PM green-lights timeline; Leadership approves spend for ROI. Limitations: event store growth (5GB/day) requires partitioning at 18mo; eventual consistency (<500ms) unsuitable for real-time inventory.

**Implementation** (Go):
```go
func (h *OrderHandler) ProcessCommand(ctx context.Context, cmd OrderCommand) error {
    if err := h.validator.Validate(cmd); err != nil {
        h.auditLog.Log(ctx, "OrderValidationFailed", cmd.OrderID, err)
        return fmt.Errorf("validation failed: %w", err)
    }
    event := OrderCreatedEvent{EventID: uuid.New().String(), OrderID: cmd.OrderID, 
                                Data: h.encrypt(cmd), Timestamp: time.Now()}
    if err := h.eventStore.Append(ctx, event); err != nil {
        return fmt.Errorf("event store append: %w", err)
    }
    if err := h.kafka.Publish(ctx, "orders.created", event); err != nil {
        h.logger.Error("kafka publish failed", "event_id", event.EventID, "error", err)
    }
    return nil
}
```

**Metrics**: Write Latency (p95): validate(15ms) + encrypt(10ms) + append(120ms) + ack(35ms) = 180ms | Target: <300ms | Constraint: 4-core limits validation, encryption adds 10ms

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Consensus |
|----------|------|------|----------|--------|----------|-----------|
| CQRS+ES | +180% throughput, audit trail | +35ms write, +40% ops | 65% CPU (3×4-core), 5GB/day | $7.8K/mo | +$150K/mo, 4mo, <200ms SLA | [Consensus] |
| Monolith | Simple, 145ms write | Max 5.5K rps, limited scale | 85% CPU (1×4-core), 1.5GB/day | $4.5K/mo | $275K/mo max, falls behind rivals | [Context] |

**Stakeholders**: **PM**: 4mo achievable, competitive parity | **Arch**: Balances throughput + complexity + team size | **Dev**: Kafka experience mitigates complexity | **Sec**: Encrypted pipeline satisfies HIPAA | **SRE**: Demands circuit breaker + 30% headroom + runbooks | **Lead**: $7.8K for +$150K revenue, ROI 18mo

## Glossary
**G1. Hexagonal** [EN] – Isolates core via ports/adapters. Enables testability, tech independence. Related: DI  
**G2. CQRS** [EN] – Separates commands (writes) from queries (reads). Optimizes scalability. Related: Event Sourcing  
**G3. Event Sourcing** [EN] – Stores state as event log. Enables audit, temporal queries. Related: CQRS  
**G4. DDD** [EN] – Domain modeling via ubiquitous language, bounded contexts, aggregates. Related: Bounded Context  
**G5. Bounded Context** [EN] – Explicit model boundary for consistency. Drives decomposition. Related: Context Map  
**G6. Aggregate** [EN] – Consistency boundary (root + entities/VOs). Enforces invariants. Related: Repository  
**G7. Repository** [EN] – Data access abstraction for aggregates. Related: Aggregate  
**G8. Domain Event** [EN] – Immutable fact. Enables decoupling, eventual consistency. Related: Event Sourcing  
**G9. Saga** [EN] – Coordinates long transactions with compensations. Related: Distributed TX  
**G10. Circuit Breaker** [EN] – Prevents cascading failures. Opens on error threshold. Related: Bulkhead  
**G11. Technical Constraint** [EN] – Hardware/platform/legacy/tech stack limits affecting design decisions. Includes CPU, memory, storage, network, runtime limits, language/framework versions. Related: Performance Budget  
**G12. Resource Constraint** [EN] – Time/budget/team limitations affecting implementation. Includes delivery deadlines, cost limits, team size/skills, hiring pipeline, training needs. Related: Scope Management  
**G13. Business/Market Constraint** [EN] – Revenue model, competitive, and business continuity factors. Includes pricing tiers, CAC/LTV, market share targets, customer segments, competitive pressure, feature prioritization. Related: Product Strategy  
**G14. Organizational Constraint** [EN] – Stakeholder, process, governance, and cultural factors. Includes approval workflows, architecture standards, vendor policies, risk appetite, remote vs co-located dynamics. Related: RACI, Change Management  
**G15. Regulatory/Compliance Constraint** [EN] – Legal and regulatory requirements affecting architecture. Includes GDPR, HIPAA, PCI-DSS, SOC 2, ISO 27001, data residency, audit logs, contractual SLAs. Related: Security, Data Governance  
**G16. Operational Constraint** [EN] – Runtime limits affecting deployment/operations. Includes SLOs, downtime windows, RTO/RPO, on-call coverage, observability limits, capacity headroom. Related: SRE  
**G17. Ecosystem Constraint** [EN] – Vendor, open-source, integration partner, and standards dependencies. Includes cloud provider lock-in, SaaS API limits, OSS community health, protocol adoption, talent pool availability. Related: Vendor Management  
**G18. Lifecycle Phase Constraint** [EN] – Phase-specific limitations across SDLC. Includes requirements ambiguity, design review timelines, CI/CD speed, test environment parity, deployment windows, CVE remediation SLA, migration risk. Related: SDLC  
**G19. Stakeholder** [EN] – Role with specific concerns/priorities in lifecycle. Includes BA (requirements), PM (roadmap), Architect (design), Developer (implementation), QA (quality), DevOps (pipeline), Security (compliance), Data (data quality), SRE (reliability), Leadership (governance). Related: RACI  
**G20. Lifecycle Phase** [EN] – Distinct stage in software development. 8 phases: Requirements & Discovery, Architecture & Design, Development, Testing & Quality, Deployment & Release, Operations & Observability, Maintenance & Support, Evolution & Governance. Related: SDLC

## Tools
**T1. Mermaid** [EN] – Text-based diagrams (flowchart, sequence, class, ER). GitHub-native. Updated: 2024-10. Free/OSS. https://mermaid.js.org  
**T2. OpenAPI** [EN] – REST API spec. Codegen, contract testing. Updated: 2024-09. Free/OSS. https://www.openapis.org  
**T3. JSON Schema** [EN] – JSON validation, docs, codegen. Updated: 2024-08. Free/OSS. https://json-schema.org  
**T4. Kubernetes** [EN] – Container orchestration. Declarative YAML. Updated: 2024-10. Free/OSS. https://kubernetes.io  
**T5. ADR** [EN] – Markdown decision log. Traceability. Updated: 2024-06. Free/OSS. https://adr.github.io

## Literature
**L1. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** – Strategic/tactical modeling, ubiquitous language, bounded contexts  
**L2. Vernon, V. (2013). *Implementing DDD*. Addison-Wesley.** – Practical context mapping, aggregates, event sourcing  
**L3. Richardson, C. (2018). *Microservices Patterns*. Manning.** – Decomposition, data, communication patterns with trade-offs  
**L4. Newman, S. (2021). *Building Microservices* (2nd). O'Reilly.** – Service boundaries, deployment, testing, security  
**L5. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.** – Distributed systems: replication, partitioning, transactions  
**L6. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.** – Repository, Unit of Work, Service Layer

## Citations
**A1.** Evans, E. (2003). *Domain-driven design*. Addison-Wesley. [EN]  
**A2.** Richardson, C. (2018). *Microservices patterns*. Manning. [EN]  
**A3.** 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]  
**A4.** Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley. [EN]  
**A5.** Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley. [EN]  
**A6.** Newman, S. (2021). *Building microservices* (2nd). O'Reilly. [EN]  
**A7.** Kleppmann, M. (2017). *Designing data-intensive applications*. O'Reilly. [EN]  
**A8.** Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns*. Addison-Wesley. [EN]  
**A9.** 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]  
**A10.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A11.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]  
**A12.** Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution. [EN]
