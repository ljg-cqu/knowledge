# Prompts

Generate 100 interview Q&A pairs based on the provided job description.

## Requirements

### 1. Coverage & Organization

- **MECE Approach:** Cover all technical areas (Mutually Exclusive, Collectively Exhaustive)
- **Elements:** Technical (techniques, algorithms, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy and resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), practical (regulations, market dynamics, risks, costs, use cases)
- **Misconception Targeting:** For each Q&A, note the misconception, bias, or oversimplified heuristic it is designed to surface and capture the corrective insight that should appear in the output narrative.
- **Context:** Historical evolution, legal/regulatory landscape, future trends; key events and statistical data
- **Perspectives:** Engineering (software, front/back-end, infra), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), management (product, requirements, architecture, system), operations (testing, marketing)
- **Difficulty & Bloom:** Foundational (20%), Intermediate (40%), Advanced (40%), grouped by topic. Target Bloom taxonomy levels: Remember/Understand (foundational), Apply/Analyze (intermediate), Evaluate/Create (advanced)

### 2. Content Design

- **Target:** Senior/expert level with deep technical understanding and broad strategic perspective
- **Evaluation:** Technical (performance, security, scalability, maintainability) and business (cost, efficiency, impact, market fit) dimensions
 - **Evaluation:** Technical (performance, security, scalability, maintainability, algorithmic complexity & error tolerance, energy/resource metrics) and business (cost, efficiency, impact, market fit, operational energy cost)
- **Trade-offs:** Address essential/non-trivial trade-offs with decision-making guidance
- **Questions:** Mix theoretical, practical, and scenario-based on real-world applications
- **Answers:** 150-300 words with technical details, technologies, and practical examples; explain key concepts/terminologies clearly using analogies, formulas, etc. as needed

### 3. Execution

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation
- **Format:** Markdown with proper headings and code blocks
 - **Clarification:** Use code snippets, tables, analogies, formulas, and diverse mermaid diagram types (structural: architecture, class, C4, ERD, block; behavioral: sequence, state, flowchart, data flow; project: Gantt, Kanban, user journey; analytical: charts, graphs, timelines, etc.). Where relevant, include complexity class plus compute/memory and energy/resource estimates (e.g., O(n), memory bounds, J/tx, kW/node).
- **Research:** Latest info from authoritative sources (official docs, codebases, standards); cross-reference multiple sources
- **Citations:** Include APA 7th edition references for all sourced material, aligning with the output template section.
- **Quality:** Ensure essential/valuable Q&A with high-quality output; apply creative then critical thinking; **evaluate from multiple angles (pros, cons, risks, benefits, alternatives, emotional/psychological impact on stakeholders, market sentiment)**; verify accuracy, completeness, relevance, and MECE compliance

## Output Template

```markdown
## [Topic Area] (Questions X-Y)

### QX: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Answer:** [150-300 words with technical details and examples]

[Code/Diagram/Table/Formula/Analogy as needed]

**Misconception Focus:** [Summarize the misconception this Q&A addresses and the corrective guidance to emphasize.]

---

## Terminology & Key Concepts

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

## APA Style Source Citations

- **References:** List all sources cited in the answers.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.