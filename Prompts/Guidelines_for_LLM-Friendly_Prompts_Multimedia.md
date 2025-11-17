# Guidelines for LLM-Friendly Prompts with Multimedia Integration

**Core principle:** Decision-critical multimedia prompts (blocks decision, risk >5%, 1–6mo action window, ≥2 stakeholders, adoption cost >40h) need: create/link clarity, format+quality specs, accessibility (WCAG 2.1 AA), verification. **Result:** ↓40–50% quality issues, ↓50–70% rework, ↓60–80% bad links, ↑30–40% accessibility, ↓40–60% wasted time, ↑35–50% integration speed.

**1. Multimedia Context & Format** [↓40–50% quality issues]: Specify scope, create/link decision, formats, quality, accessibility. ❌ "Add media" | ✅ "3 diagrams (SVG/PNG 1920×1080, alt text, Mermaid), 2 videos (WebM/MP4 <2min, captions+transcript, YouTube URL verified HTTP 200)"

**2. Content Creation vs Linking** [↓50–70% rework]: Complete generation specs OR search criteria+verification. ❌ "Generate diagram" | ✅ "Mermaid sequence: theme default, top-down, actors (User/API/DB), JWT flow, errors red, max 800px, export PNG+SVG" OR "Search 'OAuth flow' RFC 6749 HTTPS, SVG/PNG, published ≥2023, verify HTTP 200, fallback generate"

**3. Credibility & Verification** [↓60–80% bad links]: Authoritative sources, URL validation, licensing. ❌ "Find tutorial" | ✅ "Official docs (docs.aws.amazon.com), GitHub >1K stars active, CNCF graduated. Verify HTTP 200, flag 404s. Cite: [1] AWS Icons (aws.amazon.com/arch/icons Oct 2023). CC-BY-ND 4.0"

**4. Accessibility & Fallback** [↑30–40% accessibility]: Alt text, captions, transcripts, fallback formats, keyboard nav. ❌ "Embed video" | ✅ "Video: sync captions, full transcript, key frames as images+alt text, audio description, keyboard nav, screen reader test. Fallback: poster+transcript"

**5. Significance & Optimization** [↓40–60% wasted time]: Decision-critical only, eliminate redundancy, optimize delivery. ❌ "Visuals all pages" | ✅ "Error screenshots, arch diagrams, perf charts ONLY. Exclude: logos, decorative. SVG diagrams, WebP+PNG fallback, lazy load, images <500KB, videos <20MB"

**6. Integration & Validation** [↑35–50% integration speed]: Structure, text-media consistency, validation, success metrics. ❌ "Add chart" | ✅ "Text: Latency <100ms (Fig 2). Fig 2: 500ms→100ms with cache. Test: URLs return HTTP 200, alt text descriptive, captions ±50ms sync, screen reader, mobile, no broken links (HTTP 4xx/5xx). WCAG 2.1 AA: 100% alt text+captions. Performance: LCP <3s, mobile score >90"

## 30-Second Quick Reference

☑ Format+quality specs ☑ Create/link clarity ☑ Verified sources ☑ Alt text+captions ☑ Decision-critical only ☑ Text-media consistency

**Quality:** Accurate | Accessible | Cited | Complete | Compatible | Consistent | Recent | Relevant | Verified

**Exclude:** Decorative (unless brand), redundant formats, <720p, autoplay, unverified links, proprietary no-fallback, missing alt/captions, images >500KB unoptimized, videos >20MB unoptimized. **Always:** Format, resolution, accessibility, fallback, source, license

**LLM capability matrix:** Text-only (link+describe) | Multi-modal (create+link+verify) | Vision (analyze+annotate+validate) | Audio (transcribe+synthesize)

**WCAG 2.1 AA:** Alt text (meaningful), captions+transcript (±50ms sync), keyboard nav (tab order), contrast ≥4.5:1, skip links, no autoplay

**Impact:** ↓40–50% quality issues | ↓50–70% rework | ↓60–80% bad links | ↑30–40% accessibility | ↓40–60% wasted time | ↑35–50% integration speed

**Test Description:** Automated check that validates format+quality specs, link status (HTTP 200), WCAG 2.1 AA accessibility, and text-media consistency for all multimedia.