# Relationship Analysis Q&A Generator (Minimal Viable)

Generate **6-12 decision-critical relationship analysis Q&As** for informed architecture & team alignment decisions. Minimal viable template with time constraints: focus on coupling metrics, team structure alignment, and integration complexity that blocks decisions or creates material risk.

## Requirements

### Context & Scope
- **Domain**: Production-grade distributed systems (>10K rps, >1TB data, multi-team)
- **Audience**: Architect, Developer, DevOps/SRE, Leadership, PM (5 core roles)
- **Focus**: Decision-critical relationship analysis only (blocks architecture/team alignment decisions or creates material risk)
- **Effort**: 3-4h per generation cycle

**Core Principles**:
1. **Pareto Principle**: Focus on 20% of relationship patterns that drive 80% of architecture/team decisions
2. **Decision-First**: Every Q&A must block a decision or create material risk (coupling, team misalignment, integration bottleneck)
3. **Time-Constrained**: Minimal reference overhead, streamlined validation, 3-4h effort

### Output Specifications
- **Format**: 120-200 words, Mermaid diagrams, metrics tables, APA 7th [EN]/[ZH]
- **Quantity**: 6-12 Q&As; Difficulty: 25% F / 50% I / 25% A
- **Coverage**: 4 decision-critical dimensions × 3-4 lifecycle phases
  - **Dimensions**: Structural Coupling, Team Alignment (Conway's Law), Dependency Risk, Integration Complexity
  - **Phases**: Architecture & Design, Development, Deployment & Operations, Evolution & Governance
- **Traceability**: Scenario → Decision Criticality → Coupling Metrics → Decision
- **Per Q&A**: ≥1 diagram, ≥1 metrics table, quantified impact

### Content Standards
- **Precision**: Precise verbs (depends on, constrains, enables, aligns), quantified strength (coupling 0-1, Ca/Ce/Instability)
- **Credibility**: Industry case studies, academic papers; sources ≤3yr
- **Quantification**: All relationships must have metrics (coupling coefficient, team alignment score, MTTR impact, deployment frequency)
- **Concision**: 120-200w answers, diagrams/matrices over text

## Decision Criticality Framework (NEW)

**Include Q&A if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts architecture refactoring, team restructuring, or integration strategy
- **Creates Risk**: Material threat (coupling bottleneck, team misalignment, integration complexity blocking deployment)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (Architect + DevOps, Developer + Leadership, etc.)
- **Requires Action**: 1-6mo action window (not speculative)
- **Quantified Impact**: Coupling metrics (Ca/Ce/I), deployment frequency %, MTTR impact, team velocity %

**Exclude if**: Niche/legacy patterns, orthogonal/nice-to-have, already covered, speculative

## Decision-Critical Relationship Dimensions (4)

| Dimension | Decision Trigger | Example Scenario | Metrics |
|-----------|------------------|------------------|---------|
| **Structural Coupling** | Coupling >0.7 or Ca/Ce imbalance | Microservices: 50 services, avg Ce=8, I=0.8 (unstable). Refactor? | Ca, Ce, Instability I=Ce/(Ca+Ce) |
| **Team Alignment (Conway's Law)** | Team structure ≠ system architecture | 12 teams, 8 services. Misalignment → 40% slower deploys. Reorganize? | Team-service mapping, deployment frequency, MTTR |
| **Dependency Risk** | Critical path dependencies or circular deps | Payment **depends on** Stripe (external), 3 internal services. SLA risk? | Dependency depth, critical path, cycle detection |
| **Integration Complexity** | API coupling >10 or protocol mismatch | 20 microservices, 150+ API integrations. Contract testing coverage 60%. Improve? | API count, integration complexity, contract coverage % |

## Visuals & Metrics (Minimal Viable)

**Per Q&A**: ≥1 diagram (DSM/Dependency graph/Component diagram) + ≥1 metrics table (coupling/alignment/complexity quantified)

**Key Diagram Types**:
- **Structural Coupling**: DSM (Dependency Structure Matrix), Component diagram
- **Team Alignment**: Team-service mapping, org chart overlay
- **Dependency Risk**: Dependency graph, critical path diagram
- **Integration Complexity**: API diagram, contract testing matrix

## Q&A Design (Minimal Viable)

**Principles**: Decision-critical (blocks architecture/team decision), quantified (coupling metrics, team velocity impact), scenario-based (real-world system contexts)

**Example Q&A Candidates** (6-12 total):

| Dimension | Phase | Decision Trigger | Q&A Example |
|-----------|-------|------------------|------------|
| **Structural Coupling** | Architecture & Design | Coupling I >0.7 | Microservices: 50 services, avg Ce=8, I=0.8. Refactor to reduce coupling? [Blocks architecture decision] |
| **Team Alignment** | Development | Team-service mismatch | 12 teams, 8 services. Misalignment → 40% slower deploys. Reorganize teams? [Blocks org decision] |
| **Dependency Risk** | Deployment & Operations | Critical path or circular deps | Payment depends on Stripe (external). 3 internal services. SLA risk? [Creates risk] |
| **Integration Complexity** | Development | API coupling >10 or contract coverage <70% | 20 microservices, 150+ APIs. Contract testing 60%. Improve? [Blocks integration strategy] |

**Mandatory Elements per Q&A** (streamlined):
1. **Scenario context**: System scale, team structure, current state (quantified)
2. **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]
3. **Coupling metrics**: Ca, Ce, Instability, or team alignment score
4. **Precise verbs**: depends on, constrains, enables, aligns, couples to
5. **Visuals**: ≥1 diagram (DSM/dependency graph/team map) + ≥1 metrics table
6. **Trade-offs**: ≥2 alternatives with rationale
7. **Citation**: ≥1 [Ref: ID]

## Stakeholder Coverage (5 Core Roles)

| Role | Focus | Expected Detail |
|------|-------|-----------------|
| **Architect** | Coupling metrics, refactoring strategy, DSM analysis | Ca/Ce/Instability, dependency cycles, component boundaries |
| **Developer** | Code coupling, module dependencies, integration patterns | Dependency trees, coupling coefficients, interface design |
| **DevOps/SRE** | Team alignment, deployment frequency, MTTR impact | Team-service mapping, deployment pipeline, incident response |
| **Leadership** | Org structure, team velocity, strategic alignment | Conway's Law alignment, team productivity, roadmap impact |
| **PM** | Feature coupling, integration complexity, time-to-market | API dependencies, contract testing, release coordination |

## References & Quality (Minimal Viable)

### Reference Minimums (60% reduction)
- **≥12 Glossary**: Ca, Ce, Instability, Coupling, Cohesion, Cardinality, Dependency, Conway's Law, DSM, Team Alignment, Coupling Coefficient, Network Density
- **≥6 Tools**: Structurizr (C4), Lattix (DSM), Mermaid (diagrams), PlantUML (UML), Gephi (network), draw.io (architecture)
- **≥6 Literature**: Fowler (2003), Martin (2017), Newman (2010), Conway (1968), Evans (2003), Brown (2018)
- **≥8 Citations**: APA 7th [EN]/[ZH], all decision-critical, ≤3yr old

### Quality Checks

Use the **Validation Checks (12 streamlined)** section as the single source of truth for gates; all checks must PASS.

## Workflow

### 1. Plan & Build References First
**Topic Clusters**: 3–4 lifecycle phases, 6–12 Q&As, 25%/50%/25% F/I/A distribution
**References**: Glossary (≥12) → Tools (≥6) → Literature (≥6) → Citations (≥8). Use IDs: G#, T#, L#, A#. Verify: unique, recent (≥70% <5yr, ≥85% tools ≤18mo), diverse (≥5 types), accessible

### 2. Write Q&As
**Per answer**: 120–200 words, all mandatory elements from "Mandatory Elements per Q&A". **Check every 2–3**: verify checks, dimensions covered, 100% quantified, 100% precise verbs

### 3. Validate & Finalize
**Execute all 12 checks** (see Validation Checks table). **Verify**: 100% [Ref: ID] resolve, TOC/links valid, no redundancy

## Output Format

```markdown
## Contents
- [Lifecycle & Dimension Overview](#lifecycle--dimension-overview): 3–4 phases × 4 dimensions, 6–12 Q&As total
- [Q&A by Phase](#qa-by-phase): 6–12 decision-critical Q&As (120–200 words, mandatory elements)
- [References](#references): G# (≥12), T# (≥6), L# (≥6), A# (≥8)
- [Validation](#validation-checks-12-streamlined): 12 checks, all PASS

## Lifecycle & Dimension Overview

| Phase | Structural Coupling | Team Alignment | Dependency Risk | Integration Complexity | Q&A Count |
|-------|---------------------|----------------|-----------------|------------------------|-----------|
| Architecture & Design | ✓ | ✓ | ✓ | ✓ | 1–4 |
| Development | ✓ | ✓ | ✓ | ✓ | 1–4 |
| Deployment & Operations | ✓ | ✓ | ✓ | ✓ | 1–4 |
| Evolution & Governance | ✓ | ✓ | ✓ | ✓ | 1–4 |
| **Total** | **≥2** | **≥2** | **≥2** | **≥2** | **6–12** |

## Q&A by Phase

### Q1: [Relationship Scenario Question]
**Difficulty**: [F/I/A] | **Phase**: [Architecture/Development/Deployment/Evolution] | **Dimension**: [Structural Coupling / Team Alignment / Dependency Risk / Integration Complexity] | **Stakeholders**: [≥2 roles] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

**Answer** (120–200 words): [Scenario context, analysis with coupling metrics, stakeholder perspectives, decision and trade-offs, ≥1 citation]

**Visuals**: [Relationship diagram (DSM/dependency graph/team map/API diagram) + metrics table]
```

## References

### Glossary (≥12)
**G#. Term**: Definition. Formula/Quantification. Verbs. [EN/ZH]

**Examples**:
**G1. Decomposition**: Breaking whole into parts. System **decomposes into** subsystems → components → modules. Metrics: depth (4-7 levels), fan-out, leaf count. Verbs: decomposes into, partitions into. [EN]
**G2. Modularity**: High cohesion within, low coupling between. Q = (edges within / total) - random. Q>0.3 good. Metrics: LCOM 0-1, Ca, Ce. Verbs: modules within, boundaries between. [EN]
**G3. Afferent Coupling (Ca)**: Incoming dependencies. Ca = components that **depend on** this. High Ca (>10) = stable. Verbs: depends on, relies on. [EN]
**G4. Efferent Coupling (Ce)**: Outgoing dependencies. Ce = this **depends on** others. High Ce (>10) = unstable. Instability: I=Ce/(Ca+Ce), 0-1. I=0 stable, I=1 unstable. [EN]
**G5. Cardinality**: Numeric relationship between entities (ANY domain). 1:1, 1:N, M:N. Examples: Customer(1) **has** Order(N), Manager(1) **supervises** Employee(N), Platform(1) **connects** Seller(M)-Buyer(N). Crow's foot (ERD). Verbs: has, owns, connects, governs. [EN]

### Tools (≥6)
**T#. Name** (Category): Purpose. Types. Price. Updated. URL. [EN/ZH]

**Examples**:
**T1. Structurizr** (C4): Architecture diagrams. Structural, Dependency. $6-49/mo, Free OSS. 2024-10. https://structurizr.com [EN]
**T2. Lattix** (DSM): Dependency analysis. Coupling, Structural. $2000+/seat. 2024-09. https://lattix.com [EN]
**T3. PlantUML** (Diagrams): UML diagrams. Structural, Behavioral, Dependency. Free OSS. 2024-11. https://plantuml.com [EN]

### Literature (≥6)
**L#. Author(s). (Year). *Title*. Publisher.** Focus. [EN/ZH]

**Examples**:
**L1. Fowler, M. (2003). *UML Distilled*. Addison-Wesley.** UML relationships, diagrams. [EN]
**L2. Martin, R. C. (2017). *Clean Architecture*. Prentice Hall.** Coupling/cohesion, SOLID, boundaries. [EN]
**L3. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** Bounded contexts, aggregates, relationships. [EN]

### Citations (≥8)
**A#. Author. (Year). Title. Source. DOI/URL. [EN/ZH]**

**Examples**:
**A1. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4).** http://www.melconway.com/Home/Committees_Paper.html [EN]
**A2. Chen, P. P. (1976). "The Entity-Relationship Model." *ACM TODS*, 1(1), 9-36.** DOI: 10.1145/320434.320440 [EN]
**A3. Newman, M. E. J. (2010). *Networks*. Oxford.** Network analysis, centrality. ISBN: 978-0199206650 [EN]

