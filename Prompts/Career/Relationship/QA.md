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
- **Coverage**: 3-4 decision-critical dimensions × 3-4 lifecycle phases
  - **Dimensions**: Structural Coupling, Team Alignment (Conway's Law), Dependency Risk, Integration Complexity
  - **Phases**: Architecture & Design, Development, Deployment & Operations, Evolution & Governance
- **Traceability**: News → Decision Criticality → Coupling Metrics → Action
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

| Dimension | Decision Trigger | Example News | Metrics |
|-----------|------------------|--------------|---------|
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
| **Dependency Risk** | Deployment & Ops | Critical path or circular deps | Payment depends on Stripe (external). 3 internal services. SLA risk? [Creates risk] |
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

### Quality Gates (all must PASS)

| Gate | Requirement | Validation Method |
|------|-------------|-------------------|
| **Lifecycle Coverage** | All 8 phases covered with ≥3 Q&As each | Count by phase |
| **Stakeholder Coverage** | ≥8/10 roles covered with ≥2 Q&As each | Count by role |
| **Relationship Type Coverage** | All 7 relationship types covered with ≥4 Q&As each (Structural, Behavioral/Temporal, Dependency/Coupling, Business/Market, Regulatory/Compliance, Integration/Interface, Emergent/Network) | Count by type |
| **Difficulty Distribution** | 20/40/40 (F/I/A) ±5% | Count by level |
| **Relationship Network Depth** | 100% Q&As map ≥3-level relationship networks (Component → Direct relationships → Transitive relationships → Network effects) | Review all |
| **Quantified Relationships** | 100% Q&As have quantified relationship metrics (coupling 0-1, cardinality 1:1/1:N/M:N, Ca/Ce/Instability, centrality scores) | Review all |
| **Multi-Type Relationship Analysis** | ≥70% Q&As analyze ≥3 relationship types (e.g., structural + dependency + business) with interaction analysis | Review advanced Q&As |
| **Precise Relationship Verbs** | 100% Q&As use precise relationship verbs (depends on, composes, inherits from, mandates, exposes, enables, constrains, etc.) | Review all |
| **Bi-directional Relationships** | ≥50% Q&As identify bi-directional relationships (A→B and B→A with different semantics) | Review intermediate/advanced |
| **Trade-offs & Alternatives** | 100% Q&As acknowledge relationship trade-offs (tight vs loose coupling, direct vs mediated, hierarchical vs flat) | Review all |
| **Visual Relationship Diagrams** | 100% Q&As include ≥1 relationship diagram (class/component/ERD/network/DSM matrix) | Count diagrams |
| **Citation Quality** | ≥75% answers ≥1 cite, ≥40% ≥2 cites, ≥25% industry standards (UML, ArchiMate, TOGAF) | Count per answer |
| **Cross-refs** | 100% [Ref: ID] resolve | Automated check |
| **Recency** | ≥70% sources last 5yr (modeling standards evolve), ≥85% tools ≤18mo | Check dates |
| **Diversity** | ≥5 source types (academic papers, books, industry standards, tools docs, case studies), none >30% | Count by type |
| **Cross-Viewpoint Analysis** | ≥60% Q&As analyze relationships from ≥2 viewpoints (technical + business, or technical + regulatory, etc.) | Review Q&As |
| **Coupling/Cohesion Metrics** | ≥50% Q&As include coupling/cohesion metrics (Ca, Ce, Instability, LCOM, modularity, centrality) | Count metrics |
| **Relationship Tools** | ≥15 modern tools with purpose, pricing, update date, relationship type support | Check tools section |
| **Link Accessibility** | 100% links accessible or archived (DOI/Wayback) | Verify all links |

## Workflow

### 1. Plan & Build References First
**Topic Clusters**: 8 lifecycle phases, 30-35 Q&As (≥3/phase), 20/40/40 F/I/A distribution
**References**: Glossary (≥30) → Tools (≥15) → Literature (≥20) → Citations (≥40). Use IDs: G#, T#, L#, A#. Verify: unique, recent (≥70% <5yr, ≥85% tools ≤18mo), diverse (≥5 types), accessible

### 2. Write Q&As
**Per answer**: 150-350 words, all 10 mandatory elements. **Check every 5**: Verify gates, types covered, network depth ≥3, 100% quantified, 100% precise verbs

### 3. Validate & Finalize
**Execute all 18 gates** (see Quality Gates table). **Verify**: 100% [Ref: ID] resolve, TOC/links valid, no redundancy

## Output Format

```markdown
## Contents
- [Coverage Matrix](#coverage-matrix): 8 phases × 7 relationship types = 56 cells, ≥3 Q&As per phase, ≥4 per type, 30-35 total
- [Topic Clusters](#topic-clusters): 8 lifecycle-aligned (Requirements & Discovery → Evolution & Governance)
- [Q&A by Cluster](#qa-sections): 30-35 Q&As with mandatory 10 elements (precise verbs, quantified metrics, multi-type analysis)
- [References](#references): G# (≥30), T# (≥15), L# (≥20), A# (≥40)
- [Validation](#validation-results): 18 gates, all PASS

## Coverage Matrix

| Phase | Structural | Behavioral/Temporal | Dependency/Coupling | Business/Market | Regulatory/Compliance | Integration/Interface | Emergent/Network | Total |
|-------|-----------|--------------------|--------------------|----------------|----------------------|----------------------|-----------------|-------|
| Requirements & Discovery | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Architecture & Design | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Development | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Testing & Quality | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 5-6 |
| Deployment & Release | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Operations & Observability | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Maintenance & Support | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3-4 |
| Evolution & Governance | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3-4 |
| **Total** | **≥4** | **≥4** | **≥4** | **≥4** | **≥4** | **≥4** | **≥4** | **30-35** |

## Topic 1: [Cluster Name - Lifecycle Phase]

### Q1: [Relationship Mapping Scenario Question]
**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Role**: [Role(s)] | **Relationship Types**: [Types from 7] | **Insight**: [Relationship strength, coupling metrics, key verbs] [Ref: ID]

**Answer** (150-350 words): [Include all 10 mandatory elements - relationship network, precise verbs, quantified metrics, multi-type analysis, bi-directional relationships, trade-offs, diagrams, cross-viewpoint, stakeholder perspectives]

**Visuals**: [Relationship diagram (class/component/ERD/network) + DSM matrix + metrics table + cross-viewpoint analysis]

---

## References

### Glossary (≥30)
**G#. Term**: Definition. Formula/Quantification. Verbs. [EN/ZH]

**Examples**:
**G1. Decomposition**: Breaking whole into parts. System **decomposes into** subsystems → components → modules. Metrics: depth (4-7 levels), fan-out, leaf count. Verbs: decomposes into, partitions into. [EN]
**G2. Modularity**: High cohesion within, low coupling between. Q = (edges within / total) - random. Q>0.3 good. Metrics: LCOM 0-1, Ca, Ce. Verbs: modules within, boundaries between. [EN]
**G3. Afferent Coupling (Ca)**: Incoming dependencies. Ca = components that **depend on** this. High Ca (>10) = stable. Verbs: depends on, relies on. [EN]
**G4. Efferent Coupling (Ce)**: Outgoing dependencies. Ce = this **depends on** others. High Ce (>10) = unstable. Instability: I=Ce/(Ca+Ce), 0-1. I=0 stable, I=1 unstable. [EN]
**G5. Cardinality**: Numeric relationship between entities (ANY domain). 1:1, 1:N, M:N. Examples: Customer(1) **has** Order(N), Manager(1) **supervises** Employee(N), Platform(1) **connects** Seller(M)-Buyer(N). Crow's foot (ERD). Verbs: has, owns, connects, governs. [EN]

### Tools (≥15)
**T#. Name** (Category): Purpose. Types. Price. Updated. URL. [EN/ZH]

**Examples**:
**T1. Structurizr** (C4): Architecture diagrams. Structural, Dependency. $6-49/mo, Free OSS. 2024-10. https://structurizr.com [EN]
**T2. Lattix** (DSM): Dependency analysis. Coupling, Structural. $2000+/seat. 2024-09. https://lattix.com [EN]
**T3. PlantUML** (Diagrams): UML diagrams. Structural, Behavioral, Dependency. Free OSS. 2024-11. https://plantuml.com [EN]

### Literature (≥20)
**L#. Author(s). (Year). *Title*. Publisher.** Focus. [EN/ZH]

**Examples**:
**L1. Fowler, M. (2003). *UML Distilled*. Addison-Wesley.** UML relationships, diagrams. [EN]
**L2. Martin, R. C. (2017). *Clean Architecture*. Prentice Hall.** Coupling/cohesion, SOLID, boundaries. [EN]
**L3. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** Bounded contexts, aggregates, relationships. [EN]

### Citations (≥40)
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
| **Phases Covered** | ≥3-4 lifecycle phases | Architecture, Development, Deployment, Evolution |
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
- **Phase**: [Architecture/Development/Deployment/Evolution]
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
