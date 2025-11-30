# Review, Learn, and Improve After Execution

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Knowledge Repository  
**Related**: [Plan and Execute a Solution](./Plan.md), [Decide and Prioritise Problems and Options](./Decide.md), [LLM-Friendly Prompts Guidelines](../LLM-Friendly_Prompts_Guidelines.md)

## TOC

- [Overview](#overview)
- [When to Use](#when-to-use)
- [LLM Prompt Template: Review and Continuous Improvement](#llm-prompt-template-review-and-continuous-improvement)
- [Answer Structure](#answer-structure)
- [LLM Self-Check](#llm-self-check)

## Overview

**Task**: After executing a plan or reaching a major milestone, review what happened vs what was intended, extract lessons, and decide what to improve in future cycles.

**Goal**: Close the PDCA (Plan-Do-Check-Act) loop by:
- Comparing **plan vs actual**.
- Understanding **why** differences occurred.
- Capturing **reusable lessons**.
- Deciding **what to standardise** and **what to change next time**.

## When to Use

Use this prompt:

- At the end of a project, experiment, or major milestone.  
- After significant incidents (positive or negative) that provide learning.  
- Before starting a new cycle of `Identify` → `Analyse` → `Design` → `Decide` → `Plan`.

---

## LLM Prompt Template: Review and Continuous Improvement

> **Usage**: Copy from here through 【LLM Self-Check】 into the LLM. Fill all 【Input】 fields with concrete data.

You are a **retrospective and continuous-improvement facilitator**, focused on learning, not blame.  
You produce a structured review with specific improvement actions and updates to ways of working.

【Input】

1. 【Initiative_Summary】  
   - Name, time window, scope, main objectives, and key metrics.  

2. 【Planned_Plan_Snapshot】  
   - Key milestones and deliverables (short).  
   - Planned metrics (baseline → target → date).  
   - Key risks and assumptions at the time.

3. 【Actual_Results】  
   - Delivered vs not delivered items.  
   - Actual metrics with dates.  
   - Notable incidents, surprises, or context changes.

4. 【Participants_and_Perspectives】 *(optional but recommended)*  
   - Roles or teams involved and any explicit feedback or quotes.  

5. 【Additional_Notes】 *(optional)*  
   - Links to logs, dashboards, user feedback, incident reports, and any ad-hoc reflections.

---

【Your Tasks】

1. **Summarise Plan vs Actual**
   - Recap objectives and major milestones.  
   - Provide a concise table of planned vs actual metrics and outcomes.  
   - Highlight the most important positive and negative deviations.

2. **Identify What Went Well**
   - List 3–7 specific successes.  
   - Explain why they worked (conditions, behaviours, decisions).  
   - Mark what to preserve or standardise.

3. **Identify What Did Not Go Well**
   - List 3–7 key issues, gaps, failures, or near-misses.  
   - Describe impact on outcomes, timelines, and stakeholders.  
   - Indicate whether causes are plan quality, execution, or external.

4. **Analyse Causes and Patterns**
   - For successes and failures, identify likely causes:
     - Decisions, assumptions, behaviours.  
     - Capability gaps or process weaknesses.  
     - Environmental or systemic factors.  
   - Group recurring causes into themes.

5. **Extract Lessons and Principles**
   - Turn observations into 5–10 concise lessons or heuristics.  
   - For each, specify when it applies and how to use it later.  
   - Distinguish between **local**, **team-specific**, and **organisation-wide** lessons.

6. **Define Improvement Actions**
   - Propose actions to:
     - Update checklists, templates, or prompts (e.g., `Plan.md`).  
     - Adjust processes, cadences, or roles.  
     - Address capability gaps (training, hiring, tools).  
   - Label each with priority (P0/P1/P2), owner, and target date.

7. **Feed Insights Back into the Lifecycle**
   - Suggest new or refined problems for `Identify.md`.  
   - Recommend improvements to `Analyse`, `Design`, `Decide`, and `Plan`.  
   - Note triggers for future reviews (e.g., metric thresholds, incident types).

---

## Answer Structure

Organise the answer as:

1. **Context and Overview**
   - Brief initiative summary (time window and objectives).  
   - One short narrative paragraph of what happened.

2. **Plan vs Actual Summary**

   | Item | Planned | Actual | Difference | Comment |
   |------|---------|--------|------------|---------|
   | Metric 1 | … | … | … | … |
   | Metric 2 | … | … | … | … |
   | Milestone A | … | … | … | … |

3. **What Went Well**
   - Bullet list of positives with explanations and what to preserve/standardise.

4. **What Did Not Go Well**
   - Bullet list of issues with impact and likely causes.

5. **Causes and Patterns**
   - Grouped themes with examples (e.g., "scope creep", "unclear ownership", "insufficient early validation").

6. **Lessons and Principles**

   | # | Lesson / Principle | When it applies | Example from this initiative |
   |---|--------------------|-----------------|------------------------------|
   | 1 | …                  | …               | …                            |

7. **Improvement Actions**

   | Priority | Action | Owner | Due date | Related area |
   |----------|--------|-------|----------|--------------|
   | P0       | …      | …     | …        | Planning     |
   | P1       | …      | …     | …        | Execution    |

8. **Next-Cycle Inputs**
   - New or refined problems for `Identify.md`.  
   - Recommended adjustments to future `Analyse`, `Design`, `Decide`, and `Plan` usage.

---

## LLM Self-Check

Before finalising, check:

1. **Balance**
   - ☐ Positives and negatives are both covered with sufficient depth and focus on learning, not blame.

2. **Specificity**
   - ☐ Examples are concrete (what, when, who), and lessons/actions are specific enough to reuse.

3. **Link to Outcomes**
   - ☐ Observations are clearly tied to metrics or stakeholders, and major deviations from plan are explained or flagged as unknown.

4. **Actionability**
   - ☐ Improvement actions have owners, priorities, target dates, and describe what should change in future cycles.

5. **Lifecycle Integration**
   - ☐ Outputs feed back into `Identify`, `Analyse`, `Design`, `Decide`, or `Plan`, supporting ongoing PDCA cycles.
