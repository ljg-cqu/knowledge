# Case Study / Scenario-Based Prompt Template

Purpose: Multi-part scenario questions that assess systems thinking, trade-off analysis, and concise recommendations.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Scenario Scope & Distribution

- Generate 16–20 case study scenarios in total. Let distribution across topic clusters follow the MECE coverage plan so each cluster receives proportional attention.
- **Stretch tier (senior/expert):** When extended depth is required, target 20–22 scenarios total while preserving the difficulty mix and proportional cluster coverage.
- Number scenarios sequentially (Scenario 1, Scenario 2, …) and add anchors in the Contents section.
- Maintain Foundational (20%), Intermediate (40%), Advanced (40%) distribution targeting Bloom Analyze/Evaluate. Foundational scenarios emphasize straightforward diagnoses, intermediate scenarios compare alternatives and trade-offs, advanced scenarios synthesize complex interactions and recommendations.

### Scenario Composition & Context

- Draft 200–400 word scenarios with explicit constraints, assumed facts, and self-contained context reflecting real-world complexity (technical debt, resource limits, stakeholder conflict).
- Cover technical (techniques, algorithms, complexity profiles, protocols, patterns, best practices, frameworks, formulas, libraries, hardware requirements/optimizations including energy/resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, permission/consensus governance, upgrade/rollback strategies, risks, costs, use cases) dimensions.
- Structure tasks MECE-style (3–4 prompts) spanning issue identification, solution proposals with trade-offs, remediation plans, stakeholder communication, decision recommendations.
- Provide contextual grounding: historical evolution, legal/regulatory landscape, future trends, key events, statistical data, system interactions. Highlight technical metrics (protocols, patterns, performance, complexity, distributed consistency, reliability/HA) and business metrics (cost, impact, risk, market fit). For RWA scenarios, include tokenization standards, custody requirements, compliance obligations, asset lifecycle details.
- Reference authoritative repositories, SDKs, tooling suites, audits with notes on language support, licensing, maturity, integration hooks, distributed consistency models, and performance/security benchmarks, consolidating shared notes in the global Codebase & Library References section.
- Curate references with language diversity targets (adjust if credible sources are unavailable): ~60% high-quality English references, ~30% high-quality Chinese references, ~10% high-quality references in other relevant languages. Label each source with language/jurisdiction and prioritize the most authoritative material per language.

### Analytical Coverage & Perspectives

