To effectively test and verify TPS and cross-chain communication for Aleph Zero, first specify the cloud environment, system requirements (CPU, RAM, disk, bandwidth), number of nodes, and node topology, then outline the necessary resources, components, tools, and strategies for deployment, testing, and verification. Finally, provide step-by-step guidance to build a local network on Ubuntu, test and verify TPS, and implement cross-chain communication testing and verification. Use lists and tables for clarity and readability.

Sat Jul 12 2025

### Cloud Environment Recommendations for Aleph Zero Node Deployment

For effective testing of Transactions Per Second (TPS) and cross-chain communication on Aleph Zero, deploying nodes within a reliable and low-latency cloud environment is highly recommended. Cloud providers are often chosen for practical reasons, despite the preference for personal hardware from a decentralization standpoint. Amazon Web Services (AWS) is a recommended option, with specific instances like `c5d.4xlarge` or higher, equipped with `gp3 EBS` storage configured to 16,000 IOPS. For superior disk performance, `NVMe Local Instances` are preferred over EBS. Beyond traditional cloud providers, platforms such as OnFinality offer managed multi-cloud solutions that facilitate easy deployment, monitoring, and scaling of Aleph Zero testnet nodes, supporting validator, full, and archive node types. Additionally, innovative decentralized cloud solutions like Acurast are integrated with Aleph Zero, providing cost-effective and privacy-focused computational resources, which can serve as an alternative cloud environment for node deployment.

### System Requirements for Aleph Zero Nodes

The system requirements for Aleph Zero nodes vary based on their designated role, such as validator, archive, or compute resource node, but a general baseline ensures effective testing and deployment. For validator nodes, a **CPU** with at least 8 modern `x86_64` cores from Intel or AMD is recommended for efficient computation. Compute Resource Nodes, conversely, necessitate more robust CPUs, with a minimum of 12 cores/24 threads operating at a clock speed of 2.4GHz or higher, including examples like Intel Xeon and AMD EPYC processors. In terms of **RAM**, validator nodes should possess approximately 32 GB to ensure stable operation. Compute Resource Nodes benefit from higher RAM, with a minimum of 64 GB recommended, and 128 GB or more suggested for optimal performance with multiple concurrent workloads. For **disk storage**, validator nodes running pruned configurations require a minimum of 500 GB `NVMe SSD` for fast input/output operations. Archive nodes, which store complete historical blockchain data, need at least 2 TB `NVMe SSD` storage. Compute Resource Nodes require at least 1 TB `NVMe SSD`, although datacenter-grade HDDs with large and fast caches can also be used. Regarding **network bandwidth**, validator nodes require a sustained connection of at least 100 Mbps with low latency and high reliability. Compute Resource Nodes should have a minimum of 500 Mbps bandwidth, with 1 Gbps recommended for peak performance. It is also noteworthy that running nodes on bare-metal servers is generally preferred for performance and reliability, as virtualized environments might be less suitable for compute resource nodes.

### Number of Nodes and Topology for Testing

For comprehensive TPS and cross-chain communication testing on Aleph Zero, a specific node count and network topology are crucial. Historically, Aleph Zero's TPS tests have involved deploying around 112 nodes geographically distributed across five continents to simulate a real-world, decentralized environment. This extensive setup enabled the network to achieve impressive validation times of approximately 416 milliseconds for a simulated 89,600 TPS. For robust cross-chain communication, a sufficiently distributed and redundant set of nodes, similar in scale to those used for TPS testing, is necessary to ensure security and reliability in message passing.

The node topology adopted by Aleph Zero for testing purposes is a distributed network of validator nodes operating under a rotating committee model and a "hub and spoke" architecture. A rotating committee of validators, typically exceeding 100 members (e.g., currently almost 132 active validators with 50 chosen for block production), secures and validates transactions. These committees are re-elected periodically, such as every 15 minutes, ensuring a dynamic group and bolstering decentralization and robustness. The geographical distribution, with nodes deployed across multiple cloud regions (e.g., 112 AWS nodes across five continents), is vital for scaling tests and replicating real-world network conditions. Aleph Zero employs a "hub and spoke" model, where the main public blockchain serves as the "hub," and businesses or private instances act as "spokes," facilitating trustless and efficient interaction while maintaining private networks. The platform utilizes a Directed Acyclic Graph (DAG) as an intermediary data structure, which enables parallel transaction processing and consensus ordering, contributing to its speed and scalability. The core consensus protocol, AlephBFT, is an asynchronous Byzantine Fault Tolerant (aBFT) and leaderless protocol, designed to maintain network resilience even if up to 33% of nodes behave maliciously. For cross-chain communication, Aleph Zero leverages bridges such as MOST for Ethereum connectivity and has strategically acquired a parachain slot for a unique bridge to Polkadot, which relies on the consensus models of both chains rather than smart contracts. Furthermore, integration with Router Protocol enhances its interoperability across diverse blockchain networks.

