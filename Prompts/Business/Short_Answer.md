# Short Answer / Calculation - Business Understanding for Software Architecture

**Purpose**: Generate comprehensive, self-contained short answer assessments that translate business requirements into actionable architecture decisions for senior technical leaders.

---

# Part I: Specifications

## Quick Reference

- **Target Audience**: Senior technical leaders, software architects, and expert practitioners
- **Objective**: Produce 25–40 short answer problems that explicitly map business drivers to architecture decisions
- **Deliverables**: Self-contained problems with clear business context, MECE-structured reasoning, worked solutions with citations, and objective grading rubrics
- **Quality Standard**: All problems must demonstrate business-to-architecture translation with measurable validation criteria

## Specifications

### Scope and Structure

**Scope Definition**:
- Generate exactly 25–40 problems, each containing:
  - Explicit business constraints and success criteria
  - Clear architecture implications and trade-offs
  - Complete context (scope, assumptions, stakeholder impact)
  - All necessary artifacts for standalone assessment

**Problem Structure** (MECE Coverage):
- **Self-Contained Design**: Each problem includes all assumptions, constraints, business context, and required deliverables
- **Difficulty Distribution**: Maintain strict 20/40/40 ratio (Foundational/Intermediate/Advanced)
- **Problem Type Coverage**:
  - Business model analysis (2–3 sentences with BMC/Value Proposition mapping)
  - Value stream mapping (identify waste, optimization opportunities)
  - Risk assessment (quantitative where possible, with mitigation strategies)
  - Architectural justification (2–4 sentences with explicit trade-off analysis)
  - Trade-off calculation (cost, performance, maintainability, scalability)

**Expected Answer Format**:
- **Reasoning Structure**: Apply MECE principles with 2–4 step solutions
- **Business-to-Architecture Mapping**: Explicit translation from business drivers to technical decisions
- **Evidence**: Minimum 1 citation per solution ([Ref: ID] format)
- **Self-Review**: Include reasoning validation prompts where complexity warrants

**Grading Model** (10-point scale):
- Business Analysis: 40% (4 points) - Correct identification of business drivers, constraints, stakeholder impact
- Value Mapping: 30% (3 points) - Accurate translation to technical features and quality attributes
- Architectural Decisions: 30% (3 points) - Justified architecture choices with trade-off analysis
- **Partial Credit**: Award proportional points for incomplete but directionally correct answers
- **Tolerance**: Accept alternative valid frameworks (document in rubric)

**Alternative Solution Paths**:
- Document all acceptable approaches (e.g., BMC vs. Lean Canvas, DDD vs. functional decomposition)
- Note framework applicability conditions
- Acknowledge valid trade-offs and context-dependent decisions

### Citation Standards

**Language Distribution** (Target Mix):
- English (EN): 50–70% of total citations
- Chinese (ZH): 20–40% of total citations  
- Other languages: 5–15% of total citations
- **Tagging**: All citations must include language tag ([EN], [ZH], [JA], etc.)

**Source Type Requirements** (Minimum ≥3 types):
1. **Business Frameworks & Methodologies**: BMC, Lean Canvas, Value Proposition Design, OKRs, North Star Metric
2. **Architecture Patterns & Practices**: DDD, Microservices patterns, Event-driven architecture, CQRS, Hexagonal architecture
3. **Case Studies & Industry Reports**: Real-world implementations, transformation journeys, failure analyses
4. **Tools & Platforms**: Architecture tools (C4, ArchiMate), collaboration platforms (Miro, Confluence), development frameworks

