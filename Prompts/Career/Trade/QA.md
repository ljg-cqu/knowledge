# Interview Q&A Generator: Trading & Investment (Minimal Viable)

**Purpose**: Generate 6–12 decision-critical scenario-based Q&A pairs testing judgment, risk management, position sizing for Trader/Senior Trader/Portfolio Manager roles (3–15 years experience)

**Scope**: Decision-critical trading across 3–4 MECE domains | Theory 20–40% / Practice 60–80%  
**Output**: 6–12 Q&A (120–200w) | F:I:A = 20:40:40% (±5pp) | EN 50–70%, ZH 20–40%, Other 5–15% | ≥50% sources <3yr  
**Requirements**: Decision Criticality Framework (mandatory) | Authoritative sources | Citations | Limitations | Trade-offs | ≥70% scenario-based with multi-variable constraints | 60% reduction across all dimensions

---

## Quality Standards

**Content**: ≥70% test judgment under uncertainty | ≥80% cite frameworks with sources + limitations | ≥50% acknowledge trade-offs/alternatives/"when NOT" | ≥60% step-by-step reasoning | All have non-obvious, decision-useful, falsifiable insights

**Citations**: ≥70% ≥1 [Ref: ID], ≥30% ≥2 | All resolve | APA 7th + DOI + [lang]

**References** (collect BEFORE): **G#≥6** (Glossary: Sharpe, VaR, Greeks, Alpha, Beta, Drawdown, Kelly, Sortino) | **T#≥3** (Tools: name, pricing, users, integrations, update ≤18mo, URL) | **L#≥4** (Literature: Hull, Taleb, Lo, Chan) | **A#≥6** (Citations)

**Source Tiers**: Academic/Standards > Central Banks/Exchanges > Consultancies > Vendor > Trade > Practitioner | ≥3 types, none >25%, prefer DOIs, all accessible

**Artifacts**: Per domain: ≥1 diagram + ≥1 table

---

## Decision Criticality Framework (NEW - MANDATORY)

**Include if ≥1 criterion satisfied**:
1. **Blocks Decision**: Directly impacts position sizing, risk limits, strategy pivot, or portfolio rebalancing go/no-go
2. **Creates Risk**: Material threat (VaR breach, drawdown spike, correlation breakdown, tail loss >25%)
3. **Affects ≥2 Core Roles**: Multi-stakeholder impact (Trader + Risk Manager, Portfolio Manager + CRO)
4. **Requires Action**: 1–6mo action window (not speculative)
5. **Quantified Impact**: Sharpe change, VaR %, DD %, correlation shift, PnL impact $

**Exclude if**: Niche/legacy strategies (<5% adoption), Orthogonal/nice-to-have, Already covered, Speculative

---

## Trading Domains (MECE - Decision-Critical Only: 3-4)

| Domain | Scope | Decision Criticality | Examples |
|--------|-------|---------------------|----------|
| **Risk Management & Position Sizing** | Risk metrics, sizing, hedging, construction | Blocks decision, Creates risk | VaR breach, Sharpe target, drawdown limits, Kelly sizing, Greeks |
| **Trading Strategy & Execution** | Strategy development, execution, alpha generation | Blocks decision, Affects roles | Momentum vs. mean reversion, execution slippage, alpha capture |
| **Portfolio Management & Optimization** | Allocation, rebalancing, correlation management | Creates risk, Quantified impact | Risk parity, correlation breakdown, diversification failure, rebalancing |
| **Performance & Attribution** (Optional) | PnL analysis, attribution, benchmarking | Affects roles, Requires action | Sharpe/Sortino decomposition, alpha/beta attribution, metrics |

---

## Terminology (Decision-Critical Only)

**Sharpe**: (Return - RiskFree) / StdDev; ≥1 good, ≥2 excellent | **VaR**: Max loss at confidence level | **Greeks**: Delta, Gamma, Vega, Theta | **Drawdown**: Peak-to-trough decline | **Kelly**: f* = (p×b - q) / b | **Sortino**: Penalizes downside only

---

## Difficulty Levels

| Level | % | Variables | Frameworks | Theory:Practice | Minimum |
|-------|---|-----------|------------|-----------------|---------|
| **F** | 20±5 | 1, clear | 1–2 standard | 60:40 | 2-step logic, 1 framework, 1 limitation, 1 citation |
| **I** | 40±5 | 2–3, ambiguous | 2–3, compare | 40:60 | 3-step logic, 2 frameworks, trade-offs, 2 limitations, 2+ citations |
| **A** | 40±5 | Multi, conflicting | 3+, adapt | 20:80 | 4–5 step logic, 3+ frameworks, alternatives, roadmap, 3+ limitations, 3+ citations |

