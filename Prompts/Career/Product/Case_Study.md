# Case Study Generator - Product Manager

Generate judgment-based PM case studies for senior/director/VP levels testing strategic thinking, prioritization, stakeholder management, and trade-off decisions.

---

## Contents

- [Part I: Specifications](#part-i-specifications)
  - [Scope](#scope)
  - [Users](#users)
  - [Targets](#targets)
  - [Constraints](#constraints)
  - [Scenario Structure](#scenario-structure)
  - [Evidence Standards](#evidence-standards)
  - [Reference Minimums](#reference-minimums)
  - [Quality Gates](#quality-gates)
  - [Validation Checks](#validation-checks)
- [Part II: Instructions](#part-ii-instructions)
  - [1. Plan Topics](#1-plan-topics)
  - [2. Collect References](#2-collect-references)
  - [3. Generate Scenarios](#3-generate-scenarios)
  - [4. Create Rubrics](#4-create-rubrics)
  - [5. Populate References](#5-populate-references)
  - [6. Validate](#6-validate)
  - [7. Submit](#7-submit)
- [Part III: Output Format](#part-iii-output-format)
  - [Structure](#structure)
  - [Templates](#templates)
  - [Example](#example)

---

# Part I: Specifications

## Scope

**In:** Strategy, discovery/validation, prioritization/roadmapping, metrics/growth, stakeholder alignment, GTM.

**Out:** Implementation, design execution, sales tactics, financial modeling, org restructuring.

---

## Users

| Role | Success Criteria |
|------|------------------|
| **LLM** | Meets all quality gates |
| **Hiring Manager** | ≥80% test trade-offs |
| **Candidate** | Clear context, MECE tasks |
| **Evaluator** | <10% scoring variance |

---

## Targets

Generate 16-22 scenarios (20/40/40% F/I/A) testing judgment over recall.

| Metric | Target |
|--------|--------|
| Count | 16-22 |
| Difficulty | 20/40/40% (F/I/A) |
| Citations | ≥70% ≥1; ≥30% ≥2 |
| Languages | 60% EN / 30% ZH / 10% other |
| Recency | ≥50% last 3yr (≥70% AI) |
| Judgment | ≥80% trade-offs |
| Context | 200-400 words |
| MECE | 100% non-overlapping |

---

## Constraints

**Assumptions:** 3-7yr PM experience; knows frameworks (RICE, JTBD, AARRR, OKR); evaluated by PM leaders.

**Limits:** 45-60min/scenario; 200-400 word context; ≤300 word deliverables; accessible URLs; realistic metrics.

**Risks:** Approximated data; outdated tools (>18mo); >25% single-source bias.

---

## Scenario Structure

Each includes:

1. **Difficulty:** F | I | A
2. **Domain:** Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM
3. **Context (200-400w):** Market, users, metrics, stakeholders, constraints, ≥1 [Ref: ID]
4. **Tasks (3-4 MECE):** Objectives, outputs, points (20-30 total), criteria
5. **Rubric:** Partial credit, gaps, bonuses
6. **Trade-Offs (≥1):** Value vs revenue | Short vs long | Build vs buy vs partner | Breadth vs depth | Acquisition vs retention

---

## Evidence Standards

**Format:** APA 7th + language tags [EN/ZH/JP/ES]. Inline: [Ref: ID].

**Flags:**
- `[Evidence: source]` - Verifiable
- `[Assumption: rationale]` - Unverified
- `[Open Question: need]` - Requires research

**Types:** Frameworks (RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST), research, literature (Cagan, Olsen, Torres, Perri, Patton, Klement), tools (Mixpanel, Amplitude, ProductBoard, Dovetail).

---

## Reference Minimums

| Section | Min | Examples |
|---------|-----|----------|
| **Glossary** | ≥10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST |
| **Tools** | ≥5 | Mixpanel, Amplitude, ProductBoard (pricing, users, update, integrations) |
| **Literature** | ≥6 | Cagan, Olsen, Torres, Perri, 俞军, 梁宁 |
| **APA** | ≥12 | 60% EN / 30% ZH / 10% other |

**If unmet:** Document actual, rationale, plan.

---

## Quality Gates

All must pass:

| Gate | Requirement |
|------|-------------|
| **Recency** | ≥50% <3yr (≥70% AI) |
| **Diversity** | ≥3 types; ≤25% single |
| **Evidence** | ≥70% ≥1 cite; ≥30% ≥2 |
| **Links** | All accessible |
| **Cross-refs** | All [Ref: ID] resolve |
| **MECE** | Non-overlapping, complete |
| **Judgment** | ≥80% trade-offs |

**Scaling:** >25 scenarios: 1.5× minimums.

---

## Validation Checks

Execute sequentially. Fix failures before proceeding.

| # | Check | Pass Criteria |
|---|-------|---------------|
| 1 | **Counts** | G≥10, T≥5, L≥6, A≥12, S:16-22 |
| 2 | **Citations** | ≥70% ≥1; ≥30% ≥2 |
| 3 | **Language** | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | **Recency** | ≥50% <3yr (≥70% AI) |
| 5 | **Diversity** | ≥3 types; ≤25% single |
| 6 | **Links** | All accessible |
| 7 | **Cross-refs** | All resolve |
| 8 | **Context** | Sample 5: 200-400w |
| 9 | **MECE** | Non-overlapping |
| 10 | **Rubrics** | All complete |
| 11 | **Judgment** | ≥80% trade-offs |

---

# Part II: Instructions

Execute sequentially. Verify before advancing.

## 1. Plan Topics

Select 4-6 domains, allocate 3-4 scenarios/domain (16-22 total), assign 20/40/40% F/I/A, map trade-offs.

**Verify:** 16-22 ✓ | 20/40/40% ✓ | ≥3/cluster ✓ | Trade-offs ✓

---

## 2. Collect References

Build base: G≥10 (RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST), T≥5 (Mixpanel, Amplitude, ProductBoard + pricing/users/update/integrations), L≥6 (Cagan, Olsen, Torres, Perri, 俞军, 梁宁), A≥12 (IDs, tags).

**Verify:** G≥10, T≥5, L≥6, A≥12 ✓ | 60/30/10% lang ✓ | ≥50% <3yr ✓ | ≥3 types, ≤25% single ✓ | URLs ✓

---

## 3. Generate Scenarios

**Context (200-400w):** Market, users, metrics, stakeholders, constraints, ≥1 [Ref: ID].

**Tasks (3-4 MECE):** (1) Diagnosis+framework (6-10pt), (2) Evaluation+prioritization (8-12pt), (3) Stakeholder comms (4-8pt), (4) Validation (4-8pt, optional).

**Rubrics:** Elements, partial credit, gaps, bonuses.

**Verify (every 3):** 200-400w ✓ | ≥1 cite ✓ | 3-4 MECE ✓ | Rubrics ✓ | ≥1 trade-off ✓

---

## 4. Create Rubrics

Define rubrics (elements, partial credit, 20-30pt), gaps, bonuses (+1-2pt).

**Verify:** All rubrics ✓ | Points sum ✓ | Gaps ✓ | Bonuses ✓

---

## 5. Populate References

**Glossary:** Name, definition, uses.  
**Tools:** Category, pricing, users, update, integrations, URL.  
**Literature:** Author, title, year, publisher, summary.  
**APA:** Full format + tags.

**Verify:** [Ref: ID] resolve ✓ | No orphans ✓ | URLs ✓ | Format ✓

---

## 6. Validate

Execute 11 checks, document, fix, re-run until PASS.

**Verify:** All 11 PASS ✓ | Report ✓ | No failures ✓

---

## 7. Submit

Checklist, TOC+anchors, formatting, review.

**Verify:** 100% checklist ✓ | TOC ✓ | No errors ✓ | Ready ✓

---

# Part III: Output Format

## Structure

**Sections:**
1. **TOC:** H2/H3 anchors
2. **Scenarios:** One H3 each
3. **References:** Glossary, Tools, Literature, APA
4. **Validation:** Check table

**Format:** Markdown, tables, code blocks, bullets, ≤120 chars/line.

---

## Templates

### Scenario

```markdown
### Scenario X: [Title]

**Difficulty:** [F|I|A] | **Domain:** [Strategy|Discovery|Prioritization|Metrics|Stakeholder|GTM]

**Context (200-400w):** [Market, users, metrics, stakeholders, constraints, ≥1 [Ref: ID]]

**Task 1: [Title] (Xpt)**
[Objective]
**Expected:** Element 1, 2, 3
**Grading:** Criterion 1: Ypt, Criterion 2: Zpt

**Task 2-3:** [Repeat]

**Gaps:** Gap 1, 2, 3

**Bonus:** Approach 1: +Xpt, Approach 2: +Ypt
```

### References

```markdown
**Glossary:**
G1. [Framework]: [Definition]. [Uses].

**Tools:**
T1. [Tool] ([Category]): [Description]. [Pricing]. [Users]. Updated [Date]. [URL].

**Literature:**
L1. [Author]. ([Year]). *[Title]*. [Publisher]. [Summary].

**APA:**
A1. [Full APA 7th]. [Tag]
```

### Validation

```markdown
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Languages | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% <3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Context | 5/5 compliant | PASS/FAIL |
| MECE | Y/X verified | PASS/FAIL |
| Rubrics | Y/X complete | PASS/FAIL |
| Judgment | X% trade-offs | PASS/FAIL |

**Status:** [ALL PASS / FAILURES]
**Failures:** [Check]: [Issue] - [Fix]
```

---

## Example

### Scenario 1: Enterprise vs Mass Market Conflict

**Difficulty:** A | **Domain:** Strategy, Prioritization

**Context:**

B2B SaaS: 50K SMB ($50/mo) + 5 enterprise ($200K/yr, 40% ARR). Enterprise wants custom workflow builder (6mo). Vision: simplicity, self-serve [Ref: L4]. Custom adds complexity, needs services.

Analytics [Ref: T1]:
- SMB activation: 65% (7d), retention: 72% (90d)
- Enterprise retention: 95%

CEO: enterprise churn risk ($200-400K) [Assumption]. Engineering: custom delays activation by 2Q. Market [Ref: A8]: SMB TAM 10×, enterprise predictable.

Sales: custom unlocks 10 deals ($2M) [Open Question: close rate?]. Analytics [Ref: T3]: simplified onboarding → 15% activation (+7.5K users, +$450K) [Evidence: Q3 2023 A/B].

**Task 1: Diagnosis+Framework (8pt)**

Apply RICE [Ref: G2] and JTBD [Ref: G3]. What's the strategic tension? Which framework best?

**Expected:** Tension (short-term revenue vs PMF), RICE calcs, JTBD (why custom?), strategy not tactics, opportunity cost [Ref: L3].

**Grading:** Tension: 2pt, RICE: 2pt, JTBD: 2pt, Limitations: 2pt.

**Task 2: Decision Matrix (10pt)**

Evaluate: (1) Enterprise custom, (2) SMB activation, (3) Generalized builder, (4) Hybrid. Recommend.

**Expected:**

| Criterion | Wt | Enterprise | SMB | Generalized | Hybrid |
|-----------|----|-----------|----|-------------|--------|
| Revenue (12mo) | 25% | $2M | $450K | $1M | $1.5M |
| Alignment | 25% | Low | High | High | Med |
| PMF [Ref: G5] | 20% | Neg | Pos | Pos | Neutral |
| Reach | 15% | 5-15 | 50K+ | All | Both |
| Risk | 10% | High | Low | High | Med |
| Moat | 5% | Low | Med | High | Med |

Recommendation addressing CEO, principles.

**Grading:** Criteria: 3pt, 4 options: 3pt, Weighting: 1pt, Clear rec: 2pt, Hybrid: 1pt.

**Task 3: Stakeholder Memo (6pt, ≤300w)**

**Expected:** Situation (request, tension, data), Recommendation (path, timeline), Rationale (criteria, scores), Risk mitigation, Metrics, Next steps.

**Grading:** Structure: 2pt, Data-driven: 2pt, Addresses CEO: 1pt, Actionable: 1pt.

**Gaps:** Binary thinking, mechanical frameworks, ignoring costs, no quantification, no experiments, missing feasibility/alignment.

**Bonus:** JTBD interviews: +2pt, Beta plan: +2pt, Monitoring: +1pt, Churn mitigation: +1pt.

---

**Last Updated:** 2025-11-11
