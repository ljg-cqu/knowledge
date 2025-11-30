# Social Recovery and Guardian Trust Assumptions in MPC Wallets – Nine-Aspects Analysis

**Last Updated**: 2025-11-30  
**Status**: Draft  
**Owner**: Security & Product Team

---

## Pre-Section: Context Recap

- **Problem title**: Social recovery and guardian trust assumptions in MPC wallets
- **Current state**:
  - Social recovery wallets and seedless MPC wallets distribute recovery authority across guardian networks, typically requiring an m-of-n threshold of guardians to reconstruct access when a user loses their primary device or signing key. Implementations such as Argent, Loopring, Safe, ZenGo and others combine smart contracts, MPC, and guardian voting to deliver seedless recovery while preserving non-custodial control in normal operation  
    [Source: What is a Social Recovery Wallet?, Gate.com Learn, 2024; Social Recovery Wallets: Can They Solve the Seed Phrase Problem? Complete 2025 Guide, Yellow.com, 2025; ERC-7093: Social Recovery Interface, Ethereum EIP-7093, 2023].
  - Seed-phrase–based self-custody has led to large-scale, irreversible losses: Chainalysis estimated at least 2.3M BTC lost as of 2018, with a further ~1.5M BTC in inactive investment wallets likely lost, consistent with industry estimates that ~20% of BTC supply is permanently inaccessible  
    [Source: Bitcoin’s $30 billion sell-off, Chainalysis, 2018; Social Recovery Wallets Guide, Yellow.com, 2025].
  - Social recovery wallets attempt to fix this by allowing users to regain access via guardians instead of a single seed, but this replaces “single human key management failure” with complex **guardian trust assumptions**, including collusion, coercion, social engineering, and relationship breakdown risks  
    [Source: Gate.com Social Recovery Wallet article, 2024; ERC-7093 Motivation section, 2023; Problem Statement – Social Recovery and Guardian Trust Assumptions, 2025].
- **Pain points**:
  - **Guardian collusion**: A threshold of guardians (e.g., 3-of-5) can legitimately initiate recovery and rotate control to an attacker-controlled key if they collude or are collectively compromised. Once executed, on-chain recovery is indistinguishable from a legitimate operation  
    [Source: ERC-7093: Social Recovery Interface, Security Considerations; Yellow.com Social Recovery Guide, Security Analysis and Threat Modeling, 2025].
  - **Social engineering of guardians**: Guardians are usually non-technical friends, family, or lightly authenticated institutional services. Social engineering statistics show only ~20% of people successfully recognize and report phishing simulations, with median click times of ~21 seconds, indicating high susceptibility to targeted manipulation  
    [Source: 70 Social Engineering Statistics for 2025, Spacelift, 2025].
  - **Coercion and relationship disputes**: Guardians may be coerced (physical threats, legal or social pressure) or fall into conflict with the user (divorce, business disputes, family conflicts), leading either to malicious recovery against user wishes or refusal to participate in legitimate recovery  
    [Estimate based on: Problem Statement – Guardian coercion and dispute scenarios; general coercion patterns in high-net-worth crime cases, Medium confidence].
  - **User mental-model gap**: Users often choose guardians based on personal trust (“people who care about me”) rather than adversarial security properties (collusion risk, geographic and jurisdictional diversity, long-term relationship stability) and rarely understand the effective power they are delegating  
    [Source: Problem Statement – User Security Awareness; Yellow.com Social Recovery Guide, User Experience sections, 2025].
- **Goals**:
  - Reduce unauthorized recovery events caused by guardian collusion, social engineering, or coercion to **<10% (min) / <5% (target) / <1% (ideal)** of all recovery incidents by 2027 across major providers  
    [Source: Problem Statement – Goals and success criteria].
  - Increase proportion of social recovery implementations that **cannot be compromised solely by a colluding personal-guardian majority** (e.g., require at least one institutional or hardware-based guardian, or independent policy verifier) to **≥50% (min) / ≥70% (target) / ≥90% (ideal)** by Q4 2026  
    [Source: Problem Statement – Goals and success criteria; ERC-7093 Motivation].
  - Achieve **≥60% (min) / ≥80% (target) / ≥90% (ideal)** of designated guardians completing basic security training (verification procedures, phishing detection, coercion-handling playbooks) by Q4 2027  
    [Source: Problem Statement – Guardian security education goals].
  - Implement adaptive time-locks and multi-channel notification such that **≥95%** of high-value unauthorized recovery attempts are detected and cancelled before completion  
    [Source: Problem Statement – Time-lock effectiveness; Yellow.com Social Recovery Guide, Security Patterns, 2025].
- **Hard constraints**:
  - 24‑month improvement window (Q1 2026–Q4 2027) for major upgrades across guardian authentication, training, and policy frameworks, with per-provider budgets of roughly **USD 300k–1M** and limited UX headroom for added friction  
    [Source: Problem Statement – Key constraints and resources].
  - Non-custodial positioning must be preserved for many MPC wallets; excessive centralization of guardianship in a single institution or provider may trigger regulatory “custody” classification  
    [Estimate based on: global custody regulations and industry interpretations, Medium confidence].
  - Guardian participation is voluntary and largely uncompensated for personal guardians, so complex hardware requirements or heavy KYC flows may significantly reduce willingness to serve as guardians  
    [Source: Problem Statement – Trust model trade-offs; 70 Social Engineering Statistics, Spacelift 2025 (user behavior under friction)].
