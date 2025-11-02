# Prompts

Generate 100 interview Q&A pairs based on the provided job description.

## Requirements

### Coverage & Organization

**MECE topic coverage**
- Cover all technical areas using a mutually exclusive, collectively exhaustive structure.
- Include technical (techniques, algorithms, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy/resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, risks, costs, use cases) elements.
- Reference authoritative codebases, SDKs, audits, and tooling suites; record language support, licensing, maturity, integration hooks, and performance/security benchmarks.

**Insight coverage per Q&A**
- Document the misconception, bias, or oversimplified heuristic surfaced and write the corrective insight into the narrative.
- Capture failure/unhappy paths (e.g., rollback gaps, degraded service, stakeholder misalignment) plus mitigation guidance.
- Highlight meaningful comparisons or contrasts (technologies, architectures, governance patterns, etc.) and the rationale for option selection.
- Surface stakeholder tensions, conflict drivers, feedback loops, and resolution tactics to probe communication and alignment strategies.
- Summarize adoption signals, interoperability impacts, roadmap considerations, operational risks, and open research tracks that emerge.

**Context & perspective balance**
- Provide historical evolution, legal/regulatory landscape, future trends, key events, and statistical data for each cluster.
- Address perspectives spanning engineering (software, front-end, back-end, infrastructure), architecture & infrastructure (including hardware design, deployment, energy/resource consumption), database & data engineering, quality assurance/testing, product & program management, requirements/business analysis, operations/DevOps, and marketing & go-to-market.

**Difficulty profile**
- Maintain Foundational (20%), Intermediate (40%), Advanced (40%) distribution grouped by topic.
- Align Bloom taxonomy targets: Remember/Understand (foundational), Apply/Analyze (intermediate), Evaluate/Create (advanced).

### Content Design

- Target senior/expert readers with both deep technical understanding and broad strategic perspective.
- Evaluate answers along technical dimensions (performance, security, scalability, maintainability, algorithmic complexity & error tolerance, reliability/HA, energy/resource metrics) and business dimensions (cost, efficiency, impact, market fit, operational energy cost).
- Address essential and non-trivial trade-offs with clear decision-making guidance.
- Mix theoretical, practical, and scenario-based questions grounded in real-world applications.
- Write 150–300 word answers with technical details, concrete technologies, and practical examples; clarify terminology with analogies, formulas, or visuals when helpful.
- Maintain evidence discipline: state assumptions, validation checks, counterexamples, and alternatives to keep reasoning auditable.
- Integrate authoritative sources (standards, peer-reviewed literature, regulatory reports, vetted references) and explain why each is trusted.
- Highlight collaboration, permission, trust, and governance considerations plus cross-functional alignment tactics influencing execution quality.

### Execution

- Plan before drafting: reflect on approach, outline coverage, and ensure MECE structure.
- Deliver in Markdown with clear headings and code blocks.
- Use clarifying assets (code snippets, tables, analogies, formulas, mermaid diagrams—architecture, class, C4, ERD, block, sequence, state, flowchart, data flow, Gantt, Kanban, user journey, analytical charts). Include complexity class, compute/memory bounds, and energy/resource estimates when relevant.
- Research using current authoritative sources (official docs, codebases, standards) and cross-check multiple references.
- Document consulted codebases/tools and justify their reliability.
- Provide a compact Contents block linking to major sections for quick scanning.
- Cite sources in APA 7th edition and ensure alignment with the output template.
- Apply creative then critical thinking, evaluate from multiple angles (pros, cons, risks, benefits, alternatives, emotional/psychological impact on stakeholders, market sentiment), and verify accuracy, completeness, relevance, and MECE compliance.

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