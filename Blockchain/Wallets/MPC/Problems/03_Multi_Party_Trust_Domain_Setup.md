# Multi-Party Trust Domain Setup Complexity

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Platform Team

## Problem Statement

1. **[Important]** Q: Organizations deploying MPC wallets face significant challenges identifying and coordinating independent trust domains, requiring 2-4 months for partner selection and integration while struggling to find parties matching scale, security, and uptime requirements. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     MPC security requires distributing key shares across truly independent parties with sufficient separation, but finding partners matching operational scale (millions of users, 99.9% uptime), security requirements (SOC 2, penetration testing), and trust separation proves extremely difficult. Organizations spend 2-4 months on partner selection and 4-8 weeks on integration, with many defaulting to less secure cloud-only deployments due to partnership overhead. This affects enterprise adoption, institutional custody providers, and blockchain infrastructure requiring MPC for key management.
   
   - **Background and current situation**: 
     MPC security depends on key share separation across independent trust domains; compromising one domain must not expose complete keys [Blog: Berkeley MPC, 2023]. Finding suitable parties requires matching multiple criteria: operational scale (handle millions of users, 99.9% uptime SLA), security posture (SOC 2 Type II, regular audits, incident response), geographic/jurisdictional separation (different legal entities, data centers, cloud providers), 24/7 support availability [Blog: Berkeley MPC, 2023]. Signal explored MPC for secure value recovery but could not identify partners matching their scale (millions of users) and privacy guarantees [Blog: Berkeley MPC, 2023]. Coinbase WaaS initially deployed 2-of-2 (user + Coinbase) but institutional clients demand 3-of-5 models requiring additional independent parties [Guide: Stackup, 2024]. ISRG's ENPA project (COVID exposure notifications) required 2-4 weeks partner selection + 4-8 weeks integration between ISRG, NIH, Apple, Google, with significant cross-organizational coordination overhead [Blog: Berkeley MPC, 2023]. Most consumer MPC wallets (ZenGo, Coinbase) use 2-of-2 or 2-of-3 with provider-controlled shares, reducing security separation but avoiding partnership complexity [Guide: Stackup, 2024].
   
   - **Goals and success criteria**: 
     Partner identification time: 2-4 months (current) → <4 weeks (min) / <2 weeks (target) / <1 week (ideal) through standardized partner marketplaces. Integration complexity: 4-8 weeks (current) → <2 weeks (min) / <1 week (target) / <3 days (ideal) via standardized protocols and APIs. Partner availability: Limited suitable partners (current) → ≥10 vetted partners per use case (min) / ≥20 (target) / ≥50 (ideal) through partner ecosystem development. Trust separation: Most deployments use provider-controlled shares (current low separation) → ≥80% deployments achieve true multi-party separation (min) / ≥90% (target) by Q4 2025. Enterprise adoption: Partnership overhead blocking adoption → ≥50% enterprise prospects successfully deploy (current <20%) by Q4 2025.
   
   - **Key constraints and resources**: 
     Timeline: Q1 2025 - Q4 2025 (12 months ecosystem development); Budget: $500K-$1.5M for partner marketplace platform + certification program + integration tooling; Team: 1-2 business development + 2-3 platform engineers + 1 security auditor; Partner requirements: Cannot lower security standards (SOC 2, 99.9% uptime non-negotiable), geographic/jurisdictional separation needed for regulatory compliance, 24/7 support required for production systems; Technology: Need standardized MPC party interfaces, interoperable authentication mechanisms, compatible key management protocols; Legal: Partnership agreements require 2-4 weeks legal review, data processing agreements for GDPR/CCPA compliance; Trust model: Partners must not collude (independent ownership, separate incentives).
   
   - **Stakeholders and roles**: 
     MPC Wallet Providers (20+ companies, need ≥3 vetted partners per deployment, constraint: 2-4 month partnership overhead blocks launches); Enterprise Customers (est. 500+ institutional custody prospects, need 3-of-5 or 5-of-7 models, constraint: cannot accept single-provider trust assumptions); Potential MPC Partners (universities, non-profits, cloud providers, need clear certification criteria, constraint: uncertain ROI for building MPC infrastructure); Regulators (financial authorities, need demonstrated trust separation for custody approval, constraint: must audit complete partner network); End Users (millions of digital asset holders, need transparent trust model, constraint: cannot evaluate partner security independently); Integration Engineers (100+ developers deploying MPC, need standardized APIs, constraint: each partner integration currently requires 40-200 hours custom work).
   
   - **Time scale and impact scope**: 
     Timeline: Q1 2025 - Q4 2025 (12 months platform development + partner onboarding); Systems: Partner discovery marketplace, security certification framework, standardized MPC party APIs, key ceremony orchestration, cross-party authentication infrastructure; Scale: 20+ MPC wallet providers, 500+ enterprise prospects, target 50+ certified partners by Q4 2025; Current impact: 2-4 month partnership overhead per deployment, <20% enterprise prospect conversion due to complexity; Adoption blockers: Signal unable to deploy MPC due to lack of suitable partners, institutional clients requiring 3-of-5 models facing 6-12 month partner identification; Regions: Global (regulatory requirements vary by jurisdiction, complicating partner selection).
   
   - **Historical attempts and existing solutions (if any)**: 
     2021-2023: Most providers defaulted to 2-of-2 models (user + provider) to avoid partnership complexity, sacrificing trust separation [Guide: Stackup, 2024]. 2022-2023: Cloud providers (AWS Nitro, Azure SGX, Google AMD-SEV) offered hardware enclaves as "virtual parties," but require trusting single cloud vendor and lack application-level attestation [Blog: Berkeley MPC, 2023]. 2023: ISRG's ENPA project (COVID notifications) required 2-4 weeks partner selection between ISRG, NIH, Apple, Google, with significant cross-organizational overhead for testing, deployment coordination, shared infrastructure [Blog: Berkeley MPC, 2023]. 2024: Coinbase explored partner networks for institutional clients but found limited suitable candidates matching scale and security requirements [implied from Guide: Stackup, 2024]. Key lesson: Partnership overhead drives providers toward less secure single-entity deployments; lack of standardized partner marketplace and certification framework prevents ecosystem scaling.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: Partner selection takes 2-4 months, integration takes 4-8 weeks [Blog: Berkeley MPC, 2023]; Signal could not identify suitable MPC partners matching scale and privacy requirements [Blog: Berkeley MPC, 2023]; ISRG ENPA required 2-4 weeks partner selection for NIH, Apple, Google collaboration [Blog: Berkeley MPC, 2023]; Most consumer wallets use 2-of-2 or 2-of-3 with provider-controlled shares [Guide: Stackup, 2024]; Enterprise clients require 3-of-5 or 5-of-7 models [Guide: Stackup, 2024]; Integration requires 40-200 hours engineering per partner [Blog: Berkeley MPC, 2023].
     - **Assumptions**: est. 20+ MPC wallet providers (market sizing from major players: Fireblocks, ZenGo, Coinbase, Binance, BitGo, Web3Auth, Lit Protocol, etc.); est. 500+ enterprise custody prospects (inferred from institutional crypto custody market growth, Coinbase Prime institutional focus); $500K-$1.5M platform development budget (2-3 platform engineers × 12 months × $150K + BD × $200K + security auditor × $120K + $100K infrastructure); <20% enterprise conversion rate (inferred from stated partnership complexity blocking adoption); target 50+ certified partners by Q4 2025 (ambitious but necessary for ecosystem liquidity).
     - **Uncertainties**: Actual number of willing and capable partners unknown (universities? non-profits? specialized infrastructure providers?); Partner incentive model unclear (fee-per-signature? subscription? grant-funded?); Legal framework for multi-party liability unclear (who is responsible if one party is compromised?); Regulatory acceptance of standardized partner certification unknown (will regulators accept third-party certification or require individual audits?); Minimum viable partner count unknown (is 10 partners sufficient? 20? 50?).