### Necessary Resources, Components, and Tools

To effectively deploy, test, and verify Aleph Zero's TPS and cross-chain communication, a comprehensive set of resources, components, and tools is required. For cloud and hardware resources, it is essential to utilize reliable, low-latency cloud providers like AWS, deploying instances comparable to or exceeding `c5d.4xlarge` with `NVMe SSD` storage configured for high IOPS. Node hardware specifications for validators should include a minimum of 8 modern CPU cores (Intel or AMD), at least 32 GB of RAM, and a minimum of 500 GB `NVMe SSD` for pruned nodes. Network bandwidth should be at least 100 Mbps with low latency.

The necessary Aleph Zero node software includes validator, full, or archivist node binaries appropriately configured, alongside the implementation of the AlephBFT consensus protocol. Configuration files for node parameters and telemetry monitoring are also vital. Deployment and orchestration tools should include containerization platforms such as Docker for consistent node environments and Infrastructure as Code tools like Terraform or Ansible for automated provisioning. For monitoring and metrics, Grafana dashboards and Prometheus are recommended for collecting and visualizing telemetry and performance data.

Regarding testing and verification, specialized TPS testing tools are needed to generate and measure transaction throughput on Aleph Zero nodes. For cross-chain communication, frameworks that support protocols like Router Protocol and Polkadot-JS are beneficial for integration and testing. Comprehensive logging and analytics tools are also essential for detailed transaction and event logging to verify throughput and communication correctness. The network topology should support a global node network of around 100 or more nodes to ensure realistic TPS and cross-chain testing scenarios, along with rotating validator committees that incorporate secure random selection mechanisms. Lastly, access to Aleph Zero's official documentation and community resources is important for support and up-to-date information, particularly concerning testnet environments that mirror mainnet conditions.

### Strategies for Deployment, Testing, and Verification

Effective deployment of Aleph Zero nodes and setting up a test environment for TPS and cross-chain communication verification involves several strategic considerations. For deployment, it is advisable to utilize reliable, low-latency cloud providers such as AWS, with instances like `c5d.4xlarge` or better, configured with `NVMe SSD` storage for high IOPS. Hardware specifications for nodes should adhere to minimums of 8 modern CPU cores, 32 GB RAM, 500 GB `NVMe SSD` for pruned nodes, and at least 100 Mbps low-latency network bandwidth. To mimic a truly decentralized and distributed network for accurate testing, approximately 100 to 112 nodes should be deployed globally, for example, across five continents. A rotating validator committee, selected randomly for consensus, is essential to maintain decentralization and robustness in the network.

Deployment strategies should involve using provided deployment scripts with sensible defaults, while allowing for careful customization of runtime parameters like node type, telemetry, and pruning to ensure node functionality. Node binaries can be built from source or deployed using prebuilt Docker images for streamlined setup. It is crucial to maintain up-to-date node software versions to ensure network compatibility and performance.

For testing and verifying TPS, specialized tools capable of generating high transaction loads and measuring throughput are necessary. Monitoring tools like Prometheus and Grafana should be implemented to gather telemetry data, including transaction latency, throughput, and resource utilization during tests. Tests should be conducted under various load conditions to assess stability, scalability, and fault tolerance, with a focus on repeatability for consistent results and regression detection. Early and frequent integration of performance testing into the continuous integration pipeline is also recommended to promptly identify performance issues.

To verify cross-chain communication, employing decentralized frameworks that ensure secure, atomic, and trustless smart contract execution across chains without centralized intermediaries is a key strategy. Cryptographic proofs, such as signatures, hashes, zero-knowledge proofs, and receipts, are fundamental for verifying the authenticity and atomicity of cross-chain transactions. Tests should simulate cross-chain smart contract calls, ensuring state consistency and correct execution across heterogeneous blockchains. Validation of authentication and authorization of cross-chain messages is performed by verifying blockchain identities, collateral lockups, and transaction mempools. Detailed logs of cross-chain communication events should be captured and monitored to verify message flow, latencies, and error handling. Security and Denial-of-Service (DoS) mitigation analysis should also be performed, potentially incorporating economic cost mechanisms and isolated chain state handling.

