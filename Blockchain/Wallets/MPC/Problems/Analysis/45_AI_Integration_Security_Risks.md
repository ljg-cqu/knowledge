# AI Integration Security Risks in MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security Team

---

## Pre-Section: Context Recap

- **Problem title**: AI integration security risks in MPC wallets using Model Context Protocol (MCP) and AI agents
- **Current state**:
  - ~58% of digital asset custody providers have integrated AI into MPC or advanced wallets for fraud detection, transaction simulation, and smart recovery by 2025
    [Source: "How MPC Wallets Are Evolving for Better Security", Safeheron, 2025-07-15].
  - Coinbase Payments MCP exposes text-based wallet control (e.g., "send 0.1 ETH to X") to AI agents such as ChatGPT, Claude, and Gemini, driving a 10,000% surge in x402 protocol usage to ~500K transactions in one week after launch
    [Source: Coinbase Developer Platform Payments MCP launch blog, 2025-10; Market: x402 Protocol Activity Report, 2025-10].
  - Security researchers have demonstrated prompt injection, memory injection, and tool-poisoning attacks that can exfiltrate credentials or trigger unauthorized actions in AI agents integrated with wallets
    [Source: Brave Browser/BraveNewCoin OTP extraction proof-of-concept, 2025; Princeton University memory injection research, 2025; Security analysis by SlowMist, 2025].
  - OpenAI’s security leadership publicly acknowledges prompt injection as an "unsolved security problem" despite extensive safety work
    [Source: OpenAI security officer statement on prompt injection, 2025].
- **Pain points**:
  - **Unsolved structural vulnerability**: Prompt injection and related attacks (tool poisoning, indirect injection, memory manipulation) can subvert model instructions and security policies that sit above wallet APIs, turning AI from a guardrail into an attack vector
    [Source: OWASP LLM Security, 2023+; Model Context Protocol security best practices, 2024+].
  - **Direct wallet access via MCP**: AI agents can prepare or in some cases initiate wallet actions such as transfers and approvals; if tools are over-permissive or context isolation fails, a single compromised prompt can lead to multi-account losses
    [Source: Model Context Protocol specification & security best practices, 2024+; Coinbase Developer Platform Payments MCP docs, 2025].
  - **High-value, high-scale environment**: Institutional MPC custody platforms secure an estimated $50B+ in assets and serve tens of millions of users; a single successful attack could drain many wallets simultaneously
    [Estimate based on: Market share of major custodians (Coinbase, BitGo, Fireblocks, Anchorage) and 58% AI integration rate, Medium confidence].
  - **Sparse operational telemetry**: Providers have limited public data on AI-related incidents, detection rates, or false-positive rates, making it difficult to calibrate controls.
- **Goals** (by ~Q4 2026):
  - Reduce AI-related security incidents to **<1 per 100K AI-assisted transactions (minimum) / <1 per 500K (target) / <1 per 1M (ideal)**.
  - Achieve **99% / 99.9% / 99.99%** detection and blocking rate for prompt-injection-style attacks in pre-production testing and production monitoring.
  - Keep AI-powered fraud detection **false positives <5% (min) / <2% (target) / <0.5% (ideal)** of legitimate transactions flagged.
  - Detect and contain AI-related security incidents within **≤15 min (min) / ≤5 min (target) / ≤1 min (ideal)** from anomaly detection to containment.
  - Limit **annual losses from AI-related vulnerabilities to <$1M (min) / <$100K (target) / ideally $0** across the platform
    [Source: Problem statement – Goals and success criteria; Chainalysis 2025 Crypto Crime Mid-Year Update, 2025-06].
- **Hard constraints**:
  - **Prompt injection has no perfect technical fix today**; defenses are probabilistic and layered rather than absolute
    [Source: OpenAI security officer statement, 2025; OWASP LLM Security, 2023+].
  - 24-month window (Q1 2025–Q4 2026) and a typical **$1M–$3M per major provider** budget for AI security—covering red teaming, monitoring, engineering, audits, and training
    [Source: Problem statement – Key constraints and resources].
  - Strict latency budgets and availability targets (e.g., sub-second fraud scoring, 99.99% uptime) for exchanges and custody providers
    [Source: Major exchange and custody SLA benchmarks; Webasha AI fraud detection overview, 2025].
  - Regulatory requirements from NIST AI RMF, EU AI Act, and financial regulators demanding explainability, human oversight, and robust access control
    [Source: NIST AI Risk Management Framework 1.0, 2023; EU AI Act text for high-risk AI systems, 2024+].
- **Key facts**:
  - $2.17B was stolen from crypto platforms in the first half of 2025, exceeding all of 2024; 59% of losses (~$1.83B) came from access-control failures, a category that AI-integrated wallets can exacerbate if misconfigured
    [Source: Chainalysis, "2025 Crypto Crime Mid-Year Update", 2025-06].
  - AI-driven crypto attacks increased **1,025% vs. 2023**, and overall crypto thefts rose **303% in Q1 2025**, with a single ByBit incident accounting for $1.46B (69% of losses that period)
    [Source: Chainalysis, 2025-06].
  - 87% of surveyed crypto users are willing to let AI agents manage at least 10% of their portfolio, dramatically expanding the attack surface if agent tooling is insecure
    [Source: Industry survey on AI agents and crypto users, 2025-04].
  - AI agent token market value grew from **<$5B → $15B** (222%) and is projected at **$60B** by end-2025; AI agents themselves projected to grow from **10K → 1M+** instances
    [Source: Industry Analysis, 2024-Q4].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   MPC wallets are integrating AI agents via MCP and similar protocols to improve fraud detection, UX, and recovery. However, prompt injection, memory injection, and tool poisoning enable adversaries to hijack AI agents, manipulate their context, and coerce them into authorizing or facilitating unauthorized wallet actions, in an environment where stolen funds are irreversible and attack scale is global
   [Source: JFrog, "CVE-2025-6515: Prompt Hijacking Attack Affects MCP Ecosystem", 2025; Model Context Protocol security best practices, 2024+; Brave Browser/BraveNewCoin OTP attack write-up, 2025; Princeton memory injection research, 2025].

