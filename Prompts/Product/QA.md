# PM Interview Q&A Generator

Generate 25–30 scenario-based interview questions testing senior/director/VP-level Product Manager judgment with evidence-based answers, visual artifacts, and quantitative validation.

## I. Definitions & Scope

**Terms**:
- **Q&A**: Scenario question–answer pair testing judgment (not recall)
- **Floor (≥)**: Minimum required threshold
- **Quality gate**: Mandatory checkpoint—fail = stop and fix
- **Difficulty**: F (Foundational) = execution; I (Intermediate) = strategy/trade-offs; A (Advanced) = portfolio/vision/P&L
- **Dimensions**: Product (user value), Business (revenue), Strategic (market), Operational (execution, risk)

**Scope**: Senior+ PM scenarios with stakeholder tension, resource constraints, strategic ambiguity. **Exclude**: Trivia, greenfield design, junior tasks, domain-specific technical questions.

## II. Requirements

### Quantitative Floors

**Q&A Composition**:
- Total: 25–30 pairs | Difficulty: 20% F / 40% I / 40% A (±5%)
- Answer length: 150–300 words (excluding artifacts)
- Citations: ≥70% have ≥1; ≥30% have ≥2
- Each answer addresses ≥2 dimensions

**Topic Coverage (MECE—Mutually Exclusive, Collectively Exhaustive)**:
1. Strategy & Vision (5–6) | 2. Discovery & User Research (4–5) | 3. Prioritization & Roadmapping (5–6) | 4. Metrics & Analytics (4–5) | 5. Stakeholder Management (4–5) | 6. Go-to-Market & Growth (4–5)

**Reference Floors** (build before Q&A generation):
- **Glossary**: ≥10 terms (RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST, HEART, Value/Effort Matrix, KANO, V2MOM, Dual-track Agile)
- **Tools**: ≥5 platforms (analytics, roadmapping, research, collaboration, feedback)
- **Literature**: ≥6 books/frameworks (≥2 Chinese: 俞军, 梁宁, 苏杰)
- **Citations**: ≥12 APA 7th sources with language tags ([EN], [ZH])

**Visual Artifacts**: ≥1 diagram + ≥1 table per topic

**Scaling**: For >30 Q&A, multiply reference floors by 1.5× (round up).

### Citation Standards

**Format**: APA 7th + language tag: `Author, A. (Year). *Title*. Publisher. [EN]`

**Inline**: `[Ref: ID]` after claims/metrics/frameworks | IDs: G# = Glossary, T# = Tool, L# = Literature, A# = Citation

**Language Distribution**: EN 50–70% (target 60%) | ZH 20–40% (target 30%) | Other 5–15% (target 10%)

**Source Diversity** (≥3 types): Frameworks (RICE, JTBD, OST) | Research/data (studies, benchmarks) | Case studies (launches, postmortems) | Tools (Mixpanel, ProductBoard, Dovetail)

### Quality Gates (Mandatory—fail ANY = stop, fix, re-validate ALL)

1. **Recency**: ≥50% from last 3yrs (≥70% for AI/ML/platform/data)
2. **Source Diversity**: ≥3 types; no type >25%
3. **Per-Topic Evidence**: Each topic has ≥2 authoritative sources + ≥1 tool
4. **Tool Completeness**: All include pricing, user base, update date (≤18 months), ≥3 integrations
5. **Link Validation**: 100% URLs accessible or archived
6. **Cross-Reference Integrity**: 100% [Ref: ID] resolve; no orphaned entries

## III. Execution Steps

### Step 1: Plan Topic Allocation

Distribute 25–30 across 6 topics (20%F/40%I/40%A). Each topic: 4–6 Q&A with ≥1F, ≥1I, ≥1A.
Example (30): Strategy (5), Discovery (5), Prioritization (6), Metrics (5), Stakeholder (4), GTM (5) = 6F/12I/12A

### Step 2: Build Reference Foundation (BEFORE Q&A generation → run Gates 1–6 after)

