# Short Answer Framework – Product Manager

Generate PM assessments for senior/director/VP Product Managers (2–5 years SaaS/platform/B2B/B2C experience).

**Scope:**
- 25–40 problems across 6 domains: Strategy, Discovery & Validation, Prioritization & Roadmapping, Metrics & Growth, Stakeholder Management, Go-to-Market
- Multi-source citations: ~60% EN, ~30% ZH, ~10% other
- Partial credit for methodology/judgment

---

# Part I: Specifications

## Problem Specifications

**Count:** 25–40 | **Difficulty:** 20% F / 40% I / 40% A (±5%)
- F: Core frameworks (AARRR, RICE)
- I: Trade-offs, cross-functional scenarios
- A: Strategic decisions, multi-stakeholder conflicts, ambiguity

**Domains (4–8 each):**
1. Strategy: Vision, positioning, market
2. Discovery: Research, testing, PMF
3. Prioritization: RICE, ICE, backlog
4. Metrics: North Star, AARRR, retention
5. Stakeholder: Alignment, conflict resolution
6. GTM: Launch, PLG, enablement

**Format:**
- Prompt: 2–3 sentences (context + question)
- Answer: 2–4 steps + citations [Ref: G#/T#/L#/A#]
- Solution: Reasoning + methodology + alternatives/trade-offs

**Grading:** Correctness 40% | Reasoning 30% | Practicality 20% | Completeness 10%

## Reference Requirements

**Minimums:**
| Type | Min | Examples |
|------|-----|----------|
| Glossary (G#) | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, Continuous Discovery |
| Tools (T#) | 5 | Mixpanel, ProductBoard, Dovetail, Miro, Optimizely |
| Literature (L#) | 6 | Cagan, Olsen, Torres, Perri, 俞军, 梁宁 (≥4 Western, ≥2 Eastern) |
| APA (A#) | 12 | APA 7th + language tags: ~60% EN, ~30% ZH, ~10% other |

**Scaling:** 41–60: 1.5× | 61+: 2×
**Exceptions:** Document shortfall + rationale + plan (e.g., "Tools: 4/5. Adding Split.io")

## Citation Standards

**Language:** EN 50–70% | ZH 20–40% | Other 5–15% + tags [EN]/[ZH]/[JA]/[KO]/[DE]. Romanize non-Latin.

**Source Types (≥3 of 4, max 25%):**
1. Frameworks (RICE, JTBD, OKR, PLG)
2. Research/Data (studies, benchmarks, reports)
3. Literature (Cagan, Torres, 俞军, 梁宁, papers)
4. Tools (Mixpanel, ProductBoard, Dovetail)

**Format:** APA 7th
- Required: Author, Year, *Title*, Publisher, DOI/URL, [Tag]
- Inline: [Ref: G#/T#/L#/A#]
- Example: "Apply RICE [Ref: G2, T2, A2]"

**Coverage:**
- ≥70% problems cite ≥1 ref; ≥30% cite ≥2+ refs
- DOI > URL > archived
- All [Ref: ID] resolve to Part III

## Quality Gates

1. **Recency:** ≥50% last 3yr (≥70% AI/platform). Flag >10yr.
2. **Diversity:** ≥3/4 types; none >25%.
3. **Evidence:** ≥70% cite ≥1 ref; ≥30% cite ≥2+ refs. Advanced need ≥2.
4. **Tool Metadata:** Pricing, XK+ companies (2–3 clients), update ≤18mo, integrations (3–5), PM use (2–3), HTTPS.
5. **Links:** DOI > URL > archived. Test all; flag "[Archived: DATE]".
6. **Cross-refs:** All [Ref: ID] resolve. No orphans. ≥80% entries cited ≥1 problem.

## Success Criteria

**Mandatory:**
| Criterion | Spec | Check |
|-----------|------|-------|
| References | G≥10, T≥5, L≥6, A≥12 | Count |
| Problems | 25–40 | Count |
| Difficulty | 20%F/40%I/40%A (±5%) | Calculate |
| Language | EN 50–70%, ZH 20–40%, Other 5–15% | Count tags |
| Quality gates | All 6 PASS | Run |
| Report | All PASS | Template |

**Performance:**
- Avg ≥1.5 citations/problem
- ≥8 distinct frameworks
- ≥90% include metrics/tools/data
- ≥25% mention trade-offs/alternatives

---

# Part II: Workflow

Execute sequentially with inline checks.

## Step 1: Plan Distribution

**Goal:** Balanced 25–40 problems across 6 domains (MECE).

1. Allocate 4–8 per domain (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM).
2. Assign 20%F/40%I/40%A: F=frameworks/definitions, I=trade-offs/scenarios, A=strategic/conflicts/ambiguity.
3. **Check:** [ ] Count 25–40 [ ] Difficulty 20/40/40 (±5%) [ ] Each 4–8 [ ] No gaps/overlaps

## Step 2: Collect References

**Goal:** Diverse, authoritative, current references.

1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST. Format: **G#. Term** – Definition. Used for: [contexts]. Related: [terms].
2. **Tools (≥5)**: Mixpanel, ProductBoard, Dovetail, Miro, Optimizely. Format: **T#. Tool** (Category) – Description. Pricing. XK+ users (clients). Updated [DATE]. Integrates: [platforms]. PM use: [cases]. [URL].
3. **Literature (≥6, ≥4 West, ≥2 East)**: Cagan, Olsen, Torres, Perri, 俞军, 梁宁. Format: **L#. Author. (Year). *Title*. Publisher.** – Contribution. Use cases.
4. **APA (≥12)**: APA 7th + tags [EN]/[ZH]/[JA]. Romanize non-Latin. Format: **A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**.
5. **Check:** [ ] G≥10, T≥5 (≥3 cat), L≥6 (≥4W, ≥2E), A≥12 [ ] Lang EN 50–70%, ZH 20–40%, Other 5–15% [ ] ≥50% last 3yr [ ] ≥3/4 types, none >25% [ ] Tool metadata complete [ ] Links tested

## Step 3: Generate Problems

**Goal:** Structured, evidence-based PM problems.

**Per problem:**
1. **Prompt (2–3 sent)**: Context (scenario + constraints) + frameworks/metrics + question. Avoid vagueness/jargon/multiple questions.
2. **Answer (2–4 steps)**: Actionable + [Ref: G#/T#/L#/A#]. User-centric, data-driven, iterative.
3. **Solution (4–8 sent)**: Reasoning + citations. Flow: Problem → Framework → Application → Validation → Outcome. I/A: alternatives + trade-offs. A: flag misconceptions.
4. **Check (every 5):** [ ] Prompt 2–3 sent, clear [ ] Answer 2–4 steps, cite ≥1 [ ] ≥70% cite ≥1, ≥30% cite ≥2+ [ ] Solution 4–8 sent, trade-offs (I/A), alternatives (A) [ ] Consistent terms [ ] Aligns domain + difficulty [ ] Coherent logic

## Step 4: Populate References

**Goal:** Formatted references supporting all citations.

1. **G#**: **G#. Term** – Definition. Used for: [contexts]. Related: [terms]. ≥10, all 6 domains.
2. **T#**: **T#. Tool** (Category) – Description. Pricing. XK+ users (clients). Updated [DATE]. Integrates: [platforms]. PM use: [cases]. [URL]. ≥5, ≥3 cat, ≤18mo, test links.
3. **L#**: **L#. Author. (Year). *Title*. Publisher.** – Contribution. Use cases. ≥6 (≥4W, ≥2E).
4. **A#**: **A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**. Romanize. ≥12, ~60%EN/~30%ZH/~10%other, ≥50% last 3yr, test links.
5. **Check:** [ ] All [Ref: ID] resolve [ ] ≥80% entries cited ≥1 [ ] Consistent G#/T#/L#/A# [ ] Tool metadata complete [ ] Links tested/archived

## Step 5: Validate & Submit

**Goal:** Verify specs, gates, criteria.

**7 Checks:**
1. Counts: G≥10, T≥5, L≥6, A≥12, P=25–40, 20/40/40 (±5%)
2. Citation: ≥70% cite ≥1; ≥30% cite ≥2+
3. Language: EN 50–70%, ZH 20–40%, Other 5–15%
4. Recency: ≥50% last 3yr (≥70% AI/platform)
5. Diversity: ≥3/4 types, none >25%
6. Links: All accessible/archived
7. Cross-refs: All resolve; ≥80% cited

**Report:**
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
| Citation | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |

**If FAIL:** Stop. Document (check, expected vs actual, cause). Fix. Re-run. Repeat until 7/7 PASS.
**Submit:** 7/7 PASS + report + format match + metadata complete + links tested.

---

# Part III: Output Template

## Validation Report
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
| Citation | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |

## Contents
- [Problems](#problems-1-n)
- [References](#references): [Glossary](#glossary) | [Tools](#tools) | [Literature](#literature) | [APA](#apa-citations)

---

## Problems (1–N)

### Problem X
**Diff:** [F/I/A] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Prompt:** (2–3 sent: context + question)

**Answer:** (2–4 steps + [Ref: ID])

**Solution:** (4–8 sent: reasoning + citations + alternatives/trade-offs + misconceptions if A)

---

## References

### Glossary
**G#. Term** – Definition. Used: [contexts]. Related: [terms].
**Ex:** **G1. RICE** – Reach × Impact × Confidence ÷ Effort. Used: roadmap, backlog. Related: ICE, KANO.
[≥10, all 6 domains]

### Tools
**T#. Tool** (Category) – Description. Pricing. XK+ (clients). Updated [Q# YYYY]. Integrates: [platforms]. PM use: [cases]. [URL]
**Ex:** **T1. Mixpanel** (Analytics) – Events, funnels, cohorts, A/B. Freemium–Enterprise. 8K+ (Uber, Netflix). Q3 2024. Integrates: Segment, Salesforce. PM: Activation, retention. https://mixpanel.com
[≥5, ≥3 cat]

### Literature
**L#. Author. (Year). *Title*. Publisher.** – Contribution. Use.
**Ex:** **L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.** – Discovery vs delivery. Foundational PM.
[≥6: ≥4W, ≥2E]

### APA Citations
**A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**
**Ex:** **A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**
**Non-Latin:** **A3. 俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]** (Yu, J. (2020). *Yu Jun's product methodology*. CITIC.)
[≥12: ~60%EN, ~30%ZH, ~10%other]

---

## Example

### Problem 1
**Diff:** I | **Domain:** Metrics

**Prompt:** B2B SaaS: 65% 30d retention, 70% activation. CEO wants +10pp retention in 6mo. Suggest framework + 2–3 steps with metrics.

**Answer:**
- RICE [Ref: G2, T2]: rank by reach, impact, confidence, effort
- Focus: (1) onboarding 70% new users [G7], (2) engagement at-risk cohorts [G1], (3) feature adoption power users
- Track retention curves, funnels, cohorts via Mixpanel [T1]/Amplitude [T3]; validate interviews [L4, A6]

**Solution:**
RICE [G2, T2, A2]: Onboarding (R=700, I=Hi, C=80%, E=3w)→560. Engagement (R=2000, I=Hi, C=60%, E=4w)→900 (top). Feature (R=300, I=Med, C=70%, E=2w)→210. Prioritize engagement: cohorts [T3] for at-risk (declining 14d); emails [G8]; track 7/30d retention. Analytics [T1]: North Star [G4] (weekly active); cohort dashboard; funnels; A/B. Validate [L4, A6]: weekly interviews; OST [G10]; experiments. Alternatives: ICE [L2] if uncertain (faster, less precise). Risk: spam [A15] (limit 2/wk, opt-out). Avoid vanity metrics [G4, A9]; focus activated/retained. Outcome: 4–6% lift 3mo, 10% by mo 6 [T1, T3].

---