2. **Key contradictions**
   - **Security vs. usability & automation**: Deep integration lets AI block scams and streamline approvals, but the more authority AI has, the more damage a compromised prompt or tool can inflict
     [Source: Safeheron MPC wallet security trends, 2025; Webasha AI fraud detection review, 2025].
   - **Openness vs. control**: MCP encourages rich tool ecosystems and cross-application interoperability; each new tool and data source increases the risk of indirect prompt injection and cross-system propagation of malicious instructions
     [Source: MCP specification & security best practices, 2024+; OWASP LLM Security, 2023+].
   - **Strong fraud models vs. false positives**: Aggressive blocking policies help stop novel attacks but can sharply increase false positives, harming user trust and business metrics
     [Source: Unit21, "False Positives: Causes, How to Calculate, & How to Reduce", 2025; Webasha fraud detection blog, 2025].
   - **Centralized AI platforms vs. decentralized assets**: Wallets may rely on centralized AI providers (OpenAI, Anthropic, Google) while protecting decentralized crypto assets; failures or policy changes in AI platforms can propagate instantly across many wallets.

3. **Actors in tension**
   - Security and risk teams insisting on conservative AI privileges, robust isolation, and heavy monitoring.
   - Product and growth teams pushing for frictionless, AI-driven UX and differentiation.
   - AI platform providers optimizing general-purpose capabilities vs. finance-specific safety.
   - Regulators and institutional clients demanding explainability and traditional control models, yet lacking detailed understanding of LLM attack vectors.

### 1.2 Goals and conditions

- **Security outcomes**:
  - Achieve **near-zero** successful AI-mediated unauthorized wallet actions in production (target: <1 incident per 500K–1M AI-assisted transactions by Q4 2026).
  - Reduce the fraction of total crypto losses attributable to AI-related access-control failures to **negligible (<1–2%)** within 2–3 years, even as AI adoption grows
    [Estimate based on: Chainalysis 2025 mid-year loss composition, 2025-06, Medium confidence].
- **Detection goals**:
  - 99–99.99% detection and blocking of prompt injection attempts in testing and red-team campaigns, with continuous evaluation against new attack patterns
    [Source: OWASP LLM Security, 2023+; Microsoft "Protecting against indirect injection attacks in MCP", 2025].
  - Ability to trace each AI-triggered wallet action back to prompts, tools, and policy decisions for forensic and regulatory review.
- **Operational goals**:
  - Keep additional latency from AI safety controls within **+50–150 ms p95** for online flows so as not to break UX or trading SLAs
    [Estimate based on: exchange latency budgets and AI fraud detection benchmarks, Medium confidence].
  - Maintain **false positive rate <2–5%** for fraud/abuse flags to avoid user churn and operations overload
    [Source: Unit21 false positive guidance, 2025; Webasha blog, 2025].
- **Conditions**:
  - Must comply with NIST AI RMF principles (governance, mapping, measurement, management) and EU AI Act obligations for high-risk financial AI systems
    [Source: NIST AI RMF 1.0, 2023; EU AI Act, 2024+].
  - Need to be compatible with existing MPC stacks and custody processes; cannot require full re-platforming of all wallets in 24 months.

### 1.3 Extensibility and reframing

- **Attribute reframing – "one system, many attributes"**  
  Treat "AI-integrated MPC wallet" as a composite system with attributes: (1) **Model layer** (foundation model, fine-tuning), (2) **Context layer** (MCP tools, memory, retrieval), (3) **Control layer** (policy engine, approvals, limits), and (4) **Wallet layer** (MPC, HSMs, on-chain contracts). Risk arises from misalignment across these layers rather than any single component
  [Source: OWASP LLM Security, 2023+; MCP security best practices, 2024+].

- **Scope reframing – advisory vs. control-plane AI**  
  Instead of the binary "AI or no AI", distinguish between:
  - **Advisory AI**: analysis and recommendations only; humans or deterministic services own final actions.
  - **Control-plane AI**: AI can directly trigger or pre-authorize wallet actions via MCP tools.
  Reframing allows risk-tiered deployment: high-risk flows may restrict AI to advisory mode, while low-risk flows can use deeper automation.

- **Risk reframing – from "prompt injection" to "context integrity"**  
  Rather than focusing narrowly on prompts, consider **context integrity**: ensuring that all inputs, tools, and memories that influence wallet actions come from authenticated, authorized, and sanity-checked sources. This widens the solution space to include supply-chain security for tools, data provenance, and memory hygiene, not just prompt filtering
  [Source: Microsoft AI Prompt Shield and supply chain security guidance, 2025; OWASP LLM Security, 2023+].

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Models and agents**: Foundation models (GPT-class, Claude, Gemini) and derived agents performing fraud analysis, transaction simulation, and user interaction.
- **MCP and tool layer**: Model Context Protocol servers, tool definitions, permissions, and session management linking AI agents to wallet operations like balance checks, transaction building, and risk scoring
  [Source: MCP specification & security best practices, 2024+; Coinbase Developer Platform docs, 2025].
