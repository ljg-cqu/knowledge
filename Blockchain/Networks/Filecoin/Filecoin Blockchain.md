Filecoin Blockchain

Wed Jun 25 2025

### Introduction to the Filecoin Blockchain

The Filecoin blockchain is an open-source, peer-to-peer network specifically designed to facilitate decentralized file storage through built-in economic incentives and cryptographic proofs. Its core purpose is to transform unused digital storage into a secure and efficient marketplace for managing and retrieving data. Developed by Protocol Labs, Filecoin aims to address common challenges in traditional cloud storage, such as privacy concerns, centralized control, security vulnerabilities, and limited connectivity. The network operates by connecting individuals or entities needing storage (clients) with those offering their spare disk space (storage providers or miners), establishing an open market for storage and retrieval services accessible to all. Filecoin leverages blockchain technology to ensure transactions are transparent, immutable, and trustless, thereby enhancing data resilience and accessibility.

### Underlying Technology and Architecture

Filecoin's architecture is built on a unique blockchain structure that utilizes a chain of **tipsets** instead of individual blocks. A tipset is a collection of blocks with the same height, enabling multiple storage providers to produce blocks concurrently within each epoch, which significantly increases network throughput. Each tipset is assigned a specific weight, and the consensus protocol guides network nodes to build upon the "heaviest chain," which helps prevent interference from nodes attempting to create invalid blocks.

The Filecoin network is powered by a peer-to-peer (P2P) architecture, relying on various types of nodes. These include Lotus (written in Go), Fuhon (written in C++), and Forest (written in Rust), with Lotus being the most advanced node-based system used by the Filecoin blockchain mainnet. The network also categorizes nodes by their services, such as chain verifier nodes, client nodes, storage provider nodes, and retrieval provider nodes, all of which must provide chain verification services.

Furthermore, the Filecoin network incorporates several **built-in system actors** that function as "objects" with specific states and methods for interaction. These actors facilitate critical network operations, including initializing new actors (Init actor), scheduling critical functions (Cron actor), managing user accounts (Account actor), handling block rewards (Reward actor), managing storage mining (Storage miner actor), tracking storage power (Storage power actor), managing storage deals (Storage market actor), and supporting multi-signature wallet operations (Multisig actor). Additionally, the Ethereum Address Manager (EAM) actor assigns Ethereum-compatible addresses, including those for EVM smart contracts, enabling seamless interaction with existing Ethereum tools. Filecoin is also compatible with other smart contract networks like Ethereum, Polygon, Avalanche, and Solana, by storing data off-chain and recording verifiable Content IDs (CIDs) and storage proofs on the Filecoin chain.

Filecoin is built on top of the InterPlanetary File System (IPFS), a protocol that enables peers to store, request, and share data using a distributed file system where each file is uniquely identified by content addressing. Filecoin adds an incentive layer to IPFS, ensuring persistent storage by requiring storage deals to be recorded on-chain and proofs of storage to be submitted over time, with payments, penalties, and block rewards enforced by the decentralized protocol.

### Consensus Mechanisms

The Filecoin blockchain achieves network consensus through the **Expected Consensus (EC)** algorithm, a probabilistic, Byzantine fault-tolerant protocol that is secret, fair, and verifiable. EC operates by conducting a leader election among storage providers in each epoch, where the probability of being elected to submit a block is directly proportional to the amount of provable storage, known as "storage power," a miner contributes to the network. This process is akin to proof-of-stake but is based on proof-of-storage. The leader election uses Drand as a randomness beacon to ensure fairness and verifiability, drawing participants and their storage power from a continuously updated "Power Table" maintained by the storage power actor.

After leaders are elected, they generate a **Winning Proof-of-Spacetime (WinningPoSt)** using randomness to prove they hold a copy of the data at a specific moment in time. Multiple elected leaders can propose blocks in an epoch, and all valid blocks produced are grouped into a tipset. The EC process concludes by applying a weighting function to select the heaviest chain, and the tipset is added to it, enforcing "soft finality" to ensure finality without compromising chain availability.

