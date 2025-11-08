### Comprehensive Report on Software Safety and Security for Smart Contract Engineers

Smart contracts, as self-executing code deployed on decentralized blockchain networks, form the foundational layer for complex applications in decentralized finance (DeFi), non-fungible tokens (NFTs), and GameFi. The role of a smart contract engineer is paramount in ensuring the safety and security of these systems, which manage significant financial value and sensitive digital assets across various blockchain ecosystems such as Ethereum (EVM), Solana, Aptos, and Sui. Unlike traditional software, the immutable nature of smart contracts means that deployed vulnerabilities can lead to irreversible financial losses, making a robust approach to safety and security indispensable throughout the entire development lifecycle.

### I. Safety Assurance in Smart Contracts

Safety assurance focuses on preventing unintended harm or system failures that could lead to economic loss, operational disruption, or user distress. For smart contracts, this involves identifying and mitigating hazards arising from logical flaws, unexpected states, or environmental factors.

#### Hazard Identification and Analysis

Systematic hazard analysis is crucial for smart contracts to uncover potential failure modes before deployment. Methods like Failure Mode and Effects Analysis (FMEA) or Bow-tie diagrams help break down complex contract interactions into manageable components, identifying where unintended behavior could occur. For instance, an external call failing or a state not updating correctly before a critical operation can be identified as a hazard leading to asset drain. These analyses prioritize risks based on their severity, occurrence, and detectability, often culminating in a Risk Priority Number (RPN) to guide mitigation efforts. The IEC 61508 standard provides a framework for functional safety, which can be adapted to specify safety integrity levels (SILs) for smart contract functions, demanding rigorous design and verification for critical operations.

#### Fail-Safe and Fail-Operational Design Patterns

In the event of an anomaly or fault, smart contracts can be designed to adopt specific behaviors to protect assets and maintain system integrity.
- ***Fail-Safe Design***: This principle ensures that a system, upon detecting a failure or critical anomaly, transitions into a predefined safe state, preventing further damage or loss. For smart contracts, this often manifests as an *emergency stop* or *kill switch* mechanism. When activated, a kill switch can halt transactions, trading, or other critical operations within the platform, safeguarding users' assets while an incident response team investigates and remediates. This is a crucial safety layer, similar to a circuit breaker, to freeze contract functions in emergencies. The European Union's Data Act has even mandated a "Mandatory Smart Contract Kill Switch" from January 11, 2024, sparking debates about its impact on decentralization and immutability.
- ***Fail-Operational Design***: While less common in smart contracts due to their immutable nature, fail-operational design aims for continued operation, albeit potentially with reduced functionality, even after a component failure. This might involve redundant components or processes that can take over seamlessly. In a blockchain context, this could relate to mechanisms like emergency upgrade capabilities that allow for deploying new, patched contract logic to restore full functionality following an incident, rather than a complete halt. However, this often introduces centralization risks and requires careful governance via multi-signature approvals or time-locked upgrades.

#### Redundancy and Fault Tolerance

Redundancy strategies ensure that if one part of the smart contract system fails, another component can take over, maintaining continuous service and protecting assets. For high-stakes DeFi protocols or NFT marketplaces, this can involve using diversified oracles to prevent single points of failure in price feeds, or employing multiple independent contracts for different core functionalities (e.g., order matching, payment processing) with cross-checking mechanisms. While true hardware-level redundancy is inherent to the blockchain network itself, smart contract developers can design software-level redundancy through modular architectures and robust error handling to enhance overall system resilience.

### II. Security Assurance in Smart Contracts

Security assurance focuses on protecting smart contracts from malicious attacks, unauthorized access, and data manipulation. This involves proactive threat identification, rigorous testing, and robust access controls.

#### Threat Modeling with STRIDE

Threat modeling is a structured process to identify potential threats, vulnerabilities, and countermeasures. The STRIDE framework (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege) is widely used to categorize threats against smart contract components and interactions. For instance, "Tampering" could relate to unauthorized modification of contract state, while "Denial of Service" could be achieved through excessive gas consumption. By applying STRIDE, engineers can systematically uncover weaknesses and design preventative controls, ensuring a comprehensive security posture for DeFi, NFT, and GameFi applications.

#### Common Smart Contract Vulnerabilities

