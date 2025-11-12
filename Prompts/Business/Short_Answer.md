# Short Answer: Business-to-Architecture Translation

Generate 25–40 assessment problems mapping business requirements to architecture decisions for senior technical leaders.

---

## Task Definition

**Audience**: Senior technical leaders (software architecture, business strategy, organizational design expertise)

**Deliverable**: 25–40 problems (20% Foundational / 40% Intermediate / 40% Advanced)

**Structure per Problem**:
- Business scenario (constraints, assumptions, stakeholder impact)
- Expected answer (1–2 sentences/point)
- Worked solution (2–4 MECE steps, ≥1 [Ref: ID] citation)
- Grading rubric (10pts: Business 4, Value 3, Architecture 3)

**Types**: Business model analysis, value stream mapping, risk assessment, architecture justification, trade-off calculation

**Assumptions**: Alternative frameworks acceptable if documented; partial credit for directionally correct answers

**Success Criteria**:
- 100% complete structure; ≥80% require business-to-architecture translation
- Citations: ≥70% problems ≥1 source, ≥30% problems ≥2+ sources
- Citation quality: 50-70% EN, 20-40% ZH, 5-15% other; ≥50% last 3yr; ≥3 types; 100% valid URLs
- All 10 validation checks pass

## Reference Requirements

| Section | Min | Format | Criteria |
|---------|-----|--------|----------|
| **Glossary** | 10 | **G#. Term**: Definition. [Lang] | Domain terms (BMC, DDD, Conway's Law, ADR, etc.) |
| **Tools** | 5 | **T#. Tool**: Purpose, tier, users, update, URL. [Lang] | Active tools (Miro, ArchiMate, C4, Confluence, LucidChart) |
| **Literature** | 6 | **L#. Author, Year, Title, Publisher.** Topics. | Seminal + recent (Business Model Generation, DDD, Team Topologies) |
| **APA** | 12 | **A#. Full APA 7th. [Lang]** | APA 7th; language mix; verified URLs |

**Citation Quality**: EN 50-70%, ZH 20-40%, other 5-15%; ≥50% last 3yr (≥70% for fast-evolving); ≥3 types, no type >25%; prioritize peer-reviewed/authoritative; 100% accessible URLs

## Validation (Execute Before Delivery)

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | Count | Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12; Problems 25-40 (20%/40%/40%) |
| 2 | Citation Coverage | ≥70% problems ≥1 source; ≥30% ≥2+ |
| 3 | Language Mix | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | Recency | ≥50% last 3yr (≥70% fast-evolving) |
| 5 | Diversity | ≥3 types; no type >25% |
| 6 | URL Access | 100% valid/archived |
| 7 | Cross-Refs | All [Ref: ID] resolve |
| 8 | Completeness | 100% have answer + solution + rubric |
| 9 | MECE Logic | 100% show business-to-architecture mapping |
| 10 | Translation | ≥80% require explicit business → architecture mapping |

**Remediation**: Document gap, fix, re-run failed + subsequent checks (max 3 cycles)

---

## Execution Steps

### 1. Plan (MECE Clusters)
Create 4–6 clusters (4–8 problems each):
- **Strategic Modeling**: BMC, value proposition, capability mapping
- **Value & Risk**: Value stream, risk quantification, cost-benefit
- **Organizational**: Conway's Law, team topologies, boundaries
- **Architecture Translation**: Requirements → decisions, constraints, trade-offs
- **Evolution**: Technical debt, migration, evolution
- **Integration**: System boundaries, context mapping, patterns

**Validate**: 25–40 total; 20%/40%/40% difficulty; MECE coverage

### 2. Collect References
Build sections meeting minimums and quality criteria:
- **Glossary** (≥10): Domain terms
- **Tools** (≥5): Tools with tier, users, URLs
- **Literature** (≥6): Seminal + recent works
- **APA** (≥12): APA 7th with language tags

**Validate**: Language mix, recency, diversity, URL accessibility

### 3. Generate Problems (Batch of 5)
Per problem:
- **Statement** (2–4 sentences): Scenario, stakeholders, constraints, assumptions, question
- **Expected Answer** (1–2 sentences/point): Key mappings
- **Worked Solution** (2–4 MECE steps): Business-to-architecture translation; ≥1 [Ref: ID]; self-review for Intermediate/Advanced
- **Grading Rubric** (10pts): Business (4), Value (3), Architecture (3); partial credit defined

**Validate after each batch**: Complete structure, MECE reasoning, citations resolve, self-review, ≥80% require translation

### 4. Finalize References
- Populate with consistent formatting
- Cross-validate: All [Ref: ID] resolve
- Test URLs; archive dead links
- Audit language mix, recency, diversity

