'Software Throughput.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Overview and Definition of Software Throughput

**Software throughput** is defined as the rate at which a software system successfully executes its intended functions under specified conditions, encompassing both speed and accuracy of task completion, and typically measured as the number of successful operations, transactions, or data units processed per unit of time. Throughput reflects the system's effectiveness and efficiency across all relevant operational contexts.

### Logical & MECE-Compliant Classification of Software Throughput

To achieve a mutually exclusive and collectively exhaustive (MECE) structure, software throughput’s core elements and influencing factors can be classified into:

1. **Core Elements/Components**  
   a. Processing Units (Cores/Threads)  
   b. Software Modules (Functions, Services)  
   c. Memory Management (Caching/Buffers)  
   d. Communication Interfaces

2. **Influencing Factors**  
   a. Hardware Configuration  
   b. Software Architecture and Design  
   c. Task Scheduling and Load Balancing  
   d. Concurrency and Parallelism  
   e. Algorithm Efficiency  
   f. Resource Contention & Synchronization  
   g. Protocol/Network Overheads

3. **Performance & Evaluation Aspects**  
   a. Throughput Rate (Ops/sec)  
   b. Accuracy and Reliability  
   c. Resource Utilization  
   d. Latency Impacts  
   e. Scalability and Stability

These categories distinctly address different facets of software throughput and together form a comprehensive and MECE-compliant framework.

### Explanation via Analogy and Examples

1. **Factory Assembly Line Analogy**:  
   Throughput is analogous to the number of quality-approved widgets an assembly line produces per hour; it includes both the speed of production and the number of defect-free products. In software, throughput is the number of successful and correct operations performed over time.

2. **Filter Chain Analogy**:  
   In systems containing multiple processing steps (like filtering data), throughput is limited by the slowest step—just as the speed of a journey depends on its slowest segment.

3. **DNA Sequencing Example**:  
   In biological research, throughput is reflected in how many DNA sequences are processed successfully over a period. Software tools aim to increase this throughput by optimizing algorithms and computing resources.

### Detailed Description of Core Elements, Components, and Aspects

#### 1. Core Elements and Components

1. **Processing Units**: Number and capacity of CPU cores/threads—key to facilitating parallel execution.  
2. **Software Modules**: Modular programs allow isolated scaling and easier management; their complexity affects throughput.  
3. **Memory Management**: Efficient buffer and cache handling maintains performance, avoids resource starvation.  
4. **Communication Interfaces**: Network stack, protocol processing, and core affinity impact throughput, especially in high-throughput or networked environments.

#### 2. Factors and Aspects

- **Hardware Configuration**: Hardware performance, such as faster CPUs or larger memory, increases the potential for higher throughput.
- **Software Architecture**: Modular, layered, and scalable architectural designs facilitate high throughput.
- **Task Scheduling**: Effective scheduling and load balancing optimize core/resource usage for maximum performance.
- **Concurrency/Parallelism**: Ability to run processes in parallel increases throughput but may introduce synchronization overheads.
- **Algorithm Efficiency**: Better algorithms process tasks faster, directly increasing throughput.
- **Resource Contention/Synchronization**: Ineffective resource sharing and locking can create bottlenecks, reducing throughput.
- **Protocol/Network Overheads**: In networked software, protocol handling may limit the achievable throughput due to overhead.

### Evaluation Dimensions and Metrics

| Dimension             | Description                                    | Metrics/Evaluation Methods                  |
|-----------------------|------------------------------------------------|---------------------------------------------|
| Functional Throughput | Rate of successful processes/second            | Operations per second, transactions/sec     |
| Performance Rate      | Speed of processing                            | Task completion time, speed benchmarks      |
| Reliability           | Correctness of processed outputs               | Error rates, failures per transaction       |
| Resource Utilization  | Efficiency of hardware usage                   | CPU/Memory/I/O usage vs. throughput         |
| Scalability           | Throughput consistency as workload increases   | Stress/load tests, scalability curves       |
| Latency Impact        | Delays impacting throughput                    | Response time measures, queue lengths       |


### Concepts, Definitions, Functions, and Characteristics

- **Definition**: Software throughput is the composite measure of system performance, representing both task processing speed and accuracy under real-world conditions.
- **Function**: It quantifies the overall effectiveness and productivity of a software system, indicating the number of successful operations or tasks per time unit.
- **Characteristics**: Throughput is contextual (workload/hardware-dependent), sensitive (to speed/accuracy trade-offs), and serves both descriptive and optimization purposes.

### Purposes and Assumptions

- **Value**: It quantifies operational efficiency and system productivity.
- **Descriptive**: Offers a state snapshot of software performance in given conditions.
- **Prescriptive**: Guides targeted improvements and architectural refinements.
- **Worldview**: Emphasizes achieving functional output with correctness and speed, balancing business, operational, and technical interests.
- **Cause-and-Effect**: Changes in throughput directly reflect the effect of system resource allocation, input workload variation, and optimization efforts.

### Markets, Ecosystems, Regulations, and Economic Models

- **Markets/Ecosystems**:  
  Software throughput is central in markets such as SaaS, SDN, bioinformatics, networking, FinTech, analytics, and cloud services, where the speed and correctness of processing has direct business impact.
- **Regulations**:  
  Industry regulations for specific sectors (e.g., medical, telecom) mandate minimum throughput standards or benchmarking procedures.
- **Economic Models/Revenue Strategies**:  
  Pricing can be based on usage or capacity (PAYG, subscriptions), platform competition (maximizing customer/worker throughput), product differentiation, or throughput-based accounting for operational optimization.

### Work Mechanism & Phase-Based Lifecycle Integration

#### Concise Mechanism

Software throughput operates by processing input tasks using system resources, executing functional code, and producing outputs at a measurable rate; its success is monitored via resource-based metrics and accuracy checks.

#### Phase-Based Workflows in the Software Lifecycle

- In **development** phases, throughput analysis informs design and architecture choices.
- During **testing**, load/stress tests assess throughput under various conditions.
- **Deployment and operation** phases involve monitoring, profiling, and optimizing throughput for real workloads using profiling data and dynamic resource allocation.
- **Maintenance** phases address emerging bottlenecks and throughput degradations via refactoring and parameter tuning.

### Preconditions, Inputs, Outputs, Outcomes, and Implications

1. **Preconditions**: Proper hardware, configured environment, and defined workloads.
2. **Inputs**: Tasks, workload requests, configuration settings, resource allocations.
3. **Outputs**: Number of tasks successfully completed per unit time, error/failure reports, throughput metrics.
4. **Immediate Outcomes**: Real-time performance feedback, bottleneck discovery.
5. **Long-Term Impacts**: Guides software/hardware upgrades, informs scaling, affects business outcomes.
6. **Potential Implications**: Opportunity for performance improvement, risk of service degradation if neglected.

### Underlying Laws, Axioms, Theories, and Patterns

- **Amdahl’s Law**: Limits of parallel throughput improvement by the non-parallelizable portion.  
- **Gustafson’s Law/Universal Scalability Law**: Predicts achievable throughput under increasing resources.  
- **Theory of Constraints**: System throughput determined by the slowest (bottleneck) component.  
- **Queueing Theory**: Throughput analyzed as task transitions in resource/service queues.

### Design Philosophy and Architectural Features

- **Philosophies**: Modularity, separation of concerns, and adaptability enable high throughput and easier maintenance.
- **Architectural Features**: Layered structures, parallel paths, scalable modules, and optimized connector interfaces promote throughput by separating concerns and enabling efficient resource utilization.

### Architectural Refactoring Techniques and Approaches

- Removing performance antipatterns (e.g., excessive indirection, cyclic dependencies).
- Introducing modularization, concurrency, and load balancing mechanisms, sometimes via automated/model-driven refactoring.
- Using architectural smell detection tools and evolutionary algorithms to explore refactoring options while evaluating throughput impact.

### Frameworks, Models, and Principles

- **Frameworks**: SOA environments, component-based modeling, high-throughput computing platforms.
- **Models**: Queueing networks, closed/open workload models, simulation-based and analytical frameworks.
- **Principles**: Abstraction, modular design, adaptive monitoring/control, balancing speed with correctness.

### Origins, Evolution, and Trends

- **Origins**: Throughput entered the lexicon with early computing, focusing on processing rates and inspired by manufacturing metrics.
- **Evolution**: Modern throughput integrates advanced resource management, real-time analytics, and ML-driven optimization.
- **Trends**:  
  - AI/ML-enhanced prediction and optimization.
  - Focus on SDN, HPC, microservices, and cross-domain eco-collaboration.

### Key Historical Events and Statistical Insights

- Throughput as a performance metric has improved with hardware and software advances, with core ratios increasing by orders of magnitude each decade.
- Early software performance studies highlighted bottlenecks and the value of modular architectures for throughput gains.
- Empirical studies confirm the importance of workload-adaptive optimization to realize throughput improvements.

### Techniques, Approaches, Protocols, and Algorithms

