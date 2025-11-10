# Short Answer – Product Manager

Framework for generating high-quality product management short answer assessments with proper structure, citations, and multi-dimensional evaluation.

---

# Part I: Specifications

## Scope and Constraints

- **Problem count**: 25–40 for senior/director/VP level Product Managers
- **Difficulty split**: 20% Foundational / 40% Intermediate / 40% Advanced
- **Problem types**: Product strategy, prioritization, metrics, stakeholder communication, trade-off analysis
- **Problem format**: Self-contained prompt (2–3 sentences); concise answer (2–4 steps with frameworks, metrics, principles); worked solution with [Ref: ID] citations
- **Grading approach**: Partial credit for correct method, setup, and product judgment; document alternative valid approaches

## Reference Floors

| Section | Minimum | Content |
|---------|---------|----------|
| Glossary | 10 | RICE, AARRR, JTBD, North Star, PMF, OKR, PLG, OST, etc. |
| Tools | 5 | Analytics, roadmapping, research platforms, collaboration |
| Literature | 6 | PM frameworks, market analyses, launches, case studies |
| APA Citations | 12 | ~60% EN / ~30% ZH / ~10% other (APA 7th with language tags) |

**Scaling**: For >40 problems, increase floors by ~1.5×. Prioritize quality gates before raising floors.  
**Exception**: If floor unmet, state shortfall + rationale + sourcing plan.

## Citation Standards

- **Language mix**: ~60% [EN], ~30% [ZH], ~10% other; tag each citation
- **Source types**: (1) Product frameworks; (2) Research & data; (3) PM literature; (4) Tools & platforms
- **Format**: APA 7th edition with language tags
- **Inline usage**: Use [Ref: ID] in worked solutions when citing frameworks, data, insights, metrics, best practices

## Quality Gates

- **Recency**: ≥50% citations from last 3 years (≥70% for AI/platform domains)
- **Diversity**: ≥3 source types; no single source >25%
- **Evidence**: ≥70% problems cite ≥1 reference; ≥30% cite ≥2 references
- **Tool metadata**: Pricing, user base, last update ≤18 months, key integrations
- **Links**: All accessible or archived (DOIs preferred)
- **Cross-references**: All [Ref: ID] resolve to G#/T#/L#/A# entries

## Success Criteria

- All reference floors met or exception documented
- Problem count and difficulty split within spec
- Citation language mix within tolerance (EN 50–70%, ZH 20–40%, Other 5–15%)
- All quality gates passed
- Validation report complete with all PASS results
- Output format matches Part III template exactly

---

# Part II: Instructions

## Workflow

Follow these steps sequentially. Execute inline checks before proceeding.

### Step 1: Plan Problem Distribution

1. Identify 4–6 PM domains: Product Strategy | Discovery & Validation | Prioritization & Roadmapping | Metrics & Growth | Stakeholder Management | Go-to-Market
2. Allocate 4–8 problems per domain (total 25–40)
3. Assign difficulty ensuring 20/40/40 split (Foundational/Intermediate/Advanced)
4. **Self-check**: Total within 25–40; ratio ≈ 20/40/40

### Step 2: Collect References

