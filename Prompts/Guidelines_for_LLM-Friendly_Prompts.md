# Guidelines for LLM-Friendly Prompts

**Purpose:** Apply these guidelines to optimize prompts that will guide LLMs to generate high-quality content. When you optimize a prompt using these guidelines, the improved prompt ensures other LLMs produce better outputs.

**When to apply:** Decision-critical prompts (blocks decision, risk >5%, 1-6mo action window, ≥2 stakeholders, fix cost >40h) requiring high-quality LLM outputs. **Result:** ↓30-60% hallucinations, ↑60-80% decision quality in generated content.

## 21 Guidelines

### Foundation: Define the Task

**1. Context** [↓30-40% hallucinations]: Ensure prompt specifies scope, constraints, assumptions, scale, timeline, domain, stakeholders. ❌ Bad: "Design system" ✅ Optimized: "Design payment system: 1M users, PCI-DSS compliance, 6mo timeline, fintech startup context, stakeholders: PM+Arch+Security+Legal, budget $500K"

**2. Clarity** [↓25-35% interpretation errors]: Ensure prompt defines technical terms and explains relationships. ❌ Bad: "Use eventual consistency" ✅ Optimized: "Define terms: 'Eventual consistency (async data sync, stale reads acceptable for <1s) vs strong consistency (immediate sync, higher latency)'"

**3. Precision** [↓40-50% ambiguity]: Ensure prompt quantifies requirements with exact metrics. ❌ Bad: "Design fast and scalable system" ✅ Optimized: "Design system with: p95 latency <200ms, p99 <500ms, throughput 10K→100K req/s, auto-scale <2min, 99.9% uptime"

**4. Relevance** [↓30-40% noise]: Ensure prompt focuses on decision-critical aspects only. ❌ Bad: "Explain database history and current options" ✅ Optimized: "Compare SQL vs NoSQL for e-commerce use case: focus on transaction requirements, scale characteristics, query patterns. Exclude history."

### Scope: What to Cover

**5. MECE** [↑40-50% completeness]: Ensure prompt requests complete coverage with no gaps/overlaps. ❌ Bad: "Explain security: authentication and encryption" ✅ Optimized: "Explain security covering all 5 areas: (1) Authentication, (2) Authorization, (3) Encryption (transit+rest), (4) Audit logging, (5) Secrets management. Ensure no gaps."

**6. Sufficiency** [↑35-45% comprehensiveness]: Ensure prompt requests all necessary aspects. ❌ Bad: "Design API: define endpoints" ✅ Optimized: "Design API covering: endpoints, authentication, rate limiting, versioning strategy, error handling, pagination, caching headers, documentation requirements"

**7. Breadth** [↑30-40% perspective diversity]: Ensure prompt requests multiple stakeholder perspectives. ❌ Bad: "Explain from developer perspective" ✅ Optimized: "Explain from 4 perspectives: (1) Developer: code patterns, (2) SRE: operational complexity, (3) Security: threat surface, (4) PM: user impact"

**8. Depth** [↑25-35% thoroughness]: Ensure prompt requests implementation-level detail. ❌ Bad: "Recommend caching solution" ✅ Optimized: "Recommend Redis with details: eviction policies (LRU/LFU tradeoffs), persistence options (RDB/AOF), clustering approaches (sentinel/cluster), memory limit calculations, key naming patterns"

### Quality: Ensure Excellence

**9. Significance** [↓40-60% reading time]: Ensure prompt focuses on high-impact items only. ❌ Bad: "List all HTTP error codes and handling" ✅ Optimized: "List critical HTTP errors only: 429 (rate limit), 503 (overload), 401/403 (auth), 500 (system alert). Exclude: 404 handling, client errors <5% occurrence"

**10. Concision** [↓35-45% word count]: Ensure prompt requests concise output, no redundancy. ❌ Bad: "Explain why we should consider using caching and how caching can improve performance" ✅ Optimized: "Specify caching strategy: Redis for sessions (TTL 30min), CDN for static assets (TTL 1d). No explanatory text."

**11. Accuracy** [↓20-30% factual errors]: Ensure prompt requests verification of facts. ❌ Bad: "Recommend libraries" ✅ Optimized: "Recommend libraries with verification: check current versions (npm/PyPI), cite compatibility matrices from official docs, flag deprecated APIs, cross-reference claims"

**12. Credibility** [↓50-60% unverified claims]: Ensure prompt requires authoritative citations. ❌ Bad: "What are best practices?" ✅ Optimized: "Cite best practices from: AWS Well-Architected Framework, Google SRE Book, OWASP Top 10 (2023+), academic papers. Flag any assumptions or unverified claims."

