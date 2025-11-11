# Pattern-Based Q&A Generation Template

Generate 30 Q&As (20/40/40 F/I/A, 150–300 words) demonstrating proven patterns with
empirical evidence, multi-stakeholder value, and clear boundaries.

## Context, Scope, Constraints, and Assumptions

**Scope**: Pattern-based Q&A generation covering 11 domains (Regulatory, Business,
Market, Technical, Data, Organizational, NFR [10 sub-dimensions], Process, Hybrid)
using 70+ proven patterns.

**Target Audience**: LLMs generating Q&A content and human reviewers validating output.

**Constraints** (MUST preserve):

- Structure: 3-part organization (Part I: Quality Standards, Part II: Workflow,
  Part III: Output Structure)
- Counts: 30 Q&As (6 Foundational / 12 Intermediate / 12 Advanced)
- References: ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations
- Validation: All 21 validation steps with original thresholds intact
- Pattern catalog: 70+ patterns preserved
- Supporting artifacts: Domain-specific visual/example/metric table retained

**Terminology Policy** (RFC 2119):

- **MUST**: Mandatory requirement; failure = invalid output
- **SHOULD**: Strong recommendation; exceptions require justification
- **MAY**: Optional; use at discretion

**Style Conventions**:

- Format: GitHub-Flavored Markdown
- Line length: ≤120 characters for readability in diffs
- Links: Relative links for internal references; external links must be direct
  and authoritative
- Structure: Concise bullets and simple tables; numbered lists for ordered steps

**Key Assumptions**:

- Outputs will be validated against all 21 validation steps before submission
- Evidence must be cited using [Ref: ID] notation
- All patterns require empirical effectiveness evidence (company/metrics/adoption)
- Multi-stakeholder analysis (≥2 stakeholder groups) MUST be demonstrated

---

# Part I: Quality Standards

## Terminology and Modal Verbs

**RFC 2119 Modal Verbs**: MUST (mandatory), SHOULD (strong recommendation),
MAY (optional).

**Normalized Terms**:

- Use "Q&A" (not "question-answer" or "QA")
- Use "pattern" (not "design pattern" or "architectural pattern" unless
  specifically referring to those subcategories)
- Use "stakeholder" (not "actor" or "participant")
- Use "evidence" (not "proof" or "validation data") for empirical support
- Use "citation" (not "reference" or "source") for [Ref: ID] inline markers
- Use "domain" (not "category" or "area") for the 11 top-level groupings

## Evidence and Credibility Policy

### Accuracy Verification

**Claim Classification**:

- **Critical**: Core pattern definitions, effectiveness metrics, compliance
  requirements, trade-off analyses
- **Supporting**: Context, examples, tool descriptions, background information

**Evidence Requirements**:

- Critical claims: MUST have ≥1 authoritative citation; SHOULD have ≥2 independent
  sources for cross-verification
- Supporting claims: SHOULD have ≥1 citation when non-obvious
- Obvious/common knowledge: MAY omit citation (e.g., "HTTP uses TCP")

**Verification Checklist**:

1. Claim → Classify as Critical or Supporting
2. Source → Identify authoritative source(s)
3. Quote/Paraphrase → Extract relevant evidence
4. Link → Provide direct URL or DOI
5. Date → Note publication/update date
6. Cross-check → For critical claims, verify with 2nd independent source

### Source Credibility Tiers

**Tier 1 (Highest)**: Peer-reviewed papers, official standards (ISO, NIST, IETF),
regulatory documents (GDPR, CCPA), formal specifications (OpenAPI, BPMN)

