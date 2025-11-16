# Mechanism-Focused PM Interview Q&A Generator (Minimal Viable)

Generate 6-8 decision-critical mechanism-analysis questions testing senior+ PM (5-15 yrs) on causal reasoning and systemic thinking.

## I. Foundation

**Purpose**: Assess understanding of growth loops, user behavior, scaling dynamics, system interactions, feedback loops.

**Terminology**: Floor=minimum | Gate=mandatory checkpoint (fail=stop/fix) | Difficulty: F=understand, I=analyze, A=design/optimize | Mechanisms: Growth/Retention/Monetization/User Behavior/Market/System

**Scope**: Causal relationships, feedback loops, system dynamics.

**Exclude**: Trivia, surface descriptions, tool details, generic practices.

**Constraints**: 150-300 words/answer | ≥70% with ≥1 citation (≥30% with ≥2) | 100% mechanism-focused | Senior+ only.

**Assumptions**: Core mechanism knowledge; user provides domain context or accepts generic scenarios; quantitative models state assumptions.

**Limitations**: Generic mechanisms lack domain nuance—customize per industry; flag uncertainty for emergent behaviors.

## II. Requirements & Gates

**Floors**: Q&A: 6-8 (25%F/50%I/25%A±5%) | 150-300 words | ≥2 causal/feedback each | Citations: ≥80%≥1, ≥50%≥2 | Mechanisms (decision-critical): Growth(1-2), Retention(1-2), Monetization(1), User Behavior(1-2), Market(1), System(1) | Refs: G≥8, T≥4, L≥5(≥1 ZH), A≥8 | Visuals: ≥1 diagram+table per mechanism type | 

**Citations**: APA 7th+tag: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: G#/T#/L#/A#]` | Lang: EN 60-70%, ZH 20-30%, Other 5-10% | Types: ≥2 (Frameworks/Research/Cases); no type >40%

**Gates** (fail any=stop/fix/re-validate all):
1. **Decision Criticality**: 100% satisfy ≥1 criterion (Blocks decision, Creates risk, Affects ≥2 stakeholders, Actively evolving)
2. **Recency**: ≥50% <3yrs | Flag dated
3. **Evidence**: Each mechanism type ≥1 auth+≥1 tool | Add sources
4. **Links**: 100% accessible | Archive/replace
5. **Cross-Refs**: 100% resolve; no orphans | Fix

## III. Execution

### Step 1: Plan (Minimal Viable)
Distribute 6-8 across 4-6 decision-critical types (25%F/50%I/25%A). Each: 1-2 Q&A.
**Example (8)**: Growth(1), Retention(1), Monetization(1), User Behavior(2), Market(1), System(1) = 2F/4I/2A

### Step 2: Build References (Minimal Viable)

**Glossary (≥8)**: Growth Loops, Network Effects, Viral Coefficient, Habit Formation, Retention Curve, Unit Economics, Feedback Systems, Market Dynamics
**Format**: Term | definition (1 sent w/ causal) | mechanisms | limits | ID: G1...

**Tools (≥4)**: Analytics (Mixpanel, Amplitude), Research (UserTesting), Collab (Miro), Feedback (Pendo)
**Include**: Category | pricing | users | update≤18mo | use case | URL | ID: T1...

**Literature (≥5)**: EN—Eyal (*Hooked*), Chen (*Cold Start*), Reeves (*Flywheel*) | ZH(≥1)—俞军 (*俞军产品方法论*)
**Include**: Author | title | year | mechanisms | ID: L1...

**Citations (≥8)**: APA 7th+tag | verify ≥50% <3yrs | classify type | ID: A1...
**Alt Sources**: Lenny's Newsletter, Product Coalition, HBR

### Step 3: Generate Q&A (Decision-Critical Only)

**Question**: Focus: mechanism analysis ("Explain how...", "What drives...", "Why X→Y?", "Map loop...") | Context: product/user/market/scale | Single ask | Avoid: "What is", "List", surface

