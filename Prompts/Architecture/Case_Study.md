# Case Study: Architecture Decision Assessment Generator

## Purpose

**Objective:** Generate multi-scenario assessments evaluating technical leaders' ability to translate requirements into architecture decisions.

**Target:** Exam designers, educators, enterprise architects, training developers.

**Scope:** 16–22 scenarios across 5 clusters (Structural Design, Behavioral Patterns, Quality Attributes, Data Architecture, System Evolution).

**Constraints:** Production-ready code, accessible citations, MECE coverage, 20/40/40% difficulty.

**Assumptions:** Intermediate architecture knowledge; real-world complexity; immediately usable outputs.

## Standards

Apply all guidelines from Guidelines_for_LLM-Friendly_Prompts.md. Key requirements:
- **Clarity:** Define all jargon; use specific, consistent terms
- **MECE:** No overlaps/gaps in coverage
- **Concision:** Essential information only
- **Evidence:** Cite authoritative sources; flag uncertainty
- **Logic:** Explicit reasoning chains
- **Risk/Value:** Quantify trade-offs; prioritize high-value, low-risk; mitigate high-risk
- **Fairness:** Balanced perspectives; acknowledge limitations, alternatives
- **Structure:** Tables, diagrams, code blocks; TOC linking sections
- **Validation:** Self-review, error checks, measurable outcomes

## Requirements

### Scenario Bank

**Distribution:** 16–22 scenarios; 20% Foundational / 40% Intermediate / 40% Advanced; 3–5 per cluster.

**Diversity:** ≥3 industries (tech, healthcare, finance, manufacturing); ≥2 sizes (startup, SME, enterprise); ≥2 contexts (greenfield, legacy migration, scale-up).

### Scenario Structure

**Context (200–400 words):** ≥2 technical constraints, ≥2 stakeholder roles (diverse), ≥1 system requirement, ≥1 org factor, ≥1 `[Ref: ID]`.

**Tasks (3–4):** MECE tasks spanning requirements analysis → architecture decisions. Types: pattern selection, component design, trade-off analysis, ADR, migration planning.

**Deliverables:**
- **Diagram:** Mermaid (<120 nodes); show boundaries, flows
- **Trade-off Matrix:** Options → pros/cons/metrics + rationale; quantify (latency, throughput, cost); cite or flag "estimated"
- **Implementation:** Code (10-30 lines, production-ready, error handling), tech + versions, integration + dependencies
- **Decision Memo (≤300 words):** Recommendations + risk mitigation, reasoning chain, quantified trade-offs, risk (probability/impact), uncertainties, alternatives

**Grading:** Requirements (25%), architecture (35%), implementation (25%), justification (15%). Specify partial credit.

**Trade-Offs:** Scalability vs complexity, consistency vs availability, coupling vs performance, time-to-market vs debt. Quantify (e.g., "3x latency for 10x flexibility"). Prioritize high-value/low-risk; flag high-risk + mitigation.

**Conflicts:** For conflicting patterns (microservices vs monolith, CQRS vs CRUD, sync vs async), present balanced perspectives with citations, quantified trade-offs, reasoning chain. Acknowledge limitations, biases, counterarguments.

### References

**Language:** ~60% EN, ~30% ZH, ~10% other (tag: [EN]/[ZH])

**Types (all 4):** (1) Architecture patterns, (2) Quality attributes, (3) Case studies (peer-reviewed/industry-validated), (4) Tools.

**Quality:** Prioritize authoritative, tested sources (peer-reviewed papers, established books, production-validated cases). Flag uncertainties ("estimated"/"approximate"/"unverified").

**Format:** APA 7th + tags. Inline: `[Ref: ID]`. Verify facts, cross-check years/authors.

**Minimums:** Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12. If unmet: state shortfall, rationale, plan. Scale: >25 scenarios → 1.5×.

---

## Output Format

**Structure:** TOC linking to Scenario Bank, References (Glossary, Tools, Literature, APA), Validation Report.

### Scenario Template

**Scenario X: [Title]** | **Difficulty:** [F/I/A] | **Domain:** [Cluster]

**Context:** 200–400 words (≥2 constraints, ≥2 stakeholders, ≥1 requirement, ≥1 org factor, ≥1 `[Ref: ID]`).

**Task 1: [Name] (X pts)**  
Description with deliverable and success criteria.  
**Expected:** [Measurable outcomes]  
**Grading:** [Criterion 1 (X pts) partial credit | Criterion 2 (Y pts) | ...]  
**Reasoning:** Explicit chain connecting requirements → architecture.

**Task 2–4:** [Repeat]

