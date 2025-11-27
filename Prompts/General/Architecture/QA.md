# Architecture Assessment Q&A Generator (Universal)

**Problem**: Professionals struggle translating architectural/strategic concepts to practical implementation across domains, reducing assessment quality due to theory-practice gaps (↓30-40%).

**Scope**: 5 Q&A pairs for senior/architect roles (5-15 years experience), concept-to-implementation translation across industries (technology, healthcare, manufacturing, education, business operations, public sector, etc.).

**Constraints**: Domain-appropriate formats (diagrams, workflows, specifications, protocols, blueprints, models); 150-300 words/answer; concrete examples with 10-30 lines/steps.

**Assumptions**: Familiarity with domain-specific architectural frameworks, standards, and best practices.

**Scale**: 1-5 candidates/session, 10-15min/question.

**Timeline**: 45-60min assessment; immediate use.

**Stakeholders**: Hiring managers, senior practitioners, architects, domain experts, team leads, operations managers, strategic planners.

**Output**: 5 Q&As across 5 dimensions with practical examples, quantified trade-offs, ≥2 alternatives, ≥1 citation each.

**Success**: All validation checks pass (≥6 citations, ≥3 tools/frameworks/methodologies, ≥3 literature, ≥5 glossary).

**Decision-Criticality** (Include if ≥1 criterion satisfied):
- **Blocks Decision**: Impacts architectural choice, resource allocation, or strategic direction
- **Creates Risk**: Material threat (capacity limits, safety concerns, sustainability issues, compliance gaps)
- **Affects ≥2 Stakeholder Roles**: Multi-team impact (Designer + Implementer, Operations + Quality Assurance, Clinical + Administrative, Production + Quality Control)
- **Requires Action**: 1-6mo implementation window (not theoretical)
- **Quantified Impact**: Measurable metrics (efficiency %, cost $, complexity score, time saved, quality improvement, safety incidents, throughput, outcomes)

---

## Cross-Domain Applicability

This framework applies universally by mapping the 5 dimensions to any domain:

| Dimension | Software | Healthcare | Manufacturing | Education | Business Ops |
|-----------|----------|------------|---------------|-----------|--------------|
| **Structural** | Microservices, layers | Care teams, facilities | Production cells, lines | Curriculum units, programs | Org units, divisions |
| **Behavioral** | API calls, events | Patient pathways, handoffs | Assembly sequences, flows | Learning activities, assessments | Business processes, approvals |
| **Quality** | Performance, security | Patient safety, outcomes | Defect rates, yield | Learning outcomes, retention | Service levels, compliance |
| **Resources** | Compute, storage | Staff, beds, equipment | Machines, materials, labor | Teachers, classrooms, time | Budget, people, capacity |
| **Integration** | APIs, messaging | Referrals, care coordination | Supply chain, logistics | Interdisciplinary learning | Cross-functional collaboration |

**Key Principle**: Focus on *concepts* (decomposition, orchestration, optimization) rather than *artifacts* (code, protocols, blueprints). The underlying architectural thinking remains constant; only the expression changes.

---

## Requirements

### Specifications
- **Count**: 5 (1 per dimension)
- **Difficulty**: 20% F (Foundational) / 40% I (Intermediate) / 40% A (Advanced) — **F**=execution-level, **I**=strategy/trade-offs, **A**=portfolio/vision
- **Answer Length**: 150-300 words (examples excluded)
- **Components**: Framework/pattern, rationale, practical example, trade-offs, metrics
- **Citations**: ≥1 each; ≥2 for Advanced

### Dimensions (5, 1 Q&A Each)
1. **Structural**: Organization, decomposition, modularity (hierarchies, divisions, boundaries, relationships, layering)
2. **Behavioral**: Processes, workflows, orchestration (sequences, dependencies, controls, interactions, flows)
3. **Quality**: Performance, reliability, sustainability (standards, safeguards, optimization, assurance, resilience)
4. **Resources**: Allocation, management, optimization (capacity, utilization, constraints, planning, distribution)
5. **Integration**: Communication, coordination, interoperability (protocols, interfaces, handoffs, alignment, synchronization)

