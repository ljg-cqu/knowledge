# ConsensusMechanism Vocabulary: Linking Words

1. **Linking Word**: however (type: discourse marker)
   **Meaning**: 
   - Introduces a contrasting idea or unexpected consequence that qualifies the previous statement
   - *Function*: Creates logical contrast between clauses or sentences showing exception or limitation
   
   **Synonyms**: nevertheless, nonetheless, yet, still, but
   
   **Antonyms**: moreover, furthermore, additionally, likewise, similarly
   
   **When to Use**: When presenting limitations, tradeoffs, or contrasts in consensus mechanism properties. Common in technical writing to acknowledge constraints.
   
   **When NOT to Use**: Avoid overuse—one "however" per paragraph is typically sufficient. Don't use when adding supporting points (use "moreover").
   
   **Common Patterns**: 
   - [Clause structure]: [Independent clause]. However, [contrasting clause].
   - [Position]: sentence-initial (most common), mid-sentence (between commas)
   - [Punctuation]: Period before; comma after when sentence-initial
   - [Common errors to avoid]: Comma splice ("Bitcoin is secure, however it's slow"), wrong logical relationship
   
   **Root Analysis**: how + ever (in whatever way)
   
   **Etymology**: Middle English "how" + "ever" → Concessive conjunction
   
   **Examples [Casual]**: 
   - PoS is energy-efficient. However, it requires careful mechanism design.
   - Byzantine consensus provides instant finality. However, it requires less than one-third Byzantine nodes.
   
   **Examples [Formal]**: 
   - Nakamoto consensus achieves permissionless participation. However, it provides only probabilistic finality with exponentially decreasing reversal probability.
   - Committee-based validation enhances scalability. However, it introduces additional complexity in validator selection and rotation mechanisms.

1. **Linking Word**: therefore (type: connector)
   **Meaning**: 
   - Indicates logical consequence or conclusion drawn from previous statement
   - *Function*: Shows cause-effect relationship or logical deduction
   
   **Synonyms**: thus, consequently, accordingly, hence, as a result
   
   **Antonyms**: however, nevertheless, despite this, conversely
   
   **When to Use**: When drawing conclusions from consensus properties, showing logical implications, or explaining consequences.
   
   **When NOT to Use**: Only use when genuine logical consequence exists. Don't use for contrast (use "however") or additional info (use "moreover").
   
   **Common Patterns**: 
   - [Clause structure]: [Premise]. Therefore, [conclusion].
   - [Position]: sentence-initial (most common), mid-sentence (between commas)
   - [Punctuation]: Period or semicolon before; comma after when sentence-initial
   - [Common errors to avoid]: Comma splice, weak logical connection, overuse
   
   **Root Analysis**: there + fore (for that reason)
   
   **Etymology**: Old English "þær" (there) + "fore" (before) → Logical conclusion marker
   
   **Examples [Casual]**: 
   - PoW requires massive energy. Therefore, many projects are switching to PoS.
   - The network has fewer than one-third Byzantine nodes. Therefore, consensus can be achieved.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance requires 2f+1 honest nodes among 3f+1 total. Therefore, the protocol tolerates up to f Byzantine failures.
   - Probabilistic finality converges exponentially with confirmation depth. Therefore, deep reorganizations become economically infeasible.

1. **Linking Word**: whereas (type: subordinating)
   **Meaning**: 
   - Introduces contrasting subordinate clause showing difference between two things
   - *Function*: Creates direct comparison highlighting differences
   
   **Synonyms**: while (contrast), in contrast to, as opposed to
   
   **Antonyms**: similarly, likewise, just as, in the same way
   
   **When to Use**: For direct comparisons between consensus mechanisms (PoW vs. PoS), highlighting contrasting properties.
   
   **When NOT to Use**: "Whereas" requires contrast. Don't use for similarity (use "just as") or sequence (use "when").
   
   **Common Patterns**: 
   - [Clause structure]: [Clause A], whereas [contrasting clause B].
   - [Position]: mid-sentence (most common), sentence-initial (formal)
   - [Punctuation]: Comma before "whereas" when mid-sentence
   - [Common errors to avoid]: Using for time (use "when"), missing comma
   
   **Root Analysis**: where + as (in the place that)
   
   **Etymology**: Middle English "whereas" → Contrastive conjunction
   
   **Examples [Casual]**: 
   - PoS uses staked capital, whereas PoW uses computational power.
   - BFT provides instant finality, whereas Nakamoto consensus is probabilistic.
   
   **Examples [Formal]**: 
   - Deterministic finality protocols achieve irreversibility within one round, whereas probabilistic consensus converges asymptotically.
   - Permissionless systems prioritize censorship resistance, whereas permissioned networks optimize for efficiency and regulatory compliance.

