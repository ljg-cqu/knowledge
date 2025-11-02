# Cloze / Fill-in-the-Blank Prompt Template

Purpose: Short fill-in-the-blank items to test precise recall (definitions, terms, short phrases, equations).

## Contents

- [Requirements](#requirements)
  - [Item Scope & Distribution](#item-scope--distribution)
  - [Term Selection & Context](#term-selection--context)
  - [Analytical Coverage & Perspectives](#analytical-coverage--perspectives)
  - [Diagnostic Focus](#diagnostic-focus)
  - [Content Design](#content-design)
  - [Evaluation & Grading](#evaluation--grading)
  - [Execution & Format](#execution--format)
- [Output Template](#output-template)

## Requirements

### Item Scope & Distribution

- Generate 24–32 cloze items in total. Allocate items across topic clusters based on the MECE coverage plan so each cluster receives proportional emphasis.
- **Stretch tier (senior/expert):** For extended mastery checks, target 32–36 items total while maintaining the same difficulty mix and proportional cluster coverage.
- Number items sequentially (Item 1, Item 2, …) with matching anchors in the Contents block.
- Maintain Foundational (20%), Intermediate (40%), Advanced (40%) distribution targeting Bloom Remember/Understand. Foundational items focus on direct recall, intermediate items test conceptual relationships, advanced items probe nuanced distinctions, multi-blank context, or scenario-dependent terminology.

### Term Selection & Context

- Apply MECE principles when selecting terms/phrases across technical (techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements and energy/resource optimization), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, key terms, acronyms, market dynamics, permission/consensus governance, risks, costs, use cases) pillars.
- Keep each blank narrowly scoped and unambiguous; avoid overlapping blanks and ambiguous phrasing.
- Provide surrounding context that clarifies the blank and incorporates historical evolution, legal/regulatory landscape, future trends, key events, statistical data, and relevant narratives.
- Include authoritative codebases, SDKs, tooling suites when terminology relates to specific implementations, noting language support, licensing, maturity, integration hooks.
- Use authoritative literature (white/yellow papers, peer-reviewed studies, standards, books/manuals, vetted encyclopedias) to anchor definitions.
- Curate references with language diversity targets (adjust if credible sources are unavailable): ~60% high-quality English references, ~30% high-quality Chinese references, ~10% high-quality references in other relevant languages. Label each source with language/jurisdiction and prefer the most authoritative material per language.

### Analytical Coverage & Perspectives

- Document authoritative validation for each term, including sources confirming definitions and usage.
- Capture counterexamples/edge cases: near-miss terms, commonly confused phrases, failure/unhappy path interpretations plus corrective guidance.
- Record explicit assumptions, validation checks, alternatives considered (synonyms/related terms), and actionable conclusions in grader notes where relevant.
- Address terminology connected to stakeholder tension, communication friction, or feedback loops to support alignment discussions.
- Incorporate governance and trust dimensions (permission vs decentralization, trust guarantees, privacy/transparency balances, design-pattern choices, error-tolerance expectations, reliability/high-availability strategies).
- Provide coverage across engineering disciplines (front-end, back-end, full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- Integrate philosophical, economic, financial, capital-market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical perspectives when terminology intersects those domains.
- Include terms signaling adoption, interoperability, roadmap implications (including upgrade sequencing), operational risks (including upgrade readiness, testing coverage, rollback triggers), unresolved questions, and emerging risks.

### Diagnostic Focus

- Explicitly state the misconception, near-miss, or bias each blank targets and outline corrective notes for interviewer guidance.
- Highlight decision criteria when comparing close alternatives or competing methodologies.
- Capture stakeholder conflict or feedback cues relevant to the terminology.

### Content Design

- Target senior/expert audiences expected to demonstrate precise recall and nuanced understanding.
- Provide canonical answer arrays listing accepted synonyms and alternate spellings (e.g., ["decentralization", "decentralisation"]).
- Define normalization rules: case-insensitive matching, whitespace trimming, punctuation stripping; specify rounding/formatting conventions for numeric responses.
- Note per-blank scoring (e.g., 1 point each) and tolerance ranges for numeric values.

### Evaluation & Grading

- Supply acceptance lists with common variations and synonyms for every blank.
- Specify numeric tolerances (±% or ±absolute) where applicable.
- Document grader notes on borderline answers, near misses, and partial-credit guidance.
- Explain distractor notes describing why common incorrect answers fail, supporting feedback systems.

### Execution & Format

- Plan thoroughly before authoring to ensure MECE coverage and difficulty balance.
- Present content in Markdown with clear headings; indicate blanks using underscores (___) or bracketed placeholders ([blank]).
- Provide ALT text for any inline images or diagrams.
- Use clarifying aids—mermaid diagrams, tables, code snippets, analogies—while ensuring mermaid portability (no edge labels, quote node labels containing special characters like parentheses or slashes).
- Use precise technical language and explain key terminology as needed.
- Integrate real-world contexts so items reflect practical applications.
- Provide a comprehensive Contents section at the top that lists every topic/group and nests each item beneath it using the exact titles that appear in the body, alongside links to the prefatory and global reference sections.
- Provide required prefatory sections: Contents; Executive Summary (2–3 bullets on assessment goals, term coverage, scoring approach); Coverage & Difficulty Summary (difficulty table plus topic cluster mapping); Glossary, Terminology & Acronyms; How to Use This in Interviews (auto-grading guidance, normalization rules); Key Decision Criteria Checklist (terminology domain considerations); Key Decision Criteria Matrix (Quick Picks for term usage patterns when applicable); Codebase & Library References; Authoritative Literature & Reports; APA Style Source Citations.
- Tag each item with Difficulty and Bloom level.
- Base content on current authoritative sources; cross-reference to ensure quality, accuracy, completeness, relevance, and MECE compliance.
- Maintain holistic reasoning so terminology remains aligned with cross-disciplinary relevance.
- Cite definitions using APA 7th edition formatting via a single consolidated references section.
- Annotate the reference list by source language (target ~60% English, ~30% Chinese, ~10% other languages). Document gaps when credible non-English sources are unavailable and rely on strong English references as needed.

### Shared Evaluation Checklist (apply to every item)

- **Technical Evaluation**: performance, security, scalability, maintainability, algorithm complexity & error tolerance, reliability/high availability, distributed consistency guarantees, hardware requirements & energy/resource consumption when pertinent to the term.
- **Business Evaluation**: cost, efficiency, impact, market fit implications of the terminology.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: keep shared definitions in the global Glossary, Terminology & Acronyms section; add item-specific clarifications only when unique.
- **Context & Background**: capture historical evolution, regulatory landscape, technical context, market dynamics, key events/statistics tied to the term.
- **Validation & Evidence Checks**: reference authoritative sources validating definitions/usage.
- **Counterexamples & Edge Cases**: log confusing alternatives, clarify distinctions, and note mitigation guidance.
- **Alternatives & Trade-offs**: document competing terms/synonyms, articulate selection criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: assess term relevance across engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: consider systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models.
- **Inference Summary**: note adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness/testing coverage/rollback triggers).
- **Collaboration & Communication Plan**: highlight stakeholders, communication cadence/channels, alignment tactics relevant to terminology usage.
- **Organizational & Strategic Fit**: describe business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation linked to the term.
- **Codebase & Library References**: cite repositories/libraries when terms arise from specific tools in the global Codebase & Library References section, including stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes.
- **Authoritative Literature**: list standards, papers, documentation supporting usage with core findings and implications in the global Authoritative Literature & Reports section.
- **Actionable Conclusions**: summarize key takeaways, prioritized actions, or principles enforced by the term.
- **Open Questions & Research Agenda**: capture remaining challenges, hypotheses, experiments, data/resource needs, timelines/ownership for deeper exploration.
- **APA Style Source Citations**: maintain a consolidated APA 7th edition reference list rather than per-item entries; ensure each item cites sources back to that section.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Item Bank](#item-bank-items-1-15)
  - [Topic 1: Topic title](#topic-1-topic-title)
    - [Item 1: Topic](#item-1-topic)
    - [Item 2: Topic](#item-2-topic)
  - [Topic 2: Topic title](#topic-2-topic-title)
    - [Item 3: Topic](#item-3-topic)
    - [Item 4: Topic](#item-4-topic)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)

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

## Glossary, Terminology & Acronyms

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

## Codebase & Library References

- [Aggregate repositories, SDKs, audits, or tooling suites referenced across the cloze bank. Include stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, and permission/governance notes.]

## Authoritative Literature & Reports

- [List standards, documentation, audits, white/yellow papers, books/manuals, and peer-reviewed research supporting terminology usage across items. Summarize core findings, practical implications, and language/jurisdiction tags.]

## Item Bank (Items 1–15)

### Topic 1: [Topic title | scope]

#### Item 1: Topic

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

**Misconception Focus:** [Highlight the confusion this item is designed to surface and the clarification to reinforce.]

**Failure Path Insight:** [Describe the failure scenario or incorrect application this item is meant to surface and the mitigation guidance.]

**Comparison Notes:** [Capture the key comparison/contrast insight (e.g., term vs. synonym/alternative) and the selection criteria to emphasize.]

**Conflict/Feedback Notes:** [Summarize conflict triggers, stakeholder feedback cues, and recommended alignment tactics tied to this terminology.]

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

### Actionable Conclusions (learning objective)

- [Key takeaway or principle the term reinforces; prioritized action]

### Open Questions & Research Agenda (for advanced terms)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

## APA Style Source Citations

- **References:** List sources for specialized terminology or definitions across items.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and annotate language/jurisdiction tags.
- **Verification:** Ensure each reference is credible, current, and directly supports the content; document gaps when non-English sources are unavailable.
```
