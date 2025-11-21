1. Q: Rust's ownership system has three core rules: each value has ___ owner, only ___ owner at a time, and values are dropped when ___ go out of scope.
   A: one; one; owners

1. Q: Solana's theoretical transaction throughput capacity is ___ TPS.
   A: 65,000

1. Q: In Ethereum consensus, what is the finality requirement? Wait ___ blocks on Ethereum, ___ slots on Solana.
   A: 12; 32

1. Q: The AMM constant product formula is ___.
   A: x * y = k

1. Q: List the 3 Rust pointer types with their ownership characteristics: ___, ___, ___.
   A: &T (shared immutable reference), &mut T (exclusive mutable reference), Box<T> (owned heap allocation)

1. Q: In a blockchain stablecoin ecosystem, list the 6 core parties.
   A: issuers, custodians, users, exchanges, oracles, regulators

1. Q: Ethereum's Fusaka hard-fork in 2025 increases data capacity by up to ___x.
   A: 20

1. Q: Solana's proposed 2025 upgrade increases block capacity from ___ to ___ Compute Units.
   A: 60M; 100M

1. Q: Patricia Merkle Trie is used in Ethereum for ___ data management.
   A: state

1. Q: List the 3 slashing conditions in Ethereum consensus.
   A: double voting (same slot, different attestation data), surround voting (source-target span violations), attestation timing violations

1. Q: ECDSA stands for ___.
   A: Elliptic Curve Digital Signature Algorithm

1. Q: zk-SNARKs stands for ___.
   A: Zero-Knowledge Succinct Non-Interactive Argument of Knowledge

1. Q: In cross-chain bridge security, threshold signature validation typically requires ___% + 1 validators.
   A: 66 (or 2/3)

1. Q: For high-throughput DEX design, typical target P99 latency is under ___ ms at ___ TPS.
   A: 100; 50,000

1. Q: Ethereum block time target is approximately ___ seconds.
   A: 12

1. Q: Solana block time is approximately ___ seconds.
   A: 0.4

1. Q: In Rust, the `Arc<Mutex<T>>` pattern is used for ___.
   A: thread-safe shared mutable state (or multi-threaded shared state with interior mutability)

1. Q: Gas optimization best practice: batch storage operations can reduce gas costs by approximately ___%.
   A: 40

1. Q: For production blockchain nodes, cache hit ratio should be greater than ___%.
   A: 85

1. Q: Database read latency P95 target for healthy blockchain nodes is under ___ μs.
   A: 500

1. Q: List the 3 main DEX security vulnerabilities to protect against.
   A: reentrancy attacks, oracle manipulation, slippage attacks

1. Q: Merkle tree is used to verify ___ of data.
   A: integrity (or completeness)

1. Q: In Solana's account model, programs are ___, and data is stored in ___.
   A: stateless; separate accounts

1. Q: The maximum account data size in Solana is ___ MB.
   A: 10

1. Q: For blockchain event monitoring, the standard confirmation depth is ___ blocks on Ethereum.
   A: 12

1. Q: ERC-20 is a standard for ___ on Ethereum.
   A: fungible tokens

1. Q: MiCA stands for ___.
   A: Markets in Crypto-Assets Regulation

1. Q: In KYC/AML compliance for stablecoins, banks globally spend significant amounts, with costs increasing operational overhead by approximately ___-___%.
   A: 15; 30

1. Q: List the 4 main stablecoin revenue models.
   A: seigniorage, collateral yield, transaction fees, DeFi integration fees

1. Q: Algorithmic stablecoins rely on ___ to absorb price fluctuations.
   A: a second, volatile governance token

1. Q: For memory-efficient trie implementation, LRU cache hit ratio target is ___%.
   A: 90+

1. Q: Rust's `async/await` uses ___ runtime for multi-threaded work-stealing scheduling.
   A: Tokio (or async-std)

1. Q: In Rust, the `?` operator is used for ___.
   A: error propagation (or early return on error)

1. Q: List the 3 Rust naming conventions: type-level constructs use ___, functions/variables use ___, constants use ___.
   A: UpperCamelCase; snake_case; SCREAMING_SNAKE_CASE

1. Q: Rust profiling tools for blockchain optimization include ___, ___, and ___.
   A: cargo flamegraph; perf; valgrind

1. Q: The two-heap approach for median tracking has insertion time complexity of ___ and median calculation of ___.
   A: O(log n); O(1)

1. Q: For cross-chain bridges, the primary security risks are ___, ___, and ___.
   A: 51% attacks, eclipse attacks, front-running attacks

1. Q: Rate limiting for cross-chain bridges typically caps transfers at ___ ETH equivalent per hour.
   A: 1000

1. Q: In Web3 indexer design, backpressure channel capacity should be ___x throughput.
   A: 2

1. Q: Ideal DEX swap slippage protection parameter: reject if actual output is less than ___% of expected.
   A: 95-99 (minimum amount out threshold)

1. Q: Rust's ownership model reduces memory-related runtime bugs by ___-___%.
   A: 60; 80

1. Q: For validator performance, target consensus state transition processing time should be under ___ ms.
   A: 50-100

1. Q: In order matching engines, CEX latency is typically ___-___ ms vs DEX ___-___ ms.
   A: 1; 10; 50; 200

1. Q: CEX throughput is approximately ___x higher than DEX throughput.
   A: 100

1. Q: Solana's Sealevel runtime enables ___ transaction execution.
   A: parallel

1. Q: Transaction pool (mempool) eviction policy should prioritize transactions by ___.
   A: fee (or gas price)

1. Q: For blockchain state storage, typical DB read IOPS target is under ___ read/s.
   A: 8,000

1. Q: Event-driven smart contract platforms can reduce latency by ___-___x compared to transaction-driven models.
   A: 2.2; 4.6

1. Q: List the 3 blockchain data structures essential for integrity and efficiency.
   A: Merkle tree, Patricia trie, Merkle Patricia trie

1. Q: Consensus mechanism trade-off: PoW is ___ but ___, while PoS is ___ but may have ___.
   A: secure; energy-intensive; energy-efficient; centralization risk

1. Q: For high-availability blockchain nodes, recovery time objective should be under ___ seconds after failure.
   A: 5

1. Q: Rust compile times for large codebases (>100k LOC) may reach ___-___ minutes.
   A: 2; 5