1. **Linking Word**: although (type: subordinating)
   **Meaning**: 
   - Introduces subordinate clause expressing concession or limitation despite main clause
   - *Function*: Shows something is true despite an obstacle or contrary expectation
   
   **Synonyms**: though, even though, despite the fact that, while
   
   **Antonyms**: because, since, as (causal)
   
   **When to Use**: For acknowledging limitations while asserting main points about consensus protocols.
   
   **When NOT to Use**: "Although" expresses concession. Don't use for cause (use "because") or time (use "when").
   
   **Common Patterns**: 
   - [Clause structure]: Although [concession], [main assertion]. OR [Main assertion], although [concession].
   - [Position]: sentence-initial or mid-sentence
   - [Punctuation]: Comma separates clauses
   - [Common errors to avoid]: Comma splice with "however," confusing with "because"
   
   **Root Analysis**: all + though (entirely even if)
   
   **Etymology**: Middle English "all though" → Concessive conjunction
   
   **Examples [Casual]**: 
   - Although PoW is secure, it wastes energy.
   - The protocol achieves consensus, although some validators may be offline.
   
   **Examples [Formal]**: 
   - Although Byzantine fault tolerance provides deterministic finality, it requires strong network assumptions.
   - The protocol maintains liveness, although throughput degrades under adversarial conditions.

1. **Linking Word**: because (type: subordinating)
   **Meaning**: 
   - Introduces subordinate clause providing reason or explanation for main clause
   - *Function*: Establishes causal relationship showing why something occurs
   
   **Synonyms**: since, as, due to the fact that, for the reason that
   
   **Antonyms**: although, despite, even though (concessive)
   
   **When to Use**: For explaining mechanisms, justifying design choices, or stating reasons in consensus analysis.
   
   **When NOT to Use**: "Because" indicates cause. Don't use for contrast (use "although") or time (use "when").
   
   **Common Patterns**: 
   - [Clause structure]: [Effect] because [cause]. OR Because [cause], [effect].
   - [Position]: mid-sentence (most common), sentence-initial (emphasis)
   - [Punctuation]: Comma before "because" is optional; after when sentence-initial
   - [Common errors to avoid]: Fragment ("Because the protocol is secure."), comma splice
   
   **Root Analysis**: by + cause (for the reason)
   
   **Etymology**: Middle English "bi cause" → Causal conjunction
   
   **Examples [Casual]**: 
   - PoS is efficient because it doesn't require mining.
   - The network forked because two miners found blocks simultaneously.
   
   **Examples [Formal]**: 
   - The protocol achieves consensus because honest validators constitute a supermajority.
   - Byzantine fault tolerance is limited to f < n/3 because greater fault ratios enable safety violations.

