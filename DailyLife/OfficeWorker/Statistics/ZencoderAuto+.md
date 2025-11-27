# Office Worker Daily Life: Statistical Analysis Q&A

## Overview

**Context**: Statistical reasoning applied to office worker daily routines from morning wake-up through evening sleep, focusing on decision-critical scenarios impacting productivity, health, and organizational efficiency.

**Difficulty Distribution**: 20% F / 40% I / 40% A

**Topics Covered**: Inference, Experimental Design, Modeling, Interpretation

**Domains**: Workplace productivity, commuting optimization, health analytics, organizational behavior

---

## Q&A Pairs

### Q1: Morning Commute Time Analysis

**Scenario**: An office worker tracks commute times over 30 days: mean = 42 min (SD = 12 min) via subway vs. 15 days by car: mean = 38 min (SD = 18 min). They want to determine if car commuting is significantly faster to justify $200/month parking costs. What statistical test should they use and what factors should they consider?

**Difficulty**: F | **Topic**: Inference | **Criticality**: Blocks decision

**Insight**: Sample size imbalance and variance differences require careful test selection; practical vs. statistical significance matters for cost-benefit decisions.

**Answer**:

**Framework**: Two-sample comparison with unequal variances and sample sizes (Welch's t-test).

**Analysis Steps**:
1. **Test Choice**: Welch's t-test appropriate for unequal variances (SD_car = 18 vs. SD_subway = 12) and unequal n (30 vs. 15).
2. **Assumptions**: Check normality (CLT applies with n ≥ 15); independence (daily commutes); measurement consistency (same route/time windows).
3. **Effect Size**: Difference = 4 minutes/day × 20 workdays/month = 80 min/month saved.
4. **Cost-Benefit**: $200/month ÷ 80 min = $2.50/minute—evaluate against personal value of time.
5. **Confounds**: Weather, traffic patterns, seasonal variation, departure time flexibility.

**Trade-offs**: Larger car commute variance (SD = 18) suggests unpredictability; statistical significance may not justify cost if confidence interval is wide.

**Software**: Python (scipy.stats.ttest_ind with equal_var=False), R (t.test), Excel (T.TEST function).

**Recommendation**: Calculate 95% CI for difference; if lower bound < 5 min, cost may not justify switch. Consider collecting more car data (n = 30) for balanced comparison.

**Pitfalls**: Ignoring variance differences; not accounting for time-of-day effects; overlooking hidden costs (stress, parking availability).

**Artifact**:

```
Commute Method Comparison
┌──────────┬─────────┬────────┬──────┐
│ Method   │ Mean(min)│ SD(min)│  n   │
├──────────┼─────────┼────────┼──────┤
│ Subway   │   42    │   12   │  30  │
│ Car      │   38    │   18   │  15  │
├──────────┼─────────┼────────┼──────┤
│ Diff     │    4    │   --   │  --  │
└──────────┴─────────┴────────┴──────┘

Estimated 95% CI: (-4.2, 12.2) minutes
→ Includes 0, suggests no clear advantage
```

**Justification**: Decision impacts monthly budget ($200) and daily schedule; incorrect analysis leads to suboptimal financial/time allocation affecting work-life balance.

---

### Q2: Office Productivity and Meeting Optimization

**Scenario**: A manager observes that teams with >15 hours/week in meetings report 20% lower task completion rates (n = 8 teams) compared to teams with <8 hours/week (n = 12 teams). They want to implement a "meeting cap" policy. What analyses should precede this decision, and what confounds must be addressed?

**Difficulty**: I | **Topic**: Experimental Design | **Criticality**: Affects ≥2 stakeholder roles (Managers, Teams, Executives)

**Insight**: Correlation ≠ causation; meeting intensity may be a symptom, not cause, of low productivity; requires controlling for team characteristics and establishing causal mechanisms.

**Answer**:

**Framework**: Observational study with potential confounders requiring regression adjustment or propensity score methods.

**Domain Context**: Organizational interventions affect team dynamics, morale, and cross-functional collaboration; hasty policies risk disrupting essential coordination.

**Dimensions (Applied/Interpretive)**:

1. **Confounders**: Team size, project complexity, tenure, departmental function (e.g., R&D vs. operations), existing workload.
2. **Reverse Causality**: Struggling teams may hold more meetings to address problems; correlation doesn't indicate direction.
3. **Analysis Approach**:
   - Multiple regression: Control for team characteristics (size, domain, complexity scores).
   - Stratification: Compare similar teams (e.g., same department, size) with different meeting loads.
   - Mediation analysis: Test if meeting time affects outcomes through specific pathways (interruptions, context-switching).
4. **Experimental Option**: Pilot A/B test with randomized meeting caps in 4-6 teams over 2-3 months; measure task completion, quality, and team satisfaction.

**Assumptions**: Task completion rates measured consistently; meeting necessity varies by function; team self-selection into meeting patterns.

**Trade-offs**: Policy simplicity vs. flexibility; short-term productivity vs. long-term collaboration quality; may need department-specific thresholds.

**Software**: R (lm, matchit for propensity scores), Python (statsmodels, scikit-learn), Tableau for dashboard tracking.

**Pitfalls**: Simpson's paradox (aggregated analysis masks subgroup patterns); ignoring meeting quality/relevance; not distinguishing synchronous vs. asynchronous alternatives.

**Recommendation**: Before policy implementation, conduct regression analysis controlling for confounders; pilot test with voluntary teams; measure leading indicators (context switches, focus time) alongside task completion.

**Artifact**:

```
Causal Diagram (DAG)
                Team Complexity
                       ↓
Meeting Hours → Task Completion ← Project Type
       ↑                ↓
   Team Size      Team Morale
   
Confounders to control:
• Team size, department, project complexity
• Existing productivity baseline
• Cross-functional dependencies

Proposed Experimental Design:
├─ Control Group (n=6): Current meeting patterns
└─ Treatment Group (n=6): 10-hour/week cap
   
Duration: 3 months
Metrics: Task completion, quality scores, satisfaction surveys
```

**Justification**: Policy affects multiple teams (Analysts, Engineers, Managers); incorrect intervention wastes organizational resources, harms morale, and may reduce necessary coordination; quantified impact on 20% productivity difference requires validation before scaling.

---

### Q3: Restaurant Lunch Choice Optimization

**Scenario**: An office district has 5 restaurants. A worker collected data over 60 days: Restaurant A (Italian, 15-min walk, $15, n=20 visits), Restaurant B (Cafe, 5-min walk, $12, n=25), Restaurant C (Asian, 10-min walk, $18, n=15). They rated satisfaction (1-10). How should they model optimal choice considering time, cost, and satisfaction trade-offs?

**Difficulty**: I | **Topic**: Modeling | **Criticality**: Requires action (daily decision optimization)

**Insight**: Multi-objective optimization requires weighting personal preferences; historical data reveals revealed preferences but may miss unmeasured factors.

**Answer**:

**Framework**: Multi-attribute utility theory (MAUT) or discrete choice modeling.

**Domain Context**: Daily lunch decisions accumulate to ~250 choices/year; optimization saves time and money while maintaining satisfaction and dietary variety.

**Analysis Approach**:

1. **Descriptive Statistics**: Calculate mean satisfaction, cost, and time by restaurant; identify variance (consistency) in satisfaction ratings.
2. **Revealed Preferences**: Current visit frequency (B: 42%, A: 33%, C: 25%) suggests implicit weighting of factors.
3. **Utility Function**: U = w₁(Satisfaction) - w₂(Cost) - w₃(Time), where weights (w) reflect personal priorities.
4. **Weight Estimation**:
   - Regression: Satisfaction ~ Cost + Time + Restaurant fixed effects
   - Stated preferences: Survey to elicit willingness-to-pay for satisfaction/time
   - Infer weights from past choices using logistic regression (choice ~ satisfaction + cost + time)
5. **Optimization**: Given estimated weights, rank restaurants by expected utility; adjust for variety preferences (avoid monotony).

**Assumptions**: Satisfaction ratings stable over time; no unmeasured factors (social interactions, menu variety); marginal utility of money and time constant.

**Trade-offs**: Model complexity vs. interpretability; historical data reflects past weather/mood but may not predict future; balancing optimization with serendipity/variety.

**Software**: Python (pandas, scikit-learn for regression, scipy.optimize), R (mlogit package for discrete choice), Excel for quick calculations.

**Pitfalls**: Overfitting to historical data; ignoring categorical preferences (dietary restrictions, cravings); not accounting for restaurant closures or menu changes.

**Recommendation**: Estimate utility weights from logistic regression; create decision rule (e.g., "choose highest utility option 70% of time, random selection 30% for variety"); re-calibrate quarterly as preferences shift.

**Artifact**:

| Restaurant | Satisfaction (mean) | Cost ($) | Time (min) | Visits | Utility* |
|------------|---------------------|----------|------------|--------|----------|
| A (Italian)| 8.2                 | 15       | 15         | 20     | 6.0      |
| B (Cafe)   | 7.5                 | 12       | 5          | 25     | 6.8      |
| C (Asian)  | 8.8                 | 18       | 10         | 15     | 6.2      |

*Utility = Satisfaction - 0.2×Cost - 0.1×Time (estimated weights)

**Logistic Regression Output**:
```
Choice ~ Satisfaction (β=0.45, p<0.01) + Cost (β=-0.12, p=0.03) + Time (β=-0.08, p=0.05)
→ Satisfaction most important, followed by cost
```

**Justification**: Daily decision repeated 250+ times/year; suboptimal choices accumulate to $500-1000 and 20-40 hours annually; principled approach improves consistency and satisfaction while accommodating preferences.

---

### Q4: Sleep Patterns and Work Performance Correlation

**Scenario**: HR analytics team collects data from 200 employees using wearables: average sleep duration (hours), sleep quality score (1-100), and next-day performance metrics (task completion %, error rate, self-reported focus 1-10) over 3 months. They find that employees sleeping 7-8 hours have 15% higher performance scores than those sleeping <6 hours (p=0.001). Management wants to promote "sleep hygiene" campaigns. What advanced analyses are needed to establish causality and guide intervention design?

**Difficulty**: A | **Topic**: Inference + Modeling | **Criticality**: Affects ≥2 stakeholder roles (Employees, HR, Executives), Creates risk (incorrect inference, privacy concerns)

**Insight**: Observational data with potential bidirectional causality (poor sleep → low performance vs. high stress → poor sleep + low performance); requires causal inference methods and careful privacy/ethics considerations.

**Answer**:

**Framework**: Causal inference using instrumental variables, difference-in-differences, or regression discontinuity; multilevel modeling for repeated measures.

**Domain Context**: Workplace wellness interventions impact employee health, privacy, and organizational culture; misattribution of causality leads to ineffective programs and wasted investment; wearable data raises privacy/consent issues.

**Dimensions (Interpretive/Applied/Computational)**:

1. **Confounders**: Workload (high stress → poor sleep + low performance), personal factors (childcare, health conditions), job type, age, baseline performance.
2. **Bidirectionality**: Stressed employees may sleep poorly AND perform poorly; correlation doesn't prove sleep is the causal factor.
3. **Advanced Analyses**:
   - **Mixed-effects models**: Account for individual baselines and repeated measures (lmer in R).
   - **Fixed-effects regression**: Remove time-invariant confounders (individual differences).
   - **Granger causality tests**: Assess temporal precedence (does sleep predict next-day performance better than reverse?).
   - **Instrumental variables**: Use exogenous shocks (daylight saving time transitions, unexpected late meetings) as instruments for sleep disruption.
   - **Propensity score matching**: Compare similar employees with different sleep patterns.
4. **Privacy/Ethics**: Ensure anonymization; voluntary participation; avoid penalizing low performers; transparent data use policies.
5. **Intervention Design**: Randomized controlled trial (RCT) with control group; measure multiple outcomes (performance, health, satisfaction, retention); 6-month horizon for habit formation.

**Assumptions**: Wearable data accurate; self-reported focus unbiased; performance metrics capture quality (not just quantity); employees consent to data sharing.

**Trade-offs**: Observational study is cheap but confounded; RCT is rigorous but expensive and requires participation; interventions may have heterogeneous effects across job types.

**Software**: R (lme4, plm for panel data, ivreg for IV), Python (linearmodels, statsmodels for panel/IV), Stata for econometric models.

**Pitfalls**: Selection bias (healthier employees use wearables); measurement error (wearables misclassify sleep stages); ignoring job-specific demands (night shifts, on-call roles); privacy violations damaging trust.

**Recommendation**: 
1. Conduct fixed-effects regression to control for individual baselines.
2. Use Granger causality to test temporal precedence.
3. Pilot RCT with sleep hygiene training (n=50 treatment, n=50 control) measuring performance, sleep, and satisfaction over 6 months.
4. Implement strict privacy protocols (aggregate reporting only, opt-in, no individual tracking).
5. Stratify analysis by job type, workload, and demographics to detect heterogeneous effects.

**Artifact**:

```
Causal Diagram (DAG)
              Workload/Stress
                 ↓        ↓
         Sleep Duration → Performance
                 ↑            ↑
           Personal Factors   Job Type
           (Age, Health)

Panel Regression Results (Fixed Effects):
────────────────────────────────────────
Performance = β₀ + β₁(Sleep) + β₂(Workload) + ε
────────────────────────────────────────
Sleep (hrs)     β=4.2,  p<0.001  ✓
Workload (hrs)  β=-2.8, p<0.001  ✓
Within R²: 0.34
────────────────────────────────────────

Granger Causality Test:
Sleep → Performance: F=12.3, p<0.001  ✓ (causal direction supported)
Performance → Sleep: F=2.1, p=0.14    ✗ (reverse not supported)

Proposed RCT Design:
├─ Treatment (n=50): Sleep hygiene training + flexible start times
└─ Control (n=50): Standard schedule

Duration: 6 months
Metrics: Sleep duration/quality, task completion, error rate, 
         job satisfaction, turnover intention
Stratification: By department, baseline sleep, workload
```

**Justification**: Intervention affects 200+ employees across departments (HR, Management, individual contributors); incorrect causal inference leads to multi-million dollar investment in ineffective wellness programs; privacy violations risk legal/ethical issues and erode trust; quantified 15% performance difference translates to significant organizational productivity; requires rigorous methodology to separate sleep effects from confounders before policy implementation.

---

### Q5: Work-Life Balance Metrics Across Departments

**Scenario**: Executive team analyzes annual survey data (n=500 employees across 5 departments): reported work-life balance scores (1-10), overtime hours/week, remote work days/month, and turnover intention (1-5 scale). Finance department shows lowest balance (mean=4.2) and highest turnover intention (mean=3.8), despite 30% higher compensation. CEO asks: "Should we mandate remote work policies or revise compensation further?" What strategic analysis framework should guide this decision?

**Difficulty**: A | **Topic**: Interpretation + Experimental Design | **Criticality**: Affects ≥2 stakeholder roles (Executives, Managers, HR, Employees), Requires action (6-month policy implementation), Quantified impact (turnover costs)

**Insight**: Compensation doesn't offset poor work-life balance; one-size-fits-all policies may backfire across departments; requires understanding mechanism (workload vs. autonomy vs. culture) before intervention.

**Answer**:

**Framework**: Mixed-methods approach combining quantitative modeling (mediation analysis, structural equation modeling) with qualitative insights (focus groups, exit interviews); pilot testing before organization-wide rollout.

**Domain Context**: Turnover costs 1.5-2× annual salary (recruiting, training, productivity loss); Finance department's specialized skills make retention critical; policy changes affect organizational culture, equity across departments, and operational feasibility (client-facing roles may require on-site presence).

**Strategic Analysis**:

1. **Mechanism Identification**:
   - **Mediation analysis**: Does work-life balance mediate relationship between overtime/remote work and turnover intention?
   - **Structural equation modeling (SEM)**: Test competing models (workload → balance → turnover vs. autonomy → balance → turnover).
   - **Department-specific analysis**: Finance may have unique stressors (end-of-quarter crunches, regulatory deadlines) not shared by other departments.

2. **Qualitative Investigation**:
   - **Focus groups**: Explore what drives low balance in Finance (workload intensity, lack of flexibility, culture of presenteeism, client demands).
   - **Exit interviews**: Analyze turnover reasons (actual vs. stated) from past 2 years.
   - **Benchmark**: Compare Finance work-life balance scores to industry standards (finance sector notoriously demanding).

3. **Policy Options**:
   - **Remote work**: May help work-life balance but risks "always-on" culture if not bounded; consider hybrid model with "core hours."
   - **Workload management**: Address root cause (overtime hours) through staffing increases, process automation, or deadline adjustments.
   - **Compensation vs. time**: Survey revealed preferences: Would Finance employees trade 10% pay for 20% fewer overtime hours?
   - **Department-specific solutions**: Tailor policies (Finance: flexible deadlines; Sales: remote work; Operations: shift flexibility).

4. **Experimental Design**:
   - **Pilot RCT**: Select 2 Finance teams (n=20 each); one receives mandatory remote work 3 days/week + workload review, other continues current model.
   - **Duration**: 6 months to allow habit formation and turnover intention shifts.
   - **Metrics**: Work-life balance scores, overtime hours, turnover intention, productivity (quality of financial reports, audit findings), team cohesion.
   - **Qualitative feedback**: Monthly pulse surveys, manager observations.

5. **Decision Criteria**:
   - If remote work improves balance without productivity loss: Scale to Finance.
   - If workload reduction needed: Hire additional staff or automate (ROI analysis).
   - If compensation isn't key lever: Redirect budget to staffing/process improvements.

**Assumptions**: Survey responses honest (anonymous collection); turnover intention predicts actual turnover (validate with historical data); departments have different needs (avoid one-size-fits-all).

**Trade-offs**: Remote work may improve autonomy but reduce collaboration; hiring increases costs but reduces overtime burnout; department-specific policies create equity concerns but better address needs.

**Software**: R (lavaan for SEM, mediation package), Python (semopy), SPSS for survey analysis, Tableau for dashboard visualization, Qualtrics for pulse surveys.

**Pitfalls**: Assuming compensation solves all problems; implementing remote work without addressing workload (shifts long hours to home); ignoring department differences; not measuring leading indicators (stress, engagement) alongside lagging ones (turnover); confusing correlation (remote work associated with better balance) with causation (flexible workers may self-select).

**Recommendation**:
1. Conduct mediation analysis to identify mechanism (workload vs. flexibility vs. culture).
2. Run Finance focus groups to understand root causes.
3. Pilot test hybrid remote work (3 days/week) + workload audit in 2 Finance teams for 6 months.
4. Track work-life balance, productivity, and turnover intention; compare to control teams.
5. Based on results, scale successful interventions department-specifically.
6. Avoid blanket remote mandates until pilot validates effectiveness and operational feasibility.

**Artifact**:

```
Department Comparison
┌───────────┬──────────┬──────────┬─────────┬──────────┐
│ Department│ Balance  │ Overtime │ Remote  │ Turnover │
│           │ (1-10)   │ (hrs/wk) │ (days/mo│ Intent   │
├───────────┼──────────┼──────────┼─────────┼──────────┤
│ Finance   │  4.2     │   15     │    2    │   3.8    │
│ Engineering│ 6.8     │    8     │   10    │   2.1    │
│ Sales     │  6.2     │   10     │    8    │   2.5    │
│ Operations│  5.9     │   12     │    3    │   2.9    │
│ Marketing │  7.1     │    7     │   12    │   1.9    │
└───────────┴──────────┴──────────┴─────────┴──────────┘

Mediation Model (SEM):
                 Work-Life Balance (β=-0.52, p<0.001)
                          ↓
Overtime Hours → Turnover Intention
(Direct: β=0.18, p=0.04)
(Indirect via Balance: β=0.31, p<0.001)
→ 63% of overtime effect mediated by balance

Pilot RCT Design:
Finance Department (n=40)
├─ Treatment Team A (n=20): 3 days/week remote + workload review
└─ Control Team B (n=20): Current model (on-site, standard hours)

Measures (monthly): Balance, overtime, productivity, cohesion
Duration: 6 months
Success Criteria: 
  • Balance ↑ by 1.5 points
  • Turnover intention ↓ by 1.0 point
  • Productivity maintained (audit quality, report accuracy)
```

**Justification**: Decision impacts 500 employees across 5 departments; Finance turnover costs ~$2-3M annually (100 employees × 20% turnover × $150K replacement cost); incorrect policy wastes resources and may worsen morale; remote work mandate without addressing workload risks burnout at home; department-specific needs require tailored solutions validated through pilots; quantified metrics (4.2 balance score, 3.8 turnover intention) enable measurable intervention goals; strategic impact on organizational culture, retention, and competitive advantage requires rigorous evidence before commitment.

---

## References

### Glossary

**Causal Inference**: Methods to establish cause-effect relationships from observational or experimental data, addressing confounding and selection bias.

**Confounding Variable**: Factor associated with both predictor and outcome, distorting apparent relationship (e.g., workload affects both sleep and performance).

**Effect Size (Cohen's d)**: Standardized measure of difference between groups; d=0.2 (small), 0.5 (medium), 0.8 (large).

**Fixed Effects Model**: Regression controlling for individual-specific time-invariant factors by analyzing within-person variation.

**Granger Causality**: Time-series method testing if past values of X predict Y better than Y's past alone; suggests temporal precedence.

**Instrumental Variable (IV)**: Variable affecting outcome only through predictor, used to address endogeneity (e.g., daylight saving time affects sleep but not directly performance).

**Mediation Analysis**: Examines how predictor affects outcome through intermediate variable (e.g., overtime → work-life balance → turnover).

**Mixed-Effects Model**: Regression with fixed effects (population averages) and random effects (individual/group variation); handles repeated measures.

**Multi-Attribute Utility Theory (MAUT)**: Framework for combining multiple criteria (cost, time, satisfaction) into single utility score using weights.

**Propensity Score Matching**: Method pairing similar units differing only in treatment to approximate randomized experiment.

**Structural Equation Modeling (SEM)**: Framework testing complex causal relationships among multiple variables simultaneously.

**Welch's t-test**: Two-sample t-test not assuming equal variances; robust to heteroscedasticity.

### Tools

**Statistical Software**:
- **R**: Open-source statistical environment; packages: lme4 (mixed models), lavaan (SEM), matchit (propensity scores), pwr (power analysis)
- **Python**: General-purpose language with statistics libraries: scipy.stats, statsmodels, scikit-learn (machine learning), linearmodels (panel/IV)
- **Stata**: Commercial software strong in econometrics, causal inference, panel data
- **SPSS**: User-friendly commercial software for survey analysis, descriptive statistics

**Data Visualization**:
- **Tableau**: Business intelligence platform for interactive dashboards
- **ggplot2 (R)**: Publication-quality graphics with grammar-of-graphics framework
- **matplotlib/seaborn (Python)**: Flexible plotting libraries

**Survey Tools**:
- **Qualtrics**: Enterprise survey platform with advanced logic, integration
- **Google Forms**: Free, simple survey tool for basic needs

**Productivity Tracking**:
- **Wearables**: Fitbit, Apple Watch, Oura Ring for sleep/activity monitoring
- **Time Tracking**: Toggl, RescueTime for work hour analysis

### Textbooks

1. **Introductory Statistics**:
   - *Statistics* by Freedman, Pisani, Purves (conceptual foundation)
   - *OpenIntro Statistics* (free, applied focus)

2. **Applied Regression & Modeling**:
   - *Regression and Other Stories* by Gelman, Hill, Vehtari (modern, causal focus)
   - *An Introduction to Statistical Learning* by James et al. (machine learning accessible)

3. **Causal Inference**:
   - *Causal Inference: The Mixtape* by Cunningham (econometric methods, free online)
   - *The Book of Why* by Pearl & Mackenzie (conceptual introduction to causality)

4. **Experimental Design**:
   - *Design and Analysis of Experiments* by Montgomery (comprehensive, industrial focus)
   - *Field Experiments* by Gerber & Green (social science applications)

5. **Survey Methodology**:
   - *Survey Methodology* by Groves et al. (comprehensive reference)

6. **Organizational Research**:
   - *Organizational Research Methods* journal (current methodologies)

### Citations

- Cohen, J. (1988). *Statistical power analysis for the behavioral sciences* (2nd ed.). Lawrence Erlbaum Associates.

- Cunningham, S. (2021). *Causal inference: The mixtape*. Yale University Press.

- Freedman, D., Pisani, R., & Purves, R. (2007). *Statistics* (4th ed.). W.W. Norton & Company.

- Gelman, A., Hill, J., & Vehtari, A. (2020). *Regression and other stories*. Cambridge University Press.

- Groves, R. M., Fowler, F. J., Couper, M. P., Lepkowski, J. M., Singer, E., & Tourangeau, R. (2009). *Survey methodology* (2nd ed.). John Wiley & Sons.

- Imbens, G. W., & Rubin, D. B. (2015). *Causal inference for statistics, social, and biomedical sciences*. Cambridge University Press.

- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An introduction to statistical learning with applications in R* (2nd ed.). Springer.

- Montgomery, D. C. (2017). *Design and analysis of experiments* (9th ed.). John Wiley & Sons.

- Pearl, J., & Mackenzie, D. (2018). *The book of why: The new science of cause and effect*. Basic Books.

- Rosenbaum, P. R., & Rubin, D. B. (1983). The central role of the propensity score in observational studies for causal effects. *Biometrika*, 70(1), 41-55.

---

## Evaluation

### Practice Questions

1. **Your commute data shows equal means but car has 3× higher variance than subway. What does this imply for decision-making beyond average time saved?**

2. **If implementing a meeting cap policy, what would be an appropriate control group and why might randomization be challenging in organizational settings?**

3. **In the restaurant choice model, how would you incorporate non-linear preferences (e.g., diminishing returns of satisfaction above 8/10)?**

4. **What ethical concerns arise from employer-collected sleep data, and how would you design informed consent procedures?**

5. **Why might Finance department's work-life balance issues require different interventions than Engineering, even if both have similar overtime hours?**

### Checklist for Decision-Critical Analysis

- [ ] **Identify confounders**: List variables affecting both predictor and outcome
- [ ] **Check assumptions**: Normality, independence, equal variance, measurement validity
- [ ] **Establish temporality**: Does predictor precede outcome? (Granger causality, lagged models)
- [ ] **Quantify uncertainty**: Report confidence intervals, effect sizes, not just p-values
- [ ] **Consider practical significance**: Is statistically significant difference meaningful in context?
- [ ] **Address selection bias**: Are compared groups similar? Use matching or adjustment methods
- [ ] **Test robustness**: Sensitivity analysis to assumptions; do results hold with alternative specifications?
- [ ] **Plan intervention**: Pilot test before full implementation; measure leading/lagging indicators
- [ ] **Stakeholder impact**: Who is affected? What are costs/benefits across roles?
- [ ] **Ethical review**: Privacy, consent, equity, unintended consequences

### Assessment Guide

**For Each Q&A Pair, Evaluate**:

1. **Clarity**: Is the scenario realistic and decision-critical?
2. **Framework**: Does answer provide structured approach (not just isolated facts)?
3. **Context**: Are domain-specific considerations addressed (industry norms, constraints)?
4. **Assumptions**: Are key assumptions stated explicitly?
5. **Trade-offs**: Are limitations and alternative approaches discussed?
6. **Software**: Are appropriate tools mentioned with specific packages/functions?
7. **Pitfalls**: Are common errors and misinterpretations highlighted?
8. **Justification**: Is decision-criticality clearly explained with quantified impact?
9. **Artifact**: Does visual/table enhance understanding beyond text?
10. **References**: Are methods and concepts properly cited?

**Overall Assessment**:
- [ ] Difficulty distribution: 20% F / 40% I / 40% A
- [ ] Topics: Inference, Design, Modeling, Interpretation represented
- [ ] Real-world scenarios from diverse contexts (commuting, workplace, health, organizational)
- [ ] Answers: 150-250 words with structure, examples, domain insights
- [ ] Decision-criticality: Blocks decision, creates risk, affects stakeholders, requires action, quantified impact
