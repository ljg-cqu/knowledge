'Software Security.' Requirements: 1. Ensure compliance with MECE. 2. Classify/categorize logically and appropriately if necessary. 3. Explain with analogy and examples. 4. Use numbered lists for clear explanations when possible. 5. Describe core elements, components, factors and aspects. 6. List core evaluation dimensions and corresponding evaluations if applicable. 7. Describe their concepts, definitions, functions, and characteristics. 8. Clarify their purposes and assumptions (Value, Descriptive, Prescriptive, Worldview, Cause-and-Effect). 9. Describe relevant markets, ecosystems, regulations, and economic models, and explain the corresponding strategies used to generate revenue. 10. Describe their work mechanism concisely first and then explain how they work with phase-based workflows throughout the entire lifecycle. 11. Clarify their preconditions, inputs, outputs, immediate outcomes, long-term impacts, and potential implications. 12. Clarify their underlying laws, axioms, theories, and patterns. 13. Describe the design philosophy and architectural features. 14. Provide ideas, techniques, and means of architectural refactoring. 15. Clarify relevant frameworks, models, and principles. 16. Clarify their origins, evolutions, and trends. 17. List key historical events, core factual statements, raw data points, and summarized statistical insights. 18. Clarify techniques, methods, approaches, protocols, and algorithms.  19. Describe contradictions and trade-offs. 20. Identify and list all major competitors (including the one being searched at present) with concise descriptions within the target market or industry segment. 21. Conduct a comprehensive competitor analysis to evaluate each competitor’s (including the one being searched at present) operational strategies, product offerings, market position, and performance metrics. 22. Perform a SWOT analysis for each competitor (including the one being searched at present), categorizing findings into strengths, weaknesses, opportunities, and threats. 23. Clarify principles, rules, constrains, limitations, vulnerabilities, challenges, obstacles, and risks. 24. Describe potential security vulnerabilities, troubleshooting methods, attack tactics, prevention methods and emergency measures. 25. Describe potential performance bottlenecks, troubleshooting methods and optimization measures. 26. Explain priorities, use cases, pitfalls, and best practices. 27. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 28. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 29. Clarify cardinality-based relationships (1:1, 1:M, M:N). 26. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 30. Describe the existing non-trivial problems and potential approaches to address them. 31. Introduce the relevant research topics of significant value that remain to be overcome. 32. Introduce the possible directions and approaches of within-domain and cross-domain innovation. 33. Predict the ultimate form of the related development. 34. Make a summary table at the end with purposes, characteristics, use cases, ect. for clarity. 35. Append the terminologies, formulas, and analogies at the end with concise descriptions for each item.

Thu Jun 12 2025

### Overview, Concepts, and Definitions

Software security is the discipline devoted to ensuring software systems remain trustworthy and robust against threats, vulnerabilities, and malicious attacks throughout their lifecycle, guaranteeing the confidentiality, integrity, and availability of data and system functions. The domain is MECE-compliant, categorizing its concerns into technical, human, procedural, and environmental aspects, with further sub-classification across elements (confidentiality, integrity, etc.), activities (control implementation, testing, maintenance), and phases (from requirements to deployment). The function of software security is to protect digital assets and users from unauthorized actions, maintain reliable operations, and ensure legal and organizational compliance.

### Key Elements, Components, Factors, and Aspects

#### 1. Core Elements

1. **Confidentiality**: Ensuring data is only accessed by authorized parties.  
2. **Integrity**: Preventing unauthorized modification of data.  
3. **Availability**: Guaranteeing access to data and functions as needed.  
4. **Authentication**: Verifying identities interacting with the software.  
5. **Authorization and Access Control**: Governing permitted actions for users and components.  
6. **Accountability and Auditing**: Tracking changes and access for assurance and forensic analysis.  
7. **Non-repudiation**: Preventing parties from denying their actions.

#### 2. Components

- **Security Requirements and Specifications**: Formal declarations of security objectives.  
- **Security Architecture and Design**: Overall structural decisions embedding security mechanisms.  
- **Controls and Mechanisms**: Cryptography, input validation, sandboxing, session management.  
- **Security Testing and Verification**: Static analysis tools, dynamic/fuzz testing, penetration tests.  
- **Security Metrics and Evaluation**: Quantitative scores for vulnerabilities and process effectiveness.

#### 3. Influencing Factors

- **Human Factors**: Developer security awareness, cognitive biases, organizational culture.  
- **Technological Factors**: Code complexity, use of third-party components, development tools.  
- **Organizational Factors**: Management prioritization, investment in security, policy enforcement.  
- **External**: Regulations, evolving threats, and market drivers.

#### 4. Aspects

- **Lifecycle Integration**: Security considerations from requirements to maintenance.  
- **Component-Based Security**: Addressing risks from integrating third-party libraries.  
- **Process and Evaluation**: Utilizing best practices, security metrics, and regular reviews.

**Analogy:** Software security mirrors the design of a fortified city. Gates (authentication) limit entry, guards (authorization) verify intentions, walls (encryption, input validation) block external threats, patrols (auditing, monitoring) detect anomalies, and policies (security requirements) establish governance. Maintenance (patching, updates) repairs weaknesses, and the city’s blueprint (architecture) ensures defenses are coherent from the ground up.

**Example:** The #gotofail bug in Apple software, caused by a small logic error, demonstrates how even a minor code flaw can jeopardize the city’s gate, allowing attackers unintended access.

### Core Evaluation Dimensions and Corresponding Metrics

1. **Vulnerability Metrics**: Counts/severity of known software vulnerabilities; exposure scores.
2. **Security Functionality Metrics**: Coverage and effectiveness of security controls.  
3. **Code/Design Metrics**: Code complexity, coupling, cohesion, static analysis alerts.  
4. **Process Metrics**: Frequency of security activities (threat modeling, reviews), training coverage.  
5. **Operational Metrics**: Incident rate, response times, runtime resilience.  
6. **Testing Metrics**: Coverage and thoroughness of security-specific tests.  
7. **Assurance/Certification**: Adherence to standards (e.g., Common Criteria), certification levels.

### Purposes and Underlying Assumptions

Software security aligns with the following purposes and assumptions:

- **Value**: Safeguarding organizational assets, data, and reputation.
- **Descriptive**: Clarifies the threat environment and the status of implemented controls.
- **Prescriptive**: Prescribes best practices, guidelines, and requirements for software teams.
- **Worldview**: Assumes an adversarial ecosystem that actively seeks to exploit weaknesses.
- **Cause-and-Effect**: Security measures -reduce-> risk of successful attack, while weak practices <-increase- vulnerabilities and breaches.

### Market Landscape, Ecosystem, Regulations, and Economic Models

The software security industry is highly competitive, featuring a range of solution providers from established IT vendors to specialized startups. The ecosystem encompasses open-source communities, SaaS/cloud providers, and aggressive competition, often driven by negative network externalities—where more widespread use of a product can attract more attackers, making coverage paradoxically lower than general software markets.

**Regulations:** Compliance mandates such as GDPR, HIPAA, ISO 27001, and others enforce security rigor and shape software lifecycle decisions. National and regional efforts (e.g., "Made in China 2025") impact geopolitics and intellectual property.

**Economic Models:** Revenue is generated via subscriptions, service contracts, licensing, cloud-based models, bug-bounty programs, and value-add analytics. Negative externalities lead to larger vendor numbers, higher prices, and less differentiation relative to traditional software markets.

### Work Mechanism and Phase-Based Lifecycle Workflow

Software security is enacted through systematic, phased embedding of security activities throughout the software development lifecycle (SDLC). The main workflow:

1. **Requirements Planning**: Elicit and specify security needs, conduct risk/threat modeling.  
2. **Architecture/Design**: Apply security principles (least privilege, defense in depth), threat modeling, selection of secure components.  
3. **Implementation**: Enforce secure coding standards, run static code analysis, peer reviews.  
4. **Testing**: Perform dynamic testing, penetration testing, coverage evaluation.
5. **Deployment**: Harden environments, disable superfluous features, validate configurations.  
6. **Maintenance and Operations**: Monitor, patch, incident response, periodic audits.

This orchestrated process reduces risks and ensures vulnerabilities are addressed proactively rather than post-factum, which is both more effective and economically efficient.

### Preconditions, Inputs, Outputs, Outcomes, and Impacts

- **Preconditions:** Awareness of threat environment, skilled teams, established policies, development toolchain readiness.
- **Inputs:** Security requirements, threat intelligence, standards, secure design patterns, and verification tools.
- **Outputs:** Secure software with embedded controls, audit trails, compliance evidence, and robust operational configurations.
- **Immediate Outcomes:** Early detection of vulnerabilities, improved compliance, and increased team awareness.
- **Long-term Impacts:** Reduction in incidents and remediation costs; enhanced trust, reputation, and competitive advantage; mature security culture.
- **Potential Implications:** Improved societal digital safety, possible increased costs, and performance trade-offs.

### Underlying Laws, Axioms, Theories, and Patterns

Software security theory is grounded in:

