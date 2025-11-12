# Software Architecture Interview Q&A Generator

Generate 25-30 interview Q&A pairs for senior/architect/expert roles demonstrating architecture-to-code translation.

## Scope & Success Criteria

**Audience**: Senior developers (5+ years), architects, technical experts  
**Output**: 25-30 Q&As across 6 MECE dimensions with production code, quantified trade-offs, ≥2 alternatives, citations  
**Success**: 19/19 validation checks PASS

**Assumptions**: Distributed systems (>10K rps, >1TB data), idiomatic Go/Java/Python/TypeScript, cloud-native context, foundational knowledge (layered, MVC, REST)

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Total Count** | 25-30 |
| **Difficulty Mix** | 20% Foundational (core concepts) / 40% Intermediate (trade-offs) / 40% Advanced (optimization) |
| **Answer Length** | 150-300 words (code excluded) |
| **Components** | Pattern → rationale → code → trade-offs → metrics |
| **Citations** | ≥1 each; ≥2 for complex |
| **Per Cluster** | Diagram + code + comparison table + metric formula |

## Coverage (6 Dimensions, 4-6 Q&As Each)

1. **Structural**: Decomposition, modularity, coupling, boundaries (hexagonal, layers)
2. **Behavioral**: Events, state, orchestration, error handling (saga, circuit breaker)
3. **Quality**: Performance, scalability, reliability, security (rate limiting, encryption)
4. **Data**: Persistence, caching, consistency, partitioning (CQRS, sharding)
5. **Integration**: APIs, messaging, protocols (REST, gRPC, streaming)
6. **Evolution**: Refactoring, migration, technical debt (strangler fig, feature toggles)

## Content Standards

**Traceability**: Requirements → Constraints → Pattern → Code → Metrics

**Quantified Trade-offs**: ✅ "CQRS: 10x read, +20-40ms write, +30% complexity" ❌ "Microservices are complex"

**Context Thresholds**: Team (<10 vs >50), Throughput (<100 vs 100-10K vs >10K rps), Data (<1TB vs 1-100TB vs >100TB), Stage (greenfield vs legacy)

**Balanced Perspectives**: ≥2 alternatives with table; explicit assumptions/limitations; tag `[Consensus]`/`[Context-dependent]`/`[Emerging]`

**Precise Language**: Define terms inline; consistent terminology; concrete metrics ("<300ms p95" not "fast"); minimal jargon

## Artifacts

**Diagram-Code-Metric Mapping**:

| Dimension | Diagram | Code Example | Metric Formula |
|-----------|---------|--------------|----------------|
| Structural | Class/Component | Interface/DI | `Cohesion = Related / Total` |
| Behavioral | Sequence/State | Event handler | `Latency = Response - Process` |
| Quality | Deployment | Config/optimization | `Throughput = Requests / Time` |
| Data | ERD/Data flow | Repository pattern | `Cache Hit = Hits / Total × 100%` |
| Integration | API/Sequence | HTTP/gRPC client | `Latency = Net + Process` |
| Evolution | Migration roadmap | Strangler Fig pattern | `Risk = Changed / Total × Complexity` |

**Format**: Diagrams (Mermaid <120 nodes, type matches dimension); Code (10-30 lines, idiomatic, production-ready with error handling); Tables (quantitative, "Use When" column); Metrics (formula + variables + target)

**Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Bulkhead, Event Sourcing, API Gateway, Message Queue, Strangler Fig, Feature Toggle

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥10 | Terms with relationships (e.g., "Hexagonal: isolation via ports/adapters. Related: DI") |
| **Tools** | ≥5 | URL (valid), update ≤18mo, pricing, adoption metrics |
| **Literature** | ≥6 | Authoritative books (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann) |
| **Citations** | ≥12 | APA 7th, 60% [EN] / 30% [ZH] / 10% other (±10%) |

**Quality**: Recency (≥50% last 3yr, ≥70% cloud); Diversity (≥3 types, <25% single source); Credibility (peer-reviewed, authoritative); 100% valid links

---

# Generation Process

## 1. Plan Structure

**Actions**: Select 5-6 clusters across 6 dimensions → Allocate 4-6 Q&As/cluster (25-30 total) → Assign 1F/2I/2A per cluster

**Checks**: Total 25-30; 20/40/40% F/I/A (±5%); all 6 dimensions; no overlap

## 2. Build References

**Actions**: Glossary (≥10 terms + relationships) → Tools (≥5: URL, update ≤18mo, pricing, adoption) → Literature (≥6 books + relevance) → Citations (≥12 APA 7th [EN]/[ZH])

