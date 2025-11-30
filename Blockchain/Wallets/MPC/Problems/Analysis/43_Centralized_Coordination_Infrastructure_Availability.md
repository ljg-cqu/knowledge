# Centralized Coordination Infrastructure Creating Single Point of Failure in MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Infrastructure & Security Team

---

## Pre-Section: Context Recap

- **Problem title**: Centralized coordination infrastructure creating single point of failure in MPC wallets
- **Current state**:
  - Most production MPC wallets rely on vendor-operated coordination servers (Firebase Cloud Messaging, Amazon SQS, proprietary APIs/WebSockets) to relay multi-round protocol messages between key-share holders during DKG and signing.
    [Source: "MPC Wallets: A Complete Technical Guide (2025)", Stackup, Sections "How MPC Wallets Actually Work" and "Network Communication in MPC".]
  - These coordination servers are typically deployed in one or a few cloud regions (often AWS US-EAST-1) under a single vendor’s administrative control, creating tightly coupled dependencies.
    [Source: AWS cloud outage analysis, TechTarget, 2025, "Executive summary" and "The cloud dependency dilemma"; Problem statement – Background and current situation.]
  - October 20–21, 2025 AWS US-EAST-1 DNS/DynamoDB outage took down Coinbase, Base L2, Infura, Robinhood and other platforms that market themselves as "decentralized" but were hosted centrally, exposing infrastructure centralization risk.
    [Source: "Your 'Decentralized' Crypto Platform Just Crashed Because of Amazon AWS Outage", CoinCentral, 2025, TLDR & outage description; "The AWS Outage Shows Why Crypto Can't Keep Relying On Centralized Infrastructure", CoinDesk, 2025.]
- **Pain points**:
  - Coordination server downtime, DDoS, or censorship can globally block transaction signing even when all key shares remain safe, contradicting the core value proposition of MPC wallets as eliminating single points of failure.
    [Source: Silence Laboratories–Waku partnership blog summary, 2023, quoted in problem statement; "MPC does have a single point of failure", Cubist Blog, 2024.]
  - Vendor or cloud provider concentration (e.g., AWS dominance) creates correlated outage risk across multiple wallets, custodians and L2s, amplifying systemic impact.
    [Source: TechTarget, 2025, "AWS cloud outage reveals vendor concentration risk"; CoinCentral, 2025 AWS outage report.]
  - Government censorship or sanctions enforced at the coordination layer (coercing vendors) can selectively block users or jurisdictions without touching the underlying blockchain.
    [Source: Silence Laboratories blog summary, 2023; Problem statement – Background and current situation.]
  - Vendor business failure, acquisition, or unilateral shutdown of the coordination service can permanently strand user funds if no alternative path for message coordination exists.
    [Source: "Decentralized MPC — The Future Infrastructure for Crypto Wallets", Decentralized MPC Blog, 2024, architecture discussion; Problem statement – Problem description and historical attempts.]
- **Goals** (from problem statement, refined):
  - **Operational independence**: ≥99% signing success rate during primary vendor coordination outages by Q4 2026, via decentralized relays, offline signing, and multi-vendor fallback (current: ~0% when server down).
  - **Censorship resistance**: Remove any single actor’s unilateral ability to block transactions at coordination layer; target 0 vendor-initiated censorship incidents by Q4 2026.
  - **Vendor diversification**: Reduce single-provider dependence so that no more than 20% of traffic for any major MPC wallet depends on a single cloud region or vendor by Q4 2027.
  - **Business continuity**: Ensure 100% recoverability of user assets and signing capability in the event of coordination vendor failure by Q4 2026.
  - **Transparency**: ≥80% of MPC wallet providers publicly disclose coordination architecture, dependencies, and SLAs by Q2 2026.
  [Source: Problem statement – Goals and success criteria.]
- **Hard constraints**:
  - Time window: Q1 2026–Q4 2027 (24 months) for peer-to-peer integration, multi-vendor rollout, and ecosystem adoption.
  - Budget: Roughly USD 2–6M per major provider for decentralized relay integration, multi-cloud deployment, offline signing, testing and migration; industry-wide USD 10–30M for 10–15 providers.
  - UX constraints: Peer-to-peer discovery adds 1–5 seconds of latency vs. <500 ms for centralized relays; offline signing flows are more complex and may reduce conversion.
  - Regulatory constraints: Some regulators prefer centralized chokepoints for AML/KYT, creating tension with censorship resistance.
  [Source: Problem statement – Key constraints and resources.]
