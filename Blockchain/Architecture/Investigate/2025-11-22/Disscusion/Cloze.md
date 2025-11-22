1. Q: For Bitcoin’s original Layer 1 design that combines consensus, execution, and data availability in a single monolithic chain, what kind of on‑chain throughput are we actually talking about?
   A: **Researcher A:** Right, it’s surprisingly low in raw TPS terms—roughly in the single digits.

      **Engineer B:** Right, the investigations put it around 3–7 transactions per second on‑chain.

      **A:** Which is tiny compared to Visa‑style systems, but it matches Bitcoin’s choice to prioritize security and decentralization.

      **Product C:** So that 3–7 TPS number is the trade‑off: strong censorship resistance, limited Layer 1 throughput.


1. Q: Ethereum also started as a largely monolithic design. On its early base layer, what kind of transaction throughput did it typically achieve before rollups became central?
   A: **Engineer A:** In practice, the reports describe Ethereum’s early mainnet as handling on the order of tens of TPS.

      **Architect B:** More concretely, about 15–30 transactions per second on the base layer.

      **A:** Which explains why DeFi and NFT waves quickly hit scalability limits—15–30 TPS can’t handle global demand.

      **Product C:** Exactly. That 15–30 TPS window is what pushed the ecosystem toward Layer 2 rollups.


1. Q: When people talk about the blockchain “scalability trilemma”, which three properties are considered to be in tension?
   A: **Architect A:** Textbook one—the classic trio is decentralization, security, and scalability.

      **Engineer B:** So the idea is: you can’t usually maximize all three at once—improving one tends to pressure the others.

      **A:** Right. Every architecture we studied is basically choosing a point in that decentralization–security–scalability space.


1. Q: The investigations compare different state models. How do Bitcoin, Ethereum, and newer Move‑style chains differ here?
   A: **Researcher A:** At a high level, Bitcoin sticks with the UTXO model—unspent transaction outputs.

      **Engineer B:** Ethereum shifted to an account model instead.

      **A:** And Sui/Aptos go further with object‑ or resource‑oriented models.

      **B:** So if we summarize: Bitcoin → UTXO, Ethereum → account, Sui/Aptos → object/resource‑oriented.


1. Q: Ethereum’s “Merge” was a big milestone. When did it happen, and how much did it cut energy consumption?
   A: **Engineer A:** Historically, the Merge landed on September 15, 2022.

      **Researcher B:** And the energy impact was dramatic—about a 99.98% reduction.

      **A:** So: September 15, 2022, and roughly 99.98% lower energy use after moving to Proof‑of‑Stake.


1. Q: After The Merge, what consensus mechanism actually secures Ethereum instead of Proof‑of‑Work mining?
   A: **Engineer A:** Since the Merge, it’s fully on Proof‑of‑Stake now.

      **Architect B:** Right—validators stake ETH, propose and attest to blocks, and get rewarded or slashed accordingly.

      **A:** So when we talk about Ethereum post‑Merge, the consensus backbone is Proof‑of‑Stake.


1. Q: In Ethereum’s rollup‑centric roadmap, how much can Layer 2 rollups reduce costs and increase effective throughput compared to the base layer?
   A: **Researcher A:** On costs, the numbers in the investigations are pretty aggressive—rollups can cut transaction costs by about 10–100×.

      **Engineer B:** And that cost reduction translates into much higher effective throughput at the user level.

      **A:** So we should remember that 10–100× drop in costs as a core justification for the rollup‑centric strategy.


1. Q: EIP‑4844 (proto‑danksharding) introduced blob data space. Roughly how much did this cut typical rollup data costs?
   A: **Engineer A:** For EIP‑4844, the cited figure is around a 95% reduction.

      **Architect B:** That’s huge—95% lower data costs for rollups means sustainable low‑fee transactions on Layer 2.

      **A:** So, EIP‑4844 → new blob space → about 95% cost reduction for rollup data.


1. Q: In the layered architecture described in the investigations, what are the primary roles of Layer 0, Layer 1, and Layer 2?
   A: **Architect A:** Layer‑wise, Layer 0 focuses on interoperability and shared security.

      **Engineer B:** Layer 1 is about consensus and base security.

      **A:** And Layer 2 is where execution scaling happens.

      **B:** Plus, Layer 3 is mentioned as application‑specific customization—but the core trio is: interoperability at Layer 0, consensus at Layer 1, execution at Layer 2.


