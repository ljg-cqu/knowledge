# ConsensusMechanism Vocabulary: Adverbs

1. **Adverb**: deterministically (type: manner)
   **Meaning**: 
   - In a way that produces the same result every time given the same input, without randomness
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: predictably, certainly, definitively, invariably, consistently
   
   **Antonyms**: randomly, probabilistically, stochastically, unpredictably, variably
   
   **When to Use**: When describing finality mechanisms, leader selection, or protocol behavior that is non-random.
   
   **When NOT to Use**: Don't use for probabilistic consensus or random selection processes.
   
   **Common Phrases**: 
   - finalize deterministically
   - select deterministically
   - progress deterministically
   - compute deterministically
   - execute deterministically
   
   **Root Analysis**: deterministic (definite) + -ally (in a manner)
   
   **Etymology**: Latin "determinare" (decide) → "deterministically" → Computing/consensus context
   
   **Examples [Casual]**: 
   - BFT protocols finalize blocks deterministically—no waiting for probabilistic confirmation.
   - The leader is selected deterministically using a verifiable random function.
   
   **Examples [Formal]**: 
   - The protocol achieves finality deterministically within a single round under honest supermajority assumptions.
   - State transitions execute deterministically across all nodes to ensure consensus consistency.

1. **Adverb**: probabilistically (type: manner)
   **Meaning**: 
   - In a way based on likelihood and statistical confidence rather than certainty
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: statistically, stochastically, randomly, uncertainly, convergently
   
   **Antonyms**: deterministically, certainly, definitively, predictably, absolutely
   
   **When to Use**: When describing Nakamoto consensus finality, confirmation confidence, or convergence properties.
   
   **When NOT to Use**: Not applicable to BFT-style instant finality mechanisms.
   
   **Common Phrases**: 
   - finalize probabilistically
   - converge probabilistically
   - confirm probabilistically
   - secure probabilistically
   - guarantee probabilistically
   
   **Root Analysis**: probabilistic (likelihood-based) + -ally (in a manner)
   
   **Etymology**: Latin "probabilis" (likely) → "probabilistically" → Consensus analysis
   
   **Examples [Casual]**: 
   - Bitcoin finalizes transactions probabilistically—security grows with each new block.
   - The protocol converges probabilistically rather than providing instant finality.
   
   **Examples [Formal]**: 
   - Nakamoto consensus achieves finality probabilistically with exponentially decreasing reversal probability.
   - The protocol converges probabilistically toward unanimous agreement as blockchain length increases.

1. **Adverb**: asynchronously (type: manner)
   **Meaning**: 
   - In a manner without timing assumptions or coordination of message delivery
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: independently, without coordination, timing-free, unbounded, desynchronized
   
   **Antonyms**: synchronously, coordinately, with timing, bounded, lockstep
   
   **When to Use**: When describing network communication models or consensus operation under varying delays.
   
   **When NOT to Use**: Most practical systems assume partial synchrony, not full asynchrony.
   
   **Common Phrases**: 
   - operate asynchronously
   - communicate asynchronously
   - process asynchronously
   - execute asynchronously
   - validate asynchronously
   
   **Root Analysis**: asynchronous (without timing) + -ly (in a manner)
   
   **Etymology**: Greek "a-" (without) + "synchronos" → "asynchronously" → Distributed systems
   
   **Examples [Casual]**: 
   - Nodes communicate asynchronously without assuming when messages will arrive.
   - The protocol operates asynchronously, handling arbitrary message delays.
   
   **Examples [Formal]**: 
   - The consensus algorithm operates asynchronously without timing assumptions on network latency.
   - Validators process attestations asynchronously, achieving eventual consistency despite unbounded delays.

