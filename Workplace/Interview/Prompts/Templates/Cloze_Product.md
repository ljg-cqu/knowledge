# Cloze / Fill-in-the-Blank – Product Manager

Framework for generating high-quality product management fill-in-the-blank assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

Define quality requirements, standards, and constraints for PM scenarios.

## Specifications

### Scope and Structure

- **Scope**: 24–40 items for senior/director/VP level Product Managers
- **Format**: Unambiguous blanks (___); array of acceptable answers
- **Difficulty Distribution**: Maintain 20/40/40 balance (Foundational/Intermediate/Advanced)
- **Normalization**: Case-insensitive, trim whitespace, strip punctuation; specify numeric tolerances
- **Grading**: Acceptance lists with tolerances; document borderline answers, partial credit
- **Conflict Handling**: For contested terminology, acceptance lists include valid variants from different PM schools/regions/frameworks

### Citation Standards

- **Languages**: ~60% EN, ~30% ZH, ~10% other (tag each: [EN], [ZH], etc.)
- **Source Types**: (1) Product frameworks (RICE, AARRR, JTBD, OKR); (2) Research & data (market analyses, user research, case studies); (3) PM literature (books, articles, launches); (4) Tools & platforms (analytics, roadmapping, research tools)
- **Format**: APA 7th with language tags
- **Distribution**: Product Tools/Platforms; PM Literature/Case Studies
- **Inline Citation**: Use [Ref: ID] in rationales when referencing factual claims, definitions, frameworks, and product specifications. Narrative/connective sentences may remain uncited.

### Reference Minimum Requirements

| Section | Floor | Content |
|---------|-------|---------|
| Glossary | ≥10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, etc. |
| Tools | ≥5 | Analytics, roadmapping, research platforms, collaboration |
| Literature | ≥6 | PM frameworks, market analyses, launches, case studies |
| Citations | ≥12 | ~60% EN / ~30% ZH / ~10% other (APA 7th with tags) |

**Exception**: If floor unmet, state shortfall + rationale + sourcing plan.

### Quality Gates

- **Recency**: ≥50% citations from last 3 years (≥70% for AI/platform domains)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% items have ≥1 citation; ≥30% have ≥2 citations
- **Tool Details**: Pricing, user base, last update ≤18 months, key integrations
- **Links**: Validate accessibility; use DOIs/archived URLs
- **Cross-refs**: All [Ref: ID] resolve to entries

> Scaling: For >40 items, increase floors by ~1.5×. Prioritize gates before raising floors.

### Pre-Submission Validation

Execute ALL steps below. Present results in validation report table. Fix failures and re-run until all PASS.

**Step 1 – Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Items 24–40 (20/40/40)
**Step 2 – Citations**: ≥70% items have ≥1; ≥30% have ≥2
**Step 3 – Language**: EN 50-70%, ZH 20-40%, Other 5-15%
**Step 4 – Recency**: ≥50% from last 3 years (≥70% for AI/platform)
**Step 5 – Diversity**: ≥3 source types; no single >25%
**Step 6 – Links**: All accessible or archived
**Step 7 – Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)

**Validation Report Template:**
```
| Check | Result | Status |
|-------|--------|--------|
| Floors | G:X T:Y L:Z A:W I:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language dist | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
```
> **MANDATORY:** If ANY check shows FAIL, stop, fix issues, regenerate, and re-run validation. Only proceed when ALL checks show PASS.

### Submission Checklist
- [ ] All validation steps PASS (see report table above)
- [ ] ALL reference floors met + quality gates passed

---

# Part II: Instructions

Execute generation workflow with inline quality checks at each step.

## Instructions

Follow these steps in order. Execute inline quality checks at each step before proceeding.

### Step 1: Topic Identification & Planning
1. Identify 4–6 PM clusters: Product Strategy | Discovery & Validation | Prioritization & Roadmapping | Metrics & Growth | Stakeholder Management | Go-to-Market
2. Allocate 4–8 items per cluster (total 24–40)
3. Assign difficulty levels ensuring 20/40/40 balance
4. **Check**: Total = 24–40, ratio ≈20/40/40

