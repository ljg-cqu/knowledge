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

**Goal**: Produce a realistic, trackable plan: who does what, by when, and how success is measured.

## When to Use

Use this prompt when:

- You have selected problems or options.  
- You need an implementation or experiment plan for the next sprint/month/quarter.

---

## LLM Prompt Template

> **Usage**: Copy from this line through "LLM Self-Check" into the LLM.  
> Replace every 【Input】 placeholder with concrete details before submitting. The message must be self-contained; do not rely on previous chat history.

You are an **implementation planning and execution consultant**. Turn chosen options into a feasible plan with clear milestones, tasks, metrics, risks, and review points.

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
   - Available people/roles and approximate capacity.  
   - Budget, tools/systems, external partners, and key constraints (holidays, other commitments, legal/compliance).

5. 【Known_Risks_and_Dependencies】 *(optional)*  
   - Major known risks and assumptions from earlier analysis.  
   - Cross-team or external dependencies and hard deadlines (regulatory, customer, launch).

---

【Your Tasks】

Optimise for actionability and concision; prefer tables and bullets over long prose.

1. **Clarify Scope and Goals**  
   - Restate what is in scope and explicitly out of scope.  
   - Translate objectives into 2–5 measurable goals (baseline → target → date).

2. **Define Milestones**  
   - Break the work into 3–7 milestones across the planning window.  
   - For each milestone, define outcome, target completion date, and entry/exit criteria.

3. **Create a Work Breakdown**  
   - For each milestone, list tasks with owner (role/person), short description, estimate, dependencies, and priority (Critical/Important/Optional).  
   - Highlight critical-path tasks and any blocking dependencies.

4. **Plan Experiments and Validation**  
   - Identify experiments or pilots needed to validate key assumptions or compare options.  
   - For each experiment: hypothesis, metric and target, duration and sample size (if applicable), and decision rule (what happens on success/failure/mixed).

5. **Define Monitoring and Feedback Loops**  
   - Specify what will be tracked (metrics and qualitative signals) and where (dashboards/reports).  
   - Define how often and by whom progress is reviewed, and how scope changes or new information update the plan.

6. **Compile Risk, Dependencies, and Commitments**  
   - Create a risk register: risk, probability, impact, mitigation, owner.  
   - List key dependencies and how to manage them (owner, agreements, alignment meetings).  
   - Summarise commitments: what will be delivered, by when, under which assumptions, and how progress and success will be tracked.

---

## Answer Structure

Organise the answer as (sections 1–4 are mandatory; 5–7 as needed). Keep it concise: use bullets and tables; avoid repeating information across sections.

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

   - C/I/O = Critical / Important / Optional.

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
   - ☐ The plan is self-contained and understandable without previous chat context.  
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
   - ☐ Critical vs important vs optional items are clearly distinguishable.  
   - ☐ The plan primarily uses tables/bullets; prose is concise with no redundant sections.
