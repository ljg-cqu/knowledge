### 联盟链与RWA数字化：Hyperledger Fabric和FISCO BCOS的深度解析

在当前技术驱动的商业环境中，去中心化数字平台正革新着传统行业，特别是网约车租赁等对效率、透明度和信任度要求极高的领域。通过集成SaaS、AI和区块链技术，可以为运力供给侧的大B（租赁公司）、小B（平台经理人）和司机提供深度服务，显著提升行业数字化水平，保障各方权益，并构建一个透明、高效、可信的新型商业生态。本报告将深入探讨Hyperledger Fabric和FISCO BCOS等主流联盟链框架，其权限管理、共识机制、节点部署和性能优化，以及在RWA（真实世界资产）数字化和智能合约开发中的应用，特别关注数据安全与隐私保护.

#### Hyperledger Fabric架构与核心组件

Hyperledger Fabric是一个为企业级应用设计的开源许可型分布式账本技术（DLT）平台，旨在支持超越比特币等数字货币的商业应用。它采用高度模块化和可配置的架构，以实现广泛行业用例的创新、多功能性和优化。Fabric的设计从一开始就考虑了企业用途，提供了其他区块链平台不具备的独特功能。

##### 节点角色及其功能
在Hyperledger Fabric网络中，不同的节点承担着特定的角色，共同维护网络的正常运行和数据的一致性:
- **客户端（Client）**: 指与网络进行交易的身份。
- **管理员（Admin）**: 负责处理管理任务，例如将对等节点加入通道。
- **对等节点（Peer）**: 如果对等节点认可或提交交易，则其扮演对等角色。对等节点是区块链网络的基础，托管账本，并可以通过智能合约被应用程序查询和更新。它们执行智能合约并处理交易，但不负责交易的机械打包。
- **排序节点（Orderer）**: 属于排序服务中的节点。排序服务负责建立交易的顺序，并将它们打包成区块。
- **成员（Member）**: 主要用于指定策略，例如在多方组织策略中定义成员资格 ("OR('Org1MSP.member', 'Org2MSP.member')")。

##### 成员服务提供商（MSP）与身份管理
所有与区块链网络交互的实体，包括对等节点、应用程序、管理员和排序节点，都通过其数字证书和成员服务提供商（MSP）定义来获取其组织身份。MSP抽象了证书颁发、证书验证和用户认证背后的所有加密机制和协议。每个组织都应使用独立的证书颁发机构（CA）来管理其排序节点，无论是作为根CA还是部署根CA及其关联的中间CA，这取决于具体需求。

##### 通道（Channels）
通道是Hyperledger Fabric实现数据隔离和隐私的关键机制。它允许多个参与方在网络中建立一个子网络，只有该通道的成员才能看到特定的交易。这确保了只有参与通道的节点才能访问智能合约（链码）和交易数据，从而保护了代码和数据的隐私和机密性。通道还可以执行基本的访问控制，限制谁可以读写数据或配置通道。

#### Hyperledger Fabric的交易流与共识机制

Hyperledger Fabric采用独特的“执行-排序-验证”（execute-order-validate）架构，与大多数区块链系统采用的“排序-执行”模型不同。这种架构将交易流分为三个阶段，解决了弹性、灵活性、可伸缩性、性能和机密性方面的挑战。

##### 交易提案与背书（Phase One）
在第一阶段，客户端应用程序通过受信任的对等节点向Fabric网关服务发送交易提案。该对等节点会执行提议的交易，或将其转发给其组织中的另一个对等节点执行。网关还将交易转发给背书策略中要求的组织中的对等节点。这些背书对等节点运行交易并返回交易响应给网关服务，但此时它们不会将提议的更新应用到自己的账本副本。

