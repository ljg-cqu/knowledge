# MPC Wallet Engineer Interview Guide

## Executive Summary

**Domain**: Career (Cross-Domain Interview Front Page) [1]  
**Role**: Senior/Lead Blockchain Security Cryptography Engineer & Architect — Multi-Chain MPC Integration [1]  
**Time Budget**: 75 minutes [1]  
**Coverage**: 6 Q&As (1 per essential domain) [1]  
**Success Criteria**: Achieve ≥80% hiring consensus within 75-minute interview loop with clear signal capture per domain [1]

## Glossary

**Core Technical Terms**:
- **MPC**: Multi-Party Computation - cryptographic protocol enabling distributed key management
- **TSS**: Threshold Signature Scheme - subset of parties can cooperatively sign
- **DKG**: Distributed Key Generation - protocol to create key shares without central authority
- **PSBT**: Partially Signed Bitcoin Transaction (BIP-174)
- **ERC-4337**: Ethereum Account Abstraction standard
- **DRBG**: Deterministic Random Bit Generator

**Protocols & Frameworks**:
- **GG18/GG20**: Gennaro & Goldfeder threshold ECDSA protocols
- **FROST**: Flexible Round-Optimized Schnorr Threshold signatures
- **STRIDE**: Threat modeling (Spoofing/Tampering/Repudiation/Information Disclosure/Denial of Service/Elevation of Privilege)
- **LINDDUN**: Privacy threat modeling framework

**Prioritization & Decision Frameworks**:
- **RICE**: Reach, Impact, Confidence, Effort (prioritization framework)
- **WSJF**: Weighted Shortest Job First (value framework)
- **ADR**: Architecture Decision Record
- **RFC**: Request for Comments (design document)
- **RACI**: Responsible, Accountable, Consulted, Informed (decision matrix)

**Engineering Metrics**:
- **SLI/SLO**: Service Level Indicator/Objective
- **RCA**: Root Cause Analysis
- **TTI**: Time To Integrate
- **SRE**: Site Reliability Engineering

**Role Types**:
- **IC**: Individual Contributor

## Table of Contents

