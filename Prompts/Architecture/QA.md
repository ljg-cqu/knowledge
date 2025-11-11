# Software Architecture Interview Q&A Generator

Generate 25-30 interview Q&A pairs for senior/architect/expert roles demonstrating architecture-to-code translation.

**Target Audience**: Senior developers, architects, technical experts  
**Coverage**: 6 dimensions (structural, behavioral, quality, data, integration, evolution)  
**Output**: Production-ready code, quantified trade-offs, multiple alternatives, authoritative citations  
**Success**: Pass 19/19 validation checks

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

## Coverage (6 Dimensions, Mutually Exclusive)

Cover all dimensions with 4-6 Q&As each:

1. **Structural**: Components, modularity, coupling, boundaries
2. **Behavioral**: Events, state, orchestration, error handling
3. **Quality**: Performance, scalability, reliability, security
4. **Data**: Persistence, caching, consistency, partitioning
5. **Integration**: APIs, messaging, service communication
6. **Evolution**: Refactoring, migration, technical debt

## Content Standards

**Traceability Chain**:  
Requirements → Constraints → Pattern → Code → Metrics

**Quantified Trade-offs**:  
✅ "CQRS: 10x read scalability, +20-40ms write latency, +30% complexity"  
❌ "Microservices are complex"

**Specific Context** (provide thresholds):  
Team size (<10 vs >50), throughput (<100 vs >10K rps), data (<1TB vs >100TB), stage (greenfield vs legacy)

**Balanced Perspectives**:  
≥2 alternatives with comparison; explicit assumptions/limitations; tag consensus level (`[Consensus]`/`[Context-dependent]`/`[Emerging]`)

**Precise Language**:  
Define terms inline; consistent terminology; specific metrics ("<300ms p95", not "fast"); minimal jargon

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

**Format**:  
Diagrams (Mermaid, <120 nodes); Code (10-30 lines, idiomatic Go/Java/Python/TypeScript, production-ready); Tables (Markdown, quantitative); Metrics (formula + variables + target)

**Common Patterns** (illustrative):  
Hexagonal (isolation), Event-Driven (async), CQRS (read/write split), Microservices (decomposition), Layered (separation), DDD (bounded contexts)

## References

| Component | Minimum | Requirements |
|-----------|---------|--------------|
| **Glossary** | ≥10 | Define key terms (e.g., Hexagonal, CQRS, Event Sourcing, DDD, Aggregate, Saga, Circuit Breaker) |
| **Tools** | ≥5 | URL, update ≤18mo, pricing, adoption metrics |
| **Literature** | ≥6 | Industry books (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann) |
| **Citations** | ≥12 | APA 7th, tagged: 60% [EN] / 30% [ZH] / 10% other |

**Quality Standards**:  
Recency (≥50% last 3yr, ≥70% for cloud); Diversity (≥3 types, <25% single source); Credibility (peer-reviewed, authoritative); Resolution (100% valid links)

---

# Generation Process

## 1. Plan Structure

**Goal**: MECE coverage of 6 dimensions

**Actions**:  
Select 5-6 clusters → Allocate 4-6 Q&As per cluster (total 25-30) → Assign difficulty (1F/2I/2A per cluster)

**Checks**:  
Total 25-30; Difficulty 20/40/40% (±5%); All 6 dimensions; No overlap

## 2. Build References

**Goal**: Authoritative sources

**Actions**:  
Create Glossary (≥10 terms, definitions, relationships), Tools (≥5 with URL/update/pricing/adoption), Literature (≥6 books with relevance), Citations (≥12 APA 7th with IDs/tags)

**Checks**:  
Counts met; Language 60/30/10%; Recency ≥50%; Diversity ≥3 types; URLs valid

## 3. Write Q&As

**Goal**: Scenario-based questions (≥70% "How would you..."/"When should you...") with comprehensive answers

**Each Answer Must Include**:  
150-300 words; ≥1 citation (≥2 for complex); pattern name → rationale → code → metrics; 10-30 line code snippet (idiomatic, production-ready); quantified trade-off; ≥2 alternatives with assumptions/limitations

