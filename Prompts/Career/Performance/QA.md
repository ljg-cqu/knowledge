# Performance Engineering Q&A Generator (Minimal Viable)

Generate 2-4 decision-critical Q&As for performance engineering—minimal viable tracking for informed decisions with limited time.

## Context & Scope

**Problem**: Inconsistent performance advice leading to suboptimal decisions, hallucinations in optimization strategies, incomplete bottleneck analysis.
**Scope**: Decision-critical topics—bottleneck analysis, optimization strategies, tool evaluation, architectural patterns. Applicable to systems with measurable SLOs, from low-volume to high-scale.
**Constraints**: Assumes basic performance knowledge; focuses on production-ready solutions.
**Assumptions**: Users typically have access to profiling tools and observability (APM/logs/traces); adapt if tools are unavailable.
**Scale**: Individual engineers to large teams.
**Timeline**: Immediate use; 30-60s pre-send check; assume bi-weekly regeneration.
**Stakeholders**: Performance Engineers, SREs, Backend Developers, Architects, DevOps.
**Resources**: Any capable LLM plus standard profiling tools.
**Domain**: Web/cloud/microservices/distributed/real-time/data-intensive systems.
**Exclude**: Hardware selection, network topology, vendor comparisons, non-performance concerns.
**Cadence**: Bi-weekly | 1-2h effort | Expires: 2 weeks.

## Requirements

**Quantity**: 2-4 Q&A pairs.
**Difficulty**: 25% Foundational, 50% Intermediate, 25% Advanced.
**Coverage**: Balance across 4 dimensions (Latency, Throughput, Scalability, Resources) and 4 phases (Measure/Analyze/Optimize/Validate).
**Answer Format**: 150-250 words prose (excluding code/diagrams), with [Ref: ID]; include Mermaid diagrams, YAML/JSON/code as needed; APA 7th citations [EN]/[ZH].
**Performance Chain**: SLO → Measure → Analyze (Bottleneck) → Optimize → Validate → Quantified Impact (required).
**Per Cluster (1-2 total)**: ≥1 diagram, ≥1 practical element, ≥1 metrics table.

**Decision Criticality**: Satisfy ≥1 of: Blocks decision, Creates risk, Affects ≥2 roles, Requires action (1-6mo), Quantified impact.
**Clarity**: Glossary-defined terms [G: Term]; numeric specifics ("p99 <50ms" not "fast").
**Precision**: Specific values; exact [Ref: ID]; quantified thresholds.
**Accuracy**: Cross-check formulas/benchmarks; flag assumptions; prefer tools updated within ≤18mo (justify older ones).
**Credibility**: Benchmarks ≤3yr; peer-reviewed/production case studies; authoritative sources.
**Significance**: High-impact (≥20% gain or critical path); proven bottlenecks.
**Concision**: Minimize redundancy; prefer tables/diagrams over prose.
**Risk/Value**: Explicit cost-benefit; ≥1 alternative with trade-offs; mitigation for high-risk.
**Fairness**: Balanced trade-offs; acknowledge limitations/assumptions.

## Key Elements

### Performance Dimensions

| Dimension | Focus | Criticality | Key Metrics | When Critical |
|-----------|-------|-------------|-------------|---------------|
| Latency | Minimize response time | SLO compliance | p50/p95/p99, TTFB | >20% degradation |
| Throughput | Maximize requests/sec | Capacity planning | RPS, error rate | Traffic spikes |
| Scalability | Handle growth | Roadmap blocking | Scalability factor, cost/req | 10x+ growth |
| Resources | Optimize CPU/memory/I/O/cost | Cost/reliability risk | CPU %, Memory %, Cost $ | >20% cost increase |

### Optimization Patterns

| Pattern | Context | Advantage | Trade-offs | Gains | Risk/Mitigation |
|---------|---------|-----------|------------|-------|-----------------|
| Caching | Read-heavy (>80%) | 40-95% latency ↓ | Consistency vs speed | 40-60% latency ↓ | Stale data; TTL/invalidation |
| Connection Pooling | High overhead | 10-100x reuse | Pool size vs limits | 50-90% latency ↓ | Leaks; detection |
| Async Processing | Long tasks | Improved throughput | Immediate vs completion | 2-10x throughput | Lost messages; queues |
| DB Optimization | Query bottlenecks | 10-1000x speedup | Read vs write | 10-1000x speedup | Slow writes; selective indexes |
| Horizontal Scaling | Stateless | Linear scaling | Cost vs capacity | To 100s nodes | Uneven load; hashing |

### Visuals & Formulas

| Type | Diagram | Formula & Target | When to Use |
|------|---------|------------------|-------------|
| Profiling | Flamegraph | CPU Time = Σ(function time); >80% identified | Bottlenecks |
| Bottleneck | Sequence | Bottleneck Factor = Component/Total; Amdahl's speedup | Multi-component |
| Caching | Cache flow | Hit Rate = Hits/(Hits+Misses) × 100% (≥95%) | Read-heavy |
| Load Testing | Performance curve | Throughput vs Load; Breaking point | Capacity validation |
| Optimization | Before/after | Improvement % = (Baseline - Optimized)/Baseline × 100% | Impact quantification |

## Q&A Guidelines