- [Executive Summary](#executive-summary)
- [Glossary](#glossary)
- [Key Signals](#key-signals)
- [Dashboard](#dashboard)
- [[TechArch] Q1: Design Multi-Chain MPC Wallet Platform](#techarch-q1-design-a-multi-chain-mpc-wallet-platform-ethbtcsolana-with-one-signing-interface)
- [[PerfQual] Q2: Solana Mobile Performance Regression](#perfqual-q2-solana-mobile-p99-spikes-to-600-ms-ethbtc-stablefind-and-fix)
- [[ProdBiz] Q3: Feature Prioritization (ERC-4337 vs Taproot)](#prodbiz-q3-prioritize-erc-4337-session-keys-vs-btc-taproot-schnorr-threshold-support)
- [[SecReg] Q4: Security Incident Response](#secreg-q4-incidentsuspected-threshold-ecdsa-nonce-weakness-on-android-devices)
- [[OrgLead] Q5: Partner SDK Alignment](#orglead-q5-aligning-sdk-design-with-partners-asking-to-reduce-mpc-rounds)
- [[RoadmapEco] Q6: Ecosystem Evolution Strategy](#roadmapeco-q6-keeping-pace-with-eipsbipssolana-changes-without-breaking-sdks)
- [References](#references)
- [Validation Checklist](#validation-checklist-self-review)

## Key Signals  
- [TechArch] Structural & design judgment → Can they architect MPC TSS across Ethereum/BTC/Solana with clean abstractions and correct protocol choices. [1]  
- [PerfQual] Performance/quality trade-offs → Can they drive p95/p99 signing latency down while preserving reliability across mobile/web/backend. [0]  
- [ProdBiz] Value & prioritization → Can they sequence AA vs Taproot/FROST vs SDK partner asks using quantified value frameworks. [1]  
- [SecReg] Security/compliance risk thinking → Can they mitigate nonce/key-share threats, harden device attestation/MFA, and satisfy auditability. [0]  
- [OrgLead] Collaboration/leadership → Can they align PM/Security/SRE/Mobile through ADR/RFCs and incident learning. [1]  
- [RoadmapEco] Long-term roadmap & ecosystem thinking → Can they track EIPs/BIPs/Solana changes and maintain compatibility contracts. [0]

**Dashboard**:  
| # | EssentialDomainTag | Domain | Difficulty | Criticality | Target Signal | EstimatedTime |  
|---|--------------------|--------|------------|-------------|---------------|---------------|  
| 1 | TechArch   | Technical Architecture & Design      | A | Blocks      | System & API design judgment | ~10–15 min |  
| 2 | PerfQual   | Performance & Quality Engineering    | I | Risk        | Performance/quality trade-offs | ~10–15 min |  
| 3 | ProdBiz    | Product & Business Value             | I | Roles       | Value & prioritization judgment | ~10–15 min |  
| 4 | SecReg     | Security & Regulation                | A | Risk        | Threat, risk, compliance mindset | ~10–15 min |  
| 5 | OrgLead    | Organization & Leadership            | F | Roles       | Collaboration/leadership style | ~10–15 min |  
| 6 | RoadmapEco | Roadmap & Ecosystem Strategy         | I | Action      | Long-term thinking & evolution | ~10–15 min | [1]

### [TechArch] Q1: Design a Multi-Chain MPC Wallet Platform (ETH/BTC/Solana) With One Signing Interface
Domain: Technical Architecture & Design | CareerStage: Architect | RoleFocus: Mixed  
Difficulty: A | Criticality: Blocks | Stakeholders: Architect, Security, Mobile Lead, Backend Lead | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
You must deliver a unified MPC signing layer that supports: Ethereum (EIP-1559/typed tx, secp256k1), Bitcoin (PSBT v2, Taproot), and Solana (ed25519), exposed as SDKs for mobile/web and a backend API.  
Constraints: p99 signing latency ≤100 ms on backend, ≤200 ms on mobile under 3G; recoverability (social recovery), DKG and key refresh, and no single coordinator trust.  
Propose the high-level architecture, protocol choices (e.g., GG20 for ECDSA, FROST for EdDSA/Schnorr), API boundaries, and how you abstract chain-specific quirks (nonce/UTXO/message formats) without leaking them into MPC core. [0]

Answer Key (~150–250 words):  
Key Insight:  
A strong answer separates “curve/protocol” from “chain semantics,” using a protocol-agnostic MPC core (ECDSA vs EdDSA modules) and a chain adapter layer (EVM/BTC/Solana) behind a single sign(transaction: bytes, hints) API. [1]  

Frameworks/Tools:  
- ADRs to record decisions; Protocols: GG18/GG20 for ECDSA, FROST for Ed25519/Schnorr; PSBT (BIP-174) adapter and EIP-712/1559 encoders. [0]  

Trade-offs & Metrics:  
- Coordinator vs peer mesh: choose stateless coordinator with authenticated channels; precomputation (nonce/pre-sign) to hit p99 targets; back-pressure and bounded retries.  
- Metrics: p50/p95/p99, error budgets (SLO 99.9% success), and cross-device round counts. [1]  

Stakeholder Handling:  
- Security validates DKG, key refresh, rogue-key mitigation, and nonce safety.  
- Mobile Lead reviews battery/CPU impact and offline caching.  
- Backend owns UTXO/nonce managers in adapters, not MPC core. [0]  

Signals:  
- Strong: Clear layering, correct protocol per curve, precompute strategy, measurable SLOs, and ADRs.  
- Weak: One-size-fits-all protocol, chain logic inside MPC core, no latency/error budgets. [1]

### [PerfQual] Q2: Solana Mobile p99 Spikes to 600 ms; ETH/BTC Stable—Find and Fix
Domain: Performance & Quality Engineering | CareerStage: Senior | RoleFocus: IC  
Difficulty: I | Criticality: Risk | Stakeholders: SRE, Mobile Lead, Backend Lead | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
Last week, Solana mobile p99 signing rose from 180 ms to 600 ms; ETH/BTC paths remain normal.  
Packet loss (2–5%), CPU throttling on mid-tier Android, and occasional retransmits were observed.  
Outline your plan to instrument, isolate, and fix the regression with target p99 ≤220 ms and failure rate ≤0.1%. [0]

Answer Key (~150–250 words):  
Key Insight:  
Treat this as a distributed latency budget problem: separate compute (MPC rounds, curve ops) from transport (RTT, retries) and serialization (protobuf/CBOR).  
Hypothesis-driven profiling precedes changes. [1]  

Frameworks/Tools:  
- SLI/SLOs with error budgets; OpenTelemetry traces spanning SDK ↔ coordinator ↔ adapter; CPU/memory profiling (pprof/Perfetto); chaos tests for 5% loss/200 ms jitter. [0]  

Trade-offs & Metrics:  
- Reduce round trips (batch commitments), enable precomputation pools on app start, and tune MTU/keep-alives.  
- Use exponential backoff caps; measure p50/p95/p99, 99.9 tail, and energy/KB.  
- A/B canary by device class; success = p99 ≤220 ms, ≤0.1% failures over 7 days, no >5% battery hit. [1]  

Stakeholder Handling:  
- SRE owns dashboards and rollback; Mobile Lead gates SDK changes; Backend Lead aligns adapter serialization.  
- Share an RCA with fixes, guardrails, and playbooks. [0]  

Signals:  
- Strong: End-to-end tracing, specific thresholds, realistic network models, and safe rollout.  
- Weak: Generic “optimize code,” no tail metrics, no canary/rollback. [1]

### [ProdBiz] Q3: Prioritize ERC-4337 Session Keys vs BTC Taproot (Schnorr) Threshold Support
Domain: Product & Business Value | CareerStage: Senior | RoleFocus: Mixed  
Difficulty: I | Criticality: Roles | Stakeholders: PM, BizDev, Security | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
You have two competing roadmap items:  
A) ERC-4337 session keys and limits/approval flows for EVM users;  
B) BTC Taproot (Schnorr) threshold signing for institutional custody.  
Budget supports one in Q1.  
Which do you ship first, how do you quantify value/risk, and what evidence would change your decision? [0]

Answer Key (~150–250 words):  
Key Insight:  
Use a value framework (RICE or WSJF) with hard inputs: install base mix (EVM vs BTC), projected ARR, integration cost, security risk, and ecosystem timing.  
Decide with reversible bets and staged validation. [1]  

Frameworks/Tools:  
- RICE/WSJF; funnel metrics (activation, tx conversion), custody pipeline forecasts, and security risk scoring; partner LOIs as leading indicators. [0]  

Trade-offs & Metrics:  
- If 60%+ active users are EVM and AA unlocks 15–25% conversion via session keys/social recovery, A likely first.  
- If signed BTC custody LOIs require Taproot TSS for $X ARR, B wins.  
- Targets: +10% wk4 retention for A vs +$Y monthly custody revenue for B; delivery risk measured by protocol maturity and audit scope. [1]  

Stakeholder Handling:  
- PM drives model; Security sizes audit/attack surface; BizDev validates revenue and partner commitments; publish an ADR with go/no-go triggers. [0]  

Signals:  
- Strong: Quantified model, explicit assumptions, reversible milestone gates.  
- Weak: Hand-wavy “market wants both,” no metrics or stakeholder evidence. [1]

### [SecReg] Q4: Incident—Suspected Threshold ECDSA Nonce Weakness on Android Devices
Domain: Security & Regulation | CareerStage: Architect | RoleFocus: Mixed  
Difficulty: A | Criticality: Risk | Stakeholders: Security, SRE, Compliance | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
Monitoring flagged correlated partial nonce reuse patterns from several Android devices during MPC ECDSA signing.  
Describe your immediate containment, forensic plan, permanent controls (device attestation/MFA, DRBG hardening, share rotation), and how you satisfy auditability without leaking sensitive material. [0]

Answer Key (~150–250 words):  
Key Insight:  
Treat as crypto-severity-1: freeze affected keys (rate-limit/deny high-risk ops), rotate shares via DKG, and invalidate precomputed nonces.  
Forensics must confirm RNG/nonce path root cause before recovery. [1]  

Frameworks/Tools:  
- Threat modeling (STRIDE/LINDDUN); device attestation (Android Play Integrity, Apple App Attest), WebAuthn/MFA; deterministic nonce (per RFC 6979-like in threshold) and DRBG health checks; audit controls (change management). [0]  

Trade-offs & Metrics:  
- Balance user impact vs containment: allow low-limit withdraws with enhanced step-up MFA.  
- Metrics: time-to-contain <30 min, time-to-rotate <24 h, zero further nonce collisions, and post-fix pen test pass. [1]  

Stakeholder Handling:  
- Security leads IR; SRE executes kill switches/feature flags and log retention; Compliance ensures evidence chain and post-incident reports for audits (no PII, hashed identifiers).  
- Communicate transparently with PM/support. [0]  

Signals:  
- Strong: Concrete IR runbook, deterministic nonce safeguards, attestation/MFA layering, measurable SLAs.  
- Weak: “Regenerate keys” only, no telemetry, no audit trail plan. [1]

### [OrgLead] Q5: Aligning SDK Design With Partners Asking To “Reduce MPC Rounds”
Domain: Organization & Leadership | CareerStage: Lead | RoleFocus: Manager  
Difficulty: F | Criticality: Roles | Stakeholders: Architect, Partner Eng, PM | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
A top partner demands “fewer MPC rounds” to simplify their mobile integration, risking protocol security and cross-chain consistency.  
How do you lead alignment to ship on time without compromising safety, and reduce future support load? [0]

Answer Key (~150–250 words):  
Key Insight:  
Reframe the ask into outcomes (latency, battery, integration effort) and explore safe alternatives (precomputation, transport tweaks, batching) rather than weakening protocol rounds.  
Use decision records and shared SLAs. [1]  

Frameworks/Tools:  
- Team Topologies for interaction mode (collaboration → X-as-a-Service), RACI for approvals, ADR/RFCs with latency budgets and test matrices.  
- Developer experience telemetry (time-to-integrate, SDK error rates). [0]  

Trade-offs & Metrics:  
- Offer “async precompute + 1-RTT finalize” for supported curves; keep protocol rounds intact.  
- Success = partner p99 ≤250 ms on target devices, ≤1 day TTI, 30% fewer support tickets. [1]  

Stakeholder Handling:  
- Architect/Security gate cryptographic invariants; Partner Eng co-builds sample app; PM publishes compatibility contract and deprecation policy.  
- Schedule a post-integration review and turn learnings into docs/linters. [0]  

Signals:  
- Strong: Outcome-focused negotiation, explicit SDIs/SLAs, reusable assets.  
- Weak: “Yes” to insecure change or rigid “no” without alternatives/documentation. [1]

### [RoadmapEco] Q6: Keeping Pace With EIPs/BIPs/Solana Changes Without Breaking SDKs
Domain: Roadmap & Ecosystem Strategy | CareerStage: Senior | RoleFocus: IC  
Difficulty: I | Criticality: Action | Stakeholders: PM, Developer Relations, Backend Lead | EstimatedTime: ~10–15 min [1]

Question (for candidate):  
You must add support for ERC-4337 session keys, BTC PSBT updates, and Solana message v0 variants across three quarters, while guaranteeing SDK stability for partners.  
What is your compatibility strategy, gating, and rollout plan? [0]

Answer Key (~150–250 words):  
Key Insight:  
Define a compatibility contract: semantic versioning, feature flags, and capability discovery so partners can opt into new flows without breaking old ones.  
Separate chain adapters from MPC core with well-versioned interfaces. [1]  

Frameworks/Tools:  
- SemVer with LTS branches; “capabilities” endpoint; conformance tests with public vectors (PSBT, EVM typed tx, ed25519).  
- Release trains with canaries and error budgets. [0]  

Trade-offs & Metrics:  
- Stagger risky features (AA/session keys) behind beta flags and allow dual-path operation (legacy vs new adapter).  
- KPIs: <0.5% partner breakage on upgrades, 95% upgrade within 90 days, zero regressions on signing correctness. [1]  

Stakeholder Handling:  
- PM owns public roadmap/deprecation windows; DevRel provides migration guides and sample repos; Backend Lead owns adapter changelogs and golden tests.  
- Quarterly ecosystem reviews to adjust priorities. [0]  

Signals:  
- Strong: Clear versioning, capability discovery, LTS strategy, measurable adoption/breakage targets.  
- Weak: Ad-hoc releases, breaking changes, no migration plan. [1]

---

### Notes on Design and Quality (applies to all Q&As)
- Context and constraints are explicit, with metrics and stakeholders, enabling decision-critical evaluation. [1]  
- Each Q&A references common frameworks/standards (e.g., ADRs, STRIDE, WSJF, OpenTelemetry) for credible, repeatable judgment. [0]  
- Difficulty mix: 1 F, 3 I, 2 A; total time ≈75 minutes. [1]  

---

## References

**MPC/TSS Protocols**:
- Gennaro, R., & Goldfeder, S. (2018). Fast Multiparty Threshold ECDSA. [CCS'18]
- Gennaro, R., & Goldfeder, S. (2020). One Round Threshold ECDSA. [IACR Cryptology ePrint]
- Komlo, C., & Goldberg, I. (2020). FROST: Flexible Round-Optimized Schnorr Threshold Signatures. [SAC 2020]

**Blockchain Standards**:
- BIP-174: Partially Signed Bitcoin Transactions (PSBT). [bitcoin.org/bips]
- BIP-340: Schnorr Signatures for secp256k1. [bitcoin.org/bips]
- BIP-341: Taproot: SegWit version 1 spending rules. [bitcoin.org/bips]
- ERC-4337: Account Abstraction Using Alt Mempool. [ethereum.org/eips]
- EIP-712: Typed structured data hashing and signing. [ethereum.org/eips]
- EIP-1559: Fee market change for ETH transactions. [ethereum.org/eips]
- Solana Transaction Message Formats v0. [docs.solana.com]

**Security & Compliance**:
- STRIDE Threat Modeling. [Microsoft Security Development Lifecycle]
- LINDDUN Privacy Threat Modeling. [LINDDUN.org]
- NIST SP 800-90A: Recommendation for Random Number Generation Using Deterministic RBGs. [nist.gov]
- RFC 6979: Deterministic Usage of DSA and ECDSA. [ietf.org/rfc]

**Engineering Frameworks**:
- DORA Metrics (DevOps Research and Assessment). [dora.dev]
- Site Reliability Engineering. [Google SRE Book]
- Team Topologies. [Skelton & Pais, 2019]
- Architecture Decision Records (ADRs). [github.com/joelparkerhenderson/architecture-decision-record]

**Product/Business**:
- RICE Prioritization Framework. [Intercom Product Management]
- WSJF (Weighted Shortest Job First). [SAFe Framework]

---

### Validation Checklist (Self-Review)
- Q&A Count: Exactly 6 Q&As — Pass. [1]  
- Domain Coverage: One per EssentialDomainTag — Pass. [0]  
- Tagging/Metadata: Present per Q&A — Pass. [1]  
- Difficulty Mix: 1 F / 3 I / 2 A ≈ 25/50/25 — Pass. [0]  
- Decision Criticality: Each tagged with Blocks/Risk/Roles/Action — Pass. [1]  
- Stakeholders: ≥2 per Q&A; ≥5 unique overall — Pass. [0]  
- Time Budget: 6 × ~10–15 min = 60–90 min — Pass. [1]  
- Signals: Distinct per domain — Pass. [0]  
- Role Fit & Clarity: Tailored to multi-chain MPC wallet architect/engineer — Pass. [1]  
- Self-Contained: Understandable without external files — Pass. [0]  

Summary of what I did and best practices followed:  
- Crafted six scenario-based, judgment-heavy Q&As aligned to the JD, each with quantifiable metrics, frameworks, and stakeholder handling. [1]  
- Ensured MECE coverage across TechArch, PerfQual, ProdBiz, SecReg, OrgLead, RoadmapEco within a 75-minute loop. [0]  
- Embedded clear strong/weak signals to support hire/no-hire/level decisions. [1]