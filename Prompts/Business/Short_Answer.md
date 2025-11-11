# Short Answer: Business-to-Architecture Translation

Generate 25–40 self-contained assessment problems mapping business requirements to architecture decisions for senior technical leaders.

---

**Context**: Generate 25–40 assessment problems for senior technical leaders evaluating business-to-architecture translation skills.

**Scope**: Each problem must include:
- Business scenario with explicit constraints, assumptions, stakeholder impact
- Architecture implications and trade-offs
- Expected answer, worked solution (2–4 MECE steps), grading rubric (10-point scale)
- Self-contained context (no external dependencies)

**Constraints**:
- Difficulty: 20% Foundational / 40% Intermediate / 40% Advanced
- Problem types: Business model analysis, value stream mapping, risk assessment, architecture justification, trade-off calculation
- Citations: ≥1 per solution using [Ref: ID] format
- Solution structure: MECE reasoning, explicit business-to-architecture mapping

**Assumptions**:
- Audience has domain expertise in software architecture, business strategy, organizational design
- Alternative frameworks acceptable (BMC vs. Lean Canvas, DDD vs. functional decomposition) if documented
- Partial credit awarded for directionally correct incomplete answers

**Success Criteria** (measurable):
- 100% problems have complete structure (scenario, answer, solution, rubric)
- ≥80% problems require explicit business-to-architecture translation
- ≥70% problems cite ≥1 source; ≥30% cite ≥2+ sources
- All citations meet language mix (50-70% EN, 20-40% ZH, 5-15% other), recency (≥50% last 3 years), diversity (≥3 types), accessibility (100% valid URLs)
- All 10 validation steps pass before delivery

**Grading Model** (10 points):
- Business Analysis: 4 pts (identify drivers, constraints, stakeholder impact)
- Value Mapping: 3 pts (translate to technical features/quality attributes)
- Architecture Decisions: 3 pts (justified choices with trade-off analysis)
- Partial credit: Proportional points for incomplete but correct answers

## Reference Requirements

| Section | Min | Format | Quality Criteria |
|---------|-----|--------|------------------|
| **Glossary** | 10 | **G#. Term**: Definition. Context. [Lang] | Define all domain terms (BMC, DDD, Conway's Law, Technical Debt, ADR, etc.) |
| **Tools** | 5 | **T#. Tool**: Purpose, tier, users, update, URL. [Lang] | Verify URLs; prioritize active tools (Miro, ArchiMate, C4, Confluence, LucidChart) |
| **Literature** | 6 | **L#. Author, Year, Title, Publisher.** Topics. | Seminal + recent works (Business Model Generation, DDD, Team Topologies, Microservices Patterns) |
| **APA Citations** | 12 | **A#. Full APA 7th citation. [Lang]** | Follow APA 7th; maintain language mix; verify accessibility |

