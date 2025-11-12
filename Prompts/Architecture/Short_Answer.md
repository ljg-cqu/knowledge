# Software Architecture Interview Q&A Generator

Generate 25-30 interview Q&A pairs for senior/architect/expert roles demonstrating architecture-to-code translation.

## Context & Scope

**Target Audience**: Senior developers, architects, technical experts preparing for system design interviews  
**Scope**: Software architecture patterns, distributed systems, scalability, and design trade-offs  
**Constraints**: Production-ready code only (Go/Java/Python/TypeScript); quantified metrics required; authoritative sources mandatory  
**Assumptions**: Readers have 5+ years development experience; understand basic design patterns; require decision-making guidance  
**Output**: Clear, understandable Q&A pairs with inline term definitions, production-ready code, quantified trade-offs, multiple alternatives, authoritative citations  
**Success Criteria**: Pass 19/19 validation checks with measurable quality metrics

## Guideline Compliance Overview

This prompt optimizes for all 21 LLM-friendly guidelines:

**Foundation** (Define Task): Context ✓, Clarity ✓ (inline definitions, clear explanations), Precision ✓ (specific metrics, consistent terminology), Relevance ✓ (on-topic focus)

**Scope** (Coverage): MECE ✓ (mutually exclusive dimensions), Sufficiency ✓ (comprehensive coverage), Breadth ✓ (multiple perspectives), Depth ✓ (150-300 words, thorough treatment)

**Quality** (Excellence): Significance ✓ (prioritize important info), Concision ✓ (remove redundancy), Accuracy ✓ (verifiable, cross-checked), Credibility ✓ (authoritative sources, peer-reviewed), Logic ✓ (coherent reasoning, traceability), Risk/Value ✓ (cost/benefit/risk assessment, mitigation), Fairness ✓ (balanced perspectives, acknowledged limitations)

**Format** (Presentation): Structure ✓ (lists, tables, diagrams, formulas, code), Output Format ✓ (structured TOC with links)

**Validation** (Correctness): Evidence ✓ (cited sources, flagged uncertainty), Validation ✓ (self-review, 19 checks), Practicality ✓ (actionable, implementable), Success Criteria ✓ (19/19 PASS + 10 quality criteria)

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

## Coverage (6 Dimensions - MECE)

**MECE Principle**: Mutually Exclusive (no overlap), Collectively Exhaustive (complete coverage)

Cover all dimensions with 4-6 Q&As each, ensuring sufficient depth and breadth:

1. **Structural**: Components, modularity, coupling, boundaries, separation of concerns
2. **Behavioral**: Events, state, orchestration, error handling, workflow patterns
3. **Quality**: Performance, scalability, reliability, security, maintainability
4. **Data**: Persistence, caching, consistency, partitioning, data modeling
5. **Integration**: APIs, messaging, service communication, protocols, contracts
6. **Evolution**: Refactoring, migration, technical debt, versioning, backward compatibility

**Sufficiency Check**: Ensure comprehensive coverage of all necessary aspects within each dimension; request multiple perspectives where appropriate; provide thorough treatment with sufficient detail

## Content Standards

**Clarity Requirements**:  
All explanations must be clear and understandable; define technical terms inline on first use; avoid jargon without definition; use consistent terminology throughout

**Relevance Requirements**:  
Stay on topic; focus on software architecture and system design; exclude tangential information not directly related to the question; prioritize significant information over trivial details

**Traceability Chain** (show reasoning):  
Requirements → Constraints → Pattern Selection (with rationale) → Code → Metrics → Validation

**Quantified Trade-offs** (precise metrics required):  
✅ "CQRS: 10x read scalability, +20-40ms write latency (p95), +30% code complexity, 2-week implementation"  
❌ "Microservices are complex" (vague, unquantified, no context)

**Specific Context** (provide decision thresholds):  
Team size (<10 vs >50 engineers), throughput (<100 vs >10K requests/sec), data volume (<1TB vs >100TB), project stage (greenfield vs brownfield/legacy), timeline (<1mo vs >6mo)

