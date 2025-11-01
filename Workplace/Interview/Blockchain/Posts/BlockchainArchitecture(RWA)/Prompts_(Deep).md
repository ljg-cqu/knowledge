# Prompts

Generate 25 interview Q&A pairs based on the provided job description.

## Requirements

### 1. Coverage & Organization

- **MECE Approach:** Cover all technical areas (Mutually Exclusive, Collectively Exhaustive)
- **Elements:** Technical (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), practical (regulations, market dynamics, permission/consensus governance, upgrade planning/rollback strategies, risks, costs, use cases)
- **Context:** Historical evolution, legal/regulatory landscape, future trends; key events and statistical data
- **Codebases & Libraries:** Identify authoritative repositories, SDKs, tooling suites, and audits; capture language support, licensing, maturity, integration hooks, distributed consistency models, and performance/security benchmarks.
- **Inference Lists:** Provide bullet summaries for adoption signals, interoperability impacts, roadmap implications, and operational risks per topic cluster.
- **Open Questions & Research:** Surface unresolved problems, knowledge gaps, emergent risks, and prioritized investigation tracks per topic cluster.
- **Authoritative Literature:** Distill takeaways from white/yellow papers, peer-reviewed studies, theses, market investigations, regulatory reports, books/manuals, and vetted encyclopedic resources; link claims to practical implementation guidance.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions for each topic cluster.
- **Collaboration & Organizational Dynamics:** Address cross-functional communication, governance models, institutional constraints, change management, and cultural alignment within teams and partner organizations.
- **Governance & Trust Dimensions:** Assess permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.
- **Perspectives:** Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market
- **Philosophical & Macro Disciplines:** Integrate philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis across topic clusters.
- **Difficulty:** Foundational (20%), Intermediate (40%), Advanced (40%), grouped by topic

### 2. Content Design

- **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Evaluation:** Technical (throughput/latency performance, security, scalability, maintainability, reliability/HA) and business (cost, efficiency, impact, market fit) dimensions
- **Trade-offs:** Address essential/non-trivial trade-offs with decision-making guidance, including permissioning vs. decentralization choices, trust/privacy balances, algorithmic complexity limits, and upgrade path risks with mitigation strategies
- **Governance & Assurance:** Examine how permission boundaries, stakeholder trust models, privacy/transparency requirements, error-tolerance envelopes, and distributed consistency guarantees influence architectural options.
- **Macro Narratives:** Relate answers to systemic dynamics (economic cycles, stock/crypto market behaviors, liquidity and valuation trends, regulatory shifts, geopolitical/security considerations, societal adoption patterns, organizational behavior, historical precedents, macroeconomic/industry economic models).
- **Collaboration & Communication:** Surface stakeholder alignment plans, cross-team workflows, and communication cadences that impact execution quality.
- **Organizational & Strategic Operations:** Highlight business model implications, institutional capabilities, change readiness, and long-term strategic positioning.
- **Questions:** Mix theoretical, practical, and scenario-based on real-world applications
- **Answers:** 150-300 words with technical details, technologies, and practical examples; explain key concepts/terminologies clearly using analogies, formulas, etc. as needed

### 3. Execution

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation
- **Format:** Markdown with proper headings and code blocks
- **Clarification:** Include at least one mermaid diagram and one table per Q&A for clarity; also use code snippets, tables, analogies, comparisons, formulas, and diverse mermaid diagram types (structural: architecture, class, C4, ERD, block; behavioral: sequence, state, flowchart, data flow; project: Gantt, Kanban, user journey; analytical: charts, graphs, timelines, etc.)
- **Research:** Latest info from authoritative sources (official docs, white/yellow papers, academic theses, market investigations, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); cross-reference multiple sources
- **Citations:** Include APA 7th edition references for all sourced material, aligning with the output template section.
- **Quality:** Ensure essential/valuable Q&A with high-quality output; apply creative then critical thinking; evaluate from multiple angles per the template's **Multi-Angle Evaluation** checklist (pros, cons, risks, benefits, alternatives, stakeholder emotional/psychological impact, market sentiment); verify accuracy, completeness, relevance, and MECE compliance
- **Holistic Reasoning:** Harmonize technical depth with philosophical rigor and macro-level insight; trace implications across disciplines while maintaining MECE clarity.

