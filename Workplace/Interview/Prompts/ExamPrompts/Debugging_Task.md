# Debugging / Code-Reading Prompt Template

Purpose: Provide a short buggy code snippet plus failing output; ask students to fix the bug, explain the root cause, and supply minimal passing tests.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 5–8 debugging tasks per topic cluster (aim for 7+ when comprehensive coverage is needed; use 5–6 for focused or narrow topic clusters). Difficulty distribution: Foundational (20%), Intermediate (50%), Advanced (30%).
- **Numbering:** Number all tasks sequentially (Task 1, Task 2, etc.) for easy tracking and reference. Include task numbers in Contents links.
- **Bloom Taxonomy:** Target Analyze/Evaluate levels. Foundational tasks involve identifying obvious bugs with clear error messages; intermediate tasks require tracing logic flow and understanding API contracts; advanced tasks demand evaluating subtle concurrency issues or security vulnerabilities.
- **Bug Scope & Elements:** Provide a single, realistic, focused bug in a 10–50 line snippet. Avoid multi-bug puzzles unless explicitly testing triage skills. Cover: **Technical** (algorithms, algorithm complexity issues, protocols, patterns, best practices, frameworks, libraries, hardware/resource issues), **Theoretical** (principles, models), and **Practical** (edge-case handling, security flaws, permission/consensus governance bugs, use cases).
- **Bug Types:** Cover common categories: off-by-one errors, type mismatches, incorrect API usage, concurrency issues, edge-case handling, logic errors, security flaws (e.g., missing validation), performance issues, or governance/permission violations.
- **Context:** Include minimal surrounding context (imports, data structures, function calls) to make the bug reproducible without extraneous code. Include relevant historical context, API documentation, best practices, or common pitfall notes.
- **Codebases & Libraries:** When bugs involve framework-specific issues, reference authoritative repositories, SDKs, official documentation, and known pitfalls.
- **Authoritative Literature:** Base realistic bugs on documented anti-patterns from white/yellow papers, security audits, standards, or API documentation.
- **Critical Thinking Artifacts:** Capture explicit assumption lists, validation checks, counterexamples/edge cases, alternatives considered, and actionable conclusions in the expected solution and grader notes.
- **Validation & Evidence Checks:** Provide test cases demonstrating the bug and validating the fix.
- **Counterexamples & Edge Cases:** Include scenarios where naive fixes might fail or where alternative fix approaches have trade-offs, emphasizing failure/unhappy paths and recovery expectations.
- **Governance & Trust Dimensions:** Include bugs related to permission boundaries, trust model violations, privacy leaks, design-pattern mismatches, system error-tolerance failures, or reliability/HA issues when applicable.
- **Perspectives:** Ensure coverage across: Engineering (front-end, back-end, full-stack), architecture & infrastructure (including hardware design, deployment, and energy/resource consumption), database & data engineering, quality assurance/testing, product management, project/program management, requirements/business analysis, operations & DevOps, marketing & go-to-market.
- **Philosophical & Macro Disciplines:** For advanced bugs, integrate broader considerations from philosophy (necessity vs. contingency, ethics, epistemology), economics, finance, capital markets (stock/crypto/commodity exchanges, liquidity, valuation), psychology, sociology, anthropology, law, policy, military strategy, education systems, and historical analysis as relevant to bug context.
- **Collaboration & Organizational Dynamics:** For advanced bugs, consider how bugs impact cross-functional communication, governance models, institutional constraints, or change management.
- **Organizational & Strategic Operations:** For advanced bugs, consider business model impact, institutional capabilities, change readiness implications, and strategic positioning effects of the bug and fix.
- **Inference Lists:** For advanced bugs, test understanding of how bugs affect adoption signals, interoperability impacts, roadmap implications (including upgrade sequencing), and operational risks (including upgrade readiness, testing coverage, rollback triggers).
- **Open Questions & Research:** For advanced bugs, surface awareness of systemic issues, edge cases, emergent risks, and investigation needs revealed by the bug.
- **Misconception Targeting:** Document the debugging misconception or faulty heuristic each task should expose, along with the corrective framing to include in the output template for interviewer debriefs.

### 2. Content Design

- **Target Level:** Analyze/Evaluate (Bloom). Test ability to read code, diagnose root causes, and propose correct fixes with technical depth and awareness of best practices (senior/expert level).
- **Deliverables:** Require three outputs:
  1. **Corrected code:** Fixed version with minimal changes (annotate changes with comments if helpful).
  2. **Root-cause explanation:** 2–4 sentence explanation identifying the bug, why it occurs, and what principle/pattern was violated.
  3. **Passing tests:** Minimal test cases that now pass (previously failed) to demonstrate the fix.
- **Failing Output:** Provide realistic failing test output (stderr, assertion errors, unexpected behavior) to guide diagnosis.
- **Evaluation Dimensions:** Technical (correctness, security, performance impact, maintainability) and practical (adherence to API contracts, best practices, error-tolerance expectations).
- **Trade-offs:** For advanced bugs, highlight trade-offs in fix approaches (e.g., simple fix vs robust fix, performance vs clarity).
- **Governance & Assurance:** When applicable, assess fixes for permission boundary violations, trust model integrity, or privacy/transparency requirements.