- **Key facts**:
  - At least **2.3M BTC** are lost, with another ~1.5M BTC likely lost in inactive investment wallets, supporting the narrative that seed-phrase–only models generate enormous, permanent losses  
    [Source: Bitcoin’s $30 billion sell-off, Chainalysis, 2018].
  - Social recovery wallets shift risk from “single human mistake” to **multi-guardian coordination and verification**, relying on guardians to correctly authenticate the user, review recovery requests, and resist manipulation  
    [Source: ERC-7093 Abstract and Motivation; Gate.com Social Recovery Wallet article, 2024].
  - Social engineering–driven breaches are common: human error and social engineering contributed to ~68% of breaches in 2024, and only ~20% of users pass phishing simulations without error, indicating a high baseline susceptibility that will also affect guardians  
    [Source: 70 Social Engineering Statistics for 2025, Spacelift, citing APWG/FBI/industry data].

---

## 1. Problem Definition (Aspect 1)

### 1.1 Problem and contradictions

1. **Core problem**  
   MPC-based social recovery wallets rely on guardian networks to safely restore access when users lose devices or keys, but the same mechanisms can be abused when guardians collude, are socially engineered, coerced, or become hostile, enabling unauthorized key rotation that is indistinguishable from legitimate recovery on-chain  
   [Source: ERC-7093: Social Recovery Interface, Security Considerations; Gate.com Social Recovery Wallet article, 2024; Yellow.com Social Recovery Guide, Threat Modeling, 2025].

2. **Key contradictions**
   - **Usability vs. adversarial trust design**: Social recovery is marketed as “just choose people you trust”, yet robust security requires modeling guardians as potential adversaries subject to coercion, phishing, and life events; these mindsets conflict for mainstream users  
     [Source: Yellow.com Social Recovery Guide, User Experience; 70 Social Engineering Statistics, Spacelift 2025].
   - **Decentralization vs. institutional guardians**: Relying only on personal guardians risks collusion and social engineering; adding institutional guardians (wallet provider, email provider, custody partner) raises centralization and regulatory-custody concerns  
     [Source: ERC-7093 Motivation; Problem Statement – Trust model trade-offs].
   - **Recovery reliability vs. collusion resistance**: High thresholds and diverse guardians reduce collusion but increase the probability that legitimate recovery fails (unreachable guardians, relationship breakdowns, death), particularly over multi-year horizons  
     [Estimate based on: typical guardian set size and relationship volatility, Medium confidence].

3. **Who is in conflict?**
   - End users who want simple, low-friction recovery and who mentally equate “trust” with personal closeness rather than security properties.
   - Guardians (friends, family, institutions) who gain high-stakes recovery power without compensation or professional security training.
   - Wallet providers seeking strong security and differentiation via UX, but constrained by budgets, regulatory uncertainty, and the risk that additional friction harms adoption  
     [Source: Problem Statement – Stakeholders and roles].

### 1.2 Goals and conditions

- **Security goal**: Ensure that **guardian networks cannot be cheaply exploited** for unauthorized recovery, such that successful guardian-driven theft requires either highly improbable collusion across independent trust domains or extreme coercion scenarios, not routine phishing or casual manipulation.
- **Reliability goal**: Maintain or improve successful legitimate recovery rates compared with today’s social recovery implementations (>95% recovery success within configured time windows) while adding stronger guarantees against unauthorized access  
  [Estimate based on: current social recovery UX patterns in Argent/Loopring, Yellow.com Guide, Medium confidence].
- **Governance goal**: Standardize guardian selection guidelines, verification procedures, and legal obligations (e.g., fiduciary duty for institutional guardians) across major providers to reduce inconsistent, fragile trust models  
  [Source: ERC-7093 Motivation; Problem Statement – Legal framework goals].
- **Measurement conditions**: Track unauthorized recovery incidents, guardian participation/attrition rates, and user comprehension of trust models via in-app quizzes and incident reports; design metrics that respect privacy but still surface systemic risk trends  
  [Source: Problem Statement – Goals & success criteria].

### 1.3 Extensibility and reframing

- **Attribute reframing – “one object, many attributes”**:  
  The object is the **guardian network + policy**, with attributes including number of guardians, diversity across social circles and institutions, authentication strength, time-locks, dispute mechanisms, and legal commitments. An explicit attribute view reveals that “friends only” guardianship and “friends + institution + hardware” guardianship are fundamentally different trust models.
- **Structure reframing – personal vs. institutional, on-chain vs. off-chain**:  
  Guardian authority can be implemented via smart contracts (ERC-7093 style policies), off-chain MPC services, or hybrid combinations. Thinking in terms of **trust domains** (household, workplace, bank, wallet provider, jurisdiction) helps designers reason about correlated failures and collusion risks  
  [Source: ERC-7093 Abstract and Recovery Account Workflow; Yellow.com Guide, Technical Architecture, 2025].
