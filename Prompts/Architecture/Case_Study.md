# Case Study: Architecture Decision Assessment Generator

## Purpose & Scope

**Objective:** Generate multi-scenario assessments evaluating technical leaders' ability to translate requirements into architecture decisions.

**Target Audience:** Exam designers, educators, enterprise architects, training developers.

**Scope:** 16–22 scenarios across 5 domain clusters with comprehensive reference materials.

**Constraints:** Production-ready code, accessible citations, MECE coverage, balanced difficulty distribution.

**Assumptions:** Users have intermediate software architecture knowledge; scenarios target real-world complexity; outputs must be immediately usable without additional editing.

## Quality Standards

All outputs must adhere to these standards:

**Foundation:**
- **Context:** Explicit scope, constraints, assumptions
- **Clarity:** Clear explanations; all jargon defined
- **Precision:** Specific terms; consistent terminology; no ambiguity
- **Relevance:** On-topic content only; exclude tangential information

**Scope:**
- **MECE:** Complete, non-overlapping coverage
- **Sufficiency:** Comprehensive coverage of all necessary aspects
- **Breadth:** Multiple perspectives where appropriate
- **Depth:** Thorough treatment with sufficient detail

**Excellence:**
- **Significance:** Prioritize important information; exclude trivial details
- **Concision:** No redundancy; essential information only
- **Accuracy:** Verified facts; cross-checked information
- **Credibility:** Authoritative, high-quality, tested sources; flag uncertainties
- **Logic:** Coherent reasoning; sound structure; explicit reasoning chains
- **Risk/Value:** Assess risks/costs/benefits; prioritize high-value, low-risk; flag high-risk with mitigation
- **Fairness:** Balanced perspectives; acknowledge limitations, alternatives, trade-offs

**Format:**
- **Structure:** Tables, diagrams, code blocks with clear organization
- **Output Format:** TOC linking to all sections

**Validation:**
- **Evidence:** Cite credible sources; flag uncertainty
- **Validation:** Reasoning chains, self-review, error checks
- **Practicality:** Actionable, implementable guidance
- **Success Criteria:** Measurable, concrete outcomes

**Key Concepts:**
- **Hexagonal Architecture:** Isolates core via ports/adapters. Enables testability, tech independence
- **CQRS (Command Query Responsibility Segregation):** Separates commands (writes) from queries (reads). Optimizes scalability
- **Event Sourcing:** Stores state as event log. Enables audit, temporal queries
- **DDD (Domain-Driven Design):** Software design approach using ubiquitous language, bounded contexts, strategic/tactical patterns
- **Bounded Context:** Explicit model boundary for consistency. Drives decomposition
- **ADR (Architecture Decision Records):** Documented architecture decisions with context, rationale, consequences
- **Conway's Law:** Organizations design systems mirroring their communication structure
- **Circuit Breaker:** Prevents cascading failures. Opens on error threshold
- **MECE:** Mutually Exclusive, Collectively Exhaustive—no overlaps, no gaps

## Requirements

### Scenario Bank

**Scope:** 16–22 scenarios; 20% Foundational / 40% Intermediate / 40% Advanced; 5 domain clusters with 3–5 scenarios each: (1) Structural Design, (2) Behavioral Patterns, (3) Quality Attributes, (4) Data Architecture, (5) System Evolution.

**Diversity:** ≥3 industries (tech, healthcare, finance, manufacturing); ≥2 company sizes (startup, SME, enterprise); ≥2 contexts (greenfield, legacy migration, scale-up).

### Scenario Structure

Each scenario includes:

**Context (200–400 words):** ≥2 technical constraints, ≥2 stakeholder roles (diverse: architects, engineers, product managers, operations), ≥1 system requirement, ≥1 organizational factor, ≥1 `[Ref: ID]` citation.

**Tasks (3–4):** MECE (Mutually Exclusive, Collectively Exhaustive) tasks spanning requirements analysis → architecture decisions. Types: pattern selection, component design, trade-off analysis, ADR creation, migration planning.