Smart contracts are susceptible to various attack vectors, many of which have led to significant financial losses in the past.
- ***Reentrancy Attacks***: One of the most infamous vulnerabilities, reentrancy occurs when a contract calls an external contract before updating its own state, allowing the external contract to recursively call back into the vulnerable function and drain funds repeatedly. The historic DAO hack in 2016, which resulted in a $60 million loss, is a prime example of a reentrancy exploit. Mitigation strategies include the "checks-effects-interactions" (CEI) pattern, where state changes are performed before external calls, and using reentrancy locks (mutexes) to prevent recursive calls.
- ***Flash Loan Attacks***: Unique to DeFi, flash loan attacks involve borrowing large sums of assets without collateral, manipulating market prices or oracle feeds, and then repaying the loan within the same atomic transaction, all to profit from the manipulation. Examples include the Euler Finance attack in 2023 ($197 million stolen) and various attacks on DeFi platforms on Ethereum. Defenses include robust oracle validation, multi-oracle systems, and transaction pattern monitoring to detect and prevent price manipulation.
- ***Privilege Escalation***: These vulnerabilities occur when an attacker gains unauthorized, elevated permissions within a smart contract, potentially leading to control over critical functions or asset management. This can arise from insecure admin roles, improper access control implementations, or flaws in upgrade mechanisms. The `onlyOwner` pattern, widely adopted for access control, helps prevent such attacks by restricting sensitive functions to specific authorized addresses.
- ***OWASP Smart Contract Top 10***: Similar to its web application counterpart, the OWASP Smart Contract Top 10 (updated for 2025) provides an awareness document outlining the most critical security risks for Web3 developers and security teams. Key vulnerabilities listed include Access Control Vulnerabilities, Price Oracle Manipulation, Logic Errors, Lack of Input Validation, Reentrancy Attacks, and Unchecked External Calls. This framework guides the prioritization of security measures and helps in understanding the impact of gas limit issues.

#### Security Testing Methodologies and Tools

A multi-faceted approach to security testing is essential for smart contracts, combining automated tools with manual review.
- ***Static Application Security Testing (SAST)***: SAST tools analyze source code (e.g., Solidity, Rust, Move) or bytecode without execution to identify vulnerabilities early in the development cycle. *Slither*, developed by Trail of Bits, is a prominent static analysis framework for Solidity smart contracts, converting them into an intermediate representation called SlithIR to facilitate vulnerability detection and code optimization. It is fast, accurate, and outperforms other static analysis tools in speed and robustness. *MythX* is another tool that combines static, dynamic, and symbolic analysis for comprehensive auditing.
- ***Dynamic Application Security Testing (DAST)***: DAST tools test running smart contracts by interacting with them, simulating real-world attack scenarios to uncover vulnerabilities that might only manifest during execution.
- ***Fuzzing***: This automated technique generates a vast number of semi-random inputs to smart contract functions to trigger unexpected states, errors, or vulnerabilities. Modern fuzzers, such as Diligence Fuzzing, can perform gray-box, property-based fuzzing at scale, leveraging tools like the Harvey fuzzer. Fuzzing is crucial for uncovering reentrancy attacks, integer overflows, and other common pitfalls, and can even be tailored to discover profitable vulnerabilities for bug bounty programs.
- ***Penetration Testing***: Expert-driven penetration tests involve structured adversarial attempts to actively exploit vulnerabilities within a smart contract or protocol. This provides practical validation of attack vectors and assesses real-world impact.
- ***Formal Verification***: This rigorous process mathematically proves the correctness and safety properties of smart contract code against a formal specification, aiming to ensure the absence of certain vulnerabilities. While complex and resource-intensive, formal verification offers the highest level of assurance, particularly for critical financial smart contracts.

### III. Operational Resilience for Smart Contract Platforms

Operational resilience ensures that blockchain-based systems and smart contract platforms can withstand and recover from security incidents or operational failures, maintaining continuous and reliable service.

#### Monitoring and Anomaly Detection

Real-time monitoring of blockchain transactions, network activities, and smart contract states is critical for early detection of incidents. Anomaly detection systems, often leveraging machine learning and AI, analyze these data streams to identify unusual patterns that could indicate a security breach, such as flash loan attacks, liquidity drain risks, or unauthorized governance actions. Tools like ADvISE and BAD are designed to detect anomalous activities by analyzing blockchain metadata, including forks, to identify malicious requests. Integrating anomaly detection with decentralized identity management can enhance reliability by verifying the source of alerts, thereby reducing false positives.

#### Business Continuity Planning and Incident Response

A well-defined incident response plan is essential for containing damage and recovering from smart contract exploits. This includes:
- ***Emergency Upgrade Mechanisms and Kill Switches***: As discussed under fail-safe design, these are embedded controls that allow for rapid limitation, pausing, or termination of contract functionality during an exploit. For example, Solana network validators implemented an emergency update to address a serious security vulnerability. While providing critical safety nets, these mechanisms also require robust governance (e.g., multi-signature approvals, timelocks) to prevent their misuse. Frameworks like SEAM automate the conversion of standard Solidity contracts into upgradable versions to simplify this process.
- ***Post-Incident Audit Protocols***: After an incident, thorough security audits are conducted to perform root cause analysis, assess the vulnerability, and verify fixes. This often involves a combination of manual code review, automated analysis, and dynamic testing. Blockchain analytics and forensic services assist in tracing compromised funds and understanding the attack's scope and impact. These audits ensure that lessons learned are integrated into future development and security practices.

### IV. Compliance and Governance for Smart Contract Deployment

Compliance and governance define the legal, ethical, and operational framework for smart contract deployment, ensuring transparency, accountability, and adherence to regulatory mandates.

#### Audit Trails and Documentation Standards

