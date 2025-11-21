# MPC Wallet Engineer - Reflection Questions

1. Q: Learning that GG20 has a security vulnerability (missing zero-knowledge range proofs) despite being widely deployed, how does this change your understanding of "mature" vs "secure" in cryptographic protocols?
   A:
   - **Maturity ≠ Security**: Widespread deployment and community usage don't guarantee absence of theoretical vulnerabilities
   - **Academic scrutiny matters**: Security often emerges from continued research, not just production usage
   - **Defense in depth**: "Mature" protocols may have operational advantages (tooling, expertise) but shouldn't be assumed secure without ongoing security review
   - **Update assumptions**: Check protocol security papers from last 2 years, not just initial publication. Cryptography is an evolving field.

1. Q: You discover that your "perfect" modular architecture for MPC wallet adds 20% latency overhead compared to chain-specific implementations. How does this challenge your assumptions about abstraction vs performance?
   A:
   - **Abstraction has costs**: Clean architecture isn't free - indirection, polymorphism, and generalization add measurable overhead
   - **Context-dependent trade-offs**: For infrastructure code (high-frequency signing), performance often trumps elegance. For application code (configuration), abstraction wins.
   - **Premature optimization vs informed design**: Need to profile before abstracting. Some abstractions are negligible cost (interfaces), others significant (dynamic dispatch in hot paths).
   - **Updated mental model**: "Make it correct, make it clear, measure, THEN optimize" rather than "abstract everything upfront"

1. Q: After implementing threshold signatures, you realize most security breaches come from social engineering and phishing, not cryptographic attacks. How does this change your approach to wallet security?
   A:
   - **Security is holistic**: Strongest cryptography means nothing if users are tricked into malicious actions
   - **User education as security layer**: UX that makes phishing obvious (clear transaction previews, suspicious pattern warnings) is as important as crypto
   - **Threat model expansion**: Initial focus on "key theft" missed "user coercion" attack vector
   - **Design implications**: Add friction strategically (confirmation delays for large transfers, guardian notifications) rather than minimize friction universally

1. Q: You've been optimizing for mobile signing latency, but user surveys reveal 70% of users primarily care about "not losing funds." How does this shift your understanding of user priorities?
   A:
   - **Stated needs vs revealed preferences**: Performance metrics engineers track may not align with user-perceived value
   - **Jobs-to-be-done framework**: Users "hire" wallets for security/peace-of-mind, not transaction speed (except power users)
   - **Feature priority recalibration**: Social recovery and backup UX should precede performance optimization
   - **Metrics reconsidered**: Track "accounts successfully recovered" not just "P95 signing latency" as success metric

1. Q: Implementing MPC protocols, you notice most complexity comes from handling failures and Byzantine faults rather than the core cryptography. What does this reveal about distributed systems design?
   A:
   - **Happy path is 20%, edge cases are 80%**: Clean whiteboards showing "ideal protocol flow" miss real-world challenges
   - **Failure modes define complexity**: Network partitions, malicious parties, timeouts, and retries dominate implementation
   - **Testing assumptions**: Unit tests for crypto correctness are necessary but insufficient; need chaos engineering and adversarial testing
   - **Design philosophy**: Start with "what can go wrong" (STRIDE) not "how it should work" (ideal flow)

1. Q: You designed a "chain-agnostic" MPC core, but each blockchain integration still requires weeks of chain-specific work. What assumptions about abstraction were challenged?
   A:
   - **Leaky abstractions**: Blockchains differ in fundamental ways (UTXO vs account model, nonce management, gas mechanisms) that resist unification
   - **Semantic vs syntactic abstraction**: Can unify syntax (interface signatures) but not semantics (transaction lifecycle, confirmation finality)
   - **80/20 principle**: Abstraction handles 80% of common logic but final 20% (chain quirks) is irreducible effort
   - **Revised approach**: Accept chain-specific adapters as inevitable, focus abstraction on MPC protocol layer instead

