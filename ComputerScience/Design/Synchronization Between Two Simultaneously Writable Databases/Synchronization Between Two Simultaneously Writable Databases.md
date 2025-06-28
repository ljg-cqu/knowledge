Synchronization Between Two Simultaneously Writable Databases

Sat Jun 28 2025

### Overview of Synchronization Between Simultaneously Writable Databases

Synchronization between two simultaneously writable databases, often termed multi-primary or active-active replication, is a critical component of modern distributed systems, enhancing scalability, fault tolerance, and high availability across various applications and services. This process involves keeping multiple copies of a database consistent with one another, allowing changes to be made on both sides and synchronized bidirectionally. It is distinct from data replication, which primarily focuses on creating multiple copies for fault tolerance, as synchronization specifically aims to maintain consistency and accuracy between a primary data repository, or "single source of truth," and other data sources. This ensures that modifications in one database are efficiently propagated and applied to the other, minimizing discrepancies and facilitating real-time or near real-time updates across the synchronized systems. Such synchronization is crucial for ensuring seamless user experiences, system reliability, scalability, fault tolerance, and compliance with data integrity requirements.

### Challenges in Synchronization with Concurrent Writes

Synchronizing data between two databases that can be written to simultaneously presents significant complexities. A primary issue is the occurrence of **update conflicts**, which arise when concurrent changes are made on both databases, necessitating robust detection and resolution mechanisms to maintain data integrity and prevent data loss. Ensuring data consistency across replicas is further complicated by factors such as network latency, failures, or partitions, which can delay synchronization and introduce inconsistencies during write operations. The **CAP theorem** highlights a fundamental trade-off among Consistency, Availability, and Partition tolerance, implying that a distributed system can only guarantee two of these three properties. For instance, to maintain strong consistency during network partitions, systems may need to block write operations, thereby sacrificing availability.

Achieving strong consistency often requires complex synchronization protocols, which can negatively impact performance, particularly in geographically distributed systems. Additionally, the overhead associated with replication and increased latency due to synchronizing data changes across sites can degrade write performance. The system must efficiently manage concurrency control and conflict reconciliation without incurring excessive resource contention, deadlocks, or slowdowns. Scalability also poses a challenge, as the complexity and network usage escalate with an increasing number of nodes and transactions. Furthermore, if the databases are not initially synchronized or if the application was not designed for two-way synchronization, attempting to synchronize them can be a mistake. Determining which change should take priority in a conflict can be a "downright logic error" if the system accepts inputs from both sides, often requiring human intervention to understand the overall situation and ensure correct conflict resolution. Without proper design, automatic conflict resolution processes can lead to silent data loss as conflicting data from a non-preferred side is overwritten. This also complicates maintaining reliable audit trails and record versions, which can become "unreliable junk" due to poorly designed synchronization processes. Moreover, disaster recovery becomes challenging, as restoring one side from a backup can disrupt synchronization and consistency across the system.

### Key Algorithms and Protocols for Concurrent Writes

Various algorithms and protocols have been developed to address the complexities of synchronizing data between concurrently writable databases. **Timestamp-based algorithms** are a class of concurrency control algorithms designed to achieve read-write and write-write synchronization in distributed database systems by ordering operations and resolving conflicts. These algorithms facilitate concurrent execution by having sites exchange writesets and timestamps before operations, which helps to avoid update restarts. A proposed transactional asynchronous replication scheme for mobile database systems also discusses conflict detection and resolution strategies based on timestamps.

**Concurrency control algorithms** broadly fall into three main classes: locking algorithms, timestamp algorithms, and optimistic (or certification) algorithms, all aiming to manage concurrent access and prevent incorrect results from read and write operations. For instance, snapshot isolation, a concurrency control algorithm, can be modified to automatically detect and prevent anomalies at runtime, providing serializable isolation while preserving properties like non-blocking readers and writers.

**Consensus algorithms** such as Paxos and Raft are crucial for ensuring agreement among nodes in distributed systems and maintaining strong consistency. These algorithms ensure that all databases agree on a specific log line before a value is inserted, thereby maintaining consistency even if some nodes fail. This mechanism ensures strong consistency as all nodes must agree on a value before a write operation proceeds.

