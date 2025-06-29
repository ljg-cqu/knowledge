Requirements: 1. Ensure compliance with MECE. 2. Explain clearly and briefly, using simple analogies and examples. 3. Use numbered lists for clarity when suitable. 4. Clarify core elements, components, structure, and context. 5. Clarify related concepts, definitions, functions, and purposes. 6. Clarify types, characteristics, along with their reasons and evidence. 7. Explain the significance, along with reasons and evidence. 8. Clarify internal implementation, work mechanisms, ,principles and rules. 9. Clarify the phase-based preconditions, inputs, and outputs. 10. Clarify architectural design philosophy, patterns, and features. 11. Clarify contradictions, trade-offs, and decisions, providing both qualitative and quantitative guidelines. 12. Clarify cause-and-effect relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 13. Clarify interdependency relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 14. Clarify cardinality-based relationships (1:1, 1:M, M:N). 15. Clarify contradictory relationships, using symbols like '<-verb(s)-', '-verb(s)->', and '<-verb(s)->'. 16. Make a summary table at the end with definitions, purposes, characteristics, ect. for clarity.

Sun Jun 29 2025

Extensibility in problem analysis refers to the inherent property of a problem that allows it to be expanded and transformed, offering multiple pathways for its resolution and adaptation [P0:1]. It is a crucial aspect of designing systems that can evolve and accommodate future changes with minimal disruption.

### Definition and Purpose of Extensibility
Extensibility is the capability of a system to grow and adapt. In the context of software, it specifically means the ability to enhance a product's functionality without modifying its core architecture. The purpose of extensibility is to allow developers to accommodate future changes, add new features, and adapt to evolving requirements with minimal disruption or significant rewrites. It mitigates the risk of being locked into a rigid feature set, ensuring a company's ability to scale and support future growth.

### Core Elements and Types of Extensibility
Problem extensibility encompasses four core elements that allow for a multifaceted approach to analysis and solution finding:
-   **Divergence (发散性)**: This element signifies that a single problem or thing can possess multiple characteristics, and conversely, a single characteristic can apply to multiple things or values [P0:6]. This multiplicity allows for diverse methods and approaches in problem-solving [P0:6]. An example is a consulting company's training session, which simultaneously promotes theories, conducts market research, generates material for a monograph, and builds future research ties [P3:2].
-   **Relevance (相关性)**: Relevance describes the interconnectedness of problems and their characteristics, where changes in one aspect can lead to "conductive transformations" in others [P0:7]. For instance, raising employee wages improves well-being, boosts work enthusiasm, and increases consumption capacity [P3:3].
-   **Inclusiveness (蕴含性)**: This principle indicates that achieving a lower-level goal or problem implicitly leads to the attainment of a higher-level one [P0:8]. The "anti-acquisition" strategy, where a foundational achievement implies a broader one, illustrates this qualitatively [P3:4].
-   **Expandability (可扩性)**: Expandability suggests that problems can be combined or decomposed into new problems, often leading to novel properties or solutions [P0:9]. This is seen in software development where complex projects are divided into smaller, manageable parts for efficient completion [P3:4]. It is also evident in sales layout analysis, where related items are grouped to leverage consumer needs for combination purchases [P3:4].

### Significance and Benefits of Extensibility
Extensibility is vital for ensuring that software and problem-solving approaches remain adaptable and maintainable over time.
-   **Adaptability**: Extensible systems can adjust to changing requirements and business needs without needing extensive refactoring or redesign.
-   **Scalability**: By allowing new features to be added incrementally, extensible systems can scale to accommodate growing complexity and user demands. This supports agility in development projects.
-   **Maintainability**: Extensible codebases are easier to maintain because changes can be localized to specific modules or components, reducing the impact on the entire system.
-   **Reusability**: Extensibility promotes code reuse by enabling the integration of third-party libraries, frameworks, or plugins, and allows for shared functionalities among different teams without duplication of effort.

