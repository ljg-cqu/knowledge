# Cloze / Fill-in-the-Blank Prompt Template

Purpose: Short fill-in-the-blank items to test precise recall (definitions, terms, short phrases, equations).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 10–15 cloze items per topic cluster (aim for 12+ when comprehensive coverage is needed; use 10–11 for focused or narrow topic clusters). Difficulty distribution: Foundational (30%), Intermediate (50%), Advanced (20%).
- **Numbering:** Number all items sequentially (Item 1, Item 2, etc.) for easy tracking and reference. Include item numbers in Contents links.
- **Bloom Taxonomy:** Target Remember/Understand levels. Foundational items test direct recall of definitions; intermediate items require understanding of relationships between concepts; advanced items test comprehension of nuanced distinctions or context-dependent terminology.
- **Term Selection & Elements:** Use MECE principles to choose target terms/phrases. Cover: **Technical** (techniques, algorithms, algorithm complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), **Theoretical** (theories, principles, axioms, laws, assumptions, models), and **Practical** (regulations, key terms, acronyms, market dynamics, permission/consensus governance, risks, costs, use cases).
- **Scope:** Keep each item narrowly scoped and unambiguous. Avoid overlapping blanks or ambiguous phrasing that could confuse candidates.
- **Validation & Evidence Checks:** Provide authoritative sources confirming term definitions and usage.
- **Counterexamples & Edge Cases:** Include related terms often confused with target terms, with clear distinctions.
- **Context:** Provide sufficient surrounding text to make the blank unambiguous; include relevant historical evolution, legal/regulatory landscape, future trends, key events, and statistical data.
- **Codebases & Libraries:** When testing library/framework terminology, ensure terms reflect current authoritative repositories, SDKs, and tooling suites.
- **Authoritative Literature:** Base terminology on white/yellow papers, peer-reviewed studies, standards, books/manuals, and vetted encyclopedic resources.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases (near-miss terms), alternatives considered (synonyms/related terms), and actionable conclusions in grader notes where relevant.
- **Governance & Trust Dimensions:** Include terms related to permission models vs. decentralization levels, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** Include relevant terms from philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as appropriate.
- **Collaboration & Organizational Dynamics:** Include terms related to cross-functional communication, governance models, institutional constraints, change management, and cultural alignment.
- **Organizational & Strategic Operations:** Include terminology related to business model implications, institutional capabilities, change readiness, and long-term strategic positioning.
- **Inference Lists:** Include terms related to adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- **Open Questions & Research:** Include awareness of terminology related to unresolved problems, knowledge gaps, emergent risks per topic cluster.

### 2. Content Design

- **Target Level:** Remember/Understand (Bloom). Test factual recall, definition accuracy, and basic comprehension (senior/expert level with deep technical understanding and broad strategic perspective).
- **Answer Format:** Provide canonical answers as arrays including accepted synonyms (e.g., ["scalability", "scale"]) and alternate spellings (e.g., "decentralization" vs "decentralisation").
- **Normalization Rules:** Define explicit rules: case-insensitive matching, whitespace trimming, punctuation stripping. State rounding/formatting conventions for numeric answers.
- **Partial Credit:** State per-blank scoring (e.g., 1 point per correct blank) and tolerance ranges for numeric values.

### 3. Evaluation & Grading

- **Acceptance Lists:** Provide a list of acceptable answers per blank; include common variations and synonyms.
- **Tolerances:** For numeric blanks, specify acceptable ranges (e.g., ±2% or ±0.5 units).
- **Grader Notes:** Document borderline cases and common near-miss answers; provide guidance on when to award partial credit.
- **Distractor Notes:** Include a brief note on why common wrong answers are incorrect to aid feedback systems.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use underscores (___) or brackets ([blank]) to indicate blanks clearly.
- **Accessibility:** Provide ALT text for any inline images or diagrams used in cloze items.
- **Clarity Aids:** When helpful, use mermaid diagrams, tables, code snippets, or analogies to provide context. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Ensure surrounding context clearly defines terms; use precise technical language.
- **Context Integration:** Include relevant historical, regulatory, or technical context in the surrounding text where appropriate.
- **Real-World Grounding:** Base items on real-world terminology and practical applications.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all items (Item 1–Item n) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and Item 1–Item n)
  - Executive Summary (2–3 bullets: assessment goals, term coverage scope, scoring approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and item indices); Topic Cluster Mapping Table (Cluster → scope → item indices)
  - Glossary & Acronym Index (core terms tested in cloze items)
  - How to Use This in Interviews (auto-grading guidance and normalization rules)
  - Key Decision Criteria Checklist (when applicable to terminology domain)
  - Key Decision Criteria Matrix (Quick Picks) for term selection/usage patterns (when applicable)
