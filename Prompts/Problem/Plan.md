# Plan and Execute a Solution

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Knowledge Repository  
**Related**: [Decide and Prioritise Problems and Options](./Decide.md), [Design Solutions and Architectures for a Problem](./Design.md), [LLM-Friendly Prompts Guidelines](../LLM-Friendly_Prompts_Guidelines.md)

## TOC

- [Overview](#overview)
- [When to Use](#when-to-use)
- [LLM Prompt Template](#llm-prompt-template)
- [Answer Structure](#answer-structure)
- [LLM Self-Check](#llm-self-check)

## Overview

**Task**: Turn chosen options into a concrete execution or experiment plan (milestones, tasks, owners, timelines, metrics, risks).  

**Goal**: Produce a realistic, trackable plan so everyone knows who does what by when, and how success will be measured.

## When to Use

Use this prompt when:

- You have selected problems or options (see `Decide.md`).  
- You need an implementation or experiment plan for the next time window (e.g., sprint, month, quarter).

---

## LLM Prompt Template

> **Usage**: Copy from this line to the end of "LLM Self-Check" into the LLM.  
> Replace every 【Input】 placeholder with specific details before submitting. Do not rely on previous chat messages for context.

You are an **implementation planning and execution consultant**.  
You turn chosen options into a feasible plan with clear milestones, tasks, metrics, risks, and review points.

【Input】

1. 【Chosen_Items】  
   - IDs, names, and 1–2 sentence summaries of selected problems/options.  
   - Links to their analyses/decisions, plus a short recap of key conclusions inline.

2. 【Objectives_and_Metrics】  
   - Target outcomes for this planning horizon (baseline → target → date, with units).  
   - 3–7 key metrics that define success.

3. 【Time_Horizon_and_Cadence】  
   - Planning window (e.g., 2-week sprint, 3-month project).  
   - Preferred cadence for check-ins (e.g., weekly stand-up, monthly review).

4. 【Team_and_Resources】  
   - Available people and roles; approximate capacity if known.  
   - Budget, tools, systems, and any external partners.  
   - Constraints such as holidays, other commitments, or legal/compliance limits.

5. 【Known_Risks_and_Dependencies】 *(optional)*  
   - Major known risks and assumptions from earlier analysis.  
   - Cross-team or external dependencies and hard deadlines (regulatory, customer, launch).

---

【Your Tasks】

1. **Clarify Scope and Goals**  
   - Restate what is in scope and explicitly out of scope.  
   - Translate objectives into 2–5 measurable goals (baseline → target → date).

2. **Define Milestones**  
   - Break the work into 3–7 milestones across the planning window.  
   - For each milestone, define outcome, target completion date, and entry/exit criteria.

3. **Create a Work Breakdown**  
   - For each milestone, list tasks with owner (role/person), short description, estimate, and dependencies.  
   - Highlight critical-path tasks and any blocking dependencies.

4. **Plan Experiments and Validation**  
   - Identify experiments or pilots needed to validate key assumptions or compare options.  
   - For each experiment: hypothesis, metric and target, duration and sample size (if applicable), and decision rule (what happens on success/failure/mixed).

5. **Define Monitoring and Feedback Loops**  
   - Specify what will be tracked (metrics and qualitative signals) and where (dashboards/reports).  
   - Define how often and by whom progress is reviewed, and how scope changes or new information update the plan.

6. **Compile Risk, Dependencies, and Commitments**  
   - Create a simple risk register: risk, probability, impact, mitigation, owner.  
   - List key dependencies and how to manage them (owner, agreements, alignment meetings).  
   - Summarise commitments: what will be delivered, by when, under what assumptions, and how progress and success will be recognised.

---

## Answer Structure

Organise the answer as:

1. **Planning Context**  
   - Scope, goals, time window, major constraints and assumptions.

2. **Milestones Overview**

   | # | Milestone | Target date | Outcome / Exit criteria |
   |---|-----------|-------------|-------------------------|
   | 1 | …         | …           | …                       |
   | 2 | …         | …           | …                       |

3. **Work Breakdown by Milestone**  
   - For each milestone, a table:

   | Task ID | Task | Owner | Estimate | Dependencies | Priority (C/I/O) | Notes |
   |---------|------|-------|----------|--------------|------------------|-------|
   | …       | …    | …     | …        | …            | …                | …     |

4. **Experiments and Validation Plan**

   | Experiment | Hypothesis | Metric & target | Duration | Decision rule |
   |-----------|------------|-----------------|----------|---------------|
   | …         | …          | …               | …        | …             |

5. **Risk and Dependency Register**

   | Risk | Probability | Impact | Mitigation | Owner |
   |------|-------------|--------|-----------|-------|
   | …    | …           | …      | …         | …     |

   | Dependency | Owner | Type (internal/external) | Risk if delayed | Mitigation |
   |-----------|-------|--------------------------|-----------------|-----------|
   | …         | …     | …                        | …               | …         |

6. **Monitoring, Cadence, and Governance**  
   - Check-in cadence, attendees, and where progress is tracked (dashboards, reports).  
   - How decisions and changes will be documented and communicated.

7. **Summary of Commitments**  
   - Bullet list of key deliverables with dates and owners.  
   - Assumptions and out-of-scope items.

---

## LLM Self-Check

Before finalising, quickly verify:

1. **Feasibility**  
   - ☐ Milestones and tasks are realistic for the given time window and team capacity.  
   - ☐ The critical path is explicit and makes sense.

2. **Clarity and Precision**  
   - ☐ Every task has an owner and a short, concrete description.  
   - ☐ Metrics and objectives have baseline → target → date and clear units.

3. **Risk and Dependencies**  
   - ☐ Major risks, assumptions, and dependencies have owners and mitigations.  
   - ☐ At least one risk relates to learning/uncertainty, not only delivery.

4. **Monitoring and Adaptability**  
   - ☐ There is a clear review cadence and a place to see the metrics (dashboard/report).  
   - ☐ Experiments or checkpoints test major assumptions and can trigger updates to the plan.

5. **Actionability and Priority**  
   - ☐ A team could start executing tomorrow based on this plan.  
   - ☐ Critical vs important vs optional items are clearly distinguishable, and the plan is concise (no redundant sections).
