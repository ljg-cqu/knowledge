

Sun Jun 29 2025

SPEEDEX is a novel, fully on-chain decentralized exchange (DEX) designed to achieve high throughput, eliminate internal arbitrage, and prevent certain front-running attacks by utilizing an Arrow-Debreu exchange market structure. It aims to offer a scalable, parallelizable, and economically efficient solution for secure asset trading without centralized control.

### 💡 Core Concept & Innovation

SPEEDEX is a decentralized exchange (DEX) that facilitates secure asset trading while ensuring no single party exerts undue control over the market. Its foundational innovation lies in adopting an Arrow-Debreu exchange market structure, which fixes asset valuations for all trades within a specific block of transactions.

#### On-Chain Operation
- **Full On-Chain Execution**: Unlike some DEXes that rely on off-chain solutions, SPEEDEX operates entirely within a Layer-1 blockchain. This design maintains market liquidity without fragmentation across multiple chains or rollups.

#### Commutative Semantics & Batch Processing
- **Fixed Exchange Rates**: By executing all orders at the same exchange rate within a block, SPEEDEX ensures transactions are commutative. This means the order in which trades are processed does not affect the final outcome, which is critical for efficient parallelization.
- **Unified Batch Processing**: It processes a block of limit orders as a single, unified batch, determining unique exchange rates applicable to that entire batch.

### 🚀 Key Advantages & Features

SPEEDEX offers several significant advantages over previous decentralized exchanges, focusing on performance, fairness, and scalability.

- **High Throughput**: It is capable of processing over 200,000 transactions per second (TPS) on 48-core servers, even when managing tens of millions of open offers.
- **Elimination of Internal Arbitrage**: The system ensures that a direct trade between two assets (e.g., A to B) always receives a price equal to or better than trading through an intermediate asset (e.g., A to C then C to B), optimizing liquidity utilization.
- **Prevention of Certain Front-Running**: By fixing exchange rates per block, SPEEDEX removes opportunities for risk-free front-running, where malicious actors exploit transaction ordering for profit. This reduces Miner Extractable Value (MEV) derived from reordering transactions.
- **Equal Access**: Every user is provided with an equal level of access to exchange rates within a given block, promoting fairness.
- **Efficient Parallelization**: Its commutative design allows for highly efficient parallel processing of transactions across multiple CPU cores, enabling scalability with hardware improvements without altering transaction semantics.
- **Account-Based Scalability**: SPEEDEX demonstrates that account-based ledgers can achieve horizontal scalability, supporting millions of accounts effectively.
- **Zero-Sum System**: It guarantees that no user's trade price is worse than their specified minimum limit price, although some users might achieve better or worse prices compared to sequential execution.

### ⚙️ Technical Design & Algorithms

The core of SPEEDEX's technical design revolves around sophisticated algorithms for batch clearing and efficient data management.

