# English Pronunciation Q&A Generation Framework

**When:** Decision-critical pronunciation work (exam prep, high-stakes speaking assessments, curriculum design) where high-quality, citation-based Q&As are needed within 4-6 hours.

## Scope & Requirements

Generate 30-40 discriminative pronunciation Q&As for B2-C2 learners comparing GA (General American), RP (Received Pronunciation), and other accents (Indian, Australian, Canadian) with IPA-based phonetic analysis.

**Targets**: 30-40 Q&As | 150-300 words/answer | 25/40/35% Basic/Intermediate/Advanced split
**Citations**: ≥15 refs total (≥8 dictionaries, ≥6 academic, ≥5 guides, ≥3 corpora) | ≥70% Q&As cited | ≥40% recent (<5yr) | ≥3 accent types | Max 20% single source
**Per Cluster**: 5-7 Q&As | ≥1 IPA table + ≥1 diagram | ≥2 dictionaries + ≥1 academic ref
**Timebox**: 4-6 hours to generate the full set; 60-90 minutes for a representative learner session.

**Definitions**: MECE (Mutually Exclusive, Collectively Exhaustive) | IPA (International Phonetic Alphabet) | ≥ (minimum) | ✓/✗ (pass/fail)

## Content Principles

**Coverage**: MECE across vowels, consonants, stress, intonation, connected speech, rhythm, accent comparison
**Depth**: Articulatory descriptions, common errors, minimal pairs, regional variations, perception vs production
**Breadth**: Phonetics (articulation), phonology (patterns), perception, production, sociolinguistics (accents)
**Significance / Essential Only**: Focus on high-frequency patterns (>20% of everyday speech); exclude rare allophones (<5%), archaic pronunciations, obscure dialects, and long theoretical digressions that do not change teaching or learning decisions
**Accuracy**: Cross-reference IPA from multiple authoritative dictionaries (Cambridge, Oxford, Merriam-Webster)
**Neutrality**: Present GA/RP/other as equal variants, not hierarchies; distinguish standard from prestige
**Exclusions**: No general history of English, full phonological theory, or speculative trends without data; prioritize patterns that materially affect learner outcomes

## Workflow

### 1. Plan (6-7 MECE Clusters)
- Allocate 5-7 Q&As per cluster (total 30-40): 25% Basic, 40% Intermediate, 35% Advanced
- Ensure ≥60% GA vs RP, ≥20% other accents; verify ≥15 sources available
**Clusters**: 1) Vowel Sounds 2) Consonant Sounds 3) Word Stress 4) Sentence Stress & Rhythm 5) Intonation 6) Connected Speech 7) Accent Comparison

### 2. Collect References
- Gather ≥8 dictionaries (D1-Dn), ≥6 academic (A1-An), ≥5 guides (P1-Pn), ≥3 corpora (C1-Cn)
- Tag: Accent (GA/RP/Multi), year, type | Ensure GA+RP ≥80%, recent ≥40%
**Required**: Cambridge, Oxford, Longman, Merriam-Webster dictionaries + ≥1 specialized accent dictionary

### 3. Generate Q&As
- Write 150-300 words: IPA transcriptions, articulatory descriptions, minimal pairs, accent comparisons
- Cite ≥1 `[Ref: ID]` for IPA/phonetic claims/accent differences | State concrete Key Insight
- Frame neutrally; prioritize high-frequency patterns (>20%) | Self-review every 5 Q&As: verify claims against sources and flag assumptions or low-confidence areas

### 4. Create Artifacts
- Per cluster: ≥1 IPA table (vowel charts, consonant inventories, GA vs RP, minimal pairs) + ≥1 diagram (vocal tract, stress patterns, intonation contours)

### 5. Compile References
- Complete all fields with edition/year (dictionaries), DOIs (academic) | Verify all `[Ref: ID]` resolve | Mark any unsupported claims as `[Assumption]` and keep them <10% of total content

### 6. Validate

**Tiers**: Express (steps 1,2,6,7) | Standard (steps 1,2,3,5,6,7,8, recommended) | Thorough (all 11)

**Checklist**:
1. Count: 30-40 Q&As, 25/40/35 ratio, 6-7 clusters
2. Citations: ≥70% cited
3. Accent: ≥60% GA/RP, ≥20% other
4. Recency: ≥40% <5yr
5. Diversity: ≥3 types, max 20% single source
6. Links: All accessible
7. Cross-refs: All `[Ref: ID]` resolve
8. Words: Sample 5, verify 150-300
9. IPA: Sample 5, verify against 2+ dictionaries
10. Per-cluster: Table + diagram + ≥2 dictionaries + ≥1 academic
11. Neutrality: Sample 3, no hierarchy

**Report**: `| Check | Result | Status |` (Count, Citations, Accent, Recency, Diversity, Links, Cross-refs, Words, IPA, Per-cluster, Neutrality)

