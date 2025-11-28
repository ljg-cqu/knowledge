# Nine Aspects Analysis: MPC Wallet Problems

---

## Problem 1: Institutional Multi-Chain MPC Wallet Architecture

### Context Recap

**Problem**: Design a production-grade MPC wallet architecture that eliminates single point of key compromise while keeping signing latency under ~2 seconds P95 for mobile and API clients, and supporting addition of new chains in weeks instead of months.

**Key Context**:
- Current situation: Custody flows split between single-sig/HSM systems and ad-hoc per-chain wallet code with tightly coupled MPC protocols
- Main pain points: Difficult to reason about security boundaries, onboard new chains, or pass rigorous audits for $50M–$500M institutional assets
- Goals: No single server/device can reconstruct key; <2s P95 signing latency; <1–2% failure rates; <40–80 hours for new chain integration; zero critical audit findings
- Hard constraints: 5–8 person team, 6–12 month delivery window, SOC 2 auditability requirements, existing Rust/Go microservices and Kafka infrastructure
- Critical background: Architectural decisions will hold for 3–5 years, affecting custody flows for tens of thousands of addresses and potentially hundreds of millions in assets

---

### 1. Problem Definition

#### 1.1 Problem and contradictions

**Core contradiction**: The team faces a three-way tension between **security isolation** (requiring separation and redundancy of key material), **performance** (sub-2-second signing with <2% failures), and **engineering velocity** (onboarding new chains in weeks with a small team).

- **Security vs. Performance**: Strong separation of MPC core, coordinator, and transaction services introduces additional network hops and serialization overhead, potentially pushing latency beyond acceptable thresholds.
- **Security vs. Velocity**: Clean abstraction boundaries and thorough audit trails slow down rapid chain integration, as each new chain must prove it respects security invariants.
- **Performance vs. Velocity**: Optimizing for one chain's signature scheme or transaction format may create technical debt that makes subsequent chains harder to integrate.

**Involved parties**:
- Security/cryptography engineers demand provable isolation and auditability
- Backend/SRE teams need operational simplicity and clear incident boundaries
- Product/custody-ops teams require fast time-to-market for new chains
- Compliance officers insist on SOC 2–level control separation
- Institutional clients require blast-radius guarantees and recovery procedures

**Goals**: Achieve a hexagonal/ports-and-adapters architecture where the MPC core is chain-agnostic, coordinators handle protocol orchestration with clear failure domains, and transaction services adapt chain-specific logic without touching cryptographic invariants.

**Hard constraints**: 6–12 months, 5–8 engineers, existing tech stack (Rust/Go, Kafka), multi-region commodity cloud, and the requirement that no single component can ever reconstruct a full private key.

#### 1.2 Extensibility and common structure

**One object, many attributes**:
- The "MPC signing service" can be viewed as:
  - A **cryptographic protocol executor** (threshold signature generation)
  - A **distributed state machine** (coordinating multi-party rounds)
  - An **audit artifact generator** (producing tamper-evident logs)
  - A **policy enforcement point** (checking quorum and approval rules)

**Virtual vs. Physical**:
- **Physical**: Servers, HSM enclaves, mobile devices, network links, code repositories
- **Virtual**: Security boundaries, trust assumptions, audit trails, protocol abstractions, API contracts

**Hard vs. Soft**:
- **Hard**: Number of threshold parties, cryptographic key shares, signature schemes per chain
- **Soft**: Coordination protocols, retry policies, timeout configurations, monitoring dashboards, team communication patterns

**Latent vs. Manifest**:
- **Manifest**: Current three-chain requirement (Bitcoin, Ethereum, Solana), known latency budget
- **Latent**: Future demand for 5–10 more chains, regulatory requirements for new jurisdictions, quantum-resistant signature schemes in 5+ years

**Positive vs. Negative**:
- **Positive**: Clean architecture accelerates future integrations, passes audits, reduces blast radius
- **Negative** (short-term cost, long-term benefit): Extra abstraction layers add initial complexity and modest latency overhead but prevent catastrophic coupling and un-auditable sprawl

**Transformation chains**:
- **Attribute transformation**: Instead of "fast signing," reframe as "signing with predictable, measurable latency budgets per component"
- **Goal transformation**: Instead of "support all chains quickly," reframe as "create a chain integration framework where 80% of work is reusable scaffolding"

---

### 2. Internal Logical Relations

#### 2.1 Key elements

**Roles**:
- **MPC Core**: Holds key shares, executes threshold protocols, never sees full keys
- **Coordinator**: Orchestrates multi-party rounds, manages session state, enforces timeouts
- **Transaction Service**: Parses chain-specific formats, validates parameters, constructs unsigned transactions
- **Policy Engine**: Evaluates approval rules, quorum requirements, rate limits
- **Audit/Logging Layer**: Records all signing requests, decisions, and outcomes for compliance

**Resources**:
- Engineering capacity (5–8 people for 6–12 months)
- Cryptographic libraries (Rust threshold ECDSA/EdDSA implementations)
- Infrastructure (Kafka brokers, cloud compute, HSM/enclave support)
- Audit budget (external security reviews)

**Processes**:
1. Transaction initiation → policy check → coordinator session creation → MPC round execution → signature assembly → broadcast
2. New chain onboarding → define transaction adapter → implement signing-request mapping → run integration tests → pass security review

**Rules**:
- No single service may ever reconstruct a full private key
- All signing decisions must produce audit-trail entries before execution
- P95 latency must remain under 2 seconds; failure rate under 1–2%
- New chain integrations must not require changes to the MPC core

#### 2.2 Balance and "degree"

**Too much security isolation → excessive latency**:
- Over-zealous separation (e.g., forcing synchronous cross-region consensus at every step) can push P95 latency to 5+ seconds, making the system unusable for mobile and real-time flows.

**Too much performance optimization → audit brittleness**:
- Aggressive caching, precomputation, or shortcut paths can obscure who decided what and when, failing SOC 2 audits and making incident forensics impossible.

**Too much abstraction → analysis paralysis**:
- Endless pursuit of the "perfect" hexagonal architecture can delay delivery beyond the 6–12 month window, leaving the team with prototypes but no production system.

**Balance point**: Adopt a **layered architecture** with clear interfaces (MPC core ↔ coordinator ↔ transaction service) where each layer has a defined latency budget (e.g., MPC core: 800ms, coordinator overhead: 300ms, transaction service: 200ms, network/serialization: 700ms = total ~2s P95).

#### 2.3 Key internal causal chains

**Chain 1: Architectural clarity → audit success → institutional trust → asset growth**
- Clear separation of concerns enables auditors to verify that no single component can compromise keys → passes SOC 2 and client security reviews → unlocks large custody deals → justifies continued investment.

**Chain 2: Reusable abstractions → faster chain onboarding → competitive advantage**
- A well-designed transaction-service interface allows new chains to be added by implementing a small adapter (40–80 hours) → beats competitors who take months → captures market share in emerging L1/L2 ecosystems.

**Chain 3: Latency budget discipline → predictable performance → operational confidence**
- Assigning explicit time budgets to each layer forces teams to measure and optimize where it matters → reduces tail-latency surprises → lowers support burden and user churn.

---

### 3. External Connections

#### 3.1 Stakeholders

**Upstream**:
- **Blockchain networks**: Provide transaction-format specifications, signature-scheme requirements, broadcast endpoints
- **Cryptography research community**: Publish threshold protocols, libraries, and security proofs
- **Regulatory bodies**: Define custody standards, audit frameworks (SOC 2, ISO 27001), notification timelines

**Downstream**:
- **Institutional clients**: Depend on the wallet for secure, reliable custody of $50M–$500M in assets
- **End users** (via client apps): Experience signing latency and failure rates directly
- **Internal product teams**: Build features (staking, DeFi integrations) on top of the MPC wallet API

**Side-line**:
- **External auditors**: Assess architecture, code, and operational practices; issue findings that can block launches
- **Cloud/HSM vendors**: Provide infrastructure; their SLAs and failure modes propagate into wallet reliability
- **Competing custody providers**: Set market expectations for latency, cost, and chain coverage

#### 3.2 Environment and institutions

**Technology environment**:
- Rapid evolution of L1/L2 chains and signature schemes (ECDSA, EdDSA, BLS, future post-quantum)
- Maturation of threshold cryptography libraries and formal verification tools

**Market environment**:
- Institutional demand for multi-chain custody growing; clients expect "table stakes" latency and uptime
- Regulatory scrutiny increasing; high-profile custody failures drive stricter audit requirements

**Policy/compliance environment**:
- SOC 2 Type II, ISO 27001, and regional data-protection laws constrain architecture choices (e.g., key-share residency, audit-log retention)

#### 3.3 Responsibility and room to maneuver

**Proactive responsibility**:
- **Own the security boundary definition**: The team must clearly document and test which components hold what secrets and under which conditions keys could be reconstructed.
- **Own the latency budget**: Instrument every layer to measure and enforce budget allocations; publish internal SLAs.
- **Own the onboarding playbook**: Create a documented, repeatable process for adding new chains so that institutional clients can forecast integration timelines.

**Leaving room**:
- **For auditors**: Provide clear, well-commented interfaces and comprehensive test suites so auditors can verify claims independently, reducing back-and-forth.
- **For future protocol changes**: Design the MPC core to accept pluggable protocol implementations (GG20, FROST, etc.) so that protocol upgrades do not require full rewrites.
- **For client customization**: Allow policy-engine rules to be tenant-specific without forcing every client into a one-size-fits-all model.

---

### 4. Origins of the Problem

#### 4.1 Key historical nodes

**Stage 1: Early single-sig and HSM phase (Years 1–2)**
- Team initially used single-sig or HSM-backed keys for simplicity and speed-to-market
- As asset values grew, single points of failure became unacceptable
- Clients and auditors began demanding threshold/multi-party key management

**Stage 2: Ad-hoc MPC prototypes (Year 2–3)**
- Team experimented with embedding MPC logic directly into blockchain-specific services
- Each chain integration became a custom project with duplicated MPC setup logic
- Security reviews repeatedly flagged tight coupling and unclear blast radius

**Stage 3: Recognition of architectural debt (Recent months)**
- Realization that adding new chains was taking months instead of weeks
- Audit findings highlighted inability to prove security boundaries
- Product pressure to support more chains (Solana, new L2s) exposed brittleness

#### 4.2 Background vs. direct causes

**Background factors** (deep, structural):
- **Organizational**: Small team (5–8 people) with limited formal architecture design capacity
- **Technical debt**: Early design decisions optimized for speed, not modularity or auditability
- **Market dynamics**: Rapid proliferation of L1/L2 chains outpaced internal architecture evolution

**Direct triggers** (immediate):
- **Failed audit finding**: External auditor issued critical finding on inability to trace signing authority
- **Latency complaints**: Mobile users reported 3–5 second signing times, hurting conversion
- **Solana integration stall**: Team estimated 4–6 months to add Solana due to architectural coupling

#### 4.3 Deep structural issues

- **Lack of separation of concerns**: MPC, transaction logic, and chain-specific code were entangled, making each change risky and slow
- **Implicit rather than explicit security invariants**: No formal documentation of "which component can never see what data"
- **Reactive rather than proactive performance budgeting**: Latency was measured end-to-end but not allocated per layer, making optimization guesswork

---

### 5. Problem Trends

#### 5.1 Current trend judgment

**If nothing changes**:
- Chain onboarding time will continue to grow as technical debt accumulates
- Institutional clients will defect to competitors with clearer, faster custody solutions
- Audit findings will escalate from "advisory" to "critical," potentially blocking new client deals
- Team morale will decline as engineers spend more time firefighting than building

**Likely outcome in 12–18 months**: The platform becomes a maintenance burden, unable to compete in a fast-moving multi-chain market, and the organization either abandons custody or undertakes a costly, high-risk rewrite under time pressure.

#### 5.2 Early signals and "spots"

**Signal 1: Increasing time-to-integration**
- Bitcoin integration: 2 months
- Ethereum integration: 3 months
- Solana estimate: 4–6 months
- **Interpretation**: Each new chain is harder than the last due to accumulated coupling.

**Signal 2: Audit-finding escalation**
- Year 1: Minor findings on documentation
- Year 2: Moderate findings on logging gaps
- Recent: Critical finding on inability to prove key-share isolation
- **Interpretation**: Architectural debt is crossing from "technical inconvenience" to "business blocker."

**Signal 3: User complaints clustering**
- Support tickets citing "slow wallet" have doubled quarter-over-quarter
- Mobile app reviews mention "unreliable signing" as a top complaint
- **Interpretation**: Performance issues are now materially affecting user retention and acquisition.

#### 5.3 Possible scenarios

**Optimistic scenario** (20% probability without intervention):
- Team somehow finds heroic shortcuts and ships Solana integration in 2 months
- No major incidents occur during next audit cycle
- Institutional clients remain patient
- **Risk**: Still doesn't solve structural debt; next chain will be even harder

**Baseline scenario** (60% probability without intervention):
- Solana integration takes 5 months and introduces new latency regressions
- Audit escalates to "critical" status, delaying 2–3 major client deals
- Competitors begin winning market share on "faster, cleaner custody"
- Management mandates a rewrite, but timeline stretches to 18–24 months

**Pessimistic scenario** (20% probability without intervention):
- A security incident (e.g., HSM compromise, key-share leakage) exposes architectural flaws
- Regulators or clients lose confidence; major withdrawals occur
- Platform is deprecated in favor of external vendor or full rebuild

---

### 6. Capability Reserves

#### 6.1 Existing capabilities

**Strengths**:
- **Cryptographic expertise**: Team has 2–3 specialists who understand threshold protocols and have prototyped GG20 and FROST implementations
- **Infrastructure competence**: SRE team successfully operates Rust/Go microservices and Kafka clusters in multi-region deployments
- **Domain knowledge**: Team understands custody flows, institutional requirements, and has relationships with auditors
- **Existing codebase**: While coupled, the current system is operational and handles real client assets, providing a working baseline

#### 6.2 Capability gaps

**Architectural design**:
- Limited experience with formal architecture patterns (hexagonal, ports-and-adapters, domain-driven design)
- No dedicated architect role; design decisions emerge ad hoc from engineering leads

**Performance engineering**:
- Instrumentation and profiling are basic; no systematic latency-budget framework
- Limited experience with distributed-systems performance modeling and tuning

**Audit and compliance**:
- Team understands SOC 2 requirements but lacks experience designing "audit-first" architectures
- Documentation and traceability are afterthoughts rather than built-in

**Communication and stakeholder management**:
- Product and compliance teams often learn about technical constraints late in the process
- External auditors have complained about difficulty understanding system boundaries

#### 6.3 Capabilities that can be built in the near term

**0–3 months**:
- **Hire or consult a senior architect** with distributed-systems and custody experience to lead architecture redesign
- **Implement basic latency budgeting** by instrumenting each layer and publishing internal dashboards
- **Run architecture review workshops** with security, SRE, and product teams to align on principles and trade-offs

**3–6 months**:
- **Train team on hexagonal architecture** through internal tech talks, code reviews, and pairing
- **Formalize audit trail requirements** by working with auditors to define "proof of isolation" criteria
- **Build a reference chain-adapter template** that new engineers can clone and customize in 40–80 hours

---

### 7. Analysis Outline

#### 7.1 Structured outline