1. **Linking Word**: moreover (type: connector)
   **Meaning**: 
   - Adds additional supporting information or strengthening evidence to previous statement
   - *Function*: Provides additive logical relationship emphasizing cumulative support
   
   **Synonyms**: furthermore, additionally, in addition, besides, also
   
   **Antonyms**: however, conversely, on the contrary, nevertheless
   
   **When to Use**: When adding supporting points, cumulative advantages, or additional evidence.
   
   **When NOT to Use**: Don't use for contrast (use "however") or conclusion (use "therefore"). Avoid overuse.
   
   **Common Patterns**: 
   - [Clause structure]: [Point A]. Moreover, [additional supporting point B].
   - [Position]: sentence-initial (most common)
   - [Punctuation]: Period before; comma after
   - [Common errors to avoid]: Using for contrast, comma splice, overuse
   
   **Root Analysis**: more + over (in addition to)
   
   **Etymology**: Middle English "more" + "over" → Additive conjunction
   
   **Examples [Casual]**: 
   - PoS is energy-efficient. Moreover, it allows for faster finality.
   - The protocol is secure. Moreover, it scales to thousands of validators.
   
   **Examples [Formal]**: 
   - Byzantine consensus provides deterministic finality. Moreover, it achieves optimal resilience of f < n/3 Byzantine faults.
   - The protocol minimizes communication complexity. Moreover, it maintains security under asynchronous network conditions.

1. **Linking Word**: consequently (type: connector)
   **Meaning**: 
   - Introduces result or effect following logically from previous cause or condition
   - *Function*: Shows cause-effect relationship with emphasis on inevitable result
   
   **Synonyms**: therefore, thus, as a result, accordingly, hence
   
   **Antonyms**: conversely, however, nevertheless, despite this
   
   **When to Use**: For showing inevitable consequences of consensus properties or design decisions.
   
   **When NOT to Use**: Use only when strong causal relationship exists. Similar to "therefore" but slightly more formal.
   
   **Common Patterns**: 
   - [Clause structure]: [Cause]. Consequently, [effect/result].
   - [Position]: sentence-initial (most common), mid-sentence (between commas)
   - [Punctuation]: Period or semicolon before; comma after when sentence-initial
   - [Common errors to avoid]: Weak causal link, comma splice, overuse with "therefore"
   
   **Root Analysis**: consequent (following as result) + -ly
   
   **Etymology**: Latin "consequens" (following) → Result marker
   
   **Examples [Casual]**: 
   - The protocol requires supermajority agreement. Consequently, it tolerates up to one-third Byzantine nodes.
   - Network latency increased significantly. Consequently, consensus rounds timed out.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance mandates 2f+1 honest participants among 3f+1 nodes. Consequently, the resilience threshold cannot exceed f < n/3.
   - Validator stake distributions exhibit power-law characteristics. Consequently, the protocol implements stake-weighted random selection to maintain proportional influence.

1. **Linking Word**: alternatively (type: connector)
   **Meaning**: 
   - Introduces a different option, approach, or possibility as substitute
   - *Function*: Presents alternative choice or method
   
   **Synonyms**: instead, as an alternative, or, another option is
   
   **Antonyms**: similarly, likewise, in addition, moreover
   
   **When to Use**: When presenting alternative consensus mechanisms, design choices, or approaches.
   
   **When NOT to Use**: "Alternatively" suggests substitution, not addition. Use "additionally" for extra options.
   
   **Common Patterns**: 
   - [Clause structure]: [Option A]. Alternatively, [option B].
   - [Position]: sentence-initial (most common)
   - [Punctuation]: Period before; comma after
   - [Common errors to avoid]: Using for additional (not alternative) options
   
   **Root Analysis**: alternative (other choice) + -ly
   
   **Etymology**: Latin "alternare" (do by turns) → Choice marker
   
   **Examples [Casual]**: 
   - You can use PoW for security. Alternatively, PoS offers energy efficiency.
   - Validators can attest immediately. Alternatively, they can wait for confirmation.
   
   **Examples [Formal]**: 
   - Protocols may achieve finality through BFT consensus. Alternatively, probabilistic convergence via longest-chain rules provides comparable security guarantees.
   - Leader selection can employ verifiable random functions. Alternatively, stake-weighted deterministic rotation ensures fairness.

