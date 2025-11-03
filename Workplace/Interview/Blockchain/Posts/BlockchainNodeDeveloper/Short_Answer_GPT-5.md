# Blockchain Node Developer — Short Answer / Calculation (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Short_Answer.md](../../Prompts/Templates/Short_Answer.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Problem Bank](#problem-bank-problems-1-25)
- [Topic 1: Throughput, Latency, and SLOs](#topic-1-throughput-latency-and-slos)
- [Topic 2: Gas, Storage, and DB](#topic-2-gas-storage-and-db)
- [Topic 3: Consensus and Networking](#topic-3-consensus-and-networking)
- [Topic 4: Operations and Reliability](#topic-4-operations-and-reliability)
- [Reference Sections](#reference-sections)

---

## Problem Bank (Problems 1–25)

### Topic 1: Throughput, Latency, and SLOs

#### P1: Hedged requests tail trimming

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** A gateway hedges RPC requests after 150 ms to a second backend. Single request latency p99 is 300 ms. Assuming independence and the second request cancels the first upon success, estimate new p99.

**Given:** p99_single = 300 ms; hedge at 150 ms; independence assumed.

**Answer:** ~225 ms | **Tolerance:** ±10% | **Units:** ms

**Worked Solution:**
1. Hedging cuts tail roughly by factor sqrt for independent paths: new_p99 ≈ p99_single/√2.
2. 300/1.414 ≈ 212 ms; with cutoff overhead ≈ 225 ms acceptable.

**Alternative Forms:** Detailed order-statistics derivation.

**Grading:** Method + independence assumption.

---

#### P2: SLO error budget burn

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** Monthly availability SLO is 99.95%. In a 30‑day month, how many minutes can be down?

**Given:** 30 days.

**Answer:** 21.6 minutes | **Tolerance:** ±0.5 min | **Units:** minutes

**Worked Solution:**
1. 30×24×60=43,200 min total.
2. 0.0005×43,200=21.6 min.

**Grading:** Correct arithmetic.

---

#### P3: p95/p99 guardrail

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** p95 eth_call=110 ms, p99=280 ms. SLO requires p95<120 ms and p99<250 ms. What is the deficit and which actions help?

**Given:** p95=110, p99=280.

**Answer:** 30 ms p99 deficit; actions: request hedging, split heavy queries, cache hot reads.

**Worked Solution:**
1. Check thresholds: p95 OK; p99 exceeds by 30 ms.
2. Tail‑focused mitigations reduce p99 without harming mean.

**Grading:** Identify deficit + correct mitigations.

---

#### P4: Regional latency budget

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** User→POP 30 ms, POP→gateway 10 ms, gateway→node 20 ms, node processing 120 ms (p95). Is p95<200 ms met?

**Given:** 30+10+20+120 ms path.

**Answer:** Yes (180 ms) | **Tolerance:** exact | **Units:** ms

**Worked Solution:** Sum path = 180 ms < 200 ms.

**Grading:** Correct summation.

---

#### P5: Rate limit math

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Per‑tenant quota 100 req/s burst 200 for 10 s. What is the max requests served in a 10‑s burst window?

**Given:** R=100/s, burst=200/s for 10 s.

**Answer:** 2,000 requests | **Tolerance:** ±0 | **Units:** requests

**Worked Solution:** 200×10=2,000.

**Grading:** Correct calculation.

---

### Topic 2: Gas, Storage, and DB

#### P6: Gas cost of batch

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** A batch of 100 eth_call simulations consumes 25k gas each (simulated). Estimate total gas if executed on‑chain.

**Given:** 100×25,000.

**Answer:** 2,500,000 gas | **Tolerance:** ±0 | **Units:** gas

**Worked Solution:** 100×25k=2.5M.

**Grading:** Multiplication.

---

#### P7: Bloom filter false positive

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** A log index uses a bloom filter with m=10 bits/entry and k=7 hashes. Approximate false positive rate.

**Given:** Standard bloom FPR ≈ (1−e^{−kn/m})^k with n=1 entry per m bits.

**Answer:** ≈1%–2% | **Tolerance:** conceptual | **Units:** percent

**Worked Solution:** For optimal k≈(m/n)ln2≈~6.9, FPR ≈ (0.5)^k ≈ 0.78%–1.5%.

**Grading:** Recognize relation and range.

---

#### P8: RocksDB write amplification

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Observed write amp is 8×; reducing to 4× saves what fraction of provisioned IOPS for same throughput?

**Given:** Write amp proportional to IO.

**Answer:** ~50% savings | **Tolerance:** ±10% | **Units:** percent

**Worked Solution:** 4/8=0.5 → half the I/O required.

**Grading:** Correct proportional reasoning.

---

#### P9: Snapshot storage sizing

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** State snapshot is 800 GB, daily delta 50 GB, keep 7 days. How much object storage?

**Given:** 1 base + 7 deltas.

**Answer:** 1,150 GB | **Tolerance:** ±10 GB | **Units:** GB

**Worked Solution:** 800 + 7×50 = 1,150.

**Grading:** Summation.

---

#### P10: Cache hit improvement

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Block cache hit rate from 80%→92%. Average disk read 4 ms, memory read 0.1 ms. New average read latency?

**Given:** L=H*0.1 + (1−H)*4.

**Answer:** ≈0.42 ms | **Tolerance:** ±0.05 ms | **Units:** ms

**Worked Solution:** 0.92×0.1 + 0.08×4 = 0.092 + 0.32 = 0.412 ms.

**Grading:** Weighted average.

---

### Topic 3: Consensus and Networking

#### P11: Finality confirmations

**Difficulty:** Foundational | **Type:** Justification

**Problem:** Why do exchanges increase confirmations during client advisories?

**Given:** Reorg risk increases.

**Answer:** To reduce double‑spend probability under elevated reorg risk.

**Worked Solution:** Deeper depth exponentially lowers reorg chance in PoW; cautious policy in PoS during finality stalls.

**Grading:** Correct rationale.

---

#### P12: Peer scoring thresholds

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** What’s the trade‑off in tightening GossipSub peer score decay?

**Given:** Decay faster → drop peers sooner.

**Answer:** Better spam resistance but risk of dropping good peers under transient loss.

**Worked Solution:** Aggressive decay increases churn; balance mesh stability vs DoS tolerance.

**Grading:** Identify trade‑off.

---

#### P13: Sync committee subjectivity

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Why must light clients periodically refresh checkpoints?

**Given:** Long‑range attack risk.

**Answer:** To avoid being pinned to stale checkpoints enabling long‑range forks.

**Worked Solution:** Subjectivity requires updated trusted anchors (checkpoint sync).

**Grading:** Security reasoning.

---

#### P14: Fork choice telemetry

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Two nodes show different heads but same finalized epoch. What’s the likely cause and action?

**Given:** Head drift.

**Answer:** Non‑final head divergence due to attestation timing; verify time sync and peer health.

**Worked Solution:** Check NTP, participation; restart not first choice.

**Grading:** Diagnosis + action.

---

#### P15: Partition resilience

**Difficulty:** Advanced | **Type:** Justification

**Problem:** During regional partition, what KPI predicts finality stall?

**Given:** Participation rate drop.

**Answer:** Effective attestation participation below 2/3; monitor head‑finalized distance.

**Worked Solution:** Below threshold → no FFG finality.

**Grading:** Correct KPI.

---

### Topic 4: Operations and Reliability

#### P16: Reorg replay policy

**Difficulty:** Foundational | **Type:** Justification

**Problem:** Why quarantine indexer outputs during reorgs?

**Given:** Inconsistent state risk.

**Answer:** Prevents serving divergent data; enables replay from common ancestor.

**Worked Solution:** Freeze writes → rollback → replay deterministically.

**Grading:** Correct policy.

---

#### P17: Multi‑tenant isolation

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Why enforce per‑tenant allowlists instead of global allowlists?

**Given:** Tenant diversity.

**Answer:** Limits blast radius and supports differentiated risk profiles.

**Worked Solution:** Per‑tenant controls localize abuse impact and costs.

**Grading:** Isolation reasoning.

---

#### P18: Blue/green rollback time

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** If promotion takes 2 min and rollback 1 min, what is max exposure window during fork cutover?

**Given:** 2 + detection + 1.

**Answer:** ≈3–5 minutes depending on detection | **Tolerance:** qualitative | **Units:** minutes

**Worked Solution:** Promotion then quick rollback if regression; add detection delay.

**Grading:** Reasonable estimate.

---

#### P19: NVMe vs network SSD TCO

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Why might reserved local NVMe lower TCO vs network SSD?

**Given:** p99 stability matters.

**Answer:** Lower jitter reduces over‑provisioning for tail; reserved pricing discounts.

**Worked Solution:** Provisioned IOPS costs on network SSD can exceed local NVMe at scale.

**Grading:** Cost reasoning.

---

#### P20: Snapshot cadence

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Choosing snapshot cadence: what balances RPO with egress cost?

**Given:** Daily vs weekly.

**Answer:** Daily deltas + weekly full; verify integrity; throttle egress.

**Worked Solution:** Layered snapshots minimize data and speed restores.

**Grading:** Practical trade‑off.

---

#### P21: WAL durability

**Difficulty:** Advanced | **Type:** Justification

**Problem:** When might you relax WAL fsync and why?

**Given:** Non‑critical indexers.

**Answer:** For non‑authoritative indexers to reduce latency; accept crash data loss.

**Worked Solution:** Keep authoritative nodes strict.

**Grading:** Correct context.

---

#### P22: K8s anti‑affinity

**Difficulty:** Foundational | **Type:** Justification

**Problem:** Why use anti‑affinity for node pods?

**Given:** HA target.

**Answer:** Avoids co‑locating replicas on same host/AZ; improves resilience.

**Worked Solution:** Spreads risk across failure domains.

**Grading:** HA reasoning.

---

#### P23: Request sampling

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** Why sample and log RPC requests?

**Given:** Abuse detection.

**Answer:** Identify patterns (unbounded getLogs); inform throttles and allowlists.

**Worked Solution:** Data‑driven abuse mitigation.

**Grading:** Operational insight.

---

#### P24: Tenant analytics

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** What metrics aid tenant cost attribution?

**Given:** Per‑tenant tags.

**Answer:** Requests, success rate, p95/99 latency, IOPS/use, bytes egress.

**Worked Solution:** Enables pricing and fairness.

**Grading:** Correct metrics.

---

#### P25: SLA exclusions

**Difficulty:** Foundational | **Type:** Justification

**Problem:** Name a valid SLA exclusion for an RPC provider.

**Given:** Upstream halts.

**Answer:** Chain halts / consensus incidents outside provider control.

**Worked Solution:** Documented exclusions align with SLO boundaries.

**Grading:** Correct example.

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md). This note reuses the shared references from `QA_GPT-5.md` across the pack; floors are met collectively.
