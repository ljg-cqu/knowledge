# Pattern-Based Q&A Generation Template

**Context**: Decision-critical patterns for informed decision-making with time constraints. Minimal viable coverage. Audience: architects, developers, business stakeholders (core roles only).

**Scope**: 8-12 Q&As (2F/4I/2-6A; 150-250 words); ≥12 glossary, ≥6 tools, ≥6 literature, ≥8 citations; 20-30 decision-critical patterns.

**Constraints**: GFM ≤120 char/line; Tier 1-2 sources prioritized; RFC 2119; [Ref: ID] citations.

**Success Criteria**: 12 validation steps PASS; 100% patterns meet Decision Criticality Framework; 100% critical claims cited; MECE verified; links accessible.

---

## Mandatory Outputs (Minimal Viable)

- 8-12 Q&As: 2F/4I/2-6A (150-250 words each)
- References: ≥12 glossary, ≥6 tools, ≥6 literature, ≥8 citations
- 20-30 decision-critical patterns across 4-6 domains
- All 12 validation steps PASS
- 100% patterns satisfy ≥1 Decision Criticality criterion

**4-6 Decision-Critical Domains** (MECE): Regulatory, Business, Technical, Data, Organizational, NFR (Security, Reliability, Observability, Scalability, Adaptability)

**RFC 2119**: MUST (mandatory), SHOULD (strong recommendation), MAY (optional)

---

## Decision Criticality Framework (NEW)

**Include Q&A if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts architecture choice, technology selection, or strategic pivot
- **Creates Risk**: Identifies material threat (performance, reliability, security, compliance)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (Architect + DevOps, Dev + Security, etc.)
- **Actively Evolving**: Pattern adoption/best practices changing in past 12-18 months
- **High Adoption Barrier**: >40h learning/implementation cost; blocks velocity if ignored

**Exclude Q&A if**:
- Niche/legacy (<5% adoption or impact)
- Orthogonal/nice-to-have (no decision impact)
- Already covered by another Q&A

---

## Pattern Quality Criteria (Streamlined)

1. **Reusability**: ≥2 contexts, adaptation points
2. **Proven Effectiveness**: ≥1 company, ≥1 quantified metric, [Ref: ID]
3. **Applicability Boundaries**: "Applies when" + "Avoid when"
4. **Multi-Stakeholder Value**: ≥2 groups, value, concerns
5. **Trade-offs**: ≥1 benefit, ≥1 cost ("improves X at expense of Y")
6. **Anti-Patterns**: ≥1 failure mode, mitigations

## Answer Structure (5-Step Template, Minimal Viable)

1. **Claim**: State pattern/principle
2. **Rationale**: Explain mechanism, causality, why now
3. **Evidence**: Cite empirical data [Ref: ID]
4. **Implications**: Consequences across ≥2 stakeholders
5. **Trade-offs & Boundaries**: Benefits vs. costs, "Applies when" + "Avoid when"

*Rationale: Ensures logic, evidence, decision-critical boundaries, actionability*

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

## 12-Step Validation (Minimal Viable)

### References (1-4)
1. Counts: Glossary ≥12, Tools ≥6, Literature ≥6, Citations ≥8; Q&As 8-12 (2/4/2-6)
2. Citation Coverage: ≥80% answers ≥1, ≥50% ≥2
3. Languages: EN 60-70%, ZH 20-30%, Other 5-10%
4. Recency: ≥50% <3yr; Links all accessible/archived

### Content (5-8)
5. Word Count: 5 samples 150-250
6. Decision Criticality: 100% satisfy ≥1 criterion (Blocks/Risk/Roles/Evolving/Barrier)
7. Insights: Concrete (boundaries/trade-offs/anti-patterns)
8. Per-Topic: ≥1 source + ≥1 tool

### Patterns (9-12)
9. Visuals: ≥70% with diagram+table+metric
10. Evidence: ≥80% empirical proof
11. Quantitative: ≥70% with metrics
12. Examples: ≥80% domain-appropriate

## Best Practices (Minimal Viable)

**Required**:
- Apply 5-step template
- Justify Decision Criticality (≥1 criterion)
- Cite critical claims (Tier 1-2, ≥1 source)
- ≥2 stakeholder perspectives
- Explicit boundaries ("Applies when", "Avoid when")
- Trade-offs ("X at expense of Y")
- Concrete examples (code/diagram)
- RFC 2119 terms
- Lines ≤120 chars
- Prioritize high-value, high-impact patterns

