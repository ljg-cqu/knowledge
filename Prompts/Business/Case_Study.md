# Case Study: Business Understanding for Software Architecture

Framework for generating case study assessments that link business understanding to software architecture decisions.

## Purpose & Audience

**Purpose:** Generate rigorous, multi-scenario assessments evaluating senior/architect/expert technical leaders' ability to translate business requirements into architecture decisions.

**Target Audience:** Exam designers, educators, enterprise architects, training program developers.

**When to Use:** Creating assessments for technical leadership programs, architecture certification exams, enterprise training materials.

**Prerequisites:** Familiarity with business-architecture integration, Business Model Canvas (BMC), Domain-Driven Design (DDD), and architecture decision-making frameworks.

**Assumptions:**
- LLM has access to current business and architecture knowledge
- User will validate all references and citations for accuracy
- Outputs will be reviewed by domain experts before deployment
- User can access tools for citation verification and link checking

---

# Part I: Requirements & Output Specification

## Scenario Bank Requirements

### Scope

- **Count:** 16–22 scenarios total
- **Difficulty Distribution:** 20% Foundational / 40% Intermediate / 40% Advanced
- **Domain Clusters:** 5 clusters with 3–5 scenarios each:
  1. Strategic Modeling
  2. Value & Risk Analysis
  3. Organizational Dynamics
  4. Architectural Translation
  5. Evolution & Adaptation

### Scenario Structure

Each scenario MUST include:

**Context (200–400 words):**
- At least 2 business constraints
- At least 2 stakeholder roles (diverse: not only C-suite; include engineers, customers, regulators)
- At least 1 market dynamic
- At least 1 organizational factor
- At least 1 `[Ref: ID]` citation

**Tasks (3–4 per scenario):**
- MUST be Mutually Exclusive and Collectively Exhaustive (MECE):
  - Mutually Exclusive: No overlapping responsibilities between tasks
  - Collectively Exhaustive: All aspects of scenario covered by task set
- MUST span business understanding → architecture translation
- Task types: model analysis, value mapping, risk assessment, decisions, stakeholder communication

**Deliverable Specifications:**
- Business Model Analysis: Identify affected BMC blocks; map business changes to value propositions; recognize customer segment implications (table or structured list format)
- Value Mapping Matrix: 2-column table linking value propositions to technical features + risk model with prioritization rationale
- Risk Assessment: Identify business risks, operational constraints, regulatory requirements with severity/impact ratings (High/Medium/Low)
- Architecture Decision Memo: ≤300 words with recommendations, business justification, trade-off analysis, stakeholder alignment

**Grading Framework:**
- Business analysis (30%)
- Value mapping (25%)
- Architecture decisions (30%)
- Justification & trade-offs (15%)
- Partial credit rubrics MUST specify point allocations for incomplete responses

**Trade-Off Categories (MUST address):**
- Value vs technical debt
- Revenue model vs architecture complexity
- Stakeholder alignment vs design purity
- Speed to market vs quality attributes

**Conflict Handling:** When frameworks conflict (e.g., BMC vs Lean Canvas, DDD patterns vs pragmatism):
- Present both perspectives with citations
- State trade-offs explicitly
- Recommend context-specific choice with rationale

**Diversity Requirements:** Scenarios MUST cover:
- Industries: Technology, healthcare, finance, manufacturing (at least 3)
- Company sizes: Startup, SME, enterprise (at least 2)
- Regions: North America, Europe, Asia (at least 2 implied or stated)

### Citation Standards

**Language Distribution:** ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)

**Source Types (MUST include all 4):**
1. Business frameworks (BMC, Lean Canvas, Value Proposition Canvas)
2. Architecture patterns (DDD, microservices, event-driven)
3. Case studies & research reports
4. Tools (modeling, documentation, diagramming)

**Format:** APA 7th edition with language tags

**Inline Citation:** Use `[Ref: ID]` for business models, frameworks, patterns, trade-offs, organizational dynamics

### Reference Section Minimums

| Section | Minimum Count | Examples |
|---------|---------------|----------|
| Glossary, Terminology & Acronyms | ≥10 | BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR |
| Business & Architecture Tools | ≥5 | Miro, ArchiMate, C4 Model, Confluence, Wardley Maps |
| Authoritative Literature & Reports | ≥6 | Osterwalder, Evans, Vernon, Conway, Hohpe, Richardson + ZH sources |
| APA Style Source Citations | ≥12 | Mix of EN/ZH/other; verify language distribution |

**Exception Handling:** If floor counts cannot be met, you MUST:
1. State shortfall quantity and affected section
2. Provide rationale (e.g., "Limited recent ZH sources on Wardley Mapping")
3. Propose sourcing plan to meet minimums

