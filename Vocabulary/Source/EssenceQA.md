# Source Vocabulary – Essence Thinking Q&A

## Essence Loop Executive Summary

**Domain**: Essence Thinking – Sources, Evidence, and Information Quality  
**Role**: Mixed (students, researchers, analysts, journalists, product/ops leads)  
**Industry**: Education / Research / Media / Data & Tech  
**Time Budget**: 60 minutes  
**Coverage**: 5 Q&As (essence-thinking focus on *Source* vocabulary)

**Key Signals** (1–3 bullets):
- Ability to isolate 3–5 decision-critical *source* levers (type, distance, quality, provenance) from noisy input. 
- Ability to group those levers into 2–3 MECE clusters (for example, Source Type / Quality / Provenance) without overlap.  
- Ability to tie source vocabulary to concrete decisions about what to trust, what to cite, and what to ignore.

---

## Q1: Choosing sources for a first research essay

**EssenceDimensions**: [SignalVsNoise, ScopeBoundaries] | **Difficulty**: F | **RoleContext**: First-year undergraduate writing a research essay  
**Criticality**: [Blocks, Quantified] | **Stakeholders**: Student, Instructor | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:  
You must write a 2,000-word essay on social media and mental health. Your search returns: viral opinion pieces, personal blogs, government statistics, peer-reviewed studies, a long Wikipedia page, several YouTube videos, and a commercial report behind a paywall. You have limited time and access only to what your library subscription covers. Past assignments lost marks because students cited weak or unclear sources (random blogs, unsourced charts). Your instructor wants you to “show good judgment about sources” more than to read everything.

From this situation:  
1. Identify the **3–5 most essential levers** that should drive which sources you select and cite.  
2. Group them into **2–3 non-overlapping clusters** and name each cluster.  
3. Explain **what you will consciously de-prioritize or drop** and how you will measure whether your source mix is strong enough.

**Answer Key (~150–250 words)**:  
- **Target Essence Levers (3–5)**:  
  - Favour primary and high-quality secondary sources (peer-reviewed articles, official statistics).  
  - Check reliability and credibility of each outlet (track record, transparency, clear authorship).  
  - Prefer sources with clear provenance and citations you can follow.  
  - Limit unsupported opinion pieces to minor context, if at all.  
- **Clusters (2–3, MECE)**:  
  - *Source Type & Distance*: Prioritize peer-reviewed studies and official statistics; use textbooks or high-quality reviews as secondary syntheses; treat blogs and YouTube as low-priority context.  
  - *Quality & Provenance*: Choose sources with named authors, methods, and traceable references; skip anonymous charts or unclear data origins.  
- **Decision Link**: These clusters decide which 5–10 sources enter your bibliography and which stay out, directly affecting the essay’s credibility.  
- **Metrics & Priorities**: Aim for at least 70–80% of citations from primary/official sources; 0 citations from unreferenced opinion blogs.  
- **Common Failure Modes**: Counting sources instead of weighing quality; leaning on Wikipedia or viral posts as main evidence.

---

## Q2: Verifying breaking news with conflicting sources

**EssenceDimensions**: [ClusterMECE, DecisionLevers] | **Difficulty**: I | **RoleContext**: Newsroom journalist covering a breaking story  
**Criticality**: [Blocks, Risk, Stakeholders] | **Stakeholders**: Journalist, Editor, Audience, Source(s) | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:  
A major outage hits a popular payment app. On social media, users claim their money has “disappeared.” An anonymous employee sends you leaked screenshots suggesting a security breach. The company posts an official statement calling it a “temporary display issue” and denies any data loss. A regulator has not yet commented. Your editor wants a story in 45 minutes but warns: “We cannot falsely accuse them of losing funds.” You must decide what to publish now, what to hold, and which sources to highlight or downplay.

From this situation:  
1. Identify **3–5 essence levers** about *sources* that should shape your first article.  
2. Group them into **2–3 MECE clusters** (for example, On-the-record vs Anonymous vs Third-party) and name each cluster.  
3. Explain how each cluster **drives concrete editorial decisions** on wording, attribution, and follow-up.

