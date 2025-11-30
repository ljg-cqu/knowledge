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

**Task**: Choose **which problems or options to tackle first** and document a decision log: what was chosen, why, assumptions, and what is deferred.

**Goal**: Turn many possible items into a **short list of committed priorities** aligned with impact, risk, and capacity.

## When to Use

Use this prompt when:

- Have **multiple problems** from `Identify.md`, or
- Have **multiple solution options** from `Design.md` for one problem, and
- Need a **transparent, reviewable prioritisation** instead of ad-hoc choices.

---

## LLM Prompt Template: Decision and Prioritisation

> **Usage**: Copy from here to the end of 【LLM Self-Check】 into the LLM. Fill all 【Input】 fields before sending.

You are a **decision and prioritisation consultant**. Rank items using explicit criteria and produce a short, reviewable decision log.

【Input】

1. 【Decision_Scope】  
   - What is being prioritised: **problems**, **solutions for one problem**, or a **portfolio**?  
   - Decision time horizon (e.g., next 2 weeks / quarter / year) and review cadence.

2. 【Candidate_List】  
   - Table of items with:  
     - ID or short name; one-line description  
     - Expected impact on key metrics (e.g., revenue %, risk, cost)  
     - Rough effort / cost (size, people, or budget)  
     - Risk level and main risks  
     - Time-criticality (deadlines, windows)  
     - Key dependencies or prerequisites  
     - Current baseline for main metric(s) (if known)

3. 【Context_and_Strategy】  
   - Goals this decision should serve (organisational or personal).  
   - Strategic themes or guardrails (e.g., "reduce risk first", "grow revenue", "stabilise platform").  
   - Capacity constraints (budget, people, time) and any must-hit targets (e.g., OKRs).

4. 【Additional_Information】 *(optional)*  
   - Extracts from prior analyses or designs (e.g., from `Analyse.md` or `Design.md`).  
   - Hard constraints (must-do items, regulatory deadlines).  
   - Items that cannot be chosen now and why (e.g., missing data, blocked dependency).

---

【Your Tasks】

1. **Clarify Decision Objective and Constraints**
   - Restate the decision scope and time horizon.  
   - Define success in measurable terms (e.g., "select 3–5 P0 items for next quarter" with target metrics).  
   - Summarise hard constraints (budget, people, timing, mandatory items).

2. **Define a Simple Scoring Model**
   - Pick 3–5 non-overlapping criteria for value, cost, risk, timing, and alignment (e.g., impact, effort/cost, risk reduction, time-criticality, strategic alignment).  
   - State the scale and direction for each (e.g., 1–5, higher = better).  
   - Optionally assign weights (e.g., impact 40%, risk 30%, effort 30%).

3. **Score Each Item**
   - For each candidate, assign criterion scores with 1–2 short justifications and compute an aggregate score (e.g., weighted sum or ICE-like formula).  
   - Flag items with low data quality or high uncertainty.

4. **Create a Prioritised List**
   - Sort items by score and judgement.  
   - Group into tiers:
     - 【P0 - Critical】: must do in this horizon.  
     - 【P1 - Important】: should do if capacity allows.  
     - 【P2 - Optional】: nice-to-have or speculative.  
   - Mark which items fit within current capacity and which are beyond it.

5. **Document Decision, Trade-offs, and Assumptions**
   - For each P0 item: brief rationale (impact, risk, timing) plus key dependencies/blockers.  
   - For deprioritised items: reasons (e.g., lower value, higher effort, timing, low confidence).  
   - Make trade-offs explicit between top alternatives (cost, benefit, risk).  
   - List assumptions that would trigger revisiting the decision if they change.

6. **Suggest Next Steps**
   - For selected P0/P1 items: next actions (e.g., create implementation plan, owners, and rough start date).  
   - For high-uncertainty but high-potential items: small experiments or discovery work to clarify value.

---

## Answer Structure

Answer structure:

1. **Decision Context**
   - Scope, time horizon, goals, and main stakeholders.  
   - Constraints, capacity, and any must-do items.

2. **Criteria and Scoring Model**
   - List criteria, definitions, and directions (higher = better/worse).  
   - Any weights or tie-breaking rules.

3. **Scored Item Table**

   | ID | Name | Impact | Effort | Risk | Time-criticality | Alignment | Total Score | Notes |
   |----|------|--------|--------|------|------------------|----------|-------------|-------|
   | …  | …    | …      | …      | …    | …                | …        | …           | …     |

4. **Prioritised List and Tiers**
   - Items grouped into P0 / P1 / P2 with brief rationale and key trade-offs.  
   - Capacity line: which items fit in this horizon vs are deferred.

5. **Decision Log**
   - Bullet summary of: decisions, reasons, major risks, assumptions, and when to revisit.

6. **Recommendations and Next Steps**
   - Immediate actions for P0 items.  
   - When and how to revisit this prioritisation (e.g., after new data, regular cadence).

---

## LLM Self-Check

Before finalising, check:

1. **Clarity**
   - ☐ Decision scope, time horizon, success metrics, and capacity limits are explicit.  
   - ☐ Criteria are clearly defined and understandable to non-experts.

2. **Transparency**
   - ☐ Every item has visible scores and short justifications.  
   - ☐ Priority tiers (P0/P1/P2) follow logically from scores, constraints, and stated trade-offs.

3. **Focus**
   - ☐ Top ~20% of items capture most expected value; lower-value or low-confidence items are explicitly deferred.  
   - ☐ Major risks and downsides of the recommended set are stated.

4. **Robustness and Fairness**
   - ☐ Key assumptions that could flip the decision are listed, with when to revisit.  
   - ☐ No important stakeholder or criterion is ignored without explanation; obvious biases are called out.

5. **Actionability and Evidence**
   - ☐ It is obvious which items should move into detailed planning and what happens first.  
   - ☐ Any critical numbers or facts are based on the provided data; uncertainties are flagged instead of invented.