- **Risk reframing – from “guardian failure” to “guardian system design”**:  
  Rather than focusing on whether a specific guardian is trustworthy, the problem becomes **designing a guardian system where any realistic subset of compromised guardians still cannot bypass time-locks, detection, and dispute processes**. This shifts emphasis from personal judgment to protocol-enforced constraints and verifiable policies.

---

## 2. Internal Logical Relations (Aspect 2)

### 2.1 Key elements

- **Users and primary signing keys**: Users hold a primary signing key (locally or via MPC), used for day-to-day transactions. Recovery changes which key is recognized as valid by the wallet smart contract or MPC coordinator  
  [Source: Gate.com Social Recovery Wallet article, 2024; Yellow.com Guide, How Social Recovery Works, 2025].
- **Guardians and guardian categories**: Guardians may be other user devices, personal contacts, institutions, or smart-contract–based entities like NFTs/SBTs, each with different authentication capabilities and failure modes  
  [Source: ERC-7093 Motivation; ERC-7093 DataTypes and Interfaces].
- **Recovery policies and thresholds**: Policies describe which guardians, in what combinations and with what thresholds and lock periods, may authorize recovery. ERC-7093 explicitly separates policy verification from the core account contract so policies can evolve independently  
  [Source: ERC-7093 Abstract and Specification].
- **Time-locks and notifications**: Time delays (24h–7d) and multi-channel notifications (email, app push, SMS, on-chain events) provide a window for users to detect and cancel unauthorized recovery attempts before assets are drained  
  [Source: Yellow.com Social Recovery Guide, Security Patterns; Problem Statement – Time-lock standards].
- **Guardian verification and UX surfaces**: Guardians interact via email links, app approvals, hardware keys, or video calls. These UX paths are primary attack surfaces for phishing, smishing, vishing, and pretexting  
  [Source: 70 Social Engineering Statistics for 2025, Spacelift; Gate.com Social Recovery article].

### 2.2 Balance and “degree” issues

- **Threshold vs. availability**: Higher thresholds (e.g., 4-of-7) reduce the chance that a small colluding clique can steal funds but increase the chance that legitimate recovery fails because one or more guardians are unavailable or unwilling. Lower thresholds (e.g., 2-of-3) are more usable but fragile in the face of collusion  
  [Estimate based on: threshold cryptography properties and social recovery architectures, Medium confidence].
- **Guardian diversity vs. mental overhead**: Encouraging users to select guardians across families, geographies, and institutions improves collusion resistance, but users may find it harder to explain the scheme and coordinate in emergencies.
- **Verification strength vs. friction**: Using strong multi-factor verification (FIDO keys, biometrics, video calls) for guardians materially reduces social engineering success probability, but each added step risks guardian drop-off or delayed response  
  [Source: ERC-7093 Motivation (customizable verification); 70 Social Engineering Statistics, Spacelift 2025].
- **Time-lock duration vs. user impatience**: Longer time-locks improve detection probability for unauthorized recovery but feel slow and frustrating for legitimate recovery, pushing users toward custodial alternatives or unsafe hacks (e.g., bypassing time-locks via privileged upgrade paths).

### 2.3 Causal chains

1. **Phishing-driven unauthorized recovery chain**  
   Weak guardian verification (email-only links, no secondary factor) → attacker sends highly targeted phishing emails/SMS to guardians claiming urgent recovery for the user → majority of guardians approve without independent voice/video verification → time-lock is short (24h) and user is offline → attacker rotates key and drains funds  
   [Source: 70 Social Engineering Statistics, Spacelift 2025 (low simulation success rates, high phishing prevalence); Yellow.com Social Recovery Guide, Social Engineering Risks].

2. **Relationship breakdown and collusion chain**  
   Guardians are selected purely from close social circle (spouse, business partner, co-founder) → relationship deteriorates (divorce, business dispute) → colluding guardians initiate recovery to lock out user or seize control during conflict → user struggles to contest, as on-chain event appears indistinguishable from authorized recovery without extra dispute mechanisms  
   [Estimate based on: typical social recovery guardian patterns and divorce/business dispute statistics; Problem Statement – Guardianship disputes].

3. **Over-centralization chain**  
   Provider offers “default guardianship” where provider-controlled keys or email providers act as majority guardians for convenience → over time, large share of user base adopts default, de facto centralizing recovery power in a single or small set of institutions → compromise, regulatory action, or policy change at those institutions now affects millions of wallets simultaneously  
   [Source: ERC-7093 Motivation (multiple guardian types, avoid single points of failure); Yellow.com Guide, Market Landscape and Adoption].

---

## 3. External Connections (Aspect 3)

### 3.1 Stakeholders and conflicts

