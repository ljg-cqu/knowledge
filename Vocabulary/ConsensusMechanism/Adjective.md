# ConsensusMechanism Vocabulary: Adjectives

1. **Adjective**: Byzantine (non-gradable)
   **Meaning**: 
   - Relating to arbitrary or malicious behavior by network participants who may deviate from protocol rules in any way
   - *(Technical)* Describing fault tolerance that accounts for nodes acting adversarially, not just failing passively
   
   **Synonyms**: adversarial, malicious, arbitrary, hostile, faulty
   
   **Antonyms**: honest, cooperative, compliant, benign, crash-only
   
   **When to Use**: When discussing fault models, consensus security, or protocol assumptions about participant behavior.
   
   **When NOT to Use**: Don't confuse Byzantine faults (arbitrary behavior) with crash faults (simple failures). Use "Byzantine" for adversarial contexts.
   
   **Common Phrases**: 
   - Byzantine fault tolerance
   - Byzantine node
   - Byzantine behavior
   - Byzantine generals problem
   - Byzantine agreement
   
   **Root Analysis**: Byzantine (relating to Byzantium) - named after Byzantine Generals Problem
   
   **Etymology**: Byzantium (ancient city) → Byzantine Generals Problem (Lamport, 1982) → Distributed systems fault model
   
   **Examples [Casual]**: 
   - Byzantine nodes might lie, send conflicting messages, or try to disrupt consensus.
   - The protocol can handle up to one-third Byzantine validators.
   
   **Examples [Formal]**: 
   - Byzantine fault-tolerant consensus protocols achieve agreement despite the presence of adversarial nodes.
   - The protocol assumes a partially synchronous network with up to f Byzantine participants among 3f+1 nodes.

1. **Adjective**: deterministic (non-gradable)
   **Meaning**: 
   - Producing the same result every time given the same input, without randomness or probability
   - *(Technical)* Providing guaranteed finality or outcomes rather than probabilistic convergence
   
   **Synonyms**: definite, certain, guaranteed, predictable, absolute
   
   **Antonyms**: probabilistic, stochastic, random, uncertain, variable
   
   **When to Use**: When contrasting BFT consensus (deterministic finality) with Nakamoto consensus (probabilistic finality).
   
   **When NOT to Use**: Clarify whether discussing deterministic finality, deterministic execution, or deterministic selection.
   
   **Common Phrases**: 
   - deterministic finality
   - deterministic consensus
   - deterministic outcome
   - deterministic selection
   - deterministic behavior
   
   **Root Analysis**: determine (decide definitively) + -istic (characterized by)
   
   **Etymology**: Latin "determinare" (limit/decide) → "deterministic" in mathematics/computing → Blockchain finality type
   
   **Examples [Casual]**: 
   - BFT consensus provides deterministic finality—once confirmed, it's final.
   - Deterministic protocols don't rely on probabilistic convergence.
   
   **Examples [Formal]**: 
   - Byzantine fault-tolerant protocols provide deterministic finality within a single round under honest supermajority.
   - Deterministic leader selection eliminates randomness-based timing attacks.

1. **Adjective**: probabilistic (non-gradable)
   **Meaning**: 
   - Based on likelihood and statistical confidence rather than absolute certainty
   - *(Technical)* Describing finality that strengthens over time but never reaches 100% mathematical certainty
   
   **Synonyms**: statistical, stochastic, likelihood-based, non-deterministic, convergent
   
   **Antonyms**: deterministic, certain, guaranteed, definite, absolute
   
   **When to Use**: When discussing Nakamoto consensus, Bitcoin/Ethereum PoW, or confirmation requirements.
   
   **When NOT to Use**: Don't use for BFT-style instant finality. Specify that finality becomes exponentially certain over time.
   
   **Common Phrases**: 
   - probabilistic finality
   - probabilistic consensus
   - probabilistic guarantee
   - probabilistic convergence
   - probabilistic model
   
   **Root Analysis**: probable (likely) + -istic (characterized by)
   
   **Etymology**: Latin "probabilis" (likely) → "probabilistic" in mathematics → Blockchain finality type (Nakamoto, 2008)
   
   **Examples [Casual]**: 
   - Bitcoin uses probabilistic finality—transactions become more secure with each block.
   - Probabilistic consensus means there's always a tiny chance of reversal.
   
   **Examples [Formal]**: 
   - Probabilistic finality in Nakamoto consensus exhibits exponential security growth with confirmation depth.
   - The protocol achieves probabilistic convergence with probability approaching unity as blockchain length increases.

