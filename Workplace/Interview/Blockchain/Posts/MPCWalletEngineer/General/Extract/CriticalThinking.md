# MPC Wallet Engineer - Critical Thinking Questions

1. Q: A vendor claims their MPC wallet is "absolutely secure because it uses threshold signatures and no single party can steal funds." Evaluate this claim's logical validity and identify potential gaps in the argument.
   A: This argument commits the fallacy of oversimplification by conflating "distributed trust" with "absolute security." Key issues:
   - Assumes all parties remain honest (ignores malicious coalition attacks where t+1 parties collude)
   - Focuses only on key theft while ignoring side-channel attacks, implementation bugs, or social engineering
   - "Absolutely secure" is an unfalsifiable claim—no cryptographic system is provably secure against all attack vectors
   - Missing: threat model scope (what attacks ARE defended against?), implementation quality evidence (audits, formal verification), and operational security practices
   A stronger claim would specify: "Protects against single-point compromise via threshold signatures, assuming honest majority and secure implementation verified by [auditor]."

1. Q: An architect argues: "We should use GG20 for all chains because it's faster than CGGMP21, and our security team hasn't found any exploits in our implementation." Critique this reasoning.
   A: This argument exhibits several logical flaws:
   - **Appeal to ignorance**: "No exploits found" doesn't prove security exists—it may indicate insufficient testing
   - **Cherry-picking**: Focuses on GG20's speed advantage while ignoring its documented missing zero-knowledge range proofs vulnerability
   - **One-size-fits-all thinking**: Different chains have different signature schemes (EdDSA for Solana), making GG20 inapplicable universally
   - **Outdated information**: Academic research has identified GG20's key-extraction vulnerability; ignoring peer-reviewed findings is intellectually dishonest
   To strengthen: Provide benchmarks showing GG20 performance advantage is mission-critical, evidence of mitigations for known vulnerabilities, and justification for not using CGGMP21's security improvements.

1. Q: A product manager states: "Users abandoned our wallet because of high gas fees, so we should implement account abstraction immediately." Evaluate the causal reasoning and evidence quality.
   A: This argument makes several unwarranted causal leaps:
   - **Correlation ≠ Causation**: User abandonment may correlate with gas fees, but other factors (UX complexity, competitor features, market conditions) could be primary drivers
   - **Insufficient evidence**: "Users abandoned" lacks quantification—what percentage? How was this measured? Was it compared to control groups?
   - **Hasty generalization**: Even if gas fees drove some churn, account abstraction may not be the optimal solution (alternatives: L2 migration, gas subsidies, batch transactions)
   - **Missing cost-benefit analysis**: Ignores engineering cost (6-8 weeks), opportunity cost of not building other features, and potential new risks from AA complexity
   To improve: Present user survey data attributing churn to gas fees, A/B test results from competitors with AA, and prioritization analysis comparing AA to alternatives.

1. Q: A security engineer claims: "Our MPC wallet is safer than hardware wallets because hardware wallets have a single point of failure." Assess this argument's soundness.
   A: This argument suffers from false dichotomy and incomplete threat modeling:
   - **False comparison**: MPC distributes key shares but introduces network attack surface; hardware wallets have physical isolation. Different threat models, not strictly comparable.
   - **Selective focus**: Highlights hardware wallets' physical SPOF while ignoring MPC's software vulnerabilities (implementation bugs, side-channel attacks on each party, network compromise)
   - **Ignores deployment context**: Hardware wallets excel for cold storage; MPC wallets excel for programmatic signing. "Safer" depends on use case.
   - **Oversimplified threat model**: Assumes physical loss is the primary threat, ignoring malware, supply chain attacks, or user error scenarios where each approach has different profiles
   A rigorous argument would specify threat models, provide quantitative risk assessments (attack probability × impact), and acknowledge trade-offs rather than absolute claims.

1. Q: An executive argues: "We should prioritize social recovery over session keys because 40% of users fear losing their funds, based on an NPS survey." Evaluate the argument structure and evidence validity.
   A: While more data-driven than previous examples, this argument has several weaknesses:
   - **Survey methodology unclear**: NPS measures satisfaction, not feature preferences. Were users specifically asked about recovery features? Wording bias can skew results.
   - **Sample representativeness**: 40% of which users? Early adopters vs mainstream? Self-selected survey respondents may not represent broader market.
   - **Conflates fear with action**: Users fearing loss doesn't prove they'll adopt social recovery or that it's the best solution (alternatives: better backup UX, insurance products)
   - **Ignores opportunity cost**: Doesn't compare against session keys' potential impact on activation/retention metrics
   - **Missing competitive analysis**: Are competitors offering social recovery? Is this table stakes or differentiator?
   To strengthen: Supplement with competitor feature analysis, A/B test results if available, and WSJF scoring that weighs business value, time criticality, risk reduction, and effort.