1. **Adverb**: cryptographically (type: manner)
   **Meaning**: 
   - Using mathematical techniques for securing, verifying, or protecting information
   - *(Position)* Typically mid-position modifying verbs like "sign," "verify," "secure"
   
   **Synonyms**: mathematically, securely, provably, through encryption, via hashing
   
   **Antonyms**: plainly, unsecured, unverified, openly, without protection
   
   **When to Use**: When describing security mechanisms, signature schemes, or verification processes.
   
   **When NOT to Use**: Specify the cryptographic primitive when relevant (hash, signature, commitment).
   
   **Common Phrases**: 
   - cryptographically secure
   - cryptographically sign
   - cryptographically verify
   - cryptographically provable
   - cryptographically hash
   
   **Root Analysis**: cryptographic (hidden-writing) + -ally (in a manner)
   
   **Etymology**: Greek "kryptos" (hidden) + "graphein" (write) → "cryptographically"
   
   **Examples [Casual]**: 
   - Validators cryptographically sign their votes to prevent forgery.
   - Block hashes are cryptographically linked to prevent tampering.
   
   **Examples [Formal]**: 
   - Validators cryptographically attest to blocks using BLS signature schemes.
   - The protocol employs cryptographically verifiable random functions for deterministic leader selection.

1. **Adverb**: adversarially (type: manner)
   **Meaning**: 
   - In a hostile or attacking manner designed to compromise security or disrupt operation
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: maliciously, hostilely, antagonistically, with intent to harm, attackingly
   
   **Antonyms**: honestly, cooperatively, benignly, compliantly, supportively
   
   **When to Use**: When discussing attack scenarios, threat models, or worst-case security analysis.
   
   **When NOT to Use**: Distinguish adversarial behavior (intentional harm) from rational self-interest or accidental faults.
   
   **Common Phrases**: 
   - behave adversarially
   - act adversarially
   - attack adversarially
   - operate adversarially
   - deviate adversarially
   
   **Root Analysis**: adversarial (hostile) + -ly (in a manner)
   
   **Etymology**: Latin "adversarius" (opponent) → "adversarially" → Security analysis
   
   **Examples [Casual]**: 
   - Byzantine nodes may behave adversarially to disrupt consensus.
   - The protocol remains secure even when validators act adversarially.
   
   **Examples [Formal]**: 
   - Security analysis assumes validators may deviate adversarially from protocol specifications.
   - The protocol tolerates coalitions acting adversarially comprising up to one-third of participants.

1. **Adverb**: efficiently (type: manner)
   **Meaning**: 
   - In a way that achieves maximum output with minimum resource waste
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: optimally, economically, effectively, productively, resourcefully
   
   **Antonyms**: inefficiently, wastefully, poorly, slowly, expensively
   
   **When to Use**: When discussing protocol performance, resource usage, or optimization.
   
   **When NOT to Use**: Specify efficiency dimension (communication, computation, energy, latency).
   
   **Common Phrases**: 
   - process efficiently
   - aggregate efficiently
   - verify efficiently
   - scale efficiently
   - operate efficiently
   
   **Root Analysis**: efficient (productive) + -ly (in a manner)
   
   **Etymology**: Latin "efficere" (accomplish) → "efficiently" → Performance optimization
   
   **Examples [Casual]**: 
   - BLS signatures let you efficiently aggregate thousands of validator votes.
   - PoS validates transactions more efficiently than PoW mining.
   
   **Examples [Formal]**: 
   - The protocol aggregates attestations efficiently using constant-size signature schemes.
   - Committee-based validation processes transactions efficiently with logarithmic communication complexity.

1. **Adverb**: eventually (type: time)
   **Meaning**: 
   - At some unspecified future time, after a potentially long delay
   - *(Position)* Typically front-position or mid-position
   
   **Synonyms**: ultimately, finally, in time, sooner or later, in the end
   
   **Antonyms**: immediately, instantly, never, always, perpetually
   
   **When to Use**: When discussing liveness guarantees, convergence properties, or asynchronous protocols.
   
   **When NOT to Use**: "Eventually" implies no time bound. For bounded-time guarantees, use "within [timeframe]."
   
   **Common Phrases**: 
   - eventually finalize
   - eventually converge
   - eventually process
   - eventually agree
   - eventually consistent
   
   **Root Analysis**: eventual (occurring at end) + -ly (in a manner)
   
   **Etymology**: Latin "eventus" (outcome) → "eventually" → Liveness guarantees in distributed systems
   
   **Examples [Casual]**: 
   - The network will eventually finalize your transaction, even with delays.
   - Nodes eventually synchronize even after temporary disconnections.
   
   **Examples [Formal]**: 
   - The protocol guarantees transactions eventually finalize under asynchronous network conditions.
   - Consensus is eventually achieved when network synchrony assumptions are satisfied.

