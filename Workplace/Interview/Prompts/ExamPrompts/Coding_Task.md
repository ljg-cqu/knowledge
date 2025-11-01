# Coding Task (Machine-Gradable) Prompt Template

Purpose: Narrow, self-contained programming tasks designed for automated grading with unit tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 5–8 coding tasks per topic cluster. Difficulty distribution: Foundational (20%), Intermediate (50%), Advanced (30%).
- **Numbering:** Number all tasks sequentially (Task 1, Task 2, etc.) for easy tracking and reference. Include task numbers in Contents links.
- **Bloom Taxonomy:** Target Apply/Create levels. Foundational tasks test basic implementation of known algorithms; intermediate tasks require applying patterns to solve multi-step problems; advanced tasks demand creating novel solutions or optimizing for complex constraints.
- **Task Scope & Elements:** Keep tasks narrowly scoped and self-contained. Use MECE when building a question bank to avoid overlapping concepts. Cover: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, market dynamics, permission/consensus governance, risks, costs, use cases, edge-case handling).
- **Specification:** Provide complete problem description including input/output formats, function signature, data structures, allowed libraries, and all edge cases. Include relevant historical evolution, technical context, and real-world application scenarios.
- **Constraints:** State explicit constraints: time limits (e.g., 1s per test), memory limits (e.g., 256MB), allowed standard libraries, and prohibited approaches (if any).
- **Complexity:** Specify expected algorithm complexity (time/space) when relevant to the learning objective.
- **Validation & Evidence Checks:** Provide test cases and benchmarks that support correct implementation.
- **Counterexamples & Edge Cases:** Test handling of edge cases through hidden tests (empty inputs, large inputs, boundary values).
- **Codebases & Libraries:** Identify authoritative repositories, SDKs, tooling suites when tasks involve specific frameworks or protocols; capture language support, licensing, maturity, integration hooks.
- **Authoritative Literature:** Base tasks on algorithms/protocols from white/yellow papers, peer-reviewed studies, standards, books/manuals, and vetted encyclopedic resources.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions (e.g., in reference solution notes and grader guidance), especially for advanced tasks.
- **Governance & Trust Dimensions:** When relevant, include permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/HA strategies in task specifications (e.g., cryptographic validation, access control, distributed consistency).
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** For advanced tasks, integrate broader considerations from philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as appropriate.
- **Collaboration & Organizational Dynamics:** For advanced tasks, consider cross-functional communication patterns, governance models, institutional constraints, and change management in code design.
- **Organizational & Strategic Operations:** For advanced tasks, consider business model implications, institutional capabilities, change readiness, and long-term strategic positioning in code architecture and design choices.
- **Inference Lists:** For advanced tasks, test implementations that inform adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- **Open Questions & Research:** For advanced tasks, surface awareness of implementation limitations, edge cases, emergent risks, and investigation needs in code comments or documentation.

### 2. Content Design

- **Target Level:** Apply/Create (Bloom). Test ability to implement algorithms, manipulate data structures, handle edge cases, and write clean, idiomatic code with technical depth and practical application awareness.
- **Starter Code:** Provide a skeleton with function signature, docstrings, and placeholder comments to guide implementation. Include necessary imports and data structure definitions.
- **Test Coverage:** Supply 6–10 unit tests covering:
  - **Public tests (3–5):** Shown to students for immediate feedback; include basic cases and one edge case.
  - **Hidden tests (3–5):** Not shown; test robustness, performance, and additional edge cases (e.g., empty inputs, large inputs, boundary values).
- **Reference Solution:** Provide a correct, well-commented implementation and brief explanation of approach/complexity.
- **Evaluation Dimensions:** Technical (throughput/latency performance, security, scalability, maintainability, reliability/HA, algorithm complexity, error tolerance) and business (efficiency, practical impact) considerations.
- **Trade-offs:** For advanced tasks, address essential trade-offs (e.g., time vs space complexity, security vs performance, consistency vs availability).
- **Governance & Assurance:** When applicable, examine permission boundaries, trust models, privacy requirements, and error-tolerance expectations in code design.

### 3. Evaluation & Grading

- **Scoring Breakdown:** Recommended: Correctness (70%), Edge-case handling (20%), Code style/tests (10%). Adjust proportions per difficulty while maintaining 100% total.
- **Grader Notes:** Document common implementation mistakes, performance pitfalls, and partial-credit guidance (e.g., correct logic but inefficient → 70%).
- **Auto-Grading:** Use an isolated test runner (e.g., pytest, unittest, jest). Public tests provide feedback; hidden tests ensure robustness without over-fitting.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use fenced code blocks. Specify language (e.g., `python`, `javascript`) and include instructions to run tests locally.
- **Security:** Avoid shipping secrets (private keys, API tokens). Use ephemeral/generated keys or mock credentials where blockchain/crypto interactions are needed.
- **Clarity Aids:** Include a small flowchart (mermaid) showing input→processing→output flow when helpful. Use tables to summarize test cases or constraints. Use diverse visualization types: mermaid diagrams (structural, behavioral, analytical), analogies, comparisons. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Explain key concepts/terminologies clearly in problem descriptions and comments.
- **Context Integration:** Include relevant technical context, best practices, and real-world application scenarios.
- **Real-World Grounding:** Base tasks on real-world applications and practical coding scenarios.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all tasks (Task 1–Task n) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and Task 1–Task n)
  - Executive Summary (2–4 bullets: assessment goals, programming scope, auto-grading approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and task indices); Topic Cluster Mapping Table (Cluster → scope → task indices)
  - Glossary & Acronym Index (key algorithms, data structures, protocol concepts tested)
  - How to Use This in Interviews (auto-grading setup, scoring breakdown, and local testing instructions)
  - Key Decision Criteria Checklist (when applicable: algorithm selection criteria, security requirements, performance targets, etc.)
  - Key Decision Criteria Matrix (Quick Picks) mapping implementation approaches to criteria (when applicable)
- **Tags:** Label each task with Difficulty, Bloom level, and language.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Ensure tasks reflect best practices and broader software engineering principles.
- **Citations:** Include APA 7th edition references for tasks referencing external protocols, algorithms, or standards.

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

````
```
