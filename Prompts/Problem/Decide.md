# Decide and Prioritise Problems and Options

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Knowledge Repository  
**Related**: [Extract Problem Statements](./Identify.md), [Nine Aspects for Analyzing Problems](./Analyse.md), [Design Solutions and Architectures for a Problem](./Design.md), [LLM-Friendly Prompts Guidelines](../LLM-Friendly_Prompts_Guidelines.md)

## TOC

- [Overview](#overview)
- [When to Use](#when-to-use)
- [LLM Prompt Template: Decision and Prioritisation](#llm-prompt-template-decision-and-prioritisation)
- [Answer Structure](#answer-structure)
- [LLM Self-Check](#llm-self-check)

## Overview

**Task**: Help choose **which problems or options to tackle first**, and document a clear decision log: what was chosen, why, under which assumptions, and what is deferred.

**Goal**: Turn a long list of possible work into a **small set of committed priorities** aligned with impact, risk, and capacity.

## When to Use

Use this prompt when:

- You have **multiple problems** extracted via `Identify.md`, or
- You have **multiple solution options** from `Design.md` for one problem, and
- You need a **transparent, reviewable decision** rather than ad-hoc choices.

---

## LLM Prompt Template: Decision and Prioritisation

> **Usage**: Copy from this line to the end of 【LLM Self-Check】 into the LLM.  
> Fill all 【Input】 placeholders with concrete values before submitting.

You are a **decision and prioritisation consultant**.  
You help rank problems or solution options using simple, explicit criteria, and you create a concise decision log that stakeholders can review and refine.

【Input】

1. 【Decision_Scope】  
   - Are we prioritising **problems**, **solutions for one problem**, or a **mixed portfolio**?  
   - Time horizon for this decision (e.g., next 2 weeks / quarter / year).

2. 【Candidate_List】  
   - Table of items with at least:  
     - ID or short name  
     - One-line description  
     - Expected impact (qualitative or rough quantitative)  
     - Rough effort / cost estimate  
     - Risk level (and main risks)  
     - Time-criticality (deadlines, windows of opportunity)  
     - Key dependencies

3. 【Context_and_Strategy】  
   - Organisational or personal goals relevant to this decision.  
   - Strategic themes or guardrails (e.g., "reduce risk first", "grow revenue", "stabilise platform").  
   - Capacity constraints (budget, people, time).

4. 【Additional_Information】 *(optional)*  
   - Existing analyses (`Analyse.md`) or designs (`Design.md`) for some items.  
   - Hard constraints (must-do items, regulatory deadlines).  
   - Items that cannot be chosen now (with reasons).

---

【Your Tasks】

1. **Clarify Decision Objective and Constraints**
   - Restate the decision scope in concrete terms.  
   - Clarify what **success** looks like for this decision (e.g., "select 3–5 P0 items for next quarter").  
   - Summarise hard constraints (budget, people, timing).

2. **Define a Simple Scoring Model**
   - Choose 3–5 criteria such as:
     - Impact (on key metrics).
     - Effort/cost.
     - Risk reduction.
     - Time-criticality.
     - Strategic alignment.  
   - Explain how each criterion is scored (e.g., 1–5 scale; higher is better or worse).  
   - Optionally assign weights to criteria (e.g., impact 40%, risk 30%, effort 30%).

3. **Score Each Item**
   - For every candidate:
     - Provide criterion scores with 1–2 bullet justifications each.  
     - Compute a simple aggregate score (e.g., weighted sum or ICE-like formula).  
   - Call out items whose scores are highly uncertain and why.

4. **Create a Prioritised List**
   - Sort items by aggregate score and judgement.  
   - Group items into priority tiers:
     - 【P0 - Critical】: must do in this horizon.  
     - 【P1 - Important】: should do if capacity allows.  
     - 【P2 - Optional】: nice-to-have or speculative.  
   - Show which items **fit within current capacity** and which are **beyond** it.

5. **Document the Decision and Assumptions**
   - For each P0 item:
     - Short rationale (impact, risk, timing).  
     - Dependencies and obvious blockers.  
   - For deprioritised items:
     - Reasons (low impact, high effort, timing, low confidence, etc.).  
   - List key **assumptions** that, if changed, would warrant revisiting the decision.

6. **Suggest Next Steps**
   - For the selected P0/P1 items:
     - Point to what should happen next (e.g., "Run `Plan.md` to create implementation plan").  
   - For high-uncertainty but high-potential items:
     - Suggest small experiments or discovery work to clarify their value.

---

## Answer Structure

Organise your answer as:

1. **Decision Context**
   - Scope of decision, time horizon, main goals.  
   - Summary of constraints and capacity.

2. **Criteria and Scoring Model**
   - List criteria, definitions, and directions (higher = better/worse).  
   - Any weights or tie-breaking rules.

3. **Scored Item Table**

   | ID | Name | Impact | Effort | Risk | Time-criticality | Alignment | Total Score | Notes |
   |----|------|--------|--------|------|------------------|----------|-------------|-------|
   | …  | …    | …      | …      | …    | …                | …        | …           | …     |

4. **Prioritised List and Tiers**
   - Items grouped into P0 / P1 / P2, with brief rationale.  
   - Capacity line: which items are realistically feasible in this horizon.

5. **Decision Log**
   - Bullet-point summary of:
     - What was decided.  
     - Why these items were selected or deferred.  
     - Major risks or regrets.  
     - Key assumptions and review triggers.

6. **Recommendations and Next Steps**
   - Immediate actions for P0 items (e.g., "Create plan using `Plan.md`").  
   - When and how to revisit this prioritisation (e.g., after new data, quarterly).

---

## LLM Self-Check

Before finalising:

1. **Clarity**
   - ☐ Decision scope and time horizon are explicit.  
   - ☐ Criteria are clearly defined and understandable to non-experts.

2. **Transparency**
   - ☐ Every item has visible scores and short justifications.  
   - ☐ Priority tiers (P0/P1/P2) follow logically from scores and constraints.

3. **80/20 Focus**
   - ☐ Top ~20% of items clearly account for most of the expected value.  
   - ☐ Some lower-value or low-confidence items are explicitly deferred.

4. **Robustness**
   - ☐ Key assumptions that could flip the decision are listed.  
   - ☐ There is a simple plan for when to revisit the decision.

5. **Actionability**
   - ☐ It is obvious which items should move into detailed planning (`Plan.md`).  
   - ☐ Stakeholders can read this decision log and quickly understand the why.
