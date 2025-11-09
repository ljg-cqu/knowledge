# Interview Q&A - Business Understanding for Software Architecture

Framework for generating high-quality interview question banks focused on comprehensive business understanding that benefits software architecture decisions.

---

# Part I: Specifications

## Scope and Content Principles

**Scope**: 25–30 Q&A pairs for senior/architect/expert-level technical leaders.

**Answer Length**: 150–300 words covering business-technical alignment, strategic trade-offs, value mapping, organizational constraints.

**Difficulty Distribution**: 20/40/40 balance (Foundational/Intermediate/Advanced).

**Content Principles**:

- **MECE Coverage**: Four dimensions (Strategic Modeling, Documentation, Visualization, Analysis) × Four perspectives (Strategic, Operational, Organizational, Architectural)
- **Analysis Required**: Value mapping (propositions → technical features), risk assessment (business/operational/regulatory), constraint analysis, evolution planning, business-technical mapping
- **Multi-Perspective**: Strategic (business model, market position), Operational (processes, capabilities), Organizational (structure, culture), Architectural (system design, technical debt)
- **Framework Handling**: Present competing frameworks (Business Model Canvas vs Lean Canvas, Value Stream vs Process Mapping); cite counter-evidence; acknowledge context (B2B vs B2C, enterprise vs startup, regulated vs unregulated)
- **Practitioner Clarity**: State field consensus vs disagreements; distinguish universal principles vs context-specific practices; trace architectural decisions to business value

## Evaluation Dimensions

Assess answers across four lenses:

- **Business**: Value propositions, revenue models, customer segments, market positioning, competitive dynamics
- **Strategic**: Business model evolution, growth adaptability, risk mitigation, regulatory landscape, investment priorities
- **Organizational**: Team structure, communication patterns, capability gaps, cultural alignment, change management
- **Architectural**: Business-technical mapping, constraint translation, flexibility requirements, scalability drivers, technical debt implications

## Terminology and ID Conventions

**Standard Terms**:

- **business-technical mapping**: Tracing business drivers to architectural decisions
- **topic**: Thematic grouping of 4–6 related Q&A pairs

**Reference ID Format**:

- **G#**: Glossary term (G1, G2, ...)
- **T#**: Tool (T1, T2, ...)
- **L#**: Literature (L1, L2, ...)
- **A#**: APA-style citation (A1, A2, ...)
- **In-text**: Use [G1], [T2], [L3], [A4] after claims

## Reference Requirements

| Category       | Min Count | Required Fields                                                                           | ID Prefix | Citation Rules                                                                                                                                                                                                                |
| -------------- | --------- | ----------------------------------------------------------------------------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Glossary**   | ≥10       | Term, definition, usage, related concepts, language tag                                   | G#        | Include BMC, Value Proposition, Customer Segment, DDD, Bounded Context, Conway's Law, Technical Debt, Capability Mapping, Living Documentation, ADR, Wardley Mapping, Value Stream Mapping, Revenue Stream, System Boundaries |
| **Tools**      | ≥5        | Name, purpose, pricing, adoption metrics, last update (≤18 months), key integrations, URL | T#        | Include business modeling (Miro), architecture visualization (ArchiMate, C4), documentation (Confluence), diagramming (LucidChart), strategic planning (Wardley Maps)                                                         |
| **Literature** | ≥6        | Author(s), year, title, publisher, language tag                                           | L#        | Include Osterwalder (Business Model), Evans/Vernon (DDD), Conway (organizational design), Hohpe (integration), Richardson (microservices) + ZH sources                                                                        |
| **Citations**  | ≥12       | APA 7th format with language tags                                                         | A#        | ~60% EN / ~30% ZH / ~10% other; ≥50% from last 3 years (≥70% for digital transformation/cloud-native)                                                                                                                         |

**Per Topic**: ≥2 authoritative sources + ≥1 tool reference.

**Quality Gates**:

- **Recency**: ≥50% citations from last 3 years (≥70% for digital transformation/cloud-native)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% answers have ≥1 citation; ≥30% have ≥2 citations
- **Links**: Validate accessibility; use DOIs/archived URLs
- **Cross-refs**: All [Ref: ID] resolve to entries

> **Scaling**: For >30 Q&A, increase floors by ~1.5×. Prioritize gates before raising floors.

## Visual Requirements

