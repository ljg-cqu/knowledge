# Case Study / Scenario - Business Understanding for Software Architecture

Framework for generating high-quality case study/scenario assessments focused on comprehensive business understanding that benefits software architecture decisions.

---

# Part I: Specifications

Define quality requirements, standards, and constraints.

## Specifications

### Scope and Structure

- **Scope**: 16–22 scenarios for senior/architect/expert level technical leaders
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Context**: 200–400 words with business constraints, stakeholders, market dynamics, organizational factors
- **Tasks**: 3–4 MECE tasks per scenario covering business-to-architecture transition
- **Deliverables**: Business model analyses, value mapping matrices, risk assessments, architecture decision memos (≤300 words), stakeholder communications
- **Trade-offs**: Business value vs technical debt, short-term revenue vs long-term architecture, organizational alignment vs optimal design, market speed vs quality
- **Grading**: Partial-credit checklists; document business-technical mapping, value alignment, risk mitigation
- **Conflict Handling**: Solutions acknowledge competing business frameworks (BMC vs Lean Canvas); clarify where practitioners agree vs disagree on approach

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Business frameworks & methodologies; (2) Architecture patterns & practices; (3) Case studies & industry reports; (4) Tools & platforms
- **Format**: APA 7th with language tags
- **Distribution**: Business/Architecture tools; Literature/Reports
- **Inline Citation**: Use [Ref: ID] in context descriptions when referencing business models, frameworks, architectural patterns, trade-offs, and organizational dynamics

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Business Model Canvas, Value Proposition, DDD, Conway's Law, Technical Debt, etc. |
| Business & Architecture Tools | ≥5 entries | Business modeling, architecture visualization, documentation platforms |
| Authoritative Literature & Reports | ≥6 entries | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Quality Gates

- Recency: ≥50% of citations from the last 3 years; for digital transformation/cloud-native domains, target ≥70% from the last 2 years
- Source diversity: Include at least 3 source types; no single source >25% of total citations
- Evidence coverage: ≥70% of scenarios include ≥1 inline citation in context; ≥30% include ≥2 citations tied to distinct claims
- Tool maturity: Each tool entry includes pricing, adoption metrics, last update ≤18 months, key integrations
- Deduplication: Canonicalize and avoid duplicate entries; prefer persistent links (DOIs, archived URLs)
- Link validity: Validate that links resolve (or provide archived link) at time of delivery
- Cross-reference binding: Use reference IDs and link scenarios to specific items in the Reference Sections
- Business-Technical Mapping: ≥80% of scenarios explicitly trace business drivers to architectural decisions

> Scaling guidance: For sets >25 scenarios, increase floor counts by ~1.5× (round up). Prioritize meeting the Quality Gates first.

### Pre-Submission Validation

Execute ALL steps below. Present results in a validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Count Audit**
- Count: Glossary entries, Tool entries, Literature entries, APA citations, Scenarios (total + by difficulty level)
- Report: `Glossary: X (target ≥10) | Tools: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Scenarios: N total (F foundational, I intermediate, A advanced)`
- Pass if: All counts meet minimums AND difficulty ratio ≈20/40/40

**Step 2 – Citation Coverage Scan**
- For EACH scenario context: Count inline `[Ref: ...]` occurrences
- Report: `X of Y scenarios have ≥1 citation (Z%); W of Y have ≥2 citations (V%)`
- Pass if: ≥70% have ≥1 citation AND ≥30% have ≥2 citations

**Step 3 – Language Distribution Check**
- Count citations with `[EN]`, `[ZH]`, and other language tags
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass if: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%

**Step 4 – Recency Verification**
- Extract publication year from EACH citation
- Report: `X of Y citations (Z%) from 2022-2025 (last 3 years)`
- Pass if: ≥50% from last 3 years (≥70% for digital transformation/cloud-native)

