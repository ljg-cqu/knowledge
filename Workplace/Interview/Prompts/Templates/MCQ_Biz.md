# Multiple-Choice Questions - Business Understanding for Software Architecture

Framework for generating high-quality MCQ assessments focused on comprehensive business understanding that benefits software architecture decisions.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Scope**: 40–80 MCQs for senior/architect/expert level technical leaders
- **Format**: Concise stems (1–2 sentences), 4 options, exactly one correct
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Distractors**: Map to business-technical misalignments, outdated practices, or framework misapplications
- **Rationale**: 1–2 sentences with citation; explicitly connect business drivers to architectural implications
- **Grading**: Machine-gradable; no partial credit
- **Conflict Handling**: For contentious frameworks (BMC vs Lean Canvas), distractors reflect legitimate competing views; rationale clarifies context-dependent applicability

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH], etc.)
- **Source Types**: (1) Business frameworks & methodologies; (2) Architecture patterns & practices; (3) Case studies & industry reports; (4) Tools & platforms
- **Format**: APA 7th with language tags
- **Inline Citation**: Use [Ref: ID] in rationales when referencing business models, frameworks, architectural patterns, trade-offs

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Business Model Canvas, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, etc. |
| Business & Architecture Tools | ≥5 entries | Miro, ArchiMate/C4, Confluence, LucidChart, Wardley Maps |
| Authoritative Literature & Reports | ≥6 entries | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

### Quality Gates

- Recency: ≥50% citations from last 3 years (≥70% for digital transformation/cloud-native)
- Source diversity: ≥3 source types; no single source >25%
- Evidence coverage: ≥70% questions with ≥1 citation; ≥30% with ≥2 citations
- Tool maturity: Pricing, adoption metrics, last update ≤18 months, key integrations
- Business-Technical Mapping: ≥70% questions test business-to-architecture translation

### Pre-Submission Validation

**Step 1 – Count Audit**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Questions 40-80 (20/40/40)
**Step 2 – Citation Coverage**: ≥70% have ≥1; ≥30% have ≥2
**Step 3 – Language**: EN 50-70%, ZH 20-40%, Other 5-15%
**Step 4 – Recency**: ≥50% last 3yr (≥70% for digital transformation)
**Step 5 – Source Diversity**: ≥3 types; no single >25%
**Step 6 – Links**: All accessible or archived
**Step 7 – Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
**Step 8 – Answer Correctness**: Exactly one correct per question
**Step 9 – Distractor Quality**: Map to business-technical misalignments
**Step 10 – Option Unambiguity**: Mutually exclusive, unambiguous
**Step 11 – Business-Technical Mapping**: ≥70% test translation skills

---

# Part II: Instructions

### Step 1: Topic Identification & Planning
1. Identify 4-8 clusters: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation
2. Allocate 5-10 questions per cluster (total 40-80); assign 20/40/40 difficulty
3. **Check**: Total = 40-80, ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather ≥10 glossary (BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, etc.)
2. Gather ≥5 tools (Miro, ArchiMate/C4, Confluence, LucidChart, Wardley Maps)
3. Gather ≥6 literature (Osterwalder, Evans, Vernon, Conway, Skelton, Richardson + ZH sources)
4. Gather ≥12 APA citations; tag language, year, type
5. **Check**: Counts, language ~60/30/10%, recency ≥50%, diversity ≥3 types

### Step 3: Question Generation
1. Write stems testing business-to-architecture translation (not just recall)
2. Create 4 options: 1 correct + 3 distractors mapping to specific misalignments
3. Write rationales with ≥1 [Ref: ID]; explicitly connect business to architecture
4. **Check**: Every 10 questions verify: exactly one correct, quality distractors, business-technical mapping, citations

### Step 4: Reference Compilation
Populate Glossary/Tools/Literature/APA; ensure all [Ref: ID] resolve

### Step 5: Validation
Execute all 11 steps; fix failures; re-validate until all PASS

---

# Part III: Output Format

