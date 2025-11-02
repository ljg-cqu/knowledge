# Coding Task (Machine-Gradable) Prompt Template

Purpose: Narrow, self-contained programming tasks designed for automated grading with unit tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Task Scope & Distribution

- Generate 5–8 coding tasks per topic cluster (use 7+ for comprehensive sets, 5–6 for narrow focus).
- Number tasks sequentially (Task 1, Task 2, …) with anchors in the Contents section.
- Maintain Foundational (20%), Intermediate (50%), Advanced (30%) distribution targeting Bloom Apply/Create: foundational tasks implement known algorithms, intermediate tasks apply patterns to multi-step problems, advanced tasks design novel or optimized solutions under complex constraints.

### Specification & Context

- Keep tasks narrowly scoped and self-contained; apply MECE principles to avoid overlapping concepts.
- Cover technical, theoretical, and practical elements: techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations (including energy/resource consumption); theories, principles, axioms, laws, assumptions, models; regulations, market dynamics, permission/consensus governance, risks, costs, use cases, edge-case handling.
- Provide a complete specification: input/output formats, function signatures, data structures, allowed/prohibited libraries, explicit constraints (time/memory limits), and historical or real-world application context.
- State expected time/space complexity when learning objectives demand it.
- Reference authoritative repositories, SDKs, tooling suites with details on language support, licensing, maturity, integration hooks; base tasks on protocols/algorithms documented in white/yellow papers, peer-reviewed studies, standards, books/manuals, curated encyclopedias.

### Analytical Coverage & Diagnostics