1. **Linking Word**: specifically (type: connector)
   **Meaning**: 
   - Introduces precise details, examples, or specifications of general statement
   - *Function*: Narrows focus to particular case or detail
   
   **Synonyms**: in particular, particularly, precisely, namely, to be specific
   
   **Antonyms**: generally, broadly, overall, in general
   
   **When to Use**: When providing specific examples, technical details, or precise definitions.
   
   **When NOT to Use**: Don't overuse. Reserve for genuinely important specifications.
   
   **Common Patterns**: 
   - [Clause structure]: [General statement]. Specifically, [specific detail/example].
   - [Position]: sentence-initial (most common), mid-sentence (between commas)
   - [Punctuation]: Period before; comma after when sentence-initial
   - [Common errors to avoid]: Using without actual specification, overuse
   
   **Root Analysis**: specific (precise) + -ally
   
   **Etymology**: Latin "species" (kind) → Specification marker
   
   **Examples [Casual]**: 
   - Byzantine faults cause problems. Specifically, malicious validators can double-sign blocks.
   - The protocol has timing assumptions. Specifically, messages must arrive within 5 seconds.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance requires strict fault bounds. Specifically, honest validators must constitute at least two-thirds of the participant set.
   - The protocol employs cryptographic primitives for security. Specifically, BLS signatures enable efficient attestation aggregation.

1. **Linking Word**: meanwhile (type: connector)
   **Meaning**: 
   - Indicates simultaneous occurrence or parallel developments
   - *Function*: Shows temporal parallelism or contrasting concurrent events
   
   **Synonyms**: at the same time, simultaneously, in the meantime, concurrently
   
   **Antonyms**: subsequently, later, afterwards, then, next
   
   **When to Use**: For describing parallel consensus processes or concurrent validator activities.
   
   **When NOT to Use**: "Meanwhile" indicates simultaneity. Use "subsequently" for sequential events.
   
   **Common Patterns**: 
   - [Clause structure]: [Event A occurs]. Meanwhile, [parallel event B occurs].
   - [Position]: sentence-initial (most common)
   - [Punctuation]: Period before; comma after
   - [Common errors to avoid]: Using for sequential (not parallel) events
   
   **Root Analysis**: mean (middle) + while (time period)
   
   **Etymology**: Middle English "mean while" → Temporal parallelism marker
   
   **Examples [Casual]**: 
   - Validators attest to the block. Meanwhile, the proposer prepares the next block.
   - One shard processes transactions. Meanwhile, other shards operate independently.
   
   **Examples [Formal]**: 
   - Committee A validates transactions within its shard. Meanwhile, Committee B operates autonomously on parallel state transitions.
   - The protocol achieves consensus on block n. Meanwhile, the next leader prepares proposals for block n+1.

1. **Linking Word**: furthermore (type: connector)
   **Meaning**: 
   - Adds additional supporting information or evidence to strengthen argument
   - *Function*: Provides additive logical relationship (similar to "moreover" but slightly more formal)
   
   **Synonyms**: moreover, additionally, in addition, besides, also
   
   **Antonyms**: however, conversely, on the contrary, nevertheless
   
   **When to Use**: When building cumulative case with multiple supporting points.
   
   **When NOT to Use**: Very similar to "moreover"—avoid using both in same paragraph. Don't use for contrast.
   
   **Common Patterns**: 
   - [Clause structure]: [Point A]. Furthermore, [additional supporting point B].
   - [Position]: sentence-initial (most common)
   - [Punctuation]: Period before; comma after
   - [Common errors to avoid]: Overuse with "moreover," using for contrast, comma splice
   
   **Root Analysis**: further (additional) + more
   
   **Etymology**: Old English "further" + "more" → Additive conjunction
   
   **Examples [Casual]**: 
   - PoS is more efficient than PoW. Furthermore, it enables faster finality.
   - The protocol is secure against Byzantine faults. Furthermore, it maintains liveness under asynchrony.
   
   **Examples [Formal]**: 
   - Byzantine consensus achieves deterministic finality within one round. Furthermore, it provides optimal fault tolerance of f < n/3.
   - The protocol minimizes communication overhead through signature aggregation. Furthermore, it enables linear scalability in validator set size.