##### 交易提交与排序（Phase Two）
交易提案成功完成后，客户端应用程序从Fabric网关服务接收到一个已背书的交易提案响应以进行签名。对于已背书的交易，网关服务将交易转发给排序服务。排序服务将该交易与其他已背书的交易一起排序，并将它们打包成一个区块。排序服务节点并发地接收来自许多不同应用程序客户端的交易。这些区块最终将被分发给通道上的所有对等节点，以进行第三阶段的验证和提交。交易在区块内的排序不一定与排序服务接收的顺序相同，但排序服务确保了交易的严格顺序，对等节点将使用此顺序进行验证和提交。Hyperledger Fabric中的区块是最终的，一旦交易写入区块，其在账本中的位置就不可更改。

##### 交易验证与提交（Phase Three）
第三阶段涉及排序服务将已排序和打包的区块分发给通道上的对等节点，以进行验证和提交到账本。每个对等节点会独立验证分发的区块，确保账本保持一致。具体来说，通道中的每个对等节点将验证区块中的每笔交易，以确保它已被所需的组织背书，其背书匹配，并且没有被其他最近提交的交易失效。失效的交易仍保留在排序节点创建的不可变区块中，但会被对等节点标记为无效，并且不会更新账本状态。

##### 排序服务实现
Fabric支持可插拔的共识协议，可以根据特定部署或解决方案的信任假设进行定制。
- **Raft**: 从v1.4.1开始引入，Raft是一种基于Raft协议实现的崩溃容错（CFT）排序服务。它采用“领导者和追随者”模型，其中（每个通道）选举一个领导者节点，其决策由追随者复制。Raft可以承受节点损失，只要多数排序节点（即“法定人数”）保持可用。
- **拜占庭容错（BFT）**: 从v3.0开始，Fabric支持基于SmartBFT库的BFT排序服务。BFT排序服务不仅可以承受崩溃故障，还可以承受一部分恶意节点的行为。它能容忍高达（但不包括）三分之一的恶意节点，这与Raft不同，Raft不适用于这种严峻的对抗模型。BFT排序服务的领导者不是动态选择的，而是通过轮询方式轮换。

#### Hyperledger Fabric的隐私与保密性

在企业用例中，交易和数据的隐私性至关重要，因为参与者通常不完全信任彼此（例如，同一行业的竞争对手）。Hyperledger Fabric通过其通道架构和私有数据功能来解决这一挑战。

##### 通道实现数据隔离
如前所述，通道为参与者提供了一个建立私有子网络的方式，只有通道成员才能访问特定的交易和智能合约。这意味着，敏感的业务关系、价格信息或专有数据可以在需要保密的方之间进行交易，而不会暴露给通道上的所有其他参与者。

##### 私有数据集合（PDCs）
PDCs是Hyperledger Fabric在通道内部提供更细粒度隐私控制的强大功能。它们允许通道中的特定组织子集共享数据，而无需将这些数据暴露给通道上的所有组织。PDCs的引入是为了解决在Fabric v1.2之前，当一组组织需要对其他组织保密数据时，必须创建新的独立通道所带来的管理开销。

PDCs的工作机制如下：
- **数据流**: 在交易提案阶段，包含私有数据参数的交易提案被发送给背书对等节点。这些私有数据参数不会被转发和存储到公共块存储或公共状态数据库。
- **临时存储**: 交易模拟后，私有读写集被临时存储在每个背书对等节点账本中的临时存储数据库（Transient Store Database）中。
- **数据传播**: 背书对等节点通过gossip数据传播协议将生成的私有读写集传播给至少N个其他被授权的集合成员对等节点，以实现数据冗余。
- **公共账本上的哈希**: 私有读写集的哈希值与公共读写集一起被包含在背书的提案响应中。这个哈希值被排序、验证并提交到所有对等节点的公共块存储和公共状态数据库。因此，所有对等节点都能看到哈希，但只有被授权的对等节点才能看到实际的私有数据。
- **私有数据存储**: 被授权的对等节点会验证其临时存储数据库中的私有读写集与哈希是否匹配。验证成功后，私有读写集会被提交到该对等节点的私有读写集存储和私有状态数据库中。
- **数据恢复**: 如果某个被授权的对等节点在背书时缺少私有读写集，它可以通过gossip协议向其他成员对等节点请求缺失的私有读写集。

