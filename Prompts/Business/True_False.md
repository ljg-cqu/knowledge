# True/False Statements - Business Understanding for Software Architecture

Generate high-quality true/false assessments testing business-architecture relationships for senior technical leaders.

---

# Part I: Specifications

## Specifications

### Context & Objectives

- **Purpose**: Evaluate how well senior technical leaders connect business strategy decisions to architectural responses.
- **Primary audience**: Architects, staff-plus engineers, and product-aligned technology leaders operating in enterprise or scale-up settings.
- **Assumptions & constraints**: Participants understand core business strategy frameworks and modern architecture practices; statements must remain actionable for multi-team programs with regulated and cloud-first considerations.
- **High-level success indicator**: A balanced statement set that is precise, machine-gradable, and defends answers with evidence-based rationales.

### Statement Scope & Structure

| Element | Requirement | Notes |
|---|---|---|
| Scope | 18–32 statements covering the end-to-end business-to-architecture lifecycle | Clusters must remain mutually exclusive and collectively exhaustive (MECE). |
| Format | Declarative sentences ≤2 lines; avoid double negatives and ambiguous qualifiers | Each prompt focuses on one claim. |
| Difficulty mix | 20% foundational, 40% intermediate, 40% advanced | Round to nearest whole statement while maintaining coverage across clusters. |
| Rationale | 1–2 sentences anchored by citations; explicitly explain the business → architecture linkage | Highlight assumptions when the truth value depends on context. |
| Optional justification | 2–3 sentences (≈70% answer clarity, ≈30% situational nuance) | Use when extra guidance increases fairness or reduces misinterpretation risk. |
| Grading | Binary True/False answers with unambiguous rationales | Ensure machine gradability by avoiding context-free contradictions. |

### Difficulty & Coverage Targets

- Allocate statements across 4–6 thematic clusters (e.g., Strategic Modeling, Value & Risk, Organizational Dynamics, Architectural Translation, Evolution & Adaptation, Governance & Compliance).
- Within each cluster, maintain the global 20/40/40 difficulty distribution to ensure breadth and depth.
- At least 70% of statements must evaluate direct business-architecture relationships; use the remainder to cover enabling considerations (risk, compliance, organizational readiness).

### Evidence, Citations & Language Mix

- Cite authoritative sources using APA 7th edition and language tags (e.g., **[EN]**, **[ZH]**, **[ES]**); include inline references as `[Ref: ID]` mapping to G#/T#/L#/A#.
- Maintain language distribution: 60% English, 30% Chinese, 10% other languages (±5%). Provide translations or summaries where clarity may suffer.
- Use a minimum of three source types: business frameworks/methodologies, architecture practices/patterns, case studies/reports, tools/platform documentation. No single type may exceed 25% of total citations.
- Ensure ≥50% of citations are ≤3 years old (≥70% for cloud or digital-transformation topics) and flag uncertainties or context-limited claims.

### Quality Criteria Aligned with LLM-Friendly Guidelines

1. **Clarity**: Define terms, avoid jargon without explanation, and restate complex assumptions plainly.
2. **Precision**: Use specific business scenarios, metrics, or architectural patterns instead of generic language.
3. **MECE coverage**: Clusters must cover the topic space without overlap; map each statement to exactly one cluster.
4. **Depth & breadth**: Balance strategic, organizational, technical, and operational perspectives, highlighting both benefits and risks.
5. **Significance & relevance**: Prioritize statements that test high-impact decisions; exclude trivial operational trivia.
6. **Fairness & balance**: Acknowledge assumptions, limitations, counterexamples, and trade-offs in rationales.
7. **Risk/value articulation**: Call out risks, mitigations, and value drivers when truth values depend on them.
8. **Validation readiness**: Structure answers so automated or manual reviews can quickly confirm evidence, citations, and logic.

### Reference Minimum Requirements

| Reference Section | Minimum | Purpose |
|---|---|---|
| Glossary & Acronyms | ≥10 | Anchor terminology and reduce ambiguity for multilingual audiences. |
| Tools & Platforms | ≥5 | Provide actionable resources for modeling, visualization, and governance. |
| Literature & Reports | ≥6 | Supply authoritative depth across business, architecture, and organizational design domains. |
| APA Citations | ≥12 | Guarantee sufficient evidence; enforce language and source-type diversity. |

