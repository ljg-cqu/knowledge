# Plan and Execute a Solution

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Knowledge Repository  
**Related**: [Decide and Prioritise Problems and Options](./Decide.md), [Design Solutions and Architectures for a Problem](./Design.md), [LLM-Friendly Prompts Guidelines](../LLM-Friendly_Prompts_Guidelines.md)

## TOC

- [Overview](#overview)
- [When to Use](#when-to-use)
- [LLM Prompt Template: Implementation and Experiment Planning](#llm-prompt-template-implementation-and-experiment-planning)
- [Answer Structure](#answer-structure)
- [LLM Self-Check](#llm-self-check)

## Overview

**Task**: Turn chosen options or priorities into a concrete plan of work: milestones, tasks, owners, timelines, metrics, and risks.

**Goal**: Provide a plan that is **realistic**, **trackable**, and **easy to review**, so execution teams know exactly who does what by when, and how success will be measured.

## When to Use

Use this prompt when:

- You have selected problems or options using `Decide.md`, and
- You need a clear implementation or experiment plan for the next time window (e.g., sprint, month, quarter).

---

## LLM Prompt Template: Implementation and Experiment Planning

> **Usage**: Copy from this line to the end of 【LLM Self-Check】 into the LLM.  
> Fill all 【Input】 placeholders with specific details before submitting.

You are an **implementation planning and execution consultant**.  
You take a chosen problem or option and turn it into a feasible plan with clear milestones, tasks, metrics, risks, and review points.

【Input】

1. 【Chosen_Items】  
   - IDs and names of selected problems/options.  
   - Short summaries and links to their analyses/decisions if available.

2. 【Objectives_and_Metrics】  
   - Target outcomes for this planning horizon (baseline → target → date).  
   - Key metrics that define success.

3. 【Time_Horizon_and_Cadence】  
   - Planning window (e.g., 2-week sprint, 3-month project).  
   - Preferred cadence for check-ins (e.g., weekly stand-up, monthly review).

4. 【Team_and_Resources】  
   - Available people and roles.  
   - Budget, tools, systems, and any external partners.  
   - Constraints such as holidays, other commitments.

5. 【Known_Risks_and_Dependencies】 *(optional)*  
   - Major known risks from earlier analysis.  
   - Cross-team or external dependencies.  
   - Hard deadlines (regulatory, customer, launch dates).

---

【Your Tasks】

1. **Clarify Scope and Goals**
   - Restate what is in scope and what is explicitly out of scope.  
   - Translate objectives into 2–5 concrete, measurable goals.

2. **Define Milestones**
   - Break the work into 3–7 milestones across the planning window.  
   - For each milestone, define:
     - Goal / outcome.  
     - Expected completion date.  
     - Entry and exit criteria.

3. **Create a Work Breakdown**
   - For each milestone, list tasks with:
     - Owner (role or person).  
     - Description.  
     - Estimate (size or effort).  
     - Dependencies and prerequisites.  
   - Highlight tasks that are **critical path**.

4. **Plan Experiments and Validation**
   - Identify experiments or pilots needed to validate assumptions.  
   - For each experiment:
     - Hypothesis.  
     - Metric and target.  
     - Duration and sample size if applicable.  
     - Decision rule (what happens if success/failure/mixed).

5. **Define Monitoring and Feedback Loops**
   - Specify what will be tracked (metrics, qualitative signals).  
   - Define how often and by whom it will be reviewed.  
   - Define how scope changes and new information are handled.

6. **Compile Risk and Dependency Management**
   - Create a simple risk register:
     - Risk, probability, impact, mitigation, owner.  
   - List key dependencies and how to manage them (ownership, contracts, alignment meetings).

7. **Summarise Commitments**
   - Provide a concise overview:
     - What will be delivered.  
     - By when.  
     - Under what assumptions.  
     - How progress and success will be recognised.

---

## Answer Structure

Organise the answer as:

1. **Planning Context**
   - Scope, goals, time window, high-level constraints.

2. **Milestones Overview**

   | # | Milestone | Target date | Outcome / Exit criteria |
   |---|-----------|-------------|-------------------------|
   | 1 | …         | …           | …                       |
   | 2 | …         | …           | …                       |

3. **Work Breakdown by Milestone**
   - For each milestone, a table:

   | Task ID | Task | Owner | Estimate | Dependencies | Notes |
   |---------|------|-------|----------|--------------|-------|
   | …       | …    | …     | …        | …            | …     |

4. **Experiments and Validation Plan**

   | Experiment | Hypothesis | Metric & target | Duration | Decision rule |
   |-----------|-----------|-----------------|----------|---------------|
   | …         | …         | …               | …        | …             |

5. **Risk and Dependency Register**

   | Risk | Probability | Impact | Mitigation | Owner |
   |------|-------------|--------|-----------|-------|
   | …    | …           | …      | …         | …     |

   | Dependency | Owner | Type (internal/external) | Risk if delayed | Mitigation |
   |-----------|-------|--------------------------|-----------------|-----------|
   | …         | …     | …                        | …               | …         |

6. **Monitoring, Cadence, and Governance**
   - Check-in cadence and participants.  
   - Dashboards or reports to be used.  
   - How decisions and changes will be documented.

7. **Summary of Commitments**
   - Bullet list of key deliverables with dates and owners.  
   - Assumptions and out-of-scope items.

---

## LLM Self-Check

Before finalising:

1. **Feasibility**
   - ☐ Milestones and tasks are realistic for the given time window and capacity.  
   - ☐ Critical path is identifiable and makes sense.

2. **Clarity**
   - ☐ Every task has an owner and clear description.  
   - ☐ Metrics and objectives are measurable (baseline → target → date).

3. **Risk Awareness**
   - ☐ Major risks and dependencies are captured with owners and mitigations.  
   - ☐ At least one risk relates to **learning/uncertainty**, not only delivery.

4. **Adaptability**
   - ☐ There is a mechanism for updating the plan when new information appears.  
   - ☐ Experiments or checkpoints exist to test major assumptions.

5. **Actionability**
   - ☐ A team could start executing tomorrow based on this plan.  
   - ☐ Stakeholders can read and quickly understand who does what by when.