**Citation Quality**:
- Language: 50-70% [EN], 20-40% [ZH], 5-15% other
- Recency: ≥50% last 3 years (≥70% for digital transformation/cloud-native/AI/ML)
- Diversity: ≥3 source types (business frameworks, architecture patterns, case studies, tools); no type >25%
- Credibility: Prioritize peer-reviewed research, established frameworks, authoritative practitioners
- Accessibility: 100% URLs accessible or archived (Internet Archive)
- Inline format: [Ref: G#/T#/L#/A#]

## Validation (Execute Before Delivery)

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | Count | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12; Problems 25-40 (20%/40%/40% difficulty) |
| 2 | Citation Coverage | ≥70% problems cite ≥1 source; ≥30% cite ≥2+ |
| 3 | Language Mix | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | Recency | ≥50% last 3 years (≥70% for fast-evolving domains) |
| 5 | Diversity | ≥3 source types; no type >25% |
| 6 | URL Access | 100% URLs valid or archived |
| 7 | Cross-Refs | All [Ref: ID] resolve to valid entries |
| 8 | Completeness | 100% problems have answer + solution + rubric |
| 9 | MECE Logic | 100% solutions show business-to-architecture mapping |
| 10 | Translation | ≥80% problems require explicit business → architecture mapping |

**Remediation**: If any check fails, document gap, fix, re-run failed + subsequent checks (max 3 cycles)

---

## Execution Steps

### 1. Plan (MECE Clusters)
Create 4–6 MECE problem clusters (4–8 problems each) addressing distinct business perspectives:
- Strategic Modeling: BMC analysis, value proposition, capability mapping
- Value & Risk: Value stream optimization, risk quantification, cost-benefit
- Organizational: Conway's Law, team topologies, boundaries
- Architecture Translation: Requirements → decisions, constraints, trade-offs
- Evolution: Technical debt, migration, architectural evolution
- Integration: System boundaries, context mapping, patterns

**Validate**: Total 25–40 problems; 20%/40%/40% difficulty; MECE coverage

### 2. Collect References
Build reference sections meeting minimum counts and quality criteria:
- **Glossary** (≥10): Define domain terms (BMC, DDD, Conway's Law, Technical Debt, ADR, etc.)
- **Tools** (≥5): Document tools with tier, users, URLs (Miro, ArchiMate, C4, Confluence, LucidChart)
- **Literature** (≥6): Include seminal + recent works (Business Model Generation, DDD, Team Topologies)
- **APA** (≥12): Follow APA 7th with language tags; maintain language mix

**Validate**: Language mix (50-70% EN, 20-40% ZH, 5-15% other), recency (≥50% last 3 years), diversity (≥3 types, no type >25%), accessibility (100% valid URLs)

### 3. Generate Problems (Batch of 5)
For each problem:
- **Statement** (2–4 sentences): Business scenario, stakeholders, constraints, assumptions, question
- **Expected Answer** (1–2 sentences/point): Concise key mappings
- **Worked Solution** (2–4 MECE steps): Show business-to-architecture translation; cite ≥1 source [Ref: ID]; include self-review for Intermediate/Advanced
- **Grading Rubric** (10 pts): Business Analysis (4), Value Mapping (3), Architecture Decisions (3); define partial credit

**Validate after each batch**: Complete structure, MECE reasoning, citations resolve, self-review included, ≥80% require business-to-architecture translation

### 4. Finalize References
- Populate all sections with consistent formatting
- Cross-validate: All [Ref: ID] resolve to valid entries (G#/T#/L#/A#)
- Test URLs; archive dead links (Internet Archive)
- Audit language mix, recency, diversity

### 5. Validate & Report
Execute 10-step validation checklist. If any step fails:
1. Document gap
2. Remediate
3. Re-run failed + subsequent steps (max 3 cycles)

Generate validation report:
```markdown
| Step | Item | Status | Notes |
|------|------|--------|-------|
| 1 | Count | PASS | Glossary: X, Tools: Y, Literature: Z, APA: W, Problems: N (F/I/A) |
| 2 | Citation Coverage | PASS | X% ≥1 citation; Y% ≥2 |
| 3 | Language Mix | PASS | EN: X%, ZH: Y%, Other: Z% |
| 4 | Recency | PASS | X% last 3 years |
| 5 | Diversity | PASS | X types; max Y% |
| 6 | URL Access | PASS | All valid/archived |
| 7 | Cross-Refs | PASS | All resolve |
| 8 | Completeness | PASS | All complete |
| 9 | MECE Logic | PASS | All map business-to-architecture |
| 10 | Translation | PASS | X% explicit mapping |
**Overall**: ✓ ALL PASS
```

---

## Output Format

**Structure**: TOC → Problem Bank (by topic clusters) → Reference Sections → Validation Report

**Formatting**:
- **TOC**: Anchor links to all sections and subsections
- **Lists**: Bullets (unordered), numbers (sequential)
- **Tables**: Comparisons, rubrics, references
- **Diagrams**: Mermaid (no styling/colors)
- **Code**: Fenced blocks with language tags
- **Formulas**: LaTeX syntax
- **Emphasis**: **bold** (key terms), *italics* (emphasis), `code` (technical terms)

**Template**:
```markdown
## Contents
1. [Problem Bank](#problem-bank)
   - [Topic 1: Strategic Modeling](#topic-1-strategic-modeling)
   - [Topic 2: Value & Risk Analysis](#topic-2-value--risk-analysis)
   - [Topic 3: Organizational Dynamics](#topic-3-organizational-dynamics)
   - [Topic 4: Architecture Translation](#topic-4-architecture-translation)
   - [Topic 5: Evolution & Adaptation](#topic-5-evolution--adaptation)
   - [Topic 6: Integration & Boundaries](#topic-6-integration--boundaries)
2. [Reference Sections](#reference-sections)
   - [Glossary](#glossary-terminology--acronyms)
   - [Tools](#business--architecture-tools)
   - [Literature](#authoritative-literature--case-studies)
   - [APA Citations](#apa-style-source-citations)
3. [Validation Report](#validation-report)
```

---

## Example Problem

**Problem**: SaaS company shifts from monthly to annual billing. Analyze Business Model Canvas impact and identify 3 architectural requirements. **[Intermediate]**

**Expected Answer**:
1. **BMC**: Revenue Streams (MRR→ARR), Customer Relationships (transactional→commitment), Key Activities (acquisition→retention)
2. **Architecture**: Subscription management (annual cycles, prorated changes), Revenue recognition (GAAP/IFRS deferred revenue), Customer success (health scoring, renewal prediction)

**Worked Solution**:

**Step 1 - BMC Analysis** [Ref: G1, A1]:
- **Revenue Streams**: MRR→ARR; cash flow predictability ↑ → deferred revenue system
- **Customer Relationships**: Transactional→commitment; CLV ↑, retention pressure ↑ → health scoring
- **Key Activities**: Transaction→retention; retention economics → usage monitoring, renewal prediction

**Step 2 - Value & Segment Mapping** [Ref: G2, G11]:
- **Value Prop**: Flexibility→cost savings+predictability → usage dashboards
- **Segment**: SMB→Enterprise → SSO, audit logs, SLA

**Step 3 - Architecture Translation** [Ref: A7, A10]:
1. **Subscription Management**: Event-sourced service; upgrades/downgrades, prorated refunds; trade-off: complexity vs. flexibility
2. **Revenue Recognition**: Separate billing/revenue domains [Ref: G3]; amortization, audit trails; trade-off: build vs. buy
3. **Customer Success**: Analytics pipeline; telemetry, renewal risk; integrations: CRM/support/analytics

**Step 4 - Risks** [Ref: G5]:
- Technical debt (rushed) → phased rollout, testing
- Data consistency (multi-system) → event-driven architecture
- Migration (existing customers) → gradual migration, dual-track

**Grading Rubric (10 pts)**:
- **Business Analysis (4)**: 4=all 3 BMC + impact; 3=2 components; 2=1 component; 0-1=incomplete
- **Value Mapping (3)**: 3=VP+segment→features; 2=one dimension; 1=mention only; 0=none
- **Architecture (3)**: 3=all 3 systems + justification; 2=2 systems; 1=list only; 0=missing
- **Partial credit**: Proportional for directionally correct answers
- **Alternatives**: Lean Canvas/VP Canvas acceptable (document in rubric)

**Self-Review**: Business driver → distinct requirement? Trade-offs justified? ≥3 citations? MECE?

---

## Terminology

**G1. Business Model Canvas (BMC)**: 9-block template mapping business to tech (Segments, Value Props, Channels, Relationships, Revenue, Resources, Activities, Partnerships, Costs). [EN]

**G2. Value Proposition**: Products/services creating customer value. Maps to features, quality attributes. [EN]

**G3. Domain-Driven Design (DDD)**: Domain modeling via expert collaboration. Defines microservices boundaries, team organization. [EN]

**G4. Conway's Law**: "Systems mirror organizational communication structure." Guides team topology, architecture alignment. [EN]

**G5. Technical Debt**: Rework cost from quick solutions. Drives refactoring prioritization, risk assessment. [EN]

**G6. Architecture Decision Records (ADR)**: Decision documentation (context, consequences, trade-offs). [EN]

**G7. Bounded Context**: DDD domain model boundaries. Enables microservices decomposition, team autonomy. [EN]

**G8. Capability Mapping**: Implementation-independent business capabilities. Strategic planning, gap analysis. [EN]

**G9. Living Documentation**: Auto-evolving system docs. Knowledge sharing, architectural understanding. [EN]

**G10. Wardley Mapping**: Strategic visualization by visibility/evolution. Decision-making, change anticipation. [EN]

**G11. Customer Segment**: Target groups. Maps to interfaces, workflows, data models. [EN]

**G12. Revenue Stream**: Income methods (subscription, usage, freemium). Impacts metering, billing, multi-tenancy. [EN]

**G13. Value Stream Mapping**: Lean delivery visualization. Identifies waste, bottlenecks. [EN]

**G14. System Boundaries**: Scope (in vs. out). Determines interfaces, integration. [EN]

**G15. Process Mapping**: Workflow visualization (activities, decisions, flows). Optimization, automation. [EN]

## Tools

**T1. Miro**: Visual collaboration (BMC, diagrams). Freemium-Enterprise. 80M+ users. Q4 2024. https://miro.com [EN]

**T2. ArchiMate**: Enterprise architecture (business/app/tech). ISO 42010. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model**: Hierarchical diagrams (Context, Container, Component, Code). Free. https://c4model.com [EN]

**T4. Confluence**: Documentation (ADRs, living docs). Free-Enterprise. 75K+ companies. Q3 2024. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart**: Cloud diagramming. Individual-Enterprise. 60M+ users. Q4 2024. https://www.lucidchart.com [EN]

## Literature

**L1. Osterwalder, A., & Pigneur, Y. (2010). *Business Model Generation*. Wiley.** BMC; business-tech alignment.

**L2. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** DDD patterns; domain modeling.

**L3. Vernon, V. (2013). *Implementing Domain-Driven Design*. Addison-Wesley.** Practical DDD; context mapping.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4), 28-31.** Conway's Law; organizational impact.

**L5. Skelton, M., & Pais, M. (2019). *Team Topologies*. IT Revolution Press.** Team patterns.

**L6. Richardson, C. (2018). *Microservices Patterns*. Manning.** Decomposition, patterns.

## APA Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). *Business model generation: A handbook for visionaries, game changers, and challengers*. Wiley. [EN]**

**A2. Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley. [EN]**

**A3. 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]**

**A4. Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley. [EN]**

**A5. Conway, M. E. (1968). How do committees invent? *Datamation*, 14(4), 28-31. [EN]**

**A6. Skelton, M., & Pais, M. (2019). *Team topologies: Organizing business and technology teams for fast flow*. IT Revolution Press. [EN]**

**A7. Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning. [EN]**

**A8. Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns*. Addison-Wesley. [EN]**

**A9. 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]**

**A10. Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley. [EN]**

**A11. Newman, S. (2021). *Building microservices* (2nd ed.). O'Reilly. [EN]**

**A12. 肖然. (2020). *企业级业务架构设计*. 机械工业出版社. [ZH]**

**A13. Brown, S. (2018). *Software architecture for developers* (Vol. 2). Leanpub. [EN]**

**A14. Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]**

**A15. Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution Press. [EN]**

**A16. Wardley, S. (2018). *Wardley maps: Topographical intelligence in business*. Medium. https://medium.com/wardleymaps [EN]**
