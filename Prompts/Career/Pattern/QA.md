# Pattern-Based Q&A Generation Template

## Context
- **Problem**: Generate decision-critical Q&A content for career development patterns
- **Scope**: 8-12 Q&As (2 Fundamental/4 Intermediate/2-6 Advanced; 150-250 words each); ≥12 glossary terms, ≥6 tools, ≥6 literature references, ≥8 citations; 20-30 decision-critical patterns across 4-6 domains
- **Constraints**: Use readable Markdown formatting; prioritize Tier 1-2 sources; use RFC 2119 terminology; inline citations [Ref: ID]
- **Assumptions**: Patterns are decision-critical; access to current industry knowledge
- **Scale**: Individual and team use
- **Stakeholders**: Architects, developers, business stakeholders; technical writers, PMs
- **Resources**: LLM and reliable references for verification

**Success Criteria**: All 12 validation steps PASS; 100% patterns meet ≥1 Decision Criticality criterion; 100% critical claims cited with Tier 1-2 sources; MECE domains verified; all links accessible/archived.

**Key Terms**:
- **F/I/A**: Fundamental (basic), Intermediate (applied), Advanced (expert-level)
- **MECE**: Mutually Exclusive, Collectively Exhaustive
- **RFC 2119**: MUST (mandatory), SHOULD (recommended), MAY (optional)
- **Decision Criticality**: Patterns that block decisions, create risk, affect ≥2 roles, are evolving, or have high adoption barriers

## Mandatory Outputs
- 8-12 Q&As: 2F/4I/2-6A (150-250 words each)
- References: ≥12 glossary, ≥6 tools, ≥6 literature, ≥8 citations
- 4-6 Decision-Critical Domains (MECE)
- All 12 validation steps PASS
- 100% patterns satisfy ≥1 Decision Criticality criterion

## Decision Criticality Framework
**Include Q&A if ≥1 criterion satisfied**:
- **Blocks Decision**: Impacts architecture, technology, business model, market position, or strategic pivot
- **Creates Risk**: Material threat (performance, reliability, security, compliance)
- **Affects ≥2 Core Roles**: Multi-stakeholder impact (e.g., Architect + DevOps)
- **Actively Evolving**: Adoption/best practices changing in past 12-18 months
- **High Adoption Barrier**: >40h learning/implementation effort; blocks velocity if ignored

**Exclude Q&A if**:
- Niche/legacy (<5% adoption or impact)
- Orthogonal/nice-to-have (no decision impact)
- Already covered by another Q&A

## Content Guidelines
### Pattern Quality Criteria
1. **Reusability**: ≥2 contexts, adaptation points
2. **Effectiveness**: ≥1 company, ≥1 quantified metric [Ref: ID]
3. **Boundaries**: "Applies when" + "Avoid when"
4. **Stakeholders**: ≥2 groups, value, concerns
5. **Trade-offs**: ≥1 benefit, ≥1 cost ("improves X at expense of Y")
6. **Anti-Patterns**: ≥1 failure mode, mitigations

### Answer Structure (5-Step Template)
1. **Claim**: State pattern/principle
2. **Rationale**: Explain mechanism, causality, why now
3. **Evidence**: Cite empirical data [Ref: ID]
4. **Implications**: Consequences across ≥2 stakeholders
5. **Trade-offs & Boundaries**: Benefits vs. costs, "Applies when" + "Avoid when"

