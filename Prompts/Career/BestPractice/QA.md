# Software Development Best Practices Interview Q&A Generator

**Mission**: Generate 8-12 critical Q&As on decision-blocking best practices for informed decision-making with limited time. **Focus**: Minimal viable tracking—only practices that block decisions, create risk, or affect ≥3 stakeholders.

## Context

**Audience**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead  
**Scope**: 8 phases × 10 categories × 10 stakeholders × 6 viewpoints (selective coverage)  
**Output**: 8-12 Q&As (25/50/25% F/I/A) | Quantified benefits | References (G≥10, T≥6, L≥6, C≥8)  
**Assumptions**: Production systems (>10K rps, >1TB data), cloud-native, multi-team (10-100 engineers), regulated  
**Success**: 15/15 checks PASS (streamlined validation)

## Coverage

**8 Phases** (≥6/8 covered across 8-12 Q&As): Requirements → Design → Development → Testing → Deployment → Operations → Maintenance → Evolution

**10 Categories** (≥2/Q&A; ≥7/10 covered overall):

| Category | Standards & Metrics |
|----------|--------------------|
| Technical | SOLID, Clean Code, TDD, complexity ≤10, 0 lint |
| Quality | Pyramid 70/20/10, ≥80% coverage, chaos |
| Security | Zero-Trust, OWASP Top 10, SAST/DAST/SCA, STRIDE |
| Operational | SRE, SLO/Error Budget, ≥99.9% uptime, MTTR ≤30min |
| Performance | Caching 40-60% ↓, p95 <300ms, horizontal scale |
| Data | Schema versioning, RPO/RTO, partitioning, quality |
| DevOps | CI/CD, IaC, GitOps, DORA elite: daily ≤15% fail |
| Observability | Tracing, RED/USE, MTTD <5min, on-call |
| Collaboration | Agile, DOR/DOD, retros 15-25% ↑velocity, ADRs |
| Business | Value stream, OKRs, ROI, cost optimization |

**10 Stakeholders** (≥2/Q&A): BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead

**6 Viewpoints** (target coverage ≥5/6): Technical (code, arch, testing), Business (ROI, time-to-market), Regulatory (GDPR/HIPAA/PCI-DSS), Operational (SLOs, monitoring, DR), Data (schema, quality, governance), Security (threat model, zero-trust)

## Decision Criticality Framework

**Include Q&A if ANY apply**:
- **Blocks Decision**: Standard/tool/pattern choice prevents progress (e.g., TDD adoption, CI/CD strategy, SLO targets)
- **Creates Risk**: Compliance, security, performance SLA impact if ignored (e.g., Zero-Trust, data governance, observability)
- **Affects ≥3 Stakeholders**: Multi-role coordination needed (e.g., architecture decisions, deployment strategy, incident response)
- **Actively Evolving**: Standard/tool/method changed in past 12 months (e.g., new OWASP guidance, observability tooling)
- **High Adoption Barrier**: Learning curve or integration complexity >40 hours (e.g., chaos engineering, advanced SRE patterns)

**Exclude if**:
- Niche/legacy (adoption <5% in target domain)
- Orthogonal to core workflow (nice-to-have, not critical)
- Covered by existing Q&A (no new decision point)

## Content Standards

**Q&A Structure** (150-350 words): Header (Difficulty+Phase+Category+Stakeholders+Viewpoints) | Key Insight (quantified) | Best Practice (source) | Body (Problem→Practice→Implementation→Benefits→Metrics→Anti-patterns→Context) | Implementation (10-30 lines) | Metrics (criteria+formula+benchmarks+targets) | Comparison (≥2 approaches) | Anti-patterns (≥2) | Citations (≥1, ≥2 for advanced)

**Quality**: Evidence-based (quantified from research), Context clarity (specify applicability), Balanced (≥2 approaches, trade-offs, tags), Actionable (concrete examples), Industry standards (DORA/SRE/OWASP/NIST/ISO/CIS)

## References

| Type | Min | Requirements |
|------|-----|--------------|
| Glossary | 10 | Only terms used in Q&As; cover decision-critical categories and phases |
| Tools | 6 | URL, updated ≤18mo, pricing, phase, productivity metric if available |
| Literature | 6 | Canonical references only (DORA/SRE/OWASP/Clean Code/Agile/Team Topologies) |
| Citations | 8 | APA 7th, 60/30/10% EN/ZH/Other (±10%), ≥60% ≤3yr, URLs for all web sources |

**Quality Gates**: ≥60% tools last 2yr, ≥50% methods last 3yr; 100% valid URLs; peer-reviewed or authoritative sources

## Generation Process

