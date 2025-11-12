# Cloze: Software Architecture Patterns

Generate fill-in-the-blank assessments (24–40 items) testing senior professionals (5+ years) on architecture patterns, principles, and trade-offs.

**Output**: Complete document with TOC, item bank, references, and validation summary per Output Structure.

---

## Task

**Context**: Create unambiguous cloze items with `___` blanks testing architecture across 4–6 MECE clusters covering full domain without overlap.

**Scope**: Cover structural, behavioral, quality, data, integration, and evolution perspectives with performance, trade-offs, and context guidance.

**Clusters**: Structural Patterns | Behavioral Patterns | Quality Attributes | Data Architecture | Integration Patterns | Architecture Evolution

**Constraints**: 
- Case-insensitive; trim whitespace; strip punctuation
- 1 blank = 1 primary answer + variants (synonyms, regional spellings, abbreviations)
- Rationale: [Concept] + [Implication with trade-offs/limitations/risks] + [When to use/avoid] + [≥1 [Ref: ID]]
- Advanced items: Include performance/cost; flag high-risk with mitigation

**Difficulty** (MECE):
- Foundational (20%): Industry-standard terms (Hexagonal, CQRS, DDD, Microservices)
- Intermediate (40%): Pattern application, trade-off recognition  
- Advanced (40%): Performance metrics, context-specific optimizations, limitations

---

## Requirements

### Content Quality

**Clarity**: Clear, precise language; define technical terms/acronyms on first use; avoid ambiguity  
**Precision**: Consistent terminology; specify exact metrics/thresholds  
**Relevance**: Architecture-relevant only; exclude tangential details  
**Significance**: Important concepts and high-impact patterns; exclude trivial/obscure patterns  
**Concision**: No redundancy; direct phrasing maintaining clarity  
**Logic**: Coherent reasoning; logical structure (concept → implication → trade-offs → citations)

### References (4 sections with inline [Ref: ID])