---

## Answer Structure (120–200w, Streamlined)

1. **Context** (~20w): Restate scenario/challenge, decision point
2. **Analysis** (~30w): Root causes [Ref: ID], frameworks, multi-variable assessment
3. **Reasoning** (~40w): Step-by-step logic [Ref: ID], cause-effect, quantified impact
4. **Recommendations** (~40w): Actions, priorities, trade-offs, alternatives [Ref: ID]
5. **Limitations** (~20w): Constraints, "when NOT", risks [Ref: ID]
6. **Key Insight**: Non-obvious, decision-useful, falsifiable, quantified

---

## Examples

### F (20%): Explain + Apply
**Q**: What is the Sharpe Ratio and when should it be used?  
**A** (~150w): Sharpe = (Return - RiskFree) / StdDev [Ref: G1]; measures risk-adjusted returns. ≥1.0 good, ≥2.0 excellent [Ref: L1]. Use for comparing strategies on risk-adjusted basis [Ref: A1]. **Limitations**: Assumes normality—fails with fat tails/skew [Ref: L2]. Penalizes upside volatility equally; use Sortino for asymmetric returns [Ref: G8]. Sensitive to period/frequency [Ref: A2]. Doesn't capture tail risk (use VaR/CVaR) [Ref: G2]. Best for symmetric strategies; misleading for options/crisis alpha.

### I (40%): Diagnose + Apply Multiple
**Q**: Long/short: Sharpe 1.8, max DD -18%, current DD -12% (4mo). VaR breached 3× this quarter. Assess risk.  
**A** (~180w): Sharpe 1.8 strong [Ref: G1], but -12% DD (approaching max) + VaR breaches signal elevated risk [Ref: G2, G6]. Variables: (1) Concentration/crowding [Ref: L3]; (2) Correlation spike (diversification breakdown) [Ref: A5]; (3) Vol regime shift [Ref: L4]. **Approach**: Decompose PnL by sector/factor [Ref: G13, T1]; check exposures vs. limits [Ref: G15]; stress test 2008/2020 [Ref: A7]; calculate CVaR [Ref: L2]. **Decision**: Reduce gross 20-30% if concentration >40% or stress loss >25%. **Limitations**: Attribution lags; models explain 60-80% [Ref: L3]. DD recovery uncertain [Ref: G6]. Metrics backward-looking [Ref: A5].

### A (40%): Synthesize + Justify
**Q**: 60/40 stocks/bonds, Sharpe 0.9, correlation rising 0.2→0.6. CIO wants higher returns without more risk. Respond.  
**A** (~280w): Rising correlation undermines diversification—QE-era breakdown [Ref: L4, A10]. 0.9 Sharpe constrained by dual headwinds: rates hurt bonds, inflation pressures stocks [Ref: A11]. Correlation 0.2→0.6 reduces efficiency [Ref: G14, L1]. **Response**: "60/40 faces structural issues. Propose multi-asset risk parity or alternatives." **Strategy**: (1) Q1: 15% alternatives (commodities, CTAs, market-neutral)—correlation 0.1-0.3 [Ref: L5, A10, A12]; (2) Q2: Risk parity by volatility [Ref: G14]; Black-Litterman with macro views [Ref: L6]; (3) Q3-Q4: Tail hedge via OTM puts (1-2%) [Ref: L2]; options overlay. **Alternative**: Leverage 60/40 to 1.5× if Sharpe target >1.2 [Ref: L5]—increases tail risk. **When NOT**: Crisis/deleveraging (illiquidity) [Ref: L2]; board rejects complexity. **Limitations**: 1-3yr lockups, 2/20 fees [Ref: A12]; risk parity amplifies crisis vol [Ref: L4]; leverage magnifies DD; rebalancing 30-50bps [Ref: A13]. Requires sophisticated infrastructure [Ref: T2].

---

## Balanced Perspectives

**Viewpoints**: Discretionary vs. Systematic | Long vs. Short-term | Momentum vs. Mean Reversion | Risk Parity vs. Market-cap | Single vs. Multi-asset | Active vs. Passive

**Required**: 2+ alternatives [Ref: ID] | "When NOT" | Limitations [Ref: ID] | Counterarguments | Quantified trade-offs

**Insight Quality**: Concrete, non-obvious, decision-useful, falsifiable  
✅ "Tests risk regime diagnosis; distinguishes risk managers from PnL chasers"  
❌ "About trading risk" (vague, obvious)

---

## Process

### 1. Reference Collection (BEFORE Q&A)
Collect G#≥10, T#≥5, L#≥6, A#≥12 | Verify language mix, recency, diversity, accessibility