**Prohibited**:
- Vague language without clarification
- Tier 5 for critical claims
- Omitting failure modes/anti-patterns
- Presenting as universally applicable
- Dead links
- Unsubstantiated claims
- Non-decision-critical patterns

---

## Workflow (Minimal Viable)

### A. Plan
**Tasks**: 1) Apply Decision Criticality Framework 2) Select 4-6 decision-critical domains 3) Allocate 8-12 Q&As (2F/4I/2-6A) 4) Verify MECE+Decision Criticality
**Gate**: ✓ 4-6 domains, ✓ 8-12 allocated, ✓ 100% meet ≥1 criterion

### B. Draft
**Tasks**: 1) References ≥12/6/6/8 (~60/30/10 langs, ≥50% <3yr, Tier 1-2) 2) 8-12 Q&As (5-step, Decision Criticality, [Ref: ID], ≥2 stakeholders, validate every 3) 3) Visuals per domain
**Gate**: ✓ 8-12 Q&As (150-250), ✓ References, ✓ Langs ~60/30/10, ✓ Recency ≥50% <3yr, ✓ Citations ≥80%

### C. Validate
**Tasks**: 1) Run 12 checks 2) Document failures 3) Fix+re-validate until 100% PASS
**Gate**: ✓ 12 PASS, ✓ No broken links, ✓ No placeholders, ✓ 100% Decision Criticality

### D. Finalize
**Tasks**: 1) Verify constraints 2) 100% critical claims cited 3) MECE boundaries 4) Self-review
**Gate**: ✓ Constraints, ✓ 100% cited, ✓ Checklist, ✓ Self-review

---

## Output Structure (Minimal Viable)

### TOC (Minimal Viable)
```markdown
## Contents
- [Decision Criticality Framework](#decision-criticality-framework)
- [Topic Areas](#topic-areas) - Q1-12
- [Topic 1: Domain](#topic-1) (Q1-QX) [F/I/A]
- [References](#references): [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [Citations](#citations)
- [Validation Report](#validation-report)
```

### Template (Minimal Viable)
```markdown
# [Title]

## Contents
[TOC]

## Context
[Scope, constraints, assumptions, audience - 2-3 sentences]

## Decision Criticality Framework
[Include Q&A if ≥1 criterion: Blocks/Risk/Roles/Evolving/Barrier]

## Topic Areas
[Table: domains, Q# ranges, F/I/A - MECE, Decision Criticality]

## Topic 1: [Domain]

### Q1: [Question]
**Level**: [F/I/A] | **Domain**: [Type] | **Decision Criticality**: [Criterion]
**Key Insight**: [Strategic, quantified, decision-critical]

**Answer** (150-250): [5-step + [Ref: ID]]

**Criteria Met**:
1. **Reusability**: ≥2 contexts
2. **Effectiveness**: Company+metric+[Ref: ID]
3. **Boundaries**: "Applies/Avoid when"
4. **Stakeholders**: ≥2 groups, value
5. **Trade-offs**: Benefits vs. costs
6. **Anti-Patterns**: Failures+mitigations

**Example**: [Code/diagram]
**Artifacts**: [Mermaid+table+metric]

[Repeat Q2-Q12]

## References (Minimal Viable)

### Glossary (≥12)
[Alphabetical, definitions, [Lang] - only terms used in Q&As]

### Tools (≥6)
[Features, pricing, adoption, verified <18mo, URL]

### Literature (≥6)
[APA 7th, [Lang] - canonical references only]

### Citations (≥8)
[APA 7th, [Lang], match [Ref: ID]]

## Validation Report
[12 steps: PASS/FAIL + metrics]
```

### Artifacts by Domain (Decision-Critical Only)

| Domain | Diagrams | Examples | Metrics |
|--------|----------|----------|---------|
| **Regulatory** | Compliance flow | GDPR YAML | Compliance % |
| **Business** | Canvas | Revenue models | CLV, CAC |
| **Technical** | Sequence/Component | Pattern code | Coupling % |
| **Data** | ERD, Flow | DDL/SQL | Normalization, Perf |
| **Organizational** | Team topology | Team structure | Alignment % |
| **NFR-Security** | Threat model | Security config | Vulnerabilities |
| **NFR-Reliability** | Retry flow | Idempotency keys | Recovery % |
| **NFR-Observability** | Tracing | Distributed traces | MTTD |
| **NFR-Scalability** | Scaling strategy | Horizontal scaling | Factor |
| **NFR-Adaptability** | Feature flags | Toggle code | Lead Time |