1. **Adjective**: decentralized (gradable)
   **Meaning**: 
   - Distributed across many independent participants without central authority or single point of control
   - *(Technical)* Having consensus power dispersed such that no single entity or small coalition can unilaterally control outcomes
   
   **Synonyms**: distributed, dispersed, peer-to-peer, non-hierarchical, autonomous
   
   **Antonyms**: centralized, concentrated, hierarchical, controlled, monopolized
   
   **When to Use**: When discussing network architecture, validator distribution, or protocol governance.
   
   **When NOT to Use**: "Decentralized" is spectrum—specify degree or metrics (Nakamoto coefficient, Gini coefficient).
   
   **Common Phrases**: 
   - decentralized network
   - decentralized consensus
   - highly decentralized
   - decentralized system
   - decentralization degree
   
   **Root Analysis**: de- (away from) + central + -ized (made to be)
   
   **Etymology**: Latin "centrum" (center) → "decentralized" in organizational theory → Blockchain architecture principle
   
   **Examples [Casual]**: 
   - Bitcoin is highly decentralized with thousands of independent miners.
   - More decentralized systems are harder to attack or censor.
   
   **Examples [Formal]**: 
   - Protocol decentralization is measured by validator distribution, geographic dispersion, and client diversity.
   - Decentralized consensus mechanisms sacrifice efficiency for censorship resistance and fault tolerance.

1. **Adjective**: permissionless (non-gradable)
   **Meaning**: 
   - Allowing anyone to participate without requiring approval or identity verification
   - *(Technical)* Having open validator sets where participation depends on resources (stake/hashpower) rather than authorization
   
   **Synonyms**: open, unrestricted, censorship-resistant, authorization-free, public
   
   **Antonyms**: permissioned, restricted, authorized, controlled, private
   
   **When to Use**: When discussing public blockchains, validator entry barriers, or network accessibility.
   
   **When NOT to Use**: Distinguish permissionless (open participation) from trustless (no trust assumptions). Both concepts are related but distinct.
   
   **Common Phrases**: 
   - permissionless network
   - permissionless participation
   - permissionless blockchain
   - permissionless consensus
   - permissionless entry
   
   **Root Analysis**: permission + -less (without)
   
   **Etymology**: "Permission" (authorization) + "-less" (without) → Blockchain context (2008+)
   
   **Examples [Casual]**: 
   - Bitcoin is permissionless—anyone can become a miner without asking.
   - Permissionless systems let you join without KYC or approval.
   
   **Examples [Formal]**: 
   - Permissionless consensus mechanisms enable open participation subject only to economic or computational constraints.
   - The protocol maintains permissionless validator entry to preserve censorship resistance and decentralization.

1. **Adjective**: asynchronous (non-gradable)
   **Meaning**: 
   - Having no assumptions about message delivery timing or global clock synchronization
   - *(Technical)* Operating without guaranteed bounds on network latency or processing delays
   
   **Synonyms**: timing-independent, unbounded-delay, clockless, unsynchronized
   
   **Antonyms**: synchronous, time-bounded, clock-synchronized, instantaneous
   
   **When to Use**: When discussing network models, consensus assumptions, or protocol guarantees under varying conditions.
   
   **When NOT to Use**: Distinguish asynchronous (no timing assumptions) from partially synchronous (eventual timing bounds).
   
   **Common Phrases**: 
   - asynchronous network
   - asynchronous consensus
   - asynchronous model
   - asynchronous communication
   - asynchronous assumption
   
   **Root Analysis**: a- (without) + syn- (together) + chron (time) + -ous (having quality)
   
   **Etymology**: Greek "a-" (without) + "synchronos" (simultaneous) → Distributed systems model (1980s)
   
   **Examples [Casual]**: 
   - Asynchronous networks don't assume messages arrive in any particular time.
   - Real-world networks are mostly asynchronous with unpredictable delays.
   
   **Examples [Formal]**: 
   - Asynchronous Byzantine consensus protocols achieve liveness without timing assumptions but sacrifice efficiency.
   - The FLP impossibility theorem proves deterministic consensus is impossible in fully asynchronous systems with even one crash fault.

