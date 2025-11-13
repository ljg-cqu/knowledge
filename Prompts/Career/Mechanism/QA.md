# Mechanism-Focused PM Interview Q&A Generator

Generate 25–30 mechanism-analysis questions testing senior+ PM (5-15 yrs) understanding of product/system/business mechanisms via causal reasoning and systemic thinking.

## I. Context & Scope

**Purpose**: Assess senior+ PM understanding of underlying mechanisms—growth loops, user behavior, scaling dynamics, system interactions, feedback loops.

**Terminology**
- **Floor**: Minimum threshold
- **Gate**: Mandatory checkpoint (fail = stop/fix)
- **Difficulty**: F=understand, I=analyze, A=design/optimize
- **Mechanisms**: Growth/Retention/Monetization/User Behavior/Market/System

**Scope**: Causal relationships, feedback loops, system dynamics.

**Exclude**: Trivia, surface descriptions, tool-specific details, generic best practices.

**Constraints**: 150-300 words/answer (excluding artifacts) | ≥70% questions with ≥1 citation (≥30% with ≥2) | 100% mechanism-focused | Senior+ only.

**Assumptions**: Core mechanism knowledge (growth loops, network effects, habit formation, flywheels, viral coefficients, unit economics); user provides domain context or accepts generic scenarios; quantitative models require stated assumptions.

**Limitations**: Generic mechanisms lack domain nuance—customize per industry; acknowledge uncertainty for emergent behaviors.

## II. Requirements

### Quantitative Floors

| Component | Requirement |
|-----------|-------------|
| **Q&A** | 25–30 total \| 20%F/40%I/40%A (±5%) \| 150–300 words \| ≥2 causal relationships/feedback loops each |
| **Citations** | ≥70% with ≥1 cite (≥30% with ≥2) |
| **Mechanism Coverage (MECE)** | Growth (5–6) \| Retention (4–5) \| Monetization (4–5) \| User Behavior (5–6) \| Market (4–5) \| System (4–5) |
| **References** | Glossary ≥10 \| Tools ≥5 \| Literature ≥6 (≥2 ZH) \| Citations ≥12 (APA 7th + [EN]/[ZH]) |
| **Visuals** | ≥1 diagram + ≥1 table per mechanism type (6+6 minimum) |
| **Scaling** | For >30 Q&A: multiply reference floors by 1.5× |

### Citation Standards

| Aspect | Standard |
|--------|----------|
| **Format** | APA 7th + tag: `Author, A. (Year). *Title*. Publisher. [EN]` \| Inline: `[Ref: ID]` (G#/T#/L#/A#) |
| **Language** | EN 50–70% \| ZH 20–40% \| Other 5–15% |
| **Source Types** | ≥3 types: Frameworks, Research, Case studies, Tools (no type >25%) |

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

| Gate | Criterion | Mitigation |
|------|-----------|------------|
| 1. **Recency** | ≥50% from last 3yrs (≥70% for AI/ML/platform/data) | Flag dated info |
| 2. **Source Diversity** | ≥3 types; no type >25% | Expand research |
| 3. **Per-Topic Evidence** | Each mechanism type has ≥2 authoritative + ≥1 tool | Add missing sources |
| 4. **Tool Completeness** | Pricing, user base, update (≤18mo), ≥3 integrations | Complete missing fields |
| 5. **Link Validation** | 100% URLs accessible/archived | Use Web Archive or replace |
| 6. **Cross-Reference Integrity** | 100% [Ref: ID] resolve; no orphans | Fix broken references |

## III. Execution

### Step 1: Plan Allocation

Distribute 25–30 across 6 mechanism types (20%F/40%I/40%A). Each type: 4–6 Q&A with ≥1F, ≥1I, ≥1A.

**Example (30 total)**: Growth (5), Retention (5), Monetization (5), User Behavior (6), Market (4), System (5) = 6F/12I/12A

### Step 2: Build References (run Gates 1–6 after)

**Glossary (≥10)**: Growth Loops, Network Effects, Flywheels, Viral Coefficient, Habit Formation, Retention Curve, Unit Economics, Feedback Systems, Market Dynamics, Switching Costs

**Format**: Term, definition (1–2 sentences with causal explanation), mechanisms, related, limitations | Assign G1, G2...

**Tools (≥5)**: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro, Figma), Feedback (Pendo, Canny)

**Include**: Category, pricing, users, update (≤18mo), ≥3 integrations, PM use case, URL | Assign T1, T2...

**Literature (≥6)**: 
- EN—Eyal (*Hooked*), Chen (*Cold Start Problem*), Reeves (*Flywheel Effect*), Ries (*Lean Startup*)
- ZH (≥2)—俞军 (*俞军产品方法论*), 梁宁 (*产品思维30讲*), 苏杰 (*人人都是产品经理*)