Robust audit trails are critical for accountability, providing an immutable record of all smart contract transactions, state changes, and governance decisions. Blockchain's inherent immutability provides a strong foundation, but additional logging of off-chain events and administrative actions may be required. Comprehensive documentation standards mandate thorough records of development, testing, vulnerability assessments, and security audits to facilitate compliance verification and operational transparency.

#### Regulatory Frameworks

Smart contract deployments are increasingly subject to a range of regulatory frameworks:
- ***General Data Protection Regulation (GDPR)***: For smart contracts processing personal data, GDPR compliance mandates identifying roles (data controllers and processors), ensuring lawful processing bases, privacy-by-design principles, and mechanisms for data subject rights. This involves careful consideration of data handling on-chain and in related off-chain components.
- ***Financial Action Task Force (FATF) Travel Rule***: The FATF establishes standards to combat money laundering and terrorist financing, impacting Virtual Asset Service Providers (VASPs) that deploy smart contracts. The 'Travel Rule,' in force since March 2023, requires VASPs to collect and transmit originator and beneficiary information during virtual asset transfers, ensuring transaction traceability.
- ***International Standards (ISO/IEC, NIST)***: Standards such as ISO/IEC 27001 for information security management and the NIST Cybersecurity Framework (CSF) 2.0 (released in 2024) provide comprehensive guidelines for managing cybersecurity risk. These frameworks help organizations establish robust governance structures, access control policies, encryption best practices, and continuous risk assessment processes, securing both the technical codebase and operational aspects. IEC 62443 also applies for security in industrial automation and control systems, which can be relevant for smart contracts interacting with critical infrastructure.

#### Governance Models

Decentralized Autonomous Organizations (DAOs) are increasingly used for smart contract governance, allowing token holders to vote on critical decisions, including upgrades and emergency actions. This transparent, on-chain decision-making, exemplified by projects like Ethereum Name Service (ENS), helps maintain community oversight and trust. However, even DAOs require careful design to balance decentralization with the need for rapid response during security incidents. For instance, the Cetus Protocol exploit in 2025 on the Sui blockchain led to emergency halting of smart contract operations, triggering scrutiny over the Sui network's governance structure and the balance between decentralization and centralized control mechanisms.

### Conclusion

The multifaceted landscape of smart contract safety and security demands a highly skilled smart contract engineer proficient in multiple programming languages (Solidity, Move, Rust), deeply understanding blockchain ecosystems (Ethereum, Solana, Aptos, Sui), and well-versed in domain-specific challenges (DeFi, NFT, GameFi). Success hinges on a comprehensive approach encompassing proactive hazard and threat identification, rigorous testing using static analysis, fuzzing, and formal verification, robust operational resilience strategies including anomaly detection and emergency response, and strict adherence to evolving compliance and governance requirements. By integrating these practices, smart contract engineers can build resilient, trustworthy, and compliant decentralized applications that safeguard digital assets and foster confidence in the burgeoning blockchain economy.