##### 隐私数据管理与合规
PDCs允许配置数据驻留时间，即通过`blockToLive`属性定期从对等节点中清除私有数据。即使私有数据被清除，其对应的哈希值仍保留在公共块存储中，可用于审计目的。然而，需要注意的是，个人身份信息（PII）不应直接存储在区块链上，即使是加密的PII也不行。对于需要遵循GDPR等数据法规的项目，应通过外部系统存储PII，并使用ID将其与区块链数据关联起来，同时对所有必要信息进行匿名化处理。

#### FISCO BCOS：企业级联盟链平台

FISCO BCOS是一个国产开源的金融级区块链底层平台，以其安全可控、稳定易用、高性能等领先优势而著称。它致力于提升联盟链的性能。FISCO BCOS的特点在于它以太坊公链为基础，提供了更“去中心化”的选择。与Hyperledger Fabric相比，FISCO BCOS在某些方面展示了优势。

##### 节点类型与共识机制
FISCO BCOS将联盟链节点分为共识成员（consensus members）和验证节点（verification nodes）。其共识算法rpBFT将联盟链节点分为共识节点和观察者节点，并且这些节点可以通过控制台互相转换。

| 特性/平台       | Hyperledger Fabric                                                                   | FISCO BCOS                                                                           |
| :-------------- | :----------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------- |
| **架构**        | 模块化、可插拔，包含Peer、Orderer、CA等核心组件                    | 基于以太坊公链，但面向联盟链优化                                          |
| **共识机制**    | Raft (CFT), BFT (v3.0+)                                                | rpBFT                                                                       |
| **隐私机制**    | 通道 (Channels), 私有数据集合 (PDCs)                              | 隐私通道（Private Channels）                                    |
| **节点角色**    | Peer (背书/提交交易), Orderer (排序)                                    | 共识节点 (Sealer), 观察者节点 (Observer), 自由节点 (Free Node)      |
| **智能合约语言** | Go, Java, Node.js                                                          | Solidity                                                                           |
| **应用领域**    | 广泛的企业级应用，如供应链、金融、医疗                                    | 主要面向金融行业，但应用范围正在扩大                                |
| **性能**        | 可定制性高，性能受多种因素影响 (事务大小、区块大小、网络规模)             | 致力于提升联盟链性能                                               |
| **合规性**      | 许可型平台，适用于需要KYC/AML和身份认证的场景                                | 针对金融领域，注重安全可控                                                |

#### 链上与链下数据管理

在构建去中心化数字平台时，如何高效、安全地管理链上和链下数据，并确保真实世界数据能够可信地喂给智能合约，是至关重要的挑战。

##### 预言机解决方案（如Chainlink）
区块链智能合约无法直接访问链外（真实世界）数据，这就需要预言机来桥接链上和链下世界。Chainlink是领先的去中心化预言机网络，能够将资产价格、储备余额和L2排序器健康状况等真实世界数据安全地连接到智能合约。Chainlink预言机网络在安全性和可靠性方面受到DeFi、保险、NFT和游戏公司等行业的信赖。在集成预言机时，需要遵循安全最佳实践，例如使用安全的地址（如硬件钱包）拥有Chainlink节点，并建议继承VRFConsumerBaseV2以增强安全性。

##### 链下存储（IPFS/Arweave）
对于车辆图片、合同文件等大文件，直接存储在区块链上既昂贵又效率低下。最佳实践是采用去中心化存储系统如IPFS (InterPlanetary File System) 或 Arweave 来存储这些大文件。将这些文件的不可变哈希指针存储在链上，可以确保数据的完整性和可追溯性，同时将大文件存储在链下，实现成本和效率的平衡。

#### 真实世界资产（RWA）数字化与智能合约

RWA数字化是区块链领域的重要发展方向，它将实体资产映射为链上数字资产，为融资、流转提供了新的可能性。

##### RWA数字化方案设计
将租赁公司的实体车辆等RWA通过合规方式映射为链上数字资产，需要设计相应的智能合约体系。这包括定义车辆的数字身份、所有权凭证、租赁合同条款以及收益权等，并通过智能合约实现这些资产的质押、融资和流转。例如，可以使用链码实现对私有数据的访问控制，以指定哪些客户端可以查询集合中的私有数据。私有数据也可以通过链码在不同的集合之间共享或转移。

