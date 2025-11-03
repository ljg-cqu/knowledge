# Cloze / Fill-in-the-Blank

## Specifications

- **Scope**: 24–40 items
- **Format**: Unambiguous blanks (___); array of acceptable answers
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Normalization**: Case-insensitive, trim whitespace, strip punctuation; specify numeric tolerances
- **Grading**: Acceptance lists with tolerances; document borderline answers, partial credit

## Output Format

```markdown
## Contents

- [Item Bank](#item-bank-items-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Item 1: [Brief description]](#item-1-brief-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Item 2: [Brief description]](#item-2-brief-description)
- [Reference Sections](#reference-sections)

---

## Item Bank (Items 1–N)

### Topic 1: [Topic title]

#### Item 1: [Brief description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Text with ___ or [blank]]

**Acceptable Answers:** ["answer1", "answer2", "answer3"]

**Grading:** [Rubric] | **Common incorrect:** [List]

**Rationale:** [Brief explanation]

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

