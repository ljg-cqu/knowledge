# English Pronunciation MCQ Generator

Generate 50-100 expert-level MCQs on English pronunciation: phonetics, phonology, accent variations (American, British, Indian, Australian).

---

## I. Configuration

**Subject**: English Pronunciation

**Inputs**: Audience level, accent focus, difficulty preferences

**Output**: MCQ bank (JSONL + optional Markdown) + validation report

**Defaults**:
```yaml
question_count: 80
difficulty_mix: { foundational: 25%, intermediate: 45%, advanced: 30% }
accent_coverage: { american: 35%, british: 35%, comparison: 20%, other: 10% }
recency_threshold: 36mo
citation_style: APA7
```

**Terms**: Stem, options (4), key, distractors, rationale (1-2 sentences + citations), misconception

**Scaling**: >100 questions → multiply reference minimums by 1.5×

---

## II. Requirements

### Question Structure
- **Format**: 1-2 sentence stem + 4 options (one correct)
- **Difficulty**: Per config mix (25/45/30)
- **Topics**: 8-12 MECE clusters (see Topic Coverage)
- **Distractors**: Map to common misconceptions or L1 interference
- **Rationale**: 1-2 sentences with ≥1 `[Ref: ID]` citation
- **Grading**: Machine-gradable; no partial credit
- **Quality**: Significance, learner relevance, accent neutrality

### Topic Coverage (MECE Clusters)
Balanced question distribution across:

1. **Vowel Sounds** (15-20)
   - Monophthongs, diphthongs, triphthongs
   - American vs British (/æ/ vs /ɑː/, /ɔ/ vs /ɒ/)
   - Reduced vowels (schwa /ə/)

2. **Consonant Sounds** (10-15)
   - Voicing, aspiration
   - Problematic consonants (/θ/, /ð/, /r/, /l/)
   - Consonant clusters

3. **Rhotic vs Non-Rhotic Accents** (8-12)
   - R-pronunciation: American (rhotic) vs British RP (non-rhotic)
   - Post-vocalic /r/, linking/intrusive /r/

4. **Word Stress** (8-12)
   - Primary/secondary stress
   - Stress shifts (PHOtograph vs phoTOGraphy)
   - Compound word stress, American vs British differences

5. **Sentence Stress & Rhythm** (6-10)
   - Content vs function word stress
   - Stress-timed rhythm, contrastive/emphatic stress

6. **Intonation Patterns** (6-10)
   - Rising vs falling intonation
   - Question intonation types
   - American vs British differences

7. **Connected Speech** (8-12)
   - Linking (C-to-V, V-to-V)
   - Assimilation, elision, reduction, weak forms

8. **Common Pronunciation Challenges** (8-12)
   - Silent letters, homophones, minimal pairs
   - Irregular spelling-to-sound patterns
   - False friends across accents

9. **Regional Accent Variations** (6-10)
   - American: General American, Southern, New York
   - British: RP, Cockney, Scottish, Northern
   - Indian and Australian English features

10. **Phonetic Transcription** (5-8)
    - IPA symbol recognition
    - American vs British transcription
    - Stress/intonation marking

11. **Historical Sound Changes** (3-5, advanced)
    - Great Vowel Shift legacy
    - American-British divergence, ongoing changes

12. **Pronunciation & Intelligibility** (3-5)
    - Critical vs non-critical features
    - Accent prestige/bias, World Englishes

### References (Minimums)
| Type | Count | Purpose |
|------|-------|---------|
| **Glossary** | ≥15 | Define phonetic terms, IPA symbols |
| **Phonetic Resources** | ≥8 | IPA charts, pronunciation dictionaries |
| **Academic Literature** | ≥10 | Phonetics textbooks, accent research |
| **Audio/Video Resources** | ≥5 | Pronunciation guides, accent samples |
| **APA Citations** | ≥15 | All sources |