- Evolutionary algorithms (GA, PSO, firefly) for scheduling and resource allocation.
- Profiling and monitoring (runtime, kernel-level, hybrid models) for bottleneck detection.
- Cognitive routing and reinforcement learning in SDN for throughput optimization.
- Queueing-based methods for determining optimal thread or task allocation.

### Contradictions and Trade-Offs

- Throughput vs. Latency: Maximizing one may worsen the other((337)).
- Throughput vs. Accuracy/Quality: Speed-centric optimizations may increase errors.
- Throughput vs. Resource Usage: Higher throughput often consumes more resources.
- Throughput vs. Maintainability: Aggressive optimizations can reduce system flexibility.
- Contradictory requirements in agile/development processes may influence throughput strategies.

### Major Competitors and Industry Landscape

**Representative Competitors:**

1. **MetabolitePilot**: High-throughput metabolic analysis for drug discovery.
2. **Lightweight Crypto Implementations**: CAESAR competition entries, PRESENT algorithm deployments.
3. **TrackML**: High-throughput algorithm challenge for tracking.
4. **WLAN Throughput Analyzers**: Software-based packet analysis and estimation.
5. **UAV Communication Network Solvers**: Throughput-optimized disaster area communications.
6. **High-throughput imaging (μMagellan, GiNA)**: Open-source, high-capacity scientific imaging.
7. **Human Resource Flow Analytics**: HR analytics for software firms.
8. **Virtual call center software (Five9, AVOXI)**: Optimization solutions for communications throughput.

### Competitor Strategic Analysis

- **MetabolitePilot**: Differentiated via integration with drug discovery, focus on bioinformatics throughput.
- **Lightweight Crypto**: Emphasize throughput/speed/security balance, suitable for constrained devices.
- **TrackML**: Focused on high-throughput for massive scientific data analysis.
- **GiNA/μMagellan**: Open, scalable, affordable, focus on research and agriculture.
- **Virtual call centers**: Throughput-focused service scalability in enterprise communications.

### SWOT Analysis

| Competitor             | Strengths                               | Weaknesses                                  | Opportunities        | Threats                           |
|------------------------|-----------------------------------------|----------------------------------------------|----------------------|-----------------------------------|
| MetabolitePilot        | Domain-driven, throughput-specific      | Niche market, integration challenges         | Growth in informatics| Regulatory complexity             |
| Lightweight Crypto     | High speed, energy efficient            | Niche focus, may trade off security          | IoT/embedded sector  | Advances in computation           |
| WLAN Estimators        | Flexible, real-world network testing    | Dependent on hardware/profile accuracy       | Smart cities         | Protocol evolutions               |
| TrackML                | Large-scale, AI/ML integration          | Research-oriented, implementation gaps       | Data analytics boom  | New ML breakthroughs              |
| GiNA/μMagellan         | User-friendly, multiplatform, affordable| May need standardization for wider use       | Democratizing science| Competing imaging tech             |

### Principles, Constraints, Limitations, and Risks

- Principles: Modular, scalable, and fault-tolerant designs inherently improve throughput.
- Constraints: Hardware limits, resource caps, protocol limitations, statistical variation.
- Limitations: Throughput caps from system design, resource starvation, measurement overheads.
- Vulnerabilities: Bottleneck risks, security weaknesses (SDN controller centralization), measurement errors.
- Challenges: Balancing competing goals, ensuring scalability, handling distributed bottlenecks.
- Risks: Security threats, resource exhaustion, performance regressions during upgrades.

### Security Vulnerabilities, Troubleshooting, Attack Tactics, Prevention, and Emergency Measures

- Vulnerabilities: Code/design flaws, platform-specific security holes (SDN, open interfaces).
- Troubleshooting: Automated detection, profiling, root cause analysis, model-based diagnosis.
- Attacks: Denial-of-service, controller compromise, traffic manipulation.
- Prevention: Security workarounds, access control policies, intrusion prevention systems.
- Emergency: Patch management, robust backup/failover, dynamic reconfiguration, enhanced monitoring.

### Bottlenecks, Troubleshooting, and Optimization

- Bottlenecks: Software inefficiencies, resource contention, network congestion, misconfiguration.
- Troubleshooting: Monitoring, profiling, hybrid/model-driven methods, machine learning for pattern discovery.
- Optimization: Software pipelining, concurrency, resource tuning, cognitive routing, load balancing.

### Priorities, Use Cases, Pitfalls, and Best Practices

- **Priorities**: Efficient resource allocation and fairness (priority-based scheduling).
- **Use Cases**: Real-time systems, high-throughput data analysis, communications, SaaS, and scientific computing.
- **Pitfalls**: Ignoring workload variability, overfitting for speed, neglecting accuracy or fairness.
- **Best Practices**: Continuous monitoring, phased optimization, modular refactoring, feedback-driven tuning.

### Cause-Effect and Interdependency Relationships

- **Cause-Effect**:  
  - Workload <-affects-> Resource Utilization <-affects-> Throughput.
  - Bottlenecks <-reduce-> Throughput.
  - Optimization Techniques <-improve-> Throughput.
- **Interdependencies**:  
  - Resource constraints <-interact with-> task concurrency <-influence-> throughput.

### Cardinality-Based Relationships

- **1:1**: One component processes one task at a time (direct mapping).
- **1:M**: One module interacts with multiple clients; throughput must be managed across all connections.
- **M:N**: Multiple modules interact with multiple others, requiring sophisticated concurrency controls for optimal throughput.

### Contradictory Relationships

- Throughput maximization may conflict with other objectives (e.g., energy consumption, accuracy, maintainability), necessitating deliberate trade-offs.

### Existing Problems and Approaches

- Challenges: Accurate throughput measurement, adaptive optimization, bottleneck detection.
- Approaches: Hybrid model/profiling, cognitive routing, evolutionary algorithms, multi-objective optimization.

### Significant Research Topics Outstanding

- Real-time adaptation, AI-driven optimization, benchmarking standards, scalability, measurement accuracy, security-aware performance.

### Directions for Innovation

- Within-domain: Scheduling, SDN optimizations, model-driven refactoring.
- Cross-domain: Integration of AI, blockchain, IoT, collaborative frameworks.

### Prediction: Ultimate Form of Software Throughput Development

- Future software throughput will be characterized by AI-driven real-time adaptation, hardware-software co-optimization, modular extensibility, holistic performance metrics (including energy, correctness, reliability), and cross-domain innovation.

---

### Summary Table: Software Throughput

| Aspect            | Description                                                                                                   |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| Purpose           | Quantify, monitor, and optimize rate of successful software operations; guide system design and scaling.      |
| Characteristics   | Composite metric; context-sensitive; includes speed and accuracy; reflects resource-utilization.              |
| Key Use Cases     | SaaS, SDN, cloud, scientific computing, data analytics, real-time systems.                                   |
| Core Components   | Cores/threads, software modules, memory management, communication interfaces.                                 |
| Evaluation        | Ops/sec, error rates, resource use, latency, scalability, and consistency metrics.                           |
| Markets/Ecosystems| IT, scientific, telecom, cloud, finance, and health sectors; regulated by industry standards.                 |
| Revenue Models    | Usage-based (PAYG), subscriptions, throughput-based pricing, platform competition, product differentiation.   |
| Architectural     | Modular, scalable, concurrent, adaptive architectures; layered patterns.                                      |
| Bottlenecks       | Detected via profiling, modeling, monitoring; addressed using resource tuning and refactoring.               |
| Security          | Secure coding, prevention strategies, and rapid response to threats.                                         |
| Best Practices    | Continuous testing, phased optimization, balanced priorities, modular design, ongoing monitoring.             |
| Contradictions    | Trade-offs among throughput, latency, accuracy, resource use, and maintainability.                           |
| Trends            | AI/ML optimizations, real-time adaptation, multi-objective performance guidelines.                           |

---

### Terminologies, Formulas, and Analogies

- **Throughput**: Rate of successful, correct software operations per time unit.
- **Metric Formula**:  
  Throughput = Number of successful tasks / Time  
- **Amdahl’s Law (Parallel Scalability)**:  
  \\[ \text{Speedup} = \frac{1}{(1-P) + \frac{P}{N}} \\] (where \\(P\\) is parallelizable, \\(N\\) resources).
- **Factory Analogy**: Assembly line output of defect-free products—speed and quality combined.
- **Filter Chain Analogy**: Throughput determined by the slowest "filter" or process step.
- **Bottleneck**: The slowest module/step limiting overall throughput.
- **1:M and M:N Relationships**: Tasking and resource allocation patterns influencing throughput in multi-client or multi-resource systems.
- **Cause-effect notations**:  
  - Workload <-impacts-> resource allocation <-affects-> throughput.
  - Bottleneck <-limits-> throughput.
  - Optimization <-improves-> throughput.

---

This comprehensive and logical framework provides a holistic, MECE-compliant foundation for understanding, evaluating, and improving software throughput across technical, operational, and business dimensions.