**Difficulty**: F=understanding ("How X?") | I=analysis ("Why X→Y?") | A=design ("Design mechanism Z")

**Decision Criticality**: ≥1 of: (1) Blocks product decision, (2) Creates risk (churn/growth stall), (3) Affects ≥2 stakeholders, (4) Actively evolving

**Answer (150–300 words)**:
1. **Key Insight** (1 sent): Core causal/feedback
2. **Mechanism**: Chain with [Ref: G#/A#]
3. **Analysis**: ≥2 causal/feedback loops
4. **Flow**: Input→process→output→feedback
5. **Quantitative**: Rates, coefficients, thresholds
6. **Loops**: Reinforcing(+)/balancing(-)
7. **Metrics**: Leading/lagging
8. **Cite**: ≥1 [Ref: ID]; flag uncertainty
9. **Artifact**: Diagram/chart

**Self-Check (per batch)**: Decision-critical | Mechanism-focused | ≥2 causal/loops | 150–300 words | Clear causality | ≥2/3 ≥1 cite (≥1/3 ≥2) | Difficulty matches

### Step 4: Visuals (Minimal: ≥1 diagram+table per type)

**Types**: Growth: loop/viral coef | Retention: curve/habit | Monetization: unit econ | User Behavior: BJ Fogg/journey | Market: competitive loop | System: feedback/causal

**Practice**: Diagrams for chains/loops | tables for quantitative | mark +/- loops | cite

### Step 5: Populate Refs (Minimal)

**G#. Term (Acronym)** | Def (w/ causal) | limits | alphabetize

**T#. Tool (Category)** | Desc | pricing | users | PM use | URL | group by cat

**L#. Author, Title, Year** | Summary (mechs) | group by lang (EN, then ZH)

**A#. [Citation] [Lang]** | APA 7th: Books: `Author, A. (Year). *Title*. Publisher. [EN]` | ZH: `俞军. (2020). *俞军产品方法论*. 中信出版社. [ZH]`

**Check**: 100% [Ref: ID] resolve | no orphans | complete fields | tagged

### Step 6: Validate (Minimal: fail any=stop/fix/re-run all)

| # | Check | Criteria | Measure |
|---|-------|----------|----------|
| 1 | Floors | G≥8, T≥4, L≥5, A≥8, Q:6-8, 25/50/25%±5 | Count |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion | Review |
| 3 | Citations | ≥80%≥1, ≥50%≥2 | Calc % |
| 4 | Lang | EN:60-70%, ZH:20-30%, Other:5-10% | Calc % |
| 5 | Recency | ≥50% <3yrs | Check dates |
| 6 | Links | 100% accessible | Test |
| 7 | Cross-Refs | 100% resolve | Validate |
| 8 | Word Count | 100% (150-300) | Sample 5 |
| 9 | Key Insights | 100% causal/feedback | Review |
| 10 | Explanations | ≥80% causal+loops+cited+limits | Sample 6-8 |
| 11 | Focus | 100% mechanism-analysis | Review |
| 12 | Artifacts | ≥1 diagram+table per type | Count |

### Step 7: Final Review

**Q**: Clarity (single ask) | Signal (mech not trivia) | Depth (causal chains/loops) | Realism (senior+) | Discriminative (reasoning>recall) | Alignment (difficulty matches)

**A** (sample ≥3): ≥2 causal/loops | Clear mech+cites | Explicit +/- loops | Evidence | Leading/lagging | ≥1 [Ref: ID] | Limits | **Artifact**: Diagram/chart

**Submit**: All 12 pass | Floors met | 5 gates pass | TOC+links | No placeholders | Consistent | Decision-critical focus

## IV. Quality Check (Minimal)

Fail ≥2 = rewrite.

| Criterion | ✓ Good | ✗ Poor |
|-----------|--------|--------|
| **Clarity** (single ask) | "Explain how LinkedIn's network effects drive growth" | "Explain LinkedIn growth and retention and monetization" |
| **Signal** (mech understanding) | "What causes Spotify's engagement loop to strengthen?" | "List engagement metrics" |
| **Depth** (causal chains) | "Map loop: content→creators→viewers→revenue→content. Where breaks?" | "Is content important?" |
| **Decision-Critical** | "Why increasing free tier sometimes reduces conversion?" (blocks pricing decision) | "Define viral coefficient" (trivia) |
| **Discriminative** (reasoning>recall) | "K-factor: 1.2→0.8. Walk through mechanism, identify failure points." | "What is freemium?" |
| **Alignment** (difficulty matches) | F: understanding \| I: analyzing \| A: designing/optimizing | Label≠content |

## V. Output (Minimal Viable)

**TOC**: 1. Overview | 2. Decision Criticality Framework | 3. Q&A by Type (4-6) | 4. Refs (G/T/L/A) | 5. Validation

## Decision Criticality Framework

**Include Q&A if ≥1 criterion is satisfied**:
- **Blocks Decision**: Directly impacts product roadmap, pricing strategy, or feature prioritization
- **Creates Risk**: Identifies material threat (churn, growth stall, competitive disadvantage)
- **Affects ≥2 Stakeholders**: Multi-team impact (PM + Eng, PM + Design, PM + Data)
- **Actively Evolving**: Market/user behavior/tech changes in past 6-12 months

**Exclude Q&A if**:
- Niche/legacy (<5% adoption or impact)
- Orthogonal/nice-to-have (no decision impact)
- Already covered by another Q&A

**Overview**: Total: [6-8] | Difficulty: [X]F([Y]%)/[X]I([Y]%)/[X]A([Y]%) | Coverage: 4-6 decision-critical types

| # | Type | Range | Count | Mix | Decision Criticality | Artifacts |
|---|------|-------|-------|-----|----------------------|----------|
| 1 | Growth | Q1–2 | 1-2 | 1F/1I or 1I | Blocks/Risk/Evolving | 1 diagram+table |
| 2 | Retention | Q3–4 | 1-2 | 1F/1I or 1I | Blocks/Risk | 1 diagram+table |
| 3 | Monetization | Q5 | 1 | 1I | Blocks/Risk | 1 diagram+table |
| 4 | User Behavior | Q6–7 | 1-2 | 1I/1A or 1I | Blocks/Stakeholders | 1 diagram+table |
| 5 | Market | Q8 | 1 | 1I | Risk/Evolving | 1 diagram+table |
| 6 | System | Optional | 0-1 | 1A | Blocks/Risk | 1 diagram |
| | **Total** | | **6-8** | **2F/4I/2A** | **100% ≥1 criterion** | **6-8** |

**Q&A**: **Type [#]: [Title]** | **Q[#]**: [Question] | **Difficulty**: [F/I/A] | **Decision Criticality**: [Criterion] | **Key Insight**: [1 sent—core causal/feedback] | **Answer** (150–300): Mech [Ref: G#/A#] | ≥2 causal | Flow (input→process→output→feedback) | Quantitative (rates/coef/thresholds) | +/- loops | Leading/lagging | ≥1 [Ref: ID] | Limits | **Artifact**: Diagram/chart

**Refs**: **G#. Term** | Def (causal) | limits | **T#. Tool (Cat)** | Desc | price | users | use | URL | **L#. Author, Title, Yr** | Summary (mechs) | by lang | **A#. [Cite] [Lang]** | APA 7th

## VI. Example (Decision-Critical)

**Q1: Explain how Spotify's Daily Mix creates a reinforcing engagement loop. What strengthens it, and where could it break?**

**Difficulty**: I | **Type**: User Behavior + Retention | **Decision Criticality**: Blocks retention strategy (personalization roadmap)

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