Filecoin's consensus mechanism is further reinforced by two key cryptographic proofs:
*   **Proof-of-Replication (PoRep)**: This proof ensures that storage providers have created a unique copy of the client's data for the network. It cryptographically verifies the agreed-upon number of copies of a stored file.
*   **Proof-of-Spacetime (PoSt)**: This mechanism requires storage providers to continuously prove they are storing clients' data throughout the entire duration of the storage deal. It includes two types: WinningPoSt, which verifies data holding at a specific time, and WindowPoSt, which confirms consistent storage over a defined period.

If storage providers fail to maintain reliable uptime or act maliciously, they face financial penalties through **slashing**, which includes Storage Fault Slashing for not maintaining healthy sectors and Consensus Fault Slashing for attempting to disrupt the consensus process.

### Data Storage and Retrieval

Filecoin operates as a decentralized marketplace for data storage and retrieval. Clients who need storage pay storage providers (miners) in FIL tokens to store their data. This dynamic creates a market where prices for storage and retrieval services are determined by supply and demand, rather than being fixed by a central authority. Clients can negotiate and customize storage contracts based on factors like duration, redundancy, and price.

The process of data storage involves several steps. Once a storage deal is agreed upon, it is recorded on the Filecoin blockchain, ensuring transparency and enforceability. Storage miners then divide the client's data into fixed-size sectors, typically 32 GiB or 64 GiB. To prove they have uniquely and securely stored the data, miners must perform a computationally intensive "sealing" process, which generates a Proof-of-Replication (PoRep). This proof is then compressed using a Zero-Knowledge Succinct Non-Interactive Argument of Knowledge (zkSNARK) and submitted to the blockchain, allowing network participants to verify data authenticity without revealing the data itself. After sealing, miners must continuously provide Proof-of-Spacetime (PoSt) to demonstrate that the data remains stored for the agreed-upon period. Storage miners are required to stake FIL tokens as collateral; if they fail to uphold their storage commitments, they can face penalties through slashing.

Data retrieval on Filecoin is handled by **Retrieval Miners**, who are compensated in FIL tokens for serving data efficiently. While storage deals are primarily recorded on-chain, retrieval deals often leverage off-chain payment channels to enable faster transactions. Clients typically initiate retrieval requests to the storage providers who originally stored their data, using the Content Identifier (CID) of the file. Retrieval miners compete based on factors such as internet bandwidth and latency to deliver data quickly.

Filecoin is primarily designed for storing large datasets over extended periods and is generally not suited for real-time, high-speed data access due to the computational burden of cryptographic proofs and sealing processes. For example, uploading a 1 MiB file can take 5 to 10 minutes, and unsealing a 32 GiB sector for retrieval can take around 3 hours. This makes Filecoin an ideal solution for archival storage, public datasets, and decentralized applications where long-term data preservation and verifiability are prioritized over immediate access speeds.

### Filecoin Native Token (FIL)

FIL is the native cryptocurrency of the Filecoin network, serving as the economic backbone that incentivizes participation, facilitates transactions, and ensures accountability within its decentralized storage system.

The role and utility of FIL include:
*   **Payments**: Users pay storage providers in FIL for data storage and retrieval services. This payment system enables an open market where clients can select providers offering the most competitive rates.
*   **Incentives and Rewards**: Storage providers earn FIL by offering storage space, maintaining data availability, and validating storage proofs. Miners also receive FIL as block rewards for contributing to the network and adding new blocks to the blockchain.
*   **Collateral and Security**: Miners are required to stake a certain amount of FIL tokens as collateral to participate in the network. This mechanism discourages dishonest behavior, as miners risk losing their staked FIL if they fail to store data reliably or act maliciously.
*   **Transaction Fees and Burning**: FIL is used to pay for transaction fees for on-chain computations and bandwidth. A portion of FIL tokens used for network fees or penalties may be burned, creating a long-term deflationary pressure on the token's supply.
*   **Governance**: FIL holders can participate in the network's governance by voting on proposals that influence the future development and direction of the Filecoin network.

