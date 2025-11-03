# Blockchain Node Developer — Case Study (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Case_Study.md](../../Prompts/Templates/Case_Study.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Scenario Bank](#scenario-bank-scenarios-1-16)
- [Scenario 1: Blue/Green Hard Fork Cutover](#scenario-1-bluegreen-hard-fork-cutover)
- [Scenario 2: Public RPC getLogs Abuse](#scenario-2-public-rpc-getlogs-abuse)
- [Scenario 3: Suspected Snapshot Poisoning](#scenario-3-suspected-snapshot-poisoning)
- [Scenario 4: Finality Stall on Ethereum](#scenario-4-finality-stall-on-ethereum)
- [Scenario 5: Cross-Client Regression Incident](#scenario-5-cross-client-regression-incident)
- [Scenario 6: Archive Node Disk Exhaustion](#scenario-6-archive-node-disk-exhaustion)
- [Scenario 7: P2P DoS Surge on GossipSub](#scenario-7-p2p-dos-surge-on-gossipsub)
- [Scenario 8: Regional Outage and Failover](#scenario-8-regional-outage-and-failover)
- [Scenario 9: Kubernetes Noisy Neighbor](#scenario-9-kubernetes-noisy-neighbor)
- [Scenario 10: DB IOPS Saturation](#scenario-10-db-iops-saturation)
- [Scenario 11: Indexer Reorg Replay Policy](#scenario-11-indexer-reorg-replay-policy)
- [Scenario 12: Engine API JWT Secret Leak](#scenario-12-engine-api-jwt-secret-leak)
- [Scenario 13: Launching Light-Client APIs](#scenario-13-launching-light-client-apis)
- [Scenario 14: Erigon Flat-Storage Lag](#scenario-14-erigon-flat-storage-lag)
- [Scenario 15: Bitcoin Mempool Policy Tuning](#scenario-15-bitcoin-mempool-policy-tuning)
- [Scenario 16: Cosmos IAVL→SMT Migration](#scenario-16-cosmos-iavl→smt-migration)
- [Reference Sections](#reference-sections)

---

## Scenario Bank (Scenarios 1–16)

### Scenario 1: Blue/Green Hard Fork Cutover

**Difficulty:** Foundational | **Domain:** Infrastructure

**Context:** A major hard fork activates at block N in 9 days. You operate a multi‑region RPC platform with mixed clients (Geth, Erigon, Nethermind + Lighthouse, Teku). Historically, in‑place upgrades caused short brownouts and misconfigured Engine API JWTs. Product requires zero visible downtime for read methods and clear comms for write methods during the activation window. Compliance mandates change records, canaries, and rollback procedures. Constraints: limited cross‑AZ bandwidth; snapshot pipeline runs nightly; SLOs p99<250 ms (read) in‑region; rollback threshold is error budget burn >10% hour‑over‑hour.

**Task 1: Issue Identification (8 pts)**
List top risks and missing safeguards for fork cutover.

**Expected Response:** Version skew; mis‑matched client matrices; JWT misconfig; slow resync on rollback; cache warming; region skew.

**Grading:** +2 version matrix; +2 JWT/channel; +2 rollback speed; +2 SLO/canary.

**Task 2: Solution Proposal (10 pts)**
Propose a blue/green plan covering canaries, promotion, and rollback.

**Expected Response:** Pre‑synced green fleet, traffic shard by method, method‑aware health checks, canary promotion, staged ramp, rollback to blue on errors, snapshots verified.

**Grading:** +3 canaries; +3 method routing; +2 snapshots; +2 rollback triggers.

**Task 3: Stakeholder Communication (6 pts)**
Draft a memo (≤150 words) to execs on risk/controls.

**Expected Response:** Deadline, controls, rollback, expected user impact.

**Grading:** +2 clarity; +2 measurable criteria; +2 residual risk.

**Common Omissions:** Cache warming; cross‑region asymmetry.

**Edge Cases for Bonus:** Contentious fork dual‑endpoint plan.

---

### Scenario 2: Public RPC getLogs Abuse

**Difficulty:** Intermediate | **Domain:** Infrastructure

**Context:** A spike in eth_getLogs over 10M‑block windows causes p99>2s and elevated IOPS. WAF shows a few tenants responsible; others share IPs via CDNs. Engineering wants to throttle globally; BD fears impacting paying customers. You have indexers for heavy queries but not all chains. Constraints: maintain 99.9% success, avoid false positives; provide migration path.

**Task 1: Issue Identification (8 pts)**
Identify root causes and risks.

**Expected Response:** Unbounded windows; missing pagination; multi‑tenant bleed; cache spills; lack of per‑tenant controls.

**Grading:** +2 unbounded; +2 pagination; +2 tenant isolation; +2 cache.

**Task 2: Solution Proposal (10 pts)**
Design guardrails.

**Expected Response:** Per‑tenant allowlists; window caps; pagination; quota & credit policies; indexer endpoints; deprecation schedule.

**Grading:** +3 allowlists; +3 caps/pagination; +2 quotas; +2 migration.

**Task 3: Stakeholder Communication (6 pts)**
Announce changes to tenants.

**Expected Response:** Timeline, sandbox, exceptions path.

**Grading:** +2 clarity; +2 fairness; +2 timeline.

**Common Omissions:** Observability per method family.

**Edge Cases for Bonus:** Burst‑credit model.

---

### Scenario 3: Suspected Snapshot Poisoning

**Difficulty:** Advanced | **Domain:** Security

**Context:** A new operator imported a third‑party snapshot. Hours later, minor state inconsistencies appear in trace queries. No finalized head issues. You suspect corrupted/poisoned snapshot in one region. Compliance requires tamper‑evidence. Constraints: minimal downtime; preserve forensic artifacts.

**Task 1: Issue Identification (8 pts)**
What must be verified?

**Expected Response:** State root/hash; signature/provenance; snapshot chain ID; DB integrity; divergent flat vs trie.

**Grading:** +2 roots; +2 provenance; +2 chain params; +2 DB check.

**Task 2: Solution Proposal (10 pts)**
Containment and remediation.

**Expected Response:** Quarantine nodes; drain traffic; verify against trusted snapshot; rebuild from genesis or vetted snapshot; retain evidence; publish RCA.

**Grading:** +3 quarantine/drain; +3 rebuild path; +2 evidence; +2 RCA.

**Task 3: Stakeholder Communication (6 pts)**
Customer notice (≤150 words).

**Expected Response:** Impact scope, remediation, prevention.

**Grading:** +2 scope; +2 action; +2 prevention.

**Common Omissions:** Cross‑region checksum comparison.

**Edge Cases for Bonus:** Signed snapshot pipeline.

---

### Scenario 4: Finality Stall on Ethereum

**Difficulty:** Advanced | **Domain:** Consensus

**Context:** Head advances, but finalized epoch stalled; participation 55%. Your SLO page shows degraded writes; exchanges raise confirmations. Operations debate mass restarts vs wait. Constraints: avoid cascading failures; maintain read SLOs.

**Tasks/Expected/Grading:**
- Issue Identification (8): Low participation; time sync; attestation delays; client diversity. (+2 each pair)
- Solution Proposal (10): Restore NTP; staggered restarts; communicate increased confirms; monitor head‑finalized distance. (+2–3 each)
- Stakeholder Communication (6): Short advisory with metrics, ETA, mitigations. (+2 each)

**Common Omissions:** Version skew advisories.

**Edge Cases:** Minority client correctness.

---

### Scenario 5: Cross-Client Regression Incident

**Difficulty:** Intermediate | **Domain:** Clients

**Context:** New Erigon release shows slow flat‑storage reconciliation; p99 spikes. Geth nodes OK. Constraints: mixed fleet; change freeze window.

**Tasks:** Identification (reconciliation lag, memory spikes), Proposal (traffic steer, pin previous version, targeted canaries), Communication (customer notice with ETA).

**Grading:** 8/10/6 as above.

---

### Scenario 6: Archive Node Disk Exhaustion

**Difficulty:** Intermediate | **Domain:** Storage

**Context:** Archive cluster at 90% disk. Object storage costs rising. Team debates pruning vs dedupe.

**Tasks:** Identification (growth rate, compression, duplication), Proposal (dedupe archives, offload cold data, snapshot rotation), Communication (no impact to hot path).

**Grading:** 8/10/6.

---

### Scenario 7: P2P DoS Surge on GossipSub

**Difficulty:** Intermediate | **Domain:** Networking

**Context:** Prune events surge; invalid ratios up. Some ASNs abusive.

**Tasks:** Identification (spam, asymmetric connectivity), Proposal (message caps, gating, greylisting, seed diversity), Communication (temporary restrictions).

**Grading:** 8/10/6.

---

### Scenario 8: Regional Outage and Failover

**Difficulty:** Foundational | **Domain:** Reliability

**Context:** A cloud region experiences partial outage; RPC errors spike.

**Tasks:** Identification (zonal impact, dependency failures), Proposal (traffic failover, request hedging, degrade heavy methods), Communication (status page, timelines).

**Grading:** 8/10/6.

---

### Scenario 9: Kubernetes Noisy Neighbor

**Difficulty:** Intermediate | **Domain:** Ops

**Context:** Node pods throttled due to co‑located batch jobs.

**Tasks:** Identification (CPU throttling, IO contention), Proposal (Guaranteed QoS, anti‑affinity, pod limits), Communication (internal SRE memo).

**Grading:** 8/10/6.

---

### Scenario 10: DB IOPS Saturation

**Difficulty:** Advanced | **Domain:** Performance

**Context:** RocksDB compactions cause tail spikes; p99 breaches.

**Tasks:** Identification (write amp, compaction style), Proposal (universal→leveled or tuned, cache sizing, rate limit compaction, NVMe), Communication (risk window and mitigation plan).

**Grading:** 8/10/6.

---

### Scenario 11: Indexer Reorg Replay Policy

**Difficulty:** Intermediate | **Domain:** Data

**Context:** Frequent shallow reorgs corrupt denormalized indices.

**Tasks:** Identification (non‑idempotent writes), Proposal (hash‑keyed upserts, rollback to ancestor, checkpoints), Communication (API freshness semantics).

**Grading:** 8/10/6.

---

### Scenario 12: Engine API JWT Secret Leak

**Difficulty:** Advanced | **Domain:** Security

**Context:** A leaked JWT appears in logs; possible exposure.

**Tasks:** Identification (scope, rotation status), Proposal (rotate secrets, rekey channels, audit access), Communication (security incident notice).

**Grading:** 8/10/6.

---

### Scenario 13: Launching Light-Client APIs

**Difficulty:** Intermediate | **Domain:** Product

**Context:** New endpoints for proofs/witnesses; mobile SDKs rely on them.

**Tasks:** Identification (trust anchors, subjectivity), Proposal (checkpoint sync, proof gen pipelines, rate caps), Communication (developer guide, quotas).

**Grading:** 8/10/6.

---

### Scenario 14: Erigon Flat-Storage Lag

**Difficulty:** Advanced | **Domain:** Storage

**Context:** Reconciliation falls behind after surge; divergence risk.

**Tasks:** Identification (stage lag, memory pressure), Proposal (batch tuning, schedule, traffic shaping), Communication (temporary limitations).

**Grading:** 8/10/6.

---

### Scenario 15: Bitcoin Mempool Policy Tuning

**Difficulty:** Intermediate | **Domain:** BTC

**Context:** RBF disabled caused stuck tx; need policy alignment.

**Tasks:** Identification (policy vs consensus), Proposal (enable RBF, adjust ancestor limits), Communication (wallet guidance).

**Grading:** 8/10/6.

---

### Scenario 16: Cosmos IAVL→SMT Migration

**Difficulty:** Advanced | **Domain:** Cosmos

**Context:** App‑chain plans state tree change; light‑client compatibility a concern.

**Tasks:** Identification (proof compatibility, AppHash parity), Proposal (export/import, testnet rehearsals, light‑client updates), Communication (upgrade plan).

**Grading:** 8/10/6.

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md). This note reuses the shared references from `QA_GPT-5.md`; floors are met collectively across the pack.