Bibliography
A. Bertolino. (2007). Software Testing Research: Achievements, Challenges, Dreams. In Future of Software Engineering (FOSE ’07). https://ieeexplore.ieee.org/document/4221614/

A. Goel. (1985). Software Reliability Models: Assumptions, Limitations, and Applicability. In IEEE Transactions on Software Engineering. https://ieeexplore.ieee.org/document/1701963/

Abhishek Singh, A. Raman, & D. Kakkar. (2014). Throughput Optimization in Cooperative Communications using Evolutionary Algorithms. In International journal of advanced research in electrical, electronics and instrumentation engineering. http://www.ijareeie.com/upload/2014/october/22B_Throughput.pdf

Andrés Silva. (2016). Reference and Structure of Software Engineering Theories. In ArXiv. https://www.semanticscholar.org/paper/1aebb0c4900e5fab3d0db21d22595bdbd1534ed1

Angela Fan, Beliz Gokkaya, Mark Harman, Mitya Lyubarskiy, Shubho Sengupta, Shin Yoo, & Jie M. Zhang. (2023). Large Language Models for Software Engineering: Survey and Open Problems. In 2023 IEEE/ACM International Conference on Software Engineering: Future of Software Engineering (ICSE-FoSE). https://ieeexplore.ieee.org/document/10449667/

AV Lakra & DK Yadav. (2015). Multi-objective tasks scheduling algorithm for cloud computing throughput optimization. In Procedia Computer Science. https://www.sciencedirect.com/science/article/pii/S1877050915006675

B Berger & YW Yu. (2023). Navigating bottlenecks and trade-offs in genomic data analysis. In Nature Reviews Genetics. https://www.nature.com/articles/s41576-022-00551-z

B Gingras, M Böckle, CT Herbst, & WT Fitch. (2013). Call acoustics reflect body size across four clades of anurans. In Journal of Zoology. https://zslpublications.onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-7998.2012.00973.x

B Han, V Gopalakrishnan, & L Ji. (2015). Network function virtualization: Challenges and opportunities for innovations. https://ieeexplore.ieee.org/abstract/document/7045396/

B Le Gal & C Jego. (2020). Low-latency and high-throughput software turbo decoders on multi-core architectures. In Annals of Telecommunications. https://link.springer.com/article/10.1007/s12243-019-00727-5

B Prabhu & N Balakumar. (2016). Methodology for Improving Security Issues and Reducing Vulnerability in Microprocessors. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2898885

B Vogel-Heuser, A Fay, I Schaefer, & M Tichy. (2015). Evolution of software in automated production systems: Challenges and research directions. https://www.sciencedirect.com/science/article/pii/S0164121215001818

Bruno Bodin, Alix Munier Kordon, & B. Dinechin. (2016). Optimal and fast throughput evaluation of CSDF. In 2016 53nd ACM/EDAC/IEEE Design Automation Conference (DAC). https://dl.acm.org/doi/10.1145/2897937.2898056

BW Boehm. (1987). Improving software productivity. In Computer. https://www.computer.org/csdl/api/v1/periodical/mags/co/1987/09/01663694/13rRUx0xPOM/download-article/pdf

C Boneti, FJ Cazorla, & R Gioiosa. (2008). Software-controlled priority characterization of POWER5 processor. https://dl.acm.org/doi/abs/10.1145/1394608.1382157

C. Duffield, R. Duffield, & S. Wilson. (2021). CHALLENGES AND RISKS. In Service Integration and Management (SIAMTM) Foundation Body of Knowledge (BoK), Second edition. http://www.jstor.org/stable/10.2307/j.ctv1m6vhq6.12

C. Ebert, Alan M. Davis, & C. Ebert. (2024). Software Principles. In IEEE Software. https://ieeexplore.ieee.org/document/10445156/

C Jin, F Zou, X Yang, & K Liu. (2021). 3-D virtual design and microstructural modeling of asphalt mixture based on a digital aggregate library. In Computers & Structures. https://www.sciencedirect.com/science/article/pii/S0045794920301814

C Laaber. (2019). Continuous software performance assessment: detecting performance problems of software libraries on every build. https://dl.acm.org/doi/abs/10.1145/3293882.3338982

C Millsap. (n.d.). Thinking Clearly About Performance, Part 1 Improving the performance of complex software is difficult, but understanding some fundamental principles can …. https://cacm.acm.org/practice/thinking-clearly-about-performance-part-1/

C Yang, P Liang, & P Avgeriou. (2018). Assumptions and their management in software development: A systematic mapping study. In Information and Software Technology. https://www.sciencedirect.com/science/article/pii/S0950584916304189

CA Brown. (2005). Teaching axiomatic design to engineers—Theory, applications, and software. In Journal of Manufacturing Systems. https://www.sciencedirect.com/science/article/pii/S0278612506800075

CA Moritz, D Yeung, & A Agarwal. (2001). SimpleFit: A framework for analyzing design trade-offs in raw architectures. https://ieeexplore.ieee.org/abstract/document/940747/

Changge Fang, I. Avis, D. Salomon, & F. Cuttitta. (2013). Novel Phenotypic Fluorescent Three-Dimensional Platforms for High-throughput Drug Screening and Personalized Chemotherapy. In Journal of Cancer. https://www.jcancer.org/v04p0402.htm

Che Zhang, Shiwei Zhang, Yi Wang, Weichao Li, Bo Jin, Ricky K. P. Mok, Qing Li, & Hong Chao Xu. (2019). Scalable Traffic Engineering for Higher Throughput in Heavily-loaded Software Defined Networks. In NOMS 2020 - 2020 IEEE/IFIP Network Operations and Management Symposium. https://arxiv.org/abs/1909.09315

CM Woodside. (1989). Throughput calculation for basic stochastic rendezvous networks. In Performance Evaluation. https://www.sciencedirect.com/science/article/pii/0166531689900394

Colin Scott, Andreas Wundsam, B. Raghavan, Aurojit Panda, Andrew Or, J. Lai, Eugene Huang, Zhi Liu, Ahmed El-Hassany, S. Whitlock, H. B. Acharya, K. Zarifis, & S. Shenker. (2014). Troubleshooting blackbox SDN control software with minimal causal sequences. In ACM SIGCOMM Computer Communication Review. https://www.semanticscholar.org/paper/2afc8d9b3a0d17fb926a6a6dd05b1fb307130a27

Connor Kimball. (2014). Comparing Virtual Call Center Software: Five9 vs AVOXI. https://www.semanticscholar.org/paper/0cfad330fbe4e242f38b9ddb09a14d489cf698ff

CU Smith. (2007). Introduction to software performance engineering: Origins and outstanding problems. https://link.springer.com/chapter/10.1007/978-3-540-72522-0_10

CU Smith & LG Williams. (2002). New software performance antipatterns: More ways to shoot yourself in the foot. In Int. CMG Conference. https://perfeng.com/papers/moreanti.pdf

D Agnew & J McNair. (2023). Detection of denial-of-service attacks in a software-defined LEO constellation network. https://par.nsf.gov/biblio/10447247

D Arcelli, V Cortellessa, & C Trubiani. (2012). Antipattern-based model refactoring for software performance improvement. https://dl.acm.org/doi/abs/10.1145/2304696.2304704

D Arcelli, V Cortellessa, & D Di Pompeo. (2018). Performance-driven software model refactoring. https://www.sciencedirect.com/science/article/pii/S0950584917301787

D Kreutz, FMV Ramos, & PE Verissimo. (2014). Software-defined networking: A comprehensive survey. https://ieeexplore.ieee.org/abstract/document/6994333/

D Minovski, N Ögren, & K Mitra. (2021). Throughput prediction using machine learning in LTE and 5G networks. https://ieeexplore.ieee.org/abstract/document/9495144/

D. Oleynik, S. Panitkin, M. Turilli, Alessio Angius, S. Oral, K. De, A. Klimentov, J. Wells, & S. Jha. (2017). High-Throughput Computing on High-Performance Platforms: A Case Study. In 2017 IEEE 13th International Conference on e-Science (e-Science). https://arxiv.org/abs/1704.00978

D R. Thorne. (2006). Throughput: a simple performance index with desirable characteristics. In Behavior research methods. https://link.springer.com/article/10.3758/BF03193886

D Tong, YR Qu, & VK Prasanna. (2014). High-throughput traffic classification on multi-core processors. https://ieeexplore.ieee.org/abstract/document/6900894/

D. Wood & E. Forman. (1899). Throughput measurement using a synthetic job stream. In AFIPS ’71 (Fall). https://dl.acm.org/citation.cfm?doid=1479064.1479074

D. Woollard, C. Mattmann, & N. Medvidović. (2009). Injecting software architectural constraints into legacy scientific applications. In 2009 ICSE Workshop on Software Engineering for Computational Science and Engineering. https://ieeexplore.ieee.org/document/5069164/