**Write-Ahead Logging (WAL)** is a technique where changes are recorded in a log before being applied to the database, ensuring durability and atomicity, and helping to maintain data consistency between primary and replica databases. This log can also serve as a source of data on modifications for multi-primary replication tools. Changes made to a database are recorded in a log and then propagated to other databases, allowing for fast and efficient replication.

**Optimistic Concurrency Control** allows multiple operations to proceed and detects conflicts at commit time, retrying the operation if a conflict is found. This approach is effective when conflicts are rare, reducing the overhead associated with locking. Another strategy is designing operations to be **idempotent**, meaning the same action can be performed multiple times without changing the result, which helps avoid unintended outcomes if operations are retried due to network issues.

### Consistency Models for Distributed Databases

In distributed systems with concurrently writable databases, **consistency models** define how data updates are managed and synchronized across multiple nodes. The selection of a consistency model directly influences the trade-offs between consistency, availability, and partition tolerance.

**Strong Consistency**, also known as linearizability, ensures that all nodes reflect the same data immediately after a write operation, providing a single, instantaneous view of the data across the system. This model simplifies semantics for application programmers, as it emulates a scenario where data is stored in a single node that processes requests one at a time. However, achieving strong consistency often requires strict synchronization protocols like Two-Phase Commit and cannot be maintained with availability during network partitions, as implied by the CAP theorem.

**Eventual Consistency** is the weakest consistency model, guaranteeing that if no new updates are made to an object, eventually all accesses will return the last updated value. This model prioritizes availability over immediate consistency and is commonly used in distributed NoSQL databases. While it offers maximum concurrency and availability, it can lead to temporary discrepancies and undesired situations, such as a personal photo becoming visible before its album's permission status is updated in a remote node. Dynamo, used by Amazon.com for services with high availability requirements, is an example of an eventually consistent data store.

**Causal Consistency** is an intermediate model, stronger than eventual consistency but weaker than strong consistency. It maintains the order of causally related operations, ensuring that the effects of an event are visible only after the effects of its dependencies are visible. For example, a photo upload operation depends on a preceding album status change, so the photo cannot be viewed before the new album status is visible. This model is achievable with availability and partition tolerance. COPS and GentleRain are two causally consistent distributed data stores, with COPS using explicit dependency checks and GentleRain using implicit dependency checks via physical timestamps. GentleRain generally offers better throughput than COPS, especially for read-heavy workloads, while COPS typically has lower update visibility latency (UVL), which is the time interval between an update's visibility in its original datacenter and a remote datacenter.

Client-centric consistency models like **Read-Your-Writes consistency** ensure that a user always sees their own updates, even if other nodes are temporarily inconsistent, which is crucial for a consistent user experience in distributed systems. The choice among these models involves balancing the requirements for consistency, availability, and partition tolerance, with hybrid models often adopted to balance performance and reliability.

### Conflict Detection and Resolution Strategies

Effective conflict detection and resolution are paramount for preserving data consistency and integrity in databases that allow multiple concurrent writes. Conflict detection involves identifying divergent updates that arise when different changes are made to the same data item simultaneously in different locations. Common methods for this include using **timestamps and version numbers** to determine the correct order of operations, a technique common in databases using Multi-Version Concurrency Control (MVCC). For instance, a timestamp-based algorithm can detect both write-write and read-write conflicts when sites from different partitions merge. Another approach is **Change Data Capture (CDC)**, which captures and tracks individual changes (inserts, updates, deletes) made to the source of truth, allowing for near real-time data synchronization. Log-based CDC, which leverages transaction logs like PostgreSQL's Write-Ahead Log (WAL), is considered the most efficient method as it captures changes from a log file with minimal impact on the source system.

Once conflicts are detected, various resolution strategies can be employed. **Last Writer Wins (LWW)** is a simple strategy that resolves conflicts by prioritizing updates based on their timestamps, accepting the most recent change. However, this method carries the risk of losing valid data if the chronologically latest write is not the desired one. **Rule-based or policy-driven resolution** allows systems to define priority rules, such as server preference or frequency of updates, to automatically resolve conflicts based on high-level criteria like value, provenance, or timestamps.