**Checks**: G≥10, T≥5, L≥6, A≥12; 60/30/10% EN/ZH/Other (±10%); ≥50% recency (≥70% cloud); ≥3 types, <25% single; 100% valid URLs

## 3. Write Q&As

**Questions**: ≥70% judgment-based ("How would you..." / "When should you..." / "Compare..."); avoid pure recall unless foundational

**Each Answer**: 150-300 words; ≥1 citation (≥2 advanced); Pattern → rationale → code → trade-offs → metrics; 10-30 lines production code; quantified trade-offs; ≥2 alternatives + table; explicit assumptions/limitations

**Validate Every 5**: Word count, citations, code syntax, traceability, question type, quantified insights

## 4. Create Artifacts

**Per Cluster**: Mermaid diagram (<120 nodes, type matches dimension) + Code (10-30 lines, error handling) + Comparison table (≥2 alternatives: Approach/Pros/Cons/Use When) + Metric formula (formula + variables + target)

**Checks**: All clusters 4/4; diagrams render; code compiles; tables formatted; formulas valid

## 5. Link References

**Actions**: Populate all sections → Extract `[Ref: ID]` from Q&As → Verify all IDs exist → Remove orphans → Validate URLs

**Checks**: G≥10, T≥5, L≥6, A≥12; 100% `[Ref: ID]` resolved; 0 broken links; 60/30/10% EN/ZH/Other; no orphans

## 6. Validate (19 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 (20/40/40%) |
| 2 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 4 | Recency | ≥50% last 3yr (≥70% cloud) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 150-300 |
| 9 | Insights | 100% quantified |
| 10 | Per-topic | ≥2 sources + ≥1 tool |
| 11 | Traceability | ≥80% arch→code |
| 12 | Question type | ≥70% judgment |
| 13 | Artifacts | ≥90% clusters 4/4 |
| 14 | Patterns | ≥80% use patterns |
| 15 | Metrics | ≥60% have metrics |
| 16 | Code | ≥80% have snippets |
| 17 | Syntax | 100% valid |
| 18 | Formulas | 100% valid |
| 19 | Review | 6/6 criteria (see §7) |

**Failure Protocol**: ANY fail → STOP → Document → Fix → Re-validate ALL → Iterate until 19/19 PASS

## 7. Final Review

**6 Criteria (All Must PASS)**:

1. **Clarity**: Logical structure; consistent terms; minimal jargon with inline definitions
2. **Accuracy**: Facts verifiable; code/diagrams valid; metrics sound
3. **Completeness**: 6 dimensions (4-6 Q&As each); minimums met; 19/19 PASS
4. **Balance**: ≥2 alternatives + table; assumptions/limitations; consensus tagged
5. **Practicality**: Actionable guidance; production code; measurable outcomes
6. **Self-Correction**: No redundancy/inconsistencies/gaps/orphans

**Submit When**: 19/19 PASS + 6/6 criteria

**High-Risk Areas**: Code syntax (validate in compiler), URLs (test all), cross-refs (verify `[Ref: ID]`)

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
| [Title] | [Type] | Q1-Q5 | 5 | 1F/2I/2A |
[6 dimensions, 25-30 total, 20/40/40% F/I/A]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [How/When/Compare question]
**Difficulty**: [F/I/A] | **Dimension**: [Type]

**Key Insight**: [Quantified trade-off in one sentence]

**Answer**: [150-300 words: Context → Pattern + rationale → Trade-offs → Metrics → Assumptions/Limitations] [≥1 citation [Ref: A1]]

**Implementation** ([Language]):
```[language]
// 10-30 lines: error handling, logging, idiomatic
```

**Diagram** (per cluster):
```mermaid
[Type matching dimension, <120 nodes]
```

**Metrics**:
| Metric | Formula | Variables | Target |
| [Name] | [Expr] | [Defs] | [Threshold] |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Consensus |
| [Option] | [Quantified] | [Quantified] | [Context] | [Tag] |
[≥2 alternatives]

---

## References

### Glossary (≥10)
**G1. [Term]** [EN/ZH/Other]  
[Definition]. **Related**: [Terms]

### Tools (≥5)
**T1. [Tool]** [Tag]  
**Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥6)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag]  
**Relevance**: [Why]

### Citations (≥12, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation Report
| # | Check | Target | Result | Status |
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 | G:X, T:Y... | PASS/FAIL |
[All 19]

**Overall**: [X/19 PASS - need 19/19]  
**Issues**: [Failures]  
**Remediation**: [Actions]
```

# Reference Examples

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
