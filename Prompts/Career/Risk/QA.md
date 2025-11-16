# Enterprise Risk Assessment Framework (Minimal Viable)

Decision-critical risk tracking: 6-12 risks × 3-4 dimensions × 4-5 lifecycle phases with quantitative validation.

**Mission**: Generate 6-12 decision-critical risks identifying, assessing, mitigating threats that block decisions or create material risk. Focus: minimal viable news tracking with time constraints.

**Context**: Production systems (>10K rps, >1TB data), regulated industries, multi-team  
**Output**: 6-12 risks (200-350w) | ≥80% mitigated | ≥70% quantified | EN 60-70%, ZH 20-30%, Other 5-10% | ≥50% refs <2yr  
**Success**: 12/12 validation PASS + decision-critical insights

## I. Decision Criticality Framework

**Include risk if ≥1 criterion satisfied**:
1. **Blocks Decision**: Directly impacts go/no-go, resource allocation, strategic pivot, release gate
2. **Creates Material Risk**: Identifies threat with quantified impact (financial, regulatory, operational, reputational)
3. **Affects ≥2 Stakeholders**: Multi-team impact (e.g., DevOps + SRE, Security + Compliance, Architect + PM)
4. **Actively Evolving**: Market/tech/regulatory changes in past 3-6 months
5. **High Adoption Barrier**: >40h effort; blocks velocity or compliance

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Force majeure, Unproven

## II. Requirements

### Coverage Floors

**Total**: 6–12 risks | 200–350 words each | ≥80% mitigated | ≥70% quantified

**Dimensions (MECE, 3-4 decision-critical)**:
1. **Technical** (2–4): Architecture, infra, security, data, performance, integration, ops
2. **Regulatory/Legal** (1–3): Compliance (GDPR, HIPAA, SOC 2), privacy, audit, licensing
3. **Business/Market** (1–3): Competition, timing, adoption, revenue, partnerships
4. **Financial** (1–2): Budget, TCO, burn rate, ROI (optional if material)

**Lifecycle (4-5 decision-critical phases)**:
- Phase 1: Requirements & Discovery
- Phase 2: Architecture & Design
- Phase 3: Development & Testing
- Phase 4: Deployment & Operations
- Phase 5: Evolution & Governance (optional if decision-critical)

**Stakeholder**: ≥5 core roles (≥60% multi-stakeholder)
- Architect, Developer, SRE, PM, Security, Leadership

**References** (build first, proportional 60-75% reduction): 
- Glossary ≥10 | Frameworks ≥5 | Tools ≥5 | Literature ≥6 (≥2 risk mgmt) | Citations ≥10 APA 7th [EN]/[ZH]

**Visuals**: ≥1 matrix + ≥1 roadmap | ≥1 heat map

**Scaling**: >12 risks → multiply floors by 1.5×

### Citations

**Format**: APA 7th + tag: `Author. (Year). *Title*. [EN]` | Inline: `[Ref: ID]` (G#/F#/T#/L#/C#)

**Distribution**: EN 50–70% | ZH 20–40% | Other 5–15%

**Types** (≥4): Frameworks (ISO 31000, FAIR, NIST), Research (Gartner, Forrester), Case studies, Tools, Standards

### Quality Gates (fail ANY = stop, fix, re-run ALL)

1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Evolving/Adoption)
2. **Recency**: ≥60% from 3yrs (≥80% cyber/cloud/fintech/health)
3. **Dimension**: Each has ≥2 sources + ≥1 framework + ≥1 tool
4. **Phase**: Each has ≥2 risks with evidence-based mitigation
5. **Ownership**: 100% have owner + escalation; ≥60% multi-stakeholder
6. **Scoring**: 100% have P/I + financial/time estimates
7. **Mitigation**: ≥80% high-severity (≥15) have 3-tier mitigation
8. **Links**: 100% accessible
9. **Cross-Refs**: 100% resolve; no orphans
10. **Dependencies**: ≥30% documented
11. **Residual**: All mitigations include residual assessment
12. **Quantification**: ≥70% quantified (financial, time, metrics)

**Fixes**: Decision Criticality → filter non-critical | Recency → flag dated | Scoring → use benchmarks | Dependencies → create graph

## III. Execution

### 1. Plan Allocation (Minimal)

Distribute 6–12 risks: 2–4/dimension, 1–3/phase.