- **Key facts**:
  - MPC wallets require multi-round communication and currently rely heavily on centralized message relays; 2-of-2 consumer MPC implementations typically involve a user device share and a provider share, both needing to be online during signing.
    [Source: Stackup, 2025, Sections "How MPC Wallets Actually Work", "Real-World Implementations", "Network Communication in MPC".]
  - MPC deployments already experience non-trivial signing latencies (2–5 seconds for 2-of-2, 5–15 seconds for 3-of-5) due to network coordination alone, before adding any decentralized relays.
    [Source: Stackup, 2025, "Performance Benchmarks and Limitations" – Signing Speed Reality.]
  - Cloud outages (AWS, Azure) and infrastructure incidents increasingly highlighted vendor concentration as systemic risk; financial regulators have started classifying hyperscale providers as critical third parties with resilience obligations.
    [Source: TechTarget, 2025, "AWS cloud outage reveals vendor concentration risk"; CoinDesk, 2025 AWS outage op-ed; UK FCA/EBA critical third party guidance summarized in TechTarget article.]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   MPC wallets are marketed as eliminating single points of failure by distributing key shares, yet in practice they often depend on a centralized, vendor-controlled coordination layer (APIs, message queues, Firebase/SQS relays) deployed on a small number of cloud regions. Outages, DDoS, regulatory orders or business decisions affecting these coordination servers can halt signing for all users globally, effectively reintroducing a central single point of failure at the infrastructure layer.
   [Source: Silence Laboratories–Waku blog summary, 2023 ("single point of control or DOS vector"); Stackup, 2025, "Network Communication in MPC"; Cubist, 2024, "MPC does have a single point of failure".]

2. **Key contradictions**
   - **"Decentralized" branding vs. centralized infrastructure**: Blockchain and MPC protocols are distributed, but coordination servers and cloud regions are centralized, so operational availability is bounded by the weakest centralized component.
     [Source: CoinCentral, 2025 AWS outage article; CoinDesk, 2025, "The AWS Outage Shows Why Crypto Can't Keep Relying On Centralized Infrastructure".]
   - **Security of keys vs. availability of signing**: Keys may be cryptographically safe due to MPC, but users are still locked out from funds when coordination servers fail, undermining actual user-perceived security.
     [Source: Stackup, 2025, "Security Benefits and Trade-offs of MPC Wallets"; Problem statement – Pain points.]
   - **Cost/latency vs. resilience**: Centralized cloud relays provide low-latency, simple operations and strong SLAs; decentralized relays and multi-cloud deployments add cost, complexity and latency but are needed for resilience and censorship resistance.
     [Source: TechTarget, 2025, sections on multi-region/multi-cloud strategies; Stackup, 2025, "Performance Benchmarks"; CoinDesk, 2025.]

3. **Who is in conflict?**
   - Product and growth teams who value fast UX, low cost, and simple centralized infrastructure.
   - Security and infrastructure engineers pushing for decentralization, multi-cloud, and peer-to-peer relays that add latency and complexity.
   - Regulators and compliance teams who may prefer centralized chokepoints for monitoring vs. users in censored or sanctioned regions who need censorship resistance.
   - Decentralized protocol teams (Waku, Nostr, etc.) advocating for permissionless infrastructure vs. commercial wallet vendors who must manage SLAs and support.
   [Source: Problem statement – Stakeholders; TechTarget, 2025; Coindesk, 2025.]

### 1.2 Goals and conditions

- **Security/availability goal**: Ensure MPC wallets remain usable (≥99% signing success in outage conditions) even when any single coordination vendor, cloud region, or network path is unavailable.
  [Estimate based on: problem statement target of ≥99% success during outages, Medium confidence.]
- **Censorship-resistance goal**: Architect coordination so that no single corporate or governmental actor can prevent honest parties from coordinating a signing session, within legal constraints.
  [Source: Silence Labs–Waku blog summary, 2023; Decentralized MPC Blog, 2024.]
- **Business-continuity goal**: Provide a deterministic migration and recovery path if a vendor exits (bankruptcy, acquisition, regulatory ban) without stranding funds.
  [Source: Problem statement – Business continuity and vendor failure scenarios.]
- **Economic goal**: Limit TCO increase for decentralization measures to ≤3–5× current coordination costs while still achieving target resilience.
  [Estimate based on: Problem statement – cost multipliers; TechTarget, 2025, multi-cloud cost trade-offs, Medium confidence.]
- **Regulatory goal**: Maintain or improve compliance posture by making dependencies transparent and clearly defining shared responsibility with cloud and relay providers.
  [Source: TechTarget, 2025; FCA/EBA critical third-party guidance as summarized there.]

### 1.3 Extensibility and reframing

- **Attribute reframing – "one object, many attributes"**:  
  The "object" is not just the MPC protocol but the full *coordination fabric* (clients, relays, cloud regions, DNS, routing, discovery). Attributes include centralization vs. distribution, trust assumptions, regulatory posture, latency, and vendor diversity. Reframing improves solution space beyond "MPC or not" to "how do we architect the whole stack to avoid single points of failure?"
  [Source: Stackup, 2025, sections on "Network Communication" and "Security Benefits and Trade-offs"; TechTarget, 2025.]

- **Scope reframing – infrastructure vs. cryptography**:  
  The issue is less about cryptographic soundness and more about infrastructure design. Even perfectly secure MPC protocols become operationally centralized if all parties depend on one relay or DNS zone.
  [Source: Cubist, 2024, "MPC does have a single point of failure"; CoinDesk, 2025.]

