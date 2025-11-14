# Relationship Analysis Interview Generator

Generate 30-35 interview Q&A pairs testing comprehensive relationship analysis across software lifecycle, covering technical, business, market, and regulatory dimensions with precise relationship verbs and quantified metrics.

## Requirements

### Context & Scope
- **Domain**: Production-grade distributed systems (>10K rps, >1TB data, multi-team)
- **Audience**: BA, PM, Architect, Developer, QA/SET, DevOps, Security, Data Engineer, SRE, Leadership
- **Focus**: Comprehensive relationship analysis (7 types) across technical ↔ business ↔ market ↔ regulatory with precise verbs

**Core Principles**:
1. **Universal Applicability**: Relationship concepts (entities, cardinality, coupling, hierarchies) apply to ANY domain—not just software (business processes, organizational structures, market ecosystems, regulatory frameworks)
2. **Structural Foundation First**: Master structural organization (decomposition, composition, layering, modularity, hierarchies) before analyzing dependencies, behaviors, or integrations

### Output Specifications
- **Format**: 150-350 words, Mermaid diagrams, metrics tables, APA 7th [EN]/[ZH]
- **Quantity**: 30-35 Q&As; Difficulty: 20/40/40 (F/I/A)
- **Coverage**: MECE 8 Lifecycle × 7 Types (≥1 Q&A per major combo)
  - **Lifecycle**: Requirements, Architecture, Development, Testing, Deployment, Operations, Maintenance, Evolution
  - **Types**: Structural, Behavioral/Temporal, Dependency/Coupling, Business/Market, Regulatory/Compliance, Integration/Interface, Emergent/Network
- **Traceability**: Entity → Direct → Transitive → Network (quantified)
- **Per Cluster**: ≥1 diagram, ≥1 DSM, ≥1 network, ≥1 constraint analysis

### Content Standards
- **Precision**: Precise verbs (depends on, constrains, enables), quantified strength (coupling 0-1, cardinality 1:1/1:N/M:N)
- **Credibility**: Industry case studies, academic papers; sources ≤3yr
- **Balance**: Bi-directional, positive/negative, direct/transitive relationships
- **Logic**: Multi-level networks with quantified metrics
- **Concision**: Diagrams/matrices over text

## Relationship Analysis Framework

### Lifecycle × Relationship Coverage (MECE Required)

Ensure ≥1 Q&A covers each phase-type combination. Example relationships by phase:

| Phase | Example Verbs | Key Focus |
|-------|--------------|-----------|
| **Requirements** | owns, constrains, demands, governs, triggers, depends on | Stakeholder-requirement, market-feature, regulation-constraint |
| **Architecture** | composes, depends on, exposes, maps to, enforces, flows through | Component-system, service-database, capability-service, layer-responsibility |
| **Development** | inherits from, imports, calls, couples to, contributes to, facilitates | Class-base, module-dependency, feature-revenue, code-framework |
| **Testing** | covers, validates, depends on, measures, verifies, balances | Test-code, quality-retention, contract-API, strategy-confidence |
| **Deployment** | stages, orchestrates, requires, enables, gates, switches | Environment-progression, release-migration, approval-production, strategy-risk |
| **Operations** | displays, notifies, depends on, defines, complies with, integrates | Dashboard-metrics, SLO-experience, service-monitoring, platform-signals |
| **Maintenance** | fixes, resolves, depends on, erodes, mandates, maintains | Patch-vulnerability, support-logging, cost-margin, compatibility-clients |
| **Evolution** | evolves, replaces, depends on, enables, mandates, shapes | Architecture-target, platform-adoption, governance-standards, Conway's Law-structure |

### Relationship Type Reference