**Per Topic**: ≥1 primary diagram + ≥1 supporting table + ≥1 quantitative element.

**Rendering Standards**:

- **Diagrams**: Prefer Mermaid (GitHub-native); include captions and legends
- **Math**: Inline `$formula$` or block `$$formula$$`; define variables on first use
- **Common Symbols**: `∑` (sum), `∏` (product), `∫` (integral), `∂` (rate), `≈` (approx), `≤/≥` (bounds), `≠` (not equal), `∀` (for all)
- **Legends**: 💡 Analogy, 📐 Formula, 🔍 Example, ⚠️ Important Note

**Diagram Selection by Analysis Type**:

| Analysis Type                  | Primary Diagram                         | Standard        | Supporting Elements                               |
| ------------------------------ | --------------------------------------- | --------------- | ------------------------------------------------- |
| **Strategic Modeling**         | Business Model Canvas, Value Stream Map | BPMN, ArchiMate | ROI: `(Revenue - Investment) / Investment × 100%` |
| **Value & Risk Analysis**      | Risk matrix, Decision tree              | DMN             | Risk: `Probability × Impact × Exposure`           |
| **Documentation**              | C4 Context/Container, Component diagram | UML, C4         | Availability: `Uptime / Total Time × 100%`        |
| **Organizational**             | Team topology, Conway's Law map         | Custom          | Communication overhead metrics                    |
| **Business-Technical Mapping** | Value→Architecture mapping              | UML, DDD        | Debt: `Remediation Cost / Dev Cost × 100%`        |
| **Evolution**                  | Migration roadmap, Timeline             | Gantt           | NPV: `Σ(Cash Flow / (1 + r)^n) - Investment`      |

**Quick Reference by Need**:

| Need                | Diagram                                 | Standard    |
| ------------------- | --------------------------------------- | ----------- |
| API design          | Class + Sequence                        | UML         |
| Workflow logic      | Activity / Process                      | UML / BPMN  |
| Decision logic      | Decision Table + Requirements           | DMN / SysML |
| Business process    | Process / Collaboration (Pools & Lanes) | BPMN        |
| Database design     | ERD + Data Flow                         | ERD / DFD   |
| System architecture | Component + Deployment                  | UML         |
| Enterprise strategy | Strategy + Migration viewpoints         | ArchiMate   |

**Anti-patterns**: Single mega-diagram, BPMN for code flow, mixed abstraction levels, >120 nodes, missing rationale.

**Business Frameworks** (apply relevant combination):

- **Business Model Canvas**: 9-block analysis → architectural implications
- **Value Proposition**: Customer segments → technical requirements
- **SWOT/Porter's Five Forces**: Strategic positioning → architecture priorities
- **Lean Canvas**: Problem-solution fit → validation strategy

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Step 1: Topic Identification & Planning

1. Identify 5–6 topics aligned with framework: Strategic Modeling (Business Model, Domain) | Value & Risk Analysis | Documentation & Visualization | Organizational Dynamics | Business-Technical Mapping | Evolution & Adaptation
2. Allocate 4–6 Q&As per topic (total 25–30); assign 20/40/40 difficulty (F/I/A)
3. **Check**: Total = 25–30, ratio ≈20/40/40

## Step 2: Reference Collection