1. **Adverb**: proportionally (type: manner)
   **Meaning**: 
   - In a way that maintains constant ratio or relative scale with another quantity
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: relatively, commensurately, correspondingly, in proportion, scalably
   
   **Antonyms**: disproportionally, independently, invariantly, without relation, absolutely
   
   **When to Use**: When discussing stake-weighted voting, reward distribution, or scalability properties.
   
   **When NOT to Use**: Specify what the proportion is relative to (stake, computation, delegation).
   
   **Common Phrases**: 
   - scale proportionally
   - reward proportionally
   - weight proportionally
   - distribute proportionally
   - vote proportionally
   
   **Root Analysis**: proportional (relative) + -ly (in a manner)
   
   **Etymology**: Latin "proportio" (comparative relation) → "proportionally" → Resource allocation
   
   **Examples [Casual]**: 
   - Validators earn rewards proportionally to their staked amount.
   - Voting power scales proportionally with your stake.
   
   **Examples [Formal]**: 
   - Validator influence is weighted proportionally to staked capital in proof-of-stake protocols.
   - Throughput scales proportionally with network partitioning in sharded architectures.

1. **Adverb**: unanimously (type: manner)
   **Meaning**: 
   - With complete agreement from all participants, without dissent
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: universally, without exception, totally, collectively, in unison
   
   **Antonyms**: divisively, partially, with dissent, by majority, incompletely
   
   **When to Use**: When discussing consensus achievement or agreement requirements.
   
   **When NOT to Use**: Most protocols require supermajority (2/3), not unanimity. Specify threshold.
   
   **Common Phrases**: 
   - agree unanimously
   - accept unanimously
   - vote unanimously
   - approve unanimously
   - decide unanimously
   
   **Root Analysis**: unanimous (all agreeing) + -ly (in a manner)
   
   **Etymology**: Latin "unanimus" (of one mind) → "unanimously" → Perfect agreement
   
   **Examples [Casual]**: 
   - Some early consensus protocols required nodes to agree unanimously.
   - Unanimity is impractical for large networks with potential faults.
   
   **Examples [Formal]**: 
   - Traditional distributed systems require unanimous agreement among non-faulty participants.
   - Byzantine consensus relaxes unanimity to supermajority agreement to tolerate malicious nodes.

1. **Adverb**: exponentially (type: manner/degree)
   **Meaning**: 
   - Increasing or decreasing at a rate proportional to the current value, accelerating rapidly
   - *(Position)* Typically mid-position modifying verbs of change
   
   **Synonyms**: dramatically, rapidly, multiplicatively, geometrically, at compounding rate
   
   **Antonyms**: linearly, slowly, gradually, arithmetically, steadily
   
   **When to Use**: When describing probabilistic finality growth, timeout increases, or security convergence.
   
   **When NOT to Use**: Distinguish exponential (multiplicative) from polynomial (power-law) or linear growth.
   
   **Common Phrases**: 
   - grow exponentially
   - increase exponentially
   - decrease exponentially
   - scale exponentially
   - improve exponentially
   
   **Root Analysis**: exponential (power-based growth) + -ly (in a manner)
   
   **Etymology**: Latin "exponere" (set forth) → Mathematical exponentiation → Growth rate description
   
   **Examples [Casual]**: 
   - Reversal probability decreases exponentially with each new confirmation.
   - Timeout durations increase exponentially to handle network delays.
   
   **Examples [Formal]**: 
   - Probabilistic finality security grows exponentially with confirmation depth in Nakamoto consensus.
   - The protocol employs exponentially increasing timeouts to achieve liveness under asynchrony.