### 2. Topic Planning
Select 5–6 domains | Allocate 4–6 Q&A each (25–30 total) | F:I:A = 20:40:40 (±5pp)

### 3. Q&A Generation
**Questions**: Scenario-based ("How would you...", "You observe..."), single ask, test judgment ≥70%, specific constraints  
**Answers**: Follow structure | Cite [Ref: ID] | Logic chains | Alternatives + "when NOT"  
**Checkpoint per 5**: Word count, citations, insights, limitations, balance

### 4. Artifacts
Per domain: ≥1 diagram + ≥1 table (markdown/ASCII)

### 5. References
**G#**: Term, definition, use  
**T#**: Name, pricing, users, integrations, update, URL  
**L#**: Author, year, title, topics  
**A#**: APA 7th + DOI + [lang]

### 6. Validation
Run checklist. **ALL PASS required. FAIL → fix → re-validate**

---

## Validation Checklist (12 Streamlined Checks)

| # | Check | Criteria | Purpose |
|---|-------|----------|---------|
| 1 | Ref counts | G≥6, T≥3, L≥4, A≥6 | Sufficiency |
| 2 | Q&A counts | 6–12, F:I:A 20:40:40 (±5pp) | Scope |
| 3 | Decision Criticality | 100% satisfy ≥1 criterion | Mandatory |
| 4 | Citations | ≥70% ≥1, ≥30% ≥2 | Evidence |
| 5 | Language | EN 50–70%, ZH 20–40%, Other 5–15% | Diversity |
| 6 | Recency | ≥50% <3yr (≥70% quant) | Currency |
| 7 | Links | All functional, prefer DOIs | Verifiability |
| 8 | Word count | Sample 5: all 120–200w | Consistency |
| 9 | Insights | All concrete, non-obvious, decision-useful | Value |
| 10 | Frameworks | ≥80% correct + cited + limitations | Accuracy |
| 11 | Artifacts | Each domain: ≥1 diagram + ≥1 table | Visual support |
| 12 | Overall | All checks PASS, Decision Criticality justified | Final review |

**Final**: ✅ ALL PASS → deliver | ❌ List failures → fix → re-validate

---

## Verification

**Cross-check**: Verify against ≥2 authoritative sources  
**Uncertainty**: Flag with qualifiers; cite confidence  
**Conflicts**: Present both with citations  
**Outdated**: Note if superseded

**Authoritative** (≥1): Peer-reviewed | 10+ years senior | Originator | Data-backed | Industry standard

---

## Pitfalls

**Questions**: ❌ Too broad → ✅ Specific scenario | ❌ Recall → ✅ Judgment | ❌ No constraints → ✅ Multi-variable | ❌ Entry-level → ✅ Senior

**Answers**: ❌ No citations → ✅ Cited | ❌ Vague → ✅ Actionable ("Reduce 30%, hedge 20-delta puts") | ❌ No limitations → ✅ "When NOT" + risks | ❌ Single → ✅ 2+ alternatives | ❌ Theory-heavy → ✅ 60–80% practice | ❌ Obvious → ✅ Non-obvious, falsifiable

---

## Output Structure (Minimal Viable)

```markdown
# Interview Q&A - Trading Professional (Minimal Viable)

## Contents
[TOC: Overview | 3-4 Domains | References (Glossary, Tools, Literature, Citations) | Validation]

## Topic Overview
| Domain | Range | Count | F/I/A | Decision Criticality |
[Distribution table with criticality column]

## Domain 1: [Name]
### Q#: [Scenario]
**Difficulty**: [F/I/A] | **Domain**: [Name] | **Decision Criticality**: [Blocks/Risk/Roles/Action/Quantified]
**Key Insight**: [Non-obvious, decision-useful, falsifiable, quantified]

**Answer** (120–200w):
**Context**: [Challenge, decision point]
**Analysis**: [Root causes, frameworks] [Ref: ID]
**Reasoning**: [Steps, quantified impact] [Ref: ID]
**Recommendations**: [Actions, trade-offs, alternatives] [Ref: ID]
**Limitations**: [Constraints, when NOT, risks] [Ref: ID]

**Artifact**:
[Diagram/table]

[Repeat for 6-12 Q&As across 3-4 domains]

## Reference Sections
### Glossary (≥6)
**G#. Term**: Definition. **Use**: Context.

### Tools (≥3)
**T#. Name**: Desc. **Pricing**: $X. **Users**: Nm+. **Integrations**: [List]. **Update**: Q# YYYY. **URL**: [link]

### Literature (≥4)
**L#.** Author (Year). *Title*. Publisher. [Topics]

### Citations (≥6)
**A#.** Full APA 7th. DOI. [EN/ZH/Other]

## Validation Report
[12-row table: # | Check | Criteria | Status | Notes]
**Final**: ✅ ALL PASS or ❌ [failures]
```

