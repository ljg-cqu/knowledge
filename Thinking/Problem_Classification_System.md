# Two-Tier Problem Classification System

**Last Updated**: 2025-11-29  
**Status**: Final v1.0  
**Owner**: Documentation Team

## Overview

**📋 Navigation**: See [Table of Contents](#table-of-contents) for priority indicators (Critical/Important/Optional).

### Key Concepts

**MECE** (Mutually Exclusive, Collectively Exhaustive): Categories don't overlap and cover all possibilities.  
**Pareto Principle (80/20)**: ~80% of effects come from ~20% of causes; used for quantitative prioritization.

### System Purpose

Two-tier classification for multi-dimensional problems:
- **Tier 1**: Single root cause (near-MECE)
- **Tier 2**: Multiple impact dimensions (multi-tag)
- **Pareto Scoring**: 1-300 scale prioritization

**Core Insight**: Problems have ONE root cause but MULTIPLE impacts.

**Example**: Database outage → Root: Technical/Architectural + Impacts: Performance, UX, Economic, Reputation

### Context

**Problem**: Organizations struggle to prioritize problems across technical, regulatory, economic, and operational dimensions. Single-tier systems lose multi-dimensional context.

**Audience**: Product managers, engineering leaders, operations directors, executives.

**Prerequisites**: ≥6mo historical data (incidents, costs, frequency), cross-functional participation, tracking infrastructure.

**Timeline**: Mo 1-3 (pilot, 70% agreement) → Mo 4-6 (rollout, 85%) → Mo 7-12 (optimization, 90%) → Year 2+ (20-30% improvement).

**Resources**: 2-4 hrs/problem initially (→30-60 min); 3-person team; quarterly updates (1-2 days); annual review (1 week).

**Constraints**: ≥20 problems; stable problems; finite resources; Pareto may not apply—validate with data.

**Quick Start**: [CRITICAL] sections (15-20 min) → [Important] sections (+30-45 min) → [Optional] as needed.

### ⚠️ Data Quality Notice

Quantitative examples (dollar amounts, percentages) are **illustrative estimates** flagged with **[^footnote]** markers. Before critical decisions: verify claims, replace with organization-specific data, cite primary sources, flag estimates explicitly. See [Data Quality and Citations](#data-quality-and-citations).

---

## Table of Contents

**[CRITICAL]** = Essential (15-20 min) | **[Important]** = Recommended (30-45 min) | **[Optional]** = Reference

1. **[Overview](#overview)** — **[CRITICAL]**
   - [Key Concepts](#key-concepts) | [System Purpose](#system-purpose) | [Context](#context)
2. **[Tier 1: Primary Root Cause Categories](#tier-1-primary-root-cause-categories-mece-optimized)** — **[CRITICAL]**
   - External Threat | Technical Constraint | Regulatory Mandate | Design/Standards Gap | Human/Organizational | Economic/Market
3. **[Tier 2: Impact Dimensions](#tier-2-impact-dimensions-multi-tag-system)** — **[Important]**
   - Security | Regulatory | Operational | UX | Economic | Performance | Trust/Reputation
4. **[Problem Severity](#problem-severity-classification)** — **[CRITICAL]**
5. **[80/20 Pareto Framework](#8020-pareto-prioritization-framework)** — **[Important]**
   - Impact Magnitude (1-10) | Frequency (1-10) | Criticality Weight (1-3×) | Resource Allocation Tiers (S/A/B/C)
6. **[Usage Guidelines](#usage-guidelines)** — **[CRITICAL]**
   - Decision Tree | Step-by-Step Process
7. **[Problem Metadata Template](#problem-metadata-template)** — **[Important]**
8. **[Validation Against MECE](#validation-against-mece-principles)** — **[Optional]**
9. **[Applicability and Limitations](#applicability-and-limitations)** — **[Important]**
10. **[Comparison with Alternatives](#comparison-with-alternative-approaches)** — **[Optional]**
11. **[Success Criteria](#success-criteria-and-measurement)** — **[Important]**
12. **[Maintenance](#maintenance-and-evolution)** — **[Optional]**
13. **[Data Quality](#data-quality-and-citations)** — **[Important]**
14. **[QA Checklist](#quality-assurance-checklist)** — **[CRITICAL]**

---

## Tier 1: Primary Root Cause Categories (MECE-Optimized)

**Principle**: Identify the **primary driver**—what fundamentally creates this problem? If removed, the problem would be eliminated.

### 1. External Threat (Adversarial/Environmental)

**Definition**: Adversaries, natural disasters, or external disruptions beyond organizational control.

**Sub-categories**: Malicious Actors | Social Engineering | Insider Threats | Natural/Geopolitical

**Examples**: Ransomware, supply chain disruptions, payment fraud ($485B annual [^1]), DDoS

**Traits**: Ceases if adversaries/shocks absent; requires defense/resilience; mitigation only

---

### 2. Technical/Architectural Constraint

**Definition**: Fundamental technical, physical, or mathematical limitations requiring paradigm shift.

**Sub-categories**: Performance Limits | Scalability Boundaries | Compatibility | Physical/Mathematical Limits

**Examples**: O(n²) complexity, MRI scan time (physics), CNC precision (vibration), last-mile delivery

**Traits**: Not "fixable" by process; requires technological breakthrough; hard constraints

---

### 3. Regulatory/Legal Mandate

**Definition**: Compliance, licensing, or jurisdictional requirements with non-compliance consequences.

**Sub-categories**: Compliance | Licensing & Classification | Tax & Financial | Privacy & Data Protection | Jurisdictional Fragmentation

**Examples**: HIPAA ($1.5M implementation [^2]), KYC/AML (15-30% abandonment, $5.1B fines [^3]), GDPR deletion

**Traits**: Disappears if regulation changes; legal-driven; non-negotiable

---

### 4. Design/Standards Gap (Ecosystem Immaturity)

**Definition**: Lack of standards, protocol fragmentation, or immature tooling/practices.

**Sub-categories**: Protocol Fragmentation | Integration Complexity | Tooling Gaps | Knowledge/Documentation Deficits

**Examples**: Microservices observability (100+ tools, $300K-$1M [^4]), EHR interoperability (FHIR <40% [^5]), IoT (50+ protocols)

**Traits**: Solvable via standardization; improves with ecosystem maturity; multi-stakeholder collaboration

---

### 5. Human/Organizational Factor

**Definition**: Coordination failures, behavioral errors, organizational conflicts, or governance disputes.

**Sub-categories**: Multi-Party Coordination | Human Error | Organizational Conflict | Knowledge/Training Gaps

**Examples**: Deployment errors (70% outages, $100K-$500K [^6]), medical errors (250K deaths/yr US [^7]), approval bottlenecks (6-18mo)

**Traits**: Technology alone insufficient; requires governance/training; high variance

---

### 6. Economic/Market Constraint

**Definition**: Cost-viability tradeoffs, market structure gaps, or economic accessibility barriers.

**Sub-categories**: Cost-Benefit Misalignment | Market Structure Gaps | Economic Accessibility | Operational Economics

**Examples**: MRI unaffordable (rural hospitals: $500K vs $100K budget), SMB security costs, tutoring ($50-100/hr), automation ROI

**Traits**: Technically feasible but economically prohibitive; improves with scale/maturity; may need new models

[^1]: Global aggregate estimate; verification needed  
[^2]: Industry estimate; verification needed  
[^3]: Survey-based; verification needed  
[^4]: Integration cost from surveys; high variance  
[^5]: Industry estimate; verification needed  
[^6]: Postmortem data; cost varies by size  
[^7]: Widely cited; methodology debated; verification needed

---

## Tier 2: Impact Dimensions (Multi-Tag System)

**Purpose**: Tag ALL applicable dimensions (typically 3-5/problem).

### 🔒 Security & Risk
**Scope**: Vulnerability to loss, breach, safety incidents, catastrophic failure  
**Indicators**: Dollar losses, incident frequency, breach rates

### 📋 Regulatory & Legal Compliance
**Scope**: Legal risk, compliance burden, non-compliance penalties  
**Indicators**: Fines, compliance costs, audit requirements

### ⚙️ Operational Efficiency
**Scope**: Process overhead, coordination burden, system reliability  
**Indicators**: Process time, staff hours, error rates, downtime

### 👥 User Experience & Adoption
**Scope**: Usability barriers, abandonment, satisfaction deficits  
**Indicators**: Completion rates, abandonment %, support tickets, NPS

### 💰 Economic & Cost
**Scope**: Financial burden, cost-benefit viability, pricing accessibility  
**Indicators**: Implementation costs, operational expenses, unit economics, ROI

### ⚡ Technical Performance
**Scope**: Speed, throughput, latency, scalability limitations  
**Indicators**: Response time, throughput (req/sec), processing delays

### 🤝 Trust & Reputation
**Scope**: Market confidence, brand credibility, stakeholder trust  
**Indicators**: NPS, customer churn, brand sentiment, incident frequency

---

## Problem Severity Classification

**[CRITICAL]**: Existential threats, catastrophic failures, regulatory violations, irreversible harm (business-ending, >$10M losses, regulatory action, fatalities)

**[Important]**: Significant barriers, competitive disadvantages, operational inefficiencies (market position erosion, customer attrition, >$1M annual cost)

**[Moderate]**: Incremental improvements, optimization opportunities, edge cases (efficiency gains, satisfaction improvements, <$1M annual value)

---

## 80/20 Pareto Prioritization Framework

**Purpose**: Data-driven prioritization using three-axis scoring to identify "vital few" (20% causing 80% impact).

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

**Sources**: Incident logs, financial systems

### Axis 2: Frequency

| Score | Frequency | Examples |
|-------|-----------|----------|
| **10** | Constant (daily) | Production incidents, fraud |
| **8** | Very Frequent (weekly) | Approvals, deployments |
| **6** | Frequent (monthly) | Compliance, maintenance |
| **4** | Periodic (quarterly/annual) | Audits, renewals |
| **2** | Occasional (multi-year) | Governance disputes |
| **1** | Rare (5+ years) | Black swans |

**Sources**: Incident logs, operational cycles  
**Aggregation**: 1,000 orgs × "rare" (2) → ecosystem "frequent" (6)

### Axis 3: Criticality Weight

| Severity | Weight | Rationale |
|----------|--------|-----------|
| **[CRITICAL]** | **3.0×** | Existential threats, irreversible harm, life-safety |
| **[Important]** | **2.0×** | Competitive differentiation, market barriers |
| **[Moderate]** | **1.0×** | Incremental improvements, optimizations |

### Example Calculations

| Problem | Impact | Freq | Crit | Score | Tier |
|---------|--------|------|------|-------|------|
| **Security Breaches** | 8 | 10 | 3.0 | **240** | S (Top 5%) |
| **Medical Diagnosis Delays** | 8 | 6 | 3.0 | **144** | S (Top 10%) |
| **Deployment Errors** | 6 | 10 | 2.0 | **120** | S (Top 10%) |
| **Supply Chain Fragmentation** | 4 | 8 | 2.0 | **64** | A (Top 20%) |
| **Approval Deadlocks** | 8 | 2 | 3.0 | **48** | A (Top 30%) |

### Resource Allocation Tiers

| Tier | Score | % Problems | Budget | Action |
|------|-------|------------|--------|--------|
| **S (Vital Few)** | ≥100 | ~20% | **60-70%** | Immediate investment, continuous monitoring |
| **A (Important Many)** | 50-99 | ~30% | **20-30%** | Scheduled improvements, automation |
| **B (Useful Minority)** | 20-49 | ~30% | **10-20%** | Incremental optimizations, defer unless strategic |
| **C (Trivial Many)** | <20 | ~20% | **<10%** | Monitor only, opportunistic fixes |

**ROI**: Tier S = ~75-80% impact; 60-70% allocation → 3-4× concentration vs. uniform; expect 30-50% improvement Year 1

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

**Step 1: Tier 1 Root Cause** — "What fundamentally creates this? If eliminated, problem disappears?"  
*Rule*: Choose most upstream cause.  
*Example*: Database slow query (5-10s) → O(n²) complexity → **2. Technical/Architectural > Performance Limits**

**Step 2: Tier 2 Impact Tags** — "Which dimensions affected?" (3-5 tags)  
*Example*: ✅ ⚡ Performance (5-10s) | 👥 UX (15% abandonment) | 💰 Economic ($600K/yr loss) | 🤝 Reputation (complaints)

**Step 3: Severity** — Critical (existential), Important (competitive), or Moderate (incremental)?  
*Example*: Competitive disadvantage + $50K/mo → **[Important]**

**Step 4: Priority Score** — `Impact (1-10) × Frequency (1-10) × Criticality (1-3×)`  
*Example*: 4 × 10 × 2.0 = **80** → **Tier A** → Schedule optimization

**Complete Classification**:
```markdown
- **Tier 1**: 2. Technical/Architectural > Performance Limits
- **Tier 2**: ⚡ Performance, 👥 UX, 💰 Economic, 🤝 Reputation
- **Severity**: [Important]
- **Score**: 80 → Tier A (Impact: 4, Freq: 10, Crit: 2.0×)
```

---

## Problem Metadata Template

```markdown
---
**Classification**:
- **Tier 1**: [Category] > [Sub-category]
- **Tier 2**: [Tag 1], [Tag 2], [Tag 3]
- **Severity**: [CRITICAL | Important | Moderate] | **Score**: [1-300] → [S|A|B|C] (I×F×C)

**Attributes**: [Domain] | [Stakeholders]

**Source**: [Source] | [✅ Verified | ⚠️ Estimated] | Updated: YYYY-MM-DD
---
```

**Example**:
```markdown
---
**Classification**:
- **Tier 1**: 5. Human/Organizational > 5.2 Human Error
- **Tier 2**: 🔒 Security, ⚙️ Operational, 💰 Economic, 🤝 Reputation
- **Severity**: [CRITICAL] | **Score**: 120 → S (6×10×2.0)

**Attributes**: Software | Engineering, Ops, Exec

**Source**: Postmortem DB (2024) | ⚠️ Estimated | Updated: 2025-11-29
---
```

---

## Validation Against MECE Principles

### Mutually Exclusive (Tier 1)

✅ Ransomware → External Threat (NOT Human—poor hygiene secondary)  
✅ HIPAA → Regulatory (NOT Operational—process is consequence)  
✅ Automation Gaps → Design Gap (NOT Operational—overhead symptom)  
✅ Approval Deadlocks → Human/Org (NOT Technical—systems work)  
✅ Query Latency → Technical (NOT Performance—that's impact)

**Result**: Functional mutual exclusivity via **upstream causes** vs. **downstream impacts**.  
**Ambiguous?** Use **primary driver test**: which elimination most directly solves problem?

### Collectively Exhaustive

✅ AI bias → Design Gap OR Human Factor  
✅ Climate impacts → External Threat  
✅ Skills shortage → Human/Organizational  
✅ Pandemic response → Human OR External Threat  
✅ Market monopoly → Economic/Market

**Result**: All problems map successfully. Category 4 catches ecosystem immaturity.

---

## Comparison with Alternative Approaches

| Approach | Pros | Cons | Best For |
|----------|------|------|----------|
| **Severity-Only** (Critical/High/Medium/Low) | Simple, fast, universal | No root cause, no solution guidance, single dimension | Incident triage, <20 problems |
| **Domain-Specific** (OWASP, ICD-10) | Deep expertise, standardized, tooling support | Not cross-domain, lacks prioritization, overly granular | Single-domain orgs, compliance-driven |
| **Impact-Only** (Security/Economic/etc.) | Multi-dimensional, stakeholder-aligned, easier consensus | No solution guidance, treats symptoms, no MECE | Stakeholder communication, risk registers |
| **Cause-Only** (Root cause without impacts) | MECE achievable, clear solution guidance, simple | Loses multi-dimensional context, harder prioritization | Engineering-focused, single-stakeholder |
| **Ad-Hoc Scoring** (Subjective judgment) | Flexible, context-specific, low overhead | Inconsistent, biased, not auditable, no learning | Small teams, rapidly changing environments |

**Trade-Off Summary**:

| Approach | MECE | Multi-Dim | Quantitative Priority | Cross-Domain | Solution Guidance | Complexity |
|----------|------|-----------|----------------------|--------------|-------------------|------------|
| **Two-Tier** | ✅ (T1) | ✅ (T2) | ✅ | ✅ | ✅ | High |
| **Severity-Only** | ❌ | ❌ | ⚠️ | ✅ | ❌ | Low |
| **Domain-Specific** | ✅ | ⚠️ | ❌ | ❌ | ✅ | Medium |
| **Impact-Only** | ❌ | ✅ | ⚠️ | ✅ | ❌ | Medium |
| **Cause-Only** | ✅ | ❌ | ⚠️ | ✅ | ✅ | Low |
| **Ad-Hoc** | ❌ | ❌ | ⚠️ | ✅ | ❌ | Very Low |

**Hybrid Recommendations**:
- **Large Enterprise**: Two-Tier (strategic) + Domain-Specific (operational)
- **Startup/SMB**: Severity-Only (first 6-12mo) → Two-Tier (when >20 problems)
- **Incident Response**: Severity-Only (triage) + Two-Tier (retrospective)
- **Regulatory-Driven**: Domain-Specific (mandated) + Two-Tier (strategic gaps)

---

## Applicability and Limitations

### When to Use

**✅ Recommended**: Multi-stakeholder/multi-domain problems | Resource allocation | Consistent classification needs | Root cause analysis | Quantifiable data (≥6mo history)

**❌ Not Recommended**: Simple/single-dimension problems | Novel/unprecedented problems | Real-time incident response | Immediate action needed | Strategic/philosophical decisions

### Limitations and Risks

| Risk | Mitigation |
|------|------------|
| **Classification Ambiguity** (10-15%) | Primary driver test; document secondary causes; quarterly review |
| **Data Quality (GIGO)** | Require sources; flag estimates; quarterly updates |
| **Quantification Bias** | Supplement with stakeholder voting; qualitative assessment |
| **Domain Calibration** | Calibrate during pilot; adjust by context |
| **Over-Reliance** | Combine with feasibility; consider strategic importance |
| **Gaming** | Require verification; external review (Tier S); audit |

### Assumptions

1. Root causes identifiable
2. Problems relatively stable
3. Impact measurable (proxy exists)
4. Resources finite
5. Pareto applies (validate with data)

### Dependencies

**Data**: Incident tracking, financial reporting, operational metrics  
**Organization**: Cross-functional agreement, maintenance commitment  
**Expertise**: Deep problem understanding

---

## Success Criteria and Measurement

### Primary Metrics

| Metric | Baseline | Year 1 | Year 2 | Measurement |
|--------|----------|--------|--------|-------------|
| **Resolution Rate** | 40-60% | +10-15% | +20-30% | (Resolved / Addressed) × 100% |
| **ROI Efficiency** | $2-4/$1 | +30-50% | +50-100% | Impact Reduced / Resources Invested |
| **Agreement** | N/A | Mo 1-3: ≥70%<br>Mo 4-6: ≥85% | ≥90% | (Matching / Total) × 100% (3 classifiers, 20 problems) |
| **Predictive Accuracy** | N/A | S: ≥75% high<br>C: ≤20% high | Same | 6mo outcomes, 20/tier |
| **Time-to-Solution** | 3-12mo | -20-30% | -30-50% | Date(Deployed) - Date(Identified) |

### Secondary Indicators

| Indicator | Target | Warning |
|-----------|--------|---------|
| **Satisfaction** (1-5) | ≥4.0 (understanding, transparency)<br>≥3.5 (trust, overhead) | <3.0 @6mo → overhead high |
| **Coverage** | ≥95% in 2 weeks | <80% → rules complex |
| **Data Quality** | Yr 1: 60-70%<br>Steady: ≥80% | Quarterly audit 50 problems |

### Milestones

| Phase | Timeline | Success | Go/No-Go |
|-------|----------|---------|----------|
| **Pilot** | Mo 1-3 | 20 problems, ≥70%, training | <60% → Refine |
| **Rollout** | Mo 4-6 | 80% coverage, ≥85%, 1st cycle | <3.0 satisfaction → Reduce overhead |
| **Optimization** | Mo 7-12 | ≥95% coverage, ≥90%, 10-15% improvement | <10% ROI → Recalibrate |
| **Steady** | Yr 2+ | ≥80% quality, 20-30% resolution, 30-50% ROI | Not met → Major revision |

### Failure Modes

| Symptom | Action |
|---------|--------|
| **Deadlock** (>10% unclassified @30d) | Refine Tier 1, add sub-category |
| **Gaming** | Mandatory verification, external audit (S) |
| **Inversion** (C > S impact) | Recalibrate scales |
| **Revolt** (bypass) | Simplify to Severity-Only 3mo |
| **No Impact** (ROI <5% @12mo) | Analyze decision influence |

### Continuous Improvement

**Quarterly**: Metrics dashboard | Sample 10 (guide solution?) | Disputes → refine tree | Predicted vs. actual (>20% mismatch → adjust) | Feedback

**Annually**: Validate MECE compliance | Assess Pareto distribution (20% → 80% impact?) | Compare ROI to alternatives | Update targets

## Maintenance and Evolution

**Schedule**: Quarterly (recalc scores, adjust tiers) | Semi-Annual (review Tier 1) | Annual (validate MECE, 6 categories) | Major Incidents (update severity)

**Tracking**: Disagreements → refine decision tree | Edge cases → new sub-categories | Tier S outcomes → validate 80/20

---

## Data Quality and Citations

**⚠️ Notice**: Document contains **illustrative estimates** ([^footnotes]). Before decisions: verify, replace with org data, cite sources, flag estimates.

### Data Quality Tiers

| Tier | Use | Requirements |
|------|-----|--------------|
| **Verified** | Tier S | Internal logs/financials <12mo, traceable, ≥2 sources |
| **Substantiated** | Tier A/B | Industry reports, named sources, ranges, flagged "estimated" |
| **Order-of-Magnitude** | Tier C (sparingly) | Explain method, flag "rough", note sensitivity |

**Citation Format**: `Impact: $2.3M | Source: [Report, Dept, Date] | Status: ✅ Verified | Updated: YYYY-MM-DD`

### References

**Classification**: Ishikawa (1990), Reason (2000) BMJ 320:768, Perrow (1999)  
**Pareto**: Koch (2011), Juran (1954) Mgmt Review 43:748  
**MECE**: Minto (2009)  
**Analysis**: Ritchey (2011), Checkland (1999)  
**Risk**: Hubbard (2009), ISO 31000:2018

---

## Quality Assurance Checklist

### Problem Documentation

☐ **Context**: Problem, stakeholders, constraints, scale  
☐ **Data**: Impact/frequency verified (≥6mo), sources, estimates flagged  
☐ **Classification**: Tier 1 + Tier 2 (3-5 tags) + Severity + Score  
☐ **Actionability**: Success criteria, alternatives, trade-offs, timeline  
☐ **Review**: ≥2 stakeholders, quarterly schedule, quality threshold (≥80% Tier S)

### System Health

**Quarterly**: Recalc scores | Verify 20%→80% | ≥90% agreement | Update data  
**Annual**: Validate MECE | Resolution (+20-30%), ROI (+30-50%) | Satisfaction (≥4.0) | Refine rules

---

**End of Document**
