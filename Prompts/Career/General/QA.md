# Career Interview General Q&A Generator (Cross-Domain Front Page)

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

**Problem**: Hiring managers and interview panels cannot practically read or apply all **18 Career Q&A generators** for each role, which leads to:
- Overly narrow interview loops (e.g., only architecture or only coding).
- Missed **decision-critical signals** from other domains (value, security, organization, roadmap).
- Interviews that overrun the time budget or fail to surface clear hire/no-hire evidence.

**Task**: For a given role and time budget, generate **exactly 6 decision-critical Q&A pairs**, **1 per essential domain**, as a **front-page, cross-domain interview loop**.

**Constraints**:
- Total interview time: **60–90 minutes** (≈10–15 minutes per Q&A).
- Q&As must be **role-specific** (e.g., "Senior Backend", "MPC Wallet Architect", "Head of Platform").
- Each Q&A must be **scenario-based**, **judgment-heavy**, and **decision-critical** (not recall).

**Inputs (before generation)**:
- Role profile (JD, level, IC vs manager, team context).
- Time budget (total minutes for this loop).
- Top 3 decision questions (e.g., "Can they design secure MPC protocols?", "Can they lead cross-team initiatives?").

**Decision Criticality** (per Q&A, include if ≥1 criterion is satisfied):
1. **Blocks Decision** – Directly impacts hire/no-hire or level decision.
2. **Creates Risk** – Bad hire would cause material loss (e.g., security, cost, morale, roadmap).
3. **Affects ≥2 Core Roles** – Multi-stakeholder impact (Architect+Dev, PM+Security, Lead+HR, etc.).
4. **Requires Action** – Evidence must be collected **now** (1–6 month impact window).
5. **Quantified Impact** – Can be expressed with metrics (latency, revenue, risk, velocity, attrition, cost).

---

## Scope & MECE Position

**Audience**: Hiring managers, tech leads, architects, PMs, HR/Recruiting, interview panel owners.

**Scope**:
- **This file is an aggregator** over the existing 18 Career Q&A generators.
- It introduces **6 non-overlapping essential domains**, each of which groups several Career files.
- For any interview loop, you must create **exactly 1 Q&A per essential domain**, for a total of **6 Q&As**.

**MECE Position**:
- This file does **not** replace or redefine the 18 Career Q&A generators.
- It provides a **cross-domain front page** to:
  - Allocate limited interview time across domains.
  - Ensure **balanced coverage** (technical, value, risk, organization, strategy).
  - Enforce a **fixed Q&A count**.