1. **Adjective**: synchronous (non-gradable)
   **Meaning**: 
   - Having strict assumptions about maximum message delivery time and coordinated clocks
   - *(Technical)* Operating under bounded network latency where messages arrive within known time limits
   
   **Synonyms**: time-bounded, coordinated, clock-synchronized, lockstep
   
   **Antonyms**: asynchronous, unbounded, timing-free, desynchronized
   
   **When to Use**: When discussing theoretical network models or protocols requiring timing assumptions.
   
   **When NOT to Use**: Real networks are rarely truly synchronous. Most practical protocols assume partial synchrony.
   
   **Common Phrases**: 
   - synchronous model
   - synchronous network
   - synchronous assumption
   - synchronous communication
   - synchronous consensus
   
   **Root Analysis**: syn- (together) + chron (time) + -ous (having quality)
   
   **Etymology**: Greek "synchronos" (simultaneous) → Distributed systems model (1980s)
   
   **Examples [Casual]**: 
   - Synchronous models assume messages always arrive within a fixed time.
   - Few real systems are truly synchronous because networks have variable delays.
   
   **Examples [Formal]**: 
   - Synchronous consensus protocols achieve optimal efficiency but fail under timing violations.
   - The synchronous model enables deterministic consensus with f < n/2 Byzantine faults.

1. **Adjective**: malicious (gradable)
   **Meaning**: 
   - Intentionally acting to harm the network, violate rules, or disrupt consensus
   - *(Technical)* Exhibiting Byzantine behavior designed to compromise safety or liveness
   
   **Synonyms**: adversarial, hostile, Byzantine, attacking, dishonest
   
   **Antonyms**: honest, benign, cooperative, compliant, trustworthy
   
   **When to Use**: When discussing threat models, attack scenarios, or validator misbehavior.
   
   **When NOT to Use**: Distinguish malicious (intentional harm) from faulty (accidental errors) or rational (self-interested) behavior.
   
   **Common Phrases**: 
   - malicious node
   - malicious validator
   - malicious behavior
   - malicious actor
   - malicious attack
   
   **Root Analysis**: malice (intent to harm) + -ous (full of)
   
   **Etymology**: Latin "malitia" (badness) → "malicious" → Distributed systems threat model
   
   **Examples [Casual]**: 
   - Malicious validators might try to double-spend or disrupt the network.
   - The protocol can tolerate some malicious nodes without failing.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance accounts for malicious participants who deviate arbitrarily from protocol specifications.
   - The protocol remains secure under malicious coalitions comprising fewer than one-third of validators.

1. **Adjective**: honest (non-gradable)
   **Meaning**: 
   - Following protocol rules correctly and faithfully without deviation
   - *(Technical)* Executing consensus algorithms as specified without malicious or erroneous behavior
   
   **Synonyms**: compliant, faithful, correct, trustworthy, rule-following
   
   **Antonyms**: malicious, Byzantine, dishonest, faulty, adversarial
   
   **When to Use**: When discussing protocol assumptions, security models, or validator behavior.
   
   **When NOT to Use**: "Honest" assumes both correct implementation and non-malicious intent. Distinguish from "rational" (self-interested).
   
   **Common Phrases**: 
   - honest majority
   - honest node
   - honest validator
   - honest behavior
   - honest participation
   
   **Root Analysis**: honest (honorable/truthful) - from Latin "honestus"
   
   **Etymology**: Latin "honestus" (honorable) → Protocol compliance in distributed systems
   
   **Examples [Casual]**: 
   - Consensus works if most validators are honest and follow the rules.
   - Honest nodes verify everything and reject invalid blocks.
   
   **Examples [Formal]**: 
   - Byzantine fault-tolerant protocols achieve consensus under an honest supermajority assumption of 2f+1 among 3f+1 nodes.
   - Honest validator behavior is incentivized through rewards and enforced through slashing mechanisms.