**Step 5 – Source Type Diversity**
- Classify EACH citation: (1) Business frameworks, (2) Architecture patterns, (3) Case studies/reports, (4) Tools
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Types present: N | Max single source: M citations (P%)`
- Pass if: ≥3 types present AND no single source >25%

**Step 6 – Link Validation**
- Test EACH URL or verify archived link exists
- Report: `Tested X links: Y accessible, Z broken` (list broken URLs)
- Pass if: All links accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- For EACH `[Ref: ID]` in scenarios: Verify ID exists in Reference Sections (G#→Glossary, T#→Tools, L#→Literature, A#→APA)
- Report: `Found X inline refs; Y resolve correctly, Z broken` (list broken refs)
- Pass if: All refs resolve (Z=0)

**Step 8 – Context Length Compliance**
- Select 5 random scenario contexts; count words
- Report: `S#: X words | S#: Y words | ...` (flag if <200 or >400)
- Pass if: All sampled contexts in 200–400 range

**Step 9 – Task MECE Verification**
- Review EACH scenario's tasks for mutual exclusivity and collective exhaustiveness
- Report: `X of Y scenarios have MECE tasks; Z have overlaps/gaps` (list issues)
- Pass if: All scenarios have MECE tasks (Z=0)

**Step 10 – Grading Rubric Completeness**
- For EACH scenario: Verify all tasks have rubrics with point allocations
- Report: `X of Y scenarios have complete rubrics; Z missing/incomplete` (list issues)
- Pass if: All scenarios have complete rubrics (Z=0)

