# Prompts

Generate 50 interview Q&A pairs based on the provided job description.

**Stretch tier (senior/expert):** When a deeper bank is required, expand to 56–62 Q&A pairs while preserving the coverage, difficulty, and artifact expectations below.

## Requirements

### Coverage & Organization

**MECE topic coverage**
- Cover all technical areas using a mutually exclusive, collectively exhaustive structure.
- Include technical (techniques, algorithms, patterns, best practices, frameworks, formulas, libraries, hardware requirements and optimizations including energy/resource consumption), theoretical (theories, principles, axioms, laws, assumptions, models), and practical (regulations, market dynamics, risks, costs, use cases) elements.
- Reference authoritative codebases, SDKs, audits, and tooling suites; record language support, licensing, maturity, integration hooks, and performance/security benchmarks, consolidating shared notes in the global Codebase & Tool References section.
- Curate citations with the following language diversity targets (adjust when credible sources are unavailable): ~60% high-quality English references, ~30% high-quality Chinese references, ~10% high-quality references in other relevant languages. Note source language/jurisdiction explicitly and prefer the most authoritative material available in each language.

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
- Integrate authoritative sources (standards, peer-reviewed literature, regulatory reports, vetted references) and explain why each is trusted, capturing shared citations in the global Authoritative Literature & Reports section.
- Highlight collaboration, permission, trust, and governance considerations plus cross-functional alignment tactics influencing execution quality.

### Execution

- Plan before drafting: reflect on approach, outline coverage, and ensure MECE structure.
- Deliver in Markdown with clear headings and code blocks.
- Use clarifying assets (code snippets, tables, analogies, formulas, mermaid diagrams—architecture, class, C4, ERD, block, sequence, state, flowchart, data flow, Gantt, Kanban, user journey, analytical charts). Include complexity class, compute/memory bounds, and energy/resource estimates when relevant.
- Research using current authoritative sources (official docs, codebases, standards) and cross-check multiple references.
- Document consulted codebases/tools and justify their reliability.
- Provide a compact Contents block linking to major sections, including the global reference sections, for quick scanning.
- Cite sources in APA 7th edition and ensure alignment with the output template.
- Apply creative then critical thinking, evaluate from multiple angles (pros, cons, risks, benefits, alternatives, emotional/psychological impact on stakeholders, market sentiment), and verify accuracy, completeness, relevance, and MECE compliance.

## Output Template

```markdown
## Contents
- [Topic Areas](#topic-areas-questions-x-y)
- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)

## Topic Areas (Questions X-Y)

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

## Glossary, Terminology & Acronyms

**[Term/Concept]:** [Clear definition with analogy/formula/example as needed]

## Codebase & Library References

- [Aggregate repositories, SDKs, audits, or tooling suites cited across the bank. Include stack, modules, maturity, licensing, integration hooks, performance/security benchmarks, and language support.]

## Authoritative Literature & Reports

- [Summarize standards, white/yellow papers, peer-reviewed literature, regulatory reports, and vetted references referenced across Q&A clusters, with notes on core findings, credibility, and language/jurisdiction.]

## APA Style Source Citations

- **References:** List all sources cited in the answers, grouped by source language with the targeted distribution (~60% English, ~30% Chinese, ~10% other languages). If credible non-English sources are not available, document the gap and default to high-quality English sources.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language tags (e.g., `[EN]`, `[ZH]`, `[JP]`).
- **Verification:** Ensure each reference is credible, jurisdiction-appropriate, and directly supports the content; highlight regulatory or legal sources when applicable.