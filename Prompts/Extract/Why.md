# Extract Why-Chain Questions

**Task**: Create 5-Why chain questions that trace decision-critical problems or phenomena from observable symptoms to root causes.

**Definition**: Each question presents an observable effect, symptom, or outcome and guides iterative causal exploration through 3-5 "why" levels to identify actionable root causes.

**Rules**:

**Coverage:**
- Read entire source thoroughly—identify all causal relationships, problems, failures, or phenomena with traceable origins
- Extract comprehensively to reflect source depth; prioritize decision-critical issues where root cause understanding drives action
- Do not skip sections; cover both explicit causal chains and implicit ones logically derivable from source

**Fidelity:**
- Ground all causal steps in relationships explicitly stated or logically implied in source
- Never invent causes, mechanisms, or relationships beyond source content
- Each "why" level must follow from the previous answer using source information

**Focus:**
- Causal exploration (not evaluation): trace backward from effect to root cause
- Decision-critical problems: failures, inefficiencies, risks, or opportunities requiring root cause understanding
- Actionable root causes: terminal point should suggest where intervention is possible
- Distinguish proximate causes (immediate triggers) from root causes (fundamental systemic issues)

**Format:**
- **Question**: 1-2 sentences presenting observable symptom/problem + prompt to trace root cause using 5-Why
- **Answer**: Chain of 3-5 levels:
  - **Symptom/Effect**: Initial observation
  - **Why 1**: Immediate cause
  - **Why 2**: Deeper cause
  - **Why 3-5**: Continue until root cause (systemic issue, fundamental constraint, or actionable point)
  - **Root Cause**: Identify the fundamental issue and why stopping here is appropriate
- Make self-contained; include minimal context needed
- May reference code, architecture, or processes—keep concise

**Output Format**:

Markdown ordered list only:
1. Q: [symptom/problem description + "Use 5-Why analysis to identify the root cause"]
   A: 
   - **Symptom**: ...
   - **Why 1**: ... (because...)
   - **Why 2**: ... (because...)
   - **Why 3**: ... (because...)
   - **Why 4-5**: ... (optional, continue if needed)
   - **Root Cause**: ... (explanation of why this is the actionable root)

**Instructions**:
- Use `1.` for every item; Markdown auto-numbers
- Output list only—no headings, comments, or explanations
- Stop the chain when you reach a root cause that is actionable, systemic, or cannot be traced further with source information