**Scaling Rule:** For >25 scenarios, increase all floor counts by 1.5× (round up).

---

## Required Output Format

**You MUST follow this structure exactly:**

```markdown
## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-n)
  - [Scenario 1: [Title]](#scenario-1-title)
  - [Scenario 2: [Title]](#scenario-2-title)
  - ...
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)
- [Validation Report](#validation-report)

---

## Scenario Bank (Scenarios 1–N)

### Scenario X: [Title]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Cluster Name]

**Context:** (200–400 words with business constraints, stakeholders, market dynamics, organizational factors, diversity; include [Ref: ID] citations)

[Business situation, value propositions, customer segments, revenue model changes, organizational structure, market pressures, regulatory requirements, competitive dynamics, alternative perspectives]

**Task 1: [Task Name] (X pts)**

[Task description requiring deliverable per specifications above]

**Expected Response:**
- [Key element 1]
- [Key element 2]
- [Key element 3]

**Grading:**
- [Criterion 1] (X pts) — includes partial credit breakdown
- [Criterion 2] (Y pts) — includes partial credit breakdown
- [Criterion 3] (Z pts) — includes partial credit breakdown

**Task 2: [Task Name] (Y pts)**

[Repeat structure]

**Task 3: [Task Name] (Z pts)**

[Repeat structure]

**Common Omissions:**
- [Typical gap 1 — e.g., missing organizational impact (Conway's Law)]
- [Typical gap 2 — e.g., no evolution/migration strategy]
- [Typical gap 3 — e.g., weak value-to-architecture tracing]

**Bonus Opportunities (optional, 1-2 pts):**
- [Advanced consideration 1]
- [Advanced consideration 2]

---

[Repeat for all scenarios]

---

## Reference Sections

Assign IDs: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA (A1…An). Use inline as `[Ref: G1, T2, A5]`.

### Glossary, Terminology & Acronyms

| ID | Term | Definition | Use Cases | Related Terms |
|----|------|------------|-----------|---------------|
| G1 | Business Model Canvas (BMC) | Strategic management template with 9 building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure [EN] | Business model design, validation, innovation | Lean Canvas, Value Proposition Canvas |
| G2 | Value Proposition | Bundle of products/services creating value for a specific customer segment; maps to technical features and quality attributes [EN] | Product-market fit, differentiation, architecture prioritization | Jobs-to-be-Done, Quality Attributes |

[Continue with G3–G10+, covering: DDD, Conway's Law, Technical Debt, ADR, Bounded Context, Capability Mapping, Living Documentation, Wardley Mapping, Customer Segment, Revenue Stream, Value Stream Mapping, System Boundaries, Process Mapping]

### Business & Architecture Tools

| ID | Tool Name | Description | Pricing | Adoption | Last Updated | Integrations | Use Cases | URL |
|----|-----------|-------------|---------|----------|--------------|--------------|-----------|-----|
| T1 | Miro | Infinite canvas for BMC, journey mapping, architecture diagrams [EN] | Freemium to Enterprise | 80M+ users (approx., Q4 2024) | Q4 2024 | Jira, Slack, Confluence | Business model workshops, architecture design | https://miro.com |
| T2 | ArchiMate | Open standard for enterprise architecture modeling; ISO/IEC/IEEE 42010 compliant [EN] | Free (standard) | Enterprise-wide adoption | 2023 (v3.2) | Modeling tools (Sparx, Archi) | Business-IT alignment, impact analysis | https://www.opengroup.org/archimate-forum |

[Continue with T3–T5+: C4 Model, Confluence, LucidChart, Wardley Maps tool]

**Tool Inclusion Criteria:**
- Pricing model stated or marked "N/A" for FOSS
- Adoption metrics cited with source or marked "approximate"
- Last update ≤18 months; if older, mark "(legacy but stable)"
- Integration list or "standalone"

### Authoritative Literature & Case Studies

| ID | Citation | Description |
|----|----------|-------------|
| L1 | Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley. | Business Model Canvas framework; foundational for business-technical alignment |
| L2 | Evans, E. (2003). *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley. | DDD patterns; ubiquitous language, bounded contexts, strategic design |

[Continue with L3–L6+: Vernon, Conway, Skelton & Pais, Richardson, ZH sources]

### APA Style Source Citations

**A1.** Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]

**A2.** Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley Professional. [EN]

**A3.** 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]
(Zhou, A. (2021). *The essence of architecture*. Publishing House of Electronics Industry.)

[Continue with A4–A12+: Vernon, Conway, Skelton & Pais, Richardson, Hohpe & Woolf, 张逸, Fowler, Newman, 肖然, Brown, Humble & Farley, Kim et al., Wardley]

**Citation Verification:** Before including citations, verify:
- Publication year matches authoritative source (publisher website, ISBN database)
- Author names spelled correctly
- For web references: include archived link (Wayback Machine) or note "as of [date]"
- For tool statistics: cite source or mark "approximate"

---

## Validation Report

Execute all validation steps below. Present results in this table. If ANY check fails, fix issues and re-validate. Proceed ONLY when ALL checks pass.

| Check | Result | Status |
|-------|--------|--------|
| **1. Count Audit** | Glossary: X (≥10) \| Tools: Y (≥5) \| Literature: Z (≥6) \| APA: W (≥12) \| Scenarios: N (F%/I%/A%) | PASS/FAIL |
| **2. Difficulty Distribution** | Foundational: F% \| Intermediate: I% \| Advanced: A% (target: 20/40/40 ±5%) | PASS/FAIL |
| **3. Citation Coverage** | X/Y scenarios ≥1 citation (Z%); W/Y scenarios ≥2 citations (V%) — target: ≥70% with ≥1, ≥30% with ≥2 | PASS/FAIL |
| **4. Language Distribution** | EN: X (Y%) \| ZH: A (B%) \| Other: C (D%) — target: EN ~50-70%, ZH ~20-40%, Other ~5-15% | PASS/FAIL |
| **5. Recency** | X/Y citations (Z%) from 2022-2025 — target: ≥50% general, ≥70% for digital transformation/cloud-native topics | PASS/FAIL |
| **6. Source Diversity** | Type 1: X \| Type 2: Y \| Type 3: Z \| Type 4: W \| Distinct types: N \| Max single source: M (P%) — target: ≥3 types, no source >25% | PASS/FAIL |
| **7. Link Validation** | Tested X links: Y accessible, Z broken — list broken: [URLs] — target: all accessible OR archived alternatives provided | PASS/FAIL |
| **8. Cross-Reference Integrity** | X inline `[Ref: ID]`: Y resolved, Z broken — list broken: [IDs] — target: all resolved (Z=0) | PASS/FAIL |
| **9. Context Length** | Sample 5 random scenarios: S#: X words \| S#: Y words \| ... — target: all in 200–400 range | PASS/FAIL |
| **10. MECE Tasks** | X/Y scenarios MECE verified; Z with overlaps/gaps — list issues: [S# details] — target: all MECE (Z=0) | PASS/FAIL |
| **11. Grading Rubrics** | X/Y scenarios complete rubrics; Z missing/incomplete — list issues: [S# details] — target: all complete (Z=0) | PASS/FAIL |
| **12. Business-Technical Mapping** | X/Y scenarios (Z%) with explicit business-to-architecture connection — target: ≥80% | PASS/FAIL |
| **13. Stakeholder Diversity** | X/Y scenarios (Z%) include diverse roles (not only C-suite) — target: ≥70% | PASS/FAIL |
| **14. Industry/Size/Region Diversity** | Industries: [list] \| Sizes: [list] \| Regions: [list] — target: ≥3 industries, ≥2 sizes, ≥2 regions | PASS/FAIL |
| **15. TOC & Anchor Links** | TOC present: Y/N \| All anchors functional: Y/N — target: both Y | PASS/FAIL |

**Mandatory:** If ANY check fails, document failures, remediate, and re-run validation. Submit only when all checks pass.
```

