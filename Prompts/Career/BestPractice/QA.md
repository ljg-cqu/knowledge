# Software Development Best Practices Interview Q&A Generator

Generate 30-35 Q&As on industry best practices across full lifecycle, all stakeholders, core viewpoints.

## Context

**Audience**: BA, PM, Arch, Dev, QA, DevOps, Sec, Data, SRE, Lead  
**Scope**: 8 phases × 10 categories × 10 stakeholders × 6 viewpoints  
**Output**: 30-35 Q&As (15/50/35% F/I/A) | Quantified benefits | References (G≥25, T≥10, L≥10, C≥15)  
**Assumptions**: Production systems (>10K rps, >1TB data), cloud-native, multi-team (10-100 engineers), regulated  
**Success**: 28/28 checks PASS

## Coverage

**8 Phases** (3-5 Q&As each): Requirements → Design → Development → Testing → Deployment → Operations → Maintenance → Evolution

**10 Categories** (≥3/Q&A):

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

**6 Viewpoints** (all): Technical (code, arch, testing), Business (ROI, time-to-market), Regulatory (GDPR/HIPAA/PCI-DSS), Operational (SLOs, monitoring, DR), Data (schema, quality, governance), Security (threat model, zero-trust)

## Content Standards

**Q&A Structure** (150-350 words): Header (Difficulty+Phase+Category+Stakeholders+Viewpoints) | Key Insight (quantified) | Best Practice (source) | Body (Problem→Practice→Implementation→Benefits→Metrics→Anti-patterns→Context) | Implementation (10-30 lines) | Metrics (criteria+formula+benchmarks+targets) | Comparison (≥2 approaches) | Anti-patterns (≥2) | Citations (≥1, ≥2 for advanced)

**Quality**: Evidence-based (quantified from research), Context clarity (specify applicability), Balanced (≥2 approaches, trade-offs, tags), Actionable (concrete examples), Industry standards (DORA/SRE/OWASP/NIST/ISO/CIS)

## References

| Type | Min | Requirements |
|------|-----|--------------|
| Glossary | 25 | Term+definition+related; cover 10 categories, 8 phases, 6 viewpoints |
| Tools | 10 | URL, updated ≤18mo, pricing, phase |
| Literature | 10 | DORA/SRE/OWASP/Clean Code/Agile/DDD/Microservices/Team Topologies |
| Citations | 15 | APA 7th, 60/30/10% EN/ZH/Other, ≥60% ≤3yr, 100% URLs |

## Generation Process

**1. Plan**: Allocate 30-35 Q&As (15/50/35% F/I/A) across 8 phases (3-5 each); map 10 categories+10 stakeholders+6 viewpoints; verify MECE

**2. References**: Build G≥25 (categories+phases+viewpoints+stakeholders), T≥10 (URL+updated+pricing), L≥10 (standards+books), C≥15 (APA 7th, 60/30/10%, ≥60% ≤3yr)

**3. Write Q&As** (validate every 5): ≥70% judgment questions; check words 150-350, citations, syntax, evidence-based, quantified, categories ≥3, stakeholders ≥2, viewpoints ≥2, anti-patterns ≥2, benchmarks ≥60%

**4. Artifacts**: Per phase - Mermaid (<120 nodes), implementation, metrics, comparison, anti-patterns; verify [Ref: ID] + URLs

**5. Validate** (28/28 PASS):

- **Counts**: G≥25, T≥10, L≥10, C≥15, Q=30-35 (15/50/35%)
- **Quality**: Citations ≥70%, EN/ZH/Other 60/30/10%, Recency ≥60%, URLs 100%, Standards ≥80%
- **Content**: Words 150-350, Evidence 100%, Quantified 100%, Judgment ≥70%, Anti-patterns ≥2, Artifacts ≥90%
- **Coverage**: Phases 8 (3-5 each), Categories 10 (≥3/Q&A, ≥80%), Stakeholders 10 (≥2/Q&A, each ≥3), Viewpoints 6 (Tech ≥30%, Biz ≥20%, Reg ≥15%, Ops ≥20%, Data ≥10%, Sec ≥15%)
- **Criteria**: Clarity, Accuracy, Completeness, Balance, Actionability, Evidence-Based, Best-Practice-Awareness, Industry-Alignment

**Failure**: ANY fail → Fix → Re-validate ALL

## Templates

**Q&A Template**:
```
**Q**: [Judgment question: How/When/Why/Compare...]
**Difficulty**: F/I/A | **Phase**: [Phase] | **Category**: [≥1] | **Stakeholders**: [≥2] | **Viewpoints**: [≥2]
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
Counts: G:X/25 T:X/10 L:X/10 C:X/15 Q:X/30-35 (F:X% I:X% A:X%)
Quality: Cites X% Lang EN:X% ZH:X% Recent X% URLs X% Standards X%
Content: Words X% Evidence X% Quantified X% Judgment X% Anti-patterns X% Artifacts X%
Coverage: Phases X/8, Categories X/10 (≥3/Q&A: X%), Stakeholders X/10 (≥2/Q&A: X%, each ≥3: X%), Viewpoints Tech X% Biz X% Reg X% Ops X% Data X% Sec X%
Status: X/28 PASS X/8 MET | Issues: [List] | Fix: [Actions]
```

## Example

### Q: How should teams adopt TDD to improve code quality and reduce defects?

**Difficulty**: I | **Phase**: Development | **Category**: Technical, Quality | **Stakeholders**: Dev, QA, Arch, Lead | **Viewpoints**: Technical, Business

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