### Citation Standards
- **Format**: APA7 (English sources)
- **IDs**: G# (Glossary), P# (Phonetic), L# (Literature), A# (Audio/Video), C# (Citations)
- **Usage**: `[Ref: ID]` in rationales
- **Hierarchy**: Phonetics textbooks → IPA standards → Peer-reviewed research → Pronunciation dictionaries → Audio
- **Confidence**: Score [0-1] for accent variation claims

### Quality Gates
1. **Recency**: ≥40% sources ≤36mo (classic texts acceptable)
2. **Diversity**: ≥4 types; max 30% single type
3. **Coverage**: ≥80% questions ≥1 citation; ≥40% ≥2
4. **Authority**: Recognized phonetics sources (Wells, Ladefoged, Roach, Cruttenden)
5. **Links**: 100% accessible/archived (DOI preferred)
6. **Integrity**: All `[Ref: ID]` resolve; no orphans
7. **Deduplication**: Canonical URLs only
8. **Accent Balance**: Citations cover American and British sources proportionally

---

## III. Execution Steps

### 1. Planning
- **Identify** 8-12 MECE clusters
- **Allocate** questions per cluster ranges
- **Assign** difficulty per 25/45/30 ratio
- **Balance** accent coverage per 35/35/20/10
- **Verify**: Count, MECE, ratios

### 2. References
- **Gather** minimums (G≥15, P≥8, L≥10, A≥5, C≥15)
- **Include**: IPA charts, phonetics textbooks, pronunciation dictionaries
- **Tag** accent, year, type
- **Assign** IDs
- **Validate** URLs (accessible/archived)
- **Verify**: Counts, accent balance, recency (≥40% ≤36mo), diversity

### 3. Questions
- **Write**: Stem + 4 options (one correct)
- **Tag**: Difficulty, accent focus, topic cluster
- **Include IPA**: Use proper notation
- **Rationale**: ≥1 `[Ref: ID]`
- **Distractors**: Map to errors (L1 interference, spelling pronunciation, accent confusion)
- **Verify** (every 10): One correct? IPA accurate? Quality distractors? ≥1 citation? Accent-neutral?

### 4. Distractor Documentation
- **Document**: Why incorrect + misconception (spelling pronunciation, L1 interference, accent confusion)
- **Note**: Error patterns + learning implications
- **Verify**: All distractors mapped to realistic errors

### 5. Compile References
- **Populate**: All sections (Glossary, Phonetic Resources, Literature, Audio/Video, Citations)
- **Match**: All `[Ref: ID]` to entries
- **Verify**: IDs resolve? IPA correct? Links persistent? Accent tags? Authority?

### 6. Validate
- **Execute** 13 checks
- **Generate** report
- **Fix** failures; **re-validate** until ALL PASS
- **Attach** final ALL PASS report

### 7. Submit
- **Review**: IPA accuracy, accent balance, learner relevance, no bias
- **Verify**: Checklist complete, topic coverage comprehensive
- **Submit** when: ALL PASS + format correct + schema-valid + IPA verified

---

## IV. Output Format

### JSONL Schema (Primary)
```json
{"id":"Q001","accent_focus":"comparison","topic":"Rhotic vs Non-Rhotic","difficulty":"intermediate","stem":"How is the word 'car' /kɑː(r)/ typically pronounced in Received Pronunciation (British)?","options":["A. /kɑːr/ with a clear /r/ sound","B. /kɑː/ without the /r/ sound","C. /kær/ with a short vowel","D. /kɔːr/ with a rounded vowel"],"key":"B","rationale":"Received Pronunciation is non-rhotic, meaning post-vocalic /r/ is not pronounced [Ref: L3] [Ref: P2]","misconceptions":["A: Applying American rhotic pattern to British RP","C: Confusing vowel quality and ignoring non-rhotic feature","D: Incorrect vowel and applying rhotic pattern"],"significance":"Understanding rhotic vs non-rhotic distinction is crucial for accent recognition and production","learner_relevance":"Common confusion point between American and British pronunciation","accent_neutrality":"Question acknowledges both pronunciations as valid in their respective dialects","evidence":[{"title":"English Phonetics and Phonology","author":"Peter Roach","year":2009,"url":"...","citation":"Roach, P. (2009)"}],"confidence":0.98}
```

