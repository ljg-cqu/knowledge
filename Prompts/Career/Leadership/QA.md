# Leadership Interview Q&A Generator

Generate 25–30 scenario-based questions testing senior+ leadership judgment with evidence-based answers, artifacts, and validation.

## I. Foundation

**Purpose**: Assess senior+ leadership (5-15 yrs) through multi-dimensional scenarios testing people leadership, transformation, strategic execution.

**Scope**: Team development, change management, strategic ambiguity, culture, conflict, org design.  
**Exclude**: Trivia, theory-only, junior tasks, domain-specific technical.

**Constraints**: 150-300 words/answer; ≥70% have ≥1 citation (≥30% have ≥2); 100% scenario-based; senior+ only.

**Key Terms**:
- **Floor**: Minimum threshold
- **Gate**: Mandatory checkpoint (fail = stop/fix)
- **Difficulty**: F (execution) | I (strategic/systemic) | A (transformation/culture)
- **Dimensions**: People | Strategic | Operational | Cultural

**Assumptions**: LLM knows frameworks (Situational Leadership, Kotter, OKR, GROW, Radical Candor, Team Topologies, 5 Dysfunctions); 10-15min/question.

**Limitations**: Generic scenarios lack industry context; ≥50% citations from last 3yrs required; framework trade-offs must be explicit; quantitative validation needs qualitative review.

## II. Requirements

### Quantitative Floors

**Q&A**: 25–30 total | 20%F/40%I/40%A (±5%) | 150–300 words | ≥70% have ≥1 cite (≥30% have ≥2) | ≥2 dimensions/answer

**Topics (MECE)**: Vision & Strategy (4–5) | People Leadership (5–6) | Change Management (4–5) | Team & Culture (5–6) | Communication (4–5) | Org Design (4–5)

**References** (build before Q&A): Glossary ≥10 | Tools ≥5 | Literature ≥6 (≥2 ZH: 陈春花, 刘澜, 宁向东) | Citations ≥12 APA 7th + [EN]/[ZH] tags

**Visuals**: ≥1 diagram + ≥1 table/topic (6+6 minimum)

**Scaling**: >30 Q&A → multiply reference floors by 1.5×

### Citation Standards

**Format**: Inline `[Ref: ID]` where ID = G#(Glossary) | T#(Tool) | L#(Literature) | A#(Citation)

