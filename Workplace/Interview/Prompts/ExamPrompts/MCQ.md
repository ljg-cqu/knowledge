# Multiple-Choice (MCQ) Prompt Template

Purpose: Single-best-answer MCQs (4 options) with plausible distractors and concise rationales for graders.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 15–25 MCQs per topic cluster (aim for 20+ when comprehensive coverage is needed; use 15–18 for focused or narrow topic clusters). Difficulty distribution: Foundational (30%), Intermediate (50%), Advanced (20%).
- **Numbering:** Number all questions sequentially (Q1, Q2, etc.) for easy tracking and reference. Include question numbers in Contents links.
- **Bloom Taxonomy:** Target Remember/Understand/Apply levels. Foundational MCQs test factual recall; intermediate MCQs require understanding relationships and selecting correct approaches; advanced MCQs demand application of concepts to novel scenarios or selection among nuanced alternatives.
- **Topic Selection & Elements:** Use MECE principles to select topics. Ensure comprehensive coverage across: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, market dynamics, permission/consensus governance, upgrade planning/rollback strategies, risks, costs, use cases). For blockchain architecture (RWA), emphasize consensus mechanisms, asset tokenization standards, custody models, scalability solutions, and regulatory frameworks.
- **Distractor Design:** Ensure distractors map to common misconceptions, near-misses, or outdated practices. Distractors must be mutually exclusive and plausible to candidates unfamiliar with the topic.
- **Balance:** Mix factual recall, conceptual understanding, and application-level questions within a bank.
- **Validation & Evidence Checks:** Provide clear evidence backing correct answers from authoritative sources.
- **Counterexamples & Edge Cases:** Include scenarios that challenge straightforward interpretations.
- **Codebases & Libraries:** When testing knowledge of specific frameworks/tools, ensure questions reflect current authoritative repositories, SDKs, tooling suites, language support, and maturity levels.
- **Inference Lists:** For advanced MCQs, test understanding of adoption signals, interoperability impacts, roadmap implications, and operational risks.
- **Authoritative Literature:** Base questions on white/yellow papers, peer-reviewed studies, standards, books/manuals, and vetted encyclopedic resources.
- **Critical Thinking Artifacts:** Include questions that test assumptions, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions.
- **Collaboration & Organizational Dynamics:** Include questions on cross-functional communication, governance models, institutional constraints, and change management where relevant.
- **Governance & Trust Dimensions:** Test understanding of permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** Include questions integrating philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as appropriate.
- **Organizational & Strategic Operations:** Include questions on business model implications, institutional capabilities, change readiness, and long-term strategic positioning where relevant.
 
- **Open Questions & Research:** For advanced questions, surface awareness of unresolved problems, knowledge gaps, emergent risks, and prioritized investigation tracks per topic cluster.

### 2. Content Design

- **Target Level:** Remember/Understand/Apply (Bloom). Adjust difficulty by the depth of reasoning required to eliminate distractors. Senior/expert level questions should test deep technical understanding and broad strategic perspective.
 - **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Stem:** Provide a clear, concise stem (1–2 sentences). Avoid double negatives, ambiguous phrasing, or "all of the above" / "none of the above" unless pedagogically justified.
- **Options:** Four options labeled A–D. Exactly one correct answer. Distractors should be similar in length and structure to the correct answer to avoid cueing.
- **Rationale:** Provide a 1–2 sentence rationale for the correct answer and brief notes (1 sentence each) explaining why distractors are incorrect (e.g., "B is incorrect because it confuses consensus finality with transaction confirmation").
- **Evaluation Dimensions:** Technical (throughput/latency performance, security, scalability, maintainability, reliability/HA, algorithm complexity, error tolerance, distributed consistency) and business (cost, efficiency, impact, market fit) considerations.
- **Trade-offs:** For advanced MCQs, test understanding of essential trade-offs (e.g., permissioning vs. decentralization, trust/privacy balances, algorithmic complexity limits, upgrade path risks).
- **Governance & Assurance:** Include questions on permission boundaries, trust models, privacy/transparency requirements, error-tolerance envelopes, and distributed consistency guarantees.
- **Macro Narratives:** For advanced questions, relate to systemic dynamics (economic cycles, stock/crypto market behaviors, liquidity and valuation trends, regulatory shifts, geopolitical/security considerations, societal adoption patterns, organizational behavior, historical precedents, macroeconomic/industry economic models).

### 3. Evaluation & Grading

- **Grading:** Machine-gradable by exact-match of the answer letter (A/B/C/D). If randomizing option order, preserve correct index in metadata.
- **Partial Credit:** Not typically used for MCQs; consider offering hints or retries in formative assessments.
- **Quality Check:** Validate that exactly one option is unambiguously correct and that all distractors are defensibly wrong.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use fenced code blocks for code snippets or configuration examples in stems/options. Include mermaid diagrams or comparison tables when clarifying technical concepts.
- **Clarification Aids:** Use diverse visualization types: mermaid diagrams (structural, behavioral, analytical), tables, code snippets, analogies, comparisons, formulas. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Explain key concepts/terminologies clearly using analogies, formulas, etc. as needed.
- **Context Integration:** Include relevant historical evolution, legal/regulatory landscape, future trends, key events, and statistical data where appropriate.
- **Real-World Grounding:** Base questions on real-world applications; mix theoretical, practical, and scenario-based contexts.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all questions (Q1–Qn) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and Q1–Qn)
  - Executive Summary (2–3 bullets: assessment goals, topic coverage, grading approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and question indices); Topic Cluster Mapping Table (Cluster → scope → question indices)
  - Glossary & Acronym Index (key terms and concepts tested)
  - How to Use This in Interviews (machine-grading approach, option randomization notes, and assessment context)
  - Key Decision Criteria Checklist (when applicable to question domain)
  - Key Decision Criteria Matrix (Quick Picks) mapping concepts to decision criteria (when applicable)
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Harmonize technical depth with broader context and macro-level insight; trace implications across disciplines while maintaining MECE clarity.
- **Citations:** Include APA 7th edition references for factual claims (protocol specs, performance benchmarks, regulatory requirements) requiring authoritative sources.

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

````
```
