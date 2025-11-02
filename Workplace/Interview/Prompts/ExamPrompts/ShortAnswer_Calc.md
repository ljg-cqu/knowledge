# Short Answer / Numeric Calculation Prompt Template

Purpose: Short constructed-response items requiring concise numeric or short-text answers (calculations, conversions, brief justification).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Problem Scope & Distribution

- Generate 20–28 problems in total. Distribute problems across topic clusters according to the MECE coverage plan so each cluster receives proportional emphasis.
- **Stretch tier (senior/expert):** For advanced cohorts, target 28–32 problems total while preserving the difficulty mix and proportional cluster coverage.
- Number problems sequentially (P1, P2, …) with matching anchors in the Contents block.
- Maintain Foundational (25%), Intermediate (50%), Advanced (25%) distribution aligned to Bloom Apply/Analyze: foundational problems apply formulas directly, intermediate ones require multi-step calculations and unit conversions, advanced ones demand method selection, assumption justification, or result interpretation.

### Data & Context Requirements

- Provide self-contained problems with all necessary data, using MECE principles to avoid overlapping question types. Cover technical (techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations including energy/resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, permission/consensus governance, upgrade/rollback strategies, risks, costs, use cases) pillars.
- State units and conventions explicitly (e.g., MB = 10^6 vs 2^20 bytes, percentages vs decimals, rounding rules) and list acceptable alternative answers when ambiguity exists.
- Mix calculation types: throughput, latency, gas costs, tokenization ratios, collateralization rates, consensus performance, resource consumption, unit conversions, formula applications, short justifications (2–3 sentences). For RWA scenarios, include asset valuation, transaction fee modeling, compliance thresholds.
- Supply contextual framing: historical evolution, technical context, regulatory landscape, key events, statistical data, real-world application scenarios.
- Cite authoritative formulas/benchmarks via standards, white/yellow papers, official documentation, peer-reviewed studies.

### Analytical Coverage & Diagnostics

- Document assumptions, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions (especially for advanced problems).
- Highlight boundary conditions and sensitivity analyses, noting failure/unhappy path outcomes and expected mitigation or rollback guidance.
- Capture common computational/conceptual misconceptions each problem surfaces, plus corrective notes for the template.
- Contrast alternative methods, assumptions, or tooling (formula variants, estimation techniques) and record decision criteria.
- Integrate governance/trust metrics (permission thresholds, trust parameters, privacy/transparency metrics, design-pattern choices, error-tolerance bounds, reliability/HA metrics) when relevant.
- Cover perspectives across engineering disciplines, architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- For advanced problems, add philosophical, economic, financial, capital-market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical angles when calculations influence those domains.
- Surface adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers), calculation limitations, uncertainty ranges, emergent risks, and research agendas.

### Content Design

- Target senior/expert Apply/Analyze capability: applying formulas, performing multi-step calculations, interpreting results, justifying reasoning with technical depth and practical awareness.
- Specify exact expected answers with units and tolerances (e.g., ±2% for percentages, ±0.5 for small integers).
- Provide worked solutions (2–4 steps) showing method, intermediate values, and final result in clear notation (mathematical expressions, pseudocode, or tables).
- Define partial-credit rules (e.g., correct method with arithmetic error = 70%; correct setup but incomplete = 50%).
- Evaluate responses against technical metrics (performance, algorithm complexity, resource consumption) and business metrics (cost efficiency, impact, market fit).
- Discuss trade-offs such as accuracy vs computational cost, security vs performance; analyze permission boundaries, trust thresholds, privacy requirements, error-tolerance parameters when relevant.

### Evaluation & Grading

- Establish normalization rules for numeric answers (strip commas, accept scientific notation, case-insensitive units).
- Specify tolerances per problem type (percentage or absolute ranges) and require manual review for short justifications.
- Provide grader notes including model answers, acceptable variations, borderline cases, and guidance for awarding partial credit.

### Execution & Format

- Plan thoroughly before authoring; ensure coverage map, difficulty mix, and artifact list are satisfied.
- Present content in Markdown with clear headings, fenced calculation steps, and explicit answer lines (e.g., “**Answer:** 42.5 ms”).
- Use tables to organize inputs/parameters and LaTeX/KaTeX formulas when helpful (e.g., `$T = N / R$`).
- Employ clarifying aids (mermaid diagrams, code snippets, analogies, comparisons) while maintaining mermaid portability (no edge labels; quote node labels containing special characters such as parentheses/slashes).
- Explain key terms/units as needed; ground problems in real-world scenarios.
- Provide a compact Contents section linking to major headings and all problems (P1–Pn) with GitHub-compatible anchors.
- Include required prefatory sections: Contents; Executive Summary (2–3 bullets on goals, calculation scope, grading approach); Coverage & Difficulty Summary (difficulty distribution table + topic cluster mapping); Glossary & Acronym Index (key formulas/units/conventions); How to Use This in Interviews (machine-grading/tolerance guidance, manual review notes); Key Decision Criteria Checklist (formula selection, accuracy requirements, computational approach, etc.); Key Decision Criteria Matrix (Quick Picks) mapping calculation methods to criteria when applicable.
- Tag each problem with Difficulty, Bloom level, and question type (calculation, conversion, justification).
- Base content on current authoritative sources; cross-reference for accuracy, completeness, relevance, MECE compliance.
- Maintain holistic reasoning by linking technical depth, macro insight, and MECE structure; cite formulas/benchmarks in APA 7th edition.

### Shared Evaluation Checklist (apply to every problem)

- **Technical Evaluation**: performance metrics, algorithm complexity, resource consumption, reliability/high availability, distributed consistency guarantees, hardware requirements & energy/resource usage.
- **Business Evaluation**: cost efficiency, impact, market fit.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: define formulas/units with analogies/examples for graders.
- **Context & Background**: outline historical evolution, regulatory context, technical background, key events/statistics influencing the calculation.
- **Validation & Evidence Checks**: provide benchmarks, data points, or studies verifying formulas and results.
- **Counterexamples & Edge Cases**: list scenarios that challenge assumptions and corresponding mitigations.
- **Alternatives & Trade-offs**: compare calculation methods, note trade-offs, specify decision criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: evaluate problem implications across engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: assess systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models.
- **Inference Summary**: capture adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: identify stakeholders, communication cadence/channels, alignment tactics relevant to the calculation outcome.
- **Organizational & Strategic Fit**: analyze business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation.
- **Codebase & Library References**: cite tools/libraries used for calculations (stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes).
- **Authoritative Literature**: reference standards, papers, documentation supporting formulas or benchmarks.
- **Actionable Conclusions**: summarize lessons, best practices, prioritized actions.
- **Open Questions & Research Agenda**: list unresolved challenges, hypotheses, experiments, data/resource needs, timelines/ownership for deeper exploration.
- **APA Style Source Citations**: ensure references comply with APA 7th edition and support problem content.

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

**Worked Solution:**
1. Throughput = transactions per block ÷ block time
2. 500 ÷ 6 = 83.33 TPS

**Partial Credit:** Method correct, arithmetic rounded incorrectly (±2%) = 70%

**Human Check:** Validate rounding explanation if answer differs by <±2%

**Misconception Focus:** [Clarify the mistaken assumption this calculation addresses and the guidance interviewers should reinforce.]

**Failure Path Insight:** [Describe the failure scenario or incorrect interpretation this calculation is meant to uncover and the mitigation guidance.]

**Comparison Notes:** [Capture the comparison/contrast insight (e.g., method A vs method B) and the decision criteria guiding the preferred approach.]

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