1. **Adverb**: simultaneously (type: time)
   **Meaning**: 
   - Happening at exactly the same time, in parallel without time separation
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: concurrently, at once, together, in parallel, synchronously
   
   **Antonyms**: sequentially, separately, one after another, consecutively, staggered
   
   **When to Use**: When discussing parallel block production, concurrent attestations, or timing conflicts.
   
   **When NOT to Use**: Perfect simultaneity is impossible in distributed systems; specify "nearly simultaneous."
   
   **Common Phrases**: 
   - occur simultaneously
   - produce simultaneously
   - validate simultaneously
   - sign simultaneously
   - broadcast simultaneously
   
   **Root Analysis**: simultaneous (same time) + -ly (in a manner)
   
   **Etymology**: Latin "simul" (together) → "simultaneously" → Concurrent events
   
   **Examples [Casual]**: 
   - When miners find blocks simultaneously, the chain temporarily forks.
   - Multiple validators attest simultaneously during each epoch.
   
   **Examples [Formal]**: 
   - Simultaneous block proposals by multiple validators are resolved through fork choice rules.
   - The protocol aggregates simultaneously broadcast attestations to achieve consensus efficiency.

1. **Adverb**: irreversibly (type: manner)
   **Meaning**: 
   - In a way that cannot be undone, changed, or reverted
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: permanently, unchangeably, definitively, immutably, finally
   
   **Antonyms**: reversibly, changeably, tentatively, temporarily, conditionally
   
   **When to Use**: When discussing finality guarantees, committed transactions, or deterministic consensus.
   
   **When NOT to Use**: Distinguish cryptographically irreversible (BFT) from economically irreversible (Nakamoto).
   
   **Common Phrases**: 
   - commit irreversibly
   - finalize irreversibly
   - record irreversibly
   - settle irreversibly
   - confirm irreversibly
   
   **Root Analysis**: ir- (not) + reversible (can be undone) + -ly (in a manner)
   
   **Etymology**: Latin "re-" (back) + "vertere" (turn) → "irreversibly" → Permanent commitment
   
   **Examples [Casual]**: 
   - BFT consensus commits blocks irreversibly—they can never be changed.
   - Once finalized, transactions are irreversibly part of the blockchain.
   
   **Examples [Formal]**: 
   - Byzantine fault-tolerant protocols commit state transitions irreversibly upon achieving supermajority attestations.
   - Finalized checkpoints are irreversibly integrated into the canonical chain history.

1. **Adverb**: periodically (type: frequency)
   **Meaning**: 
   - At regular intervals, repeating in cycles or fixed time periods
   - *(Position)* Typically front-position or mid-position
   
   **Synonyms**: regularly, cyclically, recurrently, at intervals, repeatedly
   
   **Antonyms**: continuously, randomly, sporadically, irregularly, once
   
   **When to Use**: When discussing committee rotation, epoch transitions, or checkpoint finalization.
   
   **When NOT to Use**: Specify the period length when relevant (per epoch, per block, per hour).
   
   **Common Phrases**: 
   - rotate periodically
   - finalize periodically
   - checkpoint periodically
   - shuffle periodically
   - update periodically
   
   **Root Analysis**: periodic (recurring) + -ally (in a manner)
   
   **Etymology**: Greek "periodos" (circuit) → "periodically" → Regular recurrence
   
   **Examples [Casual]**: 
   - Validators are shuffled into new committees periodically every epoch.
   - The protocol creates finality checkpoints periodically.
   
   **Examples [Formal]**: 
   - Validator committees rotate periodically to prevent persistent collusion and ensure fairness.
   - The protocol finalizes checkpoint blocks periodically at epoch boundaries.

1. **Adverb**: maliciously (type: manner)
   **Meaning**: 
   - In a deliberately harmful or hostile manner, intending to disrupt or attack
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: hostilely, adversarially, with ill intent, harmfully, destructively
   
   **Antonyms**: honestly, benignly, cooperatively, helpfully, compliantly
   
   **When to Use**: When discussing validator misbehavior, attack scenarios, or Byzantine faults.
   
   **When NOT to Use**: Distinguish malicious (intentional harm) from faulty (errors) or rational (self-interested).
   
   **Common Phrases**: 
   - act maliciously
   - behave maliciously
   - attack maliciously
   - deviate maliciously
   - operate maliciously
   
   **Root Analysis**: malicious (harmful) + -ly (in a manner)
   
   **Etymology**: Latin "malitia" (badness) → "maliciously" → Intentional harm
   
   **Examples [Casual]**: 
   - Validators acting maliciously can be detected and slashed.
   - Even if some nodes behave maliciously, consensus still works.
   
   **Examples [Formal]**: 
   - The protocol remains secure when up to f validators act maliciously in arbitrary ways.
   - Slashing mechanisms deter validators from behaving maliciously through economic penalties.