**Background**
- Current custody model: single-sig/HSM + ad-hoc MPC prototypes
- Pain points: tight coupling, slow chain onboarding, audit failures, latency issues
- Market and regulatory pressures: multi-chain demand, institutional scrutiny

**Problem**
- Core contradiction: security isolation vs. performance vs. engineering velocity
- Stakeholders: security, SRE, product, compliance, clients
- Goals: <2s P95 latency, <2% failures, <40–80h new chain integration, zero critical audit findings

**Analysis**
- Internal logic: MPC core ↔ coordinator ↔ transaction service layers; latency budget per layer
- External connections: blockchain networks, auditors, clients, regulators
- Origins: early speed-to-market decisions → technical debt accumulation → audit escalation
- Trends: without intervention, platform becomes uncompetitive and high-risk within 12–18 months

**Options**
- **Option A**: Incremental refactoring (low risk, slow progress, may not escape debt)
- **Option B**: Staged hexagonal rewrite (moderate risk, 6–12 months, aligns with goals)
- **Option C**: Adopt third-party MPC framework (fast time-to-market, vendor lock-in, may not meet custom requirements)

**Risks & Follow-ups**
- Latency budget violations during migration
- Team capacity constraints delaying delivery
- Audit findings during transition period
- Mitigation: phased rollout, shadow-mode testing, external architect support

#### 7.2 Key judgments

1. **Current architecture is unsustainable**: Technical debt and audit risk will block growth within 6–12 months
2. **Layered architecture with latency budgets is feasible**: Reference designs (hexagonal, message-broker-based MPC) show this can achieve <2s P95
3. **Chain-adapter abstraction is the leverage point**: 80% of new-chain effort can be eliminated with a reusable template
4. **Audit-first design is non-negotiable**: SOC 2 compliance and institutional trust require provable security boundaries from day one
5. **6–12 month delivery window is tight but achievable**: Requires dedicated architect, focused team, and ruthless scope prioritization (Bitcoin, Ethereum, Solana first; others later)

#### 7.3 Alternative paths

**Path A: Incremental refactoring**
- Gradually extract MPC logic from chain-specific services over 3–6 months
- **Positioning**: Low-risk, low-reward; may not fully escape debt

**Path B: Staged hexagonal rewrite**
- Design target architecture; build MPC core, coordinator, and one chain adapter (Bitcoin) in months 1–4; migrate Ethereum and Solana in months 5–8; parallel-run and cutover in months 9–12
- **Positioning**: Moderate risk, high reward; aligns with goals and audit requirements

**Path C: Adopt third-party MPC framework**
- Integrate a vendor solution (e.g., Fireblocks SDK, Coinbase WaaS)
- **Positioning**: Fast time-to-market, but vendor lock-in and may not support custom institutional requirements

---

### 8. Validating the Answer

#### 8.1 Potential biases

**Confirmation bias**: Team may favor incremental refactoring because it feels safer, ignoring evidence that debt is accelerating.

**Sunk-cost fallacy**: Reluctance to abandon current codebase even though its architecture is fundamentally unsound.

**Optimism bias**: Underestimating delivery time and complexity of staged rewrite; assuming "we can do it faster than the literature suggests."

**NIH (Not Invented Here)**: Dismissing third-party frameworks without thorough evaluation because team prefers to build in-house.

#### 8.2 Required intelligence and feedback

**Data needed**:
- **Latency breakdown per component**: Profile current system to measure actual time spent in MPC core, coordinator, transaction service, network
- **Chain integration time series**: Document actual hours spent on Bitcoin, Ethereum, and estimated hours for Solana to validate "accelerating debt" hypothesis
- **Audit findings**: Collect all audit reports and map findings to architectural elements
- **Competitor benchmarks**: Measure latency, chain coverage, and audit posture of 2–3 competing custody providers
- **User churn analysis**: Correlate support tickets and app-store reviews with latency/reliability metrics

**Experiments**:
- **Proof-of-concept chain adapter**: Build a minimal Bitcoin adapter using proposed hexagonal design; measure integration time (target: <80 hours)
- **Shadow-mode latency test**: Run new architecture in parallel with current system on synthetic traffic; measure P95 latency and failure rate
- **External architect review**: Hire consultant to audit proposed design and challenge assumptions

**Interviews**:
- **Auditors**: Ask "What would you need to see to issue zero critical findings?" and "How do best-in-class custody providers structure their architectures?"
- **Institutional clients**: Ask "What latency/reliability thresholds would make you switch providers?" and "How important is multi-chain coverage in your decision?"
- **Engineering team**: Ask "Which parts of current codebase are most painful to work with?" and "What would you need to confidently deliver new architecture in 6–12 months?"

#### 8.3 Validation plan

**Phase 1: Design validation (Months 0–2)**
- External architect reviews proposed hexagonal design
- Proof-of-concept chain adapter built and timed
- Auditors consulted on "proof of isolation" requirements
- **Go/no-go decision**: If PoC takes >120 hours or auditors express concerns, revisit design

**Phase 2: Early implementation and shadow mode (Months 3–6)**
- MPC core and Bitcoin adapter deployed in shadow mode alongside current system
- Latency and failure rate measured; compare to baseline
- **Go/no-go decision**: If P95 latency >2.5s or failure rate >3%, investigate before proceeding to Ethereum/Solana

**Phase 3: Full migration (Months 7–12)**
- Ethereum and Solana adapters completed
- Gradual cutover of production traffic (10% → 50% → 100%)
- Final audit conducted
- **Success criteria**: P95 latency <2s, failure rate <2%, zero critical audit findings, Solana integration completed in <80 hours

---

### 9. Revising the Answer

#### 9.1 Parts likely to be revised

**Latency budget allocation**: Initial estimates (800ms MPC, 300ms coordinator, 200ms transaction service, 700ms network) are based on reference designs and prototypes; real-world measurements may require rebalancing.

**Chain-adapter scope**: The 40–80 hour estimate assumes ECDSA/EdDSA chains with standard transaction formats; exotic chains (e.g., zk-rollups with custom signature schemes) may take longer.

**Team capacity**: 5–8 person team may be optimistic if key engineers are pulled into firefighting current production issues; may need to hire or temporarily reduce feature scope.

**Audit timeline**: External auditors may require more documentation or testing than anticipated, potentially extending delivery window to 12–15 months.

#### 9.2 Incremental adjustment approach

**Small-step validation**:
- Rather than committing to full rewrite, build and deploy MPC core + Bitcoin adapter first (months 1–4)
- Measure latency and audit feedback; adjust design before tackling Ethereum/Solana
- If latency budget is violated, iterate on coordinator design or investigate network optimizations (e.g., regional coordinators, precomputation)

**Gradual feature rollout**:
- Start with lower-risk, lower-AUM client segments (e.g., retail, small institutions) before migrating large custody clients
- Use shadow mode and percentage-based traffic routing to derisk cutover

**Regular check-ins**:
- Monthly architecture reviews with external consultant and internal stakeholders
- Bi-weekly latency and audit-readiness scorecards
- Quarterly go/no-go gates based on measurable criteria (latency, failure rate, audit findings, team velocity)

#### 9.3 "Better, not perfect" criteria

**Criterion 1: Provable security isolation**
- Each component's access to key material is documented and testable; auditors can verify no single component can reconstruct keys
- **Good enough**: Passes external audit with zero critical findings and no more than 2–3 minor findings

**Criterion 2: Acceptable performance**
- P95 signing latency ≤2 seconds; failure rate ≤2%
- **Good enough**: Meets thresholds for 95% of traffic; remaining 5% tail can be optimized post-launch

**Criterion 3: Reusable chain onboarding**
- New ECDSA/EdDSA chain can be added in <80 hours by a mid-level engineer following template
- **Good enough**: First new chain (beyond Bitcoin/Ethereum/Solana) takes <120 hours; subsequent chains converge to <80 hours

**Criterion 4: Operational stability**
- New architecture runs in production for 3+ months without major incidents (P0/P1)
- **Good enough**: Incident rate lower than or equal to current system; mean time to recovery (MTTR) improves

---

### 10. Summary & Action Recommendations

#### 10.1 Core insights

1. **Current architecture has crossed into unsustainable territory**: Audit findings, latency complaints, and accelerating chain-integration times indicate that incremental improvements will not suffice; a structured redesign is necessary to remain competitive and compliant.

2. **Hexagonal architecture with layered latency budgets is the leverage point**: Separating MPC core (chain-agnostic threshold signing), coordinator (protocol orchestration), and transaction services (chain adapters) enables both security auditability and engineering velocity, with measurable per-layer performance accountability.

3. **Chain-adapter abstraction can compress integration time by 80%**: A well-designed template and reusable scaffolding can reduce new-chain effort from months to <80 hours for standard ECDSA/EdDSA chains, creating a defensible competitive advantage.

4. **Audit-first design is a strategic requirement, not overhead**: Institutional clients holding $50M–$500M in assets will only trust platforms that can prove security boundaries; designing for audit from the start avoids costly retrofits and unlocks high-value deals.

5. **6–12 month delivery is tight but achievable with discipline**: Success requires hiring/consulting a senior architect, ruthless scope prioritization (Bitcoin, Ethereum, Solana only), phased validation gates, and willingness to adjust based on early feedback rather than committing to a fixed plan.

#### 10.2 Near-term action list (0–3 months)

| Priority | Action | Owner | Expected Result / Metric | Target Date |
|----------|--------|-------|---------------------------|-------------|
| **P0 Critical** | Hire or engage senior distributed-systems architect with custody experience | Head of Engineering | Architect onboarded and architecture-review workshops scheduled | Month 1, Week 2 |
| **P0 Critical** | Conduct latency profiling of current system to measure per-component breakdown | SRE Lead | Report showing actual time spent in MPC core, coordinator, transaction service, network; identify top 3 bottlenecks | Month 1, Week 4 |
| **P0 Critical** | Define hexagonal architecture design with explicit security boundaries and latency budgets | Architect + Security Lead | Architecture document approved by security, SRE, and product; auditor feedback incorporated | Month 2, Week 4 |
| **P1 Important** | Build proof-of-concept Bitcoin chain adapter using proposed design | Senior Backend Engineer | Adapter functional and tested; integration time measured (<80h target) | Month 3, Week 2 |
| **P1 Important** | Consult with external auditors on "proof of isolation" requirements | Compliance Lead + Architect | Written criteria for passing audit; list of required tests and documentation | Month 2, Week 2 |
| **P1 Important** | Establish latency and reliability monitoring dashboards with per-layer budgets | SRE Team | Grafana/Datadog dashboards showing P50/P95/P99 latency and failure rate per component; alerts configured | Month 3, Week 4 |
| **P2 Optional** | Benchmark 2–3 competing custody providers for latency and chain coverage | Product Analyst | Competitive analysis report informing performance targets and feature prioritization | Month 3, Week 2 |

#### 10.3 Risks and responses

| Risk | Impact Level | Trigger Condition | Mitigation / Response |
|------|--------------|-------------------|----------------------|
| **Latency budget violations during PoC** | **High** | Bitcoin adapter PoC shows P95 latency >2.5s in controlled tests | Investigate root cause (protocol choice, network topology, serialization); consider FROST-style 2-round protocols or regional coordinators; adjust budget allocation or extend timeline by 1–2 months |
| **Team capacity constraints** | **High** | Key engineers pulled into production firefighting; PoC or design milestones slip by >2 weeks | Hire contractor or temporarily pause non-critical feature work; escalate to management for resource reallocation; consider extending delivery window to 12–15 months |
| **Audit findings during transition** | **Medium** | Auditor raises concerns about new architecture during design review or early implementation | Address findings immediately; schedule follow-up review; adjust design if necessary; maintain shadow-mode operation of old system as fallback |
| **Underestimation of exotic chain complexity** | **Medium** | Future chain (e.g., zk-rollup, BLS-based) requires >150 hours integration | Accept that 40–80h target applies only to standard ECDSA/EdDSA chains; budget separately for exotic chains; prioritize high-demand chains first |
| **Vendor lock-in if third-party option chosen** | **Medium** | Organization decides to adopt external MPC framework for speed | Negotiate contractual exit clauses; ensure SDK supports key export/migration; maintain in-house cryptographic expertise to reduce dependency |

---


## Problem 2: Threshold-Signature Protocol Portfolio Selection

### Context Recap

**Problem**: Decide which threshold protocols (GG18/GG20 ECDSA, FROST Schnorr/EdDSA, DKLS two-party, threshold BLS) to standardize per curve and chain to balance latency, auditability, implementation complexity, and broad chain coverage while avoiding frequent risky replatforming.

**Key Context**:
- Current situation: GG20-like ECDSA protocols are battle-tested but involve 5–8 rounds (~300ms+ per round on mobile); FROST offers 2-round online signing with significantly lower latency but less production history
- Main pain points: Mobile deployments struggle with multi-round network churn; institutional clients require well-documented, independently reviewed protocols
- Goals: Cover top 3–5 chains within 12–18 months; <1.5–2s P95 mobile signing; 128-bit security with t−1 corruption tolerance; limit major protocol migrations to 1–2 events over 3–5 years
- Hard constraints: Limited in-house cryptography capacity (2–3 specialists), dependence on external libraries and audits, regulatory expectations for production-signing protocol documentation
- Critical background: Decisions made in next 3–9 months will determine protocol choices for 2–4 years, affecting thousands to millions of signatures per day

---

### 1. Problem Definition

#### 1.1 Problem and contradictions

**Core contradiction**: The team must balance **protocol maturity** (favoring older, battle-tested schemes like GG20 ECDSA), **performance** (favoring newer, faster schemes like FROST), and **operational simplicity** (preferring fewer protocols to audit and maintain).

- **Maturity vs. Performance**: GG20 ECDSA has years of production use but ~5–8 communication rounds; FROST has 2-round online signing but less long-term field experience
- **Maturity vs. Simplicity**: Supporting multiple protocols (GG20 for Bitcoin/Ethereum, FROST for Solana, BLS for consensus chains) increases audit burden and codebase complexity
- **Performance vs. Simplicity**: Optimizing protocol choice per chain (e.g., two-party DKLS for mobile-to-server flows) creates a matrix of protocol×chain combinations that's difficult to reason about and audit

**Involved parties**:
- Cryptography and security teams accountable for protocol safety and residual risk
- Mobile and backend engineers implementing and maintaining protocol code under performance targets
- Product and business teams promising which chains and features to customers
- Auditors and regulators scrutinizing protocol maturity and documentation
- End clients bearing ultimate risk of key compromise or signing outages

#### 1.2 Extensibility and common structure

**One object, many attributes**:
- A "threshold signature protocol" can be viewed as:
  - A **cryptographic primitive** (providing unforgeability and key-share privacy)
  - A **distributed algorithm** (coordinating multiple parties over unreliable networks)
  - An **auditability artifact** (requiring formal proofs, reference implementations, and independent reviews)
  - A **performance profile** (characterized by round count, computation time, bandwidth)

**Transformation chains**:
- **Protocol migration path**: GG18 → GG20 (improved security) → FROST (improved performance) → post-quantum threshold schemes (future-proofing)
- **Attribute transformation**: Instead of "which protocol is best," reframe as "which protocol portfolio minimizes total risk exposure while meeting performance thresholds"

**Virtual vs. Physical**:
- **Physical**: Cryptographic library code, network round-trips, mobile device CPU cycles, server HSM operations
- **Virtual**: Security assumptions, audit opinions, protocol "maturity," market perception of safety

