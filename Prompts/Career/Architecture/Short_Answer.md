# Software Architecture Interview Q&A Generator

Generate 25-30 interview Q&A pairs for senior/architect/expert roles demonstrating architecture-to-code translation.

## Context & Scope

**Audience**: Senior developers, architects (5+ years experience)  
**Scope**: Architecture patterns, distributed systems, scalability, trade-offs  
**Constraints**: Production code (Go/Java/Python/TypeScript); quantified metrics; authoritative sources  
**Output**: Clear Q&As with inline definitions, production code, quantified trade-offs, alternatives, citations  
**Success**: 19/19 validation PASS

---

# Core Requirements

## Question Specifications

| Aspect | Requirement |
|--------|-------------|
| **Count** | 25-30 (20% F / 40% I / 40% A) |
| **Length** | 150-300 words (code excluded) |
| **Structure** | Context → Pattern → Reasoning → Trade-offs → Code → Metrics |
| **Citations** | ≥1 each; ≥2 complex |
| **Per Dimension (Cluster)** | Diagram + code + table + formula |

## Coverage (6 Dimensions - MECE)

Cover all with 4-5 Q&As each (mutually exclusive, complete):

1. **Structural**: Components, modularity, coupling, boundaries
2. **Behavioral**: Events, state, orchestration, error handling
3. **Quality**: Performance, scalability, reliability, security
4. **Data**: Persistence, caching, consistency, partitioning
5. **Integration**: APIs, messaging, protocols, contracts
6. **Evolution**: Refactoring, migration, versioning

## Content Standards

**Clarity**: Define terms inline first use; consistent terminology; understandable explanations

**Relevance**: Architecture/system design focus; significant information only; exclude tangents

**Traceability**: Requirements → Constraints → Pattern (rationale) → Code → Metrics → Validation

**Quantified Trade-offs**: Specific metrics required  
✅ "CQRS: 10x read scalability, +20-40ms write latency (p95), +30% code complexity, 2-week implementation"  
❌ "Microservices are complex" (vague)

**Context**: Decision thresholds (team size: <10 vs >50; throughput: <100 vs >10K req/s; data: <1TB vs >100TB; stage: greenfield vs brownfield; timeline: <1mo vs >6mo)

**Balance**: ≥2 alternatives with costs/benefits/risks; explicit assumptions/limitations; tag consensus (`[Consensus]`/`[Context-dependent]`/`[Emerging]`); flag high-risk with mitigation; acknowledge trade-offs

**Precision**: Inline definitions; specific metrics ("<300ms p95", not "fast"); consistent terms

## Artifacts

**Formats**: Diagrams (Mermaid), code blocks, tables, formulas

**Per Dimension (Cluster)**:

| Dimension | Diagram | Code | Metric |
|-----------|---------|------|--------|
| Structural | Class/Component | Interface/DI | `Cohesion = Related / Total` |
| Behavioral | Sequence/State | Event handler | `Latency = Response - Process` |
| Quality | Deployment | Config/optimization | `Throughput = Requests / Time` |
| Data | ERD/Data flow | Repository | `Cache Hit = Hits / Total × 100%` |
| Integration | API/Sequence | HTTP/gRPC | `Latency = Net + Process` |
| Evolution | Migration | Strangler Fig | `Risk = Changed / Total × Complexity` |

**Requirements**: Diagrams (<120 nodes); Code (10-30 lines, production-ready); Metrics (formula + target)

**Patterns**: Hexagonal, Event-Driven, CQRS, Microservices, Layered, DDD

## References

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥10 | Key terms with relationships; consistent terminology |
| **Tools** | ≥5 | URL, update ≤18mo, pricing, adoption |
| **Literature** | ≥6 | Industry books (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann); authoritative |
| **Citations** | ≥12 | APA 7th; 60% [EN] / 30% [ZH] / 10% other; flag uncertainty |

