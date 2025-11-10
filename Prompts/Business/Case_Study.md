# Case Study: Business Understanding for Software Architecture

Framework for generating case study assessments linking business understanding to software architecture decisions.

---

# Part I: Specifications

## Specifications

### Scope and Structure

- **Scope**: 16–22 scenarios for senior/architect/expert technical leaders
- **Difficulty**: 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Context**: 200–400 words covering business constraints, stakeholders, market dynamics, organizational factors
- **Tasks**: 3–4 MECE tasks per scenario
- **Deliverables**: Business model analyses, value mapping matrices, risk assessments, architecture decision memos (≤300 words)
- **Trade-offs**: Value vs debt, revenue vs architecture, alignment vs design, speed vs quality
- **Grading**: Partial credit; assess business-technical mapping, value alignment, risk mitigation
- **Conflict Handling**: Acknowledge competing frameworks (BMC vs Lean Canvas); clarify practitioner disagreements

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag: [EN], [ZH])
- **Source Types**: (1) Business frameworks; (2) Architecture patterns; (3) Case studies/reports; (4) Tools
- **Format**: APA 7th with language tags
- **Inline Citation**: Use [Ref: ID] for business models, frameworks, patterns, trade-offs, organizational dynamics

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
|-------------------|-------------|-------|
| Glossary, Terminology & Acronyms | ≥10 | BMC, Value Proposition, DDD, Conway's Law, Technical Debt |
| Business & Architecture Tools | ≥5 | Modeling, visualization, documentation platforms |
| Authoritative Literature & Reports | ≥6 | Business strategy, architecture patterns, organizational design |
| APA Style Source Citations | ≥12 | ~60% EN / ~30% ZH / ~10% other |

> **Exception**: If floor count not met, state shortfall, rationale, and sourcing plan.

### Quality Gates

- **Recency**: ≥50% citations from last 3 years (≥70% for digital transformation/cloud-native)
- **Source diversity**: ≥3 source types; no single source >25%
- **Evidence coverage**: ≥70% scenarios with ≥1 citation; ≥30% with ≥2 distinct citations
- **Tool maturity**: Include pricing, adoption metrics, last update ≤18 months, integrations
- **Deduplication**: Canonicalize entries; prefer persistent links (DOIs, archived URLs)
- **Link validity**: Validate links resolve or provide archived alternatives
- **Cross-reference binding**: Link scenarios to Reference Section items via IDs
- **Business-Technical Mapping**: ≥80% scenarios explicitly trace business drivers to architecture

> **Scaling**: For >25 scenarios, increase floors by 1.5× (round up). Prioritize Quality Gates.

### Pre-Submission Validation

Execute all steps. Present results in validation report. Fix failures and re-validate until all pass.

**Step 1 – Count Audit**
- Count: Glossary, Tools, Literature, APA citations, Scenarios (by difficulty)
- Report: `Glossary: X (≥10) | Tools: Y (≥5) | Literature: Z (≥6) | APA: W (≥12) | Scenarios: N (F/I/A)`
- Pass: All counts ≥ minimums AND difficulty ≈20/40/40

**Step 2 – Citation Coverage Scan**
- Count inline `[Ref: ...]` per scenario
- Report: `X/Y scenarios ≥1 citation (Z%); W/Y ≥2 citations (V%)`
- Pass: ≥70% with ≥1 AND ≥30% with ≥2

**Step 3 – Language Distribution Check**
- Count citations by language tag
- Report: `EN: X (Y%) | ZH: A (B%) | Other: C (D%)`
- Pass: EN ≈50-70%, ZH ≈20-40%, Other ≈5-15%

**Step 4 – Recency Verification**
- Extract publication year per citation
- Report: `X/Y citations (Z%) from 2022-2025`
- Pass: ≥50% from last 3 years (≥70% for digital transformation/cloud-native)

**Step 5 – Source Type Diversity**
- Classify citations: (1) Business frameworks, (2) Architecture patterns, (3) Case studies/reports, (4) Tools
- Report: `Type 1: X | Type 2: Y | Type 3: Z | Type 4: W | Types: N | Max source: M (P%)`
- Pass: ≥3 types AND no source >25%

**Step 6 – Link Validation**
- Test URLs or verify archived links
- Report: `Tested X: Y accessible, Z broken` (list broken)
- Pass: All accessible OR archived alternatives provided