- **Risk reframing – from "availability incident" to "systemic concentration risk"**:  
  Rather than treating each cloud outage as an isolated incident, treat coordination centralization as a *systemic risk* similar to single-supplier risk in traditional supply chains.
  [Source: TechTarget, 2025, "vendor concentration risk"; CoinCentral, 2025; Problem statement – Time scale and impact scope.]

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Client endpoints**: Mobile apps, browser extensions, backend services that hold key shares and initiate signing.
- **Coordination servers**: Vendor-operated APIs, WebSockets, or message queues (e.g., Firebase, Amazon SQS, custom relay services) that route messages and orchestrate protocols.
  [Source: Silence Labs–Waku blog summary, 2023; Problem statement – Background.]
- **Cloud infrastructure**: Underlying cloud regions (AWS, GCP, Azure) hosting coordination servers, DNS, databases (e.g., DynamoDB).
  [Source: TechTarget, 2025; CoinCentral, 2025.]
- **Decentralized relays (potential)**: Waku/libp2p-based relay networks, Nostr relays, IPFS for data availability.
  [Source: Silence Labs–Waku blog summary; Waku.org; Nostr.com.]
- **Offline / local coordination channels**: Bluetooth, local network, QR-code based message passing to enable signing when internet or relays are unavailable.
  [Source: Problem statement – Key constraints and resources (offline signing).]
- **Observability and control plane**: Monitoring, routing policies, failover logic, and feature flags that decide which coordination paths are used.

### 2.2 Balance and "degree" issues

- **Latency vs. decentralization**:  
  Centralized relays can keep MPC signing within 2–5 seconds for 2-of-2 wallets and 5–15 seconds for 3-of-5 models; adding peer-to-peer gossip or multi-hop routing can increase this by seconds.
  [Source: Stackup, 2025, "Performance Benchmarks".]

- **Operational simplicity vs. resilience**:  
  Single-vendor, single-region deployments are easy to operate and debug but fail catastrophically; multi-region, multi-cloud and decentralized relays reduce correlated failure risk but increase configuration complexity and operational load.
  [Source: TechTarget, 2025, "Lessons and leadership imperatives"; Problem statement – Key constraints.]

- **Regulatory oversight vs. censorship resistance**:  
  Central coordination allows easier AML/KYT and account blocking, aligning with regulators; decentralized relays and offline signing make coordinated censorship harder, benefiting users in censored regimes but complicating compliance.
  [Source: Problem statement – Stakeholders; Stackup, 2025, "Regulatory Landscape and Compliance".]

### 2.3 Causal chains

1. **Cloud outage chain**:  
   DNS or database failure in AWS US-EAST-1 ⇒ coordination servers unreachable ⇒ MPC clients cannot exchange protocol messages ⇒ signing ceremonies fail globally ⇒ users locked out of funds despite healthy blockchains and intact key shares.
   [Source: CoinCentral, 2025 AWS outage TLDR; TechTarget, 2025, root-cause description.]

2. **Censorship chain**:  
   Government issues order or informal request to vendor / cloud provider ⇒ coordination servers add filters or geoblocks for certain IP ranges, user IDs or jurisdictions ⇒ affected users cannot complete signing despite meeting protocol thresholds ⇒ de facto censorship at infrastructure layer, invisible on-chain.
   [Source: Silence Labs–Waku blog summary; Problem statement – Censorship and sanctions discussion.]

3. **Vendor failure chain**:  
   Vendor shuts down coordination service (business failure, acquisition, pivot) without open-sourcing server code or providing migration tooling ⇒ no alternative infrastructure available using same coordination protocol ⇒ users hold key shares but have no coordination fabric ⇒ permanent or prolonged lockout.
   [Source: Decentralized MPC Blog, 2024; Problem statement – Business continuity and shutdown scenarios.]

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Cloud providers (AWS, GCP, Azure), DNS providers, push notification services (Firebase) | High availability, revenue, regulatory compliance, manageable complexity | Cannot guarantee 100% uptime; subject to their own operational incidents and regulations | Wallet providers depend heavily on a small number of regions/services |
| Downstream | MPC wallet providers, custodians, DeFi integrators | Reliable signing, strong uptime SLAs, compliance, competitive UX | Limited budgets; pressure for rapid shipping; existing centralized architectures | Security vs. UX/cost tension; reluctance to add latency or complexity |
| Sideline / External | End users (retail/institutional), regulators, censorship targets, decentralized relay projects (Waku, Nostr) | Asset safety, continuous access, fair markets, legal compliance (regulators), censorship resistance (targets) | Limited visibility into infra; conflicting priorities (control vs. freedom) | Regulators may discourage strong censorship resistance; users in restricted regions need it most |

[Source: Problem statement – Stakeholders and roles; Stackup, 2025; TechTarget, 2025; Waku.org; Nostr.com.]

### 3.2 Environmental factors

- **Macro cloud concentration**: Three large providers (AWS, Azure, GCP) dominate; a single regional outage can disrupt thousands of services and ripple through SaaS and API dependencies.
  [Source: TechTarget, 2025, "The cloud dependency dilemma"; CoinCentral, 2025.]
