# Leadership News Tracking Q&A Generator (Minimal Viable)

Generate 6–12 decision-critical leadership Q&As (senior+, 5-15 yrs) for informed decisions with limited time.

## I. Foundation

**Scope**: Decision-critical leadership scenarios only—blocks decisions or creates material risk.  
**Exclude**: Trivia, theory-only, junior tasks, niche/legacy, nice-to-have trends, speculation.

**Constraints**: 150–250 words/answer; ≥70% have ≥1 citation; 100% scenario-based; 100% decision-critical.

**Terminology**:
- **Floor**: Minimum threshold
- **Gate**: Mandatory checkpoint (fail = stop/fix)
- **Difficulty**: F (execution) | I (strategic/systemic) | A (transformation/culture)
- **Decision Criticality**: [Blocks/Risk/Roles/Evolving/Adoption] ← **NEW (mandatory)**

**Assumptions**: LLM knows core frameworks (Situational Leadership, Kotter, Radical Candor, Psychological Safety).

**Limitations**: Scenarios lack industry context; ≥50% citations from last 3yrs; trade-offs must be explicit; decision-critical focus only.

## II. Requirements

### Quantitative Floors (60% Reduction)

**Q&A**: 6–12 total | 25%F/50%I/25%A (±5%) | 150–250 words | ≥70% have ≥1 cite | ≥2 dimensions/answer | **100% decision-critical**

**Topics (Decision-Critical Only)**: 3–4 topics × 1–3 Q&As each
- Strategic Leadership (1–2): Blocks decision, Affects ≥2 stakeholders
- People & Retention (1–2): Creates risk, Actively evolving (remote/hybrid/AI)
- Change & Ambiguity (1–2): Blocks decision, High adoption barrier
- Culture & Trust (1–2): Creates risk, Affects ≥2 stakeholders
- *(Optional)* Communication or Org Design (if decision-critical)

**References** (proportional 60% reduction): Glossary ≥8 | Tools ≥3 | Literature ≥4 (≥1 ZH) | Citations ≥6 APA 7th + [EN]/[ZH] tags

**Visuals** (60% reduction): ≥2 diagrams + ≥1 table total (vs. 6+6 for full template)

### Decision Criticality Framework (NEW—MANDATORY)

**Include Q&A if ≥1 criterion satisfied**:
- **Blocks Decision**: Directly impacts go/no-go, resource allocation, or strategic pivot (e.g., "Restructure org?" "Promote/exit key leader?")
- **Creates Risk**: Material threat (team morale, retention, compliance, performance) with quantified impact
- **Affects ≥2 Stakeholders**: Multi-team impact (CEO + Board, VP + Team Leads, etc.)
- **Actively Evolving**: Leadership dynamics changing in past 6–12 months (remote/hybrid, AI, generational shifts, market disruption)
- **High Adoption Barrier**: >40h to learn/implement; blocks velocity or compliance

**Exclude if**: Niche/legacy (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative/rumors

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

1. **Decision Criticality**: 100% of Q&As satisfy ≥1 criterion (Blocks/Risk/Roles/Evolving/Adoption)
2. **Recency**: ≥50% from last 3yrs (≥70% for remote/hybrid/AI leadership)
3. **Diversity**: ≥2 source types; no type >50%
4. **Links**: 100% accessible/archived
5. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans

**Mitigation**: Decision Criticality fail → rewrite/replace | Recency fail → flag with caveats | Link fail → Web Archive/replace

## III. Execution (Streamlined for 6–12 Q&As)

### Step 1: Plan Allocation (Decision-Critical Only)

Distribute 6–12 across 3–4 decision-critical topics (25%F/50%I/25%A).

**Example** (10): Strategic Leadership (2), People & Retention (2), Change & Ambiguity (3), Culture & Trust (3) = 2–3F/5I/2–3A

**Justification Required**: Each Q&A must state which criterion it satisfies: [Blocks/Risk/Roles/Evolving/Adoption]

### Step 2: Build References (BEFORE Q&A → run Gates 1–5 after)

**Glossary (≥8)**: Radical Candor, Psychological Safety, Situational Leadership, Kotter's 8-Steps, Transformational Leadership, GROW, Team Topologies, 5 Dysfunctions  
**Format**: **G#. Term (Acronym)** | Definition (1–2 sentences) | Use cases | Limitations | Alphabetize

**Tools (≥3)**: Engagement (Culture Amp), Feedback (15Five), Collaboration (Miro)  
**Format**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥2) | Use case | URL

**Literature (≥4)**: EN—Brown (*Dare to Lead*), Sinek (*Leaders Eat Last*) | ZH (≥1)—陈春花 (*管理的常识*)  
**Format**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language