| Stakeholder Type | Role | Goals | Constraints | Conflicts |
|------------------|------|-------|------------|-----------|
| Upstream | Standard bodies (EIP authors), wallet protocol designers, MPC vendors | Define robust, flexible recovery standards and reference implementations | Limited control over individual app UX; must balance generality with simplicity | May design secure but complex patterns that product teams resist adopting |
| Downstream | Wallet providers, dApp developers, custodians | Deliver seedless UX, minimize account loss, differentiate via safety | Budget, roadmap pressure, performance limits, regulatory ambiguity | Tension between adding friction (security) vs. conversion/retention (growth) |
| Sideline / External | End users, guardians, regulators, consumer advocates, insurers | Safety, recoverability, clear accountability, fair distribution of liability | Low technical knowledge (users/guardians), slow regulatory cycles, incomplete data | Regulators may push for institutional guardians and liability, while users demand decentralization and privacy |

[Source: ERC-7093 Motivation; Yellow.com Social Recovery Guide – Market and Stakeholders; Problem Statement – Stakeholders and roles].

### 3.2 Environmental factors

- **Macro social engineering environment**: Social engineering incidents (phishing, smishing, pretexting, BEC) continue to grow, with ~94% of businesses experiencing phishing attacks in 2024 and many users failing simulated tests  
  [Source: 70 Social Engineering Statistics for 2025, Spacelift].
- **Regulatory and legal landscape**: Jurisdictions differ on whether social-recovery providers and institutional guardians are “custodians” with fiduciary duties; absence of clear guardianship law leaves ambiguity about liability for negligent approvals or refusal to assist in legitimate recovery  
  [Source: Problem Statement – Legal & Regulatory; ERC-7093 Motivation].
- **Competing custody models**: Hardware wallets, multi-sig, and account-abstraction–based smart contract wallets compete with social recovery by offering alternative recovery and trust models; high-profile failures in one model (e.g., guardian collusion) may shift user demand toward others.

### 3.3 Responsibility and room for maneuver

- **Standard authors and protocol designers** should clearly specify **non-negotiable trust and verification assumptions**, sample policies for heterogeneous guardians, and recommended defaults for thresholds and time-locks  
  [Source: ERC-7093 Abstract and Specification].
- **Wallet providers** must:
  - Implement secure default guardian policies rather than shifting full burden to users.
  - Provide opinionated guardian selection guidance (e.g., no more than one guardian from same household; require at least one institution or hardware key for high-value wallets).
  - Invest in guardian training and secure verification flows.
- **Guardians and institutions** need clear role definitions, procedures for verifying identity, and clarity on potential liability and escalation paths.
- **Regulators and consumer advocates** can set baseline obligations (e.g., disclosure of guardian power, required time-locks above certain balances) without unduly constraining innovation  
  [Estimate based on: analogous financial custody and consumer-protection regimes, Medium confidence].

---

## 4. Origins of the Problem (Aspect 4)

### 4.1 Historical nodes

1. **Pre-social recovery era – Seed phrases as default (2013–2018)**:  
   BIP39 mnemonics and single-key wallets dominate self-custody, leading to large-scale losses when users mismanage or lose seed phrases  
   [Source: Bitcoin’s $30 billion sell-off, Chainalysis 2018; Yellow.com Social Recovery Guide – Seed Phrase Catastrophe, 2025].
2. **Conceptualization of social recovery (2019–2021)**:  
   Vitalik Buterin and others propose social recovery as a way to retain non-custodial control while adding a human safety net via guardians, emphasizing that users’ social graphs can act as a distributed trust layer  
   [Source: Gate.com Social Recovery Wallet article, citing Buterin’s 2019–2021 writings].
3. **Early implementations (Argent, Loopring, Safe, 2018–2023)**:  
   Wallets like Argent and Loopring deploy social recovery smart contracts with guardians and time-locks; Safe (Gnosis Safe) adds flexible recovery modules and multi-sig architectures that can emulate social recovery  
   [Source: Gate.com Social Recovery Wallet article, Examples section; Yellow.com Guide – Real-world Implementations].
4. **Standardization attempts (2022–2024)**:  
   ERC-7093 is proposed as a standardized social recovery interface, separating identity/policy verification from recovery logic to support heterogeneous guardians and customizable recovery policies  
   [Source: ERC-7093: Social Recovery Interface, 2023].
5. **Scaling to tens of millions of users (2023–2025)**:  
   Seedless MPC wallets and Web2-style login providers adopt social-recovery-like architectures for mainstream users, expanding risk from niche Ethereum smart contract wallets to a broad retail population  
   [Source: Yellow.com Social Recovery Guide – Market Landscape; Problem Statement – Adoption data].

### 4.2 Background vs. direct causes

- **Background structural causes**:
  - Human cognitive limits make long-term, high-entropy secret management (seed phrases) unrealistic for mainstream users; industry responded by layering social trust but often without a rigorous adversarial model  
    [Source: Yellow.com Guide – Seed Phrase Catastrophe; usability and security research summarized therein].
  - Incentives to minimize support load and account-loss tickets pushed providers toward simple “choose your guardians” flows with limited education, underweighting complex guardian dynamics.

