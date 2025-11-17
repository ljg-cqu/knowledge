### The Role of Architecture in Stablecoin Projects

#### Q1: How do different blockchain architectures impact the design and stability mechanisms of stablecoins, considering both single-chain and multi-chain implementations?
**Difficulty:** Advanced | **Type:** Theoretical

**Answer:**
Blockchain architectures significantly influence stablecoin design and stability mechanisms, with distinct implications for single-chain and multi-chain implementations. Single-chain stablecoins, such as MakerDAO's DAI on Ethereum, rely on the underlying blockchain's security, consensus, and transaction finality for their operational integrity. The stability mechanisms for these typically involve smart contracts that algorithmically manage collateral or supply to maintain a peg, as seen in DAI's design which uses a web of smart contracts. However, being tied to a single chain means they are susceptible to that chain's congestion, fees, and potential vulnerabilities, which can affect arbitrage efficiency and peg stability. In contrast, multi-chain stablecoins aim to enhance interoperability and reduce reliance on a single ecosystem, but this introduces new architectural complexities. Cross-chain transfers often rely on centralized intermediaries, which can compromise the decentralization ideology of blockchains. Achieving trustless cross-chain stability requires robust interoperability protocols that ensure consistent peg maintenance across diverse blockchain environments, a challenge that current solutions are actively addressing. Frax, for instance, proposes a fractional-algorithmic protocol that transitions from fully collateralized to algorithmic, leveraging two tokens, FRAX and FXS, where FXS captures seigniorage value as collateralization decreases. The Frax protocol is a fully autonomous blockchain protocol, designed to maintain stability through algorithmic trading and smart contracts.

**Key Insight:** **Trade-offs** - Single-chain stablecoins offer simpler integration but suffer from single point of failure and scalability limitations of their host chain, while multi-chain stablecoins enhance reach and resilience but introduce significant interoperability and centralization risks.

**Supporting Artifacts:**

#### Q2: Explain the technical components and interactions within a fiat-backed stablecoin architecture, focusing on the roles of the issuer, reserve management, and the on-chain representation of value.
**Difficulty:** Intermediate | **Type:** Practical

**Answer:**
In a fiat-backed stablecoin architecture, such as Tether (USDT) or USD Coin (USDC), the technical components and their interactions are designed to maintain a 1:1 peg to a fiat currency like the US dollar. The primary components include the issuer, the reserve management entity, and the on-chain representation of the stablecoin. The **issuer** is typically a centralized entity responsible for minting new stablecoins and burning existing ones, directly correlating with the amount of fiat currency held in reserve. This entity also handles the redemption process, allowing users to convert their stablecoins back to fiat. **Reserve management** is critical; the issuer maintains a reserve of the pegged fiat currency or highly liquid fiat-denominated assets, such as bank deposits and government securities, to back the stablecoins in circulation. The integrity and transparency of these reserves are paramount for maintaining user trust and the stablecoin's peg. The **on-chain representation of value** involves the stablecoin existing as a token on one or more blockchains (e.g., Ethereum, Tron), where its transfer and ownership are recorded. These tokens are often implemented using standard smart contract interfaces, like ERC-20, to ensure compatibility across various decentralized applications and wallets. The interactions ensure that for every stablecoin issued, there is an equivalent value held in reserve, and the infrastructure allows for transferring and potentially redeeming these coins.

**Key Insight:** **Failure Path** - A critical failure path for fiat-backed stablecoins lies in opaque or insufficient reserve management, which can lead to a loss of trust and de-pegging from the underlying fiat currency.

#### Q3: How do oracle systems contribute to the stability and functionality of crypto-collateralized stablecoins, and what are the security considerations for their integration?
**Difficulty:** Advanced | **Type:** Theoretical

**Answer:**
Oracle systems are indispensable for the stability and functionality of crypto-collateralized stablecoins, such as DAI, by providing real-world price data to the blockchain. These systems act as bridges, feeding off-chain information, specifically the current market price of the collateralized cryptocurrency, into the on-chain smart contracts that govern the stablecoin. This price data is crucial for mechanisms like liquidation and collateralization ratio adjustments, which automatically execute to maintain the stablecoin's peg. For instance, if the value of the underlying cryptocurrency collateral drops significantly, the oracle system would trigger a liquidation event to prevent the stablecoin from becoming under-collateralized. The design of these arbitrage mechanisms, facilitated by oracles, is critical in stabilizing the price of dominant stablecoins like DAI. However, integrating oracle systems introduces significant security considerations. Oracles are potential attack vectors; if an oracle feeds manipulated or incorrect price data to the smart contract, it could lead to improper liquidations, system instability, or even the collapse of the stablecoin. Therefore, secure oracle solutions typically involve decentralization, aggregation of data from multiple sources, and reputation mechanisms to ensure data integrity and prevent single points of failure. The reliability of the oracle system directly impacts the resilience of the stablecoin's peg and its overall security.

**Key Insight:** **Failure Path** - The integrity of crypto-collateralized stablecoins is highly dependent on the security and reliability of their oracle systems; a compromised oracle can lead to systemic failure and de-pegging events.

#### Q4: Discuss the architectural differences and trade-offs between algorithmic and collateral-backed stablecoins, particularly concerning their resilience to market shocks and governance models.
**Difficulty:** Advanced | **Type:** Theoretical

**Answer:**
Algorithmic and collateral-backed stablecoins represent fundamentally different architectural approaches with distinct trade-offs in resilience to market shocks and governance models. **Collateral-backed stablecoins**, which include both fiat-backed (like USDT) and crypto-collateralized (like DAI), rely on tangible assets held in reserve to maintain their peg. Fiat-backed stablecoins are typically centralized and their stability depends on the issuer's solvency and the transparency of their reserves. Crypto-collateralized stablecoins, often decentralized, maintain their peg through over-collateralization and liquidation mechanisms governed by smart contracts and oracles. Their resilience hinges on the stability and liquidity of their underlying collateral. In contrast, **algorithmic stablecoins** aim to maintain their peg through programmatic adjustments of supply and demand, without direct collateral backing. This often involves a two-token system where a secondary token absorbs volatility or acts as a governance token, as seen in the now-defunct UST and its Luna token. While algorithmic stablecoins offer decentralization and capital efficiency, they are inherently more vulnerable to market shocks and speculative attacks due to their reliance on economic incentives and market dynamics rather than tangible reserves. The collapse of UST in 2022 exemplifies this fragility, highlighting that these designs can suffer from downward price instability when exposed to external market risk and poor financial performance. Their governance models vary, with collateral-backed stablecoins having either centralized control or decentralized autonomous organizations (DAOs), while algorithmic stablecoins typically rely on decentralized governance for protocol adjustments. A key challenge for all stablecoin designs is avoiding a trilemma of price instability risks, including moral hazards of the operating entity, exposure to external market risk, and limited coin supply.