- **Axiomatic foundations**: Core truths for security property measurement, including Bell-LaPadula and other formal state-transition models.
- **Design Patterns**: Reusable architectural templates (e.g., authentication proxy, sandbox, taint analysis).
- **Trust Theories**: Model principal authority and system assurance.
- **Separation Principles**: Least privilege, defense in depth, and open design.
- **Reliability and Vulnerability Growth Models**: Adaptive frameworks for tracking and predicting system robustness over time.

### Design Philosophy and Architectural Features

**Philosophy:** Security is not an afterthought; it must be considered from inception and woven through all architectural and operational layers.  
**Architectural Features:**
- Layered security controls (application, control, base layers).
- Modularization, separation of concerns, and risk-driven design decisions.
- Security patterns—such as authentication proxies and wrappers—integrated into architectural blueprints.
- Architectural connectors and trust domains to mediate privilege, context, and runtime conformance.
- Use of formal modeling and automated compliance verification.

### Architectural Refactoring for Security

Refactoring strategies directly enhance security by removing architectural "bad smells," decreasing exposure, and increasing maintainability.  
Techniques and means include:

1. **Extract Method and Encapsulate Field**: Isolates sensitive logic and restricts access.
2. **Introduce Parameter Object and Replace Temp with Query**: Simplifies parameter management, clarifies data flow.
3. **Security Pattern Application**: Applying known solutions such as taint analysis, authentication proxies.
4. **Static Analysis and Automated Model Checking**: Detects refactoring opportunities and architectural violations.
5. **Search-Based and Taxonomy-Driven Approaches**: Algorithmic generation of optimal, secure refactoring solutions.

**Example:** Refactoring a model by introducing taint-style checks at architectural roots reduced code hotspots susceptible to injection attacks, demonstrating dramatic improvement by centralizing controls rather than scattering mitigations.

### Frameworks, Models, and Principles

**Major Frameworks and Models:**
- **BSIMM, OpenSAMM, NIST SSDF**: Standardized, empirical models for software security maturity.
- **Microsoft SDL and Cigital’s Touchpoints**: Workflow models specifying security activities per SDLC phase.
- **Security Evaluation Models**: Incorporating both technical metrics and human “mental models” for holistic assessments.
- **Goal-Question-Metric (GQM), SQUARE, Misuse Case Modeling**: Closing the loop between goals, questions, and evaluative measures.

**Principles:** Least privilege, economy of mechanism, complete mediation, psychological acceptability, and consistent assessment/stakeholder training undergird all models.

### Origins, Evolution, and Trends

Software security emerged as traditional defense approaches (e.g., firewalls) failed to suffice for increasingly complex, interconnected applications. The late 1990s saw focus shift to code-centric flaws like buffer overflows. Emphasis moved from “add-on” to “built-in security,” integrating security concerns throughout the lifecycle and evolving toward automated, AI-driven, and model-based practices.

Trends now reflect embedding security into agile and hybrid workflows, formalizing measurement and improvement, and expanding coverage for domains like cloud/IoT and supply-chain security.

### Key Historical Events and Statistical Insights

- 1977–1990s: First intrusions, spam, viruses, and large-scale attacks (e.g., the 1987 virus, 1995 DoD breach, late-90s buffer overflow crises).
- Major incidents: OpenSSL’s “Heartbleed” (2014), Apple’s #gotofail bug (2014), Log4j vulnerabilities (2021).
- Statistical insights: Vulnerabilities grow with software size/complexity. For example, as per CVE datasets, the number of reported vulnerabilities continues to increase annually, with notable spikes in domains like healthcare.

### Techniques, Methods, Approaches, Protocols, and Algorithms

- **Static Code Analysis**: Detects vulnerabilities before code execution.
- **Dynamic and Fuzz Testing**: Exposes runtime flaws through random and boundary inputs.
- **Threat Modeling and Risk Assessment**: Systematically anticipates attacker strategies.
- **Penetration Testing**: Simulates real-world attacks in safe environments.
- **Security Protocols**: SSL/TLS for secure communications, formal verification.
- **Cryptographic Algorithms**: AES, RSA for data confidentiality/integrity.
- **Refactoring and Secure Coding Guidelines**: Reducing attack surface and architectural weaknesses.

### Contradictions and Trade-offs

Contradictory relationships and trade-offs in software security include:

- **Security <-compromises-> Usability**: Stronger controls can impede use.
- **Security <-increases-> Complexity and Cost**: More mechanisms require more resources, affecting performance and maintenance.
- **Security <-conflicts-> Availability/Performance**: High security may reduce system performance or accessibility.
- **Security investment <-delays-> Time-to-market**: More focus on security can extend development timelines.

### Major Competitors and Market Analysis

#### Competitors

1. **Traditional Security Vendors**: Offer comprehensive cybersecurity suites (e.g., Symantec, Trend Micro).
2. **Cloud/SaaS Security Providers**: Specialize in cloud and application-specific defense (e.g., Salesforce, AWS security).
3. **Open Source Security Ecosystem**: Community tools/frameworks for open-source software.
4. **Niche/Innovative Startups**: Focus on vulnerability management, automated testing, and integration (e.g., companies supporting DevSecOps workflows).
5. **Geopolitical Players**: Regional industry initiatives (e.g., Chinese government strategies).

#### Market Position and Strategies

- **Product Offerings**: Endpoint, network, application security solutions, patch management, vulnerability assessment.
- **Operational Strategies**: Continuous R&D, aggressive pricing, and vertical integration for holistic defense.
- **Performance Metrics**: Market share, vulnerability detection rates, incident response times, compliance certifications.
- **Revenue Models**: Subscription/SaaS, licensing, bundled support, analytics add-ons, bug bounty platforms.

#### SWOT Analysis (Generalized)

| Aspect       | Strengths                                        | Weaknesses                                   | Opportunities                                           | Threats                                    |
|--------------|--------------------------------------------------|----------------------------------------------|---------------------------------------------------------|---------------------------------------------|
| Traditional  | Brand, coverage, product breadth                 | Slow to adapt, legacy architectures          | Market expansion, compliance mandates                   | Agile startups, shifting tech, new threats  |
| Cloud/SaaS   | Agile, domain expertise, integration             | Limited to domain/platform                   | Cloud growth, hybrid enterprise adoption                | Fragmented competition, vendor lock-in      |
| Open Source  | Innovation, transparency, cost                   | Resource/commercialization challenges        | Collaboration, community-driven defense                 | Funding instability, support limits         |
| Niche/Startup| Innovation, flexible, targeted                   | Scale, brand, resource constraints           | AI/ML integration, emerging application domains         | Entrenched players, market entry barriers   |
| Geopolitical | State backing, ecosystem focus                   | Restricted market, data sovereignty issues   | Regional expansion, compliance-driven mandates          | Sanctions, IP theft, political risk         |

### Principles, Rules, Constraints, Limitations, Vulnerabilities, Challenges, Obstacles, Risks

- **Principles:** Least privilege, defense in depth, open design, separation of duties, fail-safe defaults.
- **Rules:** Accountability, confidentiality, integrity, availability, assessment, error classification, auditability.
- **Constraints:** Standards compliance, architectural limitations, formal modeling requirements.
- **Limitations:** Complexity, resource constraints, lack of expertise, evolving threats.
- **Vulnerabilities:** Code flaws, misuse of dependencies, design errors, insufficient testing.
- **Challenges:** Fast-evolving threats, human factors, cost management, compliance.
- **Obstacles:** Scaling, tool integration, process adoption, legacy systems.
- **Risks:** Data breaches, loss of intellectual property, operational disruptions, reputational harm.

### Security Vulnerabilities, Troubleshooting, Prevention, and Emergency Response

- **Vulnerabilities:** Buffer overflows, injection, privilege escalation, misconfigurations.
- **Troubleshooting:** Static/dynamic analysis, formal verification, penetration testing.
- **Prevention:** Secure coding, architectural tactics, automated scanning, refactoring, patch management.
- **Attack Tactics:** Exploiting code flaws, phishing, malware embedding, social engineering.
- **Emergency Measures:** Incident response teams, incident containment, audit trails, recovery protocols.

### Performance Bottlenecks, Troubleshooting, and Optimization

- **Bottlenecks:** Encryption overhead, synchronization delays, I/O load, network latency.
- **Troubleshooting:** Profiling, dependency graph analysis, bottleneck detection tools.
- **Optimization:** Architectural refactoring, hardware offloading, concurrency, batching, efficient cryptography.

### Priorities, Use Cases, Pitfalls, and Best Practices

- **Priorities:** CIA triad, authentication, authorization, accountability, and risk-based focus.
- **Use Cases:** Secure software for finance, healthcare, IoT, critical infrastructure.
- **Pitfalls:** Late-stage security, overcomplication, neglecting human factors, incomplete testing.
- **Best Practices:** Whole-life-cycle security, metrics-driven assessment, continuous training, incident preparedness.

### Cause-and-Effect Relationships

- **Cause-and-Effect Examples:**  
  - Vulnerabilities <-caused by- Software flaws  
  - Exploitation -leads to-> Security breach  
  - Poor practices <-result in- Increased risk  
  - Security controls <-mitigate- Threat impact

### Interdependency Relationships

