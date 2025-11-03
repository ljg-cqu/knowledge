# Shared References — Blockchain Node Developer

This shared reference note is used across the interview pack (QA, True/False, MCQ, Short Answer, Cloze, Case Study, Coding, Debugging). It centralizes a glossary, authoritative documentation, notable codebases, and selected literature. Citations mix English and Chinese where useful.

## Glossary (≥10)

- Execution Client (EL): Ethereum client implementing JSON-RPC, EVM, state, and Engine API on the execution layer (e.g., Geth, Nethermind, Erigon, Besu).
- Consensus Client (CL): Beacon chain client implementing proof-of-stake consensus and fork choice (e.g., Prysm, Lighthouse, Teku, Nimbus).
- Engine API: JSON-RPC interface between EL and CL used since The Merge (e.g., engine_newPayloadV2/V3/V4).
- GossipSub: PubSub protocol (libp2p) used for gossiping blocks/attestations with mesh scoring and topic scoring.
- Reorg (Chain Reorganization): Rewriting of canonical chain head due to adoption of a different fork; can orphan blocks/txs.
- Finality: Property that a block cannot be reverted without >1/3 slashable behavior; often measured by distance from head to finalized.
- P2P Peer Scoring: Mechanism to score peers by behavior (validity, contribution) for mesh maintenance and DoS resistance.
- Staged Sync (Erigon): Multi-stage pipeline (download → process → index) optimizing I/O and cache usage.
- Flat Storage (Erigon): Table design denormalizing tries into flat tables for fast reads and batch state updates.
- Snapshot: Point-in-time export of chain data/state for fast bootstrap; requires integrity verification (hash/signature).
- Mempool Policy (Bitcoin): Rules for transaction acceptance/eviction affecting propagation and fee estimation.
- SLO/Error Budget: Service Level Objective and allowed monthly error time used to govern rollouts and risk.

## Official Docs and Specs

- Ethereum Execution Layer Specs (Engine API): https://github.com/ethereum/execution-apis
- Ethereum Consensus Specs: https://github.com/ethereum/consensus-specs
- JSON-RPC API (Ethereum): https://ethereum.org/en/developers/docs/apis/json-rpc/
- libp2p GossipSub v1.1: https://github.com/libp2p/specs/tree/master/pubsub/gossipsub
- Prometheus (Go client): https://github.com/prometheus/client_golang
- JWT (IETF RFC 7519): https://datatracker.ietf.org/doc/html/rfc7519
- Bitcoin Core Policy/Mempool: https://github.com/bitcoin/bitcoin/tree/master/doc/policy
- Cosmos SDK Docs: https://docs.cosmos.network/
- CometBFT (Tendermint) Docs: https://docs.cometbft.com/

## Codebases (≥5)

- go-ethereum (Geth): https://github.com/ethereum/go-ethereum
- erigon: https://github.com/ledgerwatch/erigon
- nethermind: https://github.com/NethermindEth/nethermind
- besu: https://github.com/hyperledger/besu
- prysm: https://github.com/prysmaticlabs/prysm
- lighthouse: https://github.com/sigp/lighthouse
- teku: https://github.com/ConsenSys/teku
- nimbus-eth2: https://github.com/status-im/nimbus-eth2
- bitcoin/bitcoin: https://github.com/bitcoin/bitcoin
- cosmos/cosmos-sdk: https://github.com/cosmos/cosmos-sdk

## Literature and Deep Dives (≥6)

- The Ethereum Merge: https://blog.ethereum.org/2022/09/15/merge
- Ethereum Yellow Paper (latest): https://ethereum.github.io/yellowpaper/paper.pdf
- Erigon internal architecture: https://github.com/ledgerwatch/erigon#readme
- GossipSub design and v1.1: https://arxiv.org/abs/2007.02754
- SRE Book (SLOs/Error Budgets): https://sre.google/sre-book/service-level-objectives/
- Bitcoin mempool and fee market: https://bitcoinops.org/en/topics/mempool/

- 中文｜以太坊开发者文档（JSON-RPC 概览）: https://learnblockchain.cn/docs/ethereum/json-rpc/
- 中文｜以太坊黄皮书（翻译）: https://ethfans.org/wikis/%E9%BB%84%E7%9A%AE%E4%B9%A6

## Citations (≥12)

1) Execution-Consensus Engine API: https://github.com/ethereum/execution-apis
2) Ethereum Consensus Specs: https://github.com/ethereum/consensus-specs
3) Ethereum JSON-RPC: https://ethereum.org/en/developers/docs/apis/json-rpc/
4) GossipSub v1.1: https://github.com/libp2p/specs/tree/master/pubsub/gossipsub
5) Go Prometheus client: https://github.com/prometheus/client_golang
6) JWT (RFC 7519): https://datatracker.ietf.org/doc/html/rfc7519
7) Bitcoin policy: https://github.com/bitcoin/bitcoin/tree/master/doc/policy
8) Cosmos SDK: https://docs.cosmos.network/
9) CometBFT: https://docs.cometbft.com/
10) SRE SLOs: https://sre.google/sre-book/service-level-objectives/
11) Erigon design: https://github.com/ledgerwatch/erigon#readme
12) GossipSub paper: https://arxiv.org/abs/2007.02754
13) The Merge blog: https://blog.ethereum.org/2022/09/15/merge
14) 中文 JSON-RPC 概览: https://learnblockchain.cn/docs/ethereum/json-rpc/
15) 中文 黄皮书译本: https://ethfans.org/wikis/%E9%BB%84%E7%9A%AE%E4%B9%A6

## Notes

- Use this file as the reference anchor from all *_GPT-5.md deliverables in this folder.
- For code examples, prefer upstream client idioms (Go/Rust) and refer to official repos.
- When citing specific protocol constants or method variants (e.g., engine_newPayloadV3 vs V4), pin the spec link to a commit hash for auditability when feasible.
