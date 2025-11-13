# Statistics Q&A Generator with Deep Understanding Framework

Generate 25–30 scenario-based questions testing statistical reasoning, application, and interpretation with evidence-based answers, visual artifacts, and evaluation materials.

## I. Context & Scope

**Purpose**: Develop comprehensive statistical understanding through multi-dimensional scenarios requiring methodological judgment, interpretation, and practical application.

**Assumptions**: LLM has expertise in hypothesis testing, regression, experimental design, Bayesian/causal inference, distribution theory. Uses generic datasets. 10–20min solution time per question.

**Constraints**: 200–400 words/answer | ≥70% with ≥1 citation (≥30% with ≥2) | 100% application-based | Progressive difficulty

**Terminology**: 
- **Difficulty**: F=foundational, I=intermediate, A=advanced
- **Floors**: Minimum thresholds (≥)
- **Gates**: Mandatory checkpoints (fail→stop/fix)
- **Dimensions**: Mathematical/Applied/Interpretive/Computational

**Scope**: Real-world data scenarios, methodological decisions, assumption validation, interpretation challenges, experimental design

**Exclusions**: Pure mathematical proofs, cookbook procedures, syntax trivia, domain-specific expertise without statistical reasoning

**Limitations & Risks**: Generic datasets lack domain context; citation availability varies; computational examples prioritize concepts over syntax. **Mitigation**: Use multiple citation sources; provide explicit assumptions; focus on transferable reasoning patterns.

## II. Requirements

### Quantitative Floors

**Q&A**: 25–30 total | 20%F/40%I/40%A (±5%) | 200–400 words | ≥70% with ≥1 cite (≥30% with ≥2) | ≥2 dimensions | ≥60% with worked examples

**Topics (MECE)**: 
1. Foundations & Probability (4–5)
2. Inference & Hypothesis Testing (5–6)
3. Regression & Modeling (5–6)
4. Experimental Design & Causal Inference (4–5)
5. Multivariate & Advanced Methods (4–5)
6. Applied Statistics & Interpretation (4–5)

**References** (build before Q&A): Glossary ≥12 | Tools ≥5 | Textbooks ≥8 | Citations ≥15 (APA 7th + [EN]/[ZH] tags) | **Scaling**: >30 Q&A → 1.5× reference floors

**Visuals**: ≥1 diagram + ≥1 table per topic (6+6 minimum) | Include distribution/diagnostic plots, decision trees where applicable

**Evaluation**: ≥5 practice problems with solutions | Common pitfall checklist per topic | Assumption validation guides

### Citation Standards