- **Crypto infra centralization patterns**: Exchange frontends, RPC providers (e.g., Infura), analytics services and L2 sequencers frequently run in a small set of cloud regions, creating a shared blast radius.
  [Source: CoinCentral, 2025, sections on Coinbase, Base, Infura; CoinDesk, 2025 AWS outage op-ed.]
- **Evolving decentralized infra**: Protocols like Waku/libp2p, Nostr, Lit, dWallet, ARPA, ICP and others propose decentralized coordination and threshold signing infrastructures but are still maturing and not yet default in mainstream wallets.
  [Source: Silence Labs–Waku announcement, 2023; Decentralized MPC Blog, 2024; project documentation listed in problem references.]
- **Regulatory treatment of critical third parties**: Financial regulators increasingly classify large cloud providers as critical third parties, requiring resilience plans, but ultimate responsibility for continuity still falls on financial institutions and wallet providers.
  [Source: TechTarget, 2025, regulatory discussion section.]

### 3.3 Responsibility and room for maneuver

- **Wallet providers and custodians**:  
  Hold primary responsibility for user-facing uptime and architecture; can choose to integrate decentralized relays, multi-cloud, and offline signing, and to publish transparent architecture diagrams and SLAs.
- **Cloud providers**:  
  Responsible for improving their own resilience and transparency but cannot remove concentration risk alone; can offer multi-region primitives and better outage communication.
- **Decentralized infra projects**:  
  Need to provide production-grade SDKs, benchmarks and integration guides that meet wallet providers’ performance and operational requirements.
- **Regulators and industry bodies**:  
  Can set expectations around resilience, multi-provider strategies, and third-party risk management without prescribing specific architectures.

[Source: TechTarget, 2025, "Lessons and leadership imperatives"; Problem statement – Stakeholders; Decentralized MPC Blog, 2024.]

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **2018–2022 – First-generation MPC wallet deployments**:  
   MPC wallet vendors (Fireblocks, ZenGo, Coinbase WaaS, BitGo, Web3Auth, etc.) adopt centralized coordination servers on major clouds to achieve fast time-to-market and low-latency UX.
   [Source: Decentralized MPC Blog, 2024, historical overview; Stackup, 2025, provider comparison section.]

2. **2018–2020 – Cloud as default backend**:  
   Crypto exchanges and infra providers standardize on AWS/GCP for scalability and reliability, compounding vendor concentration risk that is later exposed in outages.
   [Source: CoinDesk, 2025 AWS outage op-ed; TechTarget, 2025.]

3. **2023 – Silence Labs + Waku integration**:  
   Silence Laboratories integrates Waku-based decentralized communication into MPC-TSS SDKs to remove centralized coordination servers and their "single point of control or DOS vector".
   [Source: Silence Labs–Waku partnership blog summary, 2023, quoted in problem; Waku.org.]

4. **2024 – Emergence of decentralized MPC infra projects**:  
   Lit Protocol, dWallet, ARPA Network, ICP threshold ECDSA, Passport Protocol and others present designs where coordination is distributed across permissionless validator networks rather than a single vendor.
   [Source: Decentralized MPC Blog, 2024, survey of projects; ICP & ARPA documentation as referenced in problem.]

5. **2024–2025 – High-profile cloud outages and crypto downtime**:  
   Multiple AWS and Azure outages (e.g., October 20–21, 2025 US-EAST-1 DNS/DynamoDB failure) highlight that supposedly decentralized crypto platforms still fail with centralized infrastructure.
   [Source: CoinCentral, 2025 AWS outage report; TechTarget, 2025; CoinDesk, 2025.]

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Strong industry bias toward using hyperscale clouds and proprietary SaaS for speed and efficiency, with limited investment in decentralized infra.
  - Marketing narratives around "no single point of failure" for MPC overshadow infrastructure realities.
    [Source: Cubist, 2024, discussion of marketing claims; Stackup, 2025, "Common MPC Wallet Myths Debunked".]

- **Direct causes**:
  - Centralized coordination server architectures with no meaningful fallback paths (no decentralized relays, no offline flows).
  - Single-region or single-cloud deployments of coordination servers, sometimes even relying on a single DNS zone or database service (e.g., DynamoDB) as critical dependency.
  - Lack of published and tested business continuity plans for coordination vendor failure scenarios.
  [Source: Problem statement – Background & constraints; TechTarget, 2025; CoinCentral, 2025.]

### 4.3 Root issues

- **Infrastructural monoculture**: A small set of cloud providers, regions, and messaging platforms underpin much of crypto and MPC infrastructure, creating correlated risk.
- **Misaligned incentives**: Short-term UX and cost optimization, plus pressure to ship, outweigh investments in redundant or decentralized infra that are invisible when things work.
- **Governance gaps**: Many providers lack board-level oversight and explicit KPIs for resilience, leading to underinvestment in multi-cloud, decentralized relays, and offline capabilities.
- **Mythologizing cryptography**: Overreliance on cryptographic decentralization as a narrative distracts from centralized operational practices.