**Deliverables:**
- **Architecture Diagram:** Component/sequence/deployment diagrams (Mermaid format, <120 nodes). Must show clear component boundaries and interaction flows.
- **Trade-off Matrix:** Architectural options → pros/cons/metrics + decision rationale (comparison table). Include quantified metrics (latency, throughput, cost) with cited sources or "estimated" flag.
- **Implementation Plan:** Code snippets (10-30 lines, production-ready with error handling), technology choices with version specifications, integration approach with dependency considerations.
- **Decision Memo:** ≤300 words: recommendations with risk mitigation strategies, technical justification with reasoning chain, quantified trade-offs, implementation risks with probability/impact assessment. Acknowledge uncertainties and alternative perspectives.

**Grading:** Requirements analysis (25%), architecture design (35%), implementation approach (25%), justification (15%). Specify partial credit point allocations.

**Trade-Offs:** Address scalability vs complexity, consistency vs availability, coupling vs performance, time-to-market vs technical debt. Quantify where possible (e.g., "3x latency for 10x flexibility"). Prioritize high-value, low-risk options; flag high-risk choices with mitigation strategies.

**Conflicts:** When patterns conflict (microservices vs monolith, CQRS vs CRUD, sync vs async), present balanced perspectives with citations for each option. State trade-offs with quantified impact. Recommend context-specific choice with logical reasoning chain. Acknowledge limitations, biases, and counterarguments.

### References

**Language:** ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH])

**Source Types (all 4 required):** (1) Architecture patterns (Hexagonal, CQRS, Event-Driven, DDD), (2) Quality attributes (performance, scalability, reliability, security), (3) Case studies/reports (prioritize peer-reviewed, industry-validated), (4) Tools (modeling, documentation, deployment).

**Quality Requirements:** Prioritize authoritative, high-quality, tested sources. Avoid low-quality or unproven content. Prefer peer-reviewed academic papers, established industry books, and production-validated case studies. Flag uncertainties with "estimated", "approximate", or "unverified" tags.

**Format:** APA 7th + language tags. Inline: `[Ref: ID]`. Verify factual correctness; cross-check publication years and author names.

**Minimums:** Glossary ≥10 (Hexagonal, CQRS, Event Sourcing, DDD, Aggregate, Saga, Circuit Breaker, Bounded Context, Domain Event, Repository), Tools ≥5 (Mermaid, OpenAPI, Kubernetes, ArchiMate, C4), Literature ≥6 (Fowler, Evans, Vernon, Richardson, Newman, Kleppmann + ZH sources), APA ≥12. If unmet: state shortfall, rationale, sourcing plan. Scale: >25 scenarios → multiply by 1.5×.

---

## Output Format

### Structure

**Contents:** TOC linking to Scenario Bank (all scenarios), Reference Sections (Glossary, Tools, Literature, APA Citations), Validation Report.

**Quality Standards:**
- **Clarity:** Use clear, understandable explanations. Define all technical terms in Glossary.
- **Precision:** Maintain consistent terminology throughout. Use specific, unambiguous language.
- **Relevance:** Stay on topic. Exclude tangential information.
- **Concision:** Remove redundancy. Include only essential information.
- **Logic:** Ensure coherent reasoning with sound structure. Each recommendation must include logical justification chain.

### Scenario Template

**Scenario X: [Title]** | **Difficulty:** [F/I/A] | **Domain:** [Cluster]

**Context:** 200–400 words (≥2 technical constraints, ≥2 stakeholders, ≥1 system requirement, ≥1 org factor, ≥1 `[Ref: ID]`). Must provide sufficient context for informed decisions while remaining focused and relevant.

**Task 1: [Name] (X pts)**  
Description requiring specified deliverable with clear success criteria.  
**Expected:** [Key elements with specific, measurable outcomes]  
**Grading:** [Criterion 1 (X pts) partial credit breakdown | Criterion 2 (Y pts) | ...] Must specify concrete evaluation metrics.  
**Reasoning Required:** Demand explicit reasoning chain showing how requirements connect to architectural choices.

