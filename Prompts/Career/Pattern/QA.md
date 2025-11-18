---
last_updated: 2025-11-18
status: Reviewed
owner: ljg-cqu
---

# Pattern-Based Q&A Generation Template

## Overview

Generate 8-12 decision-critical Q&As for career development patterns across 4-6 MECE domains.

**Scale**: 8-12 Q&As; 10-15min/question.

**Timeline**: Interview (90-120min) or self-study; immediate use.

**Stakeholders**: Developers, Architects, SREs, DevOps, Security Engineers, Data Engineers, Compliance Officers.

**Output**: Concise answers with ≥12 glossary, ≥6 tools, ≥6 literature, ≥8 citations.

**Success**: All criteria pass, 100% decision-critical, ≥80% with Tier 1-2 citations.

**Key Terms**:
- **F/I/A**: **F**=Foundational (execution), **I**=Intermediate (strategy/trade-offs), **A**=Advanced (portfolio/vision)
- **MECE**: Mutually Exclusive, Collectively Exhaustive
- **RFC 2119**: MUST/SHOULD/MAY
- **Decision Criticality**: Patterns blocking decisions, creating risk, affecting ≥2 roles, evolving, or with high adoption barriers

## Requirements
- **Q&As**: 8-12 total (2F/4I/2-6A; concise)
- **References**: ≥12 glossary, ≥6 tools, ≥6 literature, ≥8 citations
- **Domains**: 4-6 decision-critical (MECE)
- **Patterns**: 8-12 across domains
- **Validation**: All criteria pass; 100% patterns meet ≥1 criticality criterion; critical claims cited with Tier 1-2 sources; MECE domains; accessible links

## Decision-Criticality Framework
**Include if ≥1 criterion satisfied**:
- **Blocks Decision**: Architecture, technology, business, market, or strategy choices
- **Creates Risk**: Material threat (performance, reliability, security, compliance issues)
- **Affects ≥2 Stakeholder Roles**: Multi-team impact
- **Requires Action**: 1-18mo implementation window (actively evolving)
- **Quantified Impact**: Measurable metrics (adoption barrier >40h effort, performance %, cost impact)

**Exclude if**:
- Niche/legacy (<5% adoption)
- Nice-to-have (no decision impact)
- Already covered

## Content Guidelines
### Pattern Quality
1. Reusability: ≥2 contexts
2. Effectiveness: ≥1 company, ≥1 metric [Ref: ID]
3. Boundaries: "Applies when" + "Avoid when"
4. Stakeholders: ≥2 groups
5. Trade-offs: ≥1 benefit, ≥1 cost
6. Anti-patterns: ≥1 failure mode

### Answer Structure (5-Step)
1. Claim
2. Rationale
3. Evidence [Ref: ID]
4. Implications (≥2 stakeholders)
5. Trade-offs & Boundaries

### Evidence Standards
**Tiers** (prioritize 1-2):
1. Peer-reviewed/standards/regulations
2. Vendor docs/authoritative books
3. Org blogs/analyst reports
4. Expert blogs/conferences/OSS
5. Forums

**Citations**:
- Critical: ≥1 Tier 1-2, SHOULD ≥2 sources
- Supporting: ≥1 for non-obvious
- Recency: <3yr (fast-moving), <10yr (stable)
- Format: Author/Org (Year). _Title_. URL/DOI [Lang]. Inline: [Ref: ID]

### Best Practices
- Use 5-step template
- Justify criticality
- Cite claims (Tier 1-2)
- ≥2 perspectives
- Explicit boundaries/trade-offs
- Examples (code/diagram)
- RFC 2119 terms
- Prioritize high-impact

**Prohibited**: Vague language, Tier 5 for critical claims, omitting anti-patterns, universal claims, dead links, unsubstantiated claims, non-critical patterns

## Domains (MECE)
Select 4-6:

| Domain | Examples | Stakeholders |
|--------|----------|--------------|
| Regulatory | Audit trails, Consent | Compliance, Legal, Devs |
| Business | Subscription, Freemium | Execs, Product, Finance |
| Market | Blue Ocean, Innovation | Execs, Marketing, Product |
| Technical | GoF, Repository | Devs, Architects |
| Data | Polyglot, Event Sourcing | Data Eng, DBAs, Architects |
| Organizational | Conway's Law, DevOps | Managers, Execs, Leads |
| NFR | Security, Performance, etc. | Devs, Ops, Architects, Security |
| Process | Agile, Incident Response | Teams, Managers |
| Hybrid | Regulatory+Technical | Compliance, Devs |