[Source: Cubist, 2024; TechTarget, 2025; CoinDesk, 2025; Problem statement – Historical attempts and root causes.]

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- As more assets and users move to MPC wallets, the blast radius of each coordination outage grows (tens of millions of users, tens of billions of dollars potentially affected per incident).
  [Estimate based on: problem statement estimates of 100M+ users and $50B+ assets; Stackup, 2025, provider adoption overview, Medium confidence.]
- Cloud provider outages are unlikely to disappear; historical patterns across AWS, Azure, and GCP show recurring large-scale incidents due to DNS, control-plane, and configuration bugs.
  [Source: TechTarget, 2025, historical examples; CoinDesk, 2025; status pages of major providers referenced there.]
- If MPC wallets remain centrally coordinated, each outage will trigger social backlash about "fake decentralization" and erode trust in MPC architectures.
  [Source: CoinCentral, 2025 community reactions; Cubist, 2024 critique of MPC marketing.]

### 5.2 Early signals

- The Silence Labs–Waku integration and decentralized MPC projects indicate growing recognition of coordination centralization as a critical weakness.
  [Source: Silence Labs–Waku blog summary, 2023; Decentralized MPC Blog, 2024.]
- October 2025 AWS outage articles across technical and mainstream media explicitly describe crypto’s centralized infrastructure dependence and vendor concentration as systemic issues.
  [Source: CoinCentral, 2025; TechTarget, 2025; CoinDesk, 2025.]
- Regulators now classify major cloud providers as critical third parties and demand mapping of dependencies and continuity plans.
  [Source: TechTarget, 2025 regulatory commentary.]

### 5.3 Scenarios (6–24 months)

- **Optimistic**:  
  Major MPC wallet providers integrate decentralized relays (e.g., Waku/libp2p) as primary or secondary coordination layers, adopt multi-region/multi-cloud, and implement offline signing for institutional flows. Cloud outages become localized incidents; wallets maintain ≥99.99% availability independent of any single vendor.
  [Estimate based on: known technical feasibility of Waku/libp2p and multi-cloud architectures, Medium confidence.]

- **Baseline**:  
  A subset of leading providers diversify infrastructure and publish transparent architecture, while many smaller wallets remain single-vendor. Outages still impact significant portions of the ecosystem but less catastrophically than 2025 events.

- **Pessimistic**:  
  No substantial architectural change occurs; a future cloud outage or targeted DDoS/censorship incident brings down multiple major MPC wallets simultaneously during market stress, triggering regulatory backlash, lawsuits, and migration toward alternative architectures (smart contract wallets, HSM-backed custodians, or decentralized MPC networks).
  [Estimate based on: historical patterns of infrastructure incidents and regulatory reaction, Low–Medium confidence.]

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Engineering and ops talent**: Major MPC wallet providers already operate complex distributed systems and can implement multi-region/multi-cloud and peer-to-peer networking when prioritized.
  [Source: Stackup, 2025, provider case studies; problem statement – team composition.]
- **Existing decentralized networking stacks**: Waku, libp2p, Nostr and IPFS provide robust building blocks for censorship-resistant coordination, reducing the need to build everything from scratch.
  [Source: Waku.org; libp2p.io; Nostr.com; IPFS.tech.]
- **Precedents and SDKs**: Silence Labs–Waku integration and decentralized MPC projects show working reference architectures for decentralized coordination.
  [Source: Silence Labs–Waku blog; Decentralized MPC Blog, 2024.]

### 6.2 Capability gaps

- **Peer-to-peer networking expertise**: Many wallet teams are more experienced with REST/WebSockets on centralized infra than with gossip networks, NAT traversal, and pub/sub routing.
- **Resilience engineering and chaos testing**: Few providers systematically run game-day simulations or dependency mapping exercises focused on coordination-layer failures.
  [Source: TechTarget, 2025, "Lessons and leadership imperatives"; industry SRE best practices.]
- **Regulatory communication for decentralized infra**: Providers lack standardized ways to explain decentralized coordination and shared responsibility to regulators.

### 6.3 Buildable capabilities (1–6 months)

- Pilot integration of Waku or similar as a backup relay path alongside existing centralized servers, starting with low-risk flows.
- Implement multi-region rollout for existing coordination servers (e.g., AWS us-east-1 + eu-west-1 + another vendor) with active–active or active–passive failover.
- Establish SRE-led resilience program including dependency mapping, outage playbooks, and periodic failure drills targeting coordination components.
  [Estimate based on: typical timelines for network feature pilots and SRE practices in similar SaaS systems, Medium confidence.]

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: MPC wallets distribute keys but rely on centralized coordination; cloud outages expose fragility.
- **Problem**: Coordination centralization creates a de facto single point of failure and censorship vector.
- **Analysis**: Internal trade-offs (latency vs. resilience), external stakeholders, root causes, and trends.
- **Options**: (A) Multi-region/multi-cloud centralized coordination; (B) decentralized relay integration; (C) offline/mesh coordination; (D) hybrid strategy.
- **Risks**: Complexity, costs, residual centralization, regulatory friction, UX regressions.

