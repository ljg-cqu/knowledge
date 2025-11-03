# Debugging Task

## Specifications

- **Scope**: 15–22 tasks
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Bug Types**: Single focused bug (10–50 lines): off-by-one, type mismatch, API, concurrency, edge cases, logic, security, performance
- **Deliverables**: Buggy code, failing tests, corrected code (minimal fix), root-cause explanation (2–4 sentences)
- **Grading**: Fix 0–6 pts, Explanation 0–3 pts, Tests 0–1 pt; partial credit for correct diagnosis

## Output Format

```markdown
## Contents

- [Task Bank](#task-bank-tasks-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Task 1: [Bug description]](#task-1-bug-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Task 2: [Bug description]](#task-2-bug-description)
- [Reference Sections](#reference-sections)

---

## Task Bank (Tasks 1–N)

### Topic 1: [Topic title]

#### Task 1: [Bug description]

**Language:** [python/javascript/go/rust/solidity] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Buggy Code:**
```[language]
[Code with bug]
```

**Failing Output:** [Error or unexpected behavior]

**Failing Test:**
```[language]
[Test case]
```

**Corrected Code:**
```[language]
[Fixed code with comments]
```

**Root Cause:** [2–4 sentence explanation]

**Passing Tests:**
```[language]
[Test cases]
```

**Grading:** [Rubric] | **Common mistakes:** [List] | **Alternatives:** [Other valid fixes]

---

## Reference Sections

### Minimum Entry Requirements

| Reference section | Floor count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Glossary, Terminology & Acronyms

Define key terms, acronyms, and technical vocabulary with appropriate language tags.

**Format:**

```text
**Term/Acronym**: Definition [Language Tag]
```

**Example:**

```text
**MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

Document repositories, SDKs, audits, and tooling with relevant technical details.

**Required Information:** Stack/Modules, Maturity, Licensing, Integration Hooks, Performance/Security Benchmarks, Consistency Guarantees, Reliability/HA, Language Support.

**Format:**

```text
**[Project/Library Name]** (GitHub: owner/repo | License: Type)
- Description: Brief overview
- Stack: Technologies used
- Maturity: Production/Beta/Experimental
- Performance: Key metrics
- Security: Audit status, vulnerability notes
```

### Authoritative Literature & Reports

Summarize standards, white papers, peer-reviewed literature, and regulatory reports with source credibility assessment.

**Required Information:** Core Findings, Credibility, Language/Jurisdiction.

**Format:**

```text
**[Title]** (Year) [Language Tag]
- Authors: Names/Organization
- Type: Standard/White Paper/Academic Paper/Regulatory Report
- Key Findings: Summary
- Credibility: Peer-reviewed/Industry standard/Regulatory authority
- Jurisdiction: Applicable regions/markets
```

### APA Style Source Citations

List sources grouped by language (~60% EN, ~30% ZH, ~10% other). Follow APA 7th edition with language tags.

**Example:**

```text
Smith, J., & Wang, L. (2024). Blockchain consensus mechanisms: A comparative analysis.
    Journal of Distributed Systems, 15(3), 245-267. https://doi.org/10.xxxx/jds.2024.15.3.245 [EN]

张伟, & 李娜. (2024). 区块链技术在供应链金融中的应用研究.
    计算机科学, 51(2), 88-95. [ZH]

Nakamoto, S. (2008). Bitcoin: A peer-to-peer electronic cash system.
    https://bitcoin.org/bitcoin.pdf [EN]
```
```


