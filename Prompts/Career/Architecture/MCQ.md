# MCQ Generator: Software Architecture Pattern & Decision Assessment

Generate MCQs evaluating senior technical leaders' ability to select architectural patterns, evaluate trade-offs, and make evidence-based decisions.

## Context

**Purpose**: Assess practical architectural judgment in real-world scenarios.

**Scope**: Architecture patterns, quality attributes, design decisions, implementation trade-offs.

**Constraints**: Evidence-based answers; cite authoritative sources; prioritize recent (≤3 years), tested, widely-adopted approaches.

**Assumptions**: Audience has 5+ years experience; familiar with fundamental patterns; seeks guidance on distributed systems, microservices, event-driven architectures, cloud-native designs.

## Specifications

### Assessment Parameters

| Parameter | Requirement | Rationale |
| --- | --- | --- |
| **Questions** | 42–78 (20% foundational, 40% intermediate, 40% advanced) | Comprehensive coverage; emphasize application, pattern selection, trade-off evaluation over recall |
| **Audience** | Senior developers, architects (5+ years) | Architecture-to-code translation and real-world decision-making |
| **Format** | 1–2 sentence stem + 4 mutually exclusive options (exactly 1 correct) | Clarity, precision, machine-gradability, unambiguous assessment |
| **Distractors** | Map to specific errors (pattern misuse, premature optimization, over-engineering, context mismatch, incomplete understanding) | Reflect common architectural errors; diagnostic learning value |
| **Rationale** | 1–2 sentences: context → pattern → trade-off + ≥1 citation [Ref: ID] | Evidence-based reasoning; explain why optimal; acknowledge alternatives when relevant |

### Coverage (6 Dimensions, MECE)

7-13 questions per dimension (mutually exclusive, collectively exhaustive):

1. **Structural**: Components, modularity, coupling, cohesion, layering, boundaries, dependency management
2. **Behavioral**: Events, workflows, state machines, orchestration vs. choreography, error handling, resilience
3. **Quality Attributes**: Performance, scalability, availability, reliability, security, observability, maintainability
4. **Data Management**: Persistence, caching, consistency (strong/eventual), partitioning, replication, data ownership
5. **Integration**: APIs (REST/GraphQL/gRPC), messaging, service communication, contracts, versioning
6. **Evolution & Sustainability**: Refactoring, migration, technical debt, backwards compatibility, deprecation

### Reference Requirements