- **Examples:**  
  - Components <-interact with-> Security policies  
  - User security decisions <-affect-> Vulnerability exposure  
  - Policies -govern-> Process/investment  
  - Managed service providers -alter-> Risk dependencies

### Cardinality-Based Relationships

- **1:1**: Each user has one authentication token.  
- **1:M**: A user with multiple roles/privileges or one application accessing multiple resources.
- **M:N**: Multiple users can access multiple shared data objects, complicating access controls.

### Contradictory Relationships

- **Examples:**  
  - Security -conflicts-> Usability  
  - Security -compromises-> Performance  
  - Availability <-compromised by-> Confidentiality

### Existing Non-Trivial Problems and Solutions

- **Problems:** Incomplete verification, evolving attack strategies, integrating formal methods, human error, and scaling secure designs.
- **Approaches:** Multi-layered V&V, AI/ML-based detection, training, model-driven security, human-centred process design.

### Emerging Research Topics and Innovation Directions

#### Open Problems

1. Real-time analysis and response to new threats.
2. Seamless security in agile/DevOps environments.
3. Automation and formal verification at scale.
4. Advanced metrics and empirical efficacy evaluation.
5. Human and organizational process interactions.

#### Directions

1. **Within-Domain:** AI-augmented testing, model-driven security, supply chain integrity enhancements.
2. **Cross-Domain:** Blockchain-based trust, cross-domain access control, SDN security, unified policy enforcement for cyber-physical systems.
3. **Ultimate Vision:** Fully integrated, continuously automated security assurance, lifecycle-embedded, AI-powered, with adaptive defenses spanning from source to operation.

---

### SUMMARY TABLE: Purposes, Characteristics, Use Cases, and More

| Category                  | Details                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------|
| Purposes                  | Protect confidentiality, integrity, availability; safeguard assets and trust             |
| Characteristics           | Lifecycle-spanning, adaptive, multi-dimensional, evidence-driven                         |
| Use Cases                 | Secure financial/healthcare/IoT systems, compliance, risk-driven development            |
| Market/Ecosystem          | Competitive vendors (legacy, cloud, open source, startups), regulated, diversified models|
| Core Elements             | Confidentiality, integrity, availability, authentication, authorization, auditing        |
| Evaluation Dimensions     | Vulnerability exposure, metrics, control coverage, operational resilience                |
| Best Practices            | Early integration, threat modeling, continuous testing/monitoring, secure coding         |
| Key Principles            | Least privilege, defense in depth, compartmentalization, open design                     |
| Frameworks/Models         | BSIMM, OpenSAMM, Microsoft SDL, NIST SSDF, misuse cases, SQUARE                         |
| Techniques                | Static/dynamic analysis, threat modeling, refactoring, formal verification, cryptography |
| Contradictions/Trade-offs | Security vs usability/performance/cost, CIA triad balance                               |
| Research Trends           | AI/ML-augmented security, supply chain trust, agile security, blockchain for assurance   |

---

### GLOSSARY: Key Terminologies, Formulas, and Analogies

| Item            | Description                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| Confidentiality | Restricting data access to authorized parties.                                              |
| Integrity       | Preventing unauthorized data modification.                                                  |
| Availability    | Ensuring services/data are accessible when needed.                                          |
| Authentication  | Verifying identity before granting access.                                                          |
| Authorization   | Governing what authenticated entities can do.                                                       |
| Security Kernel | Core component enforcing security policies.                                                         |
| Threat Modeling | Systematic identification of threats during design.                                         |
| Static Analysis | Code examination without execution for vulnerabilities.                                             |
| Dynamic Testing | Runtime software testing for flaws under real conditions.                                   |
| Security Metrics| Quantitative measurements of security posture (e.g., vulnerability counts, control coverage).  |
| Formula: Risk   | \\( \text{Risk} = \text{Probability} \times \text{Impact} \\).                                        |
| Bell-LaPadula   | Formal model enforcing "no read up, no write down" for classified systems.                         |
| Analogy: Castle | Software is a fortress: gates (authentication), guards (authorization), walls (encryption/validation). |
| Analogy: Public Health | Security akin to preventive medicine—proactive, continuous, holistic.                     |

---

This comprehensive, MECE-compliant framework provides an expert-level, logically classified, analogy-rich analysis of software security, from core principles through industry practice, market dynamics, and emerging research frontiers, enabling organizations, engineers, and researchers to design, evaluate, and evolve trustworthy software systems.

Bibliography
A Abbas, IF Siddiqui, SUJ Lee, & AK Bashir. (2017). Binary pattern for nested cardinality constraints for software product line of IoT-based feature models. In IEEE Access. https://ieeexplore.ieee.org/abstract/document/7875079/

A Almogahed, M Omar, & NH Zakaria. (2022). Refactoring codes to improve software security requirements. In Procedia Computer Science. https://www.sciencedirect.com/science/article/pii/S1877050922007517

A Arabsorkhi & F Ghaffari. (2018). Security metrics: principles and security assessment methods. https://ieeexplore.ieee.org/abstract/document/8661030/

A. Georges, D. Buytaert, L. Eeckhout, & K. D. Bosschere. (2004). Spotting Java Performance Bottlenecks. https://www.semanticscholar.org/paper/3a8686adc33459b519799ceb41ad67a5defb92f9

A. Gueye, C. Galhardo, Irena Bojanova, & Irena Bojanova. (2023). Critical Software Security Weaknesses. In IT Professional. https://www.semanticscholar.org/paper/f6fbb2c2e03e2492b2ec6e3f9408eabe7f664884

A Kazemi, MK Golkar, & S Lajmiri. (2023). Origins of cyber security. https://www.sid.ir/fileserver/je/39851-280585-x-1143805.pdf

A Khalid, M Raza, P Afsar, & RA Khan. (2025). A SWOT Analysis of Software Development Life Cycle Security Metrics. https://onlinelibrary.wiley.com/doi/abs/10.1002/smr.2744

A Laszka, M Felegyhazi, & L Buttyán. (2014). A survey of interdependent information security games. In ACM Computing Surveys (CSUR). https://dl.acm.org/doi/abs/10.1145/2635673

A Ojala. (2016). Adjusting software revenue and pricing strategies in the era of cloud computing. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S0164121216301546

A. Polikoff, Elizabeth Lassar, & john a. powell. (2020). Cause and Effect. In A Brief History of the Subordination of African Americans in the U.S. https://www.semanticscholar.org/paper/0a7b0e1c2bbb60689ef54a6a372876735aca28c6

A. Rastogi & K. Nygard. (2019). Software Engineering Principles and Security Vulnerabilities. In International Conference on Computers and Their Applications. https://easychair.org/publications/paper/nT1J

A Sharma & PK Misra. (2017). Aspects of enhancing security in software development life cycle. https://www.researchgate.net/profile/Anuradha-Misra-3/publication/349945170_Aspects_of_Enhancing_Security_in_Software_Development_Life_Cycle/links/604873674585154e8c8ae28c/Aspects-of-Enhancing-Security-in-Software-Development-Life-Cycle.pdf

A. Steingruebl & G. Peterson. (2009). Software Assumptions Lead to Preventable Errors. In IEEE Security & Privacy. https://www.semanticscholar.org/paper/a318262a26234c743424115cf957228bc66a5740

A. Yasar, Davy Preuveneers, Yolanda Berbers, & Ghasan Bhatti. (2008). Best practices for software security: An overview. In 2008 IEEE International Multitopic Conference. https://ieeexplore.ieee.org/document/4777730/

Abdullah Almogahed, Mazni Omar, Nur Haryani Zakaria, & Abdulwadood Alawadhi. (2022). Software Security Measurements: A Survey. In 2022 International Conference on Intelligent Technology, System and Service for Internet of Everything (ITSS-IoE). https://ieeexplore.ieee.org/document/9990968/

Adeel Jameel & A. Yasar. (n.d.). Best Practices for Software Security. https://www.semanticscholar.org/paper/0c19545bcc0380d49a96b1fb324d75f8ba3420ff

AJA Wang. (2005). Information security models and metrics. https://dl.acm.org/doi/abs/10.1145/1167253.1167295

AK Alvi & M Zulkernine. (2021). A security pattern detection framework for building more secure software. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S0164121220302296

Ali M Al Mousa, Mohammad Al Qomri, Salman Al Hajri, Rachid Zagrouba, & Sghaier Chaabani. (2020). Environment Based IoT Security Risks and Vulnerabilities Management. In 2020 International Conference on Computing and Information Technology (ICCIT-1441). https://ieeexplore.ieee.org/document/9213813/

Amund Bauck Sole. (2016). Analogies of Information Security. https://www.semanticscholar.org/paper/642394d8e649cfee4cc363ab375bd969760867f3

AN Duc, R Jabangwe, & P Paul. (2017). Security challenges in IoT development: a software engineering perspective. https://dl.acm.org/doi/abs/10.1145/3120459.3120471

Ao Ding, Gaolei Li, Xiaoyu Yi, Xi Lin, Jianhua Li, & Chaofeng Zhang. (2024). Generative AI for Software Security Analysis: Fundamentals, Applications, and Challenges. In IEEE Software. https://ieeexplore.ieee.org/document/10634314/

