# Enterprise Risk Assessment Framework

Generate evidence-based risk assessment across 5 dimensions × 8 lifecycle phases with quantitative validation and mitigation strategies.

## I. Context & Scope

**Purpose**: Systematic risk identification, assessment, and mitigation across 5 dimensions × 8 lifecycle phases for all stakeholders (BA, PM, Architect, Dev, QA, DevOps, Security, Data, SRE, Leadership).

**Assumptions**: Production-grade distributed systems (>10K rps, >1TB data, multi-team); cloud-native environments; regulated domains; user provides context or accepts generic scenarios.

**Constraints**: 200-400 words/risk (excluding artifacts); ≥80% with mitigation; 100% scenario-based; quantitative scoring required.

**Terms**: Risk (potential event impacting objectives), Probability/Impact (1-5 scale), Risk Score (P×I, range 1-25), Mitigation (preventive/detective/corrective actions), Residual Risk (post-mitigation score), Quality Gate (mandatory validation checkpoint).

**Scope**: Technical debt, market dynamics, compliance, vendor dependencies, financial constraints, security, operations. **Exclude**: Force majeure, theoretical risks without precedent.

**Limitations**: Generic risks need contextualization; probability/impact scoring subjective without historical data; cross-risk dependencies compound impact.

## II. Requirements

### Quantitative Floors

**Risk Coverage**: 40–60 total risks | 200–400 words/analysis | ≥80% with mitigation | ≥60% with quantitative metrics | Each addresses stakeholder impact

**Risk Dimension Coverage (MECE)**:
1. **Technical** (8–12): Architecture, infrastructure, code quality, security, data, performance, integration, operations
2. **Business/Market** (8–12): Competition, market timing, product-market fit, pricing, adoption, revenue, partnerships
3. **Regulatory/Legal** (6–10): Compliance (GDPR, HIPAA, SOC 2), licensing, privacy, contracts, IP, audit
4. **Ecosystem** (6–10): Vendor lock-in, dependencies, platform changes, supply chain, community, standards
5. **Financial** (6–10): Budget overruns, TCO, opportunity cost, funding, burn rate, ROI, debt

**Lifecycle Coverage**: Each phase (Requirements → Evolution) needs ≥3 risks across ≥3 dimensions

**Stakeholder Coverage**: Each role must own ≥2 risks

**References** (build before risk analysis): Glossary ≥15 | Frameworks ≥8 | Tools ≥8 | Literature ≥10 (≥3 risk mgmt, ≥3 industry) | Citations ≥20 APA 7th with [EN]/[ZH] tags

**Visuals**: ≥1 risk matrix + ≥1 mitigation roadmap per dimension | ≥1 heat map across lifecycle

**Scaling**: For >60 risks, multiply reference floors by 1.5×

### Citation Standards

