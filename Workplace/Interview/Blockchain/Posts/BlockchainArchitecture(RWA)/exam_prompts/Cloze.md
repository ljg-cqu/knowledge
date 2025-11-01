# Cloze / Fill-in-the-Blank Prompt Template

Purpose: Short fill-in-the-blank items to test precise recall (definitions, terms, short phrases, equations).

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 10–15 cloze items per topic cluster. Difficulty distribution: Foundational (30%), Intermediate (50%), Advanced (20%).
- **Numbering:** Number all items sequentially (Item 1, Item 2, etc.) for easy tracking and reference. Include item numbers in Contents links.
- **Bloom Taxonomy:** Target Remember/Understand levels. Foundational items test direct recall of definitions; intermediate items require understanding of relationships between concepts; advanced items test comprehension of nuanced distinctions or context-dependent terminology.
- **Term Selection:** Use MECE principles to choose target terms/phrases. Cover key vocabulary (technical terms, protocols, acronyms), formulas, and short conceptual phrases.
- **Scope:** Keep each item narrowly scoped and unambiguous. Avoid overlapping blanks or ambiguous phrasing that could confuse candidates.
- **Context:** Provide sufficient surrounding text to make the blank unambiguous; avoid overly generic sentences.

### 2. Content Design

- **Target Level:** Remember/Understand (Bloom). Test factual recall, definition accuracy, and basic comprehension.
- **Answer Format:** Provide canonical answers as arrays including accepted synonyms (e.g., ["scalability", "scale"]) and alternate spellings (e.g., "decentralization" vs "decentralisation").
- **Normalization Rules:** Define explicit rules: case-insensitive matching, whitespace trimming, punctuation stripping. State rounding/formatting conventions for numeric answers.
- **Partial Credit:** State per-blank scoring (e.g., 1 point per correct blank) and tolerance ranges for numeric values.

### 3. Evaluation & Grading

- **Acceptance Lists:** Provide a list of acceptable answers per blank; include common variations and synonyms.
- **Tolerances:** For numeric blanks, specify acceptable ranges (e.g., ±2% or ±0.5 units).
- **Grader Notes:** Document borderline cases and common near-miss answers; provide guidance on when to award partial credit.
- **Distractor Notes:** Include a brief note on why common wrong answers are incorrect to aid feedback systems.

### 4. Execution & Format

- **Format:** Markdown. Use underscores (___) or brackets ([blank]) to indicate blanks clearly.
- **Accessibility:** Provide ALT text for any inline images or diagrams used in cloze items.
- **Tags:** Label each item with Difficulty and Bloom level.
- **Citations:** Include APA 7 citations when definitions rely on external authoritative sources (standards, papers, official documentation).

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Items 1–15](#items-115)

## Executive Summary

- [2–3 bullets: assessment goals, term coverage scope, scoring approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Items |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Core terms tested in cloze items]

## How to Use

- Auto-gradable with normalization rules; suitable for timed quizzes or self-assessment
- Per-blank scoring enables partial credit; review borderline answers manually

---

## Items 1–15

### Item 1

**Text:** The blockchain trilemma consists of ___, ___, and ___.

**Answers:**
- Blank 1: scalability (accept: scalability, scale)
- Blank 2: security (accept: security)
- Blank 3: decentralization (accept: decentralization, decentralised)

**Normalization:** case-insensitive, trim whitespace, strip punctuation  
**Partial credit:** 1 point per correct blank  
**Difficulty:** easy  
**Bloom:** Remember
```