**Key Insight:** **Trade-offs** - Algorithmic stablecoins offer decentralization and capital efficiency but possess lower resilience to market shocks compared to collateral-backed stablecoins, which trade some decentralization for tangible asset backing.

#### Q5: Evaluate the security challenges inherent in stablecoin designs, covering smart contract vulnerabilities, oracle manipulation, and systemic risks associated with decentralized finance (DeFi) integration.
**Difficulty:** Advanced | **Type:** Theoretical

**Answer:**
Stablecoin designs face a multitude of inherent security challenges, encompassing smart contract vulnerabilities, oracle manipulation, and systemic risks arising from their deep integration within decentralized finance (DeFi). **Smart contract vulnerabilities** are a primary concern, as stablecoins heavily rely on these self-executing agreements for their operational logic, collateral management, and stability mechanisms. Flaws in the code can be exploited by attackers, leading to loss of funds, unauthorized minting, or failure to maintain the peg. Audits and formal verification are critical but do not guarantee complete immunity from such exploits. **Oracle manipulation** poses another significant threat, particularly for crypto-collateralized and algorithmic stablecoins that depend on external price feeds. If an oracle is compromised or feeds incorrect data, it can trigger erroneous liquidations, destabilize collateral ratios, and lead to a de-pegging event. Decentralized oracle networks and robust data aggregation strategies are employed to mitigate this risk, but they remain a complex challenge. Furthermore, the growing integration of stablecoins into **DeFi ecosystems** introduces **systemic risks**. Stablecoins are a cornerstone of many DeFi protocols, and a significant de-pegging event or a "bank run" on a major stablecoin can trigger cascading failures across the entire DeFi landscape, as evidenced by the collapse of Iron Finance's IRON stablecoin. These interconnected systems amplify the impact of individual vulnerabilities, making stablecoin stability a concern for the broader financial system. The complex and novel cross-border regulatory challenges further complicate the security landscape, requiring both technical and policy-based solutions.

**Key Insight:** **Failure Path** - The intricate interconnectedness of stablecoins within the DeFi ecosystem means that smart contract vulnerabilities, oracle manipulation, or a significant de-pegging event in one stablecoin can trigger widespread systemic risks, leading to cascading failures across the entire decentralized financial landscape.

#### Q6: Analyze the mechanisms used to ensure price stability in stablecoins, detailing how arbitrage opportunities, collateralization ratios, and algorithmic adjustments contribute to maintaining the peg.
**Difficulty:** Intermediate | **Type:** Theoretical

**Answer:**
The price stability of stablecoins is maintained through various mechanisms, primarily leveraging arbitrage opportunities, collateralization ratios, and algorithmic adjustments. **Arbitrage opportunities** are a fundamental force; when a stablecoin deviates from its peg (e.g., trading at $0.99 or $1.01 instead of $1.00), arbitrageurs buy or sell the stablecoin to profit from the price discrepancy, thereby pushing its price back towards the peg. For fiat-backed stablecoins, this involves redeeming undervalued stablecoins for fiat or buying undervalued stablecoins to mint new ones. For crypto-collateralized stablecoins, arbitrage mechanisms are enhanced by design, improving their ability to stabilize the price. **Collateralization ratios** are crucial for crypto-collateralized stablecoins. These stablecoins are typically over-collateralized (e.g., $1.50 worth of crypto collateral for every $1 stablecoin) to absorb price fluctuations of the underlying collateral. Smart contracts monitor these ratios and initiate liquidations if the collateral value falls below a certain threshold, preventing the stablecoin from becoming under-backed. **Algorithmic adjustments** are central to algorithmic stablecoins, which do not rely on direct collateral. Instead, they use smart contracts to programmatically expand or contract the stablecoin supply in response to price deviations. For instance, if the price falls below the peg, the system might reduce supply by burning stablecoins or encouraging users to stake them for a reward. Conversely, if the price rises above the peg, new stablecoins might be minted to increase supply. The interplay of these mechanisms, often requiring regular tuning of system parameters due to dynamic market prices, is essential for maintaining a consistent exchange rate to the pegged price.

**Key Insight:** **Trade-offs** - While arbitrage and collateralization provide robust stability for asset-backed stablecoins, algorithmic adjustments, despite offering capital efficiency, introduce greater complexity and vulnerability to extreme market conditions due to their reliance on programmed incentives rather than tangible backing.

### Table: Stablecoin Type Comparison

| Feature | Fiat-Backed Stablecoins (e.g., USDT, USDC) | Crypto-Collateralized Stablecoins (e.g., DAI) | Algorithmic Stablecoins (e.g., Terra UST - defunct) |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Collateral Type** | Fiat currency (USD, EUR) or fiat-denominated assets                                                                            | Cryptocurrencies (e.g., ETH)                                           | None (relies on algorithms and secondary tokens)                                                                                                                             |
| **Stability Mechanism** | Arbitrage based on 1:1 redemption with fiat reserves                                                                           | Over-collateralization, liquidation, arbitrage, smart contracts | Algorithmic supply/demand adjustments, burning/minting mechanisms                                                                                                     |
| **Centralization Level** | Centralized (issuer holds reserves, conducts audits)                                                                            | Decentralized (governed by DAOs, smart contracts)                      | Decentralized (governed by protocols)                                                                                                                                        |
| **Resilience to Market Shocks** | High (backed by stable fiat currency)                                                                                          | Moderate to High (dependent on collateral volatility and over-collateralization) | Low (highly vulnerable to speculative attacks, economic incentive failures)                                                                                                  |
| **Transparency** | Dependent on issuer's audits and attestations                                                                                    | High (on-chain collateral, transparent smart contract logic)           | High (on-chain algorithmic logic)                                                                                                                                            |
| **Key Risk** | Issuer solvency, regulatory risk, reserve auditing                                                                               | Oracle manipulation, collateral price crashes, governance risks | De-pegging, death spirals, lack of real-world backing, incentive misalignment                                                                                            |
| **Examples** | USDT, USDC                                                                                                                        | DAI                                                                    | Terra UST (defunct), Frax (fractional-algorithmic)                                                                                                             |

