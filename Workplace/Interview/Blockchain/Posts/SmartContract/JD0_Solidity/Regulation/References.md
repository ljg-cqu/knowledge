## Reference Sections

### Glossary, Terminology & Acronyms

**G1. MiCA (Markets in Crypto-Assets Regulation)**  
EU regulation establishing a comprehensive regulatory framework for crypto-assets and related services; covers issuance, trading, custody, and service provision for crypto-assets; requires whitepapers for certain token offerings and licensing for service providers. Architectural implications: asset classification, investor protection, service provider registration, transparency requirements. Related: Prospectus Regulation, AMLD5 [EN]

**G2. FATF Travel Rule**  
Financial Action Task Force requirement for Virtual Asset Service Providers (VASPs) to collect and transmit originator and beneficiary information for transactions above certain thresholds (typically $1,000-3,000); applies to cross-border transfers of virtual assets. Architectural implications: information transmission protocols, VASP identification, compliance data storage, cross-chain messaging. Related: FinCEN CTR, EU Funds Transfer Regulation [EN]

**G3. GDPR (General Data Protection Regulation)**  
EU regulation (2016/679) establishing data protection and privacy rights for EU citizens; key principles: lawfulness, fairness, transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity, confidentiality, accountability. Architectural implications: consent management, right to erasure, data portability, privacy-by-design. Related: CCPA, Data Controller, Data Processor [EN]

**G4. Smart Contract**  
Self-executing contracts with terms directly written into code that automatically execute when predetermined conditions are met; deployed on blockchain networks like Ethereum; immutable and transparent by design. Architectural implications: deterministic execution, gas optimization, upgrade patterns, security controls. Related: EVM, Solidity, Reentrancy [EN]

**G5. DeFi (Decentralized Finance)**  
Financial services built on blockchain networks using smart contracts without traditional intermediaries; includes lending, borrowing, trading, and yield farming protocols; characterized by permissionless access and composability. Architectural implications: liquidity pools, automated market makers, yield aggregation, cross-protocol integration. Related: DApps, DAOs, Composability [EN]

**G6. AML/KYC (Anti-Money Laundering/Know Your Customer)**  
Regulatory requirements for financial institutions to prevent money laundering and terrorist financing; AML involves transaction monitoring and reporting; KYC requires customer identity verification and risk assessment. Architectural implications: identity verification, transaction screening, suspicious activity reporting, beneficial ownership tracking. Related: CDD, EDD, SAR [EN]

**G7. NFT (Non-Fungible Token)**  
Unique digital assets representing ownership of specific items or content on blockchain networks; each token has distinct properties and cannot be exchanged on a like-for-like basis; used for digital art, collectibles, gaming items, and real-world asset tokenization. Architectural implications: metadata storage, provenance tracking, royalty mechanisms, transfer restrictions. Related: ERC-721, ERC-1155 [EN]

**G8. EVM (Ethereum Virtual Machine)**  
Runtime environment for smart contracts on Ethereum and EVM-compatible blockchains; executes bytecode instructions in a sandboxed environment with deterministic outcomes; charges gas fees for computational resources. Architectural implications: gas optimization, state management, external calls, event logging. Related: Solidity, Bytecode, Gas [EN]

**G9. Gas**  
Computational unit measuring the cost of executing operations on Ethereum and EVM-compatible blockchains; users pay gas fees to compensate miners/validators for processing transactions and smart contract execution. Architectural implications: gas optimization, out-of-gas exceptions, gas scheduling, cost estimation. Related: Gwei, Wei, Block Gas Limit [EN]

**G10. Reentrancy**  
Smart contract vulnerability where an external call to another contract recursively calls back into the original function before the first invocation completes; can result in multiple withdrawals or state changes. Architectural implications: checks-effects-interactions pattern, reentrancy guards, mutex locks, static analysis. Related: The DAO Hack, ReentrancyGuard [EN]

**G11. Oracle**  
Off-chain data providers that feed external information (prices, events, randomness) to smart contracts; critical infrastructure for DeFi protocols that require real-world data to function. Architectural implications: data validation, multi-oracle aggregation, fallback mechanisms, trust assumptions. Related: Chainlink, Band Protocol, DIA [EN]

**G12. Immutable**  
Characteristic of blockchain data that cannot be altered or deleted once recorded; fundamental property ensuring auditability and trust but creates conflicts with privacy regulations. Architectural implications: data minimization, off-chain storage, cryptographic commitments, zero-knowledge proofs. Related: Immutability, Blockchain, Merkle Tree [EN]