The total supply of FIL is capped at 2 billion tokens. A significant portion, specifically 70% of the total supply, is allocated as mining rewards, which are distributed over decades and are proportional to network adoption. The Filecoin project conducted a highly anticipated Initial Coin Offering (ICO) in 2017, raising over $200 million within 30 minutes, which helped fund its development.

### Participation in the Network (Miners and Clients)

Participation in the Filecoin network involves two primary types of entities: **Miners** (Storage Providers and Retrieval Miners) and **Clients**.

**Miners**:
To become a Filecoin miner, an individual or organization needs to offer their unused disk space to the network. This typically involves significant hardware investments and technical expertise, as running a storage operation is a serious business with client data and pledged funds at stake. Miners must register on-chain and commit storage sectors, which can either be filled with client data or be Committed Capacity sectors without data. They are required to stake a certain amount of FIL tokens as collateral. This collateral acts as an incentive for honest behavior and ensures that miners fulfill their commitments; failure to maintain data availability or act maliciously results in financial penalties through slashing.

The process for storage miners involves:
1.  **Providing Storage**: Offering their storage space to the network.
2.  **Sealing Data**: Performing computation-heavy processes to create a unique representation of the data, which produces a Proof-of-Replication (PoRep). This proof verifies that the miner has genuinely stored a unique copy of the client's data.
3.  **Submitting Proofs**: Regularly submitting Proof-of-Spacetime (PoSt) to the network, demonstrating that the data is continuously being stored over the agreed-upon duration. These proofs are audited in 24-hour increments.
4.  **Block Production**: Miners are selected to mine new blocks proportionally to their verified storage power, following the Expected Consensus (EC) mechanism. Elected miners generate WinningPoSt and build a block to propagate to the network.

Retrieval Miners, the second type of miner, focus on providing quick access to data stored on the network. They earn FIL tokens by efficiently serving data to Filecoin users, and their selection often depends on internet bandwidth and latency relative to the user's location. Most storage providers also offer retrieval services.

**Clients**:
Clients are users or entities that require data storage or retrieval services. They participate in the Filecoin marketplace by paying miners in FIL tokens. Clients can negotiate storage deals with miners, selecting providers based on criteria such as price, reliability, and geographical location, giving them flexibility and control over their storage needs. When a client stores data, they receive a key to facilitate future retrievals. The Filecoin Plus program, for instance, introduces DataCap, a resource granted to "Notaries" who then allocate it to trustworthy clients, significantly incentivizing miners to store this data by boosting their block reward share.

The marketplace functions as a permissionless open market, fostering competition among miners to offer the most price-competitive and reliable storage services.

### Security Features and Protocols

The Filecoin blockchain incorporates a robust suite of security features and protocols to ensure data integrity, confidentiality, and network resilience.

Key security elements include:
*   **Cryptographic Proofs**: Filecoin heavily relies on **Proof-of-Replication (PoRep)** and **Proof-of-Spacetime (PoSt)**. PoRep ensures that a storage provider has created a unique copy of the client's data, verifying that the data has been physically stored. PoSt continuously verifies that the data remains stored over the entire duration of the storage deal. These proofs are vital for maintaining the integrity and availability of stored data and preventing fraudulent claims by miners.
*   **Expected Consensus (EC)**: As the network's consensus algorithm, EC is a probabilistic, Byzantine fault-tolerant protocol that ensures a secret, fair, and verifiable leader election process. It selects block producers based on their "storage power," making it difficult for an adversary to control the network unless they possess a significant fraction of the total storage (currently estimated around 20% for m=5). EC uses Drand as a decentralized randomness beacon to ensure unpredictability and fairness in leader selection.
*   **Decentralized Storage and Data Replication**: Filecoin's decentralized architecture distributes data across numerous nodes globally, reducing single points of failure and enhancing data privacy and durability. When a file is stored, it is divided and replicated across multiple storage providers, ensuring data accessibility even if some providers become unavailable.
*   **Encryption**: While Filecoin provides the infrastructure for verifiable storage, clients typically encrypt their data prior to storage on the network. This client-side encryption ensures that only authorized parties holding the decryption keys can access and decipher the data, thereby preserving confidentiality.
*   **Slashing Mechanisms**: To align miners' incentives with network goals and deter malicious behavior, Filecoin implements slashing. Storage providers face penalties if they fail to maintain healthy and reliable storage sectors (Storage Fault Slashing) or attempt to disrupt the consensus process (Consensus Fault Slashing).
*   **Blockchain Immutability**: The use of blockchain technology records and validates all storage transactions, making them trustless and immutable. This transparency allows clients to verify the integrity of their stored data and ensures that storage providers cannot tamper with or modify data without detection.
*   **Authentication and Authorization**: Users can authenticate themselves using public and private key cryptography, and authorization is enforced through smart contracts.

