# Extract Problem Statements

**Task**: From the source text, surface and formulate **decision-critical problem statements** in a structured format that can be used directly as input to a nine-aspects problem-analysis prompt.

**Definition**: Each item describes **one concrete problem** (not a solution) using a fixed template that captures context, goals, constraints, stakeholders, scope, history, and uncertainties. The output should be specific and quantifiable so it can be dropped into an analysis prompt without further rewriting.

**Rules**:

- **Coverage**:
  - Read the **entire source** before extracting.
  - Identify explicit and implicit problems, blockers, contradictions, gaps, risks, or opportunities.
  - Extract comprehensively to reflect the source’s depth, but prioritize **decision-critical problems**:
    - If left unaddressed, they **block important decisions** or **create material risk** (financial, operational, reputational, compliance, etc.).
    - Affect **multiple important stakeholders** (e.g., customers + internal teams, managers + frontline, upstream + downstream), or require **1–6 months** of effort or significant budget to address.
    - Have clear or inferable **quantified impact** (e.g., ≥5% change in key metrics such as revenue, cost, quality, satisfaction, safety, or workload).
- **Fidelity**:
  - Ground all problem statements in information **explicitly stated** or **logically implied** by the source.
  - Do **not** invent fictional domains, numbers, or stakeholders that contradict the source; when you generalize, stay within the source’s assumptions.
- **Focus (problem-finding, not solutioning)**:
  - Each item should clearly state **what the problem is**, for whom it is a problem, and in what context.
  - Do **not** propose detailed solutions, recommendations, or action plans here; those belong in downstream analysis prompts.
  - Avoid bundling multiple unrelated problems into one item. If needed, split into separate items.
- **Quantification and clarity**:
  - Follow the filling principle: use **specific, quantifiable descriptions** (numbers, ratios, time spans, amounts, baselines, thresholds) instead of vague phrases like "a lot", "relatively fast", "try to reduce".
  - Where exact numbers are unavailable, provide **reasonable ranges or orders of magnitude** and mark them as estimates.
  - Explicitly distinguish **known facts**, **assumptions**, and **uncertainties** in the final field.

**Output format**:

Produce a **Markdown ordered list only**. Use `1.` for every item; Markdown will auto-number. Output **only** the list—no extra headings, comments, or explanations.

For each problem, use the following structure (aligned with the [Input] template of a nine-aspects problem-analysis prompt):

1. Q: [Short context + "Formulate a structured problem statement using the following [Input] fields."]
   A:
   - **Brief description of the problem to be analyzed**: ...
   - **Background and current situation**: ... (Domain / scenario, current approach, existing phenomena or pain points.)
   - **Goals and success criteria**: ... (Desired outcomes and quantifiable metrics: time, cost, quality, satisfaction, etc. Include current baseline and "minimum acceptable / target / ideal" values.)
   - **Key constraints and resources**: ... (Time window, budget, headcount, policy / compliance requirements, tech stack, existing assets or tools, etc.)
   - **Stakeholders and roles**: ... (Main roles—e.g., customers, managers, partner teams, end users—and their core needs / constraints.)
   - **Time scale and impact scope**: ... (Impacted time span—e.g., 3 months / 1 year / 3 years—plus affected systems / businesses / regions and approximate scale such as user counts, amounts, or frequency.)
   - **Historical attempts and existing solutions (if any)**: ... (Approaches already tried, main outcomes, and key lessons learned. If none, state explicitly.)
   - **Known facts, assumptions, and uncertainties**: ... (What has been reliably verified; what is assumption-based on experience or estimates; where the biggest information gaps are now.)

**Instructions**:

- Use `1.` for every list item; rely on Markdown to auto-number.
- Make each problem statement **self-contained**: someone reading only the answer for one item should understand the problem without needing the source text.
- Keep each field concise but complete—typically **1–3 sentences** per bullet.
- For the last field, clearly label content as, for example, "Facts:", "Assumptions:", "Uncertainties:" inside the same bullet, so later analysis can see where confidence is high or low.
- Do not repeat the same problem in different wording; if two items overlap heavily, merge them into a single, sharper problem statement.
- Do **not** use references like "as mentioned above", "see previous section", or "see the source"; instead, restate the minimal context needed so each problem can serve as a standalone `[Input]` block for a nine-aspects analysis prompt.