**Validate Every 5**:  
Word count, citations, code syntax, traceability, question type, quantified insights

## 4. Create Artifacts

**Goal**: 4 artifacts per cluster

**Per Cluster**:  
Mermaid diagram (<120 nodes); 10-30 line code (with error handling); comparison table; metric formula (with variables/target)

**Checks**:  
All clusters complete; diagrams render; code compiles; tables formatted; formulas valid

## 5. Link References

**Goal**: 100% cross-reference resolution

**Actions**:  
Populate all sections → Extract all `[Ref: ID]` from Q&As → Verify all cited IDs exist → Check for orphans → Validate URLs/distribution/consistency

**Checks**:  
Minimums met; 100% resolution; 0 broken links; Language distribution correct

## 6. Validate (19 Checks)

**Goal**: All checks PASS

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 (20/40/40%) |
| 2 | Citations | ≥70% Q&As have ≥1; ≥30% have ≥2 |
| 3 | Language | 60/30/10% (±10%) |
| 4 | Recency | ≥50% (≥70% cloud) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: all 150-300 |
| 9 | Insights | 100% quantified |
| 10 | Per-topic | All: ≥2 sources + ≥1 tool |
| 11 | Traceability | ≥80% explicit arch→code |
| 12 | Question type | ≥70% judgment |
| 13 | Artifacts | ≥90% have 4/4 |
| 14 | Patterns | ≥80% use patterns |
| 15 | Metrics | ≥60% have performance metrics |
| 16 | Code | ≥80% have snippets |
| 17 | Syntax | 100% valid |
| 18 | Formulas | 100% valid |
| 19 | Review | Pass clarity/accuracy/completeness/balance/practicality |

**If ANY Fails**: Stop → Document → Fix → Re-validate ALL → Iterate until 19/19 PASS

## 7. Final Review

**Goal**: Quality assurance

**Pass All 6**:  
Clarity (logical structure, consistent terms); Accuracy (verifiable, valid code); Completeness (all dimensions, minimums met, 19/19 PASS); Balance (≥2 alternatives, stated assumptions); Practicality (concrete guidance, production code, measurable); Self-Correction (no redundancy/inconsistency/gaps)

**Submit when**: 19/19 PASS + all 6 criteria met

---

# Output Template

```markdown
## Contents
[TOC with links to: Topic Areas, each Q&A, References sections, Validation Report]

## Topic Areas
| Cluster | Range | Count | Difficulty |
| Structural | Q1-Q5 | 5 | 1F/2I/2A |
[6 clusters totaling 25-30 Q&As, 20/40/40% F/I/A]

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [Question Text]
**Difficulty**: [F/I/A] | **Type**: [Dimension]

**Key Insight**: [Quantified trade-off]

**Answer**: [150-300 words: Context → Pattern → Trade-offs → Code → Metrics] [≥1 citation via [Ref: ID]]

**Implementation**:
```[language]
[10-30 lines, production-ready, idiomatic]
```

**Diagram** (per cluster):
```mermaid
[Type matching dimension, <120 nodes]
```

**Metrics**:
| Metric | Formula | Target |

**Trade-offs**:
| Approach | Pros | Cons | Use When |
[≥2 alternatives with context]

---

## References

### Glossary (≥10)
**G1. Term** [Tag]  
Definition. Related: Concepts

### Tools (≥5)
**T1. Tool** [Tag]  
Purpose. Updated: [Date ≤18mo]. Pricing. URL

### Literature (≥6)
**L1. Author(s). (Year). *Title*. Publisher.**  
Relevance

### Citations (≥12, 60/30/10% EN/ZH/Other)
**A1. Author(s). (Year). *Title*. Publisher. [Tag]**

---

## Validation Report
| Check | Result | Status |
| 1. Counts | G:X, T:Y, L:Z, A:W, Q:N [F/I/A] | PASS/FAIL |
[All 19 checks]

**Overall**: [19/19 PASS required]  
**Issues**: [List if any]  
**Remediation**: [Actions if needed]
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