### Internal Implementation and Work Mechanisms
Extensibility in software development relies on several key principles and mechanisms:
-   **Modularity**: Systems are broken down into smaller, self-contained modules, allowing individual components to be isolated, encapsulated, and easily extended or replaced without affecting the rest of the system.
-   **Loose Coupling**: Components interact through well-defined interfaces rather than direct dependencies, reducing the ripple effects of changes and promoting independence and reusability.
-   **Open/Closed Principle**: Software entities should be "open for extension but closed for modification," meaning new functionality can be added without altering existing source code.
-   **Polymorphism**: This language feature allows methods to vary their behavior based on the run-time type of the receiver, enabling flexible design patterns and allowing for new features to be added by implementing existing interfaces and adjusting configuration code.
-   **Dependency Injection (DI)**: A design pattern that achieves extensibility by decoupling components and their dependencies, making it easier to substitute implementations and extend functionality.
-   **Interfaces and Abstract Classes**: These define contracts for components, allowing for polymorphic behavior and interchangeable implementations.
-   **Plugin Architecture**: This allows features to be added or removed dynamically at runtime, making the system adaptable without downtime.
-   **Event-Driven Architecture**: Components communicate through events and listeners, decoupling producers and consumers of events and allowing easy addition or removal of event handlers.
-   **Configuration and Metadata**: Using configuration files or metadata to define system behavior enables customization and extension without modifying source code.
-   **Design Patterns**: Patterns like Factory, Strategy, and Observer provide reusable solutions that promote modular and flexible designs, accommodating changes with minimal impact. The Adapter pattern, for instance, is a solution for extensibility when software needs to act differently depending on the context without changing its overall interface.

### Phase-Based Preconditions, Inputs, and Outputs
While the provided documents do not explicitly detail phase-based preconditions, inputs, and outputs specifically for *applying extensibility to problem analysis*, they do touch upon these concepts in general software development and problem-solving processes.
-   **Problem Definition Phase**: Preconditions involve identifying problems and understanding their nature [P0:1, 20:652]. Inputs include real-world scenarios and domain knowledge. The output is a clear, conceptual model of the problem.
-   **Analysis and Design Phase**: Preconditions include a defined problem and understanding of requirements. Inputs are the conceptual problem model and identified entities/relationships. The output is an architectural blueprint that defines system structure, components, interfaces, and interactions, designed for modularity and scalability.
-   **Implementation Phase**: Preconditions are the architectural design and defined interfaces. Inputs are the design specifications. The output is code that encapsulates behavior and data using programming constructs like functions, classes, and interfaces.

In a broader sense, preconditions for effective problem analysis include selecting the main analytical object and clearly defining the analysis theme [P0:6]. Inputs involve understanding resource conditions (internal/external) and environmental conditions (internal/external), which can be transformed based on their elasticity or rigidity [P0:6].

### Architectural Design Philosophies and Patterns
Architectural design philosophies that support extensibility emphasize adaptability, scalability, and efficiency. Key patterns include:
-   **Microkernel Design Pattern**: Offers extensibility, feature separation, and isolation by allowing the addition of other application features.
-   **Plugin Architecture**: A design pattern that enables extending software applications without modifying the existing core structure.
-   **Strategy Pattern**: A behavioral design pattern that allows algorithms to be chosen at runtime, promoting flexibility and extensibility by reducing code duplication and enhancing maintainability.
-   **Adapter Pattern**: A solution for extensibility where software needs to act differently based on context without altering the overall interface.
-   **Abstraction**: A cornerstone of effective design that simplifies complex systems by distilling them into simplified models, hiding unnecessary details, and managing complexity. It enables reusability and scalability.
-   **Modularity and Loose Coupling**: These are fundamental tenets for building adaptable and scalable software.

Platforms can be designed to be extended through native integration systems, APIs (like REST and GraphQL), or by providing access to source code. Composability, the ability to assemble complex functionality from different components, goes hand-in-hand with extensibility, reducing development resources and infrastructure overheads.

