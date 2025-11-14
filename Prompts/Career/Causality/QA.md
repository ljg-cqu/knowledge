# Causality Analysis Interview Generator

Generate 30-35 interview Q&A pairs testing causal reasoning across the software lifecycle, covering technical, business, market, and regulatory dimensions. Trace multi-level causal chains from root causes to ultimate outcomes.

## Requirements

### Context & Scope
**Domain**: Production-grade distributed systems (>10K rps, >1TB data, multi-team)
**Audience**: BA, PM, Architect, Developer, QA/SET, DevOps, Security, Data Engineer, SRE, Leadership
**Focus**: Multi-dimensional causality (technical ↔ business ↔ market ↔ regulatory) with quantified impact chains

### Output Specifications
**Format**: 150-350 words/answer with Mermaid diagrams, cause-effect matrices, quantified impacts, APA 7th [EN]/[ZH]
**Quantity**: 30-35 Q&As; Difficulty: 20% F (6-7), 40% I (12-14), 40% A (12-14)
**Coverage**: MECE across 8 Lifecycle × 5 Causality Dimensions (≥1 Q&A per major combo)
  - **Lifecycle**: Requirements, Architecture, Development, Testing, Deployment, Operations, Maintenance, Evolution
  - **Dimensions**: Technical, Business/Market, Regulatory, Cross-Domain, Emergent
**Traceability**: Root → Intermediate → Direct Causes → Effects → Outcomes (quantified at each level)
**Per Cluster**: ≥1 diagram, ≥1 multi-factor analysis, ≥1 impact table, ≥1 counterfactual

### Content Standards
**Precision**: Quantified relationships ("30% latency → 15% conversion drop"), not vague ("affects performance")
**Credibility**: Industry case studies, academic papers; sources ≤3yr; empirical evidence
**Balance**: Trade-offs, confounding factors, alternative pathways
**Logic**: Multi-level chains with quantified links
**Concision**: Diagrams/tables over text; no redundancy

## Causality Framework

### Lifecycle × Causality Dimension Matrix (MECE coverage required)

| Phase | Technical/System/Ecosystem Causality | Business/Market Causality | Regulatory/Compliance Causality | Cross-Domain Causality | Emergent Causality |
|-------|-----------------------------------|--------------------------|--------------------------------|----------------------|-------------------|
| **Requirements & Discovery** | Tech constraint → Architecture decision → Scalability limit → Performance bottleneck | Market need → Feature priority → Resource allocation → Delivery timeline | Regulatory requirement → Data handling → Architecture constraint → Tech debt | GDPR requirement → Encryption need → Performance trade-off → Cost increase | Customer expectation + Market timing + Tech maturity → Innovation risk |
| **Architecture & Design** | Monolith choice → Tight coupling → Deployment bottleneck → Team coordination overhead → Velocity decline | Microservices adoption → Infrastructure complexity → Operational cost → Team specialization → Hiring needs | SOC2 compliance → Audit logging → Storage cost → Query performance → Data retention policy | Cloud migration → Vendor lock-in → Cost overrun → Architecture re-design → Technical debt | Design pattern + Team skills + Market pressure → Architecture evolution path |
| **Development** | ORM choice → N+1 queries → Database load → Scaling cost → Performance SLA breach | Technical debt → Development velocity ↓ → Feature delay → Market opportunity loss → Revenue impact | PCI-DSS requirement → Tokenization implementation → Integration complexity → Vendor dependency → Operational overhead | API rate limiting → Retry logic → Exponential backoff → Request amplification → Cost spike | Code quality + Team experience + Timeline pressure → Quality-speed trade-off |
| **Testing & Quality** | Test automation gap → Manual testing → Release bottleneck → Deployment frequency ↓ → Competitive disadvantage | Quality gate strictness → Release delay → Market timing miss → Revenue loss → Business unit dissatisfaction | Compliance test suite → Test execution time → CI/CD pipeline duration → Developer productivity → Iteration speed | Load testing omission → Production bottleneck → Customer experience degradation → Churn rate increase → ARR decline | Test strategy + Coverage targets + Team capacity → Quality-velocity equilibrium |
| **Deployment & Release** | Blue-green deployment → Capacity doubling → Infrastructure cost → Budget approval → Release cadence constraint | Canary deployment → Gradual rollout → Market feedback → Feature pivot → Development re-prioritization | Change approval board → Deployment delay → Release window → Business milestone miss → Stakeholder pressure | Breaking API change → Client compatibility → Support burden → Customer satisfaction → Renewal risk | Deployment strategy + Risk tolerance + Market timing → Release approach |
| **Operations & Observability** | Monitoring gap → Detection delay → MTTR increase → SLO breach → Error budget exhaustion → Feature freeze | SLO violation → Customer complaints → Churn increase → NRR decline → Valuation impact → Fundraising difficulty | Data breach → Regulatory investigation → Compliance penalty → Reputational damage → Customer loss → Revenue decline | Third-party API outage → Service degradation → Customer impact → Support ticket volume → Operational cost → Team burnout | System complexity + Observability maturity + Incident response → Operational resilience |
| **Maintenance & Support** | Technical debt → Maintenance burden → Feature development time ↓ → Innovation lag → Market position loss | Support ticket volume → Engineering distraction → Feature velocity ↓ → Roadmap delay → Competitive pressure | Vulnerability disclosure → Patch urgency → Testing sacrifice → Production bug → Customer trust erosion | Legacy system maintenance → Modern stack adoption delay → Developer retention risk → Hiring difficulty → Team capability gap | Maintenance load + Innovation pressure + Resource constraint → Technical debt strategy |
| **Evolution & Governance** | Monolith → Microservices migration → Team restructuring → Communication overhead → Conway's Law → Re-architecture | Technical capability → Product innovation → Market differentiation → Pricing power → Margin improvement → Business sustainability | Regulatory change → Compliance requirement → Architecture modification → Development cost → Budget pressure → Strategic trade-off | Cloud-native adoption → Operational model shift → Team skill gap → Training investment → Hiring need → Organizational change | Technology evolution + Business strategy + Market dynamics → Digital transformation pathway |

