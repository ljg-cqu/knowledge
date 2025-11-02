# Debugging / Code-Reading Prompt Template

Purpose: Provide a short buggy code snippet plus failing output; ask students to fix the bug, explain the root cause, and supply minimal passing tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### Task Scope & Distribution

- Generate 15–20 debugging tasks in total. Allocate tasks across topic clusters following the MECE coverage plan so each cluster is represented proportionally.
- **Stretch tier (senior/expert):** When deeper coverage is required, target 20–22 tasks total while retaining the same difficulty mix and proportional cluster coverage.
- Number tasks sequentially (Task 1, Task 2, …) and include anchors in the Contents block.
- Maintain Foundational (20%), Intermediate (40%), Advanced (40%) difficulty mix aligned to Bloom Analyze/Evaluate expectations. Foundational items expose obvious bugs with clear errors, intermediate items require logic/API tracing across multiple components, advanced items highlight subtle concurrency, security, or governance failures demanding holistic remediation.

### Bug Composition & Context

- Provide a single focused bug in 10–50 lines; avoid multi-bug scenarios unless explicitly testing triage.
- Address technical, theoretical, and practical facets: algorithms and complexity issues, protocols, patterns, best practices, frameworks, libraries, hardware/resource concerns; principles/models; edge-case handling, security flaws, permission/consensus governance issues, operational use cases.
- Rotate through bug categories (off-by-one, type mismatch, incorrect API usage, concurrency, edge-case handling, logic, security, performance, governance/permission violations).
- Supply enough surrounding context (imports, data structures, calls) to reproduce the failure and include historical/API/best-practice notes when they illuminate pitfalls.
- Reference authoritative repositories, SDKs, documentation, and audits when framework-specific behavior matters; document them once in the global Codebase & Library References section. Cite anti-patterns from white/yellow papers, security audits, standards, or official docs, and capture them in the global Authoritative Literature & Reports section.
- Curate references with language diversity targets (adjust if credible sources are unavailable): ~60% high-quality English references, ~30% high-quality Chinese references, ~10% high-quality references in other relevant languages. Label each source with language/jurisdiction and prioritize the most authoritative material per language.

### Analytical Coverage & Artifacts

- Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions in solutions and grader notes.
- Provide failing tests that demonstrate the bug and passing tests that validate the fix.
- Highlight scenarios where naïve fixes fail or alternative approaches introduce trade-offs, emphasizing failure/unhappy paths and recovery expectations.
- Examine permission boundaries, trust model violations, privacy leaks, design-pattern mismatches, error-tolerance breakdowns, and reliability/high-availability impacts.
- Discuss perspectives from engineering (front-end/back-end/full-stack), architecture & infrastructure (hardware design, deployment, energy/resource consumption), database & data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations & DevOps, and marketing/go-to-market.
- For advanced prompts, extend coverage to philosophy (necessity vs contingency, ethics, epistemology), economics, finance and capital markets, psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis.
- Address cross-functional communication, governance models, institutional constraints, change management, cultural alignment, business model impact, institutional capability gaps, change readiness, strategic positioning, adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (including upgrade readiness, testing coverage, rollback triggers), and open research agendas surfaced by the bug.

### Diagnostic Focus

- Document the misconception or faulty heuristic each task exposes and articulate the corrective framing for interviewers.
- Describe the failure/unhappy path the bug reveals with mitigation or regression-testing guidance.
- Capture contrast between competing fixes or diagnostic strategies, with criteria such as performance versus maintainability guiding the preferred approach.

### Content Design

- Target senior/expert practitioners demonstrating Analyze/Evaluate proficiency.
- Require three deliverables per task: minimal-change corrected code (comment when useful), a 2–4 sentence root-cause explanation naming the violated principle/pattern, and minimal passing tests that formerly failed.
- Provide realistic failing output (stderr, assertion traces, unexpected behavior) to direct debugging effort.
- Evaluate responses for technical correctness, security, performance impact, maintainability, and practical alignment with API contracts, patterns, and error-tolerance expectations.
- Discuss trade-offs between simple and robust fixes, performance versus clarity, or alternative remediation strategies, including governance or assurance considerations (permission boundaries, trust integrity, privacy/transparency requirements).

### Evaluation & Grading

