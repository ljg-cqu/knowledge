'Distributed Consistency'. Requirements: 1. Ensure outputs are classified clearly and comply with MECE. 2. Explain clearly and briefly, using simple analogies and examples. 3. Use numbered lists for clarity when suitable. 3. Provide concise explanations and real usage examples.

Sat Jun 28 2025

### Introduction to Distributed Consistency

Distributed consistency is a fundamental concept in distributed systems that ensures data accuracy and up-to-dateness across multiple servers or nodes. It defines how and when data changes become visible across the various nodes within a system. In essence, consistency dictates how a distributed system maintains a coherent and predictable view of its data, irrespective of where or how users access it. The necessity for consistency arises from the replication mechanisms employed in distributed systems, which while resolving challenges like data durability, access, and fault tolerance, introduce the new challenge of maintaining coherence among replicas. For instance, in a system with multiple replicas, a recently sent email might disappear, or a deleted item from a shopping cart might reappear if consistency is not properly managed. Therefore, different systems have varying consistency requirements, necessitating flexibility in how consistency is configured for different operations.

### Classification of Distributed Consistency Models

Consistency models in distributed systems can be broadly categorized into three main groups: Strong Consistency, Eventual Consistency, and Intermediate Consistency (which includes Causal Consistency). This classification is designed to be mutually exclusive and collectively exhaustive, covering the spectrum of guarantees offered by distributed systems. These models represent different trade-offs between concurrency of operations versus their ordering, or between performance and correctness. The choice of a consistency model significantly impacts a system's performance, scalability, and reliability.

### Strong Consistency Models

Strong consistency models ensure that every node or replica in a distributed system has the exact same view of data at any given point in time, regardless of which client updated the data. When a write operation occurs, it conceptually locks the item across replicas and propagates the update immediately, blocking read operations to prevent inconsistent or dirty reads until all replicas are updated. This means any read operation will always return the most recent write. While providing a simple semantics for application programmers, strong consistency models are challenging to achieve alongside availability and partition-tolerance, as highlighted by the CAP theorem.

#### Types of Strong Consistency

1.  **Sequential Consistency**: In sequential consistency, operations by an individual execution unit (like a thread or process) always occur in their program order. However, operations across multiple execution units can be interleaved. The key guarantee is that all units of execution observe the same sequence of updates for a given set of variables, even if the actual read order differs from the write order, as long as the observed update sequence is consistent across all units. For example, if two threads `A` and `B` perform operations, sequential consistency allows various interleavings of their operations as long as `A`'s operations appear in `A`'s program order and `B`'s in `B`'s program order.

2.  **Linearizability**: Linearizability is an extension of sequential consistency that is stricter and often referred to as strong consistency. It ensures that operations across different units of execution maintain a real-time order, appearing instantaneous. This means if a write operation `W(V=3)` happens at time `t2`, any subsequent read at time `t3` (where `t3 > t2`) must see the value `V=3`, regardless of which unit initiated the write. Overlapping write operations can be ordered in any way, but read operations must generally reflect the most recent value in real-time, unless a read overlaps with a write on the same variable, in which case it might return a stale value. A system is linearizable if all its possible histories are linearizable.

3.  **Strict Consistency**: Strict consistency is the most stringent form, building upon linearizability by enforcing strict real-time ordering for *all* write operations, including those that overlap. It requires that all read operations across clients also observe the most recent value of variables in real-time order. For instance, if a write operation by `P1` completes, and `P3` initiates a read that overlaps with `P1`'s write, strict consistency demands `P3` to see `P1`'s write (`x=5`), unlike linearizability which might permit reading an older value (`x=0`) in such overlapping scenarios. This level of consistency is considered practically impossible to implement in real-life distributed systems due to its strong real-time adherence.

#### Characteristics and Real-World Examples of Strong Consistency

Strong consistency models provide the highest data consistency but result in the lowest application availability and throughput, along with high to very high latency. They are data-centric, meaning the system synchronizes data access operations from all units of execution to guarantee correct results.

1.  **Online Banking Applications**: In financial systems, ensuring account balances reflect all recent transactions immediately is critical to prevent issues like overspending or misallocation of funds. When money is deposited, the updated balance should be seen instantly. Google Spanner is an example of a database that provides globally distributed strong consistency for such applications.
2.  **E-commerce Flash Sales/Inventory Management**: For systems handling limited inventory, like flash sales or ticket bookings, strong consistency is vital to prevent overselling or double-booking. When a ticket is confirmed, its availability must update instantaneously across the system.
3.  **Meeting Scheduling Apps**: These applications require strong consistency to prevent conflicts, ensuring that when a time slot is booked, it is immediately unavailable to all other users.

### Eventual Consistency Models