DA Pereira & JA Williams. (2007). Origin and evolution of high throughput screening. In British journal of pharmacology. https://bpspubs.onlinelibrary.wiley.com/doi/abs/10.1038/sj.bjp.0707373

Davide Arcelli, V. Cortellessa, & Daniele Di Pompeo. (2018). Performance-Driven Software Architecture Refactoring. In 2018 IEEE International Conference on Software Architecture Companion (ICSA-C). https://ieeexplore.ieee.org/document/8432081/

DGA Smith, LA Burns, & AC Simmonett. (2020). PSI4 1.4: Open-source software for high-throughput quantum chemistry. https://pubs.aip.org/aip/jcp/article/152/18/184108/972964

D.W.-H. Wong & M. Aleksic. (2001). Performance prediction on graphics hardware using software simulation. In Canadian Conference on Electrical and Computer Engineering 2001. Conference Proceedings (Cat. No.01TH8555). https://ieeexplore.ieee.org/document/933618/

Dylan Vern Phillips, C. Dylan, & Vern Phillips. (n.d.). Algorithms in Throughput Maximization. https://www.semanticscholar.org/paper/4f04286886ac0a0ce93106d1905a3129472cfc09

EE SalisuGarba, Salim M. Ahmad, & Suleiman Ibrahim. (2017). PERFORMANCE IMPLICATIONS OF ENTERPRISE SOFTWARE DEVELOPMENT USING J 2. https://www.semanticscholar.org/paper/57a456dd9a9e6dc9ca90b7b716aefec84de7c400

Eric Bouwers, A. Deursen, & Joost Visser. (2013). Software metrics: Pitfalls and best practices. In 2013 35th International Conference on Software Engineering (ICSE). https://ieeexplore.ieee.org/document/6606755/

F Aquilani, S Balsamo, & P Inverardi. (2001). Performance analysis at the software architectural design level. In Performance Evaluation. https://www.sciencedirect.com/science/article/pii/S0166531601000359

F Losavio, L Chirinos, & N Lévy. (2003). Quality characteristics for software architecture. https://www.jot.fm/issues/issue_2003_03/article2.pdf

F Solimani, A Cardellicchio, M Nitti, A Lako, & G Dimauro. (2023). A systematic review of effective hardware and software factors affecting high-throughput plant phenotyping. In Information. https://www.mdpi.com/2078-2489/14/4/214

Fahad Khan. (2014). Innovation in software defined networking and throughput optimum scheduling algorithm. https://www.semanticscholar.org/paper/148d030ba59af627425cbd621f9c47e0b32644ca

G Boloix & PN Robillard. (1995). A software system evaluation framework. In Computer. https://ieeexplore.ieee.org/abstract/document/476196/

G Cugola & C Ghezzi. (1998). Software Processes: a Retrospective and a Path to the Future. https://onlinelibrary.wiley.com/doi/abs/10.1002/(SICI)1099-1670(199809)4:3%3C101::AID-SPIP103%3E3.0.CO;2-K

G. Holzmann. (2018). Software Components. In IEEE Software. https://ieeexplore.ieee.org/document/8354432/

G. P. C. Á. n, 준 김성, 현 이강, 운 임대, ° 기순, Won-kyu Park, Sung-joon Kim, Kang-hyun Lee, Dae-woon Lim, & Ki-soon Yu. (2017). A Study on the Throughput Enhancement in Software Implementation of Ultra Light-Weight Cryptography PRESENT. In The Journal of Korean Institute of Communications and Information Sciences. http://koreascience.or.kr/article/JAKO201710757618057.page

G Shrivastava. (n.d.). Troubleshooting Common Control System Issues. https://ijrsml.org/wp-content/uploads/2025/02/in_ijrsml_Feb_2025_GC250228-AP06-Troubleshooting-Common-Control-System-Issues-41-59.pdf

George Mathew, Amritanshu Agrawal, & T. Menzies. (2016). Finding Trends in Software Research. In IEEE Transactions on Software Engineering. https://arxiv.org/abs/1608.08100

Gongming Zhao, Liusheng Huang, Zhuolong Yu, Hongli Xu, & Pengzhan Wang. (2017). On the effect of flow table size and controller capacity on SDN network throughput. In 2017 IEEE International Conference on Communications (ICC). https://ieeexplore.ieee.org/document/7996512/

H. Aldewachi, R. Al-Zidan, M. Conner, & M. Salman. (2021). High-Throughput Screening Platforms in the Discovery of Novel Drugs for Neurodegenerative Diseases. In Bioengineering. https://www.mdpi.com/2306-5354/8/2/30

H Koziolek. (2010). Performance evaluation of component-based software systems: A survey. In Performance evaluation. https://www.sciencedirect.com/science/article/pii/S016653160900100X

H. Ö. Ünver & John A. Masciola. (2008). Using architectural software patterns in support of controlling modular high throughput screening automation systems. In 2008 IEEE International Conference on Automation Science and Engineering. https://www.semanticscholar.org/paper/9fe9856c7c300a2193b30994ebaec89df8152dd2

H. Pinkard, N. Stuurman, Kaitlin Corbin, R. Vale, & M. Krummel. (2016). Micro-Magellan: A flexible, open source acquisition software for high throughput biological light microscopy. In bioRxiv. https://www.semanticscholar.org/paper/75ee16c791c7e456108033463a2242490b202b6d

H. Sharma, A. Shastri, R. Biswas, & S. K. Singh. (2014). SGA Dynamic Parameters: The Core Components of Automated Database Tuning. In Database Systems Journal. https://www.semanticscholar.org/paper/47193c0f8b3f0a26a2ab9c23693b2b73f4221b20

Hang Zhang, Mengjing Xu, Haofeng Li, Xiaohan Mai, Jiawei Sun, Lan Mi, Jiong Ma, Xiangdong Zhu, & Yiyan Fei. (2023). Detection speed optimization of the OI-RD microscope for ultra-high throughput screening. In Biomedical optics express. https://validate.perfdrive.com/?ssa=efbc2621-7fd2-2051-8b3e-4cd536fc61ff&ssb=50769274688&ssc=https%3A%2F%2Fopg.optica.org&ssi=9c4a5589-d3hy-9f1a-c162-fdcc9e6a6719&ssk=botmanager_support@radware.com&ssm=91254272282876436135786483372760&ssn=f51fe56194564d23a64d57d3a94220164d48092369b9-ebba-8d6a-f86de8&sso=9aa9d6a-f790-1255236cf0a1c510c05df5ad7545937953d0158d04365567&ssp=93615015401749603894174966132524020&ssq=58702619665654237481696645844893145881021&ssr=MzQuNzIuMjUyLjkz&sst=python-httpx%2F0.27.2&ssv=&ssw=

HM Ali, MY Hamza, & TA Rashid. (2024). A comprehensive study on automated testing with the software lifecycle. In arXiv. https://arxiv.org/abs/2405.01608

I Bukhman & I Bukhman. (2021). Software Contradictions. https://link.springer.com/chapter/10.1007/978-981-16-1041-7_8

I Caraus, AA Alsuwailem, & R Nadon. (2015). Detecting and overcoming systematic bias in high-throughput screening technologies: a comprehensive review of practical issues and methodological solutions. https://academic.oup.com/bib/article-abstract/16/6/974/225604

I Neamtiu & T Dumitraş. (2011). Cloud software upgrades: Challenges and opportunities. https://ieeexplore.ieee.org/abstract/document/6049037/

Ion Buligiu & Georgeta Soava. (2006). Quality Research by Using Performance Evaluation Metrics for Software Systems and Components. https://www.semanticscholar.org/paper/bdba8e6cb3060b1e341f6f24940746564957840e

Iyad Lahsen Cherif, Lynda Zitoune, & V. Vèque. (2017). Joint optimization of energy consumption and throughput of directional WMNs. In 2017 IEEE International Conference on Communications (ICC). https://ieeexplore.ieee.org/document/7997322/

J. Choobineh, E. Anderson, & Evelyn J. Barry. (2009). Some Throughput Metrics for (SOA) Application Development. In Americas Conference on Information Systems. https://www.semanticscholar.org/paper/f437b7bce63ded6855b553b211239950d6886b71

J Dongarra, R Graybill, W Harrod, R Lucas, & E Lusk. (2008). DARPA’s HPCS program: History, models, tools, languages. https://www.sciencedirect.com/science/article/pii/S0065245808000016

J Mitola. (2002). Software radios: Survey, critical evaluation and future directions. In IEEE Aerospace and Electronic Systems Magazine. https://ieeexplore.ieee.org/abstract/document/210638/

J Münch. (2011). Risk management in global software development projects: Challenges, solutions, and experience. https://www.computer.org/csdl/proceedings-article/icgse-w/2011/4558a035/12OmNxj23dD

J Son & R Buyya. (2018). Priority-aware VM allocation and network bandwidth provisioning in software-defined networking (SDN)-enabled clouds. In IEEE Transactions on Sustainable Computing. https://ieeexplore.ieee.org/abstract/document/8369147/