1. **Adverb**: consistently (type: manner)
   **Meaning**: 
   - In a uniform, unchanging manner across time or instances
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: uniformly, reliably, steadily, constantly, invariably
   
   **Antonyms**: inconsistently, variably, erratically, unpredictably, sporadically
   
   **When to Use**: When discussing state agreement, protocol compliance, or deterministic execution.
   
   **When NOT to Use**: "Consistently" refers to uniformity; distinguish from "constantly" (frequency).
   
   **Common Phrases**: 
   - execute consistently
   - apply consistently
   - behave consistently
   - maintain consistently
   - enforce consistently
   
   **Root Analysis**: consistent (uniform) + -ly (in a manner)
   
   **Etymology**: Latin "consistere" (stand together) → "consistently" → Uniform behavior
   
   **Examples [Casual]**: 
   - All nodes must execute transactions consistently to maintain consensus.
   - The protocol applies rules consistently across all validators.
   
   **Examples [Formal]**: 
   - State transitions execute consistently across nodes to ensure distributed consensus.
   - Fork choice rules are applied consistently to deterministically identify the canonical chain.

1. **Adverb**: collectively (type: manner)
   **Meaning**: 
   - As a group or aggregate, combining individual actions into unified whole
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: jointly, together, as a group, cooperatively, in aggregate
   
   **Antonyms**: individually, separately, independently, alone, in isolation
   
   **When to Use**: When discussing validator cooperation, network-wide agreement, or aggregate behavior.
   
   **When NOT to Use**: Specify whether collective action is coordinated or merely aggregated independently.
   
   **Common Phrases**: 
   - decide collectively
   - agree collectively
   - validate collectively
   - maintain collectively
   - secure collectively
   
   **Root Analysis**: collective (group-based) + -ly (in a manner)
   
   **Etymology**: Latin "collectivus" (gathered) → "collectively" → Group action
   
   **Examples [Casual]**: 
   - Validators collectively secure the network through distributed consensus.
   - The network collectively decides which chain is canonical.
   
   **Examples [Formal]**: 
   - Validators collectively achieve consensus by aggregating individual attestations into supermajority agreement.
   - Network security emerges collectively from distributed validator participation rather than central authority.

1. **Adverb**: dynamically (type: manner)
   **Meaning**: 
   - In a manner that changes and adapts based on conditions, not fixed or static
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: adaptively, flexibly, responsively, variably, adjustably
   
   **Antonyms**: statically, fixedly, rigidly, unchangingly, permanently
   
   **When to Use**: When discussing difficulty adjustment, validator rotation, or adaptive protocols.
   
   **When NOT to Use**: Specify what adapts and what triggers changes.
   
   **Common Phrases**: 
   - adjust dynamically
   - adapt dynamically
   - change dynamically
   - allocate dynamically
   - update dynamically
   
   **Root Analysis**: dynamic (changing) + -ally (in a manner)
   
   **Etymology**: Greek "dynamis" (power/force) → "dynamically" → Adaptive change
   
   **Examples [Casual]**: 
   - Mining difficulty adjusts dynamically based on network hashrate.
   - Validator sets update dynamically as stake changes.
   
   **Examples [Formal]**: 
   - The protocol adjusts difficulty dynamically to maintain consistent block production intervals.
   - Validator committees are selected dynamically using cryptographic randomness to prevent predictability.