### 5. Validate & Report
Execute 10-step checklist. If failed: document, remediate, re-run (max 3 cycles)

Report format:
```markdown
| Step | Item | Status | Notes |
|------|------|--------|-------|
| 1 | Count | PASS | Glossary: X, Tools: Y, Literature: Z, APA: W, Problems: N (F/I/A) |
| 2 | Citation Coverage | PASS | X% ≥1; Y% ≥2 |
| 3 | Language Mix | PASS | EN: X%, ZH: Y%, Other: Z% |
| 4 | Recency | PASS | X% last 3yr |
| 5 | Diversity | PASS | X types; max Y% |
| 6 | URL Access | PASS | All valid/archived |
| 7 | Cross-Refs | PASS | All resolve |
| 8 | Completeness | PASS | All complete |
| 9 | MECE Logic | PASS | All map |
| 10 | Translation | PASS | X% explicit |
**Overall**: ✓ ALL PASS
```

---

## Output Format

**Structure**: TOC → Problem Bank (by clusters) → References → Validation Report

**Formatting**: TOC (anchor links), lists (bullets/numbers), tables, Mermaid diagrams (no styling), fenced code blocks, LaTeX formulas, **bold** (key terms), *italics* (emphasis), `code` (technical)

**Template**:
```markdown
## Contents
1. [Problem Bank](#problem-bank)
   - [Strategic Modeling](#topic-1-strategic-modeling)
   - [Value & Risk](#topic-2-value--risk-analysis)
   - [Organizational](#topic-3-organizational-dynamics)
   - [Architecture Translation](#topic-4-architecture-translation)
   - [Evolution](#topic-5-evolution--adaptation)
   - [Integration](#topic-6-integration--boundaries)
2. [References](#reference-sections)
   - [Glossary](#glossary-terminology--acronyms)
   - [Tools](#business--architecture-tools)
   - [Literature](#authoritative-literature--case-studies)
   - [APA](#apa-style-source-citations)
3. [Validation](#validation-report)
```

---

## Example Problem

**Problem**: SaaS shifts monthly to annual billing. Analyze BMC impact, identify 3 architectural requirements. **[Intermediate]**

**Expected Answer**:
1. **BMC**: Revenue Streams (MRR→ARR), Customer Relationships (transactional→commitment), Key Activities (acquisition→retention)
2. **Architecture**: Subscription management (annual cycles, prorated changes), Revenue recognition (deferred revenue), Customer success (health scoring, renewal prediction)

**Worked Solution**:

**Step 1 - BMC Analysis** [Ref: G1, A1]:
- **Revenue Streams**: MRR→ARR; cash predictability ↑ → deferred revenue system
- **Customer Relationships**: Transactional→commitment; CLV ↑, retention pressure ↑ → health scoring
- **Key Activities**: Transaction→retention; retention economics → usage monitoring, renewal prediction

**Step 2 - Value & Segment** [Ref: G2, G11]:
- **Value Prop**: Flexibility→cost savings+predictability → usage dashboards
- **Segment**: SMB→Enterprise → SSO, audit logs, SLA

**Step 3 - Architecture** [Ref: A7, A10]:
1. **Subscription**: Event-sourced service; upgrades/downgrades, prorated refunds; trade-off: complexity vs. flexibility
2. **Revenue Recognition**: Separate billing/revenue domains [Ref: G3]; amortization, audit trails; trade-off: build vs. buy
3. **Customer Success**: Analytics pipeline; telemetry, renewal risk; integrations: CRM/support/analytics

**Step 4 - Risks** [Ref: G5]:
- Technical debt (rushed) → phased rollout
- Data consistency (multi-system) → event-driven
- Migration (existing customers) → gradual, dual-track

**Grading Rubric (10pts)**:
- **Business (4)**: 4=all 3 BMC + impact; 3=2 components; 2=1 component; 0-1=incomplete
- **Value (3)**: 3=VP+segment→features; 2=one dimension; 1=mention; 0=none
- **Architecture (3)**: 3=all 3 systems + justification; 2=2 systems; 1=list only; 0=missing
- **Partial**: Proportional for directionally correct
- **Alternatives**: Lean Canvas/VP Canvas acceptable (document)

**Self-Review**: Business → distinct requirement? Trade-offs justified? ≥3 citations? MECE?

---

## Terminology

**G1. Business Model Canvas (BMC)**: 9-block business template (Segments, Value Props, Channels, Relationships, Revenue, Resources, Activities, Partnerships, Costs). [EN]

**G2. Value Proposition**: Products/services creating customer value. Maps to features, quality attributes. [EN]

**G3. Domain-Driven Design (DDD)**: Domain modeling via expert collaboration. Defines boundaries, team organization. [EN]

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