### Glossary, Terminology & Acronyms
**G1: Stablecoin**: A type of cryptocurrency designed to maintain a stable value relative to a specific asset or a basket of assets, such as fiat currency.
**G2: Blockchain**: A decentralized, distributed ledger technology that records transactions across many computers.
**G3: Smart Contract**: A self-executing contract with the terms of the agreement directly written into code, running on a blockchain.
**G4: Oracle System**: A service that connects smart contracts with real-world data and external systems.
**G5: Collateral**: An asset pledged by a borrower to a lender to secure a loan.
**G6: Peg**: The fixed exchange rate or value that a stablecoin aims to maintain against a reference asset, typically a fiat currency.
**G7: Decentralized Finance (DeFi)**: An umbrella term for financial applications built on blockchain technology, aiming to disintermediate traditional financial services.
**G8: Fiat-backed Stablecoin**: A stablecoin whose value is pegged to and backed by an equivalent amount of fiat currency held in reserve.
**G9: Crypto-collateralized Stablecoin**: A stablecoin whose value is pegged to and backed by other cryptocurrencies held in reserve, often over-collateralized.
**G10: Algorithmic Stablecoin**: A stablecoin that uses algorithms and smart contracts to maintain its peg without direct collateral backing, by adjusting supply and demand.
**G11: De-pegging**: The event where a stablecoin loses its intended fixed exchange rate or value against its pegged asset.

### Authoritative Literature & Reports
**L1: Stablecoins: risks, potential and regulation** (2020) ()
- Findings: Discusses the value backing of single-currency stablecoins and the broader architecture.
- Method: Article review for Banco de España Financial Stability Review.
- Impact: Provides insights into stablecoin architecture and regulatory considerations.
- DOI/URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3979495

**L2: What keeps stablecoins stable?** (2023) ()
- Findings: Quantifies how improved arbitrage design stabilizes the price of dominant stablecoins like DAI, using trades between the stablecoin treasury and private investors.
- Method: Uses trades between stablecoin treasury and private investors.
- Impact: Offers a quantitative understanding of stability mechanisms.
- DOI/URL: https://www.sciencedirect.com/science/article/pii/S0261560622001802

**L3: Stablecoins 2.0: Economic foundations and risk-based models** (2020) ()
- Findings: Provides a framework for evaluating non-custodial stablecoins and measuring stability and security.
- Method: Theoretical framework and review of models.
- Impact: Contributes to the understanding of stablecoin security and stability frameworks.
- DOI/URL: https://dl.acm.org/doi/abs/10.1145/3419614.3423261

**L4: Stablecoins** (2023) ()
- Findings: Discusses stablecoin design options, history, and challenges, including the emergence of competing fiat-backed stablecoin projects like USDC.
- Method: General discussion and outline of stablecoin evolution.
- Impact: Provides an overview of stablecoin development and challenges.
- DOI/URL: https://www.emerald.com/insight/content/doi/10.1108/978-1-80455-320-620221007

**L5: Examining User Perceptions of Stablecoins: Understandings and Risks** (2023) ()
- Findings: Investigates stablecoins' roles within the blockchain ecosystem and their effects on Bitcoin and the wider cryptocurrency market.
- Method: Technical and theoretical investigation of stablecoins.
- Impact: Offers insights into stablecoin integration and market effects.
- DOI/URL: https://www.usenix.org/system/files/soups2023-poster160_guan_abstract_final.pdf

**L6: Can stablecoins be stable?** (2022) ()
- Findings: Provides a general framework for analyzing stablecoin stability, showing how decentralized models transform.
- Method: General framework for stability analysis.
- Impact: Offers theoretical grounding for stablecoin stability assessment.
- DOI/URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4226027

**L7: The four types of stablecoins: A comparative analysis** (2023) ()
- Findings: Assesses the stability of each stablecoin type using an agent-based modeling approach.
- Method: Agent-based modeling.
- Impact: Provides comparative analysis of stablecoin stability.
- DOI/URL: https://arxiv.org/abs/2308.07041

**L8: What is stablecoin?: A survey on its mechanism and potential as decentralized payment systems** (2020) ()
- Findings: Discusses the use of crypto-collateralized and non-collateralized stablecoins as decentralized payment systems.
- Method: Survey on stablecoin mechanisms.
- Impact: Explores the potential of stablecoins in decentralized payments.
- DOI/URL: https://iaiai.org/journals/index.php/IJSKM/article/view/574

**L9: 11. Stablecoins, digital currency, and the future of money** (2020) ()
- Findings: Explores the use of blockchain for creating stable cryptocurrencies and identifies key elements of stablecoin design.
- Method: Examination of blockchain applications.
- Impact: Highlights the foundational concepts of stablecoins.
- DOI/URL: https://wip.mitpress.mit.edu/pub/17h9tjq7?trk=public_post_comment-text

**L10: How to build a stablecoin: certainty, finality, and stability through commercial law principles** (2020) ()
- Findings: Details the components of a stablecoin arrangement and their interaction, including legal aspects like linking coins to collateral and infrastructure for transfers.
- Method: Legal analysis focusing on commercial law principles.
- Impact: Provides a comprehensive overview of stablecoin components from a legal and technical perspective.
- DOI/URL: https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/berkbusj17&section=12

**L11: A Stablecoin Ecosystem Primer** (2023) ()
- Findings: Categorizes stablecoins into Fiat Collateralized, Crypto Collateralized, and Algorithmic Non-Collateralized.
- Method: Overview of the digital asset ecosystem.
- Impact: Provides a taxonomy of stablecoin types.
- DOI/URL: https://www.semanticscholar.org/paper/05d2c384f35b52a07437f06c456fb5f9d4807531

**L12: A Survey of Blockchain-Based Stablecoin: Cryptocurrencies and Central Bank Digital Currencies** (2022) ()
- Findings: Provides an overview of applications and regulations of blockchain-based stablecoins, offering a clear view of the field.
- Method: Project review and comparative analysis.
- Impact: Comprehensive survey of blockchain-based stablecoins.
- DOI/URL: https://link.springer.com/chapter/10.1007/978-981-19-8043-5_13

**L13: Classification and legal regulation of stablecoins** (2175) ()
- Findings: Discusses the formal issuance of stablecoins and their embodiment of electronic monetary value, including issuer, issuance, and redemption conditions.
- Method: Legal classification and regulatory analysis.
- Impact: Addresses legal aspects of stablecoin issuance.
- DOI/URL: https://seer.ucp.br/seer/index.php/LexHumana/article/view/2488

**L14: The Paradox of Stablecoins: Risks and Policy Challenges** (2022) ()
- Findings: Identifies Tether (USDT), USD Coin (USDC), and Binance USD (BUSD) as major fiat-backed stablecoins.
- Method: Analysis of stablecoin risks and policy challenges.
- Impact: Provides context on prominent fiat-backed stablecoins.
- DOI/URL: https://www.kcmi.re.kr/kcmifile/webzine_content/OPINION/6032/webzinepdf_6032.pdf

