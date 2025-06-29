'  Requirements: 1. Ensure outputs are classified clearly and comply with MECE. 2. Explain clearly and briefly, using simple analogies and examples. 3. Use numbered lists for clarity when suitable. 4. Assume there are three question levels: basic, intermediate, and advanced. 5. List concisely, and separately, 40 crucial basic, 40 crucial intermediate, 40 crucial advanced 'why' Q&As. 6. Order 'why' Q&As by the significance of the question within each level.

Sun Jun 29 2025

### Report on SPEEDEX: A Scalable, Parallelizable, and Economically Efficient Decentralized Exchange

### Introduction to SPEEDEX

SPEEDEX is a decentralized exchange (DEX) that enables participants to securely trade assets without granting undue control to any single party. Developed by Geoffrey Ramseyer, Ashish Goel, and David Mazières from Stanford University, SPEEDEX was presented at the 20th USENIX Symposium on Networked Systems Design and Implementation (NSDI '23), held from April 17–19, 2023, in Boston, MA, USA. The system is designed to address limitations in existing DEXes by focusing on scalability, parallelism, and economic efficiency. It aims to provide a high-quality forum for discussing ideas that advance the knowledge and understanding of networked systems. SPEEDEX is intended to be a crucial piece of infrastructure for a global payments network, enabling seamless interoperability of digital currencies and supporting cross-border remittances.

### MECE Classification of SPEEDEX Outputs

The Mutually Exclusive and Collectively Exhaustive (MECE) principle is a method of grouping information into elements that are distinct and comprehensive, ensuring no overlaps and that all relevant items are included. This framework is widely used in problem-solving and organizing information, particularly in consulting. Applying the MECE principle allows for a structured understanding of the core components of SPEEDEX's design and its contributions.

The outputs from the SPEEDEX document can be classified into the following MECE categories:

1.  **Decentralized Exchange Architecture**
    *   Integration entirely within a Layer-1 blockchain.
    *   Avoidance of liquidity fragmentation between multiple blockchains or rollups.
    *   Utilization of a batch trading model with a virtual "auctioneer".

2.  **Scalability and Parallelism**
    *   Achievement of high throughput, exceeding 200,000 transactions per second on 48-core servers.
    *   Execution of trade operations that are commutative and efficiently parallelizable.
    *   Ability to scale throughput by effectively using many CPU cores.

3.  **Economic Efficiency**
    *   Elimination of internal arbitrage opportunities.
    *   Guarantee that a direct trade always receives a price as good as trading through any third asset.
    *   Enhancement of liquidity, especially between illiquid trading pairs.

4.  **Fairness and Security Guarantees**
    *   Prevention of certain front-running attacks that increase effective bid-ask spread.
    *   Ensurance that every user receives the same, fair exchange rate within a batch.
    *   Commutativity of trades, meaning their order does not affect results.

5.  **Core Algorithmic Principles**
    *   Use of an Arrow-Debreu exchange market structure to fix asset valuations for all trades in a given block.
    *   Development of an algorithm for computing market-clearing valuations that is both asymptotically efficient and empirically practical.
    *   Requirement for computations to run efficiently within a Layer-1 state machine.

6.  **Implementation and Integration**
    *   Prototyped but not yet merged within the Stellar blockchain.
    *   Natural fit into the Stellar blockchain due to its design for a replicated state machine.
    *   Alignment with Stellar's mission of enabling low-cost and fast cross-border payments.

### Main Topics, Concepts, and Findings with Analogies

SPEEDEX introduces an innovative approach to decentralized exchanges by combining economic theory, blockchain integration, and parallel computing. Imagine SPEEDEX as a highly organized, fair, and efficient digital marketplace for trading different types of goods (assets), where:

*   **Decentralized Exchange Architecture**: Unlike many online marketplaces that act as intermediaries, SPEEDEX operates directly within a foundational blockchain, like a permanent, built-in section of a giant digital town square. This "Layer-1" integration means all transactions are handled directly on the main public ledger, avoiding the need to move between different market sections (fragmentation) that can slow things down and make prices inconsistent.

*   **Batch Trading with a Virtual Auctioneer**: Instead of people shouting out bids one by one as in a traditional auction, SPEEDEX gathers all trade requests made during a specific short period, like a few seconds. Then, a "virtual auctioneer" (a sophisticated algorithm) simultaneously determines fair prices for everyone within that batch. It's like a group order in a restaurant where everyone gets the same discount because their orders are processed together. This approach ensures fairness and prevents people from cutting in line (front-running) to get a better deal.

*   **Economic Efficiency via Market Clearing Prices**: SPEEDEX uses an advanced economic model to calculate these fair prices. This model, similar to how supply and demand naturally find a balance in a physical market, ensures that the prices set for assets within each batch are optimal. This means there are no "hidden deals" or ways to make risk-free profit by trading through different paths (internal arbitrage), making the market more honest and efficient for everyone.

*   **Scalability and Parallelism**: Because all trades within a batch are settled at the same prices and their order doesn't matter, SPEEDEX can process them simultaneously, much like having many checkout counters at a supermarket. This parallel processing allows SPEEDEX to handle a massive volume of transactions, over 200,000 per second on high-performance servers, making it incredibly fast and efficient for a global scale.

*   **Front-Running Prevention and Fairness**: A major problem in many exchanges is "front-running," where someone with faster information can place their trade just before yours to profit from your transaction. SPEEDEX's batch processing model inherently prevents this, as all trades in a batch are treated equally and settled at the same price. This ensures a fair playing field for all users, especially smaller traders who are often disadvantaged.

*   **Stellar Blockchain Integration**: SPEEDEX is being prototyped for integration with the Stellar blockchain, which is known for its fast and low-cost cross-border transactions. This integration means SPEEDEX can leverage Stellar's existing infrastructure to reach a vast global audience and handle the immense transaction volumes expected in the future of digital payments.

### Basic-Level "Why" Questions and Answers

1.  **Why is SPEEDEX designed as a decentralized exchange?**
    *   To allow secure trading without giving any single party undue control.
2.  **Why operate fully on a Layer-1 blockchain?**
    *   To integrate the exchange directly within the main blockchain for scalability and security.
3.  **Why use batch processing of trades?**
    *   To apply uniform exchange rates and enable effective parallel computation.
4.  **Why ensure all trades in a batch occur at the same exchange rates?**
    *   To guarantee fairness and eliminate order-dependency.
5.  **Why emphasize parallelizable trade operations?**
    *   To achieve high throughput and scalability.
6.  **Why does SPEEDEX prevent front-running attacks?**
    *   To protect small traders and reduce bid-ask spreads.
7.  **Why compute unique market-clearing valuations?**
    *   To eliminate arbitrage and provide the best possible prices.
8.  **Why is economic efficiency important in SPEEDEX?**
    *   To enhance liquidity, especially for illiquid pairs.
9.  **Why involve an auctioneer separating users for trading?**
    *   To simplify market clearing and price computation.
10. **Why avoid multi-hop path trades?**
    *   To maintain consistent and straightforward trading within a batch.
11. **Why integrate SPEEDEX on the Stellar blockchain?**
    *   To leverage Stellar’s transaction semantics and support horizontal scaling.
12. **Why is scalability a core design focus?**
    *   To meet the volume demands of global payments.
13. **Why use Arrow-Debreu exchange market structures?**
    *   To frame and solve the market-clearing valuation efficiently.
14. **Why combine economic theory and parallel computing?**
    *   To deliver a fast, fair, and efficient decentralized exchange.
15. **Why is fairness guaranteed in SPEEDEX?**
    *   Because the batch transaction order does not affect outcomes.
16. **Why does the design avoid giving undue control to any party?**
    *   To adhere to decentralization principles and trustlessness.
17. **Why prevent arbitrage opportunities?**
    *   To stabilize prices and maintain market integrity.
18. **Why is eliminating front-running attacks critical?**
    *   To create a secure trading environment for all users.
19. **Why is on-chain integration practical?**
    *   It ensures trust, security, and transparency directly on the blockchain.
20. **Why choose multicore servers for processing?**
    *   To maximize parallel throughput and performance.
21. **Why is a high transaction per second (TPS) rate important?**
    *   To support large-scale, real-time asset trading.
22. **Why is decentralization key to SPEEDEX’s security?**
    *   It reduces single points of failure and censorship risk.
23. **Why avoid giving one party market control?**
    *   To prevent manipulation and promote trust.
24. **Why is preventing front-running advantageous for small traders?**
    *   It lowers their trading costs and barriers.
25. **Why compute exchange rates that apply uniformly?**
    *   To simplify settlement and ensure fairness.
26. **Why compute market-clearing valuations unique to each batch?**
    *   To reflect accurate supply and demand balance.
27. **Why ensure trades are commutative?**
    *   To allow parallel and order-independent execution.
28. **Why does SPEEDEX support multiple asset types?**
    *   To enhance market diversity and user options.
29. **Why is economic efficiency combined with scalability?**
    *   To build a practical decentralized exchange usable globally.
30. **Why use parallelizable algorithms in market clearing?**
    *   To reduce latency and improve throughput.
31. **Why does the SPEEDEX auctioneer provide prices rather than individual negotiation?**
    *   To ensure price consistency and simplify trades.
32. **Why is eliminating multi-hop trades beneficial?**
    *   It reduces complexity and risk in trade execution.
33. **Why does SPEEDEX align with Stellar’s transaction semantics?**
    *   To leverage Stellar’s protocol benefits and infrastructure.
34. **Why is SPEEDEX considered practical for on-chain integration?**
    *   Because of its efficient and scalable algorithms.
35. **Why does batch trading help with economic efficiency?**
    *   It aggregates demand/supply to optimize trade outcomes.
36. **Why use a virtual auctioneer concept?**
    *   To create a centralized price-setting mechanism without centralized control.
37. **Why avoid fragmentation of market liquidity across blockchains?**
    *   To maintain concentrated liquidity and enable efficient trading.
38. **Why is a high-quality decentralized exchange crucial?**
    *   It is a crucial piece of infrastructure for a global payments network.
39. **Why is decentralization of the exchange crucial?**
    *   To ensure egalitarian, open access to the world’s financial system.
40. **Why does SPEEDEX process trades in batches?**
    *   To align with how transactions are finalized in a blockchain block.

### Intermediate-Level "Why" Questions and Answers

1.  **Why does SPEEDEX prevent front-running attacks?**
    *   Because batch trading executes trades at the same exchange rates regardless of order, eliminating transaction ordering dependencies that front-runners exploit.
2.  **Why does SPEEDEX operate entirely within a Layer-1 blockchain?**
    *   To avoid fragmenting market liquidity across multiple blockchains or rollups and ensure truly decentralized and scalable trading.
3.  **Why are market-clearing asset valuations unique in SPEEDEX?**
    *   Due to the Arrow-Debreu exchange market structure and linear utilities, ensuring a single set of prices that clear the market.
4.  **Why are trade operations commutative in SPEEDEX?**
    *   Because all trades in a batch occur at uniform exchange rates, making their execution order irrelevant and enabling parallel execution.
5.  **Why does SPEEDEX process trades in batches?**
    *   To achieve equal access to liquidity and enforce fair pricing by matching all trades at the same exchange rates per batch.
6.  **Why does SPEEDEX eliminate internal arbitrage opportunities?**
    *   It computes unique market-clearing valuations ensuring direct trades receive the same price as multi-hop trades, improving fairness and liquidity.
7.  **Why is the core algorithm for computing market-clearing valuations both asymptotically efficient and practical?**
    *   It uses a Tâtonnement iterative algorithm optimized with preprocessing, allowing efficient on-chain integration and scalability.
8.  **Why can SPEEDEX achieve over 200,000 transactions per second on multi-core servers?**
    *   Because the commutative nature of trades enables parallel processing exploiting multi-core architectures.
9.  **Why is the Arrow-Debreu exchange market model suitable for SPEEDEX?**
    *   It models asset pricing for multiple agents with individual utilities, fitting the batch trading and pricing needs of SPEEDEX.
10. **Why does SPEEDEX allow horizontal scaling of the network?**
    *   Its parallelizable design means more CPU cores can be added to increase throughput without redesigning the protocol.
11. **Why does SPEEDEX prevent multi-hop path trades from offering better prices?**
    *   Because all trading pairs receive directly computed exchange rates that are at least as good as any multi-hop path.
12. **Why does SPEEDEX's batch trading model improve liquidity for illiquid trading pairs?**
    *   By using market-clearing prices applicable to all trades simultaneously, it efficiently aggregates liquidity.
13. **Why does SPEEDEX's auctioneer not make strategic choices when setting asset valuations?**
    *   The unique market-clearing prices are an inherent property of a batch of trades, not decisions made by the auctioneer.
14. **Why is it important that trade offers be limit orders in SPEEDEX?**
    *   Because limit prices define the minimum acceptable exchange rate for executing trades consistent with trader preferences.
15. **Why does SPEEDEX integrate well with Stellar blockchain's transaction semantics?**
    *   Because Stellar supports commutative transaction types and a replicated state machine ideal for SPEEDEX's parallel processing.
16. **Why are trade offers that do not execute in one batch discarded?**
    *   Because SPEEDEX requires fresh batches with consistent valuations to maintain fairness and correctness.
17. **Why does SPEEDEX's model substitute multiple trades with a virtual auctioneer?**
    *   To simplify the exchange process and uniformly apply market-clearing valuations to all trades.
18. **Why do linear utility functions simplify equilibrium computation in SPEEDEX?**
    *   Linear utilities ensure unique market-clearing equilibrium and predictable trade behavior.
19. **Why is parallelism essential to SPEEDEX's scalability?**
    *   Because it enables simultaneous processing of independent trade operations, boosting throughput.
20. **Why does SPEEDEX need a specialized algorithm for price computation?**
    *   To efficiently handle the large number of trade offers and assets while preserving economic correctness.
21. **Why is the Tâtonnement price adjustment step multiplicative and heuristically optimized?**
    *   To accelerate convergence and improve performance beyond traditional additive adjustments.
22. **Why does SPEEDEX group offers by trading pairs and sort by limit price?**
    *   To enable efficient binary search for determining which offers execute at candidate prices.
23. **Why is it crucial that SPEEDEX preserves a DEX's financial correctness constraints?**
    *   To maintain the integrity and fairness of trades, preventing double-spends or losses.
24. **Why does SPEEDEX discourage off-chain price computation?**
    *   Off-chain computation compromises full decentralization and auditability.
25. **Why would integrating SPEEDEX in smart contract languages like Ethereum be impractical?**
    *   Because complex price computations require computational resources beyond feasible smart contract gas limits.
26. **Why does SPEEDEX's batch exchange mechanism inherently prevent front-running?**
    *   Because all trades in a batch settle simultaneously at uniform prices with no ordering advantage.
27. **Why is it beneficial that SPEEDEX does not fragment liquidity between blockchains?**
    *   Fragmented liquidity reduces efficiency and can increase slippage and spreads.
28. **Why does SPEEDEX's design support future global-scale payments infrastructure?**
    *   Because it vastly improves throughput, fairness, and liquidity compared to existing DEX designs.
29. **Why is market liquidity a key performance metric in SPEEDEX?**
    *   Greater liquidity reduces trading costs and facilitates seamless asset exchanges.
30. **Why is batch frequency important in SPEEDEX's operation?**
    *   It balances throughput, latency, and market responsiveness.
31. **Why does SPEEDEX's price computation algorithm only approximate equilibrium prices?**
    *   To guarantee fixed runtime and practical performance while keeping error minimal.
32. **Why is the elimination of transaction ordering dependencies vital in SPEEDEX?**
    *   It ensures fairness and enables parallel processing.
33. **Why does SPEEDEX's design include a preprocessing phase before equilibrium iteration?**
    *   To accelerate price computation by enabling logarithmic-time queries.
34. **Why do the algorithmic modifications from academic theory matter for SPEEDEX's practicality?**
    *   Because they enable SPEEDEX to be integrated efficiently in real-world blockchain settings.
35. **Why is there no economic loss or gain to the SPEEDEX auctioneer?**
    *   It reports market-clearing prices without making profit-driven choices.
36. **Why is fairness across trades a fundamental feature of SPEEDEX?**
    *   To ensure all market participants have equal access and pricing regardless of timing or order.
37. **Why does SPEEDEX process trades in every blockchain block?**
    *   To align batch settlement with blockchain consensus for timely finality and scalability.
38. **Why does SPEEDEX's trading logic fit the economics 101 demand-supply intuition?**
    *   Because it models market clearing through price adjustments based on supply and demand.
39. **Why is it important that the price computation process does not significantly slow down as the number of open offers increases?**
    *   To ensure consistent performance and scalability despite growing market activity.
40. **Why is SPEEDEX prototyped but not yet merged within the Stellar blockchain?**
    *   It represents ongoing research and development towards integrating advanced DEX capabilities into a major Layer-1 blockchain.

### Advanced-Level "Why" Questions and Answers

1.  **Why does SPEEDEX run entirely within a Layer-1 blockchain rather than across multiple rollups?**
    *   To avoid liquidity fragmentation, ensuring unified market depth and efficient trading without the complexity and trust assumptions of cross-rollup communication.
2.  **Why is using an Arrow-Debreu exchange market structure critical for SPEEDEX?**
    *   It fixes asset valuations within a batch, enabling fairness, eliminating internal arbitrage, and making trade operations commutative for parallel execution while preserving financial correctness.
3.  **Why is parallelism important in SPEEDEX trading?**
    *   It allows processing over 200,000 transactions per second by making trade operations commutative and batch-executable, fully leveraging multi-core server capabilities.
4.  **Why must SPEEDEX eliminate internal arbitrage opportunities?**
    *   To guarantee users get the best direct trade prices and prevent inefficiencies or exploitations that arise from trading through intermediate assets or complex multi-hop paths.
5.  **Why is preventing front-running attacks essential in DEX design?**
    *   To ensure fair market access, protect small traders from adverse price movements, and prevent manipulation that would otherwise increase effective bid-ask spreads.
6.  **Why does SPEEDEX use a batch trading model instead of continuous trades?**
    *   To process trades fairly at uniform exchange rates within a blockchain block, eliminating ordering dependencies, enhancing fairness, and enabling efficient parallel processing.
7.  **Why integrate SPEEDEX with the Stellar blockchain?**
    *   Stellar’s precisely designed transaction semantics, replicated state machine, and mission align well with SPEEDEX’s model, supporting scalability for future global payment volumes.
8.  **Why does SPEEDEX process trades against a virtual "auctioneer" rather than peer-to-peer?**
    *   It simplifies price discovery and computation by centralizing the valuation logic temporarily, ensuring consistency and eliminating the need for complex, individual path trades.
9.  **Why is economic efficiency a design priority for SPEEDEX?**
    *   To maximize liquidity, reduce bid-ask spreads, and improve price accuracy across asset pairs, thereby creating a more viable and attractive trading environment.
10. **Why is the scalability of transactions per second crucial for SPEEDEX?**
    *   To meet the demand of a global exchange environment with millions of active orders, supporting not just today's transaction volumes but those of coming decades.
11. **Why are financial correctness constraints vital in the valuation algorithm?**
    *   They ensure trades preserve the market's economic integrity, prevent issues like double-spends or financial losses to the system, and guarantee settlement fairness for all participants.
12. **Why is commutativity in trade operations beneficial?**
    *   It permits parallel processing without changing outcomes, allowing the system to leverage multi-core architectures effectively for high throughput and reduced latency.
13. **Why does SPEEDEX avoid fragmentation of market liquidity?**
    *   Fragmentation dilutes liquidity, increases slippage, and harms price discovery across different exchanges or layers, making trading less efficient and more costly.
14. **Why do traditional DEXes face limitations SPEEDEX aims to solve?**
    *   Existing DEX designs are often slow, expensive, inefficient, susceptible to front-running, and suffer from fragmented liquidity, failing to meet criteria for an ideal exchange.
15. **Why sophisticated algorithms are needed for market-clearing valuations on-chain?**
    *   To balance efficiency with correct, provably fair pricing in resource-constrained blockchain environments, while handling a large number of assets and offers.
16. **Why are batch-consistent exchange rates preferred?**
    *   They ensure all trades in a batch see the same market conditions and receive the exact same exchange rate, enhancing fairness and eliminating ordering advantages within a block.
17. **Why does SPEEDEX’s design improve small trader outcomes?**
    *   By preventing front-running attacks and ensuring uniform pricing within batches, it protects smaller traders from being disadvantaged by sophisticated market participants.
18. **Why is horizontal scaling important for SPEEDEX's future?**
    *   To accommodate growth and expanding user bases with increasing transaction demand, allowing the system to scale its throughput by adding more computational resources.
19. **Why is the market-clearing price computation asymptotically efficient?**
    *   To handle large-scale markets with tens of millions of open offers without significant performance degradation, ensuring the system remains practical as it grows.
20. **Why does SPEEDEX promote equal access to trades?**
    *   To eliminate preferential ordering advantages in the blockchain environment, ensuring all users, regardless of their resources or location, have equitable access to the world’s financial system.
21. **Why does SPEEDEX's on-chain implementation matter?**
    *   It enhances transparency, ensures auditability, and removes reliance on off-chain intermediaries, providing a truly decentralized and trustless trading experience.
22. **Why avoid multi-hop path trades in SPEEDEX?**
    *   They complicate pricing, introduce inefficiencies, and can create opportunities for internal arbitrage or lead to varying exchange rates for the same trade through different routes.
23. **Why is SPEEDEX economically efficient compared to traditional DEX models?**
    *   Due to its unique valuation algorithm and batch execution, which eliminate internal arbitrage, provide fair uniform pricing, and boost liquidity.
24. **Why does SPEEDEX require specialized parallel computing techniques?**
    *   To achieve its scalable transaction throughput by effectively utilizing multiple CPU cores and optimizing memory access patterns, which are typically challenging within smart contract environments.
25. **Why is integrating economic theory into DEX design beneficial?**
    *   It ensures the exchange operates with sound market principles, providing predictable and fair outcomes based on established economic models like the Arrow-Debreu exchange market.
26. **Why address front-running at the protocol level?**
    *   Protocol-level prevention, embedded in the system's core design, is more robust and systematic than reactive or application-layer measures, offering stronger guarantees against manipulation.
27. **Why does SPEEDEX's scalability benefit from batch processing?**
    *   Batches amortize computation costs over multiple trades, synchronize market state across a block, and, crucially, enable trades to be processed in parallel due to their commutative nature.
28. **Why is on-chain market-clearing valuation complex?**
    *   Because it requires solving large-scale equilibrium problems efficiently within the computational and gas-intensive constraints of a blockchain, making it impractical for many existing smart contracting languages.
29. **Why do SPEEDEX trades not give control to any single party?**
    *   To maintain true decentralization and reduce trust dependence on any central authority, aligning with the core principles of blockchain technology and ensuring egalitarian access.
30. **Why optimize SPEEDEX for multi-core servers?**
    *   To exploit hardware parallelism for significant performance gains, allowing the system to scale its transaction throughput by simply adding more CPU cores.
31. **Why does SPEEDEX's auctioneer model improve consistency?**
    *   It centralizes price setting temporarily within a batch without sacrificing decentralization, ensuring that all trades occurring simultaneously adhere to the same set of valuations.
32. **Why is a scalable DEX important for global payments?**
    *   To handle the immense volume and speed requirements of international transactions and remittances, facilitating seamless cross-border currency exchanges at low cost.
33. **Why is eliminating arbitrage important beyond fairness?**
    *   It stabilizes the market, improves liquidity provisioning by preventing value leakage, and ensures that the prices accurately reflect supply and demand without artificial distortions.
34. **Why does SPEEDEX prioritize reducing bid-ask spreads?**
    *   Lower spreads directly benefit traders by reducing their transaction costs, making the exchange more attractive and increasing market efficiency.
35. **Why is SPEEDEX prototype deployment significant?**
    *   It demonstrates the feasibility of integrating novel economic algorithms and advanced system designs onto a real-world Layer-1 blockchain, paving the way for future decentralized financial infrastructure.
36. **Why is SPEEDEX’s approach economically sound yet practically implementable?**
    *   It balances advanced market theory (Arrow-Debreu) with real computing constraints and practical algorithmic optimizations, making it both theoretically robust and deployable in a blockchain environment.
37. **Why is market-clearing valuation considered the core algorithmic challenge?**
    *   Because it underpins all pricing and fairness guarantees, requiring an efficient and accurate computation method that can keep up with blockchain block times.
38. **Why does SPEEDEX’s design prevent auction manipulation risks?**
    *   Through its fixed exchange rates within a batch and batch processing, it removes opportunities for malicious actors to influence prices or gain advantages through transaction ordering.
39. **Why are parallelizable trade operations rare in traditional exchanges?**
    *   Traditional exchanges often rely on strict ordering of trades to maintain consistency, which inherently limits parallel processing due to dependencies between operations.
40. **Why is SPEEDEX a candidate for powering future decentralized financial infrastructure?**
    *   Its combination of fairness, efficiency, scalability, and seamless blockchain integration meets the emerging needs of a global, decentralized financial system.

Bibliography
Behind the Scenes with SPEEDEX - Stellar. (2021). https://stellar.org/blog/developers/behind-the-scenes-with-speedex

blockchain_conference_paper/README.md at master - GitHub. (n.d.). https://github.com/jianyu-niu/blockchain_conference_paper/blob/master/README.md?plain=1

Building SPEEDEX – A Novel Design for a Scalable Decentralized ... (2021). https://stellar.org/blog/developers/building-speedex-a-novel-design-for-decentralized-exchanges

Efficient Distributed EXchange. (n.d.). https://web.stanford.edu/~ashishg/msande339/speedex-informs.pdf

Leveraging McKinsey’s MECE Framework in Digital Product Design. (2023). https://www.adrenalinmedia.com.au/insights/leveraging-mckinsey-s-mece-framework-in-digital-product-design

MECE Framework McKinsey - MBA Crystal Ball. (2024). https://www.mbacrystalball.com/blog/strategy/mece-framework/

MECE Principle - A Guide with Applied Examples | PrepLounge.com. (2024). https://www.preplounge.com/en/case-interview-basics/mece-principle

Newest “decentralized-exchange” Questions. (n.d.). https://ethereum.stackexchange.com/questions/tagged/decentralized-exchange

NSDI ’23 Call for Papers - USENIX. (2022). https://www.usenix.org/conference/nsdi23/call-for-papers

NSDI ’23 Technical Sessions - USENIX. (n.d.). https://www.usenix.org/conference/nsdi23/technical-sessions

parallel Questions &amp; answers | PDF - SlideShare. (n.d.). https://www.slideshare.net/slideshow/parallel-questions-amp-answers/60411410

[PDF] GGD-82-52 Agreement Needed on DOD Guidelines for ... - GAO. (n.d.). https://www.gao.gov/assets/ggd-82-52.pdf

[PDF] RingLeader: Efficiently Offloading Intra-Server Orchestration to NICs. (2023). https://www.usenix.org/system/files/nsdi23-lin.pdf

[PDF] Scalability of parallel algorithm-machine combinations. (n.d.). http://www.cs.iit.edu/~scs/psfiles/scalability94.pdf

[PDF] SPEEDEX - Decentralized EXchange. (2023). https://www.scs.stanford.edu/~geoff/slides/speedex_nsdi.pdf

[PDF] SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (2023). https://www.usenix.org/system/files/nsdi23-ramseyer.pdf

[PDF] Targeted Resource Management in Multi-tenant Distributed Systems. (2015). https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-mace.pdf

[PDF] The Broken Token Problem: Why Crypto Classification Remains ... (2024). https://scholarship.law.wm.edu/cgi/viewcontent.cgi?article=3282&context=facpubs

[PDF] The Evolution of Decentralized Exchange: Risks, Benefits, and ... (2024). https://wifpr.wharton.upenn.edu/wp-content/uploads/2024/07/WIFPR-Decentralized-Exchange-Harvey-Hasbrouck-and-Saleh.pdf

[PDF] Token Ecosystem Creation | Outlier Ventures. (n.d.). https://outlierventures.io/wp-content/uploads/2021/06/Token-Ecosystem-Creation-Outlier-Ventures-PDF.pdf

Protecting Decentralized Exchanges from State Derailment Defects. (2024). https://arxiv.org/html/2411.18935v2

scslab/speedex - GitHub. (2021). https://github.com/scslab/speedex

SPEEDEX: A Scalable, Parallelizable, and Economically Efficient ... (2023). https://www.usenix.org/conference/nsdi23/presentation/ramseyer

Types of Information and MECE Principle | by Denis Volkov - Medium. (2023). https://medium.com/@paralloid/types-of-information-and-mece-principle-ccc33f823809



Generated by Liner
https://getliner.com/search/s/5926611/t/86094086