### 7.2 Key judgments (for validation)

1. Coordination centralization is currently the *dominant* availability and censorship risk for MPC wallets, more so than protocol-level cryptographic weaknesses.
2. A combination of multi-cloud + decentralized relays + offline signing can materially reduce systemic risk without making UX unacceptable for most use cases.
3. Regulatory and governance alignment (board-level resilience KPIs, transparent reporting) is necessary to sustain these architectural changes.

[Source: Synthesized from TechTarget, 2025; CoinCentral, 2025; CoinDesk, 2025; Stackup, 2025; Decentralized MPC Blog, 2024.]

### 7.3 Alternative high-level paths

- **Path A – Harden centralized coordination (multi-region/multi-cloud)**: Improve resilience by treating coordination servers like Tier-0 infra and deploying them across multiple regions and vendors with tested failover.
- **Path B – Introduce decentralized relay layer**: Use Waku/libp2p or similar as primary or backup relay for MPC messages, reducing trust in any single vendor.
- **Path C – Offline/mesh coordination for critical flows**: Build Bluetooth/QR/local-network protocols for high-value institutional operations that must continue despite internet or cloud outages.
- **Path D – Hybridization with decentralized MPC networks and smart contract wallets**: Shift some use cases to architectures that do not rely on vendor-specific coordination at all.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Tech-centric bias**: Focus on engineering solutions (decentralized relays, multi-cloud) might underweight organizational and governance reforms.
- **Optimism about decentralized infra maturity**: Waku and similar protocols may face unforeseen scaling or security issues in large production deployments.
- **Underestimation of regulatory friction**: Some jurisdictions may actively discourage strong censorship resistance.
  [Source: TechTarget, 2025; Stackup, 2025, "Regulatory Landscape"; Waku project docs.]

### 8.2 Required intelligence

- Detailed dependency maps for each major MPC wallet provider: cloud regions, DNS providers, message queues, and any existing P2P components.
- Empirical latency and reliability benchmarks comparing centralized vs. decentralized coordination in realistic network conditions.
- Data on actual or near-miss censorship attempts at the coordination layer (e.g., government requests, internal decisions to block regions).
  [Source: TechTarget, 2025 (dependency mapping guidance); Stackup, 2025 (performance benchmarks suggestion).]

### 8.3 Validation plan

- **Resilience drills**: Simulate loss of a major cloud region and/or internal coordination service; measure signing success rate, failover time, and user impact.
- **Field trials**: Run parallel coordination via Waku or similar for a subset of traffic, capturing latency, error rates, and operational complexity.
- **Regulatory engagement**: Pilot disclosures of decentralized coordination architectures to selected regulators and key institutional clients; adjust designs based on feedback.

[Source: TechTarget, 2025, "Lessons and leadership imperatives"; industry SRE best practices.]

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Relative weighting between multi-cloud and decentralized relays may change as empirical latency and reliability data arrive.
- The role of decentralized MPC networks vs. smart contract wallets may shift as these ecosystems mature.
- Regulatory stances on decentralized coordination could tighten or loosen, affecting feasibility of strong censorship resistance.

### 9.2 Incremental approach

- Start with **hardened centralized infra** (multi-region, robust failover, clear dependency maps).
- Add **backup decentralized relay paths** for selected flows; then progressively expand coverage as confidence grows.
- For highest-value or highest-risk assets, implement **offline/mesh** coordination pilots.

### 9.3 "Good enough" criteria

- Measured signing availability ≥99.99% across representative 12-month window, including at least one simulated or real cloud outage.
- Documented ability to sign transactions using at least two independent coordination paths (e.g., primary cloud + decentralized relay or offline).
- Public architecture and SLA documentation meeting transparency goals; independent reviews confirm absence of single coordination chokepoints.
  [Estimate based on: best practices in high-availability financial infra and problem statement targets, Medium confidence.]

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Current MPC wallet deployments often relocate the single point of failure from *keys* to *coordination infrastructure*, undermining the decentralization narrative and creating systemic outage and censorship risk.
   [Source: Cubist, 2024; Stackup, 2025; CoinCentral, 2025; TechTarget, 2025.]
2. Cloud outages and growing regulatory attention to vendor concentration demonstrate that relying on a single coordination vendor or cloud region is no longer acceptable for critical financial infra.
   [Source: TechTarget, 2025; CoinDesk, 2025; CoinCentral, 2025.]
3. A pragmatic combination of multi-region/multi-cloud centralized coordination, decentralized relay integration, and offline/mesh capabilities can materially improve resilience within 24 months, at the cost of higher complexity and modest latency increases.
   [Source: Silence Labs–Waku blog summary; Decentralized MPC Blog, 2024; Stackup, 2025; TechTarget, 2025.]

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Map all coordination dependencies (cloud regions, queues, DNS, SaaS) for MPC signing flows → SRE Lead → Coverage: 0% → 100% of production flows mapped → 2026-02-15.
  2. Design and approve target multi-region/multi-cloud architecture for coordination services → Infra Architect → Single-region deployments: >80% → <20% of traffic single-region only → 2026-03-31.