##### 智能合约开发与安全
智能合约（在Fabric中称为“链码”）是区块链应用程序的业务逻辑，作为受信任的分布式应用程序运行。它们可以在标准编程语言（如Java、Go和Node.js）中编写。智能合约的安全性至关重要，因为它们处理着链上资产和业务逻辑。在开发智能合约时，需要关注参数的传递方式，例如通过`transient field`传递，以避免敏感信息存储在公共区块中。代码审计和严格的测试是确保智能合约安全的关键环节。

#### 性能优化与可伸缩性

Hyperledger Fabric的性能和可伸缩性是企业部署中的关键考量。性能受多种变量影响，包括事务大小、区块大小、网络规模以及CPU、内存、磁盘I/O等硬件资源。

##### 网络配置优化
- **对等节点数量**: 实验结果表明，每个组织8个对等节点，背书策略为2/8，可以使公共交易性能提高32%，私有交易性能提高21%。
- **客户端数量**: 增加客户端数量以分散工作负载对公共交易性能影响为0，但对私有交易性能有4%的提升。
- **通道数量**: 通道数量增加会导致公共交易性能下降2%，私有交易性能提高13%。
- **排序服务**: 在请求速率低于1500 tx/s时，拥有多达64个排序节点的Raft排序服务不会成为瓶颈，足以满足大多数场景需求，因为它允许31个节点崩溃仍能保持网络功能。

##### 查询优化
为了避免“影子读取”（shadow reads），即读取过时数据的问题，应避免在Fabric中使用富查询（rich queries）。更好的做法是使用键或部分键进行查询，然后在链码中进行过滤。如果必须使用富查询，创建索引可以加速查询响应，但需要注意索引的更新频率和对CPU的占用。此外，应区分存储在世界状态和账本中的数据，因为世界状态数据的维护任务会影响性能。

##### 隐私与性能的权衡
私有数据集合的实现虽然增强了隐私，但也会对性能产生影响。例如，与LevelDB相比，使用Apache CouchDB™作为状态数据库时，写入吞吐量可能会降低。在设计网络时，必须根据业务需求权衡隐私级别、性能要求和管理复杂性。例如，需要详细分析业务对数据隐私的需求，并据此创建PDCs。同时，避免在区块链上存储所有数据，特别是PII数据，以符合数据隐私法规。

### Sources 

[1] A Case Study on Ethereum, Fabric, Sawtooth and Fisco-Bcos. (2025). https://www.researchgate.net/publication/344303589_Performance_Evaluation_on_Blockchain_Systems_A_Case_Study_on_Ethereum_Fabric_Sawtooth_and_Fisco-Bcos

[2] A dynamic resource-aware endorsement strategy for improving ... (2023). https://www.sciencedirect.com/science/article/abs/pii/S0957417423004918

[3] A Privacy-Preserving Framework Using Hyperledger Fabric for EHR ... (n.d.). https://www.researchgate.net/publication/372331818_A_Privacy-Preserving_Framework_Using_Hyperledger_Fabric_for_EHR_Sharing_Applications

[4] Aggarwal, S., & Kumar, N. (2021). Chapter Sixteen - Hyperledger. Adv. Comput. https://linkinghub.elsevier.com/retrieve/pii/S0065245820300711

[5] Aleksieva, V., Valchanov, H., & Huliyan, A. (2020). Implementation of Smart-Contract, Based on Hyperledger Fabric Blockchain. 2020 21st International Symposium on Electrical Apparatus & Technologies (SIELA). https://ieeexplore.ieee.org/document/9167043/

[6] Androulaki, E., Cachin, C., Caro, A. D., Sorniotti, A., & Vukolic, M. (2017). Permissioned Blockchains and Hyperledger Fabric. ERCIM News. https://www.semanticscholar.org/paper/37cf7d80d1007eb085ad15d504b95e45ceb7d9d0