J Treibig, G Hager, & G Wellein. (2012). Performance patterns and hardware metrics on modern multicore processors: Best practices for performance engineering. https://link.springer.com/chapter/10.1007/978-3-642-36949-0_50

J Verma, A Bhandari, & G Singh. (2022). iNIDS: SWOT Analysis and TOWS Inferences of State-of-the-Art NIDS solutions for the development of Intelligent Network Intrusion Detection System. In Computer communications. https://www.sciencedirect.com/science/article/pii/S0140366422003371

JA Joao, MA Suleman, O Mutlu, & YN Patt. (2012). Bottleneck identification and scheduling in multithreaded applications. https://dl.acm.org/doi/abs/10.1145/2189750.2151001

JA Zinky. (1989). An example of automatically troubleshooting a throughput bottleneck using model based techniques. https://ieeexplore.ieee.org/abstract/document/49920/

J.A. Zinky & J.-L. Flechon. (1989). An automatic network troubleshooter for throughput bottlenecks in computer networks. In [1989] Proceedings. The Annual AI Systems in Government Conference. https://ieeexplore.ieee.org/document/47338/

Jannis Klinkenberg, Clément Foyer, Pierre Clouzet, Brice Goglin, Emmanuel Jeannot, Christian Terboven, & Anara Kozhokanova. (2024). Phase-Based Data Placement Optimization in Heterogeneous Memory. In 2024 IEEE International Conference on Cluster Computing (CLUSTER). https://ieeexplore.ieee.org/document/10740892/

JD Davis, J Laudon, & K Olukotun. (2005). Maximizing CMP throughput with mediocre cores. https://ieeexplore.ieee.org/abstract/document/1515580/

JE Neilson, CM Woodside, & DC Petriu. (1995). Software bottlenecking in client-server systems and rendezvous networks. https://ieeexplore.ieee.org/abstract/document/464543/

John Stouby Persson, L. Mathiassen, Jesper Boeg, Thomas Stenskrog Madsen, & Flemming Steinson. (2009). Managing Risks in Distributed Software Projects: An Integrative Framework. In IEEE Transactions on Engineering Management. https://ieeexplore.ieee.org/document/4815496/

JT Lawson & MP Mariani. (1978). Distributed data processing system design-A look at the partitioning problem. https://ieeexplore.ieee.org/abstract/document/810414/

K. Bhandari, K. Kumar, & A. L. Sangal. (2023). Artificial Intelligence in Software Engineering: Perspectives and Challenges. In 2023 Third International Conference on Secure Cyber Computing and Communication (ICSCCC). https://ieeexplore.ieee.org/document/10176436/

K Bian & JMJ Park. (2008). Security vulnerabilities in IEEE 802.22. https://dl.acm.org/doi/abs/10.5555/1554126.1554138

K Branson, AA Robie, J Bender, & P Perona. (2009). High-throughput ethomics in large groups of Drosophila. https://www.nature.com/articles/nmeth.1328

K Luo, J Gummaraju, & M Franklin. (2001). Balancing thoughput and fairness in SMT processors. https://www.computer.org/csdl/proceedings-article/ispass/2001/00990695/12OmNAgGwd7

K. Suthar & V. Deshpande. (2014). Review on reducing manufacturing throughput time: Various tools and techniques. In Journal of emerging technologies and innovative research. https://www.semanticscholar.org/paper/7c8c0b16b01f5e88751a47fea87eb370900dfb9b

Kai Gao, Changqiao Xu, Jianfeng Guan, & Yang Liu. (2017). A Survey of Multipath Transport Mechanism in Software Defined Network. In 2017 International Conference on Networking and Network Applications (NaNA). https://www.semanticscholar.org/paper/0794d152378177d57eb64007a750701115d4665e

Kensuke Shibata, S. Narieda, & H. Naruse. (2022). Throughput Estimation of WLAN in Multiple Channels Using a Software Based Packet Analyzer. In IEEE Networking Letters. https://ieeexplore.ieee.org/document/9829870/

L Catuogno, C Galdi, & N Pasquino. (2018). An effective methodology for measuring software resource usage. https://ieeexplore.ieee.org/abstract/document/8329218/

L Leonardi, L Lo Bello, & S Aglianò. (2020). Priority-based bandwidth management in virtualized software-defined networks. In Electronics. https://www.mdpi.com/2079-9292/9/6/1009

L Zheng, B Zhu, P Yao, Y Zhou, & C Pan. (2025). PRAGA: A priority-aware hardware/software co-design for high-throughput graph processing acceleration. https://dl.acm.org/doi/abs/10.1145/3701998

Liguo Yu & S. Ramaswamy. (2011). Examining the Relationships between Software Coupling and Software Performance: A Cross-platform Experiment. In J. Comput. Inf. Technol. https://www.semanticscholar.org/paper/f8ce1c234c8e801a351e43f7473e7bd6717efaa4

Liu Qiu-hua. (2004). Research on Software Architecture Evaluation Methods. In Application Research of Computers. https://www.semanticscholar.org/paper/8fdb28c1bf33c27a5ba5a52d5fe32279e00009f5

Long Jun. (2004). Bidding strategies for continuous and interval generation. In Electric power automation equipment. https://www.semanticscholar.org/paper/b5c46a092e5406e31f939f77af799e089826cf5a

Lucas Smith. (2009). Today’s GC-MS Analyses: How Integrated Software Is Increasing Laboratory Throughput and Productivity. In Lc Gc North America. https://www.semanticscholar.org/paper/46c66999d74c56c24e1e1a2b07869b12f2a31807

Ludwig Dierks & Sven Seuken. (2020). Revenue Maximization for Consumer Software: Subscription or Perpetual License? In ArXiv. https://www.semanticscholar.org/paper/71cbeee2f67b675f0ba2a8ce4018a0cf09b552bd

Luis Díaz-Garcia, G. Covarrubias-Pazaran, B. Schlautman, & J. Zalapa. (2016). GiNA, an Efficient and High-Throughput Software for Horticultural Phenotyping. In PLoS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0160439

M Alenezi & M Akour. (2025). AI-Driven Innovations in Software Engineering: A Review of Current Practices and Future Directions. In Applied Sciences. https://www.mdpi.com/2076-3417/15/3/1344

M Castro, M Costa, & T Harris. (2006). Securing software by enforcing data-flow integrity. https://www.usenix.org/event/osdi06/tech/full_papers/castro/castro_html/

M Cataldo, JD Herbsleb, & KM Carley. (2008). Socio-technical congruence: a framework for assessing the impact of technical and work dependencies on software development productivity. https://dl.acm.org/doi/abs/10.1145/1414004.1414008

M Dobrescu, N Egi, K Argyraki, & BG Chun. (2009). RouteBricks: Exploiting parallelism to scale software routers. https://dl.acm.org/doi/abs/10.1145/1629575.1629578

M Finsterbusch, C Richter, & E Rocha. (2013). A survey of payload-based traffic classification approaches. https://ieeexplore.ieee.org/abstract/document/6644335/

M Hashemi & S Ghiasi. (2009). Throughput-driven synthesis of embedded software for pipelined execution on multicore architectures. https://dl.acm.org/doi/abs/10.1145/1457255.1457258

M. Horodyskyi, I. Hrabchuk, І. Л. Грабчук, & Микола Петрович Городиський. (2018). Software market analysis for preparing records and reporting. https://www.semanticscholar.org/paper/ba4d9e1f636a07956dd37146328f96d35d4a443e

M Huang, W Liang, Z Xu, & S Guo. (2017). Efficient algorithms for throughput maximization in software-defined networks with consolidated middleboxes. https://ieeexplore.ieee.org/abstract/document/7972906/

M Iansiti & GL Richards. (2006). The information technology ecosystem: Structure, health, and performance. In The Antitrust Bulletin. https://journals.sagepub.com/doi/abs/10.1177/0003603X0605100104

M Karakus & A Durresi. (2017). A survey: Control plane scalability issues and approaches in software-defined networking (SDN). In Computer Networks. https://www.sciencedirect.com/science/article/pii/S138912861630411X

M Mehmandoost. (1949). Maximizing Throughput and Enhancing Strategic Decision-Making through Technological Considerations: A Systems-Based Approach to Management Accounting. In Available at SSRN 4936321. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4936321

M Noferesti & N Ezzati-Jivan. (2024). Enhancing empirical software performance engineering research with kernel-level events: A comprehensive system tracing approach. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S0164121224001626

M. Raveendra Kumar & R. Hari Kumar. (2011). Architectural refactoring of a mission critical integration application: a case study. In International Symposium on Electronic Commerce. https://dl.acm.org/doi/10.1145/1953355.1953365

M Richards. (2015). Software architecture patterns. https://isip.piconepress.com/courses/temple/ece_1111/resources/articles/20211201_software_architecture_patterns.pdf

M Salehie & L Tahvildari. (2009). Self-adaptive software: Landscape and research challenges. https://dl.acm.org/doi/abs/10.1145/1516533.1516538

