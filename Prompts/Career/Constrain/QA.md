---
last_updated: 2025-11-18
status: Reviewed
owner: ljg-cqu
---

# Constraint-Aware Architecture Interview Q&A Generator

Generate 25-30 Q&As for senior/architect roles with constraint analysis across 8 categories, 10 stakeholder roles, 8 SDLC phases.

## Context & Success Criteria

**Audience**: Senior devs (5+ years), architects  
**Scope**: 6 dimensions × 8 constraint categories × 10 stakeholders × 8 SDLC phases  
**Output**: 25-30 Q&As (20/40/40% F/I/A) | Production code | Quantified trade-offs (≥2) | Citations

**Difficulty Levels**:
- **F** = Foundational (execution-level tasks)
- **I** = Intermediate (strategy/trade-offs)
- **A** = Advanced (portfolio/vision/P&L)

**Assumptions**: Distributed systems (>10K rps, >1TB data) | Go/Java/Python/TypeScript | Cloud-native  
**Validation**: 25/25 checks PASS | 8/8 criteria met

**Decision-Criticality** (include if ≥1 criterion satisfied):
- **Blocks Decision**: Impacts architecture approach, constraint resolution, or trade-off choices
- **Creates Risk**: Material threat (constraint violations, SLA breaches, budget overruns, compliance gaps)
- **Affects ≥2 Stakeholder Roles**: Multi-team impact (e.g., Architect + DevOps, PM + Compliance)
- **Requires Action**: 1-6mo implementation window (not theoretical)
- **Quantified Impact**: Measurable constraint metrics (SLO %, cost $, resource utilization %, compliance deadlines)

---

# Coverage Requirements

## 6 Dimensions (4-6 Q&As each)
1. **Structural**: Decomposition, modularity, coupling, boundaries
2. **Behavioral**: Events, state, orchestration, error handling
3. **Quality**: Performance, scalability, reliability, security
4. **Data**: Persistence, caching, consistency, partitioning
5. **Integration**: APIs, messaging, protocols
6. **Evolution**: Refactoring, migration, technical debt

## 8 Constraint Categories (≥3/Q&A, all 8 overall)

| Category | Examples |
|----------|----------|
| **Technical** | CPU/mem/storage/network, platform, legacy APIs, versions |
| **Resource** | Deadlines, budget ($X/mo), team size/skills |
| **Business** | Pricing, CAC/LTV, market share, competitive SLAs |
| **Organizational** | Stakeholder roles, workflows, standards, risk appetite |
| **Compliance** | GDPR, HIPAA, PCI-DSS, SOC 2, audit logs, data residency |
| **Operational** | SLOs, RTO/RPO, downtime windows, 30% headroom |
| **Ecosystem** | Cloud lock-in, SaaS limits, OSS health, talent |
| **Lifecycle** | Requirements→Design→Dev→Testing→Deploy→Ops→Maintenance→Evolution |

## 10 Stakeholders (≥2/Q&A, all 10 overall)
BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

---

# Content Standards

## Q&A Structure (150-300 words)
1. **Header**: Difficulty | Dimension | Phase | Stakeholders
2. **Key Insight**: Quantified trade-off (1 sentence)
3. **Constraints**: ≥3 categories with magnitudes
4. **Body**: Context → Pattern → Trade-offs → Metrics → Assumptions → Stakeholder impact
5. **Code**: 10-30 lines with error handling + optimizations
6. **Metrics**: Formula | Variables | Target | Constraint impact
7. **Trade-offs**: ≥2 alternatives (Approach | Pros | Cons | Hardware | Budget | Business | Tag)
8. **Citations**: ≥1 (≥2 for advanced)

## Quality Standards
- **Traceability**: Requirements → Constraints → Pattern → Code → Metrics
- **Quantified Trade-offs**: ✅ "CQRS: 10x read, +35ms write, +40% ops" ❌ "complex"
- **Context Precision**: Specify magnitudes ("4-core CPU, $5K/mo, 99.9% SLA, HIPAA, 8-person, 4mo")
- **Balanced Analysis**: ≥2 alternatives; explicit assumptions/limitations; [Consensus]/[Context]/[Emerging] tags
- **Precise Language**: Define terms inline; consistent terminology; concrete metrics ("<300ms p95"); minimal jargon
- **Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Event Sourcing, Sharding, Strangler Fig

## References (G≥20 | T≥5 | L≥6 | C≥12)

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | 20 | Terms + relationships; cover all 8 categories + 10 stakeholders |
| **Tools** | 5 | Valid URL, updated ≤18mo, pricing |
| **Literature** | 6 | Fowler, Evans, Vernon, Richardson, Newman, Kleppmann |
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
- **Checkpoints**: Words 150-300 | Citations | Syntax | Traceability | Quantified | Constraints (≥3/Q&A) | Stakeholders (≥2/Q&A) | Phases | Hardware ≥40%

