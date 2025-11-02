# True / False (T/F) Prompt Template

Purpose: Short, unambiguous declarative statements for binary judgment (True/False). Include a brief rationale when full credit requires it.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Statement Scope & Distribution

- Generate 18–24 statements in total. Distribute statements across topic clusters according to the MECE coverage plan so each cluster receives proportional emphasis.
- **Stretch tier (senior/expert):** For extended coverage, target 24–28 statements total while keeping the difficulty mix and proportional cluster coverage intact.
- Number statements sequentially (S1, S2, …) with anchors in the Contents block.
- Maintain Foundational (40%), Intermediate (40%), Advanced (20%) distribution aligned to Bloom Remember/Understand/Apply: foundational items test factual recall, intermediate items probe relational understanding, advanced items apply concepts to judge scenario-based claims.

### Statement Composition & Context

- Write concise, unambiguous declarative statements (≤2 lines) that avoid double negatives and vague qualifiers.
- Apply MECE principles to prevent overlap or contradiction within the bank; cover technical, theoretical, and practical facets: techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations (including energy/resource consumption); theories, principles, axioms, laws, assumptions, models; regulations, market dynamics, permission/consensus governance, upgrade/rollback strategies, risks, costs, use cases.
- Provide rationales including historical context, regulatory/legal landscape, technical background, statistical data as needed.
- Base statements on authoritative repositories, SDKs, documentation, standards, white/yellow papers, peer-reviewed studies, books/manuals, vetted encyclopedias, documenting shared tooling in the global Codebase & Library References section and shared citations in the global Authoritative Literature & Reports section.
- Curate references with language diversity targets (adjust if credible sources are unavailable): ~60% high-quality English sources, ~30% high-quality Chinese sources, ~10% high-quality sources in other relevant languages. Label each source with language/jurisdiction and prioritize the most authoritative material per language.
- Integrate governance/trust dimensions (permission vs decentralization, trust guarantees, privacy/transparency balances, design-pattern choices, error tolerance, reliability/high availability) and highlight failure/unhappy path scenarios with mitigation guidance.
- Frame comparisons (consensus models, governance patterns, architecture options) and document criteria for preferring alternatives.
- Cover perspectives across engineering disciplines, architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- Incorporate philosophical, economic, financial, capital-market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical viewpoints when relevant.
- Address collaboration/organizational dynamics (cross-functional communication, governance models, institutional constraints, change management, cultural alignment) and organizational/strategic operations (business model implications, institutional capabilities, change readiness, strategic positioning).
- Surface adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers), unresolved questions, knowledge gaps, and emergent risks for advanced statements.

### Diagnostic Focus

- Target specific misconceptions or outdated heuristics; note corrective insights for interviewer guidance.
- Provide rationales (1–2 sentences) explaining truth value and a concise note per distractor misconception when feedback is needed.
- Allow optional written justification (2–3 sentences) for higher-credit items; specify grading split (e.g., answer 70% + rationale 30%).
- Evaluate along technical (performance, security, scalability, algorithm complexity, error tolerance, distributed consistency) and business (cost, efficiency, impact, market fit) dimensions; capture trade-offs in advanced items (e.g., BFT vs CFT throughput).
- Assess governance/assurance implications (permission boundaries, trust models, privacy/transparency requirements, reliability expectations).

### Evaluation & Grading

- Machine-grade by exact match to answer (A/True or B/False); normalize accepted inputs (“A”, “True”, “true”, “T”).
- When justification is required, award partial credit for correct letter with weak rationale or incorrect letter with insightful reasoning.
- Ensure every statement is defensible with authoritative sources; avoid subjective claims.

### Execution & Format