**Include**: Author, title, year, mechanisms explained, relevance | Assign L1, L2...

**Citations (≥12)**: Convert to APA 7th + tags | Verify ≥50% from last 3yrs | Classify by type | Assign A1, A2...

**Alternative Sources**: Gartner, Forrester, Lenny's Newsletter, Product Coalition, HBR, MIT Sloan

### Step 3: Generate Q&A (5 at a time → self-check each batch)

**Question Design**
- **Focus**: Mechanism analysis ("Explain how...", "What drives...", "Why does X lead to Y?", "Map the feedback loop...")
- **Context**: Product type, user segment, market conditions, scale
- **Complexity**: Test ≥2 mechanism types | Single ask
- **Avoid**: "What is X?", "List Y", surface-level descriptions

**Difficulty Levels**
- **F (Foundational)**: Understanding—"How does X work?"
- **I (Intermediate)**: Analysis—"Why does X cause Y?"
- **A (Advanced)**: Design/optimization—"Design a mechanism for Z"

**Answer Structure (150–300 words)**
1. **Key Insight** (1 sentence): Core causal relationship or feedback dynamic
2. **Mechanism Explanation**: Causal chain with [Ref: G#/A#]
3. **Multi-dimensional Analysis**: ≥2 causal relationships/feedback loops
4. **Flow**: Inputs → process → outputs → feedback
5. **Quantitative Dynamics**: Rates, coefficients, time scales, thresholds
6. **Loop Types**: Reinforcing (+) / balancing (-)
7. **Metrics**: Leading/lagging indicators
8. **Citations**: ≥1 [Ref: ID]; flag low confidence
9. **Artifact** (required): Causal loop diagram, system dynamics chart, or mechanism flow

**Batch Self-Check** (per 5 Q&A)
- Mechanism-focused ✓
- Explains ≥2 causal relationships ✓
- 150–300 words ✓
- Clear causality ✓
- Includes feedback loops ✓
- ≥3/5 with ≥1 cite (≥1/5 with ≥2) ✓
- Difficulty matches content ✓

### Step 4: Create Visuals (≥1 diagram + ≥1 table per mechanism type; reference from ≥50% answers)

**By Mechanism Type**
- **Growth**: Growth loop diagram, viral coefficient chart, flywheel dynamics
- **Retention**: Retention curve, habit loop, engagement cohort
- **Monetization**: Unit economics flow, pricing feedback loop, revenue driver tree
- **User Behavior**: Behavior model (BJ Fogg), journey with trigger points, motivation-ability matrix
- **Market**: Competitive response loops, ecosystem effects, network value curves
- **System**: Feedback system diagram, causal loop, stock-and-flow chart

**Best Practices**: Diagrams for causal chains/feedback loops; tables for quantitative dynamics; include time scales; show reinforcing (+) and balancing (-) loops; cite sources

### Step 5: Populate References

**Glossary**: **G#. Term (Acronym)** | Definition (with causal explanation) | Mechanism type | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (mechanisms explained) | Relevance | Group by language (EN, then ≥2 ZH)

**Citations**: **A#. [Citation] [Lang]** | APA 7th format
- Books: `Author, A. (Year). *Title*. Publisher. [EN]`
- Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]`
- Web: `Author. (Year). *Title*. Site. URL [EN]`
- ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH] (Yu, J. (2020). *Yu Jun's Product Methodology*. CITIC Press.)`

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA have tags | Sort by ID

### Step 6: Run 12 Validations (fail ANY = stop, fix, re-run ALL)

| # | Check | Measurement | Criteria | Action |
|---|-------|-------------|----------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A) | G≥10, T≥5, L≥6, A≥12, Q:25-30, 20/40/40% | Count |
| 2 | Citations | __%≥1, __%≥2 | ≥70%≥1, ≥30%≥2 | Calculate % |
| 3 | Language | EN:__%, ZH:__%, Other:__% | EN:50-70%, ZH:20-40%, Other:5-15% | Calculate % |
| 4 | Recency | __% from 3yrs (domain: ___) | ≥50% (≥70% AI/platform) | Check dates |
| 5 | Source Types | __ types; max __% | ≥3 types, max 25% | Classify |
| 6 | Links | __/__ accessible | 100% | Test URLs |
| 7 | Cross-Refs | __/__ resolved | 100% | Validate IDs |
| 8 | Word Count | __ sampled: __ compliant | 100% (150-300) | Sample 5 |
| 9 | Key Insights | __/__ concrete | 100% causal/feedback | Review all |
| 10 | Per-Mechanism Evidence | __/6 (≥2 auth + ≥1 tool) | 6/6 | Count by type |
| 11 | Mechanism Explanation | __/__ causal+loops+cited+limits | ≥80% | Sample 10 |
| 12 | Mechanism Focus | __% mechanism-analysis | ≥70% | Review all |