### Causality Dimension Reference

| Dimension | Causal Chain Pattern | Key Metrics (Relationships) | Analysis Frameworks |
|-----------|---------------------|----------------------------|--------------------|
| **Technical/System/Ecosystem** | Technology choice → System characteristics → Performance outcomes → Business impact | Latency impact = f(Architecture), Scalability = f(Design patterns), Cost = f(Tech stack) | C4 Model, ADR, Performance budgets, Capacity planning |
| **Business/Market** | Market forces → Strategic decisions → Product features → Customer behavior → Revenue outcomes | Customer acquisition cost = f(Features), Churn = f(Quality), Market share = f(Differentiation) | Business Model Canvas, Value Stream Mapping, SWOT, Porter's Five Forces |
| **Regulatory/Compliance** | Regulatory requirement → Compliance constraint → Architecture/process changes → Operational overhead → Business flexibility | Compliance cost = f(Requirements), Time-to-market = f(Approval process), Risk = f(Violations) | GDPR, HIPAA, PCI-DSS, SOC2, ISO 27001, Risk matrices |
| **Cross-Domain (Technical↔Business↔Regulatory)** | Multi-factor causality spanning domains with feedback loops and emergent effects | Total cost of ownership = f(Tech, Operations, Compliance), Competitive advantage = f(Speed, Quality, Innovation) | Systems Thinking, Causal Loop Diagrams, Theory of Constraints |
| **Emergent (Complex Multi-Factor)** | Non-linear causality with multiple interacting causes and threshold effects | System resilience = f(Technical debt, Team capability, Process maturity), Innovation capacity = f(Architecture flexibility, Team autonomy, Market feedback loops) | Cynefin Framework, Complexity Theory, Network Effects, Conway's Law |
| **Temporal Causality** | Time-delayed effects and cascading impacts across lifecycle phases | Technical debt future cost = ∫(Interest rate × Principal), Compound effects = ∏(Individual impacts) | Discounted cash flow, Technical debt quantification, Forecasting models |
| **Stakeholder Causality** | Role-specific perspectives on cause-effect chains with different optimization goals | Developer velocity = f(Tooling, Process), Business velocity = f(Market timing, Feature delivery) | Stakeholder mapping, Empathy mapping, Impact-effort matrices |

