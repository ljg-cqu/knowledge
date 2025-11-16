# Statistics Q&A Generator (Minimal Viable)

Generate **4–6 decision-critical scenario-based questions** testing statistical reasoning with evidence-based answers, visuals, and evaluation materials. Minimal viable approach for informed decision-making with time constraints.

**Cadence**: Per analysis cycle | **4–6h effort** | **Expires**: Evergreen (refresh annually or when statistical standards change)

**Scope**: Decision-critical statistical scenarios only—methodological decisions that block conclusions, create risk, or affect ≥2 stakeholders. For practitioners with limited time.

**Exclusions**: Pure proofs, cookbook procedures, syntax trivia, niche methods (<5% adoption), nice-to-have theory.

## I. Context

**Purpose**: Develop decision-critical statistical reasoning through scenarios requiring methodological judgment, interpretation, and application.

**Assumptions**: LLM expertise in hypothesis testing, regression, experimental design, Bayesian/causal inference. Generic datasets. 15–25min/question.

**Constraints**: 150–250 words/answer | ≥70% with ≥1 citation (≥30% with ≥2) | 100% application-based | Progressive difficulty

**Terminology**: F=foundational, I=intermediate, A=advanced | Floors=minimums (≥) | Gates=mandatory checks (fail→stop/fix) | Dimensions=Mathematical/Applied/Interpretive/Computational

**Decision Criticality Framework** (NEW - MANDATORY):
- **Include if ≥1 criterion satisfied**:
  - Blocks Decision: Directly impacts methodological choice, validity conclusion, or research go/no-go
  - Creates Risk: Material threat (Type I/II error, confounding, invalid inference, compliance violation)
  - Affects ≥2 Stakeholders: Multi-role impact (Analyst + Researcher, Data Scientist + Leadership)
  - Actively Evolving: Statistical practice/standards changing (e.g., p-value misuse, Bayesian adoption)
  - Quantified Impact: Adoption %, error rate reduction, decision accuracy improvement
- **Exclude if**: Niche methods (<5% adoption), nice-to-have theory, already covered, pure proofs

## II. Requirements

### Quantitative Floors (Minimal Viable)

**Q&A**: 4–6 | 25%F/50%I/25%A | 150–250 words | ≥70% with ≥1 cite (≥30% with ≥2) | ≥2 dimensions | ≥60% with worked examples

**Topics (Decision-Critical Only)**: 
1. Inference & Hypothesis Testing (1–2) — Blocks decision: p-value misuse, power analysis
2. Experimental Design & Causal Inference (1–2) — Blocks decision: confounding, RCT vs. observational
3. Regression & Modeling (1–2) — Creates risk: assumption violations, multicollinearity
4. Applied Statistics & Interpretation (1–2) — Affects stakeholders: actionable insights, communication

**References**: Glossary ≥8 | Tools ≥3 | Textbooks ≥5 | Citations ≥8 (APA 7th + [EN]/[ZH] tags)

**Visuals**: ≥1 diagram + ≥1 table per topic (4+4 minimum)

**Evaluation**: ≥2 practice problems per Q&A with solutions | Pitfall checklist per topic | Assumption validation guides

### Citation Standards