- **Direct causes of current trust-assumption risk**:
  - Guardian policies that allow unvetted personal guardians to form a threshold majority without additional safeguards (e.g., missing institutional or hardware guardians, no minimum diversity requirements).
  - Guardian verification flows that rely on weak channels (email-only approvals) with no secondary confirmation or out-of-band checks, making phishing straightforward  
    [Source: 70 Social Engineering Statistics, Spacelift 2025].
  - Lack of legal and contractual clarity for institutional guardians, resulting in ambiguous obligations and inconsistent enforcement when things go wrong  
    [Source: Problem Statement – Legal framework and uncertainties].

### 4.3 Root issues

- **Misaligned mental models**: Marketing frames guardianship in terms of “people you trust” rather than “adversaries you must defend against”, leading users to systematically underappreciate collusion and social engineering risks.
- **Insufficient standardization**: Without widely adopted standards and certification for guardian policies and verification procedures, each provider improvises, creating a patchwork of incompatible and sometimes fragile trust models  
  [Source: ERC-7093 Motivation; Problem Statement – Implementation heterogeneity].
- **Invisible risk and under-reporting**: Unauthorized recoveries may appear on-chain as legitimate events; unless victims publicize incidents and providers instrument detection, systemic guardian risk remains under-appreciated.

---

## 5. Problem Trends (Aspect 5)

### 5.1 Current trajectory (if nothing changes)

- As social recovery and seedless MPC wallets expand to tens of millions of users, **the total guardian attack surface (hundreds of millions of designated guardians)** grows rapidly, providing enticing opportunities for targeted phishing and coercion  
  [Source: Problem Statement – Guardian counts; 70 Social Engineering Statistics, Spacelift 2025].
- Seed-phrase–only models will likely continue to generate large, irreversible losses, keeping industry pressure high to adopt social recovery; however, naive guardian models will convert some of this risk from **loss due to forgetfulness** into **loss due to manipulated recovery**.
- If providers do not standardize stronger defaults (diverse guardians, time-locks, multi-factor verification), early high-profile guardian collusion or social-engineering incidents could severely damage user trust in social recovery and push regulation toward heavy-handed custodial models  
  [Estimate based on: prior reactions to major exchange and wallet breaches, Medium confidence].

### 5.2 Early signals

- Documentation and blog posts from wallets increasingly highlight guardian selection and time-locks, but still provide limited, non-quantitative guidance on collusion risk.
- Security and research articles discuss **social recovery threat modeling** as an open issue, identifying guardian collusion and social engineering as main concerns  
  [Source: Yellow.com Social Recovery Guide – Security Analysis and Threat Modeling, 2025].
- Social engineering statistics show persistent and growing susceptibility despite training, indicating that guardian phishing is likely to be effective without significant hardening  
  [Source: 70 Social Engineering Statistics for 2025, Spacelift].

### 5.3 Scenarios (6–24 months)

- **Optimistic scenario**:  
  ERC-7093-aligned standards and best practices crystallize; major MPC and smart contract wallet providers adopt **opinionated guardian policies** (heterogeneous guardian sets, strong MFA, meaningful time-locks). Industry launches guardian training modules and transparent incident reporting. Unauthorized guardian-driven recoveries become rare edge cases.

- **Baseline scenario**:  
  Top-tier providers invest heavily in guardian security, but many mid-tier or long-tail wallets implement only partial measures (e.g., time-locks but weak guardian verification). Occasional guardian-driven thefts occur, sometimes high-profile, but overall social recovery remains net better than seed-phrase–only models.

- **Pessimistic scenario**:  
  Attackers weaponize phishing and pretexting against guardian networks, organizing campaigns targeting guardians of high-value accounts. One or more large social-recovery providers suffer multi-million-dollar losses through guardian collusion or mass phishing. Regulatory backlash pushes for centralized, institution-only guardianship or stricter custodial licensing, undermining decentralized recovery goals.

[Scenarios estimated based on: adoption curves for prior wallet technologies, regulator responses to security incidents, and current trajectory of social engineering attacks, Medium confidence].

---

## 6. Capability Reserves (Aspect 6)

### 6.1 Existing strengths

- **Technical foundations and standards**: ERC-7093 already defines interfaces for heterogeneous guardians and recovery policies, enabling more robust architectures without re-deploying accounts  
  [Source: ERC-7093: Social Recovery Interface, 2023].
- **Ecosystem experience with security UX**: Many wallet teams have experience implementing multi-factor auth, phishing-resistant sign-in flows, and time-based transaction delays for DeFi and custody use cases that can be repurposed for guardian verification.
- **Market incentives**: Preventing catastrophic recovery misuse is in providers’ direct interest—stronger guardian models become a competitive differentiator for institutional and high-net-worth clients  
  [Source: Yellow.com Social Recovery Guide – Market Outlook, 2025].

### 6.2 Capability gaps

- **Guardian education and tooling**: There is limited off-the-shelf content and UX tooling for training non-technical guardians on how to verify recovery requests and respond to suspected coercion or phishing.
- **Data and analytics**: Few providers publicly share statistics on recovery attempts, guardian response times, or suspected unauthorized recoveries, making it difficult to benchmark guardian risk or calibrate time-locks and verification strength  
  [Source: Problem Statement – Uncertainties and information gaps].
