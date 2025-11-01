# True / False (T/F) Prompt Template

Purpose: Short, unambiguous declarative statements for binary judgment (True/False). Include a brief rationale when full credit requires it.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 12–20 True/False statements per topic cluster. Difficulty distribution: Foundational (40%), Intermediate (40%), Advanced (20%).
- **Numbering:** Number all statements sequentially (S1, S2, etc.) for easy tracking and reference. Include statement numbers in Contents links.
- **Bloom Taxonomy:** Target Remember/Understand/Apply levels. Foundational statements test factual recall; intermediate statements require understanding of principles and relationships; advanced statements involve applying concepts to judge scenario-based claims.
- **Statement Design & Elements:** Create factual, unambiguous declarative statements. Use MECE principles to avoid overlapping or contradictory items within a bank. Cover: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, market dynamics, permission/consensus governance, upgrade planning/rollback strategies, risks, costs, facts, use cases).
- **Precision:** Keep statements short (≤2 lines) and avoid double negatives, vague qualifiers (e.g., "often", "usually"), or ambiguous technical terms.
- **Validation & Evidence Checks:** Provide authoritative sources and evidence backing each statement's truth or falsity.
- **Counterexamples & Edge Cases:** Include scenarios where statements might seem different or require clarification.
- **Scope:** Cover key facts, definitions, principles, and simple scenario judgments. Mix foundational recall with conceptual understanding.
- **Context:** Include relevant historical context, regulatory/legal landscape, technical background, and statistical data in rationales.
- **Codebases & Libraries:** When statements involve specific frameworks/tools, ensure accuracy reflects current authoritative repositories, SDKs, and official documentation.
- **Authoritative Literature:** Base statements on white/yellow papers, peer-reviewed studies, standards, books/manuals, and vetted encyclopedic resources.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions in rationales where relevant.
- **Governance & Trust Dimensions:** Include statements on permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** Include relevant statements from philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as appropriate.
- **Collaboration & Organizational Dynamics:** Include statements on cross-functional communication, governance models, institutional constraints, change management, and cultural alignment where relevant.
- **Organizational & Strategic Operations:** Include statements on business model implications, institutional capabilities, change readiness, and long-term strategic positioning where relevant.
- **Inference Lists:** For advanced statements, test understanding of adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- **Open Questions & Research:** For advanced statements, surface awareness of unresolved problems, knowledge gaps, emergent risks per topic cluster.

### 2. Content Design

- **Target Level:** Remember/Understand/Apply (Bloom). Use factual statements for lower levels; use concise scenario-based judgments for higher levels (e.g., "Given X constraint, approach Y is optimal"). Senior/expert level statements should test deep technical understanding and awareness of nuanced distinctions.
 - **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Rationale:** Provide a 1–2 sentence rationale explaining why the statement is true or false. Include a one-sentence note on common misconceptions to aid feedback.
- **Justification (Optional):** For higher-credit items, require a brief written justification (2–3 sentences) in addition to the T/F answer. State scoring split (e.g., 70% for correct letter + 30% for valid rationale).
- **Evaluation Dimensions:** Technical (performance, security, scalability, algorithm complexity, error tolerance, distributed consistency) and business (cost, efficiency, impact, market fit) considerations when relevant.
- **Trade-offs:** For advanced statements, test understanding of trade-offs (e.g., "Byzantine fault tolerance always outperforms crash fault tolerance" - False, because of throughput trade-offs).
- **Governance & Assurance:** Include statements testing understanding of permission boundaries, trust models, privacy/transparency requirements, and reliability expectations.

### 3. Evaluation & Grading