**L15: Blockchain technology: An overview** (2022) ()
- Findings: Covers popular blockchain architectures, consensus protocols, and showcases projects using blockchain and cryptocurrency.
- Method: Overview of blockchain technology.
- Impact: Provides general background on blockchain architecture.
- DOI/URL: https://ieeexplore.ieee.org/abstract/document/9935797/

**L16: Revealing stablecoin successes: Lessons from a case study on USDT** (2023) ()
- Findings: Examines USDT as a prominent stablecoin, highlighting internal (early-mover advantages, price maintenance reserve, multi-blockchain resilience) and external factors (cryptocurrency ecosystem, regulatory constraints) driving its success.
- Method: Case study on USDT.
- Impact: Offers insights into the success factors of major stablecoins.
- DOI/URL: https://aisel.aisnet.org/iceb2023/76/

**L17: Understanding stablecoin technology and related security considerations** (2023) ()
- Findings: Explores stablecoin technology to enable understanding of various stablecoin types, taxonomies, and common security considerations.
- Method: Exploration of stablecoin technology and taxonomies.
- Impact: Contributes to a better understanding of stablecoin security.
- DOI/URL: https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936461

**L18: Regulating global stablecoins: A model-law strategy** (2022) ()
- Findings: Discusses complex cross-border regulatory challenges of stablecoins and the need for security mechanisms beyond cryptographic protections. Also mentions SEC authority over stablecoins.
- Method: Model-law strategy for regulation.
- Impact: Addresses regulatory challenges and security needs.
- DOI/URL: https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/vanlr75&section=46

**L19: Economic Nature and classification of stablecoins** (2020) ()
- Findings: Reveals the economic nature and characteristics of various stablecoin types within the financial market.
- Method: Analysis of economic nature and classification.
- Impact: Provides economic insights into stablecoin classification.
- DOI/URL: https://financetp.fa.ru/jour/issue/viewFile/62/42#page=138

**L20: A DeFi Bank Run: Iron Finance, IRON Stablecoin, and the Fall of TITAN** (2021) ()
- Findings: Analyzes the Iron Finance protocol, which issued the IRON stablecoin, and how a shock led to a bank run-like spiral, highlighting vulnerabilities in decentralized protocols.
- Method: Case study of Iron Finance.
- Impact: Illustrates failure modes in algorithmic stablecoins and DeFi.
- DOI/URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3888089

**L21: MakerDAO issues DAI stablecoins and Maker (MKR) governance tokens on Ethereum.DAI is designed to maintain a dollar value.The MakerDAO Protocol also uses a web of smart** (2023) ()
- Findings: Details how MakerDAO issues DAI stablecoins and MKR governance tokens on Ethereum, using a web of smart contracts to maintain a dollar value.
- Method: Description of MakerDAO protocol.
- Impact: Explains the architecture of a prominent crypto-collateralized stablecoin.
- DOI/URL: https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/fjcf28&section=6

**L22: It Pro’s on Crypto, Stablecoin and Blockchain** (2022) ()
- Findings: Discusses skepticism regarding stablecoin plans and notes that while blockchain has use cases, it has environmental concerns.
- Method: Discussion of crypto, stablecoin, and blockchain.
- Impact: Provides a broader perspective on the challenges and perceptions of stablecoins.
- DOI/URL: https://academic.oup.com/itnow/article/64/4/10/6835670

**L23: The curious case of stablecoins-balancing risks and rewards?** (2021) ()
- Findings: Highlights uncertainties regarding the governance and regulatory treatment of stablecoins despite their potential to transform payments.
- Method: Analysis of stablecoin risks, rewards, and regulatory approach.
- Impact: Emphasizes regulatory challenges and governance issues.
- DOI/URL: https://academic.oup.com/jiel/article-abstract/24/4/755/6446841

**L24: Bigtech, Stabletech, and Libra Coin–New Dawn, New Challenges, New Solutions** (2020) ()
- Findings: Describes stablecoins like Libra being tied to a basket of currencies and government securities, or single-currency digital coins backed by specific assets.
- Method: Discussion of Bigtech, Stabletech, and Libra Coin.
- Impact: Contextualizes asset-backed stablecoins.
- DOI/URL: https://www.jstor.org/stable/27009692

**L25: Blockchains, smart contracts, and stablecoins as a global payment system: The rise of web 3.0** (2022) ()
- Findings: Explores the role of stablecoins within blockchain systems and the type of blockchain suitable for stablecoin projects.
- Method: Survey and interviews on blockchain and stablecoins.
- Impact: Discusses stablecoin integration into payment systems.
- DOI/URL: https://www.diva-portal.org/smash/record.jsf?pid=diva2:1671071

**L26: An Analysis of Stablecoin in Public Blockchain** (2020) ()
- Findings: Provides an overview of stablecoins, their development since 2019 (over 200 projects), and their function as an application layer on blockchain systems. It details stability mechanisms, the need for system parameter tuning due to dynamic market prices, and the role of oracle systems in guiding future token prices. It also proposes Anagram, a stablecoin created via mining, pegged to fiat, with elastic supply and currency exchange entry, further enhancing price stability.
- Method: Thesis providing an overview and proposal.
- Impact: Comprehensive analysis of stablecoin mechanisms and a new proposal.
- DOI/URL: https://bridges.monash.edu/articles/An_Analysis_of_Stablecoin_in_Public_Blockchain/12219911

**L27: Regulations issue will delay stablecoin projects** (2021) ()
- Findings: Suggests that regulatory issues will delay stablecoin projects.
- Method: Emerald Expert Briefing.
- Impact: Highlights regulatory hurdles for stablecoin development.
- DOI/URL: https://www.emerald.com/insight/content/doi/10.1108/OXAN-ES264576/full/html

**L28: Comparative Cryptocurrencies and Stablecoins Regulation: A framework for a functional Comparative analysis** (2023) ()
- Findings: Focuses on frameworks for comparative analysis of cryptocurrencies and stablecoin regulation, and the increasing attention to blockchain's financial applications in the regulatory sphere.
- Method: Framework for comparative regulatory analysis.
- Impact: Contributes to regulatory understanding of stablecoins.
- DOI/URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4500090

