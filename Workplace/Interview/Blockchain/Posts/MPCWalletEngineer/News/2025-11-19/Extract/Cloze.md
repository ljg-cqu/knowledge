1. Q: The Trout threshold ECDSA protocol reduces online signing to ___ rounds and uses about ___ KB of upload bandwidth per party, delivering roughly ___x faster signing than GG18/20 in Rust benchmarks.
   A: 2 rounds; 6.5 KB; 3x

1. Q: The TARmageddon vulnerability (CVE-2025-62518) in Rust `async-tar` / `tokio-tar` libraries can enable ___ via crafted archives; a recommended mitigation in the news briefings is migrating builds to ___.
   A: remote code execution (RCE); astral-tokio-tar v0.5.6

1. Q: The "6ix1een" attack against GG18/GG20 arises from missing validation of ___ moduli in the MtA protocol; in the worst case an attacker can extract a full private key using as few as ___ signatures.
   A: Paillier; 16

1. Q: Modern ECDSA threshold schemes like MPC-CMP and CGGMP21 harden older GG18/GG20-style designs by adding ___ (on Paillier parameters) and providing stronger ___-secure proofs against malicious parties.
   A: zero-knowledge range proofs; malicious

1. Q: Compared with GG20, CGGMP21 offers ___-round online signing (after preprocessing) and supports ___ abort, allowing the system to pinpoint misbehaving parties during failed signing.
   A: one; identifiable

1. Q: FROST (Flexible Round-Optimized Schnorr Threshold signatures) is being standardized by the ___ and primarily targets chains with ___-style signatures.
   A: IETF (CFRG); Schnorr / EdDSA

1. Q: In one ERC‑4337 case study, adding Account Abstraction features such as gasless transactions, social recovery, and session keys increased user activation by about ___%, while our own Day‑7 retention could improve from roughly ___% to around ___%.
   A: 30%; 15%; 25%

1. Q: Integrating ERC‑4337 for an MPC wallet was estimated to cost about ___ engineer‑months of work to wire up a Bundler, Paymaster, and smart account logic.
   A: 6 engineer‑months

1. Q: Q2‑2025 Solana wallet‑drain exploits stole roughly ___ in value by abusing transaction simulation gaps, and about ___% of victims used wallets without clear simulation or decoding.
   A: $87M; 67%

1. Q: In one enterprise Solana case, a single client represented about ___% of Annual Usage Revenue (AUR), or roughly $___k ARR, and demanded Token‑2022 support within 90 days.
   A: 15%; 450

1. Q: Under MiCA, obtaining an EU crypto asset service provider license for wallets requires locking up roughly €___K in regulatory capital but unlocks an estimated $___–___B EU institutional custody market.
   A: €350K; $8B; $12B

1. Q: Singapore Rust cryptography specialists can command about a ___–___% salary premium over typical blockchain engineers, reaching around S$___–___ per month according to recent salary data.
   A: 35–50%; S$18,000–S$22,500

1. Q: Recent compensation reports cite Senior Cryptography Engineer salaries in the United States at roughly $___K per year, while annual turnover for such specialists in some Web3 firms reaches about ___–___%.
   A: $216K+; 45–60%