1. **Glossary**: Select ≥10 terms (RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST, etc.)
2. **Tools**: Select ≥5 platforms (analytics, roadmapping, research, collaboration)
3. **Literature**: Select ≥6 sources (Cagan, Olsen, Torres, Perri, Patton, Klement; ZH: 俞军, 梁宁, 苏杰)
4. **Citations**: Create ≥12 APA entries; tag language; assign IDs (G#/T#/L#/A#)
5. **Self-check**: Counts meet floors; language mix ~60/30/10%; recency ≥50% last 3yr; ≥3 source types

### Step 3: Generate Problems

1. For each problem:
   - Write prompt: 2–3 sentences with product context, frameworks, metrics
   - Write answer: 2–4 concise, actionable steps with frameworks, metrics, principles
   - Write worked solution: step-by-step reasoning with [Ref: ID] citations
2. **Self-check**: Every 5 problems, verify prompt length, answer clarity, citation presence, solution depth

### Step 4: Populate Reference Sections

1. Complete Glossary, Tools, Literature, APA sections per Part III format
2. Include all required metadata (tool pricing, user base, update date, integrations, etc.)
3. **Self-check**: All [Ref: ID] used in problems resolve to entries; no orphan IDs

### Step 5: Validate and Submit

Execute all validation checks. Present results in validation report. Fix failures and re-run until all PASS.

**Validation Checks:**

1. **Counts**: Glossary ≥10, Tools ≥5, Literature ≥6, APA ≥12, Problems 25–40 with 20/40/40 split
2. **Citation coverage**: ≥70% problems cite ≥1 reference; ≥30% cite ≥2 references
3. **Language mix**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: ≥50% citations from last 3 years (≥70% for AI/platform)
5. **Source diversity**: ≥3 types; no single type >25%
6. **Links**: All accessible or archived
7. **Cross-references**: All [Ref: ID] resolve correctly

**Validation Report Format** (see Part III for template)

> **MANDATORY**: If ANY check shows FAIL, stop, fix issues, regenerate, and re-run validation. Only proceed when ALL checks show PASS.

**Submission Checklist:**

- [ ] All validation checks PASS
- [ ] All reference floors met (or exception documented)
- [ ] All quality gates satisfied
- [ ] Output format matches Part III template

---

# Part III: Output Format

```markdown
## Template Structure

Use this structure for all generated short answer banks.

### Validation Report Template

Present validation results using this table:

```
| Check | Result | Status |
|-------|--------|--------|
| Counts | G:X T:Y L:Z A:W P:N (F/I/A) | PASS/FAIL |
| Citation coverage | X% ≥1, Y% ≥2 | PASS/FAIL |
| Language mix | EN:X% ZH:Y% Other:Z% | PASS/FAIL |
| Recency | X% last 3yr | PASS/FAIL |
| Source diversity | N types, max P% | PASS/FAIL |
| Links | Y/X accessible | PASS/FAIL |
| Cross-refs | Y/X resolved | PASS/FAIL |
```

### Problem Bank Structure

Use this markdown structure:

```markdown
## Contents
- [Short Answer Bank](#short-answer-bank-problems-1-n)
- [Reference Sections](#reference-sections)
  - [Glossary, Terminology & Acronyms](#glossary-terminology--acronyms)
  - [Product Tools & Platforms](#product-tools--platforms)
  - [Authoritative Literature & Case Studies](#authoritative-literature--case-studies)
  - [APA Style Source Citations](#apa-style-source-citations)

---

## Short Answer Bank (Problems 1–N)

### Problem X

**Difficulty:** [Foundational/Intermediate/Advanced] | **Domain:** [Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM]

**Prompt:** (2–3 sentences, product context, frameworks, metrics)

**Answer:** (Concise, actionable response, 2–4 steps, frameworks, metrics, product principles)

**Worked Solution:** (Step-by-step reasoning, cite [Ref: ID] for frameworks, data, best practices)

---

## Reference Sections

Assign Reference IDs and reuse them inline in worked solutions: Glossary (G1…Gn), Tools (T1…Tn), Literature (L1…Ln), APA Citations (A1…An). Example inline: [Ref: G2, T3, A5].

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

## Example Problem (Product Metrics & Prioritization)

### Problem 1

**Difficulty:** Intermediate | **Domain:** Metrics & Prioritization

**Prompt:** Your SaaS product has a 30-day retention rate of 65% and an activation rate of 70%. The CEO wants to improve retention by 10 percentage points. Suggest a prioritization framework and outline 2–3 actionable steps to achieve this goal.

**Answer:**
- Use RICE prioritization [Ref: G2, T2] to rank initiatives by reach, impact, confidence, and effort.
- Focus on onboarding improvements, personalized engagement, and targeted feature adoption campaigns.
- Monitor retention and activation metrics using Mixpanel [Ref: T1].

**Worked Solution:**
1. Apply RICE to proposed initiatives: onboarding (high reach, medium impact), engagement (medium reach, high impact), feature adoption (medium reach, medium impact).
2. Score each initiative and prioritize those with highest combined score.
3. Use Mixpanel analytics to track changes in retention and activation rates.
4. Cite relevant frameworks and tools [Ref: G2, T1, T2, A2].

---
