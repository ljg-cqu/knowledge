# Extract Debug Cards

**Task**: Create debug cards from source text that test detection and correction of decision-critical errors.

**Definition**: Each card presents a flawed statement/plan/code/decision with its correction.

## Rules

**Source Coverage**:
- Read entire text thoroughly; cover all decision-critical aspects
- Use only information explicitly stated or logically implied; never invent or contradict source content

**Error Selection**:
- Realistic, plausible mistakes (not trivial typos)
- Decision-critical: would change understanding, risk, or action

**Card Structure**:
- **Question**: Flawed content + "What is wrong and how to fix it?"
- **Answer**: (a) identify issue, (b) explain impact, (c) provide correction
- Make self-contained; include minimal context needed without source text
- May include code snippets, formulas, or diagrams—keep minimal

## Output Format

Markdown ordered list only:
1. Q: ... (flawed content + debug question)
   A: ... (issue + explanation + corrected form)

- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
