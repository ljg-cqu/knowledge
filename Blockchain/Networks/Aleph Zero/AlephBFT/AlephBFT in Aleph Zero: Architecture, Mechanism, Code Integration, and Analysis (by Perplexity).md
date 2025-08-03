<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# AlephBFT in Aleph Zero: Architecture, Mechanism, Code Integration, and Analysis

**Key Takeaway:**
AlephBFT delivers *asynchronous safety*, *monotonic finality*, and *high throughput* via a DAG-based ordering of signed “Units,” offering low-latency consensus tailored for Substrate.

## 1. Architecture \& Integration

```mermaid
flowchart LR
  subgraph Substrate Node
    C[Client] --> BI[BlockImport<AlephConfig>]
    BI --> JI[JustificationImport]
    JI --> TM[Finality-aleph Task Manager]
  end
  subgraph AlephBFT Consensus
    direction TB
    U[r−1 Units] --> U[r Units]
    DAG[Units DAG] --> OrderData
    OrderData --> FinalBlocks
  end
  TM --> AlephBFT Consensus
```

| **Component** | **Location** | **Purpose** |
| :-- | :-- | :-- |
| `block_import` | `service/new_partial` | Replace Grandpa finality gadget |
| `AlephConfig`, `Params` | `finality-aleph/src/abft/common.rs` | Configure thresholds, session length |
| `AlephNetwork` | `finality-aleph/src/abft/network.rs` | Gossip integration with libp2p |
| `AlephBFT` trait | `finality-aleph/src/abft/traits.rs` | Defines spawn hook for consensus runtime |
| Crypto types | `finality-aleph/src/abft/crypto.rs` | Signature and authority identifiers |

## 2. Protocol Sequence \& Mechanism

```mermaid
sequenceDiagram
  participant i,j,k
  loop Round r
    i->>i: can_create(r)?
    alt Yes
      i->>j: Unitᵢʳ
      i->>k: Unitᵢʳ
    end
    j->>j: parents→Unitⱼʳ
    k->>k: parents→Unitₖʳ
  end
  note right of i,j,k: DAG grows asynchronously
  i->>i: OrderData(DAG) → Finalize Blocks
```

| **Term** | **Description** |
| :-- | :-- |
| *Unit* | Signed message with `creator`, `round`, `data`, `parents`, `sig`. |
| *DAG* | Directed acyclic graph of Units, ensures extension-only (monotonicity). |
| *OrderData* | Virtual voting + head selection → deterministic batch outputs with monotonic prefix property. |
| *ForkAlert* | Alert mechanism bounding memory \& preventing spam forks. |

## 3. Code Excerpts

| **File** | **Excerpt** |
| :-- | :-- |
| `service/new_partial` | ```rust<br>let (block_import, link) = finality_aleph::block_import::<_,_,_,_,AlephConfig>(...);<br>let justification_import = link.justification_import();<br>``` |
| `finality-aleph/src/abft/common.rs` | ```rust<br>pub struct AlephConfig; <br>impl AlephBFT for AlephConfig { /* Signing=SignatureSet; AuthorityId=AuthorityId */ }<br>``` |
| `finality-aleph/src/abft/crypto.rs` | ```rust<br>pub type AuthorityId = sp_core::ed25519::Public;<br>pub type SignatureSet = sp_core::ed25519::Signature;``` |
| `finality-aleph/src/abft/network.rs` | ```rust<br>pub struct AlephNetwork { /* ... */ }<br>impl NetworkBehaviour for AlephNetwork { /* ... */ }``` |
| `finality-aleph/src/abft/traits.rs` | ```rust<br>pub trait AlephBFT {<br> type AuthorityId; type Signing;<br> fn spawn<...>() -> anyhow::Result<()>;<br>} ``` |

## 4. SWOT Analysis

| **Strengths** | **Weaknesses** |
| :-- | :-- |
| Asynchronous safety, no Δ | Lacks full async liveness (deterministic votes) |
| High throughput \& energy efficiency | Alerts add protocol overhead |
| DAG-based monotonic finality | Static session parameters |
| Native Substrate integration | No on-chain parameter tuning |

| **Opportunities** | **Threats** |
| :-- | :-- |
| Integrate randomness for liveness | Fork-bomb if alerts dropped |
| Runtime parameter configuration | Adversarial network partitions |
| Pallet abstraction \& upgrades | Latency spikes in WAN |

## 5. Comparative Analysis

| Feature | AlephBFT | PBFT | Tendermint | HotStuff |
| :-- | :-- | :-- | :-- | :-- |
| **Model** | Async BFT | Partial sync BFT | Partial sync BFT | Partial sync BFT |
| **Fault Tolerance** | f < N/3 | f < N/3 | f < N/3 | f < N/3 |
| **Msg Complexity** | O(N²)+alerts | O(N²) | O(N²)+Δ wait | O(N) pipelined |
| **Latency** | Low (no Δ) | Moderate | High (Δ) | Moderate |
| **Throughput** | High | Moderate | Moderate | High |
| **Finality** | Monotonic | Deterministic | Deterministic | Deterministic |

### References

Castro, M., \& Liskov, B. (1999). *Practical Byzantine Fault Tolerance*.
Amiri, T. (2024). *Bottlenecks in Byzantine Fault Tolerance*. USENIX NSDI.
Gasper, C., et al. (2021). *HotStuff: BFT Consensus in the Era of Blockchains*.
AlephBFT Doc Team. (2025). *What Is AlephBFT?* \& *How AlephBFT Does It?*. Cardinal-Cryptography Documentation.

