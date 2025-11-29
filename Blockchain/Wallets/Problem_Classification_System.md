# Blockchain Wallet Problem Classification System

**Last Updated**: 2025-11-29  
**Status**: Draft - Pending Citation Completion  
**Owner**: Documentation Team

## Overview

**Purpose**: Systematically classify blockchain wallet problems by root cause to prioritize resource allocation based on impact and frequency.

**System**: Two-tier classification → Priority scoring → Resource tiers
- **Tier 1**: Root cause (select 1 of 6 MECE categories)
- **Tier 2**: Impact domains (select 3-5 tags)
- **Priority Score**: Impact (1-10) × Frequency (1-10) × Weight (1.0-3.0×) = 1-300 → Tier S/A/B/C

**Resource Allocation**: S (≥100): 60-70% | A (50-99): 20-30% | B (20-49): 10-20% | C (<20): <10%

**Limitations**: Single-method approach; requires subjective scoring; data gaps per Status note above. Alternative: incident-driven reactive prioritization trades comprehensiveness for simplicity.

---

## Table of Contents

1. [Tier 1: Root Cause Categories](#tier-1-primary-root-cause-categories-mece)
2. [Tier 2: Impact Dimensions](#tier-2-impact-dimensions-multi-tag-system)
3. [Problem Severity](#problem-severity-classification)
4. [Prioritization Framework](#8020-pareto-prioritization-framework)
5. [Usage Guidelines](#usage-guidelines)
6. [Metadata & Attributes](#cross-cutting-attributes-metadata)
7. [MECE Validation](#mece-validation)
8. [Success Criteria](#success-criteria)
9. [Glossary](#glossary)
10. [References](#references)

---

## Tier 1: Primary Root Cause Categories (MECE)

**Selection Rule**: Choose the primary driver that, if eliminated, would resolve the problem.

| # | Category | Definition | Test | Examples (⚠️ Citations Needed) |
|---|----------|------------|------|-------------------------------|
| **1** | **External Threat** | Malicious actors targeting vulnerabilities | Ceases if adversaries absent; mitigated, never solved | Phishing ($880M annual, 40.8%), Bybit ($1.5B), Insider (11%) |
| **2** | **Technical Constraint** | Cryptographic/protocol boundaries requiring tech breakthroughs | Unfixable by process/education alone | Quantum (ECDSA), MPC latency (2-15s), Gas volatility (5-8×) |
| **3** | **Regulatory Mandate** | Legal requirements with compliance consequences | Disappears if regulation changes | KYC ($5.1B fines, 15-30% abandonment), Jurisdiction gaps |
| **4** | **Design/Standards Gap** | Lack of converged best practices/interoperability | Solvable via industry coordination | DeFi integration ($300K-$1M), Key refresh ($50K-$200K), Cross-chain |
| **5** | **Human/Org Factor** | Human dynamics, coordination, decision-making | Requires governance/training, not tech alone | Governance ($50M-$200M, 6-18mo), Key loss (~20% BTC) |
| **6** | **Economic Constraint** | Financial sustainability/market structure limits | Technically feasible but economically prohibitive | Insurance gaps ($5B+ needed), Custody (100-200 bps), MPC setup ($100K+) |

---

## Tier 2: Impact Dimensions (Multi-Tag System)

**Select 3-5 affected domains per problem** (unlike Tier 1, allows multiple tags)

| Dimension | Indicators | Examples |
|-----------|------------|----------|
| 🔒 **Security** | Dollar losses, breach incidents | Phishing ($880M), Bybit ($1.5B) |
| 📋 **Regulatory** | Fines, compliance costs | KYC/AML ($5.1B fines), Custody classification |
| ⚙️ **Operational** | Process time, error rates, costs | Key refresh (2-8h), Governance (6-18mo) |
| 👥 **UX/Adoption** | Abandonment %, completion rates | KYC friction (15-30%), Self-custody complexity |
| 💰 **Economic** | Implementation/operational costs | MPC setup ($100K+), Custody fees (100-200 bps) |
| ⚡ **Performance** | Latency, throughput | MPC latency (2-15s), DeFi timeouts |
| 🤝 **Trust** | Adoption rates, capital barriers | Trust deficit ($118B+ blocked), Post-FTX |

---

## Prioritization Framework

**Formula**: `Priority Score = Impact (1-10) × Frequency (1-10) × Weight (1.0-3.0×) = 1-300 → Tier S/A/B/C`

### Scoring Components

| Component | Scale | Definition | Examples |
|-----------|-------|------------|----------|
| **Impact** | 1-10 | Financial/user scope | 10: $1B+/10M+ users (FTX, Bybit) • 8: $100M-$1B/1M-10M (Phishing) • 6: $10M-$100M/100K-1M (KYC) • 4: $1M-$10M/10K-100K (DeFi) • 2: $100K-$1M/1K-10K • 1: <$100K/<1K |
| **Frequency** | 1-10 | Occurrence rate | 10: Daily (Gas, Phishing) • 8: Weekly (Multi-chain) • 6: Monthly (Key refresh) • 4: Quarterly (Audits) • 2: Multi-year (Governance) • 1: Rare 5+ years (Quantum) |
| **Weight** | 1.0-3.0× | Severity multiplier | **3.0×** [CRITICAL]: Existential threats, asset loss • **2.0×** [Important]: Competitive barriers • **1.0×** [Moderate]: Incremental gains |

### Scoring Examples & Tiers

| Problem | Impact | Freq | Weight | Score | Tier | Budget | Action |
|---------|--------|------|--------|-------|------|--------|--------|
| Phishing | 8 | 10 | 3.0× | **240** | **S** (≥100) | 60-70% | Immediate investment, continuous monitoring |
| KYC Onboarding | 6 | 10 | 3.0× | **180** | **S** | | |
| Trust Deficit | 8 | 6 | 3.0× | **144** | **S** | | |
| Gas Volatility | 4 | 10 | 2.0× | **80** | **A** (50-99) | 20-30% | Scheduled improvements, automation |
| DeFi Integration | 4 | 8 | 2.0× | **64** | **A** | | |
| Key Refresh | 4 | 6 | 2.0× | **48** | **A** | | |
| Governance Deadlock | 8 | 2 | 3.0× | **48** | **A** | | |
| *(B: 20-49)* | | | | | **B** | 10-20% | Incremental optimizations, defer unless strategic |
| *(C: <20)* | | | | | **C** | <10% | Monitor only, opportunistic fixes |

---

## Usage Guidelines

**Process**: 
1. **Tier 1** (select one): Malicious actors? → 1 | Protocol ceiling? → 2 | Legal mandate? → 3 | Standards gap? → 4 | Human coordination? → 5 | Economic constraint? → 6
2. **Tier 2** (3-5 tags): 🔒 Security | 📋 Regulatory | ⚙️ Operational | 👥 UX | 💰 Economic | ⚡ Performance | 🤝 Trust
3. **Calculate**: Impact × Frequency × Weight → Score → Tier

**Classification Examples**:

| Problem | Tier 1 | Tier 2 Tags | Weight | Score | Tier |
|---------|--------|-------------|--------|-------|------|
| Phishing | 1. External Threat | 🔒 👥 🤝 ⚙️ | 3.0× [CRITICAL] | 240 | S |
| KYC | 3. Regulatory | 📋 ⚙️ 💰 👥 🔒 | 3.0× [CRITICAL] | 180 | S |
| DeFi Integration | 4. Design Gap | ⚡ 💰 👥 ⚙️ 🔒 | 2.0× [Important] | 64 | A |

---

## Template & Maintenance

**Optional Metadata**: Wallet Type (Custody|MPC|Self-Custody) | Stakeholders (Institutional|Consumer|Provider|Regulatory) | Tech Layer (Cryptographic|Infrastructure|Application|Policy)

**Template**:
```markdown
**Tier 1**: [Category]  
**Tier 2**: [Tag] | [Tag] | [Tag]  
**Score**: Impact × Frequency × Weight = [Score] → Tier [S|A|B|C]
```

**Example (Phishing)**: Tier 1: 1. External Threat | Tier 2: 🔒 👥 🤝 ⚙️ | Score: 8 × 10 × 3.0× = 240 → S

**MECE Validation**: Use "primary driver test" for ambiguous cases—which cause, if eliminated, most directly resolves the problem? Category 4 (Design Gap) serves as catch-all for ecosystem immaturity.

**Maintenance**: Quarterly (scores, incidents) | Semi-Annual (categories) | Annual (MECE, citations)

---

## Success Criteria

| Metric | Target | Measurement |
|--------|--------|-------------|
| Classification Consistency | 90%+ agreement | Quarterly audits |
| Resource Effectiveness | 80% impact reduction (Tier S, 12mo) | Track losses, incidents, costs |
| Pareto Validity | Tier S = ≥75% total impact | Annual analysis |
| MECE Compliance | <5% ambiguous cases | Track dual-categorization |

**⚠️ Data Quality Requirements**: All metrics require authoritative citations `[Organization, Report, Date, p. X]` before decision use. Sources: security disclosures, regulatory filings, provider data, market surveys, academic research. Limitations: aggregated/self-reported data, historical extrapolation. Validation: quarterly refresh (time-sensitive) | annual audit (Tier S).

---

## Glossary

- **Root Cause (Tier 1)**: Upstream driver; if eliminated, resolves problem
- **Impact Dimension (Tier 2)**: Affected domains (3-5 tags)
- **MECE**: Mutually Exclusive, Collectively Exhaustive (Tier 1 only)
- **Priority Score**: Impact × Frequency × Weight (1-300)
- **Tiers**: S (≥100, 60-70%), A (50-99, 20-30%), B (20-49, 10-20%), C (<20, <10%)

---

## References

**All metrics require authoritative citations `[Organization, Report, Date, p. X]` for decision use**

**Financial**: Phishing $880M | Bybit $1.5B | FTX $10B+ | Governance $50M-$200M | Blocked capital $118B+ | Key refresh $50K-$200K | KYC $5-$15/user, $5.1B fines | DeFi integration $300K-$1M

**Operational**: Phishing 40.8% daily | Gas volatility 5-8× | KYC abandonment 15-30% | Lost keys ~20% Bitcoin | MPC latency 2-15s | Key refresh 2-8h | Governance deadlocks 6-18mo

---

**End of Document**