1. Q: Solana aims for high throughput at Layer 1. What special mechanism does it pair with Proof‑of‑Stake to order events before consensus?
   A: **Engineer A:** In Solana’s case, that’s Proof‑of‑History.

      **Researcher B:** Essentially a cryptographic clock that gives a verifiable ordering of events.

      **A:** So Solana combines Proof‑of‑Stake with Proof‑of‑History to sequence transactions before running consensus.


1. Q: Beyond consensus, which Solana components are highlighted in the investigations for transaction forwarding, block propagation, and parallel execution?
   A: **Engineer A:** On the networking side, Gulf Stream handles transaction forwarding.

      **Researcher B:** Turbine is for block propagation.

      **A:** And Sealevel is the parallel program execution engine.

      **B:** So the trio is: Gulf Stream, Turbine, and Sealevel.


1. Q: Marketing and technical materials often quote a theoretical upper‑bound TPS for Solana. What’s the number under ideal lab conditions?
   A: **Researcher A:** Marketing‑wise, the frequently cited figure is around 65,000 TPS.

      **Engineer B:** Right—“up to ~65,000 transactions per second” in idealized benchmarks.

      **A:** The key is to treat that 65,000 TPS as a theoretical limit, not everyday real‑world throughput.


1. Q: Between 2021 and 2024, what major reliability concern kept showing up for Solana mainnet?
   A: **Engineer A:** The big one was repeated network outages.

      **Researcher B:** Often tied to spam attacks or software bugs that stalled block production.

      **A:** So when we summarize Solana’s risk profile, we have to mention those outages as a key reliability issue.


1. Q: How does Polkadot’s interoperability model work at a high level, according to the investigations?
   A: **Architect A:** Conceptually, it centers on a relay chain that provides shared security.

      **Engineer B:** And that relay chain secures multiple parachains, which are sovereign blockchains.

      **A:** So the model is: a relay chain plus parachains, with shared security spreading across them.


1. Q: What economic mechanism do Polkadot parachain slot auctions rely on, and which token is locked up?
   A: **Researcher A:** Economically, projects bid for parachain slots by locking DOT.

      **Engineer B:** The idea is that locking significant amounts of DOT aligns their incentives with the network’s security.

      **A:** So parachain auctions → lock up DOT → economic skin in the game.


1. Q: Cosmos’s IBC protocol, launched around 2021, relies on what key component on each chain to verify cross‑chain messages?
   A: **Engineer A:** Mechanically, each chain runs a light client for the other chain.

      **Researcher B:** That light client verifies headers and Merkle proofs, so messages can be trusted without centralized custodians.

      **A:** So the core building block is the on‑chain light client.


1. Q: Early trusted multisig bridges like Ronin, Wormhole, and Poly Network used m‑of‑n signatures. What low threshold did some of them rely on, and why was that risky?
   A: **Researcher A:** In some early designs, thresholds went as low as 5‑of‑9.

      **Engineer B:** With 5‑of‑9, compromising just five keys lets an attacker drain the bridge.

      **A:** So 5‑of‑9 multisig was a concrete example of how concentrated and fragile those setups were.


1. Q: Roughly how much user value did the Ronin, Wormhole, and Poly Network bridge incidents lose in total, according to the investigations?
   A: **Researcher A:** In total, the combined losses exceeded $2 billion.

      **Engineer B:** That “>$2 billion” number is why bridge risk is treated as systemic, not just edge‑case.

      **A:** So we should remember: three hacks, more than $2 billion gone.


1. Q: Why were early custodial bridges considered more dangerous than the underlying blockchains they connected?
   A: **Architect A:** The core issue was that they centralized risk in the bridge validator set.

      **Engineer B:** Even if the base blockchains stayed secure, compromising that one bridge validator set could still steal funds.

      **A:** So, compared with trust‑minimized designs, these custodial bridges concentrated risk while the underlying blockchains remained secure.


1. Q: By 2024, how widely had Cosmos IBC been adopted, and roughly how much cross‑chain traffic did it handle annually?
   A: **Researcher A:** Adoption‑wise, it reached on the order of about 120 chains.

      **Engineer B:** And it was moving tens of millions of cross‑chain transfers per year inside that ecosystem.

      **A:** So the headline is: ~120 chains and tens of millions of IBC transfers annually.