**Step 11 – Business-Technical Mapping**
- For EACH scenario: Verify explicit connection from business drivers to architectural decisions
- Report: `X of Y scenarios have explicit mapping (Z%)`
- Pass if: ≥80% have explicit business-to-architecture mapping

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Context lengths | 5/5 compliant | PASS/FAIL |
| MECE tasks | Y/X verified | PASS/FAIL |
| Grading rubrics | Y/X complete | PASS/FAIL |
| Biz-Tech mapping | X% explicit | PASS/FAIL |
```

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate affected sections, and re-run full validation. Only proceed to submission when ALL checks show PASS.

### Submission Checklist

- [ ] Floors met (Glossary ≥10, Tools ≥5, Literature ≥6, APA citations ≥12)
- [ ] Difficulty distribution verified (20/40/40: Foundational/Intermediate/Advanced)
- [ ] Language distribution verified (~60% EN, ~30% ZH, ~10% other)
- [ ] Recency: ≥50% citations last 3 years (≥70% for digital transformation)
- [ ] Diversity: ≥3 source types, no single source >25%
- [ ] Evidence coverage: ≥70% scenarios with ≥1 citation; ≥30% with ≥2 distinct citations
- [ ] Scenario quality: Each context 200–400 words, includes relevant citations
- [ ] Tool maturity noted (pricing, adoption, last update ≤18 months, integrations)
- [ ] Links resolve or archived URLs provided
- [ ] Cross-references present (IDs used in scenarios and in Reference Sections)
- [ ] MECE tasks verified for all scenarios
- [ ] Grading rubrics complete with point allocations
- [ ] Business-technical mapping: ≥80% scenarios explicitly trace business to architecture
- [ ] Pre-submission validation completed with passing results

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 3-5 domain clusters aligned with framework: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation
2. Allocate 3-5 scenarios per cluster (total 16-22)
3. Assign difficulty levels to ensure 20/40/40 balance
4. **Inline Check**: Verify total scenarios = 16-22 AND difficulty ratio ≈20/40/40 before proceeding

### Step 2: Reference Collection
1. Gather ≥10 glossary terms (Business Model Canvas, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, etc.)
2. Gather ≥5 tools (Miro, ArchiMate/C4, Confluence, LucidChart, Wardley Maps)
3. Gather ≥6 literature sources (Osterwalder, Evans, Vernon, Conway, Hohpe, Richardson + ZH sources)
4. Gather ≥12 APA citations; tag language, year, type
5. Assign Reference IDs: G1-Gn (Glossary), T1-Tn (Tools), L1-Ln (Literature), A1-An (APA)
6. **Inline Check**: Count sources (≥10/5/6/12?), language split (≈60/30/10?), recency (≥50% last 3yr?), diversity (≥3 types?) before proceeding

### Step 3: Scenario Generation
1. For EACH scenario: Write context (200-400 words) with business constraints, stakeholders, market dynamics, organizational factors
2. In EACH context: Include ≥1 inline `[Ref: ID]` after business models, frameworks, constraints, trade-offs
3. For EACH scenario: Design 3-4 MECE tasks covering business understanding → architecture transition
4. Ensure tasks require: Business model analysis, value mapping, risk assessment, architectural decisions, stakeholder communication
5. **Inline Check**: After every 3 scenarios, verify: context lengths 200-400, ≥1 citation per scenario, MECE tasks, business-to-architecture mapping, complete rubrics

### Step 4: Grading Framework
1. For EACH task: Define expected responses showing business-to-architecture transition
2. Create grading rubrics with partial credit for: business analysis (30%), value mapping (25%), architectural decisions (30%), justification (15%)
3. Document common omissions (missing risk factors, weak value alignment, no organizational considerations)
4. **Inline Check**: All tasks have rubrics? Point allocations sum correctly? Business-technical mapping criteria present?

### Step 5: Reference Section Compilation
1. Populate Glossary, Tools, Literature, APA sections with collected sources
2. Include all required information per format
3. Ensure Reference IDs match inline citations
4. **Inline Check**: Every [Ref: ID] in scenarios resolves to an entry? All sources have required fields?

### Step 6: Pre-Submission Validation
Execute all 11 validation steps (see Part I > Pre-Submission Validation). Present validation report table. Fix any FAIL results and re-validate.

### Step 7: Final Review
Check Submission Checklist (see Part I). Submit only when all checks pass.

---

# Part III: Output Format

Template structure for generated scenario banks.

## Output Format

Use this structure when generating scenario banks:

```markdown
## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-n)
- [Scenario 1: [Title]](#scenario-1-title)
- [Scenario 2: [Title]](#scenario-2-title)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategic Modeling/Value & Risk Analysis/Organizational Dynamics/Architectural Translation/Evolution & Adaptation]

**Context:** (200–400 words with business constraints, stakeholders, market dynamics, organizational factors; include [Ref: ID] citations)

[Describe business situation, value propositions, customer segments, revenue model changes, organizational structure, market pressures, regulatory requirements, competitive dynamics]

**Task 1: Business Model Analysis (8 pts)**
Analyze the business model changes using Business Model Canvas [Ref: G1]. Identify which building blocks are affected and how they impact technical requirements.

**Expected Response:**
- Identification of affected BMC blocks (Revenue Streams, Customer Relationships, Key Activities, etc.)
- Mapping of business changes to value propositions
- Recognition of customer segment implications

**Grading:**
- Complete BMC analysis (4 pts)
- Correct identification of impacted blocks (2 pts)
- Business-to-technical mapping (2 pts)

**Task 2: Value & Risk Assessment (10 pts)**
Create a value mapping matrix and risk assessment showing how business drivers translate to architectural requirements.

**Expected Response:**
- Value Model: value propositions → technical features
- Risk Model: business risks, operational constraints, regulatory requirements
- Prioritization based on business impact

**Grading:**
- Value mapping completeness (4 pts)
- Risk identification and classification (3 pts)
- Prioritization rationale (3 pts)

**Task 3: Architectural Decision Memo (6 pts)**
Write a memo (≤300 words) recommending architectural decisions based on business analysis, addressing stakeholders' concerns.

**Expected Response:**
- Clear architectural recommendations
- Business justification for each decision
- Trade-off analysis
- Stakeholder alignment considerations

**Grading:**
- Architectural decisions clarity (2 pts)
- Business justification (2 pts)
- Trade-off analysis (1 pt)
- Stakeholder considerations (1 pt)

**Common Omissions:**
- Missing organizational impact (Conway's Law)
- No evolution/migration strategy
- Weak value-to-architecture tracing
- Ignoring technical debt implications

**Edge Cases for Bonus (2 pts):**
- Consideration of living documentation and ADR practices
- Explicit evolution strategy with phases
- Organizational restructuring recommendations

---

## Reference Sections

Assign Reference IDs and reuse them inline in scenario contexts: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G1, T2, A5].

### Glossary, Terminology & Acronyms

**G1. Business Model Canvas (BMC)**  
Strategic management template with 9 building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. Used for business model design, validation, innovation. Related: Lean Canvas, Value Proposition Canvas [EN]

**G2. Value Proposition**  
The bundle of products/services creating value for a specific customer segment. Maps to technical features and quality attributes. Used for product-market fit, differentiation, architecture prioritization. Related: Jobs-to-be-Done, Quality Attributes [EN]

**G3. Domain-Driven Design (DDD)**  
Software development approach focusing on complex domain modeling through collaboration between technical and domain experts. Used for complex business logic, microservices boundaries, team organization. Related: Event Storming, Context Mapping [EN]

**G4. Conway's Law**  
"Organizations design systems that mirror their communication structure." Used for team topology design, architecture alignment, organizational change planning. Related: Inverse Conway Maneuver, Team Topologies [EN]

**G5. Technical Debt**  
Implied cost of additional rework caused by choosing quick solutions now instead of better approaches. Used for refactoring prioritization, risk assessment, investment planning. Related: Architectural Erosion [EN]

**G6. Architecture Decision Records (ADR)**  
Lightweight documentation capturing architectural decisions, context, consequences, and trade-offs. Used for decision transparency, knowledge preservation. Related: Decision Log, Design Rationale [EN]

**G7. Bounded Context**  
DDD pattern defining explicit boundaries within which a domain model is valid. Used for microservices decomposition, team autonomy, integration design. Related: Context Map, Anti-Corruption Layer [EN]

**G8. Capability Mapping**  
Technique identifying and organizing business capabilities independent of implementation. Used for strategic planning, gap analysis, transformation roadmaps. Related: Business Capability Model, Value Stream Mapping [EN]

**G9. Living Documentation**  
Documentation that evolves with the system through automation and continuous updates. Used for knowledge sharing, onboarding, architectural understanding. Related: Documentation as Code, ADR [EN]

**G10. Wardley Mapping**  
Strategic planning technique visualizing components by visibility and evolution. Used for strategic decision-making, identifying opportunities, anticipating change. Related: Value Chain Analysis [EN]

**G11. Customer Segment**  
Distinct groups of people/organizations an enterprise aims to reach and serve. Maps to system design decisions (interfaces, workflows, data models). Used for market targeting, personalization, resource allocation. Related: Persona, Market Segmentation, ICP [EN]

**G12. Revenue Stream**  
Ways an organization generates income from customer segments (e.g., one-time sale, subscription, usage-based, freemium, licensing). Directly impacts architectural requirements (metering, billing, multi-tenancy). Used for business model design, pricing strategy, technical planning. Related: Monetization Model, Pricing Strategy [EN]

**G13. Value Stream Mapping**  
Lean technique visualizing steps in delivering value to customers, identifying waste, bottlenecks, and improvement opportunities. Used for process optimization, lead time reduction, efficiency analysis. Related: Process Mapping, Flow Analysis [EN]

**G14. System Boundaries**  
Explicit definition of what is inside vs outside the system scope; determines interfaces, integration points, and responsibilities. Used for context diagrams, scope management, interface design. Related: Context Diagram, Bounded Context, Integration Points [EN]

**G15. Process Mapping**  
Visual documentation of workflows, activities, decision points, and information flows; used for optimization, automation, understanding current state. Related: Value Stream Mapping, BPMN, Swimlane Diagrams [EN]

### Business & Architecture Tools

**T1. Miro** (Visual Collaboration & Business Modeling)  
Infinite canvas for Business Model Canvas, journey mapping, architecture diagrams. Freemium to Enterprise. 80M+ users. Updated Q4 2024. Integrates: Jira, Slack, Confluence. Use cases: Business model workshops, architecture design. https://miro.com [EN]

**T2. ArchiMate** (Enterprise Architecture Modeling)  
Open standard for enterprise architecture modeling covering business, application, technology layers. ISO/IEC/IEEE 42010 compliant. Use cases: Business-IT alignment, impact analysis. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model** (Software Architecture Diagramming)  
Hierarchical diagrams (Context, Container, Component, Code) for architecture visualization. Free, tool-agnostic. Use cases: Architecture documentation, stakeholder communication. https://c4model.com [EN]

**T4. Confluence** (Documentation & Knowledge Management)  
Team workspace for documentation, decision records, architecture diagrams. Free to Enterprise. 75K+ companies. Updated Q3 2024. Use cases: ADRs, living documentation. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart** (Diagramming & Visual Communication)  
Cloud-based diagramming for process maps, architecture diagrams. Individual to Enterprise. 60M+ users. Updated Q4 2024. Use cases: Process mapping, architecture visualization. https://www.lucidchart.com [EN]

### Authoritative Literature & Case Studies

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.**  
Business Model Canvas framework; 9 building blocks for business model design. Foundational for business-technical alignment.

**L2. Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley.**  
DDD patterns and practices; ubiquitous language, bounded contexts, strategic design. Core reference for domain modeling.

**L3. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.**  
Practical DDD implementation; context mapping, aggregates, event sourcing. Tactical patterns for complex domains.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28-31.**  
Original Conway's Law paper; organizational structure impacts system design. Foundational for team topology.

**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.**  
Team organization patterns for fast flow. Organizational design for modern software delivery.

**L6. Richardson, C. (2018). *Microservices Patterns*. Manning.**  
Microservices decomposition, data management, communication patterns. Practical architecture patterns.

### APA Style Source Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]**

**A2. Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley Professional. [EN]**

**A3. 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]**
(Zhou, A. (2021). *The essence of architecture*. Publishing House of Electronics Industry.)

**A4. Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley Professional. [EN]**

**A5. Conway, M. E. (1968). How do committees invent? *Datamation*, 14(4), 28-31. [EN]**

**A6. Skelton, M., & Pais, M. (2019). *Team topologies: Organizing business and technology teams for fast flow*. IT Revolution Press. [EN]**

**A7. Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning Publications. [EN]**

**A8. Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns: Designing, building, and deploying messaging solutions*. Addison-Wesley Professional. [EN]**

**A9. 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]**
(Zhang, Y. (2019). *Domain-driven design in practice*. Publishing House of Electronics Industry.)

**A10. Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley Professional. [EN]**

**A11. Newman, S. (2021). *Building microservices: Designing fine-grained systems* (2nd ed.). O'Reilly Media. [EN]**

**A12. 肖然. (2020). *企业级业务架构设计*. 机械工业出版社. [ZH]**
(Xiao, R. (2020). *Enterprise business architecture design*. China Machine Press.)

**A13. Brown, S. (2018). *Software architecture for developers* (Vol. 2). Leanpub. [EN]**

**A14. Humble, J., & Farley, D. (2010). *Continuous delivery: Reliable software releases through build, test, and deployment automation*. Addison-Wesley Professional. [EN]**

**A15. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). *The DevOps handbook*. IT Revolution Press. [EN]**

**A16. Wardley, S. (2018). *Wardley maps: Topographical intelligence in business*. Medium. https://medium.com/wardleymaps [EN]**
```
