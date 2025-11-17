# MCQ Generator: Business-to-Architecture Translation Assessment

Generate MCQs evaluating senior technical leaders' ability to translate business requirements into architectural decisions with evidence-based rationales.

## Specifications

### Assessment Parameters

| Parameter | Requirement |
| --- | --- |
| **Questions** | 40–80 (20% foundational, 40% intermediate, 40% advanced) |
| **Audience** | Senior technical leaders, architects, experts |
| **Format** | 1–2 sentence stem + 4 options (exactly 1 correct) |
| **Distractors** | Map to specific misalignments (outdated practices, framework misuse) |
| **Rationale** | 1–2 sentences + ≥1 citation [Ref: ID] |

### Reference Requirements

| Type | Minimum | Criteria |
| --- | --- | --- |
| **Glossary (G#)** | 10 | Domain terms with definitions, architectural relevance |
| **Tools (T#)** | 5 | Active (≤18mo update), pricing/adoption/integrations, URL |
| **Literature (L#)** | 6 | Authoritative, diverse perspectives (business/architecture/organization) |
| **APA Citations (A#)** | 12 | APA 7th, language-tagged (~60% EN, ~30% ZH, ~10% other), ≥50% from last 3 years (≥70% for emerging topics) |

### Validation Gates

1. **Count**: G≥10, T≥5, L≥6, A≥12, Q=40-80 (20/40/40 split)
2. **Citations**: ≥70% questions cite ≥1 source, ≥30% cite ≥2
3. **Language Mix**: EN 50-70%, ZH 20-40%, Other 5-15%
4. **Recency**: ≥50% sources from last 3 years (≥70% for emerging topics)
5. **Diversity**: ≥3 source types, no single type >25%
6. **Links**: All URLs accessible/archived
7. **Cross-References**: All [Ref: ID] resolve to G#/T#/L#/A#
8. **Correctness**: Exactly 1 correct answer per question
9. **Distractors**: Each maps to documented misalignment
10. **Clarity**: All options mutually exclusive, unambiguous
11. **Focus**: ≥70% test translation (not recall)

## Process

### Step 1: Plan Topics (MECE Coverage)

Identify 4-8 clusters covering business-architecture translation. Allocate 5-10 questions per cluster (40-80 total). Apply 20/40/40 difficulty split.

**Examples**: Strategic Modeling, Value/Risk Analysis, Organizational Dynamics, Architectural Translation, Evolution/Adaptation

### Step 2: Collect References

**Glossary (≥10)**: BMC, DDD, Conway's Law, Technical Debt, ADR, Bounded Context. Format: **G#. Term**: Definition + architectural relevance [LANG]

**Tools (≥5)**: Miro, ArchiMate, C4, Confluence, LucidChart, Wardley Maps. Format: **T#. Tool**: Description + pricing/adoption/update/integrations/URL [LANG]

**Literature (≥6)**: Osterwalder, Evans, Vernon, Conway, Skelton, Richardson + Chinese authors (周爱民, 张逸, 肖然). Format: **L#. Author. (Year). *Title*. Publisher.** + relevance

**APA Citations (≥12)**: APA 7th + [LANG] tags. ~60% EN, ~30% ZH, ~10% other. ≥50% from last 3 years (≥70% for emerging topics).

### Step 3: Generate Questions

**Stem**: Business scenario → architectural implication. Test translation, not recall.

**Options**: 1 correct + 3 distractors (outdated practices, correlation/causation confusion, framework misuse).

**Rationale**: Connect business driver to architecture + ≥1 [Ref: ID].

**Distractor Notes**: Document why each distractor is wrong.

**Verify every 10 questions**: 1 correct answer, distractors documented, ≥70% test translation, ≥1 citation/question, options mutually exclusive.

### Step 4: Compile References

Populate G#, T#, L#, A# with proper formatting. Verify all [Ref: ID] resolve, URLs accessible, no orphans, meets minimums.

### Step 5: Validate

Execute gates 1-11. Document failures, fix immediately, re-run until all pass.

## Output Format

### Structure

1. **Table of Contents**: Markdown links to sections (Question Bank by clusters, Reference Sections)
2. **Question Bank**: Organized by clusters
3. **Reference Sections**: G#, T#, L#, A#
4. **Validation Report**: Table with gate status + notes

### Question Format

```markdown
#### Q1: [Business scenario → architectural implication question]

**Difficulty:** [Foundational/Intermediate/Advanced]

**Options:**
- A. [Option]
- B. [Option]
- C. [Option]
- D. [Option]

**Answer:** [A/B/C/D]

**Rationale:** [Connect business to architecture + ≥1 [Ref: ID]]

**Distractor Notes:**
- [Letter]: [Why wrong]
```

### Reference Formats

**Glossary**: **G#. Term**: Definition + architectural relevance [LANG]

**Tools**: **T#. Tool**: Description + pricing/adoption/update/integrations/URL [LANG]

**Literature**: **L#. Author. (Year). *Title*. Publisher.** + relevance

**APA**: **A#. Full APA 7th citation [LANG]**
