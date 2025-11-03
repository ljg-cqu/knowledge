# Blockchain Node Developer — True / False (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/True_False.md](../../Prompts/Templates/True_False.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Statement Bank](#statement-bank-statements-1-18)
- [Topic 1: Clients & State](#topic-1-clients--state)
  - [S1: Full vs archive](#s1-full-vs-archive)
- [Topic 2: Networking & Consensus](#topic-2-networking--consensus)
- [Topic 3: Storage & Performance](#topic-3-storage--performance)
- [Topic 4: Operations, HA & Security](#topic-4-operations-ha--security)
- [Reference Sections](#reference-sections)

---

## Statement Bank (Statements 1–18)

### Topic 1: Clients & State

#### S1: Full vs archive

**Difficulty:** Foundational

**Statement:** An Ethereum archive node is required for most production RPC workloads.

**Answer:** B (False)

**Rationale:** Most production needs are served by pruned full nodes plus external indexers; archives are for time-travel state queries and deep forensics.

**Citation:** Ethereum client docs; Erigon design notes [EN]

---

#### S2: Engine API separation

**Difficulty:** Foundational

**Statement:** Post‑Merge Ethereum requires a consensus client and an execution client communicating via the Engine API.

**Answer:** A (True)

**Rationale:** Consensus clients handle fork choice/finality; execution clients handle EVM/state; they interoperate through authenticated Engine API.

**Citation:** Ethereum consensus specs; Engine API repo [EN]

---

#### S3: Cosmos ABCI boundary

**Difficulty:** Foundational

**Statement:** In Cosmos, CometBFT provides consensus/networking and Cosmos SDK provides application logic separated by ABCI.

**Answer:** A (True)

**Rationale:** The ABCI boundary allows modular evolution of app logic and consensus.

**Citation:** Cosmos SDK & CometBFT documentation [EN]

---

#### S4: Geth vs Erigon

**Difficulty:** Intermediate

**Statement:** Erigon’s flat storage and staged sync are optimized for historical queries compared to Geth’s trie-centric reads.

**Answer:** A (True)

**Rationale:** Erigon reduces random IO via flat tables and staged pipelines, improving archive-like queries.

**Citation:** Erigon docs; community benchmarks [EN]

---

#### S5: Bitcoin mempool = consensus

**Difficulty:** Intermediate

**Statement:** Bitcoin Core’s mempool policies are consensus rules and cannot vary across nodes.

**Answer:** B (False)

**Rationale:** Mempool is policy; relay fee, RBF, ancestor/descendant limits vary by node.

**Citation:** Bitcoin Core policy docs [EN]

---

#### S6: RPC trust boundaries

**Difficulty:** Intermediate

**Statement:** Exposing debug/trace RPC methods publicly is acceptable if HTTPS is enabled.

**Answer:** B (False)

**Rationale:** Debug/trace/admin expand attack surface; enforce allowlists, authN/Z, and isolation.

**Citation:** Client security hardening guides [EN]

---

#### S7: Pruning and security

**Difficulty:** Intermediate

**Statement:** Enabling state pruning weakens consensus security.

**Answer:** B (False)

**Rationale:** Pruning affects storage/queries, not consensus correctness; state root commitments remain.

**Citation:** Ethereum client pruning docs [EN]

---

### Topic 2: Networking & Consensus

#### S8: GossipSub scoring

**Difficulty:** Foundational

**Statement:** libp2p GossipSub scoring helps resist spam and eclipse by penalizing low‑quality peers.

**Answer:** A (True)

**Rationale:** Per‑topic scoring and decay improve mesh health under adversarial conditions.

**Citation:** libp2p GossipSub spec [EN]

---

#### S9: PoW finality

**Difficulty:** Intermediate

**Statement:** Proof‑of‑Work provides absolute finality after six confirmations.

**Answer:** B (False)

**Rationale:** PoW finality is probabilistic; deeper confirmations reduce but don’t eliminate reorg risk.

**Citation:** Bitcoin white paper; consensus analyses [EN]

---

#### S10: PoS stall

**Difficulty:** Intermediate

**Statement:** PoS chains with finality gadgets can stall finality under low validator participation.

**Answer:** A (True)

**Rationale:** If participation drops below thresholds, checkpoints may not finalize despite liveness at head.

**Citation:** Ethereum consensus specs (Casper FFG) [EN]

---

#### S11: LMD‑GHOST + FFG

**Difficulty:** Advanced

**Statement:** Ethereum uses LMD‑GHOST for head selection and Casper FFG for finality.

**Answer:** A (True)

**Rationale:** Combined fork choice delivers responsiveness with accountable finality.

**Citation:** Ethereum consensus specs [EN]

---

#### S12: Light clients

**Difficulty:** Advanced

**Statement:** Light clients verify full state and receipts for every block.

**Answer:** B (False)

**Rationale:** Light clients verify headers and selective proofs, not full state.

**Citation:** Light client specifications [EN]

---

### Topic 3: Storage & Performance

#### S13: DB defaults suffice

**Difficulty:** Foundational

**Statement:** Default LevelDB/RocksDB settings are usually optimal for node workloads.

**Answer:** B (False)

**Rationale:** Compaction, cache, and WAL settings require tuning to avoid stalls and high write amplification.

**Citation:** RocksDB tuning guides; client docs [EN]

---

#### S14: Snapshot sync safety

**Difficulty:** Intermediate

**Statement:** Snapshot‑based fast sync is unsafe and should never be used in production.

**Answer:** B (False)

**Rationale:** Snapshots are acceptable when verified (root/hash/signature) and sourced from trusted pipelines.

**Citation:** Geth snap sync docs; Erigon staged sync docs [EN]

---

#### S15: Flat storage trade‑offs

**Difficulty:** Intermediate

**Statement:** Flat storage eliminates the need to reconcile with trie commitments.

**Answer:** B (False)

**Rationale:** Flat tables must be reconciled to canonical trie roots to preserve provability.

**Citation:** Erigon design notes [EN]

---

### Topic 4: Operations, HA & Security

#### S16: Validator isolation

**Difficulty:** Foundational

**Statement:** Validators should not be colocated with public RPC gateways on the same host.

**Answer:** A (True)

**Rationale:** Separation reduces attack surface and noisy‑neighbor risks.

**Citation:** Operator best practices [EN]

---

#### S17: Blue/green forks

**Difficulty:** Intermediate

**Statement:** In‑place client upgrades during hard forks are preferred over blue/green cutovers.

**Answer:** B (False)

**Rationale:** Blue/green reduces blast radius and enables rollback during activation.

**Citation:** Ops playbooks; client release guidance [EN]

---

#### S18: IOPS vs throughput

**Difficulty:** Advanced

**Statement:** High sequential MB/s is the primary driver of node performance; IOPS and latency outliers matter less.

**Answer:** B (False)

**Rationale:** Node workloads are dominated by small random reads/writes; p99 latency and provisioned IOPS dominate SLOs.

**Citation:** Production benchmarking reports [EN]

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md) for formatting. This note reuses the reference set from `QA_GPT-5.md` to avoid duplication. Exception handling: Floors centralized; per‑file shortfall documented here and satisfied across the interview pack.