**Common Omissions:** [e.g., Conway's Law, scalability metrics, pattern tracing, error handling, alternatives, risk assessment]

**Bonus (1–2 pts):** [Observability, chaos engineering, multi-region, security, cost]

**Self-Review:** Verify MECE, logic, accuracy, citations, balance.

### Reference Templates

**IDs:** G1…Gn (Glossary), T1…Tn (Tools), L1…Ln (Literature), A1…An (APA). Inline: `[Ref: G1, T2, A5]`.

**Glossary:** Table: ID | Term | Definition | Use Cases | Related. Cover: Hexagonal, CQRS, Event Sourcing, DDD, Bounded Context, Aggregate, Repository, Domain Event, Saga, Circuit Breaker.

**Tools:** Table: ID | Name | Description | Pricing | Adoption | Updated (≤18mo or "(legacy)") | Integrations | Use Cases | URL. Verify URLs. Examples: Mermaid, OpenAPI, Kubernetes, C4.

**Literature:** Table: ID | Citation (APA 7th) | Description. Prioritize peer-reviewed, established authors, production-validated. Examples: Fowler, Evans, Vernon, Richardson, Newman, Kleppmann.

**APA:** Full citations + tags. Verify year/author. Web: archived or "as of [date]". Stats: cite or mark "approximate"/"estimated".

### Validation Checklist

Execute all; proceed only when PASS. If FAIL: remediate, re-validate.

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

**Step 1: Plan** — Allocate 16–22 scenarios: 5 clusters (3–5 each), 20/40/40% difficulty. Ensure MECE.  
**✓** Total 16–22? Difficulty 20/40/40 ±5%? MECE?

**Step 2: Collect References** — Gather: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 (EN ~60%, ZH ~30%). Prioritize authoritative, tested sources. Assign IDs.  
**✓** Counts? Language ~60/30/10? Recency ≥50% (≥70% cloud)? Diversity ≥3 types, max 25%? Credible?

**Step 3: Generate Scenarios** — For each: (1) Context 200–400 words (≥2 constraints, ≥2 stakeholders, ≥1 requirement, ≥1 org factor, ≥1 `[Ref: ID]`; vary industry/size/context); (2) 3–4 MECE tasks with success criteria, reasoning requirements (deliverables: diagram, trade-off matrix with metrics, implementation with error handling, decision memo with risk); (3) Rubrics (25/35/25/15%) with partial credit, omissions, metrics; (4) Bonus (1–2 pts).  
**✓** (Every 3) Context 200–400, ≥1 citation, diverse? MECE? Rubrics complete? Reasoning explicit? Risk included?

**Step 4: Compile References** — Populate tables. Verify `[Ref: ID]` resolve. Flag uncertainties.  
**✓** Refs resolve? Fields present? Stats cited/"approximate"? Uncertainties flagged?

**Step 5: Validate** — Execute 24 checks. FAIL → remediate, re-validate.

**Step 6: Self-Review** — Verify: clarity, precision, relevance, concision, accuracy, logic, fairness, practicality.

**Step 7: Finalize** — Verify TOC/anchors, format, standards.

# Reference Examples

## Glossary
**G1. Hexagonal** [EN] – Isolates core via ports/adapters. Enables testability, tech independence. Related: DI  
**G2. CQRS** [EN] – Separates commands from queries. Optimizes scalability. Related: Event Sourcing  
**G3. Event Sourcing** [EN] – Stores state as event log. Audit, temporal queries. Related: CQRS  
**G4. DDD** [EN] – Domain modeling via ubiquitous language, bounded contexts. Related: Bounded Context  
**G5. Bounded Context** [EN] – Explicit boundary for consistency. Drives decomposition. Related: Context Map  
**G6. Aggregate** [EN] – Consistency boundary. Enforces invariants. Related: Repository  
**G7. Repository** [EN] – Data access abstraction for aggregates. Related: Aggregate  
**G8. Domain Event** [EN] – Immutable fact. Decoupling, eventual consistency. Related: Event Sourcing  
**G9. Saga** [EN] – Coordinates long transactions with compensations. Related: Distributed TX  
**G10. Circuit Breaker** [EN] – Prevents cascading failures. Related: Bulkhead

## Tools
**T1. Mermaid** [EN] – Text-based diagrams. GitHub-native. 2024-10. Free. https://mermaid.js.org  
**T2. OpenAPI** [EN] – REST API spec. Codegen, testing. 2024-09. Free. https://www.openapis.org  
**T3. JSON Schema** [EN] – JSON validation, docs. 2024-08. Free. https://json-schema.org  
**T4. Kubernetes** [EN] – Container orchestration. 2024-10. Free. https://kubernetes.io  
**T5. ADR** [EN] – Decision log. Traceability. 2024-06. Free. https://adr.github.io

## Literature
**L1.** Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley. – Strategic/tactical modeling  
**L2.** Vernon, V. (2013). *Implementing DDD*. Addison-Wesley. – Context mapping, aggregates  
**L3.** Richardson, C. (2018). *Microservices Patterns*. Manning. – Decomposition, patterns, trade-offs  
**L4.** Newman, S. (2021). *Building Microservices* (2nd). O'Reilly. – Boundaries, deployment  
**L5.** Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. – Distributed systems  
**L6.** Fowler, M. (2002). *Patterns of Enterprise Application Architecture*. Addison-Wesley. – Repository, patterns

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
