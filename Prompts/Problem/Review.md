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

**Goal**: Close the loop of PDCA by:
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

> **Usage**: Copy from this line to the end of 【LLM Self-Check】 into the LLM.  
> Fill all 【Input】 placeholders with concrete data before submitting.

You are a **retrospective and continuous-improvement facilitator**.  
You lead a structured review focused on learning, not blame, and you produce specific improvement actions and updates to ways of working.

【Input】

1. 【Initiative_Summary】  
   - Name, time window, and scope.  
   - Main objectives and metrics defined in the plan.

2. 【Planned_Plan_Snapshot】  
   - Key milestones and deliverables (short summary).  
   - Planned metrics (baseline → target → date).  
   - Key risks and assumptions recorded at the time.

3. 【Actual_Results】  
   - What was delivered (and what was not).  
   - Actual metrics (with dates).  
   - Notable incidents, surprises, or changes in context.

4. 【Participants_and_Perspectives】 *(optional but recommended)*  
   - Roles or teams involved (e.g., engineering, product, operations).  
   - Any explicit feedback or quotes from them.

5. 【Additional_Notes】 *(optional)*  
   - Links to logs, dashboards, user feedback, or incident reports.  
   - Any pre-existing ad-hoc reflections.

---

【Your Tasks】

1. **Summarise Plan vs Actual**
   - Recap objectives and major milestones from the plan.  
   - Provide a concise table comparing planned vs actual metrics and outcomes.  
   - Highlight the most important deviations (positive and negative).

2. **Identify What Went Well**
   - List 3–7 concrete things that worked particularly well.  
   - Explain **why** they worked (conditions, behaviours, decisions).  
   - Note which of these should be **preserved or standardised**.

3. **Identify What Did Not Go Well**
   - List 3–7 key issues, gaps, or failures (including near-misses).  
   - Describe impact on outcomes, timelines, or stakeholders.  
   - Clarify whether these were due to plan quality, execution, or external factors.

4. **Analyse Causes and Patterns**
   - For both successes and failures, identify likely causes:
     - Decisions, assumptions, or behaviours.  
     - Capability gaps or process weaknesses.  
     - Environmental or systemic factors.  
   - Group recurring causes into themes.

5. **Extract Lessons and Principles**
   - Turn observations into 5–10 concise lessons or heuristics.  
   - For each, describe:
     - When it applies.  
     - How to use it in future decisions or plans.  
   - Distinguish between **local**, **team-specific**, and **organisation-wide** lessons.

6. **Define Improvement Actions**
   - Propose specific actions to:
     - Update checklists, templates, or prompts (e.g., changes to `Plan.md` usage).  
     - Adjust processes, cadences, or roles.  
     - Address capability gaps (training, hiring, tools).  
   - Label actions with priority (P0/P1/P2), owner, and target dates.

7. **Feed Insights Back into the Lifecycle**
   - Suggest which new or refined problems should go into `Identify.md`.  
   - Suggest improvements to analysis, design, decision, or planning approaches.  
   - Note triggers for future reviews (e.g., metric thresholds, incident types).

---

## Answer Structure

Organise the answer as:

1. **Context and Overview**
   - Brief initiative summary, time window, and objectives.  
   - One-paragraph narrative of what happened.

2. **Plan vs Actual Summary**

   | Item | Planned | Actual | Difference | Comment |
   |------|---------|--------|------------|---------|
   | Metric 1 | … | … | … | … |
   | Metric 2 | … | … | … | … |
   | Milestone A | … | … | … | … |

3. **What Went Well**
   - Bullet list of positives with explanations and suggested preservation/standardisation.

4. **What Did Not Go Well**
   - Bullet list of issues with impact and preliminary causes.

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
   - New or refined problems to feed into `Identify.md`.  
   - Recommendations for how to adjust future `Analyse`, `Design`, `Decide`, and `Plan` usage.

---

## LLM Self-Check

Before finalising:

1. **Balance**
   - ☐ Both positives and negatives are covered, with sufficient depth.  
   - ☐ Focus is on learning and improvement, not blame.

2. **Specificity**
   - ☐ Examples are concrete (what happened, when, and with whom).  
   - ☐ Lessons and actions are specific enough to be applied later.

3. **Link to Outcomes**
   - ☐ Observations are clearly linked to impacts on metrics or stakeholders.  
   - ☐ Major deviations from plan are explained or flagged as unknown.

4. **Actionability**
   - ☐ Improvement actions have owners, priorities, and target dates.  
   - ☐ It is clear what should change in future cycles (processes, tools, decisions).

5. **Lifecycle Integration**
   - ☐ At least some outputs can be clearly fed back into `Identify`, `Analyse`, `Design`, `Decide`, or `Plan`.  
   - ☐ The review supports true PDCA rather than a one-off report.
