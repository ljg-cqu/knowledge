# Pattern-Based Q&A Generation Template

**Context**: Evidence-based Q&A for software engineering patterns across 11 MECE domains. Audience: architects, developers, compliance, business stakeholders.

**Scope**: 30 Q&As (6F/12I/12A; 150-300 words); ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations; 70+ patterns.

**Constraints**: GFM ≤120 char/line; Tier 1-2 sources prioritized; RFC 2119; [Ref: ID] citations.

**Success Criteria**: 21 validation steps PASS; ≥80% patterns meet 7 criteria; 100% critical claims cited; MECE verified; links accessible.

---

## Mandatory Outputs

- 30 Q&As: 6F/12I/12A (150-300 words each)
- References: ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations
- 70+ patterns across 11 domains with evidence
- All 21 validation steps PASS
- ≥80% patterns meet ALL 7 criteria

**11 Domains** (MECE): Regulatory, Business, Market, Technical, Data, Organizational, NFR (Security, Performance, Availability, Reliability, Scalability, Observability, Adaptability, Extensibility, Maintainability, Testability), Process, Hybrid

**RFC 2119**: MUST (mandatory), SHOULD (strong recommendation), MAY (optional)

---

## Pattern Quality Criteria (ALL 7 Required)

1. **Reusability**: ≥2 contexts, adaptation points, examples
2. **Proven Effectiveness**: ≥1 company, ≥1 metric, [Ref: ID]
3. **Applicability Boundaries**: "Applies when" + "Avoid when" + example
4. **Multi-Stakeholder Value**: ≥2 groups, value, concerns
5. **Functional + NFR Coverage**: Description + ≥1 NFR + metrics
6. **Trade-offs**: ≥1 benefit, ≥1 cost ("improves X at expense of Y")
7. **Anti-Patterns**: ≥1 failure mode, exclusions, mitigations

## Answer Structure (6-Step Template)

1. **Claim**: State pattern/principle
2. **Rationale**: Explain mechanism, causality
3. **Evidence**: Cite empirical data [Ref: ID]
4. **Implications**: Consequences across stakeholders
5. **Limitations**: Constraints, assumptions, failure modes
6. **Alternatives**: When other approaches preferable

*Rationale: Ensures logic (G13), fairness (G15), evidence (G18), validation (G19)*

## Evidence Standards

### Source Tiers (Prioritize 1-2, G12: Credibility)

