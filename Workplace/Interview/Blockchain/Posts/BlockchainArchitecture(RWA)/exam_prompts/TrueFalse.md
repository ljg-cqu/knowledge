# True / False (T/F) Prompt Template

Purpose: Short, unambiguous declarative statements for binary judgment (True/False). Include a brief rationale when full credit requires it.

## Contents

- [Requirements](#requirements)
- [Output Template](#output-template)

## Requirements

### 1. Coverage & Organization

- **Question Quantity & Distribution:** Generate 12–20 True/False statements per topic cluster. Difficulty distribution: Foundational (40%), Intermediate (40%), Advanced (20%).
- **Bloom Taxonomy:** Target Remember/Understand/Apply levels. Foundational statements test factual recall; intermediate statements require understanding of principles and relationships; advanced statements involve applying concepts to judge scenario-based claims.
- **Statement Design:** Create factual, unambiguous declarative statements. Use MECE principles to avoid overlapping or contradictory items within a bank.
- **Precision:** Keep statements short (≤2 lines) and avoid double negatives, vague qualifiers (e.g., "often", "usually"), or ambiguous technical terms.
- **Scope:** Cover key facts, definitions, principles, and simple scenario judgments. Mix foundational recall with conceptual understanding.

### 2. Content Design

- **Target Level:** Remember/Understand/Apply (Bloom). Use factual statements for lower levels; use concise scenario-based judgments for higher levels (e.g., "Given X constraint, approach Y is optimal").
- **Rationale:** Provide a 1–2 sentence rationale explaining why the statement is true or false. Include a one-sentence note on common misconceptions to aid feedback.
- **Justification (Optional):** For higher-credit items, require a brief written justification (2–3 sentences) in addition to the T/F answer. State scoring split (e.g., 70% for correct letter + 30% for valid rationale).

### 3. Evaluation & Grading

- **Grading:** Machine-gradable by exact-match of answer letter (A/True or B/False). Normalize accepted inputs (e.g., accept "A", "True", "true", "T").
- **Partial Credit:** If justification is required, award partial credit for correct answer with weak justification or incorrect answer with valid reasoning that identifies a key issue.
- **Quality Check:** Ensure statements are defensible with authoritative sources; avoid subjective or opinion-based items.

### 4. Execution & Format

- **Format:** Markdown with clearly labeled statement, options (A/B), answer, and rationale. Use fenced blocks for code snippets if the statement references code behavior.
- **Tags:** Label each item with Difficulty (Foundational/Intermediate/Advanced) and Bloom level.
- **Citations:** Include APA 7 citations when statements rely on external standards, protocol specifications, regulatory requirements, or published research.

## Output Template

```markdown
## Contents

- [Executive Summary](#executive-summary)
- [Coverage & Difficulty Summary](#coverage--difficulty-summary)
- [Glossary & Acronym Index](#glossary--acronym-index)
- [How to Use](#how-to-use)
- [Statements 1–20](#statements-120)

## Executive Summary

- [2–3 bullets: assessment goals, statement scope, grading approach]

## Coverage & Difficulty Summary

| Difficulty | Count | Statements |
|---|---:|---|
| Foundational | | |
| Intermediate | | |
| Advanced | | |

## Glossary & Acronym Index

- [Key terms and concepts covered]

## How to Use

- Machine-gradable by exact-match of answer (A/True or B/False); normalize inputs ("A", "True", "true", "T")
- Optional: require justification for higher-credit items (70% for correct letter + 30% for rationale)

---

## Statements 1–20

### SX: [Short title]

**Statement:** Byzantine Fault Tolerance consensus algorithms can tolerate up to 50% malicious nodes.

**Options:**
- A. True
- B. False

**Answer:** B

**Rationale:**
- **Correct:** BFT algorithms (e.g., PBFT) can tolerate up to (n-1)/3 malicious nodes, not 50%. For example, in a 4-node network, only 1 Byzantine node can be tolerated.
- **Common misconception:** Confusion with crash fault tolerance (e.g., Raft), which tolerates up to 50% crash failures.

**Difficulty:** intermediate  
**Bloom:** Understand  
**Citation:** Castro, M., & Liskov, B. (1999). Practical Byzantine fault tolerance. *OSDI*, 99, 173–186.
```