[7] Baliga, A., Solanki, N., & Verekar, S. (2018). Performance characterization of hyperledger fabric. https://ieeexplore.ieee.org/abstract/document/8525394/

[8] Benhamouda, F., & Halevi, S. (2019). Supporting private data on hyperledger fabric with secure multiparty computation. https://ieeexplore.ieee.org/abstract/document/8700297/

[9] Best Practices for Oracle Integration with Chainlink - 7BlockLabs. (n.d.). https://7blocklabs.com/blog/best-practices-for-oracle-integration-with-chainlink

[10] Bogatov, D., Caro, A. D., Elkhiyaoui, K., & Tackmann, B. (2019). Anonymous Transactions with Revocation and Auditing in Hyperledger Fabric. IACR Cryptol. ePrint Arch. https://link.springer.com/chapter/10.1007/978-3-030-92548-2_23

[11] Bonet, V., & David, M. (2014). EasyProf 3.0. https://www.semanticscholar.org/paper/75467e2d05be76d5453d8d39a3a141a75840cb2f

[12] Bortnikov, E., & Konstantinos, C. (2018). Hyperledger fabric: a distributed operating system for permissioned blockchains. https://lists.lfdecentralizedtrust.org/g/perf-and-scale-wg/attachment/281/0/1801.10228v1.pdf

[13] Cao, B., Yan, Z., & Xia, X. (2023). Web3. IEEE Commun. Mag. https://ieeexplore.ieee.org/document/10230032/

[14] Chainlink Data Feeds. (n.d.). https://docs.chain.link/data-feeds

[15] Chainlink VRF and Security Considerations | by Jose María de la Cruz. (2023). https://medium.com/@0xjmaria/chainlink-vrf-and-security-considerations-323ffca72d59

[16] Channel Creation failed: Only 0 policies were satisfied, but needed ... (2020). https://stackoverflow.com/questions/65310894/channel-creation-failed-only-0-policies-were-satisfied-but-needed-1-of-order

[17] Demystifying Hyperledger Fabric (2/3): Private Data Collection. (2019). https://medium.com/coinmonks/demystifying-hyperledger-fabric-2-3-private-data-collection-164220ecafa5

[18] Deploy the peer — Hyperledger Fabric Docs main documentation. (n.d.). https://hyperledger-fabric.readthedocs.io/en/latest/deploypeer/peerdeploy.html

[19] Designing a Hyperledger Fabric Network | by Techie Marketer. (2019). https://medium.com/coinmonks/designing-a-hyperledger-fabric-network-7adcd78dabc3

[20] Di, J., & Zang, Q. (2021). Research on Drug Supervision System Based on Fisco Bcos Blockchain. Frontiers in Business, Economics and Management. https://drpress.org/ojs/index.php/fbem/article/view/209

[21] Distributed optimization and scheduling strategy for source load ... (2024). https://www.aimspress.com/article/doi/10.3934/energy.2024044?viewType=HTML

[22] Duarte, H. (2024). Product Quality Certification Using Blockchain. https://repositorio.ulisboa.pt/handle/10400.5/95609

[23] Ezzat, S., Saleh, Y., & Abdel-Hamid, A. (2022). Blockchain oracles: State-of-the-art and research directions. IEEE Access. https://ieeexplore.ieee.org/abstract/document/9801856/

[24] FISCO BCOS. (n.d.). https://www.fisco.com.cn/en/fisco_20.html

[25] FISCO BCOS: Challenging Hyperledger Fabric with a Consortium ... (2018). https://www.prnewswire.com/news-releases/fisco-bcos-challenging-hyperledger-fabric-with-a-consortium-chain-from-china-300733474.html

[26] FISCO-BCOS: An Enterprise-grade Permissioned Blockchain ... (2025). https://www.researchgate.net/publication/375656640_FISCO-BCOS_An_Enterprise-grade_Permissioned_Blockchain_System_with_High-performance

[27] Gottschalk, S. (2022). International financial regulation of smart contracts and asset-backed tokens. SSRN Electronic Journal. https://www.semanticscholar.org/paper/8cebd268d5777d4bdb461d94d819c1407b785452