**Constraints**: `accent_focus` ∈ {american, british, comparison, other}; `difficulty` ∈ {foundational, intermediate, advanced}; `key` ∈ {A,B,C,D}; `confidence` ∈ [0,1]

### Markdown (Optional)
```markdown
### Topic 3: Rhotic vs Non-Rhotic Accents

#### Q15: How is the word 'car' /kɑː(r)/ typically pronounced in Received Pronunciation (British)?
**Difficulty**: Intermediate | **Accent Focus**: Comparison

- A. /kɑːr/ with a clear /r/ sound
- B. /kɑː/ without the /r/ sound
- C. /kær/ with a short vowel
- D. /kɔːr/ with a rounded vowel

**Answer**: B
**Rationale**: Received Pronunciation is non-rhotic, meaning post-vocalic /r/ is not pronounced [Ref: L3] [Ref: P2]
**Significance**: Understanding rhotic vs non-rhotic distinction is crucial for accent recognition
**Learner Relevance**: Common confusion point between American and British
**Accent Neutrality**: Both pronunciations valid in their respective dialects
**Distractors**:
- A: Applying American rhotic pattern | Misconception: Assuming all English has /r/
- C: Confusing vowel quality and missing non-rhotic feature | Misconception: Spelling-based pronunciation
- D: Incorrect vowel and applying rhotic pattern | Misconception: Multiple errors
```

### References

**Usage**: `[Ref: ID]` in rationales → G# (Glossary), P# (Phonetic), L# (Literature), A# (Audio/Video), C# (Citations)

**Example**: "The word is pronounced /kɑː/ in RP because British English is non-rhotic [Ref: G5] as documented by Roach [Ref: L3]."

#### Glossary (Phonetic Terms)
**Format**: `**G#: Term**: Definition with IPA notation`

