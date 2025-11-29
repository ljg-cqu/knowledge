# Two-Tier Problem Classification System

**Last Updated**: 2025-11-29  
**Status**: Final v1.0  
**Owner**: Documentation Team

## Overview

Two-tier classification: ONE root cause (Tier 1) + MULTIPLE impacts (Tier 2) + Pareto scoring (1-300).

**Key Concepts**: MECE (Mutually Exclusive, Collectively Exhaustive), Pareto Principle (80/20).

### Context

**Problem**: Organizations struggle to prioritize across technical, regulatory, economic, operational dimensions. Single-tier systems lose multi-dimensional context.

**Audience**: Product managers, engineering leaders, operations directors, executives.

**Prerequisites**: ≥6mo historical data, cross-functional participation, tracking infrastructure. ≥20 problems, stable context, finite resources.

**Timeline**: Mo 1-3 (pilot, 70% agreement) → Mo 4-6 (rollout, 85%) → Mo 7-12 (optimization, 90%) → Year 2+ (20-30% improvement).

**Resources**: 2-4 hrs/problem initially (→30-60 min); quarterly updates (1-2 days); annual review (1 week).

**Quick Start**: [CRITICAL] sections (15-20 min) → [Important] (+30-45 min) → [Optional] as needed.

**⚠️ Data Quality**: Examples are illustrative estimates. Verify before decisions; replace with org data. See [Data Quality](#data-quality-and-citations).

---

## Table of Contents

**[CRITICAL]** = Essential (15-20 min) | **[Important]** = Recommended (30-45 min) | **[Optional]** = Reference

1. **[Overview](#overview)** — **[CRITICAL]** — Key Concepts | System Purpose | Context
2. **[Tier 1: Root Cause Categories](#tier-1-primary-root-cause-categories-mece-optimized)** — **[CRITICAL]**
3. **[Tier 2: Impact Dimensions](#tier-2-impact-dimensions-multi-tag-system)** — **[Important]**
4. **[Problem Severity](#problem-severity-classification)** — **[CRITICAL]**
5. **[80/20 Pareto Framework](#8020-pareto-prioritization-framework)** — **[Important]**
6. **[Usage Guidelines](#usage-guidelines)** — **[CRITICAL]** — Decision Tree | Step-by-Step
7. **[Problem Metadata Template](#problem-metadata-template)** — **[Important]**
8. **[MECE Validation](#validation-against-mece-principles)** — **[Optional]**
9. **[Applicability and Limitations](#applicability-and-limitations)** — **[Important]**
10. **[Comparison with Alternatives](#comparison-with-alternative-approaches)** — **[Optional]**
11. **[Success Criteria](#success-criteria-and-measurement)** — **[Important]**
12. **[Data Quality](#data-quality-and-citations)** — **[Important]**
13. **[QA Checklist](#quality-assurance-checklist)** — **[CRITICAL]**

---

## Tier 1: Primary Root Cause Categories (MECE-Optimized)

**Principle**: Identify the **primary driver**—what fundamentally creates this problem? If removed, the problem would be eliminated.

### 1. External Threat (Adversarial/Environmental)

Adversaries, natural disasters, or external disruptions beyond organizational control.

**Sub-categories**: Malicious Actors | Social Engineering | Insider Threats | Natural/Geopolitical

**Examples**: Ransomware, supply chain disruptions, DDoS, payment fraud

---

### 2. Technical/Architectural Constraint

Fundamental technical, physical, or mathematical limitations requiring paradigm shift.

**Sub-categories**: Performance Limits | Scalability Boundaries | Compatibility | Physical/Mathematical Limits

**Examples**: O(n²) complexity, MRI scan time (physics), CNC precision limits, last-mile delivery

---

### 3. Regulatory/Legal Mandate

Compliance, licensing, or jurisdictional requirements with non-compliance consequences.

**Sub-categories**: Compliance | Licensing & Classification | Tax & Financial | Privacy & Data Protection | Jurisdictional Fragmentation

**Examples**: HIPAA implementation, KYC/AML (15-30% abandonment), GDPR deletion

---

### 4. Design/Standards Gap (Ecosystem Immaturity)

Lack of standards, protocol fragmentation, or immature tooling/practices.

**Sub-categories**: Protocol Fragmentation | Integration Complexity | Tooling Gaps | Knowledge/Documentation Deficits

**Examples**: Microservices observability (100+ tools), EHR interoperability, IoT protocols (50+)

---

### 5. Human/Organizational Factor

Coordination failures, behavioral errors, organizational conflicts, or governance disputes.

**Sub-categories**: Multi-Party Coordination | Human Error | Organizational Conflict | Knowledge/Training Gaps

**Examples**: Deployment errors (70% of outages), medical errors, approval bottlenecks (6-18mo)

---

### 6. Economic/Market Constraint

Cost-viability tradeoffs, market structure gaps, or economic accessibility barriers.

**Sub-categories**: Cost-Benefit Misalignment | Market Structure Gaps | Economic Accessibility | Operational Economics

**Examples**: MRI affordability (rural hospitals), SMB security costs, tutoring pricing, automation ROI

---

## Tier 2: Impact Dimensions (Multi-Tag System)

Tag all applicable dimensions (typically 3-5/problem).

**🔒 Security & Risk**: Vulnerabilities, breaches, safety incidents | *Indicators*: Dollar losses, incident frequency, breach rates

**📋 Regulatory & Legal**: Compliance burden, legal risk, penalties | *Indicators*: Fines, compliance costs, audit requirements

**⚙️ Operational Efficiency**: Process overhead, coordination burden, reliability | *Indicators*: Process time, staff hours, error rates, downtime

**👥 User Experience**: Usability barriers, abandonment, satisfaction | *Indicators*: Completion rates, abandonment %, NPS, support tickets

**💰 Economic & Cost**: Financial burden, cost-benefit viability, accessibility | *Indicators*: Implementation costs, operational expenses, ROI

**⚡ Technical Performance**: Speed, throughput, latency, scalability | *Indicators*: Response time, req/sec, processing delays

**🤝 Trust & Reputation**: Market confidence, brand credibility | *Indicators*: NPS, customer churn, brand sentiment

---

## Problem Severity Classification

**[CRITICAL]**: Existential threats, catastrophic failures, regulatory violations, irreversible harm (>$10M, regulatory action, fatalities)

**[Important]**: Significant barriers, competitive disadvantages, inefficiencies (market erosion, attrition, >$1M annual)

**[Moderate]**: Incremental improvements, optimizations, edge cases (<$1M annual)

---

## 80/20 Pareto Prioritization Framework

Data-driven prioritization using three-axis scoring to identify "vital few" (20% causing 80% impact).

**Formula**: `Priority Score = Impact (1-10) × Frequency (1-10) × Criticality (1.0-3.0)` → Range: 1-300

### Axis 1: Impact Magnitude

| Score | Range | Examples |
|-------|-------|----------|
| **10** | Catastrophic ($1B+, 10M+ stakeholders) | Major outages, system failures |
| **8** | Severe ($100M-$1B, 1M-10M) | Fraud losses, institutional burdens |
| **6** | Significant ($10M-$100M, 100K-1M) | Compliance costs, major integrations |
| **4** | Moderate ($1M-$10M, 10K-100K) | Technology implementations |
| **2** | Minor ($100K-$1M, 1K-10K) | Process improvements, tooling |
| **1** | Minimal (<$100K, <1K) | Small optimizations |

### Axis 2: Frequency

| Score | Frequency | Examples |
|-------|-----------|----------|
| **10** | Constant (daily) | Production incidents, fraud |
| **8** | Very Frequent (weekly) | Approvals, deployments |
| **6** | Frequent (monthly) | Compliance, maintenance |
| **4** | Periodic (quarterly/annual) | Audits, renewals |
| **2** | Occasional (multi-year) | Governance disputes |
| **1** | Rare (5+ years) | Black swans |

**Note**: At ecosystem scale, 1,000 orgs × "rare" (2) → "frequent" (6)

### Axis 3: Criticality Weight

| Severity | Weight | Rationale |
|----------|--------|-----------|
| **[CRITICAL]** | **3.0×** | Existential threats, irreversible harm, life-safety |
| **[Important]** | **2.0×** | Competitive differentiation, market barriers |
| **[Moderate]** | **1.0×** | Incremental improvements, optimizations |

### Example Calculations

| Problem | I | F | C | Score | Tier |
|---------|---|---|---|-------|------|
| **Security Breaches** | 8 | 10 | 3.0 | **240** | S |
| **Medical Diagnosis Delays** | 8 | 6 | 3.0 | **144** | S |
| **Deployment Errors** | 6 | 10 | 2.0 | **120** | S |
| **Supply Chain Fragmentation** | 4 | 8 | 2.0 | **64** | A |
| **Approval Deadlocks** | 8 | 2 | 3.0 | **48** | A |

### Resource Allocation Tiers

| Tier | Score | % Problems | Budget | Action |
|------|-------|------------|--------|--------|
| **S (Vital Few)** | ≥100 | ~20% | **60-70%** | Immediate investment, continuous monitoring |
| **A (Important Many)** | 50-99 | ~30% | **20-30%** | Scheduled improvements, automation |
| **B (Useful Minority)** | 20-49 | ~30% | **10-20%** | Incremental optimizations, defer unless strategic |
| **C (Trivial Many)** | <20 | ~20% | **<10%** | Monitor only, opportunistic fixes |

**ROI**: Tier S captures ~75-80% impact with 60-70% budget → 30-50% improvement Year 1

---

## Usage Guidelines

### Classification Decision Tree

```
What fundamentally creates this problem?
├─ Adversaries/external forces? ───────► [1] External Threat
├─ Technical/physical limitation? ─────► [2] Technical/Architectural Constraint
├─ Required by law/regulation? ────────► [3] Regulatory/Legal Mandate
├─ Ecosystem lacks standards/tooling? ─► [4] Design/Standards Gap
├─ Human coordination/error? ──────────► [5] Human/Organizational Factor
└─ Economically unviable? ─────────────► [6] Economic/Market Constraint

THEN: Apply Tier 2 impact tags → Assign severity → Calculate priority score
```

### Step-by-Step Process

**Step 1: Tier 1 Root Cause** — Choose most upstream cause  
*Example*: Database slow query → O(n²) complexity → **2. Technical/Architectural > Performance Limits**

**Step 2: Tier 2 Impact Tags** — Apply 3-5 tags  
*Example*: ⚡ Performance | 👥 UX | 💰 Economic | 🤝 Reputation

**Step 3: Severity** — Critical/Important/Moderate?  
*Example*: Competitive disadvantage + $50K/mo → **[Important]**

**Step 4: Priority Score** — `Impact × Frequency × Criticality`  
*Example*: 4 × 10 × 2.0 = **80** → **Tier A**

**Result**:
```markdown
- **Tier 1**: 2. Technical/Architectural > Performance Limits
- **Tier 2**: ⚡ Performance, 👥 UX, 💰 Economic, 🤝 Reputation
- **Severity**: [Important] | **Score**: 80 → A (4×10×2.0)
```

---

## Problem Metadata Template

```markdown
---
**Tier 1**: [Category] > [Sub-category]
**Tier 2**: [Tag 1], [Tag 2], [Tag 3]
**Severity**: [CRITICAL | Important | Moderate] | **Score**: [1-300] → [S|A|B|C] (I×F×C)
**Source**: [Source] | [✅ Verified | ⚠️ Estimated] | Updated: YYYY-MM-DD
---
```

**Example**:
```markdown
---
**Tier 1**: 5. Human/Organizational > 5.2 Human Error
**Tier 2**: 🔒 Security, ⚙️ Operational, 💰 Economic, 🤝 Reputation
**Severity**: [CRITICAL] | **Score**: 120 → S (6×10×2.0)
**Source**: Postmortem DB (2024) | ⚠️ Estimated | Updated: 2025-11-29
---
```

---

## Validation Against MECE Principles

**Mutually Exclusive**: Ransomware → External Threat | HIPAA → Regulatory | Automation Gaps → Design Gap | Approval Deadlocks → Human/Org | Query Latency → Technical

**Collectively Exhaustive**: AI bias → Design Gap OR Human Factor | Climate impacts → External Threat | Skills shortage → Human/Organizational

**Rule**: Choose upstream causes over downstream impacts. Use primary driver test if ambiguous.

---

## Comparison with Alternative Approaches

| Approach | MECE | Multi-Dim | Quant Priority | Solution Guidance | Complexity | Best For |
|----------|------|-----------|----------------|-------------------|------------|----------|
| **Two-Tier** | ✅ | ✅ | ✅ | ✅ | High | Multi-stakeholder, >20 problems, resource allocation |
| **Severity-Only** | ❌ | ❌ | ⚠️ | ❌ | Low | Incident triage, <20 problems |
| **Domain-Specific** | ✅ | ⚠️ | ❌ | ✅ | Medium | Single-domain, compliance-driven |
| **Impact-Only** | ❌ | ✅ | ⚠️ | ❌ | Medium | Stakeholder communication, risk registers |
| **Cause-Only** | ✅ | ❌ | ⚠️ | ✅ | Low | Engineering-focused, single-stakeholder |

**Hybrid**: Large Enterprise (Two-Tier + Domain-Specific) | Startup (Severity-Only → Two-Tier @>20 problems) | Incident Response (Severity-Only + Two-Tier retrospective)

---

## Applicability and Limitations

**✅ Use**: Multi-stakeholder/multi-domain | Resource allocation | Root cause analysis | Quantifiable data (≥6mo)

**❌ Avoid**: Simple/single-dimension | Novel/unprecedented | Real-time incident response | Strategic/philosophical decisions

**Assumptions**: Root causes identifiable | Problems stable | Impact measurable | Resources finite | Pareto applies (validate)

**Dependencies**: Incident tracking, financial reporting, operational metrics | Cross-functional agreement | Deep problem understanding

### Risks and Mitigation

| Risk | Mitigation |
|------|------------|
| **Classification Ambiguity** (10-15%) | Primary driver test; document secondary causes; quarterly review |
| **Data Quality (GIGO)** | Require sources; flag estimates; quarterly updates |
| **Quantification Bias** | Supplement with stakeholder voting; qualitative assessment |
| **Domain Calibration** | Calibrate during pilot; adjust by context |
| **Over-Reliance** | Combine with feasibility; consider strategic importance |
| **Gaming** | Require verification; external review (Tier S); audit |

---

## Success Criteria and Measurement

### Primary Metrics

| Metric | Baseline | Year 1 | Year 2 | Measurement |
|--------|----------|--------|--------|-------------|
| **Resolution Rate** | 40-60% | +10-15% | +20-30% | (Resolved / Addressed) × 100% |
| **ROI Efficiency** | $2-4/$1 | +30-50% | +50-100% | Impact Reduced / Resources Invested |
| **Agreement** | N/A | Mo 1-3: ≥70%, Mo 4-6: ≥85% | ≥90% | (Matching / Total) × 100% (3 classifiers, 20 problems) |
| **Predictive Accuracy** | N/A | S: ≥75% high, C: ≤20% high | Same | 6mo outcomes, 20/tier |
| **Time-to-Solution** | 3-12mo | -20-30% | -30-50% | Date(Deployed) - Date(Identified) |

### Secondary Indicators

| Indicator | Target | Warning |
|-----------|--------|---------|
| **Satisfaction** (1-5) | ≥4.0 (understanding), ≥3.5 (trust) | <3.0 @6mo → overhead high |
| **Coverage** | ≥95% in 2 weeks | <80% → rules complex |
| **Data Quality** | Yr 1: 60-70%, Steady: ≥80% | Quarterly audit 50 problems |

### Milestones

| Phase | Timeline | Success | Threshold |
|-------|----------|---------|-----------|
| **Pilot** | Mo 1-3 | 20 problems, ≥70%, training | <60% → Refine |
| **Rollout** | Mo 4-6 | 80% coverage, ≥85% | <3.0 satisfaction → Simplify |
| **Optimization** | Mo 7-12 | ≥95% coverage, ≥90% | <10% ROI → Recalibrate |
| **Steady** | Yr 2+ | ≥80% quality, 20-30% resolution, 30-50% ROI | Not met → Revise |

### Failure Modes

| Symptom | Action |
|---------|--------|
| **Deadlock** (>10% unclassified) | Refine Tier 1, add sub-category |
| **Gaming** | Require verification, external audit (S) |
| **Inversion** (C > S impact) | Recalibrate scales |
| **Revolt** (bypass) | Simplify to Severity-Only 3mo |
| **No Impact** (ROI <5% @12mo) | Analyze decision influence |

### Continuous Improvement

**Quarterly**: Recalc scores, adjust tiers | Metrics dashboard | Disputes → refine tree | Predicted vs. actual (>20% mismatch → adjust)

**Annually**: Validate MECE | Assess Pareto (20% → 80%?) | Compare ROI to alternatives | Update targets

**Tracking**: Disagreements → refine tree | Edge cases → new sub-categories | Tier S outcomes → validate 80/20

---

## Data Quality and Citations

**⚠️ Notice**: Illustrative estimates flagged with [^footnotes]. Before decisions: verify, replace with org data, cite sources.

### Data Quality Tiers

| Tier | Use | Requirements |
|------|-----|--------------|
| **Verified** | Tier S | Internal logs/financials <12mo, traceable, ≥2 sources |
| **Substantiated** | Tier A/B | Industry reports, named sources, flagged "estimated" |
| **Order-of-Magnitude** | Tier C | Explain method, flag "rough" |

**Citation**: `Impact: $2.3M | Source: [Report, Dept, Date] | Status: ✅ Verified | Updated: YYYY-MM-DD`

### References

**Classification**: Ishikawa (1990), Reason (2000) BMJ 320:768, Perrow (1999)  
**Pareto**: Koch (2011), Juran (1954) Mgmt Review 43:748  
**MECE**: Minto (2009)  
**Analysis**: Ritchey (2011), Checkland (1999)  
**Risk**: Hubbard (2009), ISO 31000:2018

---

## Quality Assurance Checklist

☐ **Context**: Problem, stakeholders, constraints, scale  
☐ **Data**: Impact/frequency verified (≥6mo), sources, estimates flagged  
☐ **Classification**: Tier 1 + Tier 2 (3-5 tags) + Severity + Score  
☐ **Actionability**: Success criteria, alternatives, trade-offs  
☐ **Review**: ≥2 stakeholders, quarterly schedule, ≥80% quality (Tier S)

**System Health** — Quarterly: Recalc scores | Verify 20%→80% | ≥90% agreement | Annual: Validate MECE | Resolution (+20-30%), ROI (+30-50%), Satisfaction (≥4.0)

---

**End of Document**