**Quality**: Recency (≥50% <3yr, ≥70% cloud); Diversity (≥3 types, <25% single source); Credibility (peer-reviewed, authoritative); Accuracy (cross-checked); Links (100% valid)

---

# Generation Process

## 1. Plan Structure

**Goal**: MECE coverage (6 dimensions, 25-30 Q&As, 20/40/40% F/I/A)

**Actions**: Define 6 clusters (one per dimension) → Allocate 4-5 Q&As each → Assign difficulty (1F/2I/2A per cluster)

**Checks**: Total 25-30; Difficulty 20/40/40% (±5%); All 6 dimensions; Zero overlap; Multiple perspectives

## 2. Build References

**Goal**: Authoritative, diverse sources

**Actions**: Glossary (≥10); Tools (≥5 with URL/update/pricing); Literature (≥6 books); Citations (≥12 APA 7th with tags)

**Checks**: Counts met; Language 60/30/10%; Recency ≥50% (≥70% cloud); Diversity ≥3 types; URLs valid; Cross-checked

## 3. Write Q&As

**Goal**: Scenario-based (≥70% "How/When...") with actionable answers

**Each Answer**: 150-300 words; ≥1 citation (≥2 complex); context → pattern → reasoning → trade-offs → code → metrics; 10-30 line code; quantified trade-offs; ≥2 alternatives with costs/benefits/risks

**Self-Review**: Clarity, accuracy, completeness, logic, practicality, fairness

**Validate Every 5**: Word count, citations, syntax, traceability, question type, quantified insights

## 4. Create Artifacts

**Per Dimension (Cluster)**: Mermaid diagram (<120 nodes); 10-30 line code; comparison table; metric formula

**Checks**: All complete; diagrams render; code compiles; tables/formulas valid

## 5. Link References

**Actions**: Extract all `[Ref: ID]` → Verify IDs exist → Check orphans → Validate URLs

**Checks**: 100% resolution; 0 broken links; Language distribution correct

## 6. Validate (19 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 (20/40/40%) |
| 2 | Citations | ≥70% have ≥1; ≥30% have ≥2 |
| 3 | Language | 60/30/10% (±10%) |
| 4 | Recency | ≥50% (≥70% cloud) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 150-300 |
| 9 | Insights | 100% quantified |
| 10 | Per-topic | ≥2 sources + ≥1 tool |
| 11 | Traceability | ≥80% arch→code |
| 12 | Question type | ≥70% judgment |
| 13 | Artifacts | ≥90% have 4/4 |
| 14 | Patterns | ≥80% use patterns |
| 15 | Metrics | ≥60% performance metrics |
| 16 | Code | ≥80% have snippets |
| 17 | Syntax | 100% valid |
| 18 | Formulas | 100% valid |
| 19 | Review | Pass clarity/accuracy/completeness/balance/practicality |

**If ANY Fails**: Stop → Fix → Re-validate ALL → Iterate until 19/19 PASS

## 7. Final Review

**10 Quality Criteria**:  
1. **Clarity**: Logical structure, consistent terms, inline definitions  
2. **Accuracy**: Verifiable claims, valid syntax, cross-checked  
3. **Completeness**: 6 dimensions, minimums met, 19/19 PASS, MECE  
4. **Balance**: ≥2 alternatives, stated assumptions/limitations, trade-offs  
5. **Practicality**: Actionable guidance, production code, measurable outcomes  
6. **Significance**: Important info only, exclude trivial  
7. **Concision**: No redundancy, essential only  
8. **Logic**: Coherent reasoning, explicit traceability  
9. **Credibility**: Authoritative sources, valid citations, flagged uncertainty  
10. **Risk**: Costs/benefits/risks assessed, mitigation strategies

**Self-Correction**: No redundancy, inconsistencies, gaps, ambiguity, undefined jargon, missing citations, broken links, unquantified trade-offs

**Submit**: 19/19 PASS + 10 criteria + self-correction

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas, Q&As (Q1-Q30), References (Glossary/Tools/Literature/Citations), Validation]

