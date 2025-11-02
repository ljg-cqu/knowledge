# Prompts

Generate 100 interview Q&A pairs based on the provided job description.

## Requirements

### 1. Coverage & Organization

- **MECE Approach:** Cover all technical areas (Mutually Exclusive, Collectively Exhaustive)
- **Elements:** Technical (techniques, algorithms, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), practical (regulations, market dynamics, risks, costs, use cases)
- **Codebases & Tooling:** Reference authoritative repositories, SDKs, audits, and tooling suites with quick notes on language support, licensing, maturity, integration hooks, and performance/security benchmarks.
- **Misconception Targeting:** For each Q&A, note the misconception, bias, or oversimplified heuristic it is designed to surface and capture the corrective insight that should appear in the output narrative.
- **Failure Path Coverage:** Capture the key failure/unhappy path scenario (e.g., rollback gaps, degraded service, stakeholder misalignment) and the mitigation guidance that must appear in the output narrative.
- **Comparison Coverage:** Ensure each Q&A highlights meaningful comparisons or contrasts (technologies, architectures, governance patterns, etc.) where relevant, capturing the rationale for preferring one option over another in the output narrative.
- **Conflict & Feedback Coverage:** Surface stakeholder tensions, conflict drivers, feedback loops, and resolution tactics so interviewers can probe communication and alignment strategies.
- **Signals & Risks:** Summarize adoption signals, interoperability impacts, roadmap implications, and operational risks for each topic cluster.
- **Open Research:** Flag unresolved issues, knowledge gaps, or prioritized investigation tracks that emerge.
- **Context:** Historical evolution, legal/regulatory landscape, future trends; key events and statistical data
- **Perspectives:** Engineering (software, front/back-end, infra), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product & program management, requirements/business analysis, operations/DevOps, marketing & go-to-market
- **Difficulty & Bloom:** Foundational (20%), Intermediate (40%), Advanced (40%), grouped by topic. Target Bloom taxonomy levels: Remember/Understand (foundational), Apply/Analyze (intermediate), Evaluate/Create (advanced)

### 2. Content Design

- **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Evaluation:** Technical (performance, security, scalability, maintainability, algorithmic complexity & error tolerance, reliability/HA, energy/resource metrics) and business (cost, efficiency, impact, market fit, operational energy cost)
- **Trade-offs:** Address essential/non-trivial trade-offs with decision-making guidance
- **Questions:** Mix theoretical, practical, and scenario-based on real-world applications
- **Answers:** 150-300 words with technical details, technologies, and practical examples; explain key concepts/terminologies clearly using analogies, formulas, etc. as needed
- **Evidence Discipline:** State explicit assumptions, validation checks, counterexamples, and alternatives to keep reasoning auditable.
- **Authoritative Sources:** Integrate takeaways from standards, peer-reviewed literature, regulatory reports, and other vetted references that directly support the guidance.
- **Collaboration & Governance:** Highlight permission/trust considerations and cross-functional alignment tactics that influence execution quality.

### 3. Execution

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation
- **Format:** Markdown with proper headings and code blocks
- **Clarification:** Use code snippets, tables, analogies, formulas, and diverse mermaid diagram types (structural: architecture, class, C4, ERD, block; behavioral: sequence, state, flowchart, data flow; project: Gantt, Kanban, user journey; analytical: charts, graphs, timelines, etc.). Where relevant, include complexity class plus compute/memory and energy/resource estimates (e.g., O(n), memory bounds, J/tx, kW/node).
- **Research:** Latest info from authoritative sources (official docs, codebases, standards); cross-reference multiple sources
- **Documentation:** Call out the specific codebases/tools consulted and note why each is trusted.
- **Navigation:** Begin with a compact contents block linking to the major sections of the output for quick scanning.
- **Citations:** Include APA 7th edition references for all sourced material, aligning with the output template section.
- **Quality:** Ensure essential/valuable Q&A with high-quality output; apply creative then critical thinking; **evaluate from multiple angles (pros, cons, risks, benefits, alternatives, emotional/psychological impact on stakeholders, market sentiment)**; verify accuracy, completeness, relevance, and MECE compliance

## Output Template

```markdown
## Contents
- [Topic Areas](#topic-area-questions-x-y)
- [Terminology & Key Concepts](#terminology--key-concepts)
- [APA Style Source Citations](#apa-style-source-citations)

## [Topic Area] (Questions X-Y)

### QX: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Answer:** [150-300 words with technical details and examples]

[Code/Diagram/Table/Formula/Analogy as needed]

**Misconception Focus:** [Summarize the misconception this Q&A addresses and the corrective guidance to emphasize.]

**Failure Path Insight:** [Describe the failure/unhappy path surfaced and the mitigation or contingency guidance to highlight.]

**Comparison Notes:** [Capture the key comparison/contrast insights and decision criteria that arose in the answer.]

**Conflict/Feedback Notes:** [Summarize stakeholder tensions, feedback signals, and alignment tactics highlighted in the answer.]

**Code & Tool References:** [List key repositories, SDKs, audits, or tooling suites with relevance notes.]

**Evidence Checklist:**
- Assumptions: [...]
- Validation: [...]
- Counterexample & Mitigation: [...]
- Alternative Considered: [...]

**Signals & Open Questions:** [Capture adoption signals, interoperability impacts, roadmap implications, operational risks, and research priorities.]

**Cross-Functional & Governance Notes:** [Highlight permission/trust considerations, alignment tactics, and organizational dynamics.]

---

## Terminology & Key Concepts

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

## APA Style Source Citations

- **References:** List all sources cited in the answers.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.