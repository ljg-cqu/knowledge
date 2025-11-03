# Interview Q&A

Framework for generating high-quality interview question banks with proper structure, citations, and multi-dimensional evaluation.

---

## Specifications

### Scope and Structure

- **Scope**: 25–30 Q&A pairs for senior/expert level
- **Answer Length**: 150–300 words covering misconceptions, failure paths, trade-offs, decision criteria
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Artifacts**: ≥1 diagram + ≥1 table per topic cluster

### Content Principles

- **MECE Coverage**: Technical, theoretical, practical, contextual
- **Analysis Required**: Assumptions, failure paths, comparisons, trade-offs, adoption signals
- **Multi-Perspective**: Engineering, architecture, QA, product, operations, security, economics, policy

### Evaluation Dimensions

- **Technical**: Performance, security, scalability, reliability
- **Business**: Cost, efficiency, impact, market fit
- **Strategic**: Regulatory landscape, adoption barriers, competitive dynamics
- **Actionable**: Best practices, mitigations, open questions

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Sources**: Official docs, peer-reviewed studies, standards, audits, vetted code
- **Format**: APA 7th with language tags
- **Distribution**: Codebase/libraries (repos, maturity, benchmarks); Literature/Reports

### Reference Minimum Requirements

| Reference Section | Floor Count | Notes |
| --- | --- | --- |
| Glossary, Terminology & Acronyms | ≥10 entries | Core concepts, domain-specific jargon, localized terminology |
| Codebase & Library References | ≥5 entries | Primary stack components, SDKs, supporting tooling |
| Authoritative Literature & Reports | ≥6 entries | Standards, peer-reviewed work, regulatory/industry analyses |
| APA Style Source Citations | ≥12 total | Language mix (~60% EN / ~30% ZH / ~10% other) |

> **Exception handling:** If a section cannot meet the floor count, explicitly state the shortfall, provide rationale, and outline a plan to source additional materials.

### Usage Guidelines

1. **Structure & Coverage**: Follow complete framework structure and apply MECE principles
2. **Difficulty Balance**: Maintain 20/40/40 distribution (Foundational/Intermediate/Advanced)
3. **Reference Minimums**: Meet all floor counts (≥10 glossary, ≥5 codebase, ≥6 literature, ≥12 citations)
4. **Language Distribution**: Include multilingual sources with tags (~60% EN, ~30% ZH, ~10% other)
5. **Format Consistency**: Maintain uniform formatting across all reference sections
6. **Visual Support**: Include supporting artifacts (diagrams, tables, code samples) per topic cluster
7. **Multi-Dimensional Analysis**: Address engineering, business, strategic, and operational perspectives
8. **Gap Management**: Document any shortfalls with rationale and remediation plan

---

## Output Format

Use this structure when generating question banks:

```markdown
## Contents

- [Topic Areas](#topic-areas-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
  - [Q2: [Question text]](#q2-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q3: [Question text]](#q3-question-text)
- [Reference Sections](#reference-sections)

---

## Topic Areas (Questions 1–N)

### Topic 1: [Topic title]

#### Q1: [Question text]

**Difficulty:** [Foundational/Intermediate/Advanced] | **Type:** [Theoretical/Practical/Scenario]

**Answer:** (150-300 words with technical depth, examples, trade-offs)

**Supporting Artifacts:** [Mermaid Diagram/table/code/formula]

**Key Insights:** Misconception | Failure Path | Trade-offs

---

## Reference Sections

### Glossary, Terminology & Acronyms

**Format:**

```text
**Term/Acronym**: Definition [Language Tag]
```

**Example:**

```text
**MECE** (Mutually Exclusive, Collectively Exhaustive): Framework ensuring categories don't overlap and cover all possibilities [EN]
```

### Codebase & Library References

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


