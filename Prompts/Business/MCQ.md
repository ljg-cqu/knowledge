# MCQ Generator: Business Understanding for Software Architecture

Generates MCQ assessments testing business-to-architecture translation skills for senior technical leaders.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Scope**: 40–80 questions targeting senior/architect/expert technical leaders
- **Format**: 1–2 sentence stems, 4 options, 1 correct answer
- **Difficulty**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Distractors**: Map to business-technical misalignments, outdated practices, framework misapplications
- **Rationale**: 1–2 sentences with citation connecting business drivers to architectural implications
- **Grading**: Machine-gradable, no partial credit
- **Contentious Frameworks**: Distractors reflect competing views; rationales clarify context-dependent applicability

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tagged: [EN], [ZH])
- **Source Types**: Business frameworks, architecture patterns, case studies, tools/platforms
- **Format**: APA 7th edition with language tags
- **Inline**: [Ref: ID] for business models, frameworks, patterns, trade-offs

### Reference Minimum Requirements

| Section | Minimum | Examples |
| --- | --- | --- |
| Glossary & Acronyms | ≥10 | BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR |
| Tools & Platforms | ≥5 | Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps |
| Literature & Reports | ≥6 | Business strategy, architecture patterns, organizational design |
| APA Citations | ≥12 | Language mix: ~60% EN / ~30% ZH / ~10% other |

### Quality Gates

- **Recency**: ≥50% from last 3 years (≥70% for digital transformation/cloud-native)
- **Source Diversity**: ≥3 types; no single source >25%
- **Citation Coverage**: ≥70% questions cite ≥1 source; ≥30% cite ≥2 sources
- **Tool Maturity**: Pricing, adoption metrics, last update ≤18 months, integrations
- **Business-Technical Mapping**: ≥70% test translation skills

### Pre-Submission Validation

1. **Count Audit**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Questions 40-80 (20/40/40 difficulty)
2. **Citation Coverage**: ≥70% cite ≥1; ≥30% cite ≥2
3. **Language Mix**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% last 3yr (≥70% digital transformation/cloud-native)
5. **Source Diversity**: ≥3 types; no single >25%
6. **Link Validity**: All accessible or archived
7. **Cross-References**: All [Ref: ID] resolve to G#/T#/L#/A#
8. **Answer Correctness**: Exactly 1 correct per question
9. **Distractor Quality**: Map to specific business-technical misalignments
10. **Option Clarity**: Mutually exclusive and unambiguous
11. **Business Mapping**: ≥70% test business-to-architecture translation

---

# Part II: Instructions

### Step 1: Topic Identification & Planning
1. Identify 4-8 clusters: Strategic Modeling, Value & Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution & Adaptation
2. Allocate 5-10 questions per cluster (total 40-80) with 20/40/40 difficulty distribution
3. **Verify**: Total 40-80 questions, difficulty ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather ≥10 glossary entries (BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR)
2. Gather ≥5 tools (Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps)
3. Gather ≥6 literature sources (Osterwalder, Evans, Vernon, Conway, Skelton, Richardson + Chinese sources)
4. Gather ≥12 APA citations with language tag, year, type
5. **Verify**: Counts met, language ~60/30/10%, recency ≥50%, diversity ≥3 types

### Step 3: Question Generation
1. Write stems testing business-to-architecture translation (not mere recall)
2. Create 4 options: 1 correct + 3 distractors mapping to specific misalignments
3. Write rationales with ≥1 [Ref: ID] explicitly connecting business drivers to architecture
4. **Verify per 10 questions**: 1 correct answer, quality distractors, business-technical mapping, citations present

### Step 4: Reference Compilation
Populate all reference sections (Glossary, Tools, Literature, APA); verify all [Ref: ID] resolve

### Step 5: Validation
Execute all 11 validation steps; fix failures; repeat until all pass

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

**G1. Business Model Canvas (BMC)**: 9-block template for business modeling (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure). Maps to technical requirements. [EN]

**G2. Value Proposition**: Products/services creating customer value. Maps to features and quality attributes (performance, reliability, usability). [EN]

**G3. Domain-Driven Design (DDD)**: Complex domain modeling through technical-domain expert collaboration. Defines microservices boundaries and team organization. [EN]

**G4. Conway's Law**: "Organizations design systems mirroring their communication structure." Guides team topology and architecture alignment. [EN]

**G5. Technical Debt**: Rework cost from choosing expedient solutions over long-term quality. Guides refactoring prioritization and risk assessment. [EN]

**G6. Architecture Decision Records (ADR)**: Lightweight documentation capturing architectural decisions, context, consequences, and trade-offs. Enables decision transparency and knowledge preservation. [EN]

**G7. Bounded Context**: DDD pattern defining explicit domain model boundaries. Guides microservices decomposition and team autonomy. [EN]

**G8. Capability Mapping**: Business capabilities identified independent of implementation. Supports strategic planning, gap analysis, and transformation roadmaps. [EN]

**G9. Living Documentation**: Automated documentation evolving with the system. Enables knowledge sharing and architectural understanding. [EN]

**G10. Wardley Mapping**: Strategic visualization of components by visibility and evolution stage. Supports strategic decisions and change anticipation. [EN]

**G11. Customer Segment**: Distinct target groups an enterprise serves. Maps to system design (interfaces, workflows, data models) for targeting and personalization. [EN]

**G12. Revenue Stream**: Income generation method (subscription, usage-based, freemium). Drives architectural requirements (metering, billing, multi-tenancy). [EN]

**G13. Value Stream Mapping**: Lean technique visualizing value delivery steps to identify waste and bottlenecks. Enables process optimization and lead time reduction. [EN]

**G14. System Boundaries**: Explicit scope definition determining interfaces and integration points. Used in context diagrams and scope management. [EN]

**G15. Process Mapping**: Visual documentation of workflows, activities, decisions, and information flows. Supports optimization, automation, and current-state analysis. [EN]

### Business & Architecture Tools

**T1. Miro**: Visual collaboration platform for BMC and architecture diagrams. Freemium-Enterprise. 80M+ users. Last update: Q4 2024. https://miro.com [EN]

**T2. ArchiMate**: Enterprise architecture modeling standard for business, application, and technology layers. ISO/IEC/IEEE 42010 compliant. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model**: Hierarchical architecture diagrams (Context, Container, Component, Code). Free, tool-agnostic. https://c4model.com [EN]

**T4. Confluence**: Documentation platform for ADRs and living documentation. Free-Enterprise. 75K+ companies. Last update: Q3 2024. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart**: Cloud diagramming for process maps and architecture diagrams. Individual-Enterprise. 60M+ users. Last update: Q4 2024. https://www.lucidchart.com [EN]

### Authoritative Literature & Case Studies

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** Defines BMC framework for business-technical alignment.

**L2. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** Foundational DDD patterns and domain modeling techniques.

**L3. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical DDD implementation and context mapping.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28-31.** Original Conway's Law paper on organizational impact.

**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.** Modern team organization patterns for fast flow.

**L6. Richardson, C. (2018). *Microservices Patterns*. Manning.** Microservices decomposition strategies and implementation patterns.

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