- Summarize adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (including upgrade readiness, testing coverage, rollback triggers) per scenario.
- Surface unresolved problems, knowledge gaps, emergent risks, prioritized investigation tracks.
- Capture explicit assumptions, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions.
- Address cross-functional communication, governance models, institutional constraints, change management, cultural alignment, business model implications, institutional capabilities, change readiness, strategic positioning.
- Evaluate permission vs decentralization, trust guarantees, privacy/transparency balances, design-pattern choices, error-tolerance expectations, reliability/high-availability strategies.
- Incorporate perspectives: engineering (front-end, back-end, full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- Integrate philosophical (necessity vs contingency, ethics, epistemology), economic, financial, capital-market, psychological, sociological, anthropological, legal, policy, military strategy, education system, and historical viewpoints where applicable.
- Require evidence: data points, benchmarks, or citations validating recommendations.

### Diagnostic Focus

- Identify the misconception or oversimplified heuristic each scenario reveals and outline corrective guidance for interviewers.
- Highlight failure/unhappy path trajectories (e.g., rollback missteps, degraded performance, stakeholder conflict) and specify mitigation/contingency notes for the template.
- Emphasize comparisons (architectural patterns, governance models, rollout strategies) and codify decision criteria for selecting preferred options.

### Content Design

- Target senior/expert candidates who synthesize information, compare options, and justify recommendations with depth.
- Require deliverables such as issue lists, ≤300-word solution memos, decision matrices, stakeholder communication drafts, remediation timelines.
- Test essential trade-offs: privacy vs transparency, throughput vs consistency, centralization vs decentralization, cost vs resilience, permissioning vs decentralization, trust/privacy balances, algorithmic complexity limits, upgrade path risks with mitigation strategies.
- Evaluate outputs along technical (throughput/latency, security, scalability, maintainability, reliability/HA, algorithm complexity, error tolerance, distributed consistency guarantees) and business (cost, efficiency, impact, market fit) axes.
- Examine how permission boundaries, trust models, privacy/transparency requirements, error-tolerance envelopes, distributed consistency guarantees shape solutions.
- Connect responses to macro narratives (economic cycles, stock/crypto markets, liquidity/valuation trends, regulatory shifts, geopolitical/security factors, societal adoption, organizational behavior, historical precedents, macro/industry models).
- Surface stakeholder alignment plans, cross-team workflows, communication cadences that affect execution quality.
- Articulate business model implications, institutional capabilities, change readiness, long-term strategic positioning.

### Evaluation & Grading

- Provide scoring bands per task (e.g., Task 1: 8 pts, Task 2: 10 pts, Task 3: 6 pts) with clear criteria.
- Offer partial-credit checklists (e.g., correct diagnosis but incomplete solution = 60%) and document expected evidence and common omissions.
- Detail grader notes: key points, acceptable alternatives, edge cases worth bonus credit.

### Execution & Format

- Plan thoroughly before generation; validate coverage, difficulty balance, and artifact checklist.
- Deliver content in Markdown with clear task headings, fenced code blocks, and tables. Store supplemental assets in `assets/` (logs, configs, diagrams) when needed.
- Use decision matrices, mermaid diagrams (sequence, flow, structural), comparison tables, code snippets, analogies, formulas to clarify interactions. For mermaid portability avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- Define terminology with analogies/formulas/examples when useful.
- Integrate historical, regulatory, and technical context plus key events/statistics.
- Base scenarios on real-world applications spanning theoretical, practical, and scenario contexts.
- Include a compact Contents section linking to major sections and every scenario (Scenario 1–Scenario n) with GitHub-compatible anchors.
- Include required prefatory sections: Contents; Executive Summary (2–4 bullets on assessment goals, topic scope, trade-offs tested); Coverage & Difficulty Summary (difficulty table plus topic cluster mapping); Glossary, Terminology & Acronyms; How to Use This in Interviews (evaluation guidance, rubric notes); Key Decision Criteria Checklist (privacy, performance SLOs, security, interop, ops/HA-DR, governance/upgrades, etc.); Key Decision Criteria Matrix (Quick Picks) mapping criteria to preferred approaches when applicable); Codebase & Library References; Authoritative Literature & Reports; APA Style Source Citations.
- Tag each scenario with Difficulty and Bloom level.
- Maintain research rigor: use authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases), avoid outdated references, cross-check information.
- Ensure holistic reasoning that balances technical depth, philosophical rigor, macro insight, and MECE clarity.
- Cite standards, frameworks, regulatory references, and other sources in APA 7th edition, pointing every in-text citation to a single consolidated references section and summarizing sources in the global Authoritative Literature & Reports section.
- Annotate the scenario bibliography by source language (targeting ~60% English, ~30% Chinese, ~10% other languages). Document gaps when credible non-English sources cannot be located.

### Shared Evaluation Checklist (apply to every scenario and response)