- Every Q&A must:
  - Be tagged with **exactly one EssentialDomainTag** from the [Essential Domain Tags](#essential-domain-tags) table.
  - Respect the **boundaries and intent** of the underlying Career files mapped to that domain.

**Exclude**:
- Generic/educational questions that could fit any domain but are not decision-critical.
- Q&As that duplicate content from domain files verbatim (this file reframes, it does not copy).
- Loops with more or fewer than **6 Q&As**.

---

## Requirements

### Q&A Count and Coverage

- **Total Q&As**: **6** per interview loop.
- **Domain coverage**: Exactly **1 Q&A for each EssentialDomainTag** in the [table](#essential-domain-tags):
  1. `TechArch` – Technical Architecture & Design
  2. `PerfQual` – Performance & Quality Engineering
  3. `ProdBiz` – Product & Business Value
  4. `SecReg` – Security & Regulation
  5. `OrgLead` – Organization & Leadership
  6. `RoadmapEco` – Roadmap & Ecosystem Strategy

### Word Count and Time Budget

- **Answer length** (per Q&A, excluding examples/diagrams): **150–250 words**.
- **Time per Q&A**: 10–15 minutes (ask, probing, follow-ups).
- **Total loop**: 60–90 minutes across all 6 Q&As.

### Metadata (Per Q&A)

Each Q&A must provide a one-line metadata row:

- **EssentialDomainTag**: `[TechArch|PerfQual|ProdBiz|SecReg|OrgLead|RoadmapEco]`  
- **CareerStage**: `Junior | Mid | Senior | Lead | Architect`  
- **RoleFocus**: `IC | Manager | Mixed`  
- **Difficulty**: `F | I | A` (Foundational / Intermediate / Advanced)  
- **Stakeholders**: 2–4 primary roles (e.g., Architect, PM, SRE, Security, HR)  
- **EstimatedTime**: `~10–15 min`

**Difficulty mix (for all 6 Q&As together)**:
- Approx. **25% F / 50% I / 25% A** (e.g., 1–2 F, 3 I, 1–2 A).

### References

This aggregator may **reuse references and frameworks** from the 18 Career files, but each Q&A here must still be self-contained:

- At least **1 reference or framework name** per Q&A (book, standard, method, tool, or metric family).
- No strict citation floor here; the detailed references live in the domain files.

---

## Execution

### 1. Clarify Role and Time Budget

1. Capture role and level (e.g., "Senior Backend", "Staff MPC Wallet Engineer").
2. Confirm total interview time (60–90 min) and panel structure.
3. List the **top 3 decision questions** for this hire.

### 2. Map Role to Essential Domains

For each EssentialDomainTag:

- Identify which underlying Career files are most relevant (see [Essential Domain Tags](#essential-domain-tags)).
- Decide **what signal** you need from that domain (e.g., architectural judgment, performance trade-offs, risk appetite, leadership style).

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
| **Domain Coverage** | 1 Q&A per EssentialDomainTag (TechArch, PerfQual, ProdBiz, SecReg, OrgLead, RoadmapEco) | ☐ |
| **Difficulty Mix** | Overall ≈25% F / 50% I / 25% A (1–2 F, 3 I, 1–2 A) | ☐ |
| **Decision Criticality** | 100% Q&As satisfy ≥1 criterion (Blocks/Risk/Roles/Action/Quantified) | ☐ |
| **Stakeholders** | Each Q&A names ≥2 roles; across loop, ≥5 distinct roles | ☐ |
| **Time Budget** | Total estimated time 60–90 min; no Q&A >15 min | ☐ |
| **Signals** | Each Q&A targets a distinct signal (architecture, performance, value, risk, org, roadmap) | ☐ |
| **Role Fit** | All Q&As match the JD and level (no off-scope questions) | ☐ |
| **Clarity** | All questions are scenario-based, non-ambiguous, non-trivia | ☐ |
| **Self-Contained** | Each Q&A understandable without opening domain files | ☐ |

---

## Question Quality

**Good (for this file)**:
- **Scenario-based and role-specific**, with clear tension (trade-offs, constraints, conflicting stakeholders).
- **Aligned to one essential domain** (e.g., TechArch focuses on architecture judgment, not on compensation).
- **Decision-critical**: A strong vs weak answer clearly changes hire/no-hire or level.

**Bad (for this file)**:
- Pure theory or definitions ("What is CQRS? Describe patterns of leadership.").
- Overlapping domains (e.g., a question that is half architecture, half org, but not clearly tagged).
- Too broad ("Tell me about your career"), or too narrow (simple coding puzzle).

---

## Output Format

### Executive Summary

```markdown
**Domain**: Career (Cross-Domain Interview Front Page)  
**Role**: [Role title, level]  
**Time Budget**: [Total minutes, e.g., 75]  
**Coverage**: 6 Q&As (1 per essential domain)

**Key Signals** (1–3 bullets):
- [TechArch] Structural & design judgment → [main signal]
- [PerfQual] Performance/quality trade-offs → [main signal]
- [ProdBiz] Value & prioritization → [main signal]
- [SecReg] Security/compliance risk thinking → [main signal]
- [OrgLead] Collaboration/leadership → [main signal]
- [RoadmapEco] Long-term roadmap & ecosystem thinking → [main signal]

**Dashboard**:
| # | EssentialDomainTag | Domain | Difficulty | Target Signal | EstimatedTime |
|---|--------------------|--------|------------|---------------|---------------|
| 1 | TechArch   | Technical Architecture & Design      | I/A | System & API design judgment | ~10–15 min |
| 2 | PerfQual   | Performance & Quality Engineering    | I   | Performance/quality trade-offs | ~10–15 min |
| 3 | ProdBiz    | Product & Business Value             | I   | Value & prioritization judgment | ~10–15 min |
| 4 | SecReg     | Security & Regulation                | I/A | Threat, risk, compliance mindset | ~10–15 min |
| 5 | OrgLead    | Organization & Leadership            | F/I | Collaboration/leadership style | ~10–15 min |
| 6 | RoadmapEco | Roadmap & Ecosystem Strategy         | I/A | Long-term thinking & evolution | ~10–15 min |
```

### General Career Q&A Template

```markdown
### [EssentialDomainTag] Q#: [Scenario Question Title]

**Domain**: [Domain name] | **CareerStage**: [Junior/Mid/Senior/Lead/Architect] | **RoleFocus**: [IC/Manager/Mixed]  
**Difficulty**: [F/I/A] | **Stakeholders**: [Role1, Role2, (Role3, Role4 optional)] | **EstimatedTime**: ~[10–15] min

**Question (for candidate)**:  
[Decision-critical scenario question, grounded in the candidate's likely work. Include constraints, trade-offs, and at least 2 stakeholder perspectives.]

**Answer Key (~150–250 words)**:  
**Key Insight**: [What a strong answer prioritizes and why; main trade-off or judgment.]  
**Frameworks/Tools**: [1–3 relevant methods, patterns, or tools they might reference (e.g., ADRs, DORA metrics, STRIDE, WSJF, Team Topologies).]  
**Trade-offs & Metrics**: [How strong candidates balance alternatives, quantify impact (latency, cost, risk, velocity, NPS, etc.), and reason about constraints.]  
**Stakeholder Handling**: [How they communicate decisions to Architect/PM/SRE/Security/Leadership, negotiate conflicts, and align expectations.]  
**Signals**:  
- **Strong**: [Concrete, structured, metric-aware, acknowledges risks/limits.]  
- **Weak**: [Vague, purely theoretical, ignores metrics, or misses key stakeholders.]
```

---

## Essential Domain Tags

Use this table to understand the **6 non-overlapping essential domains** and how they group the 18 existing Career Q&A generators.

| EssentialDomainTag | Domain Name                         | Primary Focus                                     | Mapped Career Files (examples) |
|--------------------|-------------------------------------|---------------------------------------------------|---------------------------------|
| TechArch           | Technical Architecture & Design     | System structure, patterns, protocols, constraints| Architecture/QA.md, Pattern/QA.md, Protocol/QA.md, Constrain/QA.md |
| PerfQual           | Performance & Quality Engineering   | Performance, scalability, reliability, data & tests| Performance/QA.md, Quality/QA.md, Statistics/QA.md, CaseStudy/QA.md |
| ProdBiz            | Product & Business Value            | Business models, product strategy, value trade-offs| Business/QA.md, Product/QA.md, Value/QA.md |
| SecReg             | Security & Regulation               | Security engineering, threats, compliance, audits | Security/QA.md, Regulation/QA.md |
| OrgLead            | Organization & Leadership           | Team structure, leadership, collaboration         | Leadership/QA.md, Organization/QA.md, Collaboration/QA.md |
| RoadmapEco         | Roadmap & Ecosystem Strategy        | Technology evolution, standards, ecosystem integration | Roadmap/QA.md, Ecosystem/QA.md |

**Rules**:
- Every Q&A in this file must:
  - Start with a heading prefixed by `[EssentialDomainTag]`.
  - Use the corresponding **Domain Name** from this table.
- When designing a loop for a specific role:
  - Use the mapped Career files as **inspiration and structure**, but keep each Q&A here **self-contained**.
  - Do **not** create new domains; always map to one of the 6 EssentialDomainTags.