### Step-by-Step Guide for Local Network Setup on Ubuntu

To establish a local Aleph Zero network on Ubuntu for testing TPS and cross-chain communication, follow these steps:

1.  **Prepare Your Ubuntu System**: Ensure your Ubuntu system is version 20.04 LTS or newer. Update system packages by running `sudo apt update && sudo apt upgrade -y`.
2.  **Install Required Dependencies**: Install Docker and Docker Compose for containerized node deployment using `sudo apt install -y docker.io docker-compose`. Optionally, add your user to the `docker` group with `sudo groupadd docker` and `sudo usermod -aG docker $USER`, then apply changes with `newgrp docker`.
3.  **Obtain Aleph Zero Node Software**: Clone the Aleph Node Runner repository using `git clone https://github.com/Cardinal-Cryptography/aleph-node-runner` and navigate into the directory with `cd aleph-node-runner`. Regular updates to the repository are advised for new releases and patches.
4.  **Configure and Run Nodes**: Execute the node setup script with `./run_node.sh -n <your_node_name> --ip <your_public_ip>` for each node, providing a unique name and IP address. Ensure that ports 9944, 30333, and 30343 are open and available.
5.  **Monitor Node Logs and Status**: Use `docker logs -f <your_node_name> --tail 20` to monitor node activity and confirm successful startup and network connections.
6.  **Node Updates and Maintenance**: To update a node, first stop it with `docker stop <your_node_name>`, then pull the latest changes from the repository, and re-run the script.
7.  **Local Network Considerations**: For a meaningful testnet, deploy multiple nodes (e.g., 10 or more) on your local or cloud Ubuntu instances. Automate deployment and management using container orchestration or custom scripts.
8.  **Additional Tools**: For real-time performance analysis, enable telemetry and monitoring via Prometheus and Grafana.

### Step-by-Step Guide to Test and Verify TPS on the Local Aleph Zero Network

To accurately test and verify the Transactions Per Second (TPS) on a local Aleph Zero network, follow these steps:

1.  **Set Up the Local Network Environment**: Ensure your Ubuntu 20.04 LTS or newer system is prepared with adequate hardware specifications. Each node should have at least 4 CPU cores, a minimum of 8 GB RAM (more for higher throughput), SSD storage with at least 100 GB for blockchain data, and a stable network connection of at least 100 Mbps.
2.  **Determine Number of Nodes and Topology**: Deploy a minimum of 10 validator nodes to create a representative testnet. Configure these nodes in a peer-to-peer mesh network to ensure full connectivity, assigning unique IP addresses and opening necessary ports (typically 9944, 30333, and 30343).
3.  **Install Dependencies**: Install Docker and Docker Compose on all machines. Clone the Aleph Zero node runner repository to simplify node deployment and management.
4.  **Deploy Aleph Zero Nodes**: Use the provided run scripts to launch each Aleph Zero node within Docker containers. Monitor the logs from each container to confirm that nodes start successfully and establish network connections.
5.  **Prepare TPS Testing Tools**: Utilize specialized TPS benchmarking tools compatible with Aleph Zero to generate concurrent transaction loads. Integrate Prometheus and Grafana to visualize real-time performance data, including throughput and latency.
6.  **Conduct TPS Testing**: Initiate controlled transaction traffic at varying loads to stress test the network. Continuously monitor key metrics such as TPS, transaction latency, block confirmation times, and resource utilization (CPU, RAM, disk I/O).
7.  **Analyze Results**: Collect and analyze the logs and performance metrics to verify the TPS performance of your local network. Confirm transaction finality and ensure that no transactions are dropped or stalled during the tests.
8.  **Iterate and Optimize**: Based on the analysis, adjust node counts, hardware resources, or network configurations to identify optimal settings for TPS. Thoroughly re-test any changes to confirm improvements in performance and stability.

### Step-by-Step Guide to Implement and Verify Cross-Chain Communication Testing on Local Network

To implement and verify cross-chain communication testing on a local Aleph Zero network, proceed with the following steps:

1.  **Prepare Your Environment**: Ensure your Ubuntu 20.04 LTS or newer system is adequately equipped with a multi-core CPU, at least 16 GB of RAM, 100 GB or more of SSD storage, and a network bandwidth of 1 Gbps or higher to support multiple nodes and cross-chain traffic.
2.  **Set Up Aleph Zero Nodes for the Local Testnet**: Deploy multiple Aleph Zero nodes (preferably 10 or more) using Docker and Docker Compose for efficient network simulation. Assign unique node names and IP addresses to each instance, ensuring that ports 9944, 30333, and 30343 are open. Utilize scripts from the Aleph Node Runner repository, such as `run_node.sh`, to automate node setup and management.
3.  **Deploy Cross-Chain Components**: Integrate cross-chain bridges like MOST to enable communication between your local Aleph Zero network and a simulated Ethereum environment. For Polkadot connectivity, deploy the zParachain bridge using the acquired parachain slot. Additionally, consider integrating Router Protocol's Cross-Chain Intent Framework (CCIP) to broaden interoperability with other blockchain networks.
4.  **Set Up Testing Frameworks and Tools**: Implement or simulate cross-chain transactions by developing smart contracts designed to facilitate asset transfers and message passing between the interconnected chains. Use testing tools compatible with Aleph Zero's ink! smart contract environment for contract deployment and interaction. Implement telemetry and monitoring tools like Prometheus and Grafana to capture critical performance metrics during cross-chain interactions.
5.  **Testing Cross-Chain Communication**: Conduct rigorous tests involving asset transfers across the interconnected chains via MOST or other configured bridges, verifying the successful passage and finality of messages. Perform verification of transaction inclusion and message authenticity using cryptographic proofs and by observing relayer activities. Monitor logs from both the Aleph Zero nodes and the bridge components for any communication errors or security vulnerabilities. Validate that guardians within the bridge architectures are performing their expected roles and governance actions without faults.
6.  **Verification and Analysis**: Analyze the collected metrics to ensure that cross-chain transactions meet predefined speed, throughput, and security requirements. Utilize on-chain audits and detailed logs to confirm the atomicity and consistency of cross-chain smart contract interactions. Proactively address any security vulnerabilities detected during testing, including potential attack vectors related to light clients or relayers.
7.  **Iterate and Scale**: Increase the network size or complexity of the simulated cross-chain environment to replicate production-like conditions. Adjust node and network configurations based on initial test results to optimize performance and reliability of the cross-chain communication pathways.

Bibliography
About Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/explore/about-aleph-zero

Acurast’s Unstoppable Compute Accessible On Aleph Zero - Medium. (2024). https://acurast.medium.com/acurasts-unstoppable-compute-accessible-on-aleph-zero-48c10b516e67

AJ Akbarfam, G Dorai, & H Maleki. (2024). Secure Cross-Chain Provenance for Digital Forensics Collaboration. https://ieeexplore.ieee.org/abstract/document/10835543/

Aleph Zero Case Study - AWS setup of blockchain networks. (n.d.). https://10clouds.com/case-studies/alephzero/

Aleph Zero is a gem in the Polkadot Ecosystem!! - Medium. (2023). https://medium.com/@polkanotes/aleph-zero-is-a-gem-in-the-polkadot-ecosystem-92e5369a62da

Aleph Zero: Learn Everything from its Detailed Working to Unique ... (2023). https://www.antiersolutions.com/blogs/demystifying-aleph-zero-working-benefits-native-currency-unique-features/

Aleph Zero Q4 Overview - Reflexivity Research. (2022). https://www.reflexivityresearch.com/free-reports/aleph-zero-q4-overview

Anna Pappa. (2023). Trust your network with entanglement. In Nature Physics. https://www.nature.com/articles/s41567-023-01957-0

B Sowa. (n.d.). Control software and simulation environment for the Aleph2 robot–a Mars rover prototype. https://ii.uni.wroc.pl/media/uploads/2020/10/21/sowa-bazej.pdf

Blockchain Interoperability: Cross-chain at scale | Chainstack Blog. (2024). https://chainstack.com/blockchain-interoperability-cross-chain-at-scale/

Breaking the Limits: The Power of Aleph Zero’s Layer 1 ... - Medium. (2023). https://medium.com/@researchcoindelta/breaking-the-limits-the-power-of-aleph-zeros-layer-1-zero-knowledge-proof-system-e4dad99cc9c9

Building from source | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/building-and-running-from-source-advanced/building-from-source