### Success Criteria

- Statement bank passes automated count, coverage, and difficulty checks on the first review cycle.
- ≥70% of statements include ≥1 citation; ≥30% include ≥2 citations spanning different source types.
- Rationales explicitly connect business moves to architectural consequences and mention risk/value implications when applicable.
- All cross-references resolve correctly, and URLs are live or archived.

### Validation Checklist

1. **Coverage audit**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Statements 18–32 with 20/40/40 difficulty.
2. **Cluster balance**: Each thematic cluster has 3–6 statements and unique focus areas.
3. **Citation coverage**: ≥70% statements include ≥1 citation; ≥30% include ≥2 from distinct source types.
4. **Language distribution**: EN 50–70%, ZH 20–40%, Other 5–15%; translations provided when needed.
5. **Recency check**: ≥50% citations within 3 years; ≥70% for digital/cloud topics.
6. **Source diversity**: ≥3 source types represented; none exceed 25% of total citations.
7. **Evidence integrity**: Every `[Ref: ID]` maps to G#/T#/L#/A# entries; URLs are accessible.
8. **Logic & fairness**: Answers are unambiguous, rationales explain assumptions, and counterpoints are acknowledged.
9. **Risk/value articulation**: Statements discussing trade-offs explicitly mention risk mitigation or value realization.
10. **Final self-review**: Run spelling/grammar checks, confirm formatting (headings, tables, code blocks), and document validation results.

---

# Part II: Instructions

### Step 1: Define Clusters & Objectives
1. Select 4–6 thematic clusters that collectively cover strategic intent, value & risk management, organizational dynamics, architectural translation, evolution, and governance. Document rationale for cluster selection.
2. Map success criteria to each cluster (e.g., "Strategic Modeling" stresses market shifts → capability changes). Confirm clusters are MECE and align with stakeholder needs.
3. Draft a coverage plan showing statement counts per cluster and difficulty levels to hit the 20/40/40 target.

### Step 2: Curate Evidence Base
1. Build a reference matrix tracking glossary, tools, literature, and APA citations with language tags, publication year, and source type.
2. Prioritize recent (≤3 years) and authoritative sources; note any gaps requiring targeted research.
3. Collect contextual data (metrics, case studies, regulatory constraints) that will ground statements in actionable reality.

### Step 3: Craft Statements & Rationales
1. For each cluster, draft declarative statements linking a business trigger to an architectural consequence. Avoid definitions or trivia.
2. Assign difficulty levels, verify wording clarity, and ensure statements remain single-claim and machine-gradable.
3. Write rationales highlighting assumptions, risk/value implications, and at least one `[Ref: ID]`. Use optional justifications when nuance improves fairness.
4. Every five statements, perform a micro-audit: confirm difficulty mix, citation presence, MECE alignment, and language distribution progress.

### Step 4: Assemble Reference Sections
1. Populate glossary, tools, literature, and APA sections; ensure entries are concise, distinct, and mapped to statement references.
2. Validate language mix, source diversity, and recency requirements. Add archival links if primary sources are unstable.
3. Cross-check that every `[Ref: ID]` resolves to an entry and that no citation exceeds the source-type cap.

### Step 5: Run Validation & Self-Review
1. Execute the full validation checklist from Part I; document pass/fail status and remediation actions.
2. Perform a final edit for clarity, tone, and formatting (headings, tables, code blocks, Mermaid diagrams when included).
3. Summarize validation results in a short bullet list to accompany delivery, noting any residual risks or reviewer notes.

---

# Part III: Output Format

Structure the final deliverable so reviewers can navigate quickly and verify compliance with the specifications.

- Begin with a contents section (`## Contents`) linking to all top-level headings and relevant subsections.
- Use semantic Markdown (H1–H4), bullet/numbered lists, tables, Mermaid diagrams, and language-tagged code blocks to present information cleanly.
- Include a short "Validation Summary" section near the end noting checklist results and any flagged risks.

```markdown
## Contents

- [Statement Bank](#statement-bank-statements-1-n)
  - [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)
- [Validation Summary](#validation-summary)

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

---

## Validation Summary

- **Checklist status**: 10/10 checks passed (see Part I for criteria).
- **Language mix**: EN 60%, ZH 30%, Other 10%.
- **Recent citations**: 65% ≤3 years old; cloud/digital topics 80%.
```