**Glossary (≥10)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST (optional: HEART, Value/Effort, KANO, V2MOM, Dual-track, ICE). Format: term, definition (1–2 sentences), use cases, related terms. Assign G1, G2, G3...

**Tools (≥5)**: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro, Figma), Feedback (Pendo, Canny). Include: category, pricing, user base, update (≤18mo), ≥3 integrations, PM use case, URL. Assign T1, T2, T3...

**Literature (≥6)**: EN—Cagan (*Inspired*), Olsen (*Lean Product Playbook*), Torres (*Continuous Discovery*). ZH (≥2)—俞军 (*俞军产品方法论*), 梁宁 (*产品思维30讲*), 苏杰 (*人人都是产品经理*). Include: author, title, year, summary, frameworks. Assign L1, L2, L3...

**APA Citations (≥12)**: Convert above to APA 7th + language tags. Verify ≥50% from last 3yrs. Classify: frameworks/research/case studies/tools. Assign A1, A2, A3...

### Step 3: Generate Q&A (5 at a time → self-check each batch)

**Question Format**: Scenario ("How would you...", "Walk me through...", "CEO wants X—what do you do?"). Include constraints (time, resources, stakeholder pressure, conflicting data). Test ≥2 judgment signals: trade-offs, opportunity cost, stakeholder tension, incomplete info, execution complexity. Single unambiguous ask. **Avoid**: "What is X?", "List Y", "Define Z"

**Difficulty Alignment**: F = execution ("Track activation?") | I = strategy/trade-offs ("Churn vs. features?") | A = portfolio/vision/P&L ("Choose: API, mobile, or intl?")

