# User Experience Interview Q&A Generator

Generate 25-30 evidence-based Q&As validating senior UX capabilities across 6 dimensions with artifacts, quantified trade-offs, and validation.

## Table of Contents
1. [Context & Requirements](#context--requirements)
2. [Execution](#execution)
3. [Output Format](#output-format)
4. [Reference Examples](#reference-examples)

## Context & Requirements

**Purpose**: Assess senior UX designers (5+ years), leads, principals through judgment-based scenarios.

**Assumptions**: Digital products (web/mobile/SaaS); foundational UX knowledge; 10-15min/question.

**Key Terms**:
- **Judgment Question**: Trade-off analysis, not recall ("How would you..." vs "What is...")
- **Design Artifact**: Production-ready spec with dimensions/states/interactions
- **Floor**: Minimum threshold (≥)
- **Quality Gate**: Fail = stop, fix, re-validate all

**Scope**: Multi-platform design, accessibility, system scalability, research methods | **Exclude**: Junior concepts, single-platform specifics, pure theory

**Limitations**: Generic scenarios lack domain nuance; add role-specific validation

### Quantitative Floors

| Component | Requirements |
|-----------|-------------|
| **Q&As** | 25-30 total \| 20/40/40% F/I/A (±5%) \| 150-300 words \| ≥70% ≥1 cite, ≥30% ≥2 cites \| ≥70% judgment |
| **Dimensions** (MECE) | 1. Research & Testing (4-6) \| 2. Information Architecture (4-6) \| 3. Visual Design (4-6) \| 4. Interaction Design (4-6) \| 5. Accessibility (4-6) \| 6. Design Systems (4-6) |
| **References** | Glossary ≥10 \| Tools ≥5 \| Literature ≥6 \| Citations ≥12 APA 7th with [EN]/[ZH] tags |
| **Artifacts** | ≥1 diagram + spec + table + metric per dimension (24 minimum) |

**Legend**: F=Foundational, I=Intermediate, A=Advanced

### Dimension Specifications

1. **Research & Testing**: User research, usability testing, analytics, A/B testing, validation
2. **Information Architecture**: Navigation, taxonomies, mental models, card sorting, findability
3. **Visual Design & UI**: Layout, typography, color theory, design tokens, grids, hierarchy
4. **Interaction Design**: User flows, states, feedback, microinteractions, progressive disclosure
5. **Accessibility & Inclusion**: WCAG compliance, ARIA, screen readers, inclusive design, i18n
6. **Design Systems**: Component libraries, atomic design, governance, versioning, scalability

### Citation Standards

**Format**: APA 7th + tag: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: ID]` (G#=Glossary, T#=Tool, L#=Literature, A#=Citation)

**Distribution**: EN 60% (±10%) | ZH 30% (±10%) | Other 10% (±5%) | **Source Types** (≥3): Research, tools, frameworks, case studies

### Quality Gates (fail ANY = stop, fix, re-validate ALL)

| # | Gate | Criteria | Mitigation |
|---|------|----------|------------|
| 1 | **Recency** | ≥50% from last 3yrs (≥70% for digital/web/SaaS) | Flag with caveats |
| 2 | **Source Diversity** | ≥3 types; no type >25% | Expand research |
| 3 | **Per-Dimension Evidence** | Each dimension ≥2 authoritative + ≥1 tool | Add sources |
| 4 | **Tool Completeness** | Pricing, update (≤18mo), ≥3 integrations, adoption | - |
| 5 | **Link Validation** | 100% URLs accessible/archived | Web Archive or replace |
| 6 | **Cross-Reference Integrity** | 100% [Ref: ID] resolve; no orphans | Fix references |

## Execution

### Step 1: Plan Allocation

Distribute 25-30 across 6 dimensions (20/40/40% F/I/A). Each: 4-6 Q&As with ≥1F, ≥1I, ≥1A.

**Example** (30 Q&As, senior designer):
- Research (5): 1F/2I/2A | IA (5): 1F/2I/2A | Visual (6): 1F/2I/3A
- Interaction (5): 1F/2I/2A | Accessibility (4): 0F/2I/2A | Systems (5): 1F/2I/2A
- **Total**: 6F/12I/12A (20/40/40%)

### Step 2: Build References (run Gates 1-6 after)

**Glossary (≥10)**: Progressive Disclosure, Information Architecture, Affordance, Cognitive Load, Design Tokens, Atomic Design, Heuristic Evaluation, Card Sorting, SUS, WCAG
- **Format**: Term, definition (1-2 sentences), related terms, use cases
- **Example**: `G1. Progressive Disclosure [EN] | Reveals information incrementally to reduce cognitive load | Related: G4-Cognitive Load | Use: Complex forms, dashboards`

**Tools (≥5)**: Design (Figma, Sketch), Analytics (Hotjar, Mixpanel), Research (Optimal Workshop, UserTesting), Dev (Storybook, Chromatic), Accessibility (Axe DevTools, WAVE)
- **Include**: Category, pricing, adoption, update (≤18mo), ≥3 integrations, use case, URL

**Literature (≥6)**: EN—Norman (*Design of Everyday Things*), Krug (*Don't Make Me Think*), Cooper (*About Face*), Gothelf (*Lean UX*), Knapp (*Sprint*), Nielsen (*Prioritizing Web Usability*) | ZH (≥2)—刘津/李月 (*用户体验要素*), 俞军 (*俞军产品方法论*)

**Citations (≥12)**: Convert to APA 7th + tags | Verify ≥50% from last 3yrs | Classify: research/tools/frameworks/case studies

### Step 3: Generate Q&As (5 at a time → self-check each batch)

**Question Formula**:
- **Format**: "How would you...", "When should you...", "Compare approaches for..."
- **Include**: Team size (solo/<5/>20), users (<1K/1K-100K/>1M), platforms (1/2-3/>3), time/budget
- **Avoid**: "What is...", "Define...", "List features of..."

**Complexity Calibration**:
- **F**: "How do you calculate SUS score from user testing?"
- **I**: "Navigation test shows 60% findability (target: 80%). Compare IA restructure vs. search enhancement."
- **A**: "Design system serves 15 teams across web/mobile/voice. How do you govern token updates without breaking products?"

**Answer Structure** (150-300 words):
1. **Context**: State scenario constraints
2. **Pattern + Rationale**: Approach with [Ref: G#/A#]
3. **Design Artifact**: Spec (dimensions, states, interactions, tokens)
4. **Quantified Trade-offs**: "Option A: +35% completion, -25% engagement" with table
5. **Alternatives**: ≥2 options with "Use When" guidance
6. **Metrics**: Formula + variables + target ("SUS ≥70")
7. **Limitations**: Assumptions, edge cases, boundaries

**Batch Self-Check** (per 5): ✓ Judgment-based | ✓ 150-300 words | ✓ Production-ready artifact | ✓ Quantified trade-offs | ✓ ≥2 alternatives + table | ✓ ≥3/5 ≥1 cite (≥1/5 ≥2) | ✓ Complexity matches content

### Step 4: Create Artifacts (≥1 diagram + spec + table + metric per dimension)

**Diagram Types**:
- **Research**: Journey map, research plan, test script, funnel analysis
- **IA**: Sitemap, user flow, card sorting, navigation tree
- **Visual**: Wireframe, mockup, component spec, token hierarchy
- **Interaction**: State diagram, flow, microinteraction spec, pattern library
- **Accessibility**: ARIA tree, keyboard navigation, WCAG checklist, screen reader path
- **Systems**: Component library, token schema, versioning strategy, adoption dashboard

**Design Spec Format**: Component name | Dimensions (px/rem) | States (default/hover/active/disabled/loading) | Tokens (color/spacing/typography) | Accessibility (ARIA, keyboard, focus) | Responsive breakpoints

**Metric Formulas**:

| Dimension | Metric | Formula | Target |
|-----------|--------|---------|--------|
| Research | SUS Score | `(Σ(Q1-Q10) - 5) × 2.5` | ≥70 |
| IA | Findability | `Found in ≤3 clicks / Total × 100%` | >80% |
| Visual | Contrast Ratio | `(L1 + 0.05) / (L2 + 0.05)` | ≥4.5:1 (AA) |
| Interaction | Task Success | `Completed / Attempted × 100%` | >90% |
| Accessibility | WCAG Compliance | `Passed / Total Criteria × 100%` | 100% Level AA |
| Systems | Adoption Rate | `Teams Using / Total Teams × 100%` | >70% in 6mo |

**Best Practices**: Mermaid diagrams <120 nodes; annotate with dimensions/units; include "Use When" column; cite sources `[Ref: A7]`; reference from ≥50% Q&As

### Step 5: Populate References

**Glossary**: **G#. Term** [Lang] | Definition | Related | Use cases | Alphabetize

**Tools**: **T#. Tool (Category)** [Lang] | Description | Pricing | Update (Q# YYYY) | Integrations (≥3) | Use case | URL | Group by category

**Literature**: **L#. Author, Title, Year** [Lang] | Summary (focus/frameworks) | Relevance | Group by language (EN, then ZH)

**Citations**: **A#. [Citation] [Lang]** | APA 7th formats:
- Books: `Author, A. (Year). *Title*. Publisher. [EN]`
- Articles: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]`
- Web: `Author. (Year). *Title*. Site. URL [EN]`
- ZH: `刘津, & 李月. (2017). *用户体验要素*. 机械工业出版社. [ZH]`

**Final Check**: ✓ 100% [Ref: ID] resolve | ✓ No orphans | ✓ All fields complete | ✓ All APA have [EN]/[ZH] tags

### Step 6: Validation (fail ANY = stop, fix, re-run ALL)

**19 Validation Checks**:

| # | Check | Criteria | Example |
|---|-------|----------|---------|
| 1 | Floors | G≥10, T≥5, L≥6, A≥12, Q=25-30, 20/40/40% (±5%) | G:12 T:6 L:7 A:15 Q:30 (6F/12I/12A) |
| 2 | Citations | ≥70% ≥1; ≥30% ≥2 | 80%≥1, 35%≥2 → PASS |
| 3 | Language | EN 60%, ZH 30%, Other 10% (±10%) | EN:58%, ZH:32%, Other:10% → PASS |
| 4 | Recency | ≥50% from 3yrs (≥70% digital/web/SaaS) | 72% from 3yrs (SaaS) → PASS |
| 5 | Source Types | ≥3 types; max 25% | 4 types; max 23% → PASS |
| 6 | Links | 100% accessible/archived | 28/28 → PASS |
| 7 | Cross-Refs | 100% resolved | 180/180 → PASS |
| 8 | Word Count | Sample 5; 100% within 150-300 | 5 sampled: 5 compliant → PASS |
| 9 | Quantified Insights | 100% have metrics/percentages | 30/30 → PASS |
| 10 | Per-Dimension Evidence | 6/6 ≥2 authoritative + ≥1 tool | 6/6 → PASS |
| 11 | Traceability | ≥80% design→spec with annotations | 85% → PASS |
| 12 | Question Type | ≥70% judgment-based | 75% → PASS |
| 13 | Artifacts | ≥90% dimensions have all 4 (diagram/spec/table/metric) | 100% (6/6) → PASS |
| 14 | Patterns | ≥80% reference design patterns | 83% → PASS |
| 15 | Metrics | ≥60% Q&As have success metrics | 65% → PASS |
| 16 | Design Specs | ≥80% Q&As have artifacts | 82% → PASS |
| 17 | Validity | 100% specs production-ready (dimensions/states/tokens) | 30/30 → PASS |
| 18 | Formulas | 100% mathematically valid | 12/12 → PASS |
| 19 | Review | 6/6 criteria PASS (see below) | 6/6 → PASS |

**Review Criteria #19** (all must PASS):

1. **Clarity**: Logical structure | Consistent terminology | Minimal jargon with inline definitions | Clear traceability
2. **Accuracy**: Verifiable facts | Valid diagrams/code | Sound metrics | Research-backed claims
3. **Completeness**: 6 dimensions (4-6 Q&As each) | All floors met | 19/19 validations PASS | No placeholders
4. **Balance**: ≥2 alternatives + comparison table | Explicit assumptions/limitations | Consensus tags
5. **Practicality**: Actionable guidance | Production-ready specs | Measurable outcomes | Real-world constraints
6. **Self-Correction**: No redundancy | No inconsistencies | No gaps | No orphaned references

**Q&A Quality Check** (sample ≥5):
- **Clarity**: Single focus | ✓ "Compare card sorting vs. tree testing for IA" | ✗ "Design IA AND implement accessibility"
- **Judgment**: Tests decision-making | ✓ "SUS is 65 (target: 75). Prioritize navigation vs. content?" | ✗ "What is SUS?"
- **Depth**: Enables trade-off analysis | ✓ "Progressive disclosure: +35% completion, -25% engagement. When to use?" | ✗ "Is progressive disclosure good?"
- **Realism**: Production context | ✓ "15 teams use design system. Token update breaks 3 products. Resolve?" | ✗ "Create design system"
- **Discriminative**: Separates levels | ✓ "When would WCAG AA fail user needs? Supplement how?" | ✗ "Meets WCAG AA?"

**Submission Checklist**: ✓ 19/19 PASS | ✓ All floors met | ✓ 6 quality gates passed | ✓ TOC with working links | ✓ No placeholders | ✓ Consistent formatting

**Pilot Test**: Share with 2-3 designers → 1 mock interview/person → iterate before deployment

## Output Format

### A. TOC Structure

1. Context & Requirements
2. Execution (Steps 1-6)
3. Q&As by Dimension
   - 3.1 Research & Testing (Q1-Q5)
   - 3.2 Information Architecture (Q6-Q10)
   - 3.3 Visual Design (Q11-Q16)
   - 3.4 Interaction Design (Q17-Q21)
   - 3.5 Accessibility (Q22-Q25)
   - 3.6 Design Systems (Q26-Q30)
4. References
   - 4.1 Glossary (G1-G12)
   - 4.2 Tools (T1-T6)
   - 4.3 Literature (L1-L7)
   - 4.4 Citations (A1-A15)
5. Validation Report (filled)

### B. Dimension Overview

**Total**: [25-30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 6 dimensions (MECE)

| # | Dimension | Range | Count | Mix | Artifacts |
|---|-----------|-------|-------|-----|-----------|
| 1 | Research & Testing | Q1-Q5 | 5 | 1F/2I/2A | diagram+spec+table+metric |
| 2 | Information Architecture | Q6-Q10 | 5 | 1F/2I/2A | diagram+spec+table+metric |
| 3 | Visual Design & UI | Q11-16 | 6 | 1F/2I/3A | diagram+spec+table+metric |
| 4 | Interaction Design | Q17-21 | 5 | 1F/2I/2A | diagram+spec+table+metric |
| 5 | Accessibility & Inclusion | Q22-25 | 4 | 0F/2I/2A | diagram+spec+table+metric |
| 6 | Design Systems | Q26-30 | 5 | 1F/2I/2A | diagram+spec+table+metric |
| | **Total** | | **30** | **6F/12I/12A** | **24 artifacts** |

**Legend**: F=foundational | I=intermediate | A=advanced

**Usage**: Select 1-2 dimensions (5-10 Q&As) for interview → demonstrate 3-4 per candidate → adjust difficulty by role

### C. Q&A Template

---

**Dimension 1: [Title]**

**Q1: [How/When/Compare judgment question with constraints]**

**Difficulty**: [F/I/A] | **Dimension**: [Type]

**Key Insight**: [Quantified trade-off in one sentence]

**Answer** (150-300 words):
Context → Pattern [Ref: G#/A#] + rationale → Design artifact → Quantified trade-offs → Alternatives → Metrics → Limitations

**Design Specification**:
```
Component: [Name]
Dimensions: [px/rem with responsive breakpoints]
States: default, hover, active, disabled, loading
Tokens: color-primary-500, spacing-md, font-body-base
Accessibility: ARIA roles, keyboard navigation, focus indicators
Interactions: [Triggers and behaviors]
```

**Diagram**:
```mermaid
[Type matching dimension: flowchart/journey/sequence/stateDiagram, <120 nodes]
```

**Metrics**:
| Metric | Formula | Variables | Target |
| [Name] | [Expression] | [Definitions] | [Threshold] |

**Trade-offs**:
| Approach | Pros | Cons | Use When | Consensus |
| [Option 1] | [+35% metric] | [-25% metric] | [Context: team/users/platform] | [Tag] |
| [Option 2] | [+quantified] | [-quantified] | [Context] | [Tag] |

**Limitations**: [Explicit assumptions, edge cases, context boundaries]

---

### D. Reference Formats

**Glossary**: **G#. Term** [EN/ZH/Other] | Definition | **Related**: [Terms] | **Use**: [Cases] | Alphabetize

**Tools**: **T#. Tool (Category)** [Lang] | Description | **Pricing**: [Type] | **Updated**: Q# YYYY | **Integrations**: [≥3] | **Use**: [Case] | **URL**: [Link] | Group by category

**Literature**: **L#. Author, Title, Year** [Lang] | Summary (focus/frameworks) | **Relevance**: [To UX practice] | Group by language (EN, then ZH)

**Citations**: **A#. [Citation] [Lang]** | APA 7th + language tag

## Reference Examples

### Glossary (≥10)
**G1. Progressive Disclosure** [EN] | Reveals information incrementally to reduce cognitive load | **Related**: G4-Cognitive Load | **Use**: Complex forms, dashboards, onboarding  
**G2. Information Architecture** [EN] | Structural design of information environments for findability and usability | **Related**: G8-Card Sorting, Navigation | **Use**: Sitemaps, navigation design  
**G3. Affordance** [EN] | Object property suggesting how to use it; visual cues for interaction | **Related**: Signifier, Visual Design | **Use**: Button design, interactive elements  
**G4. Cognitive Load** [EN] | Mental effort required to process information; minimize to improve UX | **Related**: G1-Progressive Disclosure | **Use**: Form design, dashboard layouts  
**G5. Design Tokens** [EN] | Centralized design values (color, spacing, typography) enabling consistency | **Related**: G6-Design System | **Use**: Multi-platform consistency  
**G6. Atomic Design** [EN] | Hierarchical component system (atoms → molecules → organisms → templates → pages) | **Related**: G5-Design Tokens, Component Libraries | **Use**: Design system architecture  
**G7. Heuristic Evaluation** [EN] | Usability inspection using Nielsen's 10 principles | **Related**: Usability Testing | **Use**: Expert review, quick audits  
**G8. Card Sorting** [EN] | Users group content to inform IA; open/closed variants | **Related**: G2-Information Architecture | **Use**: Navigation design, taxonomy  
**G9. System Usability Scale (SUS)** [EN] | 10-item questionnaire for perceived usability; score 0-100 | **Related**: Usability Metrics | **Use**: Benchmark usability  
**G10. WCAG** [EN] | Web Content Accessibility Guidelines; POUR principles (Perceivable, Operable, Understandable, Robust) | **Related**: Accessibility, ARIA | **Use**: Compliance validation

### Tools (≥5)
**T1. Figma** [EN] | Collaborative design platform for UI/UX, components, prototyping, design systems | **Pricing**: Freemium | **Updated**: Q4 2024 | **Integrations**: Slack, Jira, Storybook, Zeplin, FigJam | **Use**: Interface design, design systems | **URL**: https://figma.com  
**T2. Hotjar** [EN] | User behavior analytics with heatmaps, session recordings, surveys, feedback widgets | **Pricing**: Freemium | **Updated**: Q3 2024 | **Integrations**: Google Analytics, Optimizely, Slack, Segment | **Use**: User research, analytics | **URL**: https://hotjar.com  
**T3. Optimal Workshop** [EN] | IA research tools: card sorting, tree testing, first click testing, surveys | **Pricing**: Paid | **Updated**: Q3 2024 | **Integrations**: UserTesting, Miro, Notion, Airtable | **Use**: Information architecture | **URL**: https://optimalworkshop.com  
**T4. Axe DevTools** [EN] | Accessibility testing for WCAG compliance; browser extension and CLI | **Pricing**: Freemium | **Updated**: Q4 2024 | **Integrations**: Chrome, Firefox, VSCode, Jira, GitHub | **Use**: Accessibility audits | **URL**: https://deque.com/axe  
**T5. Storybook** [EN] | Component documentation and isolated development environment; open-source | **Pricing**: Free/OSS | **Updated**: Q4 2024 | **Integrations**: React, Vue, Angular, Figma, Chromatic | **Use**: Design system documentation | **URL**: https://storybook.js.org

### Literature (≥6)
**L1. Norman, D. (2013). *The Design of Everyday Things* (Revised). Basic Books.** [EN] | Foundational human-centered design: affordances, signifiers, conceptual models, feedback, constraints | **Relevance**: Core UX principles for interaction design  
**L2. Krug, S. (2014). *Don't Make Me Think* (3rd). New Riders.** [EN] | Usability principles: web navigation, visual clarity, user testing methods, practical guidelines | **Relevance**: Applied usability for web/mobile design  
**L3. Cooper, A., Reimann, R., & Cronin, D. (2014). *About Face: The Essentials of Interaction Design* (4th). Wiley.** [EN] | Goal-directed design, personas, interaction patterns, interface design principles | **Relevance**: Comprehensive interaction design framework  
**L4. Gothelf, J., & Seiden, J. (2021). *Lean UX* (3rd). O'Reilly.** [EN] | Collaborative design, hypothesis-driven development, MVP validation, continuous discovery | **Relevance**: Agile UX methods for product teams  
**L5. Knapp, J., Zeratsky, J., & Kowitz, B. (2016). *Sprint: How to Solve Big Problems*. Simon & Schuster.** [EN] | Design sprints, rapid prototyping, user validation, decision-making frameworks | **Relevance**: Fast iteration and validation  
**L6. Nielsen, J., & Loranger, H. (2006). *Prioritizing Web Usability*. New Riders.** [EN] | Usability heuristics, testing methods, web best practices, eye-tracking research | **Relevance**: Evidence-based web usability

### Citations (≥12, APA 7th, 60/30/10%)
**A1.** Norman, D. (2013). *The design of everyday things* (Revised). Basic Books. [EN]  
**A2.** Krug, S. (2014). *Don't make me think* (3rd). New Riders. [EN]  
**A3.** 刘津, & 李月. (2017). *用户体验要素*. 机械工业出版社. [ZH]  
**A4.** Cooper, A., Reimann, R., & Cronin, D. (2014). *About face: The essentials of interaction design* (4th). Wiley. [EN]  
**A5.** Gothelf, J., & Seiden, J. (2021). *Lean UX* (3rd). O'Reilly. [EN]  
**A6.** Nielsen, J., & Loranger, H. (2006). *Prioritizing web usability*. New Riders. [EN]  
**A7.** Knapp, J., Zeratsky, J., & Kowitz, B. (2016). *Sprint: How to solve big problems*. Simon & Schuster. [EN]  
**A8.** Rosenfeld, L., Morville, P., & Arango, J. (2015). *Information architecture* (4th). O'Reilly. [EN]  
**A9.** 俞军. (2019). *俞军产品方法论*. 中信出版社. [ZH]  
**A10.** Frost, B. (2016). *Atomic design*. Brad Frost. [EN]  
**A11.** Lidwell, W., Holden, K., & Butler, J. (2010). *Universal principles of design* (Revised). Rockport. [EN]  
**A12.** 张溪梦. (2021). *用户增长方法论*. 机械工业出版社. [ZH]