Ongoing security enhancements include proposals like consistent broadcast protocols to prevent adversarial equivocation and further strengthen the network's resilience against attacks.

### Notable Use Cases and Real-World Applications

Filecoin serves as a robust, decentralized, and verifiable platform for storing and interacting with data, offering a powerful alternative to traditional cloud storage solutions. Its design, which combines cryptographic proofs and economic incentives, enables a wide range of real-world applications:

*   **Decentralized Cloud Storage**: This is the most direct application, where Filecoin provides a secure, censorship-resistant, and potentially more cost-effective alternative to centralized cloud providers like Amazon Web Services or Google Cloud. It allows users to rent out unused hard drive space, fostering a global marketplace for data storage.
*   **Archival and Content Preservation**: Filecoin is used by institutions for long-term archival of important public data, including open-access scientific data, historical archives, and creative commons media. Notable examples include the **Internet Archive** and the **Shoah Foundation**, which use Filecoin for content preservation and backup.
*   **Web3 Native Storage**: Filecoin provides scalable storage for decentralized applications (dApps), blockchain projects, and non-fungible tokens (NFTs). It is increasingly serving as a backend for storing NFT content and metadata, ensuring their provenance and immutability. The Filecoin Virtual Machine (FVM) enables Web3 developers to build dApps and data DAOs leveraging Filecoin's storage infrastructure.
*   **Media and Streaming**: Filecoin's compatibility with various data types, including audio and video files, allows Web3 platforms like Audius (music streaming) and Huddle01 (video conferencing) to use it as a decentralized storage backend.
*   **Enterprise Storage**: Filecoin is evolving to offer a decentralized storage marketplace tailored for enterprise use, facilitating decentralized computing and AI capabilities as part of a Decentralized Physical Infrastructure Network (DePIN).
*   **Cost-Effective Archiving**: For traditional Web2 datasets, Filecoin offers a cost-effective solution for archiving, presenting a strong alternative to conventional cloud storage, with claims of being up to 95% lower cost compared to some centralized services.

The network has demonstrated substantial growth, with approximately 4,500 storage providers and 17 EiB (exbibytes) of capacity as of October 2022, making it the world's largest decentralized storage network.

### Recent Developments and Future Roadmap

Filecoin has demonstrated significant progress and ambitious plans, with recent developments focusing on enhancing network efficiency, economics, and adaptability. The **NV25 "Teep" upgrade**, officially launched in April 2025, brought major improvements to the network.