For more complex scenarios, **Conflict-Free Replicated Data Types (CRDTs)** are special data structures that allow concurrent updates to be merged automatically without conflicts. CRDTs ensure eventual consistency without coordination overhead, making them suitable for distributed systems where immediate consistency is not strictly required. In cases where automated methods cannot safely determine the correct data state, **manual intervention** by human users is required to review and resolve conflicts. Additionally, some systems allow for **rollback and retry**, where conflicting transactions are reverted and then re-attempted after necessary corrections are applied. A generic framework for conflict resolution can support semantics-based conflict resolution policies and application-specific compensation procedures.

### Architectures and Real-world Implementations

Real-world architectures supporting synchronization between two simultaneously writable databases often involve **multi-primary replication** (also known as multi-master replication), where all databases can act as both sources and replicas, and changes made to one database are propagated to all others. This type of replication is beneficial for write-heavy workloads.

Open-source tools like **Bucardo** and commercial ones like **EDB Replication Server** are prominent examples for PostgreSQL, enabling multi-primary replication. Bucardo is an open-source tool for logical replication, supporting both primary-replica and multi-primary modes, and uses triggers and tracing tables to mark modifications. It features a three-tier architecture with a Master Control Process (MCP), Control Processes (CTL), and KID processes for replication work, including conflict checking and resolution on primary keys. Bucardo also allows custom code for handling conflicts and exceptions automatically, offering elasticity in invoking compensation actions. EDB xDB Replication Server supports multi-primary replication for PostgreSQL and EDB PostgreSQL Advanced Servers. It utilizes processes spawned by each database instance to write data to Kafka streams for propagation and manages configuration via ZooKeeper. EDB xDB can detect changes using both triggers and write-ahead log (WAL) plugins, making it potentially lighter and faster as it doesn't require additional disk writes for trigger-based tools. While Bucardo was found to be lighter and faster in reconciling databases, xDB performed better in continuous synchronization in some experimental evaluations.

Other notable data syncing tools that automate the process include **SymmetricDS**, an open-source software supporting multiple relational databases like MySQL, PostgreSQL, and Oracle, as well as commercial tools like **Talend, Informatica, and Boomi**. For cloud-based infrastructures, services such as **AWS Database Migration Service (DMS)** and **Azure Database Migration Service** can be used to synchronize databases, leveraging the scalability and reliability of cloud platforms. Oracle GoldenGate is another real-time data integration and replication software for heterogeneous environments including Oracle, SQL Server, and DB2.

Real-world deployments, such as the **ALICE experiment at CERN**, illustrate the practical application of these solutions. To ensure high availability for their experiment conditions and calibration database (CCDB), two writable instances of PostgreSQL were deployed and synchronized in quasi-real-time using Bucardo. This system was designed to prevent data loss in insert-insert conflicts (where rows with the same key are simultaneously inserted into different instances) and handle high data rates. Such implementations demonstrate that existing multi-primary replication tools can be effectively applied to highly available, soft real-time systems, handling loads significantly higher than required in some use cases.

Bibliography
A. Yadav & A. Agarwal. (2010). A Distributed Architecture for Transactions Synchronization in Distributed Database Systems. https://www.semanticscholar.org/paper/fffadd6789cac2e1d89fa5ad15320d168c44a7a2

Annette Bieniusa & Alexey Gotsman. (2017). Proceedings of the 3rd International Workshop on Principles and Practice of Consistency for Distributed Data. In European Conference on Computer Systems. https://www.semanticscholar.org/paper/21a7bb4db279a551f98a7a594153963f3dcd198e

Best way to synchronize data between two different databases. (2015). https://softwareengineering.stackexchange.com/questions/288370/best-way-to-synchronize-data-between-two-different-databases

Causal consistency - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/Causal_consistency

Conflict Detection in Distributed Workflows | Prompts.ai. (2025). https://www.prompts.ai/en/blog-details/conflict-detection-in-distributed-workflows

Conflict Management - CouchDB: The Definitive Guide. (n.d.). https://guide.couchdb.org/draft/conflicts.html

Conflicts and Concurrency in Distributed Systems - GeeksforGeeks. (2024). https://www.geeksforgeeks.org/computer-networks/conflicts-and-concurrency-in-distributed-systems/