### Standards
- **Trade-offs**: Quantified with domain-appropriate metrics, e.g., 
  - Technical: "Centralized architecture: 50% faster decisions, +30% coordination overhead"
  - Operations: "Hub-and-spoke model: 40% reduced transport costs, +25% hub congestion"
  - Healthcare: "Integrated care team: 35% better outcomes, +20% coordination time"
  - Manufacturing: "Parallel production lines: 2x throughput, +40% complexity, +15% floor space"
- **Perspectives**: ≥2 alternatives with table; assumptions/limitations; tags `[Consensus]`/`[Context-dependent]`
- **Language**: Define domain-specific terms; concrete metrics; minimal jargon; translate technical concepts to business value

### Artifacts
- **Diagram**: Visual representation (<120 elements) using domain-appropriate format (flowcharts, org charts, process maps, network diagrams, facility layouts, value stream maps, concept maps, system diagrams, blueprints)
- **Example**: 10-30 steps/lines, implementation-ready (workflow, specification, procedure, protocol, policy, guideline, checklist, standard operating procedure)
- **Table**: ≥2 alternatives (Approach/Pros/Cons/Use When/Consensus)
- **Metric**: Formula + variables + target (quantified performance indicators)

### References
- **Glossary**: ≥5 domain-specific terms (technical vocabulary, industry acronyms, specialized concepts)
- **Tools/Frameworks/Methodologies**: ≥3 (valid references, recent updates)
  - Examples: TOGAF, Six Sigma, Lean, ITIL, Balanced Scorecard, Design Thinking, Agile, PMBOK, ISO standards, clinical guidelines
- **Literature**: ≥3 authoritative sources (academic research, industry publications, standards bodies, professional associations, seminal books)
- **Citations**: ≥6 APA 7th, ≥2 domains/perspectives (cross-disciplinary when applicable)

---

## Process

1. **Identify Domain Context**: Determine the industry/field and adapt terminology accordingly
2. **Select 5 Dimensions**: Choose one question per dimension with 20/40/40 difficulty mix (F/I/A)
3. **Build References**: Gather domain-appropriate tools/frameworks/methodologies, literature, and terms meeting thresholds
4. **Write Q&As**: Develop questions with required components (framework, rationale, example, trade-offs, metrics)
5. **Create Artifacts**: Generate domain-appropriate diagrams, implementations, tables, and metrics per dimension
6. **Validate**: Check counts, citations, recency, links, and domain relevance
7. **Refine**: Ensure terminology is domain-appropriate and examples are practical/recognizable

**Failure**: Fix validation issues and re-validate until all checks pass

---

## Output Template

```markdown
## Contents
[TOC]

## Topic Areas
| Dimension | Count | Difficulty |
| [Type] | 1 | F/A |
[5 total]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [Question]
**Difficulty**: [F/A] | **Dimension**: [Type]

**Key Insight**: [Quantified trade-off]

**Answer**: [150-300 words: Context, framework/pattern, trade-offs, metrics] [Citation]

**Implementation** ([Format]):
```[format]
[Practical example: workflow steps, specification, protocol, procedure, policy, guideline, SOP, checklist]
[Domain-specific: code for software, clinical pathway for healthcare, production schedule for manufacturing, lesson plan for education]
```

**Diagram**:
```mermaid
[Visual representation appropriate to domain]
[flowchart: processes/workflows | sequence: interactions/handoffs | organization: structures/hierarchies | network: connections/relationships]
[value stream map: manufacturing | care pathway: healthcare | service blueprint: customer experience | data flow: information systems]
```

**Metrics**:
| Metric | Formula | Variables | Target |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Consensus |
[≥2 rows]

---

## References

### Glossary (≥5)
**G1. [Term]** – [Definition]. Related: [Terms]

### Tools/Frameworks/Methodologies (≥3)
**T1. [Tool/Framework/Methodology]** – [Purpose/Application]. Domain: [Industry/Field]. Updated: [Date]. Reference: [Link/Source]

### Literature (≥3)
**L1. Author. (Year). *Title*.** – [Relevance to domain]

### Citations (≥6)
**A1.** Author. (Year). *Title*. [Domain/Discipline]

---

## Validation
| Check | Target | Status |
| Counts | G≥5, T≥3, L≥3, A≥6, Q=5 | PASS/FAIL |

**Overall**: [Pass rate]
```