Key recent developments and roadmap highlights include:
*   **Filecoin Virtual Machine (FVM)**: There has been notable progress in the FVM, which enables the deployment of smart contracts on Filecoin, allowing developers to build more complex decentralized applications that leverage Filecoin's storage infrastructure.
*   **Fast Finality (F3)**: Introduced with the Tuk Tuk upgrade in November 2024, Fast Finality aims to drastically speed up transaction finality from 7.5 hours to mere seconds, making the network 450 times faster. This upgrade also brings improved security and better randomness for smart contracts.
*   **DePIN and AI Integration**: Filecoin's 2024 roadmap includes introducing Decentralized Physical Infrastructure Network (DePIN) services, computing, storage, and AI networks as Layer 2 solutions and integrated platforms. This aligns with Filecoin's vision of supporting decentralized computing and Artificial Intelligence capabilities.
*   **Ecosystem Expansion**: Filecoin continues to expand its ecosystem through strategic partnerships and collaborations, including those with green energy companies to promote efficient and sustainable decentralized storage. The Filecoin Foundation, established in 2020, actively supports the protocol's development and broader decentralized web projects.
*   **Community Engagement and Governance**: Filecoin fosters a substantial developer community and a supporting grant program. There is active community engagement in governance discussions, with initiatives like Filecoin Plus, which involves community-selected Notaries allocating DataCap to trustworthy clients to incentivize useful storage.
*   **Network Tooling and Dashboards**: The ongoing expansion of development tools, libraries, providers, and software integration mechanisms has simplified application development on Filecoin. New dashboards are being launched to improve user and developer experiences.
*   **Improved Retrieval Markets**: Updates include enhancing retrieval capabilities to make it an open market where individuals and organizations can contract with retrieval providers for content delivery. Object-level retention, ACL enforcement, and up to 50% faster speeds have also been noted in recent updates.

The Filecoin Foundation's top objective for 2025 is to mobilize the community to ensure Filecoin works seamlessly and achieves product-market fit. These continuous developments position Filecoin to remain a leading project in the growing decentralized storage industry.

### Advantages and Challenges of Filecoin

Filecoin offers several compelling advantages over traditional centralized storage solutions:
*   **Decentralization and Censorship Resistance**: Filecoin mitigates risks associated with centralized data storage, such as privacy breaches and censorship, by distributing data across a global network of independent operators. This eliminates single points of failure, making the network resilient against attacks and outages.
*   **Economic Incentives and Competitive Pricing**: The FIL token and its tokenomics align the interests of all network participants. Miners are incentivized to provide reliable storage services, leading to competitive prices for clients, often significantly lower than traditional cloud providers.
*   **Verifiable Storage**: Filecoin employs cryptographic proofs (PoRep and PoSt) that publicly audit miners' storage, ensuring data integrity and reliability. Clients can trust that their data is securely stored and untampered with.
*   **Scalability**: The open market mechanism allows the network to dynamically adjust to changes in demand for storage, accommodating the growing data needs of the digital world. Filecoin is the largest distributed storage network with petabyte-scale capacity.
*   **Diverse Use Cases**: Filecoin's flexibility makes it suitable for various applications, including NFT storage, large dataset archiving, and hosting decentralized web applications, expanding possibilities for data storage and access.

Despite its numerous benefits, Filecoin faces certain challenges:
*   **Technical Complexity and Barrier to Entry**: Becoming a storage provider on Filecoin requires substantial hardware investment and technical expertise, which can limit participation to more proficient users.
*   **Performance Limitations**: Compared to traditional cloud services, Filecoin's I/O performance can be slower, particularly for data sealing and retrieval due to the cryptographic proofs and processing overhead. This makes it more suitable for archival data rather than real-time applications.
*   **"Rent" Not Own**: Users "rent" storage space from miners, meaning they do not explicitly "own" the data on the protocol. Storage miners are only incentivized to host data as long as they receive FIL payments from users.
*   **Privacy Misconceptions**: It is a common misconception that data stored on Filecoin is private by default. In reality, when a storage miner hosts user data, they announce its content to the network for replication and retrieval. Users wishing to store private data must encrypt it *before* publishing it to the network.
*   **Market Competition**: Filecoin operates in a competitive landscape with other decentralized storage networks (e.g., Storj, Arweave) and established centralized cloud storage services, requiring continuous innovation and adaptation.
*   **User Adoption and Education**: As a relatively new technology, decentralized systems present a steep learning curve for many users and businesses, which can impede widespread adoption.

Bibliography
A Guide to Filecoin Storage Mining. (2020). https://filecoin.io/blog/posts/a-guide-to-filecoin-storage-mining/