Eventual consistency is the weakest but most popular consistency level, particularly favored by NoSQL data stores like MongoDB, Amazon DynamoDB, and Apache Cassandra. This model tolerates temporary inconsistencies among replicas, guaranteeing that if no new write operations occur on a given data item, all replicas will eventually converge to the same state and serve read requests with the last updated value. It allows the system to temporarily be in an inconsistent state, prioritizing high availability and partition tolerance over immediate consistency.

#### Characteristics and Real-World Examples of Eventual Consistency

Eventual consistency offers the lowest data consistency but the highest application availability and throughput, making it suitable for systems prioritizing performance and continuous operation. It is typically client-centric, meaning the system primarily focuses on data access operations from the concerned process and assumes other units of execution have no significant impact.

1.  **Domain Name System (DNS)**: The DNS is a classic example, successfully handling billions of requests daily while relying on eventual consistency. Updates to domain entries take time to propagate across DNS servers globally.
2.  **Social Media Features**: Features like product reviews, ratings on Amazon, or counts of likes/views on Facebook and YouTube are typically eventually consistent. A user might see an older count for a short period before the system eventually synchronizes.
3.  **Airline Website Ticket Prices**: The ticket price displayed on the front page of an airline website might be eventually consistent, meaning it could temporarily show a slightly outdated price before updating.
4.  **Amazon's Dynamo**: A key-value store, Dynamo uses eventual consistency to manage the state of some Amazon.com services, prioritizing very high availability. It allows application designers to configure consistency levels by adjusting parameters like N (number of replicas), R (read quorum), and W (write quorum), enabling trade-offs between availability and consistency. Setting W to 1 ensures that a PUT operation is rarely rejected, but increases the risk of inconsistency.

### Intermediate Consistency Models

Intermediate consistency models strike a balance between the strictness of strong consistency and the relaxed nature of eventual consistency, offering varying degrees of ordering and freshness guarantees. They are often explored to improve efficiency and programmability without sacrificing scalability.

#### Types of Intermediate Consistency

1.  **Consistent Prefix Read**: This guarantee ensures that a replica will not read data out of order, even if the data itself is stale. If data `x` has updates `A`, `B`, and `C` in sequence, every replica receives these updates in the same order. While different nodes may return different versions of the same data at the same time, they maintain the order of updates. This model has a low data consistency, high application availability, and moderate throughput, and is data-centric.
    *   **Bounded Staleness Consistency**: This is an extension of consistent prefix reads that allows users to configure a maximum staleness threshold for data. The threshold can be defined by time (e.g., maximum 5 seconds stale) or by the number of versions/updates a read can lag behind writes. It maintains a global ordering guarantee with this configurable threshold. It is more expensive than weaker models and has high data consistency but low app availability and throughput. Real-world examples include stock ticker applications, weather tracking apps, and online gaming apps.

2.  **Session Guarantees**: Session guarantees correlate multiple read and write operations within a specific group, known as a session. These guarantees ensure that a unit of execution (e.g., a client) does not encounter anomalies in its own read and write operations during an active session. However, these guarantees may not apply across different sessions, classifying them as weak consistency overall.
    *   **Read-Your-Own-Write (RYOW)**: Guarantees that if a client writes a value, subsequent reads by the *same client* will see that update, even if other replicas haven't yet received it. This can be achieved by making a single replica handle all requests from the same unit of execution, or by synchronously replicating writes to all followers. An example is deleting a mail from Gmail and expecting it not to reappear upon refreshing the page.
    *   **Monotonic Read**: Ensures that if a client reads a value, any subsequent read by the same client in the same session will return either the same value or a more recent one, never an older value. This is also "sticky" in nature, typically routing requests from a session to the same server or set of servers. An example is ensuring that when you open Gmail and click on an email, the content is not empty because the server you landed on is unaware of the latest update.
    *   **Write Follows Read (WFR)**: Guarantees that if a write operation follows a read operation by the same unit of execution, the write operation will follow all the writes that influenced the preceding read. It also includes a propagation guarantee that all other replicas will eventually see the writes in the same order. This is also known as session causality. A real-life example is replying to a tweet, where the reply can only be made visible after the original tweet is written to the system and seen by the user.
    *   **Monotonic Write (MW)**: Ensures that a write operation by a process on a data item completes before any successive write operation on that same data item by the same process. This means an execution unit will see its own successive updates in order, and eventually, all other replicas will also see these writes in the same order. An example is editing a Wikipedia article, where version `n+1` must always replace version `n` for updates by the same client.

3.  **Causal Consistency**: Causal consistency enforces ordering only for causally related writes across different units of execution. If an operation depends on a previous one (e.g., reading `x` then writing `y` based on `x`), causal consistency guarantees that all units of execution will observe `y` only after observing the related `x`. Unrelated writes, however, can be ordered arbitrarily. This model is weaker than strong consistency but stronger than eventual consistency. Causal consistency is achievable with availability and partition-tolerance. COPS and GentleRain are two distributed data stores that implement causal consistency.

#### Characteristics and Real-World Examples of Causal Consistency

Causal consistency provides moderate data consistency, high application availability, and moderate latency and throughput. It is a data-centric perspective.

