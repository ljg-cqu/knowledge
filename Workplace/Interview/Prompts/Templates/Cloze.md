# Cloze / Fill-in-the-Blank

*See [../Requirements.md](../Requirements.md) for common guidelines.*

## Specifications

- **Scope**: 24–36 items
- **Format**: Unambiguous blanks (___); array of acceptable answers
- **Normalization**: Case-insensitive, trim whitespace, strip punctuation; specify numeric tolerances
- **Grading**: Acceptance lists with tolerances; document borderline answers, partial credit

## Output Format

```markdown
## Contents

- [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
- [Codebase & Library References](#codebase--library-references)
- [Authoritative Literature & Reports](#authoritative-literature--reports)
- [APA Style Source Citations](#apa-style-source-citations)
- [Item Bank](#item-bank-items-1-n)
- [Topic 1: [Topic title]](#topic-1-topic-title)
  - [Item 1: [Brief description]](#item-1-brief-description)
- [Topic 2: [Topic title]](#topic-2-topic-title)
  - [Item 2: [Brief description]](#item-2-brief-description)

---

## Glossary, Terminology & Acronyms

[Key terms tested in cloze items with language tags]

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

## Item Bank (Items 1–N)

### Topic 1: [Topic title]

#### Item 1: [Brief description]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Statement:** [Text with ___ or [blank]]

**Acceptable Answers:** ["answer1", "answer2", "answer3"]

**Grading:** [Rubric] | **Common incorrect:** [List]

**Rationale:** [Brief explanation]
```