**Severity Target**: Critical (≥20): 15–25% | High (15–19): 40–50% | Med (10–14): 25–35% | Low (5–9): ≤10%

### 2. Build References (Minimal, run Gates after)

**Glossary (≥10)**: Risk, Threat, Vulnerability, Impact, Probability, Mitigation, Residual, Appetite, Tolerance, RTO, RPO, MTTR, CVSS, STRIDE, FAIR | **Format**: term, definition, context | Assign G1-G#

**Frameworks (≥5)**: ISO 31000, FAIR, NIST CSF, STRIDE, OWASP Top 10 | **Format**: purpose, application, limits | Assign F1-F#

**Tools (≥5)**: Risk (ServiceNow GRC, Archer), Security (Snyk, SonarQube), Monitor (Prometheus, Grafana), Compliance (Vanta, Drata), Incident (PagerDuty) | **Format**: category, features, pricing, integrations (≥2), URL | Assign T1-T#

**Literature (≥6)**: EN—*SRE* (Beyer), *Security Engineering* (Anderson), *Release It!* (Nygard), *Accelerate* (Forsgren), ISO 31000:2018 | ZH (≥1)—风险管理 | **Format**: author, title, year, applicability | Assign L1-L#

**Citations (≥10)**: APA 7th + [EN]/[ZH] | ≥60% from 3yrs | Types: frameworks/standards/research/cases | Assign C1-C# | **Alternatives**: Gartner, Forrester, NIST, Verizon DBIR

### 3. Generate Risks (batch 2–3, self-check each)

**ID**: [Dimension]-[Phase]-[SpecificRisk]

