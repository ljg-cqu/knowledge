# Cross-Cloud Deployment Operational Complexity

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: DevOps Team

## Problem Statement

1. **[Important]** Q: Organizations deploying MPC across multiple cloud providers for trust separation face 3x development effort, inconsistent hardware enclave attestation mechanisms, and 2-5x higher egress costs compared to single-cloud deployments. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Multi-cloud MPC deployments require developing and maintaining separate codebases for each cloud provider's distinct hardware enclaves (AWS Nitro, Azure SGX, Google AMD-SEV), with each software update requiring 3x effort for attestation, testing, and deployment. Organizations also face 2-5x higher network egress costs for cross-cloud communication and significant operational complexity managing inconsistent APIs, monitoring, and incident response across providers. This affects 10+ MPC wallet providers and 100+ enterprise deployments requiring trust separation.
   
   - **Background and current situation**: 
     Cloud hardware enclaves offer trust separation: AWS Nitro (Docker container attestation), Azure Intel SGX (application-level attestation), Google AMD-SEV (kernel-level attestation) [Blog: Berkeley MPC, 2023]. Each cloud provider requires distinct development, deployment, and attestation approach: no unified standard [Blog: Berkeley MPC, 2023]. Signal allocated significant resources to achieve acceptable application-level attestation and reproducible builds across multiple platforms, citing this as "foremost obstacle" to deployment [Blog: Berkeley MPC, 2023]. Multi-cloud tools (Terraform) only abstract simple operations, excluding complex cloud-specific services like hardware enclaves [Blog: Berkeley MPC, 2023]. Network egress costs: AWS charges $0.09/GB outbound, Azure $0.087/GB, Google Cloud $0.12/GB; cross-cloud MPC signing generates 10-50 KB per transaction [Blog: Berkeley MPC, 2023]. For 1M transactions/month: $900-$6,000/month egress costs vs $0 for intra-cloud [calculation]. ISRG's ENPA cross-cloud deployment faced significantly higher latency and egress fees compared to intra-cloud communication [Blog: Berkeley MPC, 2023].
   
   - **Goals and success criteria**: 
     Development effort: 3x effort per cloud (current) → 1.5x (min) / 1.2x (target) / 1x (ideal) through standardization and abstraction layers by Q4 2025. Attestation unification: 3 distinct mechanisms (current) → unified abstraction supporting all providers (target) by Q3 2025. Network egress cost: $900-$6,000/month per 1M transactions (current) → <$500/month (min) / <$200/month (target) / <$100/month (ideal) through protocol optimization. Deployment complexity: Custom per-cloud deployment scripts (current) → unified deployment pipeline supporting multi-cloud (target) by Q3 2025. Operational overhead: 3x monitoring/alerting/incident response (current) → unified operational dashboard (target) by Q4 2025. Enterprise adoption: Multi-cloud requirements blocking 40-60% prospects → <20% blocked (target) by Q4 2025.
   
   - **Key constraints and resources**: 
     Timeline: Q1 2025 - Q4 2025 (12 months); Budget: $600K-$1.5M for abstraction layer development + deployment tooling + cost optimization; Team: 3-4 platform engineers + 2-3 enclave specialists + 1-2 DevOps engineers; Technology: Cannot eliminate cloud-specific enclave APIs (AWS Nitro, Azure SGX, Google AMD-SEV fundamentally different architectures), limited by egress pricing (negotiation possible but floor at $0.05-$0.08/GB), must maintain reproducible builds for security; Compatibility: Existing single-cloud deployments must migrate to unified platform without service disruption; Security: Cannot compromise attestation rigor to simplify development (application-level attestation required for Signal-level security); Cloud contracts: Existing commitments may lock organizations into specific providers for 1-3 years.
   
   - **Stakeholders and roles**: 
     MPC Wallet Providers (10+ companies, need multi-cloud for trust separation, constraint: 3x development effort limits smaller providers); Platform Engineers (50+ across industry, need unified tools, constraint: currently spend 60-80% time on cloud-specific customization); Security Teams (20+ across providers, need consistent attestation, constraint: must audit 3 separate enclave implementations per update); Enterprise Customers (100+ requiring multi-cloud, need transparent trust separation, constraint: 40-60% block deployment due to operational complexity perception); Cloud Providers (AWS, Azure, Google, need MPC customer adoption, constraint: unwilling to standardize enclave APIs due to competitive differentiation); DevOps Teams (30+ managing MPC infrastructure, need unified monitoring, constraint: 3x operational overhead managing multiple cloud consoles, alerting systems).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2025 - Q4 2025 (12 months platform development); Systems: Hardware enclave attestation framework, multi-cloud deployment pipeline, network optimization layer, unified monitoring and observability, cost tracking and optimization; Scale: 10+ MPC providers, 100+ enterprise deployments, est. 50M+ end users; Current state: Each provider independently solving multi-cloud complexity (3x redundant development effort industry-wide); Cost impact: $900-$6,000/month per 1M transactions egress costs (est. $100K-$500K annual for major providers); Operational impact: 60-80% platform engineering time spent on cloud-specific customization; Adoption blocker: 40-60% enterprise prospects delay/abandon due to multi-cloud operational complexity concerns.
   
   - **Historical attempts and existing solutions (if any)**: 
     2021-2022: Most providers defaulted to single-cloud deployments (typically AWS) to avoid multi-cloud complexity, sacrificing trust separation [implied from Blog: Berkeley MPC, 2023]. 2022-2023: Generic multi-cloud tools (Terraform, Pulumi) tested but failed to abstract enclave-specific complexity; each provider still requires custom attestation and deployment scripts [Blog: Berkeley MPC, 2023]. 2023: Signal invested significant resources in multi-cloud enclave abstraction, citing it as "foremost obstacle" but eventually achieving acceptable application-level attestation [Blog: Berkeley MPC, 2023]. 2023-2024: ISRG's ENPA project deployed cross-cloud (ISRG + NIH on different providers) but experienced "significantly higher latency and egress fees" compared to intra-cloud, leading to preference for cloud deployment in subsequent Divvi Up service [Blog: Berkeley MPC, 2023]. Key lesson: Cloud provider enclave differentiation (AWS Nitro vs Azure SGX vs Google AMD-SEV) creates unavoidable complexity; lack of industry-wide abstraction layer forces each provider to independently solve same problems, multiplying effort 10x across industry.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: 3 distinct enclave mechanisms: AWS Nitro (Docker attestation), Azure SGX (application attestation), Google AMD-SEV (kernel attestation) [Blog: Berkeley MPC, 2023]; Signal calls multi-cloud attestation "foremost obstacle" to deployment [Blog: Berkeley MPC, 2023]; ISRG ENPA experienced "significantly higher latency and egress fees" cross-cloud [Blog: Berkeley MPC, 2023]; Generic multi-cloud tools cannot abstract enclave complexity [Blog: Berkeley MPC, 2023]; AWS egress $0.09/GB, Azure $0.087/GB, Google Cloud $0.12/GB (2024 pricing); MPC signing generates 10-50 KB per transaction (protocol overhead).
     - **Assumptions**: 3x development effort per cloud (inferred from Signal's "significant resources" comment + need for separate attestation, testing, deployment per cloud); 10+ MPC providers requiring multi-cloud (market sizing: Fireblocks, ZenGo, Coinbase, Binance, BitGo, Web3Auth, Lit Protocol, etc.); 100+ enterprise deployments (inferred from institutional custody market + Signal's millions of users scale); $900-$6,000/month egress for 1M transactions (calculation: 1M × 10-50 KB × $0.09-$0.12/GB); 60-80% platform engineering time on cloud customization (inferred from "3x effort" + operational complexity statements); 40-60% enterprise prospects blocked (inferred from stated complexity concerns + partnership overhead); $600K-$1.5M budget (3-4 platform engineers × 12 months × $150K + 2-3 enclave specialists × $180K + DevOps × 2 × $140K + $100K infrastructure).
     - **Uncertainties**: Theoretical minimum development overhead unknown (can abstraction reduce to 1.2x? or fundamental limit at 1.5x due to enclave differences?); Cloud provider willingness to collaborate on standardization unknown (competitive differentiation vs ecosystem growth trade-off); Cost optimization ceiling unclear (can protocol changes reduce egress? or fixed at 10-50 KB per transaction?); Industry coordination feasibility uncertain (will 10+ providers collaborate on shared abstraction layer? or continue independent solutions?); Regulatory impact unknown (will regulators accept unified attestation? or require per-cloud security audits?).

