# Multiple-Choice (MCQ) Prompt Template

Purpose: Single-best-answer MCQs (4 options) with plausible distractors and concise rationales for graders.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 15–25 MCQs per topic cluster. Difficulty distribution: Foundational (30%), Intermediate (50%), Advanced (20%).
- **Numbering:** Number all questions sequentially (Q1, Q2, etc.) for easy tracking and reference. Include question numbers in Contents links.
- **Bloom Taxonomy:** Target Remember/Understand/Apply levels. Foundational MCQs test factual recall; intermediate MCQs require understanding relationships and selecting correct approaches; advanced MCQs demand application of concepts to novel scenarios or selection among nuanced alternatives.
- **Topic Selection:** Use MECE principles to select topics. Ensure comprehensive coverage across technical areas (protocols, algorithms, patterns), theoretical foundations (principles, models), and practical concerns (regulations, use cases, trade-offs). For blockchain architecture (RWA), emphasize consensus mechanisms, asset tokenization standards, custody models, scalability solutions, and regulatory frameworks.
- **Distractor Design:** Ensure distractors map to common misconceptions, near-misses, or outdated practices. Distractors must be mutually exclusive and plausible to candidates unfamiliar with the topic.
- **Balance:** Mix factual recall, conceptual understanding, and application-level questions within a bank.

### 2. Content Design

- **Target Level:** Remember/Understand/Apply (Bloom). Adjust difficulty by the depth of reasoning required to eliminate distractors.
- **Stem:** Provide a clear, concise stem (1–2 sentences). Avoid double negatives, ambiguous phrasing, or "all of the above" / "none of the above" unless pedagogically justified.
- **Options:** Four options labeled A–D. Exactly one correct answer. Distractors should be similar in length and structure to the correct answer to avoid cueing.
- **Rationale:** Provide a 1–2 sentence rationale for the correct answer and brief notes (1 sentence each) explaining why distractors are incorrect (e.g., "B is incorrect because it confuses consensus finality with transaction confirmation").

### 3. Evaluation & Grading

- **Grading:** Machine-gradable by exact-match of the answer letter (A/B/C/D). If randomizing option order, preserve correct index in metadata.
- **Partial Credit:** Not typically used for MCQs; consider offering hints or retries in formative assessments.
- **Quality Check:** Validate that exactly one option is unambiguously correct and that all distractors are defensibly wrong.

### 4. Execution & Format

- **Format:** Markdown. Use fenced code blocks for code snippets or configuration examples in stems/options. Include mermaid diagrams or comparison tables when clarifying technical concepts.
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Citations:** Include APA 7 citations for factual claims (protocol specs, performance benchmarks, regulatory requirements) requiring authoritative sources.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Questions 1–25](#questions-125)

## Executive Summary

- [2–3 bullets: assessment goals, topic coverage, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Questions |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key terms and concepts tested]

## How to Use

- Machine-gradable by exact-match of answer letter; shuffle options client-side to randomize
- Use for formative assessment or timed quizzes; review distractor analytics to identify misconceptions

---

## Questions 1–25

### Q1: Which consensus mechanism prioritizes finality over throughput in permissioned blockchains?

**Stem:** Which consensus mechanism prioritizes finality over throughput in permissioned blockchains?

**Options:**
- A. Raft
- B. PBFT
- C. Proof of Work
- D. Proof of Stake

**Answer:** B

**Rationale:**
- **Correct (B):** PBFT provides Byzantine fault tolerance with deterministic finality, prioritizing safety over speed in permissioned settings.

**Distractor notes:**
- A: Raft provides crash fault tolerance but not Byzantine fault tolerance; suitable for non-adversarial environments.
- C: Proof of Work is used in permissionless blockchains and prioritizes decentralization over finality.
- D: Proof of Stake is primarily for permissionless chains; finality mechanisms vary by implementation.

**Difficulty:** Intermediate  
**Bloom:** Apply
```