**L29: The Evolutionary Development of Money: From Minted Coins to Cryptocurrencies** (2022) ()
- Findings: Compares USDC and USDT stablecoins, analyzes centralized versus decentralized stablecoins, and specifies their backing. Discusses the market share of USDT, USDC, and DAI, and highlights stablecoins' role in addressing volatility and increasing cross-border payment efficiency.
- Method: Study on money evolution, blockchain analysis, and cryptocurrency comparison.
- Impact: Provides comprehensive analysis and comparison of major stablecoins and their market impact.
- DOI/URL: https://www.business-inform.net/export_pdf/business-inform-2022-11_0-pages-190_194.pdf

**L30: Meta's many woes cloud future of its stablecoin** (2022) ()
- Findings: Indicates that Meta's stablecoin faces a challenging future.
- Method: Emerald Expert Briefing.
- Impact: Illustrates challenges in stablecoin development by large tech companies.
- DOI/URL: https://www.emerald.com/insight/content/doi/10.1108/OXAN-ES266935/full/html

**L31: An insight into Central Bank Digital Currency** (2023) ()
- Findings: Discusses the rise of cryptocurrencies and stablecoins, and how a well-designed retail Central Bank Digital Currency (CBDC) could protect monetary sovereignty against currency competition. Also notes the trade-off between privacy and security in CBDC design, and the need for compliance with AML, CFT, and KYC regulations.
- Method: Literature review survey.
- Impact: Provides insights into the policy implications of stablecoins and CBDCs.
- DOI/URL: https://doi.org/10.5281/zenodo.7569141

**L32: Qualitative study of heuristics and biases influencing cryptocurrency investment** (2023) ()
- Findings: Mentions interview questions asked to participants in cryptocurrency projects.
- Method: Qualitative study.
- Impact: General context for interview questions related to cryptocurrency projects.
- DOI/URL: https://digikogu.taltech.ee/et/Download/411dd81-abca-4442-bb75-7e3d2171bd49/Krptovaluutasseinvesteerimistmjutavateheurist.pdf

**L33: Decentralized Governance of Stablecoins with Option Pricing** (2021) ()
- Findings: Models incentive security in non-custodial stablecoins and derives conditions for participation across risk absorbers and governance token holders. Applies option pricing theory to derive optimal interest rates and conditions for secure protocols.
- Method: Game-theoretic modeling and option pricing theory.
- Impact: Provides a theoretical framework for decentralized stablecoin governance and security.
- DOI/URL: https://www.semanticscholar.org/paper/d1a5b5b6e6943c2d667c529c90f46aae87fec100

**L34: Preferring stablecoin over dollar: Evidence from a survey of Ethereum platform traders** (2023) ()
- Findings: A survey of Ethereum traders shows 60% prefer stablecoins over the US dollar, despite stablecoin's variance of return being significantly larger than the dollar's.
- Method: Survey of Ethereum trading market participants.
- Impact: Provides empirical evidence on user preferences and perceived stability of stablecoins.
- DOI/URL: https://www.sciencedirect.com/science/article/pii/S0261560622001991

**L35: Computer Science Abstractions to Help Reason About Decentralized Stablecoin Design** (2023) ()
- Findings: Examines decentralized and capital-efficient stablecoins using smart contracts that algorithmically trade to maintain stability. Shows that a capital-efficient algorithmic stablecoin cannot be provably stable. Provides a formal exposition of Central Bank Digital Currencies and discusses regulatory similarities between money-market funds and stablecoins.
- Method: Computer science abstractions and formal exposition.
- Impact: Offers a scientific perspective on stablecoin design and limitations.
- DOI/URL: https://ieeexplore.ieee.org/document/10258164/

**L36: Unbacked Crypto-Assets, Stablecoins and CBDC** (2023) ()
- Findings: Reviews unbacked crypto-assets, stablecoins, and central bank digital currencies, providing definitions of frequently misconstrued terms.
- Method: Review of payment innovations.
- Impact: Clarifies terminology and concepts in the digital asset space.
- DOI/URL: https://link.springer.com/chapter/10.1007/978-3-031-39520-8_9

**L37: Stablecoins and cryptocurrency returns: What is the role of Tether?** (3605) ()
- Findings: Studies the cross-sectional interdependence between cryptocurrency returns and Tether USD deviations from its U.S. dollar parity. Does not focus on the legitimacy of USDT as a true stablecoin.
- Method: Methodological study of cross-sectional interdependence.
- Impact: Analyzes market dynamics related to Tether.
- DOI/URL: https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=3605451

**L38: Stablecoins: the possibility of a cryptocurrency becoming the future means of payment** (2022) ()
- Findings: Discusses stablecoins' features as a stable cryptocurrency that facilitates cross-border payments, and references UST as an algorithmic stablecoin backed by LUNA.
- Method: Literature review.
- Impact: Highlights payment potential and past algorithmic stablecoin models.
- DOI/URL: https://www.diva-portal.org/smash/record.jsf?pid=diva2:1697220

**L39: Reducing the Volatility of Cryptocurrencies--A Survey of Stablecoins** (2021) ()
- Findings: Surveys different types of stablecoins and their stability mechanisms, classifying approaches into fiat/asset-backed, crypto-collateralized, and algorithmic. Assesses trade-offs and discusses challenges for future adoption.
- Method: Survey and classification.
- Impact: Comprehensive overview of stablecoin types and challenges.
- DOI/URL: https://arxiv.org/abs/2103.01340

**L40: Stablecoins: Types and Applications** (2020) ()
- Findings: Defines stablecoins as digital tokens aiming to stabilize major currencies in the crypto market, built on stabilization tools like tokenized funds, off-chain/on-chain collateralized, and algorithmic. Distinguishes private-issued and state-issued stablecoins.
- Method: Detailed overview of stabilization mechanisms.
- Impact: Provides a comprehensive overview of stablecoin types and their applications.
- DOI/URL: https://www.semanticscholar.org/paper/02d7ee82382330ab85d085752f4d786dca5e46cd

**L41: Blockchain meets metaverse and digital asset management: A comprehensive survey** (2023) ()
- Findings: Clarifies the role of blockchain in the metaverse, including digital asset management.
- Method: Comprehensive survey.
- Impact: General context for blockchain applications.
- DOI/URL: https://ieeexplore.ieee.org/abstract/document/10068493/

**L42: Blockchain Interoperability with Cross-chain Stablecoin Payments** (2020) ()
- Findings: Discusses the balkanized nature of blockchains and how cross-chain stablecoin transfers currently rely on centralized middlemen, contrasting with the decentralization ideology. Proposes an alternative system for trustless cross-chain stablecoin transfer.
- Method: Thesis proposing an alternative system.
- Impact: Addresses a critical challenge in multi-chain stablecoin architecture.
- DOI/URL: https://www.semanticscholar.org/paper/693ec71ab2cb52d46e665657ce5082445f6758fc