**Components** (200–350 words, minimal viable):
1. **Statement** (1–2 sent): Event + consequence
2. **Phase**: When manifests
3. **Dimension**: Primary
4. **Decision Criticality**: [Criterion met: Blocks/Risk/Stakeholders/Evolving/Adoption]
5. **Probability** (1–5): Score + justification [Ref: F#]
6. **Impact** (1–5): Score + financial/time/reputation [Ref: F#]
7. **Score**: P × I (1–25) | Severity
8. **Stakeholders**: Owner, affected, escalation (≥2 roles)
9. **Root Causes**: Tech/process/org [Ref: G#/C#]
10. **Triggers**: Leading indicators, monitoring [Ref: T#]
11. **Mitigation**:
    - **Prevent**: Actions, owner, timeline, cost [Ref: T#]
    - **Detect**: Monitoring, SLA [Ref: T#]
    - **Correct**: Response, RTO/RPO, runbook [Ref: T#]
12. **Residual**: Post-mitigation P/I, score, acceptance
13. **Metrics**: KPIs
14. **Citations**: ≥1 [Ref] (≥2 for high)
15. **Artifact** (Crit/High): Matrix, roadmap, or runbook

**Batch Check**:
- Decision-critical (≥1 criterion)
- Phase-contextualized
- 200–350 words
- P/I scored + justified
- Owner assigned
- ≥80% mitigated (3-tier for high)
- ≥70% quantified
- Residual calculated

### 4. Create Visuals (Minimal)

**Risk Matrix** (5×5): P (Y) × I (X) | Zones: Green (1–6), Yellow (8–12), Orange (15–16), Red (≥20) | Label IDs

**Roadmap** (per dimension): Gantt—prevent/detect/correct with owners, milestones | Sections: Quick Wins, Strategic

**Heat Map**: 4-5 phases (cols) × 3-4 dimensions (rows) | Intensity = aggregated score | Include count/cell

**Domain Artifacts** (decision-critical only):
- **Technical**: STRIDE model or dependency graph
- **Regulatory**: Compliance matrix or audit timeline
- **Business**: Competitive landscape or adoption funnel
- **Financial**: OpEx/CapEx or burn rate (if material)

**Standards**: Consistent colors | Severity scores | Mitigation status | Citations | Timestamps

### 5. Populate References

**Glossary**: **G#. Term (Acronym)** | Definition (scale/formula) | Context | Related | Limits | Alphabetical

**Frameworks**: **F#. Name** | Purpose | Components | Application | Limits | Source

**Tools**: **T#. Tool (Category)** | Desc | Features | Pricing | Integrations (≥3) | Compliance | Update (Q# YYYY) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (concepts, frameworks) | Applicability (industry, phase, dimension) | Relevance | Group by language

**Citations**: **C#. [Citation] [Lang]** | APA 7th | Sort by ID

**Verify**: 100% resolve | No orphans | Complete fields | APA + tags | Tools compliance documented

### 6. Validate (fail ANY = stop, fix, re-run ALL)

1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Evolving/Adoption)
2. **Floors**: G≥10, F≥5, T≥5, L≥6, C≥10, Risks=6–12
3. **Dimensions**: 3-4/3-4 ≥2 risks; 2–4/dimension
4. **Phases**: 4-5/4-5 ≥1 risk across ≥2 dimensions
5. **Severity**: Crit 15–25%, High 40–50%, Med 25–35%, Low ≤10%
6. **Ownership**: 100% owner+escalation; ≥60% multi-stakeholder
7. **Mitigation**: ≥80% have strategy; ≥80% high (≥15) 3-tier
8. **Scoring**: 100% P/I justified; ≥70% quantified
9. **Citations**: ≥80% ≥1; ≥50% high ≥2
10. **Recency**: ≥60% from 3yrs (≥80% cyber/cloud/fintech/health)
11. **Links**: 100% accessible
12. **Artifacts**: Crit/High 100%, Med ≥50%

### 7. Review

**Quality** (sample ≥10):
- **Clarity**: Concrete, measurable, contextualized
- **Relevance**: Real precedent (cases, breaches, postmortems)
- **Completeness**: All 15 components
- **Actionability**: Mitigation specific, costed, owned, time-bound
- **Quantification**: P/I data-justified
- **Alignment**: Owner has authority; escalation appropriate

**Balance**: No dimension over/under-represented

**Realism**: Phase-contextualized; feasible mitigation

**Stakeholder Verification**:
- **Leadership**: Escalation correct; estimates reasonable; appetite aligned
- **Architect**: Tech risks sound; mitigation doesn't add risk
- **Security**: Threat models complete; compliance mapped; residual acceptable
- **SRE**: Ops include monitoring; MTTR/RTO realistic
- **DevOps**: Deployment has rollback; pipeline secure
- **PM**: Business prioritized; timing analyzed; competition assessed
- **Finance**: TCO included; ROI assumptions documented

**Final Checks**:
- All 18 validations PASS
- Floors met
- 12 gates passed
- TOC with taxonomy
- No placeholders
- Consistent format
- Balanced coverage
- Exportable register (CSV/JSON)
- Heat maps timestamped
- Executive summary: top 10 + priorities

## IV. Validation Report (Minimal, fill all; ANY fail = stop, fix, re-run ALL)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Decision Criticality | __% satisfy ≥1 criterion | 100% | | PASS/FAIL |
| 2 | Floors | G:__ F:__ T:__ L:__ C:__ Risks:__ | G≥10, F≥5, T≥5, L≥6, C≥10, 6-12 | | PASS/FAIL |
| 3 | Dimensions | Tech:__ Reg:__ Biz:__ Fin:__ | 3-4/3-4; 2-4 each | | PASS/FAIL |
| 4 | Phases | __/4-5 ≥1 risk ≥2 dimensions | 4-5/4-5 | | PASS/FAIL |
| 5 | Severity | Crit:__% High:__% Med:__% Low:__% | C:15-25%, H:40-50%, M:25-35%, L:≤10% | | PASS/FAIL |
| 6 | Ownership | __/__ owner+escalation; __%multi | 100%; ≥60% | | PASS/FAIL |
| 7 | Mitigation | __%strategy; __%high 3-tier | ≥80% strategy; ≥80% high 3-tier | | PASS/FAIL |
| 8 | Scoring | 100% P/I; __%quantified | 100% P/I; ≥70% quantified | | PASS/FAIL |
| 9 | Citations | __%≥1, __%high≥2 | ≥80%≥1, ≥50%high≥2 | | PASS/FAIL |
| 10| Recency | __% from 3yrs (domain:__) | ≥60% (≥80% cyber/cloud/fintech/health) | | PASS/FAIL |
| 11| Links | __/__ accessible | 100% | | PASS/FAIL |
| 12| Artifacts | Crit/High:__%Med:__% | C/H:100%, M:≥50% | | PASS/FAIL |

## V. Quality Standards

1. **Clarity**: Specific, measurable event+consequence | ✓ "DB migration fails, 4hr+ downtime" | ✗ "System issues"

2. **Context**: Phase-tied | ✓ "Requirements: Incomplete NFRs → redesign in Dev (3mo, $500K)" | ✗ "Project delays"

3. **Quantification**: P/I justified | ✓ "P=4 (60% migrations fail—DORA 2023); I=4 ($800K, 8wk, churn)" | ✗ "High risk"

4. **Actionability**: Specific, costed, owned | ✓ "Prevent: Schema versioning + staging test ($20K, 2wk, DevOps). Detect: Dashboard. Correct: Auto-rollback (1hr RTO)" | ✗ "Test more"

5. **Realism**: Precedent-based | ✓ "GitLab 2017 DB incident (6hr loss) [Ref: C12]" | ✗ "Theoretical worst-case"

6. **Alignment**: Owner authority | ✓ "Owner: DevOps Lead (budget+access). Escalate: CTO if RTO>2hr" | ✗ "Owner: Junior dev"

7. **Completeness**: All 15 components | ✓ Statement, phase, dimension, P/I, stakeholder, causes, triggers, dependencies, 3-tier, residual, metrics, citations, artifact | ✗ Missing mitigation

8. **Categorization**: Correct dimension | ✓ Technical: Architecture coupling → deployment fail | ✗ Budget overrun as technical (→ Financial)

## VI. Output Format (Minimal)

### A. TOC
1. Executive Summary (Top risks + priorities) | 2. Taxonomy (3-4×4-5 matrix) | 3. Register | 4. Roadmap | 5. References | 6. Validation | 7. Appendices (Heat map, RACI)

### B. Taxonomy Overview (Minimal)
**Total**: [6–12] | **Severity**: Crit [X] ([Y]%) / High [X] ([Y]%) / Med [X] ([Y]%) / Low [X] ([Y]%) | **Coverage**: 3-4 dimensions × 4-5 phases

| # | Dimension | Count | Mix (C/H/M/L) | Artifacts |
|---|-----------|-------|---------------|-----------|
| 1 | Technical | 2–4 | 1C/1-2H/1M/0L | Matrix + Threat model |
| 2 | Regulatory/Legal | 1–3 | 0-1C/1H/1-2M/0L | Matrix + Compliance |
| 3 | Business/Market | 1–3 | 0-1C/1H/1-2M/0L | Matrix + Competitive |
| 4 | Financial | 1–2 | 0C/0-1H/1M/0L | Matrix + Cost (if material) |
| | **Total** | **6–12** | **1-2C/3-5H/3-5M/0L** | **3-4 matrices + 1 roadmap + heat map** |

Legend: C=Critical (≥20) | H=High (15–19) | M=Medium (10–14) | L=Low (5–9)

### C. Phase Distribution (Minimal)

| Phase | Tech | Reg | Biz | Fin | **Total** | **Top** |
|-------|------|-----|-----|-----|-----------|---------|
| 1. Requirements & Discovery | 1 | 1 | 1 | 0 | **3** | 18-20 (H-C) |
| 2. Architecture & Design | 1 | 0-1 | 0-1 | 0 | **1-3** | 16-18 (H) |
| 3. Development & Testing | 1 | 0 | 0-1 | 0 | **1-2** | 12-16 (M-H) |
| 4. Deployment & Operations | 1 | 0-1 | 0 | 0-1 | **1-3** | 15-20 (H-C) |
| 5. Evolution & Governance | 0 | 0 | 0 | 0 | **0-1** | 12 (M) |
| **Total** | **2-4** | **1-3** | **1-3** | **1-2** | **6–12** | - |

### D. Risk Entry Format (Minimal)

**Dimension**: [Technical/Regulatory/Business/Financial]

**RISK-[ID]: [Dimension]-[Phase]-[SpecificRisk]**

**Statement**: [Event + consequence, 1–2 sentences]

**Phase**: [Requirements & Discovery/Architecture & Design/Development & Testing/Deployment & Operations/Evolution & Governance]

**Decision Criticality**: [Criterion: Blocks/Risk/Stakeholders/Evolving/Adoption]

**Probability** (1–5): [Score] | [Justification with data] [Ref: F#/C#]

**Impact** (1–5): [Score] | Financial: [$X], Time: [X wks], Reputation: [churn, SLA, penalty]

**Score**: [P × I] | Severity: [Critical/High/Medium/Low]

**Stakeholders**:
- **Owner**: [Role with authority]
- **Affected**: [≥2 teams]
- **Escalation**: [Conditions → Role]

**Root Causes**: [Tech/process/org] [Ref: G#/C#]

**Triggers**: 
- **Leading**: [Metrics]
- **Monitoring**: [Tools, alerts] [Ref: T#]

**Dependencies**: [Related risks] | Cross-refs: [IDs]

**Mitigation**:

1. **Prevent** (reduce P):
   - Actions: [Steps]
   - Owner: [Role]
   - Timeline: [Duration]
   - Cost: [$X]
   - Tools: [Ref: T#]

2. **Detect**:
   - Monitoring: [Dashboards, thresholds]
   - Tools: [Ref: T#]
   - SLA: [Target]

3. **Correct**:
   - Actions: [Rollback, DR, failover]
   - Owner: [Role]
   - RTO/RPO: [Targets]
   - Runbook: [Link]
   - Tools: [Ref: T#]

**Residual**:
- Post-P: [Score]
- Post-I: [Score]
- Residual: [P × I]
- Acceptance: [Rationale or escalation]

**Metrics**: [KPIs]

**Citations**: [Ref: C#, ...] (≥1 Crit/High, ≥1 Med/Low)

**Artifact** *(Crit/High)*: [Matrix, roadmap, or runbook]

---

**Example**:

**RISK-T-DEV-01: Technical-Development-UntestedDatabaseMigration**

**Statement**: DB schema migration without staging testing causes data inconsistency, app errors, 4–8hr downtime requiring rollback.

**Phase**: Development

**Probability** (1–5): 4 | 60% orgs experience migration incidents in microservices (DORA 2023); team lacks automated testing [Ref: C15]

**Impact** (1–5): 4 | Financial: $800K (labor $200K + revenue $500K/hr × 4hr + churn $100K), Time: 8wk recovery, Reputation: SLA breach (99.9%→99.5%), 3 enterprise escalations

**Score**: 16 | Severity: High

**Stakeholders**:
- **Owner**: DevOps Lead (staging authority, pipeline, $50K budget)
- **Affected**: Backend, QA, SRE, CS
- **Escalation**: RTO >2hr or revenue-impacting → CTO; SLA breach → CEO + customers

**Root Causes**: [Ref: G8-Tech Debt] Insufficient test coverage; no schema versioning; staging-prod drift; manual deployment

**Triggers**:
- **Leading**: Rising CI failures; schema complexity +20%/qtr; config drift
- **Monitoring**: Schema dashboard (Grafana) [Ref: T5]; error >1% sustained 5min [Ref: T6]; pool exhaustion

**Dependencies**: Cross-refs: RISK-T-DEP-02 (rollback failure amplifies), RISK-B-OPS-01 (churn accelerates in peak)

**Mitigation**:

1. **Prevent** (→ P=2):
   - Actions: (1) Liquibase/Flyway [Ref: T3]; (2) CI test with prod-like volume (10K+ rows); (3) staging parity (weekly drift); (4) peer review
   - Owner: DevOps Lead (impl) + Backend Lead (review)
   - Timeline: 6wk (2wk setup + 2wk harness + 2wk rollout)
   - Cost: $25K (Liquibase $15K/yr + 80hrs $10K)
   - Tools: [Ref: T3-Liquibase, T4-Testcontainers]

2. **Detect** (5min SLA):
   - Monitoring: Health dashboard (pre-checks, progress, post-validation) [Ref: T5]; alert error >0.5% or p95 >500ms (baseline 200ms)
   - Tools: [Ref: T5-Grafana, T6-Prometheus]
   - SLA: Alert 2min; incident 5min

3. **Correct** (RTO 1hr):
   - Actions: (1) Auto-rollback (DB restore from snapshot + app revert); (2) hotfix (expedited review + canary); (3) comms template
   - Owner: SRE on-call (exec) + DevOps Lead (hotfix approval)
   - RTO/RPO: 1hr RTO (30min detect + 30min rollback), 15min RPO (log shipping)
   - Runbook: [/runbooks/db-migration-incident.md]
   - Tools: [Ref: T7-PagerDuty, T8-Backup]

**Residual**:
- Post-P: 2 (Unlikely, 10–25%)
- Post-I: 3 (Moderate, $200K + 2wk)
- Residual: 6 (Low)
- Acceptance: Within appetite (<10); blue-green DB cost-prohibitive ($200K+ infra) for current scale; revisit at 100K+ users

**Metrics**: Zero migration incidents 12mo; 100% pass staging; cycle time <3 days (PR→prod)

**Citations**: 
- [Ref: C15] Forsgren, N., et al. (2023). *DORA State of DevOps*. Google Cloud. [EN]
- [Ref: C16] Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly. Ch. 4. [EN]
- [Ref: C17] Richardson, C. (2018). *Microservices Patterns*. Manning. [EN]

**Artifact**: 
- Matrix: P=4, I=4 (red zone)
- Timeline: [Gantt: 6wk preventive + milestones]
- Runbook: [Flow: detect → diagnose → rollback → validate → comms]

### E. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition (scale/formula) | Usage | Related | Limits | Alphabetical

**Frameworks**: **F#. Name** | Purpose | Components | Application | Limits | Source

**Tools**: **T#. Tool (Category)** | Desc | Features | Pricing | Integrations (≥3) | Compliance | Update (Q# YYYY) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (concepts, frameworks) | Applicability (industry, phase, dimension) | Relevance | Group by language

**Citations**: **C#. [Citation] [Lang]** | APA 7th

## VII. Template (Minimal)

```markdown
# Enterprise Risk Assessment: [Project/System]

**Date**: [YYYY-MM-DD]  
**Scope**: [System, e.g., "Payment microservices"]  
**Team**: [Size, structure]  
**Context**: [Budget, timeline, regulatory]

---

## Executive Summary

### Top Risks (6-12)

| Rank | ID | Name | Score | Dimension | Phase | Owner | Priority |
|------|----|------|-------|-----------|-------|-------|----------|
| 1 | RISK-T-REQ-01 | [Risk name] | 20 (C) | Technical | Requirements | [Role] | Immediate |
| 2 | RISK-R-REQ-01 | [Risk name] | 18 (H) | Regulatory | Requirements | [Role] | High |
| ... | ... | ... | ... | ... | ... | ... | ... |

### Mitigation Priorities

**Immediate (Wk 1-4)**: [Critical risks]  
**High (Mo 2-3)**: [High-severity risks]  
**Strategic (Q2-4)**: [Med systemic risks]

---

## Taxonomy

[3-4×4-5 matrix: dimension × phase with counts + heat map]

---

## Register

### Technical Risks (2-4)

**RISK-T-[ID]: [Dimension]-[Phase]-[SpecificRisk]**

[Full entry per Section VI.D]

---

[Continue for all 6-12 risks by dimension]

---

## References

### Glossary (≥10)

**G1. Risk Score** | P × I (1–25) | Risk prioritization | Related: P, I, Severity

[≥10 terms]

### Frameworks (≥5)

**F1. ISO 31000:2018** | Enterprise risk mgmt | Principles, framework, process | Apply across phases

[≥5 frameworks]

### Tools (≥5)

[≥5 with specs]

### Literature (≥6)

[≥6 with ≥2 risk mgmt]

### Citations (≥10)

[≥10 APA 7th + tags]

---

## Validation

[Completed 12-validation table from Section IV]

---

## Appendices

### A. Risk Matrices

[3-4 matrices, 1 per dimension]

### B. Heat Map

[4-5 phases × 3-4 dimensions, color-coded]

### C. Roadmap

[Gantt: prevent/detect/correct with owners, timelines]

### D. RACI

[Risk ownership across roles]

```

---

## VIII. Submission Checklist (Minimal)

✅ 12 validations PASS  
✅ Executive summary: top risks  
✅ Taxonomy complete (3-4×4-5)  
✅ 6-12 risks with 15 components  
✅ Crit/High have artifacts  
✅ All have owner + escalation  
✅ High-severity have 3-tier mitigation  
✅ Roadmap with timeline + costs  
✅ References: G≥10, F≥5, T≥5, L≥6, C≥10  
✅ Citations: APA 7th + tags  
✅ Heat map + RACI  
✅ No placeholders  
✅ Consistent format  
✅ Balanced coverage (3-4 dimensions × 4-5 phases)  
✅ Decision Criticality 100% justified  
✅ Reviewed by ≥3 stakeholder roles