**Format**: APA 7th + tag: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: ID]` (G#=Glossary, F#=Framework, T#=Tool, L#=Literature, C#=Citation)

**Distribution**: EN 50–70% (target 60%) | ZH 20–40% (target 30%) | Other 5–15% (target 10%)

**Source Types** (≥4): Risk frameworks (ISO 31000, FAIR, NIST), Industry research (Gartner, Forrester), Case studies (postmortems, breaches), Risk tools (ServiceNow, Archer), Compliance standards (GDPR, SOC 2)

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

1. **Recency**: ≥60% from last 3yrs (≥80% for cyber/cloud/fintech/health)
2. **Source Diversity**: ≥4 types; no type >30%
3. **Per-Dimension Coverage**: Each dimension has ≥3 authoritative sources + ≥2 frameworks + ≥1 tool
4. **Per-Phase Coverage**: Each phase has ≥3 risks with evidence-based mitigation
5. **Stakeholder Validation**: 100% risks have owner + escalation path
6. **Quantitative Scoring**: ≥80% have P/I scores + financial/time estimates
7. **Mitigation Completeness**: ≥80% high-severity (score ≥15) have 3-tier mitigation
8. **Tool Completeness**: Risk tools include features, integrations, compliance support
9. **Link Validation**: 100% URLs accessible/archived
10. **Cross-Reference Integrity**: 100% [Ref: ID] resolve; no orphans
11. **Dependency Mapping**: Cross-risk dependencies identified
12. **Residual Risk**: All mitigations include residual risk assessment

**Mitigation**: Recency fail → flag dated standards | Diversity fail → expand domains | Scoring fail → use industry benchmarks | Dependency fail → create dependency graph

## III. Execution

### Step 1: Plan Risk Allocation

Distribute 40–60 risks across 5 dimensions × 8 phases. Target: 5–7 risks/dimension, 3–8 risks/phase.

**Severity Distribution Target**: Critical (≥20): 10–15% | High (15–19): 25–30% | Medium (10–14): 40–45% | Low (5–9): 15–20%

### Step 2: Build References (BEFORE risk analysis → run Gates 1–12 after)

**Glossary (≥15)**: Risk, Threat, Vulnerability, Impact, Probability, Mitigation, Residual Risk, Risk Appetite, Risk Tolerance, SLA, SLO, SLI, MTTR, MTBF, RTO, RPO, CVSS, CVE, STRIDE, DREAD, FAIR, ISO 31000, NIST CSF, COBIT, TCO, ROI, Error Budget | Format: term, definition, formula/scale, usage context, related terms | Assign G1, G2...

**Frameworks (≥8)**: ISO 31000 (risk mgmt), FAIR (financial quantification), NIST CSF, STRIDE (threat modeling), DREAD (rating), COBIT (IT governance), TOGAF (architecture risk), OWASP Top 10, CIS Controls, DORA Metrics, SRE principles | Include: purpose, components, application, limitations, references | Assign F1, F2...

**Tools (≥8)**: Risk Management (ServiceNow GRC, Archer, LogicGate, RiskLens), Security (Snyk, SonarQube, Checkmarx, Wiz), Monitoring (Prometheus, Grafana, Datadog, New Relic), Compliance (Vanta, Drata, OneTrust), Incident (PagerDuty, Opsgenie) | Include: category, features, pricing, integrations, compliance support, update date, URL | Assign T1, T2...

**Literature (≥10)**: EN—*Site Reliability Engineering* (Beyer), *Security Engineering* (Anderson), *Release It!* (Nygard), *The Phoenix Project* (Kim), *Accelerate* (Forsgren), ISO 31000:2018, NIST SP 800-30 | ZH (≥3)—风险管理标准, 信息安全管理, 合规性指南 | Include: author, title, year, key concepts, applicability | Assign L1, L2...

**Citations (≥20)**: APA 7th + tags | Verify ≥60% from last 3yrs | Classify: frameworks/standards/research/case studies/tools | Assign C1, C2... | **Alternatives**: Gartner Risk Research, Forrester Security, SANS, OWASP, NIST, ISO, Verizon DBIR, CSA

### Step 3: Generate Risk Assessments (5–10 at a time → self-check each batch)

**Risk Identification**: Scenario-based, contextualized to lifecycle phase | Name: "[Dimension]-[Phase]-[SpecificRisk]" | Root cause analysis | Triggering conditions | Affected stakeholders

**Risk Analysis** (200–400 words):
1. **Risk Statement** (1–2 sentences): Event and consequence
2. **Lifecycle Phase**: When risk manifests
3. **Dimension**: Primary (+ secondary if applicable)
4. **Probability** (1–5): 1=Rare (<10%), 2=Unlikely (10–25%), 3=Possible (25–50%), 4=Likely (50–75%), 5=Almost Certain (>75%) [Ref: F#]
5. **Impact** (1–5): 1=Negligible, 2=Minor, 3=Moderate, 4=Major, 5=Catastrophic (financial, time, reputation) [Ref: F#]
6. **Risk Score**: P × I (range 1–25)
7. **Stakeholder Impact**: Owner, affected teams, escalation path
8. **Root Causes**: Technical/process/organizational [Ref: G#/C#]
9. **Triggers & Indicators**: Leading indicators, monitoring metrics [Ref: T#]
10. **Dependencies**: Related risks, cascading effects
11. **Mitigation Strategy**:
    - **Preventive**: Reduce probability (e.g., architecture review, testing)
    - **Detective**: Monitor/alert (e.g., dashboards, anomaly detection) [Ref: T#]
    - **Corrective**: Response plan (e.g., rollback, DR) [Ref: L#]
    - **Timeline**: Implementation phases with milestones
    - **Cost Estimate**: Resources, tools, time
12. **Residual Risk**: Post-mitigation P/I scores
13. **Success Metrics**: KPIs to validate effectiveness
14. **Citations**: ≥2 [Ref: ID] for high-severity, ≥1 for medium/low
15. **Artifact** (required for Critical/High): Risk matrix, roadmap, decision tree, runbook

**Batch Self-Check** (per 5–10 risks): 
- Scenario-based, contextualized to phase
- 200–400 words
- P/I scored with justification
- Stakeholder owner assigned
- ≥80% have mitigation (3-tier for high-severity)
- ≥4/5 have ≥1 citation
- Financial/time estimates for high-severity
- Residual risk calculated

### Step 4: Create Visuals

**Risk Matrices (5×5 per dimension)**: Plot by P (Y) × I (X) | Color zones: Green (1–6), Yellow (8–12), Orange (15–16), Red (≥20) | Label with ID

**Mitigation Roadmaps (per dimension)**: Gantt timeline showing preventive/detective/corrective actions with owners, milestones, dependencies | Include Quick Wins, Strategic Initiatives, Backlog

**Lifecycle Heat Map**: 8 phases (cols) × 5 dimensions (rows) | Cell intensity = aggregated risk score | Include risk count/cell

**Additional Artifacts**:
- **Technical**: STRIDE threat model, dependency graph, failure mode tree
- **Business/Market**: Competitive landscape, market timing, adoption funnel with risk points
- **Regulatory/Legal**: Compliance matrix, audit timeline, data flow with PII markers
- **Ecosystem**: Vendor dependency map, integration risk matrix, platform roadmap alignment
- **Financial**: Cost breakdown (OpEx/CapEx), burn rate projection, ROI sensitivity

**Risk Dependency Graph**: Network diagram showing cascading risks

**Best Practices**: Consistent color coding | Include severity scores | Show mitigation status | Cite sources | Include legends + timestamps

### Step 5: Populate References

**Glossary**: **G#. Term (Acronym)** | Definition (scale/formula) | Usage context | Related terms | Limitations | Alphabetize

**Frameworks**: **F#. Framework Name** | Purpose | Components | Application | Limitations | Source

**Tools**: **T#. Tool (Category)** | Description | Features | Pricing | Integrations (≥3) | Compliance | Update (Q# YYYY) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (key concepts, frameworks, cases) | Applicability (industry, phase, dimension) | Relevance | Group by language

**Citations**: **C#. [Citation] [Lang]** | APA 7th format | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | Citations have APA + tags | Tools have compliance documented

### Step 6: Run 18 Validations (fail ANY = stop, fix, re-run ALL)

1. **Floors**: G≥15, F≥8, T≥8, L≥10, C≥20, Risks=40–60
2. **Dimension Coverage**: 5/5 dimensions ≥5 risks; distribution 8–12/dimension (±2)
3. **Phase Coverage**: 8/8 phases ≥3 risks across ≥3 dimensions
4. **Severity Distribution**: Crit (≥20): 10–15% | High (15–19): 25–30% | Med (10–14): 40–45% | Low (5–9): 15–20%
5. **Stakeholder Assignment**: 100% have owner + escalation; each stakeholder owns ≥2
6. **Mitigation Coverage**: ≥80% have strategy; ≥80% high-severity (≥15) have 3-tier
7. **Quantitative Scoring**: 100% have P/I scores with justification; ≥60% have estimates
8. **Residual Risk**: 100% mitigated risks have residual documented
9. **Citations**: ≥80% risks ≥1 citation; ≥60% high-severity ≥2
10. **Language Distribution**: EN: 50–70%, ZH: 20–40%, Other: 5–15%
11. **Recency**: ≥60% from 3yrs (≥80% cyber/cloud/fintech/health)
12. **Source Diversity**: ≥4 types; no type >30%
13. **Links**: 100% URLs accessible/archived
14. **Cross-References**: 100% [Ref: ID] resolve; no orphans
15. **Word Count**: Sample 10 risks; 100% within 200–400 words
16. **Framework Application**: ≥80% correctly apply frameworks + cite + document limits
17. **Dependency Mapping**: Graph includes all cascading risks; ≥30% risks have dependencies documented
18. **Artifact Completeness**: 100% Crit/High have artifacts; ≥50% Med have artifacts

### Step 7: Final Review

**Risk Quality** (sample ≥10 across dimensions/phases): 
- **Clarity**: Concrete, measurable, contextualized
- **Relevance**: Real-world precedent (case studies, breaches, postmortems)
- **Completeness**: All 15 components present
- **Actionability**: Mitigation specific, costed, time-bound with owners
- **Quantification**: P/I justified with data/benchmarks
- **Stakeholder Alignment**: Owner has authority/capability; escalation appropriate

**Cross-Dimension Balance**: No over/under-representation; technical doesn't dominate

**Lifecycle Realism**: Risks contextualized to phase maturity

**Mitigation Feasibility**: Implementable given constraints; no unrealistic dependencies

**Stakeholder Review Checklist**:
- **Leadership**: High-severity escalation paths correct; financial estimates reasonable; risk appetite aligned
- **Architect**: Technical risks architecturally sound; mitigation doesn't introduce greater risk
- **Security**: Threat models complete; compliance has regulatory mapping; residual acceptable
- **SRE**: Operational risks include monitoring/alerting; MTTR/RTO realistic
- **DevOps**: Deployment risks have rollback plans; pipeline security validated
- **PM**: Business risks prioritized; market timing analyzed; competitive threats assessed
- **Finance**: Cost includes TCO (not just CapEx); ROI assumptions documented

**Submission Checklist**: 
- All 18 validations PASS
- All floors met
- All 12 quality gates passed
- TOC with risk taxonomy
- No placeholders/TBDs
- Consistent formatting
- Balanced coverage
- Risk register exportable (CSV/JSON)
- Heat maps/matrices timestamped
- Executive summary with top 10 risks + mitigation priorities

## IV. Validation Report (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check                    | Measurement                                    | Criteria                                      | Result | Status    |
|---|--------------------------|------------------------------------------------|-----------------------------------------------|--------|-----------|
| 1 | Floors                   | G:__ F:__ T:__ L:__ C:__ Risks:__              | G≥15, F≥8, T≥8, L≥10, C≥20, Risks:40-60       |        | PASS/FAIL |
| 2 | Dimension Coverage       | Tech:__ Biz:__ Reg:__ Eco:__ Fin:__            | Each dimension: 8-12 risks (±2)               |        | PASS/FAIL |
| 3 | Phase Coverage           | __/8 phases have ≥3 risks across ≥3 dimensions | 8/8                                           |        | PASS/FAIL |
| 4 | Severity Distribution    | Crit:__% High:__% Med:__% Low:__%              | Crit:10-15%, High:25-30%, Med:40-45%, Low:15-20% |     | PASS/FAIL |
| 5 | Stakeholder Assignment   | __/__ risks have owner+escalation              | 100%; each stakeholder owns ≥2                |        | PASS/FAIL |
| 6 | Mitigation Coverage      | __% have strategy; __% high-severity 3-tier    | ≥80% strategy; ≥80% high 3-tier               |        | PASS/FAIL |
| 7 | Quantitative Scoring     | __% have P/I scores; __% have estimates        | 100% scores; ≥60% estimates                   |        | PASS/FAIL |
| 8 | Residual Risk            | __/__ mitigated risks have residual            | 100%                                          |        | PASS/FAIL |
| 9 | Citations                | __%≥1, __%≥2 (high-severity)                   | ≥80%≥1, ≥60% high≥2                           |        | PASS/FAIL |
| 10| Language Distribution    | EN:__%, ZH:__%, Other:__%                      | EN:50-70%, ZH:20-40%, Other:5-15%             |        | PASS/FAIL |
| 11| Recency                  | __% from 3yrs (domain: ___)                    | ≥60% (≥80% cyber/cloud/fintech/health)        |        | PASS/FAIL |
| 12| Source Diversity         | __ types; max __%                              | ≥4 types, max 30%                             |        | PASS/FAIL |
| 13| Links                    | __/__ accessible                               | 100%                                          |        | PASS/FAIL |
| 14| Cross-References         | __/__ resolved                                 | 100%                                          |        | PASS/FAIL |
| 15| Word Count               | __ sampled: __ compliant                       | 100% (200-400)                                |        | PASS/FAIL |
| 16| Framework Application    | __/__ correct+cited+limits                     | ≥80%                                          |        | PASS/FAIL |
| 17| Dependency Mapping       | __% risks have dependencies documented         | ≥30%                                          |        | PASS/FAIL |
| 18| Artifact Completeness    | Crit/High:__% Med:__%                          | Crit/High:100%, Med:≥50%                      |        | PASS/FAIL |

## V. Risk Quality (review each; fails ≥2 criteria = revise/replace)

1. **Clarity**: Specific, measurable event + consequence | ✓ "Database migration fails during deployment causing 4hr+ downtime" | ✗ "System might have issues"

2. **Contextualization**: Tied to specific lifecycle phase | ✓ "Requirements phase: Incomplete NFRs lead to architecture redesign in Development (3mo delay, $500K)" | ✗ "Project delays happen"

3. **Quantification**: P/I scored with justification | ✓ "P=4 (60% microservices migrations encounter schema conflicts—DORA 2023); I=4 ($800K, 8wk delay, churn)" | ✗ "High risk"

4. **Actionability**: Mitigation specific, costed, owned | ✓ "Preventive: Schema versioning + test in staging ($20K, 2wk, DevOps). Detective: Health dashboard. Corrective: Rollback automation (1hr RTO)" | ✗ "Test more"

5. **Realism**: Based on precedent | ✓ "GitLab 2017 DB incident (6hr loss, 5K users) demonstrates severity [Ref: C12]" | ✗ "Theoretical worst-case"

6. **Stakeholder Alignment**: Owner has authority | ✓ "Owner: DevOps Lead (budget + staging access). Escalation: CTO if RTO >2hr or revenue-impacting" | ✗ "Owner: Junior dev"

7. **Completeness**: All 15 components | ✓ Has statement, phase, dimension, P/I, stakeholder, causes, triggers, dependencies, 3-tier mitigation, residual, metrics, citation, artifact | ✗ Missing mitigation/residual

8. **Dimension Appropriateness**: Correctly categorized | ✓ Technical: Architecture coupling causing deployment failures | ✗ Calling budget overrun technical (should be Financial)

## VI. Output Format

### A. TOC
1. Executive Summary (Top 10 risks + priorities) | 2. Risk Taxonomy (5×8 matrix) | 3. Risk Register | 4. Mitigation Roadmap | 5. References | 6. Validation Report | 7. Appendices (Heat maps, dependency graph, RACI)

### B. Risk Taxonomy Overview
**Total Risks**: [40–60] | **Severity**: Critical [X] ([Y]%) / High [X] ([Y]%) / Medium [X] ([Y]%) / Low [X] ([Y]%) | **Coverage**: 5 dimensions × 8 phases (MECE)

| # | Dimension          | Risk Count | Severity Mix (C/H/M/L) | Artifacts                                    |
|---|--------------------|------------|-------------------------|----------------------------------------------|
| 1 | Technical          | 8–12       | 2C/3H/4M/2L             | Risk matrix + Threat model + Roadmap         |
| 2 | Business/Market    | 8–12       | 1C/3H/5M/2L             | Risk matrix + Competitive analysis + Roadmap |
| 3 | Regulatory/Legal   | 6–10       | 1C/2H/4M/1L             | Risk matrix + Compliance matrix + Roadmap    |
| 4 | Ecosystem          | 6–10       | 1C/2H/4M/2L             | Risk matrix + Dependency map + Roadmap       |
| 5 | Financial          | 6–10       | 1C/3H/3M/2L             | Risk matrix + Cost sensitivity + Roadmap     |
|   | **Total**          | **50**     | **7C/13H/20M/9L**       | **5 matrices + 5 roadmaps + heat map + graph** |

Legend: C=Critical (≥20) | H=High (15–19) | M=Medium (10–14) | L=Low (5–9)

### C. Lifecycle Phase Distribution

| Phase                       | Tech | Biz | Reg | Eco | Fin | **Total** | **Top Score** |
|-----------------------------|------|-----|-----|-----|-----|-----------|---------------|
| 1. Requirements & Discovery | 2    | 3   | 2   | 1   | 2   | **10**    | 20 (Crit)     |
| 2. Architecture & Design    | 2    | 1   | 2   | 2   | 1   | **8**     | 18 (High)     |
| 3. Development              | 2    | 1   | 1   | 2   | 1   | **7**     | 16 (High)     |
| 4. Testing & Quality        | 1    | 1   | 1   | 1   | 1   | **5**     | 15 (High)     |
| 5. Deployment & Release     | 1    | 1   | 1   | 1   | 1   | **5**     | 20 (Crit)     |
| 6. Operations & Observability | 1  | 1   | 0   | 0   | 1   | **3**     | 16 (High)     |
| 7. Maintenance & Support    | 1    | 1   | 1   | 0   | 1   | **4**     | 12 (Med)      |
| 8. Evolution & Governance   | 0    | 1   | 0   | 1   | 0   | **2**     | 12 (Med)      |
| **Total**                   | **10** | **10** | **8** | **8** | **8** | **50** | - |

### D. Risk Entry Format

**Dimension: [Technical/Business/Regulatory/Ecosystem/Financial]**

**RISK-[ID]: [Dimension]-[Phase]-[SpecificRisk]**

**Risk Statement**: [1–2 sentences: event + consequence]

**Lifecycle Phase**: [Requirements/Design/Development/Testing/Deployment/Operations/Maintenance/Evolution]

**Probability** (1–5): [Score] | [Justification with data/precedent] [Ref: F#/C#]

**Impact** (1–5): [Score] | Financial: [$X], Time: [X wks], Reputation: [churn, SLA breach, penalty]

**Risk Score**: [P × I] | Severity: [Critical/High/Medium/Low]

**Stakeholder Impact**:
- **Owner**: [Role with authority/capability]
- **Affected Teams**: [List]
- **Escalation Path**: [Conditions → Role]

**Root Causes**: [Technical/process/organizational] [Ref: G#/C#]

**Triggers & Indicators**: 
- **Leading Indicators**: [Metrics to monitor]
- **Monitoring**: [Tools, dashboards, alerts] [Ref: T#]

**Dependencies**: [Related risks, cascading] | Cross-refs: [RISK-IDs]

**Mitigation Strategy** (200–400 words total):

1. **Preventive** (reduce probability):
   - Actions: [Steps]
   - Owner: [Role]
   - Timeline: [Duration]
   - Cost: [$X or hours]
   - Tools: [Ref: T#]

2. **Detective** (early detection):
   - Monitoring: [Dashboards, alerts, thresholds]
   - Tools: [Ref: T#]
   - SLA: [Detection target]

3. **Corrective** (response):
   - Actions: [Rollback, DR, failover]
   - Owner: [Role]
   - RTO/RPO: [Targets]
   - Runbook: [Link]
   - Tools: [Ref: T#]

**Residual Risk**:
- Post-mitigation Probability: [Score]
- Post-mitigation Impact: [Score]
- Residual Score: [P × I]
- Acceptance: [Why acceptable or escalation]

**Success Metrics**: [KPIs to validate effectiveness]

**Citations**: [Ref: C#, C#, ...] (≥2 for Crit/High, ≥1 for Med/Low)

**Artifact** *(required for Crit/High)*: [Matrix position, timeline, tree, runbook, dashboard]

---

**Example Entry**:

**RISK-T-DEV-01: Technical-Development-UntestedDatabaseMigration**

**Risk Statement**: Database schema migration deployed without comprehensive staging testing causes data inconsistency, application errors, and extended downtime (4–8 hours) requiring rollback or emergency hotfix.

**Lifecycle Phase**: Development

**Probability** (1–5): 4 | 60% of organizations experience migration incidents in microservices within first year (DORA 2023); team lacks automated testing [Ref: C15]

**Impact** (1–5): 4 | Financial: $800K (labor $200K + revenue $500K/hr × 4hr + churn $100K), Time: 8wk recovery, Reputation: SLA breach (99.9%→99.5%), 3 enterprise escalations

**Risk Score**: 16 | Severity: High

**Stakeholder Impact**:
- **Owner**: DevOps Lead (staging authority, pipeline control, $50K budget)
- **Affected Teams**: Backend (schema changes), QA (test data), SRE (incident response), CS (escalations)
- **Escalation Path**: If RTO >2hr or revenue-impacting → CTO; if SLA breach → CEO + customers

**Root Causes**: [Ref: G8-Technical Debt] Insufficient test coverage; no schema versioning; staging-production drift; manual deployment susceptible to error

**Triggers & Indicators**:
- **Leading Indicators**: Rising CI test failures; schema complexity +20%/quarter; staging-prod config drift
- **Monitoring**: Schema health dashboard (Grafana) [Ref: T5]; error rate >1% sustained 5min [Ref: T6]; connection pool exhaustion

**Dependencies**: Cross-refs: RISK-T-DEP-02 (rollback failure amplifies impact), RISK-B-OPS-01 (churn accelerates during peak)

**Mitigation Strategy**:

1. **Preventive** (reduce to P=2):
   - Actions: (1) Implement Liquibase/Flyway [Ref: T3]; (2) automated CI testing with production-like volume (10K+ rows); (3) staging parity validation (weekly drift detection); (4) peer review for schema changes
   - Owner: DevOps Lead (implementation) + Backend Lead (review)
   - Timeline: 6wk (2wk setup + 2wk harness + 2wk rollout)
   - Cost: $25K (Liquibase $15K/yr + 80 hours $10K)
   - Tools: [Ref: T3-Liquibase, T4-Testcontainers]

2. **Detective** (5min SLA):
   - Monitoring: Health dashboard (pre-checks, progress, post-validation) [Ref: T5-Grafana]; alert on error >0.5% or p95 >500ms (baseline 200ms)
   - Tools: [Ref: T5-Grafana, T6-Prometheus]
   - SLA: Alert 2min; incident declared 5min

3. **Corrective** (RTO 1hr):
   - Actions: (1) Automated rollback (DB restore from pre-migration snapshot + app revert); (2) hotfix process (expedited review + canary); (3) communication template
   - Owner: SRE on-call (execution) + DevOps Lead (hotfix approval)
   - RTO/RPO: 1hr RTO (30min detect + 30min rollback), 15min RPO (transaction log shipping)
   - Runbook: [/runbooks/db-migration-incident.md]
   - Tools: [Ref: T7-PagerDuty, T8-Backup/restore]

**Residual Risk**:
- Post-mitigation Probability: 2 (Unlikely, 10–25%)
- Post-mitigation Impact: 3 (Moderate, $200K + 2wk)
- Residual Score: 6 (Low)
- Acceptance: Within risk appetite (score <10); further reduction (blue-green DB) cost-prohibitive ($200K+ infra) for current scale; revisit at 100K+ users

**Success Metrics**: Zero migration incidents in 12mo; 100% pass staging validation; mean cycle time <3 days (PR→production)

**Citations**: 
- [Ref: C15] Forsgren, N., et al. (2023). *DORA State of DevOps Report*. Google Cloud. [EN]
- [Ref: C16] Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. (Ch. 4: Schema Evolution) [EN]
- [Ref: C17] Richardson, C. (2018). *Microservices Patterns*. Manning. (Pattern: Database per Service) [EN]

**Artifact**: 
- Risk matrix: P=4, I=4 (upper-right red zone)
- Mitigation timeline: [Gantt: 6-week preventive with milestones]
- Runbook: [Flowchart: detection → diagnosis → rollback decision → execution → validation → communication]

### E. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition (scale/formula) | Usage | Related | Limitations | Alphabetize

**Frameworks**: **F#. Framework Name** | Purpose | Components | Application | Limitations | Source

**Tools**: **T#. Tool (Category)** | Description | Features | Pricing | Integrations (≥3) | Compliance | Update (Q# YYYY) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (concepts, frameworks, cases) | Applicability (industry, phase, dimension) | Relevance | Group by language

**Citations**: **C#. [Citation] [Lang]** | APA 7th + tags

## VII. Risk Assessment Template (Ready-to-Use)

```markdown
# Enterprise Risk Assessment: [Project/System Name]

