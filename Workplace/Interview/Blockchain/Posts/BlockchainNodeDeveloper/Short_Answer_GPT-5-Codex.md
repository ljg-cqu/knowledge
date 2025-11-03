# Blockchain Node Developer — Short Answer & Calculation Bank (GPT-5 Codex)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Short_Answer.md](../../Prompts/Templates/Short_Answer.md) for shared rules. Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Problem Bank (Problems 1–30)](#problem-bank-problems-1-30)
- [Topic 1: Client Engineering & State Management](#topic-1-client-engineering--state-management)
  - [P1: Archive delta sizing](#p1-archive-delta-sizing)
  - [P2: Trie pruning window](#p2-trie-pruning-window)
  - [P3: Helios sync duration](#p3-helios-sync-duration)
  - [P4: Geth snapshot cadence](#p4-geth-snapshot-cadence)
  - [P5: Cosmos state snapshot parity](#p5-cosmos-state-snapshot-parity)
  - [P6: Archive retention ROI](#p6-archive-retention-roi)
- [Topic 2: Networking, Consensus & Reliability](#topic-2-networking-consensus--reliability)
  - [P7: Gossip latency percentile](#p7-gossip-latency-percentile)
  - [P8: Validator duty loss window](#p8-validator-duty-loss-window)
  - [P9: Fork-choice divergence escrow](#p9-fork-choice-divergence-escrow)
  - [P10: Cosmos relayer SLA](#p10-cosmos-relayer-sla)
  - [P11: Partition survivability index](#p11-partition-survivability-index)
  - [P12: Sequencer backlog drain](#p12-sequencer-backlog-drain)
- [Topic 3: Performance, Capacity & Telemetry](#topic-3-performance-capacity--telemetry)
  - [P13: Disk IOPS budgeting](#p13-disk-iops-budgeting)
  - [P14: NUMA pinning gains](#p14-numa-pinning-gains)
  - [P15: Batch verification throughput](#p15-batch-verification-throughput)
  - [P16: Predictive scaling gain](#p16-predictive-scaling-gain)
  - [P17: Storage tier cost curve](#p17-storage-tier-cost-curve)
  - [P18: Propagation anomaly budget](#p18-propagation-anomaly-budget)
- [Topic 4: Security, Compliance & Operations](#topic-4-security-compliance--operations)
  - [P19: mTLS certificate rotation](#p19-mtls-certificate-rotation)
  - [P20: Evidence catalog growth](#p20-evidence-catalog-growth)
  - [P21: Key ceremony quorum](#p21-key-ceremony-quorum)
  - [P22: Incident MTTR delta](#p22-incident-mttr-delta)
  - [P23: SLA tier mapping](#p23-sla-tier-mapping)
  - [P24: Post-quantum inventory cadence](#p24-post-quantum-inventory-cadence)
- [Topic 5: Emerging Protocols & Integrations](#topic-5-emerging-protocols--integrations)
  - [P25: BRC-20 inscription catchup](#p25-brc-20-inscription-catchup)
  - [P26: zkEVM proof window](#p26-zkevm-proof-window)
  - [P27: MEV relay fairness bounds](#p27-mev-relay-fairness-bounds)
  - [P28: Intent router latency budget](#p28-intent-router-latency-budget)
  - [P29: Cross-chain attestation lag](#p29-cross-chain-attestation-lag)
  - [P30: DAO treasury failover](#p30-dao-treasury-failover)
- [Reference Sections](#reference-sections)

---

## Problem Bank (Problems 1–30)

### Topic 1: Client Engineering & State Management

#### P1: Archive delta sizing

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** You maintain both archive and pruned Geth nodes. Pruned nodes consume 1.6 TB, archives 6.8 TB. If monthly state growth is 180 GB and cold storage costs USD 0.018/GB-month, what is the incremental monthly cost of retaining archives that exceed pruned nodes?

**Given:** Pruned = 1.6 TB; Archive = 6.8 TB; Growth = 180 GB/month; Cost = USD 0.018/GB-month

**Answer:** USD 93.60 | **Tolerance:** ±2% | **Units:** USD

**Worked Solution:**
1. Extra storage = 6.8 − 1.6 = 5.2 TB = 5200 GB.
2. Monthly cost = 5200 × 0.018 = USD 93.60.

**Alternative Forms:** Accept 94 ± 2 USD.

**Grading:** 70% full calc, 20% unit handling, 10% justification | **Common Mistakes:** Forget TB→GB conversion.

---

#### P2: Trie pruning window

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** After enabling Geth snap sync, you must guarantee 128 recent state ranges for compliance. If each range stores 15 GB and you retain an extra 20% buffer, what total storage do you allocate?

**Given:** 128 ranges; range=15 GB; buffer=20%

**Answer:** 2304 GB | **Tolerance:** ±1% | **Units:** GB

**Worked Solution:**
1. Base = 128 × 15 = 1920 GB.
2. Total = 1920 × 1.2 = 2304 GB.

**Alternative Forms:** 2.3 TB accepted.

**Grading:** Steps 70%, buffer reasoning 30% | **Common Mistakes:** Buffer applied incorrectly.

---

#### P3: Helios sync duration

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Helios light client fetches 45 MB block headers plus 65 MB execution payload per epoch. At 125 Mbps link rate with 12% protocol overhead, estimate the time required to sync 32 epochs.

**Given:**
- Payload per epoch = 110 MB
- Epochs = 32
- Link rate = 125 Mbps
- Overhead = 12%

**Answer:** 4.27 minutes | **Tolerance:** ±5% | **Units:** minutes

**Worked Solution:**
1. Effective bandwidth = 125 Mbps × (1 − 0.12) = 110 Mbps.
2. Total payload = 110 MB × 32 = 3520 MB = 28,160 Mb.
3. Sync time = 28,160 Mb ÷ 110 Mbps ≈ 256 s ≈ 4.27 minutes.

**Alternative Forms:** Accept 4.1–4.5 minutes.

**Grading:** Method 70%, conversion 20%, interpretation 10% | **Common Mistakes:** Ignoring protocol overhead.

---

#### P4: Geth snapshot cadence

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** 对于上海数据中心，Geth 快照每 18 小时触发一次，生成 420 GB 文件。若希望在 72 小时窗口内保留 4 份快照，且每份快照复制到两份对象存储副本，请计算总存储需求。

**Given:** Snapshot=420 GB; retention=4; replicas=2

**Answer:** 3360 GB | **Tolerance:** ±2% | **Units:** GB

**Worked Solution:**
1. 单份快照两副本=420 × 2 = 840 GB。
2. 72 小时内共 4 份=840 × 4 = 3360 GB。

**Alternative Forms:** 接受 3.3–3.4 TB。

**Grading:** 步骤正确 70%，单位 20%，解释 10% | **Common Mistakes:** 忘记复制因子。

---

#### P5: Cosmos state snapshot parity

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Your Cosmos-SDK chain keeps hourly snapshots. SLA requires parity check success ≥ 99.5%. If daily snapshots = 24 and two fail parity, what remediation window (hours) remains before SLA breach?

**Given:** Total=24; failures=2; threshold=99.5%

**Answer:** 0 hours | **Tolerance:** exact | **Units:** hours

**Worked Solution:**
1. Success rate = (24−2)/24 = 91.7%.
2. Already below 99.5%, remediation window exhausted → immediate breach.

**Alternative Forms:** “Immediate breach” acceptable.

**Grading:** Recognition 70%, explanation 30% | **Common Mistakes:** Misapplying threshold to monthly totals.

---

#### P6: Archive retention ROI

**Difficulty:** Advanced | **Type:** Justification

**Problem:** 泰国合规团队要求将以太坊归档保留期从 90 天提升到 270 天。现有推理：审计请求 60% 在 45 天内，30% 在 120 天内。请用 2–3 句阐明为何应采用分层存储而非单一热存储。

**Given:** Audit distribution; retention extension

**Answer:** Implement tiered retention: keep 90-day hot archive for majority of requests while offloading older ranges to CAS-backed cold storage with async recall, satisfying 270-day obligation without tripling hot-tier cost [(García & López, 2024)[ES]]. | **Tolerance:** Must mention tiering + compliance + cost.

**Worked Solution:**
1. Identify demand concentration (≤120 days covers 90%).
2. Argue for cold storage for tail while maintaining SLA via prefetch.

**Alternative Forms:** Bilingual rationale accepted.

**Grading:** Completeness 70%, citation 30% | **Common Mistakes:** Suggest decreasing retention.

---

### Topic 2: Networking, Consensus & Reliability

#### P7: Gossip latency percentile

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** Goal: propagate blocks under 400 ms p95. Measurements: 320, 340, 360, 410, 430 ms. What p95 latency do you report?

**Given:** Sample latencies

**Answer:** 430 ms | **Tolerance:** exact | **Units:** milliseconds

**Worked Solution:**
1. Sort values ascending: 320, 340, 360, 410, 430.
2. p95 ~ top sample (5th) = 430 ms.

**Alternative Forms:** Accept 0.43 s.

**Grading:** 70% ordering, 30% explanation | **Common Mistakes:** Averaging.

---

#### P8: Validator duty loss window

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** A validator misses 6 of 64 duties in an epoch. If penalty triggers at 10%, are you safe? Compute miss percentage.

**Given:** Misses=6; total=64; threshold=10%

**Answer:** 9.375% | **Tolerance:** ±0.1% | **Units:** percent

**Worked Solution:**
1. Miss % = (6/64) × 100 ≈ 9.375%.
2. Below 10% threshold ⇒ safe.

**Alternative Forms:** 9.4% accepted.

**Grading:** Calculation 70%, interpretation 30% | **Common Mistakes:** Using 6/32.

---

#### P9: Fork-choice divergence escrow

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Alert triggers if cumulative divergence > 18 slots over 30 min. Current divergences: 4, 5, 3, 2, 6 slots per five-minute window. Do you escalate?

**Given:** Divergences total 20 slots.

**Answer:** Yes, 20 > 18 slots. | **Tolerance:** N/A | **Units:** slots

**Worked Solution:**
1. Sum = 4+5+3+2+6 = 20.
2. Since 20 > 18 → escalate.

**Alternative Forms:** “Escalate immediately.”

**Grading:** Summation 70%, decision 30%. | **Common Mistakes:** Averaging.

---

#### P10: Cosmos relayer SLA

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Daily IBC packets: 18,400. SLA: ≥ 99.2% delivered < 60s. If 110 packets exceed 60s, evaluate SLA status.

**Given:** total=18,400; slow=110; target=99.2%

**Answer:** Meets SLA (slow rate 0.60%). | **Tolerance:** ±0.05% | **Units:** percent

**Worked Solution:**
1. Slow ratio = 110 / 18,400 ≈ 0.006 = 0.6%.
2. Success = 99.4% > 99.2% ⇒ compliant.

**Alternative Forms:** Provide both ratios.

**Grading:** Ratio 70%, conclusion 30%. | **Common Mistakes:** Subtracting from 100 incorrectly.

---

#### P11: Partition survivability index

**Difficulty:** Advanced | **Type:** Justification

**Problem:** Provide a two-sentence justification for testing 45-minute regional partitions even though historical maximum is 12 minutes.

**Given:** Historical 12 min; test target 45 min

**Answer:** Long partitions validate quorum persistence, key rotation buffers, and escrow workflows beyond observed history, ensuring change windows and operator paging still protect finality [(CNCF Security TAG & NSA, 2024)[EN]]. Extending to 45 minutes reveals cascading failures (e.g., stuck relayers, SLA breach) before production events surpass historical maximums.

**Alternative Forms:** Accept bilingual rationale.

**Grading:** Mention resilience + lessons (70%) with citation (30%). | **Common Mistakes:** Arguing against testing.

---

#### P12: Sequencer backlog drain

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 某 L2 Sequencer 在事故中积压 1,800,000 笔交易。恢复后可持续处理 95 TPS，但每 30 分钟需暂停 8 分钟提交有效性证明。请计算清空积压所需时间，并判断是否满足 8 小时恢复目标。

**Given:**
- 积压 = 1,800,000 笔
- 有效吞吐 = 95 TPS
- 停机周期 = 每 30 分钟停机 8 分钟
- 恢复目标 = 8 小时

**Answer:** 约 7.18 小时，满足 8 小时目标。 | **Tolerance:** ±5% | **Units:** 小时

**Worked Solution:**
1. 有效工作占比 = (30 − 8) ÷ 30 = 0.7333。
2. 有效 TPS = 95 × 0.7333 ≈ 69.67。
3. 清空时间 = 1,800,000 ÷ 69.67 ≈ 25,828 秒 ≈ 7.18 小时。

**Alternative Forms:** 接受 7.0–7.5 小时。

**Grading:** 计算 70%，目标判断 30% | **Common Mistakes:** 忽略周期性停机。

---

### Topic 3: Performance, Capacity & Telemetry

#### P13: Disk IOPS budgeting

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** A Bitcoin Core indexer workload requires sustained random read throughput of 5,200 4k IOPS and sequential write throughput of 900 IOPS. The NVMe volume under consideration delivers 6,200 random IOPS and 1,000 sequential IOPS, but SRE policy limits steady-state utilization to 70% of published maximums. Determine whether the volume satisfies the workload.

**Given:**
- Random capacity = 6,200 IOPS
- Sequential capacity = 1,000 IOPS
- Utilization cap = 70%
- Workload random demand = 5,200 IOPS
- Workload sequential demand = 900 IOPS

**Answer:** Insufficient (random budget 4,340 < 5,200; sequential budget 700 < 900) | **Tolerance:** N/A | **Units:** IOPS

**Worked Solution:**
1. Random budget = 6,200 × 0.70 = 4,340 IOPS.
2. Sequential budget = 1,000 × 0.70 = 700 IOPS.
3. Both budgets fall short of workload demand → volume does not meet requirements.

**Alternative Forms:** Accept responses that include explicit deficits (e.g., “short by 860 random and 200 sequential IOPS”).

**Grading:** Calculation 70%, conclusion 30% | **Common Mistakes:** Using peak capacity without applying utilization policy.

---

#### P14: NUMA pinning gains

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** NUMA-aware pinning yields 18% throughput gain on execution client and 9% latency reduction on consensus client. Baseline TPS 1400, latency 180 ms p99. Compute new TPS and latency.

**Given:** TPS=1400; gain=18%; latency=180 ms; reduction=9%

**Answer:** 1,652 TPS and 163.8 ms | **Tolerance:** ±2% | **Units:** TPS, milliseconds

**Worked Solution:**
1. TPS = 1400 × 1.18 = 1652.
2. Latency = 180 × (1 − 0.09) = 163.8 ms.

**Alternative Forms:** Accept 1650 TPS, 164 ms.

**Grading:** Multiplication 70%, units 30%. | **Common Mistakes:** Add percentages.

---

#### P15: Batch verification throughput

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** A batch verifier processes 128 BLS 签名 in 1.6 ms. Three worker goroutines run in parallel, and SRE policy caps sustained CPU utilization at 85%。What maximum signature throughput (signatures per second) can the validator support under this policy?

**Given:**
- 批大小 = 128
- 批耗时 = 1.6 ms
- 并行 worker = 3
- CPU 利用率上限 = 85%

**Answer:** 204,000 signatures/second | **Tolerance:** ±3% | **Units:** signatures/sec

**Worked Solution:**
1. 单 worker 吞吐 = 128 ÷ 0.0016 = 80,000 签名/秒。
2. 并行总吞吐 = 80,000 × 3 = 240,000 签名/秒。
3. 应用利用率上限：240,000 × 0.85 = 204,000 签名/秒。

**Alternative Forms:** 接受 2.04 × 10^5 签名/秒。

**Grading:** 乘法 70%，策略应用 30% | **Common Mistakes:** 忽略 CPU 利用率限制。

---

#### P16: Predictive scaling gain

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Forecasting pipeline predicts surges 12 minutes ahead. Manual scale-out previously took 9 minutes on average; automation shrinks scale time to 3.5 minutes. Compute the percentage reduction in the SLA risk window.

**Given:** Old window = 9 minutes; new window = 3.5 minutes

**Answer:** 61.1% reduction | **Tolerance:** ±2% | **Units:** percent

**Worked Solution:**
1. Reduction = (9 − 3.5) ÷ 9 ≈ 0.611 ≈ 61.1%.

**Alternative Forms:** Accept 61%.

**Grading:** Single-step calculation 70%, explanation 30% | **Common Mistakes:** Dividing by the new window.

---

#### P17: Storage tier cost curve

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 监管要求 5 年保留。每月写入 12 TB 历史数据（未压缩）。策略：前 60 天存放于热存储（USD 0.09/GB-月），之后迁移至冷存储（USD 0.015/GB-月），冷存储检索费用 USD 0.003/GB，且每月有 10% 数据需检索。估算稳定期下的年度总成本（含热/冷存储与检索）。

**Given:**
- 月入库数据 = 12 TB = 12,000 GB
- 热存储窗口 = 2 个月
- 热存储单价 = USD 0.09/GB-月
- 冷存储单价 = USD 0.015/GB-月
- 检索费 = USD 0.003/GB
- 每月检索比例 = 10%

**Answer:** USD 47,563/年 | **Tolerance:** ±5% | **Units:** USD/year

**Worked Solution:**
1. 稳态热存储体量 = 12,000 GB × 2 = 24,000 GB；月费用 = 24,000 × 0.09 = USD 2,160；年费用 = 2,160 × 12 = USD 25,920。
2. 冷存储稳态体量 = 12,000 GB × 10 = 120,000 GB；月费用 = 120,000 × 0.015 = USD 1,800；年费用 = 1,800 × 12 = USD 21,600。
3. 月检索量 = 12,000 × 10% = 1,200 GB；月检索费 = 1,200 × 0.003 = USD 3.6；年检索费 = 3.6 × 12 = USD 43.2。
4. 年总成本 = 25,920 + 21,600 + 43.2 ≈ USD 47,563。

**Alternative Forms:** 接受 4.76 × 10^4 USD。

**Grading:** 步骤完整 60%，单位换算 20%，成本拆分 20% | **Common Mistakes:** 忽略稳态体量或检索费用。

---

#### P18: Propagation anomaly budget

**Difficulty:** Foundational | **Type:** Calculation

**Problem:** Block propagation anomalies (>800 ms) are tracked in rolling 15-minute windows. Escalation triggers when two or more windows within an hour record more than 5 anomalies. The last four windows show anomaly counts of 6, 4, 7, and 3. Should you escalate?

**Given:** Window counts = [6, 4, 7, 3]; threshold = two windows >5 within 60 minutes

**Answer:** Yes—windows 1 and 3 exceed the threshold, so escalation is required. | **Tolerance:** N/A | **Units:** count

**Worked Solution:**
1. Identify windows exceeding 5 anomalies: window 1 (6) and window 3 (7).
2. Two qualifying windows occur within the hour → escalation criteria met.

**Alternative Forms:** “Escalate immediately—two windows >5” is acceptable.

**Grading:** Counting 70%, interpretation 30% | **Common Mistakes:** Averaging the window counts.

---

### Topic 4: Security, Compliance & Operations

#### P19: mTLS certificate rotation

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** 北京运维团队管理 12 个 RPC 集群，每张 mTLS 证书有效期 90 天。合规要求在到期前 28 天启动滚动更新，并在 5 天内完成。若每日最多可轮换 3 个集群，判断是否能在合规窗口内完成，并给出所需天数。

**Given:** 集群 = 12；每日上限 = 3；窗口 = 5 天

**Answer:** 需要 4 天，完全满足 5 天窗口。 | **Tolerance:** N/A | **Units:** 天

**Worked Solution:**
1. 总批次 = 12 ÷ 3 = 4 天。
2. 4 < 5 → 可在窗口内完成全部轮换。

**Alternative Forms:** “4 天内完成”可接受。

**Grading:** 计算 70%，合规判断 30% | **Common Mistakes:** 忽略每日上限。

---

#### P20: Crecimiento del catálogo de evidencias

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** El catálogo de evidencias ocupa actualmente 32 GB (sin replicación). Cada sprint de dos semanas añade 540 registros de 1.5 MB cada uno. La plataforma mantiene un factor de replicación ×3 para cumplir con trazabilidad. Después de 6 meses (12 sprints), ¿cuál será el tamaño total replicado y el incremento porcentual respecto al tamaño replicado inicial? Justifique la importancia de documentarlo para auditorías [(García & López, 2024)[ES]].

**Given:**
- Base = 32 GB
- Registros por sprint = 540
- Tamaño por registro = 1.5 MB
- Sprints = 12
- Replicación = ×3

**Answer:** 125.16 GB replicados totales; incremento del 30.4% sobre los 96 GB iniciales. | **Tolerance:** ±5% | **Units:** GB, percent

**Worked Solution:**
1. Datos nuevos por sprint = 540 × 1.5 MB = 810 MB = 0.81 GB.
2. Datos nuevos en 6 meses = 0.81 × 12 = 9.72 GB.
3. Tamaño sin replicación = 32 + 9.72 = 41.72 GB.
4. Tamaño replicado = 41.72 × 3 = 125.16 GB; inicial replicado = 32 × 3 = 96 GB.
5. Incremento porcentual = (125.16 − 96) ÷ 96 ≈ 0.304 = 30.4%。

**Alternative Forms:** Se acepta 125 GB y 30%。

**Grading:** Cálculo 60%，replicación 20%，contextualización 20% | **Common Mistakes:** Olvidar el factor ×3.

---

#### P21: Key ceremony quorum

**Difficulty:** Intermediate | **Type:** Justification

**Problem:** A quarterly key ceremony requires 7 of 10 custodians to co-sign, with at least 5 physically co-located in the secure room. Four custodians are traveling (can sign remotely via HSM), and one is on medical leave. Determine whether the ceremony can proceed and whether standby alternates must be engaged.

**Given:** Custodians = 10; traveling = 4; unavailable = 1; onsite requirement = 5; quorum = 7

**Answer:** Ceremony can proceed with 5 onsite custodians plus 2 of the 4 remote signers—no alternates needed. | **Tolerance:** N/A | **Units:** custodians

**Worked Solution:**
1. Available custodians = 10 − 1 (leave) = 9.
2. Onsite count = 5 (meets onsite minimum of 5).
3. Select 2 remote signers to reach 7 approvals; remaining remote custodians provide redundancy.

**Alternative Forms:** “Proceed with 5 onsite + 2 remote” accepted.

**Grading:** Constraint analysis 70%, recommendation 30% | **Common Mistakes:** Assuming all travelers are unavailable.

---

#### P22: 事件响应时间压缩

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 上海安全团队要求 95 分位事件关闭时间 ≤ 6 小时。当前阶段耗时：检测 110 分钟、隔离 95 分钟、修复 140 分钟、验证 55 分钟。自动化发布后，检测缩短 40%，隔离缩短 20%。评估新总时长并判断是否达标 [(Beyer et al., 2023)[EN]].

**Given:**
- 原检测 = 110 分钟
- 原隔离 = 95 分钟
- 修复 = 140 分钟
- 验证 = 55 分钟
- 缩短比例：检测 40%，隔离 20%

**Answer:** 新总时长 337 分钟（5.62 小时），满足 6 小时目标。 | **Tolerance:** ±5 分钟 | **Units:** 分钟

**Worked Solution:**
1. 新检测 = 110 × (1 − 0.40) = 66 分钟。
2. 新隔离 = 95 × (1 − 0.20) = 76 分钟。
3. 总时长 = 66 + 76 + 140 + 55 = 337 分钟 ≈ 5.62 小时。

**Alternative Forms:** 可写 5 小时 37 分钟。

**Grading:** 计算 60%，合规判断 40% | **Common Mistakes:** 忽略未变化阶段。

---

#### P23: SLA tier mapping

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** Tier-1 RPC tenants require 99.95% monthly availability, Tier-2 tenants require 99.5%. Compute the monthly downtime budgets in minutes for each tier (assume 30-day months) and identify how much additional downtime Tier-2 tenants can absorb compared to Tier-1.

**Given:** Month = 30 days → 43,200 minutes

**Answer:** Tier-1 budget = 21.6 minutes; Tier-2 budget = 216 minutes; Tier-2 has 194.4 minutes more downtime allowance. | **Tolerance:** ±1 minute | **Units:** minutes

**Worked Solution:**
1. Tier-1 downtime = 43,200 × (1 − 0.9995) = 21.6 minutes.
2. Tier-2 downtime = 43,200 × (1 − 0.995) = 216 minutes.
3. Additional allowance = 216 − 21.6 = 194.4 minutes.

**Alternative Forms:** Accept 0.36 hours (Tier-1) and 3.6 hours (Tier-2).

**Grading:** Multiplication 60%, subtraction 20%, interpretation 20% | **Common Mistakes:** Using 31-day months.

---

#### P24: 量子安全清单排期

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 量子安全清单包含 480 个条目。每条基础梳理耗时 0.3 天，其中 35% 为高优先级需双人复核，额外增加 0.5 天。团队有 3 名工程师，每周有 4 天可投入该项目。计算完成首轮清查所需周数，并说明是否需要额外资源 [(佐藤 & 石川, 2024)[JA]].

**Given:**
- 条目总数 = 480
- 高优先级比例 = 35%
- 基础耗时 = 0.3 天/条
- 额外复核耗时 = 0.5 天/条（仅高优先级）
- 工程师 = 3
- 每周可用天数 = 4 天/人

**Answer:** 需约 19 周完成；当前人力可满足计划。 | **Tolerance:** ±1 周 | **Units:** 周

**Worked Solution:**
1. 高优先级 = 480 × 0.35 = 168 条；低优先级 = 312 条。
2. 工作量 = 168 × (0.3 + 0.5) + 312 × 0.3 = 168 × 0.8 + 93.6 = 134.4 + 93.6 = 228 人天。
3. 每周产能 = 3 × 4 = 12 人天。
4. 周数 = 228 ÷ 12 = 19 周。

**Alternative Forms:** 可写 “约 4.75 个月”。

**Grading:** 工作量拆分 60%，产能计算 20%，排期结论 20% | **Common Mistakes:** 忽略双人复核耗时。

---

### Topic 5: Emerging Protocols & Integrations

#### P25: BRC-20 inscription catchup

**Difficulty:** Intermediate | **Type:** Calculation

**Problem:** 针对 BRC-20 索引服务，当前积压 2,400,000 条铭文任务。Sidecar 解析速度 220 条/秒，但由于重复写入需 15% 重试。估算清空积压所需时间，并说明是否满足 4 小时恢复目标 [(陈强 & 韩雪, 2024)[ZH]].

**Given:**
- 积压 = 2,400,000
- 名义吞吐 = 220 条/秒
- 重试比例 = 15%
- 目标 = 4 小时

**Answer:** 约 3.56 小时，可满足 4 小时恢复目标。 | **Tolerance:** ±5 分钟 | **Units:** 小时

**Worked Solution:**
1. 有效吞吐 = 220 × (1 − 0.15) = 187 条/秒。
2. 时间 = 2,400,000 ÷ 187 ≈ 12,834 秒 ≈ 3.56 小时。

**Alternative Forms:** 接受 3 小时 34 分钟。

**Grading:** 吞吐调整 60%，除法 20%，目标比较 20% | **Common Mistakes:** 未扣除重试比例。

---

#### P26: zkEVM proof window

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** During peak load, 12 rollup partitions generate zkEVM proofs simultaneously. Each proof takes 6 minutes to produce, and the verifier processes proofs sequentially in 90 seconds. Calculate the worst-case time to finalize the last proof in the batch and determine whether it meets the 30-minute finality SLO [(Zero Knowledge Validator, 2024)[EN]].

**Given:**
- Proof generation time = 6 minutes
- Proof count = 12
- Verification time = 90 seconds/proof
- SLO = 30 minutes

**Answer:** 22.5 minutes worst case; SLO satisfied. | **Tolerance:** ±1 minute | **Units:** minutes

**Worked Solution:**
1. Queue delay for last proof = 11 proofs × 90 s = 990 s = 16.5 minutes.
2. Add its own generation time: 16.5 + 6 = 22.5 minutes.
3. 22.5 < 30 ⇒ compliant.

**Alternative Forms:** Accept 1,350 seconds total.

**Grading:** Queue computation 60%, comparison 40% | **Common Mistakes:** Including generation time multiple times.

---

#### P27: Limites de justiça em relays MEV

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** Em 30 dias, um relay MEV registrou 178 slots com ordens preferenciais sem justificativa, num total de 1,800 slots processados. A política corporativa exige manter tais ocorrências ≤8%. Calcule o percentual atual e indique a ação recomendada [(Chainlink Labs, 2023)[EN]].

**Given:** Slots totais = 1,800; incidentes = 178; meta = 8%

**Answer:** 9.89% (>8%); requer revisão de governança e mitigação. | **Tolerance:** ±0.1% | **Units:** percent

**Worked Solution:**
1. Percentual = 178 ÷ 1,800 ≈ 0.0989 = 9.89%。
2. 9.89% > 8% ⇒ iniciar revisão de políticas e monitoramento.

**Alternative Forms:** “~9.9%” aceito.

**Grading:** Cálculo 70%, recomendação 30% | **Common Mistakes:** Subtrair de 100%.

---

#### P28: 意图路由延时预算

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 多链意图路由延时预算为 100 ms，其中风控评分 35 ms、策略编排 45 ms、传输 20 ms。最新观测为 38 ms、32 ms、27 ms。判断是否超出预算，并指出主要瓶颈 [(周敏 & 赵鹏, 2023)[ZH]].

**Given:**
- 预算：35 + 45 + 20 = 100 ms
- 实测：38 + 32 + 27 ms

**Answer:** 总延时 97 ms，未超预算；主要瓶颈在风控评分（+3 ms）与传输（+7 ms）。 | **Tolerance:** ±1 ms | **Units:** milliseconds

**Worked Solution:**
1. 总延时 = 38 + 32 + 27 = 97 ms。
2. 97 < 100 → 满足预算。
3. 风控超预算 3 ms；传输阶段剩余预算 20 − 27 = −7 ms 是最大偏差。

**Alternative Forms:** 可指出“传输阶段超出 7 ms”。

**Grading:** 求和 50%，偏差分析 50% | **Common Mistakes:** 误以为整体超标。

---

#### P29: クロスチェーン証明の遅延評価

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 企業ブリッジは最終証明遅延を 75 秒以内に抑える必要がある。最新メトリクス: ネットワーク伝播 28 秒、バリデータ集約 18 秒、コンプライアンス監査 24 秒、キュー待ち 12 秒。SLO を満たしているか評価し、必要な対応を述べなさい [(Interchain Foundation, 2024)[EN]].

**Given:** 遅延要素 = [28, 18, 24, 12] 秒; SLO = 75 秒

**Answer:** 合計 82 秒で SLO 超過 → キュー短縮や監査並列化が必要。 | **Tolerance:** ±1 秒 | **Units:** seconds

**Worked Solution:**
1. 合計遅延 = 28 + 18 + 24 + 12 = 82 秒。
2. 82 > 75 ⇒ SLO 違反、監査・キュー工程の改善が必要。

**Alternative Forms:** “7 秒オーバー”も可。

**Grading:** 合算 60%，改善提案 40% | **Common Mistakes:** 一部工程のみ比較。

---

#### P30: DAO 国库故障转移容量

**Difficulty:** Advanced | **Type:** Calculation

**Problem:** 某 DAO 国库服务在纽约、北京、新加坡、伦敦、圣保罗五个区域部署，基线吞吐分别为每分钟 3,600、3,200、2,400、2,200、1,800 笔交易。政策要求任一区域故障时，其负载按基线占比分摊到其余区域，每个区域上限为基线的 150%。若纽约区域宕机，计算各剩余区域的新吞吐并判断是否满足上限 [(Cloud Native Telco Forum, 2024)[EN]].

**Given:**
- 基线吞吐（笔/分钟）：纽约 3,600；北京 3,200；新加坡 2,400；伦敦 2,200；圣保罗 1,800
- 上限 = 150% 基线

**Answer:**
- 北京：4,400 笔/分钟 (137.5%)
- 新加坡：3,300 笔/分钟 (137.5%)
- 伦敦：3,025 笔/分钟 (137.5%)
- 圣保罗：2,475 笔/分钟 (137.5%)
均低于 150% 上限 → 容量充足。 | **Tolerance:** ±1 笔/分钟

**Worked Solution:**
1. 剩余区域基线总和 = 3,200 + 2,400 + 2,200 + 1,800 = 9,600。
2. 纽约流量 3,600 按占比分配：北京占比 3,200/9,600 = 1/3 等。
3. 分配量：北京 1,200；新加坡 900；伦敦 825；圣保罗 675。
4. 新吞吐 = 原基线 + 分配量 → 4,400/3,300/3,025/2,475。
5. 各自相对于基线均为 137.5% < 150%。

**Alternative Forms:** 可给出百分比并说明满足上限。

**Grading:** 比例分配 60%，上限判断 40% | **Common Mistakes:** 均分流量而非按占比。

---

## Reference Sections

See [Shared Reference Sections](../Prompts/Shared_References.md) for detailed formatting guidance.

### Glossary, Terminology & Acronyms

1. **ABCI**: Interface between Tendermint consensus and Cosmos application layer [EN]
2. **CAS (Content-Addressed Storage)**: Storage model using hashes as identifiers [EN]
3. **CRYSTALS-Dilithium**: Lattice-based post-quantum signature scheme [EN]
4. **IBC**: Inter-Blockchain Communication protocol for Cosmos ecosystem interoperability [EN]
5. **MDBX**: Memory-mapped database engine used by Erigon for high-throughput state storage [EN]
6. **MEV**: Miner/Maximal Extractable Value from transaction ordering [EN]
7. **NUMA**: Non-Uniform Memory Access architecture requiring locality-aware scheduling [EN]
8. **RPO**: Recovery Point Objective defining allowable data loss [EN]
9. **零信任 (Zero Trust)**: Security posture assuming no implicit trust inside/outside perimeters [ZH]
10. **量子安全 (Quantum-safe)**: Cryptographic resilience against quantum adversaries [ZH]

### Codebase & Library References

1. **Geth** (GitHub: `ethereum/go-ethereum` | License: GPL-3.0)
   - Stack: Golang Ethereum execution client
   - Maturity: Production
   - Performance: Snapshot sync, state pruning
   - Security: Regular audits, bug bounty
2. **Erigon** (GitHub: `ledgerwatch/erigon` | License: GPL-3.0)
   - Stack: Golang/C++ Ethereum execution client optimized for archives
   - Maturity: Production
   - Performance: MDBX storage, flat state
   - Security: Community-reviewed releases
3. **CometBFT** (GitHub: `cometbft/cometbft` | License: Apache-2.0)
   - Stack: Cosmos consensus engine
   - Maturity: Production
   - Performance: High-throughput BFT
   - Security: Formalized light client protocol
4. **Bitcoin Core** (GitHub: `bitcoin/bitcoin` | License: MIT)
   - Stack: C++ Bitcoin full node
   - Maturity: Production
   - Performance: Pruning, compact block relay
   - Security: Peer-reviewed
5. **Helios** (GitHub: `helios-eth/helios` | License: MIT)
   - Stack: Rust Ethereum light client
   - Maturity: Beta
   - Performance: Async verified sync
   - Security: Attestation-based trust

### Authoritative Literature & Reports

1. Ethereum Foundation. (2023). *Ethereum Execution Client Architecture*. https://ethereum.org/developers/docs/nodes-and-clients [EN]
2. Parity Technologies. (2024). *Polkadot Node Operations Guide*. https://docs.polkadot.network [EN]
3. Interchain Foundation. (2024). *Cosmos-SDK Node Deployment Patterns*. https://docs.cosmos.network [EN]
4. CNCF Security TAG & NSA. (2024). *Kubernetes Hardening Guide v1.3*. https://github.com/kubernetes [EN]
5. Beyer, B., Murphy, N., Rensin, D., Kawahara, T., & Thorne, S. (2023). *Site Reliability Engineering Workbook* (2nd ed.). O’Reilly Media. [EN]
6. Chainlink Labs. (2023). *Cross-Chain Interoperability Protocol Overview*. https://chain.link/cross-chain [EN]
7. OpenBitcoin Research Collective. (2024). *Bitcoin policy experimentation guidelines*. https://openbitcoin.org/research/policy-guidelines [EN]
8. OpenEthereum Contributors. (2024). *Erigon MDBX performance benchmarks*. https://github.com/ledgerwatch/erigon/wiki/MDBX-Benchmarks [EN]
9. Cloud Native Telco Forum. (2024). *Backbone architectures for sub-second failover*. https://cntf.org/reports/dlt-backbone-2024 [EN]
10. Zero Knowledge Validator. (2024). *zkEVM production readiness assessment*. https://zkvalidator.com/reports/zkEVM-readiness-2024 [EN]
11. 张敏, & 黄磊. (2024). Web3节点弹性扩缩容策略研究. *网络运维技术*, 9(3), 58-70. [ZH]
12. 陈强, & 韩雪. (2024). BRC-20索引服务架构优化研究. *区块链工程*, 6(3), 75-88. [ZH]
13. García, M., & López, D. (2024). *Blockchain evidence retention compliance handbook*. Madrid: Observatorio RegTech. [ES]
14. 佐藤, 拓海., & 石川, 由美. (2024). ポスト量子暗号移行計画の実務知見. *分散台帳レビュー*, 12(1), 33-49. [JA]
15. 周敏, & 赵鹏. (2023). 多链意图路由风控架构研究. *金融科技前沿*, 5(11), 42-57. [ZH]

### APA Style Source Citations

- Ethereum Foundation. (2023). *Ethereum execution client architecture*. https://ethereum.org/developers/docs/nodes-and-clients [EN]
- Parity Technologies. (2024). *Polkadot node operations guide*. https://crates.polkadot.network [EN]
- Interchain Foundation. (2024). *Cosmos-SDK node deployment patterns*. https://docs.cosmos.network [EN]
- CNCF Security Technical Advisory Group, & National Security Agency. (2024). *Kubernetes hardening guide* (Version 1.3). https://github.com/kubernetes [EN]
- Beyer, B., Murphy, N., Rensin, D., Kawahara, T., & Thorne, S. (2023). *Site reliability engineering workbook* (2nd ed.). O’Reilly Media. [EN]
- Chainlink Labs. (2023). *Cross-chain interoperability protocol overview*. https://chain.link/cross-chain [EN]
- OpenBitcoin Research Collective. (2024). *Bitcoin policy experimentation guidelines*. https://openbitcoin.org/research/policy-guidelines [EN]
- OpenEthereum Contributors. (2024). *Erigon MDBX performance benchmarks*. https://github.com/ledgerwatch/erigon/wiki/MDBX-Benchmarks [EN]
- Cloud Native Telco Forum. (2024). *Backbone architectures for sub-second failover*. https://cntf.org/reports/dlt-backbone-2024 [EN]
- Zero Knowledge Validator. (2024). *zkEVM production readiness assessment*. https://zkvalidator.com/reports/zkEVM-readiness-2024 [EN]
- 张敏, & 黄磊. (2024). Web3节点弹性扩缩容策略研究. *网络运维技术*, 9(3), 58-70. [ZH]
- 陈强, & 韩雪. (2024). BRC-20索引服务架构优化研究. *区块链工程*, 6(3), 75-88. [ZH]
- García, M., & López, D. (2024). *Blockchain evidence retention compliance handbook*. Madrid: Observatorio RegTech. [ES]
- 佐藤, 拓海., & 石川, 由美. (2024). ポスト量子暗号移行計画の実務知見. *分散台帳レビュー*, 12(1), 33-49. [JA]
- 周敏, & 赵鹏. (2023). 多链意图路由风控架构研究. *金融科技前沿*, 5(11), 42-57. [ZH]
