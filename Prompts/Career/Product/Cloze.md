# Cloze – Product Manager

Generate PM fill-in-the-blank assessments for senior+ PMs.

---

# Specifications

## Task Definition

**Scope**: 24–40 items; 20/40/40 difficulty (Foundational/Intermediate/Advanced); ~60% EN, ~30% ZH, ~10% other.

**Constraints**: PM domain; unambiguous blanks (___); normalized answers (case-insensitive, trim, strip punctuation, ±0.01 numeric); no PII; no vendor bias.

**Coverage**: MECE across Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM. Include definitions, metrics, frameworks, trade-offs. Advanced: rationale, edge cases, alternatives.

## Quality & Validation

**Minimums**: Glossary ≥10, Tools ≥5, Literature ≥6, APA Citations ≥12 (7th ed + [EN]/[ZH])

**Gates**:
- **Recency**: ≥50% last 3yr (≥70% AI/platform)
- **Diversity**: ≥3 source types; single <25%
- **Evidence**: ≥70% cite ≥1; ≥30% cite ≥2
- **Links**: All accessible/archived; prefer DOI
- **Cross-refs**: All [Ref: G#/T#/L#/A#] resolve
- **Concision**: Statements ≤200 chars; rationales ≤2 sentences
- **Logic**: Rationales = claim → reason → evidence
- **Risk/Value**: ≥30% advanced show trade-offs
- **Fairness**: Contested show assumptions + alternatives

**Tool Details**: Pricing, users, update ≤18mo, integrations

**Grading Config**:
```json
{
  "normalization": {"caseInsensitive": true, "trimWhitespace": true, "stripPunctuation": true, "numericTolerance": 0.01},
  "items": [{"id": "1", "statement": "Framework scoring by reach, impact, confidence, effort is ___.", "acceptableAnswers": ["RICE", "RICE prioritization"], "domain": "Prioritization", "difficulty": "Foundational"}]
}
```

**Checklist**: Run all; fix failures; re-run until PASS.

| Check | Requirement | Format |
|-------|------------|--------|
| Floors | G≥10, T≥5, L≥6, A≥12, Items 24–40 (20/40/40) | G:X T:Y L:Z A:W I:N |
| Citations | ≥70% ≥1; ≥30% ≥2 | X% ≥1, Y% ≥2 |
| Language | EN 50-70%, ZH 20-40%, Other 5-15% | EN:X% ZH:Y% Other:Z% |
| Recency | ≥50% last 3yr (≥70% AI/platform) | X% last 3yr |
| Diversity | ≥3 types; max <25% | N types, max P% |
| Links | All accessible/archived | Y/X |
| Cross-refs | All [Ref: ID] resolve | Y/X |
| Concision | Stmt ≤200; rationale ≤2 sent | S/X, R/X |
| Logic | Claim→reason→evidence (≥10% spot) | Sample N |
| Risk/Value | ≥30% advanced show trade-offs | PASS/FAIL |
| Fairness | Contested show assumptions/alternatives | PASS/FAIL |

**Stop on failure. Fix, regenerate, re-validate.**

---

# Instructions

Execute sequentially; verify at each step.

1. **Plan**: Identify 4–6 clusters (Strategy | Discovery | Prioritization | Metrics | Stakeholder | GTM); allocate 4–8 items/cluster; assign 20/40/40 difficulty. **Verify**: 24–40 total.

2. **References**:
   - Glossary ≥10: RICE, AARRR, JTBD, North Star, PMF, OKR, Continuous Discovery, PLG, Feature Factory, OST
   - Tools ≥5: Analytics (Mixpanel, Amplitude), Roadmapping (ProductBoard, Aha!), Research (Dovetail, UserTesting), Collaboration (Miro)
   - Literature ≥6: EN (Cagan, Olsen, Torres, Perri, Patton, Klement); ZH (俞军, 梁宁, 苏杰)
   - Citations ≥12: Assign IDs (G#/T#/L#/A#); tag language/year/type
   
   **Verify**: Counts, language 60/30/10%, recency ≥50% last 3yr, ≥3 types.

3. **Generate**: Write unambiguous blanks; define answer arrays; add 1–2 sentence rationales citing [Ref: ID]. **Verify** every 5: clarity, citations, answers.

4. **Populate**: Complete Glossary, Tools, Literature, APA. **Verify**: All [Ref: ID] resolve.

5. **Validate**: Run checklist; fix failures; re-run until PASS.

6. **Submit**: All checks PASS.

---

# Output Format

Include TOC. Use lists, tables, diagrams, code blocks.

## Structure

### Cloze Bank (Items 1–N)

**Item X**  
**Difficulty**: Foundational/Intermediate/Advanced | **Domain**: Strategy/Discovery/Prioritization/Metrics/Stakeholder/GTM  
**Statement**: (≤200 chars)  
**Acceptable Answers**: [array]  
**Rationale**: 1–2 sentences citing [Ref: ID]

### References

Assign IDs: G# (Glossary), T# (Tools), L# (Literature), A# (APA). Cite as [Ref: G2, T3, A5].

**Glossary (≥10)**: Term, definition, use cases, related  
Example: **G2. RICE** – Reach × Impact × Confidence ÷ Effort scoring for prioritization. Use: roadmap, backlog. Related: ICE, Value/Effort, KANO

**Tools (≥5)**: Name (Category), features, pricing, users, updated, integrations, PM use, URL  
Example: **T2. ProductBoard** (Roadmapping) – Feedback aggregation, value/effort matrix, roadmap views. $25/maker/mo–Enterprise. 6K+ (Microsoft, Zoom). Q4 2024. Jira, Slack, Salesforce. RICE scoring, stakeholder comms. https://productboard.com

**Literature (≥6)**: Author. Year. Title. Publisher. Summary (1–2 sent)  
Example: **L4. Torres, T. (2021). *Continuous Discovery Habits*. Product Talk LLC.** Weekly touchpoints, opportunity trees, discovery process.

**APA (≥12)**: APA 7th + [EN]/[ZH]  
Example: **A6. Torres, T. (2021). *Continuous discovery habits: Discover products that create customer value and business value*. Product Talk LLC. [EN]**

---
