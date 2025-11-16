# Guidelines for LLM Multimedia: Essential Only

**Time is precious.** Include multimedia ONLY if: **≥1 Decision-Critical** (blocks decision, >40% comprehension gain vs text, accessibility/WCAG 2.1 AA compliance required, affects ≥2 stakeholder types, multi-modal necessity) + **ALL High-Quality** (accurate, format-appropriate, cited sources, actionable) + **ALL Minimal Sufficient** (necessary for decision, context-specific, non-redundant w/text) + **WCAG 2.1 AA** (alt text, captions, transcripts, text fallbacks).

**Result**: 75% less multimedia, 100% decision capability + WCAG 2.1 AA compliance.

---

## 6 Guidelines (Tier 1: Prevent Errors | Tier 2: Ensure Accessibility)

**Tier 1: Prevent Errors (Must Have)**

**1. Format Spec** [↓40-50% quality issues]: Specify type (image/audio/video), format (PNG/MP4/SVG/Mermaid), purpose, constraints.
❌ "Show deployment" | ✅ "Mermaid sequence (SVG, <80 nodes): CI/CD→registry→K8s. Screen-reader accessible"

**2. Generate vs Link** [↓50-70% rework]: State whether generate (Mermaid/ASCII) or link. No image creation/hallucinated URLs.
❌ "Show AWS arch" | ✅ "Mermaid: VPC/ALB/ECS/RDS. NO image files/URLs. Text-based only"

**3. Source Verify** [↓60-80% hallucinated links]: Require official docs, verify URLs, reject placeholders.
❌ "Link K8s video" | ✅ "Official kubernetes.io/CNCF YouTube. Verify URL. If none: 'No verified video'+text fallback"

**Tier 2: Ensure Accessibility (WCAG 2.1 AA Required)**

**4. Accessibility** [↑30-40% compliance]: WCAG 2.1 AA: alt text, captions, transcripts, text alternatives.
❌ "Add diagram" | ✅ "Mermaid+text description: 1) Purpose, 2) Components, 3) Relationships, 4) Decisions. Standalone complete"

**5. Essential Only** [↓40-60% reading time]: Include ONLY if adds decision-critical info not in text.
❌ "Add images everywhere" | ✅ "Diagram ONLY if: complex relationships, ≥3 components, aids decision. Skip decorative"

**6. Structure** [↑30-40% implementation]: Context, metadata (title/source/date/license), text alternative, takeaway.
❌ Diagram without context | ✅ "1) Why? 2) Media, 3) Metadata, 4) Alt text, 5) Key point"

---

## Quick Reference (30s before requesting multimedia)

**Before requesting multimedia:**
- [ ] Format: type/format/purpose/constraints specified
- [ ] Generate (Mermaid/ASCII) or link (verified only, no hallucinated URLs)
- [ ] Official sources only (docs/repos)
- [ ] WCAG 2.1 AA: alt text/captions/transcripts
- [ ] Essential only (adds decision-critical info not in text)
- [ ] Structure: context/metadata/alt text/takeaway

---

## Exclude Statement (Copy to prompt)

```
Exclude: decorative media, hallucinated URLs/placeholders, redundant w/text (unless >40% comprehension gain), no alt text, image generation (LLM can't create), unverified sources, platform-specific formats, marketing screenshots, concept art.

Include ONLY: Mermaid/ASCII diagrams (text-based), verified official links (docs/repos), text alternatives for ALL media, WCAG 2.1 AA compliant, decision-critical visualizations (architecture, workflows, data flows).
```

## Quality Checklist (Validate output)

- [ ] Accurate (verified content/sources)
- [ ] WCAG 2.1 AA (alt text/captions/transcripts/4.5:1 contrast)
- [ ] Relevant (decision-critical, not decorative)
- [ ] Format-appropriate (Mermaid for diagrams, not image URLs)
- [ ] Verifiable (official sources, working URLs)
- [ ] Non-redundant (adds info not in text)
- [ ] Structured (context/metadata/alt text/takeaway)
- [ ] Fallback (text alternative for all media)
- [ ] Cross-platform (not platform-locked)
- [ ] Cost-effective (adds >40% comprehension vs effort)

---

## LLM Capabilities (Choose appropriate format)

- **Text-only LLMs** (GPT-4, Claude): Mermaid/ASCII/code/descriptions | ❌ NO: image/audio/video creation
- **Multi-modal LLMs** (GPT-4V, Claude 3): +image analysis | ❌ NO: media creation | ✅ Analyze existing, describe requirements
- **Image generators** (DALL-E, Midjourney): Concept/marketing visuals | ❌ NO: technical diagrams, real photos, hallucinated content

## Impact

Quality issues ↓40-50% • Rework ↓50-70% • Hallucinated links ↓60-80% • Accessibility ↑30-40% • Reading ↓40-60% • Speed ↑30-40% • **Overall ↑50-70%**

## WCAG 2.1 AA (Mandatory)

**Images**: Alt text (purpose+content, not "image of"), long desc for complex, 4.5:1 contrast, no text-in-image
**Video/Audio**: Captions (synced), transcripts, audio descriptions, no autoplay
**Interactive**: Keyboard-accessible, focus indicators, labels, error messages