- Use a rubric such as Fix correctness (0–6 pts), Explanation depth (0–3 pts), Tests provided (0–1 pt); adjust per difficulty.
- Grant partial credit for correct diagnosis with incomplete fix or a correct fix with thin explanation.
- Document common incorrect approaches, valid alternative fixes, and edge cases that merit bonus credit.
- Reinforce the targeted misconception, failure path expectations, and comparison notes within grader guidance.

-### Execution & Format

- Plan deliberately before writing; map coverage, difficulty mix, and artifact requirements.
- During planning, scaffold Contents, prefatory sections, and global reference blocks with `[TBD]` placeholders; replace each placeholder once the associated debugging task, fix, and validation artifacts are finalized.
- Capture citation metadata immediately after writing each task (author, year, title, URL/DOI, language tag) and consolidate entries into the global Authoritative Literature & Reports and APA sections during post-processing.
- Present content in Markdown with clear headings and fenced code blocks for buggy code, failing output, corrected code, and tests. Include run instructions.
- Ensure each topic cluster collectively employs clarifying aids—mermaid diagrams (structural, behavioral, analytical), tables, analogies, comparisons—while maintaining portability (avoid mermaid edge labels and quote node labels containing special characters such as parentheses or slashes).
- Explain terminology and error patterns in context; integrate API documentation and best-practice commentary.
- Ground scenarios in real-world debugging incidents.
- Base content on current authoritative sources (official docs, white/yellow papers, academic theses, audits, standards, curated wikis/encyclopedias, codebases); cross-reference to ensure accuracy, completeness, relevance, and MECE compliance. When a retrieval pipeline pre-collects resources, document its scope and supplement with per-task research to cover gaps.
- Provide a comprehensive Contents section at the top that lists every topic/group and nests each task beneath it using the exact titles that appear in the body, alongside links to the prefatory and global reference sections. Maintain `[TBD]` labels until headings and anchors are final.
- Include required prefatory sections: Contents, Executive Summary (assessment goals, bug coverage, evaluation approach), Coverage & Difficulty Summary (difficulty table plus topic cluster mapping), Glossary, Terminology & Acronyms (key APIs/patterns), How to Use This in Interviews (rubric, partial credit, fix verification), Key Decision Criteria Checklist (fix approach/security/performance/etc.), Key Decision Criteria Matrix (Quick Picks mapping approaches to criteria when applicable), Codebase & Library References, Authoritative Literature & Reports, and APA Style Source Citations. Keep the Task Bank as the final major section so the plan-first scaffold stays visible and additional debugging tasks can be appended or resumed cleanly after truncation.
- Tag each task with Difficulty, Bloom level, and language.
- Apply holistic reasoning so bugs teach broader debugging principles; cite references using APA 7th edition through a single consolidated references section.
- Annotate the bibliography by source language (targeting ~60% English, ~30% Chinese, ~10% other languages) and document gaps when non-English sources are unavailable.

### Finalization Checklist

- Remove all `[TBD]` placeholders and confirm Contents anchors match the finalized headings.
- Verify task counts, difficulty mix, and topic distribution align with Requirements targets.
- Ensure each topic cluster provides the required supporting artifacts (diagrams, tables, comparisons) and that buggy code, corrected code, explanations, and tests are complete and consistent.
- Confirm every in-text citation maps to the consolidated APA section with correct language tags and that the Authoritative Literature & Reports summary reflects the final source set.
- Execute the provided tests against the corrected code to validate fixes, then perform a holistic QA for accuracy, coherence, formatting, and MECE compliance before delivery.

### Shared Evaluation Checklist (applies to every task)

