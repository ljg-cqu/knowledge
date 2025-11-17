# PM Interview Q&A Generator (Optimized)

Generate **6-12 decision-critical scenario-based interview questions** testing senior/director/VP-level PM judgment. Focus: techniques that block decisions or create material risk (revenue >$1M, strategic pivot, churn >5%).

## I. Context & Scope (60% Reduction)

**Purpose**: Assess senior+ PM judgment (5-15 yrs) through decision-critical scenarios requiring stakeholder navigation and strategic trade-offs.

**Assumptions**: LLM knows frameworks (RICE, JTBD, OKR, North Star, PMF); user provides context or accepts generic scenarios; text/JSON output; 10-15min discussion per question.

**Constraints**: 150-250 words/answer (excluding artifacts); ≥70% citation coverage; 100% decision-critical scenarios; senior+ level only.

**Terms**: Q&A (scenario question–answer testing judgment), Floor (≥ = minimum threshold), Quality gate (mandatory checkpoint—fail = stop/fix), Difficulty (F=execution, I=strategy/trade-offs, A=portfolio/vision/P&L), Dimensions (Product/Business/Strategic/Operational).

**Scope**: Stakeholder tension, resource constraints, strategic ambiguity. **Exclude**: Trivia, greenfield design, junior tasks, domain-specific technical questions.

**Limitations**: Generic scenarios lack industry nuance (customize per industry); citation availability varies (≥50% from last 3yrs); framework application needs contextual judgment (include trade-offs/limitations); quantitative validation focuses on process (add qualitative review).

## II. Requirements

## Decision Criticality Framework (NEW - MANDATORY)

**Include if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts roadmap prioritization, go/no-go, or strategic pivot (revenue >$1M)
- **Creates Risk**: Material competitive threat, churn signal (>5% monthly), or strategic misalignment
- **Affects ≥2 Stakeholders**: Multi-team impact (PM + Exec, PM + Eng, PM + Sales, etc.)
- **Actively Evolving**: Product/market/org dynamics changing in past 3–6 months
- **Quantified Impact**: Revenue $, pipeline $, adoption %, retention %, or market share

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative

### Quantitative Floors (60% Reduction)

**Q&A**: **6-12 total** | 25%F/50%I/25%A | 150–250 words | ≥70% have ≥1 cite | Each answer addresses ≥2 dimensions

**Topic Coverage (Decision-Critical)**: 1. Strategy & Prioritization (2–3) | 2. Metrics & Decision-Making (2–3) | 3. Stakeholder Alignment (1–2) | *(Optional) GTM (1)*

**References** (build before Q&A): Glossary ≥8 terms | Tools ≥3 platforms | Literature ≥4 books (≥1 ZH) | Citations ≥6 APA 7th with [EN]/[ZH] tags

**Visuals**: ≥1 diagram + ≥1 table per topic (compressed)

### Citation Standards

