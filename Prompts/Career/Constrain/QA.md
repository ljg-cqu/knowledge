# Constraint-Aware Architecture Q&A Generator

Generate 6-12 decision-critical Q&As for architects with constraint analysis—minimal viable set for informed decisions under time constraints.

## LLM Prompt Essentials

Ensure each Q&A:
1. Starts with complete context: problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.
2. Makes constraints explicit: name categories with magnitudes; aim for ≥2 categories per Q&A.
3. Quantifies trade-offs: compare ≥2 alternatives with concrete metrics, costs, risks; state assumptions.
4. Surfaces stakeholders and phases: map to SDLC phases and ≥2 stakeholders with concerns.
5. Uses structured, concise format: follow template; keep answers concise (typically 150-250 words); avoid repetition.
6. Includes citations and self-checks: cite ≥1 source per Q&A (≥2 for I/A); verify calculations, terminology, links.

## Context & Success Criteria

**Problem**: Architects face time-constrained decisions with multiple constraints, risking suboptimal outcomes without structured analysis.

**Audience**: Architects (5+ years), senior engineers.

**Scope**: 3-4 decision-critical dimensions × 4-5 constraint categories × 5 stakeholders × 4-5 SDLC phases.

**Output**: 6-12 Q&As (25/50/25% F/I/A) with quantified trade-offs (≥2 alternatives each) and citations.

**Assumptions**: Basic architecture knowledge.

**Stakeholders**: Architect, Developer, DevOps/SRE, Security, Leadership.

**Success Criteria**: 100% decision-critical Q&As with quantified trade-offs, ≥2 alternatives, full stakeholder coverage.

## Key Terms
- **F/I/A**: Foundation/Intermediate/Advanced difficulty.
- **SDLC Phases**: Design, Development, Testing, Deployment, Operations.
- **Decision-Critical**: Blocks decisions, creates risk, affects stakeholders, or reflects evolving constraints (>5% impact).
- **Quantified Trade-offs**: Explicit comparisons with metrics (e.g., +35ms latency, +40% ops complexity).
- **MECE**: Mutually Exclusive, Collectively Exhaustive.

## Coverage Requirements

### 3-4 Decision-Critical Dimensions (2-3 Q&As each)
1. **Structural & Quality**: Decomposition, modularity, performance, scalability, reliability.
2. **Data & Consistency**: Persistence, caching, consistency, partitioning.
3. **Integration & Evolution**: APIs, messaging, refactoring, migration, technical debt.
4. **(Optional) Behavioral**: Events, state, orchestration, error handling.

### 4-5 Constraint Categories (≥2 per Q&A; cover all overall)
- **Technical**: Hardware, platform, legacy.
- **Resource**: Deadlines, budget, team skills.
- **Business**: Pricing, market share, competition.
- **Compliance**: Regulations, data residency.
- **Operational**: SLOs, RTO/RPO, downtime.

### 5 Stakeholders (≥2 per Q&A; cover all)
Architect, Developer, DevOps/SRE, Security, Leadership.

## Content Standards

### Q&A Structure (Concise, typically 150-250 words)
1. **Header**: Difficulty | Dimension | Phase | Stakeholders | Decision Criticality.
2. **Key Insight**: Quantified trade-off (1 sentence).
3. **Constraints**: ≥1 category with magnitudes (aim ≥2).
4. **Body**: Context → Pattern → Trade-offs → Metrics → Impact.
5. **Code**: Optional 10-20 lines with error handling if clarifies constraints.
6. **Trade-offs**: ≥2 alternatives (Approach | Pros | Cons | Hardware | Budget | Business | Tag).
7. **Citations**: ≥1 (≥2 for I/A).

### Quality Standards
- **Traceability**: Requirements → Constraints → Pattern → Code → Metrics.
- **Quantified Trade-offs**: Explicit metrics comparisons.
- **Context Precision**: Specify magnitudes (e.g., "4-core CPU, $5K/mo budget, 99.9% SLA").
- **Balanced Analysis**: ≥2 alternatives; explicit assumptions; tags [Consensus]/[Context]/[Emerging].
- **Precise Language**: Define terms inline; consistent; concrete metrics; minimal jargon.
- **Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Event Sourcing, Sharding, Strangler Fig.

### References
- **Glossary**: ≥10 terms from Q&As; cover categories.
- **Tools**: ≥4 with valid URLs (<18mo old), pricing; decision-critical only.
- **Literature**: ≥5 canonical sources.
- **Citations**: ≥8 in APA 7th; mix EN/ZH/Other (≥2 languages); ≥50% <3yr old; 100% valid URLs.

---

# Generation Process

### 1. Plan
- Allocate 6-12 Q&As across 3-4 dimensions (25/50/25% F/I/A).
- Map 4-5 constraint categories, 5 stakeholders, 4-5 SDLC phases.
- Ensure decision criticality: all Q&As meet ≥1 criterion (blocks decision, creates risk, affects stakeholders, evolving constraints).

