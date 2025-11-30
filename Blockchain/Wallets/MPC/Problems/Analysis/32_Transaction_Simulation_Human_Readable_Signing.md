# Transaction Simulation and Human-Readable Signing in MPC Wallets

**Last Updated**: 2025-11-30  
**Status**: Draft – Nine-Aspects Analysis  
**Owner**: Security & Product Engineering Team

---

## Context Recap

- **Problem title**: Transaction Simulation and Human-Readable Signing in MPC Wallets
- **Current state**:
  - Most MPC and non-MPC wallets still present users with opaque calldata or short labels when signing complex transactions (DeFi interactions, batch calls, Permit/Permit2 approvals), forcing them to “blind sign” without fully understanding outcomes
    [Source: What is Blind Signing?, Ledger Academy, 2023].
  - Blind signing is a key enabler of phishing scams that abuse ERC‑20 `permit` and Uniswap Permit2 to obtain unlimited spending approvals and drain assets after a single signature
    [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
  - Hypernative highlights that MPC wallets solved key management but left a “blind signing gap”: institutions still authorize opaque payloads without strong simulation or intent awareness, relying on human intuition and manual review
    [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
  - Emerging solutions (MetaMask + Blockaid, Tenderly Simulation API, Blocknative Simulation Platform, Alchemy Transaction Simulation API) demonstrate that real-time transaction simulation and risk analysis can be integrated directly into wallet flows
    [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024; Transaction Simulation API, Alchemy Docs, 2024; Simulation Platform, Blocknative Docs, 2024].
- **Pain points**:
  - Users sign opaque payloads (hex data, generic function names) and only see the *actual* effect once a transaction lands on-chain, leading to “post-sign regret” and fraud incidents
    [Source: What is Blind Signing?, Ledger Academy, 2023; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].
  - Permit/Permit2, signature-based approvals, and proxy/multicall patterns are heavily abused in phishing; a single malicious signature can grant unlimited allowances or redirect funds
    [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
  - Internal incident reviews attribute an estimated **20–40%** of MPC-wallet user fraud losses to blind signing of opaque approvals and complex calls, with annual losses on the order of **$500K–$2M** and 150–250 monthly support tickets for “unexpected transaction outcomes”
    [Estimate: Based on internal post‑mortems and aggregated industry scam reports (2023–2025), Medium confidence].
- **Goals** (from problem statement, made more explicit):
  - **Decode coverage**: Accurately decode and simulate ≥95% of transactions by monthly active user volume across supported chains.
  - **Fraud reduction**: Cut blind-signing–driven losses and “unexpected transaction” tickets by ≥50% within 12 months.
  - **Latency**: Keep added simulation + decode overhead ≤200 ms p95 in typical signing flows.
  - **Risk detection**: Flag ≥90% of known malicious patterns (unlimited approvals, known scam contracts, suspicious delegate/multicall patterns) with <5% false-positive rate.
  - **Timeline**: Deliver EVM transaction simulation and human-readable signing UX within 3–5 months (Q1–Q2 2025), then extend to priority non‑EVM chains.
- **Hard constraints**:
  - ABI/IDL fragmentation and lack of verified contract metadata for long‑tail contracts
    [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
  - Third‑party simulation APIs introduce latency, reliability, and cost constraints; deep on-chain simulation on mobile devices is CPU/battery limited
    [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024; Simulation Platform, Blocknative Docs, 2024].
  - Engineering capacity: ~2 FTE blockchain/security engineers for 3–5 months; operational budget **$60K** implementation + **$5K–$10K/month** for APIs and indexing.
- **Key facts**:
  - Blind signing—approving actions without seeing clear, trustworthy transaction details—is widely recognized as a systemic wallet vulnerability
    [Source: What is Blind Signing?, Ledger Academy, 2023; Blind Signing – A Security Black Hole for the Ethereum Community, Keystone Blog, 2022].
  - MetaMask and other wallets have started integrating transaction simulation and security providers (e.g., Blockaid) to flag scams before users sign
    [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].
  - Tenderly and other infra providers show that simulation can return detailed previews (balances, tokens in/out, internal calls) suitable for human-readable signing flows
    [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

1. **Core problem**  
   MPC wallet users routinely sign opaque, complex transaction payloads (Permit/Permit2 approvals, proxy calls, batched DeFi interactions) without clear visibility into *what will actually happen*, because decoding and simulation coverage is incomplete and UX is limited to generic labels. This “blind signing” behavior enables phishing and scam patterns that convert a single signature into open‑ended asset theft, causing an estimated 20–40% of overall wallet fraud losses in some environments
   [Source: What is Blind Signing?, Ledger Academy, 2023; Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024; MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].

2. **Key contradictions**
   - **Security vs. UX speed**: High‑fidelity simulation and deep decoding require network calls, contract metadata, and sometimes multiple simulations (e.g., different gas settings), which add latency and complexity. Simplified flows are faster but leave users blind to risk
     [Source: Transaction Simulation API, Alchemy Docs, 2024; Simulation Platform, Blocknative Docs, 2024].
   - **Coverage vs. maintainability**: Covering ≥95% of transactions across EVM and non‑EVM chains demands continuous ABI/IDL ingestion, protocol tracking, and signature pattern updates; under‑resourced teams default to narrow coverage on “top N” protocols, leaving a long tail of opaque interactions exploitable by attackers
     [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
   - **False positives vs. false negatives**: Strict risk heuristics catch more scams but may overwhelm users with warnings, causing alert fatigue and ignored prompts; conservative heuristics reduce noise but allow sophisticated phishing to slip through
     [Source: Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

3. **Who is in conflict?**
   - **End users** want clear, simple, near‑instant confirmations but also strong protection from scams.
   - **Security/risk teams** want high‑coverage simulation, conservative defaults, and strong warnings—even if some legitimate transactions are slowed or blocked.
   - **Product/UX** teams aim to keep signing flows under ~5 seconds and avoid disruptive warnings that hurt conversion.
   - **Infrastructure and finance** owners must manage simulation API costs and reliability while meeting fraud‑loss targets.

### 1.2 Goals & conditions

- **Decode & simulation coverage**:
  - Baseline: ~40–60% of volume with rich decoding (simple ERC‑20/NFT transfers; limited coverage for Permit/Permit2 and multicalls)
    [Estimate: Based on current wallet decode capabilities vs. DeFi usage mix, Medium confidence].
  - Target: ≥95% of transactions by volume have structured decode + simulation summary (assets in/out, approvals, key internal calls).
- **Fraud and regret reduction**:
  - Baseline: 150–250 “I didn’t expect this transaction to do that” support tickets/month; blind‑signing losses ~$500K–$2M/year (internal plus industry estimates).
  - Target: ≥50% reduction in such tickets and ≥60% reduction in blind‑signing losses within 12 months.
- **Performance & UX**:
  - Added simulation + decode overhead ≤200 ms p95 for typical EVM transactions when using regional simulation backends or efficient caching
    [Source: Transaction Simulation API, Alchemy Docs, 2024; Simulation Platform, Blocknative Docs, 2024].
  - Total signing experience (user confirm time + simulation) remains within **<5 s** for normal users; high‑risk flows may accept slightly longer.
- **Operational constraints**:
  - Timeline: 3–5 months to ship EVM support to production with incremental rollouts.
  - Budget: Implementation ~$60K plus $5K–$10K/month Opex for simulation, indexing, and security providers.
  - Team: 2 FTE engineers (security + blockchain) plus partial support from product and UX.

### 1.3 Extensibility & reframing

- **From “decode calldata” → “explain intent and outcomes”**: The real object is not only decoding function signatures but explaining *intent* (“You are granting unlimited USDC approval to contract X”) and *effect* (“Your USDC balance could decrease by up to N; contract Y gains spending rights”). This broader framing includes simulation, risk scoring, and education
  [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].
- **From “single transaction” → “session and policy”**: Instead of analyzing each transaction in isolation, think in terms of user sessions and policies (e.g., “permit only up to $500 per day to protocol A”), which changes how simulation and warnings are configured.
- **From “wallet feature” → “shared security layer”**: Simulation engines and risk providers can serve multiple wallets, custodians, and dApps as shared infrastructure, enabling economies of scale and better threat intelligence
  [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; Simulation Platform, Blocknative Docs, 2024].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements inside the problem

- **Decoding layer**: ABI/IDL resolution, function signature databases, log and event decoders, metadata for known protocols (DEXs, bridges, NFT markets)
  [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
- **Simulation engine**: On‑prem or third‑party services (Tenderly, Blocknative, Alchemy) that execute hypothetical transactions against recent state to predict outcomes (balance changes, token flows, reverts)
  [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024; Simulation Platform, Blocknative Docs, 2024; Transaction Simulation API, Alchemy Docs, 2024].
- **Risk and policy engine**: Rules, heuristics, and models to detect known scam patterns (unlimited approvals, interactions with known malicious contracts, unusual delegatecalls/multicalls, suspicious token flows)
  [Source: Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].
- **Human-readable UX**: Surfaces that summarize assets in/out, approvals, counterparties, and risk level in clear language on web/mobile and, for hardware setups, on trusted screens
  [Source: What is Blind Signing?, Ledger Academy, 2023].
- **Telemetry and logging**: Detailed logs of simulations, warnings issued, overrides, and post‑transaction outcomes to calibrate heuristics and audit incidents.

### 2.2 Balance & “degree”

- **Fidelity vs. latency**: Deeper simulations (including internal calls, gas dynamics, and multiple execution paths) improve risk coverage but increase overhead; slimming simulation to “balance deltas + approvals” reduces depth but keeps signing fast
  [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].
- **On‑device vs. remote compute**:
  - On‑device EVM execution increases privacy and independence but is limited by mobile CPU and storage.
  - Remote simulation (cloud or third‑party) is faster to iterate and can share infrastructure across customers but raises trust, privacy, and dependency concerns
    [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
- **Heuristic strictness vs. user friction**:
  - Aggressive blocking or warning on ambiguous patterns reduces missed scams but can cause false alarms and user fatigue.
  - Too permissive settings minimize friction but fail to shift fraud statistics.

### 2.3 Causal chains

1. **Permit phishing chain**  
   User visits phishing site → site requests `permit` or Permit2 signature with unlimited allowance → wallet displays generic signing prompt with opaque hex or vague label → user blindly signs → attacker later transfers tokens via approved contract without further prompts → user discovers drained balance
   [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024; What is Blind Signing?, Ledger Academy, 2023].

2. **Simulation‑absent MPC signing chain**  
   Institution integrates MPC wallet for custody → focuses on key management, not transaction semantics → signers receive only high‑level labels or hashes in signing UI → phishing or compromised dApp constructs dangerous proxy/multicall → signers approve assuming dApp vetted the details → post‑trade review reveals loss; root cause traced to lack of simulation at signing time
   [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].

3. **Simulation‑in‑the‑loop protection chain**  
   User initiates transaction → wallet invokes simulation API → engine executes transaction against latest state, decodes token movements and approvals → risk engine scores transaction and optionally compares against known malicious patterns → UI displays “You are granting unlimited USDC approval to contract X; risk: high” and blocks or requires extra confirmation → many scams are prevented before broadcast
   [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders & interactions

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream – End users (retail & prosumers) | Initiate and sign transactions using MPC wallets | Understand clearly what they are signing; avoid scams; keep flows <5 s | Limited technical knowledge; overload from too much detail | Want strong protection *and* minimal friction; may skip warnings if too frequent |
| Upstream – DApp & protocol developers | Build DeFi, NFT, and other contracts that users interact with | Smooth integration with wallets; minimal friction for legitimate flows | Limited control over wallet UX; may use complex patterns (multicalls, proxies) | May resist warnings that make their flows look “risky” or complicated |
| Downstream – Wallet/MPC providers | Operate signing infrastructure and UX | Reduce fraud losses, support costs, and reputational risk while keeping UX competitive | Budget, latency SLAs, engineering capacity | Must balance simulation depth, third-party dependencies, and UX constraints |
| Downstream – Simulation/security providers | Offer APIs for transaction preview and scam detection | Maximize adoption and accuracy; monetize per‑call or subscription | Must manage privacy, latency, and false positives | Tight integration may increase provider lock‑in and reduce wallet independence |
| Sideline/External – Regulators, auditors, insurers | Evaluate custody/security posture & consumer protection | Ensure reasonable controls against phishing and fraud | Limited visibility into technical details; evolving standards | May demand strong controls that increase friction or require disclosures |

[Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025; MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

### 3.2 Environment factors

- **Scam evolution**: Phishing campaigns increasingly target signature‑based approvals, Permit2, and sophisticated multicalls because they bypass traditional “send funds to X” patterns users recognize as risky
  [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
- **Wallet competition**: Popular wallets (e.g., MetaMask, Rabby) now market transaction simulation and security alerts as differentiating features, raising user expectations for human‑readable signing
  [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].
- **Regulatory pressure**: As consumer losses mount, regulators increasingly question whether sophisticated wallet providers took “reasonable steps” to prevent obvious phishing and blind-signing losses, especially in institutional MPC custody settings
  [Estimate: Based on global trends in crypto enforcement and consumer-protection guidance, Medium confidence].

### 3.3 Responsibility & room for maneuver

- **Wallet/MPC providers** are primarily responsible for:
  - Integrating simulation and decoding into signing flows.
  - Designing risk policies (block vs. warn) aligned with user segments and regulatory expectations.
  - Ensuring privacy and reliability of any third‑party integrations.
- **DApps and protocols** can:
  - Provide clearer metadata, ABIs, and intent descriptions.
  - Avoid unnecessarily dangerous patterns (e.g., unlimited approvals when bounded allowances suffice).
- **Simulation and security providers** must:
  - Maintain up‑to‑date threat intel and contract metadata.
  - Provide clear SLAs and privacy guarantees.
- **Users and institutions** can:
  - Choose wallets with robust simulation features.
  - Configure policies (per‑app limits, allowlists) and insist on transparent reporting of blocked/warned scams.

[Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2015–2019 – ERC‑20 and basic wallet UX**: ERC‑20 tokens and early DeFi protocols rely on `approve` + `transferFrom` patterns; wallets display minimal information, but scams are relatively unsophisticated
   [Source: Ethereum ERC‑20 Token Standard, Ethereum Foundation Docs, 2017].
2. **2019–2021 – Permit and Permit2**: EIP‑2612 introduces `permit` for gasless approvals; Uniswap launches Permit2 to standardize approvals across tokens. Phishing attacks pivot to off‑chain signatures granting broad allowances
   [Source: EIP‑2612: permit – 712-signed approvals, Ethereum Improvement Proposals, 2019; Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
3. **2020–2023 – MPC wallet adoption**: MPC wallets solve key‑management challenges for institutions and advanced users, but their signing flows remain largely opaque, with limited simulation
   [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
4. **2022–2024 – Early simulation deployments**: Wallets and infra providers roll out transaction preview and security alerts using simulation APIs and security providers (e.g., Blockaid), proving feasibility at scale
   [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Blockchains were designed for machine verification, not human readability; calldata and contract logic are inherently low‑level.
  - Wallet UX historically focused on key control and gas settings rather than semantic explanations of complex DeFi actions.
- **Direct technical causes**:
  - Lack of integrated transaction simulation and decoding in MPC signing flows.
  - No consistent intent schema or metadata across dApps; long‑tail contracts have no verified ABI or human‑readable descriptions.
  - Risk analysis limited to address allowlists/blacklists without full execution context.

[Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025; What is Blind Signing?, Ledger Academy, 2023].

### 4.3 Root issues

- **Semantic gap**: Large gap between low‑level calldata and the human’s mental model of “send 100 USDC to Alice” or “stake tokens in protocol X”. Simulation and decoding aim precisely to close this gap but are not yet ubiquitous.
- **Incomplete threat modeling**: Many wallet designs assumed that if a user clicks “Sign”, they bear responsibility for understanding the transaction, underestimating phishing sophistication and cognitive overload.
- **Underinvestment in shared infrastructure**: Until recently, there was no strong ecosystem of simulation and security providers; many teams tried to build ad hoc decoders instead of leveraging specialized infra.

[Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- Blind‑signing scams are trending upward as attackers refine Permit/Permit2 and signature‑based patterns
  [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
- Competing wallets increasingly differentiate on simulation and security alerts; providers that lack comparable features risk being perceived as unsafe or outdated
  [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023].
- Institutions using MPC wallets without robust simulation continue to face tail‑risk events where a single compromised operator or phishing attack causes outsized losses and difficult post‑mortem explanations to clients and regulators
  [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].

### 5.2 Early signals

- Growing educational content from hardware wallet vendors and security teams warning explicitly about blind signing and recommending clearer signing flows
  [Source: What is Blind Signing?, Ledger Academy, 2023].
- Rapid rise of specialized transaction simulation APIs and security providers integrated into popular wallets and dApps.
- Increased mention of “transaction preview”, “simulation”, and “security alerts” in wallet marketing, suggesting user demand for more transparent signing.

### 5.3 6–24 month scenarios

- **Optimistic**:  
  High‑coverage simulation and human‑readable signing become baseline features in major MPC and non‑MPC wallets. Blind‑signing‑driven losses drop by ≥60%, support tickets halve, and regulators cite such controls as examples of good practice.
- **Baseline**:  
  Leading providers integrate simulation for EVM chains and major protocols, but coverage gaps remain for long‑tail contracts and non‑EVM ecosystems. Losses and complaints decline moderately but not dramatically.
- **Pessimistic**:  
  Simulation adoption stalls due to cost and complexity. Attackers continue exploiting Permit/Permit2 and multicalls. One or more high‑profile institutional incidents highlight blind signing in MPC contexts, prompting reactive, regulator‑driven changes.

[Estimate: Based on current product roadmaps and public feature announcements, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Mature infra providers**: Tenderly, Blocknative, and Alchemy already offer high‑quality simulation and preview APIs with wallet‑specific guides
  [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024; Simulation Platform, Blocknative Docs, 2024; Transaction Simulation API, Alchemy Docs, 2024].
- **MPC security expertise**: Existing teams have strong cryptographic and security backgrounds, positioning them well to reason about transaction semantics and risk.
- **Telemetry & logs**: Current systems likely already log transactions, addresses, and failures, which can be mined for training and calibrating risk heuristics.

### 6.2 Capability gaps

- **Cross‑chain decode and ABI management**: Limited tooling to continuously ingest and maintain ABIs/IDLs across EVM and non‑EVM chains.
- **Dedicated risk analytics**: Need for specialists who combine blockchain analytics, UX, and security product thinking rather than pure protocol or backend engineers.
- **Trusted UI for signers**: In institutional MPC setups, signer UIs may lack rich displays; improving trusted surfaces (dedicated signing terminals or secure mobile apps) is non‑trivial.

### 6.3 Buildable capabilities (1–6 months)

- Establish a **transaction semantics team** combining 1–2 engineers and 1 product/UX specialist to own simulation, decoding, and human-readable UX.
- Integrate with at least one major simulation provider (Tenderly, Blocknative, Alchemy) for EVM chains, with an abstraction layer to allow future provider changes.
- Build an internal **pattern library** of high‑risk signatures and behaviors (unlimited approvals, suspicious delegatecalls, interacting with known malicious contracts) and map them to user‑facing warnings.

[Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline (summary)

1. **Background**: Blind signing remains a core weakness in both MPC and non‑MPC wallets; scam patterns are increasingly centered on signatures and approvals.
2. **Problem**: Lack of comprehensive simulation, decoding, and human‑readable UX leads users to approve dangerous transactions they do not understand.
3. **Analysis**: Internal trade‑offs (latency, coverage, false‑positive rates), ecosystem forces (scam evolution, regulatory pressure), and available simulation infra.
4. **Options**: Third‑party simulation integration, in‑house simulation, hybrid risk providers, and layered UX protections.
5. **Risks**: Over‑reliance on single vendors, alert fatigue, implementation bugs, and privacy concerns.

### 7.2 Key judgments (to validate)

- **【P0】** High‑coverage transaction simulation and human-readable signing can reduce blind‑signing‑driven fraud and regret incidents by ≥50% within 12 months if properly deployed and tuned
  [Estimate: Based on early results from wallets integrating simulation and security providers; Medium confidence].
- **【P0】** Permit/Permit2 phishing and opaque multicalls will remain dominant vectors for some time; designing explicitly against these patterns yields outsized risk reduction
  [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
- **【P1】** Users will tolerate ~100–200 ms additional latency in signing flows if the output is clear, trustworthy explanations and obvious risk reduction
  [Source: Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].
- **【P1】** Overly noisy risk warnings will backfire via alert fatigue; careful UX and threshold tuning are as important as simulation accuracy.

### 7.3 Alternative high-level paths

- **Option A – Third‑party simulation first**: Integrate one or more mature simulation providers (Tenderly/Blocknative/Alchemy) and focus efforts on risk policies and UX.
- **Option B – In‑house simulation and decode engine**: Build custom EVM simulation and decoding in‑house for maximum control and privacy, using external providers only as fallback.
- **Option C – Hybrid “security provider” model**: Use specialized providers (e.g., Blockaid‑like services) that combine simulation, threat intel, and risk scoring while retaining the ability to override or complement with internal rules.

[Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Security vendor bias**: Over‑relying on vendor marketing claims about detection rates and latency without independent validation.
- **UX optimism bias**: Assuming users will carefully read and act on detailed simulation output; in reality, many click through prompts.
- **Data visibility bias**: Internal incident data may under‑report blind‑signing fraud because many victims never contact support or cannot articulate what went wrong.

[Source: Using transaction security providers to protect yourself from scams, MetaMask Support, 2024; What is Blind Signing?, Ledger Academy, 2023].

### 8.2 Required intelligence

- **Empirical incident data**: Detailed categorization of fraud and support tickets by root cause (blind signing vs. other).
- **A/B tests** of different simulation UX variants (minimal vs. rich detail, explicit risk scores vs. simple “safe/unsafe” labels) and their impact on completion rates and scam prevention.
- **Latency and cost benchmarks** across simulation providers at realistic traffic volumes and chain coverage.

### 8.3 Validation plan

1. **Instrument current state (Month 1)**
   - Tag signing flows with whether simulation is present, which warnings (if any) are shown, and subsequent fraud/support incidents.
2. **Run pilot of simulation + human-readable signing (Months 2–3)**
   - Enable for a subset of EVM users and measure changes in:  
     a) frequency of blind‑signing‑like signatures,  
     b) fraud incidents tied to approvals and complex DeFi calls,  
     c) user drop‑off in signing flows.
3. **Compare providers / configurations (Months 3–4)**
   - Benchmark at least two simulation/risk configurations (e.g., vendor A vs. vendor B vs. in‑house) across accuracy, latency, coverage, and cost.
4. **Refine policies and UX (Months 4–5)**
   - Tune thresholds, wording, and escalation paths (e.g., extra confirmation for high‑risk actions) based on pilot data.

[Estimate: Based on typical product experimentation cycles in wallet and fintech teams, Medium confidence].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative estimates for fraud reduction and coverage will change as real telemetry and A/B results arrive.
- Preferred architecture may shift if more efficient or privacy‑preserving simulation techniques emerge, or if regulatory guidance demands specific controls.

### 9.2 Incremental approach

- Start with **EVM‑only** support for high‑volume chains and top protocols; expand to long‑tail and non‑EVM later.
- Roll out simulation **as warnings first**, then selectively enforce blocks for well‑understood high‑risk patterns.
- Introduce **opt‑in advanced details** for expert users while keeping default views simple.

### 9.3 “Good enough” criteria

- ≥95% by volume of EVM transactions have simulation results with clear human‑readable summaries.
- Blind‑signing‑related fraud incidents and “unexpected transaction” tickets reduced by ≥50% from baseline.
- No material increase in legitimate transaction abandonment beyond agreed thresholds (e.g., <5–10% relative change for core flows).

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Blind signing of opaque payloads—especially Permit/Permit2 approvals, proxy calls, and multicalls—is a primary driver of wallet scams and regret incidents
   [Source: What is Blind Signing?, Ledger Academy, 2023; Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].
2. MPC wallets have historically focused on key management and protocol security but left the semantic layer (what is being signed) underspecified, creating a “blind signing gap” that institutions are now pressured to close
   [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025].
3. Practical transaction simulation and risk analysis are already deployed at scale in leading wallets; the challenge is not feasibility but coverage, latency, UX design, and governance over third‑party dependencies
   [Source: MetaMask enables privacy-preserving security alerts with Blockaid, MetaMask, 2023; How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].
4. A structured program combining simulation integration, decode coverage expansion, human-readable UX, and data‑driven risk tuning can plausibly cut blind‑signing losses by ≥50% within a year.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric (baseline → target) → Date**

- **【P0 – Critical】 Integrate baseline EVM transaction simulation into signing flow**  
  → Security & Blockchain Eng Lead  
  → Metric: % of EVM tx with simulation preview in pilot cohort: 0% → ≥80%  
  → Date: 2025-03-31  
  [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024].

- **【P0 – Critical】 Design and ship human-readable signing UX for approvals and complex DeFi interactions**  
  → Product & UX Lead  
  → Metric: Coverage of top protocols (by tx volume) with structured summaries: 0% → ≥90%  
  → Date: 2025-03-31  
  [Source: What is Blind Signing?, Ledger Academy, 2023; Using transaction security providers to protect yourself from scams, MetaMask Support, 2024].

- **【P1 – Important】 Implement risk rules for high‑risk patterns (unlimited approvals, known scam contracts, suspicious multicalls)**  
  → Security Team  
  → Metric: Detection coverage of known high‑risk patterns in backtest: 0% → ≥90%  
  → Date: 2025-04-30  
  [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024].

- **【P1 – Important】 Launch A/B tests for simulation UX variants**  
  → Product Analytics  
  → Metric: Fraud/support incidents per 1,000 tx in control vs. treatment; change in completion rates  
  → Date: 2025-04-30.

- **【P2 – Optional】 Explore non‑EVM and hardware‑wallet integration paths**  
  → Architecture & Research  
  → Metric: Feasibility report and prototype for at least one non‑EVM chain and one hardware‑wallet partner  
  → Date: 2025-06-30  
  [Source: Transaction Verification: A Solution to Blind Signing in Hardware Wallets, Blockaid Blog, 2023].

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Over‑reliance on single simulation provider | High | Medium | Provider outage, pricing changes, or quality issues | Build abstraction layer; support multiple providers and in‑house fallback for critical chains | Eng Lead |
| Alert fatigue from excessive or poorly tuned warnings | Medium | High | Users frequently override or disable warnings; support complaints about “spammy” prompts | Iterative UX research; tiered warnings; separate high‑risk blocks from low‑risk informational hints | Product & UX Lead |
| Privacy or data‑sharing concerns with third‑party providers | High | Medium | Regulatory or client objections to sharing transaction data for simulation | Use privacy‑preserving designs (e.g., local hashing, limited data fields); negotiate data‑handling terms; prefer on‑prem or VPC deployment options | Legal & Security |
| Implementation bugs causing incorrect previews or missed risks | High | Medium | Incidents where preview showed safe outcome but actual tx caused loss | Independent testing; shadow simulation vs. mainnet outcomes; phased rollouts; external audits of critical logic | Security & QA |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Third‑party simulation as primary engine** | Fast time‑to‑market; leverages mature infra and threat intel | Ongoing API costs; dependency on external SLAs | Vendor lock‑in; privacy concerns; regional outages | Need quick coverage for EVM with limited internal capacity | When strict data‑sovereignty or on‑prem requirements block third‑party use |
| **B. In‑house simulation & decoding** | Maximum control and privacy; tailored optimizations | High initial build and maintenance cost; slower rollout | Underestimation of complexity; lagging feature parity with ecosystem | Large scale, strong infra team, and long‑term commitment | When team is small or timeline is <3–4 months |
| **C. Hybrid security provider (simulation + risk scoring)** | Combines simulation with curated risk intel; offloads much detection logic | Similar dependency and cost issues; black‑box risk models may be hard to audit | Missed edge cases; difficulty tuning to specific user segments | When team wants strong protection with minimal internal data‑science effort | When regulators or clients demand fully explainable, in‑house risk models |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Blind signing** | Approving a transaction or message without being able to verify its details (e.g., opaque hex or unclear summary) | N/A | Major cause of wallet scams and user errors [Source: What is Blind Signing?, Ledger Academy, 2023] |
| **Transaction simulation** | Executing a hypothetical transaction against recent blockchain state to predict outcomes (balance changes, token transfers, internal calls) without broadcasting on‑chain | N/A | Basis for transaction preview and security alerts [Source: How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API, Tenderly Docs, 2024] |
| **Human-readable signing** | UX pattern that presents clear natural‑language summaries of what a signature or transaction will do (assets, approvals, risks) instead of raw calldata | N/A | Key approach to reducing blind‑signing risk |
| **Permit (EIP‑2612)** | ERC‑20 extension enabling off‑chain, EIP‑712‑signed approvals (`permit`) that set allowances without separate on‑chain `approve` transactions | N/A | Widely used but frequently abused in phishing [Source: EIP‑2612: permit – 712-signed approvals, Ethereum Improvement Proposals, 2019] |
| **Permit2** | Uniswap‑designed contract and standard to unify token approvals and improve UX; also targeted by phishing schemes exploiting signature‑based approvals | N/A | Important vector for approval‑based scams [Source: Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing, Gate Learn, 2024] |
| **Transaction security provider** | Service that analyzes pending transactions or signature requests, often via simulation and threat intel, and returns risk assessments or alerts | N/A | Used in MetaMask integrations with Blockaid [Source: Using transaction security providers to protect yourself from scams, MetaMask Support, 2024] |
| **Decode coverage** | Proportion of transactions for which the wallet can produce structured, human‑readable explanations (functions, parameters, assets affected) | % of tx volume | Key success metric for simulation + decoding program |
| **False positive rate (FPR)** | Percentage of benign transactions incorrectly flagged as risky | % | Tuning FPR is crucial to avoid alert fatigue |
| **False negative rate (FNR)** | Percentage of truly malicious or high‑risk transactions not flagged by the detection system | % | Lowering FNR is central to fraud reduction goals |
| **MPC wallet** | Wallet architecture in which private keys are split into multiple shares and signatures are produced via multi‑party computation rather than a single key holder | N/A | Target environment for this problem [Source: MPC Wallet Security in 2025: Solving the Blind Signing Gap, Hypernative, 2025] |
| **Trusted display** | Device or screen that shows verified transaction details independently of potentially compromised software, helping users avoid blind signing | N/A | Important for hardware‑wallet and institutional setups [Source: What is Blind Signing?, Ledger Academy, 2023] |

---

## 12. References

### Tier 1 – Standards & Specifications

1. **Ethereum Foundation / EIP Editors.** (2019). *EIP‑2612: permit – 712-signed approvals*. Ethereum Improvement Proposals. https://eips.ethereum.org/EIPS/eip-2612  
   **[Cited in**: 4.1, 11 **]**

### Tier 2 – Industry Reports, Vendor Docs & Security Guides

2. **Hypernative.** (2025). *MPC Wallet Security in 2025: Solving the Blind Signing Gap*. Hypernative Blog. https://www.hypernative.io/blog/mpc-wallet-security-in-2025-solving-the-blind-signing-gap  
   **[Cited in**: Context Recap, 1–4, 6, 7, 10, 11 **]**

3. **Ledger.** (2023). *What is Blind Signing?* Ledger Academy. https://www.ledger.com/academy/cryptos-greatest-weakness-blind-signing-explained  
   **[Cited in**: Context Recap, 1, 2, 4, 5, 8, 10, 11 **]**

4. **Gate Learn.** (2024). *Is your wallet safe? How hackers exploit Permit, Uniswap Permit2, and signatures for phishing.* Gate.io Learn. https://www.gate.com/learn/articles/is-your-wallet-safe-how-hackers-exploit-permit-uniswap-permit2-and-signatures-for-phishing/4197  
   **[Cited in**: Context Recap, 1, 2, 4, 5, 7, 10, 11 **]**

5. **MetaMask.** (2023). *MetaMask enables privacy-preserving security alerts with Blockaid to protect users and flag malicious dapps.* MetaMask News. https://metamask.io/news/metamask-enables-privacy-preserving-security-alerts-with-blockaid  
   **[Cited in**: Context Recap, 2, 3, 5, 6, 7, 10 **]**

6. **MetaMask Support.** (2024). *Using transaction security providers to protect yourself from scams.* MetaMask Help Center. https://support.metamask.io/stay-safe/safety-in-web3/using-transaction-security-providers-to-protect-yourself-from-scams  
   **[Cited in**: Context Recap, 1, 2, 3, 6, 7, 8, 10 **]**

7. **Tenderly.** (2024). *How to Add Transaction Preview to a Rabby Wallet Using Tenderly Simulation API.* Tenderly Documentation. https://docs.tenderly.co/simulations/guides/how-to-add-transaction-preview-to-a-rabby-wallet-using-tenderly-simulation-api  
   **[Cited in**: Context Recap, 2, 6, 7, 8, 10 **]**

8. **Blocknative.** (2024). *Simulation Platform.* Blocknative Docs. https://www.blocknative.com/simulation-platform  
   **[Cited in**: Context Recap, 1.2, 2.1, 6 **]**

9. **Alchemy.** (2024). *Transaction Simulation API.* Alchemy Documentation. https://www.alchemy.com/transaction-simulation  
   **[Cited in**: Context Recap, 1.2, 2.1, 6 **]**

10. **Blockaid.** (2023). *Transaction Verification: A Solution to Blind Signing in Hardware Wallets.* Blockaid Blog. https://www.blockaid.io/blog/transaction-verification-a-solution-to-blind-signing-in-hardware-wallets  
   **[Cited in**: 10.2 **]**

11. **Keystone.** (2022). *Blind Signing — A Security Black Hole for the Ethereum Community.* Keystone Blog. https://blog.keyst.one/blind-signing-a-security-black-hole-for-the-ethereum-community-13f909b848b6  
   **[Cited in**: Context Recap, 4 **]**

### Internal & Estimates

12. **Problem Statement – Transaction Simulation and Human-Readable Signing.** (2025). Internal documentation (Security & Product Engineering Team).  
   **[Cited in**: Context Recap; Sections 1–3, 5–10 **]**

13. **Supplementary Analysis – Blockchain MPC Wallet Problem Extraction (GPT5).** (2025-11-28). Internal analysis, lines 221–230.  
   **[Used for**: Baseline estimates of loss distribution and decode coverage; treated as estimates requiring external validation **]**

14. **Estimates & Assumptions.** Various.  
   Method: Synthesis of internal incident data, public scam‑loss reports, and qualitative evidence from industry blogs and vendor docs (2023–2025). Confidence: Medium. Validation: A/B tests and telemetry in production.  
   **[Used in**: Context Recap; Sections 1, 5, 7–10 **]**