| Section | Min | Criteria |
|---------|-----|----------|
| **Glossary** (G#) | 10 | Terms + implications + related concepts; define acronyms; [Language Tag] |
| **Tools** (T#) | 5 | ≥10K users; URL + adoption + use cases |
| **Literature** (L#) | 6 | Books/journals/reports; peer-reviewed or practitioner-recognized |
| **APA Citations** (A#) | 12 | APA 7th + [Language Tag]; ~60% EN, ~30% ZH, ~10% other; authoritative sources |

### Quality Gates (100% compliance)

| Gate | Target |
|------|--------|
| Citation Coverage | ≥70% items ≥1 citation; ≥30% ≥2 citations |
| Recency | ≥50% ≤3yr (≥70% cloud-native/microservices) |
| Source Diversity | ≥3 types; ≤25% single source; ≥3 regions; balanced perspectives |
| Pattern-Practice | ≥70% test pattern-to-practice |
| Trade-off Coverage | ≥50% mention trade-offs/limitations/constraints |
| Link Integrity | 100% URLs accessible/archived; all [Ref: ID] resolve |
| MECE | Zero overlap; complete coverage |
| Accuracy | All claims verified; uncertainty flagged |

### Answer Validation

**Primary**: Canonical terms from authoritative sources (>10K citations or industry-wide adoption)  
**Variants**: Regional (US/UK), historical, abbreviations, framework-specific  
**Borderline**: Include if ≥2 authoritative sources within 5yr; document rationale  
**Conflicts**: Include all recognized variants; specify version if changed; document conflicting guidance with context  
**Uncertainty**: Flag uncertain/evolving terms; cite multiple perspectives; avoid contested claims as definitive

---

## Process

### 1. Plan (MECE)
Select 4–6 clusters (no overlap, complete coverage); 4–8 items/cluster; 20/40/40 difficulty distribution. Document cluster selection reasoning.

### 2. Collect References
Gather authoritative, diverse, recent sources meeting minimums and gates. Prioritize peer-reviewed/practitioner-recognized; include multiple perspectives; flag uncertainty/conflicts.

### 3. Generate Items
Per item:
- **Draft**: Single unambiguous blank with expert context (define jargon)
- **Acceptance**: Primary + variants from ≥2 authoritative sources (5yr); document borderline
- **Rationale**: Concept + implication with trade-offs/limitations/constraints + ≥1 [Ref: ID]
- **Self-Review** (every 5 items): 
  - Ambiguity? (multiple interpretations?)
  - Completeness? (missing synonyms?)
  - Citations? (credible? accurate?)
  - Difficulty? (appropriate tier?)
  - Trade-offs? (limitations acknowledged?)

### 4. Compile References
Populate with consistent IDs; verify [Ref: ID] resolve; archive unstable URLs. Cross-check accuracy.

### 5. Validate
100% checklist compliance before delivery:
- Accuracy checks on all claims
- MECE verification (no overlap, complete coverage)
- Balanced perspectives and trade-offs
- URLs and reference integrity
- Document assumptions/limitations/deviations in Notes

---

## Output Structure

**Format**: Markdown (H2 sections, H3 subsections, H4 items)  
**Navigation**: Clickable TOC with anchor links  
**Organization**: Group by cluster; consistent formatting

```markdown
## Table of Contents
- [Item Bank](#item-bank): [Topic 1](#topic-1-structural-patterns) | [Topic 2](#topic-2-behavioral-patterns) | [Topic 3](#topic-3-quality-attributes) | ...
- [References](#references): [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [APA Citations](#apa-citations)
- [Validation Summary](#validation-summary)

---

## Item Bank

### Topic 1: Structural Patterns

#### Item 1: The ___ architecture pattern isolates core business logic via ports and adapters.

**Difficulty:** Foundational

**Acceptable Answers:**
- Hexagonal
- Hexagonal Architecture
- Ports and Adapters

**Rationale:** Hexagonal Architecture [Ref: G1] uses ports (interfaces) and adapters (implementations) to isolate domain core from external dependencies (UI, databases, APIs), enabling independent testing and technology swapping [Ref: A5]. Trade-off: Increased abstraction layers add initial complexity and learning curve.

---

#### Item 2: [Next item...]

---

### Topic 2: Behavioral Patterns

...

---

## References

### Glossary

**G1. Term**: Definition with architectural implications. [Language Tag]

...

---

### Tools

**T1. Tool**: Purpose; adoption metrics; URL. [Language Tag]

...

---

### Literature

**L1. Author(s). (Year). *Title*. Publisher.** Relevance. [Language Tag]

...

---

### APA Citations

**A1. Author(s). (Year). *Title*. Publisher. [Language Tag]**

...

---

## Validation Summary

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Items | 24–40 | [N] | ✅/❌ |
| Foundational | 20% (±5%) | [%] | ✅/❌ |
| Intermediate | 40% (±5%) | [%] | ✅/❌ |
| Advanced | 40% (±5%) | [%] | ✅/❌ |
| Glossary | ≥10 | [N] | ✅/❌ |
| Tools | ≥5 | [N] | ✅/❌ |
| Literature | ≥6 | [N] | ✅/❌ |
| APA | ≥12 | [N] | ✅/❌ |
| Citation Coverage (≥1) | ≥70% | [%] | ✅/❌ |
| Citation Coverage (≥2) | ≥30% | [%] | ✅/❌ |
| Language EN | 50–70% | [%] | ✅/❌ |
| Language ZH | 20–40% | [%] | ✅/❌ |
| Recency ≤3yr | ≥50% | [%] | ✅/❌ |
| Source Types | ≥3 | [N] | ✅/❌ |
| Pattern-Practice Mapping | ≥70% | [%] | ✅/❌ |
| Trade-off Coverage | ≥50% | [%] | ✅/❌ |
| Balanced Perspectives | Pass | [Pass/Fail] | ✅/❌ |
| URLs Accessible | 100% | [%] | ✅/❌ |
| References Resolve | 100% | [%] | ✅/❌ |
| MECE | Pass | [Pass/Fail] | ✅/❌ |
| Accuracy Check | Pass | [Pass/Fail] | ✅/❌ |

**Notes**: [Document assumptions, limitations, deviations, borderline cases, conflicts, or recommendations]
```

---

## Success Criteria

**Measurable Outcomes**: Must:
1. Pass 100% quality gates (all ✅)
2. 24–40 items with 20/40/40 distribution (±5%)
3. Meet reference minimums (≥10 Glossary, ≥5 Tools, ≥6 Literature, ≥12 APA)
4. ≥70% citation coverage (≥1) and ≥30% (≥2)
5. ≥50% trade-off coverage in rationales
6. Balanced perspectives (enterprise/startup, scales)
7. 100% URL accessibility and reference integrity
8. Zero MECE violations (no overlap, complete coverage)

**Practical Utility**: Items must:
- Be unambiguous (single interpretation by experts)
- Be answerable by target audience (senior, 5+ years)
- Have clear right/wrong answers with justification
- Represent real-world architectural decisions

**Quality Indicators**: Strong submissions:
- Precise technical language with defined terms
- Context-aware trade-offs (when to use/avoid)
- Multiple authoritative sources per concept
- Recent references (≥50% within 3yr)
- Diverse perspectives without vendor/framework bias

---

## Examples

**Foundational**: The ___ architecture pattern isolates core business logic via ports and adapters.  
Answers: Hexagonal | Hexagonal Architecture | Ports and Adapters  
Rationale: Hexagonal Architecture [Ref: G1] uses ports/adapters to isolate domain core from external dependencies [Ref: A5], enabling independent testing and technology swapping. Trade-off: Additional abstraction layers increase initial development complexity.

**Intermediate**: CQRS separates ___ (writes) from queries (reads) to optimize scalability independently.  
Answers: commands | command | write operations | writes  
Rationale: CQRS (Command Query Responsibility Segregation) [Ref: G2] decouples command (write) models from query (read) models [Ref: A2], allowing independent scaling (e.g., 1 write node + 10 read replicas) and specialized optimization per workload [Ref: L3]. Trade-offs: Eventual consistency requires conflict resolution strategies; increases operational complexity with separate data stores.

**Advanced**: In Event Sourcing, storing state as ___ enables temporal queries and audit trails with trade-off of query complexity.  
Answers: event log | events | event stream | immutable events | event history  
Rationale: Event Sourcing [Ref: G3] persists domain changes as immutable event sequence [Ref: L2], enabling point-in-time reconstruction and complete audit [Ref: A4]. Trade-offs: Requires event replay for current state (100ms-5s for 1M events), schema evolution strategies [Ref: A7], and increased storage (mitigated by snapshotting). Best for domains requiring strong audit/compliance; avoid for simple CRUD.

---

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