**L43: On Stablecoins: Stability Mechanisms and Use Cases for Real People** (2020) ()
- Findings: Reviews existing stablecoin mechanisms, highlighting asset-backed and seigniorage share-based categories, and their utility with DeFi smart contracts.
- Method: Comprehensive review with real-world examples.
- Impact: Provides a review of stablecoin architecture and use cases.
- DOI/URL: https://www.semanticscholar.org/paper/a8c531cadeb69dc88781a551d019d9e56566ffbd

**L44: Simulating the MakerDAO Stablecoin** (2021) ()
- Findings: Presents DAISIM, a computational simulation framework for the MakerDAO single-collateral stablecoin, modeling investors and incorporating automated order matching.
- Method: Computational simulation framework.
- Impact: Provides a tool for evaluating stablecoin projects.
- DOI/URL: https://ieeexplore.ieee.org/document/9461135/

**L45: Some Simple Economics of Stablecoins** (2022) ()
- Findings: Describes key stablecoin design choices, from reserve composition to stability mechanisms, and their benefits in programmable payments, financial inclusion, and DeFi.
- Method: Review of stablecoin economics.
- Impact: Offers insights into the economic benefits and trade-offs of stablecoins.
- DOI/URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3985699

**L46: Survey of prominent blockchain development platforms** (2023) ()
- Findings: Guides developers in selecting appropriate platforms for blockchain projects.
- Method: Survey of blockchain platforms.
- Impact: General resource for blockchain development.
- DOI/URL: https://www.sciencedirect.com/science/article/pii/S1084804523000693

**L47: Frax: A Fractional-Algorithmic Stablecoin Protocol** (2022) ()
- Findings: Proposes and implements FRAX, a 2-token fractional-algorithmic blockchain protocol that transitions a fully collateralized stablecoin to fully algorithmic, using a secondary token (FXS) to capture seigniorage value.
- Method: Protocol proposal and implementation.
- Impact: Describes a specific algorithmic stablecoin architecture.
- DOI/URL: https://ieeexplore.ieee.org/document/9881815/

**L48: Stablecoins as a crypto safe haven? Not all of them!** (2020) ()
- Findings: Analyzes the safe haven properties of major stablecoins like USDT, USDC, TUSD, PAX, DAI, GUSD, and finds only TUSD, PAX, and GUSD serve as safe havens.
- Method: Quantitative analysis using high-frequency data across exchanges.
- Impact: Provides empirical data on stablecoin safe haven properties.
- DOI/URL: https://www.semanticscholar.org/paper/9f6fa5cae0632ee15816022868a3b12cf901cbec

**L49: What Drives the (In)stability of a Stablecoin?** (2023) ()
- Findings: Provides a game-theoretical model to identify reasons for stablecoin de-pegging, revealing different price equilibria based on architecture and volatility minimization mechanisms. Supported by empirical data of 22 stablecoins.
- Method: Game-theoretical model and empirical data analysis.
- Impact: Offers a theoretical and empirical understanding of stablecoin instability.
- DOI/URL: https://ieeexplore.ieee.org/document/10634419/

**L50: A Token Economics Explanation for the De-Pegging of the Algorithmic Stablecoin: Analysis of the Case of Terra** (2023) ()
- Findings: Investigates the collapse of Terra's UST, identifying misalignment in economic incentive structure as a key contributor to de-pegging. Found that undercompensation of UST during redemption played a significant role.
- Method: In-depth analysis of token economics using on-chain data.
- Impact: Provides crucial insights into the failure modes of algorithmic stablecoins.
- DOI/URL: https://www.semanticscholar.org/paper/da975038c3d73724ce07b2ca77ed1ee00f3b0a90

**L51: Regulation may lag stablecoin usage, delaying projects** (2020) ()
- Findings: Highlights that global stablecoins, without adequate regulation, carry systemic risks, despite benefits like cheaper payments.
- Method: Emerald Expert Briefing.
- Impact: Discusses systemic risks and regulatory lag.
- DOI/URL: https://www.emerald.com/insight/content/doi/10.1108/OXAN-DB256276/full/html

**L52: Corporate Governance Challenges in Initial Coin Offerings** (2020) ()
- Findings: Discusses corporate governance challenges in ICOs, including exacerbated agency problems and the failure of traditional governance mechanisms to protect tokenholders.
- Method: Analysis of corporate governance challenges.
- Impact: Provides context on governance issues in tokenized projects.
- DOI/URL: https://www.semanticscholar.org/paper/fe69d090cae0a340d6882808f4278a5f8c63a799

**L53: Crypto Technical Analysis–Tools & BOTs Development** (2021) ()
- Findings: Mentions USTD as a stablecoin that floats around the price of the dollar and discusses its use in crypto trading.
- Method: Thesis on crypto technical analysis and BOT development.
- Impact: General context for USDT's market behavior.
- DOI/URL: https://www.theseus.fi/handle/10024/510408

**L54: Distributed Ledger Architecture for Collaborative Megaproject Management with Authenticated Participants** (2021) ()
- Findings: Discusses stablecoins pegged to fiat money, crypto, or project budgets, serving as platforms' native currency.
- Method: Study on distributed ledger architecture.
- Impact: Provides context on stablecoin use in project management.
- DOI/URL: https://dl.acm.org/doi/abs/10.1145/3460537.3460563

**L55: A blockchain ontology for DApps development** (2022) ()
- Findings: Mentions MakerDAO managing the Dai stablecoin.
- Method: Ontology for DApp development.
- Impact: Provides a specific example of stablecoin management within a DApp context.
- DOI/URL: https://ieeexplore.ieee.org/abstract/document/9770809/

**L56: Steem blockchain: Mining the inner structure of the graph** (2020) ()
- Findings: Mentions SBD as a stablecoin designed to help newcomers invest in the Steem ecosystem.
- Method: Study of Steem blockchain.
- Impact: Provides an example of a specific stablecoin.
- DOI/URL: https://ieeexplore.ieee.org/abstract/document/9261418/

**L57: The Trilemma of Stablecoin** (2021) ()
- Findings: Proposes a theoretical framework revealing a trilemma of price instability risks (moral hazards, external market risk, limited coin supply) in stablecoin design. A large-scale survey found that people perceive moral hazards and financial risks as greater than upward price instability.
- Method: Theoretical framework and global survey.
- Impact: Uncovers fundamental principles of stablecoin price stability and associated risks.
- DOI/URL: https://www.semanticscholar.org/paper/88ee0213c871a87d28451f647f5bcdfae8adcc48