**Design Principles**: Decision-critical (blocks decisions or creates risk), real-world (production-like scenarios with constraints/SLOs), actionable (concrete next steps), evidence-based (proven patterns/benchmarks).

Examples:
- Good: "80% latency in DB queries. Pooling vs caching for 4K rps?"
- Poor: "What is profiling?"

Stakeholder Focus: Profiling/optimization (Engineers), SLO/monitoring (SREs), Code tuning (Developers), Design patterns (Architects), Infrastructure (DevOps).

**Mandatory Elements**: Scenario context with constraints/SLOs/bottleneck [Ref: ID]; ≥1 decision criticality criterion; complete performance chain; practical code/config (5-30 lines); ≥1 citation; key insight with quantified impact; explicit trade-offs; ≥1 alternative; risk/mitigation strategies.

## Reference Requirements

- ≥4 Glossary [G#]: Definitions, formulas, targets, usage.
- ≥2 Tools [T#]: Purpose, pricing, last update, integrations, URL (prefer ≤18mo).
- ≥3 Literature [L#]: Citations, coverage, key sections.
- ≥5 Citations [A#]: APA 7th [EN]/[ZH]; DOI/URLs.

## Quality Gates

| # | Gate | Requirement | Threshold |
|---|------|-------------|-----------|
| 1 | Decision Criticality | ≥1 criterion | 100% |
| 2 | Quantity | 2-4 Q&As | 2-4 |
| 3 | Difficulty | 25/50/25 F/I/A | ±10% |
| 4 | Performance Chain | Complete | 100% |
| 5 | Practical Elements | ≥1 per Q&A | 100% |
| 6 | Citations | ≥1 per answer | 100% |
| 7 | Trade-offs | Explicit + ≥1 alternative | 100% |
| 8 | Quantified Impact | Numeric | 100% |
| 9 | Reference Floors | G≥4, T≥2, L≥3, A≥5 | Met |
| 10 | Clarity | All terms defined | 100% |

## Workflow

1. Plan Topics: 1-2 clusters (e.g., Latency, Throughput); plan 2-4 Q&As total (≈1-2 per cluster); 25/50/25 difficulty.
2. Build References: Glossary → Tools → Literature → Citations; verify recency/diversity.
3. Write Q&As: Scenario-driven; 150-250 words; include all elements; validate incrementally.
4. Add Visuals: ≥1 diagram, metrics table, practical per cluster.
5. Complete References: Full details; cross-check.
6. Validate: Against 12 gates.

## Output Format

```markdown
# Performance Engineering Q&A ([Period])

## Contents
1. Executive Summary: 2-3 insights; dashboard.
2. Q&A by Cluster (2-4 total, 1-2 clusters).
3. References (≥4 G, ≥2 T, ≥3 L, ≥5 A).
4. Validation Results (10 gates).

## Context & Coverage
Domain/Audience/Constraints/In Scope/Out of Scope.

### Coverage Matrix
| Dimension \ Phase | Measure | Analyze | Optimize | Validate |
|-------------------|---------|---------|----------|----------|
| Latency | Q# | Q# | Q# | Q# |
| Throughput | Q# | Q# | Q# | Q# |
| Scalability | Q# | Q# | Q# | Q# |
| Resources | Q# | Q# | Q# | Q# |

## Q&A by Cluster

### Cluster 1: [Name]

#### Q1: [Question]
**Difficulty**: [F/I/A] | **Dimension**: [Latency/etc] | **Phase**: [Measure/etc]
**Key Insight**: [Quantified impact] [Ref: ID]

**Answer** (150-250 words): [Performance Chain with [Ref: ID]]

**Practical** (5-30 lines): ```yaml ... ```

**Visual**: ```mermaid ... ```

**Metrics**:
| Metric | Formula | Baseline | Optimized | Improvement | Rationale |
|--------|---------|----------|-----------|-------------|-----------|
| ... | ... | ... | ... | ... | ... |

**Trade-offs**: ...
**Alternatives**: ...
**Risk/Mitigation**: ...
**Validation**: ...

## References

### Glossary
**G1. p50/p95/p99**: Definition, formula, targets, usage.

### Tools
**T1. k6**: Purpose, pricing, update, integrations, URL.

### Literature
**L1. Gregg (2020)**: Citation, coverage, sections.

### Citations
**A1. Dean & Barroso (2013)**: Citation [EN].

## Validation Results
| # | Gate | Status | Evidence |
|---|------|--------|----------|
| ... | ... | PASS | ... |
```

## Example Validation
| # | Gate | Status | Evidence |
| 1 | Decision Criticality | PASS | All satisfy ≥1 |
| 2 | Quantity | PASS | 2-4 Q&As |
| 3 | Difficulty | PASS | 25/50/25 F/I/A |
| 4 | Performance Chain | PASS | Complete |
| 5 | Practical Elements | PASS | ≥1 per Q&A |
| 6 | Citations | PASS | ≥1 per answer |
| 7 | Trade-offs | PASS | Explicit + ≥1 alternative |
| 8 | Quantified Impact | PASS | Numeric |
| 9 | Reference Floors | PASS | G≥4, T≥2, L≥3, A≥5 |
| 10 | Clarity | PASS | All terms defined |

**Summary**: All gates PASS.
