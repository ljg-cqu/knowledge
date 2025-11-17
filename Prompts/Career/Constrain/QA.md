# Constraint-Aware Architecture Q&A Generator (Minimal Viable)

Generate 6-12 decision-critical Q&As for architects with constraint analysis—minimal viable set for informed decisions with time constraints.

## LLM-Friendly Prompts Guidelines

To ensure high-quality, hallucination-free output with improved decision quality, follow these guidelines when generating the Q&As:

1. **Context**: State problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.
2. **Clarity**: Define key terms and relationships; use diagrams for complex concepts.
3. **Precision**: Use exact metrics, formulas, units; use math blocks for complex formulas.
4. **Relevance**: Focus on essential information; move non-critical details to appendices.
5. **MECE**: Ensure sections are distinct with no gaps or overlaps.
6. **Sufficiency**: Cover all necessary dimensions (what, why, how, when, who, constraints, alternatives, risks, outcomes).
7. **Breadth**: Include relevant stakeholder perspectives.
8. **Depth**: Request implementation-level detail for high-impact areas.
9. **Significance**: Focus on high-impact items; deemphasize low-impact details.
10. **Priority**: Order by importance; label priority levels explicitly (critical/important/optional).
11. **Conciseness**: Eliminate redundancy; state each concept once.
12. **Accuracy**: Verify facts against authoritative sources.
13. **Credibility**: Cite recent (2023+) primary sources.
14. **Logic**: Provide coherent arguments with explicit trade-offs.
15. **Risk/Value**: Compare ≥2 alternatives with costs, benefits, risks.
16. **Fairness**: Provide balanced view with counterarguments, limitations.
17. **Structure**: Use headings, lists, tables, diagrams.
18. **Consistency**: Use consistent hierarchy and formatting.
19. **Evidence**: Provide structured citations with source details, recency, uncertainty flags.
20. **Verification**: Self-review and error checking.
21. **Practicality**: Provide concrete steps, examples, tools, commands.
22. **Success Criteria**: Define measurable outcomes with baselines, targets.