M Spraul, M Hofmann, & M Ackermann. (1997). … injection proton nuclear magnetic resonance spectroscopy combined with pattern recognition methods: implications for rapid structural studies and high throughput …. https://pubs.rsc.org/en/content/articlehtml/1997/ac/a705551j

M Stal. (2014). Refactoring software architectures. In Agile Software Architecture. https://www.sciencedirect.com/science/article/pii/B9780124077720000034

M Subramaniyan, A Skoogh, & AS Muhammad. (2020). A data-driven approach to diagnosing throughput bottlenecks from a maintenance perspective. https://www.sciencedirect.com/science/article/pii/S0360835220305519

M Vogeser & YV Zhang. (2018). Understanding the strategic landscape surrounding the implementation of mass spectrometry in the clinical laboratory: a SWOT analysis. In Clinical Mass Spectrometry. https://www.sciencedirect.com/science/article/pii/S2376999818300035

MA Malina & HSO Nørreklit. (2007). Relations among measures, climate of control, and performance measurement models. https://onlinelibrary.wiley.com/doi/abs/10.1506/car.24.3.10

Mahmood A. Al-Shareeda, Abeer Abdullah Alsadhan, Hamzah H. Qasim, & S. Manickam. (2024). Software defined networking for internet of things: review, techniques, challenges, and future directions. In Bulletin of Electrical Engineering and Informatics. https://www.semanticscholar.org/paper/a218b66503a9182bb380359b3adb05f72f37e28b

Mansi Sood, Ankur A. Kulkarni, & Sharayu Moharir. (2020). Duopolistic platform competition for revenue and throughput. In ArXiv. https://www.semanticscholar.org/paper/da51aa8ec141af31d31eab979ed6555ec75959b0

Maria Jo, Castro Sousa, & Helena Mendes Moreira. (1998). A survey on the Software Maintenance Process. In Proceedings. International Conference on Software Maintenance (Cat. No. 98CB36272). https://www.semanticscholar.org/paper/b366be37e68c9942c4a02904691dfd9ed2da4cd9

Marijana Mojsilović, I. Terzić, Snežana Gavrilović, & Goran Miodragović. (2021). Carrier optimization using CAD software and biologically inspired algorithms. In IMK-14 - Istrazivanje i razvoj. https://www.semanticscholar.org/paper/398962ad9d1892505ff8d2af7fc556bf79be86d8

Mateusz Kikolski. (2016). Identification of production bottlenecks with the use of Plant Simulation software. In Ekonomia i Zarzadzanie. https://www.semanticscholar.org/paper/77573ddbcf58108c1270663a9b84e3db78c1fc28

MI Babar & M Ramzan. (2011). Challenges and future trends in software requirements prioritization. https://ieeexplore.ieee.org/abstract/document/6020888/

MN Wirawan & M Lubis. (2024). Evaluating Quality of Service: Throughput, Packet Loss, and Delay in Tree Topology with Ryu and Pox Controllers in Software-Defined Network. https://ieeexplore.ieee.org/abstract/document/10748026/

MR Braz & SR Vergilio. (2006). Software effort estimation based on use cases. https://ieeexplore.ieee.org/abstract/document/4020081/

Muhammad Arief Nugroho & N. Suwastika. (2018). Perancangan Intrusion Prevention System pada Jaringan Software Defined Networks. In JUMANJI (Jurnal Masyarakat Informatika Unjani). https://www.semanticscholar.org/paper/b70ba2baf9dea7b42ff1c6b1f2f24e1cac43b615

MYK Brusniak, ST Kwok, & M Christiansen. (2011). ATAQS: A computational software tool for high throughput transition optimization and validation for selected reaction monitoring mass spectrometry. https://link.springer.com/article/10.1186/1471-2105-12-78

N. Alshahwan, M. Harman, & Alexandru Marginean. (2023). Software Testing Research Challenges: An Industrial Perspective. In 2023 IEEE Conference on Software Testing, Verification and Validation (ICST). https://ieeexplore.ieee.org/document/10132192/

N Bonin, E Doster, H Worley, & LJ Pinnell. (2023). … , v3. 0: an updated comprehensive database of antimicrobial resistance determinants and an improved software pipeline for classification using high-throughput …. https://academic.oup.com/nar/article-abstract/51/D1/D744/6830666

N Hanford, V Ahuja, & M Farrens. (2014). Analysis of the effect of core affinity on high-throughput flows. https://ieeexplore.ieee.org/abstract/document/7017638/

N Hanford, V Ahuja, M Farrens, & D Ghosal. (2016). Improving network performance on multicore systems: Impact of core affinities on high throughput flows. https://www.sciencedirect.com/science/article/pii/S0167739X15002927

N Nagappan, T Ball, & B Murphy. (2006). Using historical in-process and product metrics for early estimation of software failures. https://ieeexplore.ieee.org/abstract/document/4021972/

N Rios, RO Spínola, & M Mendonça. (2019). Supporting analysis of technical debt causes and effects with cross-company probabilistic cause-effect diagrams. https://ieeexplore.ieee.org/abstract/document/8785063/

Nagaraju Tumakuru Anadanaiah & M. V. Panduranga Rao. (2024). Cognitive routing in software defined networks using learning models with latency and throughput constraints. In IAES International Journal of Artificial Intelligence (IJ-AI). https://www.semanticscholar.org/paper/0920d01e8606a3857c4e704a95967cebaa78dab9

Netanel Zakay & D. Feitelson. (2017). Models for evaluating throughput. In Proceedings of the 10th ACM International Systems and Storage Conference. https://www.semanticscholar.org/paper/4122c51d521cbfa8ade6ae7726953c184dc7af20

NNV Ferreira & JJ Langerman. (2014). Proving that the release management process can enhance throughput in software development projects. https://ieeexplore.ieee.org/abstract/document/6926496/

O. Vidal, G. Verelst, J. Lacan, E. Alberty, J. Radzik, & M. Bousquet. (2012). Next generation High Throughput Satellite system. In 2012 IEEE First AESS European Conference on Satellite Telecommunications (ESTEL). https://ieeexplore.ieee.org/document/6400146/

OB Yahia, Z Garroussi, & O Bélanger. (2024). Evolution of high-throughput satellite systems: A vision of programmable regenerative payload. https://ieeexplore.ieee.org/abstract/document/10648786/

OB Yahia, Z Garroussi, O Bélanger, & B Sansò. (2023). Evolution of high throughput satellite systems: Vision, requirements, and key technologies. https://arxiv.org/abs/2310.04389

OH Alhazmi, YK Malaiya, & I Ray. (2007). Measuring, analyzing and predicting security vulnerabilities in software systems. In computers & security. https://www.sciencedirect.com/science/article/pii/S0167404806001520

Özkan Yildiz & Onur Demirörs. (2009). Adopting Software Quality Measures for Healthcare Processes. In Studies in health technology and informatics. https://www.semanticscholar.org/paper/9ea90326c3c071855c63bf69144aac0baa15d39d

P Berander, LO Damm, J Eriksson, & T Gorschek. (2005). Software quality attributes and trade-offs. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=57d7ef7a35d480e2ebd41f66ece451c4d7a7a40a

P. Meyer. (2012). Identifying core components in software systems. https://www.semanticscholar.org/paper/a50ff0bbc8daeeeed1642af7555f22ac50cc6d87

P Rotella. (2018). Software security vulnerabilities: baselining and benchmarking. https://dl.acm.org/doi/abs/10.1145/3194707.3194708

Puneet Goswami, Pradeep Kumar, & K. Nand. (2012). EVALUATION OF COMPLEXITY FOR COMPONENTS IN COMPONENT BASED SOFTWARE ENGINEERING. https://www.semanticscholar.org/paper/411c5a9e46d8ade6887264b97db569c896029275

R. Akhpashev, V. Drozdova, Andrey V. Andreev, & Gregory G. Patrushev. (2017). Cross-platform software and hardware solutions for the problems of analysis and multi-objective optimization of the UL throughput in LTE networks. In 2017 18th International Conference of Young Specialists on Micro/Nanotechnologies and Electron Devices (EDM). https://ieeexplore.ieee.org/document/7981734/

R. Balakrishnan & Dr. N. Sankarram. (2020). SELF-AWARE ADAPTABLE SOFTWARE ARCHITECTURAL PATTERN BASED ON ASSOCIATION RULE MINING. https://www.semanticscholar.org/paper/e764b42626bc876ada5ae90335502ff646932caf

R Cohen & Y Nezri. (2019). Cardinality estimation in a virtualized network device using online machine learning. In IEEE/ACM Transactions on Networking. https://ieeexplore.ieee.org/abstract/document/8845758/

R Das, A Laederach, SM Pearlman, & D Herschlag. (2005). SAFA: semi-automated footprinting analysis software for high-throughput quantification of nucleic acid footprinting experiments. In Rna. https://rnajournal.cshlp.org/content/11/3/344.short