**1. Plan (8-12 Q&As)**: Select candidate Q&As across all phases (target coverage ≥6/8), prioritize by **Decision Criticality** (blocks decision, creates risk, affects ≥3 stakeholders, actively evolving); difficulty 25/50/25% F/I/A; verify viewpoints ≥5/6 and ≥8 stakeholders covered

**2. References** (G≥10, T≥6, L≥6, C≥8): Build glossary with only decision-critical terms; tools with productivity metrics; canonical literature only; citations 60/30/10% EN/ZH/Other

**3. Write Q&As** (validate every 3): ≥70% judgment questions; check words 150-350, citations ≥1 (≥2 advanced), evidence-based, quantified, decision criticality justified, stakeholders ≥2, viewpoints ≥2, anti-patterns ≥2

**4. Artifacts**: Per Q&A - Mermaid diagram (<120 nodes) + implementation + metrics table + comparison; verify [Ref: ID] + URLs

**5. Validate** (15/15 PASS—Streamlined):

- **Counts**: G≥10, T≥6, L≥6, C≥8, Q=8-12 (25/50/25%)
- **Quality**: Citations ≥70%, EN/ZH/Other 60/30/10%, Recency ≥60%, URLs 100%
- **Content**: Words 150-350, Evidence 100%, Quantified 100%, Judgment ≥70%, Anti-patterns ≥2, Artifacts ≥90%
- **Coverage**: Phases ≥6/8, Categories ≥7/10, Stakeholders ≥8/10 (≥2/Q&A), Viewpoints ≥5/6
- **Decision Criticality**: 100% justified (blocks/risk/stakeholders/evolving)
- **Criteria**: Clarity, Accuracy, Actionability, Evidence-Based, Best-Practice-Awareness, Industry-Alignment

**Failure**: ANY fail → Fix → Re-validate ALL

## Templates

**Q&A Template**:
```
**Q**: [Judgment question: How/When/Why/Compare...]
**Difficulty**: F/I/A | **Phase**: [Phase] | **Category**: [≥2] | **Stakeholders**: [≥2] | **Viewpoints**: [≥2]
**Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving] – [Justification]
**Key Insight**: [Quantified benefit, 1 sentence]
**Best Practice**: [Name | Source]
**Answer** (150-350 words): Problem → Practice → Implementation → Benefits → Metrics → Anti-patterns → Context [Ref: X]
**Implementation** (10-30 lines): [Code/Config/Process]
**Metrics**: Criteria | Formula | Benchmarks | Targets
**Comparison**: | Approach | Benefits | Risks | When to Use | Adoption | Tag |
**Anti-patterns**: [≥2]
**Stakeholders**: [≥2 with concerns/benefits]
```

**Validation Template**:
```
Counts: G:X/10 T:X/6 L:X/6 C:X/8 Q:X/8-12 (F:X% I:X% A:X%)
Quality: Cites X% Lang EN:X% ZH:X% Recent X% URLs X% Standards X%
Content: Words X% Evidence X% Quantified X% Judgment X% Anti-patterns X% Artifacts X%
Coverage: Phases X/8, Categories X/10, Stakeholders X/10 (≥2/Q&A: X%), Viewpoints X/6
Decision Criticality: X/X justified (Blocks/Risk/Stakeholders/Evolving)
Status: X/15 PASS | Issues: [List] | Fix: [Actions]
```

## Example

### Q: How should teams adopt TDD to improve code quality and reduce defects?

**Difficulty**: I | **Phase**: Development | **Category**: Technical, Quality | **Stakeholders**: Dev, QA, Arch, Lead | **Viewpoints**: Technical, Business

**Decision Criticality**: **Blocks Decision** – TDD adoption blocks code quality strategy; affects ≥3 stakeholders (Dev, QA, Arch, Lead); actively evolving (XP/Agile standard, 60% adoption FAANG)

**Key Insight**: TDD: 40-60% defect reduction, 2-10x maintenance cost reduction over 2yr (Microsoft 2009).

**Best Practice**: Test-Driven Development | Kent Beck, Agile Manifesto, Microsoft/IBM Research

**Answer** (280 words): TDD follows Red-Green-Refactor: write failing test, implement minimal code, refactor. Addresses defects escaping to production (avg 15-30% traditional). Requires training (2-4wk), IDE support (JUnit/pytest), CI integration, quality-first culture [Ref: A1, A5]. Benefits: 40-60% defect ↓ (Microsoft 4-team study), 2-10x maintenance cost ↓, improved design (testable=better architecture), living docs (tests as specs), faster debugging [Ref: A8]. Metrics: ≥80% coverage, <10 complexity, ≥95% pass rate, <5min runtime. Anti-patterns: Testing implementation (brittle), ignoring refactor (debt), tests-after-code (loses design benefit), skipping under pressure (quality spiral) [Ref: A6]. Context: Effective for teams >5, greenfield/modules, complex logic. Less for UI prototypes, data pipelines, spikes. Stakeholders: Dev (confidence, faster debug), QA (shift-left), Arch (modularity), Lead (15-35% upfront for 40-60% defect ↓, 2-10x maintenance savings). Adoption: 60% Agile teams, FAANG standard.

