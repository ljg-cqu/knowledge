# Case Study Generator - Product Manager

Generate product case study assessments with multi-dimensional evaluation, structured reasoning, and evidence-based decision-making for senior/director/VP Product Managers.

---

## Contents

- [Part I: Specifications](#part-i-specifications)
  - [Purpose and Scope](#purpose-and-scope)
  - [Users and Stakeholders](#users-and-stakeholders)
  - [Goals and Success Metrics](#goals-and-success-metrics)
  - [Assumptions and Constraints](#assumptions-and-constraints)
  - [Scenario Structure Requirements](#scenario-structure-requirements)
  - [Citation and Evidence Standards](#citation-and-evidence-standards)
  - [Reference Requirements](#reference-requirements)
  - [Quality Gates](#quality-gates)
  - [Pre-Submission Validation](#pre-submission-validation)
  - [Submission Checklist](#submission-checklist)
- [Part II: Instructions](#part-ii-instructions)
  - [Step 1: Topic Planning](#step-1-topic-planning)
  - [Step 2: Reference Collection](#step-2-reference-collection)
  - [Step 3: Scenario Generation](#step-3-scenario-generation)
  - [Step 4: Grading Framework](#step-4-grading-framework)
  - [Step 5: References](#step-5-references)
  - [Step 6: Validation](#step-6-validation)
  - [Step 7: Submission](#step-7-submission)
- [Part III: Output Format](#part-iii-output-format)
  - [Document Structure](#document-structure)
  - [Scenario Template](#scenario-template)
  - [Reference Sections Template](#reference-sections-template)
  - [Validation Report Template](#validation-report-template)
  - [Example Scenario](#example-scenario)

---

# Part I: Specifications

## Purpose and Scope

Generate realistic, judgment-based product management scenarios assessing strategic thinking, prioritization, stakeholder management, and decision-making under constraints for senior/director/VP PM candidates.

**In Scope:** Product strategy, discovery/validation, prioritization/roadmapping, metrics/growth, stakeholder alignment, GTM planning.

**Out of Scope:** Implementation details, design execution, sales tactics, complex financial modeling, organizational restructuring.

---

## Users and Stakeholders

| Role | Needs | Success Criteria |
|------|-------|------------------|
| **LLM Generator** | Clear instructions, templates, validation steps | Produces scenario bank meeting all quality gates |
| **Hiring Manager** | Realistic scenarios testing judgment over recall | ≥80% scenarios require trade-off analysis |
| **Candidate (PM)** | Clear context, MECE tasks, fair evaluation | Understands scenario constraints and expectations |
| **Evaluator/Grader** | Detailed rubrics, partial-credit guidance | Can consistently score with <10% variance |

---

## Goals and Success Metrics

Generate 16-22 scenarios (20% Foundational / 40% Intermediate / 40% Advanced) testing product judgment over framework recall.

| Metric | Target |
|--------|--------|
| Scenario count | 16-22 |
| Difficulty | 20/40/40% (F/I/A) |
| Citations | ≥70% with ≥1; ≥30% with ≥2 |
| Languages | 60% EN / 30% ZH / 10% other |
| Recency | ≥50% last 3yr (≥70% AI/platform) |
| Judgment focus | ≥80% require trade-offs |
| Context length | 200-400 words |
| MECE tasks | 100% non-overlapping |

---

## Assumptions and Constraints

**Assumptions:** Candidates have 3-7 years PM experience; understand frameworks (RICE, JTBD, AARRR, OKR); evaluated by experienced PM leaders.

**Constraints:** 45-60 min/scenario; 200-400 word context; ≤300 word deliverables; accessible URLs/DOIs required; realistic synthetic metrics.

**Risk Flags:** Market data may be approximated; outdated tools (>18mo) reduce relevance; >25% single-source creates bias.

---

## Scenario Structure Requirements

Each scenario must include:

1. **Difficulty:** Foundational | Intermediate | Advanced
2. **Domain:** Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM
3. **Context (200-400 words):** Market landscape, user segments, business metrics, stakeholder positions, constraints, ≥1 citation [Ref: ID]
4. **Tasks (3-4 MECE):** Clear objectives, expected outputs, point allocation (20-30 pts total), evaluation criteria
5. **Grading Rubric:** Partial-credit breakdown, common gaps, bonus opportunities
6. **Trade-Offs (≥1):** User value vs revenue | Short vs long-term | Build vs buy vs partner | Breadth vs depth | Acquisition vs retention

---

## Citation and Evidence Standards

**Format:** APA 7th with language tags [EN], [ZH], [JP], [ES]. Inline: [Ref: ID].

**Evidence Flags:**
- `[Evidence: source]` - Verifiable claim
- `[Assumption: rationale]` - Unverified assumption
- `[Open Question: validation need]` - Requires research

**Source Types:** Frameworks (RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST), research (market/user/competitive), literature (Cagan, Olsen, Torres, Perri, Patton, Klement), tools (Mixpanel, Amplitude, ProductBoard, Dovetail).

---

## Reference Requirements

| Section | Minimum | Examples |
|---------|---------|----------|
| **Glossary** | ≥10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, Feature Factory, Continuous Discovery |
| **Tools** | ≥5 | Mixpanel, Amplitude, ProductBoard, Aha!, Dovetail (with pricing, users, update date, integrations) |
| **Literature** | ≥6 | Cagan, Olsen, Torres, Perri, Patton, Klement, 俞军, 梁宁 |
| **APA Citations** | ≥12 | ~60% EN / ~30% ZH / ~10% other |

**If minimums unmet:** Document actual vs target, rationale, sourcing plan.

---

## Quality Gates

All must pass before submission:

| Gate | Requirement |
|------|-------------|
| **Recency** | ≥50% last 3yr (≥70% AI/platform) |
| **Diversity** | ≥3 types; max 25% single source |
| **Evidence** | ≥70% with ≥1 citation; ≥30% with ≥2 |
| **Links** | All URLs accessible/archived |
| **Cross-refs** | All [Ref: ID] resolve |
| **MECE** | Tasks non-overlapping, complete |
| **Judgment** | ≥80% test trade-offs vs recall |

**Scaling:** For >25 scenarios, increase floors by 1.5×.

---

## Pre-Submission Validation

Execute all 11 checks sequentially. Fix failures before proceeding.

| # | Check | Requirement |
|---|-------|-------------|
| 1 | **Counts** | G≥10, T≥5, L≥6, A≥12, S:16-22 |
| 2 | **Citations** | ≥70% with ≥1; ≥30% with ≥2 |
| 3 | **Language** | EN 50-70%, ZH 20-40%, Other 5-15% |
| 4 | **Recency** | ≥50% last 3yr (≥70% AI/platform) |
| 5 | **Diversity** | ≥3 types; max 25% single source |
| 6 | **Links** | All accessible/archived |
| 7 | **Cross-refs** | All [Ref: ID] resolve |
| 8 | **Context** | Sample 5: all 200-400 words |
| 9 | **MECE** | Tasks non-overlapping, complete |
| 10 | **Rubrics** | All have grading + points |
| 11 | **Judgment** | ≥80% test judgment vs recall |

---

## Submission Checklist

- [ ] All 11 validation checks PASS
- [ ] Reference floors met (G≥10, T≥5, L≥6, A≥12)
- [ ] Quality gates satisfied
- [ ] Difficulty: 20/40/40% (F/I/A)
- [ ] Languages: ~60/30/10% (EN/ZH/Other)
- [ ] All [Ref: ID] resolve
- [ ] Context: 200-400 words
- [ ] Rubrics complete
- [ ] Trade-offs in ≥80%
- [ ] TOC with anchor links
- [ ] Validation report complete

---

# Part II: Instructions

Execute steps sequentially. Verify completion criteria before advancing.

## Step 1: Topic Planning

Define balanced scenario distribution: Select 4-6 domains (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM), allocate 3-4 scenarios per domain (16-22 total), assign difficulty (20/40/40% F/I/A), map trade-off types.

**Verify:** Count 16-22 ✓ | Difficulty 20/40/40% ✓ | ≥3 per cluster ✓ | Trade-offs distributed ✓

---

## Step 2: Reference Collection

Build diverse reference base: Glossary ≥10 (RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST), Tools ≥5 (Mixpanel, Amplitude, ProductBoard, Dovetail with pricing/users/updates/integrations), Literature ≥6 (Cagan, Olsen, Torres, Perri, 俞军, 梁宁), APA ≥12 (stable IDs, language tags).

**Verify:** Counts G≥10, T≥5, L≥6, A≥12 ✓ | Languages 60/30/10% ✓ | Recency ≥50% last 3yr ✓ | Diversity ≥3 types, max 25% single ✓ | URLs accessible ✓

---

## Step 3: Scenario Generation

Write context (200-400 words): market landscape, user segments, business metrics, stakeholder positions, constraints, ≥1 [Ref: ID].

Design 3-4 MECE tasks: (1) Problem diagnosis + framework (6-10 pts), (2) Option evaluation + prioritization (8-12 pts), (3) Stakeholder communication (4-8 pts), (4) Validation plan (4-8 pts optional).

Create rubrics: expected elements, partial credit, common gaps, bonus approaches.

**Verify (every 3):** Context 200-400 words ✓ | ≥1 citation ✓ | 3-4 MECE tasks ✓ | Rubrics complete ✓ | ≥1 trade-off ✓

---

## Step 4: Grading Framework

Define per-task rubrics (expected elements, partial credit, 20-30 pts total), document common gaps, define bonus approaches (+1-2 pts).

**Verify:** All rubrics ✓ | Points sum correctly ✓ | Gaps documented ✓ | Bonuses specified ✓

---

## Step 5: References

Populate sections: Glossary (name, definition, use cases), Tools (category, pricing, users, update, integrations, URL), Literature (author, title, year, publisher, summary), APA Citations (full format with language tags).

**Verify:** All [Ref: ID] resolve ✓ | No orphans ✓ | URLs functional ✓ | Format consistent ✓

---

## Step 6: Validation

Execute 11 checks from Pre-Submission Validation, document results, fix failures, re-run until all PASS.

**Verify:** All 11 PASS ✓ | Report complete ✓ | No failures ✓

---

## Step 7: Submission

Complete checklist, generate TOC with anchors, review formatting, final read-through.

**Verify:** Checklist 100% ✓ | TOC functional ✓ | No format errors ✓ | Ready ✓

---

# Part III: Output Format

## Document Structure

**Required Sections:**
1. **TOC:** Anchor links to all H2/H3
2. **Scenario Bank:** One H3 per scenario
3. **References:** Glossary, Tools, Literature, APA Citations
4. **Validation Report:** Check results table

**Format:** GitHub Markdown, tables for data, fenced code blocks with language tags, bullet lists, lines ≤120 chars.

---

## Scenario Template

```markdown
### Scenario X: [Title]

**Difficulty:** [F|I|A] | **Domain:** [Strategy|Discovery|Prioritization|Metrics|Stakeholder|GTM]

**Context:** (200-400 words) [Market, users, metrics, stakeholders, constraints, ≥1 [Ref: ID]]

**Task 1: [Title] (X pts)**
[Objective]
**Expected:** Element 1, Element 2, Element 3
**Grading:** Criterion 1: Y pts, Criterion 2: Z pts

**Task 2-3:** [Repeat structure]

**Common Gaps:** Gap 1, Gap 2, Gap 3

**Bonus:** Approach 1: +X pts, Approach 2: +Y pts
```

---

## Reference Sections Template

```markdown
**Glossary:**
G1. [Framework]: [Definition]. [Use cases]. [Related].

**Tools:**
T1. [Tool] ([Category]): [Description]. [Pricing]. [Users]. Updated [Date]. [URL].

**Literature:**
L1. [Author]. ([Year]). *[Title]*. [Publisher]. [Summary].

**APA Citations:**
A1. [Full APA 7th]. [Language Tag]
```

---

## Validation Report Template

```markdown
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W S:N (F/I/A) | PASS/FAIL |
| Citations | X% ≥1, Y% ≥2 | PASS/FAIL |
| Languages | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
| Context | 5/5 compliant | PASS/FAIL |
| MECE | Y/X verified | PASS/FAIL |
| Rubrics | Y/X complete | PASS/FAIL |
| Judgment | X% judgment-based | PASS/FAIL |

**Status:** [ALL PASS / FAILURES]
**Failures:** [Check]: [Description] - [Remediation]
```

---

## Example Scenario

### Scenario 1: Enterprise vs Mass Market Feature Conflict

**Difficulty:** Advanced | **Domain:** Product Strategy, Prioritization

**Context:**

B2B SaaS productivity tool: 50K SMB users ($50/mo avg) + 5 enterprise clients ($200K/yr, 40% ARR). Top enterprise clients request sophisticated custom workflow builder (6mo build).

Product vision: simplicity, self-serve onboarding for mass market. Research [Ref: L4] shows SMBs value ease + quick time-to-value [Ref: G8]. Custom workflow adds UI complexity, requires professional services.

Analytics [Ref: T1] data:
- SMB activation: 65% (core feature within 7d)
- SMB retention (90d): 72%
- Enterprise retention: 95%
- Top 3 features: 80%+ SMB adoption

CEO concerned about enterprise churn [Assumption: Loss of 1-2 enterprise clients = $200-400K ARR impact]. Engineering: custom workflow delays activation improvements by 2Q. Market analysis [Ref: A8]: SMB TAM 10× enterprise, but enterprise more predictable.

Sales: custom feature unlocks 10 enterprise deals ($2M ARR potential) [Open Question: What's the close rate and timeline?]. Analytics [Ref: T3]: simplified onboarding improves SMB activation 15% (+7.5K users, +$450K ARR) [Evidence: A/B test from Q3 2023].

**Task 1: Problem Diagnosis & Framework Application (8 pts)**

Apply RICE [Ref: G2] and JTBD [Ref: G3] to analyze both options. What is the core strategic tension? Which framework reveals it best?

**Expected:**
- Strategic tension identified: short-term revenue vs long-term PMF/scalability
- RICE analysis for both options with actual numbers from context
- JTBD analysis: What job do enterprise customers need done? Why custom vs generalized?
- Recognition that this is a strategy decision, not just prioritization
- Acknowledgment of opportunity cost and product principles [Ref: L3]

**Grading:**
- Strategic tension articulated (not just tactical choice): 2 pts
- RICE calculations with context data: 2 pts
- JTBD to uncover underlying needs: 2 pts
- Recognition of framework limitations and strategic nature: 2 pts

**Task 2: Prioritization & Decision Matrix (10 pts)**

Evaluate four options: (1) Enterprise custom workflow, (2) SMB activation improvements, (3) Generalized workflow builder, (4) Hybrid approach (partner/services layer). Recommend with rationale.

**Expected:**

| Criterion | Weight | Enterprise Custom | SMB Activation | Generalized Builder | Hybrid |
|-----------|--------|-------------------|----------------|---------------------|--------|
| Revenue impact (12mo) | 25% | $2M | $450K | $1M | $1.5M |
| Strategic alignment | 25% | Low (custom) | High (self-serve) | High | Medium |
| PMF impact [Ref: G5] | 20% | Negative (complexity) | Positive (easier onboarding) | Positive | Neutral |
| Reach (users affected) | 15% | 5-15 enterprise | 50K+ SMB | All | Both |
| Execution risk | 10% | High (complexity) | Low (known) | High (scope) | Medium |
| Competitive moat | 5% | Low (replicable) | Medium | High | Medium |

Recommendation with clear rationale addressing CEO concerns and product principles.

**Grading:**
- Comprehensive criteria (revenue/strategy/PMF/reach/risk): 3 pts
- All four options evaluated (not binary thinking): 3 pts
- Appropriate weighting: 1 pt
- Clear recommendation addressing stakeholders: 2 pts
- Consideration of hybrid/3rd options: 1 pt

**Task 3: Stakeholder Communication (6 pts)**

Draft memo (≤300 words) to CEO and exec team.

**Expected:**
- Situation: Enterprise request, strategic tension, data summary
- Recommendation: Specific path forward with timeline
- Rationale: Decision criteria, scores, why this serves business best
- Risk mitigation: How to protect enterprise relationship
- Success metrics: How you'll measure if decision was right
- Next steps: Immediate actions, timeline, check-in points

**Grading:**
- Clarity and structure (exec-friendly format): 2 pts
- Data-driven reasoning (metrics, not opinions): 2 pts
- Addresses CEO concerns (enterprise worry): 1 pt
- Actionable next steps (clear path forward): 1 pt

**Common Product Judgment Gaps:**
- Binary thinking (enterprise OR SMB) vs exploring generalized/hybrid options
- Mechanical framework application without strategic context
- Ignoring opportunity costs
- Not quantifying impact with available data
- No experiments/validation before full commitment
- Overlooking execution feasibility
- Missing stakeholder alignment plan

**Exemplary Approaches for Bonus:**
- Discovery interviews to validate enterprise JTBD before deciding: +2 pts
- A/B test or beta plan for generalized builder to de-risk: +2 pts
- Monitoring plan with leading indicators (activation, enterprise NPS): +1 pt
- Specific mitigation strategy for enterprise churn risk: +1 pt

---

**Last Updated:** 2025-11-11