## 4. Artifacts & Links
- Per cluster: Mermaid (<120 nodes) + code + metrics + trade-offs
- Verify [Ref: ID] resolved, 100% valid URLs

## 5. Final Validation (25/25 PASS)

**Counts**: G≥20 | T≥5 | L≥6 | C≥12 | Q=25-30 (20/40/40%)  
**Quality**: Citations ≥70% | EN 60%/ZH 30%/Other 10% | Recency ≥50% | URLs 100% | Cross-refs 100%  
**Content**: Words 150-300 | Quantified 100% | Judgment ≥70% | Traceability ≥80% | Artifacts ≥90% | Syntax 100%  
**Coverage**: Constraints (≥80% Q&As ≥3) | Stakeholders all 10 | Phases all 8 | Hardware ≥40% | Business ≥30% | Ecosystem ≥30%  
**Criteria**: Clarity | Accuracy | Completeness | Balance | Practicality | Self-Correction | Constraint-Awareness | Stakeholder-Awareness

**Failure**: ANY fail → Fix → Re-validate ALL

---

# Templates

## Q&A
```
**Q**: [Judgment question with multi-dimensional constraints]
**Difficulty**: F/I/A | **Dimension**: [1-6] | **Phase**: [SDLC] | **Stakeholders**: [≥2]
**Key Insight**: [Quantified trade-off, 1 sentence]
**Constraints**: [≥3 categories with magnitudes]
**Answer** (150-300 words): [Context → Pattern → Trade-offs → Metrics → Assumptions → Impact] [Ref: X]
**Code** (10-30 lines): [Language + error handling + optimizations]
**Metrics**: [Formula | Variables | Target | Constraint impact]
**Trade-offs**: | Approach | Pros | Cons | Hardware | Budget | Business | Tag |
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
**Coverage**: Constraints X% | Stakeholders X% | Phases X% | HW X% | Biz X% | Eco X%
**Status**: X/25 PASS | X/8 MET | **Issues**: [List] | **Fix**: [Actions]
```

# Example

## Q: Design high-throughput order processing for regulated healthcare marketplace under hardware/compliance constraints?

**Difficulty**: A | **Dimension**: Structural+Data | **Phase**: Design, Dev, Ops | **Stakeholders**: Arch, Dev, Sec, Data, SRE, Lead

**Key Insight**: Event-driven CQRS achieves 15K rps on 4-core (+180% vs monolith), +35ms write latency, +40% ops complexity, HIPAA-compliant.

**Constraints**: **Technical**: 4-core, 16GB, 500 IOPS | **Resource**: $8K/mo, 8 devs, 1 SRE, 4mo | **Business**: $500K/mo, 15% share, <200ms SLA | **Compliance**: HIPAA, SOC 2 | **Operational**: 99.9% | **Ecosystem**: AWS, Kafka OSS, SOAP legacy

**Answer** (280 words): CQRS with event sourcing: commands → append-only store (HIPAA audit), queries → materialized views (cached). Independent scaling (3 write, 6 read) within $8K/mo, <200ms latency [Ref: A2, A7]. Stack: Kafka OSS (PHI encrypted TLS 1.3), PostgreSQL (events), Redis (reads). Legacy SOAP via anti-corruption layer + circuit breaker. Trade-offs: +35ms write (vs 2s baseline), +40% ops (team Kafka experience), +60% storage ($2.4K/mo). Impact: +$150K/mo capacity, 4mo feasible [Ref: A4]. Metrics: p95 write 180ms, reads 25ms, CPU 65%, $7.8K/mo. Stakeholder alignment: Sec (encrypted), SRE (runbooks), PM (timeline), Lead (ROI). Limits: 5GB/day growth → partition at 18mo; <500ms eventual consistency unsuitable for real-time inventory.

**Code** (Go):
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

**Metrics**: p95 write: validate(15) + encrypt(10) + append(120) + ack(35) = 180ms | Target <300ms | 4-core limits validation, encryption +10ms

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| CQRS+ES | +180% throughput, audit | +35ms write, +40% ops | 65% CPU (3×4-core), 5GB/day | $7.8K | +$150K/mo, 4mo, <200ms | [Consensus] |
| Monolith | Simple, 145ms write | Max 5.5K rps | 85% CPU (1×4-core), 1.5GB/day | $4.5K | $275K/mo max | [Context] |

**Stakeholders**: **PM**: 4mo, parity | **Arch**: Balances throughput/complexity/team | **Dev**: Kafka XP mitigates ops | **Sec**: TLS 1.3 HIPAA | **SRE**: Circuit breaker + 30% headroom | **Lead**: ROI 18mo