### 2. Build References
- Glossary: ≥10 terms from Q&As; cover categories.
- Tools: ≥4 with valid URLs (<18mo), pricing; decision-critical.
- Literature: ≥5 canonical sources.
- Citations: ≥8 in APA 7th; mix EN/ZH/Other (≥2 languages); ≥50% <3yr; valid URLs.

### 3. Write Q&As (Validate Every 3)
- Questions: ≥70% judgment-based with multi-dimensional constraints.
- Checkpoints: Concise answers | Citations | Syntax | Traceability | Quantified trade-offs | ≥2 constraints | ≥2 stakeholders | Decision criticality.
- Artifacts: ≥80% with diagram/table; add code if clarifies constraints.

### 4. Final Validation (All Pass)
- **Counts**: G≥10 | T≥4 | L≥5 | C≥8 | Q=6-12 (25/50/25% F/I/A).
- **Quality**: 100% citations (I/A ≥2) | ≥2 languages | ≥50% recent | 100% URLs.
- **Content**: Concise | 100% quantified | ≥70% judgment | ≥80% traceable/artifacts | 100% syntax.
- **Coverage**: 100% critical | ≥80% ≥2 constraints | All 5 stakeholders | 4-5 phases | ≥30% business.
- **Criteria**: Decision-critical, clear, accurate, balanced, practical, constraint-aware.
- Fix failures and re-validate.

---

## Templates

### Q&A
```
**Q**: [Judgment question with multi-dimensional constraints]
**Difficulty**: F/I/A | **Dimension**: [1-3] | **Phase**: [SDLC] | **Stakeholders**: [≥2]
**Decision Criticality**: [Blocks/Risk/Roles/Evolving]
**Key Insight**: [Quantified trade-off, 1 sentence]
**Constraints**: [Categories with magnitudes (≥2)]
**Answer** (concise): [Context → Pattern → Trade-offs → Metrics → Impact] [Ref: X]
**Code** (optional; 10-20 lines if clarifies): [Language + error handling]
**Trade-offs**: | Approach | Pros | Cons | Hardware | Budget | Business | Tag |
**Stakeholders**: [≥2 with concerns]
```

### References
- **Glossary** (≥10): Term → Definition.
- **Tools** (≥4): Name → Purpose | Updated | Pricing | URL.
- **Literature** (≥5): Author (Year). Title. Publisher.
- **Citations** (≥8): APA 7th; mix EN/ZH/Other (≥2 languages).

### Validation Report
```
**Counts**: G:X/10 | T:X/4 | L:X/5 | C:X/8 | Q:X/6-12 (F:X% I:X% A:X%)
**Quality**: Cites X% (100%, I/A ≥2) | Lang EN:X% ZH:X% Other:X% | Recent X% | URLs X%
**Content**: Concise X% | Quantified X% | Judgment X% | Trace X% | Artifacts X% | Syntax X%
**Coverage**: Critical X% | Constraints X% | Stakeholders X% | Phases X% | Business X%
**Status**: X/12 PASS | **Issues**: [List] | **Fix**: [Actions]
```

## Example Q&A

**Q**: How to design a scalable data processing system under budget and performance constraints?

**Difficulty**: I | **Dimension**: Structural & Quality | **Phase**: Design | **Stakeholders**: Architect, Developer, SRE

**Decision Criticality**: Blocks decision (performance bottleneck), Affects stakeholders (team scaling)

**Key Insight**: Microservices achieve 2x throughput on same budget, +20% latency, +30% operational complexity.

**Constraints**: **Technical**: 8-core CPU, 99.9% uptime | **Resource**: $10K/mo budget, 3-month timeline

**Answer** (180 words): Use microservices with API gateway for independent scaling. Commands via REST, events via message queue. Trade-offs: +20ms latency vs monolithic 50ms, +30% ops cost. Metrics: throughput 10K req/s, cost $9.5K/mo. Stakeholders: Dev (modularity), SRE (monitoring).

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| Microservices | Scalable, resilient | Complex ops | 70% CPU | $9.5K | +2x capacity | [Consensus] |
| Monolith | Simple | Limited scale | 90% CPU | $8K | Baseline | [Context] |

## References

### Glossary (≥10)
**G1. CQRS** – Separates commands/queries.
**G2. Event Sourcing** – State as event log.
... (additional terms as needed)

### Tools (≥4)
**T1. Mermaid** – Text diagrams. Free. https://mermaid.js.org
**T2. ADR** – Decision records. Free. https://adr.github.io
... (additional tools)

### Literature (≥5)
**L1.** Evans (2003). *Domain-Driven Design*. Addison-Wesley
**L2.** Richardson (2018). *Microservices Patterns*. Manning
... (additional sources)

### Citations (≥8)
**A1.** Evans (2003). *Domain-driven design*. Addison-Wesley [EN]
**A2.** Richardson (2018). *Microservices patterns*. Manning [EN]
... (additional citations)