**Answer Key (~150–250 words)**:  
- **Target Essence Levers (3–5)**:  
  - On-the-record vs anonymous sourcing (company statement vs leak).  
  - Independence and potential bias of each source (company PR vs internal whistleblower vs users).  
  - Verifiability of key claims (can balances be checked, logs confirmed, regulator contacted).  
  - Provenance and completeness of leaked materials.
- **Clusters (2–3, MECE)**:  
  - *Official & Verifiable*: Company statement, observable app behaviour, any regulator comments; used for cautious factual core.  
  - *Anonymous & Leaked*: Employee screenshots treated as leads, not facts; clearly labelled as “according to an anonymous source,” pending verification.  
  - *Public Signals*: User reports as evidence of impact but recognized as noisy and anecdotal.  
- **Decision Link**: These clusters shape the article’s spine: you can safely report the outage and user impact, quote the official explanation, and mention that leaked materials suggest deeper issues *without* asserting them as confirmed.  
- **Metrics & Priorities**: First priority is zero unverified factual accusations; track number of key claims backed by at least two independent sources.  
- **Common Failure Modes**: Treating a single leak as definitive; burying the company’s on-the-record statement; blurring fact with speculation.

---

## Q3: Selecting data sources for a KPI dashboard

**EssenceDimensions**: [SignalVsNoise, MetricsPriorities] | **Difficulty**: I | **RoleContext**: Data analyst designing an executive dashboard  
**Criticality**: [Blocks, Quantified, Stakeholders] | **Stakeholders**: Analyst, Execs, Finance, Operations | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:  
You are building a revenue and user-activity dashboard for executives. Possible data sources include: raw event logs from the product, a marketing vendor’s tracking pixels, finance’s monthly spreadsheets, a legacy data warehouse with incomplete documentation, and a new analytics database with partial backfill. Different teams argue that “their numbers” are correct. Executives want “one source of truth” and are tired of conflicting charts in meetings.

From this situation:  
1. Identify **3–5 essence levers** related to *data sources* that should guide which feeds power the dashboard.  
2. Group them into **2–3 non-overlapping clusters** and name each cluster.  
3. Propose **1–3 simple metrics and priorities** for source choice and reconciliation.

**Answer Key (~150–250 words)**:  
- **Target Essence Levers (3–5)**:  
  - Clear definition of primary sources for each KPI (for example, finance system for revenue, product events for usage).  
  - Data provenance and documentation quality (how traceable and auditable each dataset is).  
  - Reliability and timeliness (refresh cadence, known gaps, error rates).  
  - Independence or conflicts of interest (vendor KPIs vs internal logs).
- **Clusters (2–3, MECE)**:  
  - *Authoritative Systems*: Declare finance as the primary source for revenue and product events as the primary source for usage; others become reference checks.  
  - *Quality & Provenance*: Prefer sources with documented schemas, lineage, and checks over undocumented legacy tables, even if they look familiar.  
  - *Reconciliation Layer*: Where multiple sources exist, design explicit comparison views instead of mixing numbers silently.  
- **Decision Link**: These clusters determine which databases and tables feed “official” KPIs and which are side-by-side sanity checks, reducing meeting fights about where numbers came from.  
- **Metrics & Priorities**: Track the percentage of KPIs with a single named primary source, number of unexplained source mismatches, and time to reconcile discrepancies.  
- **Common Failure Modes**: Building dashboards on whichever dataset is easiest to query; hiding source differences behind averaged or blended figures.

---

## Q4: Scoping source requirements for an internal decision memo

**EssenceDimensions**: [ClusterMECE, ScopeBoundaries] | **Difficulty**: I | **RoleContext**: Product manager writing a recommendation memo  
**Criticality**: [Blocks, Action, Stakeholders] | **Stakeholders**: PM, Leadership, Finance, Legal | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:  
You are proposing a new subscription pricing model. Stakeholders send you many potential “sources”: old Excel models, market research decks, competitor screenshots, a consultant’s report, internal churn analyses, and anecdotal sales stories. Leadership wants a crisp 6-page memo with “just enough” data and citations to support a decision within a month. If you include everything, the memo will be unreadable; if you include too little, it will feel like guesswork.

