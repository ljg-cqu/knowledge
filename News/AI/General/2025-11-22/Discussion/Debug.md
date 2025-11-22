# Discussion - Debug Cards

1. Q: Our CFO is modeling 12-month runway with CAC increasing 10-15% due to AI startup competition. The market report says AI startups captured 52.5% of VC funding with competitors outspending on acquisition. What's wrong with this assumption?
   A: **Finance Lead:** Wait, where's the 10-15% coming from?
   
   **Analyst:** The report explicitly states CAC may increase 20-40%, not 10-15%.
   
   **CFO:** So we're underestimating by half?
   
   **Analyst:** Exactly. That could miscalculate runway by 2 to 4 months. Could trigger emergency fundraising or layoffs.
   
   **Finance Lead:** Right. How do we fix this?
   
   **Analyst:** Model three scenarios—20%, 30%, 40% CAC increase. Include sensitivity analysis showing cash exhaustion dates at each level. For Formation-stage startups with under 12 months runway, use 40% for conservative planning.
   
   **Finance Lead:** Makes sense. Conservative is safer here.

1. Q: Our engineering team planned a staged rollout for critical RCE patches: dev on Day 1, staging Day 5, low-priority prod Day 12, high-priority prod Day 20. What's wrong with this timeline?
   A: **Security Lead:** Wait, 20 days total? The report recommends patching within 2 weeks—that's 14 days.
   
   **Engineer:** We wanted thorough testing between stages.
   
   **Security Lead:** I get that. But critical RCE vulnerabilities expose production to immediate compromise. Extending to 20 days increases exploitation window by 43%.
   
   **CTO:** And high-priority production gets patched last?
   
   **Security Lead:** Exactly. That's the highest-risk approach. Potential data exfiltration, service disruption, regulatory penalties.
   
   **Engineer:** Got it. How should we compress this?
   
   **Security Lead:** Hmm... [pause] Dev Day 1, staging Day 3-4, low-priority prod Day 7-8, high-priority prod Day 12-14. 24-hour monitoring between stages. For mission-critical systems, consider temporary workarounds—network segmentation, WAF rules—immediately while testing patches in parallel.
   
   **CTO:** Right. Aggressive but necessary.

1. Q: Our product team read GPT-5.1 "significantly outperforms" GPT-4 in reasoning, so they're migrating all features immediately. They allocated 1 sprint for full migration, plan to deploy to production without A/B testing. What's wrong here?
   A: **PM:** One sprint, no testing? That seems fast.
   
   **Engineer A:** Right. The report recommends 2 sprints for evaluation plus testing, not immediate full migration. They skipped benchmarking entirely.
   
   **PM:** Mm-hmm. And no A/B testing?
   
   **Engineer B:** Exactly. Report explicitly recommends monitoring customer NPS and satisfaction scores bi-weekly during migration with success metric of no more than 5% NPS degradation.
   
   **CTO:** What about cost?
   
   **Engineer A:** Good question. GPT-5.1 is 20-30% more expensive. Migrating all features means potentially 20-30% increase in inference costs. They didn't evaluate cost-performance trade-offs.
   
   **CTO:** Ouch. That's significant.
   
   **PM:** So what's the right approach?
   
   **Engineer B:** Let me think... [pause] Define top 3 reasoning-critical use cases, allocate 2 sprints for parallel benchmarks with 20-30 test cases from production data. Migrate highest-value use case first with A/B testing, monitor NPS bi-weekly, stage additional migrations only if success criteria are met.
   
   **PM:** Makes sense. Staged and measured.

1. Q: Marketing wants to reposition our product as "autonomous AI agents" despite having only basic workflow automation and API integrations. They claim this aligns with 78% enterprise adoption. What's problematic?
   A: **Product Lead:** Wait, do we actually have autonomous capabilities?
   
   **Engineer:** Basic workflow automation, yes. Autonomous task execution? No.
   
   **Product Lead:** Right. The report defines agentic AI as "autonomous task execution, tool use, workflow orchestration" and recommends messaging pivot "if product already has 2+ agentic capabilities."
   
   **Marketing Lead:** We have workflow automation and integrations.
   
   **Product Lead:** True, but not autonomy. Report recommends "Product-First Approach" for products where "features non-existent"—build features before repositioning.
   
   **Counsel:** What's the risk here?
   
   **Product Lead:** Creates customer expectations mismatch. Reputation damage when buyers discover limited autonomy. Plus potential false advertising concerns.
   
   **Counsel:** Ah, I see. Legal exposure.
   
   **Engineer:** What should we do instead?
   
   **Product Lead:** Hmm... [pause] Follow the report's Gradual Messaging Evolution. A/B test agentic messaging in new campaigns while maintaining legacy positioning, or invest 3-6 months building genuine agentic capabilities. Alternatively, use "Human-in-Loop Agent" framing to accurately describe supervised automation without overpromising.
   
   **Marketing Lead:** Got it. Honest positioning first.

1. Q: Our CTO read the EU Digital Omnibus may delay high-risk AI system rules by 16 months and immediately canceled all AI Act compliance work for 2026. We operate healthcare AI tools in the EU. What's wrong with this decision?
   A: **Regulatory Lead:** Healthcare AI is high-risk under AI Act Annex III, right?
   
   **Counsel:** Correct. And the report explicitly recommends "Maintain Original Timeline" for high-risk exposure, specifically for regulated industries including healthcare.
   
   **CTO:** But the delay gives us 16 extra months.
   
   **Regulatory Lead:** "May delay"—not guaranteed. Canceling compliance creates massive debt if delay doesn't materialize.
   
   **Counsel:** Exactly. Plus healthcare has GDPR and sector-specific regulations that apply regardless of AI Act timeline.
   
   **Product Lead:** What's the recommended approach?
   
   **Regulatory Lead:** Continue August 2026 compliance prep despite potential delay. Rationale from report: "Readiness regardless of final timeline, competitive advantage if standards tighten." For healthcare, maintain foundational work—model documentation, data lineage, explainability—that applies regardless of final timeline.
   
   **CTO:** Got it. Staying prepared.

1. Q: Our CFO allocated exactly $68K per month for AI infrastructure in 2026 based on the report's projection from $50K. Current spend could increase to $68K with 36% growth. They present this as "data-driven" budgeting. What's insufficient?
   A: **Finance Lead:** Hmm... That's a single-point estimate based on industry average.
   
   **Analyst:** Right. Report recommends "Hybrid Model: Reforecast +20%, initiate optimization workstream" or modeling three scenarios—plus 20%, plus 30%, plus 40%—with trade-offs. Single estimate ignores uncertainty.
   
   **Engineer:** And 36% is industry average. Report warns this includes "organizations with vastly different AI usage patterns" and that "individual company's cost drivers may differ significantly."
   
   **Finance Lead:** Mm-hmm. No quarterly review gates? No optimization plan?
   
   **Analyst:** Exactly. Report recommends quarterly review gates and identifying top 3 optimization opportunities to achieve 15-20% cost efficiency gain.
   
   **CFO:** I see. So what's the fix?
   
   **Finance Lead:** Let me think... [pause] Model three scenarios tied to feature roadmap—base case plus 20%, moderate plus 30%, aggressive plus 40%. Implement cost tracking dashboard by feature and user cohort. Prioritize top 3 optimizations—prompt caching, model downgrading for low-value requests, usage-based throttling. Establish monthly AI cost review with Engineering, quarterly decision gates to reallocate based on actual burn rate.
   
   **CFO:** Makes sense. More adaptive budgeting.