- **Technical Evaluation**: performance, security, scalability, maintainability, algorithm complexity, error tolerance, reliability/high availability, distributed consistency guarantees, hardware requirements and energy/resource consumption.
- **Business Evaluation**: cost, efficiency, impact, market fit.
- **Multi-Angle Review**: pros, cons, risks (including upgrade/migration and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust/privacy/transparency considerations.
- **Terminology & Key Concepts**: keep shared definitions in the global Glossary, Terminology & Acronyms section; add scenario-specific clarifications only when unique.
- **Context & Background**: capture historical evolution, regulatory landscape, technical context, market dynamics, key events/statistics relevant to the scenario.
- **Validation & Evidence Checks**: include data points, benchmarks, experiments supporting conclusions.
- **Counterexamples & Edge Cases**: document challenging scenarios and mitigation strategies.
- **Alternatives & Trade-offs**: compare options, record trade-offs, specify decision criteria (permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance).
- **Perspective-Based Insights**: interpret responses across engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: discuss systemic forces, regulatory/policy trajectories, market structure/liquidity, geopolitical/security implications, societal adoption/behavior shifts, competitive ecosystem positioning, macroeconomic/industry models.
- **Inference Summary**: note adoption signals, interoperability impacts, roadmap implications (upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: identify stakeholders, communication cadence/channels, cross-functional alignment tactics.
- **Organizational & Strategic Fit**: analyze business model impact, institutional capabilities/gaps, change management/governance, strategic positioning/differentiation.
- **Codebase & Library References**: list repositories/libraries with stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes.
- **Authoritative Literature**: cite papers, standards, audits, books with core findings, practical implications, credibility signals.
- **Actionable Conclusions & Next Steps**: summarize decisions, prioritized actions, owners/timelines.
- **Open Questions & Research Agenda**: capture remaining challenges, hypotheses, experiments, data/resource needs, timelines/ownership for exploration.
- **APA Style Source Citations**: maintain a consolidated APA 7th edition reference list rather than per-scenario entries; ensure each scenario cites sources back to that section.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Scenarios](#scenarios)
  - [Scenario 1: Title](#scenario-1-title)
  - [Scenario 2: Title](#scenario-2-title)
  - ... (link to each scenario)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)

## Executive Summary

- [2–4 bullets: assessment goals, topic scope, key trade-offs tested]

## Coverage & Difficulty Summary

| Difficulty | Count | Scenarios |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Scenarios |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Scenario 1–x |
| [Cluster B] | [Scope/Boundaries] | Scenario (x+1)–y |

## Glossary, Terminology & Acronyms

- [Key terms and acronyms used across scenarios]

## How to Use This in Interviews

- Allow 45–60 min per scenario; evaluate depth of analysis, trade-off reasoning, and communication clarity
- Use rubrics for consistent grading; award partial credit per task checklist

## Key Decision Criteria Checklist

- [List key criteria relevant to the scenario domain, e.g., privacy & compliance, performance SLOs, security posture, interop & liquidity, ops & HA/DR, governance & upgrades, tokenomics & RWA when applicable]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Approach A | Preferred Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Approach description] | [Approach description] | [Decision guidance] |
| [Criterion 2] | [Approach description] | [Approach description] | [Decision guidance] |

---

## Scenario 1: [Title]

**Language:** python  
**Difficulty:** Intermediate  
**Bloom:** Analyze/Evaluate

### Scenario Context

<200–400 word scenario text with constraints, metrics, stakeholder details>

### Tasks

1. Identify top 3 issues
2. Propose 2 solutions and discuss trade-offs
3. Draft a recommendation memo (≤300 words)

### Expected Key Points

- **Task 1:** [List expected issues and evidence to cite]
- **Task 2:** [List expected solutions, trade-offs, and decision criteria]
- **Task 3:** [List key elements of a strong memo: clarity, justification, stakeholder framing]

### Grading Rubric

| Task | Max Points | Criteria |
|---|---:|---|
| Task 1 | 8 | Correctness, completeness, evidence |
| Task 2 | 10 | Feasibility, trade-off depth, alternatives |
| Task 3 | 6 | Clarity, structure, decision justification |

### Grader Notes

- Partial credit: Correct diagnosis + incomplete solution = 60%
- Bonus: Novel insights, consideration of edge cases, stakeholder impact analysis
- Common omissions: [List typical gaps]

### Misconception Focus

- [Describe the misconception this scenario reveals and the guidance for steering candidates toward the accurate model.]

### Failure Path Insight

- [Summarize the failure or unhappy path the scenario is designed to surface and the mitigation/contingency expectations.]

### Comparison Notes

- [Document the key comparison/contrast insights and decision criteria highlighted by this scenario.]

### Supporting Artifacts (for scenario context clarity)

- Mermaid diagrams (e.g., architecture, sequence, flowchart)
- Tables (e.g., comparison, data summary, decision matrix)
- Code snippets, analogies, comparisons, formulas as needed

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

### Context & Background (scenario grounding)

- Historical Evolution: [...]
- Regulatory Landscape: [...]
- Technical Context: [...]
- Market Dynamics: [...]
- Key Events & Statistics: [...]

### Perspective-Based Insights (evaluate candidate responses from these angles)

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

### Market & Macro Systems Analysis (for advanced scenarios)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (scenario implications)

- Adoption Signals: [...]
- Interoperability Impacts: [...]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, rollback triggers]

### Collaboration & Communication Plan (expected in candidate responses)

- Stakeholders & Roles: [...]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

### Organizational & Strategic Fit (expected in candidate responses)

- Business Model Impact: [...]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

### Assumptions & Preconditions (scenario setup)

- [Explicit assumption + rationale]

### Validation & Evidence Checks (expected in candidate responses)

- [Data point, benchmark, or experiment backing the solution]

### Counterexamples & Edge Cases (expected in candidate responses)

- [Scenario that challenges the main solution + mitigation]

### Alternatives Considered (expected in candidate responses)

- [Option compared, trade-off summary, selection rationale]

### Trade-offs & Decision Guidance (expected in candidate responses)

- [Critical trade-off analysis and recommended decision criteria with explicit permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, and upgrade/rollback guidance]

### Actionable Conclusions & Next Steps (expected in candidate recommendations)

- [Decision, prioritized action, owner/timeline cues]

### Open Questions & Research Agenda (for advanced scenarios)

- Remaining Challenges: [...]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

## APA Style Source Citations

- **References:** List all sources cited across scenarios, grouped by language when relevant.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language/jurisdiction tags.
- **Verification:** Ensure each reference is credible, current, and directly supports the content; cross-check scenario tags against this list.
```