## Table of Contents
- [Context & Success Criteria](#context--success-criteria)
- [Coverage Requirements](#coverage-requirements)
- [Content Standards](#content-standards)
- [Generation Process](#generation-process)
- [Templates](#templates)
- [Example](#example)
- [References](#references)
- [Self-Assessment](#self-assessment)

## Context & Success Criteria

**Problem**: Architects face time-constrained decisions in distributed systems with multiple constraints, risking suboptimal outcomes without structured analysis.

**Audience**: Architects (5+ years), senior engineers

**Scope**: 3-4 decision-critical dimensions × 4-5 constraint categories × ≥5 core stakeholders × 4-5 SDLC phases

**Output**: 6-12 Q&As (25/50/25% F/I/A) | Quantified trade-offs (≥2) | Citations

**Assumptions**: Distributed systems (>10K rps, >1TB data) | Go/Java/Python/TypeScript | Cloud-native | Timeline: 30-60min generation

**Constraints**: Assumes basic architecture knowledge

**Stakeholders**: Architects, Developers, SRE, Security, Leadership

**Resources**: Any LLM; no cost

**Validation**: 12/12 checks PASS | 6/6 criteria met

**Success Criteria**: 100% decision-critical Q&As (baseline: 80%), ≥80% quantified trade-offs (baseline: 60%), p95 generation time <60min (baseline: 90min), stakeholder coverage 100% (baseline: 80%)

## Key Terms
- **F/I/A**: Foundation/Intermediate/Advanced difficulty levels
- **SDLC Phases**: Software Development Life Cycle phases (Design, Development, Testing, Deployment, Operations)
- **Decision-Critical**: >5% impact or blocks key decisions
- **Quantified Trade-offs**: Explicit comparisons with metrics (e.g., +35ms latency, +40% ops complexity)
- **MECE**: Mutually Exclusive, Collectively Exhaustive coverage

---

# Coverage Requirements

## 3-4 Decision-Critical Dimensions (2-3 Q&As each)
1. **Structural & Quality**: Decomposition, modularity, performance, scalability, reliability
2. **Data & Consistency**: Persistence, caching, consistency, partitioning
3. **Integration & Evolution**: APIs, messaging, refactoring, migration, technical debt
4. *(Optional) Behavioral*: Events, state, orchestration, error handling

## 4-5 Decision-Critical Constraint Categories (≥2/Q&A, all covered)

| Category | Examples | Decision Criticality |
|----------|----------|---------------------|
| **Technical** | CPU/mem/storage/network, platform, legacy APIs, versions | Blocks architecture, adoption barrier |
| **Resource** | Deadlines, budget ($X/mo), team size/skills | Blocks feasibility, timeline risk |
| **Business** | Pricing, CAC/LTV, market share, competitive SLAs | Blocks roadmap, revenue impact |
| **Compliance** | GDPR, HIPAA, PCI-DSS, SOC 2, audit logs, data residency | Creates regulatory risk |
| **Operational** | SLOs, RTO/RPO, downtime windows, 30% headroom | Blocks reliability decisions |

## 5 Core Stakeholders (≥2/Q&A, all 5 covered)
Architect, Developer, DevOps/SRE, Security, Leadership

---

# Content Standards

## Q&A Structure (150-250 words, Minimal Viable)
1. **Header**: Difficulty | Dimension | Phase | Stakeholders | Decision Criticality
2. **Key Insight**: Quantified trade-off (1 sentence)
3. **Constraints**: ≥2 decision-critical categories with magnitudes
4. **Body**: Context → Pattern → Trade-offs → Metrics → Stakeholder impact
5. **Code**: 10-20 lines with error handling (optional for F)
6. **Trade-offs**: ≥2 alternatives (Approach | Pros | Cons | Hardware | Budget | Business | Tag)
7. **Citations**: ≥1 (≥2 for I/A)

## Quality Standards
- **Traceability**: Requirements → Constraints → Pattern → Code → Metrics
- **Quantified Trade-offs**: ✅ "CQRS: 10x read, +35ms write, +40% ops" ❌ "complex"
- **Context Precision**: Specify magnitudes ("4-core CPU, $5K/mo, 99.9% SLA, HIPAA, 8-person, 4mo")
- **Balanced Analysis**: ≥2 alternatives; explicit assumptions/limitations; [Consensus]/[Context]/[Emerging] tags
- **Precise Language**: Define terms inline; consistent terminology; concrete metrics ("<300ms p95"); minimal jargon
- **Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Event Sourcing, Sharding, Strangler Fig

## References (Minimal Viable Set)

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | 10 | Only terms used in Q&As; cover decision-critical categories |
| **Tools** | 4 | Valid URL, updated ≤18mo, pricing, decision-critical only |
| **Literature** | 5 | Canonical sources: Fowler, Evans, Vernon, Richardson, Newman |
| **Citations** | 8 | APA 7th; 60% EN/30% ZH/10% other; ≥50% last 3yr; 100% valid URLs |

---

# Generation Process

## 1. Plan (Minimal Viable)
- Allocate 6-12 Q&As across 3-4 dimensions (25/50/25% F/I/A)
- Map 4-5 decision-critical constraint categories + 5 core stakeholders + 4-5 phases
- Verify decision criticality: all Q&As satisfy ≥1 criterion (Blocks decision, Creates risk, Affects stakeholders, Actively evolving)

## 2. Build References (Minimal)
- Glossary: Only terms used in Q&As; decision-critical categories
- Tools: URL, updated ≤18mo, pricing, decision-critical only
- Literature: Canonical sources only
- Citations: APA 7th, 60/30/10% EN/ZH/Other, ≥50% last 3yr, valid URLs

## 3. Write Q&As (Validate Every 3)
- **Questions**: ≥70% judgment ("How/When/Compare..."); multi-dimensional constraints
- **Checkpoints**: Words 150-250 | Citations | Syntax | Traceability | Quantified | Constraints (≥2/Q&A) | Stakeholders (≥2/Q&A) | Decision Criticality ✓

## 4. Artifacts & Links
- For ≥80% Q&As: Mermaid diagram + code (optional for F) + trade-offs table
- Verify [Ref: ID] resolved, 100% valid URLs

## 5. Final Validation (12/12 PASS)

**Counts**: G≥10 | T≥4 | L≥5 | C≥8 | Q=6-12 (25/50/25%)
**Quality**: Citations ≥80% | EN 60%/ZH 30%/Other 10% | Recency ≥50% | URLs 100% | Cross-refs 100%
**Content**: Words 150-250 | Quantified 100% | Judgment ≥70% | Traceability ≥80% | Artifacts ≥80% | Syntax 100%
**Coverage**: Decision Criticality 100% | Constraints (≥80% Q&As ≥2) | Stakeholders all 5 | Phases 4-5 | Business ≥30%
**Criteria**: Decision-Critical | Clarity | Accuracy | Balance | Practicality | Constraint-Awareness

**Failure**: ANY fail → Fix → Re-validate ALL

---

# Templates

## Q&A (Minimal Viable)
```
**Q**: [Judgment question with multi-dimensional constraints]
**Difficulty**: F/I/A | **Dimension**: [1-3] | **Phase**: [SDLC] | **Stakeholders**: [≥2]
**Decision Criticality**: [Blocks/Risk/Roles/Evolving]
**Key Insight**: [Quantified trade-off, 1 sentence]
**Constraints**: [≥2 decision-critical categories with magnitudes]
**Answer** (150-250 words): [Context → Pattern → Trade-offs → Metrics → Impact] [Ref: X]
**Code** (10-20 lines, optional for F): [Language + error handling]
**Trade-offs**: | Approach | Pros | Cons | Hardware | Budget | Business | Tag |
**Stakeholders**: [≥2 with concerns]
```

## References (Minimal Viable)
- **Glossary** (≥10): Term [EN/ZH] → Definition + Context (only terms used in Q&As)
- **Tools** (≥4): Name → Purpose | Updated | Pricing | URL
- **Literature** (≥5): Author (Year). Title. Publisher (canonical only)
- **Citations** (≥8): APA 7th, 60/30/10% EN/ZH/Other

## Validation Report (Minimal Viable)
```
**Counts**: G:X/10 | T:X/4 | L:X/5 | C:X/8 | Q:X/6-12 (F:X% I:X% A:X%)
**Quality**: Cites X% | Lang EN:X% ZH:X% | Recent X% | URLs X% | Links X%
**Content**: Words X% | Quantified X% | Judgment X% | Trace X% | Artifacts X% | Syntax X%
**Coverage**: Decision Criticality X% | Constraints X% | Stakeholders X% | Phases X% | Business X%
**Status**: X/12 PASS | X/6 MET | **Issues**: [List] | **Fix**: [Actions]
```

# Example

## Q: Design high-throughput order processing for regulated healthcare marketplace under hardware/compliance constraints?

**Difficulty**: A | **Dimension**: Structural & Quality | **Phase**: Design, Dev | **Stakeholders**: Arch, Dev, Sec, Lead
**Decision Criticality**: Blocks architecture (15K rps requirement), Creates risk (HIPAA compliance)

**Key Insight**: Event-driven CQRS achieves 15K rps on 4-core (+180% vs monolith), +35ms write latency, +40% ops complexity, HIPAA-compliant.

**Constraints**: **Technical**: 4-core, 16GB, 500 IOPS | **Resource**: $8K/mo, 4mo | **Compliance**: HIPAA, SOC 2

**Answer** (220 words): CQRS with event sourcing: commands → append-only store (HIPAA audit), queries → materialized views (cached). Independent scaling (3 write, 6 read) within $8K/mo, <200ms latency [Ref: A2]. Stack: Kafka OSS (PHI encrypted TLS 1.3), PostgreSQL (events), Redis (reads). Legacy SOAP via anti-corruption layer + circuit breaker. Trade-offs: +35ms write (vs 145ms monolith baseline), +40% ops (team Kafka experience). Impact: +$150K/mo capacity, 4mo feasible [Ref: A4]. Metrics: p95 write 180ms, reads 25ms, CPU 65%, $7.8K/mo. Stakeholder alignment: Sec (encrypted), Lead (ROI). Limits: 5GB/day growth → partition at 18mo.

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

## Glossary (Minimal Viable - Only Terms Used in Q&As)
**G1. CQRS** [EN] – Separates commands/queries. Related: Event Sourcing
**G2. Event Sourcing** [EN] – State as event log. Audit, temporal queries. Related: CQRS
**G3. Circuit Breaker** [EN] – Prevents cascading failures. Related: Bulkhead
**G4. Technical Constraint** [EN] – CPU/mem/storage/network/platform/legacy/versions. Related: Performance Budget
**G5. Resource Constraint** [EN] – Time/budget/team limits. Deadlines, costs, skills. Related: Scope
**G6. Business Constraint** [EN] – Revenue, competitive, continuity. Pricing, CAC/LTV, share, features. Related: Product
**G7. Compliance Constraint** [EN] – Legal/regulatory. GDPR, HIPAA, PCI-DSS, SOC 2, residency, audit. Related: Security
**G8. Operational Constraint** [EN] – Runtime limits. SLOs, RTO/RPO, downtime, headroom. Related: SRE
**G9. Trade-off** [EN] – Quantified choice between ≥2 approaches with explicit pros/cons. Related: Decision
**G10. Decision Criticality** [EN] – Criterion for Q&A inclusion: Blocks decision, Creates risk, Affects stakeholders, Actively evolving. Related: Priority

## Tools (Minimal Viable - Decision-Critical Only)
**T1. Mermaid** – Text diagrams. GitHub-native. 2024-10. Free. https://mermaid.js.org
**T2. ADR** – Decision log. Traceability. 2024-06. Free. https://adr.github.io
**T3. OpenAPI** – REST spec. Codegen, testing. 2024-09. Free. https://www.openapis.org
**T4. Kubernetes** – Container orchestration. 2024-10. Free. https://kubernetes.io

## Literature (Minimal Viable - Canonical Only)
**L1.** Evans (2003). *Domain-Driven Design*. Addison-Wesley – Strategic/tactical modeling
**L2.** Richardson (2018). *Microservices Patterns*. Manning – Decomposition, trade-offs
**L3.** Kleppmann (2017). *Data-Intensive Apps*. O'Reilly – Replication, partitioning
**L4.** Newman (2021). *Building Microservices* (2nd). O'Reilly – Boundaries, deployment
**L5.** Fowler (2002). *Enterprise Architecture*. Addison-Wesley – Repository, Service Layer

## Citations (Minimal Viable)
**A1.** Evans (2003). *Domain-driven design*. Addison-Wesley [EN]
**A2.** Richardson (2018). *Microservices patterns*. Manning [EN]
**A3.** Kleppmann (2017). *Data-intensive apps*. O'Reilly [EN]
**A4.** Vernon (2013). *Implementing DDD*. Addison-Wesley [EN]
**A5.** Newman (2021). *Building microservices*. O'Reilly [EN]
**A6.** Fowler (2002). *Enterprise architecture*. Addison-Wesley [EN]
**A7.** 周爱民 (2021). *架构的本质*. 电子工业 [ZH]
**A8.** 张逸 (2019). *领域驱动实践*. 电子工业 [ZH]

## Self-Assessment
**Accurate** | **Precise** | **Cited** | **Complete** (MECE) | **Actionable** | **Consistent** | **Relevant** | **Balanced** | **Recent** (2023+) | **Testable**

**Trade-offs**:
- **Rigor vs. Speed**: Detailed validation increases upfront time but reduces iteration
- **Depth vs. Breadth**: Implementation details may be too long for some uses
- **Precision vs. Accessibility**: Technical specificity may reduce readability

**Limitations**: Metrics lack external validation; single framework (no alternatives compared); observational only

**Future**: A/B testing, framework comparison, success criteria, user feedback