| Relationship Type | Relationship Verbs (Precise) | Key Metrics (Quantified) | Analysis Frameworks | Diagram Types |
|-------------------|------------------------------|--------------------------|---------------------|---------------|
| **Structural** | composes, contains, owns, encapsulates, aggregates, inherits from, implements, extends, part of, consists of, decomposes into, layers on, modules within, boundaries between, abstracts over | Coupling coefficient (0-1), Cohesion metric (LCOM 0-1), Depth of inheritance (0-N), Component count, Modularity index, Abstraction level (0-N layers), Decomposition depth, Boundary clarity | UML Class Diagrams, Component Diagrams, Package Diagrams, C4 Model (4-level abstraction), Domain Models, Decomposition Trees, Layer Diagrams | Class diagrams, component diagrams, package diagrams, ERD, decomposition trees, layer diagrams, module boundaries |
| **Behavioral/Temporal** | triggers, follows, precedes, flows through, transitions to, executes before/after, synchronizes with, awaits, propagates, cascades | Event frequency (events/sec), Latency (ms), Throughput (ops/sec), State transition probability, Sequence depth (steps) | UML Sequence Diagrams, State Machines, Activity Diagrams, BPMN, Event Storming | Sequence diagrams, state machines, activity diagrams, event flows |
| **Dependency/Coupling** | depends on, requires, relies on, couples to, binds to, calls, invokes, uses, references, imports | Dependency weight (0-1), Afferent coupling (Ca), Efferent coupling (Ce), Instability (I=Ce/(Ca+Ce)), Distance from main sequence | Dependency Structure Matrix (DSM), Dependency Graphs, Call Graphs, Impact Analysis | Dependency graphs, DSM matrices, call trees, coupling matrices |
| **Business/Market** | contributes to, enables, supports, drives, influences, shapes, determines, constrains, competes with, complements | Revenue attribution ($), Customer lifetime value (CLV), Market share (%), Competitive advantage index, ROI (%), Time-to-market (days) | Business Model Canvas, Value Proposition Canvas, Value Stream Mapping, Porter's Five Forces, Wardley Maps | Business capability maps, value streams, customer journey maps, positioning matrices |
| **Regulatory/Compliance** | governs, mandates, requires, forbids, permits, restricts, enforces, validates, complies with, certifies | Compliance coverage (%), Violation risk score (CVSS), Audit finding count, Regulatory cost ($), Certification status, Policy enforcement (%) | GDPR, HIPAA, PCI-DSS, SOC2, ISO 27001, NIST Framework, Compliance Matrices, Risk Registers | Compliance matrices, risk heat maps, audit trails, policy hierarchies, control mappings |
| **Integration/Interface** | exposes, consumes, integrates with, transforms, adapts, translates, routes, proxies, mediates, orchestrates | API call volume (requests/sec), Integration complexity (interface count), Protocol compatibility (%), Latency overhead (ms), Transformation cost (CPU%) | API Design (REST, GraphQL, gRPC), Integration Patterns, ESB, Service Mesh, Contract Testing | API diagrams, integration architecture, data flow diagrams, protocol layers, contracts |
| **Emergent/Network** | emerges from, amplifies, reinforces, balances, competes with, influences, shapes, evolves, distributes, accumulates | Network density (edges/nodes), Centrality (betweenness, degree, closeness), Clustering coefficient, Emergence score, Network effect multiplier | Network Analysis, Graph Theory, Systems Thinking, Conway's Law, Complexity Theory, Agent-Based Modeling | Network graphs, force-directed layouts, centrality heat maps, feedback loops, system dynamics |

## Visuals & Metrics

Use diagrams and metrics from Relationship Type Reference (Section 2.2). Key diagram types: Class/Component/ERD (structural), Sequence/State (behavioral), DSM/Dependency graph (coupling), Value stream/Journey map (business), Compliance matrix (regulatory), API/Integration (interface), Network graph (emergent).

## Relationship Analysis Frameworks & Approaches