- **Legal frameworks and contracts**: Institutional guardianship lacks standardized contractual templates and clear liability allocation for negligent approvals, making institutions wary of deeper involvement.

### 6.3 Buildable capabilities (1–6 months)

- Implement standardized **guardian verification flows** using phishing-resistant MFA, signed messages, or video verification templates, with clear copy and checklists for guardians.
- Add recovery **telemetry and alerts**: tagging recovery attempts with context (IP, device, risk score), logging guardian responses, and surfacing anomalies for security review.
- Develop **guardian playbooks**: simple guides for “how to verify a recovery request”, “what to do if you suspect coercion”, and “when to refuse” that can be embedded directly in guardian UX  
  [Estimate based on: typical product/security engineering timelines for UX, training content, and analytics, Medium confidence].

---

## 7. Analysis Outline (Aspect 7)

### 7.1 Structured outline

- **Background**: Seed phrase usability failures and large-scale coin losses drive adoption of social recovery wallets and seedless MPC models.
- **Problem**: Guardian networks, if naively designed and operated, introduce new systemic trust assumptions—collusion, social engineering, coercion, and disputes—that can compromise assets despite cryptographic distribution.
- **Analysis**: Internal trust structure, external stakeholders, historical evolution, and trend scenarios all point to guardian design as a central security bottleneck.
- **Options**: Hardening guardian policies (diversity, thresholds), strengthening verification and time-locks, adding institutional and hardware guardians, and standardizing training and legal frameworks.
- **Risks**: User friction, guardian attrition, regulatory overreach, and residual edge-case vulnerabilities.

### 7.2 Key judgments (for validation)

1. Guardian-based recovery can remain **net safer** than seed-phrase–only self-custody if guardian trust models are systematically hardened; otherwise, risk merely shifts rather than decreases.
2. Stronger defaults—diversified guardians, meaningful time-locks, MFA-based verification—can substantially reduce unauthorized recovery risk **without collapsing adoption**, if designed and communicated well.
3. Legal and contractual frameworks for institutional guardians will be necessary to unlock broader use of institutions as robust, accountable guardians for higher-value wallets.

### 7.3 Alternative high-level paths

- **Path A – Opinionated, high-assurance defaults**: Provider ships strong guardian defaults (diversity rules, minimum time-locks, MFA) with limited user override, prioritizing safety.
- **Path B – Flexible but guided configuration**: Provider exposes configuration knobs but embeds strong recommendations, risk scores, and warnings, allowing advanced users to deviate.
- **Path C – Segmented architectures**: High-value or institutional users receive stricter guardian regimes (institutional + hardware guardians, stronger legal contracts), while low-value wallets accept slightly higher risk with simpler setups.

---

## 8. Validating the Answer (Aspect 8)

### 8.1 Potential biases and blind spots

- **Security-centric bias**: Analysis may overweight security at the expense of UX and growth, underestimating how quickly users abandon overly complex flows.
- **Data sparsity**: There is limited public incident data specifically about guardian misuse, so risk estimations may lean heavily on analogies from general social engineering statistics  
  [Source: 70 Social Engineering Statistics for 2025, Spacelift].
- **Western-centric regulatory assumptions**: Legal discussions may overfit to US/EU frameworks and not reflect conditions in emerging markets where many new crypto users reside.

### 8.2 Required intelligence

- Provider-level statistics on:
  - Number and composition of guardian sets (personal vs. institutional vs. hardware).
  - Recovery initiation rates, success rates, and suspected unauthorized recoveries.
  - Guardian response times and dropout rates over multi-year periods.
- User research on how people actually choose guardians and how well they understand guardian power and responsibilities.
- Legal analyses in key jurisdictions on whether and when social-recovery guardianship constitutes “custody” or fiduciary duty.

### 8.3 Validation plan

- **Data collection**: Implement anonymous, privacy-preserving logging of recovery attempts and guardian actions; publish aggregate statistics annually for industry benchmarking.
- **User studies**: Run structured interviews and surveys where participants configure guardian sets and explain choices; test comprehension with scenario-based quizzes before enabling dangerous configurations.
- **Red-team exercises**: Conduct controlled phishing and pretexting exercises targeting internal test guardian networks to measure success rates and stress-test verification flows  
  [Based on: established security awareness and phishing simulation practices summarized in Spacelift social engineering statistics, 2025].

---

## 9. Revising the Answer (Aspect 9)

### 9.1 Likely revisions

- Quantitative risk estimates (e.g., probability of unauthorized recovery per year for a given guardian configuration) will change as better telemetry and incident reports accumulate.
- Preferred guardian patterns may evolve as new guardian types (e.g., SBTs, community DAOs, insurer-backed guardians) emerge under ERC-7093-compatible interfaces  
  [Source: ERC-7093 Motivation].
- Regulatory expectations could shift, requiring stronger institutional involvement or explicit liability protections that change the optimal mix of guardians.

### 9.2 Incremental approach