- **Wallet and custody layer**: MPC engines, HSMs, smart-contract wallets, and associated key-management and policy engines controlling actual fund movements
  [Source: Stackup, "MPC Wallets: A Complete Technical Guide", 2025].
- **Security controls**: Prompt filters, content classifiers, allow/deny lists for tools, context-isolation mechanisms, red-team pipelines, and runtime monitoring.
- **Data and memory**: Long-term memory stores, vector databases, and logs that can be poisoned or misused for later decisions
  [Source: Princeton memory injection research, 2025; OWASP LLM Security, 2023+].

### 2.2 Balance and "degree" issues

- **AI autonomy vs. approval friction**  
  More autonomy (e.g., auto-approving low-value transfers) improves UX but multiplies the blast radius of a successful injection. Overly strict approvals defeat the purpose of AI integration and increase operational load.

- **Context richness vs. attack surface**  
  Rich context (emails, social feeds, on-chain history) improves fraud detection but introduces countless untrusted sources where attackers can hide malicious instructions or poisoned data
  [Source: Brave OTP attack via email, 2025; OWASP LLM Security, 2023+].

- **Detection aggressiveness vs. false positives**  
  Tight filters and anomaly thresholds catch more attacks but may block legitimate activity or drown analysts in alerts, undermining trust in AI-driven protection
  [Source: Unit21 false positive analysis, 2025].

- **Centralization vs. resilience**  
  Using a single AI provider simplifies integration but creates correlated failure modes (e.g., a novel injection bypassing that provider’s filters could affect many wallets simultaneously).

### 2.3 Causal chains

1. **Indirect prompt injection to unauthorized transfer**  
   Untrusted website or email embeds hidden instructions (white text, HTML comments, encoded payload) → AI agent ingests this content for transaction explanation → malicious instructions override original system prompt and safety rules → agent calls MCP tool to prepare or approve transfer to attacker address → user or automated process signs transaction believing it is benign
   [Source: BraveNewCoin/Brave Browser prompt injection OTP proof-of-concept, 2025; OWASP LLM Security, 2023+].

2. **Memory injection to long-term systemic drift**  
   Attacker gradually poisons long-term memory with fabricated "safe" addresses or vendors → over time, multiple agents treat these as trusted entities → future fraud checks systematically under-score attacker-related transactions → slow-drain attacks across many accounts
   [Source: Princeton University memory injection research on AI agents and crypto wallets, 2025].

3. **Tool poisoning to over-privileged AI**  
   Malicious or poorly designed MCP tools misdeclare capabilities (e.g., claiming to be "simulation only" but actually able to send signed transactions), or include hidden triggers in descriptions → agent uses tools under incorrect assumptions → attacker-crafted prompts cause real fund movements when the system believed only simulations were possible
   [Source: Microsoft, "Protecting against indirect injection attacks in MCP", 2025; SlowMist analysis of tool and JSON injection attacks, 2025].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholder relationships

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream – AI/LLM providers | Provide foundation models, MCP-compatible runtimes, and safety tooling | Maximize capability, adoption, and platform revenue while maintaining safety reputation | Limited visibility into downstream wallet-specific risks; diverse customer use cases | Wallet providers want strict, finance-grade guarantees; model providers optimize for generality and speed |
| Upstream – MCP & tool developers | Build MCP servers, tool plugins, SDKs | Broad ecosystem adoption, easy integration | Security expertise varies; incentives to ship features fast | Security teams push for strict reviews and constrained permissions |
| Downstream – MPC wallet & custody providers | Integrate AI to improve fraud detection and UX while safeguarding assets | Tight SLAs, legacy stacks, budget and timeline limits, regulatory scrutiny | Product teams push for rich AI features; risk teams and regulators prefer conservatism |
| Downstream – Exchanges and end users | Use AI-integrated wallets and agents for trading, payments, and portfolio management | Safety, convenience, low friction, transparent liability | Limited understanding of AI risks; low tolerance for losses | May enable risky features out of convenience (e.g., auto-approval) |
| External – Regulators & auditors | Define and enforce safety and compliance standards for AI in finance | Limited AI security expertise; slow rulemaking cycles | Need evidence-based guidance; may overreact after incidents |
| External – Attackers | Exploit AI and MCP weaknesses to steal funds or data | Seek asymmetric high-value payoffs | Increasingly automated attack tooling and AI use | Benefit from fragmented defenses and weak standards |

[Source: Problem statement – Stakeholders; Safeheron, 2025; Chainalysis 2025 Crypto Crime Update; NIST AI RMF, 2023].

### 3.2 Environment

- **Regulatory environment**  
  NIST AI RMF and EU AI Act treat financial AI systems as high risk, requiring risk management, transparency, robustness, and human oversight. Emerging guidance (e.g., from securities regulators and central banks) expects explainable controls around AI-mediated decisions
  [Source: NIST AI RMF 1.0, 2023; EU AI Act, 2024+].

- **Market environment**  
  Explosive growth of AI agent markets and user willingness to delegate portfolio management create strong commercial incentives to ship AI features quickly, often ahead of standardized security frameworks
  [Source: Industry Analysis, 2024-Q4; Industry survey on AI agents and portfolios, 2025-04].