1. Q: What is Polkadot’s XCMP (Cross‑Consensus Message Passing) leveraging to avoid each chain bootstrapping its own full security model?
   A: **Architect A:** For XCMP, it leans on the relay chain validators.

      **Engineer B:** Since those validators already secure all parachains together, they can safely pass messages without each chain re‑implementing its own independent security model.

      **A:** In other words, XCMP rides on shared security instead of duplicating it.


1. Q: The investigations group interoperability designs into several models. What are the three main ones plus the emerging fourth category?
   A: **Researcher A:** At a high level, the first category is trusted multisig bridges.

      **Engineer B:** Second, light‑client‑based protocols like IBC.

      **A:** Third, shared‑security frameworks like Polkadot’s XCMP.

      **B:** And as a fourth, emerging category, ZK‑based bridges.


1. Q: ZK‑based bridges change the trust model. What do they use to let a destination chain verify a source‑chain state transition, and what’s the main cost?
   A: **Engineer A:** Trust‑wise, they use succinct validity proofs—zero‑knowledge proofs that attest to a source‑chain state transition.

      **Researcher B:** The downside is high proof generation latency or cost.

      **A:** So the trade‑off is: stronger trust‑minimization via proofs, at the price of higher proof generation latency or cost.


1. Q: Move‑based platforms like Aptos and Sui talk about “resources” in their programming model. What does that mean for key assets on‑chain?
   A: **Engineer A:** In Move‑style systems, key assets are modeled as resources.

      **Researcher B:** Resources can’t be implicitly copied or destroyed—they must move or be explicitly handled.

      **A:** That resource treatment is what reduces many common smart contract vulnerabilities.


1. Q: Aptos’s Block‑STM engine is often cited in performance discussions. What execution approach does it use?
   A: **Engineer A:** Execution‑wise, it applies optimistic concurrency control.

      **Researcher B:** Many transactions run in parallel, and any that conflict are rolled back and retried.

      **A:** So Block‑STM is basically optimistic concurrency control for parallel transaction execution.


1. Q: In benchmarks, what order of magnitude throughput have Aptos and Sui demonstrated in controlled tests?
   A: **Researcher A:** Benchmark‑wise, the reports mention high five‑ to six‑figure TPS ranges.

      **Engineer B:** One headline number is around 100,000+ TPS in controlled tests.

      **A:** So “~100,000 TPS” is the rough benchmark figure we should remember, with the caveat that it’s in lab conditions.


1. Q: What key hardware‑related trade‑off do many high‑throughput chains make compared with more conservative designs?
   A: **Architect A:** The trade‑off is they expect validators to run more powerful hardware.

      **Engineer B:** Plus higher‑bandwidth network links.

      **A:** So they gain throughput, but at the cost of stricter hardware assumptions for validators.


1. Q: By 2025, the investigations group L1 architectures into three broad families. How do they characterize those families?
   A: **Researcher A:** Broadly, the first family is conservative UTXO plus simple scripts—Bitcoin‑like designs.

      **Engineer B:** Second, general‑purpose account‑based smart contracts, like Ethereum.

      **A:** Third, aggressively concurrent parallel or Move‑based designs, like Solana, Sui, and Aptos.

      **B:** So the three buckets are: UTXO, account‑based, and aggressively concurrent Move/parallel.


1. Q: Under the EU’s MiCA framework, many user‑facing crypto businesses fall into which regulated category, and what does that imply?
   A: **Policy A:** Under MiCA, they’re treated as Crypto‑Asset Service Providers—CASPs.

      **Researcher B:** CASP status means they must obtain authorization, comply with AML/KYC, and maintain local governance.

      **A:** So MiCA essentially pulls many exchanges, custodians, and similar actors into the CASP regime.


1. Q: MiCA also introduces a “significant CASP” category. What’s the user threshold for that designation?
   A: **Policy A:** The threshold is more than 15 million active EU users.

      **Researcher B:** Crossing that 15‑million line triggers enhanced supervision.

      **A:** So 15 million active EU users is the critical number to watch.


1. Q: According to the investigations, how is MiCA’s rollout phased for stablecoins, broader CASP licensing, and the TFR “travel rule”?
   A: **Policy A:** Timeline‑wise, stablecoin rules start from mid‑2024.

      **Researcher B:** Broader CASP licensing rolls out through 2025–2026.

      **A:** And the Transfer of Funds Regulation travel rule for crypto transfers kicked in from December 2024.

      **B:** So the sequence is: mid‑2024 for stablecoins, 2025–2026 for CASP licensing, and December 2024 for the travel rule.