**Latent vs. Manifest**:
- **Manifest**: Current need for ECDSA (Bitcoin/Ethereum) and EdDSA (Solana)
- **Latent**: Future demand for BLS (consensus chains), post-quantum schemes (5–10 year horizon), threshold decryption (encrypted memo fields)

---

### 2. Internal Logical Relations

#### 2.1 Key elements

**Protocol Options**:
- **GG18/GG20**: Multi-party ECDSA threshold signing; 5–8 rounds; well-audited; higher latency
- **FROST**: Schnorr/EdDSA threshold signing; 2 rounds online (after offline preprocessing); newer; lower latency
- **DKLS**: Two-party ECDSA; 3–4 rounds; optimized for mobile-server flows; less general than GG20
- **Threshold BLS**: BLS threshold signatures; aggregatable; useful for consensus but not widely supported on payment chains

**Key Trade-offs**:
- **Round count vs. latency**: Fewer rounds mean lower latency but may require more complex precomputation or cryptographic assumptions
- **Generality vs. optimization**: Multi-party protocols (GG20, FROST) support arbitrary t-of-n quorums; two-party protocols (DKLS) optimize specific topologies
- **Maturity vs. innovation**: Older protocols have more field hours and audits; newer protocols offer performance gains but less battle-testing

#### 2.2 Balance and "degree"

**Too much conservatism → competitive disadvantage**:
- Sticking only to GG20 ECDSA means ~2–3 second mobile signing latency, which loses users to faster competitors using FROST or two-party schemes.

**Too much innovation → unvalidated risk**:
- Rushing to deploy FROST before sufficient independent audits and field experience could expose users to undiscovered protocol vulnerabilities.

**Too many protocols → audit and maintenance burden**:
- Supporting GG20, FROST, DKLS, and BLS simultaneously creates a complex audit surface and increases likelihood of implementation bugs or configuration errors.

**Balance point**: Adopt a **phased portfolio approach** where mature protocols (GG20 ECDSA) handle high-value institutional flows in 2024, newer protocols (FROST EdDSA) are introduced for latency-sensitive consumer flows in 2025 after additional audits, and migration criteria (e.g., "2+ independent audits, 6+ months field experience with >1M signatures") guide transitions.

#### 2.3 Key internal causal chains

**Chain 1: Protocol round count → mobile latency → user experience → retention**
- Fewer protocol rounds reduce end-to-end latency → improves mobile UX → increases transaction completion rates → boosts user retention and revenue.

**Chain 2: Protocol maturity → audit confidence → institutional adoption → AUM growth**
- Longer field history and multiple independent audits → auditors and institutional clients trust the protocol → unlocks large custody deals → drives platform growth.

**Chain 3: Protocol diversity → implementation complexity → bug risk → potential incidents**
- Supporting multiple threshold protocols → increases codebase surface area and testing burden → raises probability of subtle implementation flaws → could lead to key compromise or signing failures.

---

### 3. External Connections

#### 3.1 Stakeholders

**Upstream**:
- **Cryptography research community**: Publishes protocol papers (GG18, GG20, FROST) and formal security proofs
- **Open-source library maintainers**: Implement and maintain reference implementations (ZenGo, Coinbase, DFINITY, ZCash foundations)
- **Audit firms**: Conduct independent security reviews of protocol implementations

**Downstream**:
- **End users**: Experience signing latency and reliability directly; bear risk of key compromise
- **Institutional clients**: Require well-documented, audited protocols; may have internal security teams that review protocol choices
- **Regulators**: Assess whether custody providers use "industry-standard" cryptographic practices