---

## Glossary

- **Application-level attestation**: Cryptographic proof that specific application code is running in hardware enclave; Azure SGX supports natively, AWS Nitro and Google AMD-SEV require workarounds.
- **AWS Nitro**: Amazon's hardware enclave based on Nitro Enclaves; attests to Docker container but not application binary, requiring additional verification layers.
- **Azure SGX (Intel SGX)**: Microsoft's hardware enclave using Intel Software Guard Extensions; supports application-level attestation natively but limited availability.
- **Egress cost**: Cloud provider charges for outbound data transfer; typically $0.05-$0.12/GB, becoming significant for cross-cloud MPC communication.
- **Google AMD-SEV**: Google Cloud's hardware enclave using AMD Secure Encrypted Virtualization; attests to kernel level, requiring custom application verification.
- **Hardware enclave**: Secure execution environment (TEE) isolating code and data from host system; used as "virtual MPC party" to achieve trust separation on single cloud.
- **Intra-cloud**: Network communication within single cloud provider's infrastructure; typically free or minimal cost (<$0.01/GB).
- **Multi-cloud deployment**: Running MPC key shares across multiple cloud providers (AWS + Azure + Google) for trust separation; 3x development effort vs single-cloud.
- **Reproducible builds**: Software compilation process producing identical binary from source code; critical for verifying attestation claims in hardware enclaves.
- **Terraform**: Multi-cloud infrastructure-as-code tool; abstracts simple operations but cannot unify enclave-specific complexity (attestation, deployment).
- **Trust separation**: Distributing MPC across independent infrastructure (different clouds) to prevent single-provider compromise; security benefit but 3x operational cost.

---

## Reference

### Technical Blogs & Case Studies
- [Blog: Berkeley MPC, 2023] - "The Deployment Dilemma: Merits & Challenges of Deploying MPC" covering Signal's multi-cloud attestation challenges and ISRG ENPA cross-cloud costs (https://mpc.cs.berkeley.edu/blog/deployment-dilemma.html)

### Cloud Provider Documentation
- AWS Nitro Enclaves: Docker container attestation architecture
- Azure Confidential Computing: Intel SGX application-level attestation
- Google Confidential VMs: AMD-SEV kernel-level attestation

### Pricing References (2024)
- AWS data transfer pricing: $0.09/GB egress
- Azure bandwidth pricing: $0.087/GB egress
- Google Cloud Network pricing: $0.12/GB egress

### Industry Examples
- Signal: Multi-cloud attestation cited as "foremost obstacle" to MPC deployment
- ISRG ENPA: Cross-cloud deployment with "significantly higher latency and egress fees"
- ISRG Divvi Up: Subsequent project preferring single-cloud deployment due to ENPA experience