**G13. Decentralized**  
System architecture without central points of control or failure; distributes authority and decision-making across multiple nodes or participants; core principle of blockchain networks. Architectural implications: consensus mechanisms, distributed storage, peer-to-peer networking, governance models. Related: Centralized, Distributed, DAO [EN]

**G14. Tokenization**  
Process of converting rights to an asset into a digital token on a blockchain; can represent ownership, access, or utility rights for both digital and physical assets. Architectural implications: token standards, ownership tracking, transfer mechanisms, compliance controls. Related: ERC-20, Security Tokens, NFTs [EN]

**G15. DLT (Distributed Ledger Technology)**  
Consensus-based data structures maintained across multiple nodes without central authority; encompasses blockchain and other distributed database technologies. Architectural implications: consensus algorithms, node management, data synchronization, network protocols. Related: Blockchain, Hashgraph, DAG [EN]

**G16. Blockchain**  
Type of distributed ledger technology that organizes data into cryptographically linked blocks forming an immutable chain; enables trustless transactions and smart contracts. Architectural implications: block structure, mining/consensus, smart contracts, cryptographic hashing. Related: Bitcoin, Ethereum, Permissioned Chains [EN]

**G17. Cryptocurrency**  
Digital or virtual currency secured by cryptography; operates independently of central banks; includes Bitcoin, Ethereum, and thousands of altcoins. Architectural implications: cryptographic protocols, wallet systems, transaction validation, monetary policy. Related: Stablecoins, CBDCs, Altcoins [EN]

**G18. Zero-Knowledge Proof**  
Cryptographic method where one party can prove to another that a statement is true without revealing any information beyond the validity of the statement itself; used for privacy-preserving transactions and compliance. Architectural implications: privacy protection, verification efficiency, trust minimization, regulatory compliance. Related: zk-SNARKs, zk-STARKs, Zcash [EN]

### How to Find/Verify Regulations

**H1. Official Regulatory Sources**  
- EU Commission Legislative Observatory for MiCA and other EU regulations
- FATF website for Travel Rule guidelines and updates
- GDPR Portal for EU data protection regulations
- National regulatory authorities (BaFin, FCA, SEC, etc.) for jurisdiction-specific guidance

**H2. Standards Organizations**  
- ISO standards repository for information security standards
- NIST Computer Security Resource Center for cybersecurity frameworks
- EBA Guidelines database for European banking regulations

**H3. Legal Databases**  
- LexisNexis and Westlaw for legal interpretations
- SSRN and academic databases for regulatory research
- Industry whitepapers and compliance guides

### Compliance & Regulatory Tools

**T1. Chainalysis**  
Blockchain data platform for compliance, investigation, and market intelligence; provides transaction monitoring, wallet tagging, and regulatory reporting for cryptocurrency businesses. Compliance scope: AML/KYC, Travel Rule, sanctions screening. Certification support: Bank Secrecy Act, MiCA compliance. Audit capabilities: Transaction tracing, entity identification. Last update: 2024. Regulatory coverage: Global cryptocurrency regulations [EN]

**T2. TRM Labs**  
Crypto compliance and risk management platform offering transaction monitoring, sanctions screening, and investigative tools for digital asset businesses. Compliance scope: AML/KYC, Travel Rule, risk scoring. Certification support: FinCEN compliance, OFAC sanctions. Audit capabilities: Risk assessment, compliance reporting. Last update: 2024. Regulatory coverage: US, EU, global VASP regulations [EN]

**T3. Elliptic**  
Blockchain analytics company providing compliance solutions for financial institutions and cryptocurrency businesses; offers wallet screening, transaction monitoring, and investigative tools. Compliance scope: AML/KYC, sanctions compliance, suspicious activity detection. Certification support: BSA/AML compliance, regulatory reporting. Audit capabilities: Risk scoring, compliance dashboards. Last update: 2024. Regulatory coverage: Global cryptocurrency and banking regulations [EN]

**T4. Notabene**  
VASP compliance platform specializing in Travel Rule solutions and regulatory reporting for cryptocurrency service providers. Compliance scope: Travel Rule, VASP registration, compliance operations. Certification support: MiCA compliance, FATF guidelines implementation. Audit capabilities: Transaction reporting, compliance workflows. Last update: 2024. Regulatory coverage: FATF Travel Rule, MiCA, global VASP regulations [EN]

