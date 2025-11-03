# Blockchain Node Developer — True/False Statements (GPT-5)

## Contents

- [Statement Bank](#statement-bank-statements-1–24)
- [Topic 1: Clients & Languages](#topic-1-clients--languages)
	- [S1: Geth language](#s1-geth-language)
	- [S2: Bitcoin Core RPC](#s2-bitcoin-core-rpc)
	- [S3: Cosmos SDK modules](#s3-cosmos-sdk-modules)
	- [S4: Docker privilege](#s4-docker-privilege)
	- [S5: StatefulSets for nodes](#s5-statefulsets-for-nodes)
- [Topic 2: State, Sync & Data](#topic-2-state-sync--data)
	- [S6: Historical state needs archive](#s6-historical-state-needs-archive)
	- [S7: Bitcoin mempool persistence](#s7-bitcoin-mempool-persistence)
	- [S8: Snap sync vs full state](#s8-snap-sync-vs-full-state)
	- [S9: txindex for Bitcoin queries](#s9-txindex-for-bitcoin-queries)
	- [S10: Pruning with txindex](#s10-pruning-with-txindex)
- [Topic 3: Consensus & Networking](#topic-3-consensus--networking)
	- [S11: Tendermint finality](#s11-tendermint-finality)
	- [S12: Devp2p on execution layer](#s12-devp2p-on-execution-layer)
	- [S13: Probabilistic finality (BTC)](#s13-probabilistic-finality-btc)
	- [S14: ABCI role](#s14-abci-role)
	- [S15: App hash consistency](#s15-app-hash-consistency)
- [Topic 4: RPC & API Surface](#topic-4-rpc--api-surface)
	- [S16: Add custom RPC in Geth](#s16-add-custom-rpc-in-geth)
	- [S17: eth_call state override](#s17-eth_call-state-override)
	- [S18: Cosmos gRPC vs Tendermint RPC](#s18-cosmos-grpc-vs-tendermint-rpc)
	- [S19: WebSocket vs filters](#s19-websocket-vs-filters)
- [Topic 5: Ops, HA & Kubernetes](#topic-5-ops-ha--kubernetes)
	- [S20: Liveness probes & reorgs](#s20-liveness-probes--reorgs)
	- [S21: Headless service + StatefulSet](#s21-headless-service--statefulset)
	- [S22: HPA for read scaling](#s22-hpa-for-read-scaling)
	- [S23: PVC access modes](#s23-pvc-access-modes)
- [Topic 6: Clients & Storage Internals](#topic-6-clients--storage-internals)
	- [S24: Erigon storage layout](#s24-erigon-storage-layout)
- [Reference Sections](#reference-sections)

---

## Statement Bank (Statements 1–24)

### Topic 1: Clients & Languages

#### S1: Geth language

**Difficulty:** Foundational

**Statement:** Geth (go-ethereum) is implemented primarily in Go (Golang).

**Answer:** A (True)

**Rationale:** The official client is written in Go and maintained under the `ethereum/go-ethereum` repository.

**Citation:** https://github.com/ethereum/go-ethereum [EN]

---

#### S2: Bitcoin Core RPC

**Difficulty:** Foundational

**Statement:** Bitcoin Core exposes a JSON-RPC interface over HTTP by default.

**Answer:** A (True)

**Rationale:** Bitcoin Core provides a JSON-RPC server on localhost for node control and wallet operations.

**Citation:** https://bitcoincore.org/en/doc/ [EN]

---

#### S3: Cosmos SDK modules

**Difficulty:** Foundational

**Statement:** Cosmos SDK application modules are written in Go.

**Answer:** A (True)

**Rationale:** The Cosmos SDK is a framework in Go for building application-specific blockchains.

**Citation:** https://github.com/cosmos/cosmos-sdk [EN]

---

#### S4: Docker privilege

**Difficulty:** Foundational

**Statement:** Running blockchain nodes in Docker requires privileged mode.

**Answer:** B (False)

**Rationale:** Most nodes run fine without `--privileged`; only specific capabilities/volumes are typically needed.

**Citation:** https://docs.docker.com/engine/reference/run/ [EN]

---

#### S5: StatefulSets for nodes

**Difficulty:** Foundational

**Statement:** Kubernetes StatefulSets are generally recommended for stateful blockchain nodes.

**Answer:** A (True)

**Rationale:** StatefulSets provide stable identities and persistent storage, fitting stateful workloads like full nodes.

**Citation:** https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ [EN]

---

### Topic 2: State, Sync & Data

#### S6: Historical state needs archive

**Difficulty:** Intermediate

**Statement:** On Geth, querying arbitrary historical account storage requires archive mode.

**Answer:** A (True)

**Rationale:** Pruned nodes don't retain all historical states; archive (`--gcmode=archive`) is required for full history.

**Citation:** https://geth.ethereum.org/docs/fundamentals/data-storage [EN]

---

#### S7: Bitcoin mempool persistence

**Difficulty:** Intermediate

**Statement:** By default, Bitcoin Core does not persist its mempool across restarts.

**Answer:** B (False)

**Rationale:** `-persistmempool` is enabled by default; mempool contents are saved to `mempool.dat` on shutdown.

**Citation:** https://bitcoincore.org/en/doc/25.0.0/rpc/mempool/getmempoolinfo/ [EN]

---

#### S8: Snap sync vs full state

**Difficulty:** Intermediate

**Statement:** Geth's snap sync doesn't download every historical state trie, reducing initial sync time.

**Answer:** A (True)

**Rationale:** Snap sync reconstructs recent state from snapshots and blocks, avoiding full historical state download.

**Citation:** https://geth.ethereum.org/docs/fundamentals/sync-modes [EN]

---

#### S9: txindex for Bitcoin queries

**Difficulty:** Intermediate

**Statement:** To query arbitrary transactions by txid via `getrawtransaction`, Bitcoin Core needs `-txindex`.

**Answer:** A (True)

**Rationale:** Without the transaction index, lookups for non-wallet transactions are limited.

**Citation:** https://bitcoincore.org/en/doc/25.0.0/rpc/rawtransactions/getrawtransaction/ [EN]

---

#### S10: Pruning with txindex

**Difficulty:** Advanced

**Statement:** Bitcoin Core allows `-txindex` when pruning is enabled (`-prune>0`).

**Answer:** B (False)

**Rationale:** Pruned nodes cannot maintain a full transaction index; `-txindex` is incompatible with pruning.

**Citation:** https://bitcoincore.org/en/doc/24.0.0/release-notes/ [EN]

---

### Topic 3: Consensus & Networking

#### S11: Tendermint finality

**Difficulty:** Intermediate

**Statement:** Tendermint/CometBFT achieves instant finality under <1/3 Byzantine faults.

**Answer:** A (True)

**Rationale:** With a supermajority of honest validators, blocks are committed with deterministic finality.

**Citation:** https://tendermint.com/static/docs/tendermint.pdf [EN]

---

#### S12: Devp2p on execution layer

**Difficulty:** Intermediate

**Statement:** Ethereum execution clients use devp2p (RLPx) for peer discovery and block/tx propagation.

**Answer:** A (True)

**Rationale:** Execution layer peers speak devp2p; the consensus (beacon) layer uses libp2p.

**Citation:** https://github.com/ethereum/devp2p [EN]

---

#### S13: Probabilistic finality (BTC)

**Difficulty:** Intermediate

**Statement:** Bitcoin provides probabilistic finality; deeper confirmations reduce reorg risk.

**Answer:** A (True)

**Rationale:** Nakamoto consensus finality increases with the number of blocks built on top of a transaction's block.

**Citation:** https://bitcoin.org/bitcoin.pdf [EN]

---

#### S14: ABCI role

**Difficulty:** Intermediate

**Statement:** In Cosmos, ABCI connects the application to the consensus engine (CometBFT).

**Answer:** A (True)

**Rationale:** ABCI defines the boundary between app logic and consensus/replication.

**Citation:** https://docs.cosmos.network/main/learn/advanced/abci [EN]

---

#### S15: App hash consistency

**Difficulty:** Advanced

**Statement:** If app hash diverges across validators, CometBFT nodes halt/panic on commit.

**Answer:** A (True)

**Rationale:** Mismatched app hashes indicate state divergence; safety requires stopping to avoid corrupt commits.

**Citation:** https://docs.cometbft.com/ [EN]

---

### Topic 4: RPC & API Surface

#### S16: Add custom RPC in Geth

**Difficulty:** Advanced

**Statement:** Adding a custom JSON-RPC method in Geth requires registering it in the API backend and RPC server.

**Answer:** A (True)

**Rationale:** New methods are wired via service structs and exposed through the RPC module registration.

**Citation:** https://geth.ethereum.org/docs/developers/dapp-developer/rpc [EN]

---

#### S17: eth_call state override

**Difficulty:** Intermediate

**Statement:** `eth_call` with state overrides mutates the node's chain state.

**Answer:** B (False)

**Rationale:** `eth_call` executes locally without persistence; overrides affect simulation only.

**Citation:** https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_call [EN]

---

#### S18: Cosmos gRPC vs Tendermint RPC

**Difficulty:** Advanced

**Statement:** Cosmos SDK exposes app-level queries via gRPC; Tendermint RPC serves consensus/network data.

**Answer:** A (True)

**Rationale:** gRPC services handle module queries/tx; Tendermint RPC provides block, tx, and event queries.

**Citation:** https://docs.cosmos.network/main/build/building-modules/query-services [EN]

---

#### S19: WebSocket vs filters

**Difficulty:** Advanced

**Statement:** `eth_subscribe` over WebSocket is preferred to legacy polling filters for realtime events.

**Answer:** A (True)

**Rationale:** Subscriptions push updates efficiently vs. `eth_getFilterChanges` polling.

**Citation:** https://geth.ethereum.org/docs/interacting-with-geth/rpc/pubsub [EN]

---

### Topic 5: Ops, HA & Kubernetes

#### S20: Liveness probes & reorgs

**Difficulty:** Intermediate

**Statement:** Liveness probes should restart nodes whenever chain reorgs occur.

**Answer:** B (False)

**Rationale:** Reorgs are normal; liveness indicates process health, not chain events. Readiness is a better gate.

**Citation:** https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/ [EN]

---

#### S21: Headless service + StatefulSet

**Difficulty:** Advanced

**Statement:** Headless Services with StatefulSets provide stable DNS identities for node pods.

**Answer:** A (True)

**Rationale:** Headless Services (`clusterIP: None`) enable stable network IDs like `pod-0.svc`.

**Citation:** https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/#stable-network-id [EN]

---

#### S22: HPA for read scaling

**Difficulty:** Advanced

**Statement:** An HPA can scale read-only RPC nodes horizontally behind a Service to absorb bursts.

**Answer:** A (True)

**Rationale:** Stateless RPC frontends/full-node replicas serving reads can scale with HPA based on metrics.

**Citation:** https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ [EN]

---

#### S23: PVC access modes

**Difficulty:** Advanced

**Statement:** ReadWriteOnce PVCs prevent simultaneous multi-pod mounts, limiting active-active state sharing.

**Answer:** A (True)

**Rationale:** RWO volumes can be mounted by a single node; shared access needs RWX-capable storage classes.

**Citation:** https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes [EN]

---

### Topic 6: Clients & Storage Internals

#### S24: Erigon storage layout

**Difficulty:** Advanced

**Statement:** Erigon uses a custom storage layout optimized for disk I/O and range queries, reducing disk usage.

**Answer:** A (True)

**Rationale:** Erigon redesigns data structures (e.g., KV tables) for performance and lower storage footprint.

**Citation:** https://github.com/ledgerwatch/erigon [EN]

---

## Reference Sections

### Minimum Entry Requirements

| Reference section | Floor count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

### Glossary, Terminology & Acronyms

**JSON-RPC**: A stateless remote procedure call protocol using JSON over HTTP/WebSocket [EN]

**gRPC**: High-performance RPC framework using HTTP/2 and Protocol Buffers [EN]

**ABCI** (Application Blockchain Interface): Interface between Cosmos app and consensus engine [EN]

**CometBFT/Tendermint**: BFT consensus engine with instant finality under <1/3 Byzantine faults [EN]

**Devp2p**: Ethereum execution-layer peer-to-peer protocol over RLPx [EN]

**RLPx**: Encrypted transport and session protocol used by devp2p [EN]

**Mempool**: Set of unconfirmed transactions each node tracks prior to inclusion in blocks [EN]

**Pruning**: Discarding historical state data while keeping blocks/headers to save disk [EN]

**Archive Node**: Node that stores all historical states for arbitrary-block queries [EN]

**Finality**: Guarantee that a committed block will not be reverted under protocol assumptions [EN]

**StatefulSet**: Kubernetes controller for ordered, persistent, identity-stable pods [EN]

**PVC** (PersistentVolumeClaim): Kubernetes storage request with defined access modes (RWO/RWX) [EN]

**Helm**: Kubernetes package manager for templating and deploying charts [EN]

**Affinity/Anti-affinity**: Scheduling constraints to distribute pods across nodes/failure domains [EN]

**Snapshot (Geth)**: State snapshot enabling fast access/sync strategies [EN]

### Codebase & Library References

**go-ethereum (Geth)** (GitHub: ethereum/go-ethereum | License: LGPL-3.0)
- Description: Official Go implementation of the Ethereum execution client
- Stack: Go, devp2p, LevelDB/pebble (varies)
- Maturity: Production
- Performance: Snap sync; state snapshots for faster reads
- Security: Active audits; long-lived OSS project

**Bitcoin Core** (GitHub: bitcoin/bitcoin | License: MIT)
- Description: Reference Bitcoin full node and wallet
- Stack: C++, LevelDB/UTXO set
- Maturity: Production
- Performance: AssumeUTXO (emerging), compact blocks
- Security: Extensive review; CVE history managed openly

**Cosmos SDK** (GitHub: cosmos/cosmos-sdk | License: Apache-2.0)
- Description: Framework for building app-specific blockchains
- Stack: Go, gRPC, IAVL/SDK store
- Maturity: Production
- Performance: ABCI++ features; concurrent mempool (varies by version)
- Security: Audited modules; ecosystem standards

**CometBFT** (GitHub: cometbft/cometbft | License: Apache-2.0)
- Description: BFT consensus engine used by Cosmos chains
- Stack: Go, P2P, WAL
- Maturity: Production
- Performance: Sub-second finality (config-dependent)
- Security: Slashing via app; evidence handling

**Erigon** (GitHub: ledgerwatch/erigon | License: GPL-3.0)
- Description: High-performance Ethereum execution client
- Stack: Go/C; optimized KV tables
- Maturity: Production
- Performance: Reduced disk usage; fast range queries
- Security: Open development; community audits

**Nethermind** (GitHub: NethermindEth/nethermind | License: GPL-3.0)
- Description: .NET-based Ethereum execution client
- Stack: C#, devp2p
- Maturity: Production
- Performance: Optimizations for tracing/indexing
- Security: Audits and active maintenance

**Reth** (GitHub: paradigmxyz/reth | License: Apache-2.0/MIT)
- Description: Rust Ethereum execution client under active development
- Stack: Rust, devp2p
- Maturity: Beta/Active development
- Performance: Modern async architecture
- Security: Ongoing reviews

**Kubernetes** (GitHub: kubernetes/kubernetes | License: Apache-2.0)
- Description: Container orchestration system
- Stack: Go, etcd
- Maturity: Production
- Performance: HPA/VPA; efficient scheduling
- Security: RBAC, PSP replacements, admission controls

**Docker** (GitHub: moby/moby | License: Apache-2.0)
- Description: Container engine
- Stack: Go, containerd
- Maturity: Production
- Performance: Layered images, overlay filesystems
- Security: Namespaces, cgroups, seccomp/AppArmor profiles

### Authoritative Literature & Reports

**Bitcoin: A Peer-to-Peer Electronic Cash System** (2008) [EN]
- Authors: Satoshi Nakamoto
- Type: White Paper
- Key Findings: PoW and longest-chain consensus enabling decentralized cash
- Credibility: Foundational industry-defining paper
- Jurisdiction: Global

**Ethereum: A Secure Decentralised Generalised Transaction Ledger (Yellow Paper)** (2014/ongoing) [EN]
- Authors: Gavin Wood
- Type: Technical Specification
- Key Findings: EVM semantics and Ethereum protocol definition
- Credibility: Canonical technical spec
- Jurisdiction: Global

**Tendermint: Consensus without Mining** (2014) [EN]
- Authors: Jae Kwon
- Type: White Paper
- Key Findings: BFT consensus with instant finality
- Credibility: Widely cited in PoS ecosystems
- Jurisdiction: Global

**NISTIR 8202: Blockchain Technology Overview** (2018) [EN]
- Authors: C. Yaga et al., NIST
- Type: Government Report
- Key Findings: Taxonomy and security considerations for blockchain systems
- Credibility: U.S. standards body
- Jurisdiction: US/Global

**Cosmos Whitepaper: A Network of Distributed Ledgers** (2016) [EN]
- Authors: Jae Kwon, Ethan Buchman
- Type: White Paper
- Key Findings: Interoperability via IBC and BFT hubs/zones
- Credibility: Foundational for Cosmos ecosystem
- Jurisdiction: Global

**Kubernetes Documentation (Workloads/StatefulSets)** (ongoing) [EN]
- Authors: CNCF/Kubernetes SIGs
- Type: Official Documentation
- Key Findings: Best practices for stateful workloads and storage
- Credibility: Official project docs
- Jurisdiction: Global

**中国区块链白皮书** (2023) [ZH]
- Authors: 中国信息通信研究院（CAICT）
- Type: 行业白皮书
- Key Findings: 国内区块链发展现状与趋势；产业与监管洞察
- Credibility: 行业权威研究机构
- Jurisdiction: 中国

**区块链安全白皮书** (2020) [ZH]
- Authors: 国家互联网应急中心（CNCERT/CC）
- Type: 行业白皮书
- Key Findings: 区块链安全风险、攻击面与防护建议
- Credibility: 国家级网络安全机构
- Jurisdiction: 中国

### APA Style Source Citations

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system. https://bitcoin.org/bitcoin.pdf [EN]

Wood, G. (2014). Ethereum: A secure decentralised generalised transaction ledger (Yellow Paper).
		https://ethereum.github.io/yellowpaper/paper.pdf [EN]

Kwon, J. (2014). Tendermint: Consensus without mining. https://tendermint.com/static/docs/tendermint.pdf [EN]

Yaga, D., Mell, P., Roby, N., & Scarfone, K. (2018). Blockchain technology overview (NISTIR 8202).
		https://doi.org/10.6028/NIST.IR.8202 [EN]

Kwon, J., & Buchman, E. (2016). Cosmos: A network of distributed ledgers. https://v1.cosmos.network/resources/whitepaper [EN]

Ethereum Foundation. (n.d.). JSON-RPC API. https://ethereum.org/en/developers/docs/apis/json-rpc/ [EN]

Go Ethereum. (n.d.). Snap sync and data storage. https://geth.ethereum.org/docs/fundamentals/sync-modes [EN]

Bitcoin Core. (n.d.). RPC documentation. https://bitcoincore.org/en/doc/ [EN]

Kubernetes Authors. (n.d.). StatefulSets. https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/ [EN]

中国信息通信研究院. (2023). 中国区块链白皮书. https://www.caict.ac.cn/ [ZH]

国家互联网应急中心. (2020). 区块链安全白皮书. https://www.cert.org.cn/ [ZH]

Nakamoto, S. (2008). Bitcoin: Un sistema de efectivo electrónico peer-to-peer (Spanish translation).
		https://bitcoin.org/files/bitcoin-paper/bitcoin_es.pdf [ES]

---

> Note: Sources are limited to widely recognized official docs, whitepapers, and standards to ensure credibility and
> accessibility for a Blockchain Node Developer interview context.