```markdown
## Question Bank (Questions 1–N)

### Topic 1: Strategic Modeling

#### Q1: A company shifts from perpetual licensing to SaaS subscription. Which Business Model Canvas building block change MOST directly drives the need for multi-tenancy architecture?

**Difficulty:** Intermediate

**Options:**
- A. Key Partnerships (need cloud infrastructure providers)
- B. Revenue Streams (recurring revenue requires shared infrastructure for cost efficiency)
- C. Customer Relationships (continuous engagement needs better UX)
- D. Channels (online delivery requires web architecture)

**Answer:** B

**Rationale:** Revenue model shift to recurring subscription drives cost optimization requirements [Ref: G1]. Multi-tenancy enables shared infrastructure to reduce per-customer costs while maintaining isolation [Ref: A7], directly supporting the subscription economics.

**Distractor notes:**
- A: Partnerships are enablers but don't drive multi-tenancy need
- C: UX improvements are separate from multi-tenancy architecture
- D: Web delivery doesn't require multi-tenancy specifically

---

## Reference Sections

### Glossary, Terminology & Acronyms

**G1. Business Model Canvas (BMC)**: 9-block template (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure). Maps business model to technical requirements. [EN]

**G2. Value Proposition**: Bundle of products/services creating value for customer segment. Maps to technical features and quality attributes (performance, reliability, usability). [EN]

**G3. Domain-Driven Design (DDD)**: Approach focusing on complex domain modeling through technical-domain expert collaboration. Used for microservices boundaries, team organization. [EN]

**G4. Conway's Law**: "Organizations design systems mirroring their communication structure." Used for team topology design, architecture alignment. [EN]

**G5. Technical Debt**: Cost of rework from choosing quick solutions over better long-term approaches. Used for refactoring prioritization, risk assessment. [EN]

**G6. Architecture Decision Records (ADR)**: Lightweight documentation of architectural decisions, context, consequences, trade-offs. Used for decision transparency, knowledge preservation. [EN]

**G7. Bounded Context**: DDD pattern defining explicit boundaries for domain model validity. Used for microservices decomposition, team autonomy. [EN]

**G8. Capability Mapping**: Identifying business capabilities independent of implementation. Used for strategic planning, gap analysis, transformation roadmaps. [EN]

**G9. Living Documentation**: Documentation evolving with system through automation. Used for knowledge sharing, architectural understanding. [EN]

**G10. Wardley Mapping**: Strategic planning visualizing components by visibility and evolution. Used for strategic decision-making, anticipating change. [EN]

**G11. Customer Segment**: Distinct groups of people/organizations an enterprise aims to reach and serve. Maps to system design decisions (interfaces, workflows, data models). Used for market targeting, personalization. [EN]

**G12. Revenue Stream**: Ways an organization generates income from customer segments (e.g., subscription, usage-based, freemium). Directly impacts architectural requirements (metering, billing, multi-tenancy). [EN]

**G13. Value Stream Mapping**: Lean technique visualizing steps in delivering value to customers, identifying waste and bottlenecks. Used for process optimization, lead time reduction. [EN]

**G14. System Boundaries**: Explicit definition of what is inside vs outside the system scope; determines interfaces and integration points. Used for context diagrams, scope management. [EN]

**G15. Process Mapping**: Visual documentation of workflows, activities, decision points, and information flows. Used for optimization, automation, understanding current state. [EN]

### Business & Architecture Tools

**T1. Miro**: Visual collaboration for Business Model Canvas, architecture diagrams. Freemium-Enterprise. 80M+ users. Q4 2024 update. https://miro.com [EN]

**T2. ArchiMate**: Enterprise architecture modeling standard (business, application, technology layers). ISO/IEC/IEEE 42010 compliant. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model**: Hierarchical architecture diagrams (Context, Container, Component, Code). Free, tool-agnostic. https://c4model.com [EN]

**T4. Confluence**: Documentation platform for ADRs, living documentation. Free-Enterprise. 75K+ companies. Q3 2024 update. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart**: Cloud diagramming for process maps, architecture diagrams. Individual-Enterprise. 60M+ users. Q4 2024 update. https://www.lucidchart.com [EN]

### Authoritative Literature & Case Studies

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** BMC framework; business-technical alignment.

**L2. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** DDD patterns; domain modeling.

**L3. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical DDD; context mapping.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28-31.** Conway's Law; organizational impact.

**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.** Team organization patterns.

**L6. Richardson, C. (2018). *Microservices Patterns*. Manning.** Microservices decomposition, patterns.

### APA Style Source Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]**

**A2. Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley Professional. [EN]**

**A3. 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]**

**A4. Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley Professional. [EN]**

**A5. Conway, M. E. (1968). How do committees invent? *Datamation*, 14(4), 28-31. [EN]**

**A6. Skelton, M., & Pais, M. (2019). *Team topologies: Organizing business and technology teams for fast flow*. IT Revolution Press. [EN]**

**A7. Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning Publications. [EN]**

**A8. Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns*. Addison-Wesley Professional. [EN]**

**A9. 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]**

**A10. Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley Professional. [EN]**

**A11. Newman, S. (2021). *Building microservices* (2nd ed.). O'Reilly Media. [EN]**

**A12. 肖然. (2020). *企业级业务架构设计*. 机械工业出版社. [ZH]**

**A13. Brown, S. (2018). *Software architecture for developers* (Vol. 2). Leanpub. [EN]**

**A14. Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley Professional. [EN]**

**A15. Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution Press. [EN]**

**A16. Wardley, S. (2018). *Wardley maps: Topographical intelligence in business*. Medium. https://medium.com/wardleymaps [EN]**
```