Charles W. Husbands. (2004). Adding Non-Latin Data to ALEPH. https://www.semanticscholar.org/paper/a35ba871a588232a1f2cf01d5dc5631108bf371d

Chuanqi Tao & J. Gao. (2017). On building a cloud-based mobile testing infrastructure service system. In J. Syst. Softw. https://www.semanticscholar.org/paper/41578c29bd0b6aba38be126a7e5e7660e2f30690

Compute Resource Nodes Introduction - Aleph Cloud. (n.d.). https://docs.aleph.cloud/nodes/compute/introduction/

Cross-Chain Functionality Testing Checklist - QAwerk. (2025). https://qawerk.com/blog/cross-chain-functionality-testing-checklist/

Customizing your setup | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/customizing-your-setup

D. Hadley. (1967). Testing for Performance. In Nature. https://www.semanticscholar.org/paper/476e143a3727898173545d428083adcd5a7b72ff

D Mishra & S Phansalkar. (2025). Blockchain Security in Focus: A Comprehensive Investigation into Threats, Smart Contract Security, Cross-Chain Bridges, Vulnerabilities Detection Tools & …. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/10946113/

Debajani Mohanty. (2018). Testing Strategy for Ethereum Dapps. https://link.springer.com/chapter/10.1007/978-1-4842-4075-5_8

DSS Torres & H Cervantes. (2024). Towards a Systematic Refactoring Method to Support Deployability. https://ieeexplore.ieee.org/abstract/document/10795585/

H Mao, T Nie, H Sun, D Shen, & G Yu. (2022). A survey on cross-chain technology: Challenges, development, and prospect. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9982450/

Hardware requirements - Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/use/validate/hardware-requirements

How to Debug and Test Cross-Chain and Multi-Chain Transactions. (2023). https://www.linkedin.com/advice/1/what-best-ways-debug-test-cross-chain-multi-chain-transactions

How To Set Up A Validator For Aleph Zero Testnet On OnFinality. (2022). https://onfinality.medium.com/how-to-set-up-a-validator-for-aleph-zero-testnet-on-onfinality-df941bf6e8a2

how to test the TPS in private blockchain - Ethereum Stack Exchange. (2018). https://ethereum.stackexchange.com/questions/51546/how-to-test-the-tps-in-private-blockchain

Hui Wang, Yu-lang Cen, & Xuefeng Li. (2017). Blockchain Router: A Cross-Chain Communication Protocol. In Proceedings of the 6th International Conference on Informatics, Environment, Energy and Applications. https://dl.acm.org/doi/10.1145/3070617.3070634

ink! Developers Security Guideline - Aleph Zero. (2023). https://docs.alephzero.org/aleph-zero/build/security-course-by-kudelski-security/ink-developers-security-guideline

Jane Aitkens. (2016). Turning Aleph’s Photocopy Requests into a Scan Delivery Service. https://www.semanticscholar.org/paper/1e3b1bcc2ce8a19c2e3a6ced43208d56390b1ee3

K. Panetta, E. Manolakos, E. Czeck, & Jamie A. Heller. (1997). Multiple Experiment Environments for Testing. In Journal of Electronic Testing. https://link.springer.com/article/10.1023/A:1008218506450

K. Weaving. (1981). Verification of high-level protocol implementations. In Comput. Commun. https://linkinghub.elsevier.com/retrieve/pii/0140366481901225

L Duan, H Huang, C Li, & W Ni. (2025). A Novel Cross-Chain Hierarchical Federated Learning Framework for Enhancing Service Security and Communication Efficiency. https://ieeexplore.ieee.org/abstract/document/10970074/

Lili Cheng, Zhiying Lv, Osama Alfarraj, Amr Tolba, X. Yu, & Yongjun Ren. (2024). Secure cross-chain interaction solution in multi-blockchain environment. In Heliyon. https://linkinghub.elsevier.com/retrieve/pii/S2405844024048928

Linda Allbee & B. Friesen. (2009). ALEPH Version 20 Collaborative Testing. https://www.semanticscholar.org/paper/c84733fa28deef276fa042ce0ebd4eb8e1d1a8da

M. Kofler. (2001). The Test Environment. https://www.semanticscholar.org/paper/fd65ef53b7eee8c7bbd4abdf43073fbfeb1e4319

Massimo Nardone & Vladimir Silva. (2015). Deployment and Compilation Tips. https://www.semanticscholar.org/paper/b21e5928fa2fac349fe28d117dd8ab615e880124