**Answer Structure** (150–300 words):
1. **Key Insight** (1 sentence): Specific dilemma/tension (e.g., "revenue vs. PMF")
2. **Framework/approach**: Methods [Ref: G#/A#]
3. **Multi-dimensional analysis**: ≥2 dimensions (Product, Business, Strategic, Operational)
4. **Concrete steps**: Sequenced actions
5. **Trade-offs**: Optimize vs. sacrifice
6. **Stakeholder communication**: How present
7. **Success criteria**: How measure
8. **Citations**: ≥1 [Ref: ID]
9. **Artifact** (optional): Matrix, journey, dashboard, roadmap

**Batch Self-Check** (per 5): Scenario-based (not "What is...") | Test ≥2 judgment signals | 150–300 words | Concrete Key Insight | ≥2 dimensions | ≥3/5 have ≥1 citation; ≥1/5 has ≥2 | Difficulty labels match content

### Step 4: Create Visual Artifacts (≥1 diagram + ≥1 table per topic; reference from ≥50% answers)

**Strategy**: Roadmap (now/next/later), competitive 2×2, weighted decision matrix | **Discovery**: User journey (stages/pains/opportunities), research synthesis (insight/evidence/impact/action) | **Prioritization**: Opportunity Solution Tree, Value/Effort 2×2, RICE table | **Metrics**: AARRR funnel, cohort chart, dashboard (KPI/current/target/trend/owner) | **Stakeholder**: Power/interest 2×2, matrix (name/interest/concern/engagement) | **GTM**: Growth loop, channel strategy, launch checklist, channel performance

### Step 5: Populate Reference Sections

**Glossary**: **G#. Term (Acronym)** | Definition (1–2 sentences) | Use cases | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | User base | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (focus, frameworks) | Relevance | Group by language (≥2 ZH)

**APA Citations**: **A#. [Citation] [Lang]** | Books: `Author, A. (Year). *Title*. Publisher. [EN]` | Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]` | Web: `Author. (Year). *Title*. Site. URL [EN]` | Romanized ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH] (Yu, J. (2020). *Yu Jun's Product Methodology*. CITIC Press.)` | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA have language tags

### Step 6: Run 12 Validations (fail ANY = stop, fix, re-run ALL; include table in output)

1. **Floors**: G≥10, T≥5, L≥6, A≥12, Q=25–30, 20%F/40%I/40%A (±5%)
2. **Citations**: ≥70% have ≥1; ≥30% have ≥2
3. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
4. **Recency**: ≥50% from last 3yrs (≥70% if AI/ML/platform/data)
5. **Source Types**: ≥3 types; no type >25%
6. **Links**: 100% accessible/archived
7. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans
8. **Word Count**: Sample 5 answers; 100% within 150–300
9. **Key Insights**: 100% concrete (specific dilemma/tension)
10. **Per-Topic Evidence**: 6/6 topics have ≥2 authoritative + ≥1 tool
11. **Framework Usage**: ≥80% correct + cited + limitations
12. **Judgment Ratio**: ≥70% scenario-based (not "What is...", "List...")

### Step 7: Final Quality Review

**Questions**: Clarity (single ask) | Signal (judgment not trivia) | Depth (trade-offs) | Realism (senior+ PM) | Discriminative (judgment over recall) | Alignment (difficulty matches seniority)

**Answers** (sample ≥5): ≥2 dimensions | Concrete steps/frameworks | Explicit trade-offs | Supporting citations | Success criteria

**Submission**: All 12 validations PASS | All floors met (G≥10/T≥5/L≥6/A≥12) | All 6 gates passed | TOC with anchor links | No placeholders | Consistent formatting

## IV. Validation Report Template (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥10, T≥5, L≥6, A≥12, Q:25-30, 20/40/40% | | PASS/FAIL |
| 2 | Citations          | __%≥1, __%≥2                          | ≥70%≥1, ≥30%≥2                      | | PASS/FAIL |
| 3 | Language           | EN:__%, ZH:__%, Other:__%             | EN:50-70%, ZH:20-40%, Other:5-15%   | | PASS/FAIL |
| 4 | Recency            | __% from 3yrs (domain: ___)           | ≥50% (≥70% AI/platform)             | | PASS/FAIL |
| 5 | Source Types       | __ types; max __%                     | ≥3 types, max 25%                   | | PASS/FAIL |
| 6 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 7 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 8 | Word Count         | __ sampled: __ compliant              | 100% (150-300)                      | | PASS/FAIL |
| 9 | Key Insights       | __/__ concrete                        | 100%                                | | PASS/FAIL |
| 10| Per-Topic Evidence | __/6 (≥2 auth + ≥1 tool)              | 6/6                                 | | PASS/FAIL |
| 11| Frameworks         | __/__ correct+cited+limits            | ≥80%                                | | PASS/FAIL |
| 12| Judgment Ratio     | __% scenario-based                    | ≥70%                                | | PASS/FAIL |

## V. Question Quality Criteria (review each; fails ≥2 = rewrite/replace)

1. **Clarity**: Single ask | ✓ "Prioritize activation vs. churn?" | ✗ "Explain retention + database optimization"
2. **Signal**: Tests judgment | ✓ "CEO wants AI—approach?" | ✗ "List AARRR stages"
3. **Depth**: Enables trade-offs | ✓ "Choose: API, mobile, or intl—how decide?" | ✗ "Build mobile app—yes/no?"
4. **Realism**: Senior+ PM scenario | ✓ "Sales wants 3 custom features ($5M deal). Engineering says derails roadmap. What do?" | ✗ "Design Instagram in 45min"
5. **Discriminative**: Application not recall | ✓ "When would RICE mislead? How supplement?" | ✗ "What does RICE stand for?"
6. **Alignment**: Difficulty matches seniority | F: execution | I: strategy/trade-offs | A: portfolio/vision/P&L

## VI. Output Format (all sections mandatory)

### A. Table of Contents
1. Topic Areas Overview | 2. Questions by Topic (6 topics) | 3. Reference Sections (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Topic Overview
**Total**: [25–30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 6 PM competencies (MECE)

| # | Topic        | Range    | Count | Mix      | Artifacts     |
|---|--------------|----------|-------|----------|---------------|
| 1 | Strategy     | Q1–Q5    | 5     | 1F/2I/2A | 1 diagram+table |
| 2 | Discovery    | Q6–Q10   | 5     | 1F/2I/2A | 1 diagram+table |
| 3 | Prioritization | Q11–16 | 6     | 1F/2I/3A | 1 diagram+table |
| 4 | Metrics      | Q17–21   | 5     | 1F/2I/2A | 1 diagram+table |
| 5 | Stakeholder  | Q22–25   | 4     | 1F/2I/1A | 1 diagram+table |
| 6 | GTM          | Q26–30   | 5     | 1F/2I/2A | 1 diagram+table |
|   | **Total**    |          | **30**| **6F/12I/12A** | **6+6** |

Legend: F=execution | I=strategy/trade-offs | A=portfolio/vision/P&L

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Full Question]**

**Difficulty**: [F/I/A] | **Topic**: [Area]

**Key Insight**: [1 sentence—specific dilemma/tension]

**Answer** (150–300 words): Framework/approach [Ref: G#/A#] | ≥2 dimensions | Concrete steps | Explicit trade-offs | Stakeholder communication | Success criteria | ≥1 [Ref: ID]

**Artifact** *(optional)*: Matrix, journey, dashboard, roadmap, stakeholder map

### D. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition (1–2 sentences) | Use cases | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | User base | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (≥2 ZH)

**APA**: **A#. [Citation] [Lang]** | Books: `Author, A. (Year). *Title*. Publisher. [EN]` | Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]` | Web: `Author. (Year). *Title*. Site. URL [EN]` | Romanized ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH] (Yu, J. (2020). *Yu Jun's Product Methodology*. CITIC Press.)`

## VII. Example

**Q1: How evaluate building feature requested by top 5 enterprise customers (40% revenue) that doesn't align with product vision for mass market?**

**Difficulty**: A | **Topic**: Strategy

**Key Insight**: Tests revenue protection (enterprise retention) vs. long-term PMF (mass-market scalability); distinguishes PMs navigating executive pressure from those defaulting to pleasing customers or rigid vision.

**Answer** (248 words):

Use multi-dimensional evaluation [Ref: A1]. **First, discover JTBD** [Ref: A7]—what problem are customers solving? Surface requests often mask deeper needs revealing generalized solutions [Ref: A6].

**Second, quantify with RICE** [Ref: G2]. Enterprise: Reach (5/$2M), Impact (high retention/low acquisition), Confidence (high), Effort (unknown if custom). Mass-market: Reach (5K+ users), Impact (med/user, high cumulative), Confidence (med), Effort (similar). RICE won't capture strategic value—use decision matrix [Ref: T2].

**Third, assess against North Star** [Ref: G4]. Does this move toward outcomes or become feature factory [Ref: G9]? If generalized ("custom fields" → "flexible schema"), both segments benefit and strengthen PMF [Ref: G5].

**Finally, explore options**: (1) Generalized version; (2) Premium tier; (3) Professional services; (4) Partner ecosystem. Document precedent—product principles matter [Ref: L3]. Present analysis with clear recommendation, trade-offs, decision criteria [Ref: T2].

**Artifact**:

| Criterion           | Enterprise       | Mass Market      | Weight | E Score | M Score |
|---------------------|------------------|------------------|--------|---------|---------|
| Revenue (12mo)      | $2M (retention)  | $500K (acquisition) | 30%  | 9       | 3       |
| Strategic alignment | Low (custom)     | High (vision)    | 25%    | 2       | 9       |
| Reach               | 5 customers      | 5K+ users        | 20%    | 1       | 9       |
| Velocity impact     | High (complex)   | Low (reusable)   | 15%    | 2       | 8       |
| Competitive moat    | Low (replicable) | High (differentiator) | 10% | 3    | 9       |
| **Weighted**        |                  |                  |        | **4.8** | **7.1** |

**Recommendation**: Mass market feature + enterprise premium services
