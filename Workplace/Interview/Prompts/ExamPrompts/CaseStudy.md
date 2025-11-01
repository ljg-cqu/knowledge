# Case Study / Scenario-Based Prompt Template

Purpose: Multi-part scenario questions that assess systems thinking, trade-off analysis, and concise recommendations.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 3–5 case study scenarios per topic cluster. Difficulty distribution: Foundational (20%), Intermediate (40%), Advanced (40%).
- **Numbering:** Number all scenarios sequentially (Scenario 1, Scenario 2, etc.) for easy tracking and reference. Include scenario numbers in Contents links.
- **Bloom Taxonomy:** Target Analyze/Evaluate levels primarily. Foundational scenarios test analysis of straightforward issues; intermediate scenarios require comparing alternatives and discussing trade-offs; advanced scenarios demand evaluation of complex system interactions and synthesis of multi-faceted recommendations.
- **Scenario Design & Elements:** Provide 200–400 words with explicit constraints, assumed facts, and self-contained context. Ensure scenario reflects real-world complexity (technical debt, resource limits, stakeholder conflicts). Cover: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, market dynamics, permission/consensus governance, upgrade planning/rollback strategies, risks, costs, use cases).
- **Task Structure:** 3–4 MECE tasks covering: issue identification, solution proposals with trade-offs, remediation plans, stakeholder communication, and decision recommendations.
- **Context:** Include relevant historical evolution, legal/regulatory landscape, future trends, key events, statistical data, and system interactions. Surface technical (protocols, patterns, performance, algorithm complexity, distributed consistency, reliability/HA) and business (cost, impact, risk, market fit) dimensions. For RWA contexts, incorporate tokenization standards, custody requirements, regulatory compliance, or asset lifecycle considerations.
- **Codebases & Libraries:** When relevant, identify authoritative repositories, SDKs, tooling suites, and audits; capture language support, licensing, maturity, integration hooks, distributed consistency models, and performance/security benchmarks.
- **Inference Lists:** Provide bullet summaries for adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers) per scenario.
- **Open Questions & Research:** Surface unresolved problems, knowledge gaps, emergent risks, and prioritized investigation tracks per scenario.
- **Authoritative Literature:** Distill takeaways from white/yellow papers, peer-reviewed studies, theses, market investigations, regulatory reports, books/manuals, and vetted encyclopedic resources; link claims to practical implementation guidance.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions for each scenario.
- **Collaboration & Organizational Dynamics:** Address cross-functional communication, governance models, institutional constraints, change management, and cultural alignment within teams and partner organizations.
- **Governance & Trust Dimensions:** Assess permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.
- **Perspectives:** Ensure scenarios cover: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** Integrate philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as relevant to scenarios.
- **Validation & Evidence Checks:** Require explicit evidence, data points, or benchmarks supporting scenario solutions.
- **Counterexamples & Edge Cases:** Test understanding of edge cases and scenarios that challenge main solutions.
- **Alternatives Considered:** Require candidates to consider and compare alternative approaches.

### 2. Content Design

- **Target Level:** Analyze/Evaluate (Bloom). Expect candidates to synthesize information, compare alternatives, and justify recommendations with deep technical understanding and broad strategic perspective.
- **Deliverables:** Require outputs such as issue lists, solution memos (≤300 words), decision matrices, stakeholder communication drafts, and remediation timelines.
- **Trade-offs:** Explicitly test understanding of essential/non-trivial trade-offs (e.g., privacy vs transparency, throughput vs consistency, centralization vs decentralization, cost vs resilience, permissioning vs. decentralization choices, trust/privacy balances, algorithmic complexity limits, upgrade path risks with mitigation strategies).
- **Evaluation Dimensions:** Technical (throughput/latency performance, security, scalability, maintainability, reliability/HA, algorithm complexity, error tolerance, distributed consistency guarantees) and business (cost, efficiency, impact, market fit) dimensions.
- **Governance & Assurance:** Examine how permission boundaries, stakeholder trust models, privacy/transparency requirements, error-tolerance envelopes, and distributed consistency guarantees influence scenario solutions.
- **Macro Narratives:** Relate scenario solutions to systemic dynamics (economic cycles, stock/crypto market behaviors, liquidity and valuation trends, regulatory shifts, geopolitical/security considerations, societal adoption patterns, organizational behavior, historical precedents, macroeconomic/industry economic models).
- **Collaboration & Communication:** Surface stakeholder alignment plans, cross-team workflows, and communication cadences that impact execution quality in scenario solutions.
- **Organizational & Strategic Operations:** Highlight business model implications, institutional capabilities, change readiness, and long-term strategic positioning in scenario context and expected solutions.

