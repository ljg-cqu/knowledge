# Essential LLM Prompt Guidelines

**When:** Decision-critical (blocks decision, risk >5%, 0-6mo, ≥2 stakeholders, reversal >40h) + high-quality needed. **Result:** ↓60-75% content, ↓30-60% hallucinations, ↑60-80% quality.

## 8 Guidelines

**1. Context** [↓30-40% hallucinations]: Scale, constraints, timeline, domain. ❌ "Design API" ✅ "REST API: e-commerce <1M products, 10K req/s, Python/FastAPI, 3mo, GDPR"

**2. Precision** [↓40-50% errors]: Quantify. ❌ "Fast/scalable" ✅ "p95 <200ms, 10K→100K req/s, auto-scale <2min"

**3. Sources** [↓50-60% hallucinations]: Require citations. ❌ "Best practices?" ✅ "Cite Netflix/Amazon/CNCF, flag unverified"

**4. Essential Only** [↓40-60% time]: Exclude trivial. ❌ "All caching" ✅ "Django 5K: Redis/Memcached/Django cache for <500ms? Deciding factors only"

**5. Validate** [↓20-30% errors]: Self-review. ❌ Accept output ✅ "Verify claims, flag assumptions, check compatibility"

**6. Trade-offs** [↑60-80% quality]: ≥2 alternatives. ❌ "Use microservices?" ✅ "Microservices vs monolith: costs/benefits/risks"

**7. Balance** [↓40-50% bias]: Counterarguments, when NOT. ❌ "Why K8s?" ✅ "K8s vs Swarm/managed/VMs: pros/cons, when NOT"

**8. Structure** [↑30-40% speed]: TOC, steps, metrics. ❌ Paragraph ✅ "Decision→Steps(0-2wk/2-6wk/6-12wk+owners)→Metrics→Risks"

## Quick Check (30s)

**Before:** ☑ Context ☑ Quantified ☑ Citations ☑ Essential only ☑ Self-review ☑ ≥2 alternatives ☑ Counterarguments ☑ Structure

**Output:** Accurate | Precise | Cited | Complete | Actionable | Consistent | Relevant | Balanced | Recent (2023+)

**Exclude:** `history (unless regulatory), theory (unless >40h reversal), edge cases <5% AND low-impact, proofs, trends without data, generic advice, speculation. Context: [tech stack, scale, timeline, constraints]`