| Framework | When to Use | Pros | Cons | Trade-offs | References |
|-----------|-------------|------|------|------------|------------|
| **UML** | OO design, structural/behavioral modeling | Standard notation, broad tool support, precise | Steep learning curve, over-formal | Precision vs. agility | Fowler (2003), Booch (2005) |
| **C4 Model** | Architecture documentation, 4 abstraction levels | 4 zoom levels, simple, Mermaid support | Less behavioral, newer | Simplicity vs. completeness | Brown (2018), Structurizr |
| **ERD** | Universal modeling, ANY domain, cardinality (1:1/1:N/M:N) | Industry standard, applies anywhere, clear semantics | Less behavioral, notation variants | Universal vs. domain-specific | Chen (1976), Simsion (2005) |
| **DSM** | Dependency analysis, refactoring, cycles | Quantifies coupling (Ca/Ce), detects cycles | Scales poorly >50, less intuitive | Precision vs. visual clarity | Steward (1981), Lattix |
| **DDD** | Complex domains, bounded contexts | Maps business to code, context boundaries | High investment, domain experts needed | Alignment vs. speed | Evans (2003), Vernon (2013) |
| **Network Analysis** | Complexity, centrality, emergent patterns | Quantifies structure, detects communities | Requires graph data, O(n²) | Rigor vs. intuition | Newman (2010), Gephi, Neo4j |
| **RACI** | Stakeholder responsibilities, role clarity | Simple 4-category, clarifies ownership | Static, maintenance overhead | Clarity vs. flexibility | PMI PMBOK, ITIL |
| **Capability Mapping** | Enterprise architecture, business-IT alignment | Links business-tech, identifies redundancy | Abstract, evolves slowly | Strategic vs. tactical | TOGAF, ArchiMate |
| **Value Stream** | Process optimization, waste identification | Visualizes flow, quantifies waste | Linear view, process-centric | Process vs. system view | Rother (1999), Lean |

## Question Design

**Principles**: Test relationship analysis (not recall); real-world scenarios; map multi-type relationships; span all 7 types; use precise verbs

**Good vs. Poor Examples**:

| ✅ Good | ❌ Poor | Why |
|---------|---------|-----|
| "E-commerce: (1) Decompose 4 layers; (2) 8 bounded contexts; (3) Analyze coupling: Order **depends on** Payment (0.8), Payment **couples to** Stripe (Ce=3, Ca=1, I=0.75). Show layer, decomposition, DSM." | "What is coupling?" | Tests analysis with structure-first + quantified metrics vs. recall |
| "Payment **exposes** API (500 rps); GDPR **mandates** encryption; Encryption **increases** latency 30ms; **conflicts with** SLO. Map all types, quantify." | "How does payment work?" | Multi-type relationships with precise verbs + metrics vs. vague |
| "Microservices (20): Calculate API Gateway centrality (0.85); Conway's Law **aligns** teams; density=0.3. Use force-directed graph." | "What is microservices?" | Network analysis with quantified metrics vs. definition |
| "Auth **enables** login, **implements** OAuth2, **complies with** SOC2, **exposes** /auth; Ce=8 **constrains** deployment; downtime **costs** $10K/hr. Show DSM, capability, compliance." | "Explain OAuth2" | Cross-viewpoint (tech+business+regulatory) vs. single dimension |

### Stakeholder Context by Role

