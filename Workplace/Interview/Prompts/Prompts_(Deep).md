# Prompts

Generate 25 interview Q&A pairs based on the provided job description.

**Stretch tier (senior/expert):** When additional depth is needed, expand to 30–32 Q&A pairs while maintaining the coverage, artifact, and difficulty expectations described below.

## Requirements

### Coverage & Organization

**MECE & scope expansion**
- Use a mutually exclusive, collectively exhaustive structure across technical (techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations with energy–resource emphasis), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, permission/consensus governance, upgrade/rollback strategies, risks, costs, use cases) pillars.
- Provide contextual framing: historical evolution, legal/regulatory landscape, future trends, key events, statistical data.
- Catalog authoritative repositories, SDKs, tooling suites, and audits with language support, licensing, maturity, integration hooks, distributed consistency models, and performance/security benchmarks, consolidating shared notes in the global Codebase & Tool References section.

**Analytical artifacts per topic cluster**
- Summarize adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- Surface unresolved problems, emergent risks, knowledge gaps, and prioritized investigation tracks.
- Record explicit assumptions, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions.
- Detail collaboration dynamics, governance models, institutional constraints, change management, and cultural alignment.
- Assess permission level vs decentralization, trust guarantees, privacy/transparency balances, design-pattern choices, system error-tolerance expectations, and reliability/high-availability strategies.