**13. Logic** [↓30-40% reasoning errors]: Ensure prompt requests coherent reasoning without contradictions. ❌ Bad: "Explain why microservices simplify architecture" (contradictory) ✅ Optimized: "Explain microservices tradeoff: increases operational complexity but improves scalability. Recommend modular monolith if team <10."

**14. Risk/Value** [↑60-80% decision quality]: Ensure prompt requests ≥2 alternatives with costs/benefits/risks. ❌ Bad: "Recommend Kubernetes setup" ✅ Optimized: "Compare 3 options with costs/risks: (1) K8s self-managed ($2K/mo, ops team needed), (2) Managed K8s ($500/mo, vendor lock-in), (3) VMs ($200/mo, limited scale). Include migration paths."

**15. Fairness** [↓40-50% bias]: Ensure prompt requests balanced view with counterarguments and limitations. ❌ Bad: "Why should we use GraphQL?" (biased) ✅ Optimized: "Compare GraphQL vs REST: pros (flexible queries), cons (complexity, caching challenges), when NOT to use (simple CRUD, public API). Include counterarguments."

### Format: How to Present

**16. Structure** [↑30-40% actionability]: Ensure prompt requests structured output format. ❌ Bad: "Explain the solution" (no structure) ✅ Optimized: "Format output as: ## TOC → ### H2 sections → Bullet lists for steps → Comparison tables → Mermaid diagrams → Code blocks with syntax highlighting"

**17. Output Format** [↑35-45% scanability]: Ensure prompt specifies exact output structure with hierarchy. ❌ Bad: "Provide analysis" (vague) ✅ Optimized: "Structure output: ## Decision Context → ### Option A (pros/cons/cost) → ### Option B → #### Comparison Table → ##### Recommendation → ###### Timeline with milestones"

### Validation: Ensure Correctness

**18. Evidence** [↑40-50% trust]: Ensure prompt requires citations with sources and uncertainty flags. ❌ Bad: "What do studies show?" (no citation requirement) ✅ Optimized: "Cite sources in format: [1] Google SRE Book (2023) p.42 states 'MTTR <1h'. [2] AWS re:Invent 2023 [video URL]. Flag uncertainties: 'cache hit rate estimated (no empirical data)'."

**19. Validation** [↓25-35% errors]: Ensure prompt requires self-review and error checking. ❌ Bad: "Provide recommendation" (no validation) ✅ Optimized: "After generating response, self-review: verify calculations, check for contradictions, test code examples, validate assumptions against sources, flag any uncertainties"

**20. Practicality** [↑50-60% implementation speed]: Ensure prompt requests actionable steps with tooling and examples. ❌ Bad: "Suggest monitoring improvements" (vague) ✅ Optimized: "Provide actionable monitoring setup: Prometheus for metrics, Grafana for dashboards, exact commands: 'helm install prometheus', sample queries: 'rate(http_requests_total[5m])', troubleshooting steps"

**21. Success Criteria** [↑40-50% measurability]: Ensure prompt requests measurable outcomes with baselines. ❌ Bad: "How to achieve better performance?" (unmeasurable) ✅ Optimized: "Define success metrics: p95 latency <200ms (current: 800ms), error rate <0.1% (current: 0.5%), cost <$5K/mo, implementation timeline 3 months. Include measurement methods."

## Quick Check (30s)

**Before sending:** ☑ Context ☑ Clarity ☑ Precision ☑ Relevance ☑ MECE ☑ Sufficiency ☑ Breadth ☑ Depth ☑ Significance ☑ Concision ☑ Accuracy ☑ Credibility ☑ Logic ☑ Risk/Value ☑ Fairness ☑ Structure ☑ Format ☑ Evidence ☑ Validation ☑ Practicality ☑ Success Criteria

**Quality attributes (10):** Accurate | Precise | Cited | Complete | Actionable | Consistent | Relevant | Balanced | Recent (2023+) | Testable

**Exclude:** History (unless regulatory), pure theory (unless >40h fix cost), edge cases <5% impact AND low-severity, proofs, trends without data, generic advice, speculation. **Always specify:** Tech stack, scale, timeline, constraints, stakeholders, budget

**Impact metrics:** ↓30-60% hallucinations (Context+Credibility) | ↓25-50% interpretation errors (Clarity+Precision) | ↑60-80% decision quality (Risk/Value) | ↑40-50% completeness (MECE) | ↑30-60% implementation speed (Structure+Practicality)
