# UX Interview Q&A Generator

Generate 25-30 evidence-based Q&As validating senior UX capabilities across 6 dimensions with artifacts, quantified trade-offs, validation.

## Table of Contents
1. [Requirements](#requirements)
2. [Execution](#execution)
3. [Output Format](#output-format)
4. [Reference Examples](#reference-examples)

## Requirements

**Target**: Senior UX designers (5+ years), leads, principals via judgment-based scenarios.

**Assumptions**: Digital products (web/mobile/SaaS); foundational UX knowledge; 10-15min/question.

**Terms**:
- **Judgment Question**: Trade-off analysis ("How would you..." vs "What is...")
- **Design Artifact**: Production-ready spec (dimensions/states/interactions)
- **Floor**: Minimum threshold (≥)
- **Quality Gate**: Fail = stop, fix, re-validate all

**Scope**: Multi-platform, accessibility, systems, research | **Exclude**: Junior concepts, single-platform, pure theory | **Limitation**: Generic scenarios lack domain nuance

### Floors

| Component | Requirements |
|-----------|-------------|
| **Q&As** | 25-30 \| 20/40/40% F/I/A (±5%) \| 150-300 words \| ≥70% ≥1 cite, ≥30% ≥2 \| ≥70% judgment |
| **Dimensions** | 1. Research (4-6) \| 2. IA (4-6) \| 3. Visual (4-6) \| 4. Interaction (4-6) \| 5. Accessibility (4-6) \| 6. Systems (4-6) |
| **References** | G≥10 \| T≥5 \| L≥6 \| A≥12 APA 7th [EN]/[ZH] |
| **Artifacts** | ≥1 diagram+spec+table+metric/dimension (24 min) |

**Legend**: F=Foundational, I=Intermediate, A=Advanced | G=Glossary, T=Tool, L=Literature, A=Citation

### Dimensions (MECE)

1. **Research**: User research, usability testing, analytics, A/B testing
2. **IA**: Navigation, taxonomies, mental models, card sorting
3. **Visual**: Layout, typography, color, tokens, grids
4. **Interaction**: Flows, states, feedback, microinteractions
5. **Accessibility**: WCAG, ARIA, screen readers, i18n
6. **Systems**: Libraries, atomic design, governance, versioning

### Citations

**Format**: APA 7th + `[EN/ZH/Other]` | Inline: `[Ref: ID]`

**Distribution**: EN 60±10% \| ZH 30±10% \| Other 10±5% | **Types** (≥3): Research, tools, frameworks, cases

### Gates (fail ANY = stop, fix, re-validate ALL)

| # | Criteria | Mitigation |
|---|----------|------------|
| 1 | ≥50% from 3yrs (≥70% digital) | Flag caveats |
| 2 | ≥3 types; max 25%/type | Expand |
| 3 | Each dimension ≥2 authoritative+≥1 tool | Add sources |
| 4 | Tools: pricing, update≤18mo, ≥3 integrations | - |
| 5 | 100% URLs accessible/archived | Archive/replace |
| 6 | 100% [Ref:ID] resolve | Fix refs |

## Execution

### Step 1: Allocate

Distribute 25-30 across 6 dimensions (20/40/40% F/I/A). Each: 4-6 Q&As with ≥1F, ≥1I, ≥1A.

**Example** (30): Research (5): 1F/2I/2A | IA (5): 1F/2I/2A | Visual (6): 1F/2I/3A | Interaction (5): 1F/2I/2A | Accessibility (4): 0F/2I/2A | Systems (5): 1F/2I/2A = **6F/12I/12A**

### Step 2: Build References (run Gates 1-6 after)

**Glossary (≥10)**: Progressive Disclosure, IA, Affordance, Cognitive Load, Design Tokens, Atomic Design, Heuristic Evaluation, Card Sorting, SUS, WCAG
- **Format**: `G#. Term [Lang] | Definition | Related: [Terms] | Use: [Cases]`

**Tools (≥5)**: Design (Figma, Sketch), Analytics (Hotjar, Mixpanel), Research (Optimal Workshop, UserTesting), Dev (Storybook, Chromatic), Accessibility (Axe, WAVE)
- **Format**: `T#. Tool (Category) [Lang] | Desc | Pricing | Updated: Q# YYYY | Integrations (≥3) | Use | URL`

**Literature (≥6)**: EN—Norman, Krug, Cooper, Gothelf, Knapp, Nielsen | ZH (≥2)—刘津/李月, 俞军
- **Format**: `L#. Author, Title, Year [Lang] | Summary | Relevance`

**Citations (≥12)**: APA 7th + tags | ≥50% from 3yrs | Types: research/tools/frameworks/cases

### Step 3: Generate Q&As (5 at a time → self-check)

**Question**: "How/When/Compare..." + constraints (team: solo/<5/>20 | users: <1K/1K-100K/>1M | platforms: 1/2-3/>3 | time/budget) | **Avoid**: "What is...", "Define..."

**Complexity**:
- **F**: "Calculate SUS score from user testing"
- **I**: "60% findability (target: 80%). IA restructure vs. search enhancement?"
- **A**: "15 teams, web/mobile/voice. Govern token updates without breaking products?"

**Answer** (150-300 words): Context → Pattern [Ref:G#/A#] + rationale → Artifact (dimensions/states/interactions/tokens) → Quantified trade-offs (table) → Alternatives (≥2, "Use When") → Metrics (formula+target) → Limitations

**Self-Check**: ✓ Judgment | ✓ 150-300w | ✓ Artifact | ✓ Quantified | ✓ ≥2 alternatives+table | ✓ ≥3/5 ≥1 cite (≥1/5 ≥2) | ✓ Complexity matches

### Step 4: Artifacts (≥1 diagram+spec+table+metric/dimension)

**Diagrams**: Research (journey, funnel) | IA (sitemap, flow) | Visual (wireframe, tokens) | Interaction (state, flow) | Accessibility (ARIA, keyboard) | Systems (library, schema) | **Format**: Mermaid <120 nodes, annotated, cited

**Spec**: Component | Dimensions (px/rem) | States (default/hover/active/disabled/loading) | Tokens (color/spacing/typography) | Accessibility (ARIA/keyboard/focus) | Responsive

**Metrics**:

| Dimension | Metric | Formula | Target |
|-----------|--------|---------|--------|
| Research | SUS | `(Σ(Q1-Q10)-5)×2.5` | ≥70 |
| IA | Findability | `Found≤3 clicks/Total×100%` | >80% |
| Visual | Contrast | `(L1+0.05)/(L2+0.05)` | ≥4.5:1 |
| Interaction | Task Success | `Completed/Attempted×100%` | >90% |
| Accessibility | WCAG | `Passed/Total×100%` | 100% AA |
| Systems | Adoption | `Using/Total Teams×100%` | >70% 6mo |

### Step 5: Populate References

**Formats**:
- **G**: `G#. Term [Lang] | Def | Related | Use` (alphabetize)
- **T**: `T#. Tool (Category) [Lang] | Desc | Price | Updated Q# YYYY | Integrations (≥3) | Use | URL` (group by category)
- **L**: `L#. Author, Title, Year [Lang] | Summary | Relevance` (EN, then ZH)
- **A**: `A#. [APA 7th] [Lang]` (Books: `Author, A. (Year). *Title*. Publisher.` | Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI` | Web: `Author. (Year). *Title*. Site. URL`)

**Check**: ✓ 100% [Ref:ID] resolve | ✓ No orphans | ✓ Complete | ✓ [Lang] tags

### Step 6: Validate (fail ANY = stop, fix, re-run ALL)

**19 Checks**:

| # | Criteria | Target |
|---|----------|--------|
| 1 | Floors | G≥10, T≥5, L≥6, A≥12, Q=25-30, 20/40/40% ±5% |
| 2 | Citations | ≥70% ≥1 cite; ≥30% ≥2 |
| 3 | Language | EN 60±10%, ZH 30±10%, Other 10±5% |
| 4 | Recency | ≥50% from 3yrs (≥70% digital) |
| 5 | Types | ≥3; max 25%/type |
| 6 | Links | 100% accessible/archived |
| 7 | Cross-Refs | 100% resolve |
| 8 | Words | Sample 5; 100% in 150-300 |
| 9 | Quantified | 100% have metrics/% |
| 10 | Evidence | 6/6 dimensions ≥2 auth+≥1 tool |
| 11 | Traceability | ≥80% design→spec annotated |
| 12 | Judgment | ≥70% judgment-based |
| 13 | Artifacts | ≥90% dimensions have 4 types |
| 14 | Patterns | ≥80% reference patterns |
| 15 | Metrics | ≥60% have success metrics |
| 16 | Specs | ≥80% have artifacts |
| 17 | Production | 100% specs ready |
| 18 | Formulas | 100% mathematically valid |
| 19 | Review | 6/6 criteria (below) |

**Review (#19)**: 1) Clarity (structure, terminology, traceability) | 2) Accuracy (verifiable, valid) | 3) Completeness (6 dimensions, floors, no placeholders) | 4) Balance (≥2 alternatives, assumptions, limitations) | 5) Practicality (actionable, measurable) | 6) Self-Correction (no redundancy/gaps/orphans)

**Q&A Quality** (sample ≥5): Clarity (single focus) | Judgment (decision-making) | Depth (trade-offs) | Realism (production context) | Discriminative (separates levels)

**Submit**: ✓ 19/19 | ✓ Floors | ✓ 6 gates | ✓ TOC links | ✓ No placeholders | **Pilot**: 2-3 designers, 1 mock/person, iterate

## Output Format

### A. TOC

1. Requirements | 2. Execution (Steps 1-6) | 3. Q&As (3.1 Research | 3.2 IA | 3.3 Visual | 3.4 Interaction | 3.5 Accessibility | 3.6 Systems) | 4. References (4.1 Glossary | 4.2 Tools | 4.3 Literature | 4.4 Citations) | 5. Validation

### B. Overview

**Total**: [25-30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%)

| # | Dimension | Range | Mix | Artifacts |
|---|-----------|-------|-----|-----------|
| 1 | Research | Q1-5 | 1F/2I/2A | diagram+spec+table+metric |
| 2 | IA | Q6-10 | 1F/2I/2A | diagram+spec+table+metric |
| 3 | Visual | Q11-16 | 1F/2I/3A | diagram+spec+table+metric |
| 4 | Interaction | Q17-21 | 1F/2I/2A | diagram+spec+table+metric |
| 5 | Accessibility | Q22-25 | 0F/2I/2A | diagram+spec+table+metric |
| 6 | Systems | Q26-30 | 1F/2I/2A | diagram+spec+table+metric |
| | **Total** | **30** | **6F/12I/12A** | **24 min** |

**Usage**: Select 1-2 dimensions (5-10 Q&As), demonstrate 3-4/candidate, adjust by role

### C. Q&A Template

**Q#: [How/When/Compare + constraints]** | **Difficulty**: [F/I/A] | **Insight**: [Quantified trade-off]

**Answer** (150-300 words): Context → Pattern [Ref:G#/A#]+rationale → Artifact → Trade-offs → Alternatives (≥2, "Use When") → Metrics → Limitations

**Spec**:
```
Component: [Name] | Dimensions: [px/rem+breakpoints] | States: default/hover/active/disabled/loading
Tokens: color-X, spacing-Y, font-Z | Accessibility: ARIA/keyboard/focus | Interactions: [Triggers]
```

**Diagram**: `mermaid` (flowchart/journey/sequence/stateDiagram, <120 nodes)

**Metrics**: | Metric | Formula | Variables | Target |

**Trade-offs**: | Approach | Pros (+%) | Cons (-%) | Use When | Consensus |

**Limitations**: [Assumptions, edge cases, boundaries]

---

### D. Reference Formats

**G**: `G#. Term [Lang] | Def | Related | Use` (alphabetize)  
**T**: `T#. Tool (Category) [Lang] | Desc | Price | Updated Q# YYYY | Integrations (≥3) | Use | URL` (group)  
**L**: `L#. Author, Title, Year [Lang] | Summary | Relevance` (EN, ZH)  
**A**: `A#. [APA 7th] [Lang]`

## Reference Examples

### Glossary (≥10)
**G1. Progressive Disclosure** [EN] | Reveals info incrementally to reduce cognitive load | **Related**: G4 | **Use**: Forms, dashboards  
**G2. IA** [EN] | Structural design of info environments for findability | **Related**: G8 | **Use**: Sitemaps, navigation  
**G3. Affordance** [EN] | Visual cues suggesting how to interact | **Related**: Visual Design | **Use**: Buttons, interactive elements  
**G4. Cognitive Load** [EN] | Mental effort to process info; minimize to improve UX | **Related**: G1 | **Use**: Forms, dashboards  
**G5. Design Tokens** [EN] | Centralized design values (color/spacing/typography) | **Related**: G6 | **Use**: Multi-platform consistency  
**G6. Atomic Design** [EN] | Component hierarchy (atoms→molecules→organisms→templates→pages) | **Related**: G5 | **Use**: System architecture  
**G7. Heuristic Evaluation** [EN] | Usability inspection via Nielsen's 10 principles | **Related**: Testing | **Use**: Expert review, audits  
**G8. Card Sorting** [EN] | Users group content to inform IA | **Related**: G2 | **Use**: Navigation, taxonomy  
**G9. SUS** [EN] | 10-item usability questionnaire; 0-100 score | **Related**: Metrics | **Use**: Benchmark  
**G10. WCAG** [EN] | Accessibility guidelines; POUR principles | **Related**: ARIA | **Use**: Compliance

### Tools (≥5)
**T1. Figma** [EN] | Collaborative design for UI/UX, components, prototypes | **Pricing**: Freemium | **Updated**: Q4 2024 | **Integrations**: Slack, Jira, Storybook | **Use**: Interface design | **URL**: https://figma.com  
**T2. Hotjar** [EN] | Behavior analytics: heatmaps, recordings, surveys | **Pricing**: Freemium | **Updated**: Q3 2024 | **Integrations**: GA, Optimizely, Slack | **Use**: Research, analytics | **URL**: https://hotjar.com  
**T3. Optimal Workshop** [EN] | IA tools: card sorting, tree testing | **Pricing**: Paid | **Updated**: Q3 2024 | **Integrations**: UserTesting, Miro, Notion | **Use**: IA research | **URL**: https://optimalworkshop.com  
**T4. Axe DevTools** [EN] | WCAG testing; browser extension, CLI | **Pricing**: Freemium | **Updated**: Q4 2024 | **Integrations**: Chrome, VSCode, Jira | **Use**: Accessibility audits | **URL**: https://deque.com/axe  
**T5. Storybook** [EN] | Component docs, isolated dev environment | **Pricing**: Free/OSS | **Updated**: Q4 2024 | **Integrations**: React, Vue, Figma | **Use**: System docs | **URL**: https://storybook.js.org

### Literature (≥6)
**L1. Norman, D. (2013). *Design of Everyday Things*. Basic Books.** [EN] | Affordances, signifiers, models | **Relevance**: Core UX principles  
**L2. Krug, S. (2014). *Don't Make Me Think*. New Riders.** [EN] | Navigation, clarity, testing | **Relevance**: Applied web usability  
**L3. Cooper, A., et al. (2014). *About Face*. Wiley.** [EN] | Goal-directed design, personas, patterns | **Relevance**: Interaction framework  
**L4. Gothelf, J., & Seiden, J. (2021). *Lean UX*. O'Reilly.** [EN] | Collaborative, hypothesis-driven, MVP | **Relevance**: Agile UX  
**L5. Knapp, J., et al. (2016). *Sprint*. Simon & Schuster.** [EN] | Design sprints, prototyping, validation | **Relevance**: Fast iteration  
**L6. Nielsen, J., & Loranger, H. (2006). *Prioritizing Web Usability*. New Riders.** [EN] | Heuristics, testing, best practices | **Relevance**: Evidence-based usability

### Citations (≥12, APA 7th, 60/30/10%)
**A1.** Norman, D. (2013). *The design of everyday things*. Basic Books. [EN]  
**A2.** Krug, S. (2014). *Don't make me think*. New Riders. [EN]  
**A3.** 刘津, & 李月. (2017). *用户体验要素*. 机械工业出版社. [ZH]  
**A4.** Cooper, A., et al. (2014). *About face*. Wiley. [EN]  
**A5.** Gothelf, J., & Seiden, J. (2021). *Lean UX*. O'Reilly. [EN]  
**A6.** Nielsen, J., & Loranger, H. (2006). *Prioritizing web usability*. New Riders. [EN]  
**A7.** Knapp, J., et al. (2016). *Sprint*. Simon & Schuster. [EN]  
**A8.** Rosenfeld, L., et al. (2015). *Information architecture*. O'Reilly. [EN]  
**A9.** 俞军. (2019). *俞军产品方法论*. 中信出版社. [ZH]  
**A10.** Frost, B. (2016). *Atomic design*. Brad Frost. [EN]  
**A11.** Lidwell, W., et al. (2010). *Universal principles of design*. Rockport. [EN]  
**A12.** 张溪梦. (2021). *用户增长方法论*. 机械工业出版社. [ZH]