### Contradictions, Trade-offs, and Decisions
In software development, there are inherent trade-offs when designing for extensibility.
-   **Extensibility vs. Simplicity**: While simplicity promotes ease of understanding and maintenance, balancing it with extensibility is a common challenge. Overly general systems designed for future-proofing might lead to unnecessary code and conceptual overhead if the predicted scenarios never materialize.
-   **Extensibility vs. Performance**: Highly extensible systems might introduce layers of abstraction or indirection, which can sometimes impact performance. The decision involves weighing the need for future adaptability against immediate performance requirements.
-   **Decision-Making**: A key decision-making principle is the "rule of three," which suggests that patterns (and thus opportunities for abstraction and extensibility) emerge only after building something similar three times. This advises against premature optimization for extensibility and instead, encourages waiting for "tension" or resistance to change in the code before refactoring for extensibility. This approach prioritizes writing simple, understandable code first and then looking for patterns as needed.

Qualitatively, the trade-off involves assessing the likelihood of future changes against the current cost of implementing extensibility. Quantitatively, it might involve comparing the effort to maintain adapters for multiple potential changes versus the effort to refactor code later if a change becomes necessary.

### Cause-and-Effect and Interdependency Relationships
Cause-and-effect relationships describe how one event (the cause) directly influences another (the effect). Interdependency implies a mutual reliance or influence between entities.

Examples of relationships related to extensibility in problem analysis:
-   High Cohesion <-promotes-> Maintainability and Reusability
-   Modularity <-enables-> Extensibility
-   Loose Coupling <-reduces-> Ripple Effects of Changes
-   Designing with Extensibility in mind <-allows for-> Adaptability to Changing Requirements
-   Increased Extensibility <-can lead to-> Increased Complexity (Trade-off)
-   Accurate Problem Definition <-simplifies-> Problem Resolution [P0:1]
-   Conflict <-drives-> Reform and Innovation [P0:2]
-   One Action <-yields-> Multiple Outcomes (Divergence) [P3:2]

### Cardinality-Based Relationships
Cardinality, in data modeling, describes the numerical relationship between rows in different tables or instances of different entities. There are three main types:
1.  **One-to-One (1:1) Relationship**: One row in a database table relates to exactly one row in a second table.
    -   **Example**: A student and their student ID, where each student has one unique ID, and each ID belongs to one student. Another example is a person and their birth certificate.
    -   **Notation**: Represented with a single line connecting two entities in an Entity-Relationship (ER) diagram.
2.  **One-to-Many (1:N or 1:M) Relationship**: One row in a table relates to many rows in a second table. This is the most common database relationship, often enforced using primary and foreign keys.
    -   **Example**: A single customer places multiple orders. A doctor can have many consultations, but each consultation is associated with only one doctor. A patient can have many appointments, but each appointment involves only one patient.
    -   **Notation**: Notated with a line joining the two entities, with a single vertical line on the "one" side and a crow's foot symbol on the "many" side.
3.  **Many-to-Many (M:N) Relationship**: Many rows in one table are related to many rows in a second table.
    -   **Example**: Multiple authors can write multiple books. Many students can sign up for many classes, and a class can have many students. Doctors can have many patients, and patients can see many doctors.
    -   **Implementation**: A direct M:N relationship is not possible in relational databases and requires a cross-reference (or junction) table to convert it into two one-to-many relationships.

Cardinality is a vital piece of information for relationships between entities, crucial for later stages of database architecture and simplifying query execution plans.

### Contradictory Relationships
Contradictory relationships arise when two or more goals cannot be simultaneously achieved under the same conditions, or when subjective desires conflict with objective conditions [P0:2].
-   **Incompatible Type (不相容型)**: Conflicts between subjective desires and objective conditions <-requires-> Transformation of Objective Conditions or Goals [P0:2]. (e.g., small scale for a large elephant)
-   **Oppositional Type (对立型)**: Two or more goals cannot be simultaneously achieved under the same conditions <-requires-> Creation of a "Conversion Bridge" for Coexistence [P0:2]. (e.g., wolf and chicken in one cage)
-   **Objective Contradictory Problems (客观矛盾问题)**: Conflicts inherent in objective issues <-requires-> Human Intervention to Transform into Solvable Types [P0:2]. (e.g., pests affecting plants, desertification)
-   **Goal vs. Conditions**: When goals are fixed, conditions must be transformed. When conditions are rigid, goals must be transformed. For complex problems, both goals and conditions may need transformation [P0:2].

