# Constraint-Aware Architecture Q&A Generator

Generate decision-critical Q&As for architects on constraint analysis to enable informed decisions under time constraints.

## Essentials

Each Q&A must include:
- Complete context: problem, scope, constraints, assumptions, scale, timeline, stakeholders, resources.
- ≥2 explicit constraints with magnitudes.
- Quantified trade-offs: ≥2 alternatives with metrics, costs, risks; state assumptions.
- Mapping to SDLC phases and ≥2 stakeholders with concerns.
- Structured, concise format; avoid repetition.
- ≥1 citation (≥2 for I/A); verify accuracy.

## Context & Success Criteria

**Problem**: Time-constrained decisions with multiple constraints risk suboptimal outcomes without structured analysis.

**Audience**: Architects (5+ years), senior engineers.

**Scope**: 3-4 dimensions × 4-5 constraint categories × 5 stakeholders × 4-5 SDLC phases.

**Output**: Q&As (balanced F/I/A) with ≥2 quantified alternatives each.

**Assumptions**: Basic architecture knowledge.

**Stakeholders**: Architect, Developer, DevOps/SRE, Security, Leadership.

**Success Criteria**: All Q&As decision-critical with quantified trade-offs, ≥2 alternatives, full stakeholder coverage.

## Key Terms
- **F/I/A**: Foundation/Intermediate/Advanced.
- **SDLC Phases**: Design, Development, Testing, Deployment, Operations.
- **Decision-Critical**: Blocks decisions, creates risk, affects stakeholders, or reflects evolving constraints (>5% impact).
- **Quantified Trade-offs**: Explicit comparisons (e.g., +35ms latency, +40% ops complexity).
- **MECE**: Mutually Exclusive, Collectively Exhaustive.

## Coverage Requirements

### Dimensions
1. **Structural & Quality**: Decomposition, modularity, performance, scalability, reliability.
2. **Data & Consistency**: Persistence, caching, consistency, partitioning.
3. **Integration & Evolution**: APIs, messaging, refactoring, migration, technical debt.
4. **(Optional) Behavioral**: Events, state, orchestration, error handling.

### Constraint Categories (≥2 per Q&A)
- **Technical**: Hardware, platform, legacy.
- **Resource**: Deadlines, budget, team skills.
- **Business**: Pricing, market share, competition.
- **Compliance**: Regulations, data residency.
- **Operational**: SLOs, RTO/RPO, downtime.

## Content Standards

### Q&A Structure
1. **Header**: Difficulty | Dimension | Phase | Stakeholders | Decision Criticality.
2. **Key Insight**: Quantified trade-off (1 sentence).
3. **Constraints**: ≥2 categories with magnitudes.
4. **Body**: Context → Pattern → Trade-offs → Metrics → Impact.
5. **Code**: Optional snippet with error handling if clarifies.
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
- **Glossary**: Key terms from Q&As.
- **Tools**: Relevant tools with URLs, pricing.
- **Literature**: Canonical sources.
- **Citations**: APA 7th; mix languages; prefer recent; valid URLs.

## Generation Process

### 1. Plan
- Allocate Q&As across dimensions (balanced F/I/A).
- Map constraint categories, stakeholders, SDLC phases.
- Ensure decision-critical focus.

### 2. Build References
- Glossary: Key terms.
- Tools: Relevant with URLs, pricing.
- Literature: Canonical sources.
- Citations: APA 7th; mix languages; recent; valid URLs.

### 3. Write Q&As
- Questions: Judgment-based with multi-dimensional constraints.
- Checkpoints: Concise, cited, syntactically correct, traceable, quantified trade-offs, ≥2 constraints, ≥2 stakeholders, decision-critical.
- Artifacts: Diagrams/tables; code if clarifies.

### 4. Validate
- Ensure quantified trade-offs, citations, balance, coverage.
- Fix issues and re-validate.

## Templates

### Q&A
```
**Q**: [Judgment question with multi-dimensional constraints]
**Difficulty**: F/I/A | **Dimension**: [1-3] | **Phase**: [SDLC] | **Stakeholders**: [≥2]
**Decision Criticality**: [Blocks/Risk/Roles/Evolving]
**Key Insight**: [Quantified trade-off, 1 sentence]
**Constraints**: [≥2 categories with magnitudes]
**Answer**: [Context → Pattern → Trade-offs → Metrics → Impact] [Ref: X]
**Code** (optional): [Snippet with error handling if clarifies]
**Trade-offs**: | Approach | Pros | Cons | Hardware | Budget | Business | Tag |
**Stakeholders**: [≥2 with concerns]
```

### References
- **Glossary**: Term → Definition.
- **Tools**: Name → Purpose | Updated | Pricing | URL.
- **Literature**: Author (Year). Title. Publisher.
- **Citations**: APA 7th; mix languages.

### Validation Report
```
**Counts**: G:X | T:X | L:X | C:X | Q:X (F:X% I:X% A:X%)
**Quality**: Cites X% (I/A ≥2) | Lang EN:X% ZH:X% Other:X% | Recent X% | URLs X%
**Content**: Concise X% | Quantified X% | Judgment X% | Trace X% | Artifacts X% | Syntax X%
**Coverage**: Critical X% | Constraints X% | Stakeholders X% | Phases X% | Business X%
**Status**: X PASS | **Issues**: [List] | **Fix**: [Actions]
```

## Example Q&A

**Q**: How to design a scalable data processing system under budget and performance constraints?

**Difficulty**: I | **Dimension**: Structural & Quality | **Phase**: Design | **Stakeholders**: Architect, Developer, SRE

**Decision Criticality**: Blocks decision (performance bottleneck), Affects stakeholders (team scaling)

**Key Insight**: Microservices achieve 2x throughput on same budget, +20% latency, +30% operational complexity.

**Constraints**: **Technical**: 8-core CPU, 99.9% uptime | **Resource**: $10K/mo budget, 3-month timeline

**Answer**: Use microservices with API gateway for independent scaling. Commands via REST, events via message queue. Trade-offs: +20ms latency vs monolithic 50ms, +30% ops cost. Metrics: throughput 10K req/s, cost $9.5K/mo. Stakeholders: Dev (modularity), SRE (monitoring).

**Trade-offs**:
| Approach | Pros | Cons | Hardware | Budget | Business | Tag |
|----------|------|------|----------|--------|----------|-----|
| Microservices | Scalable, resilient | Complex ops | 70% CPU | $9.5K | +2x capacity | [Consensus] |
| Monolith | Simple | Limited scale | 90% CPU | $8K | Baseline | [Context] |

## References

### Glossary
**CQRS** – Separates commands/queries.
**Event Sourcing** – State as event log.
... (additional terms)

### Tools
**Mermaid** – Text diagrams. Free. https://mermaid.js.org
**ADR** – Decision records. Free. https://adr.github.io
... (additional tools)

### Literature
Evans (2003). *Domain-Driven Design*. Addison-Wesley
Richardson (2018). *Microservices Patterns*. Manning
... (additional sources)

### Citations
Evans (2003). *Domain-driven design*. Addison-Wesley [EN]
Richardson (2018). *Microservices patterns*. Manning [EN]
... (additional citations)
