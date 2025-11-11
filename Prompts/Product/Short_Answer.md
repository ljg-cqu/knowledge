# Short Answer Framework – Product Manager

Generate high-quality PM assessments for senior/director/VP level Product Managers.

**Constraints:**
- 25–40 problems across 6 domains: Product Strategy, Discovery & Validation, Prioritization & Roadmapping, Metrics & Growth, Stakeholder Management, Go-to-Market
- Evidence-based with multi-source citations (~60% EN, ~30% ZH, ~10% other)
- Structured markdown with validation reporting
- Partial credit for methodology and judgment

**Assumptions:** Candidates have 2–5 years PM experience in SaaS/platforms/B2B/B2C contexts.

---

# Part I: Specifications

## Problem Specifications

**Count:** 25–40 problems | **Difficulty:** 20% Foundational / 40% Intermediate / 40% Advanced (±5% tolerance)
- *Foundational*: Core frameworks (AARRR, RICE)
- *Intermediate*: Trade-off analysis, cross-functional scenarios
- *Advanced*: Strategic decisions, multi-stakeholder conflicts, ambiguous contexts

**Domain Coverage:** 4–8 problems each
1. **Product Strategy**: Vision, positioning, market analysis
2. **Discovery & Validation**: User research, hypothesis testing, PMF
3. **Prioritization & Roadmapping**: RICE, ICE, value/effort, backlog management
4. **Metrics & Growth**: North Star, AARRR, retention, activation
5. **Stakeholder Management**: Communication, alignment, conflict resolution
6. **Go-to-Market**: Launch strategy, PLG, sales enablement

