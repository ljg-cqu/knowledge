# True/False Statements - Business Understanding for Software Architecture

Generate high-quality true/false assessments testing business-architecture relationships for senior technical leaders.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Scope**: 18–32 statements targeting senior/architect/expert technical leaders
- **Format**: Declarative, ≤2 lines; no double negatives
- **Difficulty**: 20% Foundational, 40% Intermediate, 40% Advanced
- **Rationale**: 1–2 sentences with citations; link business concepts to architectural implications
- **Optional Justification**: 2–3 sentences (70% answer + 30% rationale)
- **Grading**: Machine-gradable (True/False)
- **Context-Dependent Statements**: Rationale clarifies assumptions (e.g., "Conway's Law always requires organizational restructuring")

### Citation Standards

- **Languages**: 60% EN, 30% ZH, 10% other; tag each [EN]/[ZH]
- **Source Types**: (1) Business frameworks/methodologies; (2) Architecture patterns/practices; (3) Case studies/reports; (4) Tools/platforms
- **Format**: APA 7th + language tags
- **Inline**: [Ref: ID] for frameworks, patterns, findings

### Reference Minimum Requirements

| Reference Section | Minimum | Examples |
|---|---|---|
| Glossary & Acronyms | ≥10 | BMC, Value Proposition, DDD, Conway's Law, Technical Debt |
| Tools & Platforms | ≥5 | Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps |
| Literature & Reports | ≥6 | Business strategy, architecture patterns, organizational design |
| APA Citations | ≥12 | 60% EN, 30% ZH, 10% other |

### Quality Gates

- **Recency**: ≥50% citations ≤3 years old (≥70% for digital transformation/cloud topics)
- **Diversity**: ≥3 source types; no type >25%
- **Coverage**: ≥70% statements have ≥1 citation; ≥30% have ≥2
- **Mapping**: ≥70% test business-architecture relationships

### Pre-Submission Validation

1. **Count Audit**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Statements 18-32 (20/40/40)
2. **Citation Coverage**: ≥70% have ≥1; ≥30% have ≥2
3. **Language Mix**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% ≤3yr (≥70% for digital transformation topics)
5. **Diversity**: ≥3 types; no type >25%
6. **Links**: All URLs accessible or archived
7. **Cross-refs**: All [Ref: ID] resolve to G#/T#/L#/A#
8. **Answers**: All True/False clearly justified
9. **Rationales**: All explain business-architecture link
10. **Mapping**: ≥70% test business-architecture relationships

---

# Part II: Instructions

### Step 1: Topic Identification & Planning
1. Identify 4-6 clusters: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation
2. Allocate 3-6 statements/cluster (total 18-32); maintain 20/40/40 difficulty
3. **Verify**: Total count 18-32; ratio approximates 20/40/40

### Step 2: Reference Collection
Collect ≥10 glossary entries, ≥5 tools, ≥6 literature sources, ≥12 APA citations; tag each with language, year, type

### Step 3: Statement Generation
1. Write declarative statements testing business-architecture relationships (avoid pure definitions)
2. Write rationales with ≥1 [Ref: ID]; explain business-technical link
3. **Verify**: Every 5 statements check: clear answer, complete rationale, business-technical mapping, citations present

### Step 4: Reference Compilation
Populate all reference sections (Glossary/Tools/Literature/APA); verify all [Ref: ID] resolve

### Step 5: Validation
Execute 10 validation checks; fix failures; iterate until 100% pass

---

# Part III: Output Format

```markdown
## Contents

- [Statement Bank](#statement-bank-statements-1-n)
  - [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Statement Bank (Statements 1–N)

### Topic 1: Strategic Modeling

#### Statement 1: A shift in the Revenue Streams building block of the Business Model Canvas always requires changes to the software architecture.

**Difficulty:** Intermediate

**Answer:** False

**Rationale:** Revenue model changes often drive architectural requirements (e.g., subscription → multi-tenancy) [Ref: G1, A1], but some changes (pricing adjustments, discount structures) are purely business-side. Impact depends on whether technical requirements change (metering, billing complexity, infrastructure sharing) [Ref: A7].

---

#### Statement 2: According to Conway's Law, organizational structure should be designed after the software architecture is finalized.

**Difficulty:** Advanced

**Answer:** False

**Rationale:** Conway's Law states "organizations design systems mirroring their communication structure" [Ref: G4, A5], meaning architecture reflects existing org structure, not vice versa. The Inverse Conway Maneuver restructures teams before architecture changes to enable desired design [Ref: A6]. Effective architects consider organizational dynamics during—not after—design [Ref: L4].

---

#### Statement 3: Technical debt always represents poor architectural decisions that should be eliminated immediately.

**Difficulty:** Intermediate

**Answer:** False

**Rationale:** Technical debt—choosing quick solutions over long-term approaches [Ref: G5]—can be strategic for time-to-market or hypothesis validation [Ref: A10]. Not all debt is harmful; some enables agility and should be managed, not eliminated. Key distinction: conscious debt with repayment plans vs. accidental accumulation [Ref: L2].

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