- **Grading:** Machine-gradable by exact-match of answer letter (A/True or B/False). Normalize accepted inputs (e.g., accept "A", "True", "true", "T").
- **Partial Credit:** If justification is required, award partial credit for correct answer with weak justification or incorrect answer with valid reasoning that identifies a key issue.
- **Quality Check:** Ensure statements are defensible with authoritative sources; avoid subjective or opinion-based items.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use clearly labeled statement, options (A/B), answer, and rationale. Use fenced blocks for code snippets if the statement references code behavior.
- **Clarity Aids:** When helpful, use mermaid diagrams, tables, or analogies to clarify technical concepts. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Ensure statements use precise technical language; explain key concepts in rationales.
- **Context Integration:** Include relevant historical, regulatory, or technical context in rationales where appropriate.
- **Real-World Grounding:** Base statements on real-world facts and practical scenarios.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all statements (S1–Sn) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and S1–Sn)
  - Executive Summary (2–3 bullets: assessment goals, statement scope, grading approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and statement indices); Topic Cluster Mapping Table (Cluster → scope → statement indices)
  - Glossary & Acronym Index (key terms and concepts covered)
  - How to Use This in Interviews (machine-grading by exact-match, optional justification requirements)
  - Key Decision Criteria Checklist (when applicable to statement domain)
  - Key Decision Criteria Matrix (Quick Picks) for evaluating claims (when applicable)
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Ensure statements reflect current understanding and cross-disciplinary implications.
- **Citations:** Include APA 7th edition references for statements from external standards, protocol specifications, regulatory requirements, or published research.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Statements 1–20](#statements-120)
  - [S1: Statement topic](#s1-statement-topic)
  - [S2: Statement topic](#s2-statement-topic)
  - ... (link to each statement)

## Executive Summary

- [2–3 bullets: assessment goals, statement scope, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Statements |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Statements |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | S1–x |
| [Cluster B] | [Scope/Boundaries] | S(x+1)–y |

## Glossary & Acronym Index

- [Key terms and concepts covered]

## How to Use This in Interviews

- Machine-gradable by exact-match of answer (A/True or B/False); normalize inputs ("A", "True", "true", "T")
- Optional: require justification for higher-credit items (70% for correct letter + 30% for rationale)

## Key Decision Criteria Checklist

- [List key criteria when applicable to statement domain, e.g., factual accuracy verification, principle application, scenario judgment criteria, etc.]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | True Condition | False Condition | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Condition description] | [Condition description] | [Decision guidance] |
| [Criterion 2] | [Condition description] | [Condition description] | [Decision guidance] |

---

## Statements 1–20

### S1: BFT malicious node tolerance

**Language:** N/A (or specify if code-based, e.g., python, javascript, solidity)  
**Difficulty:** Intermediate  
**Bloom:** Understand

**Statement:** Byzantine Fault Tolerance consensus algorithms can tolerate up to 50% malicious nodes.

**Options:**
- A. True
- B. False

**Answer:** B

**Rationale:**
- **Correct:** BFT algorithms (e.g., PBFT) can tolerate up to (n-1)/3 malicious nodes, not 50%. For example, in a 4-node network, only 1 Byzantine node can be tolerated.
- **Common misconception:** Confusion with crash fault tolerance (e.g., Raft), which tolerates up to 50% crash failures.

**Citation:** Castro, M., & Liskov, B. (1999). Practical Byzantine fault tolerance. *OSDI*, 99, 173–186.

### Supporting Artifacts (when helpful for complex statements)

- Mermaid diagrams (e.g., concept relationships, fault tolerance models)
- Tables (e.g., comparison of fault tolerance types)
- Formulas, code snippets, analogies to clarify concepts

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

### Evaluation Dimensions (for statement verification)

- Technical: [Performance, security, complexity aspects of the claim]
- Business: [Cost, efficiency, impact aspects when relevant]
- Trade-offs: [Trade-offs implicit in the statement]

### Assumptions & Preconditions (statement setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (statement verification)

- [Data point, benchmark, or authoritative source backing the truth/falsity]

### Counterexamples & Edge Cases (alternative scenarios)

- [Scenario where statement might appear different + clarification]

### Alternatives Considered (statement variations)

- [Related statements considered, why this specific wording was chosen]

### Trade-offs & Decision Guidance (when relevant)

- [Critical trade-off analysis implicit in the statement; decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Perspective-Based Insights (statement design angle)

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

### Market & Macro Systems Analysis (for advanced statements)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (for advanced statements)

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

### Codebase & Library References (when testing specific implementations)

- **[Tool/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

### Authoritative Literature (statement grounding)

- **[Paper/Standard/Documentation]:** [Source for the factual claim; core findings, practical implications]

### Actionable Conclusions (learning objective)

- [Key principle or distinction the statement reinforces; prioritized action]

### Open Questions & Research Agenda (for advanced statements)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### Context & Background (when relevant to statement)

- Historical Evolution: [How this fact/principle evolved]
- Technical Context: [Surrounding technical context]
- Market Dynamics: [When statement involves economic/market aspects]

### APA Style Source Citations

- **References:** List sources for factual claims from external standards, protocol specifications, regulatory requirements, or published research.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
```

````
```