R Harmon, D Raffo, & S Faulk. (2005). Value-based pricing for new software products: strategy insights for developers. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=5fc878c1fd889b8d548f07f10153fd519a03e745

R Prasad, C Dovrolis, M Murray, & K Claffy. (2003). Bandwidth estimation: metrics, measurement techniques, and tools. In IEEE network. https://ieeexplore.ieee.org/abstract/document/1248658/

R. Weidlich, M. Nussbaumer, & H. Hlavacs. (2010). Optimization towards Consolidation or Throughput for Multi-thread Software. In 2010 3rd International Symposium on Parallel Architectures, Algorithms and Programming. https://ieeexplore.ieee.org/document/5715079/

RE Al-Qutaish. (2010). Quality models in software engineering literature: an analytical and comparative study. In Journal of American Science. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=77b51002b53d002278997c71c72eaf2300a87ec7

RJ Toonen & S Hughes. (2001). Increased throughput for fragment analysis on an ABI Prism® 377 automated sequencer using a membrane comb and STRand software. In Biotechniques. https://www.researchgate.net/profile/Robert-Toonen/publication/229088959_Increased_throughput_for_fragment_analysis_on_an_ABI_PRISM_377_automated_sequencer_using_a_membrane_comb_and_STRand_software/links/53fcf24f0cf2364ccc068386/Increased-throughput-for-fragment-analysis-on-an-ABI-PRISM-377-automated-sequencer-using-a-membrane-comb-and-STRand-software.pdf

RL Nord, I Ozkaya, & RS Sangwan. (2012). Making architecture visible to improve flow management in lean software development. In IEEE software. https://ieeexplore.ieee.org/abstract/document/6226344/

Ronan Fitzpatrick, Peter Smith, & Brendan O’Shea. (2004). Software quality challenges. In International Conference on Software Engineering. https://www.semanticscholar.org/paper/952dbcab29a0daed0a80719956f2b1e10b88a6ec

Ryszard S. Romaniuk. (2011). Search for Ultimate Throughput in Ultra-Broadband Photonic Internet. In International Journal of Electronics and Telecommunications. https://www.semanticscholar.org/paper/470ed4e7a6f7ed8badebc3bcbaeb46380e71c4a4

S Amrouche, L Basara, & P Calafiura. (2023). The tracking machine learning challenge: throughput phase. https://link.springer.com/article/10.1007/s41781-023-00094-w

S Balsamo, A Di Marco, & P Inverardi. (2004). Model-based performance prediction in software development: A survey. https://ieeexplore.ieee.org/abstract/document/1291833/

S Balsamo, P Inverardi, & C Mangano. (1998). An approach to performance evaluation of software architectures. https://dl.acm.org/doi/pdf/10.1145/287318.287354

S Bashir, SV Kik, M Ruhwald, A Khan, & M Tariq. (2022). Economic analysis of different throughput scenarios and implementation strategies of computer-aided detection software as a screening and triage test for pulmonary …. In Plos one. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0277393

S Chaudhry, P Caprioli, S Yip, & M Tremblay. (2005). High-performance throughput computing. In IEEE Micro. https://ieeexplore.ieee.org/abstract/document/1463182/

S. Chou & Chung-Wei Huang. (2001). A software product model emphasizing relationships. In Proceedings Second Asia-Pacific Conference on Quality Software. https://ieeexplore.ieee.org/document/990047/

S Duttagupta, R Virk, & M Nambiar. (2014). Predicting performance in the presence of software and hardware resource bottlenecks. https://ieeexplore.ieee.org/abstract/document/6879991/

S Duttagupta, R Virk, & M Nambiar. (2015). Software bottleneck analysis during performance testing. https://ieeexplore.ieee.org/abstract/document/7344508/

S Eyerman, P Michaud, & W Rogiest. (2014). Multiprogram throughput metrics: A systematic approach. https://dl.acm.org/doi/abs/10.1145/2663346

S Gallenmüller, P Emmerich, & F Wohlfart. (2015). Comparison of frameworks for high-performance packet IO. https://ieeexplore.ieee.org/abstract/document/7110118/

S Koh. (2016). Cause-and-Effect Perspective on Software Quality: Application to ISO/IEC 25000 Series SQuaRE’s Product Quality Model. https://koreascience.kr/article/JAKO201631063313892.page

S Majumdar, CM Woodside, & JE Neilson. (1991). Performance bounds for concurrent software with rendezvous. https://www.sciencedirect.com/science/article/pii/0166531691900477

S Pai & K Pingali. (2016). A compiler for throughput optimization of graph algorithms on GPUs. https://dl.acm.org/doi/abs/10.1145/2983990.2984015

S Pargaonkar. (2023). A comprehensive review of performance testing methodologies and best practices: software quality engineering. https://www.researchgate.net/profile/Shravan-Pargaonkar/publication/375450774_A_Comprehensive_Review_of_Performance_Testing_Methodologies_and_Best_Practices_Software_Quality_Engineering/links/654a9cf8b1398a779d6e2125/A-Comprehensive-Review-of-Performance-Testing-Methodologies-and-Best-Practices-Software-Quality-Engineering.pdf

S Planning. (2002). The economic impacts of inadequate infrastructure for software testing. In National Institute of Standards and Technology. https://lara.epfl.ch/w/_media/misc/rti02economicimpactsinadequateinfrastructuresoftwaretesting.pdf

S Sen, W Lloyd, & MJ Freedman. (2010). Prophecy: Using History for High-Throughput Fault Tolerance. In NSDI. https://www.usenix.org/event/nsdi10/tech/full_papers/sen_siddhartha.pdf

S Sharma & S Srinivasan. (2022). A survey on software design based and project based metrics. https://www.ijcte.com/vol14/1310-G2180.pdf

S Shrestha. (2023). Exploring New Revenue Streams in a Software Company. https://www.theseus.fi/handle/10024/810720

S Stuijk, M Geilen, & T Basten. (2006). Exploring trade-offs in buffer requirements and throughput constraints for synchronous dataflow graphs. https://dl.acm.org/doi/abs/10.1145/1146909.1147138

S Stuijk, M Geilen, & T Basten. (2008). Throughput-buffering trade-off exploration for cyclo-static and synchronous dataflow graphs. In IEEE Transactions on Computers. https://ieeexplore.ieee.org/abstract/document/4483507/

S ur Rahman, GH Kim, & YZ Cho. (2018). Positioning of UAVs for throughput maximization in software-defined disaster area UAV communication networks. https://ieeexplore.ieee.org/abstract/document/8533581/

SA Jyothi, A Singla, & PB Godfrey. (2016). Measuring and understanding throughput of network topologies. https://ieeexplore.ieee.org/abstract/document/7877143/

SC Chao, KCJ Lin, & MS Chen. (2016). Flow classification for software-defined data centers using stream mining. https://ieeexplore.ieee.org/abstract/document/7549048/

SE Sim, S Easterbrook, & RC Holt. (2003). Using benchmarking to advance research: A challenge to software engineering. https://ieeexplore.ieee.org/abstract/document/1201189/

SI Mohamed. (2015). DevOps shifting software engineering strategy Value based perspective. In International Journal of Computer Engineering. https://www.academia.edu/download/52363089/Paper_2_-_DevOps_shifting_software_engineering_strategy-value_based_perspective-IOSR_JCE.pdf

Siddhisanket Raskar, T. Applencourt, Kalyan Kumaran, & G. Gao. (2023). Towards Maximum Throughput of Dataflow Software Pipeline under Resource Constraints. In Proceedings of the 14th International Workshop on Programming Models and Applications for Multicores and Manycores. https://www.semanticscholar.org/paper/ccdc4a0edbfa445ac5ece273d172015461012c04

Simon Bauer, Kilian Holzinger, Benedikt Jaeger, Paul Emmerich, & G. Carle. (2020). Online Monitoring of TCP Throughput Limitations. In NOMS 2020 - 2020 IEEE/IFIP Network Operations and Management Symposium. https://ieeexplore.ieee.org/document/9110324/

ST Chakradhar & A Raghunathan. (2010). Best-effort computing: Re-thinking parallel software and hardware. https://dl.acm.org/doi/abs/10.1145/1837274.1837492

Stijn Eyerman, P. Michaud, & W. Rogiest. (2014). Multiprogram Throughput Metrics. In ACM Transactions on Architecture and Code Optimization (TACO). https://www.semanticscholar.org/paper/ca990f401bc2e754e4b803ffc82819d571b4fa4c

Sujoy Sinha Roy. (2019). SaberX4: High-Throughput Software Implementation of Saber Key Encapsulation Mechanism. In 2019 IEEE 37th International Conference on Computer Design (ICCD). https://ieeexplore.ieee.org/document/8988659/

T Agerwala & M Gupta. (2006). Systems research challenges: A scale-out perspective. https://ieeexplore.ieee.org/abstract/document/5388721/

T Galkovskyi, Y Mileyko, A Bucksch, & B Moore. (2012). GiA Roots: software for the high throughput analysis of plant root system architecture. In BMC plant biology. https://link.springer.com/article/10.1186/1471-2229-12-116