Contradictions are not inherently negative; rather, they serve as a powerful impetus <-leads to-> Reform, Innovation, and Human Development [P0:2].

### Summary Table: Extensibility in Problem Analysis

| Aspect              | Definition                                                                                                                                                             | Purpose                                                                                                                                                                                                           | Characteristics                                                                                                                                                                                                                                                                                                                                                                | Examples/Evidence                                                                                                                                                                                                                                                                                                                                                                                                                             | Implementation/Application                                                                                                                                                                                                                                                                                                                             |
| :------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Extensibility**   | The inherent property of a problem that allows it to be expanded and transformed [P0:1]. In software, the ability to add functionality without modifying core code. | To enable systems to accommodate future changes, add new features, and adapt to evolving requirements with minimal disruption. To ensure scalability and longevity of digital products. | **Flexible**: Can grow and connect with other tools as needs evolve. **Modular**: Broken into smaller, self-contained components. **Open to Extension**: Allows adding features without altering existing code. **Scalable**: Accommodates growing complexity. **Reusable**: Allows different teams to add functionality without duplicating effort. | -   Smartphone with apps extending its core functionality. -   Consulting company training yielding multiple benefits (promotion, market research, content creation, networking) [P3:2]. -   Raising employee wages increasing well-being, enthusiasm, and consumption [P3:3]. -   Software projects divided into smaller parts for efficient development [P3:4]. -   Grouping related sales items like infant clothing and accessories for convenience and combination purchases [P3:4]. | -   Using interfaces and abstract classes. -   Implementing plugin architectures. -   Adopting event-driven architectures. -   Utilizing configuration files and metadata. -   Applying design patterns (Factory, Strategy, Observer, Adapter). -   Leveraging polymorphism. -   Adhering to modularity and loose coupling principles. |
| **Cardinality**     | Numerical relationship between entities or objects in data modeling. Defines how many instances of one entity relate to instances of another. | To describe the fundamental relationships between entities, crucial for database architecture and query execution plans. | Defines the maximum number of occurrences allowed in a relationship.                                                                                                                                                                                                 | **One-to-One (1:1)**: Person to Birth Certificate. **One-to-Many (1:N)**: Doctor to Consults. **Many-to-Many (M:N)**: Student to Classes. **High Cardinality**: Column with many distinct values. **Low Cardinality**: Column with many repeated values.                                                                                                                                     | Used in Entity-Relationship (ER) diagrams. M:N relationships require a cross-reference table. Essential for data modeling and database design. |
| **Trade-offs (Contradictions)** | Inherent conflicts or opposing aspects when optimizing different software quality attributes, such as extensibility vs. simplicity. | To inform decision-making during design and development by balancing competing goals.                                                                                                                                                                             | Requires prioritization and strategic planning. Can lead to over-engineering if not managed.                                                                                                                                                                                             | -   The "rule of three" guides when to apply patterns for extensibility, avoiding premature abstraction. -   Balancing complexity added by extensibility with immediate simplicity and ease of understanding. -   Choosing between maintaining extensive adapters now or refactoring later if a database change is needed. | Strategic choices on design patterns, architectural approaches, and development timelines. Often involves "waiting for tension" in the code before implementing complex extensible solutions. Qualitative assessment of future needs vs. current development cost.                                                                                                   |

Bibliography
5 Design Patterns for Software Extensibility - LinkedIn. (2023). https://www.linkedin.com/advice/3/what-most-effective-design-patterns-improving-software-1uafc

10.6 Problem-Solving by Analogy – Cognitive Psychology. (2025). https://nmoer.pressbooks.pub/cognitivepsychology/chapter/problem-solving-by-analogy/

An in-depth look at Cardinality & Modality in Database Relationships. (2019). https://medium.com/analytics-vidhya/an-in-depth-look-at-database-relationships-cardinality-modality-a3d6bba0ee1e

Cardinality (data modeling) - Wikipedia. (n.d.). https://en.wikipedia.org/wiki/Cardinality_(data_modeling)

