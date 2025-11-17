# Software Architecture Interview Q&A Generator

**Problem**: Candidates struggle to translate architecture concepts to practical code, leading to poor hiring decisions. Hallucinations reduce decision quality by 30-60%.

**Scope**: Generate 12 Q&A pairs for senior/architect roles, focusing on architecture-to-code translation.

**Constraints**: Use production-ready, idiomatic code in mainstream languages (Go, Java, Python, TypeScript, Rust).

**Assumptions**: General software architecture knowledge; layered architectures, MVC, REST.

**Audience**: Senior developers (5+ years), architects, technical experts.

**Output**: 12 Q&As across 6 dimensions with code, quantified trade-offs, ≥2 alternatives, citations.

**Success**: All validation checks pass; improves decision quality.

---

## Core Requirements

### Question Specifications
- **Total Count**: 12 (2 per dimension)
- **Difficulty Mix**: 50% Foundational / 50% Advanced
- **Answer Length**: 150-300 words (code excluded)
- **Components**: Pattern → rationale → code → trade-offs → metrics
- **Citations**: ≥1 each; ≥2 for advanced

### Coverage (6 Dimensions, 2 Q&As Each)
1. **Structural**: Decomposition, modularity, coupling (hexagonal, layers)
2. **Behavioral**: Events, state, orchestration (saga, circuit breaker)
3. **Quality**: Performance, scalability, reliability (rate limiting, encryption)
4. **Data**: Persistence, caching, consistency (CQRS, sharding)
5. **Integration**: APIs, messaging, protocols (REST, gRPC)
6. **Evolution**: Refactoring, migration (strangler fig, feature toggles)

### Content Standards
- **Quantified Trade-offs**: e.g., "CQRS: 10x read, +20-40ms write, +30% complexity"
- **Balanced Perspectives**: ≥2 alternatives with table; explicit assumptions/limitations; tag `[Consensus]`/`[Context-dependent]`/`[Emerging]`
- **Precise Language**: Define terms inline; concrete metrics; minimal jargon

### Artifacts
- **Diagram**: Mermaid (<120 nodes, type matches dimension)
- **Code**: 10-30 lines, idiomatic, production-ready with error handling
- **Table**: ≥2 alternatives (Approach/Pros/Cons/Use When/Consensus)
- **Metric**: Formula + variables + target

**Common Patterns**: Hexagonal, Event-Driven, CQRS, Saga, Circuit Breaker, Bulkhead, Event Sourcing, API Gateway, Message Queue, Strangler Fig, Feature Toggle

### References
- **Glossary**: ≥5 terms with relationships
- **Tools**: ≥3 (URL valid, update ≤18mo, pricing, adoption)
- **Literature**: ≥3 authoritative books
- **Citations**: ≥8 APA 7th, balanced languages (≥2 represented)

**Quality**: ≥50% last 3yr; ≥3 types; credible sources; 100% valid links

---

## Generation Process

1. **Plan Structure**: Select 6 dimensions → 2 Q&As each → 50/50 F/A mix
2. **Build References**: Glossary, tools, literature, citations meeting thresholds
3. **Write Q&As**: Judgment-based questions; answers with pattern, code, trade-offs, metrics, citations
4. **Create Artifacts**: Diagram, code, table, metric per dimension
5. **Link References**: Populate sections, verify cross-refs, validate URLs
6. **Validate**: Check counts, citations, language, recency, diversity, links, cross-refs, word count, insights, traceability, question type, artifacts, patterns, metrics, code, syntax, formulas, review criteria

**Failure Protocol**: Any fail → Document → Fix → Re-validate until all pass

---

## Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
| [Title] | [Type] | Q1-Q2 | 2 | F/A 50/50 |
[6 dimensions, 12 total]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [How/When/Compare question]
**Difficulty**: [F/A] | **Dimension**: [Type]

**Key Insight**: [Quantified trade-off in one sentence]

**Answer**: [150-300 words: Context → Pattern + rationale → Trade-offs → Metrics → Assumptions/Limitations] [≥1 citation [Ref: A1]]

**Implementation** ([Language]):
```[language]
// 10-30 lines: error handling, logging, idiomatic
```

**Diagram**:
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

### Glossary (≥5)
**G1. [Term]** [EN/ZH/Other]  
[Definition]. **Related**: [Terms]

### Tools (≥3)
**T1. [Tool]** [Tag]  
**Purpose**: [Desc]. **Updated**: [YYYY-MM]. **Pricing**: [Type]. **Adoption**: [Metrics]. **URL**: [Link]

### Literature (≥3)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag]  
**Relevance**: [Why]

### Citations (≥8, APA 7th, mixed)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation Report
| Check | Target | Result | Status |
| Counts | G≥5, T≥3, L≥3, A≥8, Q=12, F/A=50/50 | [Results] | PASS/FAIL |
[All checks]

**Overall**: [Pass rate]  
**Issues**: [Failures]  
**Remediation**: [Actions]
```

## Reference Examples

### Glossary
**G1. Hexagonal** [EN] – Isolates core via ports/adapters. Enables testability, tech independence. Related: DI  
**G2. CQRS** [EN] – Separates commands from queries. Optimizes scalability. Related: Event Sourcing  
**G3. Event Sourcing** [EN] – Stores state as event log. Enables audit, temporal queries. Related: CQRS  
**G4. Saga** [EN] – Coordinates long transactions with compensations. Related: Distributed TX  
**G5. Circuit Breaker** [EN] – Prevents cascading failures. Opens on error threshold. Related: Bulkhead

### Tools
**T1. Mermaid** [EN] – Text-based diagrams. Updated: 2024-10. Free/OSS. https://mermaid.js.org  
**T2. OpenAPI** [EN] – REST API spec. Updated: 2024-09. Free/OSS. https://www.openapis.org  
**T3. Kubernetes** [EN] – Container orchestration. Updated: 2024-10. Free/OSS. https://kubernetes.io

### Literature
**L1. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** – Strategic/tactical modeling  
**L2. Richardson, C. (2018). *Microservices Patterns*. Manning.** – Decomposition, communication patterns  
**L3. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.** – Distributed systems

### Citations
**A1.** Evans, E. (2003). *Domain-driven design*. Addison-Wesley. [EN]  
**A2.** Richardson, C. (2018). *Microservices patterns*. Manning. [EN]  
**A3.** 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]  
**A4.** Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley. [EN]  
**A5.** Newman, S. (2021). *Building microservices*. O'Reilly. [EN]  
**A6.** Kleppmann, M. (2017). *Designing data-intensive applications*. O'Reilly. [EN]  
**A7.** 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]  
**A8.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]

## Limitations
- **Trade-offs**: Rigor vs. speed; depth vs. breadth; precision vs. accessibility
- **Skip for**: Exploratory questions, low-stakes decisions, rapid response
- **Exclude**: Historical background, pure theory, niche cases, speculation