**Citations (≥6)**: APA 7th + tags | Verify ≥50% from last 3yrs | Assign A1, A2... | **Alternatives**: HBR, McKinsey, Gallup  
**Format**: **A#. [Full APA Citation] [Lang]** | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA have tags

### Step 3: Generate Q&A (2–3 at a time → self-check each batch)

**Question**: Scenario format ("How would you...", "Walk me through...", "Your team faces X—what do?") | Include constraints (time, resources, stakeholder pressure) | Test ≥2 judgment signals (trade-offs, people impact, incomplete info) | Single ask  
**Avoid**: "What is X?", "List Y", "Define Z"

**Difficulty Tags**: F=execution | I=strategic/systemic | A=transformation/culture

**Decision Criticality Tag** (MANDATORY): [Blocks/Risk/Roles/Evolving/Adoption] + 1-sentence justification

**Answer Structure** (150–250 words):
1. **Key Insight** (1 sentence): Specific leadership dilemma/tension
2. **Framework/approach** [Ref: G#/A#]
3. **Multi-dimensional** (≥2: People/Strategic/Operational/Cultural)
4. **Concrete steps** (3–5 bullets)
5. **Trade-offs** (≥2 alternatives)
6. **People/stakeholder impact**
7. **Success criteria**
8. **Citations** (≥1 [Ref: ID])

**Batch Self-Check** (per 2–3): Scenario-based ✓ | Tests ≥2 signals ✓ | 150–250 words ✓ | Decision-critical ✓ | ≥2 dimensions ✓ | ≥1 cite ✓ | Difficulty matches content ✓

### Step 4: Create Visuals (Compressed—≥2 diagrams + ≥1 table total)

**Minimal Viable** (60% reduction):
- **Strategic Leadership**: Decision tree or roadmap (1 diagram)
- **People & Retention**: Development matrix or 9-box (1 diagram)
- **Change & Ambiguity**: Kotter timeline or stakeholder map (1 table)
- **Culture & Trust**: Values/behavior matrix (1 table)

**Best Practices**: Mermaid for workflows; tables for matrices; include roles/timelines; cite sources

### Step 5: Run 12 Validations (fail ANY = stop, fix, re-run ALL)

| # | Check                  | Criteria                                    | Measurement |
|----|------------------------|---------------------------------------------|-------------|
| 1  | Floors                 | G≥8, T≥3, L≥4, A≥6, Q:6-12, 25/50/25% (±5%) | Count all |
| 2  | Decision Criticality   | 100% satisfy ≥1 criterion [Blocks/Risk/Roles/Evolving/Adoption] | Review all |
| 3  | Citations              | ≥70% have ≥1 cite                           | % by question |
| 4  | Language               | EN:50-70%, ZH:20-40%, Other:5-15%           | % by citation |
| 5  | Recency                | ≥50% from last 3yrs (≥70% remote/hybrid)    | % by date |
| 6  | Diversity              | ≥2 source types; no type >50%               | Count types |
| 7  | Links                  | 100% accessible/archived                    | Test all URLs |
| 8  | Cross-Refs             | 100% [Ref: ID] resolve; no orphans          | Check all refs |
| 9  | Word Count             | 100% within 150-250                         | Sample all |
| 10 | Key Insights           | 100% concrete (specific dilemma/tension)    | Review all |
| 11 | Frameworks             | ≥80% correct + cited                        | Review usage |
| 12 | Judgment Ratio         | ≥70% scenario-based                         | % testing judgment |

### Step 6: Final Review

**Questions** (spot-check ≥5): Clarity (single ask) | Signal (judgment not trivia) | Depth (trade-offs/impact) | Realism (senior+ leader) | Discriminative (application over recall) | Alignment (difficulty matches seniority)

**Answers** (spot-check ≥5): ≥2 dimensions | Concrete steps/frameworks with cites | Explicit trade-offs/alternatives | People impact | Success criteria | Acknowledges limitations/assumptions

**Submission**: All 12 validations PASS | All floors met | All gates passed | TOC with links | No placeholders | Consistent formatting | Balanced perspectives (directive vs. empowering, transformation vs. stability, people-first vs. results-first, inclusive vs. decisive)

## IV. Output Format (Minimal Viable)

### A. TOC
1. Topic Overview | 2. Questions by Topic (3–4 topics) | 3. References (Glossary, Tools, Literature, Citations) | 4. Validation Report

### B. Topic Overview

**Total**: [6–12] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 3–4 decision-critical leadership areas

| # | Topic                   | Range   | Count | Mix        | Artifacts |
|---|-------------------------|---------|-------|------------|-----------|
| 1 | Strategic Leadership    | Q1–Q2   | 1–2   | 0–1F/1–2I/0–1A | 1 diagram |
| 2 | People & Retention      | Q3–Q4   | 1–2   | 0–1F/1–2I/0–1A | 1 diagram |
| 3 | Change & Ambiguity      | Q5–Q7   | 2–3   | 1F/1–2I/1A | 1 table |
| 4 | Culture & Trust         | Q8–Q10  | 2–3   | 0–1F/1–2I/1–2A | 1 table |
|   | **Total**               |         | **6–12** | **2–3F/5I/2–3A** | **≥2 diagrams + ≥1 table** |

Legend: F=execution | I=strategic/systemic | A=transformation/culture | **Decision-Critical Only**

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Full Question]**