- Plan coverage and difficulty mix before writing.
- Structure content in Markdown with clear headings; present statements with labeled options (A. True, B. False), answer, and rationale. Use fenced code blocks when referencing code behavior.
- Employ clarity aids (mermaid diagrams, tables, analogies) as needed; maintain mermaid portability (no edge labels; quote node labels containing special characters such as parentheses/slashes).
- Explain terminology within rationales when necessary.
- Ground statements in real-world facts and scenarios.
- Include a compact Contents section linking to major headings, including the global reference sections, and all statements (S1–Sn) using GitHub-compatible anchors.
- Include required prefatory sections: Contents; Executive Summary (2–3 bullets on goals, scope, grading approach); Coverage & Difficulty Summary (difficulty table + topic cluster mapping); Glossary, Terminology & Acronyms; How to Use This in Interviews (grading guidance, optional justification instructions); Key Decision Criteria Checklist (domain-specific considerations); Key Decision Criteria Matrix (Quick Picks) mapping claim evaluation criteria when applicable); Codebase & Library References; Authoritative Literature & Reports; APA Style Source Citations.
- Tag each statement with Difficulty and Bloom level.
- Base content on up-to-date authoritative sources; cross-reference for accuracy, completeness, relevance, MECE compliance.
- Maintain holistic reasoning across disciplines; cite external standards, protocol specs, regulatory requirements using APA 7th edition.
- Annotate the bibliography by source language (targeting ~60% English, ~30% Chinese, ~10% other languages). Document gaps when credible non-English sources are unavailable and default to high-quality English references.

### Shared Evaluation Checklist (apply to every statement)

- **Technical Evaluation**: performance, security, scalability, maintainability, algorithm complexity & error tolerance, distributed consistency guarantees, hardware requirements & energy/resource consumption.
- **Business Evaluation**: cost, efficiency, impact, market fit.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: keep shared definitions in the global Glossary, Terminology & Acronyms section; add statement-specific clarifications only when unique.
- **Context & Background**: outline historical evolution, regulatory landscape, technical context, market dynamics, key events/statistics relevant to the claim.
- **Validation & Evidence Checks**: document data points, benchmarks, or sources verifying truth value.
- **Counterexamples & Edge Cases**: note scenarios requiring clarification and mitigation guidance.
- **Alternatives & Trade-offs**: compare related claims, articulate trade-offs, provide decision criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: examine implications across engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: consider systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models.
- **Inference Summary**: record adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: identify stakeholders, communication cadence/channels, alignment tactics relating to the claim.
- **Organizational & Strategic Fit**: evaluate business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation.
- **Codebase & Library References**: cite frameworks/tools referenced (stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes) in the global Codebase & Library References section.
- **Authoritative Literature**: reference standards, documentation, audits, or papers supporting the statement via the global Authoritative Literature & Reports section.
- **Actionable Conclusions**: highlight key takeaways or decision principles reinforced by the claim.
- **Open Questions & Research Agenda**: capture unresolved issues, hypotheses, required data/experiments, timelines/ownership.
- **APA Style Source Citations**: ensure all references follow APA 7th edition and directly support the content.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Statements 1–20](#statements-120)
  - [S1: Statement topic](#s1-statement-topic)
  - [S2: Statement topic](#s2-statement-topic)
  - ... (link to each statement)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)

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

## Glossary, Terminology & Acronyms

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

**Misconception Focus:** [State the misconception this statement targets and the corrective insight to emphasize during review.]

**Failure Path Insight:** [Describe the failure or unhappy path this statement is designed to probe and the mitigation guidance to reinforce.]

**Comparison Notes:** [Capture the key comparison/contrast insight this statement evaluates and the decision criteria for differentiating options.]

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

### APA Style Source Citations

- **References:** List sources for factual claims from external standards, protocol specifications, regulatory requirements, or published research.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.

## Codebase & Library References

- [Aggregate frameworks, tools, SDKs, audits, or repositories cited across the T/F bank. Include stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, and permission/governance notes.]

## Authoritative Literature & Reports

- [List standards, documentation, audits, white/yellow papers, books/manuals, and peer-reviewed studies underpinning statements. Summarize core findings, practical implications, credibility signals, and language/jurisdiction tags.]
