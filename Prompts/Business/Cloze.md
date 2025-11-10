# Cloze / Fill-in-the-Blank — Business Understanding for Software Architecture

Generate cloze assessments mapping business concepts to architectural implications.

---

# Part I: Specifications

## Context & Scope

- **Audience**: Senior/architect/expert technical leaders
- **Goal**: 24–40 items testing business-to-architecture understanding
- **Output**: Markdown; items grouped by topic clusters

## Structure & Difficulty

- **Format**: Unambiguous blanks (___); acceptance array per item
- **Difficulty**: 20/40/40 split (Foundational/Intermediate/Advanced)
- **MECE**: Non-overlapping clusters and items; complete coverage

## Grading & Normalization

- **Normalization**: Case-insensitive; trim whitespace; strip punctuation; numeric tolerances specified
- **Grading**: Acceptance lists; borderline answers documented; partial credit defined where applicable
- **Conflict Handling**: Contested terminology includes valid variants from different schools/regions

## Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tagged: [EN], [ZH])
- **Source Types**: Business frameworks, architecture patterns, case studies, tools
- **Format**: APA 7th with language tags
- **Inline**: [Ref: ID] in rationales; explicit uncertainty flags

## Reference Minimum Requirements

| Reference Section | Minimum | Examples |
|---|---|---|
| Glossary, Terminology & Acronyms | ≥10 | BMC, Value Proposition, DDD, Conway's Law, Technical Debt |
| Business & Architecture Tools | ≥5 | Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps |
| Authoritative Literature & Reports | ≥6 | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 | Language mix: ~60% EN, ~30% ZH, ~10% other |

## Quality Gates

- **Recency**: ≥50% citations ≤3 years old (≥70% for digital transformation/cloud-native)
- **Diversity**: ≥3 source types; single source ≤25%
- **Coverage**: ≥70% items have ≥1 citation; ≥30% have ≥2
- **Mapping**: ≥70% items test business-to-architecture terminology
- **MECE**: Non-overlapping topics and items; no redundancy

## Success Criteria