**L58: Leverage and Stablecoin Pegs** (2022) ()
- Findings: Explains how stablecoins maintain a constant price despite run risk and no interest, due to holders indirectly compensated by lending coins to levered traders who pay a premium for borrowing when speculative demand is strong.
- Method: Economic analysis.
- Impact: Explains the economic mechanisms behind stablecoin peg maintenance.
- DOI/URL: https://www.nber.org/system/files/working_papers/w30796/w30796.pdf

**L59: A UTXO-based Sharding Method for Stablecoin** (2022) ()
- Findings: Proposes a UTXO-based sharding method to achieve horizontal scalability in token-based systems, including stablecoins, by reducing cross-shard transactions to improve throughput and keep latency low.
- Method: Proposal and verification through experiments.
- Impact: Addresses scalability challenges for stablecoins.
- DOI/URL: https://ieeexplore.ieee.org/document/9922204/

**L60: Stable Coin Distribution and Ownership Analysis** (2023) ()
- Findings: Discusses the emergence and development of stablecoins across networks (Bitcoin, Ethereum, Cardano) and issuers (Tether, Circle/Coinbase, Binance), noting similarities in price, smart contract usage (ERC-20), and user base. Focuses on Tether (Omni, Ethereum, Tron versions), Paxos, USDC, TrueUSD, Gemini Dollar, HUSD, Binance USD, and USDK.
- Method: Analysis of stablecoin network data.
- Impact: Provides insights into stablecoin distribution and usage across various platforms.
- DOI/URL: https://www.semanticscholar.org/paper/d8fbe93bbad8b3791684c5f7b0b3447eb1d43fd9