[28] Group members management - FISCO BCOS 2.0 - Read the Docs. (n.d.). https://fisco-bcos-documentation.readthedocs.io/en/latest/docs/manual/node_management.html

[29] Houghton, R. (2013). The Chain-Link Fence Model: A Framework for Creating Security Procedures. https://www.semanticscholar.org/paper/e6e29bcb1f89ecb41bf78195c7d4dae9c92dfb23

[30] Hyperledger Fabric - Role of member vs peer. (2021). https://stackoverflow.com/questions/67405125/hyperledger-fabric-role-of-member-vs-peer

[31] Hyperledger Fabric cheat sheet - SoftwareMill. (n.d.). https://softwaremill.com/hyperledger-fabric-cheat-sheet/

[32] Hyperledger Fabric Node Deployment Service - LeewayHertz. (n.d.). https://www.leewayhertz.com/hyperledger-fabric-node-deployment-services/

[33] Hyperledger Fabric v2.3 Example Network Setup — Identities(Part I). (2021). https://medium.com/stm-blockchain/hyperledger-fabric-v2-3-example-network-setup-identities-168b5d4931cc

[34] Introduction — FISCO BCOS v2 EN v2.9.0 documentation. (n.d.). https://fisco-bcos-documentation.readthedocs.io/en/latest/docs/introduction.html

[35] Introduction — Hyperledger Fabric Docs main documentation. (2023). https://hyperledger-fabric.readthedocs.io/en/release-2.5/whatis.html

[36] Jarunde, N. (2025). From Equity to Real Estate: The Institutionalization of Asset Tokenization in Capital Markets. https://www.researchgate.net/profile/Nikhil-Jarunde/publication/394260274_From_Equity_to_Real_Estate_The_Institutionalization_of_Asset_Tokenization_in_Capital_Markets/links/68962987c345306d43cc33fc/From-Equity-to-Real-Estate-The-Institutionalization-of-Asset-Tokenization-in-Capital-Markets.pdf

[37] Jiang, L., Chang, X., Liu, Y., Misic, J., & Mišić, V. (2020). Performance analysis of Hyperledger Fabric platform: A hierarchical model approach. Peer-to-Peer Networking and Applications. https://link.springer.com/article/10.1007/s12083-019-00850-z

[38] Jonckheere, M., Ball, R. D., & Folinsbee, J. T. (1990). Characterization and analysis of chain-link fences. IEEE International Carnahan Conference on Security Technology, Crime Countermeasures. https://ieeexplore.ieee.org/document/111397/

[39] Kangogo, D., & Kocsis, I. (2024, January 1). Requirement-based, structural design for confidentiality in Hyperledger Fabric. Proceedings of the 31th Minisymposium. https://repozitorium.omikk.bme.hu/handle/10890/55187

[40] Kasula, V., Rakki, S., & Banoth, R. (2025). Enhancing Hyperledger Fabric Security with Lightweight Post-Quantum Cryptography and National Cryptographic Algorithms. https://ieeexplore.ieee.org/abstract/document/11008110/

[41] Ke, Z., & Park, N. (2022). Performance modeling and analysis of Hyperledger Fabric. Cluster Computing. https://link.springer.com/article/10.1007/s10586-022-03800-2

[42] Kumar, B. A. (2021). Developing Business-Business Private Block-Chain Smart Contracts Using Hyper-Ledger Fabric for Security, Privacy and Transparency in Supply Chain. https://link.springer.com/chapter/10.1007/978-981-16-2937-2_26

[43] Li, C., Shang, L., Wei, Z., Ge, J., Zhang, M., & Fang, Y. (2022). Commodity-Tra: A Traceable Transaction Scheme Based on FISCO BCOS. https://link.springer.com/chapter/10.1007/978-981-19-7242-3_17

[44] Maesa, D., & Mori, P. (2020). Blockchain 3.0 applications survey. J. Parallel Distributed Comput. https://linkinghub.elsevier.com/retrieve/pii/S0743731519308664