## Output Template

```markdown
## [Topic Area] (Questions X-Y)

### QX: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced]
**Question Type:** [Theoretical/Practical/Scenario]

#### Answer Narrative (150-300 words)
[Comprehensive response with technical depth and practical illustration]

#### Supporting Artifacts
- At least one Mermaid diagram (e.g., flowchart, architecture)
- At least one table (e.g., comparison, data summary)
- [Additional code snippets, formulas, analogies, comparisons as needed]

#### Comparisons
- [Relevant comparisons to aid understanding, e.g., vs. other technologies, historical vs. current, etc.]

- Technical Techniques, Protocols, Frameworks & Design Patterns: [...]
- Theoretical Principles & Models: [...]
- Practical Regulations, Permission Models & Decentralization, Upgrade Governance, Risks & Use Cases: [...]

#### Technical Evaluation (Performance | Security | Scalability | Maintainability)
- Performance (Throughput & Latency): [...]
- Security: [...]
- Scalability: [...]
- Maintainability: [...]
- Algorithm Complexity & Error Tolerance: [...]
- Reliability & High Availability: [...]
- Distributed Consistency Guarantees: [...]
- Hardware Requirements & Optimizations: [... including energy and resource consumption analysis]

#### Business Evaluation (Cost | Efficiency | Impact | Market Fit)
- Cost: [...]
- Efficiency: [...]
- Impact: [...]
- Market Fit: [...]

#### Multi-Angle Evaluation (Pros | Cons | Risks | Benefits | Stakeholder Impact | Market Sentiment)
- Pros: [...]
- Cons: [...]
- Risks: [... include upgrade/migration failure modes and rollback contingencies]
- Benefits: [...]
- Stakeholder Emotional/Psychological Impact: [...]
- Market Sentiment: [...]
- Trust & Privacy/Transparency Considerations: [...]

#### Collaboration & Communication Plan
- Stakeholders & Roles: [...]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

#### Organizational & Strategic Fit
- Business Model Impact: [...]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

#### Trade-offs & Decision Guidance
- [Critical trade-off analysis and recommended decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

#### Context & Trend Signals
- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Future Trends: [...]
- Key Events & Statistics: [...]

#### Perspective-Based Insights
- Engineering (front-end/back-end/full-stack): [...]
- Architecture & Infrastructure: [...]
- Database & Data Engineering: [...]
- Quality Assurance & Testing: [...]
- Product Management: [...]
- Project/Program Management: [...]
- Requirements & Business Analysis: [...]
- Operations, DevOps & SRE: [...]
- Marketing & Commercialization: [...]
- Team Collaboration & Communication: [...]
- Organizational & Institutional Dynamics: [...]
- Philosophy (necessity vs. contingency, ethics, epistemology): [...]
- Economics, Finance & Capital Markets (stock, crypto, commodities): [...]
- Psychology & Sociology: [...]
- Education & Workforce Development: [...]
- Anthropology & Cultural Dynamics: [...]
- Law, Policy & Governance: [...]
- Military & Security Strategy: [...]
- Historical Context & Precedents: [...]

#### Market & Macro Systems Analysis
- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]
#### Inference Summary
- Adoption Signals: [...]
- Interoperability Impacts: [...]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, and rollback triggers]

#### Terminology & Key Concepts

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

#### Assumptions & Preconditions

- [Explicit assumption + rationale]

#### Validation & Evidence Checks

- [Data point, benchmark, or experiment backing the answer]

#### Counterexamples & Edge Cases

- [Scenario that challenges the main answer + mitigation]

#### Alternatives Considered

- [Option compared, trade-off summary, selection rationale]

#### Codebase & Library References

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

#### Authoritative Literature & Reports

- **[Paper/Report/Book]:** [Core findings, practical implications, credibility signals, reference link]

#### Actionable Conclusions & Next Steps
- [Decision, prioritized action, owner/timeline cues]

#### Open Questions & Research Agenda
- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

#### APA Style Source Citations

- **References:** List all sources cited in the answers.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