## Topic Areas
| Cluster | Range | Count | Difficulty |
|---------|-------|-------|------------|
| Structural | Q1-Q5 | 5 | 1F/2I/2A |
[6 clusters, 25-30 Q&As, 20/40/40% F/I/A]

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [Question]
**Difficulty**: [F/I/A] | **Type**: [Dimension]

**Key Insight**: [Quantified trade-off + risk]

**Answer**: [150-300 words: Context → Pattern → Reasoning → Trade-offs → Code → Metrics]  
- Define terms inline first use  
- Show reasoning  
- Assess risks + mitigation  
- Flag uncertainty [Consensus]/[Context-dependent]/[Emerging]  
- Cite ≥1 [Ref: ID] (≥2 complex)  
- Actionable guidance

**Implementation**:
```[language]
[10-30 lines, production-ready]
```

**Diagram** (per cluster):
```mermaid
[<120 nodes]
```

**Metrics**:
| Metric | Formula | Target |

**Trade-offs**:
| Approach | Pros | Cons | Mitigation | Use When |
[≥2 alternatives]

---

## References

### Glossary (≥10)
**G1. Term** [Tag] – Definition. Related: Concepts

### Tools (≥5)
**T1. Tool** [Tag] – Purpose. Updated: [Date]. Pricing. URL

### Literature (≥6)
**L1. Author(s). (Year). *Title*. Publisher.** – Relevance

### Citations (≥12, 60/30/10% EN/ZH/Other)
**A1. Author(s). (Year). *Title*. Publisher. [Tag]**

---

## Validation Report
| Check | Result | Status |
| 1. Counts | G:X, T:Y, L:Z, A:W, Q:N [F/I/A] | PASS/FAIL |
[19 checks]

**Overall**: 19/19 PASS  
**Issues**: [List]  
**Remediation**: [Actions]
```

# Reference Examples

## Glossary
**G1. Hexagonal** [EN] – Isolates core via ports/adapters. Related: DI  
**G2. CQRS** [EN] – Separates writes from reads. Related: Event Sourcing  
**G3. Event Sourcing** [EN] – Stores state as event log. Related: CQRS  
**G4. DDD** [EN] – Domain modeling via ubiquitous language, bounded contexts. Related: Bounded Context  
**G5. Bounded Context** [EN] – Explicit model boundary. Related: Context Map  
**G6. Aggregate** [EN] – Consistency boundary. Related: Repository  
**G7. Repository** [EN] – Data access abstraction. Related: Aggregate  
**G8. Domain Event** [EN] – Immutable fact. Related: Event Sourcing  
**G9. Saga** [EN] – Coordinates long transactions. Related: Distributed TX  
**G10. Circuit Breaker** [EN] – Prevents cascading failures. Related: Bulkhead

## Tools
**T1. Mermaid** [EN] – Diagrams. Updated: 2024-10. Free/OSS. https://mermaid.js.org  
**T2. OpenAPI** [EN] – REST API spec. Updated: 2024-09. Free/OSS. https://www.openapis.org  
**T3. JSON Schema** [EN] – JSON validation. Updated: 2024-08. Free/OSS. https://json-schema.org  
**T4. Kubernetes** [EN] – Container orchestration. Updated: 2024-10. Free/OSS. https://kubernetes.io  
**T5. ADR** [EN] – Decision log. Updated: 2024-06. Free/OSS. https://adr.github.io

## Literature
**L1. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** – DDD fundamentals  
**L2. Vernon, V. (2013). *Implementing DDD*. Addison-Wesley.** – DDD practical  
**L3. Richardson, C. (2018). *Microservices Patterns*. Manning.** – Microservices patterns  
**L4. Newman, S. (2021). *Building Microservices* (2nd). O'Reilly.** – Microservices practice  
**L5. Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly.** – Distributed systems  
**L6. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.** – Enterprise patterns

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
