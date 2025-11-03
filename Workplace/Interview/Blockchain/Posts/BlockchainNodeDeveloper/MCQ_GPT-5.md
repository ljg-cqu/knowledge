# Blockchain Node Developer — Multiple-Choice (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/MCQ.md](../../Prompts/Templates/MCQ.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Question Bank](#question-bank-questions-1-40)
- [Topic 1: Clients & Protocol Internals](#topic-1-clients--protocol-internals)
- [Topic 2: Networking & Consensus](#topic-2-networking--consensus)
- [Topic 3: Storage & Performance](#topic-3-storage--performance)
- [Topic 4: Operations, HA & Security](#topic-4-operations-ha--security)
- [Reference Sections](#reference-sections)

---

## Question Bank (Questions 1–40)

### Topic 1: Clients & Protocol Internals

#### Q1: Execution vs consensus clients

**Language:** N/A | **Difficulty:** Foundational

Which statement best describes Ethereum’s client split post‑Merge?

- A. Execution clients handle fork choice; consensus clients execute transactions.
- B. Execution clients handle EVM/state; consensus clients handle fork choice/finality.
- C. Both client types handle the EVM; redundancy improves security.
- D. Consensus clients expose JSON‑RPC; execution clients run validators.

**Answer:** B

**Rationale:** Execution = EVM/state; Consensus = fork choice/finality; they communicate via Engine API.

**Distractor notes:** A/D invert roles; C is incorrect redundancy claim.

---

#### Q2: Engine API

**Language:** N/A | **Difficulty:** Foundational

What secures the Engine API channel between clients?

- A. TLS with self‑signed certs only
- B. JWT‑based authentication
- C. IP whitelisting exclusively
- D. Passphrase‑based HTTP Basic auth

**Answer:** B

**Rationale:** Engine API uses JWT secrets; versions must be compatible per matrices.

**Distractor notes:** A/C/D are insufficient or non‑standard for Engine API.

---

#### Q3: Geth vs Erigon focus

**Language:** N/A | **Difficulty:** Intermediate

Erigon’s architecture primarily optimizes for:

- A. Validator performance at low RAM
- B. Historical queries and lower IO amplification
- C. GPU‑accelerated EVM execution
- D. Smaller genesis state size

**Answer:** B

**Rationale:** Flat storage + staged pipelines improve historical scans and reduce random IO.

**Distractor notes:** A/C/D are unrelated.

---

#### Q4: Bitcoin RBF

**Language:** N/A | **Difficulty:** Intermediate

Replace‑by‑fee (RBF) is:

- A. A consensus rule enforced by all miners
- B. A node policy affecting mempool replacement
- C. A wallet‑only feature with no node impact
- D. Deprecated since Taproot

**Answer:** B

**Rationale:** RBF is mempool policy; not consensus.

**Distractor notes:** A/D are false; C ignores node behavior.

---

#### Q5: Cosmos ABCI

**Language:** N/A | **Difficulty:** Foundational

ABCI exists to:

- A. Embed EVM into Cosmos SDK
- B. Separate consensus/networking from application logic
- C. Provide cross‑chain RPC access
- D. Replace IAVL with SMT

**Answer:** B

**Rationale:** ABCI boundary enables modularity between CometBFT and app logic.

**Distractor notes:** A/C/D are unrelated.

---

#### Q6: RPC exposure

**Language:** N/A | **Difficulty:** Intermediate

Public RPC endpoints should:

- A. Allow debug/trace for transparency
- B. Use method allowlists and rate limits
- C. Share hosts with validator clients
- D. Run with default client configs

**Answer:** B

**Rationale:** Whitelisting + quotas mitigate abuse; validators must be isolated.

**Distractor notes:** A/C/D violate security best practices.

---

#### Q7: State trie

**Language:** N/A | **Difficulty:** Intermediate

Merkle‑Patricia tries primarily provide:

- A. Faster sequential reads
- B. Authenticated state commitments
- C. Lower disk footprint than flat tables
- D. Built‑in compression

**Answer:** B

**Rationale:** Tries commit to state roots for proofability; not IO performance.

**Distractor notes:** A/C/D are incorrect.

---

#### Q8: Archive necessity

**Language:** N/A | **Difficulty:** Foundational

Archive nodes are typically required for:

- A. Basic balances and event queries
- B. Validator operations
- C. Forensics and time‑travel state queries
- D. Mempool fee estimation

**Answer:** C

**Rationale:** Deep historical state access needs archives; others use full nodes + indexers.

**Distractor notes:** A/B/D don’t require archives.

---

#### Q9: Ethereum tracing

**Language:** N/A | **Difficulty:** Intermediate

Which client often excels at historical traces and archive‑like queries?

- A. Geth
- B. Erigon
- C. Besu
- D. Nethermind

**Answer:** B

**Rationale:** Erigon’s pipelines and flat storage aid traces.

**Distractor notes:** A/C/D are fine clients but not as focused on archive scans.

---

#### Q10: Client diversity

**Language:** N/A | **Difficulty:** Intermediate

Client diversity matters because:

- A. It guarantees 100% uptime
- B. It increases feature velocity
- C. It reduces correlated failure risk
- D. It eliminates the need for testing

**Answer:** C

**Rationale:** Diverse implementations mitigate systemic bugs.

**Distractor notes:** A/B/D are exaggerated or false.

---

### Topic 2: Networking & Consensus

#### Q11: Gossip mesh health

**Language:** N/A | **Difficulty:** Foundational

A sudden rise in prune events suggests:

- A. Healthy mesh stabilization
- B. Possible DoS or poor peer quality
- C. Underutilized bandwidth
- D. Correct JWT rotation

**Answer:** B

**Rationale:** Excess prunes indicate spam or scoring issues.

**Distractor notes:** A/C/D are unrelated.

---

#### Q12: PoW confirmations

**Language:** N/A | **Difficulty:** Foundational

More confirmations in PoW primarily:

- A. Reduce reorg probability
- B. Increase block size
- C. Speed up finality
- D. Slash dishonest miners

**Answer:** A

**Rationale:** Deeper depth lowers double‑spend risk.

**Distractor notes:** B/C/D incorrect.

---

#### Q13: Finality stall metric

**Language:** N/A | **Difficulty:** Intermediate

Finality health in Ethereum is best monitored via:

- A. Mempool size
- B. Head block time
- C. Head–finalized slot distance and participation
- D. Peer count

**Answer:** C

**Rationale:** Distance + attestation participation tracks finality.

**Distractor notes:** A/B/D are indirect.

---

#### Q14: Cosmos Proofs

**Language:** N/A | **Difficulty:** Intermediate

IAVL vs SMT key trade‑off:

- A. IAVL always smaller proofs
- B. SMT supports fixed‑depth proofs, better parallelism
- C. IAVL enables light client proofs; SMT cannot
- D. Both are identical in practice

**Answer:** B

**Rationale:** SMT offers fixed‑depth and parallel updates at storage overhead cost.

**Distractor notes:** A/C/D incorrect.

---

#### Q15: Light client anchors

**Language:** N/A | **Difficulty:** Advanced

Light client trust may be anchored in:

- A. Checkpoint sync or committee signatures
- B. Full state download
- C. RPC provider IP allowlisting
- D. Mempool snapshots

**Answer:** A

**Rationale:** Anchors include genesis/checkpoints/sync committees.

**Distractor notes:** B/C/D incorrect.

---

#### Q16: DoS hardening

**Language:** N/A | **Difficulty:** Intermediate

Effective P2P hardening includes:

- A. Unlimited peer counts
- B. Message size caps and connection gating
- C. Disabling encryption for speed
- D. Single region seed nodes

**Answer:** B

**Rationale:** Caps + gating + regional diversity reduce abuse.

**Distractor notes:** A/C/D are anti‑patterns.

---

### Topic 3: Storage & Performance

#### Q17: RocksDB compaction

**Language:** N/A | **Difficulty:** Intermediate

Universal compaction typically trades:

- A. Higher write amp for lower read amp on large files
- B. Lower write amp for higher read amp
- C. No trade‑off; defaults are optimal
- D. Only affects LevelDB, not RocksDB

**Answer:** B

**Rationale:** Universal reduces write amp; may raise read amp depending on workload.

**Distractor notes:** A/C/D incorrect.

---

#### Q18: Block cache sizing

**Language:** N/A | **Difficulty:** Foundational

A primary benefit of a larger block cache is:

- A. Faster compactions
- B. Hot‑set reads from memory
- C. Smaller SSTables
- D. Zero write amplification

**Answer:** B

**Rationale:** Cache improves hit rate for hot data.

**Distractor notes:** A/C/D incorrect.

---

#### Q19: Snapshot verification

**Language:** N/A | **Difficulty:** Intermediate

When restoring snapshots you should first:

- A. Disable fsync to speed restore
- B. Verify root/state hash and signature
- C. Change chain ID
- D. Increase peer counts

**Answer:** B

**Rationale:** Integrity verification prevents poisoned snapshots.

**Distractor notes:** A/C/D irrelevant or dangerous.

---

#### Q20: NVMe vs network SSD

**Language:** N/A | **Difficulty:** Intermediate

Networked SSDs usually introduce:

- A. Lower latency p99
- B. Higher jitter and noisy neighbor risk
- C. Higher local durability during host failure
- D. Unlimited IOPS without cost

**Answer:** B

**Rationale:** Network storage can add jitter; provisioned IOPS helps but costs.

**Distractor notes:** A/C/D incorrect.

---

#### Q21: WAL fsync

**Language:** N/A | **Difficulty:** Advanced

Disabling WAL fsync generally:

- A. Improves durability
- B. Reduces latency at the risk of data loss on crash
- C. Has no effect
- D. Only affects read‑only workloads

**Answer:** B

**Rationale:** Less fsync → lower latency but weaker crash safety.

**Distractor notes:** A/C/D false.

---

#### Q22: Flat vs trie reads

**Language:** N/A | **Difficulty:** Intermediate

Flat storage excels at:

- A. Proof generation without reconciliation
- B. Sequential scans and point lookups
- C. Compressing witnesses on chain
- D. Reducing chain head time

**Answer:** B

**Rationale:** Flat tables avoid path walks for typical reads.

**Distractor notes:** A/C/D incorrect.

---

### Topic 4: Operations, HA & Security

#### Q23: HA RPC topology

**Language:** N/A | **Difficulty:** Foundational

A robust RPC tier should:

- A. Route all requests to a single archive node
- B. Mix heterogeneous nodes behind a smart gateway
- C. Depend solely on caching layers
- D. Co‑locate validators for lower latency

**Answer:** B

**Rationale:** Heterogeneity reduces hot‑spotting and correlated failures.

**Distractor notes:** A/C/D are anti‑patterns.

---

#### Q24: Blue/green upgrades

**Language:** N/A | **Difficulty:** Intermediate

During a hard fork cutover you should:

- A. Upgrade in place across the fleet
- B. Promote pre‑synced green nodes and drain blue
- C. Change chain ID to avoid collisions
- D. Disable health checks temporarily

**Answer:** B

**Rationale:** Blue/green minimizes downtime and enables rollback.

**Distractor notes:** A/C/D incorrect.

---

#### Q25: RPC multi‑tenancy

**Language:** N/A | **Difficulty:** Intermediate

A key control for multi‑tenant RPC is:

- A. Per‑tenant allowlists and quotas
- B. Shared global rate limits
- C. Disabling auth for speed
- D. Debug enabled for premium tenants

**Answer:** A

**Rationale:** Isolation via allowlists/quotas prevents abuse and cross‑impact.

**Distractor notes:** B/C/D unsafe.

---

#### Q26: SLOs

**Language:** N/A | **Difficulty:** Intermediate

Which SLO is most realistic in‑region for eth_call/getBalance?

- A. p99 < 50 ms
- B. p99 < 250 ms
- C. p99 < 5 s
- D. No latency SLO required

**Answer:** B

**Rationale:** p99 < 250 ms is a common attainable target.

**Distractor notes:** A too aggressive; C/D poor practice.

---

#### Q27: Reorg response

**Language:** N/A | **Difficulty:** Advanced

First action during a deep reorg event:

- A. Accelerate writes to indexers
- B. Freeze stateful ops and raise confirmations
- C. Force‑kill peers
- D. Rotate JWTs

**Answer:** B

**Rationale:** Protect integrity before recovery/replay.

**Distractor notes:** A/C/D are not first actions.

---

#### Q28: Cost controls

**Language:** N/A | **Difficulty:** Intermediate

A strong cost lever without reliability loss:

- A. Replace NVMe with HDD
- B. Cache hot reads and split heavy traces to dedicated nodes
- C. Turn off snapshots
- D. Scale to zero nodes at night

**Answer:** B

**Rationale:** Caching and workload separation reduce IOPS on hot path.

**Distractor notes:** A/C/D harmful.

---

#### Q29: Kubernetes QoS

**Language:** N/A | **Difficulty:** Intermediate

For critical nodes in Kubernetes, prefer:

- A. BestEffort QoS
- B. Guaranteed QoS with requests=limits
- C. Burstable QoS without limits
- D. Pods with no resource specs

**Answer:** B

**Rationale:** Guaranteed reduces eviction and throttling risks.

**Distractor notes:** A/C/D unsafe for critical paths.

---

#### Q30: Host networking

**Language:** N/A | **Difficulty:** Intermediate

Host networking for node pods:

- A. Reduces latency but removes some isolation
- B. Increases latency and isolation
- C. Has no measurable effect
- D. Disables libp2p

**Answer:** A

**Rationale:** Host net cuts overlay overhead; weighs against isolation needs.

**Distractor notes:** B/C/D incorrect.

---

#### Q31: Go routine leaks

**Language:** go | **Difficulty:** Intermediate

Which Go pattern helps prevent goroutine leaks in long‑lived services?

- A. Spawning goroutines without context
- B. Using context cancellation and select with timeouts
- C. Panicking on slow paths
- D. Busy‑waiting on channels

**Answer:** B

**Rationale:** Contexts + timeouts and proper channel usage prevent leaks.

**Distractor notes:** A/C/D are anti‑patterns.

---

#### Q32: Rust async

**Language:** rust | **Difficulty:** Intermediate

In Rust async services, a common pitfall is:

- A. Using Send/Sync bounds
- B. Blocking in async tasks, causing executor stalls
- C. Using structured concurrency
- D. Leveraging tokio timeouts

**Answer:** B

**Rationale:** Blocking in async shuts down the reactor; use spawn_blocking or move to threads.

**Distractor notes:** A/C/D are positive practices.

---

#### Q33: Docker storage

**Language:** N/A | **Difficulty:** Intermediate

Best practice for node DB volumes:

- A. Ephemeral container filesystem
- B. Dedicated NVMe with noatime
- C. Shared NFS across all nodes
- D. tmpfs for speed

**Answer:** B

**Rationale:** Dedicated fast disks with proper mount options stabilize p99.

**Distractor notes:** A/C/D unsafe or ephemeral.

---

#### Q34: JWT handling

**Language:** N/A | **Difficulty:** Foundational

Engine API JWT secrets should be:

- A. Committed to git for portability
- B. Rotated and stored securely
- C. Shared via environment in public pods
- D. Hard‑coded in systemd files

**Answer:** B

**Rationale:** Secrets must be rotated and protected.

**Distractor notes:** A/C/D are anti‑patterns.

---

#### Q35: getLogs abuse

**Language:** N/A | **Difficulty:** Intermediate

To prevent expensive eth_getLogs abuse:

- A. Disable logs entirely
- B. Enforce bounded block ranges and pagination
- C. Allow unbounded with higher rate limits
- D. Mirror to a public provider

**Answer:** B

**Rationale:** Bound windows and paginate to contain cost.

**Distractor notes:** A/C/D not practical.

---

#### Q36: Indexer reorg safety

**Language:** N/A | **Difficulty:** Intermediate

Reorg‑safe indexing often uses:

- A. Non‑idempotent inserts
- B. Upserts keyed by (block_hash, tx_hash) and rollback
- C. Random primary keys
- D. Fulltext indexes only

**Answer:** B

**Rationale:** Hash‑keyed upserts enable deterministic replay on reorgs.

**Distractor notes:** A/C/D insufficient.

---

#### Q37: Pebble vs RocksDB

**Language:** N/A | **Difficulty:** Intermediate

Pebble is attractive for Go services because:

- A. It’s a direct drop‑in for Redis
- B. It offers RocksDB‑like features with Go integration
- C. It uses zero memory
- D. It replaces the need for snapshots

**Answer:** B

**Rationale:** Pebble brings RocksDB capabilities into Go with first‑class support.

**Distractor notes:** A/C/D false.

---

#### Q38: Docker CPU scaling

**Language:** N/A | **Difficulty:** Intermediate

Disabling CPU frequency scaling on hosts:

- A. Reduces latency jitter for sensitive stages
- B. Increases energy efficiency without downsides
- C. Has no effect on p99
- D. Breaks libp2p

**Answer:** A

**Rationale:** Fixed clocks reduce jitter for IO‑sensitive workloads.

**Distractor notes:** B/C/D incorrect.

---

#### Q39: Besu GC

**Language:** N/A | **Difficulty:** Advanced

For Besu, GC tuning often focuses on:

- A. Mark‑Sweep‑Compact only
- B. G1/ZGC settings, heap sizing, direct buffers
- C. Disabling GC
- D. Using swap to extend heap

**Answer:** B

**Rationale:** Proper GC and heap tuning stabilizes long‑running JVM clients.

**Distractor notes:** A/C/D incorrect.

---

#### Q40: Error budgets

**Language:** N/A | **Difficulty:** Intermediate

Error budgets should:

- A. Be ignored during peak traffic
- B. Govern rollout velocity when burn increases
- C. Be set to zero for strictness
- D. Replace capacity planning

**Answer:** B

**Rationale:** Budgets tie reliability to change management.

**Distractor notes:** A/C/D misuses.

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md) for formatting. This note reuses the reference set from `QA_GPT-5.md` to avoid duplication. Exception handling: Floors centralized; per‑file shortfall documented here and satisfied across the interview pack.