## Visuals & Metrics

### Causality Analysis Diagrams

| Analysis Type | Diagram (Mermaid) | Metrics (quantified relationships) | When to Use |
|---------------|-------------------|----------------------------------|-------------|
| **Causal Chain Mapping** | Cause tree, Impact flow, Causal pathway diagram | Chain depth (avg 4-6 levels), Causal strength (correlation coefficient ≥0.6), Quantified impact at each level | Requirements & Discovery - trace requirement causes to business outcomes |
| **Multi-Factor Causality** | Fishbone (Ishikawa), Influence diagram, Factor interaction matrix | Contributing factors (6-12), Interaction strength (β coefficients), Variance explained (R² ≥70%) | Architecture & Design - analyze multiple causes for design decisions |
| **Cross-Domain Impact Analysis** | Domain interaction graph, Feedback loop diagram, Causal loop (CLD) | Domain coupling strength (0-1 scale), Feedback loop delay (time units), Amplification factor (gain) | Development - understand technical↔business↔regulatory impacts |
| **Temporal Causality** | Timeline with cascading effects, Lag analysis, Compound impact chart | Time lag distribution (median, p95), Accumulation rate (Δeffect/Δtime), Discount factor for delayed effects | Testing & Quality - project long-term consequences of quality decisions |
| **Counterfactual Scenarios** | Decision tree with alternatives, What-if analysis, Scenario comparison matrix | Outcome variance across scenarios (σ), Expected value difference (ΔEV), Risk-adjusted impact | Deployment & Release - evaluate alternative approaches and their outcomes |
| **Root Cause vs Contributing Factors** | Pareto chart, Weighted factor analysis, Necessity-sufficiency matrix | Root cause identification (80-20 rule), Necessity score (0-1), Sufficiency score (0-1) | Operations & Observability - distinguish root causes from symptoms |
| **Systemic Causality Patterns** | Pattern library, Recurring causal chains, Anti-pattern catalog | Pattern frequency, Pattern impact severity, Anti-pattern cost quantification | Maintenance & Support - learn from recurring causal patterns |
| **Causal Trend Analysis** | Longitudinal causal strength, Shifting cause patterns, Emerging causality | Causal stability over time, Emerging factor identification, Trend prediction accuracy | Evolution & Governance - track how causal relationships evolve |

## Causality Analysis Frameworks & Approaches

