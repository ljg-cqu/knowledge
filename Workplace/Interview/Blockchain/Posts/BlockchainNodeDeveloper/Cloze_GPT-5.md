# Blockchain Node Developer — Cloze / Fill-in-the-Blank (GPT-5)

See [../../Prompts/Requirements.md](../../Prompts/Requirements.md) and [../../Prompts/Templates/Cloze.md](../../Prompts/Templates/Cloze.md). Role context from [Job_Description.md](Job_Description.md).

## Contents

- [Item Bank](#item-bank-items-1-24)
- [Topic 1: Clients & Internals](#topic-1-clients--internals)
- [Topic 2: Networking & Consensus](#topic-2-networking--consensus)
- [Topic 3: Storage & State](#topic-3-storage--state)
- [Topic 4: Operations & Security](#topic-4-operations--security)
- [Reference Sections](#reference-sections)

---

## Item Bank (Items 1–24)

### Topic 1: Clients & Internals

#### Item 1: Post‑Merge split

**Difficulty:** Foundational

**Statement:** Ethereum’s execution and consensus clients communicate via the ___ API secured by ___.

**Acceptable Answers:** ["Engine", "Engine API"]; ["JWT", "JSON Web Token"]

**Grading:** Both blanks required | **Common incorrect:** TLS only

**Rationale:** Engine API with JWT auth.

---

#### Item 2: Client roles

**Difficulty:** Foundational

**Statement:** The execution client runs the ___ and manages ___, while the consensus client handles ___ and ___.

**Acceptable Answers:** ["EVM"], ["state", "transaction state"], ["fork choice", "head selection"], ["finality", "attestations"]

**Grading:** All four concepts present.

**Rationale:** Role separation.

---

#### Item 3: Cosmos boundary

**Difficulty:** Foundational

**Statement:** In Cosmos, the Application Blockchain Interface is abbreviated as ___ and separates ___ from ___.

**Acceptable Answers:** ["ABCI"], ["application logic", "app"], ["consensus", "networking", "CometBFT"]

**Grading:** Correct mapping.

**Rationale:** ABCI boundary.

---

#### Item 4: Archive purpose

**Difficulty:** Foundational

**Statement:** An archive node is primarily used for ___ queries across historical ___.

**Acceptable Answers:** ["time‑travel", "historical state"], ["blocks", "heights"]

**Grading:** Both blanks required.

**Rationale:** Deep historical access.

---

#### Item 5: Erigon emphasis

**Difficulty:** Intermediate

**Statement:** Erigon’s ___ storage reduces random IO by storing direct key→value mappings, later reconciled to the ___.

**Acceptable Answers:** ["flat"], ["trie", "Merkle‑Patricia trie", "MPT"]

**Grading:** Both terms.

**Rationale:** Flat vs trie.

---

#### Item 6: Tracing

**Difficulty:** Intermediate

**Statement:** Historical transaction tracing at scale benefits from ___ snapshots and staged ___.

**Acceptable Answers:** ["state", "archive"], ["sync", "pipelines"]

**Grading:** Reasonable variants.

**Rationale:** Erigon/Geth features.

---

### Topic 2: Networking & Consensus

#### Item 7: Gossip protocol

**Difficulty:** Foundational

**Statement:** Ethereum’s beacon chain uses libp2p ___ with per‑topic ___ to manage peer quality.

**Acceptable Answers:** ["GossipSub", "gossipsub"], ["scoring", "peer scoring"]

**Grading:** Both blanks.

**Rationale:** Gossip + scoring.

---

#### Item 8: Fork choice

**Difficulty:** Intermediate

**Statement:** The head is chosen by ___‑GHOST while finality is provided by ___ FFG.

**Acceptable Answers:** ["LMD"], ["Casper", "Casper FFG"]

**Grading:** Two correct mechanisms.

**Rationale:** Ethereum fork choice.

---

#### Item 9: Finality stall

**Difficulty:** Intermediate

**Statement:** Finality can stall when validator ___ drops below threshold; monitor head–___ distance.

**Acceptable Answers:** ["participation", "inclusion"], ["finalized", "finality"]

**Grading:** Both blanks.

**Rationale:** Operational indicator.

---

#### Item 10: Light clients

**Difficulty:** Intermediate

**Statement:** Light clients verify block ___ and ___ proofs rather than full state.

**Acceptable Answers:** ["headers"], ["Merkle", "SSZ", "witness"]

**Grading:** Both concepts.

**Rationale:** Header + proof.

---

#### Item 11: Bitcoin policy

**Difficulty:** Foundational

**Statement:** Replace‑by‑fee (RBF) is a mempool ___, not a consensus ___.

**Acceptable Answers:** ["policy"], ["rule"]

**Grading:** Correct distinction.

**Rationale:** Policy vs consensus.

---

#### Item 12: DoS controls

**Difficulty:** Intermediate

**Statement:** Effective P2P DoS mitigation includes message ___ caps and connection ___.

**Acceptable Answers:** ["size", "payload"], ["gating", "limits", "filtering"]

**Grading:** Both present.

**Rationale:** Practical controls.

---

### Topic 3: Storage & State

#### Item 13: Trie purpose

**Difficulty:** Foundational

**Statement:** A Merkle‑Patricia trie provides authenticated ___ of the global ___.

**Acceptable Answers:** ["commitments", "roots"], ["state"]

**Grading:** Either "roots" or "commitments" for the first blank.

**Rationale:** Commitments to state.

---

#### Item 14: RocksDB knobs

**Difficulty:** Intermediate

**Statement:** Two critical RocksDB tuning areas for nodes are ___ strategy and block ___ size.

**Acceptable Answers:** ["compaction"], ["cache"]

**Grading:** Both terms.

**Rationale:** Compaction + cache.

---

#### Item 15: Bloom filters

**Difficulty:** Intermediate

**Statement:** Bloom filters accelerate negative lookups by using ___ bits and multiple ___ functions.

**Acceptable Answers:** ["bitmap", "bit array"], ["hash"]

**Grading:** Concepts present.

**Rationale:** Bloom basics.

---

#### Item 16: Snapshot integrity

**Difficulty:** Intermediate

**Statement:** Before serving from a snapshot, verify the state root ___ and source ___.

**Acceptable Answers:** ["hash", "root"], ["signature", "provenance"]

**Grading:** Both present.

**Rationale:** Safety checks.

---

#### Item 17: Flat vs trie

**Difficulty:** Intermediate

**Statement:** Flat storage favors ___ scans and point ___, while tries favor native ___ generation.

**Acceptable Answers:** ["sequential", "range"], ["lookups"], ["proof"]

**Grading:** All three concepts.

**Rationale:** Performance trade‑offs.

---

#### Item 18: Disk choices

**Difficulty:** Foundational

**Statement:** For hot node databases, local ___ typically provide lower p99 latency than networked SSDs.

**Acceptable Answers:** ["NVMe", "NVMe SSDs"]

**Grading:** Accept NVMe variants.

**Rationale:** Latency/jitter.

---

### Topic 4: Operations & Security

#### Item 19: Validator isolation

**Difficulty:** Foundational

**Statement:** Validators should be ___ from public RPC to reduce attack surface.

**Acceptable Answers:** ["isolated", "segregated", "separated"]

**Grading:** Concept.

**Rationale:** Defense‑in‑depth.

---

#### Item 20: RPC allowlists

**Difficulty:** Intermediate

**Statement:** Public RPC must enforce method ___ and per‑tenant ___.

**Acceptable Answers:** ["allowlists", "whitelists"], ["quotas", "rate limits"]

**Grading:** Both controls.

**Rationale:** Safety controls.

---

#### Item 21: getLogs control

**Difficulty:** Intermediate

**Statement:** To control eth_getLogs cost, enforce bounded block‑range windows and ___.

**Acceptable Answers:** ["pagination", "page limits"]

**Grading:** Correct technique.

**Rationale:** Guardrails.

---

#### Item 22: JWT handling

**Difficulty:** Foundational

**Statement:** Engine API secrets should be ___ regularly and stored ___.

**Acceptable Answers:** ["rotated"], ["securely", "in a secret store", "encrypted"]

**Grading:** Both actions.

**Rationale:** Secret hygiene.

---

#### Item 23: SLO design

**Difficulty:** Intermediate

**Statement:** Define SLOs per method family and tie rollout velocity to error budget ___.

**Acceptable Answers:** ["burn", "consumption"]

**Grading:** Correct concept.

**Rationale:** SRE practice.

---

#### Item 24: Blue/green

**Difficulty:** Intermediate

**Statement:** During fork activation, promote pre‑synced ___ nodes and drain ___ nodes.

**Acceptable Answers:** ["green"], ["blue"]

**Grading:** Both required.

**Rationale:** Safe cutover.

---

## Reference Sections

See [../../Prompts/Shared_References.md](../../Prompts/Shared_References.md). This note reuses shared references from `QA_GPT-5.md`; floors are satisfied across the pack.