Cause-and-effect relationship - (Abnormal Psychology) - Fiveable. (n.d.). https://library.fiveable.me/key-terms/abnormal-psychology/cause-and-effect-relationship

Common Trade-offs in Software Development | by i.vikash - Medium. (2023). https://medium.com/@i.vikash/common-trade-offs-in-software-development-13d6f322e83b

Database Cardinality: A Brief Overview - Coursera. (n.d.). https://www.coursera.org/articles/cardinality

Design Patterns for Extensibility : Strategy Pattern - programmium. (2018). https://programmium.wordpress.com/2018/07/19/design-patterns-for-extensibility-strategy-pattern/

Examples of Inclusion in the Workplace - LeaderFactor. (2025). https://www.leaderfactor.com/learn/examples-of-inclusion-in-the-workplace

Extensibility - Carnegie Mellon University. (2022). https://insights.sei.cmu.edu/library/extensibility/

Extensibility and Modularity - Adobe Developer. (2025). https://developer.adobe.com/commerce/php/architecture/modules/

Extensibility: Designing for Future Growth in Software Architecture. (2024). https://buildsimple.substack.com/p/extensibility-designing-for-future

Extensible and Reconfigurable Architecture: A Blueprint for Future ... (n.d.). https://uni.xyz/journal/extensible-and-reconfigurable-architectu

Extremely Extensible Software Design (Part 2) | by Benji Shults. (2018). https://medium.com/@benjishults/extremely-extensible-software-design-part-2-98d514086f9e

How can you ensure the extensibility of an algorithm? - LinkedIn. (2023). https://www.linkedin.com/advice/0/how-can-you-ensure-extensibility-algorithm-skills-algorithms-stxse

How to make a trade-off between maintainability, extensibility and ... (n.d.). https://yifan-online.com/en/km/article/detail/11347

How to Write Code That Are Extensible - Edward’s Newsletter. (2023). https://pathtosenior.substack.com/p/how-to-write-code-that-are-extensible

Java Mastery: Advancing Beyond SOLID with Abstraction ... - Medium. (2024). https://medium.com/@alxkm/java-mastery-advancing-beyond-solid-with-abstraction-extensibility-and-cohesion-d2d0c07a342d

Major Software Architecture Patterns | by Nile Bits - Medium. (2023). https://medium.com/@nile.bits/major-software-architecture-patterns-52689dd00cee

Mastering Extensibility in Software Engineering - Number Analytics. (2025). https://www.numberanalytics.com/blog/mastering-extensibility-software-engineering

Modeling the Cause-and-Effect Relationships between the ... - MDPI. (2023). https://www.mdpi.com/2071-1050/15/6/5250

[PDF] A Method for Efficient Extensibility Improvements in Embedded ... (n.d.). https://www.jsoftware.us/vol10/119-TE14.pdf

[PDF] A Rigorous, Architectural Approach to Extensible Applications. (n.d.). http://intrinsarc.com/downloads/extensible-applications-amcveigh-6-Dec-09.pdf

[PDF] AP7: Qualitative Characteristics 1—Relevance and reliability. (2005). https://www.ifrs.org/content/dam/ifrs/project/conceptual-framework-2010/ap7-qualitative-characteristics-1.pdf

[PDF] Architectural Support for Extensibility and Autonomy in Wide-Area ... (1998). https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=b7c6e8f44d1beb46d2d6cde11c2e95ed6f49677c

[PDF] Cardinality in Data Modeling - Temple MIS. (n.d.). https://community.mis.temple.edu/mis3506digitaldesignfall2018/files/2018/10/Adam-Alalouf_Cardinality.pdf

[PDF] Chapter The Many Facets of the Cause-Effect Relation. (n.d.). https://personal.ntu.edu.sg/assgkhoo/papers/khoo_chan_niu.cause_effect.2002.pdf

[PDF] Design Problem Solving:A Task Analysis. (n.d.). https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/857/775

[PDF] Extensibility - SEI Blog. (n.d.). https://insights.sei.cmu.edu/documents/1297/2022_005_001_876979.pdf

[PDF] Extensibility Design Patterns From The Initial Stage of Application ... (n.d.). https://www.duo.uio.no/bitstream/handle/10852/61661/theepank_main_document.pdf