**APA 7th Examples**:
- Book: `Author, A. (Year). *Title*. Publisher. [EN]`
- Article: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]`
- Web: `Author. (Year). *Title*. Site. URL [EN]`
- ZH: `陈春花. (2019). *管理的常识*. 机械工业出版社. [ZH] (Chen, C. (2019). *Common Sense of Management*. China Machine Press.)`

**Distribution**: EN 50–70% | ZH 20–40% | Other 5–15%

**Source Types** (≥3): Frameworks, Research, Case studies, Tools

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

1. **Recency**: ≥50% from last 3yrs (≥70% for remote/hybrid/AI leadership)
2. **Diversity**: ≥3 source types; no type >25%
3. **Per-Topic**: Each has ≥2 authoritative + ≥1 tool
4. **Tool Completeness**: Pricing, users, update (≤18mo), ≥3 integrations
5. **Links**: 100% accessible/archived
6. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans

**Mitigation**: Recency fail → flag with caveats | Diversity fail → expand research | Link fail → Web Archive/replace

## III. Execution

### Step 1: Plan Allocation

Distribute 25–30 across 6 topics (20%F/40%I/40%A). Each topic: 4–6 Q&A with ≥1F, ≥1I, ≥1A.

**Example** (30): Vision (5), People (6), Change (5), Culture (5), Comm (4), Org (5) = 6F/12I/12A

### Step 2: Build References (BEFORE Q&A → run Gates 1–6 after)

**Glossary (≥10)**: Situational Leadership, GROW, Servant Leadership, Transformational Leadership, Radical Candor, Psychological Safety, Team Topologies, 5 Dysfunctions, Kotter's 8-Steps, OKR + optional (RACI, Span of Control, Conway's Law, Growth Mindset, 1-on-1s)  
**Format**: **G#. Term (Acronym)** | Definition (1–2 sentences) | Use cases | Related | Limitations | Alphabetize

**Tools (≥5)**: Performance (15Five, Lattice), Engagement (Culture Amp, Officevibe), Feedback (360 tools, Reflektive), Development (LinkedIn Learning, Degreed), Collaboration (Miro, Slack)  
**Format**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | Use case | URL | Group by category

**Literature (≥6)**: EN—Covey (*7 Habits*), Collins (*Good to Great*), Sinek (*Leaders Eat Last*), Brown (*Dare to Lead*), Kim (*Phoenix Project*), Lencioni (*5 Dysfunctions*) | ZH (≥2)—陈春花 (*管理的常识*), 刘澜 (*领导力沉思录*), 宁向东 (*清华管理课*)  
**Format**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN, then ZH)

**Citations (≥12)**: Convert to APA 7th + tags | Verify ≥50% from last 3yrs | Classify: frameworks/research/cases/tools | Assign A1, A2... | **Alternatives**: HBR, MIT Sloan, McKinsey, Gallup, Gartner HR, DDI Forecast  
**Format**: **A#. [Full APA Citation] [Lang]** | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA have tags

### Step 3: Generate Q&A (5 at a time → self-check each batch)

**Question**: Scenario format ("How would you...", "Walk me through...", "Your team faces X—what do?") | Include constraints (time, resources, stakeholder pressure, conflicting priorities, dynamics) | Test ≥2 judgment signals (trade-offs, people impact, cultural implications, incomplete info, resistance) | Single ask  
**Avoid**: "What is X?", "List Y", "Define Z"

**Difficulty Tags**: F=execution ("Improve 1-on-1s?") | I=strategic ("Restructure underperforming org?") | A=transformation ("Build trust culture in 18mo?")

**Answer Structure** (150–300 words):
1. **Key Insight** (1 sentence): Specific leadership dilemma/tension
2. **Framework/approach** [Ref: G#/A#]
3. **Multi-dimensional** (≥2: People/Strategic/Operational/Cultural)
4. **Concrete steps**
5. **Trade-offs** (optimize vs. sacrifice; alternatives)
6. **People/stakeholder impact**
7. **Success criteria**
8. **Citations** (≥1 [Ref: ID]; flag if low confidence)
9. **Artifact** (optional): Org chart, matrix, roadmap, plan

**Batch Self-Check** (per 5): Scenario-based ✓ | Tests ≥2 signals ✓ | 150–300 words ✓ | Concrete insight ✓ | ≥2 dimensions ✓ | ≥3/5 have ≥1 cite (≥1/5 has ≥2) ✓ | Difficulty matches content ✓

### Step 4: Create Visuals (≥1 diagram + ≥1 table/topic; reference from ≥50% answers)

**By Topic**:
- **Vision**: Strategic roadmap, vision cascade, SWOT
- **People**: Development matrix, 9-box, succession plan
- **Change**: Kotter timeline, stakeholder map, impact matrix
- **Culture**: Values assessment, behavior matrix, engagement dashboard
- **Communication**: Stakeholder matrix, communication plan
- **Org**: Structure, RACI, team topology

**Best Practices**: Tables for quantitative data; diagrams for workflows; include roles/timelines; cite sources

### Step 5: Run 12 Validations (fail ANY = stop, fix, re-run ALL)

| # | Check              | Criteria                            | Measurement |
|---|--------------------|-------------------------------------|-------------|
| 1 | Floors             | G≥10, T≥5, L≥6, A≥12, Q:25-30, 20/40/40% (±5%) | Count all |
| 2 | Citations          | ≥70% have ≥1; ≥30% have ≥2          | % by question |
| 3 | Language           | EN:50-70%, ZH:20-40%, Other:5-15%   | % by citation |
| 4 | Recency            | ≥50% from last 3yrs (≥70% remote/hybrid) | % by date |
| 5 | Source Types       | ≥3 types; no type >25%              | Count types |
| 6 | Links              | 100% accessible/archived            | Test all URLs |
| 7 | Cross-Refs         | 100% [Ref: ID] resolve; no orphans  | Check all refs |
| 8 | Word Count         | 100% within 150-300                 | Sample 5+ |
| 9 | Key Insights       | 100% concrete (specific dilemma/tension) | Review all |
| 10| Per-Topic Evidence | 6/6 have ≥2 authoritative + ≥1 tool | Per-topic check |
| 11| Frameworks         | ≥80% correct + cited + limitations  | Review usage |
| 12| Judgment Ratio     | ≥70% scenario-based                 | % testing judgment |

### Step 6: Final Review

**Questions** (spot-check ≥5): Clarity (single ask) | Signal (judgment not trivia) | Depth (trade-offs/impact) | Realism (senior+ leader) | Discriminative (application over recall) | Alignment (difficulty matches seniority)

**Answers** (spot-check ≥5): ≥2 dimensions | Concrete steps/frameworks with cites | Explicit trade-offs/alternatives | People impact | Success criteria | Acknowledges limitations/assumptions

**Submission**: All 12 validations PASS | All floors met | All gates passed | TOC with links | No placeholders | Consistent formatting | Balanced perspectives (directive vs. empowering, transformation vs. stability, people-first vs. results-first, inclusive vs. decisive)

## IV. Output Format

### A. TOC
1. Topic Overview | 2. Questions by Topic (6 topics) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Topic Overview

**Total**: [25–30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 6 leadership competencies (MECE)

| # | Topic                    | Range  | Count | Mix      | Artifacts       |
|---|--------------------------|--------|-------|----------|-----------------|
| 1 | Vision & Strategy        | Q1–Q5  | 5     | 1F/2I/2A | 1 diagram+table |
| 2 | People Leadership        | Q6–Q11 | 6     | 1F/2I/3A | 1 diagram+table |
| 3 | Change Management        | Q12–16 | 5     | 1F/2I/2A | 1 diagram+table |
| 4 | Team Building & Culture  | Q17–21 | 5     | 1F/2I/2A | 1 diagram+table |
| 5 | Communication/Influence  | Q22–25 | 4     | 1F/2I/1A | 1 diagram+table |
| 6 | Org Design & Operations  | Q26–30 | 5     | 1F/2I/2A | 1 diagram+table |
|   | **Total**                |        | **30**| **6F/12I/12A** | **6+6** |

Legend: F=execution | I=strategic/systemic | A=transformation/culture

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Full Question]**

**Difficulty**: [F/I/A] | **Topic**: [Area]

**Key Insight**: [1 sentence—specific leadership dilemma/tension]

**Answer** (150–300 words): Framework [Ref: G#/A#] | ≥2 dimensions | Concrete steps | Trade-offs/alternatives | People/stakeholder impact | Success criteria | ≥1 [Ref: ID]

**Artifact** *(optional)*: Org chart, matrix, roadmap, plan

### D. Reference Sections

**Glossary**: **G#. Term (Acronym)** | Definition | Use cases | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN, then ZH)

**Citations**: **A#. [Full APA Citation] [Lang]** | Sort by ID

## V. Quality Criteria

### Question Quality (review each; fails ≥2 = rewrite/replace)

1. **Clarity**: Single ask | ✓ "Lead merger of 2 teams with conflicting cultures?" | ✗ "Explain trust + optimize sprint velocity"
2. **Signal**: Tests judgment | ✓ "Top performer toxic to team—approach?" | ✗ "List 5 Dysfunctions stages"
3. **Depth**: Enables trade-offs | ✓ "Choose: fast growth vs. sustainable culture—how decide?" | ✗ "Build culture—yes/no?"
4. **Realism**: Senior+ leader | ✓ "Board demands 30% cost cut. 2 options: deep layoffs or kill innovation. What do?" | ✗ "Design perfect org chart"
5. **Discriminative**: Application not recall | ✓ "When would Situational Leadership fail? How adapt?" | ✗ "What is Situational Leadership?"
6. **Alignment**: Difficulty matches seniority | F: execution | I: strategic/systemic | A: transformation/culture

## VI. Validation Report Template

| # | Check              | Measurement                           | Criteria                            | Result | Status    |
|---|--------------------|---------------------------------------|-------------------------------------|--------|-----------|
| 1 | Floors             | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A)| G≥10, T≥5, L≥6, A≥12, Q:25-30, 20/40/40% | | PASS/FAIL |
| 2 | Citations          | __%≥1, __%≥2                          | ≥70%≥1, ≥30%≥2                      | | PASS/FAIL |
| 3 | Language           | EN:__%, ZH:__%, Other:__%             | EN:50-70%, ZH:20-40%, Other:5-15%   | | PASS/FAIL |
| 4 | Recency            | __% from 3yrs (domain: ___)           | ≥50% (≥70% remote/hybrid)           | | PASS/FAIL |
| 5 | Source Types       | __ types; max __%                     | ≥3 types, max 25%                   | | PASS/FAIL |
| 6 | Links              | __/__ accessible                      | 100%                                | | PASS/FAIL |
| 7 | Cross-Refs         | __/__ resolved                        | 100%                                | | PASS/FAIL |
| 8 | Word Count         | __ sampled: __ compliant              | 100% (150-300)                      | | PASS/FAIL |
| 9 | Key Insights       | __/__ concrete                        | 100%                                | | PASS/FAIL |
| 10| Per-Topic Evidence | __/6 (≥2 auth + ≥1 tool)              | 6/6                                 | | PASS/FAIL |
| 11| Frameworks         | __/__ correct+cited+limits            | ≥80%                                | | PASS/FAIL |
| 12| Judgment Ratio     | __% scenario-based                    | ≥70%                                | | PASS/FAIL |

## VII. Example

**Q1: How would you lead a team through a major reorganization where 40% of roles are being eliminated, including some of your direct reports, while maintaining productivity and morale?**

**Difficulty**: A | **Topic**: Change Management & People Leadership

**Key Insight**: Tests balancing empathy (supporting impacted) with accountability (maintaining performance) and transparency (honest communication) vs. confidentiality (legal/HR constraints); distinguishes leaders navigating ambiguity from those avoiding difficult conversations or over-indexing on results vs. relationships.

**Answer** (267 words):

Use Kotter's change framework [Ref: G9] with Radical Candor [Ref: G7]. **Phase 1: Pre-announcement (1-2 weeks)**: Work with HR/legal on timeline, severance, messaging. Identify retention risks. Prepare managers for reactions [Ref: A4]. Create urgency narrative: why change necessary, consequences of inaction.

**Phase 2: Communication (Day 1-3)**: **Transparency with compassion** [Ref: G7]. Announce promptly—delays breed rumors. Explain strategic rationale, decision criteria (role-based not performance), support for impacted. One-on-ones with departing reports first (dignity, gratitude, references, outplacement). All-hands for remaining: acknowledge pain, future vision, expectations. **Avoid**: generic platitudes, false optimism, defensive posture [Ref: L4].

**Phase 3: Stabilization (Week 2-8)**: **Psychological safety** [Ref: G8]—create space for grief/anger. Redistribute work transparently using RACI [Ref: T3]. Weekly check-ins on workload/morale. Quick wins to rebuild momentum. Celebrate departing colleagues (alumni network, references) [Ref: A6].

**Trade-offs**: (1) Fast transition: reduces uncertainty but feels callous; (2) Gradual: extends pain but allows adjustment; (3) Over-communicate: builds trust but time-intensive; (4) Minimal: protects confidentiality but breeds distrust.

**Success criteria**: Retention of key talent (>90%), engagement scores (≤15% drop), productivity maintained (≥85% within 4 weeks), alumni sentiment (positive references).

**People impact**: Prioritize dignity for departing, clarity for staying, support for all. **Limitations**: Assumes some control; senior leaders may constrain communication.

**Artifact**:

| Week | Leadership Action | Team Impact | Communication | Support Structure |
|------|-------------------|-------------|---------------|-------------------|
| -2   | Align with HR/legal | Rumors starting | None (confidential) | Prep managers |
| 1    | Announce + 1-on-1s | High anxiety | All-hands + individual | EAP, outplacement |
| 2-4  | Stabilize + redistribute | Grief/uncertainty | Weekly updates | Increased 1-on-1s |
| 5-8  | Quick wins + celebrate | Cautious optimism | Bi-weekly + wins | Workload monitoring |
| 9-12 | New normal + vision | Commitment rebuilding | Monthly + strategy | Career development |

**Recommendation**: Transparent communication + empathetic execution + rapid stabilization

**Confidence**: High (established frameworks; common leadership challenge)