T. Inagaki, Yohei Ueda, T. Nakaike, & Moriyoshi Ohara. (2019). Profile-based Detection of Layered Bottlenecks. In Proceedings of the 2019 ACM/SPEC International Conference on Performance Engineering. https://dl.acm.org/doi/10.1145/3297663.3310296

T Lerher, M Borovinsek, M Ficko, & I Palcic. (2017). Parametric study of throughput performance in SBS/RS based on simulation. http://www.ijsimm.com/Full_Papers/Fulltext2017/text16-1_96-107.pdf

T Mens & T Tourwé. (2004). A survey of software refactoring. In IEEE Transactions on software engineering. https://ieeexplore.ieee.org/abstract/document/1265817/

T Sterling, M Anderson, & M Brodowicz. (2017). A survey: runtime software systems for high performance computing. https://www.superfri.org/index.php/superfri/article/view/126

T Stober & U Hansmann. (2010). Best practices for large software development projects. https://link.springer.com/content/pdf/10.1007/978-3-540-70832-2.pdf

T. Thelin, P. Runeson, & C. Wohlin. (2003). Prioritized Use Cases as a Vehicle for Software Inspections. In IEEE Softw. https://ieeexplore.ieee.org/document/1207451/

T Ulversoy. (2010). Software defined radio: Challenges and opportunities. In IEEE Communications Surveys & Tutorials. https://ieeexplore.ieee.org/abstract/document/5462981/

Tausif Zahid, Xiaojun Hei, & W. Cheng. (2016). Understanding performance bottlenecks of a multi-BSS software defined WiFi network testbed. In 2016 First IEEE International Conference on Computer Communication and the Internet (ICCCI). https://www.semanticscholar.org/paper/f1c9c790a4248f5c0973be7aed748e3e8156c1fa

Topic 2 . 4 : The Evolution of Data Models. (2009). https://www.semanticscholar.org/paper/4d4664a028930438d5a8a0bb9176c3fdd0c19aeb

Tsehay Admassu Assegie & Pramod S. Nair. (2019). A review on software defined network security risks and challenges. In TELKOMNIKA (Telecommunication Computing Electronics and Control). https://www.semanticscholar.org/paper/4f40a63037e51304708fc1b2c26a3642e12b7078

Tyler Sondag & Hridesh Rajan. (2011). Phase-based tuning for better utilization of performance-asymmetric multicore processors. In International Symposium on Code Generation and Optimization (CGO 2011). https://ieeexplore.ieee.org/document/5764670/

Uwe Röttgermann. (2005). Decentralized Throughput Optimization in Industrial Networks. https://www.semanticscholar.org/paper/dc2fe42921e07b6b46f9f824bad165b4016343e2

V. Cortellessa, Daniele Di Pompeo, Vincenzo Stoico, & Michele Tucci. (2021). On the impact of Performance Antipatterns in multi-objective software model refactoring optimization. In 2021 47th Euromicro Conference on Software Engineering and Advanced Applications (SEAA). https://ieeexplore.ieee.org/document/9582578/

V Hnamte & J Hussain. (2024). Enhancing security in Software-Defined Networks: An approach to efficient ARP spoofing attacks detection and mitigation. In Telematics and Informatics Reports. https://www.sciencedirect.com/science/article/pii/S277250302400015X

V Ramasubramani, BD Dice, & ES Harper. (2020). freud: A software suite for high throughput analysis of particle simulation data. https://www.sciencedirect.com/science/article/pii/S0010465520300916

V. Schulte-Coerne, A. Thums, & Jochen Quante. (2009). Challenges in Reengineering Automotive Software. In 2009 13th European Conference on Software Maintenance and Reengineering. https://www.semanticscholar.org/paper/2ca3eff2cc6955ed8336adc1ebc39db4d5f66c45

V Zelesky, R Schneider, J Janiszewski, & I Zamora. (2013). Software automation tools for increased throughput metabolic soft-spot identification in early drug discovery. In Bioanalysis. https://www.tandfonline.com/doi/abs/10.4155/bio.13.89

Vignesh T. Ravi, James Erwin, P. Sivakumar, C. Q. Tang, Jianxin Xiong, Ravindra Babu Ganapathi, & M. Debbage. (2017). Host Software Stack Optimizations to Maximize Aggregate Fabric Throughput. In 2017 IEEE 25th Annual Symposium on High-Performance Interconnects (HOTI). https://ieeexplore.ieee.org/document/8071062/

Volodymyr Kuharsky, Dmytro Mykhalyk, & Yuri Humen. (2024). Analyzing specifics of scalability laws for proper modeling of a system’s throughput. In Congreso Internacional de Tecnologías e Innovación. https://www.semanticscholar.org/paper/1dd5a000709f96dc3eeb9ebc31c712aa98812a8a

VS Sharma & KS Trivedi. (2007). Quantifying software performance, reliability and security: An architecture-based approach. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S0164121206002020

VS Sharma, P Jalote, & KS Trivedi. (2005). Evaluating performance attributes of layered software architecture. https://link.springer.com/chapter/10.1007/11424529_5

W Diehl, F Farahmand, & P Yalla. (2017). Comparison of hardware and software implementations of selected lightweight block ciphers. https://ieeexplore.ieee.org/abstract/document/8056808/

W Wu, A Bobyshev, M Bowden, & M Crawford. (2007). End-to-end network/application performance troubleshooting methodology. https://www.academia.edu/download/41986411/CHEP07_TroubleshootingMethodology.pdf

W Xia, Y Wen, CH Foh, & D Niyato. (2014). A survey on software-defined networking. https://ieeexplore.ieee.org/abstract/document/6834762/

Weiyang Wang, M. Dong, K. Ota, Jun Wu, Jianhua Li, & Gaolei Li. (2019). CDLB: a cross-domain load balancing mechanism for software defined networks in cloud data centre. In Int. J. Comput. Sci. Eng. https://www.inderscienceonline.com/doi/abs/10.1504/IJCSE.2019.096986

Wu Lan-an. (2008). On Computer Troubleshooting. In Experiment Science and Technology. https://www.semanticscholar.org/paper/0bb92eccb7d93db93680f529245b912aa8dc06b1

X He, J Peddersen, & S Parameswaran. (2009). LOP: A novel sram-based architecture for low power and high throughput packet classification. https://dl.acm.org/doi/abs/10.1145/1629435.1629455

X Wang, EO Conchuir, & R Vidgen. (2008). A paradoxical perspective on contradictions in agile software development. https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1054&context=ecis2008

X Wang, J Mylopoulos, & G Guizzardi. (2016). How software changes the world: The role of assumptions. https://ieeexplore.ieee.org/abstract/document/7549327/

Y Endo, Z Wang, JB Chen, & MI Seltzer. (1996). Using latency to evaluate interactive system performance. https://www.usenix.org/publications/library/proceedings/osdi96/full_papers/endo/endo.ps

Y Gan, Y Zhang, D Cheng, A Shetty, & P Rathi. (2019). An open-source benchmark suite for microservices and their hardware-software implications for cloud & edge systems. https://dl.acm.org/doi/abs/10.1145/3297858.3304013

Y Liu & JYB Lee. (2015). An empirical study of throughput prediction in mobile data networks. https://ieeexplore.ieee.org/abstract/document/7417858/

Y Wang. (2005). On the mathematical laws of software. https://ieeexplore.ieee.org/abstract/document/1557174/

Y Wang. (2006). On the informatics laws and deductive semantics of software. https://ieeexplore.ieee.org/abstract/document/1624542/

Y. Zhang, Yuxin Huang, & Chunmian Ge. (2015). Human Resource Flow and Software Firm Performance: The Role of Direct vs. Indirect Competitors. In Pacific Asia Conference on Information Systems. https://www.semanticscholar.org/paper/10081cfd5946b5898464423693464736cd601f42

Yi Sun, Xiaoqi Yin, Nanshu Wang, Junchen Jiang, Vyas Sekar, Yun Jin, & B. Sinopoli. (2015). Analyzing TCP Throughput Stability and Predictability with Implications for Adaptive Video Streaming. In ArXiv. https://www.semanticscholar.org/paper/3315472affff84086da47fb108bdfe8e7ecd9007

Z Huang, M DAngelo, & D Miyani. (2016). Talos: Neutralizing vulnerabilities with security workarounds for rapid response. https://ieeexplore.ieee.org/abstract/document/7546526/

Z. Jiang & A. Hassan. (2015). A Survey on Load Testing of Large-Scale Software Systems. In IEEE Transactions on Software Engineering. https://ieeexplore.ieee.org/document/7123673/

Z Tlaiss, I Hamchaoui, & I Amigo. (2023). Troubleshooting enhancement with automated slow-start detection. https://ieeexplore.ieee.org/abstract/document/10073485/



Generated by Liner
https://getliner.com/search/s/5926611/t/85551079