**Task 2–4:** [Repeat]

**Common Omissions:** [e.g., missing Conway's Law impact, no scalability metrics, weak pattern-requirement tracing, missing error handling, lack of alternative consideration, no risk assessment]

**Bonus (1–2 pts):** [Advanced considerations: observability, chaos engineering, multi-region deployment, security posture, cost optimization]

**Self-Review Checkpoint:** Verify MECE coverage, logical coherence, factual accuracy, citation completeness, balanced perspectives.

### Reference Templates

**IDs:** Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA (A1…An). Inline: `[Ref: G1, T2, A5]`.

**Glossary:** Table with ID, Term, Definition (clear, precise, no jargon without definition), Use Cases, Related Terms. Ensure consistent terminology. Cover: Hexagonal, CQRS, Event Sourcing, DDD, Bounded Context, Aggregate, Repository, Domain Event, Saga, Circuit Breaker, API Gateway, Service Mesh.

**Tools:** Table with ID, Tool Name, Description (concise, relevant), Pricing (or "N/A" FOSS), Adoption (cited or flag "approximate"), Last Updated (≤18 months or mark "(legacy)"), Integrations ("standalone" if none), Use Cases, URL. Verify all URLs accessible. Examples: Mermaid, OpenAPI, Kubernetes, ArchiMate, C4, JSON Schema, ADR Tools.

**Literature:** Table with ID, Citation (APA 7th verified), Description (significance and relevance). Prioritize authoritative sources: peer-reviewed, established authors, production-validated. Examples: Fowler, Evans, Vernon, Richardson, Newman, Kleppmann, Hohpe, Skelton & Pais, 周爱民, 张逸.

**APA:** Full citations with language tags. Verify publication year/author names for factual correctness. Web refs: archived link or "as of [date]". Tool stats: cite credible source or mark "approximate"/"estimated". Cross-check all information.

### Validation Checklist

Execute all; proceed only when all PASS. If any FAIL: remediate and re-validate. Each check ensures adherence to quality standards: clarity, precision, accuracy, credibility, logic, and practicality.

| # | Check | Target | Result | Status |
|---|-------|--------|--------|--------|
| 1 | Count Audit | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 | [counts] | PASS/FAIL |
| 2 | Difficulty | 20/40/40 ±5% | [F%/I%/A%] | PASS/FAIL |
| 3 | Citation Coverage | ≥70% scenarios with ≥1, ≥30% with ≥2 | [%] | PASS/FAIL |
| 4 | Language | EN ~50-70%, ZH ~20-40%, Other ~5-15% | [%] | PASS/FAIL |
| 5 | Recency | ≥50% from 2022-2025 (≥70% cloud/distributed) | [%] | PASS/FAIL |
| 6 | Source Diversity | ≥3 types, no source >25% | [types, max%] | PASS/FAIL |
| 7 | Links | All accessible OR archived | [broken: URLs] | PASS/FAIL |
| 8 | Cross-Refs | All `[Ref: ID]` resolve | [broken: IDs] | PASS/FAIL |
| 9 | Context Length | 200–400 words | [sample 5] | PASS/FAIL |
| 10 | MECE Tasks | No overlaps/gaps | [issues] | PASS/FAIL |
| 11 | Rubrics | Complete with partial credit | [missing] | PASS/FAIL |
| 12 | Requirements-Architecture Map | ≥80% explicit connection | [%] | PASS/FAIL |
| 13 | Stakeholder Diversity | ≥70% diverse roles (not only architects) | [%] | PASS/FAIL |
| 14 | Industry/Size/Context | ≥3 industries, ≥2 sizes, ≥2 contexts | [lists] | PASS/FAIL |
| 15 | Code Quality | 100% valid syntax, production-ready | [issues] | PASS/FAIL |
| 16 | Diagrams | ≥80% scenarios include diagrams | [%] | PASS/FAIL |
| 17 | Quantified Trade-offs | ≥70% include metrics (latency, throughput, etc.) | [%] | PASS/FAIL |
| 18 | TOC & Anchors | Functional links | [Y/N] | PASS/FAIL |
| 19 | Reasoning Chains | ≥80% decisions include explicit reasoning | [%] | PASS/FAIL |
| 20 | Uncertainty Flags | All estimates/approximations flagged | [unflagged] | PASS/FAIL |
| 21 | Balanced Perspectives | ≥60% conflicts show multiple viewpoints | [%] | PASS/FAIL |
| 22 | Risk Assessment | ≥70% high-risk choices include mitigation | [%] | PASS/FAIL |
| 23 | Terminology Consistency | No conflicting term usage | [conflicts] | PASS/FAIL |
| 24 | Redundancy Check | No duplicate information | [duplicates] | PASS/FAIL |

## Generation Procedure

Execute sequentially. Validate at checkpoints (✓).

**Step 1: Plan** — Allocate 16–22 scenarios across 5 clusters (3–5 each): Structural Design, Behavioral Patterns, Quality Attributes, Data Architecture, System Evolution. Assign difficulty: 20% F, 40% I, 40% A. Ensure MECE coverage (no overlaps/gaps) across clusters.  
**✓** Total 16–22? Difficulty 20/40/40 ±5%? MECE verified?

**Step 2: Collect References** — Gather Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 (language ~60/30/10). Prioritize authoritative, high-quality, tested sources. Verify factual correctness. Assign IDs: G1-Gn, T1-Tn, L1-Ln, A1-An.  
**✓** Counts met? Language distribution ~60/30/10? Recency ≥50% (≥70% cloud/distributed)? Diversity ≥3 types, no source >25%? Sources credible and verified?

**Step 3: Generate Scenarios** — For each: (1) Context 200–400 words (≥2 technical constraints, ≥2 stakeholders, ≥1 system requirement, ≥1 org factor, ≥1 `[Ref: ID]`; vary industry/size/context; maintain clarity, precision, relevance); (2) Design 3–4 MECE tasks with explicit success criteria and reasoning requirements (requirements analysis → architecture decisions; deliverables: architecture diagram, trade-off matrix with quantified metrics, implementation plan with error handling, decision memo with risk mitigation); (3) Create rubrics (25/35/25/15%) with partial credit, common omissions, and measurable evaluation criteria; (4) Add bonus (1–2 pts) for advanced considerations.  
**✓** (Every 3 scenarios) Context 200–400 words, ≥1 citation, diverse stakeholders? MECE (no overlaps/gaps)? Rubrics complete with measurable criteria? Diversity? Reasoning chains explicit? Risk assessments included?

**Step 4: Compile References** — Populate tables (Glossary: ID/Term/Definition/Use Cases/Related; Tools: ID/Name/Description/Pricing/Adoption/Updated/Integrations/Use Cases/URL; Literature: ID/Citation/Description; APA: full with tags). Verify all inline `[Ref: ID]` resolve. Flag all uncertainties ("estimated", "approximate", "unverified").  
**✓** All refs resolve? Required fields present? Tool stats cited/"approximate"? Uncertainties flagged?

**Step 5: Validate** — Execute all 24 checks (Validation Checklist). If any FAIL: remediate and re-validate. Proceed only when all PASS.

**Step 6: Self-Review** — Perform quality review:
- **Clarity:** All technical terms defined? Explanations understandable?
- **Precision:** Terminology consistent? No ambiguity?
- **Relevance:** All content on-topic? No tangential information?
- **Concision:** Redundancy removed? Only essential information included?
- **Accuracy:** Facts verified? Cross-checked?
- **Logic:** Reasoning chains coherent? Structure sound?
- **Fairness:** Balanced perspectives? Alternatives acknowledged?
- **Practicality:** Guidance actionable and implementable?

**Step 7: Finalize** — Verify TOC/anchors functional, match output format, confirm all quality standards met.

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