**Balanced Perspectives** (fairness & risk assessment):  
≥2 alternatives with comparison; explicit assumptions/limitations/biases; assess risks, costs, benefits; tag consensus level (`[Consensus]`/`[Context-dependent]`/`[Emerging]`); flag high-risk choices with mitigation strategies; acknowledge trade-offs and counterarguments

**Precise Language** (avoid ambiguity):  
Define terms inline (e.g., "p95 latency: 95th percentile response time"); consistent terminology; specific metrics ("<300ms p95", not "fast"); avoid jargon; maintain term consistency across all Q&As

## Artifacts

**Structure Formats**: Employ appropriate structures for presenting information: diagrams (Mermaid for visualization), code blocks (with language specification), tables (Markdown for comparisons), formulas (with defined variables)

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
| **Glossary** | ≥10 | Define key terms inline with relationships (e.g., Hexagonal, CQRS, Event Sourcing, DDD, Aggregate, Saga, Circuit Breaker); maintain consistent terminology |
| **Tools** | ≥5 | URL, last update ≤18mo, pricing, adoption metrics, credibility indicators |
| **Literature** | ≥6 | Industry books (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann); authoritative, peer-reviewed, high-quality sources |
| **Citations** | ≥12 | APA 7th, tagged: 60% [EN] / 30% [ZH] / 10% other; cite credible sources; flag uncertainty where applicable |

**Quality Standards** (credibility & reliability):  
Recency (≥50% last 3yr, ≥70% for cloud/emerging); Diversity (≥3 source types, <25% single source to avoid bias); Credibility (prioritize peer-reviewed, authoritative, tested sources; avoid low-quality or unproven content); Accuracy (cross-check factual correctness); Resolution (100% valid links, verified before submission)

---

# Generation Process

## 1. Plan Structure

**Goal**: MECE (Mutually Exclusive, Collectively Exhaustive) coverage of 6 dimensions with sufficient depth and breadth

**Actions**:  
Select 5-6 clusters ensuring complete, non-overlapping coverage → Allocate 4-6 Q&As per cluster (total 25-30) covering multiple perspectives → Assign difficulty (1F/2I/2A per cluster) balancing foundational concepts with advanced optimization

**Checks**:  
Total 25-30; Difficulty 20/40/40% (±5%); All 6 dimensions covered comprehensively; Zero overlap (mutually exclusive); Sufficient depth per dimension; Multiple perspectives included

## 2. Build References

**Goal**: Authoritative, credible, diverse sources

**Actions**:  
Create Glossary (≥10 terms with clear definitions avoiding jargon, relationships, consistent terminology); Tools (≥5 with URL/update/pricing/adoption/credibility indicators); Literature (≥6 authoritative books with relevance, peer-reviewed preferred); Citations (≥12 APA 7th with IDs/tags, prioritizing high-quality, tested sources)

**Checks**:  
Counts met; Language 60/30/10%; Recency ≥50% (≥70% cloud); Diversity ≥3 types, <25% single source (avoid bias); Credibility (authoritative, peer-reviewed, avoid low-quality); URLs 100% valid; Cross-check factual correctness

## 3. Write Q&As

**Goal**: Scenario-based questions (≥70% "How would you..."/"When should you...") with comprehensive, actionable answers

**Each Answer Must Include**:  
150-300 words; ≥1 credible citation (≥2 for complex, flagging uncertainty where applicable); pattern name → rationale with reasoning → code → metrics; 10-30 line code snippet (idiomatic, production-ready, implementable); quantified trade-off with risk assessment; ≥2 alternatives with assumptions/limitations/costs/benefits; ensure recommendations are actionable and practical for real-world scenarios

**Self-Review Each Answer** (before proceeding):  
Clarity (understandable, terms defined inline); Accuracy (verifiable claims, valid code syntax); Completeness (all required elements present); Logic (coherent reasoning, sound structure); Practicality (actionable guidance, implementable solutions); Fairness (balanced perspectives, acknowledged limitations)