- **【P1 – Important】**
  3. Launch Waku/libp2p-based relay pilot for a low-risk subset of transactions (e.g., internal testnet, small user cohort) → Protocol Engineering Lead → Pilot coverage: 0% → ≥5% of signing flows → 2026-04-30.
  4. Define offline/mesh signing requirements for institutional use cases (Bluetooth/QR/local network) and create initial design → Product + Protocol Teams → Requirements doc: draft → approved → 2026-04-30.

- **【P2 – Optional】**
  5. Evaluate integration with at least one decentralized MPC network or smart contract wallet provider for non-time-critical assets → Strategy Lead → Diversified asset share: baseline → +5% on alternative architectures → 2026-06-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Complexity of multi-cloud and decentralized infra causes misconfigurations and new failure modes | High | Medium | Unexpected outages or security incidents during rollout | Staged rollouts, strong observability, independent security reviews, and chaos testing | Infra & Security Leads |
| Latency increase from decentralized relays degrades UX and adoption | Medium | Medium | p95 signing latency exceeds acceptable thresholds in pilot metrics | Optimize routing, use hybrid approach (centralized primary, decentralized backup), segment high-frequency users to more centralized flows | Product & Protocol Leads |
| Regulatory concerns over reduced central control slow or block deployment | Medium–High | Medium | Negative feedback from regulators or large institutional clients | Early engagement, transparent risk analysis, optionality (allow regulated clients to opt for more centralized coordination paths) | Compliance & Legal |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Multi-region/multi-cloud centralized coordination** | Significant improvement in availability against regional/cloud outages; easier to reason about; reuses existing stack | Infra + ops cost ↑; still centralized chokepoints; limited censorship resistance | Misconfiguration, residual dependence on a few hyperscalers | Short–medium term, when team has strong cloud expertise and strict SLAs | When primary risk is state-level censorship or vendor exit, not just outages |
| **B: Decentralized relay layer (Waku/libp2p, Nostr)** | Removes single central relay; improves censorship resistance; aligns with crypto decentralization ethos | Higher latency; more complex debugging; requires new expertise | Immature tooling; potential security/DoS vectors in P2P network | For censorship-prone jurisdictions; for providers positioning on decentralization | For ultra-low-latency trading where every second counts and outages are already mitigated by other means |
| **C: Offline/mesh coordination for critical flows** | Enables signing during severe outages or cuts; strong business continuity for institutions | UX complexity; limited throughput; requires physical or local connectivity | Operational friction; operational security of local channels | For high-value institutional treasury operations and disaster-recovery scenarios | For everyday retail transactions where always-on connectivity is expected |
| **D: Migration to decentralized MPC networks / smart contract wallets** | Eliminates dependence on vendor-specific coordination; more transparent, programmable control | Integration effort; new trust and security models; possible chain/feature limitations | Smart contract bugs; economic security assumptions; governance risks | For new products where architecture can be designed around these paradigms | For legacy products with deep integration into current MPC stack and limited migration budget |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **MPC wallet** | Wallet where private key material is split into multiple shares held by different parties/devices; signatures are produced via secure multi-party computation without reconstructing the key in one place | N/A | [Source: Stackup, 2025, "What Is an MPC Wallet?"] |
| **Coordination server** | Vendor-operated infrastructure (APIs, message queues, WebSockets, push services) that relays MPC protocol messages between parties and orchestrates signing ceremonies | N/A | Defined for this analysis; consistent with Silence Labs and problem statement |
| **Decentralized relay network** | Peer-to-peer communication fabric (e.g., Waku/libp2p, Nostr) used to route messages between participants without reliance on a single trusted relay operator | N/A | [Source: Waku.org; Nostr.com; Silence Labs–Waku blog summary, 2023] |
| **Vendor concentration risk** | Systemic risk arising when multiple services depend on a small number of third-party providers (e.g., cloud regions), so a single outage affects many downstream systems | N/A | [Source: TechTarget, 2025, "AWS cloud outage reveals vendor concentration risk"] |
| **AWS US-EAST-1 outage (Oct 2025)** | Major AWS incident caused by DNS resolution failure for DynamoDB endpoints in US-EAST-1, leading to errors across multiple services and affecting crypto platforms and other SaaS | N/A | [Source: TechTarget, 2025; CoinCentral, 2025] |
| **Censorship resistance** | Property that no single party can unilaterally block valid transactions from being created or propagated; for coordination, means no vendor or government can prevent honest parties from completing a signing ceremony | N/A | Defined for this analysis; aligned with standard crypto terminology |
| **Waku** | Censorship-resistant messaging protocol built on libp2p and used by some Web3 projects for decentralized communication | N/A | [Source: Waku.org; Silence Labs–Waku blog summary, 2023] |
| **libp2p** | Modular peer-to-peer networking stack used for building decentralized networks like IPFS and Waku | N/A | [Source: libp2p.io] |
| **Offline signing** | MPC signing flow that does not depend on internet-based vendor coordination servers, using local channels such as Bluetooth, QR codes, or LAN for message exchange | N/A | [Source: Problem statement – offline signing capabilities] |
| **Critical third party (CTP)** | External provider whose failure can have systemic impact, recognized by regulators and subject to resilience requirements | N/A | [Source: TechTarget, 2025, referencing FCA/EBA guidance] |

