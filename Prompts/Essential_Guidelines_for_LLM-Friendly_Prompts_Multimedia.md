# Guidelines for LLM Multimedia: Essential Only

**Core**: Include ONLY if ≥1 Decision-Critical (blocks decision, >40% comprehension gain, WCAG 2.1 AA required, ≥2 stakeholders) + High-Quality (accurate, format-appropriate, cited, actionable) + Minimal Sufficient (non-redundant). Result: 75% less multimedia, 100% decision capability.

## 6 Guidelines (Inline Format)

**1. Format Spec** [↓40-50% issues]: Specify type/format/purpose/constraints. ❌ "Show deployment" ✅ "Mermaid sequence (SVG, <80 nodes): CI/CD→K8s. Screen-reader accessible"

**2. Generate vs Link** [↓50-70% rework]: State generate (Mermaid/ASCII) or link. NO image creation/hallucinated URLs. ❌ "Show AWS" ✅ "Mermaid: VPC/ALB/ECS/RDS. NO images/URLs"

**3. Source Verify** [↓60-80% hallucinations]: Official docs only, verify URLs. ❌ "Link K8s video" ✅ "kubernetes.io/CNCF YouTube verified. If none: text fallback"

**4. Accessibility (WCAG 2.1 AA)** [↑30-40% compliance]: Alt text, captions, transcripts, text alternatives. ❌ "Add diagram" ✅ "Mermaid+text: 1) Purpose 2) Components 3) Relations 4) Decisions"

**5. Essential Only** [↓40-60% reading]: Include ONLY if decision-critical, not in text. ❌ "Add images everywhere" ✅ "Diagram if: complex relations, ≥3 components, aids decision"

**6. Structure** [↑30-40% speed]: Context, metadata (title/source/date/license), alt text, takeaway. ❌ Bare diagram ✅ "1) Why 2) Media 3) Metadata 4) Alt 5) Takeaway"

---

## Quick Checklist (30s)

 - ☑ Format (type/format/purpose/constraints)
 - ☑ Generate (Mermaid/ASCII) or link (verified, NO hallucinations)
 - ☑ Official sources (docs/repos)
 - ☑ WCAG 2.1 AA (alt/captions/transcripts)
 - ☑ Essential only (decision-critical)
 - ☑ Structure (context/metadata/alt/takeaway)

 ---

 ## Exclude (Copy to prompt)

```
Exclude: decorative, hallucinated URLs, redundant (unless >40% gain), no alt text, image generation, unverified sources, platform-locked, marketing, concept art.
Include ONLY: Mermaid/ASCII (text-based), verified official links, text alternatives ALL media, WCAG 2.1 AA, decision-critical (arch/workflows/data flows).
```

## Validate & Capabilities

**Quality**: Accurate • WCAG 2.1 AA (alt/captions/transcripts/4.5:1 contrast) • Relevant (decision-critical) • Format-appropriate (Mermaid, not images) • Verifiable (official sources) • Non-redundant • Structured (context/metadata/alt/takeaway) • Fallback (text alternative) • Cross-platform • Cost-effective (>40% gain)

**LLM Limits**: Text-only (GPT-4/Claude) → Mermaid/ASCII/code ❌ NO media creation | Multi-modal (GPT-4V/Claude 3) → +image analysis ❌ NO creation | Image gen (DALL-E) → Concept visuals ❌ NO technical diagrams

**WCAG 2.1 AA**: Images (alt text purpose+content, long desc complex, 4.5:1 contrast, no text-in-image) | Video/Audio (synced captions, transcripts, audio descriptions, no autoplay) | Interactive (keyboard-accessible, focus indicators, labels, error messages)

**Impact**: Quality ↓40-50% • Rework ↓50-70% • Hallucinations ↓60-80% • Accessibility ↑30-40% • Reading ↓40-60% • Speed ↑30-40% • **Overall ↑50-70%**