**Validate Every 5**:  
Word count, citations, code syntax, traceability, question type, quantified insights, error checks, reasoning clarity

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

**Goal**: Comprehensive quality assurance across all guidelines

**Pass All 10 Quality Criteria**:  
1. **Clarity**: Logical structure, consistent terminology throughout, terms defined inline, understandable explanations  
2. **Accuracy**: Verifiable claims, valid code syntax, cross-checked factual correctness  
3. **Completeness**: All 6 dimensions covered, all minimums met, 19/19 PASS, sufficient depth and breadth, MECE coverage  
4. **Balance**: ≥2 alternatives per question, stated assumptions/limitations/biases, acknowledged trade-offs and counterarguments  
5. **Practicality**: Concrete actionable guidance, production-ready implementable code, measurable outcomes  
6. **Significance**: Prioritize important information, exclude trivial details, focus on high-value insights  
7. **Concision**: Remove redundancy, include only essential information, no unnecessary repetition  
8. **Logic**: Coherent reasoning throughout, sound structure, explicit traceability chains  
9. **Credibility**: Authoritative sources, peer-reviewed literature, valid citations, flagged uncertainty  
10. **Risk Assessment**: Costs/benefits/risks assessed, high-risk choices flagged with mitigation strategies

**Self-Correction Check**:  
No redundancy; no inconsistencies; no gaps; no ambiguity; no undefined jargon; no missing citations; no broken links; no unquantified trade-offs

**Submit when**: 19/19 PASS + all 10 quality criteria met + self-correction complete

---

# Output Template

**Structure Requirements**: Use hierarchical organization with clear sections; employ lists, tables, diagrams, formulas, code blocks; ensure logical flow

```markdown
## Contents
[Structured TOC with clickable links to: Topic Areas, each individual Q&A (Q1-Q30), all References sections (Glossary/Tools/Literature/Citations), Validation Report]

## Topic Areas
| Cluster | Range | Count | Difficulty |
| Structural | Q1-Q5 | 5 | 1F/2I/2A |
[6 clusters totaling 25-30 Q&As, 20/40/40% F/I/A]

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [Question Text]
**Difficulty**: [F/I/A] | **Type**: [Dimension]

**Key Insight**: [Quantified trade-off with risk assessment]

**Answer**: [150-300 words: Context → Pattern Selection → Reasoning → Trade-offs (costs/benefits/risks) → Code → Metrics → Validation]  
- Define technical terms inline on first use  
- Show reasoning process for pattern selection  
- Assess risks and provide mitigation strategies  
- Flag uncertainty with [Consensus]/[Context-dependent]/[Emerging]  
- Cite credible sources [≥1 citation via [Ref: ID], ≥2 for complex topics]  
- Ensure actionable, implementable guidance

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

**Trade-offs** (risk/value assessment):
| Approach | Pros (Value/Benefits) | Cons (Costs/Risks) | Mitigation Strategies | Use When (Context) |
[≥2 alternatives; prioritize high-value, low-risk; flag high-risk with mitigation; acknowledge limitations and counterarguments]

---

## References

### Glossary (≥10)
**G1. Term** [Tag]  
Clear, understandable definition avoiding jargon. Maintain consistent terminology. Related: Concepts  
*[Note: Define each term inline in Q&As on first use as well]*

### Tools (≥5)
**T1. Tool** [Tag]  
Purpose. Updated: [Date ≤18mo]. Pricing. URL

### Literature (≥6)
**L1. Author(s). (Year). *Title*. Publisher.**  
Relevance

### Citations (≥12, 60/30/10% EN/ZH/Other)
**A1. Author(s). (Year). *Title*. Publisher. [Tag]**  
*[Prioritize authoritative, peer-reviewed, high-quality sources; flag uncertainty where applicable; cross-check factual correctness]*

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
