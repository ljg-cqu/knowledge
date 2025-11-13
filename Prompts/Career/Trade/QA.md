# Interview Q&A Generator: Trading & Investment

**Purpose**: Generate 25–30 scenario-based Q&A pairs testing judgment, decision-making, risk management for Trader/Senior Trader/Portfolio Manager roles (3–15 years experience)

**Scope**: Multi-asset trading across 6 MECE domains | Theory 20–40% / Practice 60–80%  
**Output**: 25–30 Q&A (150–300w) | F:I:A = 20:40:40% (±5pp) | EN 50–70%, ZH 20–40%, Other 5–15% | ≥50% sources <3yr  
**Requirements**: Authoritative sources | Citations | Limitations | Trade-offs | ≥70% scenario-based with multi-variable constraints

---

## Quality Standards

**Content**: ≥70% test judgment under uncertainty | ≥80% cite frameworks with sources + limitations | ≥50% acknowledge trade-offs/alternatives/"when NOT" | ≥60% step-by-step reasoning | All have non-obvious, decision-useful, falsifiable insights

**Citations**: ≥70% ≥1 [Ref: ID], ≥30% ≥2 | All resolve | APA 7th + DOI + [lang]

**References** (collect BEFORE): **G#≥10** (Glossary: Sharpe, VaR, Greeks, Alpha, Beta, Drawdown, Kelly, Sortino, Vol Skew, Carry, Momentum, Mean Reversion, PnL Attribution, Portfolio Optimization, Factor Models) | **T#≥5** (Tools: name, pricing, users, integrations, update ≤18mo, URL) | **L#≥6** (Literature: Hull, Taleb, Lo, Chan, Jansen, López de Prado) | **A#≥12** (Citations)

**Source Tiers**: Academic/Standards > Central Banks/Exchanges > Consultancies > Vendor > Trade > Practitioner | ≥3 types, none >25%, prefer DOIs, all accessible

**Artifacts**: Per domain: ≥1 diagram + ≥1 table

---

## Trading Domains (MECE)

| Domain | Scope | Examples |
|--------|-------|----------|
| **Market Analysis & Instruments** | Asset classes, market structure, instruments, analysis | Equities, FX, commodities, derivatives, order types, microstructure |
| **Trading Strategy & Execution** | Strategy development, backtesting, execution, alpha | Momentum, mean reversion, arbitrage, algorithms, slippage |
| **Risk Management & Position Sizing** | Risk metrics, sizing, hedging, construction | VaR, Sharpe, drawdown, Kelly, diversification, Greeks |
| **Portfolio Management & Optimization** | Theory, allocation, rebalancing, factors | MPT, Black-Litterman, risk parity, multi-asset, factors |
| **Trading Operations & Technology** | Infrastructure, data, automation, regulations | OMS, data feeds, latency, compliance, reporting |
| **Performance & Attribution** | PnL analysis, attribution, benchmarking | Sharpe/Sortino, alpha/beta decomposition, metrics |

---

## Terminology

**Sharpe**: (Return - RiskFree) / StdDev; ≥1 good, ≥2 excellent | **VaR**: Max loss at confidence level | **Greeks**: Delta, Gamma, Vega, Theta, Rho | **Alpha**: Excess vs. benchmark | **Beta**: Market correlation | **Drawdown**: Peak-to-trough decline | **Kelly**: f* = (p×b - q) / b | **Sortino**: Penalizes downside only | **Vol Skew**: Implied vol smile | **Carry**: Holding return minus funding | **Momentum**: Trend-following | **Mean Reversion**: Contrarian | **PnL Attribution**: Decompose by source | **Portfolio Optimization**: Mean-variance, risk parity | **Factor Models**: Fama-French, momentum, value, quality

---

## Difficulty Levels

| Level | % | Variables | Frameworks | Theory:Practice | Minimum |
|-------|---|-----------|------------|-----------------|---------|
| **F** | 20±5 | 1, clear | 1–2 standard | 60:40 | 2-step logic, 1 framework, 1 limitation, 1 citation |
| **I** | 40±5 | 2–3, ambiguous | 2–3, compare | 40:60 | 3-step logic, 2 frameworks, trade-offs, 2 limitations, 2+ citations |
| **A** | 40±5 | Multi, conflicting | 3+, adapt | 20:80 | 4–5 step logic, 3+ frameworks, alternatives, roadmap, 3+ limitations, 3+ citations |

