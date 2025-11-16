# Mechanism-Focused PM Interview Q&A Generator

Generate 18 mechanism-analysis questions testing senior+ PM (5-15 yrs) causal reasoning and systemic thinking.

## I. Foundation

**Purpose**: Assess understanding of growth loops, user behavior, scaling dynamics, system interactions, feedback loops.

**Terminology**: Floor=minimum | Gate=mandatory checkpoint (fail=stop/fix) | Difficulty: F=understand, I=analyze, A=design/optimize | Mechanisms: Growth/Retention/Monetization/User Behavior/Market/System

**Scope**: Causal relationships, feedback loops, system dynamics.

**Exclude**: Trivia, surface descriptions, tool details, generic practices.

**Constraints**: 150-300 words/answer | ≥70% with ≥1 citation (≥30% with ≥2) | 100% mechanism-focused | Senior+ only.

**Assumptions**: Core mechanism knowledge; user provides domain context or accepts generic scenarios; quantitative models state assumptions.

**Limitations**: Generic mechanisms lack domain nuance—customize per industry; flag uncertainty for emergent behaviors.

## II. Requirements & Gates

**Floors**: QQ&A: 25–30 (20%F/40%I/40%A±5%)A: 18 (20%F/40%I/40%A±5%) | 150–300 words | ≥2 causal/feedback each | Citations: ≥70%≥1, ≥30%≥2 | Mechanisms (MECE): Growth(3), Retention(3), Monetization(3), User Behavior(3), Market(3), System(3) | Refs: G≥10, T≥5, L≥6(≥2 ZH), A≥12 | Visuals: ≥1 diagram+table/type (12 min) | 

**Citations**: APA 7th+tag: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: G#/T#/L#/A#]` | Lang: EN 50–70%, ZH 20–40%, Other 5–15% | Types: ≥3 (Frameworks/Research/Cases/Tools); no type >25%

**Gates** (fail any=stop/fix/re-validate all):
1. **Recency**: ≥50% <3yrs (≥70% AI/ML/platform/data) | Flag dated
2. **Diversity**: ≥3 types; max 25% | Expand
3. **Evidence**: Each mechanism type ≥2 auth+≥1 tool | Add sources
4. **Tool Data**: Pricing, users, update≤18mo, ≥3 integrations | Complete
5. **Links**: 100% accessible/archived | Archive/replace
6. **Cross-Refs**: 100% resolve; no orphans | Fix

## III. Execution

### Step 1: Plan
Distribute 18 across 6 types (20%F/40%I/40%A). Each: 3 QEach: 4–6 Q&A with ≥1F, ≥1I, ≥1A.A with 1F, 1I, 1A.
**Example (18)**: Growth(3), Retention(3), Monetization(3), User Behavior(3), Market(3), System(3) = 4F/7I/7A

### Step 2: Build References (run Gates 1–6 after)

**Glossary (≥10)**: Growth Loops, Network Effects, Flywheels, Viral Coefficient, Habit Formation, Retention Curve, Unit Economics, Feedback Systems, Market Dynamics, Switching Costs
**Format**: Term | definition (1–2 sent w/ causal) | mechanisms | related | limits | ID: G1...