**Format**: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: ID]` (G#=Glossary, T#=Tool, L#=Textbook, A#=Citation)

**Distribution**: EN 60–80% | ZH 10–30% | Other 5–15% | **Source Types** (≥4): Textbooks, papers, software docs, case studies

### Quality Gates (fail ANY → stop/fix/revalidate ALL)

1. **Math Accuracy**: 100% formulas verified
2. **Source Diversity**: ≥4 types; max 30%/type
3. **Per-Topic Evidence**: Each has ≥2 texts + ≥1 applied ref + ≥1 tool
4. **Software Docs**: Version, URL, capabilities, update (≤24mo)
5. **Links**: 100% accessible/archived
6. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans
7. **Assumptions**: All explicit
8. **Worked Examples**: ≥60% with numerical solutions

## III. Execution (Minimal Viable - 4–6h)

### Step 1: Plan Allocation (30 min)

Distribute 4–6 across 4 decision-critical topics (25%F/50%I/25%A). Each topic: 1–2 Q&A with ≥1 reasoning signal.

**Example** (6 total): Inference (2), Design (1), Regression (2), Applied (1) = 1F/3I/2A

### Step 2: Build References (30–45 min) — BEFORE Q&A

**Glossary (≥8)**: Decision-critical terms only—p-value, confidence interval, Type I/II error, power, confounding, effect size, multicollinearity, bias-variance tradeoff.

**Format**: Term | Math definition (1–2 sentences) | Intuition | When to use | Misinterpretations | Assign G1–G8

**Software/Tools (≥3)**: R, Python/statsmodels, Tableau (canonical only).

**Include**: Category, version, capabilities, URL, learning curve, methods, update (≤24mo) | Assign T1–T3

**Textbooks (≥5)**: Casella & Berger (*Statistical Inference*), Gelman & Hill (*Regression*), Montgomery (*Design & Analysis*), Gelman et al. (*Bayesian Data Analysis*), McElreath (*Statistical Rethinking*)

**Include**: Author, title, year, focus, math level, key topics | Assign L1–L5

**Citations (≥8)**: APA 7th + tags | ≥50% applied/methods (last 5yrs) | Sources: JASA, J Statistical Software, arXiv stat.ME | Assign A1–A8

### Step 3: Generate Q&A (2–3 at a time → self-check each batch) (2–3h)

**Question Design**:
- Scenario-based ("Given data...", "A researcher finds...")
- Include constraints (sample size, violations, missing data, confounding)
- Test ≥2 reasoning signals (assumption validation, method choice, interpretation, robustness, limitations)
- Single focused ask
- **Avoid**: "Define X", "List Y assumptions", "Calculate Z" (without context)

**Difficulty**:
- F=foundational concepts ("Check normality?")
- I=intermediate application/interpretation ("Linear vs. logistic with censored outcomes?")
- A=advanced inference/design ("Adaptive trial with interim analysis—control Type I?")

**Answer Structure** (150–250 words):
1. Key insight (1–2 sentences)
2. Framework/method [Ref: G#/L#/A#] with notation
3. ≥2 dimensions (Mathematical/Applied/Interpretive/Computational)
4. Step-by-step + explicit assumptions
5. Worked example (≥60%): data, calculations, interpretation
6. Trade-offs (power/assumptions, bias/variance, interpretability/flexibility)
7. Common pitfalls
8. Software notes [Ref: T#]
9. Citations (≥1; ≥2 for A)
10. Artifact (≥60%): plot, decision tree, derivation, table

**Batch Self-Check** (per 2–3): Application-based | ≥2 reasoning signals | 150–250 words | Concrete insight | ≥2 dimensions | ≥2/3 worked examples | ≥2/3 with ≥1 cite (≥1/3 with ≥2) | Difficulty matches level | Assumptions explicit

### Step 4: Create Visuals (30–45 min) — ≥1 diagram + ≥1 table per topic

**Topics**: Hypothesis testing flowcharts, CI interpretation, power curves, residual/Q-Q plots, decision trees, method comparison tables, assumption checklists

**Best Practices**: Tables→numerical comparisons | Diagrams→decision processes | Plots→distributions/diagnostics | Include axis labels, units, sample sizes, critical regions | Cite software

### Step 5: Populate References (15 min)

**Glossary**: **G#. Term** | Math definition + notation | Intuition | When to use | Misinterpretations | Alphabetize

**Tools**: **T#. Software (Category)** | Description | Version | Capabilities | URL | Learning curve | Update (Month YYYY)

**Textbooks**: **L#. Author(s), Title, Year** | Focus | Math level | Key topics

**Citations**: **A#. [Citation] [Lang]** | APA 7th + tags | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA tagged | Formulas verified

### Step 6: Run 12 Validations (Streamlined) (30–45 min) — fail ANY → stop/fix/re-run ALL

1. **Floors**: G≥8, T≥3, L≥5, A≥8, Q=4–6, 25%F/50%I/25%A
2. **Citations**: ≥70% with ≥1; ≥30% with ≥2
3. **Language**: EN 60–80%, ZH 10–30%, Other 5–15%
4. **Math**: Sample 3 formulas; 100% verified
5. **Source Types**: ≥3; max 40%/type
6. **Links**: 100% accessible/archived
7. **Cross-Refs**: 100% resolve; no orphans
8. **Word Count**: Sample 3; 100% in 150–250
9. **Insights**: 100% concrete + decision-critical
10. **Per-Topic**: 4/4 have ≥2 texts + ≥1 applied + ≥1 tool
11. **Decision Criticality**: 100% satisfy ≥1 criterion [Blocks/Risk/Stakeholders/Evolving/Quantified]
12. **Assumptions**: Sample 3; 100% explicit

### Step 7: Final Review (15 min)

**Questions**: Clarity (focused ask) | Signal (statistical reasoning) | Depth (trade-offs, assumptions) | Realism (practical scenarios) | Decision Criticality (blocks decision or creates risk)

**Answers** (sample ≥3): ≥2 dimensions | Step-by-step + explicit assumptions | Worked examples | Trade-offs | Pitfalls | Software notes

**Evaluation Materials**: ≥2 practice problems per Q&A + solutions | Pitfall checklist per topic | Assumption validation guides

**Submission**: 12 validations PASS | Floors met | Decision Criticality Framework applied | TOC with links | No placeholders | Consistent notation

## IV. Validation Report (Streamlined - 12 Checks) — ANY fail → stop/fix/re-run ALL

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A) | G≥8, T≥3, L≥5, A≥8, Q:4-6, 25/50/25% | | PASS/FAIL |
| 2 | Citations | __%≥1, __%≥2 | ≥70%≥1, ≥30%≥2 | | PASS/FAIL |
| 3 | Language | EN:_%, ZH:_%, Other:_% | EN:60-80%, ZH:10-30%, Other:5-15% | | PASS/FAIL |
| 4 | Math | __ sampled: __ verified | 100% | | PASS/FAIL |
| 5 | Sources | __ types; max __% | ≥3; max 40% | | PASS/FAIL |
| 6 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 7 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 8 | Words | __ sampled: __ in range | 100% (150-250) | | PASS/FAIL |
| 9 | Insights | __/__ concrete + decision-critical | 100% | | PASS/FAIL |
| 10 | Per-Topic | __/4 (≥2 texts+≥1 app+≥1 tool) | 4/4 | | PASS/FAIL |
| 11 | Decision Criticality | __/__ satisfy ≥1 criterion | 100% [Blocks/Risk/Stakeholders/Evolving/Quantified] | | PASS/FAIL |
| 12 | Assumptions | __ sampled: __ explicit | 100% | | PASS/FAIL |

## V. Question Quality (fails ≥2 → rewrite/replace)

1. **Clarity**: Focused ask | ✓ "Test normality with n=30, right-skewed—approach?" | ✗ "Explain normality and test heteroskedasticity"
2. **Signal**: Statistical reasoning | ✓ "p=0.06, d=0.8—interpretation?" | ✗ "Define p-value"
3. **Depth**: Methodological trade-offs | ✓ "Regression vs. propensity matching for causal inference—factors?" | ✗ "Use regression?—yes/no"
4. **Realism**: Practical scenarios | ✓ "40% missing income. Imputation vs. complete case—factors?" | ✗ "Derive MLE for normal"
5. **Discriminative**: Application>memorization | ✓ "When is t-test inappropriate despite normality?" | ✗ "What are t-test assumptions?"
6. **Alignment**: Difficulty∼math level | F: foundational concepts | I: intermediate application/interpretation | A: advanced inference/design

## VI. Output Format (Minimal Viable)

### A. TOC
1. Topic Overview | 2. Q&A by Topic (4) | 3. References (Glossary, Tools, Textbooks, Citations) | 4. Evaluation Materials | 5. Validation Report

### B. Topic Overview
**Total**: [4–6] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 4 decision-critical topics

| # | Topic | Range | Count | Mix | Decision Criticality | Artifacts |
|---|-------|-------|-------|-----|---------------------|-----------|
| 1 | Inference & Hypothesis Testing | Q1–Q2 | 1–2 | 1F/1I or 1I/1A | Blocks decision: p-value misuse, power analysis | 1 diagram+table |
| 2 | Experimental Design & Causal | Q3 | 1–2 | 1F/1I or 1I/1A | Blocks decision: confounding, RCT vs. observational | 1 diagram+table |
| 3 | Regression & Modeling | Q4–Q5 | 1–2 | 1F/1I or 1I/1A | Creates risk: assumption violations, multicollinearity | 1 diagram+table |
| 4 | Applied Statistics & Interpretation | Q6 | 1–2 | 1F/1I or 1I/1A | Affects stakeholders: actionable insights, communication | 1 diagram+table |
| | **Total** | | **4–6** | **1F/3I/2A** | **100% decision-critical** | **4+4** |

Legend: F=foundational | I=intermediate | A=advanced

### C. Q&A Format (Minimal Viable)

**Topic 1: [Title]**

**Q1: [Question with Data Context]**

**Difficulty**: [F/I/A] | **Topic**: [Area] | **Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Quantified]

**Key Insight**: [1–2 sentences—core issue]

**Answer** (150–250 words): Method/framework [Ref: G#/L#/A#] + notation | ≥2 dimensions (Math/Applied/Interpretive/Computational) | Step-by-step + explicit assumptions | Worked example: data, calculations, interpretation | Trade-offs | Pitfalls | Software [Ref: T#] | ≥1 [Ref: ID] (≥2 for A)

**Artifact**: Plot, decision tree, derivation, comparison table

**Common Pitfalls**: [2–3 specific errors]

**Justification**: Why this Q&A is decision-critical [cite Decision Criticality criterion]

### D. Reference Formats

**Glossary**: **G#. Term** | Math definition + notation | Intuition | When to use | Misinterpretations | Related | Alphabetize

**Tools**: **T#. Software (Category)** | Description | Version | Capabilities | URL | Learning curve | Update (Month YYYY) | Use cases | Group by category

**Textbooks**: **L#. Author(s), Title, Year** | Focus | Math level | Key topics | Audience | Features | Group by category

**Citations**: **A#. [Citation] [Lang]** | APA 7th + tags | ZH→transliteration

### E. Evaluation Materials (Minimal Viable)

**Practice Problems**: ≥2 per Q&A with solutions

**Pitfall Checklists**: 2–3 per topic with explanations

**Assumption Guides**: Flowcharts for checking assumptions + diagnostic tests

## VII. Example (Minimal Viable)

**Q1: A clinical trial with n=45 shows treatment mean=12 (SD=8) vs. control mean=8 (SD=7). Two-sample t-test yields p=0.04, Cohen's d=0.53. Original power analysis assumed d=0.8 for n=40. How should you interpret these results and what additional analyses would strengthen the conclusion?**

**Difficulty**: I | **Topic**: Statistical Inference | **Decision Criticality**: Blocks decision (p-value misuse, power analysis)

**Key Insight**: Distinguish statistical significance from practical significance; recognize underpowered studies. p=0.04 barely crosses α=0.05 while d=0.53 falls short of design d=0.8, raising robustness questions.

**Answer** (200 words):

**Framework**: Integrated evaluation combining significance testing, effect size, power analysis [Ref: L2, A3]. Dichotomous p-value interpretation insufficient—examine CIs, practical significance [Ref: A5].

**Multi-dimensional** (Interpretive/Applied):

**1. Statistical vs. Practical Significance**: p=0.04 marginal; d=0.53 (medium) below design d=0.8. 95% CI: 4 ± 2.02 × 2.28 ≈ (−0.6, 8.6) includes 0 [Ref: G2].

**2. Power**: Observed d=0.53, n=45 → post-hoc power ≈ 0.45 [Ref: T1]. Underpowered for d≈0.5. Original design (d=0.8, n=40, power=0.80) optimistic [Ref: A7].

**3. Assumptions** [Ref: G1]:
- Normality: n=45, CLT applies. Check Q-Q plots, Shapiro-Wilk [Ref: T2—R]
- Equal variance: Levene's test; use Welch's t-test if violated
- Independence: Verify randomization

**Trade-offs**: Strict α=0.05 protects Type I error but ignores effect size. Bayesian approach incorporates priors [Ref: L3, G5].

**Software** [Ref: T2]: R—`t.test(treatment, control, var.equal=FALSE)`, `pwr.t.test(d=0.53, n=45)`, `qqnorm()`.

**Recommendation**: "Treatment shows moderate improvement (d=0.53, 95% CI: [−0.6, 8.6], p=0.04), but underpowered. Replicate with n≥70 for 80% power at d=0.5."

**Common Pitfalls**:
- Interpreting p=0.04 as "proof" (ignore effect size, CI, power)
- Post-hoc power for observed effect (circular reasoning) [Ref: A8]
- Ignoring assumption violations

**Justification**: Blocks decision—p-value misuse is endemic; practitioners confuse statistical with practical significance, leading to invalid conclusions.

**Artifact**:

| Component | Result | Interpretation | Action |
|-----------|--------|----------------|--------|
| p-value | 0.04 | Marginal (barely < 0.05) | Report with caution |
| Effect (d) | 0.53 | Medium, below design (0.8) | Acknowledge discrepancy |
| 95% CI | (−0.6, 8.6) | Includes 0; wide | Highlight uncertainty |
| Post-hoc power | ~0.45 | Underpowered (< 0.80) | Recommend replication |
| Normality | p > 0.05 | No violation | Proceed with t-test |
| Equal variance | p > 0.05 | Homoscedastic | t-test OK |
