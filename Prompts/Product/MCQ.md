# MCQ – Product Manager

Generate senior/director/VP PM multiple-choice assessments.

---

# Specifications

## Task Definition

**Scope**: 40–80 MCQs; 20/40/40 difficulty split (Foundational/Intermediate/Advanced); ~60% EN, ~30% ZH, ~10% other sources.

**Constraints**: Product management domain (strategy, discovery, metrics, execution, leadership); 1–2 sentence stems; 4 options (1 correct, 3 plausible distractors using misconceptions/outdated practices/competing frameworks); single-select; machine-gradable; no partial credit; no vendor bias.

**Coverage**: MECE clusters across Strategy | Discovery | Prioritization | Metrics | Stakeholder | Go-to-Market. Each cluster: frameworks, metrics, trade-offs, best practices. Advanced items: rationale with edge cases, alternatives.

## Quality Requirements

**Reference Floors**: Glossary ≥10, Tools ≥5, Literature ≥6, Citations ≥12 (APA 7th + language tags [EN]/[ZH])

**Quality Gates**:
- **Recency**: ≥50% last 3yr (≥70% AI/platform)
- **Diversity**: ≥3 source types; single <25%
- **Evidence**: ≥70% MCQs cite ≥1 source; ≥30% cite ≥2
- **Links**: All accessible/archived (prefer DOI)
- **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
- **Significance**: High-value questions only; exclude trivial
- **Concision**: Stems 1–2 sentences; rationales 1–2 sentences
- **Logic**: Rationales = justify correct + refute key distractor
- **Risk/Value**: Advanced items include trade-offs where applicable
- **Fairness**: Acknowledge competing frameworks/assumptions

**Tool Details**: Pricing, users, update ≤18mo, integrations

## Validation

Run all checks; fix failures; re-run until all PASS.

| Check | Requirement | Format |
|-------|------------|--------|
| Floors | G≥10, T≥5, L≥6, A≥12, MCQs 40–80 (20/40/40) | G:X T:Y L:Z A:W Q:N (F/I/A) |
| Citations | ≥70% MCQs ≥1 cite; ≥30% ≥2 cites | X% ≥1, Y% ≥2 |
| Language | EN 50-70%, ZH 20-40%, Other 5-15% | EN:X% ZH:Y% Other:Z% |
| Recency | ≥50% last 3yr (≥70% AI/platform) | X% last 3yr |
| Diversity | ≥3 source types; single <25% | N types, max P% |
| Links | All accessible/archived | Y/X accessible |
| Cross-refs | All [Ref: ID] resolve | Y/X resolved |

**Stop on ANY failure. Fix, regenerate, re-validate.**

---

# Instructions

Execute sequentially; verify before proceeding.

1. **Plan Topics**: Identify 4–6 clusters (Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM); allocate 8–16 MCQs/cluster; assign 20/40/40 difficulty. **Verify**: 40–80 total.

2. **Collect References**:
   - Glossary ≥10: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
   - Tools ≥5: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro)
   - Literature ≥6: EN (Cagan, Olsen, Torres, Perri, Patton, Klement); ZH (俞军, 梁宁, 苏杰)
   - Citations ≥12: Assign IDs (G#/T#/L#/A#); tag language/year/type
   
   **Verify**: Counts met; language 60/30/10%; recency ≥50% last 3yr; ≥3 types.

3. **Generate MCQs**: Write 1–2 sentence stems; provide 4 options (1 correct, 3 plausible distractors); add 1–2 sentence rationales citing [Ref: ID] (justify correct + refute key distractor). **Verify** every 5 MCQs: length, citations, distractor quality.

4. **Populate References**: Complete Glossary, Tools, Literature, APA sections. **Verify**: All [Ref: ID] resolve.

5. **Validate**: Run validation table; fix failures; re-run until all PASS.

6. **Submit**: All checks PASS.

---

# Output Format

Include TOC linking to sections. Use lists, tables, Mermaid diagrams, code blocks.

## Structure

### MCQ Bank (Questions 1–N)

**Question X**  
**Difficulty**: Foundational/Intermediate/Advanced | **Domain**: Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM  
**Stem**: 1–2 sentences (context, frameworks, metrics)  
A. [Option 1]  
B. [Option 2]  
C. [Option 3]  
D. [Option 4]  
**Correct Answer**: [A/B/C/D]  
**Rationale**: 1–2 sentences citing [Ref: ID] (justify correct + refute key distractor)

### Reference Sections

Assign IDs: G# (Glossary), T# (Tools), L# (Literature), A# (APA). Cite as [Ref: G2, T3, A5].

**Glossary (≥10)**: Term, definition, use cases, related concepts  
Example: **G2. RICE** – Reach × Impact × Confidence ÷ Effort. Feature scoring. Use: roadmap planning, backlog ranking. Related: ICE, Value/Effort, KANO

**Tools (≥5)**: Name (Category), features, pricing, users, updated, integrations, PM use, URL  
Example: **T2. ProductBoard** (Roadmapping) – Feedback aggregation, prioritization matrix, roadmap views. $25/maker/mo–Enterprise. 6K+ teams (Microsoft, Zoom). Updated Q4 2024. Integrates: Jira, Slack, Salesforce. Use: synthesis, RICE, stakeholder comms. https://productboard.com

**Literature (≥6)**: Author. Year. Title. Publisher. Summary (1–2 sentences)  
Example: **L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.** Weekly touchpoints, opportunity solution trees. Discovery process.

**APA (≥12)**: Full APA 7th + language tag [EN]/[ZH]  
Example: **A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

---