**Assessment Date**: [YYYY-MM-DD]  
**Scope**: [System scope, e.g., "Payment processing microservices"]  
**Team**: [Size, structure]  
**Context**: [Key constraints: budget, timeline, regulatory]

---

## Executive Summary

### Top 10 Risks (by severity)

| Rank | Risk ID | Risk Name | Score | Dimension | Phase | Owner | Priority |
|------|---------|-----------|-------|-----------|-------|-------|----------|
| 1    | RISK-T-DEP-01 | Deployment rollback failure | 20 (C) | Technical | Deployment | DevOps Lead | Immediate |
| 2    | RISK-B-REQ-01 | Market timing misalignment | 18 (H) | Business | Requirements | PM | High |
| ...  | ...         | ...                         | ...    | ...       | ...        | ...       | ...       |

### Mitigation Priorities

**Immediate (Week 1-4)**: [Critical risks]  
**High Priority (Month 2-3)**: [High-severity]  
**Strategic (Quarter 2-4)**: [Medium systemic]  
**Backlog**: [Low-severity, monitor]

---

## Risk Taxonomy

[Insert 5×8 matrix: dimension × phase with counts + heat map]

---

## Risk Register

### Technical Risks

**RISK-T-DEV-01: Technical-Development-UntestedDatabaseMigration**