Pascal Horton. (2018). Requirements. In 5G Second Phase Explained. https://www.semanticscholar.org/paper/1d4c9f8c90698101aa9136db796c677ac7238b78

Polkadot SDK. (n.d.). https://polkadot.com/platform/sdk/

R. Heaney & C. Weaver. (2006). Requirements for What Endpoint. https://link.springer.com/chapter/10.1007/978-1-59259-961-5_7

R Huang, M Motwani, I Martinez, & A Orso. (2024). Generating rest api specifications through static analysis. https://dl.acm.org/doi/abs/10.1145/3597503.3639137

Road to Mainnet: Aleph Zero - Entangle. (2024). https://blog.entangle.fi/road-to-mainnet-aleph-zero/

Running an Aleph Node on Testnet. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet

Running the node - Aleph Zero. (2024). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-mainnet/running-the-node

S. Amendolia, F. Fidecaro, S. Galeotti, M. Lippi, A. Lusiani, P. Marrocchesi, D. Passuello, C. Raffo, & B. Lofstedt. (1987). The MC68020-Based FASTBUS Read-Out Processor of the Aleph Time Projection Chamber. In IEEE Transactions on Nuclear Science. https://ieeexplore.ieee.org/document/4337315/

S Reno, SH Priya, GMA Al-Kafi, & S Tasfia. (2024). A novel approach to optimizing transaction processing rate and space requirement of blockchain via off-chain architecture. https://link.springer.com/article/10.1007/s41870-023-01685-x

The challenges of ZK Privacy and how Aleph Zero solves them. (2024). https://alephzero.org/blog/challenges-zk-privacy-and-how-aleph-zero-solves-them/

The New Aleph Zero Roadmap. (2025). https://alephzero.org/blog/the-new-aleph-zero-roadmap/

The Ultimate 2025 Guide to Blockchain in Software Testing - ACCELQ. (2025). https://www.accelq.com/blog/blockchain-testing/

TPS testing CLI tool | CLI / Performance Metrics / Testing — Hummbell. (n.d.). https://www.hummbell.com/projects/primelab-tps-tool

Ubuntu Documentation. (2009). Ubuntu 10.10 Server Guide. https://www.semanticscholar.org/paper/4eb6381d3b05c33a0622773998d47814ad7ca4f2

Understanding TPS: A Key Measure of Blockchain Speed - Aleph Zero. (n.d.). https://alephzero.org/blog/understanding-tps-key-measure-of-blockchain-speed/

Validate - Aleph Zero. (n.d.). https://docs.alephzero.org/aleph-zero/use/validate

Verifying your setup | Aleph Zero. (2025). https://docs.alephzero.org/aleph-zero/use/validate/running-an-aleph-node-on-testnet/verifying-your-setup

W Ou, S Huang, J Zheng, Q Zhang, G Zeng, & W Han. (2022). An overview on cross-chain: Mechanism, platforms, challenges and advances. In Computer Networks. https://www.sciencedirect.com/science/article/pii/S1389128622004121

What is Aleph Zero, the Complete Blockchain Guide - DappRadar. (2024). https://dappradar.com/blog/what-is-aleph-zero-the-complete-blockchain-guide

Which blockchain is the fastest? - Pontem Network. (2022). https://pontem.network/posts/which-blockchain-is-the-fastest

WJ Headrick & A Bilskie. (2023). TPS Execution in an Virtual Environment. In 2023 IEEE AUTOTESTCON. https://ieeexplore.ieee.org/abstract/document/10296120/

Y Cao, J Cao, D Bai, L Wen, Y Liu, & R Li. (2025). Map the blockchain world: A trustless and scalable blockchain interoperability protocol for cross-chain applications. https://dl.acm.org/doi/abs/10.1145/3696410.3714867

Y Xu, R He, S Dai, & Y Zhang. (2023). ChainKeeper: A cross‐chain scheme for governing the chain by chain. In IET Blockchain. https://ietresearch.onlinelibrary.wiley.com/doi/abs/10.1049/blc2.12047

Z Yin, B Zhang, J Xu, K Lu, & K Ren. (2022). Bool network: An open, distributed, secure cross-chain notary platform. https://ieeexplore.ieee.org/abstract/document/9903072/



Generated by Liner
https://getliner.com/search/s/5926611/t/86460957