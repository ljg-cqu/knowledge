# Pattern-Based Q&A Generation Template

Generate 30 evidence-based Q&As (6 Foundational, 12 Intermediate, 12 Advanced; 150-300 words each) with proven patterns, multi-stakeholder value, and explicit boundaries.

## Core Requirements

**Mandatory Outputs**:
- 30 Q&As: 6 Foundational, 12 Intermediate, 12 Advanced (150-300 words each)
- References: ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations
- Pattern Catalog: 70+ patterns across 11 domains
- Validation: All 21 steps PASS with original thresholds
- Pattern Quality: ALL 7 criteria for each pattern

**Key Terms** (RFC 2119):
- **MUST**: Mandatory requirement
- **SHOULD**: Strong recommendation
- **MAY**: Optional

**11 Domains** (MECE coverage):
Regulatory, Business, Market, Technical, Data, Organizational, NFR (Security, Performance, Availability, Reliability, Scalability, Observability, Adaptability, Extensibility, Maintainability, Testability), Process, Hybrid

**Format Standards**:
- GitHub-Flavored Markdown, ≤120 char/line
- Direct, authoritative links (archive if dead)
- Evidence cited as [Ref: ID]
- Tables, lists, diagrams, code blocks, formulas

---

# Part I: Quality Standards

## Pattern Quality Criteria (ALL 7 Required)

Each pattern MUST meet ALL 7 criteria with specific evidence:

1. **Reusability**: ≥2 contexts, adaptation points, context-specific examples
2. **Proven Effectiveness**: ≥1 company, ≥1 metric, authoritative source [Ref: ID]
3. **Applicability Boundaries**: "Applies when" + "Avoid when" conditions, ≥1 example
4. **Multi-Stakeholder Value**: ≥2 stakeholder groups, value to each, concerns addressed
5. **Functional + NFR Coverage**: Functional description + ≥1 NFR attribute with metrics
6. **Trade-offs**: ≥1 benefit, ≥1 sacrifice, comparative framing ("improves X at expense of Y")
7. **Anti-Patterns**: ≥1 failure mode, exclusion criteria, mitigation strategies

## Answer Structure (6-Step Template)

Every answer MUST follow this reasoning chain:

1. **Claim**: State pattern/principle clearly
2. **Rationale**: Explain mechanism and causality
3. **Evidence**: Cite empirical data [Ref: ID]
4. **Implications**: Describe consequences across stakeholders
5. **Limitations**: Acknowledge constraints, assumptions, failure modes
6. **Alternatives**: Identify when other approaches are preferable

## Evidence Standards

### Source Tiers (Prioritize 1-2)