---

## Complete Example (Decision-Critical)

**Q**: How manage position when VaR breached 3 days running, volatility +40%, correlation to SPX rising 0.3→0.7?

**Difficulty**: A | **Domain**: Risk Management & Position Sizing | **Decision Criticality**: Blocks decision (risk limits), Creates risk (tail loss)
**Key Insight**: Tests crisis risk response; distinguishes systematic risk managers from reactive traders. Quantified: VaR breach protocol, correlation impact on diversification, 3-phase mitigation timeline.

**Answer** (285w):  
**Context**: VaR 3× breach + vol +40% + correlation 0.3→0.7 signals regime shift—diversification breakdown, elevated tail risk [Ref: G2, G6, A5].

**Analysis**: Root causes [Ref: L4]: (1) Vol regime change (low→high); VaR calibrated on past [Ref: G2]; (2) Correlation spike (crisis contagion) undermines diversification [Ref: A10]; (3) Concentration/crowding [Ref: L3]. Decompose: check factor exposures [Ref: G13, G15], Greeks [Ref: G3], stress scenarios [Ref: A7].

**Reasoning**: VaR assumes normality—fails in fat tails [Ref: L2, A2]. 3× breach = model failure or structural change. Rising SPX correlation = systematic risk dominates [Ref: G5, L1]. Vol +40% increases tail exponentially (gamma/convexity) [Ref: G3, L2]. Must recalibrate [Ref: T2] and reduce exposure immediately [Ref: A7].

**Recommendations**: 3-phase protocol [Ref: L4, A11]: (1) Day 1: Cut gross 30% (liquidate lowest-conviction, most-correlated) [Ref: L3]; hedge systematic (SPX puts, VIX calls) [Ref: G3, L2]; (2) Day 2-3: Recalibrate VaR with 60d data + stress (2008, 2020) [Ref: T2, A7]; calculate CVaR [Ref: L2]; (3) Week 1-2: Rebalance to target (factor concentration <40%) [Ref: G15]; improve diversification [Ref: L5].

**Implementation**: Emergency committee daily 1-wk, then weekly [Ref: A11]. Real-time Greeks monitoring [Ref: T1]. CRO approval for deviations. Expect PnL hit -5-10% from deleveraging/hedging.

**Metrics**: VaR compliance >95%, CVaR <15%, correlation <0.5, max DD <20%, factor concentration <40%.

**When NOT**: If vol spike is transient event-driven (single stock, no contagion) vs. regime shift [Ref: L4]; selling into panic creates worse losses.

**Limitations**: VaR recalibration has estimation error [Ref: A2]; hedges costly (vol premium 20-30%) [Ref: L2]; deleveraging locks losses; correlation may persist 3-6mo [Ref: A10]. Data lags; execution slippage in volatile markets [Ref: T1]. CVaR needs tail data [Ref: L2]. Crisis requires judgment beyond models [Ref: L4, A11].

**Artifact**:
```
Risk Breach Response Dashboard

Breach: VaR 3 days | Vol +40% | Correlation 0.3→0.7
Metrics:
  Current: VaR $1.2M (95%, 1d) | CVaR $2.1M | Max DD -18% | Sharpe 0.6
  Target:  VaR $0.8M | CVaR $1.4M | Max DD <20% | Sharpe >1.0

┌──────────────────┬────────┬─────────┬───────────┬────────────────┐
│ Action           │ Impact │ Timeline│ Cost      │ Risk Reduction │
├──────────────────┼────────┼─────────┼───────────┼────────────────┤
│Cut Exposure 30%  │ -$300K │ Day 1   │ 1-2% PnL  │ VaR -25%       │
│SPX Puts (5% OTM) │ -$50K  │ Day 1   │ 0.5% PnL  │ Tail -30%      │
│Recalibrate VaR   │ Model  │ Day 2-3 │ 0.1% PnL  │ Accuracy +15%  │
│Factor Rebalance  │ -$200K │ Week 1-2│ 0.8% PnL  │ Correlation -20%│
└──────────────────┴────────┴─────────┴───────────┴────────────────┘

Factor Exposure:
  Momentum: 45% → 35% (reduce $200K)
  Value:    25% → 30% (increase $50K)
  Quality:  20% → Maintain
  Size:     10% → Maintain

Stress Test (Post-mitigation):
  2008 Crisis: -22% (within limit)
  2020 COVID:  -18% (within limit)
  Vol Spike:   -15% (acceptable)

Decision: Execute deleverage + hedge. Cost: -5-8% PnL.
Expected: VaR compliance restored, correlation <0.5, Sharpe recovery 3-6mo.
```