1. Q: A technical blog claims: "FROST is always better than GG20 because it requires fewer rounds (2 vs 5), making it 2.5x faster." Critique the logical validity and completeness.
   A: This argument oversimplifies through reductionism:
   - **False equivalence**: Round count ≠ total latency. Network conditions, computation complexity, and serialization overhead all contribute. FROST may have simpler per-round operations.
   - **Ignores signature scheme compatibility**: FROST is for Schnorr/EdDSA; GG20/CGGMP21 is for ECDSA. Can't directly substitute for Bitcoin/Ethereum which use ECDSA.
   - **Cherry-picks metric**: Focuses on speed while ignoring security assumptions, implementation maturity, library availability, and audit status
   - **Generalization error**: "Always better" is an absolute claim requiring universal applicability proof, but use case matters (e.g., offline signing vs high-throughput scenarios)
   A balanced argument would specify: "For EdDSA chains like Solana, FROST offers lower latency than comparable ECDSA threshold schemes, assuming network latency dominates computation time."

1. Q: An analyst reports: "Our signing failure rate increased from 0.2% to 0.8% after the last update, proving the new code introduced bugs." Evaluate the causal reasoning and alternative explanations.
   A: This post hoc ergo propter hoc reasoning jumps to conclusions:
   - **Temporal correlation assumed causation**: Update timing may coincide with external factors (increased user load, network degradation, chain congestion)
   - **Insufficient data granularity**: What specific signing paths failed? Mobile vs backend? Which chains? Without segmentation, can't isolate root cause.
   - **Confirmation bias**: Assumes code changes are culprit without testing alternative hypotheses (infrastructure changes, dependency updates, increased bot traffic)
   - **Statistical significance unclear**: 0.6% increase over what sample size and time period? Could be natural variance.
   To improve investigation: Compare failure rates segmented by device/chain/network, check for concurrent infrastructure changes, analyze error logs for failure modes, and implement controlled rollback to isolate causal factor.

1. Q: A whitepaper states: "Our MPC protocol achieves malicious security through zero-knowledge proofs, therefore no party can cheat during signing." Analyze the argument's assumptions and boundaries.
   A: This argument has hidden assumptions and overstates conclusions:
   - **Assumes correct implementation**: ZK proofs provide theoretical guarantees, but implementation bugs (incorrect proof generation/verification) can undermine security
   - **Assumes honest setup**: Some ZK proof systems require trusted setup; compromised setup enables cheating despite protocol design
   - **Ignores other attack vectors**: Malicious security for signing doesn't cover key generation, denial-of-service, or side-channel attacks
   - **Definition ambiguity**: "Cheat" is vague—does it mean generate invalid signatures, learn others' shares, or disrupt protocol? Different attacks require different defenses.
   A precise claim: "Assuming correct implementation and honest setup, our protocol's ZK range proofs prevent malicious parties from extracting honest parties' key shares during MtA share conversion (per CGGMP21 security model)."

1. Q: A consultant recommends: "Store one key share in HSM, one on user device, one in cloud backup. This provides perfect security and availability." Assess this architectural claim.
   A: This argument fails to acknowledge inherent security-availability trade-offs:
   - **False dichotomy**: "Perfect security and availability" are contradictory goals—increasing availability (cloud backup) increases attack surface
   - **Oversimplifies threat model**: Each storage location has unique vulnerabilities (HSM: insider access, Device: malware, Cloud: breach)
   - **Ignores recovery complexity**: If user device is lost, recovery requires cloud backup + HSM. If HSM is compromised, attacker needs only one additional share.
   - **No quantitative risk assessment**: Doesn't calculate aggregate compromise probability across all storage methods
   A rigorous argument would specify threat model, calculate combined failure/compromise probabilities, and acknowledge trade-offs: "This 2-of-3 scheme optimizes for availability (user can recover with device+cloud) while maintaining security assuming no two shares are simultaneously compromised."

1. Q: A team proposes: "We'll refactor our MPC core to support multiple protocol families, which will make adding new chains much easier in the future." Evaluate the cost-benefit reasoning.
   A: This argument exhibits wishful thinking without rigorous analysis:
   - **Unquantified benefit**: "Much easier" is vague. What's current integration time vs projected time post-refactor? Without metrics, can't assess ROI.
   - **Ignores opportunity cost**: Refactoring cost (time, risk) must be weighed against alternative approaches (chain-specific adapters, external services)
   - **Optimism bias**: Assumes refactor will succeed without unforeseen complications. Software rewrites often exceed time/cost estimates.
   - **Missing decision criteria**: Under what conditions is refactoring justified? (e.g., if planning >10 chain integrations, refactor pays off; if <5, may not)
   To strengthen: Provide concrete metrics (current integration: 6 weeks, projected post-refactor: 2 weeks), quantify refactoring cost (3 engineer-months), calculate break-even point (refactor pays off after 4th chain integration), and define success criteria.