D Filipović, D Sokač, & R Picek. (2020). Bidirectional database synchronization to the cloud computing platform. https://dl.acm.org/doi/abs/10.1145/3388176.3388204

H·G·索海姆 & B·奥尔斯塔德. (2014). Techniques for managing writable search results. https://www.semanticscholar.org/paper/cc261d8029a3ea02844e0a10504cd9999698d3a8

how to keep 2 database in synch - Ask TOM. (n.d.). https://asktom.oracle.com/ords/f?p=100:11:0::::P11_QUESTION_ID:1514534424469

IT Tomter. (2021). Towards a General Database Management System of Conflict-Free Replicated Relations. https://munin.uit.no/handle/10037/22344

J. Pearl. (2010). On the Consistency Rule in Causal Inference: Axiom, Definition, Assumption, or Theorem? In Epidemiology. https://www.semanticscholar.org/paper/78339db142b5443428d965c0dcf70fadd239f1e6

Jaafar Ahmed, A. Karpenko, O. Tarasyuk, A. Gorbenko, & Akbar Sheikh-Akbari. (2023). Consistency issue and related trade-offs in distributed replicated systems and databases: a review. In Radioelectronic and Computer Systems. https://www.semanticscholar.org/paper/1db04857e49b12fb0bc0d0d3c02e52d191b89ae4

Jörgen Birkler & L. Novak. (2001). Synchronizing databases are not time dependent. https://www.semanticscholar.org/paper/a375332cb75b8aa59a23ed589fbb13256644a31e

K. Lam, Jiannong Cao, Chung-Leung Pang, & S. Son. (1997). Resolving conflicts with committing transactions in distributed real-time databases. In Proceedings. Third IEEE International Conference on Engineering of Complex Computer Systems (Cat. No.97TB100168). https://ieeexplore.ieee.org/document/622296/

K. Sattler, Stefan Conrad, & G. Saake. (2000). Adding Conflict Resolution Features to a Query Language for Database Federations. In Australas. J. Inf. Syst. https://www.semanticscholar.org/paper/8ab0493ca4f238f1bab9752b282738a549a34bc6

KH Lee, MH Kim, KC Lee, & BS Kim. (2002). Conflict classification and resolution in heterogeneous information integration based on XML schema. https://ieeexplore.ieee.org/abstract/document/1181222/

KY Lam, CL Pang, SH Son, & J Cao. (1999). Resolving executing–committing conflicts in distributed real-time database systems. In the computer Journal. https://ieeexplore.ieee.org/abstract/document/8129742/

L Palopoli, D Sacca, & D Ursino. (1998). An automatic technique for detecting type conflicts in database schemes. https://dl.acm.org/doi/pdf/10.1145/288627.288671

Lucia C. Sekino. (1975). Multiple concurrent updates. In Very Large Data Bases Conference. https://dl.acm.org/citation.cfm?doid=1282480.1282525

Michael J. Cahill, Uwe Röhm, & A. Fekete. (2008). Serializable isolation for snapshot databases. In SIGMOD Conference. https://dl.acm.org/doi/10.1145/1376616.1376690

Mohammad Roohitavaf. (2016). Consistency in Distributed Data Stores. In ArXiv. https://www.semanticscholar.org/paper/25aee8cc056999a5cd21bdfd52315e3b8cec5128

N Preguiça. (2018). Conflict-free replicated data types: An overview. In arXiv. https://arxiv.org/abs/1806.10254

O Oloruntoba. (2025). Architecting Resilient Multi-Cloud Database Systems: Distributed Ledger Technology, Fault Tolerance, and Cross-Platform Synchronization. https://www.researchgate.net/profile/Oluwafemi-Oloruntoba/publication/389392985_Architecting_Resilient_Multi-Cloud_Database_Systems_Distributed_Ledger_Technology_Fault_Tolerance_and_Cross-Platform_Synchronization/links/67c09480461fb56424ec10a4/Architecting-Resilient-Multi-Cloud-Database-Systems-Distributed-Ledger-Technology-Fault-Tolerance-and-Cross-Platform-Synchronization.pdf

P Bailis & A Ghodsi. (2013). Eventual consistency today: Limitations, extensions, and beyond: How can applications be built on eventually consistent infrastructure given no guarantee of safety? In Queue. https://dl.acm.org/doi/abs/10.1145/2460276.2462076

