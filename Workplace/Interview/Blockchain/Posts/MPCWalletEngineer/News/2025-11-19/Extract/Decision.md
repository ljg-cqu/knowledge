1. Q: Your MPC wallet currently uses a GG20-based ECDSA implementation that predates the "6ix1een" Paillier modulus vulnerability disclosures. New clients are asking specifically about GG18/GG20 risk, and your internal audit has not yet verified modulus generation or ZK range proofs. What would you do and why?
   A: 
   - Commission an immediate protocol audit focused on Paillier key generation, MtA proofs, and any GG18/GG20 code paths across all chains.
   - Ship emergency hardening: either integrate the published vendor patches / ZK range proofs or plan a protocol swap (e.g., MPC‑CMP or CGGMP21) with full key rotation.
   - Define a public vulnerability response: security advisory, rotation timeline, and attestation reports for institutional prospects.
   - Prioritize migration for the highest‑value asset pools first (treasury, institutional custody) while monitoring for anomalous signing patterns everywhere.

1. Q: Research on Trout (a two‑round threshold ECDSA protocol) shows ~3x latency improvement over your current GG18/20 stack, but it relies on newer class‑group cryptography that has less production history. You have a 6–9 month runway and a mobile‑first roadmap. What would you do and why?
   A: 
   - Treat Trout as a high‑leverage but high‑risk optimization: start with a focused R&D and security review instead of an all‑in rewrite.
   - Run a side‑by‑side Rust prototype comparing latency, bandwidth, and failure modes vs. your existing protocol on real mobile and backend workloads.
   - Use results to decide between (a) migrating a narrow tier (e.g., low‑value consumer flows) under a beta flag or (b) standardizing first on a more battle‑tested upgrade such as MPC‑CMP / CGGMP21.
   - Keep GG18/20 hardened and fully patched until you have third‑party audits and clear incident‑response playbooks for any new scheme.

1. Q: You are planning a 2025 consumer MPC wallet launch. Product wants a full ERC‑4337 AA stack (session keys, social recovery, paymasters) because competitors report better retention, but engineering estimates 6–9 months of work and $10K–$50K/month in gas subsidies. You must decide the AA rollout strategy. What would you do and why?
   A: 
   - Validate user priorities with quick research: confirm that gasless flows and no‑seed onboarding really are the top two drivers for your target users.
   - Choose a phased AA plan: for example, phase 1 session keys + gasless onboarding with a partner SDK; phase 2 full social recovery and custom paymaster once economics are modeled.
   - Tie investment to explicit KPIs from the news (e.g., +10–20 percentage‑point lift in onboarding completion, 35% better 90‑day retention) and require A/B tests.
   - Cap paymaster burn with budget guardrails and pricing experiments (premium tiers, fee sharing) before committing to full subsidies at large scale.

1. Q: You want EU market access by 2026. MiCA requires capital reserves (~€350K), strong KYC/AML, and CASP authorization, while sublicensing from an existing CASP would cost a 3–5% revenue share but can start in months instead of years. How would you structure your EU strategy and why?
   A: 
   - Treat sublicensing as a bridge: negotiate white‑label terms with a reputable CASP to gain near‑term EU access and validate demand.
   - In parallel, initiate your own CASP license application where long‑term economics justify it; keep a clear budget and timeline for capital, legal, and compliance build‑out.
   - Ensure your MPC architecture (key‑share model, segregation, reporting) is designed to meet MiCA custody and asset‑segregation requirements from the start.
   - Revisit the strategy once you have traction data: if EU ARR justifies it, phase out the sublicense and migrate to your own license; otherwise, keep the lighter‑weight model.

1. Q: A CVSS 8.1 TARmageddon vulnerability is disclosed in the Rust `async-tar` / `tokio-tar` ecosystem. Your CI uses `tokio-tar` in container builds for MPC signing and key‑generation images. No exploitation is visible yet, but 12 services share this dependency. What would you do and why?
   A: 
   - Treat this as a supply‑chain emergency: rapidly inventory all `tokio-tar` usages via Cargo.lock scanning across repos.
   - Plan a prioritized migration to the maintained `astral-tokio-tar` version that includes the fix, with automated tests to catch breaking changes.
   - Add SCA and policy checks so that abandoned crates and known‑vulnerable versions cannot re‑enter the dependency tree.
   - Communicate internally (and to key partners if needed) that RCE risk is being actively mitigated with concrete deadlines and verification.

1. Q: You must staff 3 senior Rust cryptography roles in the next 6–9 months. Market data shows Singapore salaries of S$18–22.5K/month (35–50% premium), U.S. senior crypto engineers at ~$216K/year, and high turnover (45–60%) for this niche. How would you design your hiring and retention strategy?
   A: 
   - Mix local and remote hiring: anchor one senior in your primary timezone and fill remaining roles remotely where compensation and talent pools are more favorable.
   - Offer a competitive but sustainable package that may combine slightly lower base with upside (equity or tokens) and meaningful research / ownership opportunities.
   - Reduce risk of churn by building a small fellowship or upskilling track so some future capacity comes from internal engineers, not just the external market.
   - Invest early in retention levers highlighted in the briefings—transparent career ladders, research time, and regular compensation reviews tied to market data.
