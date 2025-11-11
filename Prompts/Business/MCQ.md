# MCQ Generator: Business-to-Architecture Translation Assessment

Generate Multiple-Choice Questions (MCQs) evaluating senior technical leaders' ability to translate business requirements into architectural decisions with evidence-based rationales.

## Specifications

### Assessment Parameters

| Parameter | Requirement | Rationale |
| --- | --- | --- |
| **Questions** | 40–80 total (20% foundational, 40% intermediate, 40% advanced) | Comprehensive coverage with emphasis on application over recall |
| **Audience** | Senior technical leaders, architects, experts | Business-technical integration focus |
| **Format** | 1–2 sentence stem + 4 options (exactly 1 correct) | Clarity, machine-gradability |
| **Distractors** | Map to specific misalignments (e.g., outdated practices, framework misuse) | Reflect real translation errors |
| **Rationale** | 1–2 sentences + ≥1 citation [Ref: ID] | Evidence-based, connects business to architecture |

### Reference Requirements

| Type | Minimum | Quality Criteria |
| --- | --- | --- |
| **Glossary (G#)** | 10 | Domain terms with definitions, architectural relevance |
| **Tools (T#)** | 5 | Active (≤18mo update), documented pricing/adoption/integrations, URL |
| **Literature (L#)** | 6 | Authoritative, diverse perspectives (business + architecture + organization) |
| **APA Citations (A#)** | 12 | APA 7th, language-tagged (~60% EN, ~30% ZH, ~10% other), ≥50% from last 3 years (≥70% for cloud-native/digital transformation) |

### Validation Gates (All Must Pass)

1. **Count**: G≥10, T≥5, L≥6, A≥12, Q=40-80 (20/40/40 split)
2. **Citations**: ≥70% questions cite ≥1 source, ≥30% cite ≥2 sources
3. **Language Mix**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% sources from last 3 years (≥70% for emerging topics)
5. **Diversity**: ≥3 source types, no single type >25%
6. **Links**: All URLs accessible or archived
7. **Cross-References**: All [Ref: ID] resolve to G#/T#/L#/A#
8. **Correctness**: Exactly 1 correct answer per question
9. **Distractors**: Each maps to specific misalignment (documented)
10. **Clarity**: All options mutually exclusive and unambiguous
11. **Focus**: ≥70% test business-to-architecture translation (not recall)

## Process

### Step 1: Plan Topics (MECE Coverage)

Identify 4-8 clusters covering business-architecture translation (e.g., Strategic Modeling, Value/Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution/Adaptation). Allocate 5-10 questions per cluster (40-80 total). Apply 20/40/40 difficulty split to each cluster.

### Step 2: Collect References

**Glossary (≥10)**: BMC, DDD, Conway's Law, Technical Debt, ADR, Bounded Context, etc. Format: **G#. Term**: Definition + architectural relevance [LANG]

**Tools (≥5)**: Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps. Format: **T#. Tool**: Description + pricing/adoption/update/integrations/URL [LANG]

**Literature (≥6)**: Osterwalder, Evans, Vernon, Conway, Skelton, Richardson + Chinese authors (周爱民, 张逸, 肖然). Format: **L#. Author. (Year). *Title*. Publisher.** + relevance

**APA Citations (≥12)**: APA 7th + [LANG] tags. Mix: ~60% EN, ~30% ZH, ~10% other. Ensure ≥50% from last 3 years.

### Step 3: Generate Questions

**Stem (1-2 sentences)**: Present business scenario → ask architectural implication. Test translation, not recall.

**Options (4 total)**: 1 correct + 3 distractors mapping to specific misalignments (e.g., outdated practices, confusing correlation/causation, framework misuse).

**Rationale (1-2 sentences)**: Connect business driver to architecture + ≥1 [Ref: ID] citation.

**Distractor Notes**: Explain why each distractor is wrong.

Verify every 10 questions: 1 correct answer, distractors documented, ≥70% test translation, ≥1 citation/question, options mutually exclusive.

### Step 4: Compile References

Populate all sections (G#, T#, L#, A#) with proper formatting. Verify all [Ref: ID] resolve, URLs accessible, no orphaned references, meets minimum counts.

### Step 5: Validate (Run All 11 Gates)

Execute validation gates 1-11. Document failures, fix immediately, re-run until all pass.

## Output Format

### Structure

1. **Table of Contents**: Markdown links to all sections (Question Bank by topic clusters, Reference Sections)
2. **Question Bank**: Organized by topic clusters
3. **Reference Sections**: Glossary (G#), Tools (T#), Literature (L#), APA Citations (A#)
4. **Validation Report**: Table showing 11 gates with PASS/FAIL status + notes

### Question Format Example

```markdown
#### Q1: [Business scenario → architectural implication question]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Options:**
- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

**Answer:** [A/B/C/D]

**Rationale:** [1-2 sentences connecting business to architecture + ≥1 [Ref: ID]]

**Distractor Notes:**
- [Letter]: [Why wrong]
```

### Reference Format Examples

**Glossary**: **G#. Term**: Definition + architectural relevance [LANG]

**Tools**: **T#. Tool**: Description + pricing/adoption/update/integrations/URL [LANG]

**Literature**: **L#. Author. (Year). *Title*. Publisher.** + relevance

**APA**: **A#. Full APA 7th citation [LANG]**