---

## 12. References

### Tier 1 – Primary / Technical Documentation

1. **Stackup.** (2025). *MPC Wallets: A Complete Technical Guide (2025).* Stackup. https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide  
   **[Cited in:** Context Recap; Sections 1–3, 4, 5, 6, 7, 10, 11 **]**

2. **Status pages and postmortems of major cloud providers** (AWS, Azure). (2024–2025). *Incident reports for regional outages and control-plane issues.*  
   **[Cited in:** Sections 4, 5 **]**

### Tier 2 – Industry Reports, Blogs, and Analyses

3. **CoinCentral – Trader Edge.** (2025). *Your "Decentralized" Crypto Platform Just Crashed Because of Amazon AWS Outage.* CoinCentral. https://coincentral.com/your-decentralized-crypto-platform-just-crashed-because-of-amazon-aws-outage  
   **[Cited in:** Context Recap; Sections 1–3, 4, 5, 10 **]**

4. **TechTarget – Sean Michael Kerner.** (2025). *AWS cloud outage reveals vendor concentration risk.* TechTarget SearchCIO. https://www.techtarget.com/searchcio/feature/AWS-cloud-outage-reveals-vendor-concentration-risk  
   **[Cited in:** Context Recap; Sections 1–3, 4, 5, 6–8, 10, 11 **]**

5. **CoinDesk – Max Li & Cheyenne Ligon.** (2025). *The AWS Outage Shows Why Crypto Can't Keep Relying On Centralized Infrastructure.* CoinDesk. https://www.coindesk.com/opinion/2025/11/01/the-aws-outage-shows-why-crypto-can-t-keep-relying-on-centralized-infrastructure  
   **[Cited in:** Sections 1–3, 4, 5, 10 **]**

6. **Cubist.** (2024). *MPC does have a single point of failure.* Cubist Blog. https://cubist.dev/blog/mpc-does-have-a-single-point-of-failure  
   **[Cited in:** Context Recap; Sections 1–2, 4, 5, 10 **]**

7. **Silence Laboratories.** (2023). *Silence Laboratories Partners with Waku to add Decentralised Communication to MPC-TSS SDKs.* Medium.  
   (Describes centralized coordination as "single point of control or DOS vector" and presents Waku-based decentralized relay integration.)  
   **[Cited in:** Context Recap; Sections 1–3, 4, 5, 6, 10, 11 **]**

8. **Decentralized MPC – Johnny Nan Jiang.** (2024). *Decentralized MPC — The Future Infrastructure for Crypto Wallets.* Medium.  
   (Surveys decentralized MPC infrastructures such as Lit, dWallet, ARPA, ICP, Passport Protocol, Nillion, ContinuumDAO.)  
   **[Cited in:** Context Recap; Sections 3–5, 6–7, 10 **]**

### Tier 2 – Project Documentation

9. **Vac / Waku.** (2023–2025). *Waku Documentation and Specs.* https://waku.org  
   **[Cited in:** Sections 2–3, 5–7, 11 **]**

10. **Protocol Labs – libp2p.** (2023–2025). *libp2p: A Modular Network Stack.* https://libp2p.io  
    **[Cited in:** Sections 2–3, 6, 11 **]**

11. **Nostr community.** (2022–2025). *Nostr protocol and relay design.* https://nostr.com  
    **[Cited in:** Sections 2–3, 5, 11 **]**

12. **IPFS project.** (2023–2025). *IPFS Documentation.* https://ipfs.tech  
    **[Cited in:** Sections 2–3, 6, 11 **]**

### Internal / Problem-Specific Sources and Estimates

13. **Problem Statement – Centralized Coordination Infrastructure Creating Single Point of Failure in MPC Wallets.** (2025). Internal documentation summarizing problem context, goals, constraints, impact, and stakeholders.  
    **[Cited in:** Context Recap; Sections 1–5, 6–7, 9–10 **]**

14. **Internal architecture diagrams and incident reports of major MPC wallet providers.** (2023–2025). *Service dependency maps, cloud-region usage, and prior coordination incidents.*  
    **[Cited in:** Sections 2–4, 6–8, 10 **]**

15. **Estimates and assumptions.** Various.  
    Method: extrapolation from public user and AUM figures; known provider counts; benchmark costs for infra and engineering. Confidence: Medium. Validation: refine with provider-specific telemetry and financials.  
    **[Used in:** Context Recap; Sections 1, 5–7, 9–10 **]**