- **Tags:** Label each item with Difficulty and Bloom level.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Ensure terms reflect current best practices and cross-disciplinary relevance.
- **Citations:** Include APA 7th edition references for definitions from authoritative sources (standards, papers, official documentation).

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Items 1–15](#items-115)
  - [Item 1: Topic](#item-1-topic)
  - [Item 2: Topic](#item-2-topic)
  - ... (link to each item)

## Executive Summary

- [2–3 bullets: assessment goals, term coverage scope, scoring approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Items |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Items |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Item 1–x |
| [Cluster B] | [Scope/Boundaries] | Item (x+1)–y |

## Glossary & Acronym Index

- [Core terms tested in cloze items]

## How to Use This in Interviews

- Auto-gradable with normalization rules; suitable for timed quizzes or self-assessment
- Per-blank scoring enables partial credit; review borderline answers manually

## Key Decision Criteria Checklist

- [List key criteria when applicable to terminology domain, e.g., precision requirements, context-sensitivity, terminology standardization]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Term/Usage A | Preferred Term/Usage B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Term/usage description] | [Term/usage description] | [Decision guidance] |
| [Criterion 2] | [Term/usage description] | [Term/usage description] | [Decision guidance] |

---

## Items 1–15

### Item 1

**Language:** N/A (or specify if code-based, e.g., python, javascript, solidity)  
**Difficulty:** Foundational  
**Bloom:** Remember

**Text:** The blockchain trilemma consists of ___, ___, and ___.

**Answers:**
- Blank 1: scalability (accept: scalability, scale)
- Blank 2: security (accept: security)
- Blank 3: decentralization (accept: decentralization, decentralised)

**Normalization:** case-insensitive, trim whitespace, strip punctuation  
**Partial credit:** 1 point per correct blank

### Supporting Context Artifacts (when helpful)

- Mermaid diagrams (e.g., concept maps, relationships)
- Tables (e.g., term comparisons, definitions)
- Code snippets, analogies, comparisons as context

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

### Terminology & Key Concepts (for graders)

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

### Context & Background (when relevant)

- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Technical Context: [...]
- Key Events & Statistics: [...]

### Assumptions & Preconditions (term context)

- [Explicit assumption about term usage + rationale]

### Validation & Evidence Checks (term verification)

- [Authoritative source confirming term definition/usage]

### Counterexamples & Edge Cases (term boundaries)

- [Related terms that are often confused + distinctions]

### Alternatives Considered (terminology choices)

- [Alternative terms/synonyms, why canonical term was chosen]

### Trade-offs & Decision Guidance (when relevant)

- [Critical trade-off considerations related to the term; decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Perspective-Based Insights (term context)

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

### Market & Macro Systems Analysis (for advanced terms)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (when applicable)

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

### Codebase & Library References (when testing technical terms)

- **[Repository/Library]:** [Stack, modules, maturity, licensing, integration notes, performance/security considerations; authoritative source for the term]

### Authoritative Literature (term sources)

- **[Paper/Report/Book/Standard]:** [Source for the terminology tested; core findings, practical implications]

### Actionable Conclusions (learning objective)

- [Key takeaway or principle the term reinforces; prioritized action]

### Open Questions & Research Agenda (for advanced terms)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations

- **References:** List sources for specialized terminology or definitions.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure terminology is from credible, current sources.
```