[45] Mahadev, R. (2019). Cloaking fabric, a confidentiality layer for hyperledger fabric. https://www.semanticscholar.org/paper/6b45ba0836656a04b80a48e9626bc725c2e81820

[46] Mastering Hyperledger Fabric: A Comprehensive Guide to ... (2024). https://www.intellecteu.com/blog/mastering-hyperledger-fabric-a-comprehensive-guide-to-network-management-and-private-data-collections

[47] Meir, H., Barger, A., & Manevich, Y. (2019, May 22). Increasing concurrency in hyperledger fabric. Proceedings of the 12th ACM International Conference on Systems and Storage. https://dl.acm.org/doi/10.1145/3319647.3325841

[48] Mikalsen, J. (2018). Firechain: An efficient blockchain protocol using secure gossip. https://munin.uit.no/handle/10037/13115

[49] [PDF] Blockchain Design for a Secure Pharmaceutical Supply Chain. (2025). https://scholarworks.umass.edu/server/api/core/bitstreams/dcabb4ca-524c-4422-a52d-139b51b4d1bf/content

[50] Performance comparison of FISCO BCOS, Hyperledger Fabric, and ... (n.d.). https://www.researchgate.net/figure/Performance-comparison-of-FISCO-BCOS-Hyperledger-Fabric-and-Ethereum_tbl1_382664966

[51] Pericherla, A., Paul, P., Sural, S., Vaidya, J., & Atluri, V. (2022). Towards Supporting Attribute-Based Access Control in Hyperledger Fabric Blockchain. IFIP Advances in Information and Communication Technology. https://link.springer.com/chapter/10.1007/978-3-031-06975-8_21

[52] Rao, K. V., Teja, M. S., Reddy, P. P., & Saikrishna, S. (2020). Building Permissioned Blockchain Networks Using Hyperledger Fabric. https://www.taylorfrancis.com/books/9781000178753/chapters/10.1201/9781003032588-12

[53] Roh, C., & Shin, D.-M. (2024). A Study on the Application of LBAC usingX.509 Certificates in Hyperledger Fabric Environments. Journal of Software Assessment and Valuation. https://www.semanticscholar.org/paper/d6595a9ee9997adaf50b9a8fa879d3ad9852605c

[54] Safari, M., Rezaei, N., & Khonsari, A. (2025). Blockchain-Enabled Federated Learning: A Hyperledger Fabric Approach for Secure IoT Systems. https://ieeexplore.ieee.org/abstract/document/10967432/

[55] Schaefer, C., & Edman, C. (2019). Transparent logging with hyperledger fabric. https://ieeexplore.ieee.org/abstract/document/8751339/

[56] Security and Operation Best Practices | Chainlink Documentation. (2025). https://docs.chain.link/chainlink-nodes/resources/best-security-practices

[57] Sharma, A., Schuhknecht, F., & Agrawal, D. (2018). How to databasify a blockchain: the case of hyperledger fabric. https://arxiv.org/abs/1810.13177

[58] Shashidhara, R., & Nair, R. (2025). Promise of Zero-Knowledge Proofs (ZKPs) for Blockchain Privacy and Security: Opportunities, Challenges, and Future Directions. https://onlinelibrary.wiley.com/doi/full/10.1002/spy2.461?msockid=165e478c84ed69cb1150510a85416880

[59] Sousa, J., Bessani, A., & Vukolic, M. (2017). A Byzantine Fault-Tolerant Ordering Service for the Hyperledger Fabric Blockchain Platform. 2018 48th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN). https://arxiv.org/abs/1709.06921

[60] Student, M. (n.d.). USING REAL-WORLD DATA IN BLOCKCHAIN SYSTEMS. https://nikola-pavlov.com/papers/using-real-world-data-in-blockchain-systems.pdf

[61] Thakkar, V., & Shah, V. M. (2023). Empowering Privacy: Harnessing Hyperledger Fabric to Safeguard EHR Systems. Journal of Computer Science. https://thescipub.com/abstract/10.3844/jcssp.2023.1292.1304