**Citation Format Standards**:
- **Academic Sources**: APA 7th edition with language tags
- **Industry Reports**: Include organization, publication date, URL (or archived link if unavailable)
- **Tools/Platforms**: Name, version/update date, tier (free/freemium/enterprise), user count (if public), official URL
- **Inline References**: Use [Ref: ID] format (G# for glossary, T# for tools, L# for literature, A# for APA citations)

**Citation Quality Gates**:
- **Credibility**: Prioritize peer-reviewed research, established industry frameworks, authoritative practitioners
- **Recency**: ≥50% from last 3 years (≥70% for rapidly evolving domains: digital transformation, cloud-native, AI/ML)
- **Diversity**: No single source type >25% of total citations
- **Accessibility**: All URLs must be accessible or archived (use Internet Archive for deprecated links)

### Reference Minimum Requirements

| Reference Section | Minimum Count | Quality Criteria | Examples |
| --- | --- | --- | --- |
| **Glossary, Terminology & Acronyms** | ≥10 entries | Define technical and business terms; include usage context and cross-references | BMC, Value Proposition, DDD, Bounded Context, Conway's Law, Technical Debt, ADR, Capability Mapping, Value Stream, System Boundaries |
| **Business & Architecture Tools** | ≥5 entries | Include tier, user base, recent updates, official URLs | Miro, ArchiMate, C4 Model, Confluence, LucidChart, Wardley Maps, draw.io |
| **Authoritative Literature & Reports** | ≥6 entries | Prioritize seminal works and recent authoritative sources | Business Model Generation, Domain-Driven Design, Team Topologies, Microservices Patterns, case studies |
| **APA Style Source Citations** | ≥12 total | Follow APA 7th; maintain language distribution; verify accessibility | See language mix: 50-70% EN, 20-40% ZH, 5-15% other |

### Quality Gates

**Citation Quality**:
- **Recency Threshold**: ≥50% of citations from last 3 years; ≥70% for fast-evolving domains (digital transformation, cloud-native, AI/ML, blockchain)
- **Source Diversity**: Minimum 3 distinct source types; no single type >25% of total
- **Authority**: Prioritize peer-reviewed research, established frameworks, recognized industry practitioners
- **Accessibility**: 100% of citations must have accessible or archived URLs

**Evidence Coverage**:
- **Baseline**: ≥70% of problems include ≥1 citation
- **Advanced**: ≥30% of problems include ≥2+ citations (for complex, multi-framework scenarios)
- **Citation Relevance**: Each [Ref: ID] must directly support the reasoning step where it appears

**Content Quality**:
- **Business-Technical Mapping**: ≥80% of problems require explicit translation from business drivers to architecture decisions
- **MECE Reasoning**: 100% of worked solutions demonstrate mutually exclusive, collectively exhaustive analysis
- **Completeness**: 100% of problems include business context, expected answer, worked solution, grading rubric
- **Precision**: 0 tolerance for ambiguous terminology; all domain terms defined in Glossary or inline

**Validation Coverage**:
- **Self-Review**: Include reasoning validation prompts for Intermediate and Advanced problems
- **Error Checking**: All quantitative calculations verified; all qualitative judgments justified with evidence

### Success Criteria

| Dimension | Measurable Target | Verification Method |
| --- | --- | --- |
| **Coverage** | 25–40 problems with strict 20/40/40 difficulty ratio | Count audit (Step 1 validation) |
| **Context Clarity** | 100% of problems explicitly state: business scenario, constraints, assumptions, stakeholder impact | Manual review against checklist |
| **Reasoning Quality** | 100% of worked solutions demonstrate MECE steps, cite ≥1 source, include self-review for complex problems | Citation coverage audit (Step 2), solution structure review |
| **Business-Technical Mapping** | ≥80% of problems require explicit business-to-architecture translation with justified trade-offs | Business-technical mapping audit (Step 10) |
| **Citation Standards** | All citations meet recency, diversity, accessibility, and language distribution criteria | Steps 3-6 validation |
| **Reference Completeness** | Meet minimum counts: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12 | Count audit (Step 1) |
| **Validation Completion** | All 10 validation steps executed and reported as PASS | Pre-submission validation checklist |
| **Answer Completeness** | 100% of problems have complete worked solutions with grading rubrics | Answer completeness audit (Step 8) |
| **Actionability** | 100% of solutions provide implementable guidance with concrete next steps | Practicality review |

### Pre-Submission Validation Checklist

**Execute all 10 validation steps sequentially. Record PASS/FAIL for each. Remediate all failures before proceeding.**

| Step | Validation Item | Success Criteria | Verification Method |
| --- | --- | --- | --- |
| **1** | **Count Audit** | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12; Problems 25-40 with 20/40/40 ratio | Automated count + manual difficulty classification |
| **2** | **Citation Coverage** | ≥70% problems have ≥1 citation; ≥30% have ≥2+ citations | Parse all [Ref: ID] occurrences; calculate percentages |
| **3** | **Language Distribution** | EN 50-70%, ZH 20-40%, Other 5-15% | Count language tags; calculate percentages |
| **4** | **Recency Threshold** | ≥50% citations from last 3 years (≥70% for digital transformation/cloud-native/AI/ML) | Extract publication years; calculate percentage |
| **5** | **Source Diversity** | ≥3 source types; no single type >25% | Classify sources; calculate distribution |
| **6** | **Link Accessibility** | 100% of URLs accessible or archived | Test all URLs; archive unavailable links |
| **7** | **Cross-Reference Integrity** | All [Ref: ID] resolve to valid G#/T#/L#/A# entries | Parse inline references; validate against reference sections |
| **8** | **Answer Completeness** | 100% of problems have expected answer + worked solution + grading rubric | Manual review of problem structure |
| **9** | **Solution Clarity** | 100% of solutions demonstrate clear business-to-architecture mapping with MECE steps | Manual review of solution reasoning structure |
| **10** | **Business-Technical Mapping** | ≥80% of problems require explicit business driver → architecture decision translation | Classify problems; calculate percentage |

**Remediation Protocol**:
- **If any step FAILS**: Document gap, remediate, re-run failed step + all subsequent steps
- **Iteration Limit**: Maximum 3 remediation cycles before escalating to manual review
- **Final Report**: Include validation summary table with PASS/FAIL status and remediation notes

---

# Part II: Instructions

### Step 1: Topic Identification & Planning

**Objective**: Establish MECE problem clusters with balanced difficulty distribution.

**1.1 Identify Topic Clusters** (4–6 clusters):
- **Cluster Selection Criteria**:
  - Mutually exclusive: No overlap in business-architecture focus areas
  - Collectively exhaustive: Cover full spectrum of business-to-architecture translation scenarios
  - Balanced relevance: Each cluster addresses distinct stakeholder concerns

- **Example Clusters**:
  1. **Strategic Modeling**: BMC analysis, value proposition mapping, capability modeling
  2. **Value & Risk Analysis**: Value stream optimization, risk quantification, cost-benefit analysis
  3. **Organizational Dynamics**: Conway's Law applications, team topologies, organizational boundaries
  4. **Architectural Translation**: Business requirements → architecture decisions, constraint mapping, trade-off analysis
  5. **Evolution & Adaptation**: Technical debt management, architectural evolution, migration strategies
  6. **Integration & Boundaries**: System boundaries, context mapping, integration patterns

**1.2 Allocate Problems per Cluster** (4–8 problems each):
- Distribute difficulty: Each cluster should contain Foundational, Intermediate, and Advanced problems
- Total problem count: 25–40 across all clusters
- Difficulty ratio: Maintain 20/40/40 split globally (not necessarily per cluster)

**1.3 Validation Checkpoint**:
- ✓ Total problems ∈ [25, 40]
- ✓ Global difficulty ratio = 20/40/40 (±5% tolerance)
- ✓ Clusters are MECE (no overlap, complete coverage)
- ✓ Each cluster addresses distinct business perspective
- ✓ Problem distribution per cluster ∈ [4, 8]

**Deliverable**: Cluster allocation table with problem counts and difficulty breakdown per cluster.

### Step 2: Reference Collection

**Objective**: Assemble authoritative, diverse, and current reference materials that meet all quality gates.

**2.1 Glossary, Terminology & Acronyms** (Minimum: 10 entries):
- **Content**: Define technical and business terms used across problems
- **Format**: Term name, definition, usage context, cross-references
- **Coverage**: Business frameworks (BMC, Lean Canvas), architecture patterns (DDD, Microservices), organizational concepts (Conway's Law, Team Topologies)
- **Quality**: Clear, concise definitions; avoid circular references; include practical application context

**2.2 Business & Architecture Tools** (Minimum: 5 entries):
- **Content**: Modeling, diagramming, collaboration, and documentation tools
- **Format**: Tool name, purpose, tier (free/freemium/enterprise), user count (if available), recent update date, official URL
- **Examples**: Miro, ArchiMate, C4 Model, Confluence, LucidChart, Wardley Maps, draw.io
- **Quality**: Verify URLs; prioritize widely adopted, actively maintained tools

**2.3 Authoritative Literature & Reports** (Minimum: 6 entries):
- **Content**: Seminal works, recent authoritative sources, case studies
- **Format**: Author, year, title, publisher/journal
- **Coverage**: Business strategy, architecture patterns, organizational design, domain modeling
- **Quality**: Prioritize peer-reviewed research, established practitioners, recognized industry frameworks

**2.4 APA Style Source Citations** (Minimum: 12 entries):
- **Content**: Books, journal articles, industry reports, online resources
- **Format**: APA 7th edition with language tags ([EN], [ZH], etc.)
- **Language Distribution**: 50-70% EN, 20-40% ZH, 5-15% other
- **Recency**: ≥50% from last 3 years (≥70% for digital transformation/cloud-native)
- **Diversity**: ≥3 source types; no single type >25%

**2.5 Validation Checkpoint**:
- ✓ Meet minimum counts: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12
- ✓ All citations tagged with language ([EN], [ZH], etc.)
- ✓ Publication years recorded for recency check
- ✓ Source types classified for diversity check
- ✓ All URLs tested for accessibility

**Deliverable**: Complete reference sections ready for inline citation.

### Step 3: Problem Generation

**Objective**: Create self-contained problems with complete worked solutions, grading rubrics, and validated citations.

**3.1 Problem Drafting** (Per-Problem Requirements):
- **Problem Statement** (2–4 sentences):
  - State business scenario with explicit context (industry, scale, constraints)
  - Identify stakeholders and their success criteria
  - Surface all relevant assumptions and constraints
  - Pose clear question requiring business-to-architecture translation

- **Difficulty Classification**: Tag as Foundational/Intermediate/Advanced

- **Problem Type Coverage**: Ensure mix across clusters:
  - Business model analysis (BMC, Lean Canvas, Value Proposition)
  - Value stream mapping (identify waste, optimization opportunities)
  - Risk assessment (quantitative risk calculation, mitigation strategies)
  - Architectural justification (pattern selection, trade-off analysis)
  - Trade-off calculation (cost, performance, maintainability, scalability)

**3.2 Expected Answer** (1–2 sentences per key point):
- State concise, correct answer highlighting key business-architecture mappings
- Use bullet points for multi-part answers
- Avoid implementation details (save for worked solution)

**3.3 Worked Solution** (2–4 MECE steps):
- **Step Structure**:
  - **Step Title**: Clearly describe reasoning phase (e.g., "Business Model Analysis", "Value Mapping", "Architectural Translation")
  - **Step Content**: Apply MECE reasoning; show explicit business-to-architecture mapping
  - **Citations**: Include ≥1 [Ref: ID] per solution (≥2 for complex problems)
  - **Reasoning Transparency**: Show how conclusions follow from premises

- **Self-Review Prompts** (for Intermediate/Advanced problems):
  - Include reasoning validation questions (e.g., "Confirm each business driver maps to a distinct architectural requirement")
  - Request citation coverage check (e.g., "Validate ≥1 [Ref: ID] included")
  - Prompt trade-off verification (e.g., "Verify all alternatives considered and trade-offs justified")

**3.4 Grading Rubric** (10-point scale):
- **Business Analysis (4 points)**: Criteria for identifying business drivers, constraints, stakeholder impact
- **Value Mapping (3 points)**: Criteria for translating business needs to technical features/quality attributes
- **Architectural Decisions (3 points)**: Criteria for justified architecture choices with trade-off analysis
- **Partial Credit Guidelines**: Define point allocation for incomplete but directionally correct answers

**3.5 Validation Checkpoint** (After every 5 problems):
- ✓ All problems have complete structure: statement, expected answer, worked solution, grading rubric
- ✓ All worked solutions demonstrate MECE reasoning
- ✓ All solutions include ≥1 [Ref: ID] (check for ≥2 in complex problems)
- ✓ All citations resolve to valid reference entries (G#/T#/L#/A#)
- ✓ Self-review prompts included for Intermediate/Advanced problems
- ✓ Business-to-architecture mapping explicit in ≥80% of last 5 problems

**3.6 Iteration Protocol**:
- Generate problems in batches of 5
- Run validation checkpoint after each batch
- Remediate gaps before proceeding to next batch
- Track cumulative metrics (difficulty ratio, citation coverage, business-technical mapping percentage)

**Deliverable**: Complete problem bank (25–40 problems) with validated solutions and rubrics.

### Step 4: Reference Compilation

**Objective**: Finalize all reference sections with complete, accessible, and cross-validated entries.

**4.1 Populate Reference Sections**:
- **Glossary, Terminology & Acronyms**: Ensure ≥10 entries with consistent formatting
  - Format: **ID. Term**: Definition. Usage context. [Language Tag]
  - Example: **G1. Business Model Canvas (BMC)**: 9-block template mapping business model to technical requirements. [EN]

- **Business & Architecture Tools**: Ensure ≥5 entries with current information
  - Format: **ID. Tool Name**: Purpose, tier, user count, update date, URL. [Language Tag]
  - Example: **T1. Miro**: Visual collaboration for BMC and architecture diagrams. Freemium-Enterprise. 80M+ users. Q4 2024 update. https://miro.com [EN]

- **Authoritative Literature & Reports**: Ensure ≥6 entries with complete citations
  - Format: **ID. Author, Year, Title, Publisher.** Key topics covered.
  - Example: **L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** BMC framework; business-technical alignment.

- **APA Style Source Citations**: Ensure ≥12 entries following APA 7th edition
  - Format: **ID. Full APA 7th citation. [Language Tag]**
  - Example: **A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]**

**4.2 Cross-Reference Validation**:
- Parse all [Ref: ID] in worked solutions
- Verify each reference resolves to valid entry (G#/T#/L#/A#)
- Flag and remediate any broken references
- Ensure bidirectional consistency (inline refs ↔ reference sections)

**4.3 URL Accessibility Check**:
- Test all URLs in Tools and APA sections
- Archive unavailable URLs using Internet Archive (https://web.archive.org)
- Replace dead links with archived versions
- Document archive dates for transparency

**4.4 Language and Recency Audit**:
- Count citations by language tag; verify 50-70% EN, 20-40% ZH, 5-15% other
- Extract publication years; verify ≥50% from last 3 years (≥70% for fast-evolving domains)
- Adjust reference mix if thresholds not met

**4.5 Source Diversity Check**:
- Classify citations by source type (frameworks, patterns, case studies, tools)
- Verify ≥3 source types present
- Verify no single source type >25% of total
- Add diverse sources if needed

**Deliverable**: Complete, validated reference sections with all cross-references resolved and URLs verified.

### Step 5: Final Validation & Quality Assurance

**Objective**: Execute comprehensive validation checklist, remediate all failures, and certify output meets all quality gates.

**5.1 Execute 10-Step Validation** (See Pre-Submission Validation Checklist):
- Run all validation steps sequentially
- Record PASS/FAIL status for each step
- Document specific gaps for any FAIL results

**5.2 Remediation Protocol** (For each FAIL):
1. **Identify Root Cause**: Analyze why validation failed
2. **Remediate**: Make targeted corrections to content
3. **Re-Validate**: Re-run failed step + all subsequent steps
4. **Iterate**: Repeat until PASS achieved (max 3 cycles)
5. **Escalate**: If FAIL persists after 3 cycles, flag for manual review

**5.3 Generate Validation Report**:
Create summary table documenting validation results:

```markdown
## Validation Report

| Step | Item | Status | Notes |
| --- | --- | --- | --- |
| 1 | Count Audit | PASS | Glossary: 15, Tools: 7, Literature: 8, APA: 16, Problems: 32 (6/13/13) |
| 2 | Citation Coverage | PASS | 78% problems have ≥1 citation; 34% have ≥2 |
| 3 | Language Distribution | PASS | EN: 62%, ZH: 31%, Other: 7% |
| 4 | Recency Threshold | PASS | 58% from last 3 years |
| 5 | Source Diversity | PASS | 4 source types; max single type: 23% |
| 6 | Link Accessibility | PASS | All URLs accessible or archived |
| 7 | Cross-Reference Integrity | PASS | All [Ref: ID] resolve |
| 8 | Answer Completeness | PASS | All 32 problems have complete solutions |
| 9 | Solution Clarity | PASS | All solutions show MECE business-to-architecture steps |
| 10 | Business-Technical Mapping | PASS | 84% require explicit translation |

**Overall Status**: ✓ ALL PASS - Ready for delivery
```

**5.4 Final Quality Review**:
- **Completeness**: Verify all sections present (Problem Bank, 4 Reference Sections, Validation Report)
- **Consistency**: Check terminology consistency across problems
- **Clarity**: Ensure all problems are self-contained and unambiguous
- **Actionability**: Verify solutions provide implementable guidance
- **Professional Polish**: Check formatting, grammar, spelling

**Deliverable**: Validation-certified output with comprehensive validation report.

---

# Part III: Output Format

**Mandatory Output Structure**: Begin with comprehensive Table of Contents (TOC) linking to all major sections.

**Formatting Requirements**:
- **TOC**: Must include anchor links to all top-level headings (##) and major subsections (###)
- **Lists**: Use bulleted lists for unordered items, numbered lists for sequential steps
- **Tables**: Use for structured comparisons, rubrics, reference sections
- **Diagrams**: Use Mermaid syntax for flowcharts, architecture diagrams, process flows (no styling/colors)
- **Code Blocks**: Use fenced code blocks with language tags (```markdown, ```mermaid, ```python)
- **Formulas**: Use LaTeX syntax for mathematical expressions where applicable
- **Emphasis**: Use **bold** for key terms, *italics* for emphasis, `code` for inline technical terms

```markdown
## Contents

1. [Problem Bank](#problem-bank-problems-1-n)
   - [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
   - [Topic 2: Value & Risk Analysis](#topic-2-value--risk-analysis)
   - [Topic 3: Organizational Dynamics](#topic-3-organizational-dynamics)
   - [Topic 4: Architectural Translation](#topic-4-architectural-translation)
   - [Topic 5: Evolution & Adaptation](#topic-5-evolution--adaptation)
   - [Additional topics as needed...]
2. [Reference Sections](#reference-sections)
   - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
   - [Business & Architecture Tools](#business--architecture-tools)
   - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
   - [APA Style Source Citations](#apa-style-source-citations)
3. [Validation Report](#validation-report)

---

## Problem Bank (Problems 1–N)

### Topic 1: Strategic Modeling

#### Problem 1: A SaaS company shifts from monthly to annual billing. Analyze the Business Model Canvas impact and identify 3 architectural requirements this change introduces.

**Difficulty:** Intermediate

**Expected Answer:**
1. **BMC Analysis**: Revenue Streams transition from monthly to annual prepayment; Customer Relationships shift from transactional to commitment-based; Key Activities expand to include retention and customer success
2. **Architectural Requirements** (Business-to-Architecture Mapping):
   - **Subscription Management**: Handle annual billing cycles, mid-cycle upgrades/downgrades, prorated refunds
   - **Revenue Recognition**: Implement deferred revenue accounting for annual prepayments
   - **Usage Analytics**: Track long-term consumption patterns to predict renewal risk and inform customer success interventions

**Worked Solution:**

**Step 1 - Business Model Canvas Analysis** [Ref: G1, A1]:
Apply BMC framework to identify affected components:
- **Revenue Streams**: Monthly recurring revenue (MRR) → annual recurring revenue (ARR)
  - *Business Impact*: Improved cash flow predictability, 12-month revenue commitment
  - *Technical Implication*: Deferred revenue recognition system (GAAP/IFRS compliance)
- **Customer Relationships**: Transactional (monthly renewal) → commitment-based (annual contract)
  - *Business Impact*: Higher switching costs, increased customer lifetime value (CLV), greater retention pressure
  - *Technical Implication*: Customer health scoring, proactive engagement systems
- **Key Activities**: Transaction processing → retention management + customer success
  - *Business Impact*: Shift from acquisition to retention economics
  - *Technical Implication*: Usage monitoring, renewal prediction, intervention workflows

**Step 2 - Value Proposition & Customer Segment Mapping** [Ref: G2, G11]:
- **Value Proposition Evolution**:
  - Old: Flexibility (monthly cancellation)
  - New: Cost savings (annual discount) + predictability
  - *Technical Requirement*: Transparent usage dashboards to justify annual commitment value
- **Customer Segment Shift**:
  - Old: SMB with monthly budgets
  - New: Enterprise with annual procurement cycles
  - *Technical Requirement*: Enterprise features (SSO, audit logs, SLA guarantees, dedicated support)

**Step 3 - Architectural Requirements (Business-to-Architecture Translation)** [Ref: A7, A10]:
1. **Subscription Management System**:
   - *Business Driver*: Annual billing cycles with mid-cycle changes
   - *Architecture Decision*: Event-sourced subscription service with temporal modeling
   - *Key Features*: Plan upgrades/downgrades, prorated refund calculation, contract amendments
   - *Trade-off*: Complexity vs. flexibility (chosen: flexible to support diverse enterprise needs)

2. **Revenue Recognition Engine**:
   - *Business Driver*: GAAP/IFRS compliance for deferred revenue
   - *Architecture Decision*: Separate billing and revenue recognition domains [Ref: G3]
   - *Key Features*: Amortization schedules, revenue waterfall reports, audit trails
   - *Trade-off*: Build vs. buy (consider: Stripe Billing, Chargebee, custom solution)

3. **Customer Success Platform**:
   - *Business Driver*: Retention economics; annual churn has 12x impact vs. monthly
   - *Architecture Decision*: Analytics pipeline feeding health scoring model
   - *Key Features*: Usage telemetry, engagement scoring, renewal risk prediction, automated alerts
   - *Integration Points*: CRM (Salesforce), support (Zendesk), product analytics (Amplitude)

**Step 4 - Risk & Trade-off Analysis** [Ref: G5]:
- **Technical Debt Risk**: Rushed implementation may create billing inconsistencies
  - *Mitigation*: Phased rollout, extensive testing, parallel run of old/new billing
- **Data Consistency Risk**: Multiple systems (billing, revenue, CRM) must stay synchronized
  - *Mitigation*: Event-driven architecture with event sourcing for audit trail
- **Migration Risk**: Existing monthly customers transitioning to annual
  - *Mitigation*: Gradual migration, incentivized upgrades, maintain dual-track support

**Grading Rubric (10 points total):**
- **Business Analysis (4 points)**:
  - 4 pts: Correctly identifies all 3 BMC components (Revenue Streams, Customer Relationships, Key Activities) with business impact
  - 3 pts: Identifies 2 components with impact
  - 2 pts: Identifies 1 component with impact
  - 0-1 pts: Incomplete or incorrect BMC analysis

- **Value Mapping (3 points)**:
  - 3 pts: Accurately maps Value Proposition and Customer Segment changes to technical features
  - 2 pts: Maps one dimension (VP or CS) to features
  - 1 pt: Mentions value/segment changes without technical mapping
  - 0 pts: No value mapping

- **Architectural Requirements (3 points)**:
  - 3 pts: Specifies all 3 systems with justified architecture decisions and trade-offs
  - 2 pts: Specifies 2 systems with justification
  - 1 pt: Lists requirements without justification
  - 0 pts: Missing or incorrect requirements

**Partial Credit**: Award proportional points for directionally correct but incomplete answers (e.g., 2.5 pts for identifying 2.5 BMC components).

**Alternative Frameworks**: Lean Canvas or Value Proposition Canvas also acceptable; adjust grading to map equivalent components.

**Self-Review Prompt:**
1. Does each business driver (Revenue Streams, Customer Relationships, Key Activities) map to a distinct architectural requirement?
2. Are all architecture decisions justified with trade-off analysis?
3. Are ≥3 citations included ([Ref: ID] format)?
4. Is the solution MECE (no overlapping requirements, all necessary requirements covered)?

**Validation Checkpoint:** ✓ Solution completeness, ✓ Business-to-architecture mapping, ✓ Citation coverage (3 citations), ✓ MECE reasoning

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