1. Q: After a security incident where a user's device was compromised, you realize 2-of-3 threshold provides less practical security than assumed. How does this update your mental model of threat modeling?
   A:
   - **Correlated failures**: Assumed independent share compromises, but malware can simultaneously steal device share + intercept cloud backup password
   - **Threat actors are adaptive**: Attackers target weakest link (user's phone), not cryptographic protocol
   - **Defense diversity matters**: Threshold signature helps against single-point failures, but need heterogeneous defenses (HSM + device + guardian shares)
   - **User behavior is attack surface**: Can't assume users follow security best practices (strong passwords, not rooted devices)

1. Q: You prioritized feature development over technical debt for 6 months, and now adding new chains takes 3x longer than originally. What does this teach you about sustainable engineering velocity?
   A:
   - **Technical debt compounds**: 35% debt ratio → each new feature adds more debt, creating death spiral
   - **Short-term thinking illusion**: "Faster" feature delivery upfront created "slower" delivery later due to increased complexity
   - **Refactoring as investment**: Treating refactoring as "cost" rather than "velocity investment" was flawed mental model
   - **Sustainable pace**: Allocate 20-30% capacity to architectural health, not 0% (unsustainable) or 100% (gold-plating)

1. Q: Implementing FROST for Solana, you discover EdDSA has different security assumptions than ECDSA you used for Ethereum. How does this challenge your cryptographic intuitions?
   A:
   - **Algorithms aren't fungible**: Signature schemes have subtle but critical differences (nonce generation, malleability, multi-signature compatibility)
   - **Copy-paste danger**: Can't directly port ECDSA threshold logic to EdDSA without understanding curve properties
   - **Security proofs are narrow**: FROST security proof applies to specific curves/parameters, not "any signature scheme"
   - **Epistemic humility**: When working at protocol level, consult cryptographers rather than assume transferability

1. Q: After user research, you find "social recovery" is more valued than "decentralization" among mainstream users. How does this challenge your assumptions about Web3 values?
   A:
   - **Pragmatism vs ideology**: Most users care about practical benefits (account recovery) over abstract principles (decentralization)
   - **Target audience matters**: Crypto-native users value different features than mainstream users
   - **Product-market fit evolution**: Early adopter preferences (maximize decentralization) ≠ mass market preferences (balance security/convenience)
   - **Design implications**: Offer tiered trust models rather than force full self-custody, accept "progressive decentralization"

1. Q: You assumed HSMs provide "absolute security," but discovered insider threats and supply chain attacks can still compromise them. How does this update your security mental model?
   A:
   - **No silver bullet**: HSMs raise attack cost but don't eliminate risk - security is about economics (making attacks unprofitable)
   - **Trust boundaries shift**: HSMs protect against external network attacks but not insider threats or firmware backdoors
   - **Defense in depth validated**: Single layer of protection (HSM) insufficient; need operational controls (access audits, multi-party key ceremonies)
   - **Threat model granularity**: "HSM compromise" has multiple vectors (physical theft, insider access, remote exploit) requiring different defenses

1. Q: You designed for "maximum decentralization" with 5-of-9 threshold, but users complain about recovery complexity when needing to coordinate 5 guardians. What does this reveal about decentralization trade-offs?
   A:
   - **Usability is security**: If recovery process is so complex users abandon wallets, theoretical security becomes practical insecurity
   - **Decentralization spectrum**: Not binary (centralized vs decentralized) but continuum with different trade-offs
   - **Goldilocks zone**: Enough decentralization to prevent single points of failure, not so much that coordination becomes infeasible
   - **User segmentation**: Power users may want 5-of-9, mainstream users may prefer 2-of-3 + enterprise backup. Offer choice.

1. Q: After implementing account abstraction, you realize it introduces new attack vectors (malicious paymasters, griefing attacks) you hadn't anticipated. How does this change your approach to adopting new standards?
   A:
   - **New features = new risks**: Innovation in blockchain space often means first-mover disadvantage (undiscovered attack vectors)
   - **Wait-and-see sometimes wise**: Bleeding edge adoption exposes to protocol bugs, second-mover can learn from others' mistakes
   - **Incremental deployment**: Roll out new standards to small user cohorts first, validate security/stability before mass adoption
   - **Community intelligence**: Monitor security disclosures, audit reports, and post-mortems from other implementations before deploying

1. Q: You spent 3 months optimizing signing latency from 800ms to 400ms, but user retention didn't improve. What does this teach you about perceived vs actual value?
   A:
   - **Threshold effects**: Performance improvements below user perception threshold (~300ms) don't translate to satisfaction gains
   - **Opportunity cost**: Engineering time on marginal improvements could've built features with clear user impact
   - **Metrics vs outcomes**: Optimized for latency metric without validating hypothesis that latency drives retention
   - **User research upfront**: Should've A/B tested or surveyed before assuming latency was retention bottleneck

1. Q: Implementing global MPC wallet, you discover GDPR data residency conflicts with geographic redundancy for security. How does this challenge assumptions about "more distribution = more security"?
   A:
   - **Regulatory constraints are real**: Can't store EU user data in US due to GDPR, limiting geographic distribution options
   - **Security-compliance tension**: Optimal security architecture (global redundancy) may violate compliance (data localization)
   - **Regional solutions**: May need region-specific deployments (EU-only MPC cluster) rather than global mesh
   - **Compliance as feature**: Markets with strong privacy laws may prefer data residency guarantees over maximum redundancy

1. Q: After six months in production, you notice most "critical" security features you built are rarely used, while simple backup/restore UX is most valued. What does this reveal about product priorities?
   A:
   - **Frequency vs severity**: Low-probability/high-impact events (security breaches) get over-weighted vs high-probability/low-impact (password resets)
   - **Prevention vs recovery**: Users experience recovery failures (forgotten passwords) more than security breaches
   - **Product velocity**: May have over-invested in security theater (features that signal security) vs practical usability
   - **Balanced approach**: Security essentials (threshold sigs) + excellent recovery UX, not security maximization at UX cost