**Format**: APA 7th + tag: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: ID]` (G#=Glossary, T#=Tool, L#=Literature, A#=Citation)

**Distribution**: EN 50–70% (target 60%) | ZH 20–40% (target 30%) | Other 5–15% (target 10%)

**Source Types** (≥3): Frameworks (RICE, JTBD, OST), Research/data (studies, benchmarks), Case studies (launches, postmortems), Tools (Mixpanel, ProductBoard, Dovetail)

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

1. **Recency**: ≥50% from last 3yrs (≥70% for AI/ML/platform/data)
2. **Source Diversity**: ≥3 types; no type >25%
3. **Per-Topic Evidence**: Each topic has ≥2 authoritative + ≥1 tool
4. **Tool Completeness**: Pricing, user base, update (≤18mo), ≥3 integrations
5. **Link Validation**: 100% URLs accessible/archived
6. **Cross-Reference Integrity**: 100% [Ref: ID] resolve; no orphans

**Mitigation**: Recency fail → flag dated info with caveats | Diversity fail → expand research | Link fail → use Web Archive or replace

## III. Execution

### Step 1: Plan Allocation

Decide total Q&A count (6–12) and select 3–4 decision-critical topics: Strategy & Prioritization, Metrics & Decision-Making, Stakeholder Alignment, and optional GTM.
Target overall mix 25%F/50%I/25%A; ensure each topic contributes at least one intermediate (I) question and ≥1 other difficulty across the set.
**Example** (8): Strategy & Prioritization (3: 1F/1I/1A), Metrics & Decision-Making (3: 1F/1I/1A), Stakeholder Alignment (2: 0F/2I/0A) = 2F/4I/2A (≈25/50/25)

### Step 2: Build References (BEFORE Q&A → run Gates 1–6 after)

**Glossary (≥8)**: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST + optional (HEART, Value/Effort, KANO, V2MOM, Dual-track, ICE) | Format: term, definition (1–2 sentences), use cases, related, limitations | Assign G1, G2...

**Tools (≥3)**: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro, Figma), Feedback (Pendo, Canny) | Include: category, pricing, users, update (≤18mo), ≥3 integrations, PM use case, URL | Assign T1, T2...

**Literature (≥4)**: EN—Cagan (*Inspired*), Olsen (*Lean Product Playbook*), Torres (*Continuous Discovery*) | ZH (≥1)—俞军 (*俞军产品方法论*), 梁宁 (*产品思维30讲*), 苏杰 (*人人都是产品经理*) | Include: author, title, year, summary, frameworks, relevance | Assign L1, L2...

**Citations (≥6)**: Convert to APA 7th + tags | Verify ≥50% from last 3yrs | Classify: frameworks/research/case studies/tools | Assign A1, A2... | **Alternatives**: Gartner, Forrester, Lenny's Newsletter, Product Coalition, HBR, MIT Sloan

### Step 3: Generate Q&A (5 at a time → self-check each batch)

**Question**: Scenario ("How would you...", "Walk me through...", "CEO wants X—what do?") | Include constraints (time, resources, stakeholder pressure, conflicting data) | Test ≥2 judgment signals (trade-offs, opportunity cost, stakeholder tension, incomplete info, execution complexity) | Single ask | **Avoid**: "What is X?", "List Y", "Define Z"

**Difficulty**: F=execution ("Track activation?") | I=strategy/trade-offs ("Churn vs. features?") | A=portfolio/vision/P&L ("Choose: API, mobile, or intl?")

**Answer** (150–250 words):
1. Key Insight (1 sentence): Specific dilemma/tension
2. Framework/approach [Ref: G#/A#]
3. Multi-dimensional (≥2 dimensions)
4. Concrete steps
5. Trade-offs (optimize vs. sacrifice; alternatives)
6. Stakeholder communication
7. Success criteria
8. Citations (≥1 [Ref: ID]; flag if low confidence)
9. Artifact (optional): Matrix, journey, dashboard, roadmap

**Batch Self-Check** (per 5): Scenario-based | Tests ≥2 signals | 150–250 words | Concrete insight | ≥2 dimensions | ≥3/5 have ≥1 cite (≥1/5 has ≥2) | Difficulty matches content

### Step 4: Create Visuals (≥1 diagram + ≥1 table per topic; reference from ≥50% answers)

**Strategy & Prioritization**: Roadmap (now/next/later), competitive 2×2, OST, Value/Effort 2×2, RICE table, decision matrix | **Metrics & Decision-Making**: AARRR funnel, cohort chart, dashboards, decision matrices | **Stakeholder Alignment**: Power/interest 2×2, engagement matrix | **GTM (Optional)**: Growth loop, channel strategy, launch checklist

**Best Practices**: Tables for quantitative; diagrams for workflows; include units/time periods; cite sources

### Step 5: Populate References

**Glossary**: **G#. Term (Acronym)** | Definition | Use cases | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN first, then ≥1 ZH)

**Citations**: **A#. [Citation] [Lang]** | Books: `Author, A. (Year). *Title*. Publisher. [EN]` | Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]` | Web: `Author. (Year). *Title*. Site. URL [EN]` | ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH] (Yu, J. (2020). *Yu Jun's Product Methodology*. CITIC Press.)` | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA have tags

### Step 6: Run 12 Streamlined Validations (fail ANY = stop, fix, re-run ALL)

1. **Floors**: G≥8, T≥3, L≥4, A≥6, Q=6–12, 25%F/50%I/25%A
2. **Citations**: ≥70% have ≥1 cite
3. **Decision Criticality** (NEW): 100% satisfy ≥1 criterion [Blocks/Risk/Stakeholders/Evolving/Quantified]
4. **Language**: EN 50–70%, ZH 20–40%, Other 5–15%
5. **Recency**: ≥50% from last 3yrs
6. **Links**: 100% accessible/archived
7. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans
8. **Word Count**: Sample 3; 100% within 150–250
9. **Key Insights**: 100% concrete (specific dilemma/tension)
10. **Topic Coverage**: 3-4 decision-critical topics covered
11. **Framework Usage**: ≥80% correct + cited + limitations
12. **Judgment Ratio**: ≥70% scenario-based

### Step 7: Final Review

**Questions**: Clarity (single ask) | Signal (judgment not trivia) | Depth (trade-offs) | Realism (senior+ PM) | Discriminative (application over recall) | Alignment (difficulty matches seniority)

**Answers** (sample ≥5): ≥2 dimensions | Concrete steps/frameworks with cites | Explicit trade-offs/alternatives | Evidence | Success criteria | Acknowledges limitations/assumptions

**Submission**: All 12 validations PASS | All floors met | All 6 gates passed | TOC with links | No placeholders | Consistent formatting | Balanced perspectives (test different PM philosophies: user-first vs. business-first, data-driven vs. intuition, innovation vs. execution)

## IV. Validation Report (12 Checks - Streamlined)

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥8, T≥3, L≥4, A≥6, Q:6-12, 25/50/25% | | PASS/FAIL |
| 2 | Citations          | __%≥1                                 | ≥70%≥1                              | | PASS/FAIL |
| 3 | Decision Criticality (NEW) | __/__ satisfy ≥1 criterion    | 100% [Blocks/Risk/Stakeholders/Evolving/Quantified] | | PASS/FAIL |
| 4 | Language           | EN:__%, ZH:__%, Other:__%             | EN:50-70%, ZH:20-40%, Other:5-15%   | | PASS/FAIL |
| 5 | Recency            | __% from 3yrs                         | ≥50%                                | | PASS/FAIL |
| 6 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 7 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 8 | Word Count         | __ sampled: __ compliant              | 100% (150-250)                      | | PASS/FAIL |
| 9 | Key Insights       | __/__ concrete                        | 100%                                | | PASS/FAIL |
| 10| Topic Coverage     | __/3-4 decision-critical topics       | 3-4 covered                         | | PASS/FAIL |
| 11| Frameworks         | __/__ correct+cited+limits            | ≥80%                                | | PASS/FAIL |
| 12| Judgment Ratio     | __% scenario-based                    | ≥70%                                | | PASS/FAIL |

## V. Question Quality (review each; fails ≥2 = rewrite/replace)

1. **Clarity**: Single ask | ✓ "Prioritize activation vs. churn?" | ✗ "Explain retention + database optimization"
2. **Signal**: Tests judgment | ✓ "CEO wants AI—approach?" | ✗ "List AARRR stages"
3. **Depth**: Enables trade-offs | ✓ "Choose: API, mobile, or intl—how decide?" | ✗ "Build mobile app—yes/no?"
4. **Realism**: Senior+ PM | ✓ "Sales wants 3 custom features ($5M deal). Engineering says derails roadmap. What do?" | ✗ "Design Instagram in 45min"
5. **Discriminative**: Application not recall | ✓ "When would RICE mislead? How supplement?" | ✗ "What does RICE stand for?"
6. **Alignment**: Difficulty matches seniority | F: execution | I: strategy/trade-offs | A: portfolio/vision/P&L

## VI. Output Format

### A. TOC
1. Topic Areas Overview | 2. Questions by Topic (3–4 topics) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Topic Overview (Optimized)
**Total**: [6–12] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 3-4 decision-critical PM competencies

| # | Topic          | Range  | Count | Mix      | Artifacts       | Decision Criticality |
|---|----------------|--------|-------|----------|-----------------|----------------------|
| 1 | Strategy & Prioritization | Q1–Q3  | 2–3   | 1F/1I/1A | 1 diagram+table | Blocks decision |
| 2 | Metrics & Decision-Making | Q4–Q6  | 2–3   | 1F/1I/1A | 1 diagram+table | Creates risk |
| 3 | Stakeholder Alignment | Q7–Q8  | 1–2   | 1F/1I | 1 diagram+table | Affects ≥2 roles |
| 4 | GTM (Optional) | Q9–Q12 | 1     | 1I/1A | 1 diagram+table | Actively evolving |
|   | **Total**      |        | **6–12**| **≈25%F/50%I/25%A** | **compressed** | 100% decision-critical |

Legend: F=execution | I=strategy/trade-offs | A=portfolio/vision/P&L

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Full Question]**