- Start with **low-regret hardening**: improve guardian verification (MFA, clearer instructions), introduce or lengthen time-locks where feasible, and add richer recovery notifications.
- Gradually **tighten guardian policies**: add diversity requirements and risk scoring; gently migrate existing users to safer configurations during re-activation or major app updates.
- **Pilot segmented models**: test stricter guardian policies and legal frameworks with a subset of high-value users and institutions before broader rollout.

### 9.3 “Good enough” criteria

- Default guardian configurations for new wallets meet minimal safety thresholds (e.g., no single social circle can unilaterally recover; meaningful time-locks for balances above specified thresholds).
- Unauthorized guardian-driven recovery incidents are **rare, well-documented, and containable** rather than systemic.
- Providers can explain and defend their guardian trust assumptions to regulators, partners, and sophisticated users with clear documentation and metrics.

---

## 10. Summary & Action Recommendations (Aspect 10)

### 10.1 Core insights

1. Social recovery meaningfully addresses the seed-phrase catastrophe, but naive guardian trust assumptions can recreate catastrophic risk in a new form—through guardian collusion, coercion, and social engineering  
   [Source: Yellow.com Social Recovery Guide – Seed Phrase Catastrophe & Security Analysis, 2025; 70 Social Engineering Statistics, Spacelift 2025].
2. The core design task is not just **“who do you trust?”** but **“how do we design a guardian system that is robust to partial compromise and human weakness?”**, using diverse guardians, strong verification, and time-locks  
   [Source: ERC-7093 Motivation; Problem Statement – Trust model trade-offs].
3. With opinionated defaults, better guardian UX, and clearer legal frameworks, social recovery and MPC wallets can deliver substantially lower net risk than seed-phrase–only self-custody for mainstream users.

### 10.2 Near-term action list (0–3 months)

Format: **[Priority] Action → Owner → Metric → Date**

- **【P0 – Critical】**
  1. Define and implement **safe default guardian policy** for new wallets (minimum diversity, thresholds, time-locks) → Product & Security Leads → Coverage: 0% → 100% of new wallets using safe defaults → 2026-03-31.
  2. Ship **guardian verification hardening** (MFA, explicit in-app instructions, warning banners) for all recovery flows → Wallet Engineering → Weak verification flows: >0 → 0 flows without MFA or equivalent → 2026-04-30.

- **【P1 – Important】**
  3. Launch **guardian education module** (short interactive guide and checklist) delivered when guardians are first enrolled and during recovery attempts → UX & Education → Guardian training completion: <5% → ≥60% for new guardians → 2026-06-30.
  4. Implement **enhanced recovery telemetry & alerting** (risk scoring, anomaly detection on recovery attempts) → Security Engineering → Recovery attempts with risk scoring: 0% → ≥80% → 2026-06-30.

- **【P2 – Optional】**
  5. Design and pilot **institutional guardian program** with clear contracts and liability allocations for high-value users → Biz Dev & Legal → Institutional guardian coverage: baseline → pilot with ≥3 partners → 2026-09-30.

### 10.3 Risks & mitigation

| Risk | Impact | Probability | Trigger Condition | Mitigation | Owner |
|------|--------|-------------|-------------------|-----------|-------|
| Added friction reduces guardian participation or slows legitimate recovery | Medium–High | Medium | Guardian response times increase; users report failed recoveries | Optimize flows, provide clear explanations, allow “lighter” configs for low-value wallets while keeping high-value strong | Product Lead |
| Misconfigured policies or bugs lock users out permanently | High | Low–Medium | Spike in failed recoveries or support tickets after policy changes | Stage rollouts, back up policy configs, offer break-glass institutional assistance for critical cases | Engineering Lead |
| Over-centralization in institutional guardians creates new systemic risk | High | Medium | Large share of wallets use same institution as majority guardian | Enforce diversity constraints, cap institutional share of guardian power, support multi-institution models | Architecture Lead |

### 10.4 Alternative paths comparison

| Option | Benefits | Costs | Risks | Best When | Avoid When |
|--------|----------|-------|-------|-----------|------------|
| **A: Strong opinionated defaults (provider-curated guardian sets & policies)** | Maximum risk reduction; consistent safety across user base; easier to reason about | Less user flexibility; may not fit all social contexts; higher design burden | Users circumvent system (e.g., move funds) if they feel over-constrained | Mass-market retail users with low security expertise | Power users and institutions needing bespoke setups |
| **B: Flexible configuration + guided risk scoring** | Adapts to many contexts; empowers advanced users; can be delivered incrementally | More complex UX; risk that users ignore warnings; harder to audit systemwide risk | High-risk users may pick unsafe configs; inconsistent risk levels | Mixed user base with some advanced self-custody users | Very low-literacy markets, or when regulatory pressure demands consistent minimum controls |
| **C: Tiered guardian regimes by account value/segment** | Aligns security effort with value at risk; lets small accounts stay simple | Requires segmentation logic and value thresholds; may confuse users if messaging unclear | Misclassification or abrupt value changes can leave some high-value accounts under-protected | Providers with robust analytics and KYC/segmentation capabilities | Very small providers lacking resources for segmentation and monitoring |

---