1.  **Social Media Status Updates**: If a user posts an important status on Facebook and then updates it, their online friends should receive the update as soon as possible, reflecting the causal dependency between the original post and its update.
2.  **Collaborative Document Editing**: In a collaborative editor, if one user makes an edit and another user's edit depends on the first, causal consistency ensures the dependent edit appears after the original. For example, Apache Cassandra offers an option for causal consistency.
3.  **Forum or Comment Threads**: Replies to a particular comment should appear in the order they were posted, reflecting their causal relationship. Unrelated comments, however, can appear in any order.

### Conclusion on Consistency Models

The choice of a consistency model is a critical design decision in distributed systems, as it involves balancing correctness, availability, and performance according to specific application needs. There is no single "best" solution, and real-world systems often offer different APIs or configurations to accommodate varying consistency requirements. Factors such as ease of development, tolerance for weak consistency, and the cost implications for storage, network, and system performance must be considered. Understanding the nuanced differences between models like linearizability and bounded staleness is essential for architects to make informed trade-offs and avoid costly design errors.

Bibliography
Annette Bieniusa & Alexey Gotsman. (2017). Proceedings of the 3rd International Workshop on Principles and Practice of Consistency for Distributed Data. In European Conference on Computer Systems. https://www.semanticscholar.org/paper/21a7bb4db279a551f98a7a594153963f3dcd198e

B. Kemme, G. Ramalingam, A. Schiper, M. Shapiro, K. Vaswani, Kapil Vaswani. Consistency, ©. B. Kemme, Marcos K. Aguilera, Carla Ferreira, Rodrigo Rodrigues License, Rodrigo Rodrigues, Alan Fekete License, Vivien Quéma, Amr el, Abbadi License, Carlos Baquero, Doug Terry, Sebastian Burckhardt License, Sebastian Burckhardt, … Luís Rodrigues License. (2010). Consistency in Distributed Systems. https://link.springer.com/chapter/10.1007/0-387-27601-7_19

Consistency Guarantees in Distributed Systems Explained Simply. (2021). https://kousiknath.medium.com/consistency-guarantees-in-distributed-systems-explained-simply-720caa034116

Consistency Patterns — Eventual Consistency, Strong Consistency. (2025). https://codefarm0.medium.com/consistency-patterns-eventual-consistency-strong-consistency-a1826e3a30a6

Consistency Patterns in Distributed Systems: A Complete Guide. (2024). https://www.designgurus.io/blog/consistency-patterns-distributed-systems

Distributed Data Consistency: Challenges & Solutions | Endgrate. (2024). https://endgrate.com/blog/distributed-data-consistency-challenges-and-solutions

Gerson Sunyé. (2017). Model Consistency for Distributed Collaborative Modeling. In European Conference on Modelling Foundations and Applications. https://link.springer.com/chapter/10.1007/978-3-319-61482-3_12

HNS Aldin, H Deldari, & MH Moattar. (2019). Consistency models in distributed systems: A survey on definitions, disciplines, challenges and applications. https://arxiv.org/abs/1902.03305

K Pezdek, T Whetstone, & K Reynolds. (1989). Memory for real-world scenes: The role of consistency with schema expectation. https://psycnet.apa.org/fulltext/1989-31890-001.html

Maciej Kokociński, Tadeusz Kobus, & Paweł T. Wojciechowski. (2021). On Mixing Eventual and Strong Consistency: Acute Cloud Types. In IEEE Transactions on Parallel and Distributed Systems. https://ieeexplore.ieee.org/document/9459528/

Mohammad Roohitavaf. (2016). Consistency in Distributed Data Stores. In ArXiv. https://www.semanticscholar.org/paper/25aee8cc056999a5cd21bdfd52315e3b8cec5128

Strong Consistency vs Eventual Consistency - System Design School. (n.d.). https://systemdesignschool.io/blog/eventual-consistency-vs-strong-consistency

Strong vs. Eventual Consistency: Understanding the Trade-offs in ... (2023). https://konstantinmb.medium.com/strong-vs-eventual-consistency-understanding-the-trade-offs-in-distributed-systems-8c0d7beb38ca

Understanding Consistency Models in Distributed Systems - LinkedIn. (n.d.). https://www.linkedin.com/pulse/understanding-consistency-models-distributed-systems-rajasekaran-1kb6c

Understanding Data Consistency: Types, Examples, and Use Cases. (2024). https://www.linkedin.com/pulse/understanding-data-consistency-types-examples-use-ali-oiqof

Understanding Database Consistency in Distributed Systems - TiDB. (2025). https://www.pingcap.com/article/understanding-database-consistency-in-distributed-systems/

What are the different types of consistency models in distributed ... (n.d.). https://milvus.io/ai-quick-reference/what-are-the-different-types-of-consistency-models-in-distributed-databases



Generated by Liner
https://getliner.com/search/s/5926611/t/86076915