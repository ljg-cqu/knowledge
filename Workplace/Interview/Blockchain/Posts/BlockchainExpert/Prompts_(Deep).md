# Prompts

Generate 100 interview Q&A pairs based on the provided job description.

## Requirements

### 1. Coverage & Organization

- **MECE Approach:** Cover all technical areas (Mutually Exclusive, Collectively Exhaustive)
- **Elements:** Technical (techniques, algorithms, protocols, patterns, best practices, frameworks, formulas, libraries), theoretical (theories, principles, axioms, laws, assumptions, models), practical (regulations, market dynamics, risks, costs, use cases)
- **Context:** Historical evolution, legal/regulatory landscape, future trends; key events and statistical data
- **Codebases & Libraries:** Identify authoritative repositories, SDKs, tooling suites, and audits; capture language support, licensing, maturity, integration hooks, and performance/security benchmarks.
- **Inference Lists:** Provide bullet summaries for adoption signals, interoperability impacts, roadmap implications, and operational risks per topic cluster.
- **Open Questions & Research:** Surface unresolved problems, knowledge gaps, emergent risks, and prioritized investigation tracks per topic cluster.
- **Authoritative Literature:** Distill takeaways from white/yellow papers, peer-reviewed studies, theses, market investigations, regulatory reports, books/manuals, and vetted encyclopedic resources; link claims to practical implementation guidance.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions for each topic cluster.
- **Collaboration & Organizational Dynamics:** Address cross-functional communication, governance models, institutional constraints, change management, and cultural alignment within teams and partner organizations.
- **Perspectives:** Engineering (front-end, back-end, full-stack), architecture & infrastructure, database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market
- **Philosophical & Macro Disciplines:** Integrate philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis across topic clusters.
- **Difficulty:** Foundational (20%), Intermediate (40%), Advanced (40%), grouped by topic

### 2. Content Design

- **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Evaluation:** Technical (performance, security, scalability, maintainability) and business (cost, efficiency, impact, market fit) dimensions
- **Trade-offs:** Address essential/non-trivial trade-offs with decision-making guidance
- **Macro Narratives:** Relate answers to systemic dynamics (economic cycles, stock/crypto market behaviors, liquidity and valuation trends, regulatory shifts, geopolitical/security considerations, societal adoption patterns, organizational behavior, historical precedents, macroeconomic/industry economic models).
- **Collaboration & Communication:** Surface stakeholder alignment plans, cross-team workflows, and communication cadences that impact execution quality.
- **Organizational & Strategic Operations:** Highlight business model implications, institutional capabilities, change readiness, and long-term strategic positioning.
- **Questions:** Mix theoretical, practical, and scenario-based on real-world applications
- **Answers:** 150-300 words with technical details, technologies, and practical examples; explain key concepts/terminologies clearly using analogies, formulas, etc. as needed
- **Heuristic Guidance:** Provide question-only prompt lists per Q&A covering creative, deep/critical, reflective, systems, design, strategic, lateral, ethical, scenario-planning, computational, meta-cognitive, dialectical, first-principles, and probabilistic thinking; supply at least 3 questions per mode (5 recommended) to drive self-directed exploration.

### 3. Execution

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation
- **Format:** Markdown with proper headings and code blocks
- **Clarification:** Include at least one mermaid diagram and one table per Q&A for clarity; also use code snippets, tables, analogies, comparisons, formulas, and diverse mermaid diagram types (structural: architecture, class, C4, ERD, block; behavioral: sequence, state, flowchart, data flow; project: Gantt, Kanban, user journey; analytical: charts, graphs, timelines, etc.)
- **Research:** Latest info from authoritative sources (official docs, white/yellow papers, academic theses, market investigations, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); cross-reference multiple sources
- **Citations:** Include APA 7th edition references for all sourced material, aligning with the output template section.
- **Quality:** Ensure essential/valuable Q&A with high-quality output; apply creative then critical thinking; **evaluate from multiple angles (pros, cons, risks, benefits, alternatives, emotional/psychological impact on stakeholders, market sentiment)**; verify accuracy, completeness, relevance, and MECE compliance
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

#### Element Coverage (Technical | Theoretical | Practical)
- Technical Techniques, Protocols & Frameworks: [...]
- Theoretical Principles & Models: [...]
- Practical Regulations, Risks & Use Cases: [...]

#### Technical Evaluation (Performance | Security | Scalability | Maintainability)
- Performance: [...]
- Security: [...]
- Scalability: [...]
- Maintainability: [...]

#### Business Evaluation (Cost | Efficiency | Impact | Market Fit)
- Cost: [...]
- Efficiency: [...]
- Impact: [...]
- Market Fit: [...]

#### Multi-Angle Evaluation (Pros | Cons | Risks | Benefits | Stakeholder Impact | Market Sentiment)
- Pros: [...]
- Cons: [...]
- Risks: [...]
- Benefits: [...]
- Stakeholder Emotional/Psychological Impact: [...]
- Market Sentiment: [...]

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
- [Critical trade-off analysis and recommended decision criteria]

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
- Roadmap Implications: [...]
- Operational Risks: [...]

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

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations]

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

#### Creative Thinking Prompts
- [Provide ≥3 (recommend 5) open-ended questions to stimulate creative ideas and innovative approaches]

#### Deep Thinking (Critical Thinking) Prompts
- [Provide ≥3 (recommend 5) questions for analytical, critical, and reflective thinking, e.g., assumptions, biases, implications]

#### Reflective Thinking Prompts
- [Provide ≥3 (recommend 5) questions for self-assessment, personal growth, and learning from experience]

#### Systems Thinking Prompts
- [Provide ≥3 (recommend 5) questions for understanding interconnections, holistic impacts, and systemic relationships]

#### Design Thinking Prompts
- [Provide ≥3 (recommend 5) questions for user-centered innovation, empathy, and iterative design]

#### Strategic Thinking Prompts
- [Provide ≥3 (recommend 5) questions for long-term vision, competitive advantage, and scenario planning]

#### Lateral Thinking Prompts
- [Provide ≥3 (recommend 5) questions that reframe constraints, explore analogies, or propose unconventional alternatives]

#### Ethical Thinking Prompts
- [Provide ≥3 (recommend 5) questions examining moral obligations, stakeholder ethics, and responsible conduct]

#### Scenario Planning Prompts
- [Provide ≥3 (recommend 5) questions probing future what-if situations, contingencies, and resilience strategies]

#### Computational Thinking Prompts
- [Provide ≥3 (recommend 5) questions about decomposition, pattern recognition, abstraction, and algorithmic reasoning]

#### Meta-Cognitive Prompts
- [Provide ≥3 (recommend 5) questions encouraging monitoring of reasoning quality, biases, and learning reflections]

#### Dialectical Thinking Prompts
- [Provide ≥3 (recommend 5) questions contrasting opposing viewpoints and synthesizing resolutions]

#### First-Principles Thinking Prompts
- [Provide ≥3 (recommend 5) questions that strip assumptions to fundamentals before reconstructing solutions]

#### Probabilistic Thinking Prompts
- [Provide ≥3 (recommend 5) questions assessing likelihoods, uncertainties, evidence strength, and risk distributions]