**Format**: `Author, A. (Year). *Title*. Publisher. [EN]` | Inline: `[Ref: ID]` (G#=Glossary, T#=Tool, L#=Textbook, A#=Citation)

**Distribution**: EN 60–80% | ZH 10–30% | Other 5–15% | **Source Types** (≥4): Textbooks, research papers, software docs, case studies

### Quality Gates (fail ANY → stop/fix/revalidate ALL)

1. **Math Accuracy**: 100% formulas verified
2. **Source Diversity**: ≥4 types; max 30%/type
3. **Per-Topic Evidence**: Each has ≥2 texts + ≥1 applied ref + ≥1 tool
4. **Software Docs**: Version, URL, capabilities, update (≤24mo)
5. **Links**: 100% accessible/archived
6. **Cross-Refs**: 100% [Ref: ID] resolve; no orphans
7. **Assumptions**: All explicit
8. **Worked Examples**: ≥60% with numerical solutions

**Mitigation**: Accuracy→re-verify | Diversity→expand sources | Link→archive/replace | Assumptions→add explicit sections

## III. Execution

### Step 1: Plan Allocation

Distribute 25–30 across 6 topics (20%F/40%I/40%A). Each topic: 4–6 Q&A with ≥1F, ≥1I, ≥1A.

**Example** (30 total): Foundations (5), Inference (6), Regression (6), Design (5), Multivariate (4), Applied (4) = 6F/12I/12A

### Step 2: Build References (BEFORE Q&A → run Gates 1–8 after)

**Glossary (≥12)**: Core terms—p-value, confidence interval, Type I/II error, power, bias-variance tradeoff, multicollinearity, heteroskedasticity, confounding, effect size, degrees of freedom, maximum likelihood, Bayesian prior. Optional: credible interval, Fisher information, sufficient statistic, ANOVA, bootstrapping, cross-validation.

**Format**: Term | Math definition (1–2 sentences) | Intuition | When to use | Misinterpretations | Related concepts | Assign G1, G2...

**Software/Tools (≥5)**: Statistical Computing (R, Python/scipy/statsmodels), Commercial (SAS, SPSS, Stata), Visualization (ggplot2, matplotlib, Tableau), Design (JMP, Minitab), Bayesian (Stan, PyMC).

**Include**: Category, version, capabilities, URL, learning curve, methods, update (≤24mo) | Assign T1, T2...

**Textbooks (≥8)**: 
- Foundational: Casella & Berger (*Statistical Inference*), Wasserman (*All of Statistics*), Rice (*Mathematical Statistics*)
- Applied: Gelman & Hill (*Regression*), Kutner et al. (*Applied Linear Models*), Montgomery (*Design & Analysis*)
- Bayesian: Gelman et al. (*Bayesian Data Analysis*), McElreath (*Statistical Rethinking*)

**Include**: Author, title, year, focus, math level, audience, key topics | Assign L1, L2...

**Citations (≥15)**: APA 7th + tags | Foundational texts (any year) + ≥40% applied/methods (last 5yrs) | Classify: theory/methodology/applications/software | Assign A1, A2...

**Sources**: JASA, Annals of Statistics, J Statistical Software, arXiv stat.ME, Cross Validated

### Step 3: Generate Q&A (5 at a time → self-check each batch)

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

**Answer Structure** (200–400 words):
1. Key insight (1–2 sentences): core issue
2. Framework/method [Ref: G#/L#/A#] with notation
3. Multi-dimensional (≥2): Mathematical/Applied/Interpretive/Computational
4. Step-by-step + explicit assumptions
5. Worked example (≥60%): data, calculations, interpretation
6. Trade-offs (power/assumptions, bias/variance, interpretability/flexibility)
7. Diagnostics + robustness
8. Common pitfalls
9. Software notes [Ref: T#]
10. Citations (≥1; ≥2 for A)
11. Artifact (≥60%): plot, decision tree, derivation, table

**Batch Self-Check** (per 5): Application-based | ≥2 reasoning signals | 200–400 words | Concrete insight | ≥2 dimensions | ≥3/5 worked examples | ≥3/5 with ≥1 cite (≥1/5 with ≥2) | Difficulty matches level | Assumptions explicit

### Step 4: Create Visuals (≥1 diagram + ≥1 table per topic; reference from ≥50% answers)

**Topics**: 
1. Foundations—distribution plots (normal, t, χ², F), probability trees
2. Inference—hypothesis testing flowchart, CI interpretation, power curves
3. Regression—residual/Q-Q/leverage plots, decision tree
4. Design—randomization schemes, factorial layouts, ANOVA decomposition
5. Multivariate—correlation matrices, scree plots, dendrograms
6. Applied—diagnostic flowcharts, method comparison tables, assumption checklists

**Best Practices**: Tables→numerical comparisons | Diagrams→decision processes | Plots→distributions/diagnostics | Include axis labels, units, sample sizes, critical regions | Cite software

### Step 5: Populate References

**Glossary**: **G#. Term** | Math definition (with notation) | Intuition | When to use | Misinterpretations | Related concepts | Alphabetize

**Tools**: **T#. Software (Category)** | Description | Version | Capabilities | URL | Learning curve (beginner/intermediate/advanced) | Update (Month YYYY) | Use cases | Group by category

**Textbooks**: **L#. Author(s), Title, Year** | Focus | Math level (intro/intermediate/advanced) | Key topics | Audience | Special features | Group by category

**Citations**: **A#. [Citation] [Lang]** | Books: `Author, A., & Author, B. (Year). *Title* (Ed.). Publisher. [EN]` | Journal: `Author, A. (Year). Title. *Journal*, Vol(Issue), pages. DOI [EN]` | Docs: `Project. (Year). *Title*. URL [EN]` | ZH→transliteration | Sort by ID

**Check**: 100% [Ref: ID] resolve | No orphans | All fields complete | All APA tagged | Formulas verified | Versions specified

### Step 6: Run 14 Validations (fail ANY → stop/fix/re-run ALL)

1. **Floors**: G≥12, T≥5, L≥8, A≥15, Q=25–30, 20%F/40%I/40%A (±5%)
2. **Citations**: ≥70% with ≥1; ≥30% with ≥2
3. **Language**: EN 60–80%, ZH 10–30%, Other 5–15%
4. **Math**: Sample 5 formulas; 100% verified
5. **Source Types**: ≥4; max 30%/type
6. **Links**: 100% accessible/archived
7. **Cross-Refs**: 100% resolve; no orphans
8. **Word Count**: Sample 5; 100% in 200–400
9. **Insights**: 100% concrete (specific issue)
10. **Per-Topic**: 6/6 have ≥2 texts + ≥1 applied + ≥1 tool
11. **Methods**: ≥80% correct + cited + assumptions + limits
12. **Application**: ≥70% scenario-based
13. **Examples**: ≥60% with numerical solutions
14. **Assumptions**: Sample 5; 100% explicit

### Step 7: Final Review

**Questions**: Clarity (focused ask) | Signal (statistical reasoning) | Depth (trade-offs, assumptions) | Realism (practical scenarios) | Discriminative (application>recall) | Alignment (difficulty∼math level)

**Answers** (sample ≥5): ≥2 dimensions | Step-by-step + explicit assumptions | Worked examples (where required) | Trade-offs (power/assumptions/bias-variance) | Diagnostics | Pitfalls | Software notes | Limitations/robustness

**Evaluation Materials**: Practice problems + solutions | Pitfall checklists per topic | Assumption validation guides | Method selection flowcharts | Diagnostic interpretation guides

**Submission**: 14 validations PASS | Floors met | 8 gates passed | TOC with links | No placeholders | Consistent notation | Balanced perspectives (frequentist/Bayesian, parametric/nonparametric, classical/modern)

## IV. Validation Report (fill all; ANY fail → stop/fix/re-run ALL)

| # | Check | Measurement | Criteria | Result | Status |
|---|-------|-------------|----------|--------|--------|
| 1 | Floors | G:__ T:__ L:__ A:__ Q:__ (__F/__I/__A) | G≥12, T≥5, L≥8, A≥15, Q:25-30, 20/40/40% | | PASS/FAIL |
| 2 | Citations | __%≥1, __%≥2 | ≥70%≥1, ≥30%≥2 | | PASS/FAIL |
| 3 | Language | EN:_%, ZH:_%, Other:_% | EN:60-80%, ZH:10-30%, Other:5-15% | | PASS/FAIL |
| 4 | Math | __ sampled: __ verified | 100% verified | | PASS/FAIL |
| 5 | Sources | __ types; max __% | ≥4; max 30% | | PASS/FAIL |
| 6 | Links | __/__ accessible | 100% | | PASS/FAIL |
| 7 | Cross-Refs | __/__ resolved | 100% | | PASS/FAIL |
| 8 | Words | __ sampled: __ in range | 100% (200-400) | | PASS/FAIL |
| 9 | Insights | __/__ concrete | 100% | | PASS/FAIL |
| 10 | Per-Topic | __/6 (≥2 texts+≥1 app+≥1 tool) | 6/6 | | PASS/FAIL |
| 11 | Methods | __/__ correct+cited+assumptions+limits | ≥80% | | PASS/FAIL |
| 12 | Application | __% scenario-based | ≥70% | | PASS/FAIL |
| 13 | Examples | __% with numerical solutions | ≥60% | | PASS/FAIL |
| 14 | Assumptions | __ sampled: __ explicit | 100% | | PASS/FAIL |

## V. Question Quality (review each; fails ≥2 → rewrite/replace)

1. **Clarity**: Focused ask | ✓ "Test normality with n=30, right-skewed—approach?" | ✗ "Explain normality and test heteroskedasticity"
2. **Signal**: Statistical reasoning | ✓ "p=0.06, d=0.8—interpretation?" | ✗ "Define p-value"
3. **Depth**: Methodological trade-offs | ✓ "Regression vs. propensity matching for causal inference—factors?" | ✗ "Use regression?—yes/no"
4. **Realism**: Practical scenarios | ✓ "40% missing income. Imputation vs. complete case—factors?" | ✗ "Derive MLE for normal"
5. **Discriminative**: Application>memorization | ✓ "When is t-test inappropriate despite normality?" | ✗ "What are t-test assumptions?"
6. **Alignment**: Difficulty∼math level | F: foundational concepts/checks | I: intermediate application/interpretation/trade-offs | A: advanced inference/design/decisions

## VI. Output Format

### A. TOC
1. Topic Overview | 2. Q&A by Topic (6) | 3. References (Glossary, Tools, Textbooks, Citations) | 4. Evaluation Materials | 5. Validation Report

### B. Topic Overview
**Total**: [25–30] | **Difficulty**: [X]F ([Y]%) / [X]I ([Y]%) / [X]A ([Y]%) | **Coverage**: 6 competencies (MECE)

| # | Topic | Range | Count | Mix | Artifacts |
|---|-------|-------|-------|-----|-----------|
| 1 | Foundations & Probability | Q1–Q5 | 5 | 1F/2I/2A | 1 diagram+table |
| 2 | Inference & Hypothesis Testing | Q6–Q11 | 6 | 1F/2I/3A | 1 diagram+table |
| 3 | Regression & Modeling | Q12–17 | 6 | 1F/3I/2A | 1 diagram+table |
| 4 | Experimental Design & Causal | Q18–22 | 5 | 1F/2I/2A | 1 diagram+table |
| 5 | Multivariate & Advanced | Q23–26 | 4 | 1F/1I/2A | 1 diagram+table |
| 6 | Applied Statistics | Q27–30 | 4 | 1F/2I/1A | 1 diagram+table |
| | **Total** | | **30** | **6F/12I/12A** | **6+6** |

Legend: F=foundational | I=intermediate | A=advanced

### C. Q&A Format

**Topic 1: [Title]**

**Q1: [Question with Data Context]**

**Difficulty**: [F/I/A] | **Topic**: [Area]

**Key Insight**: [1–2 sentences—core issue]

**Answer** (200–400 words): Method/framework [Ref: G#/L#/A#] + notation | ≥2 dimensions (Math/Applied/Interpretive/Computational) | Step-by-step + explicit assumptions | Worked example (if applicable): data, calculations, interpretation | Trade-offs (power/assumptions/bias-variance/interpretability) | Diagnostics + robustness | Common pitfalls | Software [Ref: T#] | ≥1 [Ref: ID] (≥2 for A)

**Artifact** *(≥60%)*: Plot, decision tree, derivation, comparison table

**Common Pitfalls**: [2–3 specific errors]

### D. Reference Formats

**Glossary**: **G#. Term** | Math definition + notation | Intuition | When to use | Misinterpretations | Related | Alphabetize

**Tools**: **T#. Software (Category)** | Description | Version | Capabilities | URL | Learning curve | Update (Month YYYY) | Use cases | Group by category

**Textbooks**: **L#. Author(s), Title, Year** | Focus | Math level | Key topics | Audience | Features | Group by category

**Citations**: **A#. [Citation] [Lang]** | APA 7th + tags | ZH→transliteration

### E. Evaluation Materials Format

**Practice Problems**: ≥5 per topic with step-by-step solutions

**Pitfall Checklists**: 5–8 per topic with explanations

**Assumption Guides**: Flowcharts for checking assumptions + diagnostic tests

**Method Decision Trees**: Visual guides for method selection based on data characteristics

## VII. Example

**Q1: A clinical trial with n=45 shows treatment mean improvement of 12 points (SD=8) vs. control mean of 8 points (SD=7). Two-sample t-test yields p=0.04, Cohen's d=0.53. The original power analysis assumed d=0.8 for n=40. How should you interpret these results and what additional analyses would strengthen the conclusion?**

**Difficulty**: I | **Topic**: Statistical Inference & Hypothesis Testing

**Key Statistical Insight**: Tests ability to distinguish statistical significance from practical significance, recognize underpowered studies, and recommend sensitivity analyses. The p=0.04 barely crosses α=0.05 while effect size (d=0.53) falls short of design assumption (d=0.8), raising robustness and clinical relevance questions.

**Answer** (378 words):

**Statistical Framework**: Use integrated evaluation combining significance testing, effect size estimation, power analysis, and robustness checks [Ref: L2, A3]. Dichotomous p-value interpretation is insufficient—examine confidence intervals, practical significance, and assumptions [Ref: A5].

**Multi-dimensional Analysis** (Interpretive/Applied/Computational):

**1. Statistical vs. Practical Significance**: p=0.04 indicates result unlikely under H₀, but marginal. Cohen's d=0.53 (medium effect) [Ref: G8] suggests moderate practical importance, but falls short of design target (d=0.8). Compute 95% CI for difference: (12-8) ± t₀.₀₂₅,₄₃ × SE ≈ 4 ± 2.02 × 2.28 ≈ (−0.6, 8.6). Interval includes 0 (barely), confirming marginal significance [Ref: G2].

**2. Power Analysis**: Observed d=0.53 with n=45 yields post-hoc power ≈ 0.45 [Ref: T1—GPower]. Study was underpowered for detecting true effect if d≈0.5. Original power calculation (d=0.8, n=40, power=0.80) was optimistic [Ref: A7].

**3. Assumptions Check** [Ref: G1]:
- **Normality**: With n=45, CLT applies if outliers minimal. Check Q-Q plots, Shapiro-Wilk test [Ref: T2—R shapiro.test()].
- **Equal variance**: Levene's test for homoscedasticity. If violated, use Welch's t-test (already robust).
- **Independence**: Verify randomization protocol; check for clustering/time trends.

**4. Robustness Checks**:
- **Permutation test**: Non-parametric alternative confirming p-value [Ref: L5].
- **Bootstrap CI**: Empirical confidence interval for difference [Ref: A9].
- **Sensitivity analysis**: Remove influential observations; reassess stability.

**Trade-offs**: (1) Strict α=0.05: Protects Type I error but ignores effect size; (2) Consider α=0.10: Increases power but higher false positives; (3) Bayesian approach: Incorporates prior information, provides probability statements [Ref: L7, G11]; (4) Equivalence testing: Test if difference is practically negligible [Ref: A11].

**Software Implementation** [Ref: T2]: R code—`t.test(treatment, control, var.equal=FALSE)`, `pwr.t.test(d=0.53, n=45)`, `qqnorm()`, `leveneTest()`.

**Recommendation**: Report results with caution. State: "Treatment shows moderate improvement (d=0.53, 95% CI: [−0.6, 8.6], p=0.04), but study was underpowered. Replicate with n≥70 for 80% power at d=0.5. Consider Bayesian analysis to incorporate prior evidence."

**Common Pitfalls**:
- Interpreting p=0.04 as "proof" of effect (ignore effect size, CI, power)
- Post-hoc power analysis for observed effect (circular reasoning) [Ref: A13]
- Ignoring assumption violations with moderate n

**Artifact**:

| Analysis Component      | Result         | Interpretation                          | Action                           |
|-------------------------|----------------|-----------------------------------------|----------------------------------|
| p-value                 | 0.04           | Marginal significance (barely < 0.05)   | Report with caution              |
| Effect size (Cohen's d) | 0.53           | Medium effect, below design (0.8)       | Acknowledge discrepancy          |
| 95% CI for difference   | (−0.6, 8.6)    | Includes 0; wide interval               | Highlight uncertainty            |
| Post-hoc power          | ~0.45          | Underpowered (< 0.80)                   | Recommend replication            |
| Normality (Shapiro-Wilk)| p > 0.05 (assumed) | No evidence of violation            | Proceed with t-test              |
| Equal variance (Levene) | p > 0.05 (assumed) | Homoscedastic                       | Standard or Welch's t-test OK    |

**Confidence**: High (standard inference scenario requiring integrated evaluation)