1. **Adjective**: economic (non-gradable)
   **Meaning**: 
   - Related to financial incentives, costs, and rational decision-making by participants
   - *(Technical)* Pertaining to game-theoretic analysis of validator behavior under monetary rewards and penalties
   
   **Synonyms**: financial, monetary, incentive-based, cost-related, game-theoretic
   
   **Antonyms**: non-economic, altruistic, technical, computational, cryptographic
   
   **When to Use**: When discussing PoS security, validator incentives, or mechanism design.
   
   **When NOT to Use**: Distinguish economic security (based on incentives) from cryptographic security (based on mathematics).
   
   **Common Phrases**: 
   - economic security
   - economic incentive
   - economic finality
   - economic penalty
   - economic mechanism
   
   **Root Analysis**: economy (resource management) + -ic (pertaining to)
   
   **Etymology**: Greek "oikonomia" (household management) → "economic" → Blockchain incentive analysis
   
   **Examples [Casual]**: 
   - PoS relies on economic incentives rather than just computational power.
   - Economic penalties make attacks expensive and unprofitable.
   
   **Examples [Formal]**: 
   - Economic finality is achieved when reverting transactions costs more than potential gains from attack.
   - The protocol employs economic mechanisms to align rational validator behavior with protocol objectives.

1. **Adjective**: finalized (non-gradable)
   **Meaning**: 
   - Permanently committed and irreversible, immune to reorganization
   - *(Technical)* Having achieved consensus finality such that reversal is impossible or economically infeasible
   
   **Synonyms**: committed, irreversible, permanent, settled, confirmed absolutely
   
   **Antonyms**: tentative, reversible, unconfirmed, pending, provisional
   
   **When to Use**: In BFT consensus contexts or after Casper finalization checkpoints in Ethereum.
   
   **When NOT to Use**: Don't use for probabilistic confirmation. "Finalized" implies deterministic irreversibility.
   
   **Common Phrases**: 
   - finalized block
   - finalized transaction
   - finalized state
   - finalized checkpoint
   - fully finalized
   
   **Root Analysis**: final + -ized (made to be)
   
   **Etymology**: Latin "finalis" (final) → "finalized" → Blockchain irreversible commitment
   
   **Examples [Casual]**: 
   - Once a block is finalized, it can never be reversed.
   - Finalized transactions are completely safe from reorganization.
   
   **Examples [Formal]**: 
   - Finalized blocks represent irreversible commitment points in the canonical blockchain history.
   - The protocol finalizes checkpoints when they receive attestations from at least two-thirds of validators.

1. **Adjective**: slashable (non-gradable)
   **Meaning**: 
   - Subject to stake confiscation as penalty for protocol violations
   - *(Technical)* Describing validator behavior that triggers penalty mechanisms through provable rule violations
   
   **Synonyms**: penalizable, punishable, forfeit-able, violation-triggering
   
   **Antonyms**: safe, compliant, unpunishable, protected, exempt
   
   **When to Use**: In proof-of-stake contexts when discussing validator behavior and penalty conditions.
   
   **When NOT to Use**: Only applicable to PoS systems with slashing mechanisms. Specify the slashing condition.
   
   **Common Phrases**: 
   - slashable offense
   - slashable behavior
   - slashable violation
   - slashable condition
   - slashable action
   
   **Root Analysis**: slash (penalty) + -able (capable of being)
   
   **Etymology**: "Slash" (cut/penalize) + "-able" → PoS penalty eligibility (2014+)
   
   **Examples [Casual]**: 
   - Double-signing is a slashable offense that costs you part of your stake.
   - Validators avoid slashable behavior to protect their deposits.
   
   **Examples [Formal]**: 
   - Slashable offenses include equivocation, surround voting, and provable protocol violations.
   - The protocol defines cryptographically verifiable slashable conditions to deter malicious behavior.