**Examples**:
- **G1: Rhotic**: Accent where /r/ is pronounced in all positions (e.g., General American)
- **G2: Non-rhotic**: Accent where post-vocalic /r/ is not pronounced (e.g., RP, Boston)
- **G3: Schwa /ə/**: Most common vowel, mid-central reduced vowel in unstressed syllables
- **G4: Diphthong**: Vowel sound gliding from one quality to another within same syllable (e.g., /aɪ/ in "price")
- **G5: Received Pronunciation (RP)**: Prestigious British accent traditionally associated with educated speakers in southern England

#### Phonetic Resources
**Format**: `**P#: Resource Name**`

**Examples**:
```
**P1: IPA Chart (International Phonetic Association)**
- Authority: IPA | URL: https://www.internationalphoneticassociation.org/content/ipa-chart
- Updated: 2020 | Description: Official IPA charts

**P2: Cambridge Dictionary Pronunciation**
- Publisher: Cambridge University Press | URL: https://dictionary.cambridge.org
- Updated: 2024 | Description: American and British pronunciations with IPA
```

#### Literature & Academic Sources
**Format**: `**L#: Title** (Year)`

**Examples**:
```
**L1: A Course in Phonetics** (2014)
- Citation: Ladefoged, P., & Johnson, K. (2014). A Course in Phonetics (7th ed.). Cengage Learning.
- Key Topics: IPA, articulatory phonetics, acoustic phonetics

**L2: Accents of English** (1982)
- Citation: Wells, J. C. (1982). Accents of English (Vols. 1-3). Cambridge University Press.
- Key Topics: Comprehensive survey of English accents worldwide

**L3: English Phonetics and Phonology** (2009)
- Citation: Roach, P. (2009). English Phonetics and Phonology (4th ed.). Cambridge University Press.
- Key Topics: British English phonology, connected speech, intonation
```

#### Audio/Video Resources
**Format**: `**A#: Resource Name**`

**Examples**:
```
**A1: BBC Learning English Pronunciation**
- Provider: BBC | URL: https://www.bbc.co.uk/learningenglish
- Type: Video + Audio | Accents: British (RP, regional)
```

#### Citations (APA7)
**Examples**:
```
Ladefoged, P., & Johnson, K. (2014). A course in phonetics (7th ed.). Cengage Learning.
Roach, P. (2009). English phonetics and phonology (4th ed.). Cambridge University Press.
Wells, J. C. (1982). Accents of English (Vols. 1-3). Cambridge University Press.
```

---

## V. Validation Protocol

**Mandatory**: Generate report before submission. ALL 13 checks must PASS. Re-validate after fixes until clean.

| Check | Pass Criteria | Report Format |
|-------|---------------|---------------|
| **1. Counts** | G≥15, P≥8, L≥10, A≥5, C≥15, Q=50-100, Ratio 25/45/30 (±5%) | `G:X P:Y L:Z A:W C:V Q:N (F/I/A: P%/Q%/R%)` |
| **2. Citations** | ≥80% questions ≥1 cite; ≥40% ≥2 cites | `X/Y ≥1 (Z%); W/Y ≥2 (V%)` |
| **3. Accent Coverage** | American 30-40%, British 30-40%, Comparison 15-25%, Other 5-15% | `AM:X (Y%) BR:A (B%) CMP:C (D%) OTH:E (F%)` |
| **4. Recency** | ≥40% last 36mo (classic texts acceptable) | `X/Y (Z%) last 36mo` |
| **5. Diversity** | ≥4 types; max 30% single | `Types=N; Max=P%` |
| **6. Links** | 100% accessible or archived | `Y/X accessible (list broken)` |
| **7. Cross-refs** | All `[Ref: ID]` resolve; no orphans | `Y/X resolved (list broken)` |
| **8. Correctness** | Exactly one correct per question | `Y/X exactly one (list issues)` |
| **9. Distractors** | All mapped to learner misconceptions | `Y/X quality (list weak)` |
| **10. Options** | All unambiguous | `Y/X clear (list vague)` |
| **11. IPA Accuracy** | All IPA notation verified against standard charts | `Y/X accurate (list errors)` |
| **12. Accent Neutrality** | No accent bias; American/British both valid | `Y/X neutral (list biased)` |
| **13. Quality** | Significance/Learner Relevance/Accent Neutrality/Logic ≥90% each | `S:X/Y LR:W/Y AN:V/Y Logic:U/Y` |

**Report Template**:
```
Config: {question_count: 80, difficulty_mix: 25/45/30, accent_coverage: 35/35/20/10}

Validation:
1. Counts: G:X P:Y L:Z A:W C:V Q:N (F/I/A: P%/Q%/R%) | PASS/FAIL
2. Citations: X/Y ≥1 (Z%); W/Y ≥2 (V%) | PASS/FAIL
3. Accent Coverage: AM:X (Y%) BR:A (B%) CMP:C (D%) OTH:E (F%) | PASS/FAIL
4. Recency: X/Y (Z%) last 36mo | PASS/FAIL
5. Diversity: Types=N; Max=P% | PASS/FAIL
6. Links: Y/X accessible (list broken) | PASS/FAIL
7. Cross-refs: Y/X resolved (list broken) | PASS/FAIL
8. Correctness: Y/X exactly one (list issues) | PASS/FAIL
9. Distractors: Y/X quality (list weak) | PASS/FAIL
10. Options: Y/X clear (list vague) | PASS/FAIL
11. IPA Accuracy: Y/X accurate (list errors) | PASS/FAIL
12. Accent Neutrality: Y/X neutral (list biased) | PASS/FAIL
13. Quality: S:X/Y LR:W/Y AN:V/Y Logic:U/Y | PASS/FAIL

Status: PASS/FAIL
Failed: [List or "None"]
Action: [Plan or "Ready"]
```

**Success**: All minimums met + distributions in range + no ambiguity/overlap + schema-valid + IPA accurate + accent-neutral + all links/refs resolve + ALL PASS.