1. **Linking Word**: nevertheless (type: connector)
   **Meaning**: 
   - Introduces statement that contrasts with or seems to contradict previous point but is still true
   - *Function*: Concessive connector showing persistence despite obstacle
   
   **Synonyms**: nonetheless, however, even so, yet, still
   
   **Antonyms**: therefore, consequently, thus, accordingly
   
   **When to Use**: For acknowledging challenges while asserting solutions or persisting conditions.
   
   **When NOT to Use**: Similar to "however" but emphasizes overcoming obstacle. Choose based on emphasis.
   
   **Common Patterns**: 
   - [Clause structure]: [Obstacle/challenge]. Nevertheless, [persisting fact/solution].
   - [Position]: sentence-initial (most common), mid-sentence (between commas)
   - [Punctuation]: Period before; comma after when sentence-initial
   - [Common errors to avoid]: Comma splice, overuse with "however"
   
   **Root Analysis**: never + the + less (not any the less for that)
   
   **Etymology**: Middle English "never the less" → Concessive conjunction
   
   **Examples [Casual]**: 
   - BFT requires strong assumptions. Nevertheless, it provides instant finality.
   - Some validators may be offline. Nevertheless, the protocol maintains liveness.
   
   **Examples [Formal]**: 
   - Byzantine consensus mandates partial synchrony assumptions. Nevertheless, it achieves superior finality properties compared to fully asynchronous protocols.
   - Committee-based validation introduces rotation complexity. Nevertheless, it enables throughput scalability unattainable in full-participation models.

1. **Linking Word**: if (type: subordinating)
   **Meaning**: 
   - Introduces conditional clause stating requirement or hypothesis for main clause
   - *Function*: Creates conditional relationship showing dependency
   
   **Synonyms**: provided that, assuming that, in case, when (conditional)
   
   **Antonyms**: (no direct antonym—negation uses "unless" or "if not")
   
   **When to Use**: For stating consensus protocol conditions, security assumptions, or requirements.
   
   **When NOT to Use**: "If" indicates condition. Use "when" for time, "because" for cause.
   
   **Common Patterns**: 
   - [Clause structure]: If [condition], [consequence]. OR [Consequence] if [condition].
   - [Position]: sentence-initial or mid-sentence
   - [Punctuation]: Comma after when sentence-initial; usually no comma when mid
   - [Common errors to avoid]: Comma splice, confusing with "whether" (indirect question)
   
   **Root Analysis**: if (Old English "gif" - condition marker)
   
   **Etymology**: Old English "gif" → Conditional conjunction
   
   **Examples [Casual]**: 
   - If validators hold 51% stake, they can attack the network.
   - The protocol fails if Byzantine nodes exceed one-third.
   
   **Examples [Formal]**: 
   - If honest validators constitute fewer than two-thirds of participants, safety guarantees may be violated.
   - Byzantine consensus achieves finality if and only if fewer than one-third of nodes exhibit Byzantine faults.

1. **Linking Word**: unless (type: subordinating)
   **Meaning**: 
   - Introduces negative condition—something happens except if condition is met
   - *Function*: Creates conditional relationship with negative logic (if not)
   
   **Synonyms**: if not, except if, except when, only if not
   
   **Antonyms**: if, provided that, when
   
   **When to Use**: For stating exceptions, necessary conditions, or negative requirements.
   
   **When NOT to Use**: "Unless" means "if not." Can often be rewritten with "if...not" for clarity.
   
   **Common Patterns**: 
   - [Clause structure]: [Statement] unless [exception condition].
   - [Position]: usually mid-sentence following main clause
   - [Punctuation]: Usually no comma before "unless"
   - [Common errors to avoid]: Double negatives, confusion with "until"
   
   **Root Analysis**: on + less (on a lesser condition)
   
   **Etymology**: Middle English "on lesse" → Negative conditional
   
   **Examples [Casual]**: 
   - The chain will fork unless validators coordinate.
   - Slashing won't occur unless you violate protocol rules.
   
   **Examples [Formal]**: 
   - Consensus cannot be achieved unless honest participants constitute at least two-thirds of the validator set.
   - The protocol maintains liveness unless network partitions persist beyond synchrony bounds.