**Tools (≥5)**: Analytics (Mixpanel, Amplitude), Roadmap (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collab (Miro, Figma), Feedback (Pendo, Canny)
**Include**: Category | pricing | users | update≤18mo | ≥3 integrations | use case | URL | ID: T1...

**Literature (≥6)**: EN—Eyal (*Hooked*), Chen (*Cold Start*), Reeves (*Flywheel*), Ries (*Lean Startup*) | ZH(≥2)—俞军 (*俞军产品方法论*), 梁宁 (*产品思维30讲*), 苏杰 (*人人都是产品经理*)
**Include**: Author | title | year | mechanisms | relevance | ID: L1...

**Citations (≥12)**: APA 7th+tag | verify ≥50% <3yrs | classify type | ID: A1...
**Alt Sources**: Gartner, Forrester, Lenny's Newsletter, Product Coalition, HBR, MIT Sloan

### Step 3: Generate Q&A (5/batch→self-check)

**Question**: Focus: mechanism analysis ("Explain how...", "What drives...", "Why X→Y?", "Map loop...") | Context: product/user/market/scale | Test ≥2 types | Single ask | Avoid: "What is", "List", surface

**Difficulty**: F=understanding ("How X?") | I=analysis ("Why X→Y?") | A=design ("Design mechanism Z")

**Answer (150–300 words)**:
1. **Key Insight** (1 sent): Core causal/feedback
2. **Mechanism**: Chain with [Ref: G#/A#]
3. **Analysis**: ≥2 causal/feedback loops
4. **Flow**: Input→process→output→feedback
5. **Quantitative**: Rates, coefficients, thresholds, time
6. **Loops**: Reinforcing(+)/balancing(-)
7. **Metrics**: Leading/lagging
8. **Cite**: ≥1 [Ref: ID]; flag uncertainty
9. **Artifact**: Diagram/chart/flow

**Self-Check (per 5)**: Mechanism-focused | ≥2 causal/loops | 150–300 words | Clear causality | ≥3/5 ≥1 cite (≥1/5 ≥2) | Difficulty matches

### Step 4: Visuals (≥1 diagram+table/type; ref from ≥50% answers)

**Types**: Growth: loop/viral coef/flywheel | Retention: curve/habit/cohort | Monetization: unit econ/pricing loop/revenue tree | User Behavior: BJ Fogg/journey/motivation-ability | Market: competitive loop/ecosystem/network | System: feedback/causal/stock-flow

**Practice**: Diagrams for chains/loops | tables for quantitative | show time scales | mark +/- loops | cite

### Step 5: Populate Refs

**G#. Term (Acronym)** | Def (w/ causal) | mech type | related | limits | alphabetize

**T#. Tool (Category)** | Desc | pricing | users | update (Q# YYYY) | ≥3 integrations | PM use | URL | group by cat

**L#. Author, Title, Year** | Summary (mechs) | relevance | group by lang (EN, then ZH≥2)

**A#. [Citation] [Lang]** | APA 7th: Books: `Author, A. (Year). *Title*. Publisher. [EN]` | Articles: `...Vol(Issue), pages. DOI [EN]` | Web: `...*Title*. Site. URL [EN]` | ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]`

**Check**: 100% [Ref: ID] resolve | no orphans | complete fields | tagged | sorted

### Step 6: Validate (fail any=stop/fix/re-run all)

| # | Check | Criteria | Measure |
|---|-------|----------|---------|
| 1 | Floors | G≥10, T≥5, L≥6, A≥12, Q:18, 20/40/40%±5 | Count |
| 2 | Citations | ≥70%≥1, ≥30%≥2 | Calc % |
| 3 | Lang | EN:50-70%, ZH:20-40%, Other:5-15% | Calc % |
| 4 | Recency | ≥50% <3yrs (≥70% AI/platform) | Check dates |
| 5 | Diversity | ≥3 types, max 25% | Classify |
| 6 | Links | 100% accessible | Test |
| 7 | Cross-Refs | 100% resolve | Validate |
| 8 | Word Count | 100% (150-300) | Sample 5 |
| 9 | Key Insights | 100% causal/feedback | Review |
| 10 | Per-Mech Evid | 6/6 (≥2 auth+≥1 tool) | Count |
| 11 | Explanations | ≥80% causal+loops+cited+limits | Sample 10 |
| 12 | Focus | ≥70% mechanism-analysis | Review |

### Step 7: Final Review

**Q**: Clarity (single ask) | Signal (mech not trivia) | Depth (causal chains/loops) | Realism (senior+) | Discriminative (reasoning>recall) | Alignment (difficulty matches)

**A** (sample ≥5): ≥2 causal/loops | Clear mech+cites | Explicit +/- loops | Evidence | Leading/lagging | Acknowledges limits/assumptions/emergent

**Submit**: All 12 pass | Floors met | 6 gates pass | TOC+links | No placeholders | Consistent | Balanced (growth/retention, viral/paid, intrinsic/extrinsic, network/content)

## IV. Quality Check

Fail ≥2 = rewrite.

| Criterion | ✓ Good | ✗ Poor |
|-----------|--------|--------|
| **Clarity** (single ask) | "Explain how LinkedIn's network effects drive growth" | "Explain LinkedIn growth and retention and monetization" |
| **Signal** (mech understanding) | "What causes Spotify's engagement loop to strengthen?" | "List engagement metrics" |
| **Depth** (causal chains) | "Map loop: content→creators→viewers→revenue→content. Where breaks?" | "Is content important?" |
| **Realism** (senior+) | "K-factor: 1.2→0.8. Walk through mechanism, identify failure points." | "Define viral coefficient" |
| **Discriminative** (reasoning>recall) | "Why increasing free tier sometimes reduces conversion?" | "What is freemium?" |
| **Alignment** (difficulty matches) | F: understanding \| I: analyzing \| A: designing/optimizing | Label≠content |

## V. Output

**TOC**: 1. Overview | 2. Q&A by Type (6) | 3. Refs (G/T/L/A) | 4. Validation

**Overview**: Total: [18] | Difficulty: [X]F([Y]%)/[X]I([Y]%)/[X]A([Y]%) | Coverage: 6 types (MECE)

| # | Type | Range | Count | Mix | Artifacts |
|---|------|-------|-------|-----|-----------|
| 1 | Growth | Q1–3 | 3 | 1F/1I/1A | 1 diagram+table |
| 2 | Retention | Q4–6 | 3 | 1F/1I/1A | 1 diagram+table |
| 3 | Monetization | Q7–9 | 3 | 1F/1I/1A | 1 diagram+table |
| 4 | User Behavior | Q10–12 | 3 | 1F/1I/1A | 1 diagram+table |
| 5 | Market | Q13–15 | 3 | 1F/1I/1A | 1 diagram+table |
| 6 | System | Q16–18 | 3 | 1F/1I/1A | 1 diagram+table |
| | **Total** | | **18** | **6F/6I/6A** | **12** |

**Q&A**: **Type [#]: [Title]** | **Q[#]**: [Question] | **Difficulty**: [F/I/A] | **Type**: [Area] | **Key Insight**: [1 sent—core causal/feedback] | **Answer** (150–300): Mech [Ref: G#/A#] | ≥2 causal | Flow (input→process→output→feedback) | Quantitative (rates/coef/thresholds) | +/- loops | Leading/lagging | ≥1 [Ref: ID] | Limits/assumptions | **Artifact**: Diagram/chart/flow

**Refs**: **G#. Term** | Def (causal) | type | related | limits | alpha | **T#. Tool (Cat)** | Desc | price | users | update≤18mo | ≥3 integrations | use | URL | by cat | **L#. Author, Title, Yr** | Summary (mechs) | relevance | by lang | **A#. [Cite] [Lang]** | APA 7th | sorted

## VI. Example

**Q1: Explain how Spotify's Daily Mix creates a reinforcing engagement loop. What strengthens it, and where could it break?**

**Difficulty**: I | **Type**: User Behavior + Retention

**Key Insight**: Daily Mix: listening data→better personalization→more listening→more data. Loop strengthens as model improves. Breaks at cold-start or filter bubble.

**Answer** (267 words):

**Flow**: Multi-stage feedback [Ref: A1]. (1) **Input**: Listening history, skips, adds, time-of-day; (2) **Process**: Collaborative filtering+content-based algorithms cluster users/tracks [Ref: G3]; (3) **Output**: Personalized playlists matching mood/context; (4) **Feedback**: Engagement (completion, skips, saves) refines model [Ref: L2].

**Reinforcing Loop (+)**: More listening→richer data→better recommendations→higher satisfaction→more listening [Ref: G1]. Virtuous cycle. Quantitative: users >1000 sessions have 3.2× retention vs <100 [Ref: A4].

**Time Dynamics**: Non-linear strengthening. Weeks 1-8 (sessions 1-50): accuracy ~65%, moderate engagement. Months 2-6 (50-500): accuracy ~85%, active use +2.1× [Ref: A5]. >500: diminishing returns, sustained high engagement.

**Break Points**: (1) **Cold start**: New users lack data, generic recs→low engagement→churn. Mitigation: onboarding questions, social imports [Ref: G7]. (2) **Filter bubble**: Over-optimization→echo chamber→boredom→stagnation. Mitigation: 15% serendipity [Ref: L6]. (3) **Competition**: Better algorithm elsewhere breaks lock-in.

**Leading**: Completion >60%, sessions/wk >5, skip <30%, new artist >2/wk.

**Limits**: Assumes listening=preference (but background noise); weakens for <2 sessions/wk users.

**Artifact**:
```
Listening ─(+)→ Data ─(+)→ Personalization
    ↑                           │
    └───(+)──← Satisfaction ←(+)┘
         └(+)→ Habit ─(+)┘
Breaks: Cold Start | Filter Bubble | Competition
```

| Stage | Sessions | Accuracy | Engagement/wk | Strength | Retention |
|-------|----------|----------|---------------|----------|-----------|
| Initial | 1-50 | 65% | 2.3 | Weak | 45% |
| Growth | 50-500 | 85% | 4.8 | Strong | 78% |
| Mature | 500+ | 88% | 5.4 | Very Strong | 92% |
