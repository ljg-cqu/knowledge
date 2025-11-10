# Short Answer / Calculation - Business Understanding for Software Architecture

Prompt template for producing self-contained, business-to-architecture short answer assessments that senior technical leaders can act on immediately.

---

# Part I: Specifications

## Quick Reference

- **Audience**: Senior / architect / expert technical leaders
- **Goal**: 25–40 short answer problems translating business drivers into architecture decisions
- **Output Focus**: Clear business context, structured reasoning, worked solutions, graded rubrics

## Specifications

### Scope and Structure

- **Scope**: Generate 25–40 problems with explicit business constraints and architecture implications.
- **Structure**: Each problem is self-contained; surface all assumptions, constraints, and required artefacts.
- **Difficulty Mix**: Preserve a 20/40/40 split across Foundational / Intermediate / Advanced.
- **Problem Types**: Business model analysis (2–3 sentences), value mapping, risk assessment, architectural justification (2–4 sentences), trade-off calculation.
- **Expected Answers**: Provide structured reasoning with business-to-architecture mapping plus 2–4 step worked solutions.
- **Grading Model**: Normalize qualitative inputs; apply tolerances; weight partial credit as Business Analysis 40%, Value Mapping 30%, Architectural Decisions 30%.
- **Alternative Paths**: Document additional valid approaches and note where multiple frameworks apply.

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH], etc.)
- **Source Types**: (1) Business frameworks & methodologies; (2) Architecture patterns & practices; (3) Case studies & industry reports; (4) Tools & platforms
- **Format**: APA 7th with language tags
- **Inline Citation**: Use [Ref: ID] in worked solutions when referencing frameworks, patterns, trade-off analyses

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Business Model Canvas, Value Proposition, DDD, Conway's Law, Technical Debt, etc. |
| Business & Architecture Tools | ≥5 entries | Miro, ArchiMate/C4, Confluence, LucidChart, Wardley Maps |
| Authoritative Literature & Reports | ≥6 entries | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

### Quality Gates

- Recency: ≥50% citations from last 3 years (≥70% for digital transformation/cloud-native).
- Source diversity: ≥3 source types; no single source >25%.
- Evidence coverage: ≥70% problems with ≥1 citation; ≥30% with ≥2 citations.
- Business-Technical Mapping: ≥80% problems require explicit business-to-architecture translation.

### Success Criteria

| Dimension | Target |
| --- | --- |
| Coverage | 25–40 problems, 20/40/40 difficulty ratio |
| Context Clarity | Every problem states business scenario, constraints, and stakeholder impact |
| Reasoning Quality | Worked solutions show MECE steps, cite sources, and request self-review |
| Validation | All ten validation checks executed and reported as PASS |

### Pre-Submission Validation

**Step 1 – Count Audit**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Problems 25-40 (20/40/40)
**Step 2 – Citation Coverage**: ≥70% have ≥1; ≥30% have ≥2
**Step 3 – Language**: EN 50-70%, ZH 20-40%, Other 5-15%
**Step 4 – Recency**: ≥50% last 3yr (≥70% for digital transformation)
**Step 5 – Source Diversity**: ≥3 types; no single >25%
**Step 6 – Links**: All accessible or archived
**Step 7 – Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
**Step 8 – Answer Completeness**: All problems have worked solutions
**Step 9 – Solution Clarity**: All solutions show business-to-architecture steps
**Step 10 – Business-Technical Mapping**: ≥80% require explicit translation

---

# Part II: Instructions

### Step 1: Topic Identification & Planning

1. Identify 4–6 clusters (e.g., Strategic Modeling, Value & Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution & Adaptation).
2. Allocate 4–8 problems per cluster; confirm the 20/40/40 difficulty mix.
3. **Check**: Total problems ∈ [25, 40]; difficulty ratio preserved; clusters cover distinct business perspectives (MECE).

### Step 2: Reference Collection
Gather ≥10 glossary, ≥5 tools, ≥6 literature, ≥12 APA citations; tag language, year, and source type.

### Step 3: Problem Generation

1. Draft problems that force business model analysis, value mapping, risk assessment, and architectural justification.
2. Build 2–4 step worked solutions applying MECE reasoning, explicit business-to-architecture translation, and cited evidence.
3. Require self-review prompts (reasoning check, validation checklist) within each solution when relevant.
4. Include ≥1 [Ref: ID] per solution and highlight where multiple citations are required.
5. **Check**: After every 5 problems confirm solution completeness, explicit mapping, and citation coverage.

### Step 4: Reference Compilation
Populate Glossary/Tools/Literature/APA; ensure all [Ref: ID] resolve and links are accessible or archived.

### Step 5: Validation

Execute all 10 validation steps, record pass/fail, remediate gaps, and re-run until all PASS.

---

# Part III: Output Format

## Contents

- [Problem Bank](#problem-bank-problems-1-n)
  - [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Problem Bank (Problems 1–N)

### Topic 1: Strategic Modeling

#### Problem 1: A SaaS company shifts from monthly to annual billing. Analyze the Business Model Canvas impact and identify 3 architectural requirements this change introduces.

**Difficulty:** Intermediate

**Expected Answer:**
1. **BMC Analysis**: Revenue Streams change (monthly → annual), Customer Relationships shift (transactional → commitment-based), Key Activities add retention focus
2. **Architectural Requirements**:
   - Subscription management system for annual cycles
   - Prorated refund calculation engine
   - Long-term usage analytics for retention insights

**Worked Solution:**

**Step 1 - Business Model Analysis** [Ref: G1]:
- Revenue Streams: Annual prepayment changes cash flow, requires different revenue recognition
- Customer Relationships: Annual commitment increases switching cost, demands higher retention focus
- Key Activities: Must add customer success, usage monitoring, renewal management

**Step 2 - Value Mapping** [Ref: G2]:
- Value Proposition: Predictable annual pricing → requires transparent usage tracking
- Customer Segment: Enterprise buyers prefer annual → need enterprise features (SSO, audit logs)

**Step 3 - Architectural Translation** [Ref: A7]:
1. Subscription management: Handle annual cycles, upgrades, downgrades, prorated refunds
2. Usage analytics: Track consumption patterns for renewal predictions
3. Customer success integration: Health scoring, usage alerts, engagement metrics

**Grading:**
- BMC analysis (4 pts): Correct identification of affected blocks
- Value mapping (3 pts): Link to technical features
- Architectural requirements (3 pts): Specific, justified requirements

**Self-Review Prompt:** Confirm the solution ties each business driver to a distinct architectural requirement and validates citation coverage (≥1 [Ref: ID]).

**Validation Check:** Count audit, citation coverage, and business-to-architecture mapping marked PASS for this problem.

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