AR Raipurkar, A Zade, & P Agrawal. (2024). A Blockchain-Based Framework for Secure and Decentralized Document Integrity Using Filecoin and Smart Contract. https://ieeexplore.ieee.org/abstract/document/10973655/

Basics | Filecoin Docs. (2025). https://docs.filecoin.io/storage-providers/basics

Blockchain - Filecoin Docs. (2025). https://docs.filecoin.io/basics/what-is-filecoin/blockchain

Consensus | Filecoin Docs. (2024). https://docs.filecoin.io/basics/the-blockchain/consensus

Crypto-economics - Filecoin Docs. (2025). https://docs.filecoin.io/basics/what-is-filecoin/crypto-economics

Decentralised Data Storage: Filecoin - Zerocap. (2023). https://zerocap.com/insights/research-lab/decentralised-data-storage-filecoin/

EJ Lopes, S Kataria, S Keshav, ST Ikram, & MR Ghalib. (2022). Live video streaming service with pay-as-you-use model on Ethereum Blockchain and InterPlanetary file system. https://link.springer.com/article/10.1007/s11276-022-03009-6

Everything you should know about Filecoin | by Coindelta - Medium. (2022). https://medium.com/@researchcoindelta/everything-you-should-know-about-filecoin-c1e14327775b

Filecoin. (n.d.). https://filecoin.io/

Filecoin - CoinList. (2025). https://coinlist.co/filecoin

Filecoin - Wikipedia. (2017). https://en.wikipedia.org/wiki/Filecoin

Filecoin - X. (2025). https://x.com/filecoin

Filecoin features: verifiable storage. (2020). https://filecoin.io/blog/posts/filecoin-features-verifiable-storage/

Filecoin (FIL): Cloud Storage and Data Retrieval | Gemini. (2020). https://www.gemini.com/cryptopedia/filecoin-fil-democratizing-cloud-storage

Filecoin (FIL) Sets Ambitious 2025 Vision with New Developments. (2025). https://blockchain.news/news/filecoin-fil-2025-vision-developments

Filecoin Foundation’s Vision and Strategic Priorities for 2025. (2024). https://fil.org/blog/filecoin-foundation-s-vision-and-strategic-priorities-for-2025

Filecoin network security - CoinSwitch. (n.d.). https://coinswitch.co/switch/crypto/filecoin-network-security-measures/

Filecoin News 108. (2025). https://filecoin.io/blog/posts/filecoin-news-108/

Filecoin Plus: Aligning Participants with Useful Storage. (2021). https://filecoin.io/blog/posts/filecoin-plus-aligning-participants-with-useful-storage/

Filecoin price today, FIL to USD live price, marketcap and chart. (2025). https://coinmarketcap.com/currencies/filecoin/

Filecoin Storage Solutions & Blockchain Development - Gemini. (2020). https://www.gemini.com/cryptopedia/filecoin-blockchain-development

Filecoin: The Airbnb of archival storage - Blocks and Files. (2022). https://blocksandfiles.com/2022/10/11/protocol-labs-filecoin/

Filecoin Tokenomics Explained - Shrimpy Academy. (2023). https://academy.shrimpy.io/post/filecoin-tokenomics-explained

Filecoin: Too Long Didn’t Read (TL;DR) | Filecoin Digestible Updates. (2025). https://filecointldr.io/

Filecoin’s Privacy Preservation: The Ecosystem’s Role in Data ... (2024). https://medium.com/crossfi-official/filecoins-privacy-preservation-the-ecosystem-s-role-in-data-security-and-confidentiality-910fa752c4c2

Fundamentals | Filecoin Docs. (2024). https://docs.filecoin.io/smart-contracts/fundamentals

H Kopp, C Bösch, & F Kargl. (2016). Koppercoin–a distributed file storage with financial incentives. https://link.springer.com/chapter/10.1007/978-3-319-49151-6_6

How does Filecoin storage ensure the security and privacy of digital ... (2022). https://www.bydfi.com/en/questions/how-does-filecoin-storage-ensure-the-security-and-privacy-of-digital-assets