## Limitations
- **Trade-offs**: Rigor vs. speed in assessment; depth vs. breadth of coverage
- **Skip for**: Low-stakes decisions, entry-level roles, routine implementations, purely operational tasks
- **Exclude**: Pure theory without practical application, speculation, domain-irrelevant patterns, trendy buzzwords without substance

## Domain Adaptation Guidelines
When applying this framework to specific domains:
1. **Terminology**: Replace technical jargon with domain-appropriate language (e.g., "components" → "care teams" in healthcare, "modules" → "departments" in organizational design)
2. **Metrics**: Use industry-standard KPIs (e.g., uptime % for IT, patient outcomes for healthcare, yield % for manufacturing, student retention for education)
3. **Standards**: Reference domain-specific frameworks (e.g., ISO standards, clinical guidelines, industry best practices, regulatory requirements)
4. **Artifacts**: Choose visualization formats familiar to the domain (e.g., BPMN for business processes, clinical pathways for healthcare, Gantt charts for project management)
5. **Examples**: Draw from recognizable scenarios within the domain to ensure practical relevance and immediate applicability

## Application Domains
This framework adapts to various contexts with domain-specific terminology and examples:

### Technology & Engineering
- **Software/Systems**: Architecture patterns, microservices design, API design, database schemas, deployment pipelines
- **Infrastructure**: Network topology, data center design, cloud architecture, disaster recovery, security frameworks
- **Product Design**: Design systems, user experience architecture, interaction patterns, information architecture

### Business & Operations
- **Organizational Design**: Reporting structures, span of control, departmental boundaries, governance models, decision rights
- **Process Management**: Business process optimization, value stream mapping, workflow automation, lean operations
- **Strategic Planning**: Portfolio management, capability models, operating models, transformation roadmaps

### Healthcare & Life Sciences
- **Clinical Operations**: Patient care pathways, clinical protocols, interdisciplinary coordination, handoff procedures
- **Healthcare Delivery**: Care delivery models, referral networks, population health systems, telehealth frameworks
- **Research**: Clinical trial design, laboratory workflows, research protocols, data management

### Manufacturing & Supply Chain
- **Production Systems**: Assembly line design, cellular manufacturing, batch processing, quality gates, production scheduling
- **Supply Chain**: Distribution networks, logistics operations, inventory systems, supplier integration, demand planning
- **Quality Management**: Inspection protocols, statistical process control, continuous improvement, root cause analysis

### Education & Training
- **Curriculum Design**: Learning pathways, competency frameworks, assessment systems, pedagogical models
- **Institutional Organization**: Academic structures, program design, student services, faculty governance
- **Learning Systems**: Educational technology architecture, content delivery, learner engagement, outcomes tracking

### Public Sector & Government
- **Service Delivery**: Citizen service models, program administration, benefits systems, multi-agency coordination
- **Policy Implementation**: Regulatory frameworks, compliance systems, enforcement mechanisms, stakeholder engagement
- **Infrastructure**: Public works planning, emergency management, resource allocation, community services

### Financial Services
- **Risk Management**: Risk frameworks, control systems, audit processes, compliance monitoring
- **Operations**: Transaction processing, settlement systems, reconciliation workflows, fraud detection
- **Service Architecture**: Branch networks, digital channels, customer journeys, product portfolios

### Retail & Hospitality
- **Store Operations**: Layout design, merchandising systems, inventory management, customer flow, point-of-sale
- **Supply Chain**: Distribution centers, replenishment systems, vendor management, logistics networks
- **Customer Experience**: Service design, touchpoint orchestration, loyalty programs, personalization

### Construction & Real Estate
- **Project Delivery**: Construction methodologies (IPD, Design-Build), phase gates, stakeholder coordination
- **Facility Management**: Space planning, maintenance systems, energy management, occupancy optimization
- **Development**: Master planning, zoning strategies, infrastructure coordination, phasing approaches

### Non-Profit & Social Services
- **Program Design**: Service delivery models, beneficiary pathways, impact frameworks, partnership structures
- **Resource Allocation**: Funding distribution, volunteer coordination, capacity building, grant management
- **Community Engagement**: Outreach strategies, stakeholder participation, feedback mechanisms, coalition building