### 3. Evaluation & Grading

- **Rubric:** Recommended scoring: Fix correctness (0–6 pts), Explanation quality (0–3 pts), Tests provided (0–1 pt). Adjust per difficulty.
- **Partial Credit:** Award partial credit for correct diagnosis even if fix is incomplete, or correct fix with weak explanation.
- **Grader Notes:** Document common incorrect approaches (e.g., treating symptom instead of root cause) and alternative valid fixes. List edge cases where fixes might fail.
- **Misconception Focus:** Explain the misconception this bug surfaces and the insight graders should reinforce.
- **Failure Path Insight:** Describe the failure/unhappy path the bug reveals and the mitigation or regression testing guidance interviewers should emphasize.

### 4. Execution & Format

- **Planning:** Think carefully, reflect on thinking, create comprehensive plan before generation.
- **Format:** Markdown with proper headings and code blocks. Use fenced code blocks for buggy code, failing output, and corrected code. Include instructions to run tests and verify the fix.
- **Clarity Aids:** When helpful, include a small mermaid diagram or table showing expected vs actual behavior, or a flowchart highlighting where logic diverges. Use diverse visualization types: mermaid diagrams (structural, behavioral, analytical), tables, analogies, comparisons. For mermaid portability: avoid edge labels and quote node labels containing special characters (parentheses, slashes).
- **Terminology:** Explain technical concepts and error patterns clearly in root-cause explanations.
- **Context Integration:** Include relevant API documentation, best practices, or common pitfall context.
- **Real-World Grounding:** Base bugs on real-world coding errors and practical debugging scenarios.
- **Navigation:** Add a compact "Contents" section near the top with anchor links to major sections and all tasks (Task 1–Task n) using GitHub-compatible anchors (lowercase, hyphens; punctuation removed).
- **Preface Sections (required at top of the document):**
  - Contents (compact ToC with anchor links to major sections and Task 1–Task n)
  - Executive Summary (2–4 bullets: assessment goals, bug type coverage, evaluation approach)
  - Coverage & Difficulty Summary: Difficulty Distribution Table (Foundational/Intermediate/Advanced with counts and task indices); Topic Cluster Mapping Table (Cluster → scope → task indices)
  - Glossary & Acronym Index (key concepts, APIs, patterns relevant to debugging tasks)
  - How to Use This in Interviews (evaluation rubric, partial credit guidelines, and fix verification instructions)
  - Key Decision Criteria Checklist (when applicable: fix approach criteria, security considerations, performance impacts, etc.)
  - Key Decision Criteria Matrix (Quick Picks) mapping fix approaches to criteria (when applicable)
- **Tags:** Label each task with Difficulty, Bloom level, and language.
- **Research & Quality:** Gather latest information from authoritative sources (official documentation, white/yellow papers, academic theses, audits, standards, books/manuals, curated wikis/encyclopedias, codebases); avoid outdated information; cross-reference multiple sources; ensure essential/valuable content with high quality; verify accuracy, completeness, relevance, and MECE compliance; apply both creative and critical thinking to validate question quality.
- **Holistic Reasoning:** Ensure bugs reflect realistic coding challenges and teach broader debugging principles.
- **Citations:** Include APA 7th edition references for bugs referencing external APIs, standards, or protocol-specific behavior.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use This in Interviews](#how-to-use-this-in-interviews)
- [Key Decision Criteria Checklist](#key-decision-criteria-checklist)
- [Key Decision Criteria Matrix (Quick Picks)](#key-decision-criteria-matrix-quick-picks)
- [Tasks](#tasks)
  - [Task 1: Title](#task-1-title)
  - [Task 2: Title](#task-2-title)
  - ... (link to each task)

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

## Glossary & Acronym Index

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

---

## Task 1: [Title]

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

### Codebase & Library References (when applicable)

- **[API/Library]:** [Correct usage pattern, common pitfalls, official documentation reference; stack, modules, maturity, licensing, integration notes, performance/security considerations, distributed consistency support, reliability/HA posture, permission/governance notes]

### Authoritative Literature (bug pattern sources)

- **[Documentation/Paper/Audit]:** [Bug pattern description, best practice guidance, reference link; core findings, practical implications]

### Actionable Conclusions (debugging takeaway)

- [Key lesson, best practice, preventive measure; prioritized action]

### Open Questions & Research Agenda (for advanced bugs)

- Remaining Challenges: [... systemic issues, edge cases revealed by bug]
- Hypotheses & Experiments: [...]
- Data/Resource Needs: [...]
- Timeline & Ownership for Exploration: [...]

### APA Style Source Citations (when referencing external APIs/standards)

- **References:** List sources for API documentation, bug pattern literature, or security advisories.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available).
- **Verification:** Ensure each reference is credible and directly supports the content.
