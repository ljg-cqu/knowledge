# Design Solutions and Architectures for a Problem

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Knowledge Repository  
**Related**: [Extract Problem Statements](./Identify.md), [Nine Aspects for Analyzing Problems](./Analyse.md), [LLM-Friendly Prompts Guidelines](../LLM-Friendly_Prompts_Guidelines.md)

## TOC

- [Overview](#overview)
- [When to Use](#when-to-use)
- [LLM Prompt Template: Solution and Architecture Design](#llm-prompt-template-solution-and-architecture-design)
- [Answer Structure](#answer-structure)
- [LLM Self-Check](#llm-self-check)

## Overview

**Task**: Starting from a clearly defined problem (and optionally a completed nine-aspects analysis), design 2–4 coherent solution or architecture options with explicit trade-offs, metrics, and risks.

**Goal**: Provide a small, high-quality set of options that are:
- **Feasible** under stated constraints.
- **Distinct** in structure or strategic stance.
- **Evaluable** via clear metrics and risk profiles.
- **Composable** into concrete implementation plans.

## When to Use

Use this prompt when **at least one** of the following is true:

- You already have a structured problem statement from `Identify.md`.
- You already have a deep analysis from `Analyse.md`.
- You need **concrete options** and **trade-off tables** before deciding or planning.
- The decision has **>5% impact** on a key metric, spans **≥2 stakeholders**, or requires **≥1 month** effort.

---

## LLM Prompt Template: Solution and Architecture Design

> **Usage**: Copy from this line to the end of 【LLM Self-Check】 into the LLM.  
> Fill all 【Input】 placeholders with concrete, quantified content before running.

You are a **solution and architecture design consultant**. Design **2–4 realistic, clearly differentiated options** to solve the problem, explain their structures, and clarify trade-offs so that later decision and implementation are straightforward.

【Input】

1. 【Problem_Summary】  
   - Short title; current state and pain points (with metrics); target state and success criteria (baseline → target → timeline).

2. 【Context_and_Constraints】  
   - Domain/environment/background; hard constraints (budget, deadlines, headcount, compliance, legacy systems); soft preferences (risk appetite, culture, strategic direction).

3. 【Existing_Analysis】 *(optional but recommended)*  
   - Key insights from nine-aspects analysis (definition, origins, trends, capabilities, validation); known root causes and leverage points; key uncertainties and open questions.

4. 【Non_Functional_Requirements】 *(optional)*  
   - Performance, reliability, security, usability, maintainability, compliance, etc.; any explicit SLOs/SLAs or quality thresholds.

5. 【Solution_Space_Constraints】 *(optional)*  
   - Options already ruled out (with reasons); mandatory components or standards; integration or interoperability requirements.

---

【Your Tasks】

1. **Reframe and Stabilise the Problem**  
   - Restate the problem in your own words; clarify what **must** change vs what must **not** change; flag any goal/constraint contradictions.

2. **Propose 2–4 Coherent Options**  
   - For each option, define a clear **concept** and **structure**; make options **meaningfully different** (not cosmetic variants); show how each addresses root causes and leverage points.

3. **Describe Architectures / Operating Models**  
   - For each option: list main components or workstreams; describe how data, control, or value flows between them; note dependencies on people, systems, processes, or vendors; if technical, sketch a simple architecture with clear boundaries; if organisational/process, sketch roles, loops, and checkpoints.

4. **Evaluate Trade-Offs**  
   - Compare options on impact (key metrics), cost (one-off and ongoing), time-to-value, risk (probability × impact), reversibility, and lock-in; highlight **conditions where each option is preferred** vs avoided.

5. **Define Evaluation Metrics and Experiments**  
   - For each option, propose 3–5 key metrics (baseline → target → timeline) and 1–3 small, safe, informative experiments or pilots to test critical uncertainties.

6. **Recommend a Shortlist**  
   - Recommend **1–2 options** for deeper evaluation; list **assumptions** the recommendation depends on and what evidence would most quickly confirm or falsify them.

---

## Answer Structure

Structure your answer as follows:

1. **Context Recap**  
   - Problem summary, current state, target state, key constraints, and non-functional requirements.

2. **Design Principles and Guardrails**  
   - 3–7 guiding principles you will respect (e.g., "prefer reversible steps", "minimise coupling", "optimise for learning speed") and any non-negotiable constraints.

3. **Options Overview Table**

   | Option | One-line description | Main idea | Expected impact | Cost level | Time-to-value | Risk level |
   |--------|----------------------|-----------|-----------------|-----------|---------------|------------|
   | A | … | … | … | … | … | … |
   | B | … | … | … | … | … | … |

4. **Option Details (per option)**  
   For each option, cover:

   - **Name and Positioning**: what this option optimises for and when it is most appropriate.  
   - **Structure / Architecture**: main components or workstreams; simple diagram in text or Mermaid (≤10 nodes); key interfaces and dependencies.  
   - **How It Addresses the Problem**: which root causes or leverage points it targets; expected primary and secondary effects.  
   - **Non-Functional Characteristics**: performance, reliability, security, compliance, maintainability, etc.  
   - **Risks and Failure Modes**: top 3–5 risks, triggers, and mitigations.  
   - **Metrics and Experiments**: 3–5 core metrics (baseline → target → timeline); 1–3 experiments or pilots and what each is testing.

5. **Trade-Off and Comparison**  
   - Compare options across impact, cost, time, risk, reversibility, and alignment with strategy; provide a concise comparison table with brief commentary; highlight **dominant options** and **clearly dominated options**.

6. **Recommendations and Next Steps**  
   - State the recommended shortlist (1–2 options) and rationale; list assumptions or uncertainties that could change the decision; propose next actions (what to prototype or pilot, which additional data to gather, which stakeholders to involve).

---

## LLM Self-Check

Before finalising the answer, verify:

1. **Clarity and Context**
   - ☐ Problem statement is precise, with metrics and constraints.  
   - ☐ Stakeholders and non-functional requirements are covered or explicitly deferred.

2. **Option Quality**
   - ☐ 2–4 **meaningfully different**, internally coherent options.  
   - ☐ Each option clearly addresses identified root causes and leverage points.

3. **Trade-Offs, Risks, and Value**
   - ☐ Trade-offs are explicit (who/what wins or loses, under what conditions).  
   - ☐ Major risks and mitigations are listed, plus at least one **baseline** (e.g., "do nothing / delay" or minimal-change) when relevant.  
   - ☐ Costs, benefits, reversibility, and lock-in are compared across options.

4. **Metrics, Experiments, and Success Criteria**
   - ☐ Key metrics defined with baseline → target → timeline.  
   - ☐ Experiments/pilots are concrete and test high-uncertainty aspects.  
   - ☐ Success criteria make it clear how to judge or iterate on each option.

5. **Actionability and Verification**
   - ☐ Recommendation is explicit (not just "it depends").  
   - ☐ Assumptions that could flip the recommendation are clearly listed.  
   - ☐ Next steps are small enough to be achievable within the stated constraints.  
   - ☐ Quick self-review for contradictions, missing constraints, or unjustified claims.