### Validation Checks (12 streamlined)

| Check | Requirement | Pass Criteria |
|-------|-------------|---------------|
| **Q&A Count** | 6-12 total | Count = 6-12 |
| **Difficulty Mix** | 25% F / 50% I / 25% A | Distribution within ±5% |
| **Decision Criticality** | 100% satisfy ≥1 criterion | All Q&As have [Blocks/Risk/Roles/Action/Quantified] |
| **Dimensions Covered** | All 4 decision-critical | Structural, Team Alignment, Dependency, Integration |
| **Phases Covered** | ≥3-4 lifecycle phases | Architecture, Development, Deployment & Operations, Evolution |
| **Stakeholder Coverage** | ≥5 core roles | Architect, Developer, DevOps/SRE, Leadership, PM |
| **Coupling Metrics** | 100% quantified | All Q&As have Ca/Ce/I or team alignment score |
| **Visuals** | ≥1 diagram + ≥1 table per Q&A | DSM, dependency graph, team map, or API diagram |
| **Citations** | ≥75% have ≥1 cite, ≥50% ≤3yr | All decision-critical, APA 7th [EN]/[ZH] |
| **Word Count** | 120-200w per Q&A | Streamlined, no bloat |
| **References** | G≥12, T≥6, L≥6, A≥8 | Minimal viable, all used in Q&As |
| **Final Review** | No redundancy, clear traceability | Scenario → Criticality → Metrics → Decision |

## Example Q&A Format (Minimal Viable)

**Q: [Scenario + decision question]**
- **Difficulty**: [F/I/A]
- **Phase**: [Architecture/Development/Deployment & Operations/Evolution]
- **Dimension**: [Structural Coupling / Team Alignment / Dependency Risk / Integration Complexity]
- **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]

**Answer** (120-200 words):
1. **Scenario** (~25w): System context, scale, team structure, current state
2. **Analysis** (~50w): Coupling metrics, team alignment, deployment frequency impact
3. **Stakeholders** (~35w): ≥2 roles, their concerns, implications
4. **Decision** (~50w): Refactor/Align/Invest/Monitor + rationale + success criteria
5. **Trade-offs** (~20w): ≥2 alternatives with pros/cons

**Visuals**:
- **Diagram**: DSM, Dependency graph, Team-service map, or API diagram (Mermaid <80 nodes)
- **Metrics Table**: Component/Team, Metric (Ca/Ce/I or alignment %), Value, Threshold, Status

**Citation**: [Ref: ID] (≥1, ≤3yr old)