## 11. Glossary

| Term | Definition | Unit/Range | Source/Context |
|------|-----------|-----------|----------------|
| **Social recovery wallet** | A wallet where users can recover access by coordinating a set of guardians who authorize changing the signing key, typically via smart contracts or MPC-backed logic | N/A | [Source: What is a Social Recovery Wallet?, Gate.com, 2024] |
| **Guardian** | A person, device, institution, or contract that holds recovery authority for a social recovery wallet, often participating by signing recovery messages or approvals | N/A | [Source: ERC-7093: Social Recovery Interface, 2023] |
| **Guardian collusion** | Scenario where enough guardians to meet the recovery threshold coordinate (or are jointly compromised) to perform unauthorized recovery and seize account control | N/A | [Source: Yellow.com Social Recovery Guide – Threat Modeling, 2025] |
| **Seed phrase** | A 12–24 word mnemonic encoding a wallet’s master private key; loss or exposure typically results in irreversible loss or theft of funds | N/A | [Source: Bitcoin’s $30 billion sell-off, Chainalysis 2018; Yellow.com Guide, 2025] |
| **MPC wallet** | Wallet architecture where private keys are split into multiple shares across devices/parties, and signing is done via multi-party computation without reconstructing the key in one place | N/A | [Source: Yellow.com Social Recovery Guide – Technical Architecture, 2025] |
| **ERC-7093** | Ethereum standard specifying interfaces for social recovery accounts, including guardians, policy verifiers, and recovery account workflows | N/A | [Source: ERC-7093: Social Recovery Interface, Ethereum EIPs, 2023] |
| **Time-lock** | A mandatory waiting period between initiating and executing a sensitive action (like recovery), designed to provide a detection and cancellation window | Hours/days | [Source: Yellow.com Guide – Security Patterns, 2025] |
| **Recovery policy** | A structured description of which guardians, thresholds, and conditions must be satisfied to authorize recovery, often encoded in smart contract or off-chain logic | N/A | [Source: ERC-7093 Specification, 2023] |
| **Social engineering** | A category of attacks (phishing, smishing, vishing, pretexting, BEC) that exploit human behavior to trick victims into performing insecure actions or revealing secrets | N/A | [Source: 70 Social Engineering Statistics for 2025, Spacelift] |
| **Pretexting** | Social engineering technique where attackers fabricate a story or identity to convince victims to provide sensitive information or approvals, often used in high-value targeted attacks | N/A | [Source: 70 Social Engineering Statistics for 2025, Spacelift] |

---

## 12. References

### Tier 1 – Standards and Primary Technical Specifications

1. **Ethereum EIP Editors & Contributors.** (2023). *ERC-7093: Social Recovery Interface*. Ethereum Improvement Proposal 7093. https://eips.ethereum.org/EIPS/eip-7093  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 6, 7, 9, 10, 11 **]**

### Tier 2 – Industry Reports, Guides, and Data

2. **Chainalysis.** (2018). *Bitcoin’s $30 billion sell-off*. Chainalysis Blog. https://www.chainalysis.com/blog/money-supply/  
   **[Cited in**: Context Recap; Sections 2, 4, 5, 11 **]**
3. **Gate.com Research Team.** (2024). *What is a Social Recovery Wallet?* Gate Learn. https://www.gate.com/learn/articles/what-is-a-social-recovery-wallet/676  
   **[Cited in**: Context Recap; Sections 1–3, 4, 11 **]**
4. **Yellow.com Editorial Team.** (2025). *Social Recovery Wallets: Can They Solve the Seed Phrase Problem? Complete 2025 Guide*. Yellow.com. https://yellow.com/learn/social-recovery-wallets-can-they-solve-the-seed-phrase-problem-complete-2025-guide  
   **[Cited in**: Context Recap; Sections 1–5, 6, 7, 10, 11 **]**
5. **Spacelift.** (2025). *70 Social Engineering Statistics for 2025*. Spacelift Blog. https://spacelift.io/blog/social-engineering-statistics  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 6, 8, 10, 11 **]**

### Internal & Problem-Specific Sources

6. **Problem Statement – Social Recovery and Guardian Trust Assumptions in MPC Wallets.** (2025). Internal documentation, Knowledge Repository.  
   **[Cited in**: Context Recap; Sections 1–3, 4, 5, 6, 7, 10 **]**

### Estimates & Assumptions (Not Formal Citations)

7. **Guardian relationship stability and collusion risk estimates.** Method: qualitative reasoning based on typical guardian compositions (friends, family, colleagues) and general divorce/business dispute statistics. Confidence: Medium. Validation: to be refined via provider telemetry and sociological data.  
   **[Used in**: Sections 1.1, 2.2, 2.3, 4.2, 5.3 **]**
8. **Regulatory treatment of guardianship and custody.** Method: analogy to traditional financial custody and fiduciary regimes in US/EU; extrapolation to crypto social-recovery context. Confidence: Low–Medium. Validation: dedicated legal analysis per jurisdiction.  
   **[Used in**: Sections 3.2, 3.3, 4.2, 5.3, 9.1 **]**