### Step 7: Final Review

**Questions**: Clarity (single ask) | Signal (mechanism not trivia) | Depth (causal chains/feedback loops) | Realism (senior+ PM) | Discriminative (causal reasoning over recall) | Alignment (difficulty matches seniority)

**Answers** (sample ≥5): ≥2 causal relationships | Clear mechanism with cites | Explicit feedback loops (reinforcing/balancing) | Evidence | Leading/lagging indicators | Acknowledges limitations/assumptions/emergent properties

**Submission**: All 12 validations PASS | All floors met | All 6 gates passed | TOC with links | No placeholders | Consistent formatting | Balanced perspectives (growth vs. retention, viral vs. paid, intrinsic vs. extrinsic, network vs. content)

## IV. Validation Report (fill all; ANY fail = stop, fix, re-run ALL)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A) | G≥10, T≥5, L≥6, A≥12, Q:25-30, 20/40/40% | | PASS/FAIL |
| 2 | Citations | __%≥1, __%≥2 | ≥70%≥1, ≥30%≥2 | | PASS/FAIL |
| 3 | Language | EN:__%, ZH:__%, Other:__% | EN:50-70%, ZH:20-40%, Other:5-15% | | PASS/FAIL |
| 4 | Recency | __% from 3yrs (domain: ___) | ≥50% (≥70% AI/platform) | | PASS/FAIL |
| 5 | Source Types | __ types; max __% | ≥3 types, max 25% | | PASS/FAIL |
| 6 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 7 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 8 | Word Count | __ sampled: __ compliant | 100% (150-300) | | PASS/FAIL |
| 9 | Key Insights | __/__ concrete causal/feedback | 100% | | PASS/FAIL |
| 10 | Per-Mechanism Evidence | __/6 (≥2 auth + ≥1 tool) | 6/6 | | PASS/FAIL |
| 11 | Mechanism Explanation | __/__ causal+loops+cited+limits | ≥80% | | PASS/FAIL |
| 12 | Mechanism Focus Ratio | __% mechanism-analysis | ≥70% | | PASS/FAIL |

## V. Question Quality Checklist

Review each question; fails ≥2 criteria = rewrite/replace.

| Criterion | Description | ✓ Good | ✗ Poor |
|-----------|-------------|--------|--------|
| **Clarity** | Single ask | "Explain how LinkedIn's network effects drive growth" | "Explain LinkedIn growth and retention and monetization" |
| **Signal** | Tests mechanism understanding | "What causes Spotify's engagement loop to strengthen over time?" | "List engagement metrics" |
| **Depth** | Explores causal chains | "Map the feedback loop: content → creators → viewers → revenue → content. Where does it break?" | "Is content important?" |
| **Realism** | Senior+ PM level | "K-factor dropped from 1.2 to 0.8. Walk through the mechanism and identify failure points." | "Define viral coefficient" |
| **Discriminative** | Causal reasoning not recall | "Why does increasing free tier features sometimes reduce conversion?" | "What is freemium?" |
| **Alignment** | Difficulty matches seniority | F: understanding \| I: analyzing \| A: designing/optimizing | Mismatch between label and content |

## VI. Output Format

### A. Table of Contents
1. Mechanism Areas Overview
2. Questions by Mechanism Type (6 types)
3. References (Glossary, Tools, Literature, Citations)
4. Validation Report

### B. Mechanism Overview