Sources: 
[1] Stablecoins: risks, potential and regulation, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3979495
[2] What keeps stablecoins stable?, https://www.sciencedirect.com/science/article/pii/S0261560622001802
[3] Stablecoins 2.0: Economic foundations and risk-based models, https://dl.acm.org/doi/abs/10.1145/3419614.3423261
[4] Stablecoins, https://www.emerald.com/insight/content/doi/10.1108/978-1-80455-320-620221007
[5] Examining User Perceptions of Stablecoins: Understandings and Risks, https://www.usenix.org/system/files/soups2023-poster160_guan_abstract_final.pdf
[6] Can stablecoins be stable?, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4226027
[7] The four types of stablecoins: A comparative analysis, https://arxiv.org/abs/2308.07041
[8] What is stablecoin?: A survey on its mechanism and potential as decentralized payment systems, https://iaiai.org/journals/index.php/IJSKM/article/view/574
[9] 11. Stablecoins, digital currency, and the future of money, https://wip.mitpress.mit.edu/pub/17h9tjq7?trk=public_post_comment-text
[10] How to build a stablecoin: certainty, finality, and stability through commercial law principles, https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/berkbusj17&section=12
[11] A Stablecoin Ecosystem Primer, https://www.semanticscholar.org/paper/05d2c384f35b52a07437f06c456fb5f9d4807531
[12] A Survey of Blockchain-Based Stablecoin: Cryptocurrencies and Central Bank Digital Currencies, https://link.springer.com/chapter/10.1007/978-981-19-8043-5_13
[13] Classification and legal regulation of stablecoins, https://seer.ucp.br/seer/index.php/LexHumana/article/view/2488
[14] The Paradox of Stablecoins: Risks and Policy Challenges, https://www.kcmi.re.kr/kcmifile/webzine_content/OPINION/6032/webzinepdf_6032.pdf
[15] Blockchain technology: An overview, https://ieeexplore.ieee.org/abstract/document/9935797/
[16] Revealing stablecoin successes: Lessons from a case study on USDT, https://aisel.aisnet.org/iceb2023/76/
[17] How stable are stablecoins?, https://www.semanticscholar.org/paper/5c87fcb5cb6d5ef30151b25497c79115b21f877e
[18] Blockchain mechanism and distributional characteristics of cryptos, https://arxiv.org/abs/2011.13240
[19] Understanding stablecoin technology and related security considerations, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=936461
[20] Regulating global stablecoins: A model-law strategy, https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/vanlr75&section=46
[21] The Case for Stringent Regulations of Stablecoins, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4179337
[22] Economic Nature and classification of stablecoins, https://financetp.fa.ru/jour/issue/viewFile/62/42#page=138
[23] From Tether to Terra: The Current Stablecoin Ecosystem and the Failure of Regulators, https://heinonline.org/hol-cgi-bin/get_pdf.cgi?handle=hein.journals/fjcf28&section=6
[24] It Pro’s on Crypto, Stablecoin and Blockchain, https://academic.oup.com/itnow/article/64/4/10/6835670
[25] The curious case of stablecoins-balancing risks and rewards?, https://academic.oup.com/jiel/article-abstract/24/4/755/6446841
[26] Bigtech, Stabletech, and Libra Coin–New Dawn, New Challenges, New Solutions, https://www.jstor.org/stable/27009692
[27] Stablecoins, Cryptocurrencies, and Blockchain, https://gfintech.pubpub.org/pub/du2rmn4t/release/2
[28] Blockchains, smart contracts, and stablecoins as a global payment system: The rise of web 3.0, https://www.diva-portal.org/smash/record.jsf?pid=diva2:1671071
[29] An Analysis of Stablecoin in Public Blockchain, https://bridges.monash.edu/articles/An_Analysis_of_Stablecoin_in_Public_Blockchain/12219911
[30] Soundness of Stablecoins, https://link.springer.com/chapter/10.1007/978-3-031-32415-4_5
[31] On Stablecoin: Ecosystem, architecture, mechanism and applicability as payment method, https://www.semanticscholar.org/paper/3504e4aab4a11e59599f0ecf402d85c830cd397d
[32] A Study on Regulation of Stablecoin, https://kiss.kstudy.com/Detail/Ar?key=4018787
[33] Crypto-assets: Economic nature, classification and regulation of turnover, https://iorj.hse.ru/data/2023/03/16/1714044663/4%20Kochergin.pdf
[34] The content and economic nature of stablecoins, https://elibrary.ru/doi_resolution.asp?doi=10.34130%2F2070-4992-2020-1-73-82
[35] Stablecoins: Past, Present, and Future, https://link.springer.com/chapter/10.1007/978-3-031-48806-1_13
[36] Regulations issue will delay stablecoin projects, https://www.emerald.com/insight/content/doi/10.1108/OXAN-ES264576/full/html
[37] Comparative Cryptocurrencies and Stablecoins Regulation: A framework for a functional Comparative analysis, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4500090
[38] Setting Standards for Stablecoin Reserves, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3970885
[39] Stablecoins – Past, Present, and Future, https://www.semanticscholar.org/paper/3adb91d628fcae2a6671a30e4186c02287d975f6
[40] The Evolutionary Development of Money: From Minted Coins to Cryptocurrencies, https://www.business-inform.net/export_pdf/business-inform-2022-11_0-pages-190_194.pdf
[41] Meta's many woes cloud future of its stablecoin, https://www.emerald.com/insight/content/doi/10.1108/OXAN-ES266935/full/html
[42] Decentralized Governance of Stablecoins with Closed Form Valuation, https://link.springer.com/chapter/10.1007/978-3-031-18679-0_4
[43] Legal Regulation of Stablecoins, https://www.semanticscholar.org/paper/42615020a1c659c2960197ba52f25911508aae7d
[44] Regulation of single currency-based stablecoin, https://kiss.kstudy.com/Detail/Ar?key=3998654
[45] An insight into Central Bank Digital Currency, https://doi.org/10.5281/zenodo.7569141
[46] Confidence Matters: a simulation-based stability Analysis of Algorithmic Stablecoins, https://www.semanticscholar.org/paper/e9e78c629390275f96e39dd3401d3bdd23f96299
[47] Qualitative study of heuristics and biases influencing cryptocurrency investment, https://digikogu.taltech.ee/et/Download/411dd831-abca-4442-bb75-7e3d2171bd49/Krptovaluutasseinvesteerimistmjutavateheurist.pdf
[48] Decentralized Governance of Stablecoins with Option Pricing, https://www.semanticscholar.org/paper/d1a5b5b6e6943c2d667c529c90f46aae87fec100
[49] Preferring stablecoin over dollar: Evidence from a survey of Ethereum platform traders, https://www.sciencedirect.com/science/article/pii/S0261560622001991
[50] Options for Designing Stablecoins and Central Bank Digital Currencies, https://www.semanticscholar.org/paper/51733586f68fb19a84574247dd5876b9539ae30e
[51] Analysis on Off-Chain Collateralised Stablecoin Demand and Volatility, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4161787
[52] Computer Science Abstractions to Help Reason About Decentralized Stablecoin Design, https://ieeexplore.ieee.org/document/10258164/
[53] Unbacked Crypto-Assets, Stablecoins and CBDC, https://link.springer.com/chapter/10.1007/978-3-031-39520-8_9
[54] Stablecoins and cryptocurrency returns: What is the role of Tether?, https://papers.ssrn.com/sol3/Delivery.cfm?abstractid=3605451
[55] Stablecoins: the possibility of a cryptocurrency becoming the future means of payment, https://www.diva-portal.org/smash/record.jsf?pid=diva2:1697220
[56] Reducing the Volatility of Cryptocurrencies--A Survey of Stablecoins, https://arxiv.org/abs/2103.01340
[57] Stablecoins and the real economy, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3973538
[58] Stablecoins: Types and Applications, https://www.semanticscholar.org/paper/02d7ee82382330ab85d085752f4d786dca5e46cd
[59] Blockchain meets metaverse and digital asset management: A comprehensive survey, https://ieeexplore.ieee.org/abstract/document/10068493/
[60] Blockchain Interoperability with Cross-chain Stablecoin Payments, https://www.semanticscholar.org/paper/693ec71ab2cb52d46e665657ce5082445f6758fc
[61] On Stablecoins: Stability Mechanisms and Use Cases for Real People, https://www.semanticscholar.org/paper/a8c531cadeb69dc88781a551d019d9e56566ffbd
[62] Simulating the MakerDAO Stablecoin, https://ieeexplore.ieee.org/document/9461135/
[63] Some Simple Economics of Stablecoins, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3985699
[64] Survey of prominent blockchain development platforms, https://www.sciencedirect.com/science/article/pii/S1084804523000693
[65] Frax: A Fractional-Algorithmic Stablecoin Protocol, https://ieeexplore.ieee.org/document/9881815/
[66] Stablecoins as a crypto safe haven? Not all of them!, https://www.semanticscholar.org/paper/9f6fa5cae0632ee15816022868a3b12cf901cbec
[67] What Drives the (In)stability of a Stablecoin?, https://ieeexplore.ieee.org/document/10634419/
[68] A Token Economics Explanation for the De-Pegging of the Algorithmic Stablecoin: Analysis of the Case of Terra, https://www.semanticscholar.org/paper/da975038c3d73724ce07b2ca77ed1ee00f3b0a90
[69] Regulation may lag stablecoin usage, delaying projects, https://www.emerald.com/insight/content/doi/10.1108/OXAN-DB256276/full/html
[70] A DeFi Bank Run: Iron Finance, IRON Stablecoin, and the Fall of TITAN, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3888089
[71] Alumni Q&A Session, https://www.semanticscholar.org/paper/50f2bf4b44a9cc926167c7db244b4083bba9aa09
[72] Index, https://doi.org/10.1108/s1569-37592022000109a019
[73] Corporate Governance Challenges in Initial Coin Offerings, https://www.semanticscholar.org/paper/fe69d090cae0a340d6882808f4278a5f8c63a799
[74] Crypto Technical Analysis–Tools & BOTs Development, https://www.theseus.fi/handle/10024/510408
[75] Currency Stability Using Blockchain Technology, https://linkinghub.elsevier.com/retrieve/pii/S0165188921000907
[76] Distributed Ledger Architecture for Collaborative Megaproject Management with Authenticated Participants, https://dl.acm.org/doi/abs/10.1145/3460537.3460563
[77] A blockchain ontology for DApps development, https://ieeexplore.ieee.org/abstract/document/9770809/
[78] Steem blockchain: Mining the inner structure of the graph, https://ieeexplore.ieee.org/abstract/document/9261418/
[79] Stablecoins: Does Design Affect Stability?, https://www.semanticscholar.org/paper/5786af844b33443a6691b4eaca87ce0bcb738b20
[80] The Trilemma of Stablecoin, https://www.semanticscholar.org/paper/88ee0213c871a87d28451f647f5bcdfae8adcc48
[81] Decentralized Stablecoin Design, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4202600
[82] Leverage and Stablecoin Pegs, https://www.nber.org/system/files/working_papers/w30796/w30796.pdf
[83] A UTXO-based Sharding Method for Stablecoin, https://ieeexplore.ieee.org/document/9922204/
[84] Stable Coin Distribution and Ownership Analysis, https://www.semanticscholar.org/paper/d8fbe93bbad8b3791684c5f7b0b3447eb1d43fd9