**Perspective & discipline breadth**
- Cover engineering (front-end, back-end, full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- Integrate philosophy (necessity vs contingency, ethics, epistemology), economics, finance and capital markets, psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis when relevant.

**Difficulty profile**
- Maintain Foundational (20%), Intermediate (40%), Advanced (40%) distribution with Bloom targets aligned: Remember/Understand, Apply/Analyze, Evaluate/Create.

### Content Design

- Target senior/expert audiences requiring deep technical, strategic, and macro-level insight.
- Evaluate along technical (throughput/latency, security, scalability, maintainability, reliability/HA) and business (cost, efficiency, impact, market fit) axes.
- Articulate trade-offs including permissioning vs decentralization, trust/privacy balances, algorithmic complexity limits, upgrade path risks with mitigation strategies.
- Explain how permission boundaries, stakeholder trust models, privacy/transparency requirements, error-tolerance envelopes, and distributed consistency guarantees influence architecture.
- Tie answers to macro narratives (economic cycles, market behaviors, liquidity/valuation trends, regulatory shifts, geopolitical/security considerations, societal adoption, organizational behavior, historical precedents, macroeconomic/industry models).
- Outline stakeholder alignment plans, cross-team workflows, communication cadences, business model implications, institutional capabilities, change readiness, and strategic positioning.
- Mix theoretical, practical, and scenario questions anchored in real-world applications.
- Produce 150–300 word answers rich in technical detail; clarify terminology with analogies, formulas, code snippets, tables, and diagrams.
- Explicitly log misconception targets, failure/unhappy paths, mitigation guidance, comparative insights, and decision criteria in the template outputs.

-### Execution

- Plan thoroughly before generation; ensure coverage map, difficulty mix, and artifact checklist are in place.
- During planning, scaffold the Contents, glossary, and global reference sections with explicit `[TBD]` placeholders that will be resolved once related content is drafted and verified.
- Capture citation metadata immediately after finishing each Q&A, maintain a running log (author, year, title, URL, language tag), and consolidate the sources into the global APA section during post-processing.
- Deliver in Markdown with clear headings and code blocks.
- Ensure each topic cluster collectively contains at least one mermaid diagram and one table. Use additional clarifying assets (code snippets, analogies, comparisons, formulas, diverse mermaid diagram types) as needed. For mermaid portability, avoid edge labels and quote node labels containing special characters.
- Research using current authoritative sources (official docs, white/yellow papers, academic theses, market investigations, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); cross-reference multiple sources and capture shared citations in the global Authoritative Literature & Reports section. When a retrieval pipeline pre-collects references, document its scope and fill gaps through targeted per-topic research.
- Curate citations with language diversity targets (adjust when credible sources are unavailable): ~60% high-quality English references, ~30% high-quality Chinese references, ~10% high-quality references in other relevant languages. Note language and jurisdiction for each source and prioritize the most authoritative evidence available per language.
- Cite all sourced material in APA 7th edition and align references with the output template.
- Ensure high-quality output via creative then critical review, leveraging the multi-angle evaluation checklist (pros, cons, risks, benefits, stakeholder emotional/psychological impact, market sentiment, alternatives).
- Ensure holistic reasoning by connecting technical detail, philosophical rigor, macro-level implications, and MECE clarity.
- Provide a comprehensive Contents section at the top that lists every topic/group and nests each question beneath it using the exact titles that appear in the body, alongside links to prefatory material and the global reference sections. Maintain `[TBD]` markers until the corresponding sections are completed, then replace them with final titles. Add optional "Back to top" anchors after each Q&A if desired. Keep the Topic Areas/Q&A section as the final major block so planning, glossary, and reference material lead and deep-dive entries can be appended or resumed cleanly after truncation.

### Finalization Checklist

- Remove all `[TBD]` placeholders and confirm the Contents block mirrors the final heading structure.
- Verify the difficulty distribution and topic coverage align with Requirements targets.
- Confirm every cited source appears in the APA section with correct language tags and matches in-text citations.
- Ensure each topic cluster includes the required diagrams, tables, and supporting artifacts with accurate references.
- Perform a holistic review for accuracy, coherence, MECE compliance, and adherence to formatting expectations.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)
- [Topic Areas](#topic-areas-questions-x-y)
  - [Topic 1: Topic title](#topic-1-topic-title)
    - [Q1: Question text](#q1-question-text)
    - [Q2: Question text](#q2-question-text)
  - [Topic 2: Topic title](#topic-2-topic-title)
    - [Q3: Question text](#q3-question-text)
    - [Q4: Question text](#q4-question-text)

## Executive Summary

- [3–6 bullets on goals, platform choices, performance/security targets, ops posture]

## Coverage & Difficulty Summary

- Difficulty distribution and indices:

| Difficulty | Count | Questions |
|---|---:|---|
| Foundational |  |  |
| Intermediate |  |  |
| Advanced |  |  |

- Topic cluster mapping:

| Topic Cluster | Scope | Questions |
|---|---|---|
| Alliance chain architecture & governance |  |  |
| Smart contracts, security & privacy |  |  |
| Data, integration, ops & economics |  |  |
| Strategy & cross-functional leadership |  |  |

## Glossary, Terminology & Acronyms

- MSP: Membership Service Provider; org identity/policy in Fabric
- CA: Certificate Authority; X.509 issuance and revocation
- DID/VC: Decentralized Identifiers / Verifiable Credentials
- PBFT/Raft: Byzantine vs crash fault tolerant consensus families

## How to Use This in Interviews

- Pick 5–7 questions aligned to candidate background; focus on trade-offs and decision criteria
- Use diagrams/tables as prompts; ask for impact of changing consensus/privacy
- Probe governance and rollback (bridge exploit, oracle outage, DR failover)

## Key Decision Criteria Checklist

- Privacy & compliance, Performance SLOs, Security posture, Interop & liquidity, Ops & HA/DR, Governance & upgrades, Tokenomics & RWA

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Prefer Hyperledger Fabric | Prefer FISCO BCOS (EVM) | Notes/Signals |
|---|---|---|---|
| Privacy & compliance | Channels + PDC, endorsement policies | Group/permissioning | Need bilateral privacy/regulator views → Fabric |
| Interop & liquidity |  | ABI/SDK reuse, L2/public bridge ease | Future cross-chain/token listings → EVM |

## Codebase & Library References

- [Aggregate repositories, SDKs, audits, or tooling suites cited across the deep-dive bank. Include stack, modules, maturity, licensing, integration hooks, performance/security benchmarks, distributed consistency guarantees, reliability/HA posture, and language support.]

## Authoritative Literature & Reports

- [Summarize standards, white/yellow papers, peer-reviewed literature, regulatory reports, and other vetted references referenced across question clusters, with notes on core findings, credibility, and language/jurisdiction.]

## APA Style Source Citations

- **References:** List all sources cited in the answers, grouped by source language with the targeted distribution (~60% English, ~30% Chinese, ~10% other languages). If credible non-English sources are not available, document the gap and default to high-quality English sources.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language tags (e.g., `[EN]`, `[ZH]`, `[JP]`).
- **Verification:** Ensure each reference is credible, jurisdiction-appropriate, and directly supports the content; highlight regulatory or legal sources when applicable.

## Topic Areas (Questions X–Y)

### Topic 1: [Topic title | scope]

#### QX: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced]
**Question Type:** [Theoretical/Practical/Scenario]

##### Answer Narrative (150-300 words)
[Comprehensive response with technical depth and practical illustration]

##### Supporting Artifacts
- At least one Mermaid diagram (e.g., flowchart, architecture)
- At least one table (e.g., comparison, data summary)
- [Additional code snippets, formulas, analogies, comparisons as needed]

**Misconception Focus:** [Summarize the misconception this question targets and the corrective guidance interviewers should reinforce.]

**Failure Path Insight:** [Describe the failure/unhappy path surfaced and the mitigation or contingency actions to highlight.]

##### Comparisons
- [Relevant comparisons to aid understanding, e.g., vs. other technologies, historical vs. current, etc.]

- Technical Techniques, Protocols, Frameworks & Design Patterns: [...]
- Theoretical Principles & Models: [...]
- Practical Regulations, Permission Models & Decentralization, Upgrade Governance, Risks & Use Cases: [...]

##### Technical Evaluation (Performance | Security | Scalability | Maintainability)
- Performance (Throughput & Latency): [...]
- Security: [...]
- Scalability: [...]
- Maintainability: [...]
- Algorithm Complexity & Error Tolerance: [...]
- Reliability & High Availability: [...]
- Distributed Consistency Guarantees: [...]
- Hardware Requirements & Optimizations: [... including energy and resource consumption analysis]

##### Business Evaluation (Cost | Efficiency | Impact | Market Fit)
- Cost: [...]
- Efficiency: [...]
- Impact: [...]
- Market Fit: [...]

##### Multi-Angle Evaluation (Pros | Cons | Risks | Benefits | Stakeholder Impact | Market Sentiment)
- Pros: [...]
- Cons: [...]
- Risks: [... include upgrade/migration failure modes and rollback contingencies]
- Benefits: [...]
- Stakeholder Emotional/Psychological Impact: [...]
- Market Sentiment: [...]
- Trust & Privacy/Transparency Considerations: [...]

##### Collaboration & Communication Plan
- Stakeholders & Roles: [...]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

##### Organizational & Strategic Fit
- Business Model Impact: [...]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

##### Trade-offs & Decision Guidance
- [Critical trade-off analysis and recommended decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

##### Context & Trend Signals
- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Future Trends: [...]
- Key Events & Statistics: [...]

##### Perspective-Based Insights
- Engineering (front-end/back-end/full-stack): [...]
- Architecture & Infrastructure: [...]
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

##### Market & Macro Systems Analysis
- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

##### Inference Summary
- Adoption Signals: [...]
- Interoperability Impacts: [...]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, and rollback triggers]

##### Assumptions & Preconditions

- [Explicit assumption + rationale]

##### Validation & Evidence Checks

- [Data point, benchmark, or experiment backing the answer]

##### Counterexamples & Edge Cases

- [Scenario that challenges the main answer + mitigation]

##### Alternatives Considered

- [Option compared, trade-off summary, selection rationale]

##### Actionable Conclusions & Next Steps
- [Decision, prioritized action, owner/timeline cues]

##### Open Questions & Research Agenda
- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]