1. Peer-reviewed, standards (ISO/NIST/IETF), regulations (GDPR/CCPA), formal specs
2. Vendor docs (AWS/Azure/GCP), authoritative books (O'Reilly), frameworks
3. Org blogs (Netflix, Fowler), analyst reports (Gartner/Forrester)
4. Expert blogs, conference talks, OSS docs
5. Forums (Stack Overflow, Reddit)

### Citation Requirements (G11: Accuracy, G18: Evidence)

- **Critical**: ≥1 Tier 1-2; SHOULD have ≥2 independent sources
- **Supporting**: ≥1 citation for non-obvious statements
- **Recency**: <3yr (fast-moving), <10yr (stable)
- **Languages**: ~60% EN, ~30% ZH, ~10% other
- **Format**: Author/Org. (Year). _Title_. URL/DOI. [Lang]. Inline: [Ref: ID]

## Pattern Domains (MECE, G5)

| Domain | Examples | Stakeholders |
|--------|----------|--------------|
| **Regulatory** | Audit trails, Consent, Data residency | Compliance, Legal, Devs |
| **Business** | Subscription, Freemium, Platform | Execs, Product, Finance |
| **Market** | Blue Ocean, Disruptive Innovation, Land & Expand | Execs, Marketing, Product |
| **Technical** | GoF, Repository, Strangler Fig | Devs, Architects |
| **Data** | Polyglot Persistence, Event Sourcing, CQRS | Data Eng, DBAs, Architects |
| **Organizational** | Conway's Law, Team Topologies, DevOps | Managers, Execs, Leads |
| **NFR-Security** | Zero-Trust, Defense-in-Depth, Secrets Mgmt | Security, Compliance |
| **NFR-Performance** | Caching, Connection Pooling, CDN | Devs, Ops |
| **NFR-Availability** | Circuit Breaker, Bulkhead, Health Checks | Ops, Business |
| **NFR-Reliability** | Retry+Backoff, Idempotency, Saga | Devs, Ops |
| **NFR-Scalability** | Horizontal Scaling, Sharding, CQRS | Architects, Ops |
| **NFR-Observability** | Distributed Tracing, Metrics, Logging | Ops, Devs |
| **NFR-Adaptability** | Feature Flags, Strategy, Plugin Arch | Devs, Product |
| **NFR-Extensibility** | DI, Open-Closed, Middleware | Devs, Architects |
| **NFR-Maintainability** | SOLID, Clean Architecture | Devs, Architects |
| **NFR-Testability** | Test Doubles, Contract Testing | Devs, QA |
| **Process** | Agile, Retrospectives, Incident Response | Teams, Managers |
| **Hybrid** | Regulatory+Technical, Compliance-by-Design | Compliance, Devs |

## 21-Step Validation (G21: Success Criteria)

### References (1-7)
1. Counts: Glossary ≥25, Tools ≥10, Literature ≥12, Citations ≥12; Q&As 30 (6/12/12)
2. Citation Coverage: ≥70% answers ≥1, ≥30% ≥2
3. Languages: EN 50-70%, ZH 20-40%, Other 5-15%
4. Recency: ≥50% <3yr (≥70% digital/cloud)
5. Diversity: ≥3 types, no type >25%
6. Links: All accessible/archived
7. Resolution: [Ref: ID] resolve; Tools: pricing+adoption+update <18mo

### Content (8-12)
8. Word Count: 5 samples 150-300
9. Insights: Concrete (boundaries/trade-offs/effectiveness/anti-patterns)
10. Per-Topic: ≥2 sources + ≥1 tool
11. Traceability: ≥80% pattern → implementation
12. Scenarios: ≥70% judgment-based

### Patterns (13-21, G9: Significance, G16: Structure, G19: Validation)
13. Visuals: ≥90% with diagram+example+table+metric
14. Evidence: ≥80% empirical proof
15. Quantitative: ≥60% with metrics/formulas
16. Examples: ≥80% domain-appropriate
17-21. 7 Criteria: ≥80% meet ALL 7

## Best Practices (G10: Concision, G14: Risk/Value, G20: Practicality)

**Required**:
- Apply 6-step template
- Cite critical claims (Tier 1-2, ≥2 sources)
- ≥2 stakeholder perspectives
- Explicit boundaries ("Applies when", "Avoid when")
- Trade-offs ("X at expense of Y")
- Risk assessment + mitigation (Medium/High-risk)
- Concrete examples (code/YAML/diagrams)
- RFC 2119 terms
- Lines ≤120 chars
- Prioritize high-value, low-risk; flag high-risk

**Prohibited**:
- Vague language without clarification
- Tier 5 for critical claims
- Omitting failure modes/anti-patterns
- Presenting as universally applicable
- Dead links
- Unsubstantiated claims

---

## Workflow

### A. Plan
**Tasks**: 1) Select 8-12 clusters across 11 domains 2) Allocate 30 Q&As (6/12/12) 3) Verify MECE+7 criteria
**Gate**: ✓ 8-12 clusters, ✓ 30 allocated, ✓ MECE verified

### B. Draft
**Tasks**: 1) References ≥25/10/12/12 (~60/30/10 langs, ≥50% <3yr, Tier 1-2) 2) 30 Q&As (6-step, 7 criteria, [Ref: ID], ≥2 stakeholders, examples, validate every 5) 3) Visuals per cluster
**Gate**: ✓ 30 Q&As (150-300), ✓ References, ✓ Langs ~60/30/10, ✓ Recency ≥50% <3yr, ✓ Visuals, ✓ Citations ≥70%

### C. Validate
**Tasks**: 1) Run 21 steps 2) Document failures 3) Fix+re-validate until 100% PASS
**Gate**: ✓ 21 PASS, ✓ No broken links, ✓ No placeholders, ✓ ≥80% meet 7 criteria

### D. Finalize
**Tasks**: 1) Verify constraints 2) 100% critical claims cited 3) MECE boundaries 4) Self-review (G19)
**Gate**: ✓ Constraints, ✓ 100% cited, ✓ Checklist, ✓ Self-review

---

## Output Structure

### TOC (G17)
```markdown
## Contents
- [Topic Areas](#topic-areas) - Q1-30
- [Topic 1: Domain](#topic-1) (Q1-QX) [F/I/A]
- [References](#references): [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [Citations](#citations)
- [Validation Report](#validation-report)
```