1. Gather resources per [Reference Requirements](#reference-requirements) table (Part I)
2. Assign IDs (G#/T#/L#/A#); tag language, year, type
3. **Check**: Meet all minimum counts, language distribution ~60/30/10%, recency ≥50% last 3yr, ≥3 types

## Step 3: Q&A Generation

1. Write scenario-based questions ("How would...", "When should..."); draft 150–300 word answers
2. Include ≥1 [Ref: ID] per answer; explicitly trace business value → architectural decisions
3. State concrete Key Insight (misalignment/constraint/value mapping failure/organizational impedance)
4. **Check**: Every 5 Q&As verify word counts, citations, business-technical mapping, judgment focus

## Step 4: Visual Artifacts

1. Per topic, create ≥3 elements: primary diagram + supporting table + quantitative formula
2. Follow [Visual Requirements](#visual-requirements) (Part I) for rendering standards
3. Apply relevant business frameworks (BMC, Value Prop, SWOT) with architectural mapping
4. **Check**: All topics covered; visuals align with analysis type (see Diagram Selection table in Part I)

## Step 5: References

1. Populate Glossary/Tools/Literature/APA with required fields (see [Reference Requirements](#reference-requirements) in Part I)
2. **Check**: All [Ref: ID] resolve

## Step 6: Validation

Execute all 15 steps from [Validation Checklist](#validation-checklist) (Part III). Fix failures; re-validate until all PASS.

## Step 7: Final Review

Apply critique criteria (Part III). Check submission checklist. Submit when all PASS.

---

# Part III: Output Format

## Question Design & Critique

**Implementation Approach** - Guide candidates through the transition framework:

1. **Value Mapping**: Identify value propositions → map to technical requirements → prioritize by business impact
2. **Risk Assessment**: Document business risks → evaluate operational constraints → consider regulatory requirements
3. **Organizational Factors**: Align with team structure → reflect communication patterns → account for future changes
4. **Business-Technical Mapping**: Show explicit connection from business drivers to architectural decisions

**Quality Criteria**:

- **Clarity**: Single unambiguous ask
  - ✅ "How would you translate a shift from one-time licensing to subscription revenue into architectural requirements?"
  - ❌ "Explain business models and microservices architecture"
- **Signal**: Tests business-technical mapping, not trivia
  - ✅ "Your CEO wants to enter a regulated market. How does this change your architecture strategy?"
  - ❌ "List the nine components of Business Model Canvas"
- **Depth**: Enables discussion of business constraints, value trade-offs, organizational impacts
  - ✅ "Choose: monolith refactor, strangler pattern, or greenfield rewrite for a company pivoting from B2B to B2C. How do you decide?"
  - ❌ "Should you use microservices? Yes/no"
- **Realism**: Scenarios matching senior/architect/expert roles bridging business and technology
  - ✅ "Sales promises real-time analytics to close a $10M deal. Engineering says it requires 6-month platform rebuild. How do you navigate this?"
  - ❌ "Design a payment system from scratch"
- **Discriminative**: Tests judgment over recall
  - ✅ "When does Conway's Law suggest organizational restructuring before technical refactoring?"
  - ❌ "What is Conway's Law?"

**Success Factors** - Answers should demonstrate:

- Maintaining current understanding (regular business review, prompt documentation updates, adaptive decisions)
- Clear communication (documented decisions, knowledge sharing, living documentation)
- Value alignment (trace decisions to business value, measure impact on value propositions, adjust based on feedback)

---

## Output Structure

```markdown
## Contents

- [Topic Areas](#topic-areas-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
  - [Q2: [Question text]](#q2-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q3: [Question text]](#q3-question-text)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Business & Architecture Tools](#business--architecture-tools)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Topic Areas: Questions 1-N

| Topic                                       | Question Range | Count  | Difficulty Mix   |
| ------------------------------------------- | -------------- | ------ | ---------------- |
| Strategic Modeling (Business Model, Domain) | Q1-Q5          | 5      | 1F, 2I, 2A       |
| Value & Risk Analysis                       | Q6-Q10         | 5      | 1F, 2I, 2A       |
| Documentation & Visualization               | Q11-Q15        | 5      | 1F, 2I, 2A       |
| Organizational Dynamics                     | Q16-Q20        | 5      | 1F, 2I, 2A       |
| Business-Technical Mapping                  | Q21-Q25        | 5      | 1F, 2I, 2A       |
| Evolution & Adaptation                      | Q26-Q30        | 5      | 1F, 2I, 2A       |
| **Total**                                   |                | **30** | **6F, 12I, 12A** |

**Legend**: F = Foundational, I = Intermediate, A = Advanced

---

## Topic 1: [Topic Title]

### Q1: [Question Text]

**Difficulty**: [Foundational/Intermediate/Advanced]  
**Type**: [Strategic Modeling/Value & Risk Analysis/Documentation & Visualization/Organizational Dynamics/Business-Technical Mapping/Evolution & Adaptation]

**Key Insight**: [One sentence stating specific business-technical misalignment/constraint trade-off/value mapping failure/organizational impedance this question exposes]

**Answer**:

[150-300 word answer with inline [Ref: ID] citations, explicitly connecting business drivers to architectural decisions]

**Supporting Artifacts** (Select 3+ matching analysis type):

| Artifact Type        | Examples                                                   | Key Formulas                                                                              |
| -------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| **Strategic**        | BMC, Value proposition map, Competitive matrix, Roadmap    | `ROI = (Revenue - Investment) / Investment × 100%`                                        |
| **Risk & Financial** | Risk matrix, Decision tree, Cost-benefit table, TCO        | `Risk = Probability × Impact × Exposure`<br>`NPV = Σ(Cash Flow / (1 + r)^n) - Investment` |
| **Technical**        | C4 diagrams, System boundary, Data flow, Component graph   | `Availability = (Total Time - Downtime) / Total Time × 100%`                              |
| **Organizational**   | Team topology, Communication map, Stakeholder diagram      | Conway's Law analysis, efficiency metrics                                                 |
| **Evolution**        | Migration roadmap, Timeline, Debt assessment, Impact table | `Debt Ratio = Remediation Cost / Dev Cost × 100%`                                         |

---

## Reference Sections

### Glossary, Terminology & Acronyms

**G1. Business Model Canvas (BMC)**  
Strategic management template with 9 building blocks: Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. Used for business model design, validation, innovation. Related: Lean Canvas, Value Proposition Canvas [EN]

**G2. Value Proposition**  
Bundle of products/services creating value for a specific customer segment; answers "why customers choose you." Maps to technical features and quality attributes. Used for product-market fit, differentiation, architecture prioritization. Related: Jobs-to-be-Done, Quality Attributes [EN]

**G3. Customer Segment**  
Distinct groups of people/organizations an enterprise aims to reach and serve, with common needs, behaviors, or attributes. Maps to system design decisions. Used for market targeting, personalization, resource allocation. Related: Persona, Market Segmentation, ICP [EN]

**G4. Domain-Driven Design (DDD)**  
Software development approach focusing on complex domain modeling through collaboration between technical and domain experts; emphasizes ubiquitous language, bounded contexts, aggregates. Used for complex business logic, microservices boundaries, team organization. Related: Event Storming, Context Mapping [EN]

**G5. Bounded Context**  
DDD pattern defining explicit boundaries within which a domain model is valid; different contexts can have different models of the same concept. Used for microservices decomposition, team autonomy, integration design. Related: Context Map, Anti-Corruption Layer [EN]

**G6. Conway's Law**  
"Organizations design systems that mirror their communication structure." Used for team topology design, architecture alignment, organizational change planning. Related: Inverse Conway Maneuver, Team Topologies [EN]

**G7. Technical Debt**  
Implied cost of additional rework caused by choosing quick/limited solutions now instead of better approaches; includes code debt, architectural debt, knowledge debt. Used for refactoring prioritization, risk assessment, investment planning. Related: Architectural Erosion, Entropy [EN]

**G8. Capability Mapping**  
Technique identifying and organizing business capabilities (what the business does) independent of how it's done; used for strategic planning, gap analysis, transformation roadmaps. Related: Business Capability Model, Value Stream Mapping [EN]

**G9. Living Documentation**  
Documentation that evolves with the system, stays current through automation and continuous updates; captures current state and evolution history. Used for knowledge sharing, onboarding, architectural understanding. Related: Documentation as Code, ADR [EN]

**G10. Architecture Decision Records (ADR)**  
Lightweight documentation capturing architectural decisions, context, consequences, and trade-offs; immutable log of choices made. Used for decision transparency, knowledge preservation, future reference. Related: Decision Log, Design Rationale [EN]

**G11. Wardley Mapping**  
Strategic planning technique visualizing components of a value chain positioned by visibility (y-axis) and evolution (x-axis). Used for strategic decision-making, identifying opportunities, anticipating change. Related: Value Chain Analysis, Strategic Positioning [EN]

**G12. Value Stream Mapping**  
Lean technique visualizing steps in delivering value to customers, identifying waste, bottlenecks, and improvement opportunities. Used for process optimization, lead time reduction, efficiency analysis. Related: Process Mapping, Flow Analysis [EN]

**G13. Revenue Stream**  
Ways an organization generates income from customer segments (e.g., one-time sale, subscription, usage-based, freemium, licensing). Directly impacts architectural requirements (metering, billing, multi-tenancy). Used for business model design, pricing strategy, technical planning. Related: Monetization Model, Pricing Strategy [EN]

**G14. System Boundaries**  
Explicit definition of what is inside vs outside the system scope; determines interfaces, integration points, and responsibilities. Used for context diagrams, scope management, interface design. Related: Context Diagram, Bounded Context, Integration Points [EN]

---

### Business & Architecture Tools

**T1. Miro** (Visual Collaboration & Business Modeling)  
Infinite canvas for BMC, Value Proposition Canvas, journey mapping, process flows, architecture diagrams. Freemium to Enterprise. 80M+ users (Dell, Cisco, Deloitte). Updated Q4 2024 (enhanced AI). Integrates: Jira, Slack, Teams, Zoom, Figma, Confluence. Use cases: Business model workshops, domain modeling, architecture design, stakeholder alignment. https://miro.com [EN]

**T2. ArchiMate** (Enterprise Architecture Modeling)  
Open standard for enterprise architecture modeling covering business, application, technology, motivation, implementation layers. Used with tools like Archi (free), Sparx EA, BiZZdesign. Supports capability mapping, process modeling, technology mapping. ISO/IEC/IEEE 42010 compliant. Use cases: Business-IT alignment, impact analysis, transformation planning. https://www.opengroup.org/archimate-forum [EN]

**T3. C4 Model** (Software Architecture Diagramming)  
Hierarchical set of diagrams (Context, Container, Component, Code) for visualizing software architecture at different abstraction levels. Free, tool-agnostic (Structurizr, PlantUML, Draw.io support). Created by Simon Brown. Use cases: Architecture documentation, stakeholder communication, onboarding. https://c4model.com [EN]

**T4. Confluence** (Documentation & Knowledge Management)  
Team workspace for documentation, decision records, architecture diagrams, process documentation. Free to Enterprise ($5.75-$11/user/mo). 75K+ companies (Spotify, LinkedIn). Updated Q3 2024 (AI-powered search, summaries). Integrates: Jira, Slack, Miro, Lucidchart, Draw.io. Use cases: ADRs, living documentation, business context sharing. https://www.atlassian.com/software/confluence [EN]

**T5. LucidChart** (Diagramming & Visual Communication)  
Cloud-based diagramming for flowcharts, process maps, org charts, architecture diagrams, ERDs. Individual ($7.95/mo) to Enterprise. 60M+ users (Google, GE, NBC). Updated Q4 2024 (AI diagram generation). Integrates: Google Workspace, Microsoft 365, Slack, Confluence, Jira. Use cases: Process mapping, capability modeling, architecture visualization, stakeholder presentations. https://www.lucidchart.com [EN]

---

### Authoritative Literature & Case Studies

**L1. Osterwalder, A., & Pigneur, Y. (2010). _Business Model Generation_. Wiley.**  
Business Model Canvas framework; 9 building blocks for designing, analyzing, innovating business models. Foundational for business-technical alignment.

**L2. Evans, E. (2003). _Domain-Driven Design: Tackling Complexity in the Heart of Software_. Addison-Wesley.**  
DDD patterns and practices; ubiquitous language, bounded contexts, strategic design. Core reference for domain modeling.

**L3. Vernon, V. (2013). _Implementing Domain-Driven Design_. Addison-Wesley.**  
Practical DDD implementation; context mapping, aggregates, event sourcing. Tactical patterns for complex domains.

**L4. Conway, M. E. (1968). "How Do Committees Invent?" _Datamation_, 14(4), 28-31.**  
Original Conway's Law paper; organizational structure impacts system design. Foundational for team topology.

**L5. Hohpe, G., & Woolf, B. (2003). _Enterprise Integration Patterns_. Addison-Wesley.**  
Integration patterns for distributed systems; messaging, routing, transformation. Reference for system integration.

**L6. Richardson, C. (2018). _Microservices Patterns_. Manning.**  
Microservices decomposition, data management, communication patterns. Practical architecture patterns.

---

### APA Style Source Citations

**A1. Osterwalder, A., & Pigneur, Y. (2010). _Business model generation: A handbook for visionaries, game changers, and challengers_. Wiley. [EN]**

**A2. Evans, E. (2003). _Domain-driven design: Tackling complexity in the heart of software_. Addison-Wesley Professional. [EN]**

**A3. 周爱民. (2021). _架构的本质_. 电子工业出版社. [ZH]**  
(Zhou, A. (2021). _The essence of architecture_. Publishing House of Electronics Industry.)

**A4. Vernon, V. (2013). _Implementing domain-driven design_. Addison-Wesley Professional. [EN]**

**A5. Conway, M. E. (1968). How do committees invent? _Datamation_, 14(4), 28-31. [EN]**

**A6. Hohpe, G., & Woolf, B. (2003). _Enterprise integration patterns: Designing, building, and deploying messaging solutions_. Addison-Wesley Professional. [EN]**

**A7. Richardson, C. (2018). _Microservices patterns: With examples in Java_. Manning Publications. [EN]**

**A8. Skelton, M., & Pais, M. (2019). _Team topologies: Organizing business and technology teams for fast flow_. IT Revolution Press. [EN]**

**A9. 张逸. (2019). _领域驱动设计实践_. 电子工业出版社. [ZH]**  
(Zhang, Y. (2019). _Domain-driven design in practice_. Publishing House of Electronics Industry.)

**A10. Fowler, M. (2002). _Patterns of enterprise application architecture_. Addison-Wesley Professional. [EN]**

**A11. Humble, J., & Farley, D. (2010). _Continuous delivery: Reliable software releases through build, test, and deployment automation_. Addison-Wesley Professional. [EN]**

**A12. Kim, G., Humble, J., Debois, P., & Willis, J. (2016). _The DevOps handbook: How to create world-class agility, reliability, and security in technology organizations_. IT Revolution Press. [EN]**

**A13. 肖然. (2020). _企业级业务架构设计_. 机械工业出版社. [ZH]**  
(Xiao, R. (2020). _Enterprise business architecture design_. China Machine Press.)

**A14. Wardley, S. (2018). _Wardley maps: Topographical intelligence in business_. Medium. https://medium.com/wardleymaps [EN]**

**A15. Brown, S. (2018). _Software architecture for developers_ (Vol. 2). Leanpub. [EN]**

**A16. Newman, S. (2021). _Building microservices: Designing fine-grained systems_ (2nd ed.). O'Reilly Media. [EN]**

---

## Validation Checklist

Execute ALL steps below. Present results in validation report table. Fix any failures and re-run validation until all checks pass.

**Step 1 – Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Q&As 25-30 (20/40/40)

**Step 2 – Citations**: ≥70% answers have ≥1; ≥30% have ≥2

**Step 3 – Language**: EN 50-70%, ZH 20-40%, Other 5-15%

**Step 4 – Recency**: ≥50% from last 3 years (≥70% for digital transformation/cloud-native)

**Step 5 – Diversity**: ≥3 source types; no single >25%

**Step 6 – Links**: All accessible or archived

**Step 7 – Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)

**Step 8 – Word Count**: Sample 5 answers; all 150-300 words

**Step 9 – Key Insights**: All concrete (business-technical misalignment/constraint trade-off/value mapping failure/organizational impedance)

**Step 10 – Per-Topic**: Each has ≥2 authoritative + ≥1 tool

**Step 11 – Business-Technical Mapping**: ≥80% of answers explicitly connect business drivers to architectural decisions with citations

**Step 12 – Judgment**: ≥70% scenario-based ("How would...", "When should...") vs recall ("What is...")

**Step 13 – Visual Element Coverage**: ≥90% of answers include primary diagram + supporting table + quantitative element

**Step 14 – Business Framework Application**: ≥80% answers apply relevant business frameworks (BMC, Value Prop, SWOT, etc.)

**Step 15 – Mathematical Analysis**: ≥60% answers include quantitative formulas or calculations where appropriate

**Validation Report Template:**

| Check                 | Result                           | Status    |
| --------------------- | -------------------------------- | --------- |
| Floors                | G:X T:Y L:Z A:W Q:N (F/I/A)      | PASS/FAIL |
| Citation coverage     | X% ≥1, Y% ≥2                     | PASS/FAIL |
| Language dist         | EN:X% ZH:Y% Other:Z%             | PASS/FAIL |
| Recency               | X% last 3yr                      | PASS/FAIL |
| Source diversity      | N types, max P%                  | PASS/FAIL |
| Links                 | Y/X accessible                   | PASS/FAIL |
| Cross-refs            | Y/X resolved                     | PASS/FAIL |
| Word counts           | 5/5 compliant                    | PASS/FAIL |
| Key Insights          | Y/X concrete                     | PASS/FAIL |
| Per-topic mins        | X/Y topics meet                  | PASS/FAIL |
| Biz-Tech mapping      | X/Y explicit                     | PASS/FAIL |
| Judgment vs Recall    | X% judgment-based                | PASS/FAIL |
| Visual coverage       | X% have diagram+table+formula    | PASS/FAIL |
| Framework application | X% apply biz frameworks          | PASS/FAIL |
| Mathematical analysis | X% include quantitative elements | PASS/FAIL |

> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate, and re-run validation. Only proceed when ALL checks show PASS.

## Submission Checklist

- [ ] All 15 validation steps PASS (see report table above)
- [ ] ALL reference floors met + quality gates passed

---

## Example Question

Demonstrates the transition framework: Business Understanding → Value/Risk Models → Architectural Decisions.

### Q1: How would you translate a company's shift from one-time perpetual licensing to subscription-based SaaS revenue into architectural requirements and constraints?

**Difficulty**: Advanced  
**Type**: Strategic Modeling, Business-Technical Mapping

**Key Insight**: Tests ability to trace business model changes through value/risk models to architectural decisions; distinguishes architects who systematically translate business drivers from those treating architecture as isolated technical concern.

**Answer**:

**Strategic Modeling** [G1]: Business Model Canvas analysis reveals Revenue Streams (upfront → recurring), Customer Relationships (transactional → continuous), Key Activities (+customer success/retention) [L1, A1].

**Value Model** [G2]: Value propositions shift to continuous delivery, uptime guarantees, feature velocity. Customer segments expand to multi-tier (freemium/pro/enterprise). Technical features required: real-time analytics, self-service onboarding, usage-based billing [A7].

**Risk Model**: Business risks (churn, downtime revenue impact), operational constraints (SLA commitments 99.9%+), regulatory requirements (data residency, SOC2/GDPR compliance) [A12, A13].

**Business-Technical Mapping** [A16]: (1) Multi-tenancy for cost efficiency with tenant isolation [L6]; (2) Usage metering via event streaming [A6]; (3) Feature flagging for tier management [A11]; (4) HA/DR for SLA compliance; (5) Regional deployment for data residency.

**Technical Debt** [G7]: Legacy assumptions (licensing checks, offline operation, customer-hosted) require migration strategy. Use Strangler pattern [A10] to extract multi-tenant services incrementally.

**Organizational Dynamics** [G6]: Conway's Law—add Customer Success, DevOps, SRE teams; architecture must enable their workflows [A8, L4]. Document decisions via ADR [G10].

**Supporting Artifact**:
```

Transition Framework: Business Understanding → Architectural Decisions

┌─────────────────────────────────────────────────────────────────────────┐
│ BUSINESS MODEL CANVAS CHANGES │
├─────────────────────────────────────────────────────────────────────────┤
│ Revenue Streams: Upfront → Recurring │
│ Customer Relationships: Transactional → Continuous │
│ Key Activities: +Customer Success, +Retention │
└─────────────────────────────────────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────────────────┐
│ VALUE MODEL │ RISK MODEL │
├────────────────────────────────┼────────────────────────────────────────┤
│ • Continuous delivery │ • Business: Churn, downtime revenue │
│ • Uptime guarantees │ • Operational: SLA 99.9%+ │
│ • Feature velocity │ • Regulatory: Data residency, SOC2 │
│ • Multi-tier segments │ │
└────────────────────────────────┴────────────────────────────────────────┘
↓
┌─────────────────────────────────────────────────────────────────────────┐
│ ARCHITECTURAL DECISIONS │
├──────────────────────────┬──────────────────────────┬──────────────────┤
│ Requirement │ Technical Solution │ Priority │
├──────────────────────────┼──────────────────────────┼──────────────────┤
│ Multi-tenant efficiency │ Tenant isolation, quotas │ Critical │
│ Usage metering │ Event streaming │ High │
│ Tier management │ Feature flags │ High │
│ SLA compliance │ HA/DR, monitoring │ Critical │
│ Data residency │ Regional deployment │ High │
│ Continuous delivery │ CI/CD, blue-green │ High │
└──────────────────────────┴──────────────────────────┴──────────────────┘

Evolution Strategy (Strangler Pattern):
Phase 1 (M1-3): Multi-tenancy foundation, basic metering
Phase 2 (M4-6): Feature flags, CI/CD pipeline  
Phase 3 (M7-9): HA/DR, regional deployment
Phase 4 (M10-12): Analytics, customer success integrations

```

---
```