- **Counts**: 24–40 items; 20/40/40 difficulty; reference minimums met
- **Quality Gates**: Citations, recency, diversity, coverage satisfied
- **References**: All [Ref: ID] resolve (G#/T#/L#/A#); links accessible/archived
- **Items**: Unambiguous blanks; complete acceptance lists

---

# Part II: Instructions

## Step 1: Topic Identification & Planning
1. Select 4–6 clusters: Strategic Modeling, Value & Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution & Adaptation
2. Allocate 4–8 items per cluster (24–40 total); 20/40/40 difficulty split
3. Verify MECE: non-overlapping clusters, complete coverage

## Step 2: Reference Collection
Gather references with language/year/type tags:
- ≥10 glossary entries
- ≥5 tools
- ≥6 literature sources
- ≥12 APA citations

## Step 3: Item Generation
1. Write unambiguous blanks targeting business–architecture terminology
2. Build acceptance lists (synonyms, variants)
3. Add rationales with ≥1 [Ref: ID]
4. Review every 5 items: ambiguity, acceptance lists, citations

## Step 4: Reference Compilation
Populate all sections; verify [Ref: ID] resolution

## Step 5: Self-Review & Validation
1. **Counts**: Glossary ≥10; Tools ≥5; Literature ≥6; APA ≥12; Items 24–40 (20/40/40)
2. **Citation coverage**: ≥70% have ≥1; ≥30% have ≥2
3. **Language mix**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: ≥50% ≤3y (≥70% for digital transformation)
5. **Source diversity**: ≥3 types; single ≤25%
6. **Links**: All accessible/archived
7. **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
8. **Answer completeness**: Complete acceptance lists
9. **Blank clarity**: All blanks unambiguous
10. **Mapping**: ≥70% test business–architecture terminology

---

# Part III: Output Format

Start the output with a TOC (e.g., '## Contents') linking to all top-level headings and list items.

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with language-tagged fences.

```markdown
## Table of Contents

### [Item Bank](#item-bank-items-1n)
- [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
- [Topic 2: Value & Risk Analysis](#topic-2-value--risk-analysis)
- [Topic 3: Organizational Dynamics](#topic-3-organizational-dynamics)
- [Topic 4: Architectural Translation](#topic-4-architectural-translation)
- [Topic 5: Evolution & Adaptation](#topic-5-evolution--adaptation)

### [Reference Sections](#reference-sections)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Business & Architecture Tools](#business--architecture-tools)
- [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
- [APA Style Source Citations](#apa-style-source-citations)

---

## Item Bank (Items 1–N)

### Topic 1: Strategic Modeling

#### Item 1: The ___ framework uses 9 building blocks to map business models to technical requirements.

**Difficulty:** Foundational

**Acceptable Answers:**
- Business Model Canvas
- BMC
- Business Model Canvas (BMC)

**Rationale:** Business Model Canvas [Ref: G1] provides structured analysis of business model changes and architectural implications [Ref: A1].

---

#### Item 2: When a company shifts from perpetual licensing to SaaS, the ___ building block changing from upfront to recurring directly drives multi-tenancy requirements.

**Difficulty:** Intermediate

**Acceptable Answers:**
- Revenue Streams
- Revenue Stream
- Revenue

**Rationale:** Recurring subscription revenue drives cost optimization [Ref: G1], requiring multi-tenancy for shared infrastructure efficiency [Ref: A7].

---

## Reference Sections

### Glossary, Terminology & Acronyms

**G1. Business Model Canvas (BMC)**: 9-block template (Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure) mapping business models to technical requirements. [EN]

**G2. Value Proposition**: Product/service bundle creating customer value. Maps to technical features and quality attributes (performance, reliability, usability). [EN]

**G3. Domain-Driven Design (DDD)**: Complex domain modeling via technical-domain expert collaboration. Defines microservices boundaries and team organization. [EN]

**G4. Conway's Law**: "Organizations design systems mirroring their communication structure." Guides team topology and architecture alignment. [EN]

**G5. Technical Debt**: Rework cost from choosing quick solutions over sustainable approaches. Prioritizes refactoring and risk assessment. [EN]

**G6. Architecture Decision Records (ADR)**: Lightweight documentation capturing architectural decisions, context, consequences, trade-offs. Ensures decision transparency and knowledge preservation. [EN]

**G7. Bounded Context**: DDD pattern defining explicit domain model boundaries. Enables microservices decomposition and team autonomy. [EN]

**G8. Capability Mapping**: Identifying implementation-independent business capabilities. Supports strategic planning, gap analysis, transformation roadmaps. [EN]

**G9. Living Documentation**: Self-updating documentation via automation. Facilitates knowledge sharing and architectural understanding. [EN]

**G10. Wardley Mapping**: Strategic planning via component visualization by visibility and evolution. Supports strategic decisions and change anticipation. [EN]

**G11. Customer Segment**: Distinct enterprise target groups. Maps to system design (interfaces, workflows, data models). [EN]

**G12. Revenue Stream**: Income generation methods (subscription, usage-based, freemium). Impacts metering, billing, multi-tenancy. [EN]

**G13. Value Stream Mapping**: Lean technique visualizing value delivery steps, identifying waste and bottlenecks. Optimizes processes and reduces lead time. [EN]

**G14. System Boundaries**: Explicit scope definition (inside vs. outside). Determines interfaces and integration points for context diagrams. [EN]

**G15. Process Mapping**: Visual workflow documentation (activities, decision points, information flows). Supports optimization and automation. [EN]

### Business & Architecture Tools

**T1. Miro**: Visual collaboration for Business Model Canvas and architecture diagrams. Freemium–Enterprise. 80M+ users. https://miro.com [EN]

**T2. ArchiMate**: Enterprise architecture modeling (business, application, technology layers). ISO/IEC/IEEE 42010 compliant. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model**: Hierarchical architecture diagrams (Context, Container, Component, Code). Free, tool-agnostic. https://c4model.com [EN]

**T4. Confluence**: Documentation platform for ADRs and living documentation. Free–Enterprise. 75K+ companies. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart**: Cloud diagramming for process maps and architecture. Individual–Enterprise. 60M+ users. https://www.lucidchart.com [EN]

### Authoritative Literature & Case Studies

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** BMC framework; business–technical alignment.

**L2. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** DDD patterns; domain modeling.

**L3. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical DDD; context mapping.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28–31.** Conway's Law; organizational impact.

**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.** Team organization patterns.

**L6. Richardson, C. (2018). *Microservices Patterns*. Manning.** Microservices decomposition and patterns.

### APA Style Source Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]**

**A2. Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley Professional. [EN]**

**A3. 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]**

**A4. Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley Professional. [EN]**

**A5. Conway, M. E. (1968). How do committees invent? *Datamation*, 14(4), 28–31. [EN]**

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