**T5. ComplyAdvantage**  
Financial crime prevention platform offering AML, sanctions, and PEP screening solutions with cryptocurrency coverage. Compliance scope: AML/KYC, sanctions screening, PEP monitoring. Certification support: BSA/AML compliance, regulatory reporting. Audit capabilities: Screening reports, compliance analytics. Last update: 2024. Regulatory coverage: Global AML/KYC regulations [EN]

**T6. SmartDec Scanner**  
Smart contract security auditing platform providing automated vulnerability detection and compliance checking for blockchain applications. Compliance scope: Smart contract security, code quality, best practices. Certification support: Security audits, vulnerability assessments. Audit capabilities: Code analysis, security reports. Last update: 2024. Regulatory coverage: Smart contract security standards [EN]

### Authoritative Regulatory Standards & Compliance Literature

**L1. Regulation (EU) 2023/1114 - MiCA**  
European Parliament and Council Regulation on markets in crypto-assets and amending Directive 2019/1937 (MiCA) [EN]

**L2. FATF Guidance for a Risk-Based Approach - Virtual Assets and VASPs**  
Financial Action Task Force Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers [EN]

**L3. Regulation (EU) 2016/679 - GDPR**  
European Parliament and Council Regulation on the protection of natural persons with regard to the processing of personal data and on the free movement of such data [EN]

**L4. Directive (EU) 2015/849 - Fourth Anti-Money Laundering Directive**  
European Parliament and Council Directive on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing [EN]

**L5. ISO/IEC 27001:2022 - Information Security Management**  
International standard for establishing, implementing, maintaining and continually improving an information security management system [EN]

**L6. NIST Cybersecurity Framework 2.0**  
National Institute of Standards and Technology Cybersecurity Framework for improving critical infrastructure cybersecurity [EN]

**L7. EBA Guidelines on ICT and security risk management**  
European Banking Authority Guidelines on Information and Communication Technology and security risk management (EBA/GL/2019/04) [EN]

**L8. SEC Digital Asset Securities Guidance**  
U.S. Securities and Exchange Commission guidance on digital asset securities and investment contract analysis [EN]

### APA Style Source Citations

**A1. European Parliament and Council. (2023). Regulation (EU) 2023/1114 of the European Parliament and of the Council of 31 May 2023 on markets in crypto-assets, and amending Directive 2019/1937 (MiCA). Official Journal of the European Union, L 114, 1-96.** [EN]

**A2. Financial Action Task Force. (2021). Guidance for a Risk-Based Approach - Virtual Assets and Virtual Asset Service Providers. Paris: FATF.** [EN]

**A3. European Parliament and Council. (2016). Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation). Official Journal of the European Union, L 119, 1-88.** [EN]

**A4. European Parliament and Council. (2015). Directive (EU) 2015/849 of the European Parliament and of the Council of 20 May 2015 on the prevention of the use of the financial system for the purposes of money laundering or terrorist financing. Official Journal of the European Union, L 141, 73-104.** [EN]

**A5. International Organization for Standardization. (2022). ISO/IEC 27001:2022 Information technology — Security techniques — Information security management systems — Requirements. Geneva: ISO.** [EN]

**A6. National Institute of Standards and Technology. (2024). NIST Cybersecurity Framework 2.0: Improving Critical Infrastructure Cybersecurity. Gaithersburg: NIST.** [EN]

**A7. European Banking Authority. (2019). EBA Guidelines on Information and Communication Technology and security risk management (EBA/GL/2019/04). Frankfurt: EBA.** [EN]

**A8. U.S. Securities and Exchange Commission. (2023). Digital Asset Securities: An Investor Bulletin. Washington: SEC.** [EN]

**A9. European Banking Authority. (2021). EBA Report on Distributed Ledger Technology in Payments. Frankfurt: EBA.** [EN]

**A10. Financial Stability Board. (2022). Regulatory issues of crypto-assets and global stablecoin arrangements. Basel: FSB.** [EN]

**A11. European Securities and Markets Authority. (2022). Report on Risks and Benefits of Crypto-Assets. Paris: ESMA.** [EN]

**A12. Commodity Futures Trading Commission. (2023). CFTC Primer on Virtual Currencies. Washington: CFTC.** [EN]