How to Understand the Filecoin Retrieval Market? | by Swan Chain. (2022). https://filswan.medium.com/how-to-understand-the-filecoin-retrieval-market-37ea561d5438

Investing in Filecoin (FIL) - Everything You Need to Know. (2025). https://www.securities.io/investing-in-filecoin/

J. Benet. (2017). Filecoin Research Roadmap for 2017. https://www.semanticscholar.org/paper/0b6799afd29d18e04f8c3ce9e4c87311dfd65bba

Learning Objectives - Filecoin - PLN Launchpad. (n.d.). https://pl-launchpad.io/curriculum/filecoin/objectives/

Overview of Filecoin’s community roadmap for the second half of 2024. (2024). https://www.bitget.com/news/detail/12560604235518

Provide Storage | Filecoin. (n.d.). https://filecoin.io/provide/

Real-world Use Cases and Applications of Filecoin and Storj. (2024). https://stackademic.com/blog/real-world-use-cases-and-applications-of-filecoin-and-storj

Retrieval market - Filecoin Docs. (2025). https://docs.filecoin.io/basics/what-is-filecoin/retrieval-market

Retrieve Data - Filecoin Docs. (2025). https://docs.filecoin.io/builder-cookbook/data-storage/retrieve-data

Shreya Khatal, Jayant Rane, Dhiren R. Patel, P. Patel, & Yann Busnel. (2020). FileShare: A Blockchain and IPFS Framework for Secure File Sharing and Data Provenance. In Algorithms for Intelligent Systems. https://www.semanticscholar.org/paper/e2a010dc2039d9c541d0e4fc6b4546bdb0d311f7

State of Filecoin 2025. (2024). https://filecointldr.io/article/state-of-filecoin-2025

Store | Filecoin. (2021). https://filecoin.io/store/

Store Data | Filecoin Docs. (2024). https://docs.filecoin.io/builder-cookbook/data-storage/store-data

Updates – Latest Network News & Technical Developments - Filecoin. (2025). https://filecoin.io/blog/updates/

Wenbo Zhang, Taoxian Wang, Chao-zhe Zhang, & Jingyu Feng. (2024). Securing multi-chain consensus against diverse miner behavior attacks in blockchain networks. In Frontiers Inf. Technol. Electron. Eng. https://www.semanticscholar.org/paper/ef70b21d62520b53d97d73ca923514fd464f486e

What is Filecoin. (2025). https://docs.filecoin.io/basics/what-is-filecoin

What is Filecoin & How does it Work? - Phemex. (2024). https://phemex.com/academy/cryptocurrency-glossary/filecoin

What is FileCoin? - The Big Whale. (n.d.). https://www.thebigwhale.io/tokens/filecoin

What Is Filecoin and How Does It Work? - CCN.com. (2024). https://www.ccn.com/education/crypto/what-is-filecoin-decentralized-blockchain-storage-solution/

What Is Filecoin (FIL)? - Komodo Platform. (2024). https://komodoplatform.com/en/academy/what-is-filecoin-fil/

What is Filecoin? (FIL) - Kraken. (2022). https://www.kraken.com/learn/what-is-filecoin-fil

What Is Filecoin (FIL)? How It Works and How to Buy FIL - Crypto.com. (2024). https://crypto.com/en/university/what-is-filecoin-fil

What is Filecoin? The leading decentralized storage network. (2023). https://cointelegraph.com/learn/articles/what-is-filecoin-the-leading-decentralized-storage-network

Xuechao Wang, Sarah Azouvi, & Marko Vukoli’c. (2023). Security Analysis of Filecoin’s Expected Consensus in the Byzantine vs Honest Model. In Conference on Advances in Financial Technologies. https://www.semanticscholar.org/paper/14a794b6d93816aecc79407d6963e5cb6436d0c5

Y. Boyle. (2018). Use cases of Blockchain: Application and Interworking. https://www.semanticscholar.org/paper/5fd75e4d1f5b159c2865a9f66b88cb3e5791b74a



Generated by Liner
https://getliner.com/search/s/5926611/t/85975092