**Tier 1**: Peer-reviewed papers, standards (ISO/NIST/IETF), regulations (GDPR/CCPA), formal specs
**Tier 2**: Official vendor docs (AWS/Azure/GCP), authoritative books (O'Reilly), established frameworks
**Tier 3**: Reputable org blogs (Netflix, Martin Fowler), analyst reports (Gartner/Forrester)
**Tier 4**: Expert blogs, conference talks, OSS project docs
**Tier 5**: Forums (Stack Overflow, Reddit), Q&A sites

### Citation Requirements

**Critical Claims**: ≥1 Tier 1-2 source; SHOULD have ≥2 independent sources
**Supporting Claims**: ≥1 citation for non-obvious statements
**Recency**: <3 years (fast-moving), <10 years (stable domains)
**Languages**: ~60% EN, ~30% ZH, ~10% other
**Format**: Author/Org. (Year). _Title_ [Edition]. URL/DOI. [Language]. Inline: [Ref: CitationID]

## Pattern Domains (MECE)

| Domain | Examples | Stakeholders |
|--------|----------|--------------|
| **Regulatory** | Audit trails, Consent, Data residency | Compliance, Legal, Developers |
| **Business** | Subscription, Freemium, Platform | Executives, Product, Finance |
| **Market** | Blue Ocean, Disruptive Innovation, Land & Expand | Executives, Marketing, Product |
| **Technical** | GoF patterns, Repository, Strangler Fig | Developers, Architects |
| **Data** | Polyglot Persistence, Event Sourcing, CQRS | Data Engineers, DBAs, Architects |
| **Organizational** | Conway's Law, Team Topologies, DevOps | Managers, Executives, Team Leads |
| **NFR-Security** | Zero-Trust, Defense-in-Depth, Secrets Mgmt | Security, Compliance |
| **NFR-Performance** | Caching, Connection Pooling, CDN | Developers, Operations |
| **NFR-Availability** | Circuit Breaker, Bulkhead, Health Checks | Operations, Business |
| **NFR-Reliability** | Retry+Backoff, Idempotency, Saga | Developers, Operations |
| **NFR-Scalability** | Horizontal Scaling, Sharding, CQRS | Architects, Operations |
| **NFR-Observability** | Distributed Tracing, Metrics, Logging | Operations, Developers |
| **NFR-Adaptability** | Feature Flags, Strategy, Plugin Arch | Developers, Product |
| **NFR-Extensibility** | DI, Open-Closed, Middleware | Developers, Architects |
| **NFR-Maintainability** | SOLID, Clean Architecture | Developers, Architects |
| **NFR-Testability** | Test Doubles, Contract Testing | Developers, QA |
| **Process** | Agile, Retrospectives, Incident Response | Teams, Managers |
| **Hybrid** | Regulatory+Technical, Compliance-by-Design | Compliance, Developers |

## 21-Step Validation (All MUST PASS)

### References (Steps 1-7)
1. **Counts**: Glossary ≥25, Tools ≥10, Literature ≥12, Citations ≥12; Q&As 30 (6/12/12 F/I/A)
2. **Citation Coverage**: ≥70% answers ≥1 cite, ≥30% ≥2 cites
3. **Languages**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% <3yr (≥70% digital/cloud)
5. **Diversity**: ≥3 source types, no type >25%
6. **Links**: All accessible or archived
7. **Resolution**: All [Ref: ID] resolve; Tools: pricing + adoption + last update <18mo

### Content (Steps 8-12)
8. **Word Count**: 5 samples all 150-300
9. **Insights**: All concrete (boundaries/trade-offs/effectiveness/anti-patterns)
10. **Per-Topic**: ≥2 sources + ≥1 tool
11. **Traceability**: ≥80% pattern → implementation
12. **Scenarios**: ≥70% judgment-based

### Patterns (Steps 13-21)
13. **Visuals**: ≥90% with diagram + example + table + metric
14. **Evidence**: ≥80% patterns with empirical proof
15. **Quantitative**: ≥60% with metrics/formulas
16. **Examples**: ≥80% domain-appropriate
17-21. **7 Criteria**: ≥80% answers meet ALL 7 pattern criteria

## Best Practices

**Required Actions**:
- Apply 6-step template (Claim → Rationale → Evidence → Implications → Limitations → Alternatives)
- Cite critical claims with Tier 1-2 sources (≥2 sources preferred)
- Present ≥2 stakeholder perspectives per pattern
- Define boundaries explicitly ("Applies when", "Avoid when")
- Document trade-offs ("Improves X at expense of Y")
- Include concrete examples (code/YAML/diagrams)
- Use RFC 2119 terms consistently (MUST/SHOULD/MAY)
- Keep lines ≤120 characters

**Prohibited Actions**:
- Vague language ("as needed", "where appropriate") without clarification
- Tier 5 sources for critical claims
- Omitting failure modes and anti-patterns
- Presenting patterns as universally applicable
- Dead links (archive if unavailable)

---

# Part II: Workflow

## 4-Stage Workflow

### A. Plan
**Objective**: Establish scope, verify MECE coverage

**Tasks**:
1. Select 8-12 pattern clusters across 11 domains
2. Allocate 30 Q&As (6F/12I/12A) across clusters
3. Verify MECE domain coverage and 7 criteria understanding

**Gate**: ✓ 8-12 clusters, ✓ 30 Q&As allocated (6/12/12), ✓ MECE verified

### B. Draft
**Objective**: Generate content and artifacts

**Tasks**:
1. **References**: Collect ≥25/≥10/≥12/≥12 (glossary/tools/literature/citations)
   - Languages: ~60% EN, ~30% ZH, ~10% other
   - Recency: ≥50% <3yr, prefer Tier 1-2 sources
2. **Q&As**: Write 30 scenario-based Q&As (150-300 words)
   - Apply 6-step template, ALL 7 criteria per pattern
   - ≥1 [Ref: ID] per answer, ≥2 stakeholder views
   - Concrete examples (code/YAML/diagrams)
   - Validate every 5 Q&As
3. **Visuals**: Mermaid + example + table + metric per cluster

**Gate**: ✓ 30 Q&As (150-300 words), ✓ References (≥25/≥10/≥12/≥12), ✓ Languages ~60/30/10, ✓ Recency ≥50% <3yr, ✓ Visuals per cluster, ✓ Citations in ≥70%

### C. Validate
**Objective**: Execute 21-step validation

**Tasks**:
1. Run all 21 validation steps
2. Document failures
3. Fix all failures and re-validate until 100% PASS

**Gate**: ✓ All 21 steps PASS, ✓ No broken links, ✓ No placeholders, ✓ ≥80% meet 7 criteria

### D. Finalize
**Objective**: Complete review and submission

**Tasks**:
1. Verify constraints (structure, 30 Q&As, 21 steps, 70+ patterns, references)
2. Ensure 100% critical claims have evidence
3. Verify MECE boundaries and submission checklist

**Gate**: ✓ Constraints met, ✓ 100% critical claims cited, ✓ Checklist complete

---

# Part III: Output Structure

## Required TOC

```markdown
## Contents
- [Topic Areas](#topic-areas) - Q1-30 Overview
- [Topic 1: Domain](#topic-1) (Q1-QX) [F/I/A]
- [References](#references): [Glossary](#glossary) (≥25) | [Tools](#tools) (≥10) | [Literature](#literature) (≥12) | [Citations](#citations) (≥12)
- [Validation Report](#validation-report)
```

## Output Template

```markdown
# [Title]

## Contents
[See Required TOC]

## Context
[Scope, constraints, target audience - 2-3 sentences]

## Topic Areas
[Table: 11 domains, Q# ranges, F/I/A distribution]

## Topic 1: [Domain]

### Q1: [Question]
**Level**: [Foundational/Intermediate/Advanced] | **Domain**: [Type] | **Insight**: [Boundaries/Trade-offs/Anti-patterns]

**Answer** (150-300 words): [6-step template with [Ref: ID] citations]

**7 Pattern Criteria**:
1. **Reusability**: ≥2 contexts, adaptation points
2. **Effectiveness**: Company + metrics + [Ref: ID]
3. **Boundaries**: "Applies when" + "Avoid when" + example
4. **Stakeholders**: ≥2 groups, value, concerns
5. **NFR**: Functional + ≥1 NFR + metrics
6. **Trade-offs**: Benefits vs. sacrifices ("X at expense of Y")
7. **Anti-Patterns**: Failure modes + exclusions + mitigations

**Example**: [Code/YAML/diagram]
**Artifacts**: [Mermaid + table + metrics]

[Repeat Q2-Q30]

## References

### Glossary (≥25)
[Alphabetical, definitions, [Language]]

### Tools (≥10)
[Features, pricing, adoption, last verified <18mo, URL]

### Literature (≥12)
[APA 7th, [Language]]

### Citations (≥12)
[APA 7th, [Language], IDs match [Ref: ID]]

## Validation Report
[21 steps: PASS/FAIL]
```

## Supporting Artifacts by Domain

| Domain | Diagrams | Examples | Metrics |
|--------|----------|----------|---------|
| **Regulatory** | Compliance flow, Audit trail | GDPR consent YAML | Compliance %, Audit Completeness |
| **Business** | Business model canvas, Value chain | Revenue models | CLV, CAC, MRR |
| **Market** | Blue Ocean canvas, Porter's 5 Forces | Market positioning | Market Share %, Value Innovation |
| **Technical** | Class/Sequence/Component | Pattern code | Reusability %, Coupling |
| **Data** | ERD, Data flow, Lineage | DDL/SQL, Schema | Normalization, Query Perf |
| **Organizational** | Org chart, Team topology | Team structure | Conway Alignment %, Cognitive Load |
| **NFR-Security** | Threat model, Auth flow | Security config | Attack Surface, Vulnerabilities |
| **NFR-Performance** | Flamegraph, Latency breakdown | Cache strategy | Latency (p50/p95/p99), Throughput |
| **NFR-Availability** | Failure tree, Redundancy | Circuit breaker, Health checks | Uptime %, MTBF/MTTR |
| **NFR-Reliability** | Retry flow, Saga | Idempotency keys | Error Recovery %, Consistency |
| **NFR-Scalability** | Scaling strategy, Sharding | Horizontal scaling | Scalability Factor, Linear Scaling % |
| **NFR-Observability** | Tracing, Metrics dashboard | Distributed traces | Trace Coverage %, MTTD |
| **NFR-Adaptability** | Feature flags, Strategy | Toggle code | Deployment Frequency, Lead Time |
| **NFR-Extensibility** | DI container, Extension points | DI config, Middleware | Extension Points, 3rd-party Integrations |
| **NFR-Maintainability** | Clean architecture, SOLID | Refactored code | Cyclomatic Complexity, Tech Debt % |
| **NFR-Testability** | Test pyramid, Mock architecture | Test doubles, Pact | Coverage %, Test Exec Time |
| **Process** | BPMN workflow, Kanban | Process docs | Cycle Time, Lead Time, Efficiency % |
| **Hybrid** | Cross-domain diagrams | Multi-domain examples | Domain-specific + integration |

## Pattern Catalog (70+)

| Domain | Pattern | Contexts | Evidence | Stakeholders |
|--------|---------|----------|----------|--------------|
| **Regulatory** | Double-Entry Audit Trail | Financial, Healthcare, Blockchain | SOX required, all major banks | Compliance, Developers, Auditors |
| | Consent Management | GDPR, CCPA, Marketing | 10K+ orgs, 85% risk↓ | Legal, End Users, Developers |
| | Data Residency | Multi-region cloud, Fintech | AWS/Azure/GCP standard | Compliance, Ops, Business |
| **Business** | Subscription Model | SaaS, Media, Retail | $1.5T economy, 5-7x valuations | Finance, Product, Customers |
| | Freemium | Dev tools, Productivity | Slack 30%, Dropbox $2B | Marketing, Product, Users |
| | Platform/Marketplace | Airbnb, AWS, App Store | 7/10 top companies, 70% margins | Business, Producers, Consumers |
| **Market** | Blue Ocean Strategy | New categories | Cirque $800M, Wii 100M units | Executives, Product, Marketing |
| | Disruptive Innovation | Tech transitions | Netflix/Tesla, 30+ industries | Executives, Investors, Market |
| | Land and Expand | Enterprise SaaS | Slack/Dropbox, 120%+ retention | Sales, Product, Finance |
| **Technical** | Repository | DDD, Layered arch | 60-80% coupling↓ | Developers, Architects, Ops |
| | Strangler Fig | Legacy modernization | Amazon/GitHub, 90% risk↓ | Architects, Ops, Business |
| **Data** | Polyglot Persistence | Microservices, E-commerce | Netflix 3+, LinkedIn 10+, 50-80% latency↓ | Architects, DBAs, Developers |
| | Event Sourcing | Finance, Collaboration | 100% audit, Banking standard | Compliance, Developers, Business |
| | Data Lake | Analytics, ML | AWS/Azure/GCP, 90% F500 | Data scientists, Engineers, Business |
| **Organizational** | Conway's Law | Any software org | 50+ years proven, 40% coordination↓ | Executives, Architects, Managers |
| | Two-Pizza Team | Product/Platform teams | Amazon 2002, 60% meetings↓, 30% velocity↑ | Managers, Developers, Executives |
| | Team Topologies | Any org | MS/Google/Spotify, 50% load↓, 40% flow↑ | CTOs, Managers, Developers |
| | DevOps/YBIYRI | Cloud-native, SaaS | Amazon 2006, 60% MTTR↓, 10x deploys | Developers, Ops, Business |
| **NFR-Security** | Defense-in-Depth | Enterprise, Cloud, IoT | 90% attack↓, 95% F500 | Security, Compliance, Ops |
| | Zero-Trust | Remote work, Cloud-native | Google 7yr/85K, 75% breach impact | Security, Developers, Users |
| | Secrets Management | Cloud, Microservices | 30M+ Vault, 50% F500 | Security, Developers, Ops |
| **NFR-Performance** | Caching | Web apps, APIs | 40-60% latency↓, 10x throughput | Users, Developers, Ops |
| | Connection Pooling | DB, HTTP, Queues | 10-100x gain, DB standard | Developers, Ops, Users |
| | CDN | Static assets, Video | 50-70% latency↓, 70% top sites | Users, Business, Ops |
| **NFR-Availability** | Circuit Breaker | Microservices | Netflix 99.99% uptime | Ops, Developers, Users |
| | Bulkhead | Thread pools, Multi-tenant | Netflix/AWS, 80% capacity maintained | Ops, Architects, Business |
| | Health Check | K8s, Load balancers | 70% MTTR↓, <5s detection | Ops, Developers, Business |
| **NFR-Reliability** | Retry + Backoff | Network, Messages | 95% recovery, AWS default | Developers, Ops, Users |
| | Idempotency | Payments, Queues, APIs | Stripe/PayPal required, 100% consistency | Developers, Ops, Business |
| | Saga | Microservices, Long txns | Uber/Airbnb standard | Architects, Developers, Ops |
| **NFR-Scalability** | Horizontal Scaling | Web servers, APIs | Netflix/FB, 1000s instances | Ops, Architects, Business |
| | DB Sharding | High-traffic DB | Instagram 4000, Discord billions | DBAs, Developers, Business |
| | CQRS | Read-heavy, Event sourcing | 10-100x read scale, Azure/AWS | Architects, Developers, Ops |
| **NFR-Observability** | Distributed Tracing | Microservices | Standard cloud-native | Ops, Developers, Business |
| **NFR-Adaptability** | Feature Flags | CD, A/B testing | FB/Netflix 100+ deploys/day, 90% risk↓ | Developers, Product, Business |
| | Strategy Pattern | Payments, Pricing | GoF 1994, 60% duplication↓ | Developers, Business, Architects |
| | Plugin Architecture | IDEs, Browsers | VS Code 40K, WordPress 60K | Developers, Third-party, Users |
| **NFR-Extensibility** | Dependency Injection | Enterprise, Frameworks | Spring 50% share, 70% coupling↓ | Developers, Architects, Third-party |
| | Open-Closed | Libraries, APIs | SOLID 1988, 80% regression bugs↓ | Developers, QA, Business |
| | Middleware/Pipeline | Web frameworks | Express 100K packages | Developers, Third-party, Ops |
| **NFR-Maintainability** | SOLID Principles | OOP, Enterprise apps | Since 2000, 40-60% defects↓, 25% velocity↑ | Developers, Architects, New hires |
| | Clean Architecture | DDD, Microservices | Netflix/Amazon, 70% coupling↓ | Developers, Architects, Business |
| **NFR-Testability** | Test Doubles | Unit/Integration testing | 90%+ coverage, 100x faster | Developers, QA, Ops |
| | Contract Testing | Microservices, APIs | Pact/IBM/Atlassian, 95% issues caught | Developers, API consumers, Ops |
| **Process** | Retrospective | Agile/Project teams | Scrum core, 15-25% velocity↑, 30% satisfaction↑ | Teams, Managers, Individuals |

## Final Checklist

- [ ] **Validation**: All 21 steps PASS
- [ ] **Minimums**: 30 Q&As (6/12/12), ≥25/≥10/≥12/≥12 references
- [ ] **Criteria**: ≥80% answers meet ALL 7 pattern criteria
- [ ] **Structure**: TOC present and complete
- [ ] **References**: All [Ref: ID] resolve, all links accessible/archived
- [ ] **Completeness**: No placeholders or TODOs

---