## Validation Criteria
- Reference counts: Glossary ≥12, Tools ≥6, Literature ≥6, Citations ≥8; Q&As 8-12
- Citation coverage: ≥80% ≥1 citation, ≥50% ≥2
- Languages: Mix EN/ZH/other
- Recency: ≥50% <3yr; accessible links
- Word count: Sample 5 Q&As ~150-250 words
- Criticality: 100% meet ≥1 criterion
- Insights: Boundaries/trade-offs/anti-patterns
- Per-topic: ≥1 source + ≥1 tool
- Visuals: ≥70% with diagram/table/metric
- Evidence: ≥80% empirical
- Quantitative: ≥70% with metrics
- Examples: ≥80% domain-appropriate

## Workflow
1. Plan: Select domains/Q&As; verify MECE/criticality
2. Draft: Gather refs; write Q&As (5-step, cited); add visuals
3. Validate: Check 12 steps; iterate
4. Finalize: Verify all constraints

## Output Structure
- Title
- Contents [TOC]
- Context [2-3 sentences]
- Decision Criticality Framework
- Topic Areas [Table: domains, Q# ranges, levels, criticality]
- Topics [Per domain: Q&As with level/domain/criticality/insight/answer (5-step)/criteria/example/artifacts]
- References [Glossary ≥12, Tools ≥6, Literature ≥6, Citations ≥8]
- Validation Report [12 steps PASS/FAIL]

## Artifacts by Domain
| Domain | Diagrams | Examples | Metrics |
|--------|----------|----------|---------|
| Regulatory | Compliance flow | GDPR YAML | Compliance % |
| Business | Canvas | Revenue models | CLV, CAC |
| Technical | Sequence | Pattern code | Coupling % |
| Data | ERD | DDL/SQL | Normalization |
| Organizational | Team topology | Team structure | Alignment % |
| NFR-Security | Threat model | Security config | Vulnerabilities |
| NFR-Performance | Latency breakdown | Flamegraph | p50/p95/p99 |
| NFR-Availability | Failure tree | Health checks | Uptime % |
| NFR-Reliability | Retry flow | Idempotency | Recovery % |
| NFR-Observability | Tracing | Distributed traces | MTTD |
| NFR-Scalability | Scaling strategy | Horizontal scaling | Factor |
| NFR-Adaptability | Feature flags | Toggle code | Lead Time |
| NFR-Extensibility | Extension map | Plugin registry | #extensions |
| NFR-Maintainability | Layered diagram | Refactoring diff | Churn |
| NFR-Testability | Test pyramid | Contract tests | Coverage |
| Market | Market map | Blue Ocean canvas | Share % |
| Process | Workflow | Kanban board | Cycle time |
| Hybrid | Cross-domain map | Compliance flow | Risk score |

## Pattern Catalog
Select/adapt 8-12 patterns.

| Domain | Pattern | Contexts | Evidence | Stakeholders | Criticality |
|--------|---------|----------|----------|--------------|-------------|
| Regulatory | Double-Entry Audit | Financial, Healthcare | SOX | Compliance, Devs | Blocks |
| | Consent Mgmt | GDPR, CCPA | 10K+ orgs | Legal, Users, Devs | Risk |
| Business | Subscription | SaaS, Retail | $1.5T market | Finance, Product | Blocks |
| Technical | Repository | DDD | 60-80% coupling↓ | Devs, Architects | Blocks |
| Data | Event Sourcing | Finance | 100% audit | Compliance, Devs | Risk |
| Organizational | Conway's Law | Any org | 40% coordination↓ | Execs, Managers | Blocks |
| | DevOps | Cloud-native | 60% MTTR↓ | Devs, Ops | Blocks |
| NFR-Security | Zero-Trust | Remote work | 75% breach↓ | Security, Devs | Risk |
| NFR-Reliability | Retry+Backoff | Networks | 95% recovery | Devs, Ops | Blocks |
| NFR-Scalability | Horizontal Scaling | Web apps | 1000s instances | Ops, Architects | Blocks |
| NFR-Adaptability | Feature Flags | CD, A/B | 90% risk↓ | Devs, Product | Blocks |

## Quick Check
☐ Self-contained | ☐ Context/Clarity/Precision/Relevance | ☐ MECE/Sufficiency/Breadth/Depth | ☐ Significance/Priority/Conciseness/Accuracy/Credibility | ☐ Logic/Risk-Value/Fairness | ☐ Structure/Consistency | ☐ Evidence/Verification/Practicality/Success Criteria


