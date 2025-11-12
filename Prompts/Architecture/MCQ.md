# MCQ Generator: Software Architecture Pattern & Decision Assessment

Generate Multiple-Choice Questions (MCQs) evaluating senior technical leaders' ability to select and apply architectural patterns, evaluate trade-offs, and make evidence-based design decisions.

## Context & Scope

**Purpose**: Assess practical architectural judgment in real-world scenarios, emphasizing application over memorization.

**Scope**: Software architecture patterns, quality attributes, design decisions, and implementation trade-offs.

**Constraints**: Evidence-based answers only; all claims must cite authoritative sources; prioritize recent (≤3 years), tested, and widely-adopted approaches.

**Assumptions**: Target audience has 5+ years experience; familiar with fundamental patterns (MVC, Layered); seeks guidance on modern distributed systems, microservices, event-driven architectures, and cloud-native designs.

## Specifications

### Assessment Parameters

| Parameter | Requirement | Rationale |
| --- | --- | --- |
| **Questions** | 40–80 total (20% foundational, 40% intermediate, 40% advanced) | Comprehensive coverage; emphasize practical application, pattern selection, and trade-off evaluation over recall |
| **Audience** | Senior developers, architects, technical experts (5+ years) | Focus on architecture-to-code translation and real-world decision-making |
| **Format** | 1–2 sentence stem + 4 options (exactly 1 correct, mutually exclusive) | Clarity, precision, machine-gradability, unambiguous assessment |
| **Distractors** | Map to specific misalignments (e.g., pattern misuse, premature optimization, over-engineering, context mismatch, incomplete understanding) | Reflect common architectural errors; provide diagnostic value for learning |
| **Rationale** | 1–2 sentences: link context → pattern → trade-off + ≥1 citation [Ref: ID] | Evidence-based reasoning; demonstrate why correct answer is optimal given constraints; acknowledge alternatives when relevant |

### Coverage (6 Dimensions, MECE)

Cover all dimensions comprehensively with 7-13 questions each (mutually exclusive, collectively exhaustive):

1. **Structural**: Components, modularity, coupling, cohesion, layering, boundaries, dependency management
2. **Behavioral**: Events, workflows, state machines, orchestration vs. choreography, error handling, resilience patterns
3. **Quality Attributes**: Performance, scalability, availability, reliability, security, observability, maintainability
4. **Data Management**: Persistence strategies, caching, consistency models (strong/eventual), partitioning, replication, data ownership
5. **Integration**: APIs (REST/GraphQL/gRPC), messaging patterns, service communication, contracts, versioning
6. **Evolution & Sustainability**: Refactoring strategies, migration paths, technical debt management, backwards compatibility, deprecation

### Reference Requirements