From this situation:  
1. Identify **3–5 essence levers** about *sources* that should determine what evidence enters the memo.  
2. Group them into **2–3 MECE clusters** and name each cluster.  
3. Clarify **what is in-scope vs out-of-scope** for sourcing in this decision round.

**Answer Key (~150–250 words)**:  
- **Target Essence Levers (3–5)**:  
  - Priority for recent, traceable quantitative data on revenue, churn, and usage.  
  - Limited but clear competitor benchmarks from authoritative, verifiable sources.  
  - One or two qualitative sources (sales/customer insights) to explain numbers, not replace them.  
  - Exclusion of stale, undocumented spreadsheets and second-hand opinions.  
- **Clusters (2–3, MECE)**:  
  - *Core Quantitative Sources*: Finance and product analytics as primary sources for impact estimates, with clear provenance.  
  - *Market & Customer Context*: A small set of well-cited industry reports and summarized customer insights, each with links/backups.  
  - *Out-of-Scope/Appendix*: Old, unexplained models and anecdotal stories kept out of the main argument or parked in appendices.  
- **Decision Link**: These clusters define which sources appear in main charts and which are relegated, making the memo both credible and readable.  
- **Metrics & Priorities**: Limit core memo to ~5–8 cited sources; ensure 100% of numeric claims trace back to documented, verifiable origins.  
- **Common Failure Modes**: Stuffing the memo with every file you received; relying on attractive but unsupported consultant slides.

---

## Q5: Auditing sources behind an AI model’s outputs

**EssenceDimensions**: [DecisionLevers, MetricsPriorities] | **Difficulty**: A | **RoleContext**: AI governance lead reviewing training data sources  
**Criticality**: [Risk, Stakeholders, Quantified] | **Stakeholders**: Governance Lead, Legal, Data Engineers, End Users | **EstimatedTime**: ~10–15 min

**Question (for candidate)**:  
Your organization deploys a text-generation model fine-tuned on “internal and public sources.” A regulator now asks for documentation of training data sources, especially around copyrighted material, sensitive data, and known misinformation sites. Internally, you find: web scrapes with incomplete provenance, curated datasets with good documentation, proprietary customer documents that should not have been included, and a code repository of scripts with unclear logs. You must quickly identify the *essence* of the source situation to decide what to document, what to remove, and what future controls to implement.

From this situation:  
1. Identify **3–5 essence levers** concerning *sources* that should drive your audit and remediation plan.  
2. Group them into **2–3 MECE clusters** and name each cluster.  
3. Propose **1–3 key metrics and priorities** to make the model’s sourcing acceptable.

**Answer Key (~150–250 words)**:  
- **Target Essence Levers (3–5)**:  
  - Source categories (public licensed, public unlicensed, internal confidential, third-party licensed).  
  - Provenance and traceability of each category (can you show where it came from and under what terms).  
  - Presence of high-risk sources (customer data, sensitive PII, known misinformation sites).  
  - Ability to remove or re-weight problematic source segments.  
- **Clusters (2–3, MECE)**:  
  - *Legality & Rights*: Map datasets to licences and contracts; flag any sources without clear permission.  
  - *Risk & Sensitivity*: Identify data containing PII, confidential documents, or toxic/misinformation-heavy domains.  
  - *Traceability & Controls*: Assess which pipelines have full provenance and which need logging/monitoring upgrades.  
- **Decision Link**: These clusters drive go/no-go decisions: which data to purge, which sources to whitelist or blacklist, and what to disclose to regulators and users.  
- **Metrics & Priorities**: Track percentage of training tokens from fully documented, rights-cleared sources; percentage of high-risk sources removed or quarantined; and coverage of pipelines with traceable logs.  
- **Common Failure Modes**: Treating “public on the web” as permission; ignoring undocumented legacy scrapes; focusing on model behaviour without fixing upstream sources.