PA Bernstein & N Goodman. (1980). Timestamp-Based Algorithms for Concurrency Control in Distributed Database Systems. In VLDB. https://www.microsoft.com/en-us/research/uploads/prod/2020/12/TO-Algs-Bernstein-GoodmanVLDB1980.pdf

Rafał Mucha, B. Baliś, Costin Grigoraş, & J. Kitowski. (2023). Database Replication for Disconnected Operations with Quasi Real-Time Synchronization. In Comput. Sci. https://www.semanticscholar.org/paper/984726e55acc1b70a1aadbffc491e2254c6aa676

S. Dragos, M. Vaida, L. Suta, Marius-Cristian Ureche, & A. Voina. (2012). SYNCY: A software engine for data stream event synchronization. In 2012 16th International Conference on System Theory, Control and Computing (ICSTCC). https://www.semanticscholar.org/paper/52a588664f2a8855420f54b4337b99f44ddbc995

S. Madria. (1998). Handling of Mutual Conflicts in Distributed Databases Using Timestamps. In Comput. J. https://www.semanticscholar.org/paper/ba00c479a9c47995ab6f6195a42ac5a534ad9420

SA Ajila & A Al-Asaad. (2011). Mobile databases-Synchronization & conflict resolution strategies using SQL server. https://ieeexplore.ieee.org/abstract/document/6009598/

Sanny Syberfeldt. (2007). Optimistic Replication with Forward Conflict Resolution in Distributed Real-Time Databases. https://www.semanticscholar.org/paper/5709e24ec2db6ea19370e73961568883979801c8

SH Phatak & BR Badrinath. (1999). Conflict resolution and reconciliation in disconnected databases. https://ieeexplore.ieee.org/abstract/document/795148/

Sync Databases and Remove Data Silos with CDC & Apache Kafka. (n.d.). https://www.confluent.io/en-gb/blog/sync-databases-and-remove-silos-with-kafka-cdc/

Synchronizing Multiple Data Sources in a Distributed System - Medium. (2023). https://medium.com/@ketansomvanshi007/synchronizing-multiple-data-sources-in-a-distributed-system-ensuring-consistency-and-accuracy-8e087b3b5ed6

Synchronizing two databases on different servers. (2024). https://dba.stackexchange.com/questions/337604/synchronizing-two-databases-on-different-servers

Syncing Databases: How to Do It and Best Practices - Release. (2023). https://release.com/blog/syncing-databases-how-to-do-it-and-best-practices

The Art of Staying in Sync: How Distributed Systems Avoid Race ... (2024). https://medium.com/@alexglushenkov/the-art-of-staying-in-sync-how-distributed-systems-avoid-race-conditions-f59b58817e02

Wai Gen Yee & O. Frieder. (2005). Scalable synchronization of intermittently connected database clients. In International Conference on Mobile Data Management. https://www.semanticscholar.org/paper/a6fa2de90c5750a5059414dc6e1924edd1491d8d

What are some methods for conflict resolution in distributed ... - Milvus. (2025). https://milvus.io/ai-quick-reference/what-are-some-methods-for-conflict-resolution-in-distributed-databases

Yannis Katsis, Alin Deutsch, Y. Papakonstantinou, & V. Vassalos. (2012). Conflict Resolution in Online Databases *. https://www.semanticscholar.org/paper/77b0c7f494b7158ba5d2fb71f45dec973ff81550

Yuichiro Kamada. (2010). Strongly Consistent Self‐Confirming Equilibrium. In Econometrica. https://onlinelibrary.wiley.com/resolve/doi?DOI=10.3982/ECTA7496

丁治明 & 孟小峰. (2002). A Transactional Asynchronous Replication Scheme for Mobile Database Systems. https://www.semanticscholar.org/paper/8887c610bb875868c939a3174ba243909057f6ad

孙学磊, 李德逸, 王伟信, 董斌, & 董阳. (2011). Method for synchronizing multiple heterogeneous source databases based on log. https://www.semanticscholar.org/paper/155ef5e4cde058ba76bc3f3506417050699cd5b2



Generated by Liner
https://getliner.com/search/s/5926611/t/86076696