### 3. Evaluation & Grading

- **Rubric:** Provide scoring bands and breakdown per task (e.g., Task 1: 8 pts, Task 2: 10 pts, Task 3: 6 pts).
- **Partial Credit:** Supply checklists for partial credit (e.g., correct diagnosis + incomplete solution = 60%). Document expected evidence and common omissions.
- **Grader Notes:** List key points, acceptable alternative approaches, and edge cases that deserve bonus credit.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use clear task headings, fenced code blocks, and tables. Include assets in `assets/` folder (logs, configs, diagrams) when needed.
- **Clarity Aids:** Use decision matrices (criteria vs options), mermaid diagrams (sequence/flow charts), and comparison tables to clarify system interactions. Use diverse visualization types: mermaid diagrams (structural, behavioral, analytical), code snippets, analogies, comparisons, formulas. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Explain key concepts/terminologies clearly using analogies, formulas, etc. as needed.
- **Context Integration:** Include historical evolution, legal/regulatory landscape, future trends, key events, and statistical data to enrich scenarios.
- **Real-World Grounding:** Base scenarios on real-world applications; mix theoretical, practical, and scenario-based contexts reflecting actual business/technical challenges.
- **Multi-Angle Evaluation:** Evaluate scenarios from multiple angles including pros, cons, risks, benefits, alternatives, stakeholder emotional/psychological impact, and market sentiment.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all scenarios (Scenario 1–Scenario n) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and Scenario 1–Scenario n)
  - Executive Summary (2–4 bullets: assessment goals, topic scope, key trade-offs tested)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and scenario indices); Topic Cluster Mapping Table (Cluster → scope → scenario indices)
  - Glossary & Acronym Index (short definitions of key terms)
  - How to Use This in Interviews (evaluation guidance and rubric application notes)
  - Key Decision Criteria Checklist (when applicable to scenario domain: privacy, performance SLOs, security, interop, ops/HA-DR, governance/upgrades, etc.)
  - Key Decision Criteria Matrix (Quick Picks) mapping criteria to preferred approaches with notes/signals (when applicable)
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Harmonize technical depth with philosophical rigor and macro-level insight; trace implications across disciplines while maintaining MECE clarity.
- **Citations:** Include APA 7th edition references for standards, frameworks, or regulatory references used in scenarios.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Scenarios](#scenarios)
  - [Scenario 1: Title](#scenario-1-title)
  - [Scenario 2: Title](#scenario-2-title)
  - ... (link to each scenario)

## Executive Summary

- [2–4 bullets: assessment goals, topic scope, key trade-offs tested]

## Coverage & Difficulty Summary

| Difficulty | Count | Scenarios |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Scenarios |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Scenario 1–x |
| [Cluster B] | [Scope/Boundaries] | Scenario (x+1)–y |

## Glossary & Acronym Index

- [Key terms and acronyms used across scenarios]

## How to Use This in Interviews

- Allow 45–60 min per scenario; evaluate depth of analysis, trade-off reasoning, and communication clarity
- Use rubrics for consistent grading; award partial credit per task checklist

## Key Decision Criteria Checklist

- [List key criteria relevant to the scenario domain, e.g., privacy & compliance, performance SLOs, security posture, interop & liquidity, ops & HA/DR, governance & upgrades, tokenomics & RWA when applicable]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Approach A | Preferred Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Approach description] | [Approach description] | [Decision guidance] |
| [Criterion 2] | [Approach description] | [Approach description] | [Decision guidance] |

---

## Scenario 1: [Title]

**Language:** python  
**Difficulty:** Intermediate  
**Bloom:** Apply/Create

### Scenario Context

<200–400 word scenario text with constraints, metrics, stakeholder details>

### Tasks

1. Identify top 3 issues
2. Propose 2 solutions and discuss trade-offs
3. Draft a recommendation memo (≤300 words)

### Expected Key Points

- **Task 1:** [List expected issues and evidence to cite]
- **Task 2:** [List expected solutions, trade-offs, and decision criteria]
- **Task 3:** [List key elements of a strong memo: clarity, justification, stakeholder framing]

### Grading Rubric

| Task | Max Points | Criteria |
|---|---:|---|
| Task 1 | 8 | Correctness, completeness, evidence |
| Task 2 | 10 | Feasibility, trade-off depth, alternatives |
| Task 3 | 6 | Clarity, structure, decision justification |

### Grader Notes

- Partial credit: Correct diagnosis + incomplete solution = 60%
- Bonus: Novel insights, consideration of edge cases, stakeholder impact analysis
- Common omissions: [List typical gaps]

### Supporting Artifacts (for scenario context clarity)

- Mermaid diagrams (e.g., architecture, sequence, flowchart)
- Tables (e.g., comparison, data summary, decision matrix)
- Code snippets, analogies, comparisons, formulas as needed

### Technical Evaluation (Performance | Security | Scalability | Maintainability)
- Performance (Throughput & Latency): [...]
- Security: [...]
- Scalability: [...]
- Maintainability: [...]
- Algorithm Complexity & Error Tolerance: [...]
- Reliability & High Availability: [...]
- Distributed Consistency Guarantees: [...]
- Hardware Requirements & Optimizations: [... including energy and resource consumption analysis]

### Business Evaluation (Cost | Efficiency | Impact | Market Fit)
- Cost: [...]
- Efficiency: [...]
- Impact: [...]
- Market Fit: [...]

### Multi-Angle Evaluation (Pros | Cons | Risks | Benefits | Stakeholder Impact | Market Sentiment)
- Pros: [...]
- Cons: [...]
- Risks: [... include upgrade/migration failure modes and rollback contingencies]
- Benefits: [...]
- Stakeholder Emotional/Psychological Impact: [...]
- Market Sentiment: [...]
- Trust & Privacy/Transparency Considerations: [...]

### Terminology & Key Concepts (scenario domain)

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

### Context & Background (scenario grounding)

- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Technical Context: [...]
- Market Dynamics: [...]
- Key Events & Statistics: [...]

### Perspective-Based Insights (evaluate candidate responses from these angles)

- Engineering (front-end/back-end/full-stack): [...]
- Architecture & Infrastructure: [... including hardware design, deployment, energy/resource consumption]
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

### Market & Macro Systems Analysis (for advanced scenarios)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (scenario implications)

- Adoption Signals: [...]
- Interoperability Impacts: [...]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, rollback triggers]

### Collaboration & Communication Plan (expected in candidate responses)

- Stakeholders & Roles: [...]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

### Organizational & Strategic Fit (expected in candidate responses)

- Business Model Impact: [...]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

### Assumptions & Preconditions (scenario setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (expected in candidate responses)

- [Data point, benchmark, or experiment backing the solution]

### Counterexamples & Edge Cases (expected in candidate responses)

- [Scenario that challenges the main solution + mitigation]

### Alternatives Considered (expected in candidate responses)

- [Option compared, trade-off summary, selection rationale]

### Trade-offs & Decision Guidance (expected in candidate responses)

- [Critical trade-off analysis and recommended decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Codebase & Library References (when applicable)

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

### Authoritative Literature & Reports (scenario grounding)

- **[Paper/Report/Book]:** [Core findings, practical implications, credibility signals, reference link]

### Actionable Conclusions & Next Steps (expected in candidate recommendations)

- [Decision, prioritized action, owner/timeline cues]

### Open Questions & Research Agenda (for advanced scenarios)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations (scenario references)

- **References:** List all sources cited in the scenario context.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
```

````
```