### Step 2: Reference Collection
1. **Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
2. **Tools (≥5)**: Mixpanel/Amplitude (analytics), ProductBoard/Aha! (roadmapping), Dovetail/UserTesting (research), Miro (collaboration)
3. **Literature (≥6)**: Cagan, Olsen, Torres, Perri, Patton, Klement + ZH sources (俞军, 梁宁, 苏杰)
4. **Citations (≥12)**: Tag language, year, type (1–4); assign IDs (G#/T#/L#/A#)
5. **Check**: Counts, language ~60/30/10%, recency ≥50% last 3yr, ≥3 types

### Step 3: Item Generation
1. For EACH item: Write fill-in-the-blank statement (unambiguous, product context, frameworks, metrics)
2. Provide array of acceptable answers (frameworks, terminology, metrics, product principles)
3. Rationale (1–2 sentences, cite [Ref: ID] for frameworks, data, best practices)
4. **Check**: Every 5 items verify lengths, citations, answer quality

### Step 4: Reference Sections
1. Populate Glossary/Tools/Literature/APA with required fields
2. **Check**: All [Ref: ID] resolve

### Step 5: Validation
Execute all steps. Fix failures; re-validate until all PASS.

### Step 6: Final Review
Check submission checklist. Submit when all PASS.

---

# Part III: Output Format

Template structure for generated cloze banks.

## Output Format

Use this structure when generating cloze banks:

```markdown
## Contents
- [Cloze Bank](#cloze-bank-items-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Product Tools & Platforms](#product-tools--platforms)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Cloze Bank (Items 1–N)

### Item X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Statement:** (Fill-in-the-blank, product context, frameworks, metrics)

**Acceptable Answers:** [Array of frameworks, terminology, metrics, product principles]

**Rationale:** (1–2 sentences, cite [Ref: ID] for frameworks, data, best practices)

---

## Reference Sections

Assign Reference IDs and reuse them inline in item rationales: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G2, T3, A5].

### Glossary, Terminology & Acronyms

**G1. AARRR (Pirate Metrics)**  
Acquisition → Activation → Retention → Referral → Revenue framework for tracking growth across customer lifecycle. Used for SaaS metrics, funnel optimization. Related: HEART, North Star Metric

**G2. RICE Prioritization**  
Reach × Impact × Confidence ÷ Effort scoring for feature prioritization. Used for roadmap planning, backlog ranking. Related: ICE, Value/Effort Matrix, KANO

**G3. Jobs-to-be-Done (JTBD)**  
Framework for understanding the underlying "job" users hire a product to accomplish (vs demographics). Used for feature ideation, segmentation, competitive analysis. Related: Outcome-driven innovation

**G4. North Star Metric**  
Single metric capturing core product value; leading indicator of sustainable growth. Used for company alignment, PLG, OKRs. Related: OMTM, Input/Output metrics

**G5. Product-Market Fit (PMF)**  
Degree product satisfies market demand; measured when retention flattens and organic growth accelerates. Used for validation, pivot decisions, expansion. Related: Problem-solution fit, MVP

**G6. OKR (Objectives and Key Results)**  
Goal framework where Objectives = what to achieve, Key Results = how to measure. Used for quarterly planning, cross-functional alignment. Related: KPI, North Star, V2MOM

**G7. Continuous Discovery**  
Regular customer engagement through structured interviews/testing to inform decisions (vs periodic projects). Used for weekly interviews, opportunity trees, assumption testing. Related: Dual-track agile, Build-Measure-Learn

**G8. Product-Led Growth (PLG)**  
GTM strategy where product drives acquisition, conversion, expansion (vs sales-led). Used for SaaS freemium, self-serve onboarding, viral loops. Related: PQLs, Time-to-Value, Expansion revenue

**G9. Feature Factory**  
Anti-pattern: shipping features (outputs) vs solving problems (outcomes). Used in transformation discussions, outcome-based PM. Related: Build trap, Empowered teams

**G10. Opportunity Solution Tree (OST)**  
Visual framework mapping outcomes → opportunities (needs/pains) → solutions. Used for discovery planning, ideation, assumption mapping. Related: HMW statements, User story mapping

[... continue for ≥10 entries ...]

---

### Product Tools & Platforms

**T1. Mixpanel** (Product Analytics)  
Event tracking, funnel/cohort analysis, A/B testing, user segmentation. Freemium to Enterprise. 8K+ companies (Uber, Netflix). Updated Q3 2024 (AI insights). Integrates: Segment, Salesforce, Slack, Jira. PM use: Activation tracking, feature adoption, retention monitoring. https://mixpanel.com

**T2. ProductBoard** (Roadmapping & Prioritization)  
Feedback aggregation, prioritization matrix (value/effort), roadmap views, customer portal. Essentials $25/maker/mo to Enterprise. 6K+ teams (Microsoft, Zoom). Updated Q4 2024 (AI feedback analysis). Integrates: Jira, Slack, Salesforce, Intercom, Zendesk. PM use: Feedback synthesis, RICE scoring, stakeholder communication. https://www.productboard.com

**T3. Amplitude** (Product Analytics & Experimentation)  
Behavioral cohorts, retention/funnel analysis, A/B/n testing, predictive analytics. Freemium to Enterprise. 3.2K+ companies (PayPal, Ford). Updated Q3 2024 (AI insights, predictive playbooks). Integrates: Segment, Braze, Optimizely, Salesforce. PM use: North Star tracking, conversion optimization, impact analysis. https://amplitude.com

**T4. Dovetail** (User Research Repository)  
Auto transcription, tagging/theming, highlight reels, sentiment analysis, journey visualization. Freemium to Enterprise. 3K+ teams (Atlassian, Canva). Updated Q2 2024 (AI theme detection). Integrates: Zoom, Slack, Notion, Jira, UserTesting. PM use: Interview synthesis, JTBD mapping, discovery insights. https://dovetail.com

**T5. Miro** (Visual Collaboration)  
Infinite canvas, templates (story maps, journey maps, matrices), real-time collab, AI assistant. Freemium to Enterprise. 80M+ users (Dell, Cisco). Updated Q4 2024 (enhanced AI). Integrates: Jira, Slack, Teams, Zoom, Figma, Asana. PM use: Story mapping, OST workshops, roadmap planning, retrospectives. https://miro.com

[... continue for ≥5 entries ...]

---

### Authoritative Literature & Case Studies

**L1. Cagan, M. (2017). *Inspired* (2nd ed.). Wiley.**  
PM framework: discovery vs delivery, empowered teams. Foundational PM principles.

**L2. Olsen, D. (2015). *The Lean Product Playbook*. Wiley.**  
6-step process for product-market fit. Strategic planning, validation techniques.

**L3. Perri, M. (2018). *Escaping the Build Trap*. O'Reilly.**  
Outcomes over outputs, feature factory to outcome-driven culture. Organizational transformation.

**L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.**  
Weekly customer touchpoints, opportunity solution trees. Discovery process design.

**L5. Patton, J. (2014). *User Story Mapping*. O'Reilly.**  
Story mapping by user journey (vs flat backlog). Roadmap planning, MVP scoping.

**L6. Klement, A. (2016). *When Coffee and Kale Compete*. Independent.**  
JTBD: functional/emotional/social jobs. Product positioning, competitive analysis.

[... continue for ≥6 entries ...]

---

### APA Style Source Citations

**A1. Cagan, M. (2017). *Inspired: How to create tech products customers love* (2nd ed.). Wiley. [EN]**

**A2. Olsen, D. (2015). *The lean product playbook: How to innovate with minimum viable products and rapid customer feedback*. Wiley. [EN]**

**A3. 俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]**  
(Yu, J. (2020). *Yu Jun's product methodology*. CITIC Press.)

**A4. Perri, M. (2018). *Escaping the build trap: How effective product management creates real value*. O'Reilly Media. [EN]**

**A5. Patton, J. (2014). *User story mapping: Discover the whole story, build the right product*. O'Reilly Media. [EN]**

**A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

**A7. Klement, A. (2016). *When coffee and kale compete: Become great at making products people will buy*. Independent. [EN]**

**A8. Ries, E. (2011). *The lean startup: How today's entrepreneurs use continuous innovation to create radically successful businesses*. Crown Business. [EN]**

**A9. McClure, D. (2007). Startup metrics for pirates: AARRR!. *500 Startups*. https://www.slideshare.net/dmc500hats/startup-metrics-for-pirates-long-version [EN]**

**A10. 梁宁. (2018). *产品思维30讲*. 得到App. [ZH]**  
(Liang, N. (2018). *30 lectures on product thinking*. Dedao App.)

**A11. Maurya, A. (2012). *Running lean: Iterate from plan A to a plan that works* (2nd ed.). O'Reilly Media. [EN]**

**A12. Eisenmann, T., Ries, E., & Dillard, S. (2012). Hypothesis-driven entrepreneurship: The lean startup. *Harvard Business School Entrepreneurial Management Case*, (812-095). [EN]**

**A13. Gothelf, J., & Seiden, J. (2016). *Lean UX: Designing great products with agile teams* (2nd ed.). O'Reilly Media. [EN]**

**A14. Bush, L., & Dunlap, K. (2023). *Product operations: How successful companies build better products at scale*. O'Reilly Media. [EN]**

**A15. 苏杰. (2019). *人人都是产品经理2.0*. 电子工业出版社. [ZH]**  
(Su, J. (2019). *Everyone is a product manager 2.0*. Publishing House of Electronics Industry.)

**A16. Kim, G. N. (2022). *Product leadership: How top product managers launch awesome products and build successful teams*. O'Reilly Media. [EN]**

[... continue for ≥12 entries with ~60% EN, ~30% ZH, ~10% other ...]
```

---

## Example Item (Product Frameworks & Metrics)

### Item 1

**Difficulty:** Foundational | **Domain:** Product Frameworks & Metrics

**Statement:** The framework that scores features by reach, impact, confidence, and effort is called ___.

**Acceptable Answers:** [RICE, RICE prioritization]

**Rationale:** RICE [Ref: G2, A2] is a widely used product management framework for prioritizing features based on reach, impact, confidence, and effort.

---