1. **Linking Word**: when (type: subordinating)
   **Meaning**: 
   - Introduces temporal clause specifying time or condition of main clause occurrence
   - *Function*: Creates temporal or conditional relationship
   
   **Synonyms**: at the time that, whenever, as soon as, once
   
   **Antonyms**: (no direct antonym—timing alternatives use "before" or "after")
   
   **When to Use**: For describing temporal sequences in consensus protocols or condition-triggered events.
   
   **When NOT to Use**: "When" indicates time. Use "if" for hypothetical conditions without temporal aspect.
   
   **Common Patterns**: 
   - [Clause structure]: When [temporal condition], [event occurs]. OR [Event occurs] when [condition].
   - [Position]: sentence-initial or mid-sentence
   - [Punctuation]: Comma after when sentence-initial; often no comma when mid
   - [Common errors to avoid]: Confusing with "if" (condition), comma usage
   
   **Root Analysis**: Old English "hwanne" (at what time)
   
   **Etymology**: Old English "hwanne" → Temporal conjunction
   
   **Examples [Casual]**: 
   - When a validator equivocates, they get slashed.
   - The protocol finalizes blocks when enough attestations are received.
   
   **Examples [Formal]**: 
   - When validators receive supermajority attestations, blocks achieve deterministic finality.
   - Consensus rounds timeout when messages fail to arrive within designated intervals.

1. **Linking Word**: since (type: subordinating/connector)
   **Meaning**: 
   - *(Causal)* Because, for the reason that, given that
   - *(Temporal)* From a past time until now
   - *Function*: Creates causal or temporal relationship
   
   **Synonyms**: because (causal), as (causal), from the time that (temporal)
   
   **Antonyms**: although, despite (concessive)
   
   **When to Use**: For causal explanations (slightly more formal than "because") or temporal references.
   
   **When NOT to Use**: Context must clarify whether causal or temporal. Can be ambiguous.
   
   **Common Patterns**: 
   - [Clause structure]: Since [cause/past time], [effect/current state].
   - [Position]: sentence-initial (most common)
   - [Punctuation]: Comma after when sentence-initial
   - [Common errors to avoid]: Ambiguity between causal and temporal meanings
   
   **Root Analysis**: Old English "siþþan" (after that time)
   
   **Etymology**: Old English "siþþan" → Causal/temporal conjunction
   
   **Examples [Casual]**: 
   - Since PoS doesn't require mining, it saves energy.
   - Since the protocol launched, no security breaches have occurred.
   
   **Examples [Formal]**: 
   - Since Byzantine fault tolerance requires supermajority honesty, the protocol tolerates at most f < n/3 faults.
   - Since Nakamoto's 2008 whitepaper, numerous consensus mechanisms have been proposed.

1. **Linking Word**: indeed (type: discourse marker)
   **Meaning**: 
   - Emphasizes or confirms truth of statement, often with element of surprise
   - *Function*: Reinforcement and emphasis marker
   
   **Synonyms**: in fact, actually, as a matter of fact, truly, certainly
   
   **Antonyms**: supposedly, allegedly, questionably
   
   **When to Use**: For emphasizing important points or confirming counterintuitive facts.
   
   **When NOT to Use**: Avoid overuse. Reserve for genuine emphasis.
   
   **Common Patterns**: 
   - [Clause structure]: [Statement]. Indeed, [emphasizing detail]. OR [Statement], indeed, [continuation].
   - [Position]: sentence-initial, mid-sentence (between commas)
   - [Punctuation]: Comma before/after when mid-sentence; comma after when initial
   - [Common errors to avoid]: Overuse, using without genuine emphasis
   
   **Root Analysis**: in + deed (in fact, in reality)
   
   **Etymology**: Middle English "in dede" (in fact) → Emphasis marker
   
   **Examples [Casual]**: 
   - PoS is efficient. Indeed, it uses 99% less energy than PoW.
   - Byzantine faults are challenging. Indeed, some attacks are theoretically undetectable.
   
   **Examples [Formal]**: 
   - Byzantine consensus provides strong guarantees. Indeed, it achieves deterministic finality within one round.
   - Probabilistic finality converges rapidly. Indeed, security grows exponentially with confirmation depth.