1. Q: In MiCA’s architecture‑driven view, which entities are clearly CASPs, and who might sit outside the definition?
   A: **Policy A:** Concretely, staking pools, custodial wallets, centralized bridges, and some sequencer operators are obvious CASPs.

      **Researcher B:** Base‑layer validators that validate only on their own account often fall outside many interpretations.

      **A:** So the line is drawn more around service providers—like pools and bridges—than around individual validators.


1. Q: From the U.S. perspective summarized in the investigations, how do the SEC and CFTC split focus over crypto activities?
   A: **Policy A:** In the U.S., the SEC has focused heavily on centralized staking programs as potential securities offerings.

      **Researcher B:** Meanwhile, the CFTC looks more at derivatives and some spot markets.

      **A:** So SEC → staking and securities, CFTC → derivatives and some spot oversight.


1. Q: How does the modular Ethereum‑style stack change where regulatory exposure tends to concentrate, compared with more monolithic chains?
   A: **Architect A:** Structurally, in modular stacks exposure shifts toward sequencers, bridges, and staking businesses.

      **Policy B:** Monolithic chains, by contrast, concentrate more exposure on large validator operators and infrastructure providers.

      **A:** So the same economic activity ends up regulated at different layers, depending on whether the stack is modular or monolithic.


1. Q: What does the Nakamoto Coefficient measure in the context of blockchain security?
   A: **Researcher A:** Formally, it’s the minimum number of independent entities—like validators or mining pools—whose collusion could corrupt the network.

      **Engineer B:** Lower coefficient means fewer actors need to collude, so higher centralization risk.

      **A:** So the Nakamoto Coefficient quantifies how many entities you’d need to control to corrupt or control the chain.


1. Q: What consensus mechanism did Bitcoin originally use to prioritize security and censorship resistance over throughput and energy efficiency?
   A: **Engineer A:** Originally, it relied on Proof‑of‑Work.

      **Researcher B:** Specifically, a Proof‑of‑Work mechanism where miners solve computational puzzles.

      **A:** So Bitcoin’s design choice was Proof‑of‑Work, accepting energy cost for stronger security and censorship resistance.


1. Q: Ethereum’s account‑based design and rich smart‑contract layer led to rapid state growth. By the early 2020s, what kind of state sizes were typical for full nodes?
   A: **Researcher A:** Storage‑wise, the reports talk about tens to low hundreds of gigabytes.

      **Engineer B:** So a full node might need on the order of tens of GB, pushing toward low hundreds of GB as the state ballooned.

      **A:** That tens‑to‑hundreds of gigabytes range is a concrete symptom of the account‑based, high‑usage model.


1. Q: In the rollup‑centric danksharding roadmap, what’s the target number of data shards, and what ecosystem‑wide throughput do they aim for together with Layer 2s?
   A: **Architect A:** Roadmap‑wise, the plan is for 64 data shards.

      **Researcher B:** And with those shards plus rollups, the goal is roughly 100k+ TPS across the ecosystem.

      **A:** So the shorthand is: 64 shards targeting about 100k+ TPS in aggregate.


1. Q: What central qualitative lesson do the investigations draw about why new blockchain architecture generations appear?
   A: **Researcher A:** Big picture, they mainly appear to fix specific limitations of previous designs.

      **Engineer B:** Things like scalability, security, or interoperability, rather than purely academic improvements.

      **A:** So each generation is a reaction to concrete pain points—scalability, security, interoperability—more than a quest for elegance alone.


1. Q: Even with secure base layers, which component does the report say remains a systemic risk, capable of causing huge losses when it fails?
   A: **Researcher A:** In practice, bridges.

      **Engineer B:** The reports emphasize that weaknesses in bridge design and implementation can still lead to multi‑hundred‑million‑dollar losses.

      **A:** So even if the L1s are solid, bridge failures remain a systemic risk.


1. Q: Finally, what market projection do the investigations cite for blockchain interoperability from 2025 to 2035?
   A: **Researcher A:** Projection‑wise, they estimate growth from about $332.8 million in 2025.

      **Engineer B:** Up to roughly $1.83 billion by 2035.

      **A:** So the forecast is $332.8 million → $1.83 billion for the interoperability market over that decade.