| Type | Minimum | Quality Criteria |
| --- | --- | --- |
| **Glossary (G#)** | 10 | Clear, precise definitions (Hexagonal, CQRS, Event Sourcing, DDD, Aggregate, Saga, Circuit Breaker); architectural relevance; related concepts |
| **Tools (T#)** | 5 | Active maintenance (≤18mo); documented adoption/pricing/integrations; verified URLs; proven, widely-adopted |
| **Literature (L#)** | 6 | Authoritative (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann); peer-reviewed or industry-standard; proven track record |
| **APA Citations (A#)** | 12 | APA 7th; language-tagged (~60% EN, ~30% ZH, ~10% other); ≥50% from last 3 years (≥70% cloud-native); credible sources; flag uncertainty |

### Validation Gates (All Must Pass)

1. **Sufficiency**: G≥10, T≥5, L≥6, A≥12, Q=42-78 (20/40/40 split); comprehensive coverage
2. **Evidence**: ≥70% questions cite ≥1 source, ≥30% cite ≥2 sources; credible references back all claims
3. **Breadth**: EN 50-70%, ZH 20-40%, Other 5-15%; multiple linguistic perspectives
4. **Credibility**: ≥50% sources from last 3 years (≥70% cloud-native); current, tested approaches
5. **Diversity**: ≥3 source types, no type >25%; avoid over-reliance
6. **Reliability**: All URLs accessible or archived
7. **Precision**: All [Ref: ID] resolve to G#/T#/L#/A#; no orphans
8. **Accuracy**: Exactly 1 correct answer per question; factually verified; self-reviewed
9. **Logic**: Each distractor maps to specific architectural error with clear reasoning; coherent, sound structure
10. **Clarity**: All options mutually exclusive, unambiguous, consistent terminology; define jargon
11. **Significance**: ≥70% test architectural judgment and trade-off evaluation (not recall); high-value, practical scenarios
12. **Fairness**: Rationales acknowledge alternatives, trade-offs, limitations, context dependencies; avoid bias
13. **Practicality**: Questions address actionable, implementable decisions; real-world applicable
14. **Risk/Value**: Advanced questions evaluate risks, costs, benefits, mitigation strategies

## Process

### Step 1: Plan Topics (MECE Coverage)

**Objective**: Comprehensive, non-overlapping coverage of architectural domains.

**Actions**:
- Identify 6 mutually exclusive, collectively exhaustive dimensions
- Allocate 7-13 questions per dimension (42-78 total)
- Apply 20/40/40 difficulty split per dimension
- Verify complete coverage of architectural decision-making
- Prioritize practical, high-value scenarios over theory

### Step 2: Collect References

**Objective**: Build credible, authoritative, diverse reference base.

**Glossary (≥10)**: 
- Terms: Hexagonal, CQRS, Event Sourcing, DDD, Bounded Context, Aggregate, Repository, Domain Event, Saga, Circuit Breaker
- Format: **G#. Term**: Clear definition + architectural relevance + related concepts [LANG]
- Quality: Precise, unambiguous, consistent terminology

**Tools (≥5)**: 
- Examples: Mermaid, OpenAPI, JSON Schema, Kubernetes, ADR, ArchiMate, C4
- Format: **T#. Tool**: Description + pricing/adoption/last update/integrations/verified URL [LANG]
- Quality: Active (≤18mo), proven adoption, accessible docs

**Literature (≥6)**: 
- Authors: Evans, Vernon, Richardson, Newman, Kleppmann, Fowler + regional experts (周爱民, 张逸)
- Format: **L#. Author. (Year). *Title*. Publisher.** + relevance
- Quality: Authoritative, peer-reviewed or industry-standard, proven

**APA Citations (≥12)**: 
- Format: APA 7th + [LANG]
- Mix: ~60% EN, ~30% ZH, ~10% other
- Recency: ≥50% from last 3 years (≥70% cloud-native)
- Quality: Credible sources; flag uncertainty; verify accuracy

### Step 3: Generate Questions

**Objective**: Clear, precise, practical questions assessing architectural judgment.

**Stem (1-2 sentences)**: 
- Realistic scenario with specific context, constraints, requirements
- Ask for pattern selection, design decision, or trade-off evaluation
- Test judgment and application, not memorization
- Precise, consistent terminology; avoid ambiguity

**Options (4 total)**: 
- 1 correct (optimal given constraints)
- 3 distractors mapping to specific errors:
  - Pattern misuse (wrong context)
  - Premature optimization (unnecessary complexity)
  - Over-engineering (excessive abstraction)
  - Context mismatch (ignoring constraints)
  - Incomplete understanding (missing trade-offs)
- Mutually exclusive, unambiguous, structurally coherent

**Rationale (1-2 sentences)**: 
- Link: context → pattern → trade-off justification
- Quantify impacts when possible (latency, scalability, complexity)
- Cite ≥1 [Ref: ID]
- Acknowledge alternatives, limitations when relevant
- Explain why optimal given constraints

**Distractor Notes**: 
- Document why incorrect
- Specific architectural reasoning (not just "wrong")
- Explain error type and consequences
- Diagnostic learning value

**Validation (Every 10 Questions)**:
- Exactly 1 correct answer
- All distractors documented
- ≥70% test judgment (not recall)
- ≥1 citation per question
- Mutually exclusive, clear options
- Factually accurate
- Self-review for errors, ambiguity, bias

### Step 4: Compile References

**Objective**: Complete, accessible, properly formatted references.

**Actions**:
- Populate G#, T#, L#, A# with proper formatting
- Verify all [Ref: ID] resolve
- Test URLs (or archive)
- Check no orphans
- Confirm minimums (G≥10, T≥5, L≥6, A≥12)
- Consistent terminology
- Remove redundancy; essential, high-quality only

### Step 5: Validate (Run All 14 Gates)

**Objective**: All quality criteria met before delivery.

**Actions**:
- Execute gates 1-14 systematically
- Document failures with details
- Fix immediately
- Re-run after each fix
- Continue until all pass
- Final self-review: accuracy, coherence, clarity, balance, applicability

## Output Format

### Structure

1. **Table of Contents**: Markdown links to major sections (Question Bank by 6 dimensions, References, Validation Report)
2. **Question Bank**: 6 MECE dimensions; subsections for Foundational/Intermediate/Advanced per dimension
3. **Reference Sections**: 
   - Glossary (G#): Key terms, clear definitions
   - Tools (T#): Verified tools, accessibility details
   - Literature (L#): Authoritative publications
   - APA Citations (A#): Full citations, language tags
4. **Validation Report**: Table with 14 gates, PASS/FAIL, metrics, notes

### Question Format Example

```markdown
#### Q1: [Architectural scenario with context, constraints, requirements → Ask for pattern/decision/trade-off]

**Difficulty:** [Foundational/Intermediate/Advanced]
**Dimension:** [Structural/Behavioral/Quality Attributes/Data Management/Integration/Evolution & Sustainability]

**Options:**
- A. [Correct - optimal given constraints]
- B. [Distractor - error type]
- C. [Distractor - error type]
- D. [Distractor - error type]

**Answer:** [A/B/C/D]

**Rationale:** [Context → pattern → trade-off with quantified impacts. Cite ≥1 [Ref: ID]. Acknowledge alternatives/limitations. Explain why optimal.]

**Distractor Notes:**
- [Letter]: [Error type (pattern misuse, premature optimization, over-engineering, context mismatch, incomplete understanding). Why incorrect with reasoning and consequences.]
- [Letter]: [Similar]
- [Letter]: [Similar]
```

### Reference Format Examples

**Glossary**: 
```
G#. Term [LANG]: Clear definition. Architectural relevance. Related concepts: [X, Y, Z].
```

**Tools**: 
```
T#. Tool [LANG]: Description. Pricing: [Free/Paid/Tiered]. Adoption: [metrics/size]. Last Update: [YYYY-MM]. Integrations: [key]. URL: [verified link]
```

**Literature**: 
```
L#. Author. (Year). *Title*. Publisher. [Relevance and key contributions]
```

**APA Citations**: 
```
A#. APA 7th citation (Author, Year, Title, Publisher/Journal, DOI/URL). [LANG]
```

## Reference Examples

## Glossary
**G1. Hexagonal Architecture [EN]**: Pattern isolating core logic from external concerns (UI, databases, frameworks) via ports (interfaces) and adapters (implementations). Enables independent testing, technology swapping, clear separation. Related: Dependency Inversion, Clean Architecture, Onion Architecture.

**G2. CQRS [EN]**: Separates writes (commands) from reads (queries) into distinct models. Optimizes for different access patterns, enables independent scaling, supports event-driven architectures. Related: Event Sourcing, Materialized Views, Polyglot Persistence.

**G3. Event Sourcing [EN]**: Persists state as immutable event sequence rather than current state. Provides audit trail, enables temporal queries, supports event-driven integration, simplifies debugging. Related: CQRS, Event Store, Event Replay, Eventual Consistency.

**G4. Domain-Driven Design (DDD) [EN]**: Approach modeling complex domains via ubiquitous language, bounded contexts, domain-centric patterns. Drives service boundaries, manages complexity, aligns technical and business models. Related: Bounded Context, Aggregate, Entity, Value Object, Ubiquitous Language.

**G5. Bounded Context [EN]**: Explicit boundary where domain model is defined, with clear interfaces to other contexts. Defines service boundaries, prevents model contamination, enables autonomous teams. Related: Context Mapping, Anti-Corruption Layer, Shared Kernel.

**G6. Aggregate [EN]**: Consistency boundary in domain model—root entity plus related entities/value objects enforcing invariants. Defines transactional boundaries, ensures consistency, guides database design. Related: Aggregate Root, Repository, Domain Event, Eventual Consistency.

**G7. Repository [EN]**: Data access abstraction encapsulating persistence, providing collection-like interface for aggregates. Decouples domain from persistence, enables testing, supports multiple storage strategies. Related: Aggregate, Unit of Work, Data Mapper.

**G8. Domain Event [EN]**: Immutable record of significant domain occurrence. Enables loose coupling, supports event-driven architectures, facilitates integration, implements eventual consistency. Related: Event Sourcing, Message Bus, Saga, Event Handler.

**G9. Saga [EN]**: Manages long-running distributed transactions via local transaction sequence, each with compensating actions. Ensures cross-service consistency without distributed transactions, handles failures gracefully. Related: Orchestration, Choreography, Compensating Transaction, Eventual Consistency.

**G10. Circuit Breaker [EN]**: Resilience pattern preventing cascading failures by detecting failures and temporarily blocking calls. Improves stability, enables graceful degradation, provides fast failure detection. Related: Bulkhead, Retry, Timeout, Fallback.

## Tools
**T1. Mermaid [EN]**: Text-based diagramming supporting flowcharts, sequence, class, ER diagrams. Native GitHub/GitLab rendering for version-controlled docs. Pricing: Free/OSS. Adoption: 50K+ GitHub stars, widely adopted. Last Update: 2024-10. Integrations: GitHub, GitLab, VS Code, Confluence, Notion. URL: https://mermaid.js.org

**T2. OpenAPI [EN]**: REST API spec standard (formerly Swagger) enabling machine-readable contracts, code generation, automated testing. Pricing: Free/OSS. Adoption: Industry standard, supported by major gateways. Last Update: 2024-09. Integrations: Swagger UI, Postman, gateways, 40+ language generators. URL: https://www.openapis.org

**T3. JSON Schema [EN]**: Declarative language validating JSON structure, enabling contract-driven development and automated validation. Pricing: Free/OSS. Adoption: IETF standard, widely used in APIs. Last Update: 2024-08. Integrations: Most languages, API frameworks, validation libraries. URL: https://json-schema.org

**T4. Kubernetes [EN]**: Container orchestration providing declarative infrastructure, auto-scaling, self-healing, service discovery. Pricing: Free/OSS (cloud providers charge for managed). Adoption: De facto standard, CNCF graduated. Last Update: 2024-10 (quarterly). Integrations: Docker, containerd, Helm, Istio, Prometheus, major clouds. URL: https://kubernetes.io

**T5. Architecture Decision Records (ADR) [EN]**: Lightweight pattern capturing architectural decisions in Markdown within version control. Pricing: Free/template-based. Adoption: Widely adopted in enterprise and OSS. Last Update: 2024-06. Integrations: Git, GitHub, GitLab, static generators. URL: https://adr.github.io

## Literature
**L1. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.** Foundational DDD text: strategic design (bounded contexts, context mapping, ubiquitous language) and tactical patterns (aggregates, entities, value objects, repositories). Essential for domain-centric architecture and service boundaries.

**L2. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical DDD guide: context mapping, aggregate design, event sourcing, CQRS. Bridges theory and practice with real-world examples.

**L3. Richardson, C. (2018). *Microservices Patterns: With Examples in Java*. Manning.** Comprehensive microservices pattern catalog: decomposition, data management, communication, deployment. Emphasizes trade-offs and decision criteria.

**L4. Newman, S. (2021). *Building Microservices: Designing Fine-Grained Systems* (2nd ed.). O'Reilly.** Updated microservices guide: service boundaries, deployment, testing, security, organization. Covers cloud-native architectures and modern tooling.

**L5. Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly.** Distributed systems fundamentals: replication, partitioning, transactions, consistency, batch/stream processing. Essential for data architecture trade-offs.

**L6. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.** Classic enterprise patterns: layering, domain logic (Transaction Script, Domain Model, Table Module), data source (Repository, Unit of Work, Data Mapper), web presentation. Foundation for modern patterns.

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

---

## Quality Assurance Checklist

Verify alignment before finalizing:

### Foundation
- [ ] **Context**: Scope, constraints, assumptions stated
- [ ] **Clarity**: Terms defined/understood; jargon explained
- [ ] **Precision**: Specific terminology; no ambiguity; consistent
- [ ] **Relevance**: Content directly related to architectural assessment

### Scope
- [ ] **MECE**: Complete, non-overlapping coverage across 6 dimensions
- [ ] **Sufficiency**: Comprehensive coverage of architectural decision-making
- [ ] **Breadth**: Multiple perspectives in questions and references
- [ ] **Depth**: Sufficient detail in rationales and distractor explanations

### Quality
- [ ] **Significance**: High-value, practical architectural scenarios
- [ ] **Concision**: No redundancy; essential only
- [ ] **Accuracy**: Facts verified; self-reviewed
- [ ] **Credibility**: Authoritative, recent sources
- [ ] **Logic**: Coherent reasoning; sound structure
- [ ] **Risk/Value**: Trade-offs, costs, benefits in advanced questions
- [ ] **Fairness**: Alternatives, limitations, context dependencies acknowledged

### Format
- [ ] **Structure**: Tables, lists, clear hierarchy
- [ ] **Output Format**: TOC with links; consistent formatting

### Validation
- [ ] **Evidence**: Claims cited; credible sources
- [ ] **Validation**: All 14 gates passed; documented
- [ ] **Practicality**: Actionable, implementable decisions
- [ ] **Success Criteria**: Measurable outcomes in validation gates