Arina Kudriavtseva. (2024). A Software Security Evaluation Framework. In 2024 IEEE/ACM 46th International Conference on Software Engineering: Companion Proceedings (ICSE-Companion). https://www.semanticscholar.org/paper/65899cd6ae4229eebc8f2458b76b01710e103567

ASRC Murthy, M Sravani, & G Ruthmani. (2024). An In-Depth Analysis of Contemporary Security Breaches using Time Series Analysis. https://www.atlantis-press.com/proceedings/icciet-24/126002023

Asunur Cezar, Huseyin Cavusoglu, & Srinivasan Raghunathan. (2017). Sourcing Information Security Operations: The Role of Risk Interdependency and Competitive Externality in Outsourcing Decisions. In Production and Operations Management. https://www.semanticscholar.org/paper/9eefcb29f80d1dfe0ae747cbe205dd589f9b3eff

B. Bhargava. (2017). Blockhub: Blockchain-based Secure Cross-domain Software Development and Sharing System. https://www.semanticscholar.org/paper/a18d7f9910f849f22c70f0ba440f1541263521bb

B Coat. (n.d.). No Other Security Vendor Comes Close. https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=89820a0af030014e0e55dc16b2421d2915a29000

B Naqvi & A Seffah. (2019). Interdependencies, conflicts and trade-offs between security and usability: why and how should we engineer them? https://link.springer.com/chapter/10.1007/978-3-030-22351-9_21

B. Preneel. (2015). Software Security: Squaring the Circle? In 2015 IEEE/ACM 1st International Workshop on Software Protection. https://www.semanticscholar.org/paper/4cd1ced7f6e1302ce1fa849322f092d747b55818

B Schneier. (1999). Security in the real world: How to evaluate security technology. In Computer security journal. https://artofhacking.com/tucops3/hack/general/real-wrl.pdf

Babagana Ali Dapshima & Samaila Kasimu Ahmad. (2024). Evaluation and Assessment of Software Security Risks and Vulnerabilities Within the Realm of Secure DevOps. In International Journal For Multidisciplinary Research. https://www.semanticscholar.org/paper/9ff70068eb25f9505363133706deee1319a44540

Buzhen He, Tao Feng, Chunyan Liu, & Chunhua Su. (2025). CD-BISHAC: Cross-Domain Scheme for Blockchain-Based Industrial Internet of Things Security Hybrid Access Control. In IEEE Internet of Things Journal. https://ieeexplore.ieee.org/document/10745559/

C Abid. (2021). Explainable, Security-Aware and Dependency-Aware Framework for Intelligent Software Refactoring. https://deepblue.lib.umich.edu/handle/2027.42/171082

C Abid, M Kessentini, & V Alizadeh. (2020). How does refactoring impact security when improving quality? a security-aware refactoring approach. https://ieeexplore.ieee.org/abstract/document/9130035/

C. Banerjee & S. Pandey. (2009). Software Security Rules, SDLC Perspective. In ArXiv. https://www.semanticscholar.org/paper/a6b881a8c137bcb0d0ffddffa5bcfbe1d8e33415

C Paradis, R Kazman, & M Konrad. (2024). A socio-technical perspective on software vulnerabilities: A causal analysis. In Information and Software Technology. https://www.sciencedirect.com/science/article/pii/S0950584924001587

C Schmittner, T Gruber, & P Puschner. (2014). Security application of failure mode and effect analysis (FMEA). https://link.springer.com/chapter/10.1007/978-3-319-10506-2_21

C Weir, I Becker, J Noble, & L Blair. (2020). Interventions for long‐term software security: Creating a lightweight program of assurance techniques for developers. https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.2774

CB Haley, RC Laney, JD Moffett, & B Nuseibeh. (2006). Using trust assumptions with security requirements. In Requirements Engineering. https://link.springer.com/article/10.1007/s00766-005-0023-4

Chandramohan Muniraman. (2007). A PRACTICAL APPROACH TO INCLUDE SECURITY IN SOFTWARE DEVELOPMENT. https://iacis.org/iis/2007/Muniraman_Damodaran.pdf

Cheng Xuan. (2009). Research on Software Security Testing Methods. In Computer Knowledge and Technology. https://www.semanticscholar.org/paper/d01516da900e4e7ec19d5ecdf497678c7d28242a

Christian Schmitt & P. Liggesmeyer. (2014). Implications of the Operational Environmental on Software Security Requirements Engineering. In Security in Information Systems. https://www.scitepress.org/Link.aspx?doi=10.5220/0004966400630074

D Barrera, C Bellman, & P Van Oorschot. (2023). Security best practices: a critical analysis using IoT as a case study. https://dl.acm.org/doi/abs/10.1145/3563392

D. Firesmith. (2003). Security Use Cases. In J. Object Technol. https://www.jot.fm/contents/issue_2003_05/column6.html

D Guru, S Perumal, & V Varadarajan. (2079). Approaches towards Blockchain Innovation: A Survey and Future Directions. https://pdfs.semanticscholar.org/1fb2/0bca0281691a755ad03e24ef8a56927e5278.pdf

D Lazar, H Chen, X Wang, & N Zeldovich. (2014). Why does cryptographic software fail? A case study and open problems. https://dl.acm.org/doi/abs/10.1145/2637166.2637237

D Van Landuyt & W Joosen. (2022). A descriptive study of assumptions in STRIDE security threat modeling. In Software and Systems Modeling. https://link.springer.com/article/10.1007/s10270-021-00941-7

Daniel Owens SystemSecurities. (2009). Integrating Software Security Into The Software Development Lifecycle. https://www.semanticscholar.org/paper/80d44628f66859253082c591641bf477710f98f6

David Byers & N. Shahmehri. (2007). Design of a Process for Software Security. In The Second International Conference on Availability, Reliability and Security (ARES’07). https://www.semanticscholar.org/paper/4b6d7189e7f1ca3a17911c6c00613ebf6ee4e1a6

Debabrata Dey, Atanu Lahiri, & Guoying Zhang. (2011). Network Effects in the Security Software Market ∗. https://www.semanticscholar.org/paper/4f88f95f99cca784c0ed343f7d5e32bc72fc921f

Debabrata Dey, Atanu Lahiri, & Guoying Zhang. (2013). Quality Competition in the Security Software Market. In 2013 46th Hawaii International Conference on System Sciences. https://www.semanticscholar.org/paper/0a285c8ea0b6ed8b71fc297307f196f84c5fa300

Debabrata Dey, Michael G. Foster, & Guoying Zhang. (2011). Impact of Network Externality in the Security Software Market. https://www.semanticscholar.org/paper/17456d296c10475d9be7c99671657b4111cba954

Diego Rossi, Lucas Bressan, Fernanda Campos, A. Oliveira, & Victor Ströele. (2023). Educational Software and Security Vulnerabilities: an experimental study. In Anais do XXXIV Simpósio Brasileiro de Informática na Educação (SBIE 2023). https://www.semanticscholar.org/paper/1cd99599413929bd2e588f4d1802f9f17f1e09e3

DJ Betz & T Stevens. (2013). Analogical reasoning and cyber security. In Security Dialogue. https://journals.sagepub.com/doi/abs/10.1177/0967010613478323

DP Gilliam, TL Wolfe, & JS Sherif. (2003). Software security checklist for the software life cycle. https://ieeexplore.ieee.org/abstract/document/1231415/

Dr. Kamalakannan Machap & Abulla Muaza. (2021). Use of network and cyber security tools to counter the security obstacles. https://www.semanticscholar.org/paper/3705a93ce6fac68119315ac35fbc12962c9f3dc9

E Edward, AS Nyamawe, & N Elisa. (2024). A Survey on Secure Refactoring. In SN Computer Science. https://link.springer.com/article/10.1007/s42979-024-03325-y

EB Fernandez. (2004). A Methodology for Secure Software Design. In Software Engineering Research and Practice. http://masters.donntu.ru/2009/fvti/ugnichenko/library/EFLVSecSysDes1.pdf

E.J. Oyitso & E.D. Ordia. (2023). Best Practices to Implement and Pitfalls to Avoid in Cloud Application Security. In Advances in Multidisciplinary and scientific Research Journal Publication. https://www.semanticscholar.org/paper/43e3d943ac11b816ff61e7158216fcf03491f6da

Eric Amankwa, Marianne Loock, & E. Kritzinger. (2014). A conceptual analysis of information security education, information security training and information security awareness definitions. In The 9th International Conference for Internet Technology and Secured Transactions (ICITST-2014). https://ieeexplore.ieee.org/document/7038814/

F Basholli, R Mezini, & A Basholli. (2023). Security in the components of information systems. https://www.researchgate.net/profile/Fatmir-Basholli/publication/373076912_Security_in_the_components_of_information_systems/links/64d7647d25837316ee08bec8/Security-in-the-components-of-information-systems.pdf

F Piessens, B De Decker, & B De Win. (2001). Developing Secure Software: A survey and classification of common software vulnerabilities. https://link.springer.com/chapter/10.1007/978-0-387-35583-2_2

F Ponce, J Soldani, H Astudillo, & A Brogi. (2022). Smells and refactorings for microservices security: A multivocal literature review. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S016412122200111X