Sources: 
[1] A Survey of Attacks on Ethereum Smart Contracts (SoK), https://www.semanticscholar.org/paper/aec843c0f38aff6c7901391a75ec10114a3d60f8
[2] Slither: A Static Analysis Framework for Smart Contracts, https://arxiv.org/abs/1908.09878
[3] A semantic framework for the security analysis of ethereum smart contracts, https://link.springer.com/chapter/10.1007/978-3-319-89722-6_10
[4] From manual to semi-automated safety and security requirements engineering: Ensuring compliance in industry 4.0, https://ieeexplore.ieee.org/abstract/document/10905636/
[5] Ethereum smart contracts: Security vulnerabilities and security tools, https://ntnuopen.ntnu.no/ntnu-xmlui/bitstream/handle/11250/2479191/18400_FULLTEXT.pdf
[6] Blockchain technology for managers, https://link.springer.com/content/pdf/10.1007/978-3-030-85716-5.pdf
[7] Protecting DeFi Platforms against Non-Price Flash Loan Attacks, https://dl.acm.org/doi/abs/10.1145/3714393.3726503
[8] How General Data Protection Regulation Advances and Harmonizes the International Controller, Processor and Data Subject Contracts, https://digitalcommons.law.ggu.edu/theses/93/
[9] RUNTIME DETECTION OF ATTACKS ON DEFI SMART CONTRACTS, https://theses.cz/id/v1dij5/xklima34-Runtime_detection_of_attacks_on_DeFi_smart_contr_Archive.pdf
[10] Enhancing Smart Contract Security: Front-running Flash Loan DeFi Attacks and Safeguarding Smart Contracts against Oracle Deviations, https://search.proquest.com/openview/f923d7f88b06452041acfeffa98251b5/1?pq-origsite=gscholar&cbl=18750&diss=y
[11] Interchain, https://www.taylorfrancis.com/books/9781000060164/chapters/10.1201/9780429324932-8
[12] Assessment of PVST in Accordance with IEC 61508: 2010, https://digital-library.theiet.org/doi/abs/10.1049/cp.2013.1702
[13] A Survey of Security Vulnerabilities in Ethereum Smart Contracts, https://www.semanticscholar.org/paper/982944afabe18dbdf2052a89276ea4a3118b148f
[14] Ethereum, https://www.semanticscholar.org/paper/3ead9ba6582992e9d4fbafaeacb8cdca7a549ad5
[15] IEC 60870-5-102\u6807\u51c6\u5728\u5b9e\u9645\u5e94\u7528\u4e2d\u7684\u63a2\u8ba8, https://www.semanticscholar.org/paper/cc162462fa86168144f97135f4d79b1942976afb
[16] Research on Database Audit Trail, https://www.semanticscholar.org/paper/23620db3d5f68eede1d6049cf759c8fd680fa729
[17] Ethereum Name Service: the Good, the Bad, and the Ugly, https://www.semanticscholar.org/paper/76c3d280863685564b0327fca5369d8581a16f16
[18] Accelerator Shutdown Report, https://www.semanticscholar.org/paper/0f8217816f3d102c57833e25666a89ed0ebd471c
[19] \u5341\u5927DeFi\u5b89\u5168\u6700\u4f73\u5b9e\u8df5 - Chainlink Blog, https://blog.chain.link/defi-security-best-practices-zh/
[20] \u6784\u5efa\u5b89\u5168\u7684DeFi\u667a\u80fd\u5408\u7ea6:\u4ece\u5ba1\u8ba1\u5230\u6f0f\u6d1e\u9632\u62a4\u7684\u7ec8\u6781\u6307\u5357 - \u4e91\u667a\u535a\u5ba2, https://www.weitip.com/news/8637.html
[21] DeFi '21: Proceedings of the 2021 ACM CCS Workshop on Decentralized Finance and Security, Virtual Event, Republic of Korea, 19 November 2021, https://www.semanticscholar.org/paper/7cfbf385f40783a11f4fd581187a84251c9fb30a
[22] DeFi\u4ee3\u5e01\u6388\u6743\u5b89\u5168\u6307\u5357\uff1a\u4fdd\u62a4\u60a8\u7684\u6570\u5b57\u8d44\u4ea7 - \u77e5\u4e4e\u4e13\u680f, https://zhuanlan.zhihu.com/p/1945617216922968558
[23] \u805a\u7126Solidity\u3001DeFi \u4e0e\u8de8\u94fe\u6865\uff1a\u786e\u4fddopBNB \u751f\u6001\u5b89\u5168\u53d1\u5c55 - \u767b\u94fe\u793e\u533a, https://learnblockchain.cn/article/6801
[24] An Introduction to Decentralized Finance (DeFi), https://www.semanticscholar.org/paper/015ed213c9398c10a4fea0eb09a29b7bd9816d81
[25] The Full Guide on Reentrancy Attacks in Solidity Smart Contracts, https://trustbytes.io/blog/reentrancy-attacks
[26] A Comprehensive Study of Exploitable Patterns in Smart Contracts: From Vulnerability to Defense, https://www.semanticscholar.org/paper/bfa376a611961664429bc4faa19d342067d95863
[27] Jyane: Detecting Reentrancy vulnerabilities based on path profiling method, https://www.semanticscholar.org/paper/d4a01b509e69575ccb05f2df71ae15d9d2dfd153
[28] The Traitor Within: Reentrancy Attacks Explained and Resolved, https://www.kayssel.com/post/web3-4/
[29] What are Flash Loan Attacks? - Amberdata Blog, https://blog.amberdata.io/flash-loan-attacks
[30] 10 smart contract vulnerabilities with code examples - Medium, https://medium.com/coinmonks/10-smart-contract-vulnerabilities-with-code-examples-38562685fca2
[31] [PDF] Evaluation of Real-world Attacks and Defenses in Ethereum ..., https://yinzhicao.org/smartcontract/everevolvinggame.pdf
[32] List: OWASP Smart Contract Security | Curated by AnonX - Medium, https://4n0nx.medium.com/list/owasp-smart-contract-security-f729e63e3339
[33] Smart Contract Security and Privacy Taxonomy, Tools, and Challenges, https://www.semanticscholar.org/paper/78f84f39102e9c61fe128e11c28dddb8c86b17b7
[34] Cybersecurity Risk Management Framework for Blockchain Identity ..., https://pmc.ncbi.nlm.nih.gov/articles/PMC9823375/
[35] 5 Biggest Flash Loan Attacks & Stats - Koinly, https://koinly.io/blog/biggest-flash-loan-attacks-stats/
[36] [PDF] Revisiting smart contract vulnerabilities in Hyperledger Fabric, https://repository.tudelft.nl/file/File_77d07e38-a851-482a-a1f4-739f4e4e5611
[37] Securing Your Smart Contracts: 3 Common Vulnerabilities & How to ..., https://www.wolfandco.com/resources/insights/securing-smart-contracts-3-common-vulnerabilities-prevent-them/
[38] VulnHunt-GPT: a Smart Contract vulnerabilities detector based on OpenAI chatGPT, https://dl.acm.org/doi/abs/10.1145/3605098.3636003
[39] Smart Contract Vulnerabilities, Tools, and Benchmarks: An Updated Systematic Literature Review, https://arxiv.org/abs/2412.01719
[40] OWASP Smart Contract Top 10, https://owasp.org/www-project-smart-contract-top-10/
[41] OWASP Smart Contract Security, https://scs.owasp.org/
[42] Smarts Contracts Security Tools Comparison: MythX, Mythril ..., https://dreamlab.net/en/blog/post/smarts-contracts-security-tools-comparison-mythx-mythril-securify-v2-0-and-slither-1/
[43] Detecting vulnerabilities in smart contract within blockchain: a review and comparative analysis of key approaches, https://ieeexplore.ieee.org/abstract/document/9932169/
[44] Smart Contract Formal Verification - Hacken, https://hacken.io/discover/formal-verification/
[45] The Feasibility of a Smart Contract \u201cKill Switch\u201d - arXiv, https://arxiv.org/html/2407.10302v1
[46] Kill Switch (emergency stop feature in smart contracts or DeFi ..., https://blog.ueex.com/crypto-terms/kill-switch-emergency-stop-feature-in-smart-contracts-or-defi-platforms/
[47] Best Practices for Writing Secure Smart Contract Code | Nethermind, https://www.nethermind.io/blog/best-practices-for-writing-secure-smart-contract-code
[48] Smart Contract \u201cKill Switch\u201d | Documentation - VERITAS PROTOCOL, https://docs.veritasprotocol.com/thesis/smart-contract-kill-switch
[49] Electronic Gyro Engine Kill Switch, https://www.semanticscholar.org/paper/213e2d6c6854c8210a245a5c2280e40bcfb0032a
[50] Incident Response for Crypto: Triage to Recovery - Veritas Protocol, https://www.veritasprotocol.com/blog/incident-response-for-crypto-triage-to-recovery
[51] Stewards and Gatekeepers: Human and Technological Agency in the Governance of DeFi Protocols, https://www.semanticscholar.org/paper/fa473c550200db336d7658c5605c47a2aee7d382
[52] Smart Contracts & Incident Response: Insight on Current Mechanisms, https://www.openzeppelin.com/news/smart-contracts-incident-response-insight-on-current-mechanisms
[53] Consensys Diligence: Smart Contract Audits, https://diligence.consensys.io/
[54] Smart Contract Audits for Web3, DeFi & Blockchain - Resonance, https://www.resonance.security/service/smart-contract-audits
[55] A Review on the Security of the Ethereum-Based DeFi Ecosystem, https://www.semanticscholar.org/paper/4d1e4ea3fecf720c899fe29118f569bdd59b9294
[56] Reentrancy Attacks and The DAO Hack Explained - Chainlink Blog, https://blog.chain.link/reentrancy-attacks-and-the-dao-hack/
[57] The Poly Network Hack: $600 Million in Crypto Stolen and Returned ..., https://www.elliptic.co/blog/the-poly-network-hack-600-million-in-crypto-stolen-and-returned-in-24-hours
[58] Wormhole Hack: Lessons From The Wormhole Exploit - Chainalysis, https://www.chainalysis.com/blog/wormhole-hack-february-2022/
[59] Cetus Hack Exposes Potential Centralization Risks in Sui Ecosystem, https://yellow.com/en-US/news/cetus-hack-exposes-potential-centralization-risks-in-sui-ecosystem
[60] What is a Reentrancy Attack? - CertiK, https://www.certik.com/resources/blog/what-is-a-reentracy-attack
[61] Fail-operational in safety-related automotive multi-core systems, https://ieeexplore.ieee.org/document/7185051/
[62] The Rise of DeFi: Smart Contracts and Collateral in the Digital Age, https://intacapitalswiss.com/the-rise-of-defi-smart-contracts-and-collateral-in-the-digital-age/
[63] FailSafe | Trusted Security & Compliance for Blockchain and AI, https://getfailsafe.com/
[64] Beyond the Audit: Fortifying Your DeFi Protocol with Operational ..., https://aitorzaldua.medium.com/beyond-the-audit-fortifying-your-defi-protocol-with-operational-security-892347419ad5
[65] Fail-safe and fail-operational systems safeguarded with coded processing, https://ieeexplore.ieee.org/document/6625234/
[66] A User-Centric Evaluation of Smart Contract Analysis Tools in Decentralised Finance (DeFi), https://link.springer.com/chapter/10.1007/978-981-19-6414-5_25
[67] Mapping the OWASP top ten to blockchain, https://www.sciencedirect.com/science/article/pii/S1877050920323589
[68] A Complete Guide to Smart Contract Security: From Slither to Foundry, https://medium.com/@anandi.sheladiya/a-complete-guide-to-smart-contract-security-from-slither-to-foundry-639b0a463d14
[69] Your Guide to Smart Contract Fuzzing in 2024 - QuillAudits, https://www.quillaudits.com/blog/smart-contract/smart-contract-fuzzing
[70] [PDF] Smart Contract Fuzzing Towards Profitable Vulnerabilities - arXiv, https://arxiv.org/pdf/2501.08834
[71] Fuzzing For L1 Protocols And Smart Contracts - Hacken.io, https://hacken.io/discover/fuzzing-for-blockchain/
[72] Top Free Smart Contract Security and Audit Tools 2025 - Hashlock, https://hashlock.com/blog/top-free-smart-contract-security-and-audit-tools-2025
[73] An�lise das Ferramentas de Detec�ao de Vulnerabilidades para Contratos Inteligentes de Blockchains EVM, https://sol.sbc.org.br/index.php/wblockchain/article/view/35472
[74] OWASP IoT top 10 based attack dataset for machine learning, https://ieeexplore.ieee.org/abstract/document/9728969/
[75] Best Smart Contract Auditing and Security Tools - Cyfrin, https://www.cyfrin.io/blog/industry-leading-smart-contract-auditing-and-security-tools
[76] Custom Fuzzing for Smart Contract Security - Cantina.xyz, https://cantina.xyz/blog/custom-fuzzing-for-smart-contract-security
[77] Penetration Testing of Web Applications in a Bug Bounty Program, https://www.semanticscholar.org/paper/171ce668aa9e3dfe6dac0894d360ca3752316c0b
[78] SmartFuzzDriverGen: Smart Contract Fuzzing Automation for Golang, https://www.semanticscholar.org/paper/2608aca33210d56ce234f5d55f4645350a4f03f9
[79] Smart Contract Weakness Analyzer Based on Concolic Testing, https://www.semanticscholar.org/paper/ccae43c124e00521f0990c691b5cdf3a345383e7
[80] S-1 - SEC.gov, https://www.sec.gov/Archives/edgar/data/2035053/000095017025111074/ck0002035053-20250823.htm
[81] Solana's emergency update raised concerns about centralization, https://www.binance.com/en/square/post/23880115232649
[82] Blockchain Network Resilience in DeFi: Operational Risk ... - AInvest, https://www.ainvest.com/news/blockchain-network-resilience-defi-operational-risk-management-recovery-strategies-2025-2509/
[83] ADvISE: Anomaly Detection tool for blockchaIn SystEms, https://ieeexplore.ieee.org/document/8495798/
[84] AI Anomaly Detection with Decentralized Identity Management on Blockchain, https://ieeexplore.ieee.org/document/10677323/
[85] Blockchain Attack Discovery via Anomaly Detection, https://www.semanticscholar.org/paper/c0ac82c8cd3ad06d640c2db3bc41fcdfcc165b9a
[86] [PDF] Leveraging AI-powered data streams for predictive risk assessment ..., https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-2875.pdf
[87] [PDF] Decentralized Finance (Defi) Security: Ai-Based Risk Detection, https://rjwave.org/ijedr/papers/IJEDR2503016.pdf
[88] BAD: Blockchain Anomaly Detection, https://www.semanticscholar.org/paper/b4c43fb31f50266192c9cc3e0b2bdef867951fc0
[89] Incident Response Planning for Blockchain Technologies: A Vital ..., https://deepdive.world/list-of-cyber-security-services/blockchain-security/incident-response-planning/
[90] Blockchain Security 101 Key Features, Importance & Best Practices, https://www.rapidinnovation.io/post/blockchain-security-best-practices-common-threats
[91] Crypto Travel Rule Guide 2025 - Sumsub, https://sumsub.com/blog/what-is-the-fatf-travel-rule/
[92] A Practical Guide to Controller-Processor Contracts, http://www.dataprotection.ie/en/dpc-guidance/data-processing-agreements
[93] Chapter 11: Obligations of processors \u2013 Unlocking the EU General ..., https://www.whitecase.com/insight-our-thinking/chapter-11-obligations-processors-unlocking-eu-general-data-protection
[94] [PDF] Best Practices on Travel Rule Supervision - FATF, https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/Best-Practices-Travel-Rule-Supervision.pdf
[95] Everything VASPs Need to Know about the FATF Travel Rule, https://www.21analytics.ch/what-is-the-fatf-travel-rule/
[96] A Holistic Approach to Smart Contract Security, https://www.semanticscholar.org/paper/94777c6328ab419387461843a74b403da53e19a8
[97] A comprehensive survey of smart contract security: State of the art and research directions, https://linkinghub.elsevier.com/retrieve/pii/S1084804524000596
[98] SEAM: A Secure Automated and Maintainable Smart Contract Upgrade Framework, https://arxiv.org/abs/2412.00680
[99] Smart Contract Kill Switch for Security in a Private Blockchain-based Software Transaction System, https://ieeexplore.ieee.org/document/10810726/
[100] Top 7 Solidity Vulnerabilities Every Auditor Should Know in 2025, https://medium.com/coinmonks/top-7-solidity-vulnerabilities-every-auditor-should-know-in-2025-fc512b8d4d6c
[101] Vyper: A Security Comparison with Solidity Based on Common Vulnerabilities, https://arxiv.org/abs/2003.07435
[102] Revisiting interlibrary loan best practices: still viable?, https://www.semanticscholar.org/paper/548ce9e7f5ceb4a47eb00af10a56a9bd2d548c24
[103] A Broad Overview of Reentrancy Attacks in Solidity Contracts, https://www.quicknode.com/guides/ethereum-development/smart-contracts/a-broad-overview-of-reentrancy-attacks-in-solidity-contracts
[104] Hybrid Locking: An Effective Measure Against Reentrancy Attacks, https://www.semanticscholar.org/paper/27ca062807c07b1ec8c46dd99c86c4966b267044
[105] A Survey on Formal Verification for Solidity Smart Contracts, https://www.semanticscholar.org/paper/98c27dfc539a9cb33ccd483dd16c39d9dc8677d7
[106] An Empirical Analysis of Vulnerability Detection Tools for Solidity Smart Contracts Using Line Level Manually Annotated Vulnerabilities, https://arxiv.org/abs/2505.15756
[107] Formal Specification and Verification of Solidity Contracts with Events, https://www.semanticscholar.org/paper/2d17d63001f0a4502d7df8f00c77c38914cf1c75
[108] crytic/slither: Static Analyzer for Solidity and Vyper - GitHub, https://github.com/crytic/slither
[109] Slither: The Essential Static Analysis Tool Every Solidity Developer ..., https://medium.com/@BizthonOfficial/slither-the-essential-static-analysis-tool-every-solidity-developer-needs-for-bulletproof-smart-06356da0cc44
[110] E-Voting System Using Solana Blockchain, https://ieeexplore.ieee.org/document/10352452/
[111] TotalSol: A Multi-Layer Static Analysis Method for Vulnerability Detection in Ethereum Based Smart Contracts, https://ieeexplore.ieee.org/document/10990789/
[112] Lollipop: SVM Rollups on Solana, https://arxiv.org/abs/2405.08882
[113] �scar Gonz�lez Guti�rrez - Solana, https://www.semanticscholar.org/paper/a86d67419b2a95b5f092867c8bfb9839ea2b891c
[114] SolMover: Smart Contract Code Translation Based on Concepts, https://www.semanticscholar.org/paper/4760b2a1e3a4eb1c822dbd94574aef77eb499b31
[115] Evaluating and improving static analysis tools via differential mutation analysis, https://ieeexplore.ieee.org/abstract/document/9724764/
[116] \u9879\u76ee\u4ecb\u7ecd - OWASP\u4e2d\u56fd, http://www.owasp.org.cn/OWASP-CHINA/owasp-project/
[117] \u57fa\u4e8e\u533a\u5757\u94fe\u6280\u672f\u7684\u8bed\u8a00\u6559\u5b66\u7814\u7a76\u7efc\u8ff0\u53ca\u5176\u53d1\u5c55\u524d\u666f, https://www.hanspub.org/journal/paperinformation?paperID=103671
[118] OWASP Reveals Top 10 Smart Contract Vulnerabilities For 2025, https://www.linkedin.com/pulse/owasp-reveals-top-10-smart-contract-vulnerabilities-eyfte
[119] [PDF] TARGETED UPDATE ON IMPLEMENTATION OF THE FATF ..., https://www.fatf-gafi.org/content/dam/fatf-gafi/recommendations/2024-Targeted-Update-VA-VASP.pdf.coredownload.inline.pdf
[120] \u91d1\u878d\u884c\u52a8\u7279\u522b\u5de5\u4f5c\u7ec4\u52a0\u5bc6\u6307\u5357\uff1a\u4fdd\u969c\u52a0\u5bc6\u8d27\u5e01\u884c\u4e1a\u5b89\u5168 - ComplyCube, https://www.complycube.com/zh/%E9%87%91%E8%9E%8D%E8%A1%8C%E5%8A%A8%E7%89%B9%E5%88%AB%E5%B7%A5%E4%BD%9C%E7%BB%84-fatf-%E5%8A%A0%E5%AF%86%E6%8C%87%E5%8D%97%E7%A1%AE%E4%BF%9D%E8%A1%8C%E4%B8%9A%E5%AE%89%E5%85%A8/
[121] [PDF] S/2025/22 - \u5b89\u5168\u7406\u4e8b\u4f1a, https://docs.un.org/zh/S/2025/22
[122] FATF \u865b\u64ec\u8cc7\u7522\u53cd\u6d17\u9322\u6a19\u6e96\u9032\u5c55\u5831\u544a\uff1a75% \u53f8\u6cd5\u7ba1\u8f44\u5340\u90fd\u6c92\u505a\u597d - \u93c8\u65b0\u805e, https://abmedia.io/fatf-aml-cft-standard-report
[123] OWASP Top 10 Vulnerabilities 2025: A Comprehensive Guide, https://infosecwriteups.com/owasp-top-10-vulnerabilities-2025-a-comprehensive-guide-cc0019ded233
[124] Top10:2023 - OWASP Smart Contract Security, https://scs.owasp.org/sctop10/Top10%3A2023/
[125] Comparative Analysis of Large Language Models in Solidity Smart Contract Vulnerability Detection, https://ieeexplore.ieee.org/abstract/document/10959494/
[126] OWASP Top Ten, https://owasp.org/www-project-top-ten/
[127] Increasing smart contracts security by reducing false alarms - arXiv, https://arxiv.org/html/2410.17204v1
[128] OWASP Smart Contract Security (SCS) Project - GitHub, https://github.com/OWASP/owasp-scs
[129] Iec 61508-2 (2010) PDF - Scribd, https://www.scribd.com/document/449110253/IEC-61508-2-2010-pdf
[130] Mitigating the Risk of Reentrancy Attack in Smart Contract Development, https://www.semanticscholar.org/paper/355c0762ae19d06f24882f7160785b37c1352ce7
[131] Ensuring wallet application security by resolving reentrancy attacks in blockchain smart contracts, https://www.semanticscholar.org/paper/085119707d6624259a1d5c3361d15f0e4849f0e4
[132] A Static Analysis Approach to Flash Loan Vulnerabilities - arXiv, https://arxiv.org/html/2411.01230v1
[133] Poly Network exploit - Wikipedia, https://en.wikipedia.org/wiki/Poly_Network_exploit
[134] Learning from DeFi Security Breaches: 5 Case Studies, https://blocktelegraph.io/learning-from-defi-security-breaches-case-studies/
[135] Functional safety IEC 61508 / IEC 61511 the impact to certification and the user, https://ieeexplore.ieee.org/document/4493673/
[136] IEC 61508/61511\u2014Pain or gain?, https://aiche.onlinelibrary.wiley.com/doi/10.1002/prs.680220205
[137] [PDF] SAFETY INSTRUMENTED SYSTEMS - G.M. International, https://gminternational.com/inc/inc_getfile.cfm?ID=MSD0142&w=MSD
[138] [PDF] The Safety Critical Systems Handbook - hsse world, https://hsseworld.com/wp-content/uploads/2021/06/The-Safety-Critical-Systems-Handbook.pdf
[139] [PDF] IEC 61508 Commented Version.pdf, https://share.ansi.org/Shared%20Documents/News%20and%20Publications/Other%20Documents/IEC%2061508%20Commented%20Version.pdf
[140] [PDF] The NIST Cybersecurity Framework (CSF) 2.0, https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf
[141] [PDF] NIST.SP.800-61r3.pdf, https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r3.pdf
[142] Cybersecurity Framework v2.0 - CSF Tools, https://csf.tools/reference/nist-cybersecurity-framework/v2-0/
[143] The Ultimate Guide To Reentrancy - Immunefi, https://immunefi.com/blog/expert-insights/ultimate-guide-to-reentrancy/
[144] Have I Been Exploited? - A Registry of Vulnerable Ethereum Smart Contracts, https://www.semanticscholar.org/paper/601347c944977041bc018bdc8cfc4e081ceca189
[145] SWC-134 - Smart Contract Weakness Classification (SWC), https://swcregistry.io/docs/SWC-134/
[146] Security Analysis Tools for Solidity Smart Contracts: A Comparison Based on Real-World Exploits., https://webthesis.biblio.polito.it/25563/
[147] MEMBANGUN APLIKASI PEMBELAJARANSECURE WEB PROGRAMMINGBERBASIS OWASP TOP 10, https://www.semanticscholar.org/paper/efdaa146735e0f284bbe408c0299aac49dc178b0
[148] FATF urges stronger global action to address Illicit Finance Risks in ..., https://www.fatf-gafi.org/en/publications/Fatfrecommendations/targeted-update-virtual-assets-vasps-2025.html
[149] FATF Travel Rule - Merkle Science, https://www.merklescience.com/blog/fatfs-travel-rule-and-its-impact-on-vasps
[150] Mobile Health Application Security Assesment Based on OWASP Top 10 Mobile Vulnerabilities, https://www.semanticscholar.org/paper/a1c0229d4a34b1b31e3ae3adf39041a52e5d7e43
[151] ISO-27001, ISA/IEC-62443, and NIST CSF, https://www.intechww.com/iso-27001-isa-iec-62443-and-nist-csf-selecting-the-right-standard-framework-for-your-ot-cybersecurity-program/
[152] Cybersecurity Framework | NIST, https://www.nist.gov/cyberframework
[153] Security standard compliance and continuous verification for ..., https://journals.sagepub.com/doi/full/10.1177/1550147720922731
[154] Navigating Supply Chain Cyber Risk, https://www.semanticscholar.org/paper/ac8088ef7f6831385f8b4a0cdd7b586e6afdc931
[155] Senior Executives' Strategic Edicts for Consistent Information Technology Metrics over Asset Management, https://search.proquest.com/openview/50e44e354effb60f866130d7d307bc50/1?pq-origsite=gscholar&cbl=18750&diss=y
[156] 1Sandia National Laboratories, https://www.sandia.gov/app/uploads/sites/273/2024/11/Test-Platform-Survey-and-Wireless-Test-Requirements-Outline.pdf
[157] The NIST CSF 2.0 is Here! | CSRC, https://csrc.nist.gov/news/2024/the-nist-csf-20-is-here
[158] NIST Releases Version 2.0 of Landmark Cybersecurity Framework, https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework
[159] Understanding the 2024 Updates to the NIST Cybersecurity ..., https://crfsecure.org/understanding-the-2024-updates-to-the-nist-cybersecurity-framework/