**Tier 2**: Official vendor documentation (AWS, Azure, GCP), authoritative books
(O'Reilly, Pragmatic), established frameworks (Scrum Guide, Team Topologies)

**Tier 3**: Reputable organization blogs (Netflix Tech Blog, Martin Fowler),
industry analyst reports (Gartner, Forrester), recognized expert articles

**Tier 4**: Expert personal blogs, conference talks, well-maintained open-source
project docs

**Tier 5 (Lowest)**: Community forums (Stack Overflow, Reddit), Q&A sites,
unverified wikis

**Usage Guidelines**:

- Critical claims: Prefer Tiers 1-2; accept Tier 3 with corroboration
- Supporting claims: Accept Tiers 1-4; use Tier 5 with caution and note
  limitations
- For tools: Require official docs (Tier 2) for features; accept Tier 3-4 for
  adoption metrics
- Recency: Prefer sources <3 years old for fast-moving domains (cloud,
  frameworks); <10 years for stable domains (algorithms, theory)

### Significance Classification

**Critical Requirements** (MUST be complete, MUST NOT be obscured):

- 7 mandatory pattern criteria for each pattern
- 30 Q&As with 6/12/12 F/I/A distribution
- All 21 validation steps
- Reference minimums (≥25/≥10/≥12/≥12)
- Domain-specific supporting artifacts table
- MECE domain boundaries

**Nice-to-Have Enhancements** (SHOULD include when relevant):

- Additional examples beyond minimum
- Supplementary diagrams
- Extended tool descriptions
- Historical context
- Alternative perspectives

**Pruning Guideline**: If nice-to-have content exceeds 20% of section length or
obscures critical requirements, reduce or relocate it.

## Reasoning and Logical Structure

### Reasoning Template (MUST apply to pattern explanations and Q&A answers)

1. **Claim**: State the pattern, principle, or answer clearly
2. **Rationale**: Explain WHY it works or WHY it's recommended
3. **Evidence**: Cite empirical data (company adoption, metrics, studies)
4. **Implications**: Describe consequences and stakeholder impacts
5. **Limitations**: Acknowledge constraints, assumptions, and failure modes
6. **Alternatives**: Note when other approaches are preferable

**Example Application** (Idempotency pattern):

- **Claim**: Idempotency ensures operations produce the same result when repeated
- **Rationale**: Enables safe retries in distributed systems with transient
  failures
- **Evidence**: Stripe/PayPal require idempotency keys for payment APIs;
  99.99% consistency achieved [Ref: Stripe-API-Docs]
- **Implications**: Developers must generate unique keys; Ops can retry safely;
  Users avoid duplicate charges
- **Limitations**: Requires storage for deduplication; TTL needed for cleanup;
  not suitable for non-deterministic operations
- **Alternatives**: Use exactly-once semantics (Kafka, Pulsar) if message queue
  supports it; use distributed transactions (2PC) for strict consistency

### Fairness and Balanced Perspectives

**For Contentious Topics** (e.g., microservices vs monoliths, SQL vs NoSQL):

- MUST present ≥2 perspectives with citations
- MUST acknowledge trade-offs explicitly
- MUST identify when each approach is preferable
- SHOULD cite counterarguments from credible sources

**Bias and Limitations Template** (SHOULD include in answers when applicable):

- **Known Limitations**: Technical constraints, scalability bounds, cost factors
- **Trade-offs**: What is sacrificed (e.g., consistency for availability)
- **Counterarguments**: Alternative views with citations
- **Context Boundaries**: When to choose alternatives ("Use X when...; avoid X
  when...")

## Scope & Coverage

**Output**: 30 Q&As (6/12/12 Foundational/Intermediate/Advanced)
**Domains**: Regulatory, Business, Market, Technical, Data, Organizational,
NFR (10 sub-dimensions), Process, Hybrid

**MECE Statement**: The 11 domains are mutually exclusive (non-overlapping) and
collectively exhaustive (complete coverage). Hybrid domain handles cross-domain
patterns.

## Pattern Quality Criteria (7 Mandatory)

Each pattern MUST satisfy ALL 7 criteria below. Use the checklist to verify
completeness.

### 1. Reusability

**Definition**: Pattern MUST be applicable in ≥2 distinct contexts with clear
adaptation points.

**Required Details**:

- List ≥2 concrete contexts (e.g., e-commerce, fintech, healthcare)
- Identify adaptation points (what varies by context)
- Provide context-specific examples

**Checklist**:

- [ ] ≥2 contexts explicitly named
- [ ] Adaptation points identified
- [ ] Context-specific examples provided

### 2. Proven Effectiveness

**Definition**: Pattern MUST have empirical evidence of success (company adoption,
quantitative metrics, or documented case studies).

**Required Details**:

- Company/organization names using the pattern
- Quantitative metrics (% improvement, scale achieved, adoption rate)
- Citation to case study or authoritative source

**Checklist**:

- [ ] ≥1 company/organization named
- [ ] ≥1 quantitative metric cited
- [ ] Authoritative source cited [Ref: ID]

### 3. Cross-Context Applicability (Boundaries)

**Definition**: Pattern MUST define boundaries clearly (when applicable / when NOT
applicable).

**Required Details**:

- "Applies when" conditions (use cases, scale, constraints)
- "Avoid when" conditions (anti-use cases, limitations)
- Edge cases and boundary examples

**Checklist**:

- [ ] "Applies when" conditions stated
- [ ] "Avoid when" conditions stated
- [ ] ≥1 boundary example provided

### 4. Multi-Stakeholder Value

**Definition**: Pattern MUST benefit ≥2 distinct stakeholder groups.

**Required Details**:

- List ≥2 stakeholder groups (e.g., Developers, Ops, Business, Users,
  Compliance, Security)
- Describe value/benefit to each stakeholder
- Cite perspective-specific concerns

**Checklist**:

- [ ] ≥2 stakeholder groups named
- [ ] Value to each stakeholder described
- [ ] Stakeholder concerns addressed

### 5. Functional + NFR Coverage

**Definition**: Pattern MUST address both functional capability (what it does) and
Non-Functional Requirements (quality attributes like performance, security,
scalability).

**Required Details**:

- Functional capability description
- NFR attributes covered (performance, security, scalability, reliability, etc.)
- Quantitative NFR metrics (latency, throughput, uptime, etc.)

**Checklist**:

- [ ] Functional capability described
- [ ] ≥1 NFR attribute identified
- [ ] NFR metrics provided (with units)

### 6. Trade-off Analysis

**Definition**: Pattern MUST explicitly state benefits vs. sacrifices (costs,
complexity, performance, consistency, etc.).

**Required Details**:

- Benefits gained (capabilities, quality attributes)
- Sacrifices made (what is given up or increased: complexity, cost, latency, etc.)
- Comparative analysis ("improves X at the expense of Y")

**Checklist**:

- [ ] ≥1 benefit stated
- [ ] ≥1 sacrifice stated
- [ ] Comparative framing used

### 7. Anti-Pattern Awareness

**Definition**: Pattern MUST identify failure modes (how it can go wrong) and
exclusion criteria (when NOT to use it).

**Required Details**:

- Common failure modes (misconfigurations, misuse, pitfalls)
- Exclusion criteria ("do not use when...")
- Mitigation strategies for known failure modes

**Checklist**:

- [ ] ≥1 failure mode identified
- [ ] Exclusion criteria stated
- [ ] Mitigation strategies provided

### Pattern Criteria Mapping Table

| Criterion                   | Where It Appears in Output        | Validation Method              |
| --------------------------- | --------------------------------- | ------------------------------ |
| 1. Reusability              | Q&A Answer, Pattern Catalog       | Count contexts (≥2)            |
| 2. Proven Effectiveness     | Q&A Answer, Pattern Catalog       | Verify citations + metrics     |
| 3. Applicability Boundaries | Q&A Answer, Key Insight           | Check "applies/avoid when"     |
| 4. Multi-Stakeholder        | Pattern Domains table, Q&A Answer | Count stakeholders (≥2)        |
| 5. Functional + NFR         | Supporting Artifacts table        | Verify functional + NFR        |
| 6. Trade-offs               | Q&A Answer, Bias & Limitations    | Check "benefits vs sacrifices" |
| 7. Anti-Patterns            | Q&A Answer, Alternatives          | Check failure modes listed     |

## Pattern Domains

| Domain                  | Examples                                              | Stakeholders                     |
| ----------------------- | ----------------------------------------------------- | -------------------------------- |
| **Regulatory**          | Audit trails, Consent, Data residency                 | Compliance, Legal, Developers    |
| **Business**            | Subscription, Freemium, Platform                      | Executives, Product, Finance     |
| **Market**              | Blue Ocean, Disruptive Innovation, Land & Expand      | Executives, Marketing, Product   |
| **Technical**           | GoF patterns, Repository, Strangler Fig               | Developers, Architects           |
| **Data**                | Polyglot Persistence, Event Sourcing, CQRS, Data Lake | Data Engineers, DBAs, Architects |
| **Organizational**      | Conway's Law, Team Topologies, DevOps                 | Managers, Executives, Team Leads |
| **NFR-Security**        | Zero-Trust, Defense-in-Depth, Secrets Mgmt            | Security, Compliance             |
| **NFR-Performance**     | Caching, Connection Pooling, CDN                      | Developers, Operations           |
| **NFR-Availability**    | Circuit Breaker, Bulkhead, Health Checks              | Operations, Business             |
| **NFR-Reliability**     | Retry+Backoff, Idempotency, Saga                      | Developers, Operations           |
| **NFR-Scalability**     | Horizontal Scaling, Sharding, CQRS                    | Architects, Operations           |
| **NFR-Observability**   | Distributed Tracing, Metrics, Logging                 | Operations, Developers           |
| **NFR-Adaptability**    | Feature Flags, Strategy, Plugin Arch                  | Developers, Product              |
| **NFR-Extensibility**   | DI, Open-Closed, Middleware                           | Developers, Architects           |
| **NFR-Maintainability** | SOLID, Clean Architecture                             | Developers, Architects           |
| **NFR-Testability**     | Test Doubles, Contract Testing                        | Developers, QA                   |
| **Process**             | Agile, Retrospectives, Incident Response              | Teams, Managers                  |
| **Hybrid**              | Regulatory+Technical, Compliance-by-Design            | Compliance, Developers           |

### Domain Boundaries (MECE Enforcement)

**Regulatory**: Legal/compliance-driven patterns. **In-scope**: Audit, consent,
data residency, breach notification, retention policies. **Out-of-scope**:
Technical implementation details (see Technical/NFR-Security), business models
(see Business).

**Business**: Revenue models and value propositions. **In-scope**: Subscription,
freemium, marketplace, pricing strategies. **Out-of-scope**: Market positioning
(see Market), operational processes (see Process).

**Market**: Competitive strategy and market positioning. **In-scope**: Blue Ocean,
disruptive innovation, market entry, competitive advantage. **Out-of-scope**:
Revenue mechanics (see Business), internal team structure (see Organizational).

**Technical**: Software architecture and design patterns. **In-scope**: GoF patterns,
architectural styles (layered, microservices), integration patterns. **Out-of-scope**:
Quality attributes (see NFR-\*), data-specific patterns (see Data).

**Data**: Data storage, modeling, and processing patterns. **In-scope**: Polyglot
persistence, event sourcing, CQRS, data lakes, data warehouses, ETL/ELT.
**Out-of-scope**: Query performance optimization (see NFR-Performance), access
control (see NFR-Security).

**Organizational**: Team structure and collaboration patterns. **In-scope**: Conway's
Law, Team Topologies, two-pizza teams, communication structures. **Out-of-scope**:
Specific workflows (see Process), individual practices (see Process).

**NFR (10 sub-dimensions)**: Quality attribute patterns. Each sub-dimension
addresses one quality concern. **Edge cases**: When a pattern spans multiple NFR
domains (e.g., Circuit Breaker for both Availability and Reliability), classify by
primary intent or list in multiple domains.

**Process**: Workflow and methodology patterns. **In-scope**: Agile, Scrum,
retrospectives, incident response, CI/CD workflows. **Out-of-scope**: Team
structure (see Organizational), tooling (see Technical/NFR-Observability).

**Hybrid**: Patterns spanning ≥2 domains. **In-scope**: Compliance-by-Design
(Regulatory + Technical), Privacy-Preserving Analytics (Regulatory + Data),
Security-First Architecture (NFR-Security + Technical). **Usage**: Use sparingly;
prefer single domain when primary intent is clear.

## Pattern Catalog (70+ Patterns)

| Domain                  | Pattern                  | Contexts                                | Effectiveness Evidence                          | Key Stakeholders                     |
| ----------------------- | ------------------------ | --------------------------------------- | ----------------------------------------------- | ------------------------------------ |
| **Regulatory**          | Double-Entry Audit Trail | Financial, Healthcare, Blockchain, GDPR | SOX required, all major banks                   | Compliance, Developers, Auditors     |
|                         | Consent Management       | GDPR, CCPA, Marketing, Healthcare       | 10K+ orgs, 85% risk reduction                   | Legal, End Users, Developers         |
|                         | Data Residency           | Multi-region cloud, Fintech, Gov        | AWS/Azure/GCP standard                          | Compliance, Ops, Business            |
| **Business**            | Subscription Model       | SaaS, Media, Retail, B2B/B2C            | $1.5T economy, 5-7x valuations                  | Finance, Product, Customers          |
|                         | Freemium                 | Dev tools, Productivity, Storage        | Slack 30%, Dropbox $2B                          | Marketing, Product, Users            |
|                         | Platform/Marketplace     | Airbnb, AWS, App Store, Stripe          | 7/10 top companies, 70% margins                 | Business, Producers, Consumers       |
| **Market**              | Blue Ocean Strategy      | New categories, Saturated markets       | Cirque $800M, Wii 100M units                    | Executives, Product, Marketing       |
|                         | Disruptive Innovation    | Tech transitions, Market entry          | Netflix/Tesla, 30+ industries                   | Executives, Investors, Market        |
|                         | Land and Expand          | Enterprise SaaS, B2B                    | Slack/Dropbox, 120%+ retention                  | Sales, Product, Finance              |
| **Technical**           | Repository               | DDD, Layered arch, Microservices        | 60-80% coupling reduction                       | Developers, Architects, Ops          |
|                         | Strangler Fig            | Legacy modernization, Migration         | Amazon/GitHub, 90% risk reduction               | Architects, Ops, Business            |
| **NFR-Security**        | Defense-in-Depth         | Enterprise, Cloud, IoT                  | 90% attack reduction, 95% F500                  | Security, Compliance, Ops            |
|                         | Zero-Trust               | Remote work, Cloud-native, APIs         | Google 7yr/85K, 75% breach impact               | Security, Developers, Users          |
|                         | Secrets Management       | Cloud, Microservices, CI/CD             | 30M+ Vault, 50% F500                            | Security, Developers, Ops            |
| **NFR-Performance**     | Caching                  | Web apps, APIs, Databases               | 40-60% latency↓, 10x throughput                 | Users, Developers, Ops               |
|                         | Connection Pooling       | DB, HTTP, Message queues                | 10-100x gain, DB standard                       | Developers, Ops, Users               |
|                         | CDN                      | Static assets, Video, APIs              | 50-70% latency↓, 70% top sites                  | Users, Business, Ops                 |
| **NFR-Availability**    | Circuit Breaker          | Microservices, Distributed systems      | Netflix 99.99% uptime                           | Ops, Developers, Users               |
|                         | Bulkhead                 | Thread/Connection pools, Multi-tenant   | Netflix/AWS, 80% capacity maintained            | Ops, Architects, Business            |
|                         | Health Check             | K8s, Load balancers, Service mesh       | 70% MTTR↓, <5s detection                        | Ops, Developers, Business            |
| **NFR-Reliability**     | Retry + Backoff          | Network, Message processing             | 95% recovery, AWS default                       | Developers, Ops, Users               |
|                         | Idempotency              | Payments, Message queues, APIs          | Stripe/PayPal required, 100% consistency        | Developers, Ops, Business            |
|                         | Saga                     | Microservices, Long transactions        | Uber/Airbnb standard                            | Architects, Developers, Ops          |
| **NFR-Scalability**     | Horizontal Scaling       | Web servers, APIs, Stateless            | Netflix/FB, 1000s instances                     | Ops, Architects, Business            |
|                         | DB Sharding              | High-traffic DB, Multi-tenant           | Instagram 4000, Discord billions                | DBAs, Developers, Business           |
|                         | CQRS                     | Read-heavy, Event sourcing              | 10-100x read scale, Azure/AWS                   | Architects, Developers, Ops          |
| **NFR-Observability**   | Distributed Tracing      | Microservices, Distributed              | Standard cloud-native                           | Ops, Developers, Business            |
| **NFR-Adaptability**    | Feature Flags            | CD, A/B testing, Canary                 | FB/Netflix 100+ deploys/day, 90% risk↓          | Developers, Product, Business        |
|                         | Strategy Pattern         | Payments, Pricing, Routing              | GoF 1994, 60% duplication↓                      | Developers, Business, Architects     |
|                         | Plugin Architecture      | IDEs, Browsers, CMS                     | VS Code 40K, WordPress 60K                      | Developers, Third-party, Users       |
| **NFR-Extensibility**   | Dependency Injection     | Enterprise, Frameworks                  | Spring 50% share, 70% coupling↓                 | Developers, Architects, Third-party  |
|                         | Open-Closed              | Libraries, Frameworks, APIs             | SOLID 1988, 80% regression bugs↓                | Developers, QA, Business             |
|                         | Middleware/Pipeline      | Web frameworks, Message processing      | Express 100K packages                           | Developers, Third-party, Ops         |
| **NFR-Maintainability** | SOLID Principles         | OOP, Enterprise apps                    | Since 2000, 40-60% defects↓, 25% velocity↑      | Developers, Architects, New hires    |
|                         | Clean Architecture       | DDD, Microservices                      | Netflix/Amazon, 70% coupling↓                   | Developers, Architects, Business     |
| **NFR-Testability**     | Test Doubles             | Unit/Integration testing                | 90%+ coverage, 100x faster                      | Developers, QA, Ops                  |
|                         | Contract Testing         | Microservices, APIs                     | Pact/IBM/Atlassian, 95% issues caught           | Developers, API consumers, Ops       |
| **Data**                | Polyglot Persistence     | Microservices, E-commerce               | Netflix 3+, LinkedIn 10+, 50-80% latency↓       | Architects, DBAs, Developers         |
|                         | Event Sourcing           | Finance, Collaboration                  | 100% audit, Banking standard                    | Compliance, Developers, Business     |
|                         | Data Lake                | Analytics, ML, Data science             | AWS/Azure/GCP, 90% F500                         | Data scientists, Engineers, Business |
| **Organizational**      | Conway's Law             | Any software org                        | 50+ years proven, 40% coordination↓             | Executives, Architects, Managers     |
|                         | Two-Pizza Team           | Product/Platform teams                  | Amazon 2002, 60% meetings↓, 30% velocity↑       | Managers, Developers, Executives     |
|                         | Team Topologies          | Any org, Enterprises                    | MS/Google/Spotify, 50% load↓, 40% flow↑         | CTOs, Managers, Developers           |
|                         | DevOps/YBIYRI            | Cloud-native, SaaS                      | Amazon 2006, 60% MTTR↓, 10x deploys             | Developers, Ops, Business            |
| **Process**             | Retrospective            | Agile/Project teams                     | Scrum core, 15-25% velocity↑, 30% satisfaction↑ | Teams, Managers, Individuals         |

## Pattern Selection Matrices

### Business Context

| Context         | B2B SaaS     | B2C Platform | Marketplace     | Open Source        |
| --------------- | ------------ | ------------ | --------------- | ------------------ |
| Revenue         | Subscription | Freemium/Ads | Transaction     | Support/Enterprise |
| Acquisition     | Sales-led    | Product-led  | Network effects | Community-led      |
| Time to Revenue | 3-6mo        | 0-3mo        | 6-12mo          | 6-18mo             |

### Regulatory Compliance

| Requirement         | GDPR (EU)       | CCPA (CA)   | HIPAA (Health) | SOC 2 (Enterprise) |
| ------------------- | --------------- | ----------- | -------------- | ------------------ |
| Data Residency      | Required        | Optional    | Required       | Optional           |
| Consent             | Explicit opt-in | Opt-out     | N/A            | N/A                |
| Audit Trail         | Required        | Recommended | Required       | Required           |
| Erasure             | Required        | Required    | Limited        | Not required       |
| Breach Notification | 72h             | Prompt      | 60d            | Contractual        |

### NFR Patterns by System Type

| NFR Sub-Dimension | High-Traffic API    | Financial       | Real-Time         | Data-Intensive  | Microservices     |
| ----------------- | ------------------- | --------------- | ----------------- | --------------- | ----------------- |
| NFR-Security      | Auth + Rate limit   | Encrypt + Audit | mTLS + Zero-trust | Encrypt at rest | Service mesh      |
| NFR-Performance   | CDN + Cache         | Connection pool | In-mem cache      | Query optimize  | Async messaging   |
| NFR-Availability  | Circuit breaker     | Active-active   | Redundancy        | Read replicas   | Health checks     |
| NFR-Reliability   | Retry + Idempotency | 2PC + Saga      | Idempotency       | Event sourcing  | Saga + Outbox     |
| NFR-Scalability   | Horizontal + CDN    | DB sharding     | CQRS + Shard      | Partitioning    | Independent scale |

## Citation Standards

**Languages**: ~60% EN, ~30% ZH, ~10% other (tagged [EN]/[ZH])
**Source Types**: Regulatory/legal, Business/strategic, Technical,
Process/organizational, Empirical validation
**Format**: APA 7th with language tags
**Inline**: [Ref: ID] after claims, requirements, effectiveness, trade-offs

### Citation Format Specification

**Full Citation** (in Citations section):

- **Format**: Author/Organization. (Year). _Title_ [Edition/Version]. URL or DOI.
  [Language tag]
- **Example**: Fowler, M. (2018). _Refactoring: Improving the Design of Existing
  Code_ (2nd ed.). Addison-Wesley. https://martinfowler.com/books/refactoring.html
  [EN]

**Inline Citation**: [Ref: CitationID] where CitationID matches ID in Citations
section (e.g., A1, A2, L1, L2)

### Link Management and Recency

**Link Requirements**:

- Prefer direct official sources (Tier 1-2) over aggregators
- For standards: Include version/edition number in citation
- For tools: Note last verified date in Tools section
- For APIs/docs: Use versioned URLs when available (e.g., `/v2/` not `/latest/`)

**Handling Link Rot**:

- If original link is dead, use archived version (https://web.archive.org)
- Note archived date: "[Archived 2024-01-15]"
- If no archive exists, cite secondary source with note: "[Original source
  unavailable; cited via SecondarySource]"

**Recency Expectations**:

- Fast-moving domains (cloud, JS frameworks, AI/ML): <3 years preferred
- Stable domains (algorithms, patterns, theory): <10 years acceptable
- Regulatory: Must be current version of regulation; note effective date

## Reference Requirements

| Section    | Minimum | Content                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Glossary   | ≥25     | Regulatory (GDPR, CCPA, Consent, Audit Trail), Business (Freemium, Platform, Network Effects), Market (Blue Ocean, Disruptive Innovation), Technical (Repository, Strangler Fig), Data (Polyglot, Event Sourcing, Data Lake, CQRS), Organizational (Conway's Law, Team Topologies, Two-Pizza, DevOps), NFR (Circuit Breaker, Caching, Retry, Idempotency, Sharding, Zero-Trust, Feature Flags, DI, SOLID, Test Doubles) |
| Tools      | ≥10     | Compliance (OneTrust), Business (Strategyzer), Patterns (GoF, POSA), Data (dbt, Databricks, Snowflake), Org (Team Topologies), Process (BPMN.io, Miro), Monitoring (Prometheus, Grafana), Security (Vault, OWASP ZAP), Testing (Pact)                                                                                                                                                                                   |
| Literature | ≥12     | Regulatory (GDPR, NIST), Business (Osterwalder, Porter), Market (Blue Ocean, Innovator's Dilemma), Patterns (GoF, Fowler, POSA), Data (Kleppmann, Kimball), Organizational (Skelton, Forsgren), NFR (Nygard, Google SRE)                                                                                                                                                                                                |
| Citations  | ≥12     | Distinct from Literature; ~60% EN / ~30% ZH / ~10% other (APA 7th with tags)                                                                                                                                                                                                                                                                                                                                            |

**Exception**: If unmet, document shortfall + rationale + sourcing plan.

## Usage Guidelines

**DO**:

- Start with context and assumptions before diving into patterns
- Use RFC 2119 modal verbs (MUST/SHOULD/MAY) consistently
- Cite critical claims with Tier 1-2 sources; cross-verify with 2nd source
- Apply reasoning template (Claim → Rationale → Evidence → Implications →
  Limitations → Alternatives)
- Present ≥2 stakeholder perspectives for each pattern
- Include concrete examples with code/YAML/diagrams appropriate to domain
- Define boundaries explicitly ("Applies when..."; "Avoid when...")
- Document trade-offs ("Improves X at the expense of Y")
- Keep lines ≤120 characters; use bullets for lists

**DON'T**:

- Use vague terms ("as needed", "where appropriate", "etc.") without clarification
- Cite low-credibility sources (Tier 5) for critical claims
- Omit failure modes and anti-patterns
- Present patterns as universally applicable without boundaries
- Mix terminology (use "Q&A" not "QA" or "question-answer")
- Exceed 20% nice-to-have content in any section
- Use dead links; prefer archived links or secondary sources if original unavailable

**Per Q&A Cluster Requirements**:

1. MECE structure, 6/12/12 F/I/A balance, all domains covered
2. Per cluster: ≥1 Mermaid + example + table + metric; ≥2 sources + tool + validation
3. All minimums met; gaps documented with remediation

## Quality Gates

**Categories**: Recency, Diversity, Evidence, Tool details, Links, Cross-refs
**Thresholds**: Defined in Validation Steps (Part I)

## Validation Checklist (21 Steps)

### Reference Counts (Steps 1-7)

1. Glossary ≥25, Tools ≥10, Literature ≥12, Citations ≥12, Q&As 30 (6/12/12 F/I/A)
2. Citations: ≥70% answers ≥1, ≥30% ≥2
3. Language: EN 50-70%, ZH 20-40%, Other 5-15%
4. Recency: ≥50% last 3yr (≥70% digital/cloud)
5. Diversity: ≥3 source types, no single >25%
6. Links: All accessible/archived
7. Cross-refs: All [Ref: ID] resolve; Tools: pricing + adoption + update <18mo

### Content Quality (Steps 8-12)

8. Word count: 5 samples, all 150-300
9. Key insights: All concrete (boundaries/trade-offs/effectiveness/anti-patterns)
10. Per-topic: ≥2 sources + ≥1 tool
11. Pattern mapping: ≥80% pattern → implementation trace
12. Judgment: ≥70% scenario-based (not recall)

### Pattern Quality (Steps 13-21)

13. Visual: ≥90% diagram + example + table + metric
14. Application: ≥80% patterns with evidence
15. Quantitative: ≥60% metrics/formulas
16. Examples: ≥80% domain-appropriate
    17-21. **7 Pattern Criteria**: ≥80% answers meet all (see Quality Standards)

### Validation Report Template

| Step  | Check                | Result                                 | Status    |
| ----- | -------------------- | -------------------------------------- | --------- |
| 1     | Ref Counts           | G:X T:Y L:Z A:W Q:N (F/I/A)            | PASS/FAIL |
| 2     | Citations            | X% ≥1, Y% ≥2                           | PASS/FAIL |
| 3     | Language             | EN:X% ZH:Y% Other:Z%                   | PASS/FAIL |
| 4     | Recency              | X% last 3yr                            | PASS/FAIL |
| 5     | Diversity            | N types, max P%                        | PASS/FAIL |
| 6     | Links                | Y/X accessible                         | PASS/FAIL |
| 7     | Cross-refs + Tools   | Y/X resolved, pricing/adoption/recency | PASS/FAIL |
| 8     | Word count           | 5/5 in 150-300                         | PASS/FAIL |
| 9     | Key insights         | Y/X concrete                           | PASS/FAIL |
| 10    | Per-topic refs       | X/Y meet min                           | PASS/FAIL |
| 11    | Pattern mapping      | X% explicit                            | PASS/FAIL |
| 12    | Judgment focus       | X% scenario                            | PASS/FAIL |
| 13    | Visual coverage      | X% complete                            | PASS/FAIL |
| 14    | Pattern application  | X% w/ evidence                         | PASS/FAIL |
| 15    | Quantitative         | X% w/ metrics                          | PASS/FAIL |
| 16    | Examples             | X% concrete                            | PASS/FAIL |
| 17-21 | Pattern Criteria (7) | X% meet all                            | PASS/FAIL |

**MANDATORY**: If ANY FAIL, fix and re-validate until 100% PASS.

## Submission Checklist

- [ ] All 21 validation steps PASS
- [ ] All minimums + quality gates met
- [ ] ≥80% answers meet all 7 pattern criteria

## Part I Self-Review Checklist

Before proceeding to Part II, verify:

**Terminology & Consistency**:

- [ ] RFC 2119 modal verbs used consistently (MUST/SHOULD/MAY)
- [ ] Normalized terms followed (Q&A, pattern, stakeholder, evidence, citation,
      domain)
- [ ] No terminology drift across sections

**Evidence & Credibility**:

- [ ] Critical claims have ≥1 Tier 1-2 citation
- [ ] Critical claims cross-verified with ≥2 independent sources where applicable
- [ ] Source tiers appropriate for claim types
- [ ] Links direct to authoritative sources; dead links archived or noted

**Significance & Structure**:

- [ ] Critical requirements clearly distinguished from nice-to-have
- [ ] Nice-to-have content <20% of any section
- [ ] Pruning guideline applied to verbose sections

**Reasoning & Fairness**:

- [ ] Reasoning template applied to pattern explanations
- [ ] ≥2 perspectives presented for contentious topics
- [ ] Trade-offs explicitly stated (benefits vs. sacrifices)
- [ ] Limitations and counterarguments acknowledged

**Pattern Criteria & Boundaries**:

- [ ] All 7 mandatory criteria defined with checklists
- [ ] Domain boundaries (MECE) clearly stated
- [ ] In-scope/Out-of-scope documented for each domain

**Common Failure Modes**:

- Vague language ("as needed") without clarification → Replace with concrete
  criteria
- Missing evidence for critical claims → Add Tier 1-2 citations
- Overlooked anti-patterns → Add failure modes + exclusion criteria
- Unclear boundaries → Add "Applies when / Avoid when" statements

---

# Part II: Workflow

## Roles (Virtual or Assigned)

**Editor**: Overall structure, consistency, flow
**Fact-Checker**: Evidence verification, citation accuracy, cross-checking
**Terminology Steward**: RFC 2119 compliance, normalized term usage
**QA Validator**: 21-step validation execution, threshold compliance

## Stage-Gate Workflow

### Stage A: Plan

**Objectives**: Establish context, verify MECE coverage, ensure criteria
completeness.

**Tasks**:

1. Review context, scope, constraints, assumptions (from preface)
2. Select 8-12 pattern clusters from 11 domains
3. Allocate Q&As per cluster (total 30: 6 Foundational, 12 Intermediate,
   12 Advanced)
4. Verify domain MECE compliance (no overlaps, complete coverage)
5. Confirm all 7 mandatory pattern criteria are understood

**Gate Criteria**:

- [ ] 8-12 clusters selected, spanning all 11 domains
- [ ] 30 Q&As allocated with 6/12/12 F/I/A distribution
- [ ] Domain boundaries reviewed; MECE compliance confirmed
- [ ] All 7 pattern criteria checklists ready

### Stage B: Draft

**Objectives**: Generate Q&As, collect references, create supporting artifacts.

**Tasks**:

1. **References**: Collect ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations
   - Verify language distribution (~60% EN, ~30% ZH, ~10% other)
   - Verify recency (≥50% <3 years for fast-moving domains)
   - Check credibility tiers (prefer Tier 1-2 for critical claims)
2. **Q&As**: Write scenario-based questions with answers
   - Apply reasoning template (Claim → Rationale → Evidence → Implications →
     Limitations → Alternatives)
   - Include ALL 7 criteria per pattern
   - Add ≥1 [Ref: ID] inline citation per answer
   - Provide concrete examples (code, YAML, diagrams)
   - Present ≥2 stakeholder perspectives
   - Validate incrementally every 5 Q&As
3. **Visuals**: Per cluster create Mermaid + example + table + metric
   - Align with domain-specific supporting artifacts table
   - Verify functional + NFR coverage

**Gate Criteria**:

- [ ] All 30 Q&As drafted with 150-300 words each
- [ ] Reference minimums collected (≥25/≥10/≥12/≥12)
- [ ] Language distribution ~60/30/10 EN/ZH/other
- [ ] Recency ≥50% <3 years
- [ ] ≥1 Mermaid + example + table + metric per cluster
- [ ] Inline citations [Ref: ID] present in ≥70% of answers

### Stage C: Validate

**Objectives**: Execute 21-step validation, run optional tooling, fix failures.

**Tasks**:

1. Execute all 21 validation steps (see Validation Checklist)
2. Verify measurable acceptance checks beneath each step
3. Run optional tooling (if available):
   - `npx markdownlint-cli2 "Prompts/Pattern/QA.md"`
   - `npx markdown-link-check Prompts/Pattern/QA.md`
   - `npx prettier -w "Prompts/Pattern/QA.md"`
4. Document failures in validation report table
5. Fix all failures
6. Re-validate until 100% PASS

**Gate Criteria**:

- [ ] All 21 validation steps show PASS
- [ ] No broken links (all accessible or archived)
- [ ] Markdownlint passes (if run)
- [ ] No TODOs or placeholders remain
- [ ] ≥80% of answers meet all 7 pattern criteria

### Stage D: Finalize

**Objectives**: Resolve remaining issues, complete self-review, prepare
submission.

**Tasks**:

1. Complete Part I, II, III self-review checklists
2. Verify preserved constraints:
   - 3-part structure intact
   - 30 Q&As with 6/12/12 F/I/A distribution
   - 21 validation steps verbatim
   - 70+ patterns in catalog
   - Reference minimums met
   - Domain-specific artifacts table present
3. Ensure evidence present for 100% of critical claims
4. Verify MECE domain boundaries documented
5. Verify pattern criteria mapping table present
6. Final submission checklist review

**Gate Criteria**:

- [ ] All self-review checklists completed
- [ ] All preserved constraints verified
- [ ] 100% critical claims have evidence
- [ ] Submission checklist shows 100% completion

## Generation Steps (Legacy - Use Stage-Gate Workflow Above)

1. **Pattern Selection**: Select 8-12 clusters from 11 domains, allocate 2-4 Q&As
   each (30 total, 6/12/12 F/I/A). Verify coverage.

2. **References**: Collect minimums (≥25 glossary, ≥10 tools, ≥12 literature,
   ≥12 citations). Verify 60/30/10 language, ≥50% recency.

3. **Q&As**: Write scenario-based questions. Per answer: ALL 7 criteria +
   ≥1 [Ref: ID] + example. Validate every 5 Q&As.

4. **Visuals**: Per cluster: Mermaid + example + table + metric (see Supporting
   Artifacts). Verify alignment.

5. **Resolve**: Populate sections, resolve [Ref: ID]. Verify minimums.

6. **Validate**: Execute 21 steps, fix failures, re-validate to 100% PASS.

7. **Submit**: Verify checklist, submit when PASS.

## Part II Self-Review Checklist

Before proceeding to Part III, verify:

**Stage-Gate Completion**:

- [ ] Stage A (Plan) gate criteria met
- [ ] Stage B (Draft) gate criteria met
- [ ] Stage C (Validate) gate criteria met
- [ ] Stage D (Finalize) gate criteria met

**Role Responsibilities**:

- [ ] Editor: Structure and flow reviewed
- [ ] Fact-Checker: All citations verified, cross-checks completed
- [ ] Terminology Steward: RFC 2119 and normalized terms applied consistently
- [ ] QA Validator: 21-step validation executed and passed

**Common Failure Modes**:

- Incomplete pattern criteria → Use 7-criteria checklists per pattern
- Missing inline citations → Add [Ref: ID] for all non-obvious claims
- Validation failures → Fix and re-validate; do not proceed with failures
- Tooling errors → Run markdownlint/link-check; fix issues before submit

---

# Part III: Output Structure

## **MANDATORY: Table of Contents**

Every output MUST begin with a comprehensive Table of Contents (TOC) titled
"## Contents" that links to all top-level headings and major sections.

**TOC MUST Include**:

- Topic Areas (with Q1-Q30 overview)
- Each Topic with Q# range
- Reference Sections (Glossary, Tools, Literature, Citations)
- Validation Report

**TOC Verification Checklist**:

- [ ] TOC present as ## Contents
- [ ] All 11 topic domains listed with Q# ranges
- [ ] 30 total Q&As distributed as 6/12/12 F/I/A
- [ ] Reference sections linked (Glossary, Tools, Literature, Citations)
- [ ] Validation Report section linked

## Output Skeleton (Canonical Structure)

Every output MUST follow this structure:

```markdown
# [Title]

## Contents

- [Topic Areas](#topic-areas) - Q1-30 Overview
- [Topic 1: Domain Name](#topic-1) (Q1-QX) [F/I/A counts]
- ...
- [Topic 11: Domain Name](#topic-11) (QY-Q30) [F/I/A counts]
- [Reference Sections](#reference-sections)
  - [Glossary](#glossary) (≥25 entries)
  - [Tools](#tools) (≥10 entries)
  - [Literature](#literature) (≥12 entries)
  - [Citations](#citations) (≥12 entries)
- [Validation Report](#validation-report) - 21-step results

## Context and Assumptions

[Brief scope, constraints, target audience]

## Topic Areas

[Table showing 11 domains with Q# ranges, counts, F/I/A distribution]

## Topic 1: [Domain Name]

### Q1: [Question]

**Difficulty**: [Foundational/Intermediate/Advanced]
**Type**: [Domain]
**Key Insight**: [Pattern boundaries/trade-offs/effectiveness/anti-patterns]
**Answer**: [150-300 words with reasoning template, inline citations [Ref: ID]]
**Pattern Quality** (ALL 7 criteria):

1. Reusability: ...
2. Proven Effectiveness: ...
3. Applicability: ...
4. Multi-Stakeholder: ...
5. Functional + NFR: ...
6. Trade-offs: ...
7. Anti-Patterns: ...
   **Concrete Example**: [code/YAML/diagram]
   **Supporting Artifacts**: [Mermaid diagram + table + metrics]

[Repeat for Q2-Q30]

## Reference Sections

### Glossary (≥25 entries)

[Alphabetical, with definitions and [Language] tags]

### Tools (≥10 entries)

[With features, pricing, adoption, last verified date, URL]

### Literature (≥12 entries)

[APA 7th format with [Language] tags]

### Citations (≥12 entries)

[APA 7th format with [Language] tags; IDs match inline [Ref: ID]]

## Validation Report

[21-step validation results table showing PASS/FAIL]
```

**Verification Checklist for Output Structure**:

- [ ] TOC present and complete
- [ ] Context and Assumptions section present
- [ ] Topic Areas table present with 11 domains
- [ ] 30 Q&As present (6 F, 12 I, 12 A)
- [ ] Each Q&A includes all 7 pattern criteria
- [ ] Glossary ≥25 entries
- [ ] Tools ≥10 entries
- [ ] Literature ≥12 entries
- [ ] Citations ≥12 entries
- [ ] Validation Report present with 21 steps

## Q&A Design Framework

Pattern Recognition → Applicability → Implementation → Validation

**Focus**: Scenario-based (not recall), pattern application with all 7 criteria

## Format Structure

- Use lists tables diagrams formulas code blocks; diagrams in Mermaid; code with
  language-tagged fences.
- Keep lines ≤120 characters
- Use bullets for lists; numbered lists for ordered steps

```markdown
## Contents

- [Topic Areas](#topic-areas) - Q1-30 Overview
- [Topic 1: Regulatory Patterns](#topic-1) (Q1-Q3)
- [Topic 2: Business & Market Patterns](#topic-2) (Q4-Q6)
- [Topic 3: Technical Patterns](#topic-3) (Q7-Q8)
- [Topic 4: Data Patterns](#topic-4) (Q9-Q11)
- [Topic 5: Organizational Patterns](#topic-5) (Q12-Q14)
- [Topic 6: NFR - Security, Reliability & Observability](#topic-6) (Q15-Q17)
- [Topic 7: NFR - Performance, Scalability & Availability](#topic-7) (Q18-Q20)
- [Topic 8: NFR - Adaptability, Flexibility & Extensibility](#topic-8) (Q21-Q23)
- [Topic 9: NFR - Maintainability & Testability](#topic-9) (Q24-Q26)
- [Topic 10: Process Patterns](#topic-10) (Q27-Q28)
- [Topic 11: Hybrid Patterns](#topic-11) (Q29-Q30)
- [Reference Sections](#reference-sections)
  - [Glossary](#glossary) (≥25 entries)
  - [Tools](#tools) (≥10 entries)
  - [Literature](#literature) (≥12 entries)
  - [Citations](#citations) (≥12 entries)
- [Validation Report](#validation-report) - 21-step results
```

## Topic Areas

| Domain                                        | Range   | Count  | F/I/A       | Examples                                |
| --------------------------------------------- | ------- | ------ | ----------- | --------------------------------------- |
| Regulatory                                    | Q1-Q3   | 3      | 0/1/2       | GDPR, Consent, Audit                    |
| Business & Market                             | Q4-Q6   | 3      | 1/2/0       | Subscription, Blue Ocean, Land & Expand |
| Technical                                     | Q7-Q8   | 2      | 0/1/1       | Repository, Strangler Fig               |
| Data                                          | Q9-Q11  | 3      | 1/1/1       | Polyglot, Event Sourcing, CQRS          |
| Organizational                                | Q12-Q14 | 3      | 1/1/1       | Conway, Team Topologies, DevOps         |
| NFR: Security, Reliability, Observability     | Q15-Q17 | 3      | 0/1/2       | Zero-Trust, Retry, Tracing              |
| NFR: Performance, Scalability, Availability   | Q18-Q20 | 3      | 0/1/2       | Caching, Sharding, Circuit Breaker      |
| NFR: Adaptability, Flexibility, Extensibility | Q21-Q23 | 3      | 1/1/1       | Feature Flags, DI, Middleware           |
| NFR: Maintainability, Testability             | Q24-Q26 | 3      | 1/1/1       | SOLID, Clean Arch, Test Doubles         |
| Process                                       | Q27-Q28 | 2      | 1/1/0       | Retrospectives, Incident Response       |
| Hybrid                                        | Q29-Q30 | 2      | 0/1/1       | Multi-domain patterns                   |
| **Total**                                     |         | **30** | **6/12/12** |                                         |

---

## Topic 1

### Q1: [Question Text]

**Difficulty**: [Foundational/Intermediate/Advanced]
**Type**: [Regulatory/Business/Market/Technical/Data/Organizational/NFR-Security/NFR-Performance/NFR-Availability/NFR-Reliability/NFR-Scalability/NFR-Observability/NFR-Adaptability/NFR-Extensibility/NFR-Maintainability/NFR-Testability/Process/Hybrid]
**Domain**: [Specify primary domain and sub-category]

**Key Insight**: [Pattern boundaries/trade-offs/effectiveness/anti-patterns exposed]

**Answer**: [150-300 words, [Ref: ID] citations, pattern → implementation with evidence]

**Pattern Quality** (ALL 7 criteria required - use checklists from Part I):

1. **Reusability**: ≥2 contexts + adaptation points
   - Example: "E-commerce, fintech, healthcare; adaptation: currency handling,
     regulatory compliance"
2. **Proven Effectiveness**: Evidence with quantitative metrics + citations
   - Example: "Stripe/Square require idempotency; 99.99% consistency; $10B+
     transactions/year [Ref: A1]"
3. **Applicability Boundaries**: When applicable / when NOT applicable
   - Example: "Applies: >100 req/sec, distributed systems; Avoid: single-instance
     CRUD apps, deterministic batch jobs"
4. **Multi-Stakeholder Value**: ≥2 stakeholder groups with specific benefits
   - Example: "Developers: safe retry logic; Ops: reduced incident load; Business:
     no duplicate charges; Users: reliable payments"
5. **Functional + NFR Coverage**: Capability + quality attributes with metrics
   - Example: "Functional: duplicate request handling; NFR: 99.99% consistency,
     <10ms overhead, 30-day dedup window"
6. **Trade-offs**: Benefits vs. sacrifices (explicit comparative framing)
   - Example: "Improves: availability (safe retries), correctness (no duplicates);
     Sacrifices: storage overhead (dedup keys), implementation complexity
     (key generation)"
7. **Anti-Patterns**: Failure modes + exclusion criteria + mitigations
   - Example: "Failure: key collision → duplicates; key expiry → false duplicates;
     Exclusion: non-deterministic ops (random data, timestamps); Mitigation: UUID v4
     keys, configurable TTL, server-side validation"

**Concrete Example**:

```language
// Domain-appropriate: code (technical), YAML (regulatory), model (business)
```

**Supporting Artifacts** (Domain-appropriate visuals):

| Domain                  | Diagrams                             | Examples                                  | Metrics                                  |
| ----------------------- | ------------------------------------ | ----------------------------------------- | ---------------------------------------- |
| **Regulatory**          | Compliance flow, Audit trail         | GDPR consent YAML, Policy docs            | Compliance %, Audit Completeness         |
| **Business**            | Business model canvas, Value chain   | Revenue models, Partnerships              | CLV, CAC, MRR                            |
| **Market**              | Blue Ocean canvas, Porter's 5 Forces | Market positioning, Competitive landscape | Market Share %, Value Innovation         |
| **Technical**           | Class/Sequence/Component             | Pattern code                              | Reusability %, Coupling                  |
| **Data**                | ERD, Data flow, Lineage              | DDL/SQL, Schema, Pipeline                 | Normalization (1NF-5NF), Query Perf      |
| **Organizational**      | Org chart, Team topology             | Team structure, Interaction modes         | Conway Alignment %, Cognitive Load       |
| **NFR-Security**        | Threat model, Auth flow              | Security config, Vault policies           | Attack Surface, Vulnerabilities          |
| **NFR-Performance**     | Flamegraph, Latency breakdown        | Optimization, Cache strategy              | Latency (p50/p95/p99), Throughput        |
| **NFR-Availability**    | Failure tree, Redundancy             | Circuit breaker, Health checks            | Uptime %, MTBF/MTTR                      |
| **NFR-Reliability**     | Retry flow, Saga                     | Idempotency keys, Retry logic             | Error Recovery %, Consistency            |
| **NFR-Scalability**     | Scaling strategy, Sharding           | Horizontal scaling, Shard design          | Scalability Factor, Linear Scaling %     |
| **NFR-Observability**   | Tracing, Metrics dashboard           | Distributed traces, Prometheus            | Trace Coverage %, MTTD                   |
| **NFR-Adaptability**    | Feature flags, Strategy              | Toggle code, Plugin API                   | Deployment Frequency, Lead Time          |
| **NFR-Extensibility**   | DI container, Extension points       | DI config, Middleware                     | Extension Points, 3rd-party Integrations |
| **NFR-Maintainability** | Clean architecture, SOLID            | Refactored code, Docs                     | Cyclomatic Complexity, Tech Debt %       |
| **NFR-Testability**     | Test pyramid, Mock architecture      | Test doubles, Pact contracts              | Coverage %, Test Exec Time               |
| **Process**             | BPMN workflow, Kanban                | Process docs, Runbooks                    | Cycle Time, Lead Time, Efficiency %      |
| **Hybrid**              | Cross-domain diagrams                | Multi-domain examples                     | Domain-specific + integration            |

## Reference Sections

### Glossary (≥25 entries)

**G1. GDPR (General Data Protection Regulation)**  
EU data protection framework. Patterns: consent, erasure, portability, breach notification (72h). Scope: EU residents [EN]

**G2. Consent Management**  
Explicit permission for data processing with granular controls. Components: opt-in/opt-out, purpose specification, withdrawal. Related: GDPR Art. 7, CCPA [EN]

**G3. Double-Entry Audit Trail**  
Every action logged with counterparty reference; immutable, tamper-evident. Use: finance, compliance, blockchain. Formula: `Audit Completeness = Logged/Total × 100%` [EN]

**G4. Freemium**  
Free basic tier + paid premium. Metrics: conversion %, CAC, CLV. Examples: Slack, Dropbox [EN]

**G5. Platform Business Model**  
Multi-sided marketplace. Key: network effects, transaction facilitation. Examples: Airbnb, AWS, App Store [EN]

**G6. Subscription Model**  
Recurring revenue with periodic billing. Benefits: predictable cash flow, retention focus. Metrics: MRR, churn, LTV. Examples: Netflix, Salesforce [EN]

**G7. Repository Pattern**  
Data access abstraction isolating persistence. Benefits: testability, technology independence. Use: DDD, layered architecture [EN]

**G8. Circuit Breaker**  
Failure isolation preventing cascades. States: closed, open, half-open. Metrics: error threshold, timeout, backoff. Use: microservices, distributed systems [EN]

**G9. Strangler Fig**  
Incremental legacy replacement by routing to new components. Benefits: risk reduction, continuous operation. Steps: identify, replace, retire [EN]

**G10. Two-Pizza Team**  
Team size ≤ two pizzas (~5-9 people). Benefits: fast decisions, clear ownership, reduced coordination. Origin: Amazon [EN]

**G11. Retrospective**  
Regular team reflection. Structure: what went well, what didn't, actions. Frequency: sprint/iteration end. Framework: Scrum [EN]

**G12. Conway's Law**  
"Organizations design systems mirroring their communication structure." Implication: align team boundaries with architecture. Related: Team Topologies [EN]

**G13. Network Effects**  
Value increases with user base. Types: direct (social), indirect (platforms). Formula: Metcalfe's Law `Value ∝ n²` [EN]

**G14. Right to Erasure**  
Data subject deletion request. Scope: GDPR Art. 17, CCPA. Exceptions: legal obligations, public interest. Implementation: cascading deletion, anonymization [EN]

**G15. CAC (Customer Acquisition Cost)**  
Cost per customer. Formula: `CAC = (Marketing + Sales) / New Customers`. Related: CLV, payback period [EN]

**G16. Caching**  
Store computed results to reduce latency/load. Types: in-memory (Redis, Memcached), CDN, application. Metrics: hit rate, TTL. Trade-off: staleness vs performance [EN]

**G17. Retry with Exponential Backoff**  
Handle transient failures with increasing delays. Formula: `Delay = BaseDelay × 2^Attempt`. Prevents thundering herd. Requires idempotency. Use: AWS SDK, gRPC [EN]

**G18. Idempotency**  
Operation produces same result when repeated. Implementation: idempotency keys, deduplication. Essential: retries, distributed systems, payments [EN]

**G19. Database Sharding**  
Horizontal partitioning across DBs. Strategies: range, hash, geographic. Trade-off: complexity vs scalability. Examples: Instagram, Discord [EN]

**G20. Zero-Trust Architecture**  
"Never trust, always verify." Principles: verify explicitly, least privilege, assume breach. Implementation: mTLS, identity-based access, micro-segmentation [EN]

**G21. Defense-in-Depth**  
Layered security. Layers: perimeter, network, host, application, data. Rationale: no single point of failure. Related: Swiss cheese model [EN]

**G22. Bulkhead**  
Isolate resources to prevent cascades. Named after ship compartments. Implementation: thread pools, connection pools, circuit breakers per dependency [EN]

**G23. Health Check**  
Continuous status monitoring. Types: liveness (running?), readiness (serve traffic?). Use: Kubernetes, load balancers. Response: HTTP 200/503 [EN]

**G24. Horizontal Scaling**  
Add instances for load. Benefits: linear capacity, fault tolerance. Requirements: stateless, load balancer. Formula: `Capacity = Instances × Throughput` [EN]

**G25. CQRS (Command Query Responsibility Segregation)**  
Separate read/write models for independent optimization. Benefits: read scalability, write optimization. Trade-off: eventual consistency, complexity [EN]

**G26. Polyglot Persistence**  
Different DBs for different needs. Rationale: right tool for job. Examples: PostgreSQL (relational), MongoDB (documents), Redis (cache), Neo4j (graph). Trade-off: complexity vs optimization [EN]

**G27. Event Sourcing**  
Store state changes as immutable event log. Benefits: complete audit, temporal queries, replay. Use: finance, collaboration. Trade-off: complexity vs auditability [EN]

**G28. Data Lake**  
Centralized raw data repository, schema-on-read. Benefits: flexibility, cost-effective. Platforms: AWS S3, Azure Data Lake, Databricks. Use: analytics, ML [EN]

**G29. Team Topologies**  
Four team types: Stream-Aligned (product), Platform (internal services), Enabling (coaching), Complicated-Subsystem (specialists). Book: Skelton & Pais. Reduces cognitive load, improves flow [EN]

**G30. DevOps / You Build It You Run It**  
Teams own full lifecycle. Benefits: faster feedback, quality incentive, reduced handoffs. Origin: Amazon 2006, Netflix. Related: SRE [EN]

### Tools (≥10 entries)

**T1. OneTrust** (Compliance)  
GDPR/CCPA consent management, cookie compliance, privacy automation. Features: consent SDK, preference center, audit trails. Pricing: Enterprise. Adoption: 12,000+ orgs. https://onetrust.com [EN]

**T2. Strategyzer** (Business Model Canvas)  
Business Model Canvas, Value Proposition Canvas platform. Features: collaboration, templates, testing board. Pricing: Freemium. https://strategyzer.com [EN]

**T3. GoF Pattern Catalog** (Design Patterns)  
23 design patterns. Categories: Creational, Structural, Behavioral. Language-agnostic with examples. Reference: Design Patterns book [EN]

**T4. BPMN.io** (Process Modeling)  
Browser-based BPMN 2.0 modeling. Features: flowcharts, collaboration diagrams, export. Open source. https://bpmn.io [EN]

**T5. Miro** (Collaborative Whiteboarding)  
Visual collaboration for patterns, workflows, retrospectives. Templates: BMC, user story mapping. Pricing: Freemium. https://miro.com [EN]

**T6. POSA** (Pattern-Oriented Software Architecture)  
Architectural patterns catalog (5 volumes). Scope: layers, pipes-filters, microkernel, broker, MVC, reactor, proactor [EN]

**T7. Prometheus + Grafana** (Observability)  
Open-source monitoring. Prometheus: time-series metrics. Grafana: visualization. Features: alerting, service discovery. Adoption: CNCF graduated. https://prometheus.io, https://grafana.com [EN]

**T8. HashiCorp Vault** (Security)  
Secrets management. Features: dynamic secrets, encryption as service, key rotation, audit logs. Patterns: centralized secrets, least privilege. Pricing: Open source + Enterprise. https://vaultproject.io [EN]

**T9. OWASP ZAP** (Security)  
Open-source web security scanner. Use: vulnerability scanning, penetration testing, CI/CD. Patterns: security testing automation. https://owasp.org/www-project-zap/ [EN]

**T10. dbt** (Data Build Tool)  
SQL-based transformation for analytics. Patterns: data modeling, testing, documentation, version control. Adoption: 10,000+ companies. Pricing: Open source + Cloud. https://getdbt.com [EN]

**T11. Databricks / Snowflake** (Data Platforms)  
Cloud data platforms: data lake, warehouse, lakehouse. Features: unified analytics, governance, polyglot persistence support. Used: Fortune 500. Pricing: Enterprise [EN]

**T12. Team Topologies Framework** (Organizational)  
Team organization guide. Four team types, three interaction modes. Book: Skelton & Pais (2019). Tools: workshops, assessments. https://teamtopologies.com [EN]

### Literature (≥12 entries)

**L1. Official GDPR Regulation (EU 2016/679)**  
Comprehensive data protection. Key: Art. 6 (lawful basis), Art. 7 (consent), Art. 17 (erasure), Art. 33 (breach). Foundation for regulatory patterns. https://gdpr-info.eu [EN]

**L2. Osterwalder, A., & Pigneur, Y. (2010). _Business Model Generation_. Wiley.**  
Business Model Canvas: 9 building blocks. Patterns: multi-sided platforms, freemium, long tail, subscription.

**L3. Porter, M. E. (1985). _Competitive Advantage_. Free Press.**  
Value chain, generic strategies (cost leadership, differentiation, focus). Framework for strategic patterns.

**L4. Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). _Design Patterns: Elements of Reusable Object-Oriented Software_. Addison-Wesley.**  
GoF: 23 foundational patterns. Categories: Creational (5), Structural (7), Behavioral (11). Proven in OOP.

**L5. Fowler, M. (2002). _Patterns of Enterprise Application Architecture_. Addison-Wesley.**  
Architectural patterns: Repository, Unit of Work, Service Layer, Domain Model. Use: enterprise systems, web apps.

**L6. Buschmann, F., et al. (1996-2007). _Pattern-Oriented Software Architecture_ (POSA, Vols. 1-5). Wiley.**  
Comprehensive patterns: Layers, Pipes-and-Filters, Microkernel, Broker, MVC, Reactor, Proactor.

**L7. Beck, K., et al. (2001). _Manifesto for Agile Software Development_**  
Agile principles. Values: individuals, working software, collaboration, change response. Foundation for process patterns. https://agilemanifesto.org [EN]

**L8. Kim, W. C., & Mauborgne, R. (2015). _Blue Ocean Strategy, Expanded Edition_. Harvard Business Review Press.**  
Value innovation, strategy canvas, four actions framework. Cases: Cirque du Soleil, Nintendo Wii, Southwest.

**L9. Christensen, C. M. (1997). _The Innovator's Dilemma_. Harvard Business Review Press.**  
Disruptive innovation: sustaining vs disruptive technologies. Pattern for market entry and competitive response.

**L10. Nygard, M. T. (2018). _Release It!: Design and Deploy Production-Ready Software_ (2nd ed.). Pragmatic Bookshelf.**  
NFR patterns: Circuit Breaker, Bulkhead, Timeouts, Handshaking, Steady State. Real-world failures and mitigations.

**L11. Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (2016). _Site Reliability Engineering_. O'Reilly.**  
Google's SRE: SLO/SLI/SLA, error budgets, toil reduction, incident response, capacity planning. Foundation for observability/reliability.

**L12. Kleppmann, M. (2017). _Designing Data-Intensive Applications_. O'Reilly.**  
Scalability/reliability for data: replication, partitioning, transactions, consistency. Trade-offs: consistency, availability, performance.

**L13. Kimball, R., & Ross, M. (2013). _The Data Warehouse Toolkit_ (3rd ed.). Wiley.**  
Data warehousing: dimensional modeling, star schema, slowly changing dimensions, fact tables. Industry-standard for analytics.

**L14. Skelton, M., & Pais, M. (2019). _Team Topologies_. IT Revolution Press.**  
Organizational patterns: four team types, three interaction modes, Conway's Law application. Reduces cognitive load, improves flow.

**L15. Forsgren, N., Humble, J., & Kim, G. (2018). _Accelerate_. IT Revolution Press.**  
Empirical research on high-performing orgs. Patterns: DevOps, continuous delivery, trunk-based development. Data: 4-year study, 30,000+ points.

### Citations (≥12 entries)

**A1. OMG. (2013). Business Process Model and Notation (BPMN) v2.0.2. https://www.omg.org/spec/BPMN/2.0.2 [EN]**

**A2. California Legislature. (2018). California Consumer Privacy Act (CCPA), AB-375. https://leginfo.legislature.ca.gov [EN]**

**A3. Conway, M. E. (1968). How do committees invent? _Datamation_, 14(4), 28-31. [EN]**

**A4. Scrum.org. (2020). The Scrum Guide. https://scrumguides.org [EN]**

**A5. NIST. (2018). Framework for Improving Critical Infrastructure Cybersecurity v1.1. https://www.nist.gov/cyberframework [EN]**

**A6. ISO/IEC. (2022). ISO/IEC 27001:2022 Information security management systems. https://www.iso.org/standard/82875.html [EN]**

**A7. OWASP. (2021). Application Security Verification Standard 4.0.3. https://owasp.org/www-project-application-security-verification-standard/ [EN]**

**A8. The Open Group. (2021). ArchiMate 3.2 Specification. https://pubs.opengroup.org/architecture/archimate3-doc/ [EN]**

**A9. Mermaid. (2023). Mermaid Official Documentation. https://mermaid.js.org [EN]**

**A10. Pact Foundation. (2023). Pact Specification v3. https://docs.pact.io/ [EN]**

**A11. 周爱民. (2021). 架构的本质. 电子工业出版社. [ZH]**

**A12. 张逸. (2019). 领域驱动设计实践. 电子工业出版社. [ZH]**

---

## Part III Self-Review Checklist

Before final validation, verify:

**Structure & TOC**:

- [ ] TOC present as "## Contents" at document start
- [ ] All 11 topic domains listed with Q# ranges
- [ ] TOC links to all major sections (Topic Areas, References, Validation Report)
- [ ] 30 Q&As present with 6/12/12 F/I/A distribution verified

**Output Skeleton Compliance**:

- [ ] Context and Assumptions section present
- [ ] Topic Areas table present with domain/Q#/count/F-I-A/examples columns
- [ ] Each Q&A follows template: Difficulty, Type, Key Insight, Answer,
      Pattern Quality (7 criteria), Concrete Example, Supporting Artifacts
- [ ] Reference sections present: Glossary (≥25), Tools (≥10), Literature (≥12),
      Citations (≥12)
- [ ] Domain-specific supporting artifacts table present and complete

**Content Quality**:

- [ ] Each Q&A answer 150-300 words
- [ ] Reasoning template applied (Claim → Rationale → Evidence → Implications →
      Limitations → Alternatives)
- [ ] Inline citations [Ref: ID] present in ≥70% of answers
- [ ] All [Ref: ID] resolve to Citations section entries
- [ ] All 7 pattern criteria addressed per Q&A
- [ ] ≥1 concrete example (code/YAML/diagram) per cluster
- [ ] ≥1 Mermaid diagram per cluster

**Evidence & Citations**:

- [ ] Critical claims have ≥1 Tier 1-2 citation
- [ ] Citation format: APA 7th with [Language] tags
- [ ] Links direct to authoritative sources; dead links archived/noted
- [ ] Tools section includes pricing, adoption, last verified date

**Common Failure Modes**:

- Missing TOC or incomplete TOC → Add complete TOC with all sections
- Q&A count ≠30 or wrong F/I/A distribution → Adjust to exactly 30 (6/12/12)
- Missing pattern criteria → Add all 7 criteria per pattern
- Broken [Ref: ID] links → Verify all IDs match Citations section
- Reference minimums unmet → Add entries to reach ≥25/≥10/≥12/≥12

## Validation Report

Execute 21-step validation (Part I). Present results in table format. All checks
must show PASS before submission.

---

## Change Log

**2025-01-11**: Optimized template with 20-guideline alignment from
`Guidelines_for_LLM-Friendly_Prompts.md`

**Improvements Applied**:

- **Foundation** (Guidelines 1-4): Added Context/Scope/Constraints preface; RFC 2119
  terminology policy; normalized terms; replaced vague language with concrete
  criteria; pruned redundancies
- **Scope** (Guidelines 5-8): Enforced MECE domain boundaries with in-scope/
  out-of-scope definitions; expanded 7 pattern criteria with definitions,
  checklists, and mapping table; added multi-stakeholder perspective template;
  strengthened depth requirements per Part
- **Quality** (Guidelines 9-13): Added accuracy verification checklist with claim
  classification (Critical/Supporting); defined 5-tier source credibility system;
  introduced significance labels (Critical/Nice-to-have) with pruning guideline;
  added reasoning template with Idempotency example; added fairness/bias/
  limitations template
- **Format** (Guidelines 14-16): Consolidated overlapping guidance; improved
  heading hierarchy; added DO/DON'T lists; made TOC mandatory with verification
  checklist; provided explicit output skeleton
- **Validation** (Guidelines 17-20): Made evidence mandatory for critical claims
  with citation format spec; added self-review checklists at end of Parts I, II,
  III; converted abstract requirements to actionable checklists/templates; added
  measurable acceptance checks; defined common failure modes with fixes

**Structural Enhancements**:

- Stage-gate workflow (A: Plan, B: Draft, C: Validate, D: Finalize) with gate
  criteria
- Roles defined (Editor, Fact-Checker, Terminology Steward, QA Validator)
- Pattern criteria mapping table showing where each criterion appears in output
- Link management guidance (versioned URLs, archived links, recency expectations)
- Enhanced citation standards with format specification and link rot handling

**Preserved Constraints** (verified):

- 3-part structure (Quality Standards, Workflow, Output Structure)
- 30 Q&As with 6/12/12 F/I/A distribution
- Reference minimums: ≥25 glossary, ≥10 tools, ≥12 literature, ≥12 citations
- All 21 validation steps with original numbering and thresholds
- 70+ pattern catalog intact
- Domain-specific supporting artifacts table retained
- All numeric thresholds and percentages unchanged

---