## Decision-Critical Pattern Catalog (20-30)

| Domain | Pattern | Contexts | Evidence | Stakeholders | Decision Criticality |
|--------|---------|----------|----------|--------------|----------------------|
| **Regulatory** | Double-Entry Audit | Financial, Healthcare, Blockchain | SOX, all major banks | Compliance, Devs, Auditors | Blocks decision (audit compliance) |
| | Consent Mgmt | GDPR, CCPA, Marketing | 10K+ orgs, 85% risk↓ | Legal, Users, Devs | Creates risk (fines €20M+) |
| **Business** | Subscription | SaaS, Media, Retail | $1.5T, 5-7x valuations | Finance, Product, Customers | Blocks decision (revenue model) |
| | Platform | Airbnb, AWS, App Store | 7/10 top, 70% margins | Business, Producers, Consumers | Blocks decision (market strategy) |
| **Technical** | Repository | DDD, Layered | 60-80% coupling↓ | Devs, Architects, Ops | Blocks decision (architecture) |
| | Strangler Fig | Legacy modernization | Amazon/GitHub, 90% risk↓ | Architects, Ops, Business | Blocks decision (migration) |
| **Data** | Polyglot Persistence | Microservices, E-commerce | Netflix 3+, LinkedIn 10+, 50-80% latency↓ | Architects, DBAs, Devs | Blocks decision (data strategy) |
| | Event Sourcing | Finance, Collaboration | 100% audit, Banking standard | Compliance, Devs, Business | Creates risk (audit compliance) |
| **Organizational** | Conway's Law | Any org | 50+ years, 40% coordination↓ | Execs, Architects, Managers | Blocks decision (org structure) |
| | Team Topologies | Any org | MS/Google/Spotify, 50% load↓, 40% flow↑ | CTOs, Managers, Devs | Affects ≥2 roles (velocity impact) |
| | DevOps/YBIYRI | Cloud-native, SaaS | Amazon 2006, 60% MTTR↓, 10x deploys | Devs, Ops, Business | Blocks decision (deployment strategy) |
| **NFR-Security** | Zero-Trust | Remote, Cloud-native | Google 7yr/85K, 75% breach↓ | Security, Devs, Users | Creates risk (breach, compliance) |
| | Secrets Mgmt | Cloud, Microservices | 30M+ Vault, 50% F500 | Security, Devs, Ops | Blocks decision (security posture) |
| **NFR-Reliability** | Retry+Backoff | Network, Messages | 95% recovery, AWS default | Devs, Ops, Users | Blocks decision (resilience SLA) |
| | Idempotency | Payments, Queues, APIs | Stripe/PayPal, 100% consistency | Devs, Ops, Business | Blocks decision (data consistency) |
| **NFR-Observability** | Distributed Tracing | Microservices | Cloud-native standard | Ops, Devs, Business | Creates risk (incident response) |
| **NFR-Scalability** | Horizontal Scaling | Web, APIs | Netflix/FB, 1000s instances | Ops, Architects, Business | Blocks decision (performance SLA) |
| | Sharding | High-traffic DB | Instagram 4000, Discord billions | DBAs, Devs, Business | Blocks decision (data scaling) |
| **NFR-Adaptability** | Feature Flags | CD, A/B | FB/Netflix 100+/day, 90% risk↓ | Devs, Product, Business | Blocks decision (deployment velocity) |

## Final Checklist (Minimal Viable)

**Validation**:
- [ ] 12 steps PASS + metrics
- [ ] 100% meet Decision Criticality Framework

**Completeness**:
- [ ] 8-12 Q&As (2/4/2-6A; 150-250 words)
- [ ] References: ≥12/6/6/8
- [ ] 20-30 decision-critical patterns

**Quality**:
- [ ] 100% critical claims cited (Tier 1-2)
- [ ] [Ref: ID] resolve
- [ ] Links accessible/archived
- [ ] MECE verified (4-6 domains)

**Structure**:
- [ ] TOC complete
- [ ] 5-step template
- [ ] RFC 2119 correct
- [ ] GFM ≤120 char/line
- [ ] No placeholders
- [ ] Decision Criticality justified for each Q&A

---
