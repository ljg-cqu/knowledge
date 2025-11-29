# Blockchain Wallet Problem Classification System

**Last Updated**: 2025-11-29  
**Status**: Draft - Pending Citation Completion  
**Owner**: Documentation Team

## Overview

**Two-tier classification** separating **root causes** (Tier 1: what creates the problem) from **impacts** (Tier 2: what domains are affected), enabling consistent classification and data-driven resource allocation through quantitative Pareto prioritization.

**Classification Process**:
1. **Tier 1** (select one): 6 MECE root cause categories
2. **Tier 2** (select 3-5): 7 impact dimensions  
3. **Severity**: [CRITICAL] | [Important] | [Moderate]
4. **Priority Score**: Impact (1-10) × Frequency (1-10) × Weight (1.0-3.0) = 1-300 → Tier S/A/B/C

**Resource Allocation**: S (≥100): 60-70% | A (50-99): 20-30% | B (20-49): 10-20% | C (<20): <10%

---

## Table of Contents

1. [Tier 1: Primary Root Cause Categories (MECE-Optimized)](#tier-1-primary-root-cause-categories-mece-optimized)
   - [1. External Threat (Malicious Actors)](#1-external-threat-malicious-actors)
   - [2. Technical/Cryptographic Constraint](#2-technicalcryptographic-constraint)
   - [3. Regulatory/Legal Mandate](#3-regulatorylegal-mandate)
   - [4. Design/Standards Gap (Ecosystem Immaturity)](#4-designstandards-gap-ecosystem-immaturity)
   - [5. Human/Organizational Factor](#5-humanorganizational-factor)
   - [6. Economic/Market Constraint](#6-economicmarket-constraint)
2. [Tier 2: Impact Dimensions (Multi-Tag System)](#tier-2-impact-dimensions-multi-tag-system)
3. [Problem Severity Classification](#problem-severity-classification)
4. [80/20 Pareto Prioritization Framework](#8020-pareto-prioritization-framework)
   - [Rationale: Why Quantitative Scoring?](#rationale-why-quantitative-scoring)
   - [Axis 1: Impact Magnitude (Quantitative Scale)](#axis-1-impact-magnitude-quantitative-scale)
   - [Axis 2: Frequency (Occurrence Rate)](#axis-2-frequency-occurrence-rate)
   - [Axis 3: Criticality Weight (Severity Multiplier)](#axis-3-criticality-weight-severity-multiplier)
   - [Pareto Priority Score Calculation](#pareto-priority-score-calculation)
   - [80/20 Priority Tiers](#8020-priority-tiers)
   - [Strategic Application: Pareto Resource Allocation](#strategic-application-pareto-resource-allocation)
5. [Usage Guidelines](#usage-guidelines)
   - [Step-by-Step Classification Process](#step-by-step-classification-process)
   - [Classification Examples (Industry Benchmarks)](#classification-examples-industry-benchmarks)
6. [Cross-Cutting Attributes (Not Classification Categories)](#cross-cutting-attributes-not-classification-categories)
7. [Validation Against MECE Principles](#validation-against-mece-principles)
8. [Problem Metadata Template](#problem-metadata-template)
9. [Maintenance and Evolution](#maintenance-and-evolution)
10. [Success Criteria](#success-criteria)
11. [Verification and Data Quality](#verification-and-data-quality)
12. [Glossary](#glossary)
13. [References](#references)

---

## Tier 1: Primary Root Cause Categories (MECE)

**Principle**: Select the **primary driver** that, if removed, would eliminate the problem.

### 1. External Threat (Malicious Actors)

**Root Cause**: Malicious human intent targeting vulnerabilities.

**Sub-categories**: Cyberattacks | Social Engineering | Insider Fraud | Supply Chain Compromise

**Examples**: Phishing ($880M annual, 40.8% incidents [Citation needed]) | Bybit breach ($1.5B [Citation needed]) | Insider threats (11% hacks [Citation needed])

**Test**: Ceases if adversaries don't exist; mitigated, never solved

---

### 2. Technical/Cryptographic Constraint

**Root Cause**: Mathematical, cryptographic, or protocol-level boundaries unfixable without fundamental technology changes.

**Sub-categories**: Cryptographic Ceilings | Performance Limits | Network Constraints | Protocol Rigidity

**Examples**: Quantum threat (ECDSA vulnerability [Citation needed]) | MPC latency (2-15s [Citation needed]) | Gas fee volatility (5-8× spikes [Citation needed])

**Test**: Not fixable by process/education; requires technological breakthrough

---

### 3. Regulatory/Legal Mandate

**Root Cause**: External legal force requiring action, with non-compliance consequences.

**Sub-categories**: Compliance Requirements | Licensing & Classification | Tax & Reporting | Privacy Conflicts | Jurisdictional Fragmentation

**Examples**: KYC ($5.1B fines, 15-30% abandonment [Citation needed]) | Multi-jurisdiction compliance [Citation needed] | Custody classification ambiguity [Citation needed]

**Test**: Disappears if regulation changes; non-negotiable (comply or exit)

---

### 4. Design/Standards Gap (Ecosystem Immaturity)

**Root Cause**: Best practices, standards, and interoperability haven't converged.

**Sub-categories**: Protocol Fragmentation | Integration Complexity | Tooling Gaps | Knowledge/Documentation Deficits

**Examples**: DeFi integration ($300K-$1M/provider [Citation needed]) | Key refresh ($50K-$200K annual, no automation [Citation needed]) | Cross-chain incompatibility [Citation needed]

**Test**: Solvable via industry coordination; improves with maturity

---

### 5. Human/Organizational Factor

**Root Cause**: Human decision-making, interpersonal dynamics, or multi-party coordination challenges.

**Sub-categories**: Multi-Party Coordination | User Error | Organizational Conflict | Knowledge/Training Gaps

**Examples**: Governance disputes ($50M-$200M frozen, 6-18mo resolution [Citation needed]) | Key loss (~20% Bitcoin [Citation needed]) | Training gaps (8-12% completion [Citation needed])

**Test**: Not solvable by technology alone; requires governance/training

---

### 6. Economic/Market Constraint

**Root Cause**: Financial sustainability limits, market structure, or capital availability constraints.

**Sub-categories**: Cost-Benefit Misalignment | Market Structure Gaps | Economic Accessibility | Operational Economics

**Examples**: Insurance gaps ($500M-$1B vs $5B+ needed [Citation needed]) | Custody costs (100-200 bps vs TradFi 10-50 bps [Citation needed]) | MPC setup ($100K+ [Citation needed])

**Test**: Technically feasible but economically prohibitive; improves with scale

---

## Tier 2: Impact Dimensions (Multi-Tag System)

**Purpose**: Tag 3-5 affected domains per problem. Unlike Tier 1 (single root cause), Tier 2 allows multiple tags.

### 🔒 Security & Asset Protection
**Indicators**: Dollar losses, breach incidents, attack success rates  
**Examples**: Phishing ($880M [Citation needed]) | Bybit breach ($1.5B [Citation needed])

### 📋 Regulatory & Legal Compliance
**Indicators**: Fines, compliance costs, audit requirements  
**Examples**: KYC/AML ($5.1B fines [Citation needed]) | Custody classification ambiguity [Citation needed]

### ⚙️ Operational Efficiency
**Indicators**: Process time, error rates, operational costs  
**Examples**: Key refresh (2-8h [Citation needed]) | Governance deadlocks (6-18mo [Citation needed])

### 👥 User Experience & Adoption
**Indicators**: Abandonment %, completion rates, support tickets  
**Examples**: KYC friction (15-30% abandonment [Citation needed]) | Self-custody complexity [Citation needed]

### 💰 Economic & Cost
**Indicators**: Implementation costs, operational expenses, transaction fees  
**Examples**: MPC setup ($100K+ [Citation needed]) | Custody fees (100-200 bps [Citation needed])

### ⚡ Technical Performance
**Indicators**: Latency, throughput, scalability ceilings  
**Examples**: MPC latency (2-15s [Citation needed]) | DeFi timeouts

### 🤝 Trust & Market Confidence
**Indicators**: Adoption rates, capital barriers, incident frequency  
**Examples**: Trust deficit ($118B+ blocked [Citation needed]) | Post-FTX crisis [Citation needed]

---

## Problem Severity Classification

**[CRITICAL]**: Business-ending threats — asset loss, regulatory shutdown, permanent fund loss (>$10M impact)  
**[Important]**: Market position/competitive barriers — customer attrition, operational burden (>$1M annual)  
**[Moderate]**: Incremental improvements — efficiency gains, optimization opportunities (<$1M annual)

---

## 80/20 Pareto Prioritization Framework

**Formula**: `Priority Score = Impact (1-10) × Frequency (1-10) × Weight (1.0-3.0) = 1-300`

### Impact Magnitude (1-10)

| Score | Magnitude | Examples |
|-------|-----------|----------|
| **10** | Catastrophic ($1B+) | FTX ($10B), Bybit ($1.5B), Mt. Gox ($500M) |
| **8** | Severe ($100M-$1B) | Phishing ($880M annual), Frozen funds ($50M-$200M) |
| **6** | Significant ($10M-$100M) | Regulatory fines, KYC/AML infrastructure |
| **4** | Moderate ($1M-$10M) | DeFi integration ($300K-$1M), MPC setup |
| **2** | Minor ($100K-$1M) | Key refresh ($50K-$200K annual), process improvements |
| **1** | Minimal (<$100K) | Minor UX improvements, edge cases |

**User Impact Alternative**: 10M+ = 10 | 1M-10M = 8 | 100K-1M = 6 | 10K-100K = 4 | 1K-10K = 2 | <1K = 1

### Frequency (1-10)

| Score | Frequency | Examples |
|-------|-----------|----------|
| **10** | Constant (daily) | Gas volatility (5-8× monthly), Phishing (40.8% daily) |
| **8** | Very Frequent (weekly) | Signing delays, Multi-chain coordination |
| **6** | Frequent (monthly) | Compliance updates, Key refresh (quarterly aggregated) |
| **4** | Periodic (quarterly/annual) | Audits, Insurance renewals, Protocol upgrades |
| **2** | Occasional (multi-year) | Governance deadlocks (5-10% cases), Security incidents |
| **1** | Rare (<5 years) | Catastrophic failures (FTX-scale), Quantum breakthrough |

### Criticality Weight (1.0-3.0×)

| Severity | Weight | Rationale |
|----------|--------|-----------|
| **[CRITICAL]** | **3.0×** | Existential threats, asset loss, regulatory shutdown |
| **[Important]** | **2.0×** | Competitive barriers, significant operational burden |
| **[Moderate]** | **1.0×** | Incremental improvements, optimizations |

### Priority Score Examples

| Problem | Impact | Freq | Weight | Score | Tier |
|---------|--------|------|--------|-------|------|
| Phishing | 8 | 10 | 3.0× | **240** | S |
| KYC Onboarding | 6 | 10 | 3.0× | **180** | S |
| Trust Deficit | 8 | 6 | 3.0× | **144** | S |
| Gas Volatility | 4 | 10 | 2.0× | **80** | A |
| DeFi Integration | 4 | 8 | 2.0× | **64** | A |
| Key Refresh | 4 | 6 | 2.0× | **48** | A |
| Governance Deadlock | 8 | 2 | 3.0× | **48** | A |

### Priority Tiers

| Tier | Score | Budget | Action |
|------|-------|--------|--------|
| **S** | ≥100 | 60-70% | Immediate investment, continuous monitoring |
| **A** | 50-99 | 20-30% | Scheduled improvements, automation |
| **B** | 20-49 | 10-20% | Incremental optimizations, defer unless strategic |
| **C** | <20 | <10% | Monitor only, opportunistic fixes |

---

## Usage Guidelines

### Classification Process

**Step 1: Identify Tier 1** (select one upstream cause)  
Malicious actors? → 1 | Protocol ceiling? → 2 | Legal mandate? → 3 | Standards gap? → 4 | Human coordination? → 5 | Economic constraint? → 6

**Step 2: Apply Tier 2 Tags** (3-5 tags)  
🔒 Security | 📋 Regulatory | ⚙️ Operational | 👥 UX | 💰 Economic | ⚡ Performance | 🤝 Trust

**Step 3: Assign Severity**  
[CRITICAL] | [Important] | [Moderate]

**Step 4: Calculate Priority**  
Impact (1-10) × Frequency (1-10) × Weight (1.0-3.0) → Score (1-300) → Tier S/A/B/C

### Classification Examples

| Problem | Tier 1 | Tier 2 Tags | Severity | Score | Tier |
|---------|--------|-------------|----------|-------|------|
| **Phishing** | 1. External Threat | 🔒 👥 🤝 ⚙️ | [CRITICAL] | 240 | S |
| **KYC** | 3. Regulatory | 📋 ⚙️ 💰 👥 🔒 | [CRITICAL] | 180 | S |
| **Trust Deficit** | 5. Human/Org | 🤝 💰 📋 ⚙️ 🔒 | [CRITICAL] | 144 | S |
| **DeFi Integration** | 4. Design Gap | ⚡ 💰 👥 ⚙️ 🔒 | [Important] | 64 | A |
| **Key Refresh** | 4. Design Gap | ⚙️ 💰 ⚡ 🔒 👥 | [Important] | 48 | A |
| **Governance** | 5. Human/Org | ⚙️ 🔒 💰 🤝 📋 | [CRITICAL] | 48 | A |

---

## Cross-Cutting Attributes (Metadata)

**Wallet Type**: Custody | MPC | Self-Custody | General  
**Stakeholders**: Institutional | Consumer | Provider | Regulatory  
**Tech Layer**: Cryptographic | Infrastructure | Application | Policy

---

## MECE Validation

**Mutually Exclusive**: Use **primary driver test** for ambiguous cases: which cause, if eliminated, most directly solves the problem?

**Collectively Exhaustive**: Category 4 (Design/Standards Gap) acts as catch-all for ecosystem immaturity.

---

## Problem Metadata Template

```markdown
**Tier 1**: [Category] > [Sub-category]  
**Tier 2**: [Tag] | [Tag] | [Tag]  
**Severity**: [CRITICAL | Important | Moderate]  
**Score**: Impact × Frequency × Weight = [Score] → Tier [S|A|B|C]  
**Attributes**: Wallet=[Types] | Stakeholders=[List] | Layer=[Tech]
```

**Example**:
```markdown
**Tier 1**: 1. External Threat > Social Engineering  
**Tier 2**: 🔒 Sec | 👥 UX | 🤝 Trust | ⚙️ Ops  
**Severity**: [CRITICAL]  
**Score**: 8 × 10 × 3.0 = 240 → Tier S  
**Attributes**: Wallet=All | Stakeholders=All | Layer=Application
```

---

## Maintenance

**Review Cadence**: Quarterly (scores) | Semi-Annually (categories) | Annually (MECE, citations) | As-needed (incidents)

---

## Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Classification Consistency** | 90%+ agreement | Quarterly audits |
| **Resource Effectiveness** | 80% impact reduction (Tier S, 12mo) | Track losses, incidents, costs |
| **Pareto Validity** | Tier S = ≥75% impact | Annual analysis |
| **Adoption** | 100% new docs (3mo) | Compliance audit |
| **MECE Compliance** | <5% ambiguous | Track dual-categorization |

---

## Data Quality & Verification

**⚠️ CRITICAL**: Replace all `[Citation needed]` with `[Organization, Report, Date, p. X]` before decision-ready use.

**Sources**: Security disclosures | Regulatory filings | Provider data | Market surveys | Academic research

**Limitations**: Aggregated data | Self-reported metrics | Historical extrapolation | Market evolution

**Validation**: Quarterly refresh (time-sensitive data) | Annual audit (Tier S sources)

---

## Glossary

- **Root Cause (Tier 1)**: Upstream driver that, if eliminated, resolves the problem
- **Impact Dimension (Tier 2)**: Affected domains (3-5 tags per problem)
- **MECE**: Mutually Exclusive, Collectively Exhaustive (Tier 1 only)
- **Priority Score**: Impact × Frequency × Weight = 1-300
- **Tier S/A/B/C**: Resource allocation (S=60-70%, A=20-30%, B=10-20%, C=<10%)

---

## References

**Key Metrics** (require authoritative citations):

**Financial Impact**: Phishing $880M [Citation needed] | Bybit breach $1.5B [Citation needed] | FTX $10B+ [Citation needed] | Governance disputes $50M-$200M [Citation needed] | Blocked capital $118B+ [Citation needed]

**Operational Costs**: Key refresh $50K-$200K [Citation needed] | KYC $5-$15/user, $5.1B fines [Citation needed] | DeFi integration $300K-$1M [Citation needed]

**Frequency & Adoption**: Phishing 40.8% daily [Citation needed] | Gas volatility 5-8× spikes [Citation needed] | KYC abandonment 15-30% [Citation needed] | Lost keys ~20% Bitcoin [Citation needed]

---

**End of Document**