**Step 7 – Cross-Reference Integrity**
- Verify each `[Ref: ID]` exists in Reference Sections (G#→Glossary, T#→Tools, L#→Literature, A#→APA)
- Report: `X inline refs: Y resolved, Z broken` (list broken)
- Pass: All resolved (Z=0)

**Step 8 – Context Length Compliance**
- Sample 5 random scenario contexts; count words
- Report: `S#: X words | S#: Y words | ...` (flag <200 or >400)
- Pass: All in 200–400 range

**Step 9 – Task MECE Verification**
- Review scenarios for mutually exclusive, collectively exhaustive tasks
- Report: `X/Y scenarios MECE; Z with overlaps/gaps` (list issues)
- Pass: All MECE (Z=0)

**Step 10 – Grading Rubric Completeness**
- Verify all tasks have rubrics with point allocations
- Report: `X/Y scenarios complete; Z missing/incomplete` (list issues)
- Pass: All complete (Z=0)

**Step 11 – Business-Technical Mapping**
- Verify explicit business-to-architecture connections
- Report: `X/Y scenarios explicit mapping (Z%)`
- Pass: ≥80% explicit mapping

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

> **MANDATORY**: If ANY check fails, fix issues and re-validate. Proceed only when ALL pass.

### Submission Checklist

- [ ] Floors: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12
- [ ] Difficulty: 20/40/40 (Foundational/Intermediate/Advanced)
- [ ] Languages: ~60% EN, ~30% ZH, ~10% other
- [ ] Recency: ≥50% last 3 years (≥70% digital transformation)
- [ ] Diversity: ≥3 source types, no source >25%
- [ ] Citations: ≥70% scenarios ≥1; ≥30% scenarios ≥2
- [ ] Context: 200–400 words with citations
- [ ] Tools: Include pricing, adoption, last update ≤18 months, integrations
- [ ] Links: Resolve or archived
- [ ] Cross-references: IDs in scenarios and Reference Sections
- [ ] Tasks: MECE verified
- [ ] Rubrics: Complete with point allocations
- [ ] Mapping: ≥80% explicit business-to-architecture
- [ ] Validation: All checks passed

---

# Part II: Instructions

## Instructions

Execute steps sequentially with inline quality checks.

### Step 1: Topic Identification & Planning
1. Identify 3-5 domain clusters: Strategic Modeling | Value & Risk Analysis | Organizational Dynamics | Architectural Translation | Evolution & Adaptation
2. Allocate 3-5 scenarios per cluster (16-22 total)
3. Assign difficulty: 20/40/40 balance
4. **Check**: Total 16-22 AND ratio ≈20/40/40

### Step 2: Reference Collection
1. Gather ≥10 glossary terms (BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR)
2. Gather ≥5 tools (Miro, ArchiMate/C4, Confluence, LucidChart, Wardley Maps)
3. Gather ≥6 literature (Osterwalder, Evans, Vernon, Conway, Hohpe, Richardson + ZH)
4. Gather ≥12 APA citations; tag language, year, type
5. Assign IDs: G1-Gn (Glossary), T1-Tn (Tools), L1-Ln (Literature), A1-An (APA)
6. **Check**: Counts ≥10/5/6/12, languages ≈60/30/10, recency ≥50% last 3yr, diversity ≥3 types

### Step 3: Scenario Generation
1. Write context (200-400 words): business constraints, stakeholders, market dynamics, organizational factors
2. Include ≥1 `[Ref: ID]` citation per context
3. Design 3-4 MECE tasks: business understanding → architecture transition
4. Tasks require: model analysis, value mapping, risk assessment, decisions, stakeholder communication
5. **Check** (every 3 scenarios): 200-400 words, ≥1 citation, MECE tasks, business-to-architecture mapping, complete rubrics

### Step 4: Grading Framework
1. Define expected responses: business-to-architecture transition
2. Create rubrics: business analysis (30%), value mapping (25%), decisions (30%), justification (15%)
3. Document omissions: missing risks, weak alignment, no organizational considerations
4. **Check**: Rubrics complete, points sum correctly, mapping criteria present

### Step 5: Reference Section Compilation
1. Populate sections: Glossary, Tools, Literature, APA
2. Include required fields per format
3. Match Reference IDs to inline citations
4. **Check**: All [Ref: ID] resolve, all sources have required fields

### Step 6: Pre-Submission Validation
Execute all 11 validation steps (Part I). Present validation report. Fix failures and re-validate.

### Step 7: Final Review
Verify Submission Checklist (Part I). Submit when all pass.

---

# Part III: Output Format

## Output Format

Template structure:

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