Fangzhen Lin. (2000). From Causal Theories to Successor State Axioms and STRIPS-Like Systems. In AAAI/IAAI. https://www.semanticscholar.org/paper/54a0edfc2e4a982b7e4e59c76e5403927bb66dae

Fridah C. Korir. (2023). Software security models and frameworks: an overview and current trends. In World Journal of Advanced Engineering Technology and Sciences. https://wjaets.com/content/software-security-models-and-frameworks-overview-and-current-trends

G Ammons, JD Choi, M Gupta, & N Swamy. (2004). Finding and removing performance bottlenecks in large systems. https://link.springer.com/chapter/10.1007/978-3-540-24851-4_8

G Canbek. (2018). Cyber security by a new analogy:“the allegory of the 'mobile’cave.” In Journal of Applied Security Research. https://www.tandfonline.com/doi/abs/10.1080/19361610.2018.1387838

G Hatzivasilis, I Papaefstathiou, & C Manifavas. (2016). Software security, privacy, and dependability: Metrics and measurement. In IEEE Software. https://ieeexplore.ieee.org/abstract/document/7436657/

G. McGraw. (1999). Software Assurence for Security. In Computer. https://www.semanticscholar.org/paper/55daee2359aad4e5febd4b848c4523778b9cebe3

G McGraw. (2004). Software security. In IEEE Security & Privacy. https://ieeexplore.ieee.org/abstract/document/1281254/

G. McGraw. (2006). Software Security: Building Security In. In 2006 17th International Symposium on Software Reliability Engineering. https://ieeexplore.ieee.org/document/4021964/

G. McGraw. (2017). Six Tech Trends Impacting Software Security. In Computer. https://www.semanticscholar.org/paper/4165dee56425d3e720fef6ebec465858107e1916

G Sindre & AL Opdahl. (2005). Eliciting security requirements with misuse cases. In Requirements engineering. https://link.springer.com/article/10.1007/s00766-004-0194-4

Gayatri Vijiyan. (2015). Current Trends in Software Engineering Research. https://www.semanticscholar.org/paper/111c8772c83a7a19f201f6dcf3a61b5a6304cb77

Golriz Chehrazi. (2013). Economic impact of software security activities in software development. In 2013 International Conference on Risks and Security of Internet and Systems (CRiSIS). https://www.semanticscholar.org/paper/afc16d58b1fcdb2ae8063ef489efa6aa327b27a4

Gu Tian-yang. (2008). Software security testing methods and tools. In Computer Engineering and Design. https://www.semanticscholar.org/paper/2a6265fb8326f067d40c5fa233dea7653046fbdc

H Assal. (2018). The human dimension of software security and factors affecting security processes. https://carleton.scholaris.ca/items/b2ddd87d-4d7c-411c-93cb-1f4c4af3c864/full

H Assal & S Chiasson. (2018). Security in the software development lifecycle. https://www.usenix.org/conference/soups2018/presentation/assal

H Cavusoglu & B Mishra. (2004). The effect of internet security breach announcements on market value: Capital market reactions for breached firms and internet security developers. https://www.tandfonline.com/doi/abs/10.1080/10864415.2004.11044320

H Chen & MA Babar. (2024). Security for machine learning-based software systems: A survey of threats, practices, and challenges. In ACM Computing Surveys. https://dl.acm.org/doi/abs/10.1145/3638531

H Fryer. (2016). The public health analogy in web security. https://eprints.soton.ac.uk/412399/

H Mohaddes Deylami, I Ardekani, & RC Muniyandi. (2015). Effects of software security on software development life cycle and related security issues. https://www.researchgate.net/profile/Hanif_Deylami/publication/344221556_Effects_of_Software_Security_on_Software_Development_Life_Cycle_and_Related_Security_Issues/links/5f5d5f6aa6fdcc11640ed685/Effects-of-Software-Security-on-Software-Development-Life-Cycle-and-Related-Security-Issues.pdf

H Mumtaz. (2016). Software security improvement through the application of UML model refactoring. https://search.proquest.com/openview/c1709b029da87ce104a7bb1a00875398/1?pq-origsite=gscholar&cbl=18750&diss=y

H Mumtaz, M Alshayeb, S Mahmood, & M Niazi. (2018). An empirical study to improve software security through the application of code refactoring. https://www.sciencedirect.com/science/article/pii/S0950584916303664

H Saeed, I Shafi, J Ahmad, & AA Khan. (2025). Review of Techniques for Integrating Security in Software Development Lifecycle. https://search.ebscohost.com/login.aspx?direct=true&profile=ehost&scope=site&authtype=crawler&jrnl=15462218&AN=182195837&h=hVTz3%2BkHVZoHn6W4RMTUUW7%2F3Mp%2BEYKIVtkUGl8mEzMNcjvgQ63ayX95vAhsGsFekkJf9DXIrCl%2F8k0TqmnFsA%3D%3D&crl=c

H Shahriar & M Zulkernine. (2012). Mitigating program security vulnerabilities: Approaches and challenges. In ACM Computing Surveys (CSUR). https://dl.acm.org/doi/abs/10.1145/2187671.2187673

Hao Tu, Weiming Li, Dong Li, & Junqing Yu. (2014). A scalable flow rule translation implementation for software defined security. In The 16th Asia-Pacific Network Operations and Management Symposium. https://ieeexplore.ieee.org/document/6996571/

Harold F. Tipton & Steven Hernandez. (2012). Software Development Security. https://www.semanticscholar.org/paper/da82b7b3448b3bbf4fb3f38eefd57ebf251db4d0

HB Christensen, KM Hansen, & M Kyng. (2014). Analysis and design of software ecosystem architectures–Towards the 4S telemedicine ecosystem. https://www.sciencedirect.com/science/article/pii/S0950584914001050

I Ryan, U Roedig, & KJ Stol. (2023). Unhelpful assumptions in software security research. https://dl.acm.org/doi/abs/10.1145/3576915.3623122

Isaac Chin Eian, L. Yong, M. Li, Noor Affan Bin Noor Hasmaddi, & Fatima-tuz-Zahra. (2020). Integration of Security Modules in Software Development Lifecycle Phases. In ArXiv. https://www.semanticscholar.org/paper/db74951d36db015c1baa1698bc7e3a617b3f63fa

J McLean. (1990). The specification and modeling of computer security. In Computer. https://ieeexplore.ieee.org/abstract/document/48795/

J. Ren, R. Taylor, Paul Dourish, & D. Redmiles. (2005). Towards an architectural treatment of software security. In ACM SIGSOFT Software Engineering Notes. https://www.semanticscholar.org/paper/91a750cc5b405b52847154743d9a417312dd7a24

J. Ryoo, R. Kazman, & Priya Anand. (2015). Architectural Analysis for Security. In IEEE Security & Privacy. https://ieeexplore.ieee.org/document/7349074/

J Vanegue, S Heelan, & R Rolles. (2012). SMT Solvers in Software Security. In WOOT. https://www.usenix.org/conference/woot12/workshop-program/presentation/vanegue

J. Viega. (2020). 20 Years of Software Security. In Computer. https://www.semanticscholar.org/paper/ef4b378ab67b5bee68110b4c515aaed06da83dcf

J Walden. (2020). The impact of a major security event on an open source project: The case of OpenSSL. https://dl.acm.org/doi/abs/10.1145/3379597.3387465

JA Saad. (2024). Overcoming Obstacles in Model-Driven Engineering: Lessons from the Software Industry. http://103.81.70.85/handle/11348/975

James Ransome & A. Misra. (2013). Core Software Security: Security at the Source. https://www.semanticscholar.org/paper/2890346405320f93f1d527cbd9a4fe402cece12a

JEJ Tevis & JA Hamilton. (2004). Methods for the prevention, detection and removal of software security vulnerabilities. https://dl.acm.org/doi/abs/10.1145/986537.986583

Jetzabel M. Serna, Jesus Luna, Roberto Morales, & Manuel Medina. (2012). Analyzing the Trade-Offs Between Security and Performance in VANETs. https://www.semanticscholar.org/paper/289c74422058edb90f665b26380675d4d7e3549f

Jiang Zhao-hua. (2007). SWOT Analysis of Irish Software Industry. In Science Technology and Industry. https://www.semanticscholar.org/paper/c2c2579fe1be2c3b2eded26f9779b0f1dc5679e3

Jing Xiao-qing. (2005). Security principals of software system design. https://www.semanticscholar.org/paper/d9cc898f7155ce6ba85bbd4fcf64eb3383564b97

Jonathan Sönnerup & Martin Hell. (2018). Evaluating Security of Software Through Vulnerability Metrics. https://www.semanticscholar.org/paper/36130c2d95d0efa76197ce81421f3e38f081b27e

Jongmo Sohn. (2024). Analysis on Software Supply Chain Security Standards. In Society for Standards Certification and Safety. https://scholar.kyobobook.co.kr/article/detail/4050070277826

K. Bagchi & G. Udo. (2003). An Analysis of the Growth of Computer and Internet Security Breaches. In Commun. Assoc. Inf. Syst. https://www.semanticscholar.org/paper/410b1f9d8d8e7ee01d289819dc0f91d187c64502

