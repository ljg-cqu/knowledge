# Cloze – Product Manager

Generate PM fill-in-the-blank assessments for hiring and upskilling senior/director/VP-level PMs.

---

# Specifications

## Task Definition

**Scope**: 24–40 PM-focused items; 20/40/40 difficulty split (Foundational/Intermediate/Advanced); ~60% EN, ~30% ZH, ~10% other sources.

**Constraints**: Product management domain only; unambiguous blanks (___); acceptable answer arrays with normalization (case-insensitive, trim, strip punctuation, numeric ±0.01 tolerance); no PII; no vendor bias.

**Coverage**: MECE clusters across Strategy | Discovery & Validation | Prioritization & Roadmapping | Metrics & Growth | Stakeholder Management | Go-to-Market. Each cluster: definitions, metrics, frameworks, trade-offs. Advanced items: rationale, edge cases, alternatives.

## Quality Requirements

**Reference Floors**: Glossary ≥10, Tools ≥5, Literature ≥6, Citations ≥12 (APA 7th + language tags [EN]/[ZH])

**Quality Gates**:
- **Recency**: ≥50% last 3yr (≥70% AI/platform)
- **Diversity**: ≥3 source types; single <25%
- **Evidence**: ≥70% items cite ≥1 source; ≥30% cite ≥2
- **Links**: All accessible/archived (prefer DOI)
- **Cross-refs**: All [Ref: ID] resolve (G#/T#/L#/A#)
- **Significance**: High-value items only; exclude trivial
- **Concision**: Statements ≤200 chars; rationales ≤2 sentences
- **Logic**: Rationales = claim → reason → evidence
- **Risk/Value**: ≥30% advanced items include trade-offs/costs/benefits
- **Fairness**: Contested items show assumptions + alternatives

**Tool Details**: Pricing, users, update ≤18mo, integrations

**Grading Config**:
```json
{
  "normalization": {"caseInsensitive": true, "trimWhitespace": true, "stripPunctuation": true, "numericTolerance": 0.01},
  "items": [{"id": "1", "statement": "Framework scoring features by reach, impact, confidence, effort is ___.", "acceptableAnswers": ["RICE", "RICE prioritization"], "domain": "Prioritization", "difficulty": "Foundational"}],
  "policies": {"significanceFilter": true, "logicStructure": "claim-reason-evidence", "fairness": "include-alternatives-when-contested"}
}
```

## Validation

Run all checks; fix failures; re-run until all PASS.

| Check | Requirement | Format |
|-------|------------|--------|
| Floors | G≥10, T≥5, L≥6, A≥12, Items 24–40 (20/40/40) | G:X T:Y L:Z A:W I:N (F/I/A) |
| Citations | ≥70% items ≥1 cite; ≥30% ≥2 cites | X% ≥1, Y% ≥2 |
| Language | EN 50-70%, ZH 20-40%, Other 5-15% | EN:X% ZH:Y% Other:Z% |
| Recency | ≥50% last 3yr (≥70% AI/platform) | X% last 3yr |
| Diversity | ≥3 source types; single <25% | N types, max P% |
| Links | All accessible/archived | Y/X accessible |
| Cross-refs | All [Ref: ID] resolve | Y/X resolved |
| Significance | 100% high-value items | PASS/FAIL |
| Concision | Statements ≤200; rationales ≤2 sent | S/X, R/X |
| Logic | Claim→reason→evidence (spot ≥10%) | Sample N |
| Fairness | Contested items show assumptions/alternatives | PASS/FAIL |
| Risk/Value | ≥30% advanced items include trade-offs | PASS/FAIL |
| Practicality | Grader config; normalization tested | PASS/FAIL |

**Stop on ANY failure. Fix, regenerate, re-validate.**

---

# Instructions

Execute sequentially; verify before proceeding.

1. **Plan Topics**: Identify 4–6 clusters (Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM); allocate 4–8 items/cluster; assign 20/40/40 difficulty. **Verify**: 24–40 total.

2. **Collect References**:
   - Glossary ≥10: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
   - Tools ≥5: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro)
   - Literature ≥6: EN (Cagan, Olsen, Torres, Perri, Patton, Klement); ZH (俞军, 梁宁, 苏杰)
   - Citations ≥12: Assign IDs (G#/T#/L#/A#); tag language/year/type
   
   **Verify**: Counts met; language 60/30/10%; recency ≥50% last 3yr; ≥3 types.

3. **Generate Items**: Write unambiguous fill-in-the-blank statements; define acceptable answer arrays; add 1–2 sentence rationales citing [Ref: ID]. **Verify** every 5 items: clarity, citations, answer quality.

4. **Populate References**: Complete Glossary, Tools, Literature, APA sections. **Verify**: All [Ref: ID] resolve.

5. **Validate**: Run validation table; fix failures; re-run until all PASS.

6. **Submit**: All checks PASS.

---

# Output Format

Include TOC linking to sections. Use lists, tables, Mermaid diagrams, code blocks.

## Structure

### Cloze Bank (Items 1–N)

**Item X**  
**Difficulty**: Foundational/Intermediate/Advanced | **Domain**: Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM  
**Statement**: Fill-in-the-blank (≤200 chars)  
**Acceptable Answers**: [Array of valid responses]  
**Rationale**: 1–2 sentences citing [Ref: ID]

### Reference Sections

Assign IDs: G# (Glossary), T# (Tools), L# (Literature), A# (APA). Cite as [Ref: G2, T3, A5].

**Glossary (≥10)**: Term, definition, use cases, related concepts  
Example: **G2. RICE** – Reach × Impact × Confidence ÷ Effort scoring for feature prioritization. Use: roadmap planning, backlog ranking. Related: ICE, Value/Effort, KANO

**Tools (≥5)**: Name (Category), features, pricing, users, updated, integrations, PM use, URL  
Example: **T2. ProductBoard** (Roadmapping) – Features: Feedback aggregation, value/effort matrix, roadmap views. Pricing: $25/maker/mo–Enterprise. Users: 6K+ (Microsoft, Zoom). Updated: Q4 2024. Integrations: Jira, Slack, Salesforce. PM use: RICE scoring, stakeholder comms. https://productboard.com

**Literature (≥6)**: Author. Year. Title. Publisher. Summary (1–2 sentences)  
Example: **L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.** Weekly customer touchpoints, opportunity solution trees. Discovery process design.

**APA (≥12)**: Full APA 7th + language tag [EN]/[ZH]  
Example: **A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

---