**Total**: [25–30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 6 mechanism types (MECE)

| # | Mechanism Type | Range | Count | Mix | Artifacts |
|---|----------------|-------|-------|-----|-----------|
| 1 | Growth | Q1–Q5 | 5 | 1F/2I/2A | 1 diagram+table |
| 2 | Retention | Q6–Q10 | 5 | 1F/2I/2A | 1 diagram+table |
| 3 | Monetization | Q11–15 | 5 | 1F/2I/2A | 1 diagram+table |
| 4 | User Behavior | Q16–21 | 6 | 1F/2I/3A | 1 diagram+table |
| 5 | Market Dynamics | Q22–25 | 4 | 1F/2I/1A | 1 diagram+table |
| 6 | System Interactions | Q26–30 | 5 | 1F/2I/2A | 1 diagram+table |
| | **Total** | | **30** | **6F/12I/12A** | **6+6** |

Legend: F=understanding | I=analysis | A=design/optimization

### C. Q&A Format

**Mechanism Type [#]: [Title]**

**Q[#]: [Full Question]**

**Difficulty**: [F/I/A] | **Mechanism Type**: [Area]

**Key Insight**: [1 sentence—core causal relationship or feedback dynamic]

**Answer** (150–300 words):

Mechanism explanation [Ref: G#/A#] | ≥2 causal relationships | Step-by-step flow (inputs → process → outputs → feedback) | Quantitative dynamics (rates, coefficients, thresholds) | Reinforcing/balancing loops | Leading/lagging indicators | ≥1 [Ref: ID] | Limitations/assumptions

**Artifact** *(required)*: Causal loop diagram, system dynamics chart, or mechanism flow

### D. Reference Formats

**Glossary**: **G#. Term (Acronym)** | Definition (with causal explanation) | Mechanism type | Related | Limitations | Alphabetize

**Tools**: **T#. Tool (Category)** | Description | Pricing | Users | Update (Q# YYYY) | Integrations (≥3) | PM use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** | Summary (mechanisms explained) | Relevance | Group by language (EN, then ≥2 ZH)

**Citations**: **A#. [Citation] [Lang]** | APA 7th format with language tags | Sort by ID

## VII. Example

**Q1: Explain how Spotify's Daily Mix mechanism creates a reinforcing engagement loop. What makes this loop strengthen over time, and where could it break?**

**Difficulty**: I | **Mechanism Type**: User Behavior + Retention

**Key Insight**: Daily Mix creates a reinforcing feedback loop where listening data → better personalization → more listening → more data, with the loop strengthening as the recommendation model improves. The mechanism can break at the cold-start problem or if personalization becomes too narrow (filter bubble).

**Answer** (267 words):

**Mechanism Flow**: Daily Mix operates through a multi-stage feedback system [Ref: A1]. (1) **Input**: User listening history, skip patterns, playlist adds, time-of-day preferences; (2) **Process**: Collaborative filtering + content-based algorithms cluster similar users and tracks [Ref: G3]; (3) **Output**: Personalized playlists that match mood/context; (4) **Feedback**: User engagement (completion rate, skips, saves) refines the model [Ref: L2].

**Reinforcing Loop (+)**: More listening → richer data → better recommendations → higher satisfaction → more listening [Ref: G1]. This creates a **virtuous cycle** where the product becomes stickier over time. Quantitatively: users with >1000 listening sessions have 3.2× higher retention than <100 sessions [Ref: A4].

**Time Dynamics**: The loop strengthens non-linearly. Initial weeks (sessions 1-50): personalization accuracy ~65%, engagement moderate. Months 2-6 (sessions 50-500): accuracy reaches ~85%, daily active use increases 2.1× [Ref: A5]. Beyond 500 sessions: diminishing returns but sustained high engagement.

**Break Points**: (1) **Cold start**: New users lack data, generic recommendations → low engagement → churn. Mitigation: explicit onboarding questions, social graph imports [Ref: G7]. (2) **Filter bubble**: Over-optimization creates echo chamber → boredom → decreased exploration → stagnation. Mitigation: serendipity injection (15% novel tracks) [Ref: L6]. (3) **Competitive disruption**: Better algorithm elsewhere breaks lock-in.

**Leading Indicators**: Playlist completion rate (target >60%), weekly active sessions (target >5), skip rate (target <30%), new artist discovery (target >2/week).

**Limitations**: Assumes listening data accurately reflects preference (but users may listen for background noise); mechanism weakens for infrequent users (<2 sessions/week).

**Artifact**:

```
[Reinforcing Loop Diagram]

Listening History ──(+)──> Data Richness
       ↑                         │
       │                         │
       │                        (+)
       │                         │
       │                         ↓
  User Satisfaction <──(+)── Personalization
                                Quality
       │
       │
      (+) [Loop Strengthens Over Time]
       │
       ↓
   Habit Formation
       │
      (+)
       │
       ↓
More Listening ───────────────┘

[Break Points]
- Cold Start (insufficient data)
- Filter Bubble (over-optimization)
- Competitive Algorithm (external disruption)
```

| Stage | Sessions | Accuracy | Engagement | Loop Strength | Retention |
|-------|----------|----------|------------|---------------|-----------|
| Initial | 1-50 | 65% | 2.3 sessions/wk | Weak | 45% |
| Growth | 50-500 | 85% | 4.8 sessions/wk | Strong | 78% |
| Mature | 500+ | 88% | 5.4 sessions/wk | Very Strong | 92% |

**Confidence**: High (established feedback loop mechanics; supported by engagement data)