K. Hawkey, Kasia Muldner, & K. Beznosov. (2008). Balancing IT Security Management Model Trade-Offs. https://www.semanticscholar.org/paper/0db680b770420453399a2d20797bf7919bcb5021

K Petersen & C Gencel. (2013). Worldviews, research methods, and their relationship to validity in empirical software engineering research. https://ieeexplore.ieee.org/abstract/document/6693226/

K. Rahouma. (2017). REVIEWING AND APPLYING SECURITY SERVICES WITH NON-ENGLISH LETTER CODING TO SECURE SOFTWARE APPLICATIONS IN LIGHT OF SOFTWARE TRADE-OFFS. https://www.semanticscholar.org/paper/00279ebdb9b894c16d9fe2f449a51a8974d87580

Kajal Kosarkar. (2024). Fortifying Software Security: Strategies, Implementation, and Challenges. In International Journal for Research in Applied Science and Engineering Technology. https://www.semanticscholar.org/paper/6e50e35eef69d839caa77512dac3bbbc0907e285

Khalid Albulayhi, Predrag T. Tosic, & Frederick T. Sheldon. (2020). G-Model: A Novel Approach to Privacy-Preserving 1:M Microdata Publication. In 2020 7th IEEE International Conference on Cyber Security and Cloud Computing (CSCloud)/2020 6th IEEE International Conference on Edge Computing and Scalable Cloud (EdgeCom). https://ieeexplore.ieee.org/document/9170992/

L. Williams. (2013). On the Use of Software Metrics as a Predictor of Software Security Problems. https://www.semanticscholar.org/paper/da20d6b1a2c17624caad9695872aeace19890d6f

L Williams, G McGraw, & S Migues. (2018). Engineering security vulnerability prevention, detection, and response. In IEEE Software. https://ieeexplore.ieee.org/abstract/document/8409917/

M Alenezi & M Akour. (2025). AI-Driven Innovations in Software Engineering: A Review of Current Practices and Future Directions. In Applied Sciences. https://www.mdpi.com/2076-3417/15/3/1344

M Böhme, E Bodden, T Bultan, C Cadar, & Y Liu. (2024). Software Security Analysis in 2030 and Beyond: A Research Roadmap. https://dl.acm.org/doi/abs/10.1145/3708533

M Ezhei & B Tork Ladani. (2020). Interdependency analysis in security investment against strategic attacks. In Information Systems Frontiers. https://link.springer.com/article/10.1007/s10796-018-9845-8

M. Felderer, Basel Katt, P. Kalb, J. Jürjens, Martín Ochoa, F. Paci, L. M. Tran, T. Tun, Koen Yskout, R. Scandariato, Frank Piessens, Dries Vanoverberghe, Elizabeta Fourneret, M. Gander, Bjørnar Solhaug, & R. Breu. (2014). Evolution of Security Engineering Artifacts: A State of the Art Survey. In Int. J. Secur. Softw. Eng. https://www.semanticscholar.org/paper/8dfcaf52147b34dcac647743e217d95821de3b02

M Felderer, M Büchler, M Johns, & AD Brucker. (2016). Security testing: A survey. https://www.sciencedirect.com/science/article/pii/S0065245815000649

M Humayun & N Jhanjhi. (2022). Security threat and vulnerability assessment and measurement in secure software development. https://pdfs.semanticscholar.org/dda3/60c9a7fbdd2defdc5e2c80d489444347b609.pdf

M. Jaatun. (2017). Risk in the Age of Software Security. https://www.semanticscholar.org/paper/df108ec65abe46e9c8c7a79185172f3c027297d5

M. Lewis. (2008). EHRs: Top EHR vendors evaluated by IT research firm. In InfoTech Bulletin. https://www.semanticscholar.org/paper/d744e19ecc8582f27a76942746b59ca84c22157b

M. Lewis. (2010). Research firm ranks medical IT software vendors. In Medical economics. https://www.semanticscholar.org/paper/43403bba156b2a82cff86050f511933e89e2b6b3

M Linares-Vasquez, C Vendome, & Q Luo. (2015). How developers detect and fix performance bottlenecks in android apps. https://ieeexplore.ieee.org/abstract/document/7332486/

M Magas & D Kiritsis. (2022). Industry Commons: an ecosystem approach to horizontal enablers for sustainable cross-domain industrial innovation (a positioning paper). In International Journal of Production Research. https://www.tandfonline.com/doi/abs/10.1080/00207543.2021.1989514

M Mirakhorli, M Galster, & L Williams. (2020). Understanding software security from design to deployment. https://dl.acm.org/doi/abs/10.1145/3385678.3385687

M Otieno, D Odera, & JE Ounza. (2023). Theory and practice in secure software development lifecycle: A comprehensive survey. https://www.researchgate.net/profile/David-Odera-2/publication/370838016_Theory_and_Practice_in_Secure_Software_Development_Lifecycle_A_Comprehensive_Survey/links/64f0780fb55e1d34158cfae2/Theory-and-Practice-in-Secure-Software-Development-Lifecycle-A-Comprehensive-Survey.pdf

M. Povey. (2014). Apple’s #gotofail, yet more examples of why you can’t rely on the security of closed source software. https://www.semanticscholar.org/paper/101746530d1e336b1daaff116030aaa5908a69fb

M. Ramachandran. (2011). Software Security Engineering: Design and Applications. https://www.semanticscholar.org/paper/b97fd079d2b6b5a042d4c572bf2bd60c9bfce1b8

M Siavvas, D Kehagias, D Tzovaras, & E Gelenbe. (2021). A hierarchical model for quantifying software security based on static analysis alerts and software metrics. In Software Quality Journal. https://link.springer.com/article/10.1007/s11219-021-09555-0

M Silic & A Back. (2014). Information security: Critical review and future directions for research. In Information Management & Computer Security. https://www.emerald.com/insight/content/doi/10.1108/IMCS-05-2013-0041/full/html

M Siponen. (2002). Towards maturity of information security maturity criteria: six lessons learned from software maturity criteria. In Information Management & Computer Security. https://www.emerald.com/insight/content/doi/10.1108/09685220210446560/full/html

Mahzabin Tamanna, Joseph D Stephens, & Mohd Anwar. (2024). Security Implications of User Non-compliance Behavior to Software Updates: A Risk Assessment Study. In ArXiv. https://arxiv.org/abs/2411.06262

Masashi Ono. (2014). Service science in top IT vendors. In 2014 11th International Conference on Service Systems and Service Management (ICSSSM). https://www.semanticscholar.org/paper/c20d6470e3cfb6a1a3f299a6afd29c6822052220

Megha M. Moncy, Sadia Afreen, & S. Purkayastha. (2023). Healthcare Security Breaches in the United States: Insights and their Socio-Technical Implications. In ArXiv. https://www.semanticscholar.org/paper/c78ed57dcddf496a251cfa0c721d6395ea645bdf

Mercedes de la Camara, Fco Javier Saenz, J. Calvo-Manzano, & M. Arcilla. (2015). Security by design factors for developing and evaluating secure software. In 2015 10th Iberian Conference on Information Systems and Technologies (CISTI). https://ieeexplore.ieee.org/document/7170500/

MN Anwar Mohammad, M Nazir, & K Mustafa. (2019). A systematic review and analytical evaluation of security requirements engineering approaches. https://link.springer.com/article/10.1007/s13369-019-04067-3

Mohammed Abdulqawi Saleh Al-humaikani & L. A. Rahim. (2019). A Review on the Verification Approaches and Tools used to Verify the Correctness of Security Algorithms and Protocols. In International Journal of Advanced Computer Science and Applications. https://www.semanticscholar.org/paper/ae411eec19245ffeafcafdbe874515bcfa08a515

MR Tabassum, MS Siddik, & M Shoyaib. (2014). Determining interdependency among non-functional requirements to reduce conflict. https://ieeexplore.ieee.org/abstract/document/6850720/

Muhammad Ali Babar. (2024). Evidence-Based Research for Supporting Software Security in Software Development: Methodological Challenges & Strategies. In Proceedings of the 28th International Conference on Evaluation and Assessment in Software Engineering. https://www.semanticscholar.org/paper/cf00cd3194304b8d75987d1ea09c17b2e746320a

Muhammad Hasib Aslam & Ali Afzal Malik. (2024). Exploring the Impact of Software Security Best Practices. In 2024 International Conference on Frontiers of Information Technology (FIT). https://www.semanticscholar.org/paper/452fc2baad6f1413c10b96e82ca776ffabcc7519

N Dissanayake, A Jayatilaka, & M Zahedi. (2022). Software security patch management-A systematic literature review of challenges, approaches, tools and practices. https://www.sciencedirect.com/science/article/pii/S0950584921002147

N Feng, HJ Wang, & M Li. (2014). A security risk analysis model for information systems: Causal relationships of risk factors and vulnerability propagation analysis. In Information sciences. https://www.sciencedirect.com/science/article/pii/S0020025513001539

N. Medeiros, N. Ivaki, Pedro Costa, & M. Vieira. (2017). Software Metrics as Indicators of Security Vulnerabilities. In 2017 IEEE 28th International Symposium on Software Reliability Engineering (ISSRE). https://ieeexplore.ieee.org/document/8109088/

