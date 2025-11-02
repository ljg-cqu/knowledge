# Multiple-Choice

*See [../Requirements.md](../Requirements.md) for common guidelines.*

## Specifications

- **Scope**: 30–50 MCQs
- **Format**: Concise stems (1–2 sentences), 4 options, exactly one correct
- **Distractors**: Map to misconceptions or outdated practices
- **Rationale**: 1–2 sentences
- **Grading**: Machine-gradable; no partial credit

## Output Format

```markdown
## Contents

- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)
- [Question Bank](#question-bank-questions-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Q1: [Question text]](#q1-question-text)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Q2: [Question text]](#q2-question-text)

---

## Glossary, Terminology & Acronyms

[Key terms, acronyms, definitions with language tags]

---

## Codebase & Library References

- [Aggregate repositories, SDKs, audits, or tooling suites cited across the deep-dive bank. Include stack, modules, maturity, licensing, integration hooks, performance/security benchmarks, distributed consistency guarantees, reliability/HA posture, and language support.]

---

## Authoritative Literature & Reports

- [Summarize standards, white/yellow papers, peer-reviewed literature, regulatory reports, and other vetted references referenced across question clusters, with notes on core findings, credibility, and language/jurisdiction.]

---

## APA Style Source Citations

- **References:** List all sources cited in the answers, grouped by source language with the targeted distribution (~60% English, ~30% Chinese, ~10% other languages). If credible non-English sources are not available, document the gap and default to high-quality English sources.
- **Format:** Follow APA 7th edition (author, year, title, source, DOI/URL when available) and include language tags (e.g., `[EN]`, `[ZH]`, `[JP]`).
- **Verification:** Ensure each reference is credible, jurisdiction-appropriate, and directly supports the content; highlight regulatory or legal sources when applicable.

---

## Question Bank (Questions 1–N)

### Topic 1: [Topic title]

#### Q1: [Question text]

**Language:** [python/javascript/solidity/N/A] | **Difficulty:** [Foundational/Intermediate/Advanced]

**Options:**
- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

**Answer:** [A/B/C/D]

**Rationale:** [1–2 sentence explanation]

**Distractor notes:** [Why other options are incorrect]
```