### Template
```markdown
# [Title]

## Contents
[TOC]

## Context
[Scope, constraints, assumptions, audience - 2-3 sentences, G1]

## Topic Areas
[Table: domains, Q# ranges, F/I/A - MECE, G5]

## Topic 1: [Domain]

### Q1: [Question]
**Level**: [F/I/A] | **Domain**: [Type] | **Insight**: [Boundaries/Trade-offs/Anti-patterns]

**Answer** (150-300): [6-step + [Ref: ID]]

**7 Criteria**:
1. **Reusability**: ≥2 contexts, adaptation
2. **Effectiveness**: Company+metrics+[Ref: ID]
3. **Boundaries**: "Applies/Avoid when"+example
4. **Stakeholders**: ≥2 groups, value, concerns
5. **NFR**: Functional+≥1 NFR+metrics
6. **Trade-offs**: Benefits vs. costs
7. **Anti-Patterns**: Failures+exclusions+mitigations

**Risk** (G14): [L/M/H] - [Mitigation if M/H]

**Example**: [Code/YAML/diagram]
**Artifacts**: [Mermaid+table+metrics]

[Repeat Q2-Q30]

## References

### Glossary (≥25)
[Alphabetical, definitions, [Lang]]

### Tools (≥10)
[Features, pricing, adoption, verified <18mo, URL]

### Literature (≥12)
[APA 7th, [Lang]]

### Citations (≥12)
[APA 7th, [Lang], match [Ref: ID]]

## Validation Report
[21 steps: PASS/FAIL + metrics]
```

### Artifacts by Domain (G16)

| Domain | Diagrams | Examples | Metrics |
|--------|----------|----------|---------|
| **Regulatory** | Compliance flow, Audit trail | GDPR YAML | Compliance %, Completeness |
| **Business** | Canvas, Value chain | Revenue models | CLV, CAC, MRR |
| **Market** | Blue Ocean, Porter's 5 | Positioning | Share %, Innovation |
| **Technical** | Class/Sequence/Component | Pattern code | Reusability %, Coupling |
| **Data** | ERD, Flow, Lineage | DDL/SQL, Schema | Normalization, Perf |
| **Organizational** | Org/Team topology | Team structure | Alignment %, Load |
| **NFR-Security** | Threat, Auth flow | Security config | Surface, Vulnerabilities |
| **NFR-Performance** | Flamegraph, Latency | Cache strategy | p50/p95/p99, Throughput |
| **NFR-Availability** | Failure tree, Redundancy | Circuit breaker, Health | Uptime %, MTBF/MTTR |
| **NFR-Reliability** | Retry flow, Saga | Idempotency keys | Recovery %, Consistency |
| **NFR-Scalability** | Scaling, Sharding | Horizontal scaling | Factor, Linear % |
| **NFR-Observability** | Tracing, Dashboard | Distributed traces | Coverage %, MTTD |
| **NFR-Adaptability** | Feature flags, Strategy | Toggle code | Frequency, Lead Time |
| **NFR-Extensibility** | DI, Extension points | DI config, Middleware | Points, Integrations |
| **NFR-Maintainability** | Clean arch, SOLID | Refactored code | Complexity, Debt % |
| **NFR-Testability** | Pyramid, Mock arch | Doubles, Pact | Coverage %, Exec Time |
| **Process** | BPMN, Kanban | Process docs | Cycle/Lead Time, Efficiency |
| **Hybrid** | Cross-domain | Multi-domain | Domain-specific+integration |

## Pattern Catalog (70+)