Nabil M.Mohammed. (2016). Exploring software security approaches and their limitations in SDLC. https://www.semanticscholar.org/paper/0b7dd23174016889f7dee2c3e6a725e93c3cbc0c

Nagaraju Thallapally. (2021). Comprehensive Approaches to Diagnosing and Mitigating System Performance Bottlenecks. In International Journal of Scientific Research in Computer Science, Engineering and Information Technology. https://ijsrcseit.com/home/issue/view/article.php?id=CSEIT182549

Naser Ezzati-Jivan, Quentin Fournier, M. Dagenais, & A. Hamou-Lhadj. (2020). DepGraph: Localizing Performance Bottlenecks in Multi-Core Applications Using Waiting Dependency Graphs and Software Tracing. In 2020 IEEE 20th International Working Conference on Source Code Analysis and Manipulation (SCAM). https://ieeexplore.ieee.org/document/9252064/

Nassim Corteggiani, Giovanni Camurati, & Aurélien Francillon. (2018). Inception: System-Wide Security Testing of Real-World Embedded Systems Software. In USENIX Security Symposium. https://www.semanticscholar.org/paper/6b0567e16cb249a95d2906cc1ff14a51613049ef

NM Mohammed, M Niazi, & M Alshayeb. (2017). Exploring software security approaches in software development lifecycle: A systematic mapping study. https://www.sciencedirect.com/science/article/pii/S0920548916301155

O Ibidunmoye & F Hernández-Rodriguez. (2015). Performance anomaly detection and bottleneck identification. https://dl.acm.org/doi/abs/10.1145/2791120

OBSTACLES TO SUSTAINABLE SECURITY IN THE KURDISTAN REGION USING THE FUZZY DELPHI. (2022). In American International Journal of Social Science Research. https://www.semanticscholar.org/paper/696d82cf58129dc5a9d1509d3dc195cf7c337cef

Ola M. Surakhi, A. Hudaib, M. Alshraideh, & Mohammad Khanafseh. (2017). A Survey on Design Methods for Secure Software Development. In Bioinformatics. https://www.semanticscholar.org/paper/ac517c1c09b4db636a3e278d46175d12c99158c0

P. Herrmann. (2007). Trust-Based Security Policy Enforcement of Software Components ∗. https://www.semanticscholar.org/paper/be66959e03899d62cfccb0bff2fcb577c7e7cd19

P. K. Dubey, Ajay Jangid, & B. R. Chandavarkar. (2020). An Interdependency between Symmetric Ciphers and Hash Functions: A Survey. In 2020 11th International Conference on Computing, Communication and Networking Technologies (ICCCNT). https://ieeexplore.ieee.org/document/9225412/

P Morrison. (2015). A security practices evaluation framework. https://ieeexplore.ieee.org/abstract/document/7203118/

P. Skentzos. (2024). SOFTWARE SAFETY AND SECURITY BEST PRACTICES: A CASE STUDY FROM   AEROSPACE. In SAE Technical Paper Series. https://www.sae.org/content/2024-01-3443

P Veríssimo, L Rodrigues, & P Veríssimo. (2001). Fundamental security concepts. https://link.springer.com/chapter/10.1007/978-1-4615-1663-7_16

P. Vu & Tung Thanh Nguyen. (2024). Tracking Software Security Topics. In ArXiv. https://arxiv.org/abs/2409.18351

Phillip Bosco. (2020). Real-World Case Study: The Overloaded Security Professionals Guide to Prioritizing Critical Security Controls. https://www.semanticscholar.org/paper/0fd865f2fa3971a8a8617d2722e65be89bab02d8

Priya Anand & J. Ryoo. (2018). Architectural Solutions to Mitigate Security Vulnerabilities in Software Systems. In Proceedings of the 13th International Conference on Availability, Reliability and Security. https://www.semanticscholar.org/paper/02d19795fe5b34b6fe0c7e88003770e950c366fb

Priya Anand & Jungwoo Ryoo. (2021). A Pattern-based Security Solution for Software Systems with Architectural Weaknesses. In 2021 International Conference on Software Security and Assurance (ICSSA). https://ieeexplore.ieee.org/document/10833901/

PV Rangan. (1992). An axiomatic theory of trust in secure communication protocols. In Computers & Security. https://www.sciencedirect.com/science/article/pii/016740489290043Q

Quentin Rouland, Stojanche Gjorcheski, & Jason Jaskolka. (2023). Eliciting a Security Architecture Requirements Baseline from Standards and Regulations. In 2023 IEEE 31st International Requirements Engineering Conference Workshops (REW). https://www.semanticscholar.org/paper/d839ebed1da8f287aeed0f933b3a4ec355f0f957

R. Chillarege. (1999). Software Testing Best Practices. https://www.semanticscholar.org/paper/61fd2b8cb0ec1150819d00e65facfc1f6fa63557

R Croft, Y Xie, M Zahedi, & MA Babar. (2022). An empirical study of developers’ discussions about security challenges of different programming languages. https://link.springer.com/article/10.1007/s10664-021-10054-w

R. Kissel. (2014). Glossary of Key Information Security Terms. https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7298.pdf

R Ruefle, A Dorofee, & D Mundie. (2014). Computer security incident response team development and evolution. https://ieeexplore.ieee.org/abstract/document/6924672/

R Shirey. (2007). Internet security glossary, version 2. https://www.rfc-editor.org/rfc/rfc4949

RA Khan, SU Khan, HU Khan, & M Ilyas. (2021). Systematic mapping study on security approaches in secure software engineering. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9328095/

RA Khan, SU Khan, M Alzahrani, & M Ilyas. (2022). Security assurance model of software development for global software development vendors. In Ieee Access. https://ieeexplore.ieee.org/abstract/document/9782440/

Richa Adlakha, Shobhit Sharma, Aman Rawat, & Kamlesh Sharma. (2019). Cyber Security Goal’s, Issue’s, Categorization & Data Breaches. In 2019 International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon). https://www.semanticscholar.org/paper/455ec8fbea24468beef16caf5ef620d79ab78319

Ross J. Anderson. (2007). Software Security: State of the Art. In IEEE Security & Privacy Magazine. https://www.semanticscholar.org/paper/e14c2d4e085b929fdf0a1c08ad3809a399fdffe6

RS Poore. (1993). Is Network Security a Contradiction in Terms? https://www.tandfonline.com/doi/abs/10.1080/19393559308551338

S. C. D. Graaf. (2014). Complex trade-offs in the security domain. https://www.semanticscholar.org/paper/515bbae039905fe514f64dbc1ff6945dea226f30

S Cirani, G Ferrari, & L Veltri. (2013). Enforcing security mechanisms in the IP-based internet of things: An algorithmic overview. In Algorithms. https://www.mdpi.com/1999-4893/6/2/197

S Duttagupta, R Virk, & M Nambiar. (2015). Software bottleneck analysis during performance testing. https://ieeexplore.ieee.org/abstract/document/7344508/

S Ghaith & M Ó Cinnéide. (2012). Improving software security using search-based refactoring. https://link.springer.com/chapter/10.1007/978-3-642-33119-0_10

S Islam & P Falcarin. (2011). Measuring security requirements for software security. https://ieeexplore.ieee.org/abstract/document/6169137/

S Kumar & J Jamieson. (2005). Software industry in the fastest emerging market: challenges and opportunities. https://www.inderscienceonline.com/doi/abs/10.1504/IJTM.2005.005998

S. Mahmudova. (2018). About Some Methods for Software Security. In Transactions on Networks and Communications. https://www.semanticscholar.org/paper/c4ed6b82564f1d244d8ea40a00f87821e782a48b

S McGee & D Greer. (2012). Towards an understanding of the causes and effects of software requirements change: two case studies. In Requirements Engineering. https://link.springer.com/article/10.1007/s00766-012-0149-0

S. Obradović. (2002). The nature of axioms of physical theory. In European Journal of Physics. https://www.semanticscholar.org/paper/340bfaa0034dd140a1ed319f212e48743e446f93

S. Ramamoorthy, Dr. S. P. Rajagopalan, & S. Sathyalakshmi. (2010). Security and Software Architectures. https://www.semanticscholar.org/paper/54dbb2010ebe95f768c2a73753bdd408d9b832bb

S Rehman & SU Khan. (2012). Swot analysis of software quality metrics for global software development: A systematic literature review protocol. In IOSR Journal of Computer Engineering. https://www.researchgate.net/profile/Siffat-Ullah-Khan/publication/235769944_Swot_Analysis_Of_Software_Quality_Metrics_For_Global_Software_Development_A_Systematic_Literature_Review_Protocol/links/02bfe51363d3441aee000000/Swot-Analysis-Of-Software-Quality-Metrics-For-Global-Software-Development-A-Systematic-Literature-Review-Protocol.pdf

S Shrestha. (2023). Exploring New Revenue Streams in a Software Company. https://www.theseus.fi/handle/10024/810720

S. Sidhu & Himanshu Gupta. (2019). A Security Mechanism for Software Defined Vulnerabilities. In 2019 4th International Conference on Information Systems and Computer Networks (ISCON). https://ieeexplore.ieee.org/document/9036247/

