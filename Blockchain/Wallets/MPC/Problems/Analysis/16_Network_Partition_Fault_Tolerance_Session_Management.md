# Network Partition Fault Tolerance and Session Management in MPC Wallets – Nine-Aspects Analysis

**Document Metadata**
- **Analysis Date**: 2025-11-30  
- **Framework**: Nine Aspects for Analyzing Problems  
- **Source Problem File**: 16_Network_Partition_Fault_Tolerance_Session_Management.md  
- **Status**: Draft

---

## Table of Contents

1. [Context Recap](#context-recap)
2. [Problem Definition (Aspect 1)](#1-problem-definition-aspect-1)
3. [Internal Logical Relations (Aspect 2)](#2-internal-logical-relations-aspect-2)
4. [External Connections (Aspect 3)](#3-external-connections-aspect-3)
5. [Origins of the Problem (Aspect 4)](#4-origins-of-the-problem-aspect-4)
6. [Problem Trends (Aspect 5)](#5-problem-trends-aspect-5)
7. [Capability Reserves (Aspect 6)](#6-capability-reserves-aspect-6)
8. [Analysis Outline (Aspect 7)](#7-analysis-outline-aspect-7)
9. [Validating the Answer (Aspect 8)](#8-validating-the-answer-aspect-8)
10. [Revising the Answer (Aspect 9)](#9-revising-the-answer-aspect-9)
11. [Summary & Action Recommendations (Aspect 10)](#10-summary--action-recommendations-aspect-10)
12. [Glossary](#11-glossary)
13. [References](#12-references)

---

## Context Recap

- **Problem title**: Network Partition Fault Tolerance and Session Management in MPC Wallets
- **Current state**:
  - Large-scale MPC wallets (2-of-2, 2-of-3, 3-of-5) serve 100M+ users and manage $50B+ assets in production.  
    [Source: Network Partition Fault Tolerance and Session Management in MPC Wallets, Internal Problem Statement, Distributed Systems & Reliability Team, 2025-11-29]
  - Threshold ECDSA protocols such as GG20 and CGGMP21 assume a semi-synchronous network with bounded delays and multiple interactive rounds.  
    [Source: UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts (CGGMP21), Canetti et al., 2021, IACR ePrint 2021/060]
  - Most implementations use static per-round timeouts of roughly 30s–5min; under partitions, sessions often stall indefinitely until manual operator intervention (2–6h typical).  
    [Source: Problem Statement, 2025-11-29; Estimated from incident reports, 2023–2025]
- **Pain points**:
  - **Liveness failures**: When enough parties become unreachable mid-protocol, the system cannot reach the t-of-n quorum even though no party is malicious. Transactions hang, blocking high-value trades and operational flows.  
    [Source: Problem Statement, 2025-11-29; NIST IR 8460, 2023]
  - **Split-brain risk**: Misconfigured systems may allow concurrent signing sessions in different partitions, risking double-signing and violation of custody guarantees.  
    [Source: CAP theorem – Wikipedia, 2024; Problem Statement, 2025-11-29]
  - **Operational burden**: Manual diagnosis, session cleanup, and restarts take 2–6h per incident, creating high on-call load and opportunity cost estimated at $50K–$500K per major institutional event.  
    [Estimate: Based on trading desk feedback and downtime cost models; Problem Statement, 2025-11-29]
- **Goals**:
  - **Availability**: 99.9% availability for 2-of-3 wallets (≈8.7h/year downtime) and 99.99% for 3-of-5 (≈52min/year), aligned with major cloud regional/multi-region SLAs by Q4 2027.  
    [Source: AWS Compute Service Level Agreement, AWS, 2023; Cloud SLA Data summary, 2023]
  - **Fault tolerance**: Match crash-fault tolerance to threshold—e.g., 2-of-3 should tolerate the crash or partition of 1 party without loss of service in most cases.  
    [Source: NIST IR 8460, 2023; Problem Statement, 2025-11-29]
  - **Recovery time**: Reduce average recovery time from partition from 2–6h manual to <5min automated for ≥90% transient partitions by Q4 2026.  
    [Source: Problem Statement, 2025-11-29]
  - **Safety**: Maintain 100% safety (no double-signing) despite higher availability and automation.  
    [Source: Problem Statement, 2025-11-29; Gilbert & Lynch, 2002]
- **Hard constraints**:
  - Cannot loosen cryptographic security assumptions purely to gain availability (e.g., lowering threshold t for convenience).  
    [Source: CGGMP21, Canetti et al., 2021]
  - Latency: Institutional flows expect 2–10s signing latency in normal cases; long-tail behaviour must be bounded and observable (explicit fail vs silent hang).  
    [Source: Institutional custody SLA disclosures, 2022–2024]
  - Budget & talent: Per-provider investment of roughly $2M–$10M over 24 months with limited distributed-systems and MPC experts.  
    [Estimate: Problem Statement, 2025-11-29]
- **Key facts**:
  - BFT consensus typically requires 3f+1 replicas to tolerate f Byzantine faults; crash-fault-tolerant protocols often use 2f+1 to tolerate f crashes.  
    [Source: State Machine Replication and Consensus with Byzantine Adversaries, NIST IR 8460, 2023]
  - CAP theorem proves that under network partition, a system cannot simultaneously guarantee strong consistency and availability; a trade-off must be made.  
    [Source: Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services, Gilbert & Lynch, 2002]
  - Chaos engineering (e.g., Netflix Chaos Monkey) is a standard practice to validate resilience against faults such as instance termination, network partitions, and latency spikes.  
    [Source: Chaos Engineering – Wikipedia, 2024; Netflix/chaosmonkey GitHub README, 2024]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

**Core contradiction**: MPC wallets are engineered for strong adversarial security (Byzantine robustness and threshold secrecy) but deployed in real-world networks where *crash faults and partitions* are more common than active Byzantine behaviour. Safety is preserved, but liveness collapses during partitions.

**Key conflicts**:

1. **Safety vs. Availability under Partition**  
   - Strong consistency (no double-signing) implies halting when quorum cannot be reached.  
   - Institutional traders, however, need predictable availability and explicit failure modes, not silent hangs.  
   [Source: Gilbert & Lynch, 2002; CAP theorem – Wikipedia, 2024]

2. **BFT Threshold Choices vs. Crash Fault Tolerance**  
   - t-of-n thresholds are chosen mainly for Byzantine security (e.g., 2-of-3, 3-of-5), implicitly assuming semi-synchronous networks.  
   - Under partitions, offline nodes behave like crash faults; yet the system lacks explicit CFT and partition handling policies.  
   [Source: NIST IR 8460, 2023; Problem Statement, 2025-11-29]

3. **Static Timeouts vs. Highly Variable Networks**  
   - Short timeouts (<30s/round) detect failures quickly but cause false positives under transient latency spikes or regional congestion.  
   - Long timeouts (>5min) hide legitimate failures and amplify user pain during incidents.  
   [Source: Problem Statement, 2025-11-29]

4. **Cryptographic Session State vs. Operational Simplicity**  
   - Threshold ECDSA sessions maintain multi-round, ephemeral state (commitments, ZK proofs, Paillier ciphertexts).  
   - Partial progress during a partition leaves inconsistent state across parties, complicating restart, replay, and clean-up.  
   [Source: CGGMP21, 2021; Problem Statement, 2025-11-29]

5. **Manual Recovery vs. Enterprise SLAs**  
   - Current incident handling relies heavily on SREs manually inspecting logs, clearing stuck sessions, and coordinating parties.  
   - For 99.9–99.99% availability, most recovery must be automatic, observable, and testable via chaos experiments.  
   [Source: Google SRE Book, Beyer et al., 2016; Industry chaos engineering case studies, 2016–2023]

### 1.2 Goals & conditions

**Expected results with metrics**:

- **Availability**:  
  - 2-of-3 institutional wallets: 99.9% availability (≤8.7h/year downtime).  
  - 3-of-5 institutional wallets: 99.99% availability (≤52min/year).  
  [Source: AWS Compute SLA, 2023]

- **Recovery performance**:  
  - Median partition-induced incident recovery time (RTO) <5min in ≥90% of cases by Q4 2026.  
  - Automated clean-up of 100% aborted sessions within 1min (no stale locks or orphaned state).  
  [Source: Problem Statement, 2025-11-29]

- **Safety**:  
  - Zero double-sign incidents due to partition or split-brain for production wallets.  
  [Source: Problem Statement, 2025-11-29]

- **User experience**:  
  - Explicit, deterministic failure signalling to upstream applications within a bounded window (e.g., <60s) when quorum cannot be reached.  
  [Estimate: Based on user tolerance for delayed crypto transactions in major exchanges, medium confidence]

**Hard constraints**:

- Maintain or improve existing security proofs for key material and threshold schemes.  
- Avoid unbounded complexity explosions in protocol rounds; added coordination and consensus for session state must not multiply latency by >2–3× in steady-state.  
  [Source: CGGMP21 performance discussion, 2021; Google SRE guidelines on latency budgets, 2016]

### 1.3 Extensibility & reframing

**Alternative framings**:

1. **From “signing availability” → “session lifecycle reliability”**  
   - Focus on the entire lifecycle (initiation → rounds → commit/abort → cleanup), not just whether a signature is produced.

2. **From “network partition problem” → “multi-fault tolerance portfolio”**  
   - Treat partitions, slow nodes, and misconfigurations as a family of crash-like faults to be handled via unified detection, fencing, and recovery.

3. **From “synchronous MPC” → “graded synchrony spectrum”**  
   - Consider dynamic switching between semi-synchronous assumptions (normal) and conservative recovery protocols (during suspected partition), possibly borrowing ideas from asynchronous MPC for high-value flows.  
   [Source: Asynchronous MPC overview, IACR surveys, 2018–2022]

4. **From “prevent any downtime” → “optimize risk-adjusted availability”**  
   - Explicitly trade off some downtime to maintain strong safety in extreme partitions, while aggressively eliminating avoidable downtime from transient incidents.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

**Roles**:
- **MPC parties**: Nodes holding key shares (user device, provider HSM clusters, backup custodians).
- **Session coordinator/orchestrator**: Service responsible for initiating sessions, tracking round progress, applying timeouts, and deciding commit vs abort.
- **SRE/DevOps teams**: Operate infrastructure, maintain health checks, respond to incidents.
- **Institutional clients / end-user apps**: Initiate signing requests; experience latency and failures.

**Resources**:
- Cryptographic protocols (GG20/CGGMP21, EdDSA threshold variants).  
  [Source: CGGMP21, 2021]
- Network links across clouds, regions, and corporate firewalls.
- Observability stack (logs, traces, metrics on latency, failure modes).
- Chaos engineering tooling to simulate partitions and verify behaviour.  
  [Source: Chaos Engineering – Wikipedia, 2024]

**Processes**:
- Session creation → participant discovery → parameter negotiation → multi-round signing protocol.  
- Per-round communication (broadcast/point-to-point) with verification and local state update.
- Health checks, heartbeats, and reachability probing.
- Abort, rollback, and cleanup of incomplete sessions.

**Rules**:
- Threshold t-of-n signing rules; minimum online parties required for signing.
- Timeouts per round; global hard limits for session duration.
- Idempotency rules to prevent replay or duplicate execution of sessions.
- Policies for leader election or coordination when multiple parties can initiate sessions.

### 2.2 Balance & "degree"

Examples where "too much of a good thing becomes bad":

1. **Timeout duration**:
   - Too short → frequent false aborts, user-visible failures under benign slowdowns.  
   - Too long → hidden failures, long blocking times, and poor SLO adherence.  
   - Balanced approach → dynamic timeouts based on observed latency distribution (e.g., p95 per route) with safe hard caps.  
     [Estimate: Based on SRE best practices; Google SRE Book, 2016]

2. **Heartbeat frequency**:
   - Too infrequent → slow detection of partitions, long MTTR.  
   - Too frequent → excess overhead and risk of noisy alarms during transient jitter.  
   - Sweet spot → configurable intervals (e.g., 1–5s) combined with multi-sample confirmation before declaring partition.  
     [Source: NIST IR 8460, 2023]

3. **Number of parties (n)**:
   - Too small (2-of-2) → no fault tolerance; any crash breaks liveness.  
   - Too large (e.g., 5-of-9) → complex, slow communication patterns and higher probability of at least one node being slow or unreachable.  
   - Practical choices (2-of-3, 3-of-5) balance security with latency and deployability.  
     [Source: Market observation of MPC wallet deployments, 2025]

### 2.3 Causal chains

**Chain 1: Partition → Timeout → Stuck Session → Trading Losses**

```text
Network partition / severe degradation
  → One or more parties unreachable within session
  → Rounds exceed timeout but state not fully cleaned up
  → Session remains "in-progress"; new attempts may conflict
  → Transactions hang; clients retry or escalate to support
  → SRE manual intervention (2–6h) to clear state and restart
  → Missed trading opportunities ($50K–$500K per incident)
```

[Source: Problem Statement, 2025-11-29; Estimated incident postmortems]

**Chain 2: Ambiguous Quorum → Split-Brain → Double-Signing Risk**

```text
Partition splits parties into A and B
  → Quorum rules not strictly enforced at global level
  → Subsystem A (2 parties) and subsystem B (1 party) both attempt sessions
  → Lack of fencing / distributed locking
  → Conflicting signing operations potentially executed
  → Violation of "single active session per wallet" invariant
  → Possible double-sign or inconsistent audit trail
```

[Source: CAP theorem – Wikipedia, 2024; Split-brain literature in distributed databases]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder map

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream** | Cloud providers (AWS/GCP/Azure), ISPs, corporate IT / firewall admins | Provide reliable connectivity and security controls | Cannot eliminate all partitions; security policies may block MPC ports; shared infrastructure | Wallet providers want open connectivity; security teams favour restrictive rules |
| **Upstream** | Cryptographic protocol designers / researchers | Strong security proofs, minimal leakage, robustness against malicious adversaries | Typically focus on adversarial models more than crash/partition faults | Industrial deployments need operational fault tolerance, not just proofs |
| **Downstream** | Institutional clients & trading desks | Predictable, high-availability signing with bounded failure windows | Highly sensitive to downtime during market events; limited appetite for complex error handling | Wallet providers optimise for safety; traders push for availability |
| **Downstream** | Retail users & consumer apps | Simple UX, no "stuck" transactions | Limited understanding of partitions; expect near-instant confirmation or clear error | Engineering wants detailed diagnostics; retail wants simplicity |
| **Sidelineexternal** | Regulators, auditors, insurers | Custody safety, documented SLAs, incident transparency | Limited domain knowledge in MPC specifics; evolving regulation | Providers may resist strict availability commitments without fault-tolerant design |
| **Sidelineexternal** | Competing custody / wallet providers | Differentiate on reliability and security | Face similar technical constraints | Industry collaboration on standards vs competitive secrecy |

### 3.2 Environment and institutions

- **Policy & regulatory environment**: Emerging custody rules (e.g., EU MiCA, US guidance) increasingly require explicit availability and incident response commitments.  
  [Source: MiCA regulatory summaries, 2023–2024]
- **Technology environment**: Multi-cloud, multi-region deployments become the norm, but correlated failures (e.g., Internet routing issues) still cause partitions.  
  [Source: Cloud outage reports, 2019–2024]
- **Market dynamics**: Institutional adoption of digital assets drives expectations towards banking-grade SLAs; incidents can cause client churn or push migrations to competitors.  
  [Source: Crypto custody industry reports, 2022–2024]

### 3.3 Responsibility & room to maneuver

- **MPC wallet providers must**:
  - Define explicit partition-handling semantics (what happens to in-flight sessions; when is automatic abort triggered; how are users informed?).
  - Implement session-level consensus or fencing to prevent split-brain and double-signing.
  - Provide observability and documentation for external auditors.

- **Cloud / network providers**:
  - Offer connectivity SLAs and tools (e.g., cross-region networking, multi-AZ redundancy).  
  - Cannot guarantee no partitions; responsibility is shared but MPC-specific mitigation sits with wallet providers.

- **Regulators / industry bodies**:
  - Can set minimum expectations (e.g., 99.9% availability for custody, RTO < X minutes for major incidents) without dictating specific technical solutions.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Classical distributed systems era (1990s–2000s)**  
   - BFT and CFT theory matured; CAP theorem formalised consistency–availability trade-offs.  
     [Source: NIST IR 8460, 2023; Gilbert & Lynch, 2002]

2. **Threshold cryptography research (2016–2021)**  
   - MPC threshold ECDSA protocols (GG18, GG20, CGGMP21) provided practical multi-party signing with strong security assumptions but limited focus on crash fault and partition behaviour.  
     [Source: CGGMP21, 2021]

3. **First-wave MPC wallet deployments (2018–2023)**  
   - Commercial providers deployed 2-of-2, 2-of-3, and 3-of-5 configurations, focusing on key-theft prevention and HSM replacement.  
   - Network partitions were treated primarily as infrastructure events, handled by manual incident response.

4. **Scale-up and institutionalisation (2023–2025)**  
   - TVL and user counts grew, raising the cost of downtime; outages from cloud/ISP events exposed fragile session management and lack of automated recovery.  
     [Source: Problem Statement, 2025-11-29; Market observation 2025]

### 4.2 Background vs direct causes

- **Background (structural) causes**:
  - Academic MPC protocols assumed semi-synchronous networks and focused on active adversaries; operational robustness was delegated to implementers.
  - Cloud economics incentivised rapid scaling and global distribution before fully hardened failure handling.

- **Direct causes**:
  - Lack of standardised session state models (e.g., no canonical "single source of truth" for session status across parties).
  - Minimal use of distributed consensus or fencing for sessions due to perceived complexity or latency cost.
  - Static timeout policies and ad-hoc health checks.

### 4.3 Root issues

- Misalignment between **security design centre** (Byzantine adversaries, key-theft) and **dominant failure mode** in production (crash faults/partitions).
- Under-investment in reliability engineering (SRE, chaos engineering, fault injection) compared to cryptography research budgets.
- Absence of widely adopted **reference architectures** or standards for MPC wallet fault tolerance and session management.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- Growing institutional adoption increases both the *frequency* and *cost* of partition incidents.
- Cloud networking complexity (multi-cloud, cross-region peering, corporate security layers) increases the likelihood of partial connectivity failures.
- Without explicit design for partition tolerance, downtime and manual recovery windows remain in the 2–6h range, incompatible with target SLAs.

### 5.2 Early signals

- Rising support ticket volume around "stuck" or delayed transactions during major market events.  
  [Estimate: Derived from anecdotal reports in provider channels, medium confidence]
- Internal chaos experiments and ad-hoc failure drills revealing inconsistent session states and manual runbooks.
- External auditors beginning to ask about availability, partition handling, and MTTR as part of custody evaluations.

### 5.3 Scenarios (6–24 months)

- **Optimistic**  
  - Providers invest heavily in session management, distributed locking, and automated recovery.  
  - Chaos engineering becomes standard; 99.9–99.99% availability is achieved for institutional tiers.  
  - Network partitions still occur but manifest as brief, explicit failures with quick recovery.

- **Baseline**  
  - Incremental improvements (better monitoring, some automation), but no systematic re-architecture.  
  - Availability improves modestly (e.g., from 99% to 99.5–99.7%), leaving competitive and regulatory risk.

- **Pessimistic**  
  - One or more high-profile incidents where prolonged partition-induced downtime or a mismanaged split-brain causes major financial loss or regulatory scrutiny.  
  - Resulting in accelerated but reactive overhauls and tighter regulation.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- Mature cryptographic implementations of threshold schemes with strong peer-reviewed security proofs.  
  [Source: CGGMP21, 2021]
- Experience operating multi-region, multi-cloud wallet infrastructure.
- Growing SRE and DevOps practices, often already using observability tools and on-call processes.

### 6.2 Capability gaps

- Limited in-house expertise in **fault-tolerant distributed algorithms** (consensus, fencing, leader election) tailored to MPC sessions.
- Incomplete automation of incident response (e.g., no automatic session cleanup, no partition-aware routing).
- Lack of structured experimentation culture (chaos engineering, game days) specifically for MPC protocols.

### 6.3 Buildable capabilities (1–6 months)

- Establish a cross-functional **Reliability Working Group** (crypto + backend + SRE) focused on partition tolerance.
- Develop a reference **session state machine** and shared store (e.g., strongly consistent KV store) governing session lifecycle.
- Introduce basic chaos experiments (single-party crash, regional outage simulation) into pre-production environments.

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (background → problem → analysis → options → risks)

- **Background**: MPC wallets, threshold signing, current deployment patterns.
- **Problem**: Liveness failures and operational fragility during network partitions; lack of automated recovery.
- **Analysis**: Examine internal processes, dependencies, and trade-offs (safety vs availability, static vs adaptive timeouts, manual vs automated ops).
- **Options**: 
  - A) Enhance current semi-synchronous design with robust session management and partition-aware orchestration.  
  - B) Introduce a dedicated consensus/fencing layer for sessions.  
  - C) Adopt asynchronous or quasi-asynchronous MPC for critical flows.
- **Risks**: Added complexity, potential regressions in latency, implementation errors in new coordination components.

### 7.2 Key judgments (need validation)

- 【P0】 Robust session management plus conservative consensus/fencing can achieve target availability **without** changing underlying cryptographic protocols.
- 【P1】 Dynamic timeouts and adaptive routing can significantly reduce false-positive aborts and improve user experience, with acceptable implementation complexity.
- 【P1】 Chaos engineering can surface the majority of partition failure modes before production, if integrated into regular practice.
- 【P2】 Full asynchronous MPC is likely unnecessary for most flows in the 1–3 year horizon given performance and complexity overhead.

### 7.3 Alternative paths (one-line positioning)

- **Option A – Session-centric reliability**: Keep existing cryptographic protocols; invest in orchestration, state machines, and health-based routing.
- **Option B – Consensus-first approach**: Introduce Raft/Paxos-style consensus for session state to eliminate split-brain and define globally agreed outcomes.
- **Option C – Asynchronous MPC for top-tier flows**: Use asynchronous protocols only for a narrow band of ultra-critical operations.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- Overweighting distributed-systems remedies (consensus, fencing) relative to cryptographic or business-process alternatives.
- Assuming institutional users will always accept explicit failures over rare but silent hangs; needs empirical validation.
- Underestimating engineering effort and organisational change required for robust chaos engineering.

### 8.2 Required intelligence

- Detailed incident data: distribution of partition durations, affected topologies, recovery times, and financial impact.  
  [Estimate: To be collected from incident postmortems and observability data]
- Performance benchmarks for candidate coordination mechanisms (e.g., consensus for session state) under realistic workloads.
- User research on acceptable failure modes and communication patterns (e.g., explicit "try again" vs silent retries).

### 8.3 Validation plan

1. **Data collection**: Standardise incident taxonomy and logging for all partition-related incidents over 3–6 months.
2. **Chaos experiments**: Regularly inject synthetic partitions (per-region, per-party) in staging; measure session completion rates and recovery times.  
   [Source: Chaos Engineering – Wikipedia, 2024]
3. **Pilot implementations**: Roll out new session state machine and cleanup logic to a low-risk subset of wallets; compare MTTR and incident rates.
4. **User validation**: A/B test different error surfaces (explicit fail vs aggressive retry) with select institutional clients; measure satisfaction and operational friction.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Target availability and RTO numbers may be adjusted based on real-world incident distributions and regulator expectations.
- The chosen mix of Options A/B/C may shift as asynchronous MPC matures or as consensus-layer performance improves.

### 9.2 Incremental approach

- Start with **Option A** (session-centric reliability) for near-term wins: clear state machine, automated cleanup, improved observability.
- Introduce **Option B** (consensus/fencing) incrementally for the highest-value wallets or most multi-party deployments.
- Reserve **Option C** (asynchronous MPC) for specific scenarios where even small availability gaps are unacceptable and cost is justified.

### 9.3 "Good enough" criteria

- Measured availability meets or exceeds agreed SLA (e.g., 99.9% for institutional wallets) for at least two consecutive quarters.
- No unresolved partition-induced incidents exceeding agreed RTO (e.g., 30min) without clear mitigation plan.
- Incident postmortems show automated recovery and clear root-cause attribution in the majority of cases.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. The dominant production risk is not cryptographic breakage but *operational liveness* under network partitions; existing designs implicitly favour safety at the cost of availability.
2. Robust **session management**, **partition detection**, and **automated recovery** can close most of the availability gap without changing underlying MPC protocols.
3. Explicit SLAs, observability, and chaos engineering are essential to move from best-effort uptime to bank-grade reliability.
4. A staged roadmap (session-centric improvements → consensus for state → targeted asynchronous MPC) balances risk, cost, and time-to-value.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

1. **【P0】 Define canonical session state machine and storage**  
   → Architecture team  
   → Metric: 100% new signing flows use shared state model by Q2 2026  
   → Date: Draft spec by 2026-02-28

2. **【P0】 Implement automated session cleanup & fencing**  
   → Backend & SRE teams  
   → Metric: 100% aborted sessions cleaned within 1min; zero duplicate active sessions per wallet in staging by 2026-03-31  
   → Date: 2026-03-31

3. **【P1】 Introduce basic partition-aware health checks and routing**  
   → SRE & networking teams  
   → Metric: Partition detection <10s; automatic rerouting/abort in <60s in staging tests  
   → Date: 2026-04-30

4. **【P1】 Establish chaos engineering practice for MPC wallets**  
   → Reliability Working Group  
   → Metric: Monthly game days covering at least two partition scenarios; publish postmortems internally  
   → Date: 2026-05-31

5. **【P2】 Evaluate consensus or locking layer for session state**  
   → Architecture & platform teams  
   → Metric: Prototype with p95 additional latency <200ms and no data loss in failure tests  
   → Date: 2026-06-30

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|------------|-------|
| Underestimated engineering complexity delays delivery | High | Medium | Repeated slippage on milestones; technical debt accumulating | Phase roadmap; secure dedicated team; de-scope low-value features | VP Engineering |
| New coordination layer introduces outages or regressions | High | Medium | Incidents correlated with rollout of consensus/fencing | Blue/green deployment; extensive chaos testing; canary rollouts | Platform Lead |
| Institutional clients reject more explicit failure modes | Medium | Low–Medium | Negative feedback to account managers; ticket volume spikes after changes | Involve key clients early; offer configurable policies and detailed status codes | Product & Customer Success |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Session-centric reliability** | Fastest time-to-value; minimal cryptographic change; mostly orchestration and ops work | Engineering effort in backend/SRE; may not handle extreme scenarios alone | Residual edge cases in complex multi-region failures | Short–medium term; majority of flows; organisations with strong SRE teams | When regulatory or business demands require formal consensus guarantees immediately |
| **B. Consensus/fencing for session state** | Strong guarantees against split-brain; globally consistent session outcomes | Additional latency; new components to operate and secure | Implementation bugs; misconfiguration; operator unfamiliarity | High-value institutional wallets; multi-region/multi-cloud topologies | When team lacks consensus expertise; for low-value/low-volume flows |
| **C. Asynchronous MPC for critical flows** | Theoretically highest resilience to partitions and arbitrary delays | Significant performance overhead; complex protocols; limited tooling | Implementation complexity; difficult audits; small talent pool | Narrow set of ultra-critical operations where even short downtime is unacceptable | Broad, high-volume retail flows where cost/latency is critical |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|------------|-----------|----------------|
| **Asynchronous MPC** | Class of MPC protocols that remain secure and correct under arbitrary message delays without relying on fixed timeouts; typically much slower and more complex than semi-synchronous variants. | N/A | [Source: Asynchronous secure multi-party computation surveys, IACR ePrint, 2018–2022] |
| **Byzantine Fault Tolerance (BFT)** | Ability of a distributed system to operate correctly even when some nodes behave arbitrarily maliciously; often requires 3f+1 replicas to tolerate f Byzantine faults. | N/A | [Source: NIST IR 8460, 2023] |
| **CAP Theorem** | Result in distributed systems stating that in the presence of a network partition, a system can provide at most two of Consistency, Availability, and Partition tolerance. | N/A | [Source: Gilbert & Lynch, 2002] |
| **Crash Fault Tolerance (CFT)** | Tolerance of nodes that simply stop responding (crash or become unreachable), typically requiring 2f+1 replicas to tolerate f crashes. | N/A | [Source: NIST IR 8460, 2023] |
| **Heartbeat** | Periodic health-check message used to monitor liveness and detect failures or partitions between parties. | Commonly 1–5s interval | [Source: NIST IR 8460, 2023] |
| **Liveness** | Property of a system that it eventually makes progress (e.g., either completes a signature or returns a clear failure) rather than hanging indefinitely. | N/A | [Source: Distributed systems textbooks; Google SRE Book, 2016] |
| **Quorum** | Minimum number of nodes or parties required to perform an operation (e.g., t-of-n threshold for signatures). | t-of-n | [Source: CGGMP21, 2021] |
| **Recovery Time Objective (RTO)** | Target duration to restore a service after an incident (e.g., <5min for partition-induced outages). | Minutes | [Source: Business continuity planning standards; Problem Statement, 2025-11-29] |
| **Semi-synchronous Network** | Network model assuming messages are delivered within some (possibly unknown) bounded delay; underlying assumption in many MPC protocols. | N/A | [Source: CGGMP21, 2021] |
| **Session Management** | Coordination and tracking of multi-round protocol state from initiation through completion or abort, including cleanup and reporting. | N/A | [Source: Problem Statement, 2025-11-29] |
| **Split-brain** | Situation where multiple partitions of a system believe themselves to be the primary or quorum, potentially leading to conflicting operations such as double-signing. | N/A | [Source: Distributed database literature; CAP theorem discussions] |

---

## 12. References

### Tier 1 Sources (Primary: Peer-Reviewed, Official Documentation)

1. **NIST**. (2023). *State Machine Replication and Consensus with Byzantine Adversaries (NIST IR 8460)*. National Institute of Standards and Technology. https://nvlpubs.nist.gov/nistpubs/ir/2023/NIST.IR.8460.ipd.pdf  
   **[Cited in: Context Recap, 1.1, 2.2, 3.2, 11]**
2. **Canetti, R., Gennaro, R., Goldfeder, S., Makriyannis, N., & Peled, U.** (2021). *UC Non-Interactive, Proactive, Threshold ECDSA with Identifiable Aborts (CGGMP21)*. IACR Cryptology ePrint Archive, Report 2021/060. https://eprint.iacr.org/2021/060  
   **[Cited in: Context Recap, 1.1, 2.1, 6.1, 11]**
3. **Gilbert, S., & Lynch, N.** (2002). *Brewer’s Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services*. ACM SIGACT News.  
   **[Cited in: Context Recap, 1.1, 3.2, 5.1, 11]**
4. **Amazon Web Services**. (2023). *Amazon Compute Service Level Agreement*. https://aws.amazon.com/compute/sla/  
   **[Cited in: Context Recap, 1.2, 5.3]**

### Tier 2 Sources (Secondary: Industry Reports, Technical Books, Encyclopedic References)

5. **Beyer, B., Jones, C., Petoff, J., & Murphy, N.** (2016). *Site Reliability Engineering: How Google Runs Production Systems*. O’Reilly Media.  
   **[Cited in: 1.1, 1.2, 2.2, 10.2, 11]**
6. **Wikipedia contributors**. (2024). *CAP theorem*. In Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/CAP_theorem  
   **[Cited in: Context Recap, 1.1, 2.3, 3.2, 5.1]**
7. **Wikipedia contributors**. (2024). *Chaos engineering*. In Wikipedia, The Free Encyclopedia. https://en.wikipedia.org/wiki/Chaos_engineering  
   **[Cited in: Context Recap, 2.1, 8.3]**
8. **Netflix, Inc.** (2024). *Chaos Monkey – Resiliency Tool for Spinnaker*. GitHub repository. https://github.com/Netflix/chaosmonkey  
   **[Cited in: Context Recap, 2.1, 8.3]**

### Internal / Problem-Specific Sources

9. **Distributed Systems & Reliability Team**. (2025-11-29). *Network Partition Fault Tolerance and Session Management in MPC Wallets* (Problem Statement). Internal documentation.  
   **[Cited in: Context Recap, 1.1–1.3, 2.3, 4.1, 5.1, 6.1, 11]**

### Estimates & Assumptions (Not Primary References)

10. **Incident cost and frequency estimates**. Method: Derived from internal support ticket volumes, institutional trading desk interviews, and downtime cost models; Confidence: Medium; Validation: Systematic incident postmortems and financial impact analysis over 6–12 months.  
   **[Used in: Context Recap, 2.3, 5.2, 10.1]**
