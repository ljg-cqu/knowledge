# Extract How-To Questions

**Task**: Create procedural questions that test ability to execute step-by-step processes, implement methods, or follow workflows from decision-critical content.

**Definition**: Each question asks "How do you..." or "What are the steps to..." and expects a structured, executable procedure as the answer.

**Rules**:

**Coverage:**
- Read entire source thoroughly—identify all procedures, algorithms, workflows, implementation methods, and technical processes
- Extract comprehensively to reflect source depth; prioritize processes that are actionable and decision-critical
- Do not skip sections; cover both explicit step-by-step instructions and implicit procedures logically derivable from source

**Fidelity:**
- Ground all steps in procedures explicitly stated or logically implied in source
- Never invent steps, parameters, or implementation details beyond source content
- Maintain correct order, dependencies, and conditional logic from source

**Focus:**
- Executable procedures: step-by-step processes that can be followed to achieve a specific outcome
- Implementation methods: how to build, configure, or apply technical solutions
- Workflows: multi-step processes with decision points or branching logic
- Algorithms: computational procedures with defined inputs, steps, and outputs
- Techniques: specific methods for accomplishing tasks

**Format:**
- **Question**: 1-2 sentences presenting context + explicit "How do you..." or "What are the steps to..." prompt
- **Answer**: Structured procedure with:
  - Prerequisites (if applicable)
  - Numbered steps (3-10 steps typical)
  - Decision points or conditional branches (if applicable)
  - Expected outcome or validation criteria
  - May include code snippets, commands, or formulas—keep concise
- Make self-contained; include minimal context needed
- Use imperative voice for steps ("Do X", "Configure Y")

**Output Format**:

Markdown ordered list only:
1. Q: [context + "How do you..." or "What are the steps to..."]
   A: 
   - **Prerequisites**: ... (optional)
   - **Steps**:
     1. [First step with specific actions]
     2. [Second step with parameters/details]
     3. [Continue as needed]
     - *If [condition]*: [alternative step]
   - **Outcome**: ... (what success looks like)

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
- Focus on actionable, repeatable procedures rather than conceptual understanding
