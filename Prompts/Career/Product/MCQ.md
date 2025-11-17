# MCQ – Product Manager

Generate senior/director/VP PM multiple-choice assessments.

---

## Scope

**Output**: 40–80 MCQs; 20/40/40 difficulty (Foundational/Intermediate/Advanced); ~60% EN, ~30% ZH, ~10% other

**Domain**: Product management (strategy, discovery, metrics, execution, leadership)

**Format**: 1–2 sentence stems; 4 options (1 correct, 3 plausible distractors from misconceptions/outdated practices/competing frameworks); single-select; machine-gradable

**Coverage**: MECE across Strategy | Discovery | Prioritization | Metrics | Stakeholder | Go-to-Market. Include frameworks, metrics, trade-offs, best practices. Advanced: edge cases, alternatives.

## Quality Gates

**Reference Floors**: Glossary ≥10, Tools ≥5, Literature ≥6, APA Citations ≥12 (APA 7th + [EN]/[ZH] tags)

**Content**:
- **Recency**: ≥50% last 3yr (≥70% AI/platform topics)
- **Diversity**: ≥3 source types; single <25%
- **Evidence**: ≥70% MCQs cite ≥1 source; ≥30% cite ≥2
- **Links**: All accessible/archived (prefer DOI)
- **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
- **Concision**: Stems/rationales 1–2 sentences each
- **Logic**: Rationales justify correct + refute key distractor
- **Fairness**: Acknowledge competing frameworks/assumptions; no vendor bias

**Tool Details**: Pricing, users, update ≤18mo, integrations

## Validation

Run checks; fix failures; repeat until all PASS. **Stop on ANY failure.**

| Check | Requirement | Format |
|-------|------------|--------|
| Floors | G≥10, T≥5, L≥6, A≥12, MCQs 40–80 (20/40/40) | G:X T:Y L:Z A:W Q:N (F/I/A) |
| Citations | ≥70% MCQs ≥1 cite; ≥30% ≥2 cites | X% ≥1, Y% ≥2 |
| Language | EN 50-70%, ZH 20-40%, Other 5-15% | EN:X% ZH:Y% Other:Z% |
| Recency | ≥50% last 3yr; ≥70% AI/platform topics | X% last 3yr, Y% AI/platform |
| Diversity | ≥3 source types; single <25% | N types, max P% |
| Links | All accessible/archived | Y/X accessible |
| Cross-refs | All [Ref: ID] resolve | Y/X resolved |

---

## Instructions

Execute sequentially; verify after each step.

1. **Plan**: Identify 4–6 clusters; allocate 8–16 MCQs/cluster; assign difficulty 20/40/40. **Verify**: 40–80 total.

2. **Collect References**:
   - Glossary ≥10: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
   - Tools ≥5: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro)
   - Literature ≥6: EN (Cagan, Olsen, Torres, Perri, Patton, Klement); ZH (俞军, 梁宁, 苏杰)
   - Citations ≥12: Assign IDs (G#/T#/L#/A#); tag language/year/type
   
   **Verify**: Reference counts; recency ≥50% last 3yr; ≥3 source types.

3. **Generate MCQs**: 1–2 sentence stems; 4 options; 1–2 sentence rationales citing [Ref: ID]. **Verify** every 5 MCQs: length, citations, distractor quality, and overall language mix trending toward ~60% EN / ~30% ZH / ~10% other (within specified ranges).

4. **Populate References**: Complete all sections. **Verify**: All [Ref: ID] resolve.

5. **Validate**: Run table; fix failures; repeat until PASS.

6. **Submit**: All checks PASS.

---

## Output Format

Include TOC linking to sections. Use lists, tables, Mermaid diagrams, code blocks.

### MCQ Bank (Questions 1–N)

**Question X**  
**Difficulty**: Foundational/Intermediate/Advanced | **Domain**: Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM  
**Stem**: 1–2 sentences  
A. [Option 1]  
B. [Option 2]  
C. [Option 3]  
D. [Option 4]  
**Correct Answer**: [A/B/C/D]  
**Rationale**: 1–2 sentences citing [Ref: ID] (justify correct + refute key distractor)

### References

Assign IDs: G# (Glossary), T# (Tools), L# (Literature), A# (APA). Cite as [Ref: G2, T3, A5].

**Glossary (≥10)**: Term, definition, use cases, related concepts  
*Example*: **G2. RICE** – Reach × Impact × Confidence ÷ Effort. Feature scoring. Use: roadmap planning, backlog ranking. Related: ICE, Value/Effort, KANO

**Tools (≥5)**: Name (Category), features, pricing, users, updated, integrations, PM use, URL  
*Example*: **T2. ProductBoard** (Roadmapping) – Feedback aggregation, prioritization matrix, roadmap views. $25/maker/mo–Enterprise. 6K+ teams. Q4 2024. Integrates: Jira, Slack, Salesforce. Use: synthesis, RICE, stakeholder comms. https://productboard.com

**Literature (≥6)**: Author. Year. Title. Publisher. Summary (1–2 sentences)  
*Example*: **L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.** Weekly touchpoints, opportunity solution trees for discovery.

**APA (≥12)**: Full APA 7th + language tag [EN]/[ZH]  
*Example*: **A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

---