**Side-line**:
- **Competing custody providers**: Set market expectations; early adopters of FROST or BLS can gain performance advantages
- **Blockchain foundations**: Sometimes specify preferred signature schemes or provide tooling (e.g., Solana's ed25519 focus)

#### 3.2 Environment and institutions

**Technology environment**:
- Rapid maturation of threshold cryptography: FROST standardization efforts (IRTF CFRG), increasing availability of formally verified implementations
- Emergence of post-quantum signature schemes: NIST PQC standards will eventually require threshold versions

**Market environment**:
- Consumer applications prioritize sub-2-second signing; institutional applications prioritize proven security
- Competitors' protocol choices influence client expectations (e.g., "Why doesn't your platform support FROST like Provider X?")

**Regulatory environment**:
- Regulators and auditors prefer protocols with published standards, multiple independent audits, and documented field experience
- Immature protocols may trigger additional scrutiny or require custom justification

#### 3.3 Responsibility and room to maneuver

**Proactive responsibility**:
- **Own the protocol roadmap**: Publish a clear timeline for which protocols will be used for which chains and use cases, with explicit migration criteria
- **Own the audit and validation process**: Commission independent audits of all production protocols; share results with clients and regulators
- **Own performance benchmarks**: Measure and publish latency and failure-rate metrics per protocol to set realistic expectations

**Leaving room**:
- **For future protocol upgrades**: Design system to support pluggable protocols so that GG20 → FROST migrations do not require full rewrites
- **For regulatory evolution**: Maintain capability to revert to more conservative protocols if new vulnerabilities are discovered or regulations tighten
- **For client customization**: Allow institutional clients to specify protocol preferences (e.g., "only use GG20 for accounts >$10M")

---

### 4. Origins of the Problem

#### 4.1 Key historical nodes

**Stage 1: Early GG18 experiments (Year 1)**
- Team implemented GG18 ECDSA for Bitcoin/Ethereum prototypes
- Latency was acceptable for back-office institutional flows but users complained about mobile experience
- No alternatives were seriously considered due to limited cryptography capacity

**Stage 2: GG20 upgrade and FROST awareness (Year 2)**
- Team upgraded to GG20 for improved security and maintained GG18 compatibility
- Cryptography community began promoting FROST as a faster alternative for Schnorr/EdDSA chains (Solana, etc.)
- Team prototyped FROST but hesitated to deploy due to lack of field experience

**Stage 3: Mobile latency crisis and competitive pressure (Recent months)**
- Mobile users increasingly abandon flows due to ~3–5 second signing times
- Competitors begin marketing "sub-2-second signing with FROST" as a differentiator
- Product team demands faster protocols; security team insists on thorough validation

#### 4.2 Background vs. direct causes

**Background factors**:
- **Cryptographic innovation pace**: Threshold signature research has accelerated, creating a stream of new protocols with different trade-offs
- **Market fragmentation**: Different chains prefer different signature schemes (ECDSA for Bitcoin/Ethereum, EdDSA for Solana, BLS for consensus layers)
- **Limited in-house capacity**: With only 2–3 cryptography specialists, team lacks bandwidth to thoroughly evaluate and implement multiple protocols simultaneously

**Direct triggers**:
- **Mobile UX complaints**: Support tickets and app-store reviews citing "slow wallet" doubled in recent quarter
- **Competitor announcements**: Leading custody provider announced FROST support with published benchmarks showing <1.5s signing
- **Solana integration**: Adding Solana requires EdDSA, naturally raising question of whether to use threshold EdDSA variant or FROST

#### 4.3 Deep structural issues

- **Reactive protocol selection**: Team has historically chosen protocols based on immediate availability rather than strategic roadmap
- **Insufficient validation framework**: No formal criteria for "when is a protocol mature enough for production" leading to ad-hoc decisions
- **Performance-security false dichotomy**: Team has framed choice as "fast but risky" vs. "slow but safe" rather than seeking validated fast protocols

---

### 5. Problem Trends

#### 5.1 Current trend judgment

**If nothing changes**:
- GG20 ECDSA will remain the only production protocol, limiting mobile UX and Solana integration
- Competitors will capture market share by offering faster, FROST-based signing
- Product team will escalate pressure to "just ship FROST" without adequate validation
- Team may rush deployment, potentially exposing users to protocol vulnerabilities

**Likely outcome in 12–18 months**: Platform falls behind on performance, loses consumer and prosumer segments to faster competitors, and either accepts reduced market position or makes high-risk emergency protocol switch under business pressure.

#### 5.2 Early signals and "spots"

**Signal 1: User abandonment clustering**
- Mobile analytics show 15% of users abandon transaction flows after "Waiting for signature" screen exceeds 2 seconds
- Interpretation: Performance threshold has shifted; users now expect sub-2-second signing as table stakes

**Signal 2: Audit firm guidance**
- Recent audit report noted: "GG20 implementation is sound, but team should plan for protocol portfolio diversification to support future chains"
- Interpretation: Even auditors recognize that protocol monoculture is unsustainable given multi-chain roadmap

**Signal 3: FROST maturation**
- IETF CFRG published FROST draft RFC; ZCash and Coinbase have deployed FROST in production with public postmortems
- Interpretation: FROST is crossing from "research prototype" to "production-ready with caveats"

#### 5.3 Possible scenarios

**Optimistic scenario** (30% probability without intervention):
- Team continues with GG20; competitors' FROST deployments experience high-profile bugs
- Market sentiment shifts back to "slower but safer"; institutional clients reward conservatism
- **Risk**: Unlikely given increasing consumer expectations and successful FROST deployments by major providers

**Baseline scenario** (60% probability without intervention):
- Team deploys FROST for Solana in response to product pressure, but without sufficient internal validation
- No immediate incidents, but team lacks confidence in protocol safety; auditors raise concerns
- Platform operates with unclear risk profile; subsequent protocol choices remain ad-hoc

**Pessimistic scenario** (10% probability without intervention):
- Team rushes FROST deployment; subtle implementation bug or protocol weakness is discovered post-launch
- Emergency protocol downgrade or key rotation required; client trust damaged; regulatory scrutiny intensifies

---

### 6. Capability Reserves

#### 6.1 Existing capabilities

**Strengths**:
- **Cryptography expertise**: Team has 2–3 specialists who understand threshold signature theory and have implemented GG20 successfully
- **Audit relationships**: Established relationships with external audit firms who understand custody context
- **Implementation experience**: Successful GG18 → GG20 migration demonstrates team can execute protocol transitions
- **Performance measurement**: SRE team has tooling to measure per-protocol latency and failure rates

#### 6.2 Capability gaps

**Protocol evaluation**:
- No formal framework for assessing protocol maturity (e.g., number of audits, field hours, deployment scale required)
- Limited visibility into competitor and industry protocol choices and outcomes

**Implementation diversity**:
- Team has deep experience with multi-round ECDSA (GG18/GG20) but limited experience with 2-round schemes (FROST) or two-party protocols (DKLS)
- No systematic testing framework for comparing protocol implementations under realistic network conditions

**Cryptography bandwidth**:
- With only 2–3 specialists, team struggles to simultaneously maintain production GG20, evaluate FROST, and plan for future protocols (BLS, post-quantum)

#### 6.3 Capabilities that can be built in the near term

**0–3 months**:
- **Define protocol maturity criteria**: Establish checklist (e.g., "2+ independent audits, 1+ year field experience OR 6+ months + >1M production signatures, formal proof published")
- **Commission FROST audit**: Engage external firm to audit team's FROST implementation or evaluate open-source reference implementation
- **Benchmark protocol latency**: Run controlled tests comparing GG20 ECDSA, FROST EdDSA, and DKLS under realistic mobile network conditions (4G/5G, various latencies)

**3–6 months**:
- **Implement protocol abstraction layer**: Design system to support pluggable threshold protocols, enabling A/B testing and gradual rollout
- **Train team on FROST**: Internal workshops and code reviews to build confidence with 2-round protocol patterns
- **Establish protocol migration playbook**: Document process for safely transitioning from one protocol to another, including key rotation and backwards compatibility

---

### 7. Analysis Outline

#### 7.1 Structured outline

**Background**
- Current protocol: GG20 ECDSA for all chains; ~2–3s mobile signing latency
- Pain points: Mobile UX complaints, competitive pressure, Solana integration requires EdDSA
- Technology environment: FROST maturing, IETF standardization, successful production deployments by peers

**Problem**
- Core contradiction: maturity vs. performance vs. operational simplicity
- Stakeholders: cryptography team, mobile/backend engineers, product, auditors, clients
- Goals: <1.5–2s P95 mobile signing, 128-bit security, cover 3–5 chains in 12–18 months, limit migrations to 1–2 events over 3–5 years

**Analysis**
- Internal logic: Round count drives latency; protocol diversity drives complexity; maturity drives confidence
- External connections: Cryptography research, audit firms, competing providers, regulators
- Origins: Reactive protocol selection, insufficient validation framework, performance-security false dichotomy
- Trends: Without intervention, platform loses consumer market to faster competitors or makes high-risk emergency protocol switch

**Options**
- **Option A**: GG20 only (low risk, poor performance, limits consumer growth)
- **Option B**: FROST for all chains (high performance, moderate risk, requires thorough validation)
- **Option C**: Phased portfolio (GG20 for institutional, FROST for consumer, moderate complexity, balanced risk)

**Risks & Follow-ups**
- Rushing FROST without sufficient audits
- Protocol implementation bugs
- Migration complexity and downtime
- Mitigation: Independent audits, gradual rollout, comprehensive testing, clear maturity criteria

#### 7.2 Key judgments

1. **GG20-only approach is unsustainable**: Mobile latency complaints and competitive pressure will force protocol change; better to plan transition than react under pressure
2. **FROST has crossed maturity threshold for controlled deployment**: IETF standardization, production deployments by ZCash/Coinbase, and availability of audited implementations indicate FROST is ready for phased production use
3. **Protocol portfolio approach balances risk and performance**: Using GG20 for high-value institutional flows and FROST for latency-sensitive consumer flows allows team to optimize for different risk appetites
4. **Formal maturity criteria are essential**: Without clear thresholds (e.g., "2+ audits, 6+ months field experience"), protocol decisions will remain ad-hoc and contentious
5. **Protocol abstraction layer is strategic investment**: Ability to swap protocols enables A/B testing, gradual rollout, and future-proofing for post-quantum schemes

#### 7.3 Alternative paths

**Path A: GG20 only**
- Continue with GG20 ECDSA for all chains; invest in mobile network optimizations (regional coordinators, precomputation)
- **Positioning**: Lowest risk, highest performance cost; suitable only if institutional market is sole focus

**Path B: FROST for all chains**
- Deploy FROST for both ECDSA and EdDSA; sunset GG20 over 12 months
- **Positioning**: Highest performance, moderate risk; requires thorough validation and willingness to handle potential issues

**Path C: Phased portfolio**
- GG20 for institutional/high-value; FROST for consumer/mobile; gradual migration based on maturity criteria
- **Positioning**: Balanced risk/performance; moderate operational complexity; most flexible for diverse client base

---

### 8. Validating the Answer

#### 8.1 Potential biases

**Status quo bias**: Team may favor continuing with GG20 because it's familiar and "works," underweighting competitive and UX costs.

**Innovation bias**: Cryptography specialists may favor FROST because it's technically elegant, underweighting operational risk and audit burden.

**Confirmation bias**: Team may selectively cite FROST success stories while ignoring caveats or deployment challenges.

#### 8.2 Required intelligence and feedback

**Data needed**:
- **FROST field experience**: Survey of production FROST deployments (ZCash, Coinbase, others); number of signatures, incident reports, security advisories
- **Latency benchmarks**: Controlled measurements of GG20 vs FROST under identical network conditions (4G/5G, various latencies and loss rates)
- **Audit opinions**: Solicit multiple audit firms' views on FROST readiness and recommended deployment precautions
- **Client sensitivity**: Survey institutional vs consumer clients on latency tolerance and protocol-conservatism preferences

**Experiments**:
- **FROST proof-of-concept**: Implement FROST EdDSA for Solana in staging environment; measure latency, failure rate, and implementation complexity
- **A/B latency test**: Deploy FROST for 10% of consumer traffic; measure completion rates, latency P95, and error rates compared to GG20 control group
- **Load testing**: Stress-test FROST implementation with high transaction volume to identify performance or reliability issues before production

**Interviews**:
- **Peer platforms**: Ask custody providers who have deployed FROST: "What were your validation criteria?" "What issues did you encounter?" "How did you handle migration?"
- **Audit firms**: Ask "What evidence would you need to approve FROST for production?" "What are residual risks you'd flag?"
- **Protocol authors**: Ask FROST paper authors and implementers: "What are known edge cases?" "What are ongoing research questions?"

#### 8.3 Validation plan

**Phase 1: Maturity assessment (Months 0–2)**
- Survey FROST deployments; collect public postmortems and security advisories
- Commission independent audit of reference FROST implementation
- Benchmark GG20 vs FROST latency in lab and staging environments
- **Go/no-go decision**: If audit finds critical issues or field experience is insufficient, delay FROST and invest in GG20 optimizations

**Phase 2: Controlled deployment (Months 3–6)**
- Deploy FROST for Solana consumer flows (low-AUM, latency-sensitive segment)
- Monitor for 3 months; measure latency, error rate, security incidents
- **Go/no-go decision**: If error rate >3% or security concerns arise, pause expansion and investigate

**Phase 3: Expansion (Months 7–12)**
- Gradually expand FROST to larger consumer base and consider FROST for Ethereum if performance gains are significant
- Maintain GG20 for institutional/high-value flows
- Publish protocol selection criteria and roadmap for client transparency

---

### 9. Revising the Answer

#### 9.1 Parts likely to be revised

**FROST readiness timeline**: Initial assumption that FROST is ready for production may need adjustment if additional security issues are discovered or audit firms express concerns.

**Client segment protocol mapping**: Assumption that "institutional = GG20, consumer = FROST" may be too simplistic; some consumer clients may prefer conservative protocols, and some institutions may tolerate FROST for certain flows.

**Protocol migration effort**: Estimated 3–6 months for phased FROST deployment may be optimistic if backward compatibility or key rotation proves complex.

**Future protocol landscape**: Emergence of new protocols (e.g., threshold post-quantum schemes) or changes in FROST standardization status may require roadmap revision.

#### 9.2 Incremental adjustment approach

**Small-step validation**:
- Start with FROST for lowest-risk use case (e.g., Solana consumer accounts <$1K AUM)
- Measure for 1–3 months; expand only if metrics meet thresholds
- Use feature flags and A/B testing to control rollout pace

**Reversibility**:
- Maintain GG20 as fallback; design system so FROST can be disabled without service disruption
- Implement protocol-agnostic signing API so clients don't directly couple to protocol choice

**Regular check-ins**:
- Monthly protocol steering committee (cryptography, engineering, risk, product) reviews metrics and external intelligence
- Quarterly go/no-go gates based on measured criteria (latency improvement, error rate, field-incident reports)

#### 9.3 "Better, not perfect" criteria

**Criterion 1: Protocol safety**
- FROST deployment shows zero security incidents over 3 months and 1+ independent audits find no critical issues
- **Good enough**: No key compromises or unauthorized signatures; any minor issues are promptly mitigated

**Criterion 2: Performance improvement**
- FROST reduces P95 mobile signing latency from ~2–3s (GG20) to <1.5s; failure rate remains ≤2%
- **Good enough**: Measurable latency reduction (even if not hitting theoretical minimum); user completion rates improve

**Criterion 3: Operational stability**
- FROST implementation maintained alongside GG20 without significantly increasing incident rate or operational burden
- **Good enough**: Incident rate and MTTR comparable to GG20; team reports manageable complexity

**Criterion 4: Client confidence**
- Institutional clients and auditors accept FROST for approved use cases; no major client objections or defections
- **Good enough**: Clear documentation and communication prevent trust issues; clients understand risk trade-offs

---

### 10. Summary & Action Recommendations

#### 10.1 Core insights

1. **GG20-only approach has reached end-of-life for consumer use cases**: Mobile latency complaints, competitive pressure, and client expectations for sub-2-second signing indicate that protocol diversification is necessary for market competitiveness.

2. **FROST has crossed maturity threshold for controlled production use**: IETF standardization efforts, successful production deployments by major providers (ZCash, Coinbase), and availability of audited implementations indicate FROST is ready for phased deployment in consumer/mobile segments with appropriate validation.

3. **Phased portfolio approach balances risk and performance**: Using mature protocols (GG20) for high-value institutional flows while introducing faster protocols (FROST) for latency-sensitive consumer flows allows platform to optimize for different risk appetites and use cases.

4. **Formal protocol maturity criteria prevent ad-hoc decisions**: Establishing clear thresholds (e.g., "2+ independent audits, 6+ months field experience with >1M signatures, or IETF draft RFC") provides objective basis for protocol selection and migration decisions.

5. **Protocol abstraction layer enables safe experimentation**: Designing system to support pluggable protocols enables A/B testing, gradual rollout, emergency rollback, and future-proofing for new schemes (BLS, post-quantum) without architectural rewrites.

#### 10.2 Near-term action list (0–3 months)

| Priority | Action | Owner | Expected Result / Metric | Target Date |
|----------|--------|-------|---------------------------|-------------|
| **P0 Critical** | Define protocol maturity criteria and publish internal protocol roadmap | Cryptography Lead | Document specifying thresholds for production use (audits, field hours, standardization status); roadmap approved by security, engineering, and product | Month 1, Week 2 |
| **P0 Critical** | Commission independent audit of FROST implementation (internal or reference library) | Security Lead | Audit report with findings; list of required mitigations before production use | Month 2, Week 4 |
| **P0 Critical** | Benchmark GG20 vs FROST latency under realistic mobile network conditions | Mobile Engineering Lead | Report showing P50/P95/P99 latency comparison across 4G/5G networks with various loss rates; identify performance gains and edge cases | Month 1, Week 4 |
| **P1 Important** | Survey FROST production deployments and collect lessons learned | Cryptography Engineer | Report summarizing ZCash, Coinbase, and other deployments; incident reports; known edge cases and mitigation strategies | Month 2, Week 2 |
| **P1 Important** | Design protocol abstraction layer to support pluggable threshold protocols | Senior Backend Engineer | Architecture proposal for protocol-agnostic signing API; implementation plan with estimated effort | Month 3, Week 2 |
| **P1 Important** | Implement FROST proof-of-concept for Solana in staging environment | Cryptography + Backend Engineers | Functional FROST signing for Solana; latency and reliability measured; implementation complexity assessed | Month 3, Week 4 |
| **P2 Optional** | Interview peer custody providers about FROST deployment experiences | Product or Engineering Manager | Summary of lessons learned, deployment strategies, and risk mitigations from 2–3 peer platforms | Month 2, Week 4 |

#### 10.3 Risks and responses

| Risk | Impact Level | Trigger Condition | Mitigation / Response |
|------|--------------|-------------------|----------------------|
| **FROST audit finds critical vulnerability** | **High** | Independent audit identifies protocol or implementation flaw with security impact | Delay FROST deployment; work with audit firm to assess severity and mitigation options; invest in GG20 optimizations (precomputation, regional coordinators) as fallback |
| **FROST performance gains are marginal in real-world conditions** | **Medium** | Benchmarks show <20% latency improvement over optimized GG20 | Re-evaluate business case for FROST; consider whether operational complexity justifies modest gains; explore other optimizations (network topology, precomputation) |
| **Protocol abstraction layer introduces excessive overhead** | **Medium** | Pluggable protocol design adds >200ms latency or significantly increases error rate | Simplify abstraction; accept limited protocol flexibility in V1; plan refactor for V2 once requirements are clearer |
| **Institutional clients object to FROST deployment** | **Medium** | Major client or regulator expresses concern about FROST maturity for high-value flows | Maintain GG20 for institutional segment; deploy FROST only for consumer/mobile; provide clear documentation on protocol selection rationale and risk assessment |
| **Unanticipated protocol migration complexity** | **Medium** | Key rotation or backward compatibility proves more difficult than expected; timeline extends by 2–3 months | Simplify scope: deploy FROST only for new Solana accounts initially; migrate existing accounts later; accept longer timeline if necessary for safety |

---


## Problem 3: Mobile Signing Latency and Failure Rate Optimization

### Context Recap

**Problem**: Reduce mobile end-to-end signing latency and failure rates from current ~3.5s P95 and ~15% failures to acceptable levels (<1.5s P95, <2% failures) without weakening cryptographic security or over-provisioning infrastructure.

**Key Context**:
- Current situation: Profiling shows ~60% latency from multi-round threshold ECDSA, ~25% from on-device crypto, ~15% from serialization/transport; users frequently abandon or retry
- Main pain points: "Wallet feels slow or unreliable" is top support complaint; users abandon flows, hurting conversion
- Goals: Cut P95 from ~3.5s to <~1.5s; bring failures below ~1–2%; maintain ≥128-bit security; avoid >20–30% increase in mobile CPU/battery usage
- Hard constraints: Cannot change L1/L2 confirmation rules; shared MPC backend serves both mobile and institutional API flows; budget limits on global coordinator deployment; mobile SDK size and memory must stay within platform constraints
- Critical background: Improvements expected within 3–9 months; will affect tens or hundreds of thousands of mobile users and materially impact activation, transaction frequency, and retention

---

### 1. Problem Definition

#### 1.1 Problem and contradictions

**Core contradiction**: The team must optimize **latency** (requiring fewer network round-trips and faster cryptographic computation) while preserving **security** (requiring threshold protocols with sufficient parties and computational work) and **operational feasibility** (avoiding unsustainable infrastructure scaling or complex protocol changes).

- **Latency vs. Security**: Reducing protocol rounds or precomputing nonces can lower latency but may increase risk if not implemented carefully (e.g., nonce reuse vulnerabilities)
- **Latency vs. Operational Cost**: Deploying regional MPC coordinators globally reduces round-trip time but increases infrastructure complexity and cost
- **Mobile Performance vs. Battery Life**: More aggressive local cryptographic computation (e.g., precomputation on device) can reduce online signing time but drains battery and heats device

**Involved parties**:
- Mobile engineers responsible for client SDKs and UI/UX
- Backend and SRE teams operating MPC clusters and edge infrastructure
- Cryptography engineers guarding protocol safety and implementation correctness
- Product managers tracking conversion funnels and user retention metrics
- End users who care primarily about perceived speed and reliability

#### 1.2 Extensibility and common structure

**One object, many attributes**:
- "Signing latency" can be decomposed into:
  - **Protocol rounds** (number of network round-trips)
  - **Per-round latency** (network RTT + queueing + processing)
  - **Cryptographic computation** (client-side and server-side CPU time)
  - **Serialization/transport** (message encoding, TLS overhead, broker latency)

**Transformation chains**:
- Latency reduction paths:
  - **Protocol substitution**: GG20 (5–8 rounds) → FROST (2 rounds) → latency reduction
  - **Precomputation**: Move expensive operations offline → reduce online signing time
  - **Geographic optimization**: Deploy regional coordinators → reduce network RTT
  - **Algorithmic optimization**: Faster elliptic curve implementations, batch processing → reduce CPU time

**Hard vs. Soft**:
- **Hard**: Cryptographic security level (128-bit), threshold protocol round count (inherent to chosen protocol), mobile device capabilities (CPU, memory, battery)
- **Soft**: Coordinator placement strategy, timeout and retry policies, SDK caching strategies, telemetry and profiling depth

**Latent vs. Manifest**:
- **Manifest**: Current P95 latency ~3.5s and ~15% failure rate measured in production
- **Latent**: Future traffic growth will amplify queueing delays; new markets may have worse network conditions than current user base

---

### 2. Internal Logical Relations

#### 2.1 Key elements

**Latency budget breakdown** (current ~3.5s P95):
- **MPC protocol rounds**: ~60% (~2.1s) — Multi-round threshold ECDSA with mobile network RTTs of ~200–400ms per round
- **On-device cryptographic computation**: ~25% (~875ms) — Client-side elliptic curve operations, zero-knowledge proofs
- **Serialization and transport**: ~15% (~525ms) — Message encoding, TLS handshakes, Kafka broker latency, coordinator overhead

**Failure modes** (current ~15% failure rate):
- **Timeout failures** (~8%): Protocol rounds exceed timeout thresholds; mobile app retries or abandons
- **Network errors** (~5%): Connection drops, packet loss during multi-round protocol execution
- **Backend unavailability** (~2%): MPC coordinator or signing node temporarily unavailable

**Key leverage points**:
1. **Protocol round count**: Switching from 5–8 round GG20 to 2-round FROST could save ~1–1.5s
2. **Regional coordinators**: Deploying coordinators closer to user populations could reduce per-round RTT by ~100–200ms
3. **Precomputation**: Moving nonce generation and preprocessing offline could save ~200–400ms from online path
4. **Cryptographic optimization**: Faster curve implementations or hardware acceleration could save ~100–200ms

#### 2.2 Balance and "degree"

**Too much protocol optimization → security risk**:
- Aggressively precomputing or caching nonces without proper randomness or uniqueness checks can lead to nonce reuse vulnerabilities, enabling key recovery attacks.

**Too much infrastructure investment → unsustainable cost**:
- Deploying coordinators in dozens of regions with hot-standby redundancy provides excellent latency but may exceed budget and operational capacity of a small team.

**Too much mobile computation → battery drain and heat**:
- Offloading all preprocessing to mobile devices saves backend resources but causes noticeable battery drain and device heating, leading to user complaints and OS throttling.

**Balance point**: Adopt a **tiered optimization strategy** where high-impact, low-risk changes (protocol substitution to FROST, regional coordinators in 2–3 key markets) are prioritized in Phase 1 (Months 0–3), moderate-risk changes (selective precomputation with strict nonce management) in Phase 2 (Months 3–6), and optional optimizations (aggressive mobile-side caching) only if needed to hit targets.

#### 2.3 Key internal causal chains

**Chain 1: Protocol round count → network round-trips → tail latency → user abandonment**
- Fewer protocol rounds directly reduce P95 latency → improves perceived responsiveness → reduces abandonment rate → increases transaction volume and user satisfaction.

**Chain 2: Regional coordinators → lower RTT → lower per-round latency → faster signing**
- Placing coordinators geographically close to users reduces network round-trip time → makes each protocol round faster → compounds across multiple rounds to significantly reduce total latency.

**Chain 3: Failure rate → retry behavior → perceived unreliability → support burden**
- Lower failure rate reduces need for retries → improves reliability perception → decreases support tickets and negative reviews → improves retention.

---

### 3. External Connections

#### 3.1 Stakeholders

**Upstream**:
- **Mobile network providers**: Determine RTT, packet loss, and bandwidth available to mobile clients
- **Cloud/CDN providers**: Provide edge compute locations for regional coordinators
- **OS platforms** (iOS, Android): Impose constraints on background processing, battery usage, app size

**Downstream**:
- **End users**: Directly experience latency and reliability; vote with their usage and reviews
- **App store reviewers**: May downrank apps with poor performance or reliability ratings
- **Product growth teams**: Depend on smooth signing UX to drive activation and transaction funnels

**Side-line**:
- **Competing wallets**: Set user expectations; if competitors offer <1s signing, users will demand same
- **Third-party analytics and monitoring tools**: Provide telemetry on user behavior and performance metrics

#### 3.2 Environment and institutions

**Technology environment**:
- Evolution of mobile networks (5G rollout) improves RTT in some markets but many users remain on 4G or worse
- Emergence of WebAuthn and passkey standards may influence user expectations for biometric + crypto latency

**Market environment**:
- Consumer fintech applications (Venmo, Cash App) set sub-1-second transaction expectations
- Crypto-native users may be more tolerant of latency, but mainstream adoption requires parity with Web2 UX

#### 3.3 Responsibility and room to maneuver

**Proactive responsibility**:
- **Own end-to-end latency budget**: Instrument every component (mobile SDK, coordinator, MPC backend) and publish internal latency dashboards
- **Own user experience**: Provide clear UI feedback during signing (progress indicators, estimated time) to manage expectations
- **Own performance validation**: Run continuous synthetic monitoring from different geographies and network conditions

**Leaving room**:
- **For future protocol upgrades**: Design mobile SDK to support protocol versioning so that future optimizations (e.g., FROST → improved FROST variants) can be deployed without forcing all users to upgrade immediately
- **For infrastructure scaling**: Architect coordinator deployment so that adding new regions is straightforward operational task, not architectural change
- **For user control**: Allow power users to trade latency for battery (e.g., "performance mode" that does more local precomputation)

---

### 4. Origins of the Problem

#### 4.1 Key historical nodes

**Stage 1: Initial mobile SDK with GG20 (Year 1)**
- Team shipped mobile SDK using GG20 threshold ECDSA for consistency with backend
- Latency was ~2–2.5s on good networks, ~3–5s on weak networks
- Initial user base was crypto-native and relatively tolerant of delays

**Stage 2: User growth and complaint clustering (Year 2)**
- Mobile user base grew 3–5×; more mainstream users with lower latency tolerance
- Support tickets citing "slow wallet" began appearing; app store reviews mentioned "unreliable signing"
- Product team flagged latency as top growth blocker

**Stage 3: Profiling and competitive pressure (Recent months)**
- Engineering team profiled latency and identified protocol rounds as dominant factor (~60% of budget)
- Competitors began marketing sub-2-second signing; user expectations shifted
- Product team demanded immediate fixes; engineering team lacked clear optimization roadmap

#### 4.2 Background vs. direct causes

**Background factors**:
- **Protocol choice**: Early decision to use GG20 for all use cases without considering mobile-specific optimizations
- **Infrastructure topology**: Centralized MPC coordinator in single region increases RTT for global users
- **User base evolution**: Shift from crypto-native early adopters to mainstream consumers with Web2 UX expectations

**Direct triggers**:
- **User abandonment metrics**: Analytics showed 15–20% of users abandon transactions after "Waiting..." exceeds 2 seconds
- **Competitive benchmarking**: Leading competitor demonstrated <1.5s signing in head-to-head tests
- **App store rating drop**: Average rating declined from 4.5 to 4.0 stars with "slow" as recurring complaint

#### 4.3 Deep structural issues

- **Mobile-backend impedance mismatch**: Backend MPC system designed for institutional API flows (where 2–3s latency is acceptable) applied directly to mobile without mobile-specific optimization
- **Lack of latency budget discipline**: No explicit allocation of latency budget per component; optimization efforts were reactive and unsystematic
- **Insufficient telemetry**: Limited visibility into per-component latency and failure modes made root-cause analysis difficult

---

### 5. Problem Trends

#### 5.1 Current trend judgment

**If nothing changes**:
- User abandonment rate will increase as competitor wallets offer faster signing
- App store ratings will continue to decline, hurting organic growth
- Product team will either escalate pressure for immediate fixes or deprioritize mobile in favor of institutional/desktop flows
- Engineering team may make ad-hoc, high-risk optimizations under pressure

**Likely outcome in 6–12 months**: Mobile product becomes secondary offering; organization loses consumer and prosumer segments to faster competitors; or team makes emergency protocol/architecture changes that introduce instability.

#### 5.2 Early signals and "spots"

**Signal 1: Abandonment rate by latency bucket**
- Users experiencing <2s signing complete transactions 85% of the time
- Users experiencing 2–3s complete 70% of the time
- Users experiencing >3s complete only 50% of the time
- **Interpretation**: Clear latency sensitivity threshold around 2 seconds

**Signal 2: Geography-specific complaints**
- Support tickets from Asia-Pacific and Latin America (further from current US-based coordinator) are 2× more likely to cite "slow wallet"
- **Interpretation**: Network distance is material factor; regional coordinators could help

**Signal 3: Competitive pressure increasing**
- Two major competitors have announced <1.5s signing as marketing differentiator in past quarter
- **Interpretation**: Latency has become competitive battleground; table stakes are rising

#### 5.3 Possible scenarios

**Optimistic scenario** (25% probability without intervention):
- Team ships protocol optimization (e.g., FROST) and regional coordinators within 3 months
- Latency drops to <1.5s P95; user satisfaction and retention improve materially
- **Risk**: Requires rapid execution and no major protocol or infrastructure issues during rollout

**Baseline scenario** (60% probability without intervention):
- Team makes incremental optimizations (code tuning, caching) over 6 months; latency drops to ~2.5–3s
- Improvement is noticeable but insufficient; competitors maintain lead
- Product team accepts reduced mobile market position or continues pressure for more aggressive changes

**Pessimistic scenario** (15% probability without intervention):
- Team attempts risky optimization (e.g., aggressive precomputation without proper nonce management)
- Security vulnerability is introduced or infrastructure change causes reliability regression
- User trust damaged; major incident or regulatory scrutiny

---

### 6. Capability Reserves

#### 6.1 Existing capabilities

**Strengths**:
- **Mobile engineering competence**: Team has shipped and maintained mobile SDKs for iOS and Android
- **Profiling and instrumentation**: Team has identified latency breakdown and can measure per-component performance
- **Backend scalability**: SRE team operates distributed MPC infrastructure; can add regional coordinators
- **Cryptographic expertise**: Cryptography team understands protocol trade-offs and can evaluate optimization safety

#### 6.2 Capability gaps

**Performance engineering**:
- Limited experience with mobile-specific optimizations (precomputation, caching, background processing)
- No systematic A/B testing framework for evaluating latency optimizations in production

**Infrastructure expansion**:
- No established playbook for deploying regional coordinators; unclear operational overhead
- Limited visibility into which geographies would benefit most from regional deployment

**Protocol migration**:
- Team has not previously migrated mobile clients from one threshold protocol to another at scale
- Uncertainty about backward compatibility, versioning, and gradual rollout strategies

#### 6.3 Capabilities that can be built in the near term

**0–3 months**:
- **Implement geographic telemetry**: Add instrumentation to mobile SDK to report user location and per-round latency; identify high-priority regions for coordinator deployment
- **Prototype FROST mobile integration**: Build proof-of-concept FROST signing in mobile SDK; measure latency improvement and battery impact
- **Design regional coordinator playbook**: Document process for deploying, monitoring, and maintaining regional coordinators

**3–6 months**:
- **Build A/B testing infrastructure**: Implement feature flags and experiment framework to test latency optimizations on subset of users before full rollout
- **Train team on precomputation patterns**: Workshops on safe nonce generation, session management, and cache invalidation
- **Establish latency SLOs**: Define and publish per-component service-level objectives; integrate into monitoring and alerting

---

### 7. Analysis Outline

#### 7.1 Structured outline

**Background**
- Current state: ~3.5s P95 latency, ~15% failure rate on mobile; driven by multi-round protocol, mobile network conditions
- Pain points: User abandonment, poor app store ratings, competitive disadvantage
- Market pressure: Competitors offering <1.5s signing; user expectations rising

**Problem**
- Core contradiction: latency vs. security vs. operational feasibility
- Stakeholders: mobile engineers, SRE, cryptography, product, end users
- Goals: <1.5s P95 latency, <2% failures, maintain security, avoid excessive battery drain

**Analysis**
- Internal logic: Protocol rounds (60%), device crypto (25%), serialization (15%); multiple potential optimization levers
- External connections: Mobile networks, cloud providers, competing wallets, user expectations
- Origins: Protocol designed for backend, not mobile; lack of latency budget discipline; user base evolution
- Trends: Without intervention, mobile product becomes uncompetitive; team may make risky emergency changes

**Options**
- **Option A**: Protocol substitution (FROST) — High impact, moderate risk, 3–6 months
- **Option B**: Regional coordinators — Moderate impact, low risk, 2–4 months
- **Option C**: Precomputation — Moderate impact, moderate risk (nonce management), 3–6 months
- **Combined approach**: Phased deployment of A + B in Phase 1, C in Phase 2

**Risks & Follow-ups**
- Protocol migration bugs or compatibility issues
- Regional coordinator operational complexity
- Nonce reuse vulnerabilities if precomputation is mishandled
- Mitigation: Phased rollout, comprehensive testing, clear nonce-management protocols

#### 7.2 Key judgments

1. **Protocol substitution (GG20 → FROST) is highest-impact lever**: Reducing 5–8 rounds to 2 rounds can save 1–1.5s, making it most effective single optimization
2. **Regional coordinators in 2–3 key markets offer quick wins**: Deploying coordinators in APAC, LATAM, Europe can reduce RTT by 100–200ms with relatively low risk and cost
3. **Precomputation requires careful nonce management**: While precomputation can save 200–400ms, it introduces nonce reuse risk if not implemented with strict randomness and session management protocols
4. **Tiered optimization strategy balances risk and timeline**: Prioritizing high-impact, low-risk changes (protocol + regional coordinators) in Phase 1 allows team to hit <1.5s target while deferring moderate-risk optimizations (precomputation) to Phase 2 if still needed
5. **Continuous telemetry and A/B testing are essential**: Without systematic measurement and experimentation, team risks making changes that don't materially improve UX or introduce new issues

#### 7.3 Alternative paths

**Path A: Protocol-only optimization**
- Deploy FROST for mobile clients; no infrastructure or precomputation changes
- **Positioning**: Simplest approach; may hit <1.5s target if protocol is dominant bottleneck; doesn't address geographic latency disparities

**Path B: Infrastructure-first optimization**
- Deploy regional coordinators in 3–5 regions; keep GG20 protocol
- **Positioning**: Lower risk; provides geographic fairness; may not fully hit latency target without protocol change

**Path C: Comprehensive optimization**
- FROST protocol + regional coordinators + precomputation + cryptographic optimization
- **Positioning**: Highest performance ceiling; highest complexity and risk; requires careful sequencing and validation

---

### 8. Validating the Answer

#### 8.1 Potential biases

**Silver bullet bias**: Team may expect protocol substitution alone to solve latency problem, underestimating contributions from network topology and serialization overhead.

**Infrastructure bias**: SRE team may favor regional coordinator deployment because it's familiar operational task, even if protocol optimization offers greater impact.

**Risk aversion**: Team may avoid protocol migration due to perceived risk, accepting suboptimal performance rather than executing controlled change.

#### 8.2 Required intelligence and feedback

**Data needed**:
- **Geographic latency distribution**: Measure per-round RTT from different user locations to current coordinator; identify regions with >200ms RTT
- **Protocol latency breakdown**: Isolate time spent in protocol computation vs. network waiting; validate that protocol rounds are truly ~60% of budget
- **Battery impact baseline**: Measure current mobile SDK battery usage; establish ceiling for acceptable increase (e.g., <30% increase)
- **Competitor benchmarks**: Test latency of 2–3 competing wallets under identical network conditions

**Experiments**:
- **FROST proof-of-concept on mobile**: Deploy FROST to small user cohort (1–5%); measure latency improvement, failure rate, and battery impact
- **Regional coordinator pilot**: Deploy coordinator in one non-US region (e.g., Singapore); measure latency improvement for nearby users
- **A/B precomputation test**: Implement nonce precomputation for test cohort; measure online signing time reduction and monitor for any nonce-related anomalies

**Interviews**:
- **End users**: Survey or interview users who have abandoned transactions; ask about latency tolerance and reliability expectations
- **Mobile engineers from peer platforms**: Ask about optimization strategies, latency targets, and lessons learned from protocol or infrastructure changes
- **Cryptography experts**: Consult on safe precomputation patterns and nonce management best practices

#### 8.3 Validation plan

**Phase 1: High-impact, low-risk optimizations (Months 0–3)**
- Deploy FROST for mobile in staged rollout (5% → 25% → 50% → 100% over 6 weeks)
- Deploy regional coordinators in 2 key markets (e.g., Singapore, São Paulo)
- Measure P95 latency and failure rate weekly; target <1.8s P95 after Phase 1
- **Go/no-go decision**: If latency target not approached or new issues emerge, pause and investigate before Phase 2

**Phase 2: Moderate-risk optimizations (Months 3–6)**
- If Phase 1 achieves <1.8s but not <1.5s, implement selective precomputation with strict nonce-management protocol
- Deploy additional regional coordinators if geographic latency disparities remain
- **Go/no-go decision**: If precomputation introduces reliability issues, roll back and accept Phase 1 results

**Phase 3: Monitoring and refinement (Months 6–9)**
- Monitor optimized system for 3 months; measure user satisfaction, transaction volume, app store ratings
- Iterate on remaining bottlenecks (e.g., cryptographic library tuning, serialization optimization)
- **Success criteria**: P95 latency <1.5s, failure rate <2%, no security incidents, user satisfaction and retention metrics improve

---

### 9. Revising the Answer

#### 9.1 Parts likely to be revised

**Protocol impact estimate**: Assumption that FROST reduces latency from ~2.1s to ~0.7–1.0s may be optimistic if other factors (serialization, coordinator overhead) are larger than profiling suggests; may require infrastructure optimizations in addition to protocol change.

**Regional coordinator benefit**: Estimate of 100–200ms RTT reduction may not materialize if coordinator placement is suboptimal or if users are more distributed than current data suggests.

**Battery impact**: Assumption that FROST or precomputation won't significantly increase battery usage may need revision if mobile testing shows >30% increase, requiring further optimization or trade-offs.

**Timeline**: Estimate of 3–6 months for full optimization may be aggressive if protocol migration or regional deployment encounters unexpected issues; may extend to 6–9 months.

#### 9.2 Incremental adjustment approach

**Small-step validation**:
- Deploy each optimization (FROST, regional coordinators, precomputation) to 5–10% of users first
- Measure for 1–2 weeks; expand only if metrics meet thresholds and no new issues appear
- Use feature flags to enable instant rollback if problems arise

**Phased geography rollout**:
- For regional coordinators, deploy to one region first (e.g., APAC); measure for 2–4 weeks
- Expand to additional regions only after validating operational model and latency improvement

**Layered optimizations**:
- Start with protocol substitution (highest impact); measure results
- Add regional coordinators if protocol alone doesn't hit target; measure incremental benefit
- Add precomputation only if first two layers are insufficient; maintain careful nonce management

#### 9.3 "Better, not perfect" criteria

**Criterion 1: Latency improvement**
- P95 mobile signing latency ≤1.5s on typical 4G/5G networks
- **Good enough**: Achieves ≤1.8s on 90% of traffic; remaining slow tail addressed post-launch

**Criterion 2: Reliability**
- Failure rate ≤2%
- **Good enough**: Failure rate reduced from ~15% to <3%; further improvement through monitoring and iteration

**Criterion 3: Security maintained**
- No nonce reuse or key-share exposure incidents; all optimizations reviewed by cryptography team
- **Good enough**: Zero security incidents over 3-month validation period; audit sign-off on changes

**Criterion 4: User satisfaction**
- Transaction abandonment rate decreases by ≥30%; app store ratings improve by ≥0.2 stars
- **Good enough**: Measurable improvement in user behavior and feedback; support tickets re: latency decrease by ≥50%

---

### 10. Summary & Action Recommendations

#### 10.1 Core insights

1. **Protocol rounds are dominant latency factor**: ~60% of current ~3.5s P95 latency comes from multi-round threshold ECDSA; switching to 2-round FROST offers highest single-optimization impact, potentially saving 1–1.5s.

2. **Geographic network distance is material secondary factor**: Users far from current US-based coordinator experience 2× higher latency; deploying regional coordinators in 2–3 key markets (APAC, LATAM, Europe) can reduce RTT by 100–200ms with relatively low risk.

3. **Tiered optimization strategy minimizes risk while maximizing impact**: Prioritizing protocol substitution and regional coordinators in Phase 1 (high impact, moderate/low risk) allows team to approach <1.5s target; precomputation can be deferred to Phase 2 if still needed, reducing nonce-management risk.

4. **Current ~15% failure rate is unacceptable for consumer product**: Timeout and network failures drive user abandonment and poor reviews; optimizations that reduce latency will also reduce timeout failures, but separate attention to retry logic and timeout tuning is needed.

5. **Systematic telemetry and A/B testing are essential for safe optimization**: Without continuous measurement and controlled experiments, team risks making changes based on assumptions rather than data, potentially wasting effort or introducing new issues.

#### 10.2 Near-term action list (0–3 months)

| Priority | Action | Owner | Expected Result / Metric | Target Date |
|----------|--------|-------|---------------------------|-------------|
| **P0 Critical** | Implement geographic telemetry in mobile SDK to measure per-user latency and location | Mobile Engineering Lead | Dashboard showing latency distribution by geography; identify top 3 regions for coordinator deployment | Month 1, Week 2 |
| **P0 Critical** | Build and deploy FROST mobile proof-of-concept to 5% of users | Cryptography + Mobile Engineers | Latency and failure-rate comparison vs GG20 control group; battery impact measured | Month 1, Week 4 |
| **P0 Critical** | Deploy regional MPC coordinator in one key market (e.g., Singapore or São Paulo) | SRE Lead | Coordinator operational; RTT reduction measured for nearby users; operational playbook documented | Month 2, Week 2 |
| **P1 Important** | Expand FROST rollout to 25% → 50% → 100% of mobile users if PoC succeeds | Mobile + Backend Engineering Leads | P95 latency reduced from ~3.5s toward <1.8s; no security or reliability regressions | Month 3, Week 4 |
| **P1 Important** | Deploy regional coordinators in 2 additional markets if geographic disparities remain | SRE Team | RTT improvements measured in target regions; latency equity across geographies improved | Month 3, Week 2 |
| **P1 Important** | Implement A/B testing infrastructure for mobile latency experiments | Mobile Engineering + Data Team | Feature flag system operational; experiment framework allows safe testing of optimizations on user cohorts | Month 2, Week 4 |
| **P2 Optional** | Research and prototype precomputation with nonce management protocol if Phase 1 doesn't hit <1.5s target | Cryptography + Mobile Engineers | Design document for safe precomputation; PoC implementation with nonce-reuse safeguards | Month 3, Week 4 |

#### 10.3 Risks and responses

| Risk | Impact Level | Trigger Condition | Mitigation / Response |
|------|--------------|-------------------|----------------------|
| **FROST migration introduces reliability regression** | **High** | Failure rate increases above baseline during FROST rollout | Immediate rollback via feature flags; investigate root cause (protocol bugs, timeout tuning, network conditions); delay full rollout until resolved |
| **Geographic latency improvements are smaller than expected** | **Medium** | Regional coordinators reduce RTT by <50ms instead of expected 100–200ms | Re-evaluate coordinator placement; consider CDN or anycast routing; accept that protocol optimization is primary lever and infrastructure is secondary |
| **Battery usage increases significantly with FROST** | **Medium** | Mobile testing shows >40% battery drain increase compared to GG20 | Tune FROST implementation for mobile (reduce computation where possible); provide user control ("performance mode" vs "battery saver"); consider hybrid approach (FROST for WiFi, GG20 for cellular) |
| **Precomputation introduces nonce reuse vulnerability** | **High** | Security review or monitoring detects potential nonce reuse scenarios | Do not proceed with precomputation until nonce-management protocol is formally reviewed and tested; maintain strict session isolation and randomness checks |
| **Timeline delays due to unforeseen protocol or infrastructure issues** | **Medium** | Phase 1 takes 4–5 months instead of 3 months | Accept extended timeline; maintain transparent communication with product team and users; focus on delivering safe, validated optimizations rather than rushing |

---


## Problem 4: Policy-Driven Approval Engine Design

### Context Recap

**Problem**: Design and calibrate policy/approval engine to meaningfully reduce fraud and operational risk without causing alert fatigue, rubber-stamping, or parallel shadow workflows that bypass MPC controls.

**Key Context**:
- Current situation: Transaction attributes (amount, asset, counterparty, initiator, time, behavior) map to quorums and rate limits; existing financial systems show poorly tuned rules lead approvers to click through mechanically or bypass system
- Main pain points: Need balance between strong controls and smooth operations; institutional clients expect both
- Goals: High-risk transactions escalated within acceptable approval times (SLA-compliant median decision time per risk band); false-positive block rate <1–3%; majority of volume remains in policy-driven MPC flows rather than exceptions
- Hard constraints: Limited UX budget for complex approval interfaces; diverse risk appetites; need audit-understandable policies; difficulty running controlled experiments on high-value flows
- Critical background: Policy decisions influence all high-value flows over multi-year horizons; immediate effects on daily approval workload and customer satisfaction across tens of millions to billions of dollars AUM

---

### 1. Problem Definition

**Core contradiction**: The system must be **strict enough** to prevent fraud and operational errors (requiring multiple approvals, rate limits, counterparty checks) while being **permissive enough** to support legitimate business velocity (avoiding excessive approval latency or false positives that frustrate users and drive shadow workflows).

**Involved parties**: Custody ops teams (executing approvals), risk/compliance teams (defining policies), security/MPC engineers (implementing enforcement), product managers (balancing UX and safety), auditors (reviewing configurations), institutional clients (bearing loss and SLA impacts).

**Key contradiction dimensions**:
- **Safety vs. Velocity**: Requiring 3–4 approvals for every transaction above $10K prevents fraud but delays legitimate business-critical transfers
- **Precision vs. Simplicity**: Complex rules can distinguish legitimate from suspicious flows but are harder to explain, audit, and maintain
- **Consistency vs. Flexibility**: Strict uniform policies ensure fairness and auditability but don't accommodate legitimate client-specific risk appetites

---

### 2. Internal Logical Relations

**Key elements**:
- **Policy rules**: If-then logic mapping transaction attributes → required quorum, approval timeout, rate limits
- **Approval mechanisms**: Human approvers, automated risk scoring, time-locked releases
- **Feedback loops**: Approvers' behavior (click-through rate, approval latency) influences perceived urgency and policy effectiveness

**Balance points**:
- **Too strict** → alert fatigue → rubber-stamping or shadow systems
- **Too permissive** → fraud exposure → regulatory penalties or client losses
- **Sweet spot**: Risk-based tiers where low-risk flows auto-approve, medium-risk require single approval within minutes, high-risk require multiple approvals with documented rationale

---

### 3. External Connections

**Stakeholders**: Institutional clients (vary in risk appetite), regulators (require audit trails), custody ops teams (execute approvals), internal risk teams (tune policies).

**Environment**: Financial crime landscape (phishing, insider threats), regulatory frameworks (AML, KYC, sanctions screening), competitive pressure (clients demand fast turnaround).

**Responsibility**: Team must own policy tuning, approver training, and UX design; leave room for client-specific customization without creating un-auditable complexity.

---

### 4. Origins

**Historical evolution**: Early systems used coarse-grained limits (e.g., "all transfers >$100K require CFO approval"); as volume grew, approvers became bottlenecks, leading to ad-hoc workarounds and inconsistent enforcement.

**Background factors**: Lack of risk-scoring infrastructure, insufficient approver capacity, unclear policy ownership.

**Direct triggers**: Recent near-miss incidents (phishing attempts that nearly succeeded due to rubber-stamping), client complaints about approval delays, audit findings on policy gaps.

---

### 5. Problem Trends

**If nothing changes**: Approval workload will grow unsustainably; false positives will drive shadow workflows; fraud risk will increase as approvers disengage; auditors will escalate findings.

**Signals**: Increasing click-through rate (approvers spending <10s per decision), rising exception-flow volume, clustering of client complaints about approval delays.

**Scenarios**: Baseline (60%): policies remain poorly tuned, fraud incidents increase, audit escalates; Pessimistic (15%): major fraud event exposes policy failures, regulatory sanctions follow.

---

### 6. Capability Reserves

**Strengths**: Risk and compliance teams understand financial crime patterns; ops teams have approval workflow experience; MPC infrastructure can enforce programmatic controls.

**Gaps**: Limited data science capacity for risk modeling; no A/B testing framework for policy tuning; approvers lack real-time context (transaction history, entity reputation).

**Near-term builds**: Risk-scoring model, approver dashboard with contextual data, policy simulation tools, approver training programs.

---

### 7. Analysis Outline

**Problem**: Balance fraud prevention with operational velocity and user satisfaction.

**Options**:
- **A**: Coarse-grained rules (simple, easy to audit, high false-positive rate)
- **B**: Machine-learning risk scoring (adaptive, complex to explain, requires data infrastructure)
- **C**: Tiered hybrid (rules for high-confidence cases, human judgment for edge cases)

**Recommendation**: Option C — tiered hybrid with clear escalation paths and continuous policy tuning based on false-positive rates and approval latency.

---

### 8. Validating the Answer

**Required data**: Historical transaction patterns, false-positive/false-negative rates, approver decision latency, client satisfaction surveys.

**Experiments**: Shadow-mode policy testing (apply new rules to historical transactions, measure would-be outcomes); A/B test policy variants on low-risk client segments.

**Interviews**: Ops teams (approval pain points), clients (UX expectations), auditors (policy clarity requirements).

---

### 9. Revising the Answer

**Likely revisions**: Initial risk-score thresholds may need adjustment based on false-positive rates; approver capacity may be insufficient, requiring additional hiring or tooling; client-specific customizations may prove more complex than anticipated.

**Incremental approach**: Start with conservative rules; gradually relax based on measured false-positive rates; provide escape hatches for urgent legitimate flows.

---

### 10. Summary & Action Recommendations

**Core insights**:
1. **Risk-based tiering prevents both alert fatigue and fraud exposure**: Low-risk auto-approve, medium-risk single approval, high-risk multi-party approval with documentation.
2. **Approver context is critical**: Providing transaction history, entity reputation, and risk scores enables informed decisions rather than rubber-stamping.
3. **Continuous tuning based on metrics**: Monitor false-positive rate, approval latency, and click-through rate; adjust policies quarterly.

**Near-term actions** (0–3 months):

| Priority | Action | Owner | Expected Result | Target Date |
|----------|--------|-------|-----------------|-------------|
| **P0** | Define risk-based approval tiers and initial thresholds | Risk Lead | Policy document with 3–5 tiers, approved by compliance and product | Month 1, Week 2 |
| **P0** | Build approver dashboard with transaction context and risk scores | Engineering Lead | Dashboard deployed; approvers report improved decision confidence | Month 2, Week 4 |
| **P1** | Implement policy simulation tool to test rule changes on historical data | Data Engineer | Tool operational; policy changes validated before production | Month 3, Week 2 |
| **P1** | Train approval teams on new policies and dashboard usage | Ops Lead | Training complete; approvers demonstrate competency in test scenarios | Month 2, Week 2 |

**Risks**:
- **Alert fatigue despite tiers**: If thresholds too low, medium-risk tier generates excessive approvals → monitor click-through rate, adjust thresholds.
- **Client pushback on approval delays**: High-value clients may demand faster turnaround → provide VIP lanes with compensating controls (enhanced monitoring, post-approval review).
- **False negatives (missed fraud)**: Overly permissive rules may let fraud through → maintain fraud monitoring; require post-incident policy reviews.

---


## Problem 5: Balancing Liveness and Security During Partial Failures

### Context Recap

**Problem**: Decide how to adjust quorums, route around failing domains, or temporarily pause signing when some MPC share-holders are offline or compromised, balancing critical flow continuity against preserving effective corruption thresholds.

**Key Context**:
- Current situation: Production deployments use 3-of-5 or 4-of-7 across heterogeneous domains (HSMs, cloud enclaves, devices); real incidents (network partitions, maintenance, suspicious telemetry) leave parts unavailable
- Main pain points: Stakeholders push for automatic failover to keep flows moving; others concerned about silently weakening security (reducing effective independent-compromise threshold)
- Goals: Explicit policies/mechanisms for acceptable degraded modes (asset tiers, values, client types); bounds on degraded-state time (<X hours/month); limits on volume under weakened thresholds; prompt incident detection/rotation
- Hard constraints: Regulatory requirements on key-holder diversity; complexity of dynamic quorum management in MPC; operational limits on investigating/rotating compromised nodes; client intolerance for downtime and opaque risk changes
- Critical background: Policies exercised repeatedly over system lifetime under market stress; single flawed decision could enable catastrophic drain or multi-hour signing outages during critical windows

---

### 1. Problem Definition

**Core contradiction**: The system must maintain **signing availability** (requiring ability to operate with fewer parties when some are unavailable) while preserving **effective security thresholds** (ensuring minimum number of independent compromises required to drain funds doesn't silently drop to dangerous levels).

**Involved parties**: Security architects (designing quorum/failover rules), SRE/ops (monitoring health, managing incidents), risk/compliance (defining acceptable degraded-state behavior), product (promising availability SLAs), institutional clients (capital at stake).

**Key tensions**:
- **Liveness vs. Security**: Allowing 2-of-5 signing when 3 parties are offline maintains service but reduces corruption threshold from 3 to 2
- **Automation vs. Human Oversight**: Automatic failover prevents outages but may silently degrade security; manual intervention introduces delay and potential for errors under pressure
- **Transparency vs. Panic**: Notifying clients of degraded state maintains trust but may trigger unnecessary withdrawals; hiding state changes erodes trust if discovered

---

### 2. Internal Logical Relations

**Key elements**:
- **Quorum configurations**: Normal (e.g., 3-of-5), degraded (e.g., 2-of-4 if one party offline), emergency (e.g., 2-of-3 if two parties offline)
- **Asset tiers**: Critical assets (>$10M) never enter degraded mode; high-value ($1M–$10M) allow short degraded windows (<1 hour); standard assets (<$1M) tolerate longer degraded periods
- **Triggering conditions**: Automated health checks, suspicious telemetry, network partitions, scheduled maintenance

**Balance points**:
- **Too conservative** (never allow degraded mode) → prolonged outages → client frustration, business loss
- **Too permissive** (frequent auto-failover) → increased blast radius → higher fraud risk, regulatory concerns
- **Sweet spot**: Tier-based policies where critical assets remain offline in degraded state, while lower-value assets continue with enhanced monitoring and time limits

---

### 3. External Connections

**Stakeholders**: Regulators (require minimum key-holder diversity), institutional clients (intolerant of both downtime and opacity), insurance providers (assess risk profiles for coverage), incident-response teams (execute containment and rotation).

**Environment**: Market volatility can create urgent signing needs (e.g., liquidations, collateral moves) that conflict with security conservatism; regulatory frameworks impose hard constraints on acceptable degraded-state behavior.

**Responsibility**: Team must own clear degraded-mode policies, monitoring, and client communication; leave room for client-specific SLAs (some clients may prefer downtime over degraded security).

---

### 4. Origins

**Historical evolution**: Early systems used fixed thresholds without degraded-mode support, leading to complete outages during partial failures; ad-hoc manual overrides were introduced during incidents, creating inconsistent risk profiles.

**Background factors**: Lack of formal liveness-security trade-off analysis; insufficient monitoring to detect partial failures early; unclear ownership of degraded-mode decisions.

**Direct triggers**: Major outage (3-hour signing downtime) that prevented clients from meeting margin calls; subsequent demand for "never go fully offline"; conflicting security team pushback.

---

### 5. Problem Trends

**If nothing changes**: Ad-hoc degraded-mode decisions will continue, creating inconsistent risk exposure; major incident (either fraud or prolonged outage) will eventually occur; regulators or clients will lose confidence.

**Signals**: Increasing frequency of partial failures (monthly → weekly); growing volume of manual override requests; clustering of client complaints about both downtime and lack of transparency.

**Scenarios**: Baseline (60%): System continues with inconsistent policies, minor incidents accumulate, trust erodes; Pessimistic (20%): Catastrophic drain during degraded mode or multi-day outage during critical market event.

---

### 6. Capability Reserves

**Strengths**: SRE teams have incident-response experience; security teams understand cryptographic thresholds; existing MPC infrastructure supports configurable quorums.

**Gaps**: No formal framework for liveness-security trade-offs; limited automated monitoring for anomalous signing patterns in degraded mode; insufficient client communication templates for degraded-state notifications.

**Near-term builds**: Degraded-mode policy framework, automated anomaly detection, client notification templates, runbooks for safe quorum adjustments.

---

### 7. Analysis Outline

**Problem**: Balance signing availability with security preservation during partial failures.

**Options**:
- **A**: Never degrade (maintain full threshold or go offline) — Maximally secure, poor availability
- **B**: Automatic failover (always maintain signing with reduced quorum) — Maximally available, security risk
- **C**: Tier-based degraded modes (critical assets offline, standard assets continue with limits) — Balanced approach

**Recommendation**: Option C — tier-based with explicit time/volume limits, enhanced monitoring during degraded periods, and prompt incident investigation.

---

### 8. Validating the Answer

**Required data**: Historical failure patterns (frequency, duration, clustering), blast-radius analysis (% of total AUM at risk in various degraded scenarios), client SLA requirements.

**Experiments**: Table-top incident exercises (simulate partial failures, measure decision latency and quality); shadow-mode policy testing (apply proposed rules to historical incidents, evaluate outcomes).

**Interviews**: SRE teams (operational feasibility), clients (availability vs. security preferences), regulators (acceptable degraded-state behavior).

---

### 9. Revising the Answer

**Likely revisions**: Initial time/volume limits may prove too restrictive or too permissive; client segmentation may require more granular tiers; monitoring thresholds may need tuning to reduce false alarms.

**Incremental approach**: Start with conservative degraded-mode policies; gradually expand based on incident experience; maintain manual override paths for truly exceptional circumstances with post-incident review.

---

### 10. Summary & Action Recommendations

**Core insights**:
1. **Tier-based degraded modes balance liveness and security**: Critical assets remain offline; standard assets continue with time/volume limits and enhanced monitoring.
2. **Transparency and client communication are critical**: Notify clients of degraded state promptly; explain risk changes clearly to maintain trust.
3. **Automated monitoring during degraded periods**: Enhanced anomaly detection (unusual transaction patterns, velocity, counterparties) compensates for reduced quorum security.

**Near-term actions** (0–3 months):

| Priority | Action | Owner | Expected Result | Target Date |
|----------|--------|-------|-----------------|-------------|
| **P0** | Define tier-based degraded-mode policies (asset value thresholds, time limits, volume caps) | Security Lead + Risk Team | Policy document approved by compliance, product, and security; clear escalation paths | Month 1, Week 2 |
| **P0** | Implement automated health monitoring and degraded-state detection | SRE Lead | Monitoring system detects partial failures within <5 minutes; triggers alerts and policy enforcement | Month 2, Week 2 |
| **P1** | Build anomaly detection for degraded-mode signing (unusual patterns, velocity) | Data Engineer + Security | Monitoring dashboard; alerts triggered for suspicious activity during degraded periods | Month 3, Week 2 |
| **P1** | Create client notification templates and communication playbooks for degraded states | Product + Compliance | Templates approved; ops teams trained; test notifications sent to willing pilot clients | Month 2, Week 4 |
| **P1** | Conduct table-top incident exercises simulating partial failures | Security + SRE Teams | Team demonstrates competency in executing degraded-mode policies; gaps identified and addressed | Month 3, Week 4 |

**Risks**:
- **Degraded-mode policies too restrictive**: Frequent outages drive client frustration → Monitor downtime metrics; adjust time limits if SLAs violated.
- **Blast radius underestimated**: More assets at risk in degraded mode than anticipated → Conduct thorough AUM analysis; enforce stricter tier thresholds.
- **Failure clustering**: Multiple domains fail simultaneously, exceeding degraded-mode capacity → Design for geographic and vendor diversity; maintain hot-standby capacity.

---


## Problem 6: Migration from Legacy Custody to MPC Wallet

### Context Recap

**Problem**: Design migration mechanism that moves existing clients' assets, policies, and operational runbooks from single-sig/HSM custody into MPC-based key management, minimizing service interruptions and perceived risk while providing clear rollback paths.

**Key Context**:
- Current situation: Target clients operate mature HSM or multisig setups with own approval processes, audit trails, regulator familiarity; previous finance tech migrations have failed due to abrupt cutovers or indefinite shadow systems
- Main pain points: Need to move >70–80% of balances within 12–24 months, keep incident rates below baseline, maintain auditor/regulator confidence, shorten PoC-to-full-migration from months to 6–12 weeks per client
- Goals: High migration success rate, incident-free transition, reduced time-to-value, clear rollback capability
- Hard constraints: Limited implementation/onboarding capacity, clients' change-management processes, vendor lock-in concerns, compatibility between legacy and MPC policy models, avoid dual-control complexity
- Critical background: Migration spans 6–24 months per major client, affecting large asset books and daily workflows; failed migration can permanently damage trust, result in lost business, or trigger regulatory scrutiny

---

### 1. Problem Definition

**Core contradiction**: Migration must be **fast enough** to capture market opportunity and avoid prolonged dual-system complexity, yet **safe enough** to avoid service disruptions, data loss, or security regressions that would damage client trust.

**Involved parties**: Sales/account teams (managing expectations), solution architects/engineers (designing playbooks), custody ops (executing dual-run), risk/compliance (validating controls), client-side security/ops (signing off).

**Key tensions**:
- **Speed vs. Safety**: Aggressive migration timelines reduce dual-system overhead but increase risk of overlooked edge cases or integration issues
- **Standardization vs. Customization**: Standardized playbooks enable scale but may not accommodate client-specific policies, approval workflows, or regulatory requirements
- **Transparency vs. Confidence**: Openly discussing migration risks builds trust but may trigger client hesitation; downplaying risks erodes trust if issues emerge

---

### 2. Internal Logical Relations

**Migration phases**:
1. **Discovery**: Map client's existing custody setup, policies, approval workflows, audit requirements
2. **Design**: Translate legacy policies to MPC policy model; identify gaps and workarounds
3. **Parallel run**: Operate both legacy and MPC systems side-by-side; validate equivalence
4. **Cutover**: Gradually shift flows from legacy to MPC (10% → 50% → 100% over weeks/months)
5. **Decommission**: Sunset legacy system once MPC proven stable

**Balance points**:
- **Too fast** → inadequate validation → service disruptions → trust damage
- **Too slow** → prolonged dual-system complexity → operational burden, confusion about authority
- **Sweet spot**: Phased migration with clear go/no-go gates, parallel-run validation, and rapid rollback capability

---

### 3. External Connections

**Stakeholders**: Institutional clients (own legacy systems, bear migration risk), regulators (assess control continuity), auditors (validate new controls), competing custody providers (may offer alternative migration paths).

**Environment**: Regulatory expectations for custody transitions (e.g., notification timelines, control handoff documentation); market pressure (clients demand MPC features but fear disruption).

**Responsibility**: Team must own migration playbook, client communication, and incident response; leave room for client-specific timing and risk appetites.

---

### 4. Origins

**Historical evolution**: Early MPC deployments were greenfield (new clients only); as product matures, growth requires migrating existing large clients from legacy systems; initial migrations were ad-hoc and time-consuming (4–6 months per client).

**Background factors**: Lack of standardized migration playbook; insufficient tooling for policy translation and validation; unclear ownership of migration risk.

**Direct triggers**: Major client prospect demanded <8-week migration timeline; existing ad-hoc approach couldn't scale; sales pipeline bottlenecked on migration capacity.

---

### 5. Problem Trends

**If nothing changes**: Migration timelines will remain long and unpredictable; client pipeline will stall; competitors with better migration experiences will win deals; team will burn out handling bespoke migrations.

**Signals**: Increasing migration project timelines (4 months → 6 months → 8 months); rising client pushback during discovery/design phases; growing backlog of migration-ready clients waiting for capacity.

**Scenarios**: Baseline (60%): Migrations continue ad-hoc, throughput limited, market share lost to competitors; Pessimistic (15%): Major migration failure (data loss, prolonged outage) damages reputation and triggers client exodus.

---

### 6. Capability Reserves

**Strengths**: Solution architects understand both legacy and MPC systems; ops teams have dual-run experience from previous migrations; strong client relationships enable collaboration during transition.

**Gaps**: No standardized migration playbook or policy-translation toolkit; limited automation for data migration and validation; insufficient capacity to handle multiple concurrent migrations.

**Near-term builds**: Migration playbook with phase gates, policy-translation tools, automated testing framework for parallel-run validation, dedicated migration project management.

---

### 7. Analysis Outline

**Problem**: Migrate clients from legacy custody to MPC without disruption or trust damage.

**Options**:
- **A**: Big-bang cutover (fast, high risk of disruption)
- **B**: Indefinite parallel run (safe but operationally complex and confusing)
- **C**: Phased migration with time-bounded parallel run (balanced approach)

**Recommendation**: Option C — phased migration with 4-6 week parallel-run validation, clear go/no-go gates at each phase, and rapid rollback capability if issues arise.

---

### 8. Validating the Answer

**Required data**: Historical migration timelines and incident rates, client satisfaction scores, operational overhead of parallel-run periods.

**Experiments**: Pilot migration with willing client; measure actual timeline, incident count, and client satisfaction; refine playbook based on lessons learned.

**Interviews**: Clients who have migrated (what worked, what was painful), solution architects (common pitfalls), auditors (control validation requirements).

---

### 9. Revising the Answer

**Likely revisions**: Initial timeline estimates (6–12 weeks) may prove optimistic for complex clients with heavily customized policies; parallel-run duration may need extension if equivalence validation reveals edge cases.

**Incremental approach**: Start with simpler clients (standard policies, smaller AUM); refine playbook and tooling; gradually tackle more complex clients.

---

### 10. Summary & Action Recommendations

**Core insights**:
1. **Phased migration with parallel-run validation is safest path**: Gradual cutover (10% → 50% → 100%) with validation at each gate prevents large-scale disruptions.
2. **Policy translation is critical bottleneck**: Legacy approval rules must be accurately mapped to MPC policy model; automated translation tools can accelerate this and reduce errors.
3. **Clear rollback capability builds client confidence**: Knowing they can quickly revert to legacy system if issues arise reduces client hesitation and enables faster decision-making.

**Near-term actions** (0–3 months):

| Priority | Action | Owner | Expected Result | Target Date |
|----------|--------|-------|-----------------|-------------|
| **P0** | Create standardized migration playbook with phase gates and go/no-go criteria | Solutions Architecture Lead | Playbook document covering discovery, design, parallel run, cutover, decommission phases | Month 1, Week 2 |
| **P0** | Build policy-translation toolkit to map legacy rules to MPC policy model | Engineering Lead | Tool operational; reduces policy-mapping time from weeks to days; validation tests included | Month 2, Week 4 |
| **P1** | Pilot migration with 1–2 willing clients following new playbook | Migration PM + Solutions Architect | Migration complete; timeline, incidents, and client satisfaction measured; playbook refined | Month 3, Week 4 |
| **P1** | Develop automated parallel-run validation framework (compare legacy vs MPC outputs) | QA Engineer | Framework operational; automatically flags discrepancies during parallel run; reduces manual validation effort | Month 3, Week 2 |
| **P2** | Create client communication templates for each migration phase | Product + Account Teams | Templates covering discovery kickoff, design review, parallel-run start, cutover notifications, decommission confirmation | Month 2, Week 2 |

**Risks**:
- **Policy translation errors**: Mism apped rules could cause inappropriate approvals or blocks → Require client sign-off on translated policies; run parallel validation for extended period.
- **Client change-management delays**: Internal client approvals slow migration progress → Build buffer time into schedules; offer consulting support for client-side change process.
- **Parallel-run operational burden**: Running dual systems stresses ops teams → Automate validation where possible; time-bound parallel-run periods; hire temporary ops capacity if needed.

---


## Problem 7: Incident Response for Compromised MPC Shares

### Context Recap

**Problem**: Detect, analyze, and respond to partial key-share exposure events, preventing full key reconstruction or unauthorized signing while meeting strict timelines for service restoration and regulatory/contractual notifications.

**Key Context**:
- Current situation: Scenario analyses show attackers may exfiltrate memory/disk from MPC nodes without immediate fraud; teams uncertain about key-risk assessment; regulated environments require 72-hour notifications even without fund movement
- Main pain points: Need containment within <1–2 hours of detection, rotation completed within <4–8 hours, maintained/restored signing for unaffected tiers, zero/minimal realized losses, timely regulator/client notifications
- Goals: Fast containment, safe rotation, maintained service for unaffected flows, compliant notifications, documented lessons learned
- Hard constraints: Complexity of distributed key refresh/PSS protocols, risk of introducing new vulnerabilities during emergency procedures, limited on-call/forensic capacity, fixed external notification timelines (SOC 2, GDPR-like)
- Critical background: While individual incidents unfold over hours/days, design of runbooks, monitoring, and rotation must support years of continuous operation; single mishandled event could cause permanent reputation damage, regulatory sanctions, or large client departures

---

### 1. Problem Definition

**Core contradiction**: Response must be **fast enough** to contain exposure before attackers can orchestrate multi-party collusion to reconstruct keys, yet **careful enough** to avoid introducing new vulnerabilities or disrupting legitimate flows during emergency procedures.

**Involved parties**: Security ops/IR teams, cryptographers (designing refresh), SREs (executing isolation/redeployment), compliance/legal (managing notifications), clients (assets at stake).

**Key tensions**:
- **Speed vs. Safety**: Rushing refresh protocol may introduce implementation bugs or skip validation steps; delaying allows potential attacker advantage
- **Service Continuity vs. Risk Mitigation**: Maintaining signing during rotation exposes remaining shares to observation; pausing signing disrupts legitimate business
- **Transparency vs. Panic**: Immediate client notification maintains trust but may trigger unnecessary withdrawals; delayed notification risks regulatory penalties and trust erosion if discovered

---

### 2. Internal Logical Relations

**Incident phases**:
1. **Detection**: Monitoring alerts on anomalous access, telemetry, or third-party notification
2. **Assessment**: Determine which shares potentially exposed; evaluate blast radius
3. **Containment**: Isolate affected nodes; revoke network access; preserve forensic evidence
4. **Rotation**: Execute distributed key refresh or re-key protocol; validate new shares
5. **Notification**: Inform regulators, auditors, affected clients per timelines and severity
6. **Lessons learned**: Post-incident review; update runbooks and monitoring

**Balance points**:
- **Too fast** (panic response) → introduce new bugs, skip validation, disrupt service unnecessarily
- **Too slow** (analysis paralysis) → allow attackers time to coordinate, miss notification deadlines, lose client trust
- **Sweet spot**: Pre-scripted runbooks with clear decision trees, automated containment where possible, rapid but validated rotation, and templated communication

---

### 3. External Connections

**Stakeholders**: Regulators (notification requirements), clients (want immediate transparency and zero loss), forensic experts (may assist investigation), cloud/HSM vendors (may be involved in compromise).

**Environment**: Threat landscape (sophistication of attackers, common attack vectors); regulatory frameworks (notification windows, documentation requirements); insurance providers (coverage conditions).

**Responsibility**: Team must own incident detection, containment, and rotation; leave room for external expertise (forensic consultants, regulator guidance) without creating communication bottlenecks.

---

### 4. Origins

**Historical evolution**: Early designs assumed MPC node compromise would be immediately detected via fraud; realization that attackers may exfiltrate shares silently drove need for proactive monitoring and rotation capabilities.

**Background factors**: Insufficient telemetry for detecting subtle compromises; lack of tested key-refresh procedures; unclear notification obligations and templates.

**Direct triggers**: Industry incident (peer custody provider experienced partial compromise); internal red-team exercise revealed gaps in detection and response capabilities; auditor flagged lack of documented IR runbooks.

---

### 5. Problem Trends

**If nothing changes**: Detection will remain reactive (wait for fraud); response will be ad-hoc and slow; clients and regulators will lose confidence in platform's ability to handle incidents.

**Signals**: Increasing industry compromise reports; growing regulatory scrutiny of custody IR capabilities; client questions about "what would you do if..." scenarios during sales cycles.

**Scenarios**: Baseline (70%): System operates without major incident but gaps remain; minor incidents reveal response inadequacy; Pessimistic (10%): Major compromise with slow/mishandled response causes large losses and regulatory sanctions.

---

### 6. Capability Reserves

**Strengths**: Security ops team has general IR experience; cryptographers understand key-refresh protocols; existing MPC infrastructure supports re-keying.

**Gaps**: No tested end-to-end IR runbook for share compromise; limited automated containment; no pre-approved communication templates; unclear decision authority during incidents.

**Near-term builds**: IR runbook with decision trees, automated containment playbooks, notification templates (by severity level), regular IR drills/table-tops.

---

### 7. Analysis Outline

**Problem**: Respond to partial key-share exposure without full key reconstruction or service disruption.

**Options**:
- **A**: Manual ad-hoc response (flexible but slow, error-prone)
- **B**: Fully automated response (fast but may overreact or fail on edge cases)
- **C**: Scripted runbook with human gate-keeping (balanced approach)

**Recommendation**: Option C — pre-scripted containment and rotation procedures with human decision points for service-continuity and notification trade-offs.

---

### 8. Validating the Answer

**Required data**: Historical incident timelines (how long did detection, assessment, containment take?); blast-radius models (which assets at risk in various compromise scenarios); regulatory notification obligations (timelines, content requirements).

**Experiments**: Table-top IR exercises simulating various compromise scenarios; measure team response time and decision quality; identify gaps in runbooks, tooling, or authority.

**Interviews**: Security ops teams (runbook usability), legal/compliance (notification requirements), clients (transparency expectations), peer platforms (lessons from real incidents).

---

### 9. Revising the Answer

**Likely revisions**: Initial containment timelines (1–2 hours) may prove optimistic if compromise detection is delayed or forensic analysis is complex; rotation timelines (4–8 hours) may need extension if distributed refresh protocol encounters issues.

**Incremental approach**: Start with conservative response (full containment, extended rotation validation); over time, develop confidence to maintain service for unaffected tiers during rotation.

---

### 10. Summary & Action Recommendations

**Core insights**:
1. **Pre-scripted runbooks with decision trees enable fast, safe response**: Clear procedures for detection, assessment, containment, rotation, and notification reduce decision latency and error risk during high-pressure incidents.
2. **Automated containment reduces response time**: Scripted isolation of suspected-compromised nodes (network segmentation, access revocation) can execute in minutes vs. hours of manual coordination.
3. **Transparent, timely client communication preserves trust**: Even when no funds are lost, clients appreciate being informed promptly and clearly about incidents and response actions.

**Near-term actions** (0–3 months):

| Priority | Action | Owner | Expected Result | Target Date |
|----------|--------|-------|-----------------|-------------|
| **P0** | Create comprehensive IR runbook for key-share compromise scenarios | Security Lead + Cryptography Team | Runbook covering detection, assessment, containment, rotation, notification phases with decision trees | Month 1, Week 2 |
| **P0** | Implement automated containment playbooks (isolate nodes, revoke access) | Security + SRE Teams | Playbooks operational; can execute containment in <10 minutes from detection alert | Month 2, Week 2 |
| **P1** | Develop notification templates for various incident severity levels | Compliance + Legal Teams | Templates approved by legal; cover regulator, auditor, and client notifications per severity (low/medium/high) | Month 1, Week 4 |
| **P1** | Conduct table-top IR exercise simulating key-share compromise | Security + SRE + Compliance Teams | Exercise complete; team demonstrates competency; gaps identified and addressed in runbook | Month 3, Week 2 |
| **P1** | Implement telemetry and alerting for anomalous MPC node behavior | Security + SRE Teams | Monitoring dashboard; alerts for unusual access patterns, performance anomalies, telemetry gaps | Month 2, Week 4 |

**Risks**:
- **Detection delays**: Subtle compromises may evade monitoring → Invest in behavioral anomaly detection; conduct regular red-team exercises to test detection.
- **Rotation introduces instability**: Key refresh protocol bugs could disrupt service → Thoroughly test refresh procedures in staging; maintain rollback capability.
- **Communication missteps**: Poorly worded notifications could trigger client panic or regulator scrutiny → Pre-approve templates with legal; train teams on communication protocols.

---


## Problem 8: SDK and Service Offering for External Developers

### Context Recap

**Problem**: Package MPC wallet capabilities into SDK and service with clear security guarantees, integration paths, and pricing models so external teams (exchanges, DeFi protocols, startups) can adopt quickly without weakening their security posture or making economics unworkable.

**Key Context**:
- Current situation: Internal MPC infrastructure built for single custody product; now pressure to expose as SDK to multiple segments (institutional custody, DeFi, early-stage apps) with very different AUM, integration capabilities, and audit tolerances
- Main pain points: Poorly aligned pricing (e.g., high per-signature charges) can drive risky behavior or low adoption; need to enable typical startup integration in <1 week, institutional clients to meet audit requirements, reach target revenue/adoption metrics
- Goals: Enable fast integration (<1 week for startups, audit-ready for institutions), reach hundreds/thousands of developers and several million $ ARR within 1–2 years, avoid incentivizing security bypasses
- Hard constraints: Limited documentation/DevRel bandwidth, need strict tenant separation in shared MPC infrastructure, finite capacity for custom features/audits per client, challenge of pricing that works for both small and large AUM
- Critical background: SDK design and pricing decisions influence platform ecosystem and revenue mix over 2–4 years, affecting dozens to hundreds of partner projects and indirectly security of end users

---

### 1. Problem Definition

**Core contradiction**: SDK must be **simple enough** to enable rapid integration by small teams with limited crypto expertise, yet **secure and flexible enough** to meet institutional audit and customization requirements without creating unsustainable engineering burden.

**Involved parties**: Platform/SDK engineers, security architects, product/business owners, sales/account teams, external developer teams integrating SDK, their security/compliance counterparts.

**Key tensions**:
- **Simplicity vs. Flexibility**: Simple "one size fits all" SDK is easy to integrate but may not support institutional policy customization; highly flexible SDK has steep learning curve
- **Pricing for Volume vs. AUM**: Per-signature pricing works for low-volume users but penalizes high-frequency traders; AUM-based pricing works for institutional custody but doesn't fit DeFi protocols or gaming apps
- **Shared Infrastructure vs. Isolation**: Multi-tenant MPC backend reduces cost but introduces blast-radius concerns if not strictly isolated

---

### 2. Internal Logical Relations

**Key elements**:
- **SDK tiers**: Free/dev tier (low volume, standard features), startup tier (moderate volume, community support), institutional tier (high volume/AUM, custom features, dedicated support)
- **Integration paths**: Quick-start (API-only, minimal crypto exposure), advanced (custom policy engine, direct MPC protocol access)
- **Pricing dimensions**: Per-signature fees, AUM-based subscription, volume commitments, custom enterprise contracts

**Balance points**:
- **Too simple** → doesn't meet institutional requirements → limits addressable market to small players
- **Too complex** → slows integration → high drop-off rate → fails to reach adoption targets
- **Sweet spot**: Tiered approach where dev/startup tiers prioritize simplicity and standard features, institutional tier offers customization and audit support

---

### 3. External Connections

**Stakeholders**: External developers (vary in size, expertise, risk appetite), their end users (bear security risk of poor SDK integration), competing MPC SDK providers (set market expectations for pricing and features).

**Environment**: Developer ecosystem trends (preference for simple REST APIs vs. complex cryptographic libraries); investor/auditor scrutiny of crypto custody practices.

**Responsibility**: Team must own SDK documentation, developer support, and security defaults; leave room for client-specific customizations without creating un-auditable complexity or operational burden.

---

### 4. Origins

**Historical evolution**: MPC infrastructure originally internal-only; early partner integrations were bespoke and time-consuming; as demand grew, need for standardized SDK became clear.

**Background factors**: Limited DevRel/documentation resources; unclear market segmentation (treat all clients the same vs. tiered approach); no established pricing models in nascent MPC SDK market.

**Direct triggers**: Multiple inbound requests from exchanges and DeFi protocols; realization that bespoke integrations don't scale; competitive pressure from other MPC providers launching SDK offerings.

---

### 5. Problem Trends

**If nothing changes**: Partner integrations will remain slow and bespoke; team will bottleneck on custom work; addressable market will be limited to few large clients willing to pay for customization; competitors will capture developer ecosystem.

**Signals**: Growing backlog of integration requests; increasing time-per-integration; partner complaints about unclear pricing and unclear security guarantees.

**Scenarios**: Baseline (60%): SDK eventually launches but adoption is slow due to complexity or pricing issues; revenue/developer targets missed; Optimistic (30%): Well-designed SDK gains viral adoption, becomes platform growth flywheel.

---

### 6. Capability Reserves

**Strengths**: Strong core MPC infrastructure; security expertise; successful internal product deployment demonstrates viability.

**Gaps**: Limited DevRel and documentation capacity; no tiered product/pricing experience; insufficient tooling for tenant isolation and monitoring.

**Near-term builds**: SDK with tiered features, comprehensive documentation and quick-start guides, developer dashboard for monitoring and debugging, pricing calculator/simulator.

---

### 7. Analysis Outline

**Problem**: Package MPC wallet as SDK for external developers with appropriate security, simplicity, and pricing.

**Options**:
- **A**: Single-tier SDK (simple but limited flexibility, may not meet institutional needs)
- **B**: Fully customizable SDK (meets all needs but complex and slow to integrate)
- **C**: Tiered SDK (dev/startup tier simple, institutional tier flexible) — Recommended

**Recommendation**: Option C — tiered approach with clear upgrade paths, tiered pricing (free dev tier, per-signature or volume-based for startups, AUM-based for institutions).

---

### 8. Validating the Answer

**Required data**: Developer survey (integration time expectations, pricing sensitivity, feature priorities); competitive analysis (other MPC SDK pricing and features); pilot integration timelines and drop-off points.

**Experiments**: Beta SDK with 5–10 partner integrations; measure time-to-first-signature, drop-off rate, feature requests; iterate on documentation and API design.

**Interviews**: Potential SDK users (exchanges, DeFi protocols, startups) about integration pain points and pricing expectations; sales team about deal dynamics and common objections.

---

### 9. Revising the Answer

**Likely revisions**: Initial pricing models may need adjustment based on market feedback; feature tier boundaries may shift as patterns emerge; integration time estimates (< 1 week) may prove optimistic for complex use cases.

**Incremental approach**: Launch with simple dev tier and one or two pilot institutional clients; gather feedback; iterate on features, documentation, and pricing before broad launch.

---

### 10. Summary & Action Recommendations

**Core insights**:
1. **Tiered SDK balances simplicity and flexibility**: Dev/startup tier prioritizes fast integration with standard features; institutional tier offers customization and audit support.
2. **Pricing must align incentives**: Avoid per-signature pricing that penalizes high-frequency use; instead use tiered subscriptions (free dev, volume-based startup, AUM-based institutional) to align with customer value.
3. **Security defaults prevent foot-guns**: SDK should make secure integration the "path of least resistance" (e.g., default to requiring approvals for high-value transactions, make rate limits easy to configure).

**Near-term actions** (0–3 months):

| Priority | Action | Owner | Expected Result | Target Date |
|----------|--------|-------|-----------------|-------------|
| **P0** | Define tiered SDK feature matrix and pricing models (dev, startup, institutional tiers) | Product + Business Team | Product spec with clear feature boundaries and pricing; approved by engineering, sales, and finance | Month 1, Week 2 |
| **P0** | Build MVP SDK with dev tier features and comprehensive quick-start documentation | Engineering Lead | SDK functional; quick-start guide enables integration in <1 week; public API docs published | Month 2, Week 4 |
| **P1** | Onboard 3–5 beta partners (mix of startups and institutional prospects) | DevRel + Sales Teams | Beta integrations complete; feedback collected on documentation, API design, and pricing; iteration priorities identified | Month 3, Week 4 |
| **P1** | Implement developer dashboard for monitoring usage, debugging, and billing | Engineering + Product Teams | Dashboard operational; developers can self-serve for common tasks (key management, transaction history, rate limit configuration) | Month 3, Week 2 |
| **P2** | Create pricing calculator and comparison tool for developers to estimate costs | Product + Marketing Teams | Calculator published; helps developers understand pricing before committing; reduces sales friction | Month 2, Week 2 |

**Risks**:
- **Slow integration adoption**: If integration complexity or unclear value prop limits uptake → Invest heavily in documentation, example code, video tutorials; offer free integration consulting for early adopters.
- **Pricing model misalignment**: If pricing drives unwanted behavior (e.g., batching to avoid per-signature fees) → Monitor usage patterns; adjust pricing to align with value delivered.
- **Security incidents from poor SDK usage**: If developers misconfigure or misuse SDK, exposing their users → Invest in secure defaults, validation, and monitoring; provide security review checklist for institutional users.

---

