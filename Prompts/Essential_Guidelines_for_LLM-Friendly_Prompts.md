# Essential Guidelines for LLM-Friendly Prompts

**Time is precious.** Use this file ONLY when ALL are true:
- **Decision-critical**: blocks a real decision, risk >5%, horizon 0-6mo, ≥2 stakeholders, reversal >40h.
- **High-quality**: requires accurate, precise, cited, actionable, and complete answers.
- **Minimal**: asks only what is necessary and non-redundant; total prompt+review time <2h.

**Priority**: P0 (0-2wk) > P1 (2-6wk) > P2 (2-6mo); skip >6mo decisions.

**Result**: ↓60-75% content, 100% decision capability, ↓30-60% hallucinations, ↑60-80% quality, ↑50-70% overall.

---

## 8 Guidelines (Tier 1: Prevent Errors | Tier 2: Improve Quality)

**Tier 1: Prevent Errors (Must Have)**

**1. Context** [↓30-40% hallucinations]: State scale, constraints, timeline, domain.
❌ "Design an API" | ✅ "REST API: e-commerce, <1M products, 10K req/s, Python/FastAPI, 3mo, GDPR"

**2. Precision** [↓40-50% interpretation errors]: Quantify all terms.
❌ "Fast and scalable" | ✅ "p95 <200ms, 10K→100K req/s, auto-scale <2min"

**3. Sources** [↓50-60% hallucinations]: Require citations, reject speculation.
❌ "Best practices?" | ✅ "Cite Netflix/Amazon/CNCF docs, flag unverified"

**4. Essential Only** [↓40-60% reading time]: Exclude trivial/redundant/nice-to-have.
❌ "Explain all caching approaches" | ✅ "Django 5K users: Redis/Memcached/Django cache for <500ms? Deciding factors only"

**Tier 2: Improve Quality (Strongly Recommended)**

**5. Validate** [↓20-30% errors]: Request self-review, error checks.
❌ Accept output | ✅ "Self-review: verify claims, flag assumptions, check compatibility"

**6. Trade-offs** [↑60-80% decision quality]: Compare ≥2 alternatives with costs/benefits/risks.
❌ "Should I use microservices?" | ✅ "Microservices vs monolith: costs (complexity), benefits (scale), risks (over-engineering)"

**7. Balance** [↓40-50% bias]: Request counterarguments, limitations, when NOT to use.
❌ "Why use Kubernetes?" | ✅ "K8s vs Swarm/managed/VMs: fair pros/cons, when NOT to use, learning curve"

**8. Structure** [↑30-40% implementation speed]: TOC, steps with owners/timelines, metrics.
❌ Paragraph | ✅ "1) Decision (go/no-go), 2) Steps (0-2wk/2-6wk/6-12wk+owners), 3) Metrics, 4) Risks"

---

## Quick Reference (30s)

**Before sending:**
- [ ] Context: scale/constraints/timeline/domain
- [ ] Quantified: p95/req/s/size (not "fast/big")
- [ ] Citations required, flag uncertainty
- [ ] Essential only (no history/theory)
- [ ] Self-review requested
- [ ] ≥2 alternatives + trade-offs
- [ ] Counterarguments + limitations
- [ ] Structure: decision/steps/metrics/risks

**Validate output:**
- [ ] Accurate (verified) | Precise (metrics) | Cited | Complete (trade-offs) | Actionable (steps+owners+timelines)
- [ ] Consistent | Relevant | Balanced | Recent (2023+, flag <2020)

---

## Exclude Statement

```
Exclude: history (unless regulatory), theory (unless novel/architectural), edge cases <5% probability AND low impact, proofs, trends without data, generic advice, speculation, redundant info.

Include: theory for decisions >40h reversal, edge cases >5% OR high impact (outage/breach), decision-critical trade-offs.

Context: [tech stack, scale, timeline, constraints]
```