- **Technical Evaluation**: performance (throughput/latency implications), security considerations, scalability, maintainability, algorithm complexity & error tolerance, reliability/high availability, distributed consistency guarantees, hardware requirements & optimizations (including energy/resource analysis).
- **Business Evaluation**: cost impact, efficiency, broader impact, market fit.
- **Multi-Angle Evaluation**: pros, cons, risks (including upgrade/migration failure modes and rollback contingencies), benefits, stakeholder emotional/psychological impact, market sentiment, trust and privacy/transparency considerations.
- **Terminology & Key Concepts**: keep definitions in the global Glossary, Terminology & Acronyms section; add task-specific clarifications only when unique.
- **Context & Background**: outline historical evolution, regulatory landscape, technical context, market dynamics, key events/statistics when relevant.
- **Validation & Evidence Checks**: supply data points, benchmarks, or tests that verify bug reproduction and fix correctness.
- **Counterexamples & Edge Cases**: document scenarios challenging the main fix plus mitigation guidance.
- **Alternatives & Trade-offs**: compare alternative fixes, discuss trade-offs, and provide decision criteria covering permission/decentralization, trust/privacy, algorithm complexity, design-pattern alignment, upgrade/rollback guidance.
- **Perspective-Based Insights**: evaluate responses through engineering, architecture/infrastructure, database/data engineering, QA/testing, product management, project/program management, requirements/business analysis, operations/DevOps/SRE, marketing/commercialization, team collaboration/communication, organizational/institutional dynamics, philosophy, economics/finance/capital markets, psychology/sociology, education/workforce development, anthropology/cultural dynamics, law/policy/governance, military/security strategy, historical context.
- **Market & Macro Systems Analysis**: discuss systemic forces, regulatory/policy trajectories, market structure & liquidity, geopolitical/security implications, societal adoption & behavior shifts, competitive/ecosystem positioning, macroeconomic/industry models when the bug has strategic impact.
- **Inference Summary**: note adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), operational risks (upgrade readiness, testing coverage, rollback triggers).
- **Collaboration & Communication Plan**: identify stakeholders, communication cadence/channels, cross-functional alignment tactics relevant to the bug.
- **Organizational & Strategic Fit**: analyze business model impact, institutional capabilities/gaps, change management/governance requirements, strategic positioning/differentiation implications.
- **Codebase & Library References**: list APIs/libraries with usage patterns, common pitfalls, stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes.
- **Authoritative Literature**: cite documentation, papers, audits with core findings, practical implications, credibility signals.
- **Actionable Conclusions**: summarize key lessons, best practices, preventive measures, prioritized follow-up actions.
- **Open Questions & Research Agenda**: capture remaining challenges, hypotheses/experiments, data/resource needs, timeline/ownership for further exploration.
- **APA Style Source Citations**: maintain a consolidated APA 7th edition reference list rather than per-task entries; ensure each task cites sources back to that section.

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
- [Task Bank](#task-bank-tasks-1-n)
  - [Topic 1: Topic title](#topic-1-topic-title)
    - [Task 1: Title](#task-1-title)
    - [Task 2: Title](#task-2-title)
  - [Topic 2: Topic title](#topic-2-topic-title)
    - [Task 3: Title](#task-3-title)
    - [Task 4: Title](#task-4-title)

## Executive Summary

- [2–4 bullets: assessment goals, bug type coverage, evaluation approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Tasks |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

- Topic cluster mapping:

| Topic Cluster | Scope | Tasks |
|---|---|---|
| [Cluster A] | [Scope/Boundaries] | Task 1–x |
| [Cluster B] | [Scope/Boundaries] | Task (x+1)–y |

## Glossary, Terminology & Acronyms

- [Key concepts, APIs, patterns relevant to debugging tasks]

## How to Use This in Interviews

- Evaluate fix correctness, root-cause depth, and test coverage
- Scoring: Fix (0–6), Explanation (0–3), Tests (0–1)

## Key Decision Criteria Checklist

- [List key criteria when applicable, e.g., fix approach (simple vs robust), security implications, performance impact, maintainability, test coverage, etc.]

## Key Decision Criteria Matrix (Quick Picks)

| Criteria | Preferred Fix Approach A | Preferred Fix Approach B | Notes/Signals |
|---|---|---|---|
| [Criterion 1] | [Approach description] | [Approach description] | [Decision guidance] |
| [Criterion 2] | [Approach description] | [Approach description] | [Decision guidance] |

## Codebase & Library References

- [Aggregate APIs, libraries, SDKs, audits cited across debugging tasks. Include stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes.]

## Authoritative Literature & Reports

- [List standards, documentation, audits, white/yellow papers, books/manuals, and peer-reviewed studies underpinning bug patterns or fixes. Summarize core findings, practical implications, and language/jurisdiction tags.]

## APA Style Source Citations

- **References:** List all sources cited in the answers, grouped by source language with the targeted distribution (~60% English, ~30% Chinese, ~10% other languages). If credible non-English sources are not available, document the gap and default to high-quality English sources.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language tags (e.g., `[EN]`, `[ZH]`, `[JP]`).
- **Verification:** Ensure each reference is credible, jurisdiction-appropriate, and directly supports the content; highlight regulatory or legal sources when applicable.

## Task Bank (Tasks 1–n)

### Topic 1: [Topic title | scope]

#### Task 1: [Title]

**Language:** python  
**Difficulty:** Intermediate  
**Bloom:** Analyze/Evaluate

### Buggy Code

\`\`\`python
# buggy.py - Smart contract interaction for RWA token transfer
def process_rwa_transfers(transfers):
    total_value = 0
    for transfer in transfers:
        total_value += transfer['asset_value']
    return total_value / len(transfers)  # Bug: division by zero if transfers is empty
\`\`\`

### Failing Test Output

```
AssertionError: Expected 0.0 for empty transfer list, got ZeroDivisionError
```

### Tasks

1. Fix the bug
2. Explain root cause (2–4 sentences)
3. Provide tests that now pass

### Solution Notes (for graders)

**Corrected code:**

\`\`\`python
def process_rwa_transfers(transfers):
    if not transfers:
        return 0.0
    total_value = 0
    for transfer in transfers:
        total_value += transfer['asset_value']
    return total_value / len(transfers)
\`\`\`

**Root cause explanation:** The function fails when the input list is empty because it attempts division by zero. The fix adds a guard clause to return 0.0 for empty inputs, ensuring safe calculation of average asset value across RWA token transfers.

**Tests:**
- `process_rwa_transfers([])` -> `0.0` (now passes)
- `process_rwa_transfers([{"asset_value": 100000}])` -> `100000.0` (now passes)

> **Working note:** Use `[TBD]` placeholders while planning Contents and reference sections; clear all placeholders during finalization.

**Grader Notes:**
- Partial credit: Correct diagnosis but incomplete fix → 60%
- Common mistakes: catching exception instead of preventing it, incorrect edge-case handling

### Supporting Artifacts (for clarity)

- Mermaid diagrams (e.g., flowchart showing expected vs actual behavior, sequence diagram)
- Tables (e.g., expected vs actual output comparison)
- Analogies to explain the bug pattern

### Technical Evaluation Considerations (for graders)

- Performance: [Does the fix impact performance? Expected complexity]
- Security: [Does the bug or fix have security implications?]
- Maintainability: [Is the fix clear and maintainable?]
- Algorithm Complexity & Error Tolerance: [Edge case handling quality]
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

### Terminology & Key Concepts (bug pattern)

**[Bug Pattern/Concept]:** [Clear explanation with example]

### Context & Background (bug context)

- Historical Evolution: [Common pattern history]
- Technical Context: [API/framework context]
- Best Practices Violated: [...]
- Key Events & Statistics: [When relevant, e.g., security incidents]

### Validation & Evidence Checks (bug verification)

- [Data point, benchmark, or test case that demonstrates the bug/fix correctness]

### Counterexamples & Edge Cases (alternative fix scenarios)

- [Scenario where fix might fail or alternative handling + clarification]

### Alternatives Considered (fix approach variations)

- [Alternative fix approaches, why selected approach was preferred]

### Trade-offs & Decision Guidance (fix evaluation)

- [Trade-off analysis in fix approach selection; decision criteria]

### Market & Macro Systems Analysis (for advanced bugs)

- Systemic Forces & Feedback Loops: [...]
- Regulatory & Policy Trajectories: [...]
- Market Structure & Liquidity Dynamics: [...]
- Geopolitical & Security Implications: [...]
- Societal Adoption & Behavioral Shifts: [...]
- Competitive & Ecosystem Positioning: [...]
- Macroeconomic & Industry Economic Models: [...]

### Inference Summary (for advanced bugs)

- Adoption Signals: [... how bug affects adoption]
- Interoperability Impacts: [... how bug affects interoperability]
- Roadmap Implications: [... include upgrade sequencing considerations]
- Operational Risks: [... highlight upgrade readiness, testing coverage, rollback triggers]

### Collaboration & Communication Plan (when relevant)

- Stakeholders & Roles: [... who needs to be informed about the bug/fix]
- Communication Cadence & Channels: [...]
- Cross-Functional Alignment Tactics: [...]

### Organizational & Strategic Fit (when relevant)

- Business Model Impact: [... how bug affects business]
- Institutional Capabilities & Gaps: [...]
- Change Management & Governance: [...]
- Strategic Positioning & Differentiation: [...]

### Actionable Conclusions (debugging takeaway)

- [Key lesson, best practice, preventive measure; prioritized action]

### Open Questions & Research Agenda (for advanced bugs)

- Remaining Challenges: [... systemic issues, edge cases revealed by bug]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]