---

# Part II: Generation Procedure

Execute steps sequentially. Perform inline validation after steps marked with ✓.

## Step 1: Domain Planning & Allocation

1. Identify 5 domain clusters (Strategic Modeling, Value & Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution & Adaptation)
2. Allocate 3–5 scenarios per cluster (16–22 total)
3. Assign difficulty: 20% Foundational, 40% Intermediate, 40% Advanced

**✓ Verification:**
- Total count: 16–22?
- Difficulty ratio: 20/40/40 ±5%?

## Step 2: Reference Collection

1. Identify ≥10 glossary terms (BMC, Value Proposition, DDD, Conway's Law, Technical Debt, ADR, Bounded Context, Capability Mapping, Living Documentation, Wardley Mapping, Customer Segment, Revenue Stream, Value Stream Mapping, System Boundaries, Process Mapping)
2. Identify ≥5 tools (Miro, ArchiMate, C4 Model, Confluence, LucidChart with pricing, adoption, last update, integrations)
3. Identify ≥6 literature sources (Osterwalder, Evans, Vernon, Conway, Skelton & Pais, Richardson + ZH authors: 周爱民, 张逸, 肖然)
4. Compile ≥12 APA citations with language tags; verify publication years and author names
5. Assign IDs: G1-Gn (Glossary), T1-Tn (Tools), L1-Ln (Literature), A1-An (APA)

**✓ Verification:**
- Counts: ≥10/5/6/12?
- Language distribution: ~60/30/10?
- Recency: ≥50% from 2022-2025 (≥70% for digital transformation topics)?
- Source diversity: ≥3 types, no source >25%?

## Step 3: Scenario Generation

For each scenario:

1. Write context (200–400 words):
   - At least 2 business constraints (budget, timeline, regulatory, competitive)
   - At least 2 stakeholder roles (diverse: C-suite, engineers, customers, regulators, partners)
   - At least 1 market dynamic (competition, disruption, customer demand shift)
   - At least 1 organizational factor (structure, culture, Conway's Law implications)
   - Include ≥1 `[Ref: ID]` citation
   - Address diversity: vary industry, company size, region

2. Design 3–4 MECE tasks:
   - Verify Mutually Exclusive: no task overlaps another's scope
   - Verify Collectively Exhaustive: all scenario aspects covered by task set
   - Span business understanding → architecture translation
   - Require deliverables per specifications (analysis, matrix, assessment, memo)

3. Create grading rubrics:
   - Business analysis (30%), value mapping (25%), decisions (30%), justification (15%)
   - Specify point allocations for partial credit
   - Define common omissions (e.g., missing Conway's Law impact, no evolution strategy)

4. Identify bonus opportunities (1–2 pts): ADR practices, phased evolution, organizational restructuring

**✓ Verification (after every 3 scenarios):**
- Context: 200–400 words, ≥1 citation, diverse stakeholders?
- Tasks: MECE verified (no overlaps, no gaps)?
- Rubrics: complete with point allocations summing correctly?
- Business-to-architecture mapping: explicit and traceable?
- Diversity: industries, sizes, regions represented?

## Step 4: Reference Section Compilation

1. Populate Glossary with definitions, use cases, related terms (table format)
2. Populate Tools with pricing, adoption, last update, integrations, use cases
3. Populate Literature with descriptions
4. Populate APA citations with full details and language tags
5. Verify all inline `[Ref: ID]` match Reference Section IDs

**✓ Verification:**
- All inline references resolve?
- All required fields present for each source?
- Tool statistics cited or marked "approximate"?

## Step 5: Validation Execution

Execute all 15 validation checks (see Validation Report table in Part I). Document results. If any fail, remediate and re-validate.

## Step 6: Final Review

1. Verify TOC includes all scenarios and reference sections with working anchor links
2. Confirm output format matches required structure exactly
3. Run final read for clarity, concision, coherence
4. Ensure lines <120 characters where feasible (per AGENTS.md)
5. Remove trailing whitespace

**Submission Criteria:** All 15 validation checks MUST pass.

---

<!-- Optimization Traceability (for maintainers):
Applied 21 LLM-Friendly Prompt Guidelines:
- G1 (Context): Added Purpose & Audience section with assumptions
- G2 (Clarity): Operationalized Conflict Handling; expanded acronyms; replaced vague verbs
- G3 (Precision): Defined deliverable schemas; specified MECE criteria; min elements per context
- G4 (Relevance): Maintained tight scope (no changes needed)
- G5 (MECE): Consolidated Quality Gates/Validation/Checklist; eliminated redundancy
- G6-8 (Sufficiency/Breadth/Depth): Preserved comprehensive coverage
- G9 (Significance): Preserved business-technical mapping focus
- G10 (Concision): Reduced from 410 to ~310 lines (~24% reduction); consolidated validation sections
- G11 (Accuracy): Added citation verification instructions; tool statistics sourcing
- G12-14 (Credibility/Logic/Risk-Value): Preserved strengths
- G15 (Fairness): Added diversity requirements (industry/size/region); stakeholder diversity check
- G16 (Structure): Enhanced with tables for glossary, tools, literature
- G17 (Output Format): Elevated to Part I; made requirements imperative with "MUST"
- G18-21 (Evidence/Validation/Practicality/Success): Preserved comprehensive validation framework; added stakeholder & diversity checks

Changes vs original:
- Added Purpose & Audience (20 lines)
- Consolidated Quality Gates → Validation Report (saved 60 lines)
- Removed Submission Checklist (saved 15 lines, now covered by validation)
- Added diversity requirements (15 lines)
- Restructured output format as imperative specification (10 lines)
- Compressed glossary to table format example (saved 30 lines)
- Net: -100 lines (~24% reduction) with improved clarity

Preserved:
- 3-part structure (Requirements/Output, Procedure, implicit Output in Requirements)
- 11-step validation framework (enhanced to 15 checks)
- Reference section categorization
- Quantified minimums and quality gates
- Multi-language citation requirements
-->