[Full entry following format from Section VI.D]

---

[Continue for all 40-60 risks by dimension]

---

## References

### Glossary

**G1. Risk Score** | P × I (range 1–25) | Risk prioritization | Related: P, I, Severity | Limitations: Subjective without historical data

[Continue for ≥15 terms]

### Frameworks

**F1. ISO 31000:2018** | Enterprise risk mgmt | Principles, framework, process | Apply across phases | Generic—requires context | ISO (2018)

[Continue for ≥8 frameworks]

### Tools

[≥8 tools with specifications]

### Literature

[≥10 sources with ≥3 risk mgmt]

### Citations

[≥20 APA 7th with tags]

---

## Validation Report

[Insert completed 18-validation table from Section IV]

---

## Appendices

### A. Risk Matrices (by Dimension)

[5×5 grids for each dimension]

### B. Lifecycle Heat Map

[8 phases × 5 dimensions with color-coded intensity]

### C. Mitigation Roadmap

[Gantt: all activities with owners, timelines, dependencies]

### D. Risk Dependency Graph

[Network diagram: cascading risks]

### E. Stakeholder RACI

[RACI matrix: risk ownership across roles]

```

---

## VIII. Quality Checklist (Before Submission)

✅ All 18 validations PASS  
✅ Executive summary with top 10 risks  
✅ Risk taxonomy complete  
✅ All 40-60 risks have complete 15-component analysis  
✅ All Crit/High have visual artifacts  
✅ All risks have owners + escalation  
✅ All high-severity have 3-tier mitigation  
✅ Mitigation roadmap with timeline + costs  
✅ References complete (G≥15, F≥8, T≥8, L≥10, C≥20)  
✅ All citations resolve with APA 7th + tags  
✅ Heat maps + dependency graph included  
✅ Stakeholder RACI complete  
✅ No placeholders/TBDs  
✅ Consistent formatting (IDs, scales, colors)  
✅ Risk register exportable (CSV/JSON)  
✅ Reviewed by ≥3 stakeholder roles
