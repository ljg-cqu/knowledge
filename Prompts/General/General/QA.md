# Professional Interview Q&A Generator (Cross-Domain, Multi-Industry)

## Table of Contents
- [Overview](#overview)
- [Scope & MECE Position](#scope--mece-position)
- [Requirements](#requirements)
- [Execution](#execution)
- [Validation Checklist](#validation-checklist)
- [Question Quality](#question-quality)
- [Output Format](#output-format)
- [Essential Domain Tags](#essential-domain-tags)

## Overview

**Problem**: Hiring managers and interview panels cannot practically assess all competency dimensions for each role, which leads to:
- Overly narrow interview loops (e.g., only technical skills or only behavioral questions).
- Missed **decision-critical signals** from other domains (strategic thinking, risk management, stakeholder influence, operational excellence).
- Interviews that overrun the time budget or fail to surface clear hire/no-hire evidence.

**Task**: For a given role and time budget, generate **exactly 6 decision-critical Q&A pairs**, **1 per essential domain**, as a **front-page, cross-domain interview loop**.

**Constraints**:
- Total interview time: **60–90 minutes** (≈10–15 minutes per Q&A).
- Q&As must be **role-specific** (e.g., "Operations Manager", "Financial Analyst", "Clinical Research Lead", "Supply Chain Director").
- Each Q&A must be **scenario-based**, **judgment-heavy**, and **decision-critical** (not recall).

**Inputs (before generation)**:
- Role profile (JD, seniority level, individual contributor vs manager, organizational context).
- Time budget (total minutes for this loop).
- Top 3 decision questions (e.g., "Can they design effective process workflows?", "Can they lead cross-functional initiatives?", "Can they manage stakeholder expectations under constraints?").

**Decision Criticality** (per Q&A, include if ≥1 criterion is satisfied):
1. **Blocks Decision** – Directly impacts hire/no-hire or level decision.
2. **Creates Risk** – Bad hire would cause material loss (e.g., compliance violations, operational failures, financial loss, reputation damage, safety issues).
3. **Affects ≥2 Core Functions** – Multi-stakeholder impact (Operations+Finance, Legal+Business, Clinical+Administrative, etc.).
4. **Requires Action** – Evidence must be collected **now** (1–6 month impact window).
5. **Quantified Impact** – Can be expressed with metrics (cost, revenue, efficiency, quality, satisfaction, risk exposure, time-to-market).

**Success Criteria** (for using this prompt effectively):
- All **6 Q&As** are generated, pass the Validation Checklist, and cover the 6 essential domains without gaps or overlaps.
- The interview loop finishes within the **60–90 minute** time budget while still allowing follow-up questions.
- For each Q&A, the answer key defines clear **strong vs weak signals** so the panel can make or support a **hire/no-hire/level** decision.

---

## Scope & MECE Position

**Audience**: Hiring managers, department heads, functional leads, HR/Recruiting, interview panel owners across all industries.

**Scope**:
- **This file provides a universal framework** for structured professional interviews across any industry.
- It introduces **6 non-overlapping essential domains** that apply to most professional roles.
- For any interview loop, you must create **exactly 1 Q&A per essential domain**, for a total of **6 Q&As**.

**MECE Position**:
- This file provides a **cross-domain, industry-agnostic framework** to:
  - Allocate limited interview time across competency domains.
  - Ensure **balanced coverage** (functional expertise, operational excellence, value delivery, risk management, people & culture, strategic thinking).
  - Enforce a **fixed Q&A count**.
- Every Q&A must:
  - Be tagged with **exactly one EssentialDomainTag** from the [Essential Domain Tags](#essential-domain-tags) table.
  - Be adapted to the specific industry and role context.

**Exclude**:
- Generic/educational questions that could fit any domain but are not decision-critical.
- Q&As that duplicate content from domain files verbatim (this file reframes, it does not copy).
- Loops with more or fewer than **6 Q&As**.

---

## Requirements

### Q&A Count and Coverage

- **Total Q&As**: **6** per interview loop.
- **Domain coverage**: Exactly **1 Q&A for each EssentialDomainTag** in the [table](#essential-domain-tags):
  1. `FuncExpert` – Functional Expertise & Methodology
  2. `OpExcel` – Operational Excellence & Quality
  3. `ValueDel` – Value Delivery & Business Impact
  4. `RiskComp` – Risk Management & Compliance
  5. `PeopleCult` – People & Culture Leadership
  6. `StratVision` – Strategic Vision & Innovation

### Word Count and Time Budget

- **Answer length** (per Q&A, excluding examples/diagrams): **150–250 words**.
- **Time per Q&A**: 10–15 minutes (ask, probing, follow-ups).
- **Total loop**: 60–90 minutes across all 6 Q&As.

### Metadata (Per Q&A)

Each Q&A must provide a one-line metadata row:

- **EssentialDomainTag**: `[FuncExpert|OpExcel|ValueDel|RiskComp|PeopleCult|StratVision]`  
- **CareerStage**: `Entry | Mid | Senior | Lead | Executive`  
- **RoleFocus**: `IC | Manager | Hybrid`  
- **Difficulty**: `F | I | A` (Foundational / Intermediate / Advanced)  
- **Criticality**: `[Blocks | Risk | Functions | Action | Quantified]` (at least one; must align with Decision Criticality criteria above)
- **Stakeholders**: 2–4 primary functions (e.g., Operations, Finance, Legal, HR, Clinical, Business Development)  
- **EstimatedTime**: `~10–15 min`

**Difficulty mix (for all 6 Q&As together)**:
- Approx. **25% F / 50% I / 25% A** (e.g., 1–2 F, 3 I, 1–2 A).

### References

Each Q&A should reference industry-relevant frameworks and methodologies:

- At least **1 reference or framework name** per Q&A (industry standard, methodology, regulatory framework, best practice model, or metric family).
- Examples: Six Sigma, Lean, PMBOK, ISO standards, GAAP, HIPAA, Good Clinical Practice (GCP), McKinsey 7S, Balanced Scorecard, OKRs, etc.

---

## Execution

### 1. Clarify Role and Time Budget

1. Capture role, industry, and level (e.g., "Senior Financial Analyst", "Clinical Operations Manager", "Supply Chain Director").
2. Confirm total interview time (60–90 min) and panel structure.
3. List the **top 3 decision questions** for this hire.

### 2. Map Role to Essential Domains

For each EssentialDomainTag:

- Identify which competencies are most critical for the role and industry context.
- Decide **what signal** you need from that domain (e.g., technical depth, process optimization capability, risk assessment approach, stakeholder management style).

### 3. Draft 1 Q&A per Essential Domain

For each of the 6 domains:

- Write **one decision-critical scenario question** that:
  - Is grounded in the candidate's likely work.
  - Forces them to show judgment, trade-offs, and metrics.
  - Involves at least **2 stakeholders**.
- Write an **answer key** (150–250 words) with:
  - Key insight (what great looks like).
  - Frameworks or tools they might mention.
  - Trade-offs and metrics.
  - Strong vs weak signal notes.

### 4. Check Coverage and Time

- Confirm **all 6 EssentialDomainTags** are represented exactly once.
- Ensure difficulty mix ≈25% F / 50% I / 25% A.
- Ensure total time stays within **60–90 minutes**.

### 5. Run Validation Checklist

Use the [Validation Checklist](#validation-checklist) to ensure the loop is balanced and decision-critical. Fix any failure before use.

---

## Validation Checklist

| Check | Criteria | Status |
|-------|----------|--------|
| **Q&A Count** | Exactly 6 Q&As | ☐ |
| **Domain Coverage** | 1 Q&A per EssentialDomainTag (FuncExpert, OpExcel, ValueDel, RiskComp, PeopleCult, StratVision) | ☐ |
| **Tagging** | Each Q heading starts with `[EssentialDomainTag]` and includes the metadata line | ☐ |
| **Difficulty Mix** | Overall ≈25% F / 50% I / 25% A (1–2 F, 3 I, 1–2 A) | ☐ |
| **Decision Criticality** | 100% Q&As satisfy ≥1 criterion (Blocks/Risk/Functions/Action/Quantified) | ☐ |
| **Stakeholders** | Each Q&A names ≥2 functions; across loop, ≥5 distinct functions | ☐ |
| **Time Budget** | Total estimated time 60–90 min; no Q&A >15 min | ☐ |
| **Signals** | Each Q&A targets a distinct signal (expertise, operations, value, risk, people, strategy) | ☐ |
| **Role Fit** | All Q&As match the JD, industry context, and level (no off-scope questions) | ☐ |
| **Clarity** | All questions are scenario-based, non-ambiguous, non-trivia | ☐ |
| **Self-Contained** | Each Q&A understandable in the specific industry context | ☐ |

**Priority**:
- **Critical checks**: Q&A Count, Domain Coverage, Tagging, Time Budget. If any fail, fix before using the loop.
- **Important checks**: Difficulty Mix, Decision Criticality, Stakeholders, Signals, Role Fit, Clarity, Self-Contained.

---

## Question Quality

**Good (for this file)**:
- **Scenario-based and role-specific**, with clear tension (trade-offs, constraints, conflicting stakeholder priorities).
- **Aligned to one essential domain** (e.g., FuncExpert focuses on methodological judgment, not on team dynamics).
- **Decision-critical**: A strong vs weak answer clearly changes hire/no-hire or level.

**Bad (for this file)**:
- Pure theory or definitions ("What is Six Sigma? Describe leadership styles.").
- Overlapping domains (e.g., a question that is half operations, half strategy, but not clearly tagged).
- Too broad ("Tell me about your career"), or too narrow (simple trivia or recall questions).

---

## Output Format

### Executive Summary

```markdown
**Domain**: Professional Interview (Cross-Domain, Multi-Industry)  
**Role**: [Role title, level]  
**Industry**: [Industry/sector]  
**Time Budget**: [Total minutes, e.g., 75]  
**Coverage**: 6 Q&As (1 per essential domain)

**Key Signals** (1–3 bullets):
- [FuncExpert] Functional depth & methodological judgment → [main signal]
- [OpExcel] Operational efficiency & quality mindset → [main signal]
- [ValueDel] Business value & impact prioritization → [main signal]
- [RiskComp] Risk assessment & compliance thinking → [main signal]
- [PeopleCult] Collaboration & people leadership → [main signal]
- [StratVision] Strategic thinking & innovation capability → [main signal]

**Dashboard**:
| # | EssentialDomainTag | Domain | Difficulty | Criticality | Target Signal | EstimatedTime |
|---|--------------------|--------|------------|-------------|---------------|---------------|
| 1 | FuncExpert  | Functional Expertise & Methodology   | I/A | Blocks     | Domain knowledge & method mastery | ~10–15 min |
| 2 | OpExcel     | Operational Excellence & Quality     | I   | Risk       | Process optimization & quality | ~10–15 min |
| 3 | ValueDel    | Value Delivery & Business Impact     | I   | Functions  | ROI & value prioritization | ~10–15 min |
| 4 | RiskComp    | Risk Management & Compliance         | I/A | Risk       | Risk mitigation & regulatory mindset | ~10–15 min |
| 5 | PeopleCult  | People & Culture Leadership          | F/I | Functions  | Collaboration/leadership style | ~10–15 min |
| 6 | StratVision | Strategic Vision & Innovation        | I/A | Action     | Future-thinking & transformation | ~10–15 min |
```

### Professional Q&A Template

```markdown
### [EssentialDomainTag] Q#: [Scenario Question Title]

**Domain**: [Domain name] | **CareerStage**: [Entry/Mid/Senior/Lead/Executive] | **RoleFocus**: [IC/Manager/Hybrid]  
**Difficulty**: [F/I/A] | **Criticality**: [Blocks/Risk/Functions/Action/Quantified] | **Stakeholders**: [Function1, Function2, (Function3, Function4 optional)] | **EstimatedTime**: ~[10–15] min

**Question (for candidate)**:  
[Decision-critical scenario question, grounded in the candidate's likely work. Include constraints, trade-offs, and at least 2 stakeholder perspectives.]

**Answer Key (~150–250 words)**:  
**Key Insight**: [What a strong answer prioritizes and why; main trade-off or judgment.]  
**Frameworks/Methods**: [1–3 relevant industry standards, methodologies, or tools they might reference (e.g., Lean Six Sigma, PMBOK, ISO standards, GAAP, Balanced Scorecard, OKRs).]  
**Trade-offs & Metrics**: [How strong candidates balance alternatives, quantify impact (cost, time, quality, risk, efficiency, satisfaction, compliance, etc.), and reason about constraints.]  
**Stakeholder Handling**: [How they communicate decisions to Operations/Finance/Legal/Clinical/Leadership, negotiate conflicts, and align expectations across functions.]  
**Signals**:  
- **Strong**: [Concrete, structured, data-driven, acknowledges risks/limitations, considers multiple perspectives.]  
- **Weak**: [Vague, purely theoretical, ignores quantification, or misses key stakeholder concerns.]
```

---

## Essential Domain Tags

Use this table to understand the **6 non-overlapping essential domains** that apply across all professional roles and industries.

| EssentialDomainTag | Domain Name                         | Primary Focus                                     | Cross-Industry Examples |
|--------------------|-------------------------------------|---------------------------------------------------|-------------------------|
| FuncExpert         | Functional Expertise & Methodology  | Core technical/domain knowledge, methodologies, frameworks, best practices | Healthcare: Clinical protocols, diagnostic methods<br>Finance: Financial modeling, valuation techniques<br>Manufacturing: Process engineering, quality standards<br>Legal: Case law research, regulatory interpretation |
| OpExcel            | Operational Excellence & Quality    | Process efficiency, quality control, continuous improvement, measurement | Healthcare: Patient throughput, error reduction<br>Finance: Transaction processing, audit quality<br>Manufacturing: Yield optimization, defect rates<br>Supply Chain: Logistics efficiency, inventory turns |
| ValueDel           | Value Delivery & Business Impact    | ROI, business case development, prioritization, value realization | Healthcare: Patient outcomes, cost per case<br>Finance: Revenue impact, margin improvement<br>Education: Student success metrics, program ROI<br>Retail: Customer lifetime value, conversion rates |
| RiskComp           | Risk Management & Compliance        | Risk identification/mitigation, regulatory compliance, governance, audit | Healthcare: HIPAA, patient safety, malpractice risk<br>Finance: SOX, fraud prevention, credit risk<br>Pharma: FDA compliance, clinical trial safety<br>Manufacturing: OSHA, environmental compliance |
| PeopleCult         | People & Culture Leadership         | Team dynamics, talent development, cross-functional collaboration, culture | All industries: Conflict resolution, stakeholder management<br>Change management, coaching/mentoring<br>Diversity & inclusion, organizational culture<br>Performance management, succession planning |
| StratVision        | Strategic Vision & Innovation       | Long-term planning, trend analysis, transformation, competitive positioning | Healthcare: Digital health adoption, value-based care<br>Finance: Fintech disruption, market expansion<br>Retail: Omnichannel strategy, customer experience<br>Energy: Sustainability transition, technology shifts |

**Rules**:
- Every Q&A in this file must:
  - Start with a heading prefixed by `[EssentialDomainTag]`.
  - Use the corresponding **Domain Name** from this table.
  - Be adapted to the specific industry and role context.
- When designing a loop for a specific role:
  - Use industry-specific frameworks and standards relevant to the role.
  - Keep each Q&A **self-contained** and directly applicable to the target industry.
  - Do **not** create new domains; always map to one of the 6 EssentialDomainTags.
