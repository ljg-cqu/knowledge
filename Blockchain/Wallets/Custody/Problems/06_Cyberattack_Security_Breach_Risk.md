# Cyberattack and Security Breach Risk in Crypto Custody

**Last Updated**: 2025-11-29  
**Status**: Draft  
**Owner**: Documentation Team

## Problem Statement

1. **[CRITICAL]** Q: Crypto custody providers face escalating cyberattack risk with H1 2025 seeing $1.93B in stolen assets, threatening institutional confidence and requiring enhanced security infrastructure. Formulate a structured problem statement using the following [Input] fields.
   
   A:
   - **Brief description of the problem to be analyzed**: 
     Cyberattacks on crypto custody platforms resulted in $1.93B stolen assets in H1 2025, surpassing total 2024 losses, with 2025 on track to become worst year for digital asset theft [Web Search: Kroll, 2025]. North Korean state-sponsored hackers account for >$2B (60% of all exchange thefts), while phishing attacks increased 40% targeting custody users [Web Search: CoinLaw, Kroll, 2025]. Institutional investors require breach rate reduction from current industry baseline (est. 5-15 major incidents annually affecting 10-20% of custodians) to <2% custodian impact rate by Q4 2025, with security-first architecture reducing successful breach impact by >80%.
   
   - **Background and current situation**: 
     H1 2025 crypto-crime resulted in nearly $1.93B stolen assets, exceeding 2024 full-year total [Web Search: Kroll, 2025]. By October 2025, North Korean hackers stole >$2B crypto, representing 60%+ of global exchange thefts [Web Search: CoinLaw, 2025]. Phishing attacks increased 40% in early 2025, primarily through fake exchange sites [Web Search: Kroll, 2025]. February 2025 Bybit hack demonstrated continued vulnerability of even licensed custodians [Web Search: State Street, Tokenmetrics, Ocorian, 2025]. Attack vectors include: (1) hot wallet compromise (online-connected wallets vulnerable to remote attacks), (2) phishing/social engineering (targeting employees and users), (3) smart contract exploits (DeFi integration vulnerabilities), (4) supply chain attacks (compromised software dependencies), (5) insider threats (malicious employees with privileged access). Leading custodians achieving >80% breach reduction since 2022 through cold storage priority, MPC architecture, and 24/7 monitoring [Web Search: Yellow Card, BitGo, 2025].
   
   - **Goals and success criteria**: 
     Successful breach rate: current industry baseline est. 10-20% of custodians affected annually → <5% (min) / <2% (target) / 0% (ideal) by Q4 2025; Asset loss from breaches: $1.93B H1 2025 industry-wide → <$500M annually (min) / <$100M (target) / $0 (ideal); Breach detection time: current est. 24-72h → <4h (min) / <1h (target) / <15min (ideal); Incident response time: current est. 48-96h → <24h (min) / <12h (target) / <4h (ideal); Multi-layer security implementation: current est. 40-60% custodians → >80% (min) / >90% (target) / 100% (ideal); Phishing attack success rate: current 40% increase in 2025 → <10% employee click rate (min) / <5% (target) / <1% (ideal)
   
   - **Key constraints and resources**: 
     Timeline Q1-Q4 2025 (9-12mo for security infrastructure upgrade); Budget $2M-$5M capex for security infrastructure (cold storage, MPC, HSM, monitoring) + $300K-$600K/mo opex for 24/7 SOC; Team 5-10 FTE security engineers + 3-5 FTE SOC analysts + 2 FTE penetration testers + 1 CISO; Tech requirements: cold storage for 90%+ assets, MPC/HSM for key management, 24/7 monitoring/threat detection, multi-signature authorization, bug bounty program, regular penetration testing; Regulatory constraints: must meet MiCA and SEC security standards; Security constraints: maintain 99.9%+ uptime while upgrading; Cannot compromise availability during security hardening; Must support institutional SLAs
   
   - **Stakeholders and roles**: 
     Institutional investors (managing $100M-$10B+ AUM, need <2% breach risk, constraint: require security-first custodians with >80% breach reduction track record), Custody providers (50-500 clients, need competitive security, constraint: security investment <3% of operational budget), Security teams (5-10 engineers, need advanced threat detection, constraint: <1h detection time for anomalies), SOC analysts (3-5 FTE, need 24/7 monitoring tools, constraint: <15min alert response time), Compliance officers (need audit trails, constraint: demonstrate security compliance for MiCA/SEC), End clients (need asset protection, constraint: accept <0.2% security cost pass-through), Insurance underwriters (need risk assessment, constraint: breach rate <5% for coverage approval)
   
   - **Time scale and impact scope**: 
     Timeline Q1-Q4 2025 (9-12mo); Affected systems: Hot wallets (transaction processing), Cold storage (bulk asset storage), Key management (MPC/HSM), Transaction signing, Access control (employee/client authentication), Network infrastructure (DDoS protection), Smart contract integration (DeFi protocols); Geographic scope: Global custody ecosystem; Scale: $3.28B custody market [Web Search: XBTO, Yellow Card, 2025], H1 2025 losses $1.93B [Web Search: Kroll, 2025], North Korean hackers $2B+ theft [Web Search: CoinLaw, 2025], institutional portfolios $100M-$10B+; Attack surface: 100+ blockchain networks, thousands of smart contracts, millions of users
   
   - **Historical attempts and existing solutions (if any)**: 
     Cold storage adoption: offline key storage reducing remote attack surface. Outcome: leading custodians achieve 90%+ cold storage ratio, significantly reducing hot wallet breach risk [Web Search: Yellow Card, BitGo, 2025]. Multi-Party Computation (MPC): distributed key management eliminating single point of compromise. Outcome: >80% breach reduction since 2022 for MPC-enabled custodians [Web Search: Yellow Card, 2025]. 24/7 Security Operations Center (SOC): continuous monitoring and threat detection. Outcome: reduces detection time from days to hours [Web Search: Yellow Card, BitGo, 2025]. Bug bounty programs: incentivize ethical hackers to discover vulnerabilities. Outcome: identify 50-80% of critical vulnerabilities before exploitation. Multi-signature authorization: require multiple approvals for transactions. Outcome: prevents single-point insider attacks but adds operational latency. Key lesson: multi-layer security (cold storage + MPC + 24/7 monitoring + multi-sig) reduces breach success by >80%, but requires significant investment and continuous adaptation to evolving threats.
   
   - **Known facts, assumptions, and uncertainties**: 
     - **Facts**: H1 2025 crypto-crime losses $1.93B [Web Search: Kroll, 2025]; North Korean hackers >$2B theft (60% of exchange thefts) [Web Search: CoinLaw, 2025]; Phishing attacks increased 40% in early 2025 [Web Search: Kroll, 2025]; February 2025 Bybit hack affected licensed custodian [Web Search: State Street, Tokenmetrics, Ocorian, 2025]; Leading custodians achieve >80% breach reduction with multi-layer security [Web Search: Yellow Card, BitGo, 2025]; Cold storage, MPC, 24/7 monitoring becoming industry standard [Web Search: Yellow Card, BitGo, 2025]; $3.28B custody market [Web Search: XBTO, Yellow Card, 2025]
     - **Assumptions**: Industry breach rate est. 10-20% of custodians affected annually (inferred from public incident reports and custody provider counts); Current custodian multi-layer security adoption est. 40-60% (based on leading provider disclosures vs total market); Breach detection time est. 24-72h (typical cybersecurity incident timelines); Incident response time est. 48-96h (time to contain and remediate based on public incident reports); Security infrastructure capex est. $2M-$5M (cold storage hardware, MPC systems, HSM, monitoring platforms); Security opex est. $300K-$600K/mo (SOC staffing, tools, testing)
     - **Uncertainties**: Optimal security investment level vs breach risk reduction not quantified; Effectiveness of different security architectures (MPC vs HSM vs hybrid) for specific attack vectors TBD; State-sponsored attack sophistication trajectory unknown; Phishing prevention effectiveness for different user training approaches unclear; Smart contract security for custody-integrated DeFi protocols not standardized; Insurance coverage for different attack scenarios evolving; Regulatory minimum security requirements (MiCA/SEC specifics) not finalized; Zero-day vulnerability risk in custody software not predictable; Quantum computing threat timeline to cryptographic security uncertain

