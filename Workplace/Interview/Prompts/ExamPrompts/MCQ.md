# Multiple-Choice (MCQ) Prompt Template

Purpose: Single-best-answer MCQs (4 options) with plausible distractors and concise rationales for graders.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Question Scope & Distribution

- Generate 15–25 MCQs per topic cluster (aim for 20+ for comprehensive coverage, 15–18 for focused clusters).
- Number questions sequentially (Q1, Q2, …) and include anchors in the Contents section.
- Maintain Foundational (30%), Intermediate (50%), Advanced (20%) distribution aligned to Bloom Remember/Understand/Apply: foundational questions check factual recall, intermediate questions test relationships and approach selection, advanced questions require applying concepts to nuanced scenarios.

### Topic Selection & Context

- Use MECE principles to assemble topics spanning technical (techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations including energy/resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, permission/consensus governance, upgrade/rollback strategies, risks, costs, use cases) dimensions. For blockchain/RWA contexts emphasize consensus mechanisms, tokenization standards, custody models, scalability solutions, regulatory frameworks.
- Balance factual recall, conceptual understanding, and application-level questions across the bank.
- Base content on authoritative repositories, SDKs, tooling suites, standards, white/yellow papers, peer-reviewed studies, books/manuals, vetted encyclopedias; provide evidence backing correct answers.
- Include scenarios highlighting failure/unhappy paths with rollback or mitigation expectations, and ensure comparisons (protocol choices, architectural patterns, governance models) capture rationale for preferred options.
- Address perspectives across engineering (front-end, back-end, full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- Integrate governance/trust dimensions (permission vs decentralization, trust guarantees, privacy/transparency balances, design-pattern choices, error tolerance, reliability/high availability) and collaboration/organizational dynamics (cross-functional communication, governance models, institutional constraints, change management).
- Incorporate philosophical, economic, financial, capital market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical lenses where relevant.
- For advanced items, surface adoption signals, interoperability impacts, roadmap implications, operational risks, unresolved research questions, and emergent risks.

### Distractor Design & Diagnostic Focus

- Craft stems that are concise (1–2 sentences), avoid double negatives, ambiguous phrasing, or “all/none of the above” unless justified.
- Provide four options (A–D) of similar length and structure; ensure exactly one correct answer and mutually exclusive distractors.
- Map each distractor to a common misconception, near miss, or outdated practice; document corrective insights for interviewer debriefs.
- Offer rationales: 1–2 sentence explanation for the correct answer plus brief notes clarifying why each distractor is incorrect.
- Include comparison cues, failure-path considerations, and decision criteria within the explanation notes.

### Evaluation & Grading

- Machine-grade by exact match of answer letter (A/B/C/D); if shuffling options, retain metadata for the correct index.
- Partial credit typically not awarded; optionally provide hints/retries in formative contexts.
- Perform quality checks ensuring one unambiguous correct option and defensibly incorrect distractors.

### Execution & Format

- Plan coverage and difficulty distribution before writing.
- Present questions in Markdown with clear headings; use fenced code blocks for stems/options when including code or configuration snippets.
- Employ clarifying aids (mermaid diagrams, tables, code snippets, analogies, comparisons, formulas) with mermaid portability (no edge labels; quote node labels containing special characters such as parentheses/slashes).
- Explain key terminology where needed and integrate historical, regulatory, technical, and statistical context to ground questions in real-world applications.
- Provide a compact Contents section linking to major headings and each question (Q1–Qn) using GitHub-compatible anchors.
- Include required prefatory sections: Contents; Executive Summary (2–3 bullets on assessment goals, topic coverage, grading approach); Coverage & Difficulty Summary (difficulty distribution table + topic cluster mapping); Glossary & Acronym Index (key terms/concepts); How to Use This in Interviews (machine-grading approach, randomization notes, assessment context); Key Decision Criteria Checklist (domain-specific considerations); Key Decision Criteria Matrix (Quick Picks) mapping concepts to decision criteria when applicable.
- Tag each item with Difficulty and Bloom level.
- Base material on current authoritative sources; cross-reference for accuracy, completeness, relevance, and MECE compliance.
- Harmonize technical depth with broader context and macro insight; cite factual claims (protocol specs, performance benchmarks, regulatory requirements) using APA 7th edition.

### Shared Evaluation Checklist (apply to every question)

- **Technical Evaluation**: throughput/latency, security, scalability, maintainability, algorithm complexity, error tolerance, distributed consistency, hardware requirements & energy/resource consumption when relevant.
- **Business Evaluation**: cost, efficiency, impact, market fit.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: provide definitions with analogies/formulas/examples for graders.
- **Context & Background**: summarize historical evolution, regulatory landscape, technical context, market dynamics, key events/statistics informing the question.
- **Validation & Evidence Checks**: cite data points or references supporting the correct answer.
- **Counterexamples & Edge Cases**: note scenarios challenging the answer and provide clarifications.
- **Alternatives & Trade-offs**: compare options, articulate trade-offs, and list decision criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: evaluate question relevance across engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: discuss systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models where appropriate.
- **Inference Summary**: identify adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: outline stakeholders, communication cadence/channels, alignment tactics connected to question themes.
- **Organizational & Strategic Fit**: assess business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation.
- **Codebase & Library References**: list repositories, SDKs, or libraries with stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes when the question references them.
- **Authoritative Literature**: cite standards, documentation, audits, or papers underpinning the question.
- **Actionable Conclusions**: state key takeaways or decision principles reinforced by the question.
- **Open Questions & Research Agenda**: log unresolved issues, hypotheses, needed experiments/data, timelines/ownership for further study.
- **APA Style Source Citations**: ensure all references follow APA 7th edition and directly support the content.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Questions 1–25](#questions-125)
  - [Q1: Question text](#q1-question-text)
  - [Q2: Question text](#q2-question-text)
  - ... (link to each question)

## Executive Summary

- [2–3 bullets: assessment goals, topic coverage, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Questions |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Questions |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Q1–Qx |
| [Cluster B] | [Scope/Boundaries] | Q(x+1)–Qy |

## Glossary & Acronym Index

- [Key terms and concepts tested]

## How to Use This in Interviews

- Machine-gradable by exact-match of answer letter; shuffle options client-side to randomize
- Use for formative assessment or timed quizzes; review distractor analytics to identify misconceptions

## Key Decision Criteria Checklist

- [List key criteria when applicable to question domain, e.g., technology selection criteria, implementation approach evaluation, trade-off prioritization, etc.]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Option/Approach A | Preferred Option/Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Option description] | [Option description] | [Decision guidance] |
| [Criterion 2] | [Option description] | [Option description] | [Decision guidance] |

---

## Questions 1–25

### Q1: Which consensus mechanism prioritizes finality over throughput in permissioned blockchains?

**Language:** N/A (or specify if code-based, e.g., python, javascript, solidity)  
**Difficulty:** Intermediate  
**Bloom:** Apply

**Stem:** Which consensus mechanism prioritizes finality over throughput in permissioned blockchains?

**Options:**
- A. Raft
- B. PBFT
- C. Proof of Work
- D. Proof of Stake

**Answer:** B

**Rationale:**
- **Correct (B):** PBFT provides Byzantine fault tolerance with deterministic finality, prioritizing safety over speed in permissioned settings.

**Distractor notes:**
- A: Raft provides crash fault tolerance but not Byzantine fault tolerance; suitable for non-adversarial environments.
- C: Proof of Work is used in permissionless blockchains and prioritizes decentralization over finality.
- D: Proof of Stake is primarily for permissionless chains; finality mechanisms vary by implementation.

**Misconception Focus:** [State the misconception this question addresses and the key corrective feedback for interviewers.]

**Failure Path Insight:** [Describe the failure or unhappy path this scenario surfaces and the mitigation/testing guidance to emphasize.]

**Comparison Notes:** [Summarize the comparison/contrast takeaways and decision criteria highlighted by this question.]

### Supporting Artifacts (when helpful for complex MCQs)

- Mermaid diagrams (e.g., concept relationships, architecture comparison)
- Tables (e.g., feature comparison, performance benchmarks)
- Code snippets, analogies, formulas to clarify technical concepts

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

### Terminology & Key Concepts (for context)

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

### Context & Background (when relevant)

- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Technical Context: [...]
- Key Events & Statistics: [...]

### Evaluation Dimensions Tested (for graders)

- Technical: [Performance, security, scalability, complexity aspects tested]
- Business: [Cost, efficiency, impact, market fit aspects tested]
- Trade-offs: [Key trade-offs examined in question]

### Assumptions & Preconditions (question setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (expected reasoning)

- [Data point, benchmark, or experiment backing the correct answer]

### Counterexamples & Edge Cases (alternative scenarios)

- [Scenario that challenges the main answer + mitigation]

### Alternatives Considered (distractor analysis)

- [Why plausible alternatives were rejected; trade-off summary]

### Trade-offs & Decision Guidance (when relevant)

- [Critical trade-off analysis tested in the question; decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Perspective-Based Insights (question design angle)

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

### Market & Macro Systems Analysis (for advanced questions)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (for advanced questions)

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

### Codebase & Library References (when testing specific tools/frameworks)

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

### Authoritative Literature (question grounding)

- **[Paper/Standard/Documentation]:** [Source for the factual content tested]

### Actionable Conclusions (learning objective)

- [Key takeaway or principle the question reinforces; prioritized action]

### Open Questions & Research Agenda (for advanced questions)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations

- **References:** List sources for factual claims, performance benchmarks, or protocol specifications.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
```