[PDF] Extensibility Patterns - TU Dresden. (n.d.). http://st.inf.tu-dresden.de/files/teaching/ws18/dpf/exercise5.pdf

[PDF] Extensibility Patterns: Extension Access - TU Dresden. (n.d.). http://st.inf.tu-dresden.de/files/teaching/ws18/dpf/exercise5-solutions.pdf

[PDF] Metaphor - A Key to Extensible Semantic Analysis - ACL Anthology. (n.d.). https://aclanthology.org/P80-1004.pdf

[PDF] NASA Systems Engineering Handbook. (n.d.). https://www.nasa.gov/wp-content/uploads/2018/09/nasa_systems_engineering_handbook_0.pdf

[PDF] On Extensibility of Software Systems - Tidsskrift.dk. (n.d.). https://tidsskrift.dk/ece/article/download/21233/18722

[PDF] Prototyping-Oriented Software Development— Concepts and Tools. (n.d.). https://www.plus.ac.at/wp-content/uploads/2021/02/J001.pdf

[PDF] Software Engineering Processes. (n.d.). http://users.csc.calpoly.edu/~gfisher/classes/307/textbook/2.pdf

[PDF] Systems Analysis and Design, 5th Edition - UoITC. (n.d.). https://www.uoitc.edu.iq/images/documents/informatics-institute/Competitive_exam/Systemanalysisanddesign.pdf

Personality traits and complex problem solving - Frontiers. (2022). https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.788402/full

Plan for tradeoffs: You can’t optimize all software quality attributes. (2022). https://stackoverflow.blog/2022/01/17/plan-for-tradeoffs-you-cant-optimize-all-software-quality-attributes/

Please help me understand this problem about cardinality. (2024). https://dba.stackexchange.com/questions/342655/please-help-me-understand-this-problem-about-cardinality

Plugin Architecture Design Pattern — A Beginner’s Guide | Dev Leader. (n.d.). https://medium.devleader.ca/plugin-architecture-design-pattern-a-beginners-guide-to-modularity-2ff88e2a55d5

Relationship cardinality issue - Microsoft Q&A. (2021). https://learn.microsoft.com/en-au/answers/questions/459918/relationship-cardinality-issue

Strategy Design Pattern - GeeksforGeeks. (2024). https://www.geeksforgeeks.org/system-design/strategy-pattern-set-1/

The relationship between big five personality traits, coping strategies ... (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9660183/

The Rule of Three: Applying abstractions and patterns - Holden Rehg. (2021). https://holdenrehg.com/blog/2021-09-20_rule-of-three

Trade-offs and Software Engineering | by Rafael Ritter - Medium. (2020). https://rafaelritter.medium.com/trade-offs-and-software-engineering-22a41f838d9e

Trying to understand cardinality in an entity relationship diagram? (2015). https://stackoverflow.com/questions/34427694/trying-to-understand-cardinality-in-an-entity-relationship-diagram

Using Analogies for Creative Problem Solving - Thinking Directions. (2015). https://www.thinkingdirections.com/using-analogies-creative-problem-solving/

What are the characteristics of the problem-solving method? - Brainly. (2023). https://brainly.com/question/34615918

What is another word for extensibility? - WordHippo. (2009). https://www.wordhippo.com/what-is/another-word-for/extensibility.html

What Is Cardinality in Data Modeling? The Theory and Practice of ... (2021). https://vertabelo.com/blog/cardinality-in-data-modeling/

What Is Database Cardinality? - IT Glossary - SolarWinds. (2023). https://www.solarwinds.com/resources/it-glossary/database-cardinality

What Is Extensibility in Software Engineering? A Complete Guide. (2025). https://strapi.io/blog/extensibility-in-software-engineering

What is extensibility? Why you should choose extensible tools. (2025). https://www.contentful.com/blog/what-is-extensibility/

What is the purpose of data modeling cardinality? - Stack Overflow. (2012). https://stackoverflow.com/questions/12816567/what-is-the-purpose-of-data-modeling-cardinality



Generated by Liner
https://getliner.com/search/s/5926611/t/86094495