**Format:**
- **Prompt**: 2–3 sentences (context + constraints + question)
- **Answer**: 2–4 actionable steps with citations [Ref: G#/T#/L#/A#]
- **Worked Solution**: Reasoning with citations, methodology, alternatives, trade-offs

**Grading:** Correctness (40%) | Reasoning (30%) | Practicality (20%) | Completeness (10%)
- Partial credit for methodology, framework application, judgment, alternatives

## Reference Requirements

**Minimum Floors:**
| Section | Min | Content | Rationale |
|---------|-----|---------|-----------|
| Glossary (G#) | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, Continuous Discovery, Feature Factory | Framework vocabulary across 6 domains |
| Tools (T#) | 5 | Analytics (Mixpanel/Amplitude), Roadmapping (ProductBoard/Aha!), Research (Dovetail/UserTesting), Collaboration (Miro/FigJam), A/B Testing (Optimizely/LaunchDarkly) | Complete PM toolkit |
| Literature (L#) | 6 | Strategic (Cagan, Olsen), Discovery (Torres, Patton), Transformation (Perri), Cultural (俞军, 梁宁, 苏杰) | Western + Eastern PM philosophies |
| APA (A#) | 12 | ~60% [EN], ~30% [ZH], ~10% [other] with APA 7th + language tags | Cultural diversity, verification |

**Scaling:** 41–60 problems: 1.5× | 61+ problems: 2×

**Exceptions:** Document shortfall + rationale + sourcing plan (e.g., "Tools: 4/5, missing A/B platform. Niche domain. Adding Split.io (T#)")

## Citation Standards

**Language Mix:** EN 50–70% | ZH 20–40% | Other 5–15% (balances global + Eastern PM perspectives)
- Append language tags: [EN], [ZH], [JA], [KO], [DE]
- Romanize non-Latin titles in parentheses

**Source Types (MECE):** ≥3 of 4, max 25% each
1. Frameworks/Methodologies (RICE, JTBD, OKR, Continuous Discovery, PLG)
2. Research/Data (user studies, market analyses, growth benchmarks, industry reports)
3. Literature (Cagan, Olsen, Torres, Perri, 俞军, 梁宁, academic papers, case studies)
4. Tools/Platforms (Mixpanel, ProductBoard, Dovetail, Miro)

**Format:** APA 7th edition
- **Required**: Author, Year, Title (italicized), Publisher/Journal, DOI/URL, Language tag
- **Inline**: [Ref: ID] where ID = G# (Glossary), T# (Tools), L# (Literature), A# (APA)
- **Example**: "Apply RICE [Ref: G2, T2, A2]..."

**Usage:**
- Cite: Framework applications, data/metrics, best practices, tool recommendations
- Coverage: ≥70% problems cite ≥1 reference; ≥30% cite ≥2+ references
- Verification: DOI > stable URL > archived snapshot (Wayback Machine)
- Cross-reference: All [Ref: ID] must resolve to Part III entries

## Quality Gates

**1. Recency:** ≥50% from last 3 years (≥70% for AI/platform domains). Flag foundational works >10 years.

**2. Source Diversity:** ≥3 of 4 types; no type >25%. Balance practitioner wisdom, academic rigor, tool documentation.

**3. Evidence Coverage:** ≥70% problems cite ≥1 ref; ≥30% cite ≥2+ refs. Advanced problems need ≥2 refs.

**4. Tool Metadata (T#):** Include pricing, user base (XK+ companies, 2–3 clients), last update (≤18 months), integrations (3–5), PM use cases (2–3), HTTPS URL.

**5. Link Accessibility:** DOI > stable URL > archived snapshot. Test all links; flag "[Archived: DATE]".

**6. Cross-Reference Integrity:** All [Ref: ID] resolve to Part III entries. No orphan IDs. ≥80% entries cited ≥1 problem.

## Success Criteria

**Mandatory (All PASS):**
| Criterion | Specification | Validation |
|-----------|---------------|------------|
| Reference floors | G≥10, T≥5, L≥6, A≥12 (or exception) | Count entries |
| Problem count | 25–40 | Count headers |
| Difficulty | 20%F/40%I/40%A (±5%) | Calculate % |
| Language | EN 50–70%, ZH 20–40%, Other 5–15% | Count tags |
| Quality gates | All 6 PASS | Run checks |
| Validation report | All PASS | Use template |
| Format | Match Part III template | Inspect |

**Performance Indicators:**
- Citation depth: Avg ≥1.5/problem
- Framework diversity: ≥8 distinct frameworks
- Practical relevance: ≥90% include metrics/tools/data
- Alternatives: ≥25% mention trade-offs/alternatives

---

# Part II: Workflow

Execute steps sequentially with inline checks.

## Step 1: Plan Problem Distribution

**Objective:** Balanced problem set covering 6 PM domains (MECE).

**Actions:**
1. **Allocate 25–40 problems**: 4–8 per domain (Strategy, Discovery, Prioritization, Metrics, Stakeholder, GTM).
2. **Assign difficulty** (20%F/40%I/40%A):
   - Foundational: Standard frameworks, definitions
   - Intermediate: Trade-offs, scenarios, cross-functional challenges
   - Advanced: Strategic decisions, multi-stakeholder conflicts, ambiguity
3. **Self-check**:
   - [ ] Count = 25–40
   - [ ] Difficulty ≈ 20/40/40 (±5%)
   - [ ] Each domain 4–8 problems
   - [ ] No gaps/overlaps

## Step 2: Collect References

**Objective:** Diverse, authoritative, up-to-date references (frameworks, tools, literature, data).

**Actions:**
1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST. Format: **G#. Term** – Definition. Used for: [contexts]. Related: [terms].

2. **Tools (≥5)**: Analytics (Mixpanel/Amplitude), Roadmapping (ProductBoard/Aha!), Research (Dovetail/UserTesting), Collaboration (Miro/FigJam), Experimentation (Optimizely/LaunchDarkly). Format: **T#. Tool** (Category) – Description. Pricing. User base. Updated [DATE]. Integrates: [platforms]. PM use: [cases]. [URL].

3. **Literature (≥6)**: Western (≥4): Cagan, Olsen, Torres, Perri, Patton, Klement. Eastern (≥2): 俞军, 梁宁, 苏杰. Format: **L#. Author. (Year). *Title*. Publisher.** – Key contribution. Use cases.

4. **APA (≥12)**: Full APA 7th citations with language tags [EN]/[ZH]/[JA]. Romanize non-Latin titles. Format: **A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**.

5. **Self-check**:
   - [ ] G≥10, T≥5 (≥3 categories), L≥6 (≥4 Western, ≥2 Eastern), A≥12
   - [ ] Language: EN 50–70%, ZH 20–40%, Other 5–15%
   - [ ] Recency: ≥50% from last 3 years
   - [ ] Source diversity: ≥3/4 types, none >25%
   - [ ] Tool metadata complete (pricing, users, update ≤18mo, integrations, cases, link)
   - [ ] All links tested

## Step 3: Generate Problems

**Objective:** Well-structured, evidence-based problems testing PM competencies.

**Actions (for each problem):**

1. **Prompt (2–3 sentences)**: Context (scenario + constraints) + relevant frameworks/metrics + specific question. Avoid vagueness, jargon, multiple questions.

2. **Answer (2–4 steps)**: Actionable steps citing [Ref: ID]. Include frameworks (G#), tools (T#), literature (L#), sources (A#). Apply PM best practices (user-centric, data-driven, iterative).

3. **Worked Solution (4–8 sentences)**: Reasoning with citations. Flow: Problem → Framework → Application → Validation → Outcome. For Intermediate/Advanced: alternatives + trade-offs. For Advanced: flag misconceptions.

4. **Self-check (every 5 problems)**:
   - [ ] Prompt: 2–3 sentences, clear context + question
   - [ ] Answer: 2–4 steps, each cites ≥1 ref
   - [ ] Citation: ≥70% problems cite ≥1 ref; ≥30% cite ≥2+ refs
   - [ ] Solution: 4–8 sentences, reasoning, trade-offs (I/A), alternatives (A)
   - [ ] Terminology consistent
   - [ ] Aligns with domain + difficulty
   - [ ] Logic coherent

## Step 4: Populate Reference Sections

**Objective:** Comprehensive, formatted references supporting all citations.

**Actions:**
1. **Glossary (G#)**: **G#. Term** – Definition. Used for: [contexts]. Related: [terms]. ≥10 entries, all 6 domains.

2. **Tools (T#)**: **T#. Tool** (Category) – Description. Pricing. User base (clients). Updated [DATE]. Integrates: [platforms]. PM use: [cases]. [URL]. ≥5 entries, ≥3 categories, update ≤18mo, test links.

3. **Literature (L#)**: **L#. Author. (Year). *Title*. Publisher.** – Key contribution. Use cases. ≥6 entries (≥4 Western, ≥2 Eastern).

4. **APA (A#)**: **A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**. Romanize non-Latin. ≥12 entries, ~60% EN/~30% ZH/~10% other, ≥50% last 3yr, test links.

5. **Self-check**:
   - [ ] All [Ref: ID] resolve (no orphans)
   - [ ] ≥80% entries cited ≥1 problem
   - [ ] Consistent ID format (G#/T#/L#/A#)
   - [ ] Tool metadata complete
   - [ ] Literature complete
   - [ ] APA complete with tags
   - [ ] Links tested (or [Archived: DATE])

## Step 5: Validate and Submit

**Objective:** Verify all specs, quality gates, success criteria.

**Execute 7 Checks:**
1. **Counts**: G≥10, T≥5, L≥6, A≥12, P=25–40, Difficulty 20/40/40 (±5%)
2. **Citation**: ≥70% problems cite ≥1 ref; ≥30% cite ≥2+ refs
3. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: ≥50% last 3yr (≥70% AI/platform)
5. **Diversity**: ≥3/4 types, none >25%
6. **Links**: All accessible or [Archived: DATE]
7. **Cross-refs**: All [Ref: ID] resolve; ≥80% entries cited

**Generate Report:**
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
| Citation | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |

**If ANY FAIL:** Stop. Document failure (check, expected vs actual, cause). Fix (add entries, adjust, replace, repair). Re-run all checks. Repeat until 7/7 PASS.

**Submit only if 7/7 PASS with:** Validation report + format matches Part III + all metadata complete + all links tested.

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
- [Short Answer Bank](#short-answer-bank-problems-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary](#glossary-terminology--acronyms)
  - [Tools](#product-tools--platforms)
  - [Literature](#authoritative-literature--case-studies)
  - [APA Citations](#apa-style-source-citations)

---

## Short Answer Bank (Problems 1–N)

### Problem X
**Difficulty:** [F/I/A] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Prompt:** (2–3 sentences: context + frameworks/metrics + question)

**Answer:** (2–4 actionable steps citing [Ref: ID])

**Worked Solution:** (4–8 sentences: reasoning + citations + alternatives/trade-offs + misconceptions if A)

---

## Reference Sections

### Glossary, Terminology & Acronyms
**G#. Term** – Definition. Used for: [contexts]. Related: [terms].

**Example:** **G1. RICE** – Reach × Impact × Confidence ÷ Effort for prioritization. Used for roadmap planning, backlog ranking. Related: ICE, KANO.

[≥10 entries, all 6 domains]

---

### Product Tools & Platforms
**T#. Tool** (Category) – Description. Pricing. XK+ companies (clients). Updated [Q# YYYY]. Integrates: [platforms]. PM use: [cases]. [URL]

**Example:** **T1. Mixpanel** (Analytics) – Event tracking, funnels, cohorts, A/B testing. Freemium–Enterprise. 8K+ companies (Uber, Netflix). Updated Q3 2024. Integrates: Segment, Salesforce, Slack, Jira. PM use: Activation, adoption, retention. https://mixpanel.com

[≥5 entries, ≥3 categories]

---

### Authoritative Literature & Case Studies
**L#. Author. (Year). *Title*. Publisher.** – Key contribution. Use cases.

**Example:** **L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.** – Discovery vs delivery, empowered teams. Foundational PM.

[≥6 entries: ≥4 Western, ≥2 Eastern]

---

### APA Style Source Citations
**A#. Author. (Year). *Title*. Publisher. DOI/URL [Tag]**

**Example:** **A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

**Non-Latin Example:** **A3. 俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]** (Yu, J. (2020). *Yu Jun's product methodology*. CITIC Press.)

[≥12 entries: ~60% EN, ~30% ZH, ~10% other]

---

## Example Problem

### Problem 1
**Difficulty:** Intermediate | **Domain:** Metrics & Prioritization

**Prompt:** Your B2B SaaS has 30-day retention of 65%, activation of 70%. CEO wants +10pp retention in 6 months. Suggest prioritization framework and 2–3 actionable steps with metrics.

**Answer:**
- Use RICE [Ref: G2, T2] to rank by reach, impact, confidence, effort
- Focus: (1) onboarding for 70% new users [Ref: G7], (2) engagement for at-risk cohorts [Ref: G1], (3) feature adoption for power users
- Track retention curves, funnels, cohorts via Mixpanel [Ref: T1] or Amplitude [Ref: T3]; validate with interviews [Ref: L4, A6]

**Worked Solution:**
1. **RICE scoring** [Ref: G2, T2, A2]: Onboarding (R=700, I=High, C=80%, E=3wk) → 560. Engagement (R=2000, I=High, C=60%, E=4wk) → 900 (highest). Feature (R=300, I=Med, C=70%, E=2wk) → 210.
2. **Prioritize engagement**: Use cohorts [Ref: T3] for at-risk users (declining 14d usage); send personalized emails [Ref: G8]; monitor 7/30d retention.
3. **Track analytics** [Ref: T1]: Define North Star [Ref: G4] (weekly active usage); dashboard cohort retention; funnel completion; A/B tests.
4. **Validate** [Ref: L4, A6]: Weekly interviews; OST [Ref: G10] for needs; small experiments before rollout.
5. **Alternatives/Trade-offs**: ICE [Ref: L2] if data uncertain (faster, less precise). Risk: Spam [Ref: A15] (limit 2/week, opt-out). Misconception: Avoid vanity metrics [Ref: G4, A9]; focus activated/retained users.
6. **Outcome**: 4–6% lift in 3mo, 10% by mo 6 [Ref: T1, T3].

---