[62] The Ordering Service - Hyperledger Fabric - Read the Docs. (2025). https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html

[63] Using Private Data in Fabric - Hyperledger Fabric - Read the Docs. (n.d.). https://hyperledger-fabric.readthedocs.io/en/latest/private_data_tutorial.html

[64] Verhoeff, T., & Verhoeff, K. (2011). From chain-link fence to space-spanning mathematical structures. Tissue Engineering Part C-Methods. https://www.semanticscholar.org/paper/e2e0a88f52f16c72357e9e0b431d6b3485a7d888

[65] Vu, N. (2024). Tackle the Oracle Problem: Enhancing Trust and Functionality for Smart Contracts Through Blockchain Oracle. https://ro.uow.edu.au/ndownloader/files/50575734/1

[66] Wang, H., Ou, W., & Han, W. (2022). A Novel Logistics Scheme Based on Zero-Trust Model. https://link.springer.com/chapter/10.1007/978-3-031-17081-2_13

[67] Wang, S., Yang, M., Zhang, Y., Luo, Y., & Ge, T. (2021). On private data collection of hyperledger fabric. https://ieeexplore.ieee.org/abstract/document/9546412/

[68] Wang, Y., Tian, Y., Yin, X., & Hei, X. (2020). A trusted recommendation scheme for privacy protection based on federated learning. CCF Transactions on Networking. https://link.springer.com/article/10.1007/s42045-020-00045-8

[69] Wu, W., Kotaki, M., Hamada, H., Inoda, M., Maekawa, Z., Kanamaru, R., & Sanae, N. (1992). Bending properties of 2.5 Dimensional Warp Knitted Fabric Reinforced Composites. Advanced Composites Letters. https://journals.sagepub.com/doi/10.1177/096369359200100603

[70] Xu, Z., Ye, K., Dong, X., Han, H., Yan, Z., Chen, X., Liao, D., & Wang, H. (2022). DC-Gossip: An Enhanced Broadcast Protocol in Hyperledger Fabric Based on Density Clustering. https://link.springer.com/chapter/10.1007/978-3-031-19211-1_1

[71] Yang, X., Hou, J., Xu, L., & Zhu, L. (2025). zkFabLedger: Enabling Privacy Preserving and Regulatory Compliance in Hyperledger Fabric. IEEE Transactions on Network and Service Management. https://ieeexplore.ieee.org/document/10839283/

[72] Yao, L., Chen, X., Liu, Y., Hua, X., & Liu, M. (2024, July 19). Events Industry in the Web 3.0 Era: Empirical Analysis of Smart Contract Applications from China. Proceedings of the 2024 15th International Conference on E-Business, Management and Economics. https://dl.acm.org/doi/10.1145/3691422.3691484

[73] Zhao, L., & San, A. (2004). Message_Digest Algorithm 5 in Security Attestation of LINUX. Electro-Optics & Passive Countermeasures. https://www.semanticscholar.org/paper/c347276d745664fa6ec00950394dccc428ac36cf

[74] Zhou, E., Pi, B., Sun, J., Miyamae, T., & Morinaga, M. (2022). Performance Improvement by Using Pipelined Execution on Hyperledger Fabric. https://www.semanticscholar.org/paper/205d3b61dbe983d17ba56fb23f1afb5b0c698210

[75] Ковачевић, И., наука, Ф. техничких, & Сад, Н. (2022). HYPERLEDGER FABRIC BLOCKCHAIN -A. https://www.semanticscholar.org/paper/873077b6fd648ce8ac354020817467824cea75c0

[76] 陳君虹. (2020). Hyperledger Fabric 應用於全民公投之連署書驗證暨查詢平台. https://www.semanticscholar.org/paper/3bc0dbb04daf6fc473ed4d5f4a0d65f46b2200a9

[77] 龙静张. (2021). Hyperledger Fabric Endorsement Strategy Proposal Distribution Improvement Plan. Computer Science and Application. https://www.hanspub.org/journal/doi.aspx?DOI=10.12677/CSA.2021.114119