| Domain | Pattern | Contexts | Evidence | Stakeholders |
|--------|---------|----------|----------|--------------|
| **Regulatory** | Double-Entry Audit | Financial, Healthcare, Blockchain | SOX, all major banks | Compliance, Devs, Auditors |
| | Consent Mgmt | GDPR, CCPA, Marketing | 10K+ orgs, 85% risk↓ | Legal, Users, Devs |
| | Data Residency | Multi-region, Fintech | AWS/Azure/GCP | Compliance, Ops, Business |
| **Business** | Subscription | SaaS, Media, Retail | $1.5T, 5-7x valuations | Finance, Product, Customers |
| | Freemium | Dev tools, Productivity | Slack 30%, Dropbox $2B | Marketing, Product, Users |
| | Platform | Airbnb, AWS, App Store | 7/10 top, 70% margins | Business, Producers, Consumers |
| **Market** | Blue Ocean | New categories | Cirque $800M, Wii 100M | Execs, Product, Marketing |
| | Disruptive Innovation | Tech transitions | Netflix/Tesla, 30+ industries | Execs, Investors, Market |
| | Land & Expand | Enterprise SaaS | Slack/Dropbox, 120%+ retention | Sales, Product, Finance |
| **Technical** | Repository | DDD, Layered | 60-80% coupling↓ | Devs, Architects, Ops |
| | Strangler Fig | Legacy modernization | Amazon/GitHub, 90% risk↓ | Architects, Ops, Business |
| **Data** | Polyglot Persistence | Microservices, E-commerce | Netflix 3+, LinkedIn 10+, 50-80% latency↓ | Architects, DBAs, Devs |
| | Event Sourcing | Finance, Collaboration | 100% audit, Banking standard | Compliance, Devs, Business |
| | Data Lake | Analytics, ML | AWS/Azure/GCP, 90% F500 | Data Scientists, Eng, Business |
| **Organizational** | Conway's Law | Any org | 50+ years, 40% coordination↓ | Execs, Architects, Managers |
| | Two-Pizza Team | Product/Platform | Amazon 2002, 60% meetings↓, 30% velocity↑ | Managers, Devs, Execs |
| | Team Topologies | Any org | MS/Google/Spotify, 50% load↓, 40% flow↑ | CTOs, Managers, Devs |
| | DevOps/YBIYRI | Cloud-native, SaaS | Amazon 2006, 60% MTTR↓, 10x deploys | Devs, Ops, Business |
| **NFR-Security** | Defense-in-Depth | Enterprise, Cloud, IoT | 90% attack↓, 95% F500 | Security, Compliance, Ops |
| | Zero-Trust | Remote, Cloud-native | Google 7yr/85K, 75% breach↓ | Security, Devs, Users |
| | Secrets Mgmt | Cloud, Microservices | 30M+ Vault, 50% F500 | Security, Devs, Ops |
| **NFR-Performance** | Caching | Web, APIs | 40-60% latency↓, 10x throughput | Users, Devs, Ops |
| | Connection Pooling | DB, HTTP, Queues | 10-100x gain, DB standard | Devs, Ops, Users |
| | CDN | Static, Video | 50-70% latency↓, 70% top sites | Users, Business, Ops |
| **NFR-Availability** | Circuit Breaker | Microservices | Netflix 99.99% uptime | Ops, Devs, Users |
| | Bulkhead | Thread pools, Multi-tenant | Netflix/AWS, 80% capacity | Ops, Architects, Business |
| | Health Check | K8s, Load balancers | 70% MTTR↓, <5s detection | Ops, Devs, Business |
| **NFR-Reliability** | Retry+Backoff | Network, Messages | 95% recovery, AWS default | Devs, Ops, Users |
| | Idempotency | Payments, Queues, APIs | Stripe/PayPal, 100% consistency | Devs, Ops, Business |
| | Saga | Microservices, Long txns | Uber/Airbnb | Architects, Devs, Ops |
| **NFR-Scalability** | Horizontal Scaling | Web, APIs | Netflix/FB, 1000s instances | Ops, Architects, Business |
| | Sharding | High-traffic DB | Instagram 4000, Discord billions | DBAs, Devs, Business |
| | CQRS | Read-heavy, Event sourcing | 10-100x read, Azure/AWS | Architects, Devs, Ops |
| **NFR-Observability** | Distributed Tracing | Microservices | Cloud-native standard | Ops, Devs, Business |
| **NFR-Adaptability** | Feature Flags | CD, A/B | FB/Netflix 100+/day, 90% risk↓ | Devs, Product, Business |
| | Strategy | Payments, Pricing | GoF 1994, 60% duplication↓ | Devs, Business, Architects |
| | Plugin Arch | IDEs, Browsers | VS Code 40K, WordPress 60K | Devs, Third-party, Users |
| **NFR-Extensibility** | DI | Enterprise, Frameworks | Spring 50%, 70% coupling↓ | Devs, Architects, Third-party |
| | Open-Closed | Libraries, APIs | SOLID 1988, 80% bugs↓ | Devs, QA, Business |
| | Middleware | Web frameworks | Express 100K packages | Devs, Third-party, Ops |
| **NFR-Maintainability** | SOLID | OOP, Enterprise | Since 2000, 40-60% defects↓, 25% velocity↑ | Devs, Architects, New hires |
| | Clean Architecture | DDD, Microservices | Netflix/Amazon, 70% coupling↓ | Devs, Architects, Business |
| **NFR-Testability** | Test Doubles | Unit/Integration | 90%+ coverage, 100x faster | Devs, QA, Ops |
| | Contract Testing | Microservices, APIs | Pact/IBM/Atlassian, 95% caught | Devs, API consumers, Ops |
| **Process** | Retrospective | Agile/Project | Scrum core, 15-25% velocity↑, 30% satisfaction↑ | Teams, Managers, Individuals |

## Final Checklist (G21)

**Validation**:
- [ ] 21 steps PASS + metrics
- [ ] ≥80% meet 7 criteria

**Completeness**:
- [ ] 30 Q&As (6/12/12; 150-300 words)
- [ ] References: ≥25/10/12/12
- [ ] 70+ patterns with evidence

**Quality**:
- [ ] 100% critical claims cited (Tier 1-2)
- [ ] [Ref: ID] resolve
- [ ] Links accessible/archived
- [ ] MECE verified
- [ ] Risk assessments (M/H)

**Structure**:
- [ ] TOC complete
- [ ] 6-step template
- [ ] RFC 2119 correct
- [ ] GFM ≤120 char/line
- [ ] No placeholders

---
