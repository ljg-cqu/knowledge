# Cross-Cloud Deployment Operational Complexity – Nine-Aspects Analysis

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: DevOps Team

---

## Context Recap

- **Problem title**: Cross-cloud MPC deployment operational complexity and cost
- **Current state**:
  - MPC wallet and privacy-preserving analytics providers increasingly deploy key shares or aggregators across multiple clouds (AWS, Azure, Google Cloud) to gain strong trust separation and defense in depth.  
    [Source: "The Deployment Dilemma: Merits & Challenges of Deploying MPC", UC Berkeley Security Group & collaborators, accessed 2025-11-29, https://mpc.cs.berkeley.edu/blog/deployment-dilemma.html]
  - Each cloud exposes different confidential-computing primitives and attestation models: AWS Nitro Enclaves (enclave as a special VM offshoot), Azure Intel SGX (application-level enclave), Google Confidential VMs based on AMD SEV/SEV-SNP (VM/kernel-level protection).  
    [Source: AWS Nitro Enclaves documentation, accessed 2025-11-29, https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html]  
    [Source: "Azure confidential computing" overview, Microsoft Learn, accessed 2025-11-29, https://learn.microsoft.com/azure/confidential-computing/overview]  
    [Source: "Confidential Computing", Google Cloud, accessed 2025-11-29, https://cloud.google.com/confidential-computing]
  - Cross-cloud network egress is priced per GiB (internet-style pricing) and is significantly more expensive than intra-region traffic: typical public internet egress falls around $0.08–$0.12/GB for first tens of TB on AWS, Azure, and Google Cloud.  
    [Source: "AWS Data Transfer Charges for Server and Serverless Architectures", AWS APN Blog, accessed 2025-11-29, https://aws.amazon.com/blogs/apn/aws-data-transfer-charges-for-server-and-serverless-architectures/]  
    [Source: "AWS Egress Costs Explained: How To Reduce Spend", CloudZero, accessed 2025-11-29, https://www.cloudzero.com/blog/aws-egress-costs/]  
    [Source: "Azure Egress Costs: What You Should Know", DigitalOcean, accessed 2025-11-29, https://www.digitalocean.com/resources/articles/azure-egress-costs]  
    [Source: "Network pricing", Google Cloud VPC, accessed 2025-11-29, https://cloud.google.com/vpc/network-pricing]
- **Pain points**:
  - 3x+ development and DevOps effort to support three different enclave stacks, attestation mechanisms, deployment pipelines, and monitoring stacks.  
    [Source: Berkeley MPC blog – section "It’s n times the work!", accessed 2025-11-29, https://mpc.cs.berkeley.edu/blog/deployment-dilemma.html]
  - Cross-cloud MPC traffic introduces higher latency and non-trivial egress bills compared with intra-cloud topologies; ENPA and similar deployments report significantly higher latency and egress fees for cross-cloud communication.  
    [Source: Berkeley MPC blog – section "MPC in the clouds", accessed 2025-11-29]
  - Enterprise customers perceive multi-cloud MPC as complex and risky to operate, which delays or blocks deployments.
- **Goals**:
  - Reduce effective development/operations effort from ~3x per cloud to ≤1.5x (minimum) and ideally near 1.2x versus single-cloud baseline.
  - Maintain or improve security guarantees (trust separation, defense-in-depth) while reducing egress spend for a reference workload of 1M MPC transactions/month from ~2–5x single-cloud levels toward <$200–$500/month where feasible.  
    [Estimate: Derived from 10–50 KB per transaction and public egress price tables; medium confidence]
  - Provide a unified deployment, attestation, and observability experience for engineers and security teams by Q4 2025.
- **Hard constraints**:
  - Cannot change fundamental enclave differences (Nitro vs SGX vs AMD SEV) or underlying provider pricing models.
  - Must preserve application-level or equivalent attestation rigor (Signal-level bar) and reproducible builds.  
    [Source: Berkeley MPC blog – Signal discussion of reproducible builds and attestation]
  - Must support brownfield migration from existing single-cloud deployments without prolonged downtime.
- **Key facts**:
  - Multi-cloud MPC deployments (e.g., Signal, ISRG ENPA) confirm that operating across enclaves and clouds is currently a foremost obstacle and “n times the work for n MPC parties”.  
    [Source: Berkeley MPC blog, accessed 2025-11-29]
  - Generic multi-cloud tools like Terraform/Pulumi abstract basic infrastructure but do not hide enclave-specific attestation and lifecycle complexity.  
    [Source: Berkeley MPC blog; Terraform/Pulumi docs, accessed 2025-11-29]

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem & contradictions

- **Core problem**: How to deploy and operate MPC wallet infrastructure across multiple cloud providers to achieve strong trust separation **without** incurring prohibitive development overhead, operational fragility, and egress costs.
- **Key contradictions**:
  - **Security vs. Complexity**: Stronger trust separation (multi-cloud, heterogeneous enclaves) increases both implementation and operational complexity; single-cloud enclaves or pure cryptographic MPC offer simpler ops but weaker infrastructure diversity.  
    [Source: Berkeley MPC blog – security motivations for multi-cloud; Google & AWS confidential-computing docs]
  - **Standardization vs. Differentiation**: Cloud vendors intentionally differentiate enclave offerings (Nitro vs SGX vs Confidential VMs); customers want a unified abstraction and tooling layer.  
    [Source: AWS Nitro, Azure confidential computing, Google Confidential Computing docs]
  - **Cost vs. Latency vs. Privacy**: Cross-cloud network paths increase latency and egress cost, but keeping all parties intra-cloud weakens the independence of failure domains.  
    [Source: Berkeley MPC blog – ENPA experience on latency and egress; Google VPC pricing]
- **Problem statement**:
  - Given the need to run MPC parties across independent clouds for regulatory or security reasons, the team must design a **multi-cloud deployment, attestation, and observability architecture** that minimizes incremental effort and cost while maintaining strong security guarantees.

### 1.2 Goals & conditions

- **Development & operations effort**:
  - Baseline: ~3x per-cloud effort relative to a single-cloud enclave deployment (separate attestation flows, pipelines, and monitoring).  
    [Source: Berkeley MPC blog – "It’s n times the work"]
  - **Minimum acceptable**: ≤1.5x incremental cross-cloud overhead by Q4 2025.
  - **Target**: ≤1.2x overhead with strong reuse across providers.
- **Cost & performance**:
  - Baseline egress: cross-cloud data at $0.08–$0.12/GB; 1M tx/month × (10–50 KB per tx) ≈ 10–50 GB/month of cross-cloud traffic → ~$1–$6/GB ranges yield $0.8–$6k/month depending on routing and overhead.  
    [Estimate: Derived from CloudZero, DigitalOcean Azure, and Google VPC pricing tables]
  - **Minimum acceptable**: < $500/month egress for reference workload.
  - **Target**: <$200/month, keeping 95th percentile latency within acceptable thresholds (e.g., <500–700 ms end-to-end for signing).  
    [Estimate: Latency target based on interactive UX norms; low confidence]
- **Security & compliance**:
  - Maintain at least two-layer defense-in-depth: MPC cryptography + confidential-computing hardware; design to remain safe if any single enclave platform is compromised.  
    [Source: Berkeley MPC blog – perspectival shift on enclaves; Google Confidential Computing overview]
  - Preserve reproducible builds and verifiable attestation for deployed code.  
    [Source: Berkeley MPC blog – Signal reproducible builds]

### 1.3 Extensibility & reframing

- **Reframing 1 – From “cross-cloud or single-cloud” to “configurable trust tiers”**:
  - Define deployment modes: (A) single-cloud multi-enclave, (B) dual-cloud, (C) triple-cloud, with clear security vs. cost trade-offs and migration paths.
- **Reframing 2 – From “rewrite for each enclave” to “enclave capability profiles”**:
  - Treat Nitro, SGX, and Confidential VMs as profiles with explicit capabilities (attestation granularity, memory limits, I/O model); generate per-provider glue from a shared high-level spec.
- **Reframing 3 – From “raw cross-cloud traffic” to “optimized MPC transport layer”**:
  - Introduce a layer that compresses, batches, and routes messages to minimize paid egress (e.g., by co-locating heaviest traffic within a single cloud and limiting cross-cloud payloads to minimal shares or commitments).  
    [Source: Common MPC architecture patterns discussed in Berkeley MPC blog; industry MPC wallet architectures]

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key internal elements

- **Core elements**:
  - MPC protocol implementation (threshold signing, aggregation, etc.).
  - Enclave runtimes on each provider (Nitro Enclaves, SGX applications, Confidential VMs/nodes).
  - CI/CD and attestation pipeline (build, sign, verify, deploy per cloud).
  - Network fabric and MPC transport layer (intra- vs cross-cloud routing, batching, encryption).
  - Observability stack (metrics, logs, traces, security events) across clouds.
  - Cost telemetry (per-cloud egress and compute metering).
- **Relationships**:
  - Build artifacts feed into per-cloud enclave images and attestation bundles.
  - MPC transport layer orchestrates communication among enclaves and drives both latency and egress cost.
  - Observability and cost telemetry close the loop, feeding data back into topology and parameter decisions.

### 2.2 Balance & "degree"

- **Balance dimensions**:
  - **Security vs. engineering throughput**: Additional enclave hardening and cross-cloud separation improves security but slows feature delivery.
  - **Standardization vs. low-level tuning**: A high-level abstraction makes cross-cloud support feasible but can obscure provider-specific optimizations.
  - **Cost vs. redundancy**: More clouds and availability zones improve resilience but increase fixed and variable spend.
- **Optimal ranges (illustrative)**:
  - 60–70% of enclave-specific code paths autogenerated from shared templates; ≤30–40% hand-written per provider.
  - 70–80% of MPC messages kept intra-cloud; 20–30% cross-cloud for critical protocol steps only.  
    [Estimate: Heuristic based on typical MPC communication patterns]

### 2.3 Causal chains

- **Chain 1 – Enclave heterogeneity → duplicate tooling → operational fragility**:
  1. Providers expose different attestation APIs and enclave lifecycle models (Nitro vs SGX vs SEV).  
     [Source: AWS Nitro Enclaves, Azure confidential computing, Google Confidential VMs docs]
  2. Teams maintain separate scripts and pipelines per cloud.
  3. Divergence accumulates over time; bugs and security patches are not applied uniformly.
  4. Incidents become harder to diagnose because behavior differs subtly across platforms.
- **Chain 2 – Cross-cloud routing → egress & latency → user-perceived reliability**:
  1. Key-share communication crosses cloud boundaries over the public internet or interconnects.
  2. Each GB of traffic incurs egress cost tiers in each cloud plus added network hops.  
     [Source: AWS APN data-transfer blog; Azure bandwidth pricing; Google VPC network pricing]
  3. Latency spikes and cost overruns degrade SLAs and margins.
  4. Product teams are pressured to “turn off” multi-cloud mode for cost or latency reasons, undermining trust separation.

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder landscape

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| **Upstream** | Cloud providers (AWS, Azure, Google) | Differentiate confidential-computing offerings, drive workload adoption | Preserve proprietary enclave models; limited incentive to standardize APIs | Customers need standardization, not fragmentation |
| **Upstream** | Hardware vendors (Intel, AMD) | Advance SGX/TDX, SEV/SEV-SNP capabilities | Roadmaps tied to CPU cycles; side-channel mitigations evolve slowly | Application teams must keep up with microarchitectural changes |
| **Downstream** | MPC wallet providers & privacy service operators | Offer secure multi-cloud wallets and analytics with strong guarantees | Limited security engineering headcount; high integration cost | May underinvest in enclave rigor or multi-cloud to ship faster |
| **Downstream** | Enterprise customers / regulators | Trust-separation across clouds, clear attestation evidence, cost predictability | Risk-averse, constrained by compliance; limited appetite for operational complexity | Suspicion toward opaque, complex multi-cloud architectures |
| **Sideline** | Tooling vendors (IaC, observability, cost platforms) | Provide abstraction for infra, monitoring, and cloud spend | Limited enclave-specific functionality today | Missed opportunity to support MPC-specific needs |

### 3.2 Environment & policy factors

- **Regulation and compliance**:
  - Data residency, key management, and sectoral regulations (e.g., financial custody, healthcare) often **encourage or mandate separation of control domains**, making multi-cloud MPC attractive.  
    [Source: Industry MPC wallet whitepapers and regulatory guidelines; e.g., Coinbase custody docs, accessed 2025-11-29]
- **Market competition**:
  - Large institutions benchmark MPC providers on both **security posture** and **operational simplicity**; complex cross-cloud deployments can become a sales blocker despite security advantages.
- **Cloud pricing changes**:
  - Providers occasionally adjust egress and inter-region pricing; recent announcements by AWS, Azure, and Google show gradual downward trends in some egress scenarios but no elimination of outbound charges.  
    [Source: AWS, Azure, Google pricing pages and blog announcements, accessed 2025-11-29]

### 3.3 Responsibility & room for maneuver

- **Where this team must take responsibility**:
  - Define and own a **provider-agnostic abstraction** for enclave deployment, attestation, and telemetry.
  - Make **transparent trade-offs** between security level and operational cost for each deployment mode.
- **Where to leave room for others**:
  - Allow enterprises to select preferred clouds and regions within supported trust models.
  - Provide well-documented interfaces for future enclave types (e.g., Intel TDX, ARM CCA) without committing to implement them all immediately.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Single-cloud MPC and enclaves (pre-2020)**: MPC deployments and enclave usage were largely single-cloud to reduce complexity; trust separation was often achieved via multiple tenants within one provider.  
   [Source: Early MPC deployment case studies listed on MPC Deployments dashboard, accessed 2025-11-29]
2. **Rise of multi-cloud trust separation (2020–2023)**: Projects like Signal’s Secure Value Recovery and ISRG’s ENPA experimented with running MPC parties or aggregators across multiple clouds to avoid putting all trust in a single provider.  
   [Source: Berkeley MPC blog – Signal and ENPA sections]
3. **Revealed complexity (2023–2024)**: These projects publicly reported that cross-cloud enclaves were a “foremost obstacle” with significantly higher latency and egress cost than intra-cloud designs.  
   [Source: Berkeley MPC blog – "It’s n times the work!" and "MPC in the clouds"]
4. **Current state (2024–2025)**: No standard industry abstraction has emerged; each provider solves similar problems independently, multiplying industry-wide effort.

### 4.2 Background vs. direct causes

- **Background causes**:
  - Structural economic incentives for cloud vendors to differentiate services and keep customers within their ecosystems.
  - Lack of open, multi-vendor standardization for enclave attestation and lifecycle management across major clouds.
- **Direct causes**:
  - Divergent attestation formats and runtimes between Nitro, SGX, and SEV-based offerings.
  - Application designs that naively send large MPC payloads cross-cloud, amplifying egress and latency costs.

### 4.3 Root issues

- **Institutional**: No coordinating body or widely adopted open-source platform to define a neutral “multi-cloud MPC runtime and attestation spec” that clouds can target.
- **Technical**: Enclave platforms were designed primarily as **provider-specific confidential-computing products**, not as interoperable MPC building blocks.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory if unchanged

- More providers will **stick to single-cloud or dual-cloud deployments**, citing cost and complexity, and rely mainly on MPC + intra-cloud enclaves for trust separation.
- Multi-cloud deployments will remain **bespoke and high-touch**, suitable only for large teams with dedicated security/platform engineering capacity.
- The industry will see **redundant rebuilding** of similar abstraction layers across many companies, with fragmentation of best practices.

### 5.2 Early signals

- Public reports (Signal, ISRG) describing **major engineering investment** into multi-cloud enclaves and calling it a foremost deployment obstacle.  
  [Source: Berkeley MPC blog]
- Growth of confidential-computing products (AWS Nitro, Azure confidential computing, Google Confidential VMs and Confidential GKE nodes) and marketing around “lift-and-shift” for sensitive workloads.  
  [Source: respective provider landing pages, accessed 2025-11-29]
- Increased focus on **cloud egress cost optimization** in FinOps and cloud-cost tooling, indicating that outbound data is a growing line item.  
  [Source: CloudZero AWS egress article; other FinOps blogs]

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:
  - A shared open-source abstraction for multi-cloud enclaves gains traction, backed by at least one major wallet provider and one cloud vendor.
  - Teams achieve ~1.2–1.5x overhead vs. single-cloud, and cross-cloud egress is reduced via compression, batching, and more efficient MPC protocols.
- **Baseline scenario**:
  - Each provider implements **internal** abstraction layers with moderate success; overhead remains ~1.8–2.0x vs. single-cloud for serious deployments.
- **Pessimistic scenario**:
  - Due to sustained cost and complexity, multi-cloud MPC is used only for a handful of flagship deployments; most providers revert to single-cloud with a mix of MPC + on-prem HSMs or mobile enclaves.

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths (hypothesized)

- Strong cryptography and protocol-engineering teams capable of understanding MPC and enclave threat models.
- Prior production experience with at least one enclave platform (e.g., AWS Nitro or Azure SGX) and single-cloud MPC deployments.
- Existing DevOps and SRE practices for high-availability services in at least one cloud.

### 6.2 Capability gaps

- **Multi-cloud DevOps**: Limited experience with running **identical services** across several heterogeneous clouds with shared SLOs.
- **Enclave-specific engineering**: Need deeper expertise in SGX/TDX, Nitro, and SEV/SEV-SNP specifics (attestation, side-channel mitigations, patching cadence).
- **Cost and latency modeling**: Need FinOps-style skills to model egress and latency under different topologies and throughput regimes.

### 6.3 Buildable capabilities

- **Short-term (0–3 months)**:
  - Upskill 1–2 platform engineers on enclave attestation and confidential-computing primitives via focused training and pair work with specialists.
  - Stand up basic cost and latency dashboards per cloud provider.
- **Medium-term (3–12 months)**:
  - Establish a **multi-cloud platform team** (3–4 engineers) with clear mandate to own the abstraction, reference architectures, and tooling.
  - Bring in external expertise (consultants or collaboration with academic groups) to review security and abstraction design.  
    [Source: Berkeley MPC blog – collaboration between academia and industry deployments]

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

1. **Context Recap** – problem, goals, constraints (done above).
2. **Architecture options**:
   - A. Single-cloud enclaves + MPC.
   - B. Dual-cloud deployment (two providers).
   - C. Triple-cloud deployment (three major providers).
3. **Abstraction strategy**:
   - Enclave capability profiles and unified runtime.
   - Attestation unification and policy engine.
4. **Operational stack**:
   - Multi-cloud CI/CD and configuration management.
   - Unified observability and incident response.
   - Cost and latency telemetry.
5. **Risk & value analysis** of options.
6. **Action plan** (short-, medium-, and long-term).

### 7.2 Key judgments (to validate)

- Judgement 1: A well-designed abstraction layer can reduce effective per-cloud overhead to ~1.5x or better (vs. naive 3x) without meaningfully weakening security.
- Judgement 2: For many workloads, the **marginal security benefit** of moving from dual-cloud to triple-cloud deployment may be smaller than the extra operational cost and complexity.
- Judgement 3: Network egress cost and latency can be kept within acceptable bounds via topology design and MPC message optimization, avoiding the need to abandon multi-cloud for purely economic reasons.

### 7.3 Alternative high-level approaches

- **Option A – Multi-cloud native**: Build a fully general abstraction for Nitro, SGX, and SEV/SEV-SNP and commit to triple-cloud support as a first-class feature.
- **Option B – Opinionated dual-cloud**: Officially support only two clouds (e.g., AWS + Azure) with deepest integration and provide a pluggable interface for additional providers on a best-effort basis.
- **Option C – Single-cloud primary + portable fallback**: Run production MPC primarily on one cloud with enclaves, but design artifacts and pipelines so deployments could be moved or duplicated to a second cloud in a short time for disaster-recovery or regulatory reasons.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases

- **Security maximalism**: Overweighting multi-cloud trust separation benefits and underestimating the real risk and cost of operational complexity.
- **Platform bias**: Preference for a “home” cloud influencing what seems easy or hard, leading to underestimation of engineering cost on other providers.
- **Optimism bias**: Assuming abstractions will work smoothly across enclaves despite empirical evidence from Signal and ISRG that this is “n times the work”.  
  [Source: Berkeley MPC blog]

### 8.2 Required intelligence

- **Data needed**:
  - Measured end-to-end latency and egress volume for representative MPC workloads across different topologies (single-cloud, dual-cloud, triple-cloud).
  - Engineering hours spent per provider for a fixed set of changes (e.g., security patch rollout, feature release) to quantify effective multiplier.
  - Failure and incident statistics broken down by provider and enclave platform.
- **External benchmarks**:
  - Case studies of other MPC wallet and analytics deployments across clouds (Fordefi, Safeheron, etc.).  
    [Source: MPC Deployments dashboard, accessed 2025-11-29]
  - Confidential-computing reference architectures from cloud providers.

### 8.3 Validation plan

1. **Pilot topology experiments**:
   - Implement a small-scale pilot with 1M test transactions/month across different topologies and measure: e2e latency distribution, cross-cloud egress GB, and stability.
2. **Engineering effort logging**:
   - For 1–2 quarters, log engineering hours required per provider for a set of comparable tasks (e.g., protocol upgrade) to quantify the real-world overhead multiplier.
3. **Security review**:
   - Commission an external review of the multi-cloud abstraction design, focusing on attestation correctness and failure isolation.
4. **Decision thresholds**:
   - Proceed with triple-cloud GA only if: (a) effective overhead ≤1.5x vs. single-cloud, (b) egress cost for reference workload ≤target range, and (c) no material security regressions vs. bespoke per-cloud deployment.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- If pilot data shows **much higher-than-expected egress or latency**, the design may need to prioritize dual-cloud or single-cloud modes for most customers, with triple-cloud reserved for special cases.
- If enclave APIs evolve (e.g., Intel TDX, future SEV-SNP or Nitro features), parts of the abstraction may need redesign to exploit improved attestation or performance characteristics.

### 9.2 Incremental approach

- Start with **dual-cloud** deployments for a subset of customers and workloads.
- Iterate on abstraction and tooling before onboarding the third provider:
  - Phase 1: Shared attestation abstraction + per-cloud runtimes.
  - Phase 2: Unified observability + cost dashboards.
  - Phase 3: Advanced routing, batching, and topology optimization.

### 9.3 "Good enough" criteria

- Decision-makers can reliably answer:
  - What is the **incremental security gain** from adding each additional cloud?
  - What is the **incremental cost and latency** penalty?
  - Are we **operationally confident** that we can patch and monitor all parties at the required cadence?
- If yes, and metrics fall within the ranges defined in Section 1.2, the design is sufficiently mature to deploy more broadly.

---

## 10. Summary & Action Recommendations

### 10.1 Core insights

- The main challenge is **not** cryptography but **operationalizing heterogeneous enclave platforms across multiple clouds** while controlling complexity and cost.  
  [Source: Berkeley MPC blog]
- Without an explicit multi-cloud abstraction, teams pay ~3x overhead and risk inconsistent security posture across providers.
- Cross-cloud egress and latency can be meaningful but are **manageable** for many MPC workloads if topologies and protocols are designed carefully.

### 10.2 Near-term action list (0–3 months)

1. **【P0】Define enclave capability profiles and minimal abstraction** → Platform Eng Lead → Deliver v0 design doc and reference interface for Nitro, SGX, and SEV-based platforms → 2025-02-15.  
   - Include attestation format mapping, lifecycle hooks, and logging requirements.
2. **【P0】Set up multi-cloud cost & latency observability** → SRE/FinOps → Dashboards for per-cloud egress, per-topology latency, and error rates → 2025-02-28.  
   - Use provider billing exports + tracing instrumentation.
3. **【P1】Run small-scale cross-cloud pilot** → MPC Team → Evaluate 1M test tx/month across 2–3 topologies with synthetic or low-risk workload → 2025-03-31.

### 10.3 Medium-term roadmap (3–12 months)

1. **【P0】Harden unified attestation workflow** → Security + Platform → One attestation policy engine and verification path driving all providers → 2025-06-30.
2. **【P1】Productize deployment modes** → Product + Engineering → Offer clearly documented "single-cloud secure", "dual-cloud high-assurance", and "triple-cloud maximum separation" tiers with quantified guarantees and cost expectations → 2025-09-30.
3. **【P1】Publish reference architecture & threat model** → Security → Public whitepaper or customer-facing doc explaining trade-offs and controls, including dependency on enclave vendors → 2025-09-30.

---

## 11. Glossary

- **Application-level attestation**: Remote attestation model where the enclave or trusted execution environment proves that a specific application binary or measurement is running, as provided by technologies like Intel SGX; typically stronger binding to application code than VM- or container-level attestation.  
  [Source: Azure confidential computing overview]
- **AWS Nitro Enclaves**: Amazon EC2 feature that uses the Nitro hypervisor to carve out isolated compute environments from EC2 instances, enabling secure processing of highly sensitive data with minimal attack surface.  
  [Source: AWS Nitro Enclaves documentation]
- **Azure confidential computing**: Family of Azure services that use hardware-backed trusted execution environments (such as Intel SGX and AMD SEV-SNP) to protect data in use.  
  [Source: Microsoft Learn – Azure confidential computing overview]
- **Confidential VM (Google Cloud)**: Google Cloud VM type based on AMD SEV or SEV-SNP that encrypts memory and provides integrity protection, enabling confidential-computing workloads without major application changes.  
  [Source: Google Cloud confidential-computing docs]
- **Cross-cloud egress cost**: Charges applied by cloud providers when data leaves their network to the public internet or to another provider, typically on the order of $0.08–$0.12/GB for common tiers.  
  [Source: AWS APN data-transfer blog; Azure bandwidth pricing; Google VPC network pricing; CloudZero and DigitalOcean egress articles]
- **Hardware enclave**: Hardware-anchored trusted execution environment (TEE) that isolates code and data from the rest of the system, providing confidentiality and integrity guarantees even if the host OS or hypervisor is compromised.  
  [Source: Azure, AWS, Google confidential-computing docs]
- **Intra-cloud traffic**: Network communication within a single cloud provider’s infrastructure (e.g., same region or VPC/Virtual Network), usually much cheaper or free compared with cross-cloud egress.  
  [Source: AWS and Azure data transfer pricing pages; Google VPC pricing]
- **Multi-cloud deployment**: Architecture where components of a system (such as MPC parties or aggregators) are deployed across multiple independent public cloud providers to improve trust separation and resilience.
- **MPC (Secure multi-party computation)**: Cryptographic technique that allows multiple parties to jointly compute a function over their inputs without revealing those inputs, widely used for threshold key management and privacy-preserving analytics.  
  [Source: Berkeley MPC blog – MPC introduction]
- **Reproducible builds**: Build processes that reliably produce identical binaries from the same source and environment, enabling independent verification that deployed code matches open-source releases.  
  [Source: Berkeley MPC blog – Signal’s reproducible builds]
- **Trust separation**: Design principle where no single administrative or infrastructure domain has unilateral power to compromise sensitive assets (e.g., private keys); achieved via MPC, multi-cloud, multi-operator governance, or combinations thereof.

---

## 12. References

1. **Berkeley MPC Blog** – "The Deployment Dilemma: Merits & Challenges of Deploying MPC" (Signal, Coinbase, ISRG, UC Berkeley authors), UC Berkeley Security Group, accessed 2025-11-29, https://mpc.cs.berkeley.edu/blog/deployment-dilemma.html
2. **MPC Deployments Dashboard**, UC Berkeley Security Group, catalog of real-world MPC deployments including Fordefi, Safeheron, and others, accessed 2025-11-29, http://mpc.cs.berkeley.edu/
3. **AWS Nitro Enclaves Documentation** – "What is Nitro Enclaves?", AWS, accessed 2025-11-29, https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html
4. **Azure Confidential Computing Overview**, Microsoft Learn, accessed 2025-11-29, https://learn.microsoft.com/azure/confidential-computing/overview
5. **Confidential Computing (Google Cloud)**, product and documentation overview, accessed 2025-11-29, https://cloud.google.com/confidential-computing
6. **AWS APN Blog** – "AWS Data Transfer Charges for Server and Serverless Architectures", AWS Partner Network, accessed 2025-11-29, https://aws.amazon.com/blogs/apn/aws-data-transfer-charges-for-server-and-serverless-architectures/
7. **CloudZero Blog** – "AWS Egress Costs Explained: How To Reduce Spend", CloudZero, accessed 2025-11-29, https://www.cloudzero.com/blog/aws-egress-costs/
8. **Azure Bandwidth Pricing**, Microsoft Azure official pricing page, accessed 2025-11-29, https://azure.microsoft.com/pricing/details/bandwidth/
9. **Azure Egress Costs: What You Should Know**, DigitalOcean, accessed 2025-11-29, https://www.digitalocean.com/resources/articles/azure-egress-costs
10. **Network Pricing**, Google Cloud VPC documentation, accessed 2025-11-29, https://cloud.google.com/vpc/network-pricing
11. **Coinbase MPC Wallet / WaaS Whitepapers**, Coinbase, various years, accessed 2025-11-29, https://coinbase.bynder.com (MPC wallet whitepaper landing page)
12. Additional provider and standards documentation on confidential-computing, MPC wallets, and enclave security best practices, accessed 2025-11-29.