Saima Rafi, Muhammad Azeem Akbar, & A. Khan. (2024). Empirical Insights into Product Security Challenges and Practices in Software Development. In 2024 International Conference on Frontiers of Information Technology (FIT). https://ieeexplore.ieee.org/document/10838436/

Satyajit Lingras & Aruni Basu. (2025). The Security of Autonomous Vehicle Software and its National Security Implications. In European Journal of Applied Science, Engineering and Technology. https://ejaset.com/index.php/journal/article/view/190

Shaiqa Nadeem & Ahthasham Sajid. (2025). Insecure Software Development and Threat Mapping via Security Frameworks. In The Asian Bulletin of Big Data Management. https://www.semanticscholar.org/paper/67dd669f9b3f1eb7d8687298726122c50ec85228

Shamsa Alghaithi, Alreem Alkaabi, Hussam Al Hamadi, Nidal A. Al-Dmour, & Taher M. Ghazal. (2022). A Study of Risk Management Frameworks and Security Testing For Secure Software Systems. In 2022 International Conference on Electrical, Computer, Communications and Mechatronics Engineering (ICECCME). https://ieeexplore.ieee.org/document/9988363/

Souhail Mssassi & Anas Abou El Kalam. (2024). The Blockchain Trilemma: A Formal Proof of the Inherent Trade-Offs Among Decentralization, Security, and Scalability. In Applied Sciences. https://www.semanticscholar.org/paper/07a5efd12aad3c040df6ca484ab44f03be6471a6

Spiros Mancoridis. (2008). Software analysis for security. In 2008 Frontiers of Software Maintenance. https://www.semanticscholar.org/paper/71cb16584ac3d6ce1ad061dc67f3b682213801e2

ST Halkidis & A Chatzigeorgiou. (2014). Brief review of software security history with an emphasis on efforts focused at early stages of the software lifecycle. https://www.tandfonline.com/doi/abs/10.1080/15536548.2014.912481

ST Siddiqui. (2017). Significance of security metrics in secure software development. In International Journal of Applied Information Systems. https://www.ijais.org/archives/volume12/number6/1000-2017451710/

Stefanie Jasser, Katja Tuma, R. Scandariato, & Matthias Riebisch. (2018). Back to the Drawing Board - Bringing Security Constraints in an Architecture-centric Software Development Process. In International Conference on Information Systems Security and Privacy. https://www.scitepress.org/Link.aspx?doi=10.5220/0006659904380446

Steffen Becker, W. Hasselbring, Alexandra Paul, Marko Boskovic, Heiko Koziolek, Jan Ploski, A. Dhama, Henrik Lipskoch, Matthias Rohr, Daniel Winteler, Simon Giesecke, R. Meyer, M. Swaminathan, J. Happe, Margarete Muhle, & Timo Warns. (2006). Trustworthy software systems: a discussion of basic concepts and terminology. In ACM SIGSOFT Softw. Eng. Notes. https://www.semanticscholar.org/paper/0fb1688d8f5e0b69e96e596eb6e4692024596e0e

Sujit Rokka Chhetri, Jiang Wan, & M. A. Faruque. (2017). Cross-domain security of cyber-physical systems. In 2017 22nd Asia and South Pacific Design Automation Conference (ASP-DAC). https://ieeexplore.ieee.org/document/7858320/

T Yu & M Pradel. (2018). Pinpointing and repairing performance bottlenecks in concurrent programs. In Empirical Software Engineering. https://link.springer.com/article/10.1007/s10664-017-9578-1

Tamara Lopez, Helen Sharp, A. Bandara, T. Tun, Mark Levine, & B. Nuseibeh. (2022). Security Responses in Software Development. In ACM Transactions on Software Engineering and Methodology. https://dl.acm.org/doi/10.1145/3563211

Tobias Rauter, Andrea Höller, Nermin Kajtazovic, & Christian Kreiner. (2016). Asset-Centric Security Risk Assessment of Software Components. In MILS@HiPEAC. https://www.semanticscholar.org/paper/55907f649622fc7224c25f11c1f6bf62d88c45ff

Topic 2 . 4 : The Evolution of Data Models. (2009). https://www.semanticscholar.org/paper/4d4664a028930438d5a8a0bb9176c3fdd0c19aeb

Tridas Mukhopadhyay & Byung Cho Kim. (2007). Essays on software market: security, liability, and pricing. https://www.semanticscholar.org/paper/c5d365d955191d8c7bfd976df1e923b3de2480cf

V. Sharma & Kishor S. Trivedi. (2005). Architecture based analysis of performance, reliability and security of software systems. In Workshop on Software and Performance. https://dl.acm.org/doi/10.1145/1071021.1071046

V Sundaravarathan, H Alqalaf, A Siddiqui, & K Kim. (2024). Cross-Domain Solutions (CDS): A Comprehensive Survey. https://ieeexplore.ieee.org/abstract/document/10721459/

V. V. Kuliamin, Alexander Konstantinovich Petrenko, & Ekaterina Alexandrovna Rudina. (2024). Software Security by Design. In Proceedings of the Institute for System Programming of the RAS. https://www.semanticscholar.org/paper/1a91635a1a82c69ef6b23f42b41a8993b9308390

V Verma. (n.d.). Comparative Study of Revenue Generation Model in Cloud Computing. https://www.researchgate.net/profile/Vikas-Verma-17/publication/326322693_Comparative_Study_of_Revenue_Generation_Model_in_Cloud_Computing/links/651fbf09fc5c2a0c3bb86a60/Comparative-Study-of-Revenue-Generation-Model-in-Cloud-Computing.pdf

VS Sharma & KS Trivedi. (2007). Quantifying software performance, reliability and security: An architecture-based approach. In Journal of Systems and Software. https://www.sciencedirect.com/science/article/pii/S0164121206002020

W. Hong. (2007). Software Security in Source Code. In Software Guide. https://www.semanticscholar.org/paper/59b261b67e9b6f30da307d6b19ab2ad4cff0604e

W Jimenez, A Mammar, & A Cavalli. (2009). Software vulnerabilities, prevention and detection methods: A review1. https://www.academia.edu/download/30855964/wp0906.pdf#page=6

W Wang, F Dumont, & N Niu. (2020). Detecting software security vulnerabilities via requirements dependency analysis. https://ieeexplore.ieee.org/abstract/document/9222252/

Wang Tong. (2007). Security Requirement-based Software Vulnerability Analysis Model. In Computer Science. https://www.semanticscholar.org/paper/1f1a011eb1722532e292becb2d94214eb8bcf6d0

X Wang, H Yuan, Y Bu, & W Chu. (2025). Construction of Emergency Response Mechanism and Data Protection System in Network Security. https://combinatorialpress.com/article/jcmcc/Volume%20127/127bp2/Construction%20of%20Emergency%20Response%20Mechanism%20and%20Data%20Protection%20System%20in%20Network%20Security.pdf

Xinyang Jia. (2023). Research on Computer Software Security Testing Techniques and Applications. In Journal of Intelligence and Knowledge Engineering. https://www.semanticscholar.org/paper/8dccda1cf6e9b43c73a77b564d400463c85185fb

Y Liu, M Zhang, D Li, K Jee, Z Li, Z Wu, J Rhee, & P Mittal. (2018). Towards a Timely Causality Analysis for Enterprise Security. In NDSS. http://www.princeton.edu/~pmittal/publications/priotracker-ndss18.pdf

Y Vorobeychik & J Letchford. (2015). Securing interdependent assets. In Autonomous Agents and Multi-Agent Systems. https://link.springer.com/article/10.1007/s10458-014-9258-0

Yan Gao. (2024). Analysis of Software Development and Operation Measures from the Perspective of Security Technology. In Journal of Electronic Research and Application. https://www.semanticscholar.org/paper/7db084ad9cc7948e847befaaf6336b068d3f4787

Yingxu Wang. (2006). On Constraints and Count-Measures for Software Engineering. In 2006 Canadian Conference on Electrical and Computer Engineering. https://ieeexplore.ieee.org/document/4054981/

YM Liu & I Traore. (2007). Properties for security measures of software products. https://www.naturalspublishing.com/files/published/64q7p1j55er95l.pdf

Z Han, X Li, R Feng, J Hu, & G Xu. (2014). A three-dimensional model for software security evaluation. https://ieeexplore.ieee.org/abstract/document/6976565/

Zeineb Zhioua, S. Short, & Y. Roudier. (2014). Static Code Analysis for Software Security Verification: Problems and Approaches. In 2014 IEEE 38th International Computer Software and Applications Conference Workshops. https://ieeexplore.ieee.org/document/6903113

Zhang Qiang. (2005). Current research and future trends to application security. In Information Technology. https://www.semanticscholar.org/paper/5c069ef4c62105ccad19271bb5513abe149a2cae

Zhilong Wang, Lan Zhang, & Peng Liu. (2023). ChatGPT for Software Security: Exploring the Strengths and Limitations of ChatGPT in the Security Applications. In ArXiv. https://arxiv.org/abs/2307.12488



Generated by Liner
https://getliner.com/search/s/5926611/t/85551878