- Supply public and hidden tests that validate correct implementation, performance, and edge-case handling (empty inputs, large inputs, boundary values). Hidden tests must expose failure/unhappy paths and rollback expectations.
- Capture explicit assumptions, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions in reference solutions and grader notes, especially for advanced tasks.
- Document misconceptions or flawed strategies each task is designed to surface, plus corrective takeaways.
- Require comparisons between implementation strategies (data structures, concurrency models, security hardening options) and define decision criteria.
- Include governance/trust considerations (permission models, decentralization, privacy/transparency balances, design-pattern choices, error tolerance, reliability/HA expectations) when relevant.
- Examine perspectives from engineering (front-end, back-end, full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- For advanced tasks, add philosophical, economic, financial, capital-market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical lenses where appropriate.
- Discuss cross-functional communication, governance models, institutional constraints, change management, cultural alignment, business model implications, institutional capabilities, change readiness, strategic positioning, adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (including upgrade readiness, testing coverage, rollback triggers), and open research agendas tied to the implementation.

### Content Design

- Target senior/expert-level Apply/Create proficiency: implementing algorithms, manipulating data structures, handling edge cases, writing clean idiomatic code with practical awareness.
- Provide starter code with function signatures, docstrings, placeholder comments, necessary imports, and data structure definitions.
- Deliver 6–10 unit tests: 3–5 public tests (basic + representative edge case) and 3–5 hidden tests (robustness, performance, additional edge cases). Clarify test runner usage (pytest, unittest, jest, etc.).
- Include a reference solution with commentary and complexity analysis.
- Evaluate along technical dimensions (throughput/latency, security, scalability, maintainability, reliability/HA, algorithm complexity, error tolerance) and business dimensions (efficiency, practical impact).
- Address trade-offs such as time vs space complexity, security vs performance, consistency vs availability; examine permission boundaries, trust models, privacy requirements, error-tolerance expectations.

### Evaluation & Grading

- Recommend scoring breakdowns totaling 100% (e.g., Correctness 70%, Edge-case handling 20%, Code style/tests 10%) and adjust per difficulty.
- Provide grader notes detailing common implementation mistakes, performance pitfalls, partial-credit guidance (e.g., correct logic but inefficient → 70%), and tests that reveal misunderstanding of key concepts.
- Record misconception focus, failure path insights, and comparison notes for interviewers.

### Execution & Format

- Plan carefully before authoring; align coverage, difficulty mix, and artifact checklist.
- Use Markdown with clear headings and fenced code blocks for problem statements, starter code, tests, and reference solutions. Include commands for running tests locally.
- Avoid embedding secrets; use mock credentials for blockchain/crypto contexts.
- Provide clarifying aids such as flowcharts (mermaid), tables summarizing test cases/constraints, analogies, comparisons, formulas. Maintain mermaid portability (no edge labels; quote node labels containing special characters like parentheses/slashes).
- Explain terminology and key concepts within problem descriptions and comments.
- Root tasks in real-world scenarios with relevant technical context and best practices.
- Insert a compact Contents section linking to major sections and all tasks (Task 1–Task n) using GitHub-compatible anchors.
- Include required prefatory sections: Contents; Executive Summary (2–4 bullets on assessment goals, programming scope, auto-grading approach); Coverage & Difficulty Summary (difficulty table + topic cluster mapping); Glossary & Acronym Index; How to Use This in Interviews (auto-grading setup, scoring breakdown, local testing instructions); Key Decision Criteria Checklist (algorithm selection, security requirements, performance targets, etc.); Key Decision Criteria Matrix (Quick Picks) mapping implementation approaches to criteria when applicable.
- Tag each task with Difficulty, Bloom level, language.
- Base content on current authoritative sources; cross-reference for accuracy, completeness, relevance, MECE compliance.
- Apply holistic reasoning so tasks reflect best software-engineering practices; cite external protocols, algorithms, standards in APA 7th edition.

### Shared Evaluation Checklist (apply to every task)

- **Technical Evaluation**: performance (throughput/latency), security posture, scalability, maintainability, algorithm complexity & error tolerance, reliability/high availability, distributed consistency guarantees, hardware requirements & energy/resource consumption.
- **Business Evaluation**: cost implications, efficiency, impact, market fit.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: define algorithms, data structures, protocol concepts with analogies/formulas/examples for graders.
- **Context & Background**: outline historical evolution, technical context, market dynamics, regulatory landscape, key events/statistics underpinning the problem.
- **Validation & Evidence Checks**: include benchmarks, datasets, or experiments supporting solution correctness/performance.
- **Counterexamples & Edge Cases**: document scenarios challenging naive implementations and expected mitigations.
- **Alternatives & Trade-offs**: compare approaches, note trade-offs, specify decision criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: evaluate solutions across engineering disciplines, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: assess systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models when relevant.
- **Inference Summary**: identify adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: define stakeholders, communication cadence/channels, cross-functional alignment tactics for implementation.
- **Organizational & Strategic Fit**: analyze business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation.
- **Codebase & Library References**: enumerate repositories/libraries with stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes.
- **Authoritative Literature**: cite standards, documentation, audits, papers underpinning algorithms or frameworks.
- **Actionable Conclusions**: summarize best practices, design principles, prioritized follow-up actions.
- **Open Questions & Research Agenda**: list remaining challenges, hypotheses, experiments, data/resource needs, timelines/ownership for further exploration.
- **APA Style Source Citations**: ensure all references follow APA 7th edition and directly support task content.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Tasks](#tasks)
  - [Task 1: Title](#task-1-title)
  - [Task 2: Title](#task-2-title)
  - ... (link to each task)

## Executive Summary

- [2–4 bullets: assessment goals, programming scope, auto-grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Tasks |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Tasks |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Task 1–x |
| [Cluster B] | [Scope/Boundaries] | Task (x+1)–y |

## Glossary & Acronym Index

- [Key algorithms, data structures, protocol concepts tested]

## How to Use This in Interviews

- Auto-grade via isolated test runner; public tests for feedback, hidden tests for robustness
- Scoring: Correctness (60–80%), Edge cases (10–25%), Style/tests (5–10%)

## Key Decision Criteria Checklist

- [List key criteria when applicable, e.g., algorithm selection (time/space complexity targets), security requirements (input validation, cryptographic standards), performance targets (throughput/latency), code maintainability, etc.]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Approach A | Preferred Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Approach description] | [Approach description] | [Decision guidance] |
| [Criterion 2] | [Approach description] | [Approach description] | [Decision guidance] |

---

## Task 1: [Title]

**Language:** python  
**Difficulty:** Intermediate  
**Bloom:** Apply/Create

### Problem Description

Implement `validate_transfer(tx)` that checks signature, balance, and asset type.

**Function signature:** `def validate_transfer(tx):`

**Constraints:** time=1s, memory=256MB, allowed libs: stdlib

### Starter Code

\`\`\`python
def validate_transfer(tx):
    """
    Validate a blockchain transfer transaction.
    Args: tx (dict) - transaction with keys: from, to, amount, signature, asset_type
    Returns: bool - True if valid, False otherwise
    """
    # TODO: Implement validation logic
    pass
\`\`\`

### Public Tests

- input: `{"from": "alice", "to": "bob", "amount": 100, ...}` -> output: `True`
- input: `{"from": "alice", "to": "bob", "amount": -10, ...}` -> output: `False`

### Hidden Tests

(Not shown to students; test edge cases, large inputs, boundary values)

### Reference Solution

[Path to solution or brief description of approach and complexity]

### Grader Notes

- Common mistakes: missing edge-case checks, inefficient algorithms, incorrect signature validation
- Partial credit: Correct logic but inefficient → 70%

### Supporting Artifacts (problem context)

- Mermaid diagrams (e.g., flowchart showing input→processing→output, architecture)
- Tables (e.g., test case summary, constraint summary)
- Analogies, comparisons to clarify problem domain

### Technical Evaluation Considerations (for graders)

- Performance (Throughput & Latency): [Expected complexity and benchmarks]
- Security: [Validation requirements, attack vectors to consider]
- Scalability: [How solution scales with input size]
- Maintainability: [Code clarity, modularity expectations]
- Algorithm Complexity & Error Tolerance: [Big-O expectations, edge case handling]
- Reliability & High Availability: [When applicable to distributed systems tasks]
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

### Terminology & Key Concepts (problem domain)

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

### Context & Background (problem domain)

- Historical Evolution: [...]
- Technical Context: [...]
- Real-World Application: [...]
- Key Events & Statistics: [When relevant to the task]

### Assumptions & Preconditions (problem setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (expected in solution)

- [Data point, benchmark, or test backing the approach]

### Counterexamples & Edge Cases (hidden tests focus)

- [Scenario that challenges naive implementations + expected handling]

### Alternatives Considered (reference solution notes)

- [Alternative approach, trade-off summary, selection rationale]

### Trade-offs & Decision Guidance (when relevant)

- [Critical trade-off analysis in implementation approach; decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Perspective-Based Insights (task domain)

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

### Market & Macro Systems Analysis (for advanced tasks)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (for advanced tasks)

- Adoption Signals: [...]
- Interoperability Impacts: [...]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, rollback triggers]

### Collaboration & Communication Plan (when relevant)

- Stakeholders & Roles: [...]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

### Organizational & Strategic Fit (when relevant)

- Business Model Impact: [...]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

### Codebase & Library References (when applicable)

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

### Authoritative Literature (algorithm/protocol sources)

- **[Paper/Standard/Documentation]:** [Core findings, practical implications, reference link]

### Actionable Conclusions (from reference solution)

- [Key takeaway, best practice, design principle; prioritized action]

### Open Questions & Research Agenda (for advanced tasks)

- Remaining Challenges: [... implementation limitations, edge cases]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations (problem references)

- **References:** List sources for algorithms, protocols, or standards referenced in the task.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
```