| Framework | When to Use | Advantage | Disadvantage | Trade-offs | Standards/References |
|-----------|-------------|-----------|--------------|------------|---------------------|
| **5-Whys Root Cause Analysis** | Single-root problems; linear causality; incident postmortems | Simple, fast (15-30min), reveals hidden assumptions, team alignment | Stops at first plausible cause; misses multi-factor causality; depends on facilitator skill | Depth vs. speed; Simplicity vs. completeness | Lean Manufacturing, Toyota Production System, Ohno (1988) |
| **Fishbone (Ishikawa) Diagram** | Multi-factor causality; complex problems with 6+ contributing causes; design decisions | Comprehensive factor coverage (People, Process, Technology, Environment, Materials, Measurement), visual clarity | Time-intensive (1-2h); doesn't quantify causal strength; no prioritization | Breadth vs. depth; Comprehensiveness vs. actionability | Ishikawa (1968), Quality Control, Six Sigma |
| **Causal Loop Diagrams (CLD)** | Feedback loops; system dynamics; cross-domain causality; long-term effects | Shows reinforcing/balancing loops, reveals non-intuitive behavior, quantifies delays and amplification | Steep learning curve; requires systems thinking; can oversimplify | Systemic understanding vs. immediate action; Complexity modeling vs. decisiveness | Senge (1990) *Fifth Discipline*, System Dynamics, Meadows (2008) |
| **Counterfactual Reasoning** | Decision validation; alternative scenarios; A/B testing design; risk assessment | Reveals causal necessity (would outcome differ?), supports what-if analysis, quantifies decision impact | Requires controlled comparison; can't test all scenarios; confirmation bias risk | Analytical rigor vs. speed; Scenario coverage vs. decision paralysis | Pearl (2009) *Causality*, Rubin Causal Model, Potential Outcomes Framework |
| **Theory of Constraints (TOC)** | Bottleneck identification; process optimization; capacity planning | Identifies limiting factor (1 root constraint), quantifies impact, prioritizes improvement (Goldratt: focus on constraint) | Assumes single constraint dominance; shifts over time; requires continuous analysis | Focus vs. holistic view; Short-term optimization vs. long-term flexibility | Goldratt (1984) *The Goal*, Throughput Accounting, DBR (Drum-Buffer-Rope) |
| **Impact Mapping** | Feature prioritization; business-outcome tracing; roadmap planning | Traces business goal → actors → impacts → deliverables, prevents feature bloat, aligns stakeholders | Needs clear business goal; can oversimplify; maintenance overhead | Strategic alignment vs. agility; Top-down clarity vs. bottom-up innovation | Adzic (2012) *Impact Mapping*, Goal-Question-Metric, OKR frameworks |
| **Failure Mode Effects Analysis (FMEA)** | Risk assessment; architecture design; critical systems; compliance-heavy domains | Quantifies risk (RPN = Severity × Occurrence × Detection), prioritizes mitigation, industry-standard (automotive, aerospace, medical) | Time-intensive (days for complex systems); static snapshot; requires domain expertise | Proactive prevention vs. reactive speed; Rigor vs. pragmatism | IEC 60812, ISO 14971, SAE J1739, MIL-STD-1629 |
| **Pre-Mortem Analysis** | High-risk decisions; launch planning; major migrations; critical deployments | Surfaces failure scenarios proactively (30-50% more than brainstorming), psychological safety ("assume failure"), team buy-in | Can induce pessimism; time-consuming (1-2h); depends on team experience | Risk anticipation vs. momentum; Thoroughness vs. paralysis | Kahneman (2011) *Thinking Fast and Slow*, Klein (2007), Project Management Institute |
| **Regression Analysis (Statistical)** | Data-driven causality; large datasets; A/B test analysis; metric attribution | Quantifies causal strength (β coefficients, R²), controls confounding variables, statistical significance testing | Correlation ≠ causation without experiment; requires large sample; assumes linearity | Statistical rigor vs. intuition; Data requirements vs. speed | Pearl (2009), Econometrics, Causal Inference literature, Angrist & Pischke (2009) |

## Question Design

**Principles**: Test causal reasoning (not recall); real-world scenarios; trace multi-level chains; span domains

**Good vs. Poor**:
✅ Multi-level: "Fintech chose microservices → Infrastructure complexity → Cost +3x → Burn rate crisis → Fundraising pressure → Quality compromise. Trace chain, quantify impacts, show counterfactual (monolith), include CTO/CFO/CEO perspectives"
❌ Recall: "What are microservices?"

✅ Cross-domain: "GDPR → Encryption → Latency +30% → Conversion -15% → ARR -$2M. Quantify each link, show fishbone + causal loop + impact matrix"
❌ Vague: "How does GDPR affect performance?"

✅ Emergent: "Tech debt 40% + Market pressure + Attrition → Quality decline → Incidents 5x → Churn 20% → Valuation -40%. Analyze interactions, tipping points, intervention points"
❌ No depth: "Why does technical debt matter?"

✅ Temporal: "Skip load testing → Bottleneck (6mo lag) → Emergency scaling → Re-design (12mo lag) → Competitive loss. Show timeline, compound impact, TCO"
❌ No temporal: "What is load testing?"

### Stakeholder Context by Role

