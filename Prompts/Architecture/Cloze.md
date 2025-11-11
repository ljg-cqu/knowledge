# Cloze: Software Architecture Patterns

Generate comprehensive, well-structured fill-in-the-blank assessments (24–40 items) testing how senior technical professionals (5+ years) understand and apply software architecture patterns, principles, and trade-offs.

**Output Requirements**: Provide a complete, structured document with Table of Contents, organized item bank, comprehensive references, and validation summary. Follow the exact format specified in Output Structure section.

---

## Task

**Context**: Create unambiguous cloze items with `___` blanks testing architecture terminology, patterns, principles, and trade-offs across 4–6 MECE (Mutually Exclusive, Collectively Exhaustive) topic clusters covering the full domain without overlap.

**Scope**: 
- **Breadth**: Cover multiple perspectives including structural, behavioral, quality, data, and integration concerns
- **Depth**: Provide thorough treatment with sufficient detail including performance characteristics, trade-offs, and context-specific guidance

**Clusters**: Structural Patterns | Behavioral Patterns | Quality Attributes | Data Architecture | Integration Patterns | Architecture Evolution

**Constraints**: 
- Case-insensitive matching; trim whitespace; strip punctuation
- Each item: 1 blank = 1 primary answer + variants (synonyms, regional spellings, abbreviations)
- Rationale format: [Concept] + [Architectural implication with trade-offs/limitations/risks] + [Context guidance on when to use/avoid] + [≥1 citation as [Ref: ID]]
- Risk/Value assessment: For Advanced items, include performance/cost implications; flag high-risk choices with mitigation strategies

**Difficulty** (MECE distribution):
- Foundational (20%): Industry-standard terms (e.g., Hexagonal, CQRS, DDD, Microservices)
- Intermediate (40%): Pattern application, trade-off recognition  
- Advanced (40%): Performance metrics, context-specific optimizations, limitations

---

## Requirements

### Content Quality

**Clarity**: Use clear, precise language; define technical terms or acronyms on first use; avoid ambiguous phrasing  
**Precision**: Use consistent terminology throughout; specify exact metrics/thresholds where applicable  
**Relevance**: Include only architecture-relevant information; exclude tangential details  
**Significance**: Prioritize important architectural concepts and high-impact patterns; exclude trivial variations or obscure patterns with limited real-world use  
**Concision**: Eliminate redundancy; use the most direct phrasing that maintains clarity  
**Logic**: Ensure coherent reasoning in rationales; structure information logically (concept → implication → trade-offs → citations)

### References (4 sections with inline citations [Ref: ID])

