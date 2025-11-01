# Short Answer / Numeric Calculation Prompt Template

Purpose: Short constructed-response items requiring concise numeric or short-text answers (calculations, conversions, brief justification).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 8–12 short-answer/calculation problems per topic cluster (aim for 10+ when comprehensive coverage is needed; use 8–9 for focused or narrow topic clusters). Difficulty distribution: Foundational (25%), Intermediate (50%), Advanced (25%).
- **Numbering:** Number all problems sequentially (P1, P2, etc.) for easy tracking and reference. Include problem numbers in Contents links.
- **Bloom Taxonomy:** Target Apply/Analyze levels. Foundational problems test direct formula application; intermediate problems require multi-step calculations and unit conversions; advanced problems demand analysis of results, selection of appropriate methods, or justification of assumptions.
- **Problem Scope & Elements:** Self-contained problems with all necessary data. Use MECE to avoid overlapping question types across a bank. Cover: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, market dynamics, permission/consensus governance, upgrade planning/rollback strategies, risks, costs, use cases).
- **Units & Conventions:** Explicitly state units and conventions (e.g., MB = 10^6 bytes vs 2^20 bytes; percentages vs decimals; rounding rules). Provide alternate acceptable answers when ambiguity exists.
- **Problem Types:** Cover calculations (e.g., throughput, latency, gas costs, tokenization ratios, collateralization rates, consensus performance, resource consumption), unit conversions, formula applications, and short justifications (2–3 sentences). For RWA contexts, include asset valuation, transaction fee modeling, or compliance threshold calculations.
- **Validation & Evidence Checks:** Provide authoritative sources and benchmarks supporting formulas and calculation methods.
- **Counterexamples & Edge Cases:** Include calculations that test boundary conditions and sensitivity to assumptions.
- **Context:** Include relevant historical evolution, technical context, key events, statistical data, and real-world application scenarios.
- **Codebases & Libraries:** When problems involve specific frameworks/protocols, reference authoritative sources for formulas, benchmarks, and performance characteristics.
- **Authoritative Literature:** Base formulas and calculations on white/yellow papers, standards, official documentation, and peer-reviewed studies.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions for problems (especially advanced ones).
- **Governance & Trust Dimensions:** When applicable, include calculations involving permission thresholds, trust model parameters, privacy/transparency metrics, design-pattern choices, system error-tolerance bounds, or reliability/HA parameters.
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** For advanced problems, integrate philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as relevant.
- **Collaboration & Organizational Dynamics:** For advanced problems, include calculations that inform stakeholder alignment, cross-team workflows, or organizational decision-making.
- **Organizational & Strategic Operations:** For advanced problems, include calculations that inform business model impact, institutional capabilities assessment, change readiness evaluation, and strategic positioning analysis.
- **Inference Lists:** For advanced problems, test calculations that inform adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- **Open Questions & Research:** For advanced problems, surface awareness of calculation limitations, uncertainty ranges, emergent risks, and investigation needs.

### 2. Content Design

- **Target Level:** Apply/Analyze (Bloom). Test ability to apply formulas, perform multi-step calculations, interpret results, and justify reasoning with technical depth and practical awareness (senior/expert level).
- **Answer Format:** Provide exact expected answer, units, and acceptable tolerance (e.g., ±2% for percentages, ±0.5 for small integers).
- **Worked Solution:** Supply a 2–4 step worked solution showing method and intermediate results. Use clear mathematical notation or pseudocode where appropriate.
- **Partial Credit:** Define rules for method vs arithmetic credit (e.g., correct method with arithmetic error = 70%; correct setup but incomplete = 50%).
- **Evaluation Dimensions:** Technical (performance metrics, algorithm complexity, resource consumption) and business (cost efficiency, impact assessment, market fit) considerations.
- **Trade-offs:** For advanced problems, address trade-offs in approach selection (e.g., accuracy vs computational cost, security vs performance).
- **Governance & Assurance:** When applicable, include calculations that inform permission boundaries, trust thresholds, privacy requirements, or error-tolerance parameters.

### 3. Evaluation & Grading