## Glossary
**G1. Hexagonal** [EN] – Core isolation via ports/adapters. Related: DI  
**G2. CQRS** [EN] – Separates commands/queries. Related: Event Sourcing  
**G3. Event Sourcing** [EN] – State as event log. Audit, temporal queries. Related: CQRS  
**G4. DDD** [EN] – Domain modeling: language, contexts, aggregates. Related: Bounded Context  
**G5. Bounded Context** [EN] – Model boundary for consistency. Related: Context Map  
**G6. Aggregate** [EN] – Consistency boundary (root + entities/VOs). Related: Repository  
**G7. Repository** [EN] – Data access abstraction for aggregates  
**G8. Domain Event** [EN] – Immutable fact. Decoupling, eventual consistency. Related: Event Sourcing  
**G9. Saga** [EN] – Long transactions with compensations. Related: Distributed TX  
**G10. Circuit Breaker** [EN] – Prevents cascading failures. Related: Bulkhead  
**G11. Technical Constraint** [EN] – CPU/mem/storage/network/platform/legacy/versions. Related: Performance Budget  
**G12. Resource Constraint** [EN] – Time/budget/team limits. Deadlines, costs, skills. Related: Scope  
**G13. Business Constraint** [EN] – Revenue, competitive, continuity. Pricing, CAC/LTV, share, features. Related: Product  
**G14. Organizational Constraint** [EN] – Stakeholder/process/governance. Workflows, standards, risk. Related: RACI  
**G15. Compliance Constraint** [EN] – Legal/regulatory. GDPR, HIPAA, PCI-DSS, SOC 2, residency, audit. Related: Security  
**G16. Operational Constraint** [EN] – Runtime limits. SLOs, RTO/RPO, downtime, headroom. Related: SRE  
**G17. Ecosystem Constraint** [EN] – Vendor/OSS/partner dependencies. Lock-in, API limits, OSS health, talent. Related: Vendor  
**G18. Lifecycle Constraint** [EN] – Phase-specific SDLC limits. Requirements→Evolution. Related: SDLC  
**G19. Stakeholder** [EN] – Role: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead. Related: RACI  
**G20. Lifecycle Phase** [EN] – 8 phases: Requirements→Design→Dev→Test→Deploy→Ops→Maintenance→Evolution. Related: SDLC

## Tools
**T1. Mermaid** – Text diagrams. GitHub-native. 2024-10. Free. https://mermaid.js.org  
**T2. OpenAPI** – REST spec. Codegen, testing. 2024-09. Free. https://www.openapis.org  
**T3. JSON Schema** – JSON validation. 2024-08. Free. https://json-schema.org  
**T4. Kubernetes** – Container orchestration. 2024-10. Free. https://kubernetes.io  
**T5. ADR** – Decision log. Traceability. 2024-06. Free. https://adr.github.io

## Literature
**L1.** Evans (2003). *Domain-Driven Design*. Addison-Wesley – Strategic/tactical modeling  
**L2.** Vernon (2013). *Implementing DDD*. Addison-Wesley – Context mapping, aggregates  
**L3.** Richardson (2018). *Microservices Patterns*. Manning – Decomposition, trade-offs  
**L4.** Newman (2021). *Building Microservices* (2nd). O'Reilly – Boundaries, deployment  
**L5.** Kleppmann (2017). *Data-Intensive Apps*. O'Reilly – Replication, partitioning  
**L6.** Fowler (2002). *Enterprise Architecture*. Addison-Wesley – Repository, Service Layer

## Citations
**A1.** Evans (2003). *Domain-driven design*. Addison-Wesley [EN]  
**A2.** Richardson (2018). *Microservices patterns*. Manning [EN]  
**A3.** 周爱民 (2021). *架构的本质*. 电子工业 [ZH]  
**A4.** Vernon (2013). *Implementing DDD*. Addison-Wesley [EN]  
**A5.** Fowler (2002). *Enterprise architecture*. Addison-Wesley [EN]  
**A6.** Newman (2021). *Building microservices*. O'Reilly [EN]  
**A7.** Kleppmann (2017). *Data-intensive apps*. O'Reilly [EN]  
**A8.** Hohpe & Woolf (2003). *Integration patterns*. Addison-Wesley [EN]  
**A9.** 张逸 (2019). *领域驱动实践*. 电子工业 [ZH]  
**A10.** Skelton & Pais (2019). *Team topologies*. IT Revolution [EN]  
**A11.** Humble & Farley (2010). *Continuous delivery*. Addison-Wesley [EN]  
**A12.** Kim et al. (2016). *DevOps handbook*. IT Revolution [EN]