#### Price Computation
- **Arrow-Debreu Equilibrium**: The main algorithmic challenge is computing batch clearing prices, which maps to finding equilibrium in Arrow-Debreu Exchange Markets.
- **Tâtonnement Process**: SPEEDEX utilizes an iterative Tâtonnement process to efficiently approximate market clearing prices.
  - **Efficiency**: The process runs in time largely independent of the number of limit orders \\(O(\text{#assets}^2 \cdot \lg(\text{#offers}))\\), even with millions of offers.
  - **Demand Queries**: It efficiently computes demand queries using binary searches over sorted offer lists.
  - **Price Adjustment**: Employs a multiplicative, normalized price update rule with dynamic step size adjustment, supporting parallel execution of multiple Tâtonnement instances.
  - **Demand Smoothing**: Approximates offer behavior with a continuous function to manage demand discontinuities.
- **Linear Program (LP) Approximation Correction**: To explicitly correct Tâtonnement's approximation error, SPEEDEX uses a linear program.
  - **Size**: The LP's size depends on the number of asset pairs \\(O(\text{#assets}^2)\\) rather than the number of offers.
  - **Guarantees**: It ensures asset conservation, prevents offers from trading outside their limit prices, and maximizes total trading activity. Setting commissions to zero simplifies it to a maximum circulation problem, which is more algorithmically tractable.

#### Data Structures & Optimization
- **Custom Merkle-Patricia Tries**: Employs custom Merkle-Patricia tries optimized for concurrent, batched manipulation, leveraging hardware-level atomics.
- **Optimizations**: Includes precomputing offer lists for Tâtonnement, using fixed-point arithmetic for precision, and optimizing trie design for cache performance and concurrency.

### 📊 Performance & Scalability (Evaluation)

Evaluations highlight SPEEDEX's robust performance and scalability, significantly outperforming existing systems.

- **Achieved Throughput**: Exceeds 200,000 TPS on 48-core servers during testing.
- **Linear Speedup**: Demonstrates near-linear speedup with an increase in CPU cores.
- **Scalability with Offers**: Throughput only experiences an approximate 10% drop even when the number of open offers increases from 0 to tens of millions.
- **Robustness**: The Tâtonnement process converges quickly in most cases (350 out of 500 blocks in tests with volatile crypto data), even under challenging market conditions.
- **Faster Validation**: Validating and executing a block proposal from another replica is significantly faster than proposing a block, which helps delayed replicas catch up efficiently.

#### Comparison to Alternatives
| Feature                 | SPEEDEX                                    | Traditional Orderbook DEXes             | Optimistic Concurrency Control (e.g., Block-STM) | Existing Production Systems (e.g., Ethereum) |
| :---------------------- | :----------------------------------------- | :-------------------------------------- | :----------------------------------------------- | :------------------------------------------- |
| **Throughput**          | >200,000 TPS                               | Becomes bottleneck with many accounts   | Less scalable for payment workloads              | Ethereum (3k TPS), Stellar (4k TPS)          |
| **Scalability**         | Superior, near-linear speedup              | Limited, bottlenecks with account growth| Limited, especially with large batch sizes       | Significantly lower                          |
| **Internal Arbitrage**  | Eliminates                                 | Prone to                                | Not directly addressed                           | Prone to                                     |
| **Front-Running (Risk-Free)** | Prevents certain types                     | Prone to                                | Prone to                                         | Prone to                                     |

### 🚧 Limitations & Future Directions

While highly capable, SPEEDEX has identified limitations and areas for future development.

- **Latency**: The inherent batching process introduces a delay between order submission and execution. Its economic implications, particularly for market-making profitability, require further study.
- **Tâtonnement Nondeterminism**: The algorithm's randomized approximation can be made deterministic (e.g., by fixing parameters) or measured for approximation error.
- **Overdraft Prevention**: The current implementation checks for overdrafts post-block application, complicating pipelining. A deterministic approach (pre-calculating debits) is proposed for better compatibility.
- **Other Front-Running Types**: SPEEDEX does not prevent all forms of front-running (e.g., estimating prices for future batches, delaying transactions). Mitigation could involve combining with commit-reveal schemes or batching across multiple consensus blocks.
- **Linear Program Scalability**: The runtime of the Linear Program increases significantly beyond 60-80 assets. Market structure decomposition (e.g., separating core currencies from stocks via hierarchical pricing) is proposed to support more assets.
- **Limited Trade Types**: Primarily supports limit sell orders. Integrating limit buy orders and Constant Function Market Makers (CFMMs) is possible and has been done in Stellar's implementation.

### 🛠️ Implementation & Integration

SPEEDEX is designed for integration into existing blockchain infrastructures, emphasizing performance and modularity.

- **Technology Stack**: Implemented in C++20, utilizing Intel's TBB for parallel scheduling, GNU Linear Programming Kit for LP solving, and LMDB for data persistence.
- **Blockchain Integration**: Prototyped for the Stellar blockchain, where it is designed to run within every replica of the blockchain node software for optimal performance. The Stellar implementation uses two-phase blocks, initially with sequential SPEEDEX execution, allowing for future parallelization without requiring protocol upgrades.
- **Open Source**: The project's code is available as open source at `https://github.com/scslab/speedex`.

Generated by Liner
https://getliner.com/search/s/5926611/t/86093779