### Evidence Standards
**Source Tiers** (prioritize 1-2):
1. Peer-reviewed, standards (ISO/NIST/IETF), regulations (GDPR/CCPA), formal specs
2. Vendor docs (AWS/Azure/GCP), authoritative books (O'Reilly), frameworks
3. Org blogs (Netflix, Fowler), analyst reports (Gartner/Forrester)
4. Expert blogs, conference talks, OSS docs
5. Forums (Stack Overflow, Reddit)

**Citation Requirements**:
- **Critical**: ≥1 Tier 1-2; SHOULD ≥2 independent sources
- **Supporting**: ≥1 citation for non-obvious statements
- **Recency**: <3yr (fast-moving), <10yr (stable)
- **Languages**: Mix EN/ZH/other when available
- **Format**: Author/Org. (Year). _Title_. URL/DOI. [Lang]. Inline: [Ref: ID]

### Best Practices
- Apply 5-step template
- Justify Decision Criticality (≥1 criterion)
- Cite critical claims (Tier 1-2, ≥1 source)
- ≥2 stakeholder perspectives
- Explicit boundaries ("Applies when", "Avoid when")
- Trade-offs ("X at expense of Y")
- Concrete examples (code/diagram)
- RFC 2119 terms
- Prioritize high-value, high-impact patterns

**Prohibited**:
- Vague language
- Tier 5 for critical claims
- Omitting failure modes/anti-patterns
- Universally applicable claims
- Dead links
- Unsubstantiated claims
- Non-decision-critical patterns

## Pattern Domains (MECE)
Select 4-6 decision-critical domains.

| Domain | Examples | Stakeholders |
|--------|----------|--------------|
| Regulatory | Audit trails, Consent, Data residency | Compliance, Legal, Devs |
| Business | Subscription, Freemium, Platform | Execs, Product, Finance |
| Market | Blue Ocean, Disruptive Innovation | Execs, Marketing, Product |
| Technical | GoF, Repository, Strangler Fig | Devs, Architects |
| Data | Polyglot Persistence, Event Sourcing, CQRS | Data Eng, DBAs, Architects |
| Organizational | Conway's Law, Team Topologies, DevOps | Managers, Execs, Leads |
| Non-Functional Requirements | Security (Zero-Trust), Performance (Caching), Availability (Circuit Breaker), Reliability (Retry), Scalability (Sharding), Observability (Tracing), Adaptability (Feature Flags), Extensibility (DI), Maintainability (SOLID), Testability (Test Doubles) | Devs, Ops, Architects, Security |
| Process | Agile, Retrospectives, Incident Response | Teams, Managers |
| Hybrid | Regulatory+Technical, Compliance-by-Design | Compliance, Devs |

## 12-Step Validation
1. **References Counts**: Glossary ≥12, Tools ≥6, Literature ≥6, Citations ≥8; Q&As 8-12 (2/4/2-6)
2. **Citation Coverage**: ≥80% answers ≥1 citation, ≥50% ≥2
3. **Languages**: Reasonable mix EN/ZH/other
4. **Recency**: ≥50% <3yr; all links accessible/archived
5. **Word Count**: Random sample of 5 Q&As: 150-250 words each
6. **Decision Criticality**: 100% satisfy ≥1 criterion
7. **Insights**: Concrete boundaries/trade-offs/anti-patterns
8. **Per-Topic**: ≥1 source + ≥1 tool
9. **Visuals**: ≥70% with diagram+table+metric
10. **Evidence**: ≥80% empirical proof
11. **Quantitative**: ≥70% with metrics
12. **Examples**: ≥80% domain-appropriate

## Workflow
1. **Plan**: Apply Decision Criticality Framework; select 4-6 domains; allocate 8-12 Q&As; verify MECE and criticality.
2. **Draft**: Gather references (≥12/6/6/8, ≥50% <3yr); write Q&As (5-step, cited, ≥2 stakeholders); add visuals.
3. **Validate**: Run 12-step checks; fix until all PASS.
4. **Finalize**: Verify constraints, citations, MECE; self-review.

## Output Structure
### TOC
```markdown
## Contents
- [Decision Criticality Framework](#decision-criticality-framework)
- [Topic Areas](#topic-areas) - Q1-12 (8-12 total)
- [Topic 1: Domain](#topic-1) (Q1-QX) [F/I/A]
- [References](#references): Glossary | Tools | Literature | Citations
- [Validation Report](#validation-report)
```

### Template Outline
- **Title**
- **Contents** [TOC]
- **Context** [2-3 sentences on scope, constraints, assumptions, audience]
- **Decision Criticality Framework** [Criteria for inclusion]
- **Topic Areas** [Table of domains, Q# ranges, levels, criticality]
- **Topics** [Per domain: Q&As with level, domain, criticality, key insight, 150-250 word answer (5-step), criteria met, example, artifacts]
- **References** [Glossary ≥12, Tools ≥6, Literature ≥6, Citations ≥8]
- **Validation Report** [12 steps PASS/FAIL with metrics]

### Artifacts by Domain
| Domain | Diagrams | Examples | Metrics |
|--------|----------|----------|---------|
| Regulatory | Compliance flow | GDPR YAML | Compliance % |
| Business | Canvas | Revenue models | CLV, CAC |
| Technical | Sequence/Component | Pattern code | Coupling % |
| Data | ERD, Flow | DDL/SQL | Normalization, Perf |
| Organizational | Team topology | Team structure | Alignment % |
| NFR-Security | Threat model | Security config | Vulnerabilities |
| NFR-Performance | Latency breakdown | Flamegraph | p50/p95/p99 |
| NFR-Availability | Failure tree | Health checks | Uptime %, MTTR |
| NFR-Reliability | Retry flow | Idempotency keys | Recovery % |
| NFR-Observability | Tracing | Distributed traces | MTTD |
| NFR-Scalability | Scaling strategy | Horizontal scaling | Factor |
| NFR-Adaptability | Feature flags | Toggle code | Lead Time |
| NFR-Extensibility | Extension map | Plugin registry | #extensions |
| NFR-Maintainability | Layered diagram | Refactoring diff | Churn, complexity |
| NFR-Testability | Test pyramid | Contract tests | Coverage, flaky % |
| Market | Market map | Blue Ocean canvas | Share, growth % |
| Process | Workflow | Kanban board | Cycle time |
| Hybrid | Cross-domain map | Compliance-by-design flow | Risk score |

## Decision-Critical Pattern Catalog
Select/adapt to reach 20-30 patterns.

| Domain | Pattern | Contexts | Evidence | Stakeholders | Decision Criticality |
|--------|---------|----------|----------|--------------|----------------------|
| Regulatory | Double-Entry Audit | Financial, Healthcare | SOX compliance | Compliance, Devs | Blocks decision |
| | Consent Mgmt | GDPR, CCPA | 10K+ orgs, 85% risk↓ | Legal, Users, Devs | Creates risk |
| Business | Subscription | SaaS, Retail | $1.5T market | Finance, Product | Blocks decision |
| Technical | Repository | DDD | 60-80% coupling↓ | Devs, Architects | Blocks decision |
| Data | Event Sourcing | Finance | 100% audit | Compliance, Devs | Creates risk |
| Organizational | Conway's Law | Any org | 40% coordination↓ | Execs, Managers | Blocks decision |
| | DevOps | Cloud-native | 60% MTTR↓ | Devs, Ops | Blocks decision |
| NFR-Security | Zero-Trust | Remote work | 75% breach↓ | Security, Devs | Creates risk |
| NFR-Reliability | Retry+Backoff | Networks | 95% recovery | Devs, Ops | Blocks decision |
| NFR-Scalability | Horizontal Scaling | Web apps | 1000s instances | Ops, Architects | Blocks decision |
| NFR-Adaptability | Feature Flags | CD, A/B | 90% risk↓ | Devs, Product | Blocks decision |

## Final Checklist
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
- [ ] Readable formatting
- [ ] No placeholders
- [ ] Decision Criticality justified for each Q&A

## Quick Check (30s)
**Before generating Q&A:**

☐ **Self-contained**: Complete context; no cross-file refs
☐ Context | ☐ Clarity | ☐ Precision | ☐ Relevance
☐ MECE | ☐ Sufficiency | ☐ Breadth | ☐ Depth
☐ Significance | ☐ Priority | ☐ Concision | ☐ Accuracy | ☐ Credibility
☐ Logic | ☐ Risk/Value | ☐ Fairness
☐ Structure | ☐ Consistency
☐ Evidence | ☐ Verification | ☐ Practicality | ☐ Success Criteria