| Role | Causality Analysis Focus | Expected Detail |
|------|--------------------------|----------------|
| **Business Analyst** | Business requirement → System behavior → Business outcome causality; regulatory constraints → process requirements | Causal chain from business need to system requirement, impact mapping (goal → actor → impact → deliverable), quantified business outcome prediction |
| **Product Manager** | Feature decisions → Customer behavior → Revenue impact; market dynamics → product strategy causality | Feature prioritization via impact mapping, A/B test causal analysis, customer churn root cause analysis, market positioning cause-effect chains |
| **Architect** | Technical decisions → System characteristics → Business outcomes; architecture trade-offs → long-term consequences | ADRs with causal reasoning (decision → consequences), multi-factor analysis (technical + business + regulatory), counterfactual scenarios (alternative architectures), FMEA with causal chains |
| **Developer** | Code decisions → System behavior → Performance/cost/quality outcomes; technical debt → future impact | Implementation choice → performance causality (e.g., ORM → N+1 → DB load), technical debt causal analysis (shortcuts → maintenance burden → velocity decline), profiling → root cause identification |
| **QA/SET** | Test strategy → Quality outcomes; defect patterns → root causes; quality gates → release velocity | Test coverage → defect escape rate causality, quality gate strictness → release cadence trade-off, defect trend analysis → systemic root causes, test automation ROI causality |
| **DevOps** | Deployment strategy → Risk/velocity trade-offs; infrastructure decisions → Cost/performance outcomes | CI/CD pipeline design → deployment frequency causality, infrastructure choice (e.g., K8s) → operational complexity → cost, deployment failure → root cause → prevention |
| **Security** | Threat scenarios → Vulnerability chains → Breach impacts; security measures → Business constraints | Attack tree analysis (attacker goal → sub-goals → attack vectors), security requirement → performance/UX trade-off, compliance mandate → architecture constraint causality |
| **Data Engineer** | Data quality → Analytics/ML accuracy → Business decisions; schema evolution → System impacts | Data pipeline failure → downstream impact analysis, data quality issue → root cause (source system, transformation, storage), schema change → compatibility impact |
| **SRE** | System behavior → SLO outcomes; incident patterns → Systemic root causes | Incident → 5-Whys → systemic root cause, monitoring gap → MTTR causality, capacity planning decision → cost/availability trade-off, SLO violation → business impact chain |
| **Leadership** | Strategic decisions → Organizational outcomes; resource allocation → Business results; technology investment → Competitive position | Technology investment → capability → product innovation → market differentiation causality, technical debt → velocity → opportunity cost, team structure (Conway's Law) → architecture → maintainability |

**Mandatory Elements per Q&A**:
1. **Causal chain**: Root → Intermediate → Direct → Effects → Outcomes (quantified at each link)
2. **Visuals**: Diagram (fishbone/influence/CLD), matrix, impact table, counterfactual
3. **Context**: Phase, role, dimension
4. **Citation**: ≥1 [Ref: ID]
5. **Insight**: Causal strength/confounds/interventions (1 sentence)
6. **Trade-offs**: Alternatives, counterfactuals
7. **Metrics**: Formulas, quantified (%, β, R²)
8. **Multi-factor**: Contributing factors, interactions, necessity/sufficiency
9. **Temporal**: Time lags, compound effects
10. **Stakeholders**: Role perspectives, conflicting goals

## References & Quality

### Reference Minimums (scale for 30-35 Q&As)
- **≥25 Glossary**: Root Cause, Causal Chain, Causal Strength, Correlation vs Causation, Confounding/Mediating/Moderating Variables, Feedback Loops, CLD, Necessity/Sufficiency, Counterfactual, INUS Condition, Path Analysis, SEM, Granger Causality, Instrumental Variable, β, R², Interaction Effect, Time Lag, Compound Effect, Tipping Point, Conway's Law, Network Effect, Technical Debt (with formulas/quantification)
- **≥12 Tools**: Diagramming (Lucidchart, Mermaid, Vensim, InsightMaker), Statistical (R, Python DoWhy/CausalML, SPSS), RCA (Sologic, TapRooT), Mapping (Miro, ImpactMapper), BI (Tableau, Looker), A/B (Optimizely, LaunchDarkly). Include: purpose, price, update ≤18mo, dimension support
- **≥18 Literature**: Causality (Pearl 2009, Book of Why 2018), Systems (Senge 1990, Meadows 2008, Sterman 2000), Inference (Angrist & Pischke 2009, Imbens & Rubin 2015), RCA (Ohno 1988, Ishikawa 1985), Decision (Kahneman 2011, Klein 2007), Software (Goldratt 1984, Adzic 2012, Kim 2013, Richardson 2018, Kleppmann 2017), Org (Conway 1968, Team Topologies 2019)
- **≥35 Citations**: APA 7th [EN]/[ZH]; DOI/URL; academic + case studies + empirical

### Quality Gates (all must PASS)

| Gate | Requirement | Validation Method |
|------|-------------|-------------------|
| **Lifecycle Coverage** | All 8 phases covered with ≥3 Q&As each | Count by phase |
| **Stakeholder Coverage** | ≥8/10 roles covered with ≥2 Q&As each | Count by role |
| **Causality Dimension Coverage** | All 5 causality dimensions covered with ≥4 Q&As each (Technical/System/Ecosystem, Business/Market, Regulatory/Compliance, Cross-Domain, Emergent) | Count by dimension |
| **Difficulty Distribution** | 20/40/40 (F/I/A) ±5% | Count by level |
| **Causal Chain Depth** | 100% Q&As trace ≥4-level causal chains (Root → Intermediate → Direct → Effects → Outcomes) | Review all |
| **Quantified Relationships** | 100% Q&As have quantified causal impacts (%, β, R², or empirical metrics) | Review all |
| **Multi-Factor Analysis** | ≥70% Q&As analyze ≥2 contributing factors with interaction effects | Review advanced Q&As |
| **Counterfactual Scenarios** | ≥50% Q&As include "what if" alternative scenarios with outcome comparison | Review intermediate/advanced |
| **Trade-offs & Alternatives** | 100% Q&As acknowledge causal trade-offs, confounding factors, or alternative pathways | Review all |
| **Citation Quality** | ≥75% answers ≥1 cite, ≥40% ≥2 cites, ≥20% academic papers | Count per answer |
| **Cross-refs** | 100% [Ref: ID] resolve | Automated check |
| **Recency** | ≥60% sources last 5yr (causality theory is slower-changing), ≥80% tools ≤18mo | Check dates |
| **Diversity** | ≥4 source types (academic papers, books, case studies, empirical research), none >35% | Count by type |
| **Temporal Causality** | ≥40% Q&As analyze time-delayed effects, compound impacts, or accumulation | Review Q&As |
| **Stakeholder Perspectives** | ≥60% Q&As show ≥2 stakeholder viewpoints on the same causal chain | Review Q&As |
| **Causality Tools** | ≥12 modern tools with purpose, pricing, update date, causality dimension support | Check tools section |
| **Link Accessibility** | 100% links accessible or archived (DOI/Wayback) | Verify all links |

## Workflow

### 1. Plan & Build References
**Topic Clusters** (8 lifecycle, 30-35 Q&As, ≥3/phase, 20/40/40 F/I/A):
1. Requirements (4-5), 2. Architecture (4-5), 3. Development (4-5), 4. Testing (5-6), 5. Deployment (4-5), 6. Operations (4-5), 7. Maintenance (3-4), 8. Evolution (3-4)

**References BEFORE Q&As**: Glossary (≥25) → Tools (≥12) → Literature (≥18) → Citations (≥35). Use IDs: G#, T#, L#, A#. Verify: unique, recent (≥60% <5yr theory, ≥80% tools ≤18mo), diverse (≥4 types), accessible

### 2. Write Q&As
**Per answer (150-350 words)**: Include all 10 mandatory elements (see above). **Visuals per cluster**: ≥1 diagram, ≥1 matrix, ≥1 impact table, ≥1 counterfactual. **Check every 5 Q&As**: Verify gates, dimensions covered, chain depth ≥4 levels, 100% quantified

### 3. Validate & Complete
**Execute all 17 gates** (see table). **Complete references**: Glossary (definition, formulas, quantification), Tools (purpose, price, update, dimension support), Literature (APA 7th, frameworks, chapters), Citations (author, year, title, DOI/URL, [EN]/[ZH]). Verify 100% [Ref: ID] resolve

### 4. Final Review
**Check**: Terms defined (100%), Quantified (100%), Coverage (complete), Chain depth ≥4 (100%), Multi-factor (≥70%), Counterfactual (≥50%), Sources (authoritative), Trade-offs (explicit), Temporal (≥40%), Stakeholders (≥60%), TOC/links valid, No redundancy

## Output Format

```markdown
## Contents
- [Coverage Matrix](#coverage-matrix): 8 phases × 5 causality dimensions = 40 cells, ≥3 Q&As per phase, ≥4 per dimension, 30-35 total
- [Topic Clusters](#topic-clusters): 8 lifecycle-aligned (Requirements & Discovery → Evolution & Governance)
- [Q&A by Cluster](#qa-sections): 30-35 Q&As with mandatory 10 elements
- [References](#references): G# (≥25), T# (≥12), L# (≥18), A# (≥35)
- [Validation](#validation-results): 17 gates, all PASS

## Coverage Matrix

| Phase | Technical/System/Ecosystem | Business/Market | Regulatory/Compliance | Cross-Domain | Emergent | Total |
|-------|---------------------------|----------------|----------------------|--------------|----------|-------|
| Requirements & Discovery | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Architecture & Design | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Development | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Testing & Quality | ✓ | ✓ | ✓ | ✓ | ✓ | 5-6 |
| Deployment & Release | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Operations & Observability | ✓ | ✓ | ✓ | ✓ | ✓ | 4-5 |
| Maintenance & Support | ✓ | ✓ | ✓ | ✓ | ✓ | 3-4 |
| Evolution & Governance | ✓ | ✓ | ✓ | ✓ | ✓ | 3-4 |
| **Total** | **≥4** | **≥4** | **≥4** | **≥4** | **≥4** | **30-35** |

## Topic 1: [Cluster Name - Lifecycle Phase]

### Q1: [Causal Chain Scenario Question]
**Difficulty**: [F/I/A] | **Phase**: [Phase] | **Role**: [Role(s)] | **Dimensions**: [Dimension(s)] | **Insight**: [1 sentence] [Ref: ID]

**Answer** (150-350 words): [Include all 10 mandatory elements from section above]

**Visuals**: [Mermaid diagram + tables as needed per cluster requirements]

---

## References

### Glossary (≥25)
**G#. Term**: Definition. Causal relationships. Formula/Quantification. Use case. Distinctions. [EN/ZH]

**Examples**:
**G1. Root Cause**: Fundamental factor that, if eliminated, prevents outcome. Necessary + sufficient. ID via 5-Whys, fishbone. vs. Contributing factors (necessary not sufficient), Symptoms (effects). [EN]
**G2. Causal Strength**: Effect magnitude. β (regression), r (correlation), R² (variance). Formula: β = ΔY/ΔX. β=0.8 (strong), 0.5 (medium), 0.2 (weak). [EN]
**G3. Confounding Variable**: Factor causing spurious X-Y association. Z→X and Z→Y creates false X→Y. Control: randomization, stratification, regression. vs. Mediating (X→Z→Y). [EN]

### Tools (≥12)
**T#. Name** (Category): Purpose. Dimensions. Price. Updated. Integrations. Pros/Cons. URL. [EN/ZH]

**Examples**:
**T1. Vensim** (CLD): System dynamics, feedback loops. Cross-domain, Emergent. $1000/yr, Free reader. 2024-08. Python, R. Pros: Standard, simulation. Cons: Steep curve. https://vensim.com [EN]
**T2. DoWhy** (Inference): Causal reasoning, counterfactuals. Technical, Business. Apache 2.0. 2024-09. Pandas, NumPy. Pros: MS-backed, ML integration. Cons: Stats knowledge needed. https://github.com/py-why/dowhy [EN]
**T3. Miro** (Mapping): Collaborative visualization. Business, Cross-domain. $8-16/user/mo. 2024-11. Jira, Slack. Pros: Easy collab. Cons: Not analytical. https://miro.com [EN]

### Literature (≥18)
**L#. Author(s). (Year). *Title*. Publisher.** Frameworks. Key chapters. [EN/ZH]

**Examples**:
**L1. Pearl, J. (2009). *Causality* (2nd ed.). Cambridge.** Graphical models, counterfactuals, do-calculus. Ch 1-3, 7. [EN]
**L2. Senge, P. (1990). *The Fifth Discipline*. Doubleday.** Systems thinking, feedback loops, CLD. Ch 4-6. [EN]
**L3. Kahneman, D. (2011). *Thinking, Fast and Slow*. FSG.** Causal reasoning biases, pre-mortem. Ch 19, 24. [EN]

### Citations (≥35)
**A#. Author. (Year). *Title*. Source. Focus. DOI/URL. [EN/ZH]**

**Examples**:
**A1. Pearl, J., & Mackenzie, D. (2018). *The Book of Why*. Basic Books.** Causal reasoning, counterfactuals. https://www.basicbooks.com/.../the-book-of-why/... [EN]
**A2. Conway, M. E. (1968). "How Do Committees Invent?" *Datamation*, 14(4).** Conway's Law: org → architecture. http://www.melconway.com/Home/Committees_Paper.html [EN]
**A3. Kohavi, R., et al. (2020). "Online Experiments at Scale." *KDD 2020*.** A/B testing causal inference. DOI: 10.1145/3394486.3406477 [EN]

## Validation Results

| Gate | Requirement | Status | Evidence |
|------|-------------|--------|----------|
| Lifecycle | 8 phases, ≥3 each | ✅ PASS | Req=4, Arch=5, Dev=4, Test=6, Deploy=4, Ops=5, Maint=3, Evol=4 |
| Stakeholder | ≥8/10 roles, ≥2 each | ✅ PASS | BA=3, PM=4, Arch=5, Dev=4, QA=4, DevOps=3, Sec=2, Data=3, SRE=4, Lead=3 |
| Causality Dimensions | 5 dimensions, ≥4 each | ✅ PASS | Technical=8, Business=7, Regulatory=5, Cross-Domain=6, Emergent=5 |
| Difficulty | 20/40/40 ±5% | ✅ PASS | 7F/14I/14A = 20%/40%/40% |
| Causal Chain Depth | ≥4 levels, 100% | ✅ PASS | 35/35 = 100%, avg depth 5.2 levels |
| Quantified Relationships | 100% have %, β, R² | ✅ PASS | 35/35 = 100% quantified |
| Multi-Factor Analysis | ≥70% analyze ≥2 factors | ✅ PASS | 27/35 = 77% multi-factor |
| Counterfactual Scenarios | ≥50% have what-if analysis | ✅ PASS | 19/35 = 54% counterfactual |
| Trade-offs & Alternatives | 100% acknowledge | ✅ PASS | 35/35 = 100% |
| Citations | ≥75% ≥1, ≥40% ≥2, ≥20% academic | ✅ PASS | 83% ≥1, 46% ≥2, 26% academic |
| Cross-refs | 100% [Ref: ID] resolve | ✅ PASS | G1-G27, T1-T14, L1-L20, A1-A38 |
| Recency | ≥60% <5yr, ≥80% tools ≤18mo | ✅ PASS | 71% <5yr, 93% tools ≤18mo |
| Diversity | ≥4 types, none >35% | ✅ PASS | Academic 32%, Books 28%, Case studies 24%, Empirical 16% |
| Temporal Causality | ≥40% analyze time-delayed | ✅ PASS | 15/35 = 43% temporal |
| Stakeholder Perspectives | ≥60% show ≥2 viewpoints | ✅ PASS | 23/35 = 66% multi-stakeholder |
| Causality Tools | ≥12 with dimension support | ✅ PASS | 14: CLD=3, Statistical=4, RCA=2, Mapping=2, BI=2, A/B=1 |
| Links | 100% accessible/archived | ✅ PASS | 52/52 verified |
```

## Example Format

**Q: [Scenario with scale/context]**

**Difficulty**: [F/I/A] | **Phase**: [Phase(s)] | **Roles**: [Role(s)] | **Dimensions**: [Dimension(s)] | **Insight**: [1 sentence on causal strength/confounds/interventions] [Ref: ID]

**Answer** (200-300 words): [Context + scale] → [Causal chain: Root → Intermediate → Direct → Effects → Outcomes with quantified links] → [Multi-factor analysis] → [Temporal dynamics] → [Trade-offs & counterfactuals] [Ref: ID]

**Visuals** (include as needed):
- **Causal Diagram**: Fishbone/influence/CLD showing factor relationships with β coefficients
- **Matrix**: Cause level, factor, necessity/sufficiency scores, causal strength, quantified impact
- **Impact Table**: Outcomes across time periods with baseline, observed, counterfactual comparisons
- **Stakeholder Table**: Role perspectives, optimization goals, conflicting priorities

**Key Elements**: Quantified metrics (%, β, R², time lags), confounding factors, intervention points, stakeholder trade-offs, authoritative citations