- **Threat environment**  
  Sophisticated attackers (including state-linked groups) increasingly use AI for reconnaissance, phishing, and automation. Access-control failures are already the dominant category of crypto losses, and AI that can directly operate wallets amplifies these risks
  [Source: Chainalysis, 2025 Crypto Crime Mid-Year Update, 2025-06].

### 3.3 Responsibility and room for maneuver

- **AI/LLM providers**: Responsible for baseline model safety, MCP security guidance, and clear guarantees about what protections exist and what must be implemented downstream.
- **MCP and tool ecosystem**: Responsible for robust defaults (least privilege, explicit scopes, safe templates), security testing, and transparent vulnerability handling (e.g., CVE-2025-6515 disclosure by JFrog)
  [Source: JFrog CVE-2025-6515 publication, 2025; MCP security best practices, 2024+].
- **Wallet and custody providers**: Own end-to-end risk posture: which tools AI can call; which actions require human approvals; monitoring and response; and client communications.
- **Regulators and auditors**: Can set expectations that AI wallet integrations must undergo independent red teaming, have explicit segregation between advisory and control-plane behaviors, and meet access-control baselines comparable to or stricter than non-AI systems.

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Pre-2023 – Advisory analytics only**  
   Early uses of AI in wallets and exchanges focused on anomaly detection and basic analytics with no direct wallet control; risks were primarily model accuracy and bias, not direct key compromise
   [Source: Webasha AI fraud detection blog, 2025].

2. **2023–2024 – LLM agents and tool ecosystems emerge**  
   General-purpose LLMs with plugin/tool systems made it easy to connect models to arbitrary APIs, including finance and crypto services, but security models for these tools lagged behind
   [Source: OWASP LLM Security, 2023+].

3. **2024–2025 – MCP standardization and Coinbase Payments MCP launch**  
   Model Context Protocol consolidated tool semantics and interoperability across AI systems; Coinbase’s Payments MCP gave multiple AI platforms direct wallet access via x402, massively increasing transaction volume through AI-controlled flows
   [Source: Coinbase Developer Platform Payments MCP launch blog, 2025-10; Market: x402 Protocol activity report, 2025-10].

4. **2025 – Public discoveries of systemic vulnerabilities**  
   Research teams (Brave, Princeton, SlowMist, JFrog, Microsoft) documented prompt hijacking, tool poisoning, memory injection, and cross-system attacks in MCP and agent ecosystems, demonstrating concrete paths from untrusted content to credential or wallet compromise
   [Source: Brave OTP attack PoC, 2025; Princeton memory injection research, 2025; JFrog CVE-2025-6515 disclosure, 2025; SlowMist AI agent security analysis, 2025; Microsoft AI Prompt Shield blog, 2025].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - AI product cycles and competition prioritized capability and UX over conservative security baselines, particularly in consumer wallets.
  - Lack of widely adopted standards for AI-to-wallet integration; early adopters implemented proprietary patterns without shared threat models.
  - Underestimation of how easily non-technical users would delegate real control to AI agents.

- **Direct technical and operational causes**:
  - Over-permissive MCP tools (e.g., ability to create or sign transactions) without strict scoping and multi-layer approvals.
  - Absence of robust context isolation between untrusted content (webpages, emails, DMs) and tools that control funds.
  - Long-lived, shared memories or logs that can be poisoned and reused in future sessions.
  - Insufficient AI-specific monitoring, red teaming, and incident response for wallet-integrated agents
    [Source: OWASP LLM Security, 2023+; Microsoft AI Prompt Shield documentation, 2025].

### 4.3 Root issues

- **Misaligned incentives and expertise gaps**: AI teams, wallet engineers, and security specialists often operate in silos, with partial understanding of each other’s constraints and threats.
- **Immature threat models**: Many organizations still treat LLMs as "just another microservice" rather than as powerful interpreters of untrusted instructions.
- **Standards lag**: While NIST AI RMF and OWASP LLM Security exist, mapping their high-level principles into concrete requirements for MCP-integrated wallets is still emerging
  [Source: NIST AI RMF 1.0, 2023; OWASP LLM Security, 2023+].

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- AI integration into wallets will continue to accelerate due to competitive pressure and user demand, regardless of whether robust security patterns are in place
  [Source: Safeheron AI integration rate (58% of custody providers), 2025-07-15; Industry Analysis, 2024-Q4].
- Attackers will reuse and industrialize known AI attack techniques (prompt injection, tool poisoning, memory injection), integrating them into standard phishing and credential-theft playbooks.
- Because access-control failures already drive the majority of losses, incremental AI-related failures are likely to go underreported but could cause large correlated incidents, especially when multiple providers share the same AI platforms
  [Source: Chainalysis 2025 Mid-Year Crypto Crime Update, 2025-06].

### 5.2 Early signals

- Successful proof-of-concept prompt injection attacks extracting email OTPs and manipulating agents controlling wallets
  [Source: Brave Browser/BraveNewCoin PoC, 2025].
- Academic work showing persistent, cross-user memory injection and cascading spread of poisoned content between AI agents
  [Source: Princeton researchers on AI agents and crypto wallets, 2025].
- Disclosure of MCP-related CVEs (e.g., CVE-2025-6515) enabling session hijacking and prompt hijacking, highlighting protocol-level as well as application-level risks
  [Source: JFrog security research blog, 2025].