| Section | Min | Criteria |
|---------|-----|----------|
| **Glossary** (G#) | 10 | Architecture terms + pattern implications + related concepts; define acronyms; [Language Tag] |
| **Tools** (T#) | 5 | ≥10K users; URL + adoption metrics + use cases |
| **Literature** (L#) | 6 | Books/journals/reports; peer-reviewed or practitioner-recognized; include publication context |
| **APA Citations** (A#) | 12 | APA 7th + [Language Tag]; ~60% EN, ~30% ZH, ~10% other; prioritize authoritative sources |

### Quality Gates (100% compliance required)

| Gate | Target |
|------|--------|
| Citation Coverage | ≥70% items have ≥1 citation; ≥30% have ≥2 |
| Recency | ≥50% published ≤3 years (≥70% for cloud-native/microservices) |
| Source Diversity | ≥3 types; no single source >25%; ≥3 geographic regions; balanced perspectives (enterprise vs. startup contexts) |
| Pattern-Practice Mapping | ≥70% items test pattern-to-practice application |
| Trade-off Coverage | ≥50% items explicitly mention trade-offs, limitations, or context constraints in rationale |
| Link/Reference Integrity | 100% URLs accessible/archived; all [Ref: ID] resolve to G#/T#/L#/A# |
| MECE | Zero cluster overlap; complete domain coverage |
| Accuracy | All technical claims verified against authoritative sources; uncertain information flagged |

### Answer Validation

**Primary**: Canonical terms from authoritative sources (prioritize sources with >10K citations or industry-wide adoption)  
**Variants**: Regional (US/UK English), historical terms, abbreviations, framework-specific names  
**Borderline Cases**: Include if ≥2 authoritative sources use within 5 years; document rationale and source quality  
**Conflicts**: When terminology differs across sources:
  - Include all recognized variants as acceptable answers
  - Specify framework/tool version if terminology changed significantly
  - Document conflicting guidance in rationale with context (e.g., "Martin Fowler recommends X for microservices; Evans recommends Y for monoliths")
**Uncertainty**: Flag uncertain or evolving terminology; cite multiple perspectives; avoid presenting contested claims as definitive

---

## Process

### 1. Plan (MECE topology)
Select 4–6 clusters ensuring no overlap and complete domain coverage; allocate 4–8 items/cluster; apply 20/40/40 difficulty distribution per cluster. Document reasoning for cluster selection and boundaries.

### 2. Collect References
Gather authoritative, diverse, recent sources meeting minimums and quality gates above. Prioritize peer-reviewed or practitioner-recognized sources; include multiple perspectives (enterprise/startup, different architectural schools); flag any uncertainty or conflicting guidance.

### 3. Generate Items
For each item:
- **Draft**: Single unambiguous blank with sufficient expert context (avoid jargon without definition)
- **Acceptance List**: Primary + variants from ≥2 authoritative sources (5-year window); document borderline cases
- **Rationale**: Concept + architectural implication with trade-offs/limitations/context constraints + ≥1 [Ref: ID]
- **Self-Review** every 5 items: 
  - Check for ambiguity (multiple interpretations?)
  - Verify acceptance completeness (missing common synonyms?)
  - Validate citations (sources credible? claims accurate?)
  - Confirm difficulty tier (appropriate for target expertise?)
  - Assess trade-off coverage (limitations acknowledged?)

### 4. Compile References
Populate sections with consistent IDs; verify all [Ref: ID] resolve; archive unstable URLs (Wayback Machine). Cross-check factual correctness against multiple sources.

### 5. Validate
Perform comprehensive self-review of 100% checklist compliance before delivery:
- Run accuracy checks on all technical claims
- Verify MECE properties (no overlap, complete coverage)
- Confirm balanced perspectives and trade-off coverage
- Validate all URLs and reference integrity
- Document any assumptions, limitations, or deviations in Notes

---

## Output Structure

**Format**: Markdown with hierarchical structure (H2 for sections, H3 for subsections, H4 for items)  
**Navigation**: Include clickable Table of Contents with anchor links to all major sections and subsections  
**Organization**: Group items by topic cluster; maintain consistent formatting throughout

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

**Rationale:** Hexagonal Architecture [Ref: G1] uses ports (interfaces) and adapters (implementations) to isolate the domain core from external dependencies (UI, databases, APIs), enabling independent testing and technology swapping [Ref: A5]. Trade-off: Increased abstraction layers add initial complexity and learning curve.

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

**Notes**: [Document any assumptions, limitations, deviations, borderline cases, conflicting guidance, or recommendations]
```

---

## Success Criteria

**Measurable Outcomes**: A successful output must:
1. Pass 100% of quality gates in Validation Summary (all metrics ✅)
2. Contain 24–40 items with 20/40/40 difficulty distribution (±5%)
3. Meet all reference minimums (≥10 Glossary, ≥5 Tools, ≥6 Literature, ≥12 APA)
4. Achieve ≥70% citation coverage (≥1 citation) and ≥30% (≥2 citations)
5. Demonstrate ≥50% trade-off coverage in rationales
6. Show balanced perspectives across different contexts (enterprise/startup, different scales)
7. Have 100% URL accessibility and reference integrity
8. Exhibit zero MECE violations (no cluster overlap, complete domain coverage)

**Practical Utility**: Items must be:
- Unambiguous (single correct interpretation by domain experts)
- Answerable by target audience (senior professionals with 5+ years experience)
- Actionable for assessment purposes (clear right/wrong answers with justification)
- Representative of real-world architectural decision-making

**Quality Indicators**: Strong submissions demonstrate:
- Precise technical language with defined terms
- Context-aware trade-offs (when to use/avoid patterns)
- Multiple authoritative sources per concept
- Recent references (≥50% within 3 years)
- Diverse perspectives without bias toward specific vendors/frameworks

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
