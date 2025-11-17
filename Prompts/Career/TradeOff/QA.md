# Trade-Off Driven Software Architecture Q&A Generator

Generate 6-12 decision-critical Q&As demonstrating trade-off analysis for informed decisions with limited time.

**Context**: Distributed systems (>10K rps, >1TB data), cloud-native, multi-stakeholder, full SDLC  
**Audience**: Senior devs (5+ years), architects, experts  
**Success**: 12/12 validation PASS | **Effort**: 4-6 hours | **Validity**: Evergreen (refresh annually or when architecture context changes)

## Core Principle

Decision = trade-off (optimize X at Y's expense), constraint-bounded, stakeholder-dependent, with lifecycle ripples.

**Framework**: Identify ≥3 forces → Quantify ≥4 dimensions (technical, resource, business, operational) → Show constraint interactions → Map stakeholder conflicts/alignment → Define thresholds → Trace ripples → Mitigate → Validate

---

# Specifications

| Aspect | Target |
|--------|--------|
| **Count** | 6-12 Q&As @ 25% F / 50% I / 25% A |
| **Length** | 150-250 words (excl. code) |
| **Structure** | Scenario → insight → constraints → trade-offs → decision → metrics |
| **Citations** | ≥1/Q&A; ≥8 total |
| **Per Cluster** | ≥1 diagram + ≥1 table |

## Decision Criticality Framework (NEW - MANDATORY)

**Include if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts architecture go/no-go, team scaling, or strategic pivot
- **Creates Risk**: Material threat (performance regression, cost overrun >10%, compliance breach, team bottleneck)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (Architect + SRE, PM + Dev, etc.)
- **Requires Action**: 1-6mo action window (not speculative)
- **Quantified Impact**: Latency ms, throughput rps, cost $, complexity %, team size

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative

## 3-4 Decision-Critical Dimensions (MECE, 2-3 Q&As each)

1. **Structural**: Modularity vs simplicity (team scaling, deployment frequency)
2. **Behavioral**: Consistency vs availability (data correctness, system resilience)
3. **Quality**: Performance vs maintainability (SLO compliance, team velocity)
4. **(Optional) Data**: Normalization vs denormalization (query performance, storage cost)

## ≥5 Core Stakeholder Roles (≥60% multi-stakeholder)

| Role | Concerns | Priorities | Metrics |
|------|----------|------------|---------|
| **Architect** | System quality, coherence | Flexibility vs simplicity | NFR achievement, debt |
| **Developer** | Maintainability, velocity | Abstraction vs explicitness | Build time, complexity |
| **SRE** | Reliability, observability | Availability vs cost | SLO, MTTR |
| **PM** | Time-to-market, features | Speed vs quality | Release frequency, NPS |
| **Security** | Risk, compliance | Security vs usability | Vulnerability count |

## 3-4 Decision-Critical Lifecycle Phases

| Phase | Trade-Offs | Constraints | Authority |
|-------|------------|-------------|-----------|
| **Design** | Flexibility vs simplicity | Technical, Org, Ecosystem | Arch, Sec |
| **Development** | Velocity vs quality | Resource, Technical | Dev, Arch |
| **Deployment** | Speed vs safety | Operational, Resource | SRE, Lead |
| **Operations** | Availability vs cost | Operational, Technical | SRE, Ops |

## 8 Constraint Categories (All Must Be Covered)

1. **Technical**: Hardware (CPU, RAM, storage, network), Platform (cloud, runtime), Legacy, Tech stack
2. **Resource**: Time (deadlines), Budget (infra, licensing, headcount), Team (size, skills)
3. **Business/Market**: Revenue model, Market (competition, segments), Continuity, Strategy
4. **Organizational**: Stakeholder priorities, Process (CAB, ARB), Governance (ADR), Culture
5. **Regulatory/Compliance**: Data protection (GDPR, HIPAA, PCI), Standards (SOC 2, ISO), Audit
6. **Operational**: Availability (RTO/RPO), Observability, Support (SLA), Capacity
7. **Ecosystem**: Vendor lock-in, OSS (health, license), Partners (APIs), Standards, Talent
8. **Lifecycle**: Per-phase constraints (specs, debt, CI/CD, tests, rollback, incidents, CVE, migration)

## Content Standards

**Traceability**: Requirements → Constraints → Pattern → Code → Metrics

**Quantification**: Use numbers. ✅ "+180% read, +35ms write, +40% complexity" ❌ "complex"

**Context Thresholds** (when calculus changes):
- **Technical**: CPU <4/4-16/>16; RAM <8/8-64/>64GB; Storage <100/>10K IOPS; Latency <10/10-100/>100ms
- **Resource**: Team <10/10-50/>50; Budget <$10K/$10-100K/>$100K/mo; Time <3/3-12/>12mo
- **Business**: Revenue model (usage/sub/license); Share <5%/5-20%/>20%; CAC:LTV 1:1/1:3
- **Org**: Agile 2-wk/waterfall qtly; CAB <24h/2-wk; Culture fail-fast/conservative
- **Regulatory**: None/GDPR/HIPAA/PCI; SOC 2 ($50-200K); Retention 1/3/7yr
- **Operational**: SLA 99%/99.9%/99.99%/99.999%; RPS <100/100-10K/>10K; Data <1/1-100/>100TB
- **Ecosystem**: Cloud AWS/multi; OSS >1K⭐ vs stagnant; Talent popular vs niche
- **Lifecycle**: CI <10/>30min; Deploy daily/monthly; MTTR <30min/>4h; CVE <7/<30d

**Balanced**: ≥2 alternatives, explicit limits, tag [Consensus]/[Context-dependent]/[Emerging]

**Precise**: Define jargon inline (CAP—Consistency/Availability/Partition), concrete ("<300ms p95" not "fast")

## Required Per Q&A (Minimal Viable)

1. ≥3 forces (quantified)
2. ≥4 constraint categories (including technical, resource, business, operational)
3. Quantified trade-off (+40% perf, +60% cost, +30% complexity)
4. Stakeholder alignment/conflict (≥2 roles)
5. Decision criteria (go/no-go thresholds)
6. Mitigation strategy

## Required Per Cluster (Compressed)

≥1 diagram (<80 nodes) + ≥1 table (≥3 alternatives, ≥6 columns)

## Essential Trade-Off Patterns (Ensure Coverage)

**Structural**: Monolith vs Micro (team <10 vs >50), Layered vs Hexagonal, Sync vs Async (<100ms vs >1s)

**Behavioral**: Strong vs Eventual Consistency (financial vs social), Orchestration vs Choreography (<5 vs >20 svc), Fail-Fast vs Degradation

**Quality**: Perf vs Maintainability (<10ms p95), Vertical vs Horizontal (stateful vs stateless), Security vs Usability (HIPAA vs non), Observability vs Overhead (99.9% vs 99.99%)

**Data**: SQL vs NoSQL (<1TB vs >100TB), Normalization vs Denorm (write 1:1 vs read 1:100), Replicas vs CQRS, Batch vs Stream (<1GB/day vs >1TB/day)

**Integration**: REST vs gRPC (public vs internal, <100 vs >10K rps), Lock-in vs Managed (<5 vs >50 eng), Custom vs Third-Party (core vs commodity), API Versioning (1000s vs 10 clients)

**Evolution**: Big Bang vs Incremental (<3mo vs continuous), Compat vs Clean Slate (1000s vs 10 clients), Velocity vs Quality (land-grab vs mature), Innovation vs Stability (startup vs enterprise, 90% vs 99.99%)

**Cross-Cutting**: Build vs Buy (core vs commodity, <3 vs >20 eng), Automation vs Manual (>100 vs <10 deploys/mo), Standardization vs Autonomy (>50 vs <10 eng)

## References (Proportional 60% Reduction)

| Component | Min | Requirements |
|-----------|-----|--------------|
| **Glossary** | ≥10 | Decision-critical terms only (3-4 dimensions + 5 core stakeholders) |
| **Tools** | ≥3 | URL, update ≤18mo, decision-critical only |
| **Literature** | ≥4 | Canonical references only (Fowler, Evans, Vernon, Richardson, Kleppmann) |
| **Citations** | ≥8 | APA 7th; 60/30/10% EN/ZH/other (±10%) |

**Quality**: Recency (≥50% last 3yr), Diversity (≥2 types), 100% valid links

---

# Generation Process

## 1. Plan Structure (Streamlined)

1. Select 3-4 decision-critical clusters (Structural, Behavioral, Quality, ±Data)
2. Allocate 2-3 Q&As/cluster (6-12 total, 25% F / 50% I / 25% A)
3. Map patterns, ≥4 constraint categories, ≥5 core stakeholders, 3-4 phases (decision-critical only)
4. Define thresholds (≥70% Q&As)

**Example**: "Modularity vs Simplicity" (Structural, team scaling), "Consistency vs Availability" (Behavioral, data correctness)

**Checks**: 6-12 total; 25/50/25% F/I/A; ≥3 forces; decision-critical coverage; ≥70% thresholds

## 2. Build References (Compressed)

Glossary (≥10) → Tools (≥3) → Literature (≥4) → Citations (≥8, 60/30/10% EN/ZH/Other)

## 3. Write Q&As (Streamlined)

**Questions**: ≥70% judgment ("How would you..." / "When..." / "Compare..."); multi-dimensional constraints

**Answer**: Header (difficulty, dimension, phase, stakeholders) → Insight (quantified, 1 sentence) → Constraints (≥4 categories, interactions) → Body (150-250 words: rationale, trade-offs, conflicts, decision criteria, mitigation) → Citations (≥1) → Trade-offs (≥3 alt, ≥6 cols) → Stakeholder Matrix (≥2 roles)

**Validate Every 3**: Count, citations, syntax, traceability, quantification, ≥3 forces, ≥4 constraint categories, conflicts, decision criteria

## 4. Create Artifacts (Compressed)
Per Cluster: ≥1 Diagram (<80 nodes) + ≥1 Table (≥3 alt, ≥6 cols)

## 5. Link References
Populate → Extract → Verify → Remove orphans → Validate URLs

## 6. Validate (12 Checks - Streamlined)

**Essential (1-12)**:
1. Counts (G≥10, T≥3, L≥4, A≥8, Q=6-12 @25/50/25%)
2. Citations (≥100% ≥1; ≥50% ≥2)
3. Language (60/30/10%)
4. Recency (≥50% 3yr)
5. Links (100%)
6. Words (150-250)
7. Quantified (100%)
8. Decision Criticality (100% satisfy ≥1 criterion)
9. Forces (100% ≥3)
10. Constraints (100% ≥4 categories/Q&A; 100% 8 categories overall)
11. Conflicts (≥80%)
12. Mitigation (≥70%)

**Fail Protocol**: ANY fail → STOP → Fix → Re-validate ALL → 12/12 PASS

## 7. Final Review (8 Criteria—All PASS)

1. **Clarity**: Logical, consistent, jargon defined
2. **Accuracy**: Verifiable facts, valid diagrams, sound metrics
3. **Completeness**: 3-4 dims (2-3 each), all 8 constraint categories covered, ≥5 stakeholders, 3-4 phases, 12/12 PASS
4. **Trade-Off Centrality**: 100% ≥3 forces, multi-dimensional, decision-critical
5. **Quantification**: 100% quantified ≥4 dims, numerical
6. **Stakeholder Multi-Perspective**: ≥2 views, conflicts, alignment; ≥5 core roles covered
7. **Decision Criteria**: ≥70% thresholds, go/no-go defined
8. **Practicality**: Actionable, measurable, mitigation

**Submit**: 12/12 + 8/8 | **High-Risk**: Decision Criticality, URLs, quantification

---

# Output Template

```markdown
## Contents
[TOC: Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Dimension | Count | Difficulty | Trade-Offs | Constraints |
[3-4 dims, 6-12 total, 25/50/25% F/I/A]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]
**Core Trade-Off**: [Tension]

### Q1: [Question]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Phase**: [Phase(s)] | **Stakeholders**: [≥2]

**Insight**: [Quantified, ≥3 forces with numbers]

**Constraints**: [≥4 categories, interactions]

**Answer**: [150-250 words: rationale, trade-offs, conflicts, decision criteria, mitigation] [≥1 cite]

**Diagram** (per cluster):
```mermaid
[<80 nodes]
```

**Trade-offs** (≥3 alt):
| Approach | Pros | Cons | Use When | Technical | Business | Complexity | Risk | Tag |

**Stakeholder Matrix** (≥2):
| Stakeholder | Concern | Priority | Position | Alignment |

---

## References

### Glossary (≥10)
**G1. [Term]** [Lang]: [Definition]. **Related**: [Terms]

### Tools (≥3)
**T1. [Tool]** [Tag]: [Purpose]. Updated: [YYYY-MM]. [URL]

### Literature (≥4)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag]

### Citations (≥8, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [Lang]

---

## Validation
| # | Check | Target | Result | Status |
[12 checks]

**Overall**: [X/12 PASS]
**Issues**: [Failures]
**Fix**: [Actions]

**Coverage**: Constraint Categories (8/8): [counts] | ≥5 Stakeholders: [counts] | 3-4 Phases: [counts]
```

# Reference Example: Complete Q&A

### Q: How would you design a high-throughput order processing system for a regulated healthcare marketplace under tight hardware and compliance constraints?

**Difficulty**: Advanced | **Dimension**: Structural + Data | **Phase**: Design, Dev, Ops | **Stakeholders**: Arch, Dev, Sec, Data, SRE, Lead

**Insight**: Event-driven CQRS (Command Query Responsibility Segregation—separates writes/reads) achieves 15K rps on 4-core (+180% vs monolith) but +35ms write latency (p95), +40% ops complexity while satisfying HIPAA audit.

**Constraints**:
- **Technical**: 4-core 3.2GHz, 16GB RAM, 500 IOPS, <50ms network
- **Resource**: $8K/mo (12 inst max), 8 devs (4 sr, 4 mid), 1 SRE, 1 sec, 4mo, 2-wk sprints
- **Business**: $500K/mo rev ($50×10K orders/day), 15% share target, 3 rivals <200ms, enterprise (hospitals)
- **Organizational**: ARB approval, moderate risk tolerance, healthcare compliance culture, cross-functional team ownership
- **Regulatory**: HIPAA (PHI encrypt, 7yr logs), SOC 2 Type II
- **Operational**: 99.9% avail (43min/mo), SEV-1 <30min MTTR, 24/7 on-call
- **Ecosystem**: AWS lock-in OK, Kafka OSS (LTS), SOAP pharmacy (5-10s), OpenAPI partners
- **Lifecycle**: existing monolith to be decomposed, CI/CD with canary deploys, limited staging envs for migration

**Answer**: 
Healthcare PHI (Protected Health Info) orders face 8 constraint dimensions: **Technical** (4-core), **Resource** (8 eng, $8K/mo, 4mo), **Business** ($500K/mo, <200ms compete, 15% share), **Organizational** (ARB approval, moderate risk appetite, cross-functional 8-person team with 2-wk sprints), **Regulatory** (HIPAA, SOC 2), **Operational** (99.9%, 24/7), **Ecosystem** (AWS, Kafka OSS, SOAP legacy), **Lifecycle** (existing monolith migration, CI/CD with canary deploys, limited non-prod envs). CQRS with event sourcing separates: commands → event store (write-optimized, append-only for HIPAA), queries → materialized views (read-optimized, cached). Independent scaling (3 write, 6 read within budget), full audit, competitive latency [A2, A7].

Implementation: Kafka OSS (LTS) for events (TLS 1.3 + AES-256), AWS PostgreSQL (encrypted, auto-backup), Redis for reads. SOAP isolated via anti-corruption layer + circuit breaker (5s timeout, 50% threshold). Trade-offs: +35ms write (OK vs 2s legacy), +40% ops (3 stores, mitigated by Kafka exp), +60% storage ($2.4K/mo within budget). **Business**: +$150K/mo capacity, <200ms SLA, 4mo TTM [A4].

Metrics: p95 write 180ms (<300ms SLA), reads 25ms, CPU 65% (30% headroom), cost $7.8K/mo. **Alignment**: Sec approves encrypted pipeline; SRE accepts complexity w/ runbooks; PM OK 4mo; Lead approves $7.8K for +$150K ROI, compliance. Limits: event store 5GB/day → partition at 18mo; eventual consistency <500ms unsuitable for real-time inventory.

**Implementation** (Go):
```go
type OrderCommand struct {
    OrderID   string    `json:"order_id"`
    PatientID string    `json:"patient_id"`
    Items     []Item    `json:"items"`
    Timestamp time.Time `json:"timestamp"`
}

func (h *OrderHandler) ProcessCommand(ctx context.Context, cmd OrderCommand) error {
    if err := h.validator.Validate(cmd); err != nil {
        h.auditLog.Log(ctx, "OrderValidationFailed", cmd.OrderID, err)
        return fmt.Errorf("validation failed: %w", err)
    }
    
    event := OrderCreatedEvent{
        EventID:   uuid.New().String(),
        OrderID:   cmd.OrderID,
        Data:      h.encrypt(cmd),
        Timestamp: time.Now(),
    }
    if err := h.eventStore.Append(ctx, event); err != nil {
        return fmt.Errorf("event store append: %w", err)
    }
    
    if err := h.kafka.Publish(ctx, "orders.created", event); err != nil {
        h.logger.Error("kafka publish failed", "event_id", event.EventID, "error", err)
    }
    
    return nil
}
```

**Metrics**:
| Metric | Formula | Variables | Target | Constraint Impact |
|--------|---------|-----------|--------|-------------------|
| Write Latency (p95) | `validate + encrypt + append + kafka_ack` | validate=15ms, encrypt=10ms, append=120ms, ack=35ms | <300ms | Hardware: 4-core limits parallel validation; Compliance: encryption adds 10ms |
| Throughput | `instances × (cores × 1K rps / core)` | instances=3, cores=4 | ≥15K rps | Budget: $8K limits to 12 instances; Hardware: 4-core limits per-instance rps |
| Storage Growth | `events/day × avg_size × retention` | 50K events/day, 2KB avg, 7yr retention | <500GB/mo | Compliance: HIPAA 7yr retention; Budget: storage $0.10/GB-mo |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Hardware Impact | Budget Impact | Business Impact | Ecosystem Impact | Consensus |
|----------|------|------|----------|-----------------|---------------|-----------------|------------------|-----------|
| **CQRS + Event Sourcing** | +180% throughput (15K vs 5.5K); full audit trail; independent scaling | +35ms write latency; +40% ops complexity; +60% storage | Regulated domains, audit requirements, read-heavy (10:1 ratio) | CPU: 65% peak (3 nodes × 4-core); RAM: 12GB/node; Storage: 5GB/day | $7.8K/mo (compute $5.4K, storage $2.4K) | Revenue: +$150K/mo capacity; Time-to-market: 4mo; Customer: meets <200ms SLA | Kafka OSS: active community; AWS: native support; Partner APIs: event webhooks | [Consensus] |
| **Monolith + Read Replicas** | Simple ops; lower latency (145ms write); existing expertise | Max 5.5K rps (1 node × 4-core); limited scaling; audit retrofitting hard | Small teams (<5), low compliance, <10K rps, tight budgets | CPU: 85% peak (1 node × 4-core); RAM: 16GB; Storage: 1.5GB/day | $4.5K/mo (compute $3K, storage $1.5K) | Revenue: limited to $275K/mo; Competitive: falls behind rivals; Churn risk: 10% | PostgreSQL: mature; Few integrations; Partner: limited scalability | [Context-dependent] |
| **Microservices + CQRS** | +250% throughput (19K rps); best scalability | +60% ops complexity; +90% storage; requires >10 engineers | Large teams (>20), >20K rps, budget >$15K/mo, multi-region | CPU: 55% peak (6 nodes × 4-core); RAM: 8GB/node; Storage: 8GB/day | $12K/mo (compute $8K, storage $4K) | Revenue: +$300K/mo; Time-to-market: 6mo (complexity); Market: overkill current stage | Multi-vendor: avoid lock-in; Service mesh: learning curve; Partner: API versioning complexity | [Emerging] |

**Stakeholder Matrix**:
| Stakeholder | Concern | Priority | Position | Alignment |
|-------------|---------|----------|----------|-----------|
| **BA** | Domain, requirements | Correctness > Speed | Prefers CQRS: read/write separation aligns | Validates edge cases |
| **PM** | TTM, competition | Speed > Perfection | Prefers CQRS: 4mo (vs 6mo micro), <200ms SLA | Accepts +$3.3K for +$150K revenue |
| **Architect** | Quality, coherence | Balanced | Chooses CQRS: middle ground (8 team) | Mitigates w/ patterns, ADRs |
| **Developer** | Maintainability | Simplicity > Complexity | Concerned: +40% ops, 3 stores | 4/8 have Kafka exp, runbooks |
| **QA** | Quality, coverage | Quality > Speed | Neutral: more test complexity but testable | Secures +$1K/mo test env |
| **DevOps** | Deployment, pipeline | Automation + Safety | Supports w/ conditions: schema gates, canary | Schema versioning, auto-rollback |
| **Security** | Compliance | Compliance > Perf | Approves: event sourcing = HIPAA audit | Pen test $30K, +10ms latency OK |
| **Data** | Quality, schema | Flexibility + Perf | Prefers: read views, analytics | Monitors 5GB/day → 12TB/7yr |
| **SRE** | Reliability | Simplicity > Complexity | Reluctant: +40% ops | Conditional: circuit breaker, runbooks, +2 hire @12mo |
| **Leadership** | ROI, risk | Value > Elegance | Approves: $7.8K for +$150K = 45:1 ROI | Accepts +2 SRE, quarterly reviews |

**Conflicts**: PM (speed) vs SRE (simplicity) → 4mo + safeguards; Dev (simple) vs Biz (perf) → biz wins + mitigation; Sec (compliance) vs Perf → sec wins; SRE (burden) vs Lead (growth) → +2 hire; QA (test) vs PM (speed) → +$1K budget

**Key**: +40% ops + $3.3K/mo → +180% throughput, <200ms, HIPAA, 4mo, 8 team. Mitigation: Kafka exp (4/8), runbooks, +2 SRE @12mo, circuit breakers

## Glossary
**G1. Trade-Off** [EN]: Decision balancing forces (perf vs cost vs maintainability). Optimizes X at Y's expense. Constraint-bounded, stakeholder-dependent, lifecycle ripples. **Related**: Multi-Dimensional, Threshold  
**G2. Competing Forces** [EN]: Conflicting priorities (consistency vs availability, modularity vs simplicity). Requires ≥3 forces, quantified. **Related**: CAP, Triangle  
**G3. Context Threshold** [EN]: Boundary where calculus changes (monolith <10 team, micro >50; SQL <1TB, NoSQL >100TB). Defines "use when". **Related**: Constraint Boundary  
**G4. Lifecycle Ripple** [EN]: Today's decision → future impact (async +20% dev complexity → -40% ops incidents @12mo). Traces design → dev → ops → evolution. **Related**: Debt, Migration Risk  
**G5. Stakeholder Conflict** [EN]: Role disagreement (PM speed, Sec compliance, SRE simplicity). Requires resolution + alignment. **Related**: RACI  
**G6. Constraint Interaction** [EN]: Multiple constraints compound (4-core + $8K + HIPAA → eliminates shared infra). **Related**: Boundary  
**G7. Multi-Dimensional** [EN]: Quantified ≥4 dims: technical (latency, complexity), resource (cost, time), business (revenue, share), operational (SLO, MTTR), risk. **Related**: Quantified  
**G8. Mitigation** [EN]: Address downsides (perf over simplicity → runbooks, training, automation). **Related**: Risk Mgmt  
**G9. CAP** [EN]: Consistency/Availability/Partition—pick 2. Threshold: financial <100 rps → strong, social >10K → eventual. **Related**: Consistency  
**G10. CQRS** [EN]: Command Query Responsibility Segregation—separates writes/reads. +3x read, independent scale. +30% complexity, +35ms write, eventual. Use: read-heavy >10:1, audit. **Related**: Event Sourcing  
**G11. Technical Constraint** [EN]: HW/platform/legacy/stack (CPU, RAM, storage, network, runtime). **Related**: Perf Budget  
**G12. Resource Constraint** [EN]: Time/budget/team (deadlines, cost, size/skills). Drives speed vs quality. **Related**: Scope, TTM  
**G13. Business Constraint** [EN]: Revenue, competition, continuity (pricing, CAC/LTV, share, segments, pressure). Drives innovation vs stability. **Related**: Strategy  
**G14. Org Constraint** [EN]: Stakeholder/process/governance/culture (approval, standards, vendor, risk, remote). Drives standardization vs autonomy. **Related**: RACI  
**G15. Regulatory** [EN]: Legal requirements (GDPR, HIPAA, PCI, SOC 2, ISO, residency, audit). Non-negotiable. **Related**: Security, Governance  
**G16. Operational** [EN]: Runtime limits (SLOs, RTO/RPO, on-call, observability, capacity). Drives availability vs cost. **Related**: SRE, MTTR  
**G17. Ecosystem** [EN]: Vendor/OSS/partner/standard deps (lock-in, SaaS limits, OSS health, protocol, talent). Drives build vs buy. **Related**: Vendor Mgmt  
**G18. Lifecycle Constraint** [EN]: Phase limits (specs, reviews, CI/CD, test env, deploy, CVE SLA, migration). Drives big bang vs incremental. **Related**: SDLC  
**G19. Stakeholder** [EN]: Role (BA, PM, Arch, Dev, QA, Ops, Sec, Data, SRE, Lead). Each evaluates differently. **Related**: RACI, Conflict  
**G20. Lifecycle Phase** [EN]: 8 stages: Requirements, Design, Dev, Test, Deploy, Ops, Maintenance, Evolution. Ripples across. **Related**: SDLC, Ripple  
**G21. Monolith vs Micro** [EN]: Monolith (simple, fast, low latency) vs Micro (scale, autonomy, resilient). <10 team → mono, >50 → micro; <10K rps → mono, >20K → micro. **Related**: Modular Mono  
**G22. Strong vs Eventual** [EN]: Strong (correct, simple) vs Eventual (avail, scale). CAP constraint. Financial/inventory → strong, social/analytics → eventual; <100 rps → strong, >10K → eventual. **Related**: CAP, CQRS

## Tools
**T1. Mermaid** [EN]: Diagrams (flowchart, sequence, class, ER). 2024-10. Free. https://mermaid.js.org  
**T2. OpenAPI** [EN]: REST spec, codegen, contract test. 2024-09. Free. https://www.openapis.org  
**T3. JSON Schema** [EN]: JSON validation, docs, codegen. 2024-08. Free. https://json-schema.org  
**T4. Kubernetes** [EN]: Container orchestration. 2024-10. Free. https://kubernetes.io  
**T5. ADR** [EN]: Decision log, traceability. 2024-06. Free. https://adr.github.io

## Literature
**L1. Evans, E. (2003). *Domain-Driven Design*. Addison-Wesley.** Strategic/tactical, ubiquitous lang, contexts  
**L2. Vernon, V. (2013). *Implementing DDD*. Addison-Wesley.** Context mapping, aggregates, event sourcing  
**L3. Richardson, C. (2018). *Microservices Patterns*. Manning.** Decomposition, data, communication, trade-offs  
**L4. Newman, S. (2021). *Building Microservices* (2nd). O'Reilly.** Boundaries, deployment, testing, security  
**L5. Kleppmann, M. (2017). *Designing Data-Intensive Apps*. O'Reilly.** Distributed: replication, partitioning, transactions  
**L6. Fowler, M. (2002). *Patterns of Enterprise App Architecture*. Addison-Wesley.** Repository, Unit of Work, Service Layer

## Citations
**A1.** Evans, E. (2003). *Domain-driven design*. Addison-Wesley. [EN]  
**A2.** Richardson, C. (2018). *Microservices patterns*. Manning. [EN]  
**A3.** 周爱民. (2021). *架构的本质*. 电子工业出版社. [ZH]  
**A4.** Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley. [EN]  
**A5.** Fowler, M. (2002). *Patterns of enterprise application architecture*. Addison-Wesley. [EN]  
**A6.** Newman, S. (2021). *Building microservices* (2nd). O'Reilly. [EN]  
**A7.** Kleppmann, M. (2017). *Designing data-intensive applications*. O'Reilly. [EN]  
**A8.** Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns*. Addison-Wesley. [EN]  
**A9.** 张逸. (2019). *领域驱动设计实践*. 电子工业出版社. [ZH]  
**A10.** Skelton, M., & Pais, M. (2019). *Team topologies*. IT Revolution. [EN]  
**A11.** Humble, J., & Farley, D. (2010). *Continuous delivery*. Addison-Wesley. [EN]  
**A12.** Kim, G., et al. (2016). *The DevOps handbook*. IT Revolution. [EN]