1. **Adjective**: canonical (non-gradable)
   **Meaning**: 
   - Recognized as the authoritative or official chain among competing alternatives
   - *(Technical)* Representing the agreed-upon blockchain history according to fork choice rules
   
   **Synonyms**: authoritative, official, accepted, valid, main
   
   **Antonyms**: forked, alternative, competing, orphaned, rejected
   
   **When to Use**: When discussing fork choice, chain selection, or which branch nodes follow.
   
   **When NOT to Use**: During forks, multiple branches may temporarily claim to be canonical. Specify perspective.
   
   **Common Phrases**: 
   - canonical chain
   - canonical history
   - canonical block
   - canonical state
   - canonical branch
   
   **Root Analysis**: canon (standard/rule) + -ical (pertaining to)
   
   **Etymology**: Greek "kanon" (rule) → "canonical" (authoritative) → Blockchain main chain designation
   
   **Examples [Casual]**: 
   - Nodes follow the canonical chain—the one with most accumulated work.
   - After a fork, one branch becomes canonical and the other orphaned.
   
   **Examples [Formal]**: 
   - Fork choice rules deterministically identify the canonical chain from competing branches.
   - The canonical chain represents the agreed-upon transaction history across honest validators.

1. **Adjective**: adversarial (gradable)
   **Meaning**: 
   - Acting in opposition to protocol goals, potentially attempting attacks or disruption
   - *(Technical)* Exhibiting behavior designed to compromise security, violate assumptions, or exploit vulnerabilities
   
   **Synonyms**: hostile, antagonistic, attacking, malicious, opposing
   
   **Antonyms**: cooperative, honest, benign, compliant, supportive
   
   **When to Use**: When discussing security analysis, threat models, or worst-case assumptions.
   
   **When NOT to Use**: Distinguish adversarial (actively harmful) from merely rational (self-interested) or faulty (accidentally wrong).
   
   **Common Phrases**: 
   - adversarial node
   - adversarial behavior
   - adversarial environment
   - adversarial attack
   - adversarial model
   
   **Root Analysis**: adversary (opponent) + -ial (relating to)
   
   **Etymology**: Latin "adversarius" (opponent) → "adversarial" → Security analysis context
   
   **Examples [Casual]**: 
   - The protocol is designed to work even with adversarial participants.
   - Adversarial nodes try to break consensus or steal funds.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance ensures safety under adversarial coalitions comprising up to one-third of nodes.
   - Adversarial models assume rational attackers seeking to maximize damage or profit.

1. **Adjective**: atomic (non-gradable)
   **Meaning**: 
   - Executing as an indivisible unit that either completes entirely or fails entirely without partial effects
   - *(Technical)* Ensuring all-or-nothing state transitions without intermediate inconsistent states
   
   **Synonyms**: indivisible, all-or-nothing, unitary, complete, transactional
   
   **Antonyms**: divisible, partial, incremental, interruptible, incomplete
   
   **When to Use**: When discussing transaction properties, state transitions, or cross-shard operations.
   
   **When NOT to Use**: "Atomic" in blockchain differs from "atomic" in physics. Specify the all-or-nothing property clearly.
   
   **Common Phrases**: 
   - atomic transaction
   - atomic operation
   - atomic execution
   - atomic commit
   - atomic swap
   
   **Root Analysis**: atom (indivisible) + -ic (pertaining to)
   
   **Etymology**: Greek "atomos" (indivisible) → Database transactions (1970s) → Blockchain operations
   
   **Examples [Casual]**: 
   - Atomic transactions either complete fully or fail completely—no halfway states.
   - Atomic swaps let you trade crypto without trusting an exchange.
   
   **Examples [Formal]**: 
   - Atomic execution ensures state transitions maintain consistency properties despite concurrent operations.
   - Cross-shard transactions employ two-phase commit protocols to achieve atomic execution across partitions.