- **Normalization:** Define numeric normalization rules: strip commas, accept scientific notation, case-insensitive for units (e.g., "KB" vs "kb").
- **Tolerance:** Specify acceptable ranges per question type. Use percentage tolerance (e.g., ±2%) for large numbers or ratios, absolute tolerance (e.g., ±0.5) for small integer values.
- **Human Check:** Include grader notes for questions requiring short justification or interpretation (e.g., "Explain why X is more efficient than Y"). Provide model answers and acceptable variations.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use fenced calculation steps. Clearly label the final answer line (e.g., "**Answer:** 42.5 ms").
- **Clarity Aids:** Use tables to organize data (e.g., inputs, parameters), and include formulas in LaTeX/KaTeX notation when helpful (e.g., `$T = N / R$`). Use diverse visualization types: mermaid diagrams (structural, behavioral, analytical), code snippets, analogies, comparisons. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Explain key concepts/terminologies clearly using analogies, formulas, etc. as needed.
- **Context Integration:** Include relevant historical evolution, legal/regulatory landscape, future trends, key events, and statistical data where appropriate.
- **Real-World Grounding:** Base problems on real-world applications and practical scenarios.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all problems (P1–Pn) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and P1–Pn)
  - Executive Summary (2–3 bullets: assessment goals, calculation scope, grading approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and problem indices); Topic Cluster Mapping Table (Cluster → scope → problem indices)
  - Glossary & Acronym Index (key formulas, units, and conventions)
  - How to Use This in Interviews (machine-grading with tolerance checks, manual review guidance for justifications)
  - Key Decision Criteria Checklist (when applicable: formula selection, accuracy requirements, computational approach, etc.)
  - Key Decision Criteria Matrix (Quick Picks) mapping calculation methods to criteria (when applicable)
- **Tags:** Label each item with Difficulty, Bloom level, and question type (calculation/conversion/justification).
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Harmonize technical depth with broader context and macro-level insight; trace implications across disciplines while maintaining MECE clarity.
- **Citations:** Include APA 7th edition references for formulas referencing standards, protocol specifications, or published benchmarks.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Problems 1–12](#problems-112)
  - [P1: Problem title](#p1-problem-title)
  - [P2: Problem title](#p2-problem-title)
  - ... (link to each problem)

## Executive Summary

- [2–3 bullets: assessment goals, calculation scope, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Problems |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Problems |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | P1–x |
| [Cluster B] | [Scope/Boundaries] | P(x+1)–y |

## Glossary & Acronym Index

- [Key formulas, units, and conventions]

## How to Use This in Interviews

- Machine-gradable with tolerance checks; manual review for justification questions
- Scoring: Method credit + arithmetic credit; store worked solutions for feedback

## Key Decision Criteria Checklist

- [List key criteria when applicable, e.g., formula selection accuracy, computational efficiency, precision requirements, unit standardization, error bounds, etc.]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Method/Approach A | Preferred Method/Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Method description] | [Method description] | [Decision guidance] |
| [Criterion 2] | [Method description] | [Method description] | [Decision guidance] |

---

## Problems 1–12

### P1: Calculate blockchain throughput

**Language:** N/A (calculation)  
**Difficulty:** Foundational  
**Bloom:** Apply

**Problem:** A blockchain processes 500 transactions per block with an average block time of 6 seconds. Calculate the throughput in transactions per second (TPS).

**Answer:** 83.33 TPS

**Units:** transactions per second (TPS)

**Tolerance:** ±2%

**Worked solution:**
1. Transactions per block: 500
2. Block time: 6 seconds
3. TPS = 500 / 6 = 83.33 TPS

**Partial credit rules:**
- Correct formula with arithmetic error: 70% of question points
- Correct setup but incomplete: 50% of question points

### Supporting Artifacts (problem context)

- Tables (e.g., input parameters, calculation summary)
- Formulas in LaTeX/KaTeX notation (e.g., `$T = N / R$`)
- Mermaid diagrams (e.g., data flow, relationships) when helpful
- Analogies, comparisons to clarify concepts

### Technical Evaluation Considerations (for graders)
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

### Terminology & Key Concepts (problem domain)

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

### Context & Background (problem domain)

- Historical Evolution: [...]
- Technical Context: [...]
- Market Dynamics: [When calculation involves economic/financial aspects]
- Key Events & Statistics: [When relevant to the calculation]

### Assumptions & Preconditions (problem setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (expected reasoning)

- [Sanity check, benchmark comparison, or real-world validation]

### Counterexamples & Edge Cases (alternative scenarios)

- [Scenario that would change the calculation + impact]

### Alternatives Considered (calculation approaches)

- [Alternative method, trade-off summary, selection rationale]

### Trade-offs & Decision Guidance (when relevant)

- [Critical trade-off analysis in calculation approach selection; decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Perspective-Based Insights (problem domain)

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

### Market & Macro Systems Analysis (for advanced problems)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (for advanced problems)

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

- **[Tool/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes; formulas, performance characteristics]

### Authoritative Literature (formula/benchmark sources)

- **[Paper/Standard/Documentation]:** [Source for formula, benchmark, or calculation method; core findings, practical implications]

### Actionable Conclusions (problem takeaway)

- [Key insight, practical implication, design guidance; prioritized action]

### Open Questions & Research Agenda (for advanced problems)

- Remaining Challenges: [... calculation limitations, uncertainty ranges]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations

- **References:** List sources for formulas, benchmarks, or standards referenced in the problem.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
```
