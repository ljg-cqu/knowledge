# Multiple-Choice (MCQ) Prompt Template

Purpose: Single-best-answer MCQs (4 options) with plausible distractors and concise rationales for graders.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 15–25 MCQs per topic cluster. Difficulty distribution: Foundational (30%), Intermediate (50%), Advanced (20%).
- **Bloom Taxonomy:** Target Remember/Understand/Apply levels. Foundational MCQs test factual recall; intermediate MCQs require understanding relationships and selecting correct approaches; advanced MCQs demand application of concepts to novel scenarios or selection among nuanced alternatives.
- **Topic Selection:** Use MECE principles to select topics. Ensure comprehensive coverage across technical areas (protocols, algorithms, patterns), theoretical foundations (principles, models), and practical concerns (regulations, use cases, trade-offs).
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
- **Citations:** Include APA 7 citations when factual claims (e.g., protocol specs, performance benchmarks, regulatory requirements) require authoritative sourcing.

## Output Template

```markdown
Stem: <question text>

Options:
- A. Option A
- B. Option B
- C. Option C
- D. Option D

Answer: A

Rationale:
- Correct: <short explanation>
Rationale for distractors:
- B: <why wrong>
- C: <why wrong>
- D: <why wrong>

Difficulty: medium
Bloom: Apply
```