1. **Adjective**: optimal (non-gradable)
   **Meaning**: 
   - Achieving the best possible performance or security within theoretical or practical constraints
   - *(Technical)* Reaching efficiency bounds proven by impossibility results or lower bounds
   
   **Synonyms**: best possible, maximal, ideal, most efficient, theoretically best
   
   **Antonyms**: suboptimal, inefficient, improvable, wasteful, inferior
   
   **When to Use**: When discussing protocol efficiency, resource usage, or theoretical performance limits.
   
   **When NOT to Use**: Specify optimization target (latency, throughput, fault tolerance, communication complexity).
   
   **Common Phrases**: 
   - optimal efficiency
   - optimal performance
   - optimal resilience
   - optimal protocol
   - optimal tradeoff
   
   **Root Analysis**: optimum (best) + -al (pertaining to)
   
   **Etymology**: Latin "optimus" (best) → "optimal" → Performance analysis context
   
   **Examples [Casual]**: 
   - This protocol achieves optimal efficiency for BFT consensus.
   - Optimal means you can't do better without sacrificing something else.
   
   **Examples [Formal]**: 
   - The protocol achieves optimal resilience of f < n/3 Byzantine faults for asynchronous consensus.
   - Communication complexity is optimal at O(n²) messages per round given the impossibility of subquadratic BFT.

1. **Adjective**: permissioned (non-gradable)
   **Meaning**: 
   - Requiring authorization or approval to participate, with controlled validator membership
   - *(Technical)* Having closed validator sets where participation requires identity verification or invitation
   
   **Synonyms**: authorized, restricted, controlled, private, closed
   
   **Antonyms**: permissionless, open, unrestricted, public, censorship-resistant
   
   **When to Use**: When discussing enterprise blockchains, private networks, or consortium chains.
   
   **When NOT to Use**: Don't confuse permissioned participation with permissioned transactions. Specify what requires permission.
   
   **Common Phrases**: 
   - permissioned blockchain
   - permissioned network
   - permissioned consensus
   - permissioned validator
   - permissioned access
   
   **Root Analysis**: permission (authorization) + -ed (having)
   
   **Etymology**: "Permission" + "-ed" → Blockchain access control model (2015+)
   
   **Examples [Casual]**: 
   - Permissioned blockchains only let approved organizations become validators.
   - Banks often use permissioned systems where they control who participates.
   
   **Examples [Formal]**: 
   - Permissioned consensus mechanisms sacrifice censorship resistance for efficiency and regulatory compliance.
   - Permissioned networks employ identity-based access control and governance-driven validator selection.

1. **Adjective**: scalable (gradable)
   **Meaning**: 
   - Capable of handling increasing transaction volume or users without proportional resource increases
   - *(Technical)* Achieving throughput growth that outpaces linear scaling with validator or resource additions
   
   **Synonyms**: expandable, growable, high-capacity, elastic, extensible
   
   **Antonyms**: limited, bottlenecked, constrained, non-scalable, fixed-capacity
   
   **When to Use**: When discussing blockchain performance, sharding, layer-2 solutions, or capacity improvements.
   
   **When NOT to Use**: Specify scalability dimension (throughput, validator set, storage) as different aspects scale differently.
   
   **Common Phrases**: 
   - scalable consensus
   - scalable architecture
   - highly scalable
   - scalable solution
   - scalability limit
   
   **Root Analysis**: scale (size/extent) + -able (capable of)
   
   **Etymology**: "Scale" (size) + "-able" → Computing capacity context → Blockchain performance
   
   **Examples [Casual]**: 
   - Bitcoin isn't very scalable—it only handles about 7 transactions per second.
   - Sharding makes blockchains more scalable by processing transactions in parallel.
   
   **Examples [Formal]**: 
   - Scalable consensus protocols achieve throughput growth proportional to network partitioning or validator specialization.
   - The protocol employs committee-based validation to achieve logarithmic communication complexity and linear scalability.

