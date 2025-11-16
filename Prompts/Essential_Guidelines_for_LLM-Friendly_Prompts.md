# Guidelines for LLM-Friendly Prompts: Essential Only

**Time is precious.** Generate content ONLY if: **≥1 Decision-Critical** (blocks decision, creates >5% risk, 0-6mo timeline, affects ≥2 stakeholders, reversal cost >40h, dependency blocker) + **ALL High-Quality** (accurate, precise w/metrics, cited, actionable w/steps, complete w/assumptions, consistent, relevant) + **ALL Minimal Sufficient** (necessary for decision, context-specific, cost-effective <2h reading, non-redundant, novel).

**Result**: 60-75% less content, 100% decision capability.

**Priority**: P0 (0-2wk: critical path) > P1 (2wk-2mo: planned) > P2 (2-6mo: strategic) | Skip: >6mo/speculative

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

## Quick Reference (30s before sending prompt)

**Before sending prompt, verify:**
- [ ] Context: scale, constraints, timeline, domain
- [ ] Quantified: p95/req/s/size, not "fast/big"
- [ ] Citations required + flag uncertainty
- [ ] Essential only (no history/theory/nice-to-have)
- [ ] Self-review requested
- [ ] ≥2 alternatives with trade-offs
- [ ] Counterarguments + limitations
- [ ] Structure: decision/steps/metrics/risks

---

## Exclude Statement (Copy to prompt)

```
Exclude: historical context (unless regulatory/compliance), foundational theory (unless novel domain or architectural decision), edge cases <5% probability AND low impact in my context, academic proofs, trends without adoption data, generic advice not tailored to [your context: tech stack, scale, timeline, constraints], speculation without citations, redundant info.

Include: theory for architectural decisions (>40h reversal cost), edge cases >5% probability OR high impact (outages/data loss/compliance breach) in my context, decision-critical trade-offs.
```

## Quality Checklist (Validate output)

- [ ] Accurate (verified claims)
- [ ] Precise (metrics: p95/req/s/%, not "fast/large")
- [ ] Credible (cited sources, flagged assumptions)
- [ ] Complete (constraints/limits/trade-offs stated)
- [ ] Actionable (steps with owners/timelines)
- [ ] Consistent (no contradictions)
- [ ] Relevant (context-specific, not generic)
- [ ] Balanced (pros/cons, when NOT to use)
- [ ] Recent (2023+ preferred, <2020 flagged)

---

## Impact

Hallucinations ↓30-60% • Errors ↓20-50% • Reading ↓40-60% • Decision quality ↑60-80% • Speed ↑30-40% • **Overall ↑50-70%**