| Role | Relationship Analysis Focus | Expected Detail |
|------|----------------------------|----------------|
| **Business Analyst** | Business capability **maps to** system feature; Requirement **constrains** solution; Stakeholder **owns** acceptance criteria; Use case **depends on** data entities | Capability mapping (business function → feature → component), requirement traceability matrix, stakeholder-requirement-component network, domain model with entity relationships (1:1, 1:N, M:N) |
| **Product Manager** | Feature **contributes to** revenue; Customer segment **demands** capability; Market competitor **influences** pricing; Product vision **shapes** roadmap priority | Value stream mapping (customer need → feature → outcome), impact mapping (goal → actor → impact → deliverable), competitive positioning matrix, OKR-feature-metric linkage, Wardley maps |
| **Architect** | Component **composes** system; Service **depends on** database (coupling metrics); API **exposes** interface; Layer **encapsulates** responsibility; Conway's Law **aligns** teams to modules | C4 diagrams (Context/Container/Component/Code), dependency graphs with coupling metrics (Ca, Ce, Instability), ADRs documenting relationship trade-offs, DSM matrix for refactoring analysis |
| **Developer** | Class **inherits from** base; Module **imports** dependency; Function **calls** API; Code **couples to** framework (coupling coefficient); Implementation **relies on** library | UML class diagrams with inheritance/composition/aggregation, call graphs, dependency trees, coupling/cohesion metrics (LCOM, Ca, Ce), interface-implementation relationships |
| **QA/SET** | Test **covers** code (coverage %); Test suite **depends on** fixture; Contract test **validates** API; Quality gate **enforces** threshold; Flaky test **undermines** confidence | Test coverage matrix (requirement → test → code), test dependency graph, contract specifications (provider-consumer), quality metric relationships (coverage → defect density) |
| **DevOps** | Pipeline **orchestrates** stages; Environment **stages** deployment; Service **relies on** infrastructure; Feature flag **controls** rollout; Blue-green **switches** traffic | CI/CD pipeline diagram (trigger → stage → artifact), infrastructure dependency graph (service → container → VM → region), deployment topology, feature flag architecture |
| **Security** | Threat **exploits** vulnerability; Control **mitigates** risk; Policy **enforces** standard; Compliance **mandates** audit; Attack **propagates** through trust boundary | Threat models (STRIDE), attack trees (goal → sub-goal → vector), risk matrices (threat → vulnerability → impact), compliance mapping (regulation → control → evidence) |
| **Data Engineer** | Entity **relates to** entity (cardinality 1:1, 1:N, M:N—applicable to ANY domain: business entities, organizational entities, market entities, not just database); Pipeline **transforms** data; Schema **defines** structure; Migration **evolves** schema; Partition **distributes** data | ERD for universal entity modeling (business, market, technical, organizational), data flow diagrams (source → transformation → sink), schema evolution diagrams, data lineage graphs (source → derived field → dashboard) |
| **SRE** | Service **depends on** monitoring; Alert **notifies** on-call; SLO **defines** reliability; Dashboard **displays** metrics; Incident **escalates** to leadership | Service dependency graph with SLO annotations, monitoring-alert-runbook linkage, incident response RACI, observability platform integration diagram (metrics → traces → logs) |
| **Leadership** | Team **owns** service (Conway's Law); Investment **enables** capability; Platform **supports** product line; Governance **enforces** standard; Ecosystem **influences** technology choice | Organizational chart mapped to system architecture, RACI matrices, capability-investment roadmap, governance structure (policy → standard → implementation), strategic dependency analysis |

**Mandatory Elements per Q&A**:
1. **Structural foundation FIRST**: Decomposition → Layering → Modularity → Hierarchies (essential before analyzing other relationships)
2. **Relationship network**: Entity → Direct (precise verbs) → Transitive → Network effects (quantified)
3. **Visuals**: Structural diagrams, relationship diagrams (class/component/ERD/network), DSM, metrics table
4. **Context**: Phase, role, ≥3 relationship types (structural FIRST + ≥2 others)
5. **Citation**: ≥1 [Ref: ID]
6. **Insight**: Key finding on coupling metrics, bi-directional, or network effects (1 sentence)
7. **Trade-offs**: Structural alternatives (tight vs loose, hierarchical vs flat, direct vs mediated)
8. **Metrics**: Quantified (coupling 0-1, Ca/Ce/I, cardinality 1:1/1:N/M:N, centrality, modularity Q)
9. **Precise verbs**: All relationships use domain-specific verbs (see Relationship Type Reference)
10. **Stakeholder perspectives**: Role-specific analysis (≥2 viewpoints)

## References & Quality

### Reference Minimums
- **≥30 Glossary**: Structural (Decomposition, Modularity, Layering, Hierarchy); Coupling/Cohesion (Ca, Ce, LCOM, Instability I=Ce/(Ca+Ce)); Relationships (Cardinality 1:1/1:N/M:N, Dependency, Association, Inheritance); Network (Density, Centrality, Clustering); Others (Conway's Law, Network Effect, Transitive). All with formulas/quantification
- **≥15 Tools**: Modeling (PlantUML, Mermaid, Structurizr), Analysis (Lattix, Structure101, NDepend), Dependency (Gephi, NetworkX, Neo4j), Business (Miro, draw.io), Compliance (GRC, Archer). Include: purpose, price, update ≤18mo, type support
- **≥20 Literature**: UML (Fowler 2003), Architecture (Bass 2021, Brown C4 2018), DDD (Evans 2003), Data (Chen ERD 1976, Simsion 2005), Coupling (Martin 2017), Network (Newman 2010, Barabási 2016), Systems (Senge 1990), Business (TOGAF, Osterwalder BMC 2010), Teams (Conway 1968, Skelton Team Topologies 2019), Integration (Hohpe 2003)
- **≥40 Citations**: APA 7th [EN]/[ZH], DOI/URL, academic + standards (UML, ArchiMate, TOGAF) + case studies

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

## Validation Results

| Gate | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| Lifecycle | 8 phases, ≥3 each | ✅ PASS | Req=4, Arch=5, Dev=4, Test=6, Deploy=4, Ops=5, Maint=3, Evol=4 |
| Stakeholder | ≥8/10 roles, ≥2 each | ✅ PASS | BA=3, PM=4, Arch=5, Dev=4, QA=4, DevOps=3, Sec=2, Data=3, SRE=4, Lead=3 |
| Relationship Types | 7 types, ≥4 each | ✅ PASS | Structural=8, Behavioral=7, Dependency=9, Business=6, Regulatory=5, Integration=7, Emergent=6 |
| Difficulty | 20/40/40 ±5% | ✅ PASS | 7F/14I/14A = 20%/40%/40% |
| Relationship Network Depth | ≥3 levels, 100% | ✅ PASS | 35/35 = 100%, avg depth 3.8 levels |
| Quantified Relationships | 100% have metrics | ✅ PASS | 35/35 = 100% (coupling/cardinality/centrality metrics) |
| Multi-Type Analysis | ≥70% analyze ≥3 types | ✅ PASS | 28/35 = 80% multi-type |
| Precise Verbs | 100% use precise verbs | ✅ PASS | 35/35 = 100% (depends on, composes, exposes, mandates, etc.) |
| Bi-directional | ≥50% identify bi-directional | ✅ PASS | 19/35 = 54% bi-directional |
| Trade-offs | 100% acknowledge | ✅ PASS | 35/35 = 100% (tight vs loose coupling, hierarchical vs flat) |
| Visual Diagrams | 100% include ≥1 diagram | ✅ PASS | 35/35 = 100% (class/component/ERD/network/DSM) |
| Citations | ≥75% ≥1, ≥40% ≥2, ≥25% standards | ✅ PASS | 86% ≥1, 49% ≥2, 29% standards (UML/ArchiMate/TOGAF) |
| Cross-refs | 100% [Ref: ID] resolve | ✅ PASS | G1-G32, T1-T17, L1-L22, A1-A43 |
| Recency | ≥70% <5yr, ≥85% tools ≤18mo | ✅ PASS | 77% <5yr, 88% tools ≤18mo |
| Diversity | ≥5 types, none >30% | ✅ PASS | Academic 24%, Books 22%, Standards 20%, Tools 18%, Case studies 16% |
| Cross-Viewpoint | ≥60% analyze ≥2 viewpoints | ✅ PASS | 24/35 = 69% multi-viewpoint |
| Coupling/Cohesion Metrics | ≥50% include metrics | ✅ PASS | 21/35 = 60% (Ca/Ce/Instability/LCOM/centrality) |
| Relationship Tools | ≥15 with type support | ✅ PASS | 17: Modeling=5, Analysis=4, Dependency=4, Business=2, Compliance=2 |
| Links | 100% accessible/archived | ✅ PASS | 58/58 verified |
```

## Example Format

**Q: [Scenario with scale/context - describe system with specific components and relationships]**

**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Roles**: [Role(s)] | **Types**: [≥3 from 7] | **Insight**: [1 sentence: coupling/bi-directional/network effects] [Ref: ID]

**Answer** (150-350 words): [Context] → [Structure FIRST: decomposition/layering/modularity] → [Relationship network: Entity → Direct (precise verbs) → Transitive → Network (quantified)] → [Multi-type: structural + ≥2 others] → [Trade-offs] [Ref: ID]

**Visuals**:
- **Structural + Relationship Diagram**: Mermaid (class/component/ERD/network) with precise verbs
- **Dependency Matrix (DSM)**: Components, Ca/Ce/Instability
- **Metrics Table**: Component, Type, Verb, Cardinality, Coupling, Centrality
- **Cross-Viewpoint**: ≥2 stakeholder perspectives