1. **Adjective**: immutable (non-gradable)
   **Meaning**: 
   - Unchangeable once recorded, resistant to alteration or deletion
   - *(Technical)* Protected by cryptographic and consensus mechanisms that make historical modification infeasible
   
   **Synonyms**: unchangeable, permanent, unalterable, indelible, tamper-proof
   
   **Antonyms**: mutable, changeable, alterable, modifiable, erasable
   
   **When to Use**: When discussing blockchain's core property of historical permanence and tamper resistance.
   
   **When NOT to Use**: Immutability is probabilistic in some systems (Nakamoto consensus) vs. absolute in others (BFT finality).
   
   **Common Phrases**: 
   - immutable ledger
   - immutable record
   - immutable history
   - immutable data
   - immutability guarantee
   
   **Root Analysis**: im- (not) + mut (change) + -able (capable of)
   
   **Etymology**: Latin "immutabilis" (unchangeable) → Blockchain permanence property
   
   **Examples [Casual]**: 
   - Blockchain records are immutable—once written, they can't be changed.
   - Immutability means you have a permanent audit trail.
   
   **Examples [Formal]**: 
   - Cryptographic hash chains and consensus mechanisms ensure blockchain immutability against adversarial modification.
   - Immutability is achieved through computational or economic barriers that make history rewriting infeasible.

1. **Adjective**: censorship-resistant (gradable)
   **Meaning**: 
   - Difficult or impossible for any party to prevent valid transactions from being processed
   - *(Technical)* Maintaining liveness and inclusion guarantees despite attempts by validators to exclude specific transactions
   
   **Synonyms**: unstoppable, uncensorable, inclusion-guaranteed, permissionless, suppression-resistant
   
   **Antonyms**: censorable, controllable, excludable, gatekept, filterable
   
   **When to Use**: When discussing decentralization benefits, validator behavior, or protocol goals.
   
   **When NOT to Use**: Censorship resistance is a spectrum depending on decentralization degree and economic costs.
   
   **Common Phrases**: 
   - censorship-resistant network
   - censorship-resistant protocol
   - censorship-resistant transactions
   - censorship resistance guarantee
   - highly censorship-resistant
   
   **Root Analysis**: censorship (suppression) + resistant (opposing)
   
   **Etymology**: "Censorship" + "resistant" → Blockchain protocol property (2008+)
   
   **Examples [Casual]**: 
   - Bitcoin is censorship-resistant because no one can block your transactions.
   - Decentralization makes systems more censorship-resistant.
   
   **Examples [Formal]**: 
   - Censorship resistance requires sufficient validator decentralization such that no coalition can persistently exclude transactions.
   - Protocol mechanisms like encrypted mempools and proposer-builder separation enhance censorship resistance.

1. **Adjective**: live (non-gradable)
   **Meaning**: 
   - Actively operating and making progress, processing transactions and producing blocks
   - *(Technical)* Satisfying liveness properties by continuing to finalize valid transactions
   
   **Synonyms**: operational, active, functioning, progressing, working
   
   **Antonyms**: halted, stalled, stuck, frozen, deadlocked
   
   **When to Use**: When discussing whether a blockchain continues operating or has stopped making progress.
   
   **When NOT to Use**: Distinguish "live" (making progress) from "safe" (maintaining consistency). Different protocol properties.
   
   **Common Phrases**: 
   - remain live
   - liveness property
   - live system
   - keep live
   - live chain
   
   **Root Analysis**: live (active/functioning) - from Old English "libban"
   
   **Etymology**: Old English "libban" (be alive) → System operational status → Distributed systems liveness
   
   **Examples [Casual]**: 
   - The blockchain stayed live even when some validators went offline.
   - A live chain keeps producing blocks and confirming transactions.
   
   **Examples [Formal]**: 
   - The protocol remains live under asynchrony by prioritizing progress over immediate consistency.
   - Liveness guarantees ensure the system continues processing valid transactions despite up to f Byzantine failures.