**Difficulty**: [F/I/A] | **Topic**: [Area] | **Decision Criticality**: [Blocks/Risk/Roles/Evolving/Adoption]

**Criticality Justification**: [1 sentence—why this Q&A is decision-critical]

**Key Insight**: [1 sentence—specific leadership dilemma/tension]

**Answer** (150–250 words): Framework [Ref: G#/A#] | ≥2 dimensions | Concrete steps (3–5 bullets) | Trade-offs/alternatives | People/stakeholder impact | Success criteria | ≥1 [Ref: ID]

**Artifact** *(optional)*: Diagram, matrix, or roadmap

### D. Reference Sections (Minimal Viable—60% Reduction)

**Glossary (≥8)**: **G#. Term (Acronym)** | Definition (1–2 sentences) | Use cases | Limitations | Alphabetize

**Tools (≥3)**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥2) | Use case | URL

**Literature (≥4)**: **L#. Author, Title, Year** | Summary (focus/frameworks) | Relevance | Group by language (EN, then ZH)

**Citations (≥6)**: **A#. [Full APA Citation] [Lang]** | Sort by ID

## V. Quality Criteria

### Question Quality (review each; fails ≥2 = rewrite/replace)

1. **Clarity**: Single ask | ✓ "Lead merger of 2 teams with conflicting cultures?" | ✗ "Explain trust + optimize sprint velocity"
2. **Signal**: Tests judgment | ✓ "Top performer toxic to team—approach?" | ✗ "List 5 Dysfunctions stages"
3. **Depth**: Enables trade-offs | ✓ "Choose: fast growth vs. sustainable culture—how decide?" | ✗ "Build culture—yes/no?"
4. **Realism**: Senior+ leader | ✓ "Board demands 30% cost cut. 2 options: deep layoffs or kill innovation. What do?" | ✗ "Design perfect org chart"
5. **Discriminative**: Application not recall | ✓ "When would Situational Leadership fail? How adapt?" | ✗ "What is Situational Leadership?"
6. **Alignment**: Difficulty matches seniority | F: execution | I: strategic/systemic | A: transformation/culture

## VI. Validation Report Template (Minimal Viable)

| # | Check                  | Measurement                         | Criteria                                    | Result | Status    |
|----|------------------------|-------------------------------------|---------------------------------------------|--------|-----------|
| 1  | Floors                 | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A) | G≥8, T≥3, L≥4, A≥6, Q:6-12, 25/50/25% | | PASS/FAIL |
| 2  | Decision Criticality   | __/__ satisfy ≥1 criterion          | 100% [Blocks/Risk/Roles/Evolving/Adoption]  | | PASS/FAIL |
| 3  | Citations              | __%≥1                               | ≥70%≥1                                      | | PASS/FAIL |
| 4  | Language               | EN:__%, ZH:__%, Other:__%           | EN:50-70%, ZH:20-40%, Other:5-15%           | | PASS/FAIL |
| 5  | Recency                | __% from 3yrs (domain: ___)         | ≥50% (≥70% remote/hybrid)                   | | PASS/FAIL |
| 6  | Diversity              | __ types; max __%                   | ≥2 types, max 50%                           | | PASS/FAIL |
| 7  | Links                  | __/__ accessible                    | 100%                                        | | PASS/FAIL |
| 8  | Cross-Refs             | __/__ resolved                      | 100%                                        | | PASS/FAIL |
| 9  | Word Count             | __ sampled: __ compliant            | 100% (150-250)                              | | PASS/FAIL |
| 10 | Key Insights           | __/__ concrete                      | 100%                                        | | PASS/FAIL |
| 11 | Frameworks             | __/__ correct+cited                 | ≥80%                                        | | PASS/FAIL |
| 12 | Judgment Ratio         | __% scenario-based                  | ≥70%                                        | | PASS/FAIL |

## VII. Example (Decision-Critical Leadership Q&A)

**Q1: How would you lead a team through a major reorganization where 40% of roles are being eliminated, including some of your direct reports, while maintaining productivity and morale?**

**Difficulty**: A | **Topic**: Change Management & People Leadership | **Decision Criticality**: [Blocks/Risk]

**Criticality Justification**: Blocks decision on communication strategy & retention approach; creates material risk (key talent loss, morale collapse, compliance issues).

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