1. **Linking Word**: both...and (type: correlative)
   **Meaning**: 
   - Connects two elements with equal emphasis, indicating both are true simultaneously
   - *Function*: Correlative pair showing dual properties or characteristics
   
   **Synonyms**: as well as...and, not only...but also
   
   **Antonyms**: either...or, neither...nor
   
   **When to Use**: For highlighting multiple properties, dual requirements, or complementary aspects.
   
   **When NOT to Use**: Use "both...and" only for exactly two items. For more, list with commas.
   
   **Common Patterns**: 
   - [Clause structure]: Both [element A] and [element B] + verb. OR Verb + both [A] and [B].
   - [Position]: paired elements surrounding subjects, objects, or phrases
   - [Punctuation]: No comma between "both" and "and"
   - [Common errors to avoid]: Unparallel structure, more than two elements, missing "and"
   
   **Root Analysis**: both (two together) + and (addition)
   
   **Etymology**: Old English "ba þa" (both the two) → Correlative conjunction
   
   **Examples [Casual]**: 
   - PoS requires both economic security and technical correctness.
   - The protocol ensures both safety and liveness.
   
   **Examples [Formal]**: 
   - Byzantine fault tolerance achieves both deterministic finality and optimal fault resilience.
   - The consensus mechanism balances both throughput optimization and decentralization preservation.

1. **Linking Word**: either...or (type: correlative)
   **Meaning**: 
   - Presents two alternatives where one (or possibly both) must be true
   - *Function*: Correlative pair showing choice or alternatives
   
   **Synonyms**: whether...or, one or the other
   
   **Antonyms**: both...and, neither...nor
   
   **When to Use**: For presenting alternative designs, exclusive choices, or possible outcomes.
   
   **When NOT to Use**: "Either...or" traditionally implies exclusivity but can mean inclusive or. Clarify if needed.
   
   **Common Patterns**: 
   - [Clause structure]: Either [option A] or [option B] + verb. OR Verb + either [A] or [B].
   - [Position]: paired elements surrounding subjects, objects, or phrases
   - [Punctuation]: No comma between "either" and "or"
   - [Common errors to avoid]: Subject-verb agreement with plural, unparallel structure
   
   **Root Analysis**: either (one of two) + or (alternative)
   
   **Etymology**: Old English "ægþer" (each of two) → Correlative conjunction
   
   **Examples [Casual]**: 
   - Either validators follow protocol rules or they get slashed.
   - The chain will finalize either through BFT or probabilistic convergence.
   
   **Examples [Formal]**: 
   - Consensus protocols must optimize either latency or throughput, rarely achieving both simultaneously.
   - Validators either attest within designated slots or forfeit reward eligibility.

1. **Linking Word**: not only...but also (type: correlative)
   **Meaning**: 
   - Emphasizes that something has additional properties beyond expected one
   - *Function*: Correlative pair adding emphasis to second element
   
   **Synonyms**: as well as, besides, in addition to, both...and
   
   **Antonyms**: neither...nor, only, merely
   
   **When to Use**: For emphasizing multiple benefits, adding surprising additional properties.
   
   **When NOT to Use**: "But also" part can be omitted in casual speech but should be included in formal writing.
   
   **Common Patterns**: 
   - [Clause structure]: Not only [element A] but also [element B]. OR Verb + not only [A] but also [B].
   - [Position]: paired elements surrounding subjects, objects, or phrases
   - [Punctuation]: Comma optional before "but also"
   - [Common errors to avoid]: Unparallel structure, omitting "also," subject-verb agreement
   
   **Root Analysis**: not + only (limiting) + but + also (addition)
   
   **Etymology**: Combination of negation and additive elements → Emphatic correlative
   
   **Examples [Casual]**: 
   - PoS not only saves energy but also enables faster finality.
   - Byzantine faults threaten not only safety but also liveness.
   
   **Examples [Formal]**: 
   - The protocol achieves not only optimal communication complexity but also deterministic finality.
   - Committee rotation ensures not only fairness but also resilience against targeted attacks.
