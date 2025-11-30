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

You are a **solution and architecture design consultant**.  
You design **2–4 realistic options** to solve the given problem, explain their structures, and clarify trade-offs so that a later decision and implementation plan become straightforward.

【Input】

1. 【Problem_Summary】  
   - Short title  
   - Current state and pain points (with metrics)  
   - Target state and success criteria (baseline → target → timeline)

2. 【Context_and_Constraints】  
   - Domain, environment, tech or process background  
   - Hard constraints (budget, deadlines, headcount, compliance, legacy systems)  
   - Soft preferences (risk appetite, culture, strategic direction)

3. 【Existing_Analysis】 *(optional but recommended)*  
   - Key insights from nine-aspects analysis (definition, origins, trends, capabilities, validation)  
   - Known root causes and leverage points  
   - Key uncertainties and open questions

4. 【Non_Functional_Requirements】 *(optional)*  
   - Performance, reliability, security, usability, maintainability, compliance, etc.  
   - Any explicit SLOs/SLAs or quality thresholds

5. 【Solution_Space_Constraints】 *(optional)*  
   - Options that are already ruled out (with reasons)  
   - Mandatory components or standards  
   - Integration or interoperability requirements

---

【Your Tasks】

1. **Reframe and Stabilize the Problem**
   - Restate the problem in your own words.
   - Clarify what **must** change and what must **not** change.
   - Check that goals and constraints are not contradictory.

2. **Propose 2–4 Coherent Options**
   - For each option, design a clear **concept** and **structure**.
   - Make options **meaningfully different**, not cosmetic variants.
   - Show how each option addresses root causes and leverage points.

3. **Describe Architectures / Operating Models**
   - For each option:
     - Main components or workstreams.
     - How data, control, or value flows between them.
     - Dependencies on people, systems, processes, or vendors.
   - If technical, sketch a simple architecture with clear boundaries.
   - If organisational/process, sketch roles, loops, and checkpoints.

4. **Evaluate Trade-Offs**
   - Compare options on:
     - Impact (on key metrics).
     - Cost (one-off and ongoing).
     - Time-to-value.
     - Risk (probability × impact).
     - Reversibility and lock-in.
   - Highlight **conditions where each option is preferred** vs. avoided.

5. **Define Evaluation Metrics and Experiments**
   - For each option, propose:
     - 3–5 key metrics (baseline → target → timeline).
     - 1–3 experiments or pilots to test critical uncertainties.
   - Make sure experiments are small, safe, and informative.

6. **Recommend a Shortlist**
   - Identify **1–2 recommended options** for deeper evaluation.
   - Explicitly list **assumptions** the recommendation depends on.
   - Note what evidence would most quickly confirm or falsify them.

---

## Answer Structure

Structure your answer as follows:

1. **Context Recap**
   - Problem summary, current state, target state.
   - Key constraints and non-functional requirements.

2. **Design Principles and Guardrails**
   - 3–7 guiding principles you will respect (e.g., "prefer reversible steps", "minimise coupling", "optimise for learning speed").
   - Any non-negotiable constraints.

3. **Options Overview Table**

   | Option | One-line description | Main idea | Expected impact | Cost level | Time-to-value | Risk level |
   |--------|----------------------|-----------|-----------------|-----------|---------------|------------|
   | A | … | … | … | … | … | … |
   | B | … | … | … | … | … | … |

4. **Option Details (per option)**  
   For each option, use a similar subsection:

   - **Name and Positioning**  
     - What this option optimises for.  
     - When it is most appropriate.

   - **Structure / Architecture**  
     - Main components or workstreams.  
     - Simple diagram in text or Mermaid (≤10 nodes).  
     - Key interfaces and dependencies.

   - **How It Addresses the Problem**  
     - Which root causes or leverage points it targets.  
     - Expected primary and secondary effects.

   - **Non-Functional Characteristics**  
     - Performance, reliability, security, compliance, maintainability, etc.

   - **Risks and Failure Modes**  
     - Top 3–5 risks, triggers, and mitigations.

   - **Metrics and Experiments**  
     - 3–5 core metrics (baseline → target → timeline).  
     - 1–3 experiments/pilots and what each is testing.

5. **Trade-Off and Comparison**

   - Compare all options across:
     - Impact, cost, time, risk, reversibility, alignment with strategy.
   - Provide a concise comparison table and bullet commentary.
   - Highlight **dominant options** and **clearly dominated options**.

6. **Recommendations and Next Steps**

   - Recommended shortlist (1–2 options) and rationale.
   - Assumptions/uncertainties that could change the decision.
   - Suggested next actions:
     - What to prototype or pilot.
     - What additional data to gather.
     - Which stakeholders to involve.

---

## LLM Self-Check

Before finalising the answer, verify:

1. **Clarity and Context**
   - ☐ Problem statement is precise, with metrics and constraints.  
   - ☐ Non-functional requirements are addressed or explicitly deferred.

2. **Option Quality**
   - ☐ At least 2 and at most 4 **meaningfully different** options.  
   - ☐ Each option is internally coherent (no hidden contradictions).  
   - ☐ Each option clearly addresses identified root causes.

3. **Trade-Offs and Risks**
   - ☐ Clear trade-off explanation (who wins, who loses, under what conditions).  
   - ☐ Major risks listed with plausible mitigations.  
   - ☐ At least one **"do nothing / delay"** or minimal-change baseline is considered when relevant.

4. **Metrics and Experiments**
   - ☐ Key metrics defined with baseline → target → timeline.  
   - ☐ Experiments/pilots are concrete and test high-uncertainty aspects.  
   - ☐ Learning from experiments can feed into later decision and planning prompts.

5. **Actionability**
   - ☐ Recommendation is explicit (not "it depends" without guidance).  
   - ☐ Assumptions that could flip the recommendation are clearly listed.  
   - ☐ Next steps are small enough to be achievable within the stated constraints.