**Implementation** (Go):
```go
// RED: Write failing test
func TestCalculateOrderTotal(t *testing.T) {
    order := Order{Items: []Item{{Price: 100, Qty: 2}, {Price: 50, Qty: 1}}}
    if CalculateOrderTotal(order) != 250 { t.Error("Expected 250") }
}

// GREEN: Minimal code
func CalculateOrderTotal(o Order) int {
    total := 0
    for _, i := range o.Items { total += i.Price * i.Qty }
    return total
}

// REFACTOR: Improve design
func (o Order) Total() int { return o.Items.Sum(func(i Item) int { return i.Price * i.Qty }) }
```

**Metrics**: 
- Criteria: ≥80% coverage, <10 complexity, ≥95% pass, <5min CI
- Formula: Defect Density = Defects/KLOC, Target <0.5 (vs 1-25)
- Benchmarks: Microsoft 40-90% defect ↓, 15-35% time ↑; IBM 50% defect ↓
- Targets: Coverage ≥80%, mutation ≥70%, runtime <5min

**Comparison**:
| Approach | Benefits | Risks | When to Use | Adoption | Tag |
|----------|----------|-------|-------------|----------|-----|
| TDD | 40-60% defect ↓, 2-10x maint ↓, design | 15-35% time ↑, 2-4wk learn | Complex logic, high reliability | 60% Agile, FAANG | [Consensus] |
| Test-After | Faster, flexible | 2-5x defects, poor design, brittle | Prototypes, low-risk | 30% teams | [Context-Dependent] |
| No Tests | Fastest | 10-25x defects, unmaintainable | Throwaway only | <10% | [Anti-pattern] |

**Anti-patterns**:
1. **Test Implementation**: Tests break on refactor; couple to internal structure vs behavior
2. **Skip Refactor**: Debt accumulates; duplication, complexity ↑, maintainability ↓
3. **Tests After**: Loses design benefit; fits existing design vs driving good design
4. **Large Tests**: Slow (>5min); reduces frequency, defeats rapid cycle

**Stakeholders**: Dev (confidence, -50% debug time, design skills), QA (shift-left, 40-60% fewer defects), Arch (modularity, DI, boundaries), Lead (15-35% upfront → 40-60% defect ↓, 2-10x maint savings)

### Glossary
**G1. TDD** [EN] – Red-Green-Refactor; test-first. Kent Beck. Related: Unit Testing  
**G2. CI/CD** [EN] – Automated build/test/deploy. Humble & Farley. Related: DevOps  
**G3. DORA Metrics** [EN] – Frequency, lead time, failure rate, MTTR. Elite: daily, <1h. Accelerate  
**G4. SLO/SLI/Error Budget** [EN] – Service level targets, innovation vs reliability. Google SRE  
**G5. Zero-Trust** [EN] – Never trust, always verify. NIST 800-207. Related: SAST/DAST  
**G6. OWASP Top 10** [EN] – Web app risks (injection, auth, etc.). Updated 3-4yr. Related: Security  
**G7. Clean Code** [EN] – Readable, maintainable. Robert Martin. Related: SOLID  
**G8. SOLID** [EN] – SRP, OCP, LSP, ISP, DIP. Robert Martin  
**G9. Test Pyramid** [EN] – 70% unit, 20% integration, 10% E2E. Mike Cohn. Related: Testing  
**G10. IaC** [EN] – Infra as code (Terraform, CloudFormation). DevOps Handbook  
**G11. Feature Flags** [EN] – Runtime toggles; trunk-based dev, canary. Related: Deployment  
**G12. Blue/Green** [EN] – Two envs; zero-downtime switch. Related: Canary, Rolling  
**G13. Observability** [EN] – Metrics (RED/USE), logs, traces. Charity Majors. Related: Monitoring  
**G14. RED Metrics** [EN] – Rate, Errors, Duration. Tom Wilkie. Related: USE  
**G15. SRE** [EN] – Engineering for ops; SLO, error budget, toil. Google  
**G16. Chaos Engineering** [EN] – Inject failures; resilience. Netflix Chaos Monkey. Related: Testing  
**G17. ADR** [EN] – Decision records with context, options, consequences. Michael Nygard  
**G18. STRIDE** [EN] – Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Privilege. Microsoft  
**G19. DOR/DOD** [EN] – Definition Ready/Done; acceptance. Scrum. Related: Agile  
**G20. Retrospective** [EN] – Process reflection; 15-25% velocity ↑. Agile. Related: CI  
**G21. Pair Programming** [EN] – Two devs, one keyboard; 15% slower, 15-40% defect ↓. XP. Related: Collaboration  
**G22. Code Review** [EN] – Peer review; 30-60% defect detect. <400 LOC, <60min. Related: Quality  
**G23. Contract Testing** [EN] – API contracts independently. Pact. Related: Microservices  
**G24. Trunk-Based Dev** [EN] – Commit daily; short branches. DORA. Related: CI/CD  
**G25. Error Budget** [EN] – (1-SLO) failure allowance; innovation vs reliability. 99.9%=43min/mo. Google SRE