---

## Glossary

- **Bug bounty program**: Incentive system rewarding ethical hackers for discovering and reporting security vulnerabilities before malicious exploitation.
- **Cold storage**: Offline private key storage (hardware wallets, air-gapped systems, paper wallets) providing maximum security against remote attacks but requiring manual processes for transactions.
- **DDoS (Distributed Denial of Service)**: Cyberattack overwhelming systems with traffic to disrupt availability, requiring network-level protection infrastructure.
- **Hot wallet**: Online-connected wallet enabling fast transaction processing but with increased attack surface compared to cold storage.
- **MPC (Multi-Party Computation)**: Cryptographic technique distributing private key across multiple parties, preventing single-point compromise while enabling efficient transaction signing.
- **Multi-signature (Multi-sig)**: Transaction authorization requiring multiple private key signatures (e.g., 2-of-3, 3-of-5), preventing single-point insider attacks.
- **Phishing**: Social engineering attack tricking users into revealing credentials or approving malicious transactions through fake websites, emails, or messages.
- **SOC (Security Operations Center)**: Team and infrastructure providing 24/7 monitoring, threat detection, incident response, and security management.
- **Supply chain attack**: Compromise of software dependencies, libraries, or development tools to inject malicious code into custody platform.

---

## Reference

### Web Search Sources
- [Web Search: Kroll, 2025] - 2025 Cyber Threat Landscape Report, H1 2025 $1.93B crypto-crime losses, 40% increase in phishing attacks
- [Web Search: CoinLaw, 2025] - Crypto exchange hacks and security statistics 2025, North Korean hackers >$2B theft (60% of exchange thefts)
- [Web Search: State Street, Tokenmetrics, Ocorian, 2025] - February 2025 Bybit hack, custody security challenges, breaking the vault lessons
- [Web Search: Yellow Card, BitGo, 2025] - Institutional custody security-first approach, cold storage, MPC, 24/7 monitoring, >80% breach reduction since 2022
- [Web Search: XBTO, Yellow Card, 2025] - $3.28B custody market projection 2025, institutional security requirements