---

## Answer Structure

1. **Context** (1–2 sent): Restate scenario/challenge
2. **Analysis** (2–3 sent): Root causes [Ref: ID]; assumptions
3. **Reasoning** (3–4 sent): Step-by-step logic [Ref: ID]; cause-effect
4. **Recommendations** (3–4 sent): Actions, priorities, trade-offs [Ref: ID]
5. **Implementation** (I/A, 2–3 sent): Sequence, timelines, resources
6. **Metrics** (I/A, 1–2 sent): Success measures, outcomes, timeframes
7. **Limitations** (2–3 sent): Constraints, "when NOT", risks [Ref: ID]
8. **Key Insight**: Non-obvious, decision-useful, falsifiable

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

## Validation Checklist

| # | Check | Criteria | Purpose |
|---|-------|----------|---------|
| 1 | Ref counts | G≥10, T≥5, L≥6, A≥12 | Sufficiency |
| 2 | Q&A counts | 25–30, F:I:A 20:40:40 (±5pp) | Scope |
| 3 | Citations | ≥70% ≥1, ≥30% ≥2 | Evidence |
| 4 | Language | EN 50–70%, ZH 20–40%, Other 5–15% | Diversity |
| 5 | Recency | ≥50% <3yr (≥70% quant) | Currency |
| 6 | Diversity | ≥3 types, none >25% | Bias prevention |
| 7 | Links | All functional, prefer DOIs | Verifiability |
| 8 | Cross-refs | All [Ref: ID] resolve | No broken cites |
| 9 | Word count | Sample 5: all 150–300 | Consistency |
| 10 | Insights | All concrete, non-obvious, decision-useful | Value |
| 11 | Per-domain | Each: ≥2 auth + ≥1 tool | Balance |
| 12 | Frameworks | ≥80% correct + cited + limitations | Accuracy |
| 13 | Judgment | ≥70% scenario-based | Decision-making |
| 14 | Accuracy | Sample 5: cross-validate | Error detection |
| 15 | Balance | ≥50% trade-offs/limitations/alternatives | Honesty |
| 16 | Reasoning | ≥60% step-by-step | Clarity |
| 17 | Artifacts | Each domain: ≥1 diagram + ≥1 table | Visual support |
| 18 | TOC | Present with working links | Navigation |

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

## Output Structure

```markdown
# Interview Q&A - Trading Professional

## Contents
[TOC: Overview | 6 Domains | References (Glossary, Tools, Literature, Citations) | Validation]

## Topic Overview
| Domain | Range | Count | F/I/A |
[Distribution table]

## Domain 1: [Name]
### Q#: [Scenario]
**Difficulty**: [F/I/A] | **Domain**: [Name]  
**Key Insight**: [Non-obvious, decision-useful, falsifiable]

**Answer** (150–300w):  
**Context**: [Challenge]  
**Analysis**: [Root causes] [Ref: ID]  
**Reasoning**: [Steps] [Ref: ID]  
**Recommendations**: [Actions] [Ref: ID]  
**Implementation** (I/A): [Plan]  
**Metrics** (I/A): [Targets]  
**Limitations**: [Constraints, when NOT, risks] [Ref: ID]

**Artifact**:
[Diagram/table]

[Repeat for all domains]

## Reference Sections
### Glossary (≥10)
**G#. Term**: Definition. **Use**: Context.

### Tools (≥5)
**T#. Name**: Desc. **Pricing**: $X. **Users**: Nm+. **Integrations**: [List]. **Update**: Q# YYYY. **URL**: [link]

### Literature (≥6)
**L#.** Author (Year). *Title*. Publisher. [Topics]

### Citations (≥12)
**A#.** Full APA 7th. DOI. [EN/ZH/Other]

## Validation Report
[18-row table: # | Check | Criteria | Status | Notes]  
**Final**: ✅ ALL PASS or ❌ [failures]
```

---

## Complete Example

**Q**: How manage position when VaR breached 3 days running, volatility +40%, correlation to SPX rising 0.3→0.7?

**Difficulty**: A | **Domain**: Risk Management, Portfolio Management  
**Key Insight**: Tests crisis risk response; distinguishes systematic risk managers from reactive traders.

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