> **CRITICAL**: If ANY fails, halt, fix, regenerate, re-validate.

### 7. Review
- Verify 8 Design Criteria | Sample 3 Q&As for coherence | Verify accent neutrality

## Design Criteria

| Criterion | Requirement |
|---|---|
| **Clarity** | Single unambiguous concept; no compound questions |
| **Signal** | Tests understanding/articulation, not memorization |
| **Significance** | High-frequency (>20%); avoids rare (<5%) |
| **Depth** | Enables discussion of errors, L1 interference, perception vs production |
| **Trade-offs** | Compares ≥2 accents or practice strategies and makes explicit when each is preferable |
| **Balance** | Includes contexts where advice changes and avoids over-general "always"/"never" claims |
| **Realism** | Real-world scenarios; practical application |
| **Discriminative** | Distinguishes B1 vs B2 vs C1 levels |
| **Alignment** | Matches learner level |
| **Neutrality** | No accent hierarchy |

## Output Format

**Structure**: TOC | H2 (clusters) | H4 (questions) | Inline tables/diagrams | References at end

**Q&A Template**:
```markdown
## Cluster: [Area]

#### Q#: [Question]
**Difficulty:** [Basic/Intermediate/Advanced] | **Accent:** [GA/RP/Multi]

**Answer** (150-300 words):
- IPA: /phonemic/, [phonetic] with ˈprimary ˌsecondary stress
- Articulatory descriptions (place, manner, voicing)
- GA vs RP comparison plus at least one other relevant accent where useful
- Minimal pairs/examples with quantified frequency or exam impact where possible
- Common errors and when they are acceptable vs meaning-changing
- Perception vs production tips and ≥2 practice options with clear trade-offs
- Inline citations [Ref: ID]; flag any assumptions or low-confidence areas

**Key Insight:** [Error Pattern | L1 Interference | Accent Difference]

**Artifacts:** IPA Table | Diagram
```

**Citations**: `[Ref: D#]` (Dictionary), `[Ref: A#]` (Academic), `[Ref: P#]` (Guide), `[Ref: C#]` (Corpus)

## Reference Formats

**Dictionaries (D#)**: `**D#: [Name]** (Ed., Year)` | Accent coverage | IPA system | Scope | URL/ISBN  
**Example**: `**D1: Cambridge English Pronouncing Dictionary** (19th ed., 2018) | GA+RP all entries | Standard IPA with syllable boundaries | 230K+ pronunciations | ISBN: 978-1108437707`

**Academic (A#)**: `**A#: [Title]** (Year)` | Authors | Focus | Method | Key findings | DOI  
**Example**: `**A1: Vowel Shifts in Contemporary American English** (2023) | Wells, J.C. | GA vowel regional variation | Corpus 50K speakers | Northern Cities Shift continues | DOI: 10.xxxx/phonetics.2023.12345`

**Guides (P#)**: `**P#: [Title]** (Year, Publisher)` | Audience | Accent | Content type | URL  
**Example**: `**P1: BBC Learning English Pronunciation** (2024, BBC) | Intermediate-advanced | RP+GA | Video+audio+exercises | bbc.co.uk/learningenglish`

**Corpora (C#)**: `**C#: [Name]** (Year)` | Size | Accent coverage | Access | URL  
**Example**: `**C1: Speech Accent Archive** (2024) | 3K+ speakers, 170+ countries | Multiple L1 backgrounds | Public | accent.gmu.edu`

## Scaling & Exceptions

**Large** (>40): 1.5× reference floors | **Constrained** (time-limited): 0.75× mins (≥20 Q&As) | **Specialized** (single accent): 4-5 clusters, 25-30 Q&As

**Priority**: IPA accuracy + accent neutrality > floor counts

**Shortfalls** - Document: Root cause | Impact | Remediation | Risk mitigation (cross-verify IPA with 2+ sources)

## Progress Reporting

**Format**: `Cluster X/7 | Y/35 Q&As | GA:# RP:# Multi:# | # citations (D:# A:# P:# C:#) | Validation: Step #`

**Transparency**: State assumptions/constraints | Document shortfalls with alternatives | Flag confidence (High/Med/Low) on IPA | Self-review: Proficiency levels? IPA verified? Accent-neutral? Examples clear?

## Pronunciation Specifics

**IPA Standards**: /phonemic/ | [phonetic] | ˈprimary ˌsecondary stress | /ˈsɪl.ə.bl̩/ syllable boundaries | Specify simplified IPA systems

**Common Errors**: L1 interference (Spanish /e/→/ɪ/) | Minimal pairs (ship/sheep) | Sound substitution (/θ/→/s/) | Stress misplacement (PHOtograph vs phoTOgraphy) | Connected speech

**Accent Comparison**: Descriptive not prescriptive | Show systematic patterns (GA rhoticity vs RP non-rhoticity) | Note mutual intelligibility | Acknowledge regional variation | Consider L1 perspective