- Rapid creation of specialized defenses (e.g., Microsoft AI Prompt Shield, MCP security best practices), indicating recognition of the problem but also its evolving nature
  [Source: Microsoft, "Protecting against indirect injection attacks in MCP", 2025; MCP security best practices, 2024+].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**  
  - Industry converges on strong, finance-grade patterns: advisory-only AI for high-value flows, strict tool scoping, sandboxed execution, and comprehensive monitoring.
  - MCP and AI platforms bake in secure defaults and clear separation-of-duties for wallet actions.
  - AI-related wallet thefts remain rare and smaller in scale than traditional infrastructure attacks.

- **Baseline scenario**  
  - Leading providers implement layered defenses and red teaming; smaller or fast-moving projects lag.
  - Several medium-scale incidents (single- or double-digit millions) occur due to AI-mediated access-control failures, prompting incremental regulatory responses.

- **Pessimistic scenario**  
  - A major provider or ecosystem of projects suffers an AI-mediated incident that drains many wallets at once (e.g., through poisoned shared tools or cross-tenant memory injection).
  - Regulatory backlash forces rollbacks of AI features, stricter capital and control requirements, and reputational damage for AI-integrated MPC wallets.

[Scenarios estimated based on: adoption and threat trends in Chainalysis 2025 mid-year report and historical lag between new technologies and security standardization, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Mature MPC and custody security practices**: Providers already operate hardened MPC stacks, HSMs, and incident response processes for key theft, which can be extended to AI-related incidents
  [Source: Stackup MPC technical guide, 2025].
- **Emerging AI security frameworks**: NIST AI RMF, OWASP LLM Security, and MCP security best practices provide structured guidance that can be tailored to wallets
  [Source: NIST AI RMF 1.0, 2023; OWASP LLM Security, 2023+; MCP security best practices, 2024+].
- **Vendor investments in defenses**: Major AI providers and cloud platforms are shipping prompt shields, content filters, and supply-chain security features that can be composed into wallet architectures
  [Source: Microsoft AI Prompt Shield blog, 2025].
- **Chain analytics and monitoring**: Existing transaction-monitoring pipelines and AML/KYC tools can feed into AI safety and anomaly detection for AI-mediated transactions
  [Source: Chainalysis and Webasha fraud detection materials, 2025].

### 6.2 Capability gaps

- **LLM security expertise inside wallet teams**: Many MPC and security engineers are not yet deeply familiar with LLM-specific attack vectors and mitigations.
- **Cross-functional governance**: Few providers have clear AI risk governance models linking product, AI/ML, security, compliance, and legal functions.
- **Data provenance and memory hygiene**: Tooling to manage, audit, and clean AI memories and vector stores is immature.
- **Red-team and testing infrastructure**: Many organizations lack dedicated AI red teams and automated test harnesses for prompt-injection and tool-abuse scenarios
  [Source: OWASP LLM Security, 2023+; industry observations summarized in Microsoft AI security guidance, 2025].

### 6.3 Buildable capabilities (1–6 months)

- Establish an **AI security guild / tiger team** spanning AI, wallet, and security engineers, focused on MCP and wallet use cases.
- Implement **reference architectures** for advisory-only vs. control-plane AI, with clear capability boundaries and example policies.
- Stand up **AI red-teaming and chaos-testing environments** targeting prompt injection, tool misuse, and memory poisoning against staging wallets.
- Integrate **AI-specific logging and observability**: capture prompts, tool calls, outputs, and decisions tied to transaction IDs for audit and forensics (with strong privacy controls).

[Estimates based on: typical security program buildout timelines and examples from other MPC security hardening efforts, Medium confidence].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Rapid AI integration into MPC wallets via MCP; sharp increase in AI-driven attacks and access-control failure losses.
- **Problem**: Prompt injection, memory injection, and tool poisoning can turn AI-integrated wallets into large-scale attack surfaces where a single compromised prompt or tool can move funds.
- **Analysis**: Internal dynamics (autonomy vs. control, context richness vs. attack surface), external stakeholders and regulation, historical evolution, trends, capabilities, and gaps.
- **Options**: Tiered AI integration models (advisory-only vs. control-plane), strong isolation architectures, standardized MCP security profiles, and defense-in-depth.
- **Risks**: Large-scale correlated losses, regulatory backlash, usability regressions, and persistent unknown unknowns in AI behavior.

### 7.2 Key judgments (for validation)

1. **【P0】** Prompt injection and related attacks will remain structurally unsolved in the medium term; mitigation must focus on layered controls and containment rather than perfect prevention
   [Source: OpenAI security officer statement, 2025; OWASP LLM Security, 2023+].
2. **【P0】** Risk can be materially reduced by treating AI-integrated wallets as **multi-layer control systems** with strict separation between advisory AI and irreversible wallet actions, plus strong logging and approvals.
3. **【P1】** Industry-wide standards and MCP security profiles tailored to financial use cases will significantly reduce configuration and implementation errors.
4. **【P2】** Overly conservative restrictions (e.g., banning AI tools from any wallet interaction) will forgo material security and UX benefits and are unlikely to be sustainable competitively.

### 7.3 Alternative high-level paths

- **Path A – Aggressive AI control-plane integration with strong guardrails**: Allow AI agents to directly orchestrate some wallet actions under strict limits, policies, and defense-in-depth.
- **Path B – Advisory-first strategy**: Keep AI strictly advisory for most high-value flows, with deterministic services handling all direct wallet operations.
- **Path C – Minimal AI integration**: Restrict AI to out-of-band analytics and client education, avoiding MCP-based control altogether.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Security-centric bias**: Analysis may overweight catastrophic but low-frequency tail events relative to everyday UX and business trade-offs.
- **Publication bias**: Documented attacks (Brave, Princeton, JFrog) might underrepresent the true frequency and sophistication of real-world exploitation; conversely, PoCs may not map 1:1 to production systems.
- **Vendor bias**: Many sources are from companies selling AI safety or MCP tooling; they may emphasize risks that align with their products.

### 8.2 Required intelligence

- **Empirical incident data**: Number and severity of AI-mediated security incidents in wallet and exchange environments (including near-misses and internal red-team findings).
- **Tool usage patterns**: Which MCP tools are most frequently used in production and what effective scopes, rate limits, and approval models are applied.
- **Detection performance metrics**: Real false positive/false negative rates and latency for AI safety filters and anomaly detectors in production.
- **User behavior insights**: How often users override AI warnings; user comprehension of AI agent roles and permissions.

### 8.3 Validation plan

1. **AI red teaming and tabletop exercises**  
   - Run structured red-team campaigns against staging environments using known injection patterns (Brave, OWASP, Microsoft examples) and new variants.  
   - Measure success rates, detection times, and containment effectiveness.

2. **Controlled pilots of tiered AI modes**  
   - Deploy advisory-only AI for high-value flows and limited autonomous AI for low-value flows.  
   - Track fraud outcomes, false positives, UX metrics, and support tickets over 3–6 months.

3. **Data and log review**  
   - Correlate wallet incidents and near-misses with AI interactions, prompts, and tool calls.  
   - Use this data to recalibrate thresholds, refine tool scopes, and update policies.

4. **External review and audits**  
   - Engage independent AI security experts to review architectures, MCP configurations, and red-team results.  
   - Map controls explicitly to NIST AI RMF and EU AI Act requirements.

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative risk estimates (incident likelihood, loss distributions) will evolve as more field data and telemetry become available.
- Preferred architectural patterns may shift with new MCP versions, AI safety features, or alternative approaches (e.g., smaller specialized models with constrained capabilities).
- Regulatory expectations and case law may significantly change what is considered "reasonable" AI integration.

### 9.2 Incremental approach

- Start with **advisory-only AI** and strictly constrained MCP tools for high-risk flows; introduce control-plane capabilities gradually in low-risk tiers after evidence-based evaluations.
- Apply **progressive hardening**: baseline logging → anomaly detection → prompt shields and context isolation → advanced memory-hygiene and data provenance.
- Maintain **rollback options** to disable or downgrade AI features quickly if incidents or new vulnerabilities emerge.

### 9.3 "Good enough" criteria

- AI-mediated wallet flows have **no known successful exploitation** over a sustained observation period (e.g., 12–18 months) with strong red-team coverage.
- Controls and documentation are sufficient for positive findings from independent audits against NIST AI RMF and applicable financial regulations.
- AI features demonstrate **net positive impact** on fraud loss rates and UX (e.g., reduced successful scams, manageable false-positive levels), validated via A/B tests.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. AI integration via MCP fundamentally **changes the threat model** for MPC wallets: attackers can now target model prompts, tools, and memories instead of only keys and infrastructure.
2. Prompt injection and related attacks are **structural and unsolved**; effective defense requires layered controls, strict capability boundaries, and continuous monitoring rather than reliance on any single filter
   [Source: OpenAI security statement, 2025; OWASP LLM Security, 2023+].
3. A **tiered integration strategy**—advisory-only AI for high-value flows, constrained control-plane AI for low-value flows, and robust observability—offers a pragmatic path to capture AI benefits while containing systemic risk.
4. Industry-wide **standards, reference architectures, and MCP security profiles** tailored to finance will be crucial to avoid repeated, bespoke mistakes and to satisfy regulators.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

1. **【P0 – Critical】 Define AI integration tiers and policies** → CISO + Product + AI Lead → Documented policy covering advisory vs. control-plane AI, per-transaction risk tiers, and approval workflows: 0 → 1 approved policy → **2026-02-15**.
2. **【P0 – Critical】 Inventory and harden MCP tools** → AI Platform & Wallet Engineering → 100% of MCP tools reviewed and categorized; high-risk scopes (e.g., transaction sending) require multi-factor approvals and rate limits: baseline unknown → 100% inventoried and classified → **2026-03-31**.
3. **【P0 – Critical】 Establish AI red teaming for wallet use cases** → Security Engineering → Red-team playbook and first campaign completed; ≥20 high-value scenarios tested; remediation backlog created → **2026-03-31**.
4. **【P1 – Important】 Implement AI-specific observability and logging** → Platform & Data Engineering → All AI-mediated transactions linked to prompts, tools, and risk scores in logs with secure retention and access controls: 0% → ≥80% coverage → **2026-04-30**.
5. **【P1 – Important】 Pilot advisory-only vs. control-plane AI** → Product & Risk → Two pilots (retail low-value; institutional advisory) with pre/post metrics on fraud, UX, and false positives → **2026-05-31**.
6. **【P2 – Optional】 Participate in industry MCP/AI security working group** → Strategy & Standards Team → Join or initiate working group; contribute draft financial MCP security profile → **2026-06-30**.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Undetected AI-mediated wallet breach causing large losses | High | Medium | Sudden outflows correlated with AI-mediated actions; anomalous tool calls or prompts | Defense-in-depth (tiered approvals, rate limits, anomaly detection); rapid kill switches to disable risky tools; incident response runbooks | CISO & Security Engineering |
| Overly restrictive controls degrade UX and adoption | Medium | Medium | Increase in user complaints, abandoned flows, and manual review queues after AI controls rollout | Iterate thresholds using data; segment by risk tier; improve explanations and self-service appeal mechanisms | Product & Risk |
| Regulatory backlash after industry-wide incident | High | Low–Medium | High-profile AI-driven wallet hack with public/regulatory attention | Proactive engagement with regulators; transparent control mapping to NIST AI RMF/EU AI Act; independent audits and certifications | Compliance & Legal |
| Hidden dependencies on single AI or MCP vendor | Medium–High | Medium | Vendor outage or new vulnerability simultaneously affects many flows | Multi-provider strategy; abstraction layers; regular vendor risk assessments and contingency plans | Architecture & Vendor Management |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A. Aggressive control-plane AI** (AI can initiate/approve some transactions) | Maximizes automation and UX gains; strongest differentiation for power users and institutions | High complexity; requires very strong controls and monitoring; difficult regulatory story | Larger correlated losses if defenses fail; hard-to-explain failures | Mature teams with strong AI security expertise and robust governance | When organization lacks AI security depth or faces very conservative regulators |
| **B. Advisory-first AI with constrained automation** | Captures most fraud-detection and UX benefits while keeping irreversible actions behind deterministic services and human approvals | Moderate engineering effort; requires careful design of handoff flows | Residual risk from social engineering and advisory misuse; smaller automation gains | Institutions and consumer products needing balance of safety and UX | When business model depends on fully autonomous agents managing funds |
| **C. Minimal AI integration (analytics-only)** | Lowest additional attack surface from AI; easier regulatory approval | Forfeits many potential UX and security benefits; may lag competitors | Users may adopt third-party agents with worse security; shadow AI use | Very high-risk custodians, early regulatory uncertainty | When competitors are already delivering safe, audited AI-integrated wallets |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **AI Agent** | Autonomous or semi-autonomous system built on LLMs (e.g., ChatGPT, Claude, Gemini) that can take actions such as analyzing transactions or orchestrating wallet operations via tools | N/A | [Source: Industry Analysis of AI agents, 2024-Q4; Safeheron, 2025] |
| **Model Context Protocol (MCP)** | Protocol and API layer that exposes tools, resources, and data streams to AI systems in a standardized way, commonly used to connect agents to wallets and payment systems | N/A | [Source: MCP specification & security best practices, 2024+] |
| **Prompt Injection** | Attack where adversarial instructions hidden in user inputs, web pages, or other content override the system prompt or safety policies of an LLM, potentially leading to unauthorized actions | N/A | [Source: OWASP LLM Security, 2023+; Brave Browser PoC, 2025] |
| **Memory Injection Attack** | Technique where attackers plant malicious or false data into an AI system’s long-term memory so that future decisions are influenced in their favor, often persisting across sessions and users | N/A | [Source: Princeton University research on AI agents and crypto wallets, 2025] |
| **Tool / Function Poisoning** | Manipulation of tool descriptions, capabilities, or implementations so that AI agents misinterpret their safety properties (e.g., simulation-only vs. real transfers), enabling abuse of MCP-integrated tools | N/A | [Source: Microsoft AI Prompt Shield blog, 2025; SlowMist AI agent security analysis, 2025] |
| **x402 Payment Protocol** | Blockchain payment protocol used by Coinbase Payments MCP for AI-mediated transactions; experienced a 10,000% activity surge to ~500K transactions/week after MCP launch | N/A | [Source: Coinbase Developer Platform Payments MCP blog, 2025-10; x402 Protocol market report, 2025-10] |
| **Behavioral Biometrics** | AI-powered authentication using patterns such as typing speed, mouse movement, mobile gestures, and device fingerprinting instead of traditional passwords | N/A | [Source: Safeheron MPC security trends, 2025; Webasha AI in fraud detection, 2025] |
| **False Positive Rate (FPR)** | Percentage of legitimate transactions incorrectly flagged as suspicious or fraudulent by detection systems | % of legitimate events | [Source: Unit21, "False Positives" guide, 2025] |
| **Access Control Failure** | Security failure where authentication, authorization, or permission boundaries are bypassed or misconfigured, allowing unauthorized access or actions | N/A | [Source: Chainalysis, 2025 Crypto Crime Mid-Year Update, 2025-06] |
| **NIST AI Risk Management Framework (AI RMF)** | U.S. framework providing principles and processes for governing AI risks across governance, mapping, measurement, and management functions | N/A | [Source: NIST AI RMF 1.0, 2023] |
| **EU AI Act** | European Union regulatory framework for artificial intelligence, designating financial AI as high risk and imposing requirements on transparency, robustness, and oversight | N/A | [Source: EU AI Act, 2024+] |

---

## 12. References

### Tier 1 – Standards, Specifications, and Primary Security Frameworks

1. **NIST**. (2023). *AI Risk Management Framework (AI RMF 1.0)*. National Institute of Standards and Technology. https://www.nist.gov/ai-risk-management  **[Cited in: Context Recap; Sections 3.2, 4.3, 6.1, 10.1, 10.3, 11]**
2. **European Union**. (2024+). *Artificial Intelligence Act* (final text and related guidance). Official Journal of the European Union.  **[Cited in: Context Recap; Sections 3.2, 4.3, 10.1, 11]**
3. **Model Context Protocol Working Group**. (2024+). *Model Context Protocol Specification and Security Best Practices*. https://modelcontextprotocol.io/  **[Cited in: Sections Context Recap, 1.1–1.3, 2.1–2.3, 3.2–3.3, 4.1–4.2, 5.2, 6.1, 7, 10, 11]**
4. **OWASP Foundation**. (2023+). *OWASP LLM Security / OWASP Top 10 for Large Language Model Applications*. https://owasp.org/www-project-top-10-for-large-language-model-applications/  **[Cited in: Sections 1–4, 5.2, 6.1–6.2, 7–8, 10, 11]**

### Tier 2 – Industry Reports, Research Articles, and Technical Blogs

5. **Chainalysis**. (2025-06). *2025 Crypto Crime Mid-Year Update: $2.17 Billion Stolen in First Half of 2025, 59% from Access Control Failures*. Chainalysis Blog. https://www.chainalysis.com/blog/2025-crypto-crime-mid-year-update  **[Cited in: Context Recap; Sections 3.2, 5.1–5.3, 6.1, 10.1, 10.3, 11]**
6. **Safeheron**. (2025-07-15). *How MPC Wallets Are Evolving for Better Security* (AI-powered protection, seedless management, smart recovery). https://safeheron.com/blog/mpc-wallets-2025-security-trends-seedless-ai-recovery  **[Cited in: Context Recap; Sections 1.1–1.2, 2.2, 3.1, 5.1, 6.1, 7, 11]**
7. **Coinbase**. (2025-10). *Coinbase Developer Platform – Launch of Payments MCP with x402 Payment Protocol*. https://www.coinbase.com/developer-platform  **[Cited in: Context Recap; Sections 2.1–2.3, 4.1, 5.2, 11]**
8. **Market: x402 Protocol**. (2025-10). *x402 Payment Protocol Activity Report* (10,000% surge to 500K transactions/week after MCP launch).  **[Cited in: Context Recap; Sections 2.1, 5.2, 11]**
9. **Brave Browser / BraveNewCoin**. (2025). *AI Agents and Crypto Wallets – Understanding the Safety Risks* (prompt injection PoC extracting email OTP). https://bravenewcoin.com/insights/ai-agents-and-crypto-wallets-understanding-the-safety-risks  **[Cited in: Sections 1.1, 2.2–2.3, 4.1–4.2, 5.2, 11]**
10. **Princeton University Researchers**. (2025). *AI Agents Can Be Manipulated into Giving Away Your Crypto* (memory injection attacks in AI agents). Summary: Tom’s Hardware article and linked research. https://www.tomshardware.com/tech-industry/cryptocurrency/ai-agents-can-be-manipulated-into-giving-away-your-crypto-according-to-princeton-researchers  **[Cited in: Sections 1.1, 2.1–2.3, 4.1–4.2, 5.2, 6.2, 11]**
11. **JFrog Security Research**. (2025). *CVE-2025-6515: Prompt Hijacking Attack Affects MCP Ecosystem*. JFrog Blog. https://jfrog.com/blog/mcp-prompt-hijacking-vulnerability  **[Cited in: Sections 1.1, 2.1–2.3, 3.3, 4.1, 5.2]**
12. **SlowMist**. (2025). *Security Analysis of AI Agents and MCP – Data Poisoning, JSON Injection, Function Override, Cross-System Attacks*. SlowMist Security Blog.  **[Cited in: Sections 1.1, 2.1–2.3, 4.1–4.2, 6.2, 11]**
13. **Microsoft**. (2025). *Protecting Against Indirect Prompt Injection Attacks in MCP – AI Prompt Shield and Supply Chain Security*. Microsoft Developer Blog. https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp  **[Cited in: Sections 1.3, 2.3, 4.2, 5.2, 6.1–6.2, 8, 11]**
14. **Webasha**. (2025). *The Role of AI in Cryptocurrency Fraud Detection: Fighting Financial Crimes with Machine Learning*. Webasha Blog. https://www.webasha.com/blog/the-role-of-ai-in-cryptocurrency-fraud-detection-fighting-financial-crimes-with-machine-learning  **[Cited in: Context Recap; Sections 1.1–1.2, 2.2, 3.2, 6.1]**
15. **Unit21**. (2025). *False Positives: Causes, How to Calculate, & How to Reduce*. Unit21 Fraud & AML Dictionary. https://www.unit21.ai/fraud-aml-dictionary/false-positives  **[Cited in: Sections 1.1–1.2, 2.2, 5.1, 6.2, 10.2, 11]**
16. **Industry Analysis**. (2024-Q4). *AI Agent Token Market and Agent Adoption – From <$5B to $15B and 10K to 1M+ Agents*.  **[Cited in: Context Recap; Sections 3.2, 5.1, 11]**
17. **Industry Survey**. (2025-04). *User Willingness to Delegate Portfolio Management to AI Agents*.  **[Cited in: Context Recap; Sections 3.2, 5.1, 11]**

### Tier 3 – Internal Sources and Estimates (Not Formal Citations)

18. **Problem Statement – AI Integration Security Risks in MPC Wallets**. (2025). Internal documentation summarizing brief description, background, constraints, stakeholders, and impact scope.  **[Used in: Context Recap; Sections 1–3, 5–7, 10]**
19. **Estimates and Assumptions on Assets Under Custody and Budgets**. Method: extrapolation from public AUM figures of major custodians and typical security program costs; Confidence: Medium; Validation: refine with provider-specific data and audits.  **[Used in: Context Recap; Sections 1.2, 3.2, 5.1, 6.3, 9]**