1. **Adverb**: independently (type: manner)
   **Meaning**: 
   - In a manner free from external control or coordination, autonomously
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: autonomously, separately, self-sufficiently, without coordination, individually
   
   **Antonyms**: dependently, jointly, cooperatively, coordinatedly, collectively
   
   **When to Use**: When discussing validator autonomy, decentralized verification, or node independence.
   
   **When NOT to Use**: Clarify whether independence means lack of coordination or lack of correlation.
   
   **Common Phrases**: 
   - operate independently
   - validate independently
   - verify independently
   - decide independently
   - execute independently
   
   **Root Analysis**: independent (self-governing) + -ly (in a manner)
   
   **Etymology**: Latin "in-" (not) + "dependere" (hang from) → "independently" → Autonomous action
   
   **Examples [Casual]**: 
   - Each validator independently verifies blocks before voting.
   - Nodes operate independently without central coordination.
   
   **Examples [Formal]**: 
   - Validators independently execute state transitions to verify block validity before attestation.
   - Decentralized consensus requires validators to operate independently without coordinated collusion.

1. **Adverb**: incrementally (type: manner)
   **Meaning**: 
   - By small successive additions or steps, gradually building up
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: gradually, progressively, step-by-step, bit-by-bit, successively
   
   **Antonyms**: abruptly, suddenly, all-at-once, completely, immediately
   
   **When to Use**: When discussing gradual protocol upgrades, progressive state changes, or step-wise improvements.
   
   **When NOT to Use**: Distinguish incremental (small steps) from continuous (smooth) or discrete (distinct steps).
   
   **Common Phrases**: 
   - upgrade incrementally
   - improve incrementally
   - grow incrementally
   - change incrementally
   - build incrementally
   
   **Root Analysis**: incremental (gradual) + -ly (in a manner)
   
   **Etymology**: Latin "incrementum" (growth) → "incrementally" → Gradual progression
   
   **Examples [Casual]**: 
   - The protocol can be upgraded incrementally without hard forks.
   - State changes accumulate incrementally with each new block.
   
   **Examples [Formal]**: 
   - Protocol improvements are deployed incrementally through backward-compatible soft forks.
   - Blockchain state evolves incrementally through cryptographically linked state transitions.

1. **Adverb**: reliably (type: manner)
   **Meaning**: 
   - In a dependable and trustworthy manner, consistently without failure
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: dependably, consistently, faithfully, steadily, predictably
   
   **Antonyms**: unreliably, unpredictably, erratically, inconsistently, undependably
   
   **When to Use**: When discussing system guarantees, consensus properties, or fault tolerance.
   
   **When NOT to Use**: Specify reliability conditions (under what fault assumptions, network models).
   
   **Common Phrases**: 
   - operate reliably
   - process reliably
   - deliver reliably
   - function reliably
   - perform reliably
   
   **Root Analysis**: reliable (trustworthy) + -ly (in a manner)
   
   **Etymology**: Old French "relier" (fasten) → "reliably" → Dependable performance
   
   **Examples [Casual]**: 
   - The network reliably processes transactions even with some offline nodes.
   - Consensus protocols reliably maintain consistency despite failures.
   
   **Examples [Formal]**: 
   - The protocol reliably achieves consensus under Byzantine conditions with fewer than one-third faulty nodes.
   - Reliable broadcast primitives ensure messages are delivered consistently to all honest participants.

1. **Adverb**: instantly (type: time)
   **Meaning**: 
   - Immediately without delay, happening at once
   - *(Position)* Typically mid-position or end-position
   
   **Synonyms**: immediately, at once, instantaneously, right away, promptly
   
   **Antonyms**: eventually, slowly, gradually, after delay, never
   
   **When to Use**: When describing single-round BFT finality or immediate confirmation.
   
   **When NOT to Use**: Few systems provide truly instant finality. Specify "within one round/block" for precision.
   
   **Common Phrases**: 
   - finalize instantly
   - confirm instantly
   - achieve instantly
   - verify instantly
   - settle instantly
   
   **Root Analysis**: instant (immediate) + -ly (in a manner)
   
   **Etymology**: Latin "instans" (pressing upon) → "instantly" → Immediate occurrence
   
   **Examples [Casual]**: 
   - Some BFT chains finalize blocks instantly without waiting for confirmations.
   - Instant finality means transactions can't be reversed once confirmed.
   
   **Examples [Formal]**: 
   - Byzantine fault-tolerant protocols achieve instant finality within a single consensus round.
   - Single-slot finality protocols commit blocks instantly upon receiving supermajority attestations.