| Type | Minimum | Quality Criteria |
| --- | --- | --- |
| **Glossary (G#)** | 10 | Define key terms clearly and precisely (e.g., Hexagonal, CQRS, Event Sourcing, DDD, Aggregate, Saga, Circuit Breaker); include architectural relevance and related concepts |
| **Tools (T#)** | 5 | Active maintenance (≤18mo update); documented adoption/pricing/integrations; verified accessible URLs; prioritize proven, widely-adopted tools |
| **Literature (L#)** | 6 | Authoritative sources (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann, etc.); peer-reviewed or industry-standard publications; proven track record |
| **APA Citations (A#)** | 12 | APA 7th format; language-tagged (~60% EN, ~30% ZH, ~10% other); ≥50% from last 3 years (≥70% for cloud-native topics); prioritize credible, high-quality sources; flag uncertainty where applicable |

### Validation Gates (All Must Pass)

1. **Sufficiency (Count)**: G≥10, T≥5, L≥6, A≥12, Q=40-80 (20/40/40 split); ensure comprehensive coverage
2. **Evidence (Citations)**: ≥70% questions cite ≥1 source, ≥30% cite ≥2 sources; all claims backed by credible references
3. **Breadth (Language Mix)**: EN 50-70%, ZH 20-40%, Other 5-15%; multiple linguistic perspectives
4. **Credibility (Recency)**: ≥50% sources from last 3 years (≥70% for cloud-native topics); prioritize current, tested approaches
5. **Diversity (Source Types)**: ≥3 types (Glossary/Tools/Literature/Citations), no single type >25%; avoid over-reliance on single source
6. **Reliability (Links)**: All URLs accessible or archived; verify before finalizing
7. **Precision (Cross-References)**: All [Ref: ID] resolve to G#/T#/L#/A#; no orphaned references
8. **Accuracy (Correctness)**: Exactly 1 correct answer per question; factually verified; self-reviewed for errors
9. **Logic (Distractors)**: Each distractor maps to specific, documented architectural error with clear reasoning; options coherent and structurally sound
10. **Clarity & Precision**: All options mutually exclusive, unambiguous, and use consistent terminology; avoid jargon without definition
11. **Significance (Focus)**: ≥70% test architectural judgment and trade-off evaluation (not pattern recall); prioritize high-value, practical scenarios
12. **Fairness (Balance)**: Rationales acknowledge alternatives, trade-offs, limitations, and context dependencies where applicable; avoid bias toward single approach
13. **Practicality**: Questions address actionable, implementable architectural decisions; provide real-world applicability
14. **Risk/Value Assessment**: Advanced questions evaluate risks, costs, benefits, and mitigation strategies for architectural choices

## Process

### Step 1: Plan Topics (MECE Coverage)

**Objective**: Ensure comprehensive, non-overlapping coverage of architectural domains.

**Actions**:
- Identify 6 dimensions covering architectural design (mutually exclusive, collectively exhaustive)
- Allocate 7-13 questions per dimension (40-80 total)
- Apply 20/40/40 difficulty split to each dimension
- Verify all aspects of architectural decision-making are covered
- Prioritize practical, high-value scenarios over theoretical knowledge

### Step 2: Collect References

**Objective**: Build credible, authoritative, and diverse reference base.

**Glossary (≥10)**: 
- Terms: Hexagonal, CQRS, Event Sourcing, DDD, Bounded Context, Aggregate, Repository, Domain Event, Saga, Circuit Breaker
- Format: **G#. Term**: Clear definition + architectural relevance + related concepts [LANG]
- Quality: Precise terminology, avoid ambiguity, ensure consistency

**Tools (≥5)**: 
- Examples: Mermaid, OpenAPI, JSON Schema, Kubernetes, ADR, ArchiMate, C4
- Format: **T#. Tool**: Description + pricing/adoption/last update/integrations/verified URL [LANG]
- Quality: Active maintenance (≤18mo), proven adoption, accessible documentation

**Literature (≥6)**: 
- Authors: Evans, Vernon, Richardson, Newman, Kleppmann, Fowler + regional experts (周爱民, 张逸)
- Format: **L#. Author. (Year). *Title*. Publisher.** + relevance to architectural practice
- Quality: Authoritative, peer-reviewed or industry-standard, proven track record

**APA Citations (≥12)**: 
- Format: APA 7th + [LANG] tags
- Mix: ~60% EN, ~30% ZH, ~10% other (ensure multiple perspectives)
- Recency: ≥50% from last 3 years (≥70% for cloud-native topics)
- Quality: Prioritize credible sources; flag uncertainty; verify factual accuracy

### Step 3: Generate Questions

**Objective**: Create clear, precise, practical questions that assess architectural judgment.

**Stem (1-2 sentences)**: 
- Present realistic architectural scenario with specific context, constraints, and requirements
- Ask for pattern selection, design decision, or trade-off evaluation
- Test judgment and application, not memorization
- Avoid ambiguity; use precise, consistent terminology

**Options (4 total)**: 
- 1 correct answer (optimal given stated constraints)
- 3 distractors, each mapping to specific architectural error:
  - Pattern misuse (applying pattern in wrong context)
  - Premature optimization (unnecessary complexity)
  - Over-engineering (excessive abstraction)
  - Context mismatch (ignoring stated constraints)
  - Incomplete understanding (missing key trade-offs)
- Ensure mutually exclusive and unambiguous
- Options should be structurally coherent

**Rationale (1-2 sentences)**: 
- Link: context → pattern selection → trade-off justification
- Include quantified impacts when possible (e.g., latency, scalability, complexity)
- Cite ≥1 [Ref: ID] for evidence-based reasoning
- Acknowledge alternatives and limitations where relevant
- Explain why correct answer is optimal given constraints

**Distractor Notes**: 
- Document why each distractor is incorrect
- Provide specific architectural reasoning (not just "wrong pattern")
- Explain the error type and its consequences
- Serve diagnostic purpose for learning

**Validation (Every 10 Questions)**:
- Exactly 1 correct answer per question
- All distractors documented with reasoning
- ≥70% test architectural judgment (not recall)
- ≥1 citation per question
- All options mutually exclusive and clear
- Factual accuracy verified
- Self-review for errors, ambiguity, bias

### Step 4: Compile References

**Objective**: Ensure all references are complete, accessible, and properly formatted.

**Actions**:
- Populate all sections (G#, T#, L#, A#) with proper formatting
- Verify all [Ref: ID] in questions resolve to actual references
- Test all URLs for accessibility (or provide archived versions)
- Check no orphaned references exist
- Confirm minimum counts met (G≥10, T≥5, L≥6, A≥12)
- Ensure consistent terminology across references and questions
- Remove redundancy; include only essential, high-quality references

### Step 5: Validate (Run All 14 Gates)

**Objective**: Ensure all quality criteria are met before delivery.

**Actions**:
- Execute validation gates 1-14 systematically
- Document any failures with specific details
- Fix issues immediately upon detection
- Re-run validation after each fix
- Continue until all gates pass
- Perform final self-review for:
  - Factual accuracy
  - Logical coherence
  - Clarity and precision
  - Balanced perspective
  - Practical applicability

## Output Format

### Structure

1. **Table of Contents**: Markdown links to all major sections (Question Bank organized by 6 dimensions, Reference Sections, Validation Report)
2. **Question Bank**: Organized by 6 MECE dimensions; subsections for Foundational/Intermediate/Advanced within each dimension
3. **Reference Sections**: 
   - Glossary (G#): Key terms with clear definitions
   - Tools (T#): Verified tools with accessibility details
   - Literature (L#): Authoritative publications
   - APA Citations (A#): Full citations with language tags
4. **Validation Report**: Table showing all 14 gates with PASS/FAIL status, metrics, and notes

### Question Format Example

```markdown
#### Q1: [Clear architectural scenario with specific context, constraints, requirements → Ask for pattern/decision/trade-off evaluation]

**Difficulty:** [Foundational/Intermediate/Advanced]
**Dimension:** [Structural/Behavioral/Quality Attributes/Data Management/Integration/Evolution & Sustainability]

**Options:**
- A. [Correct answer - optimal given stated constraints]
- B. [Distractor - specific error type]
- C. [Distractor - specific error type]
- D. [Distractor - specific error type]

**Answer:** [A/B/C/D]

**Rationale:** [Link context → pattern selection → trade-off justification with quantified impacts where possible. Cite ≥1 [Ref: ID]. Acknowledge alternatives/limitations if relevant. Explain why this answer is optimal given constraints.]

**Distractor Notes:**
- [Letter]: [Specific error type (e.g., pattern misuse, premature optimization, over-engineering, context mismatch, incomplete understanding). Explain why incorrect with architectural reasoning and consequences. Not just "wrong pattern".]
- [Letter]: [Similar detailed explanation]
- [Letter]: [Similar detailed explanation]
```

### Reference Format Examples

**Glossary**: 
```
G#. Term [LANG]: Clear, precise definition. Architectural relevance and application context. Related concepts: [X, Y, Z].
```

**Tools**: 
```
T#. Tool [LANG]: Description of purpose and capabilities. Pricing: [Free/Paid/Tiered]. Adoption: [Usage metrics or community size]. Last Update: [YYYY-MM]. Integrations: [Key integrations]. URL: [Verified accessible link]
```

**Literature**: 
```
L#. Author. (Year). *Title*. Publisher. [Brief relevance to architectural practice and key contributions]
```

**APA Citations**: 
```
A#. Full APA 7th citation (Author, Year, Title, Publisher/Journal, DOI/URL if applicable). [LANG]
```

## Reference Examples

## Glossary
**G1. Hexagonal Architecture [EN]**: Architectural pattern that isolates core business logic from external concerns (UI, databases, frameworks) using ports (interfaces) and adapters (implementations). Architectural relevance: Enables independent testing, technology swapping, and clear separation of concerns. Related concepts: Dependency Inversion, Clean Architecture, Onion Architecture.

**G2. CQRS (Command Query Responsibility Segregation) [EN]**: Pattern that separates write operations (commands) from read operations (queries) into distinct models. Architectural relevance: Optimizes for different access patterns, enables independent scaling, supports event-driven architectures. Related concepts: Event Sourcing, Materialized Views, Polyglot Persistence.

**G3. Event Sourcing [EN]**: Pattern that persists application state as an immutable sequence of domain events rather than current state. Architectural relevance: Provides complete audit trail, enables temporal queries, supports event-driven integration, simplifies debugging. Related concepts: CQRS, Event Store, Event Replay, Eventual Consistency.

**G4. Domain-Driven Design (DDD) [EN]**: Strategic and tactical approach to software design that emphasizes modeling complex business domains through ubiquitous language, bounded contexts, and domain-centric patterns. Architectural relevance: Drives service boundaries, manages complexity, aligns technical and business models. Related concepts: Bounded Context, Aggregate, Entity, Value Object, Ubiquitous Language.

**G5. Bounded Context [EN]**: Explicit boundary within which a domain model is defined and applicable, with clear interfaces to other contexts. Architectural relevance: Defines service boundaries, prevents model contamination, enables autonomous teams. Related concepts: Context Mapping, Anti-Corruption Layer, Shared Kernel.

**G6. Aggregate [EN]**: Consistency boundary within a domain model, composed of a root entity and related entities/value objects, enforcing business invariants. Architectural relevance: Defines transactional boundaries, ensures data consistency, guides database design. Related concepts: Aggregate Root, Repository, Domain Event, Eventual Consistency.

**G7. Repository [EN]**: Abstraction for data access that encapsulates persistence logic and provides collection-like interface for aggregates. Architectural relevance: Decouples domain logic from persistence, enables testing, supports multiple storage strategies. Related concepts: Aggregate, Unit of Work, Data Mapper.

**G8. Domain Event [EN]**: Immutable record of a significant occurrence within the domain model. Architectural relevance: Enables loose coupling, supports event-driven architectures, facilitates integration, implements eventual consistency. Related concepts: Event Sourcing, Message Bus, Saga, Event Handler.

**G9. Saga [EN]**: Pattern for managing long-running distributed transactions through a sequence of local transactions, each with compensating actions for rollback. Architectural relevance: Ensures data consistency across services without distributed transactions, handles failures gracefully. Related concepts: Orchestration, Choreography, Compensating Transaction, Eventual Consistency.

**G10. Circuit Breaker [EN]**: Resilience pattern that prevents cascading failures by detecting failures and temporarily blocking calls to failing services. Architectural relevance: Improves system stability, enables graceful degradation, provides fast failure detection. Related concepts: Bulkhead, Retry, Timeout, Fallback.

## Tools
**T1. Mermaid [EN]**: Text-based diagramming tool supporting flowcharts, sequence diagrams, class diagrams, ER diagrams, and more. Native GitHub/GitLab rendering enables version-controlled architectural documentation. Pricing: Free/OSS. Adoption: 50K+ GitHub stars, widely adopted in documentation. Last Update: 2024-10. Integrations: GitHub, GitLab, VS Code, Confluence, Notion. URL: https://mermaid.js.org

**T2. OpenAPI [EN]**: REST API specification standard (formerly Swagger) enabling machine-readable API contracts, code generation, and automated testing. Pricing: Free/OSS. Adoption: Industry standard for REST APIs, supported by major API gateways. Last Update: 2024-09. Integrations: Swagger UI, Postman, API gateways, code generators for 40+ languages. URL: https://www.openapis.org

**T3. JSON Schema [EN]**: Declarative language for validating JSON document structure, enabling contract-driven development and automated validation. Pricing: Free/OSS. Adoption: IETF standard, widely used in API development. Last Update: 2024-08. Integrations: Most programming languages, API frameworks, validation libraries. URL: https://json-schema.org

**T4. Kubernetes [EN]**: Container orchestration platform providing declarative infrastructure management, auto-scaling, self-healing, and service discovery. Pricing: Free/OSS (cloud providers charge for managed services). Adoption: De facto standard for container orchestration, CNCF graduated project. Last Update: 2024-10 (quarterly releases). Integrations: Docker, containerd, Helm, Istio, Prometheus, all major cloud providers. URL: https://kubernetes.io

**T5. Architecture Decision Records (ADR) [EN]**: Lightweight documentation pattern capturing architectural decisions in Markdown files within version control. Pricing: Free/template-based. Adoption: Widely adopted in enterprise and open-source projects. Last Update: 2024-06 (template updates). Integrations: Git, GitHub, GitLab, static site generators. URL: https://adr.github.io

## Literature
**L1. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.** Foundational text on DDD introducing strategic design (bounded contexts, context mapping, ubiquitous language) and tactical patterns (aggregates, entities, value objects, repositories). Essential for understanding domain-centric architecture and service boundary identification.

**L2. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical guide to applying DDD with detailed coverage of context mapping, aggregate design patterns, event sourcing, and CQRS. Bridges theory and practice with real-world examples and implementation guidance.

**L3. Richardson, C. (2018). *Microservices Patterns: With Examples in Java*. Manning.** Comprehensive catalog of microservices patterns covering decomposition strategies, data management, communication patterns, and deployment. Emphasizes trade-offs and decision criteria for pattern selection in distributed systems.

**L4. Newman, S. (2021). *Building Microservices: Designing Fine-Grained Systems* (2nd ed.). O'Reilly.** Updated guide to microservices covering service boundaries, deployment strategies, testing approaches, security, and organizational considerations. Addresses cloud-native architectures and modern tooling.

**L5. Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems*. O'Reilly.** Deep dive into distributed systems fundamentals including replication, partitioning, transactions, consistency models, and batch/stream processing. Essential for understanding data architecture trade-offs.

**L6. Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley.** Classic catalog of enterprise patterns including layering, domain logic patterns (Transaction Script, Domain Model, Table Module), data source patterns (Repository, Unit of Work, Data Mapper), and web presentation patterns. Foundation for modern architectural patterns.

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

Before finalizing the MCQ set, verify alignment with all guidelines:

### Foundation
- [ ] **Context**: Scope, constraints, and assumptions clearly stated
- [ ] **Clarity**: All terms defined or commonly understood; jargon explained
- [ ] **Precision**: Specific terminology; no ambiguity; consistent usage
- [ ] **Relevance**: All content directly related to architectural assessment

### Scope
- [ ] **MECE**: Complete, non-overlapping coverage across 6 dimensions
- [ ] **Sufficiency**: Comprehensive coverage of architectural decision-making
- [ ] **Breadth**: Multiple perspectives reflected in questions and references
- [ ] **Depth**: Sufficient detail in rationales and distractor explanations

### Quality
- [ ] **Significance**: Focus on high-value, practical architectural scenarios
- [ ] **Concision**: No redundancy; only essential information included
- [ ] **Accuracy**: All facts verified; self-reviewed for errors
- [ ] **Credibility**: Authoritative sources; recent publications prioritized
- [ ] **Logic**: Coherent reasoning; structurally sound arguments
- [ ] **Risk/Value**: Trade-offs, costs, benefits addressed in advanced questions
- [ ] **Fairness**: Alternatives, limitations, and context dependencies acknowledged

### Format
- [ ] **Structure**: Organized with tables, lists; clear hierarchy
- [ ] **Output Format**: TOC with links to all sections; consistent formatting

### Validation
- [ ] **Evidence**: All claims cited; sources credible
- [ ] **Validation**: All 14 gates passed; documented
- [ ] **Practicality**: Questions address actionable, implementable decisions
- [ ] **Success Criteria**: Measurable outcomes defined in validation gates