**Difficulty**: [F/I/A] | **Topic**: [Area]

**Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Quantified] - [Justification]

**Key Insight**: [1 sentence—specific dilemma/tension]

**Answer** (150–250 words): Framework [Ref: G#/A#] | ≥2 dimensions | Concrete steps | Trade-offs/alternatives | Stakeholder communication | Success criteria | ≥1 [Ref: ID]

**Artifact** *(optional)*: Matrix, journey, dashboard, roadmap

### D. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition | Use cases | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN, then ≥1 ZH)

**Citations**: **A#. [Citation] [Lang]** | APA 7th format with language tags

## VII. Example

**Q1: How evaluate building feature requested by top 5 enterprise customers (40% revenue) that doesn't align with product vision for mass market?**

**Difficulty**: A | **Topic**: Strategy & Prioritization

**Key Insight**: Tests revenue protection (enterprise retention) vs. long-term PMF (mass-market scalability); distinguishes PMs navigating executive pressure from those defaulting to pleasing customers or rigid vision adherence.

**Answer** (248 words):

Use multi-dimensional evaluation [Ref: A1]. **First, discover JTBD** [Ref: A7]—what problem are customers solving? Surface requests often mask deeper needs revealing generalized solutions [Ref: A6].

**Second, quantify with RICE** [Ref: G2]. Enterprise: Reach (5/$2M), Impact (high retention/low acquisition), Confidence (high), Effort (unknown if custom). Mass-market: Reach (5K+ users), Impact (med/user, high cumulative), Confidence (med), Effort (similar). RICE won't capture strategic value—use decision matrix [Ref: T2].

**Third, assess against North Star** [Ref: G4]. Does this move toward outcomes or become feature factory [Ref: G9]? If generalized ("custom fields" → "flexible schema"), both segments benefit and strengthen PMF [Ref: G5].

**Trade-offs**: (1) Enterprise version: protects $2M but risks fragmentation/debt; (2) Generalized version: serves both but longer timeline/higher uncertainty; (3) Decline: maintains vision but risks churn/competition; (4) Premium tier: monetizes customization but adds operational complexity.

**Alternatives**: Professional services, partner ecosystem, configuration tools [Ref: L3].

**Stakeholder communication**: Present analysis with recommendation, trade-offs, criteria, precedent implications—product principles matter [Ref: T2].

**Success criteria**: If built, measure enterprise retention (+20%), mass-market adoption (≥30% use within 6mo), tech debt (≤10% velocity impact), support costs (flat/declining).

**Limitations**: Assumes enterprise needs are generalizable; may not apply if truly custom.

**Artifact**:

| Criterion           | Enterprise       | Mass Market      | Weight | E Score | M Score |
|---------------------|------------------|------------------|--------|---------|---------|
| Revenue (12mo)      | $2M (retention)  | $500K (acquisition) | 30%  | 9       | 3       |
| Strategic alignment | Low (custom)     | High (vision)    | 25%    | 2       | 9       |
| Reach               | 5 customers      | 5K+ users        | 20%    | 1       | 9       |
| Velocity impact     | High (complex)   | Low (reusable)   | 15%    | 2       | 8       |
| Competitive moat    | Low (replicable) | High (differentiator) | 10% | 3    | 9       |
| **Weighted**        |                  |                  |        | **4.8** | **7.1** |

**Recommendation**: Generalized mass-market feature + enterprise premium services for edge cases

**Confidence**: High (established frameworks; common PM dilemma)