### Tools
**T1.** GitHub Actions – CI/CD | Deploy | 2024-11 | Free/paid | https://github.com/features/actions  
**T2.** Terraform – IaC | Deploy/Ops | 2024-10 | Free/Enterprise | https://terraform.io  
**T3.** Prometheus – Metrics | Ops | 2024-10 | Free | https://prometheus.io  
**T4.** Grafana – Dashboards | Ops | 2024-11 | Free/$0+ | https://grafana.com  
**T5.** SonarQube – SAST | Dev | 2024-09 | Free/$150+ | https://sonarqube.org  
**T6.** OWASP ZAP – DAST | Test/Sec | 2024-08 | Free | https://zaproxy.org  
**T7.** Pact – Contract test | Test | 2024-07 | Free | https://pact.io  
**T8.** K6 – Load test | Test | 2024-10 | Free/Cloud | https://k6.io  
**T9.** Datadog – APM | Ops | 2024-11 | $15+/host | https://datadoghq.com  
**T10.** Vault – Secrets | Sec/Ops | 2024-09 | Free/Enterprise | https://vaultproject.io  
**T11.** OpenAPI – API spec | Design/Dev | 2024-09 | Free | https://openapis.org  
**T12.** Mermaid – Diagrams | Design | 2024-10 | Free | https://mermaid.js.org

### Literature
**L1.** Forsgren et al. (2018). *Accelerate*. IT Revolution – DORA, high-performing teams  
**L2.** Beyer et al. (2016). *Site Reliability Engineering*. O'Reilly – SLO/SLI, error budgets  
**L3.** Martin (2008). *Clean Code*. Prentice Hall – Quality, refactoring  
**L4.** Beck (2003). *Test-Driven Development*. Addison-Wesley – TDD, Red-Green-Refactor  
**L5.** Skelton & Pais (2019). *Team Topologies*. IT Revolution – Team structures, Conway's  
**L6.** Humble & Farley (2010). *Continuous Delivery*. Addison-Wesley – CI/CD, pipeline  
**L7.** Kim et al. (2016). *DevOps Handbook*. IT Revolution – Practices, culture  
**L8.** Richardson (2018). *Microservices Patterns*. Manning – Decomposition, deployment  
**L9.** Kleppmann (2017). *Designing Data-Intensive Apps*. O'Reilly – Data systems, consistency  
**L10.** OWASP (2021). *Top 10*. OWASP.org – Web security risks

### Citations
**A1.** Beck (2003). *TDD: By example*. Addison-Wesley [EN]  
**A2.** Forsgren et al. (2018). *Accelerate*. IT Revolution [EN]  
**A3.** Beyer et al. (2016). *Site reliability engineering*. O'Reilly [EN]  
**A4.** Martin (2008). *Clean code*. Prentice Hall [EN]  
**A5.** Nagappan et al. (2008). TDD quality improvement. *Empirical SE*, 13(3), 289-302 [EN]  
**A6.** Freeman & Pryce (2009). *Growing OO software, guided by tests*. Addison-Wesley [EN]  
**A7.** Skelton & Pais (2019). *Team topologies*. IT Revolution [EN]  
**A8.** Humble & Farley (2010). *Continuous delivery*. Addison-Wesley [EN]  
**A9.** Kim et al. (2016). *DevOps handbook*. IT Revolution [EN]  
**A10.** OWASP (2021). *Top 10*. https://owasp.org/Top10/ [EN]  
**A11.** NIST (2020). *Zero trust* (SP 800-207). NIST [EN]  
**A12.** 张逸 (2019). *DDD实践*. 电子工业 [ZH]  
**A13.** Richardson (2018). *Microservices patterns*. Manning [EN]  
**A14.** Kleppmann (2017). *Data-intensive apps*. O'Reilly [EN]  
**A15.** Google (2023). *SRE workbook*. O'Reilly [EN]