---

## Glossary

- **24/7 support**: Round-the-clock operational support required for production MPC deployments; critical for high-uptime services like Signal (millions of users).
- **ENPA (Exposure Notification Privacy-preserving Analytics)**: COVID-19 exposure notification system using MPC between ISRG, NIH, Apple, Google; required 2-4 weeks partner coordination.
- **Geographic separation**: Distributing MPC key shares across different physical locations (data centers, countries) to prevent single-region attacks or legal seizure.
- **Hardware enclave**: Secure execution environment (AWS Nitro, Azure SGX, Google AMD-SEV) used as "virtual MPC party"; offers separation but requires trusting cloud vendor.
- **Key ceremony**: Distributed process for generating and distributing MPC key shares across parties; requires coordination, authentication, and verification.
- **Partner marketplace**: Proposed platform connecting MPC wallet providers with certified infrastructure partners offering MPC party services.
- **SOC 2 Type II**: Security certification for service organizations covering security, availability, processing integrity, confidentiality, privacy; typically required for financial services.
- **Trust domain**: Independent organizational entity controlling MPC key shares; true separation requires different ownership, infrastructure, legal jurisdiction.
- **Trust separation**: Degree of independence between MPC parties; strong separation requires different organizations, data centers, cloud providers, legal jurisdictions.
- **3-of-5 / 5-of-7 model**: Threshold signature scheme requiring 3 of 5 (or 5 of 7) parties to sign; provides redundancy and security but requires coordinating multiple independent parties.
- **Uptime SLA**: Service Level Agreement guaranteeing system availability; 99.9% = 8.76 hours downtime/year, critical for production custody systems.

---

## Reference

### Technical Blogs & Case Studies
- [Blog: Berkeley MPC, 2023] - "The Deployment Dilemma: Merits & Challenges of Deploying MPC" (https://mpc.cs.berkeley.edu/blog/deployment-dilemma.html)
- [Guide: Stackup, 2024] - "MPC Wallets: A Complete Technical Guide" sections on trust models and deployment patterns (https://www.stackup.fi/resources/mpc-wallets-a-complete-technical-guide)

### Industry Examples
- Signal: Exploring MPC for secure value recovery, partner identification challenges
- ISRG: ENPA project (COVID exposure notifications) multi-party coordination case study
- Coinbase: WaaS and Prime institutional custody multi-party requirements

### Standards & Certifications
- SOC 2 Type II: Security certification standard for service organizations
- GDPR/CCPA: Data processing agreement requirements for multi-party deployments
