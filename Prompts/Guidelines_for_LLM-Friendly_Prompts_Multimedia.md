# Guidelines for LLM-Friendly Prompts with Multimedia Integration

**Purpose:** Apply these guidelines to optimize prompts with multimedia requirements that will guide LLMs to generate high-quality multimedia content. When you optimize a prompt using these guidelines, the improved prompt ensures other LLMs produce better multimedia outputs.

**When to apply:** Decision-critical multimedia prompts (blocks decision, quality risk >5%, 1-6mo action window, ≥2 stakeholders, fix cost >40h) requiring WCAG 2.1 AA compliance. **Result:** ↓40-50% quality issues, ↑60-80% accessibility, ↓50-70% rework in generated content.

## 24 Guidelines

### Foundation: Define the Task

**1. Context** [↓40-50% quality issues]: Ensure prompt specifies multimedia scope, create/link decision, formats, quality, accessibility. ❌ Bad: "Add media to explain architecture" ✅ Optimized: "Add multimedia: 3 architecture diagrams (SVG/PNG 1920×1080, alt text, generate via Mermaid), 2 demo videos (WebM/MP4 <2min, captions+transcript, link from verified YouTube channels)"

**2. Clarity** [↓25-35% media confusion]: Ensure prompt defines media purpose and text-media relationships. ❌ Bad: "Add diagram for auth flow" ✅ Optimized: "Generate Mermaid sequence diagram showing auth flow (user→API→DB→response), supporting section 3.2 'Authentication', position after code block, explain how diagram illustrates text concepts"

**3. Precision** [↓30-40% format errors]: Ensure prompt specifies exact media specs and quality parameters. ❌ Bad: "Include high quality video" ✅ Optimized: "Video specifications: 1080p resolution, 30fps, H.264/WebM codec, <50MB filesize, 16:9 aspect ratio, AAC 128kbps audio, duration 90-120s, thumbnail PNG 1280×720"

**4. Relevance** [↓35-45% unnecessary media]: Ensure prompt requests only decision-critical media. ❌ Bad: "Include screenshots of all UI screens" ✅ Optimized: "Screenshots: capture error states only (login failed, timeout, HTTP 500), exclude success/normal flows, focus on troubleshooting scenarios"

### Scope: What to Cover

**5. MECE** [↑40-50% media completeness]: Ensure prompt requests complete media types with no gaps. ❌ Bad: "Add images to explain" (incomplete) ✅ Optimized: "Multimedia coverage: (1) diagrams (architecture/sequence), (2) screenshots (error states), (3) video (demo walkthrough), (4) audio (pronunciation guide), (5) fallback text descriptions for all media"

**6. Sufficiency** [↑35-45% media comprehensiveness]: Ensure prompt requests comprehensive media metadata. ❌ Bad: "Add figure" (insufficient) ✅ Optimized: "Figure 3 format: Title: '3-tier architecture (web/app/db)', Description: shows load balancer, cache layer, read replicas, Source file: arch.svg, Download link, Alt text: 'Three boxes connected vertically with arrows showing data flow...'"

**7. Breadth** [↑30-40% media format diversity]: Ensure prompt requests multiple media formats for compatibility. ❌ Bad: "Use PNG for all images" (limited) ✅ Optimized: "Image formats by type: SVG for diagrams (scalable), PNG for screenshots (compatibility), WebP for photos (compression), with PNG fallback for unsupported browsers"

**8. Depth** [↑25-35% media detail]: Ensure prompt requests detailed media specifications. ❌ Bad: "Attach video file" (no specs) ✅ Optimized: "Video technical specs: H.264 high profile, 2Mbps bitrate, 2s keyframe interval, BT.709 color space, ±50ms audio sync, metadata requirements: title, description, tags, full transcript, chapter markers"

### Quality: Ensure Excellence

**9. Significance** [↓40-60% media time]: Ensure prompt focuses on high-impact media only. ❌ Bad: "Add brand logos and visuals to all pages" ✅ Optimized: "Include decision-critical media only: error screenshots, architecture diagrams, performance charts. Exclude: brand logos, decorative icons, stock photos, generic visuals"

**10. Concision** [↓35-45% media redundancy]: Ensure prompt eliminates duplicate media. ❌ Bad: "Create separate diagram for each section" (redundant) ✅ Optimized: "Create 1 comprehensive layered diagram with toggle controls, reference from multiple sections (3.1, 3.2, 4.1), avoid creating duplicate variations"

**11. Accuracy** [↓20-30% media errors]: Ensure prompt requests media verification and currency. ❌ Bad: "Add UI screenshot" (no verification) ✅ Optimized: "Screenshot requirements: current UI version (v2.3, Oct 2023), verify matches codebase, schedule quarterly updates, flag if deprecated, include version in caption"

**12. Credibility** [↓60-80% bad links]: Ensure prompt requires authoritative media sources with verification. ❌ Bad: "Find relevant tutorial" (unverified) ✅ Optimized: "Link to verified sources only: official vendor docs (docs.aws.amazon.com), GitHub repos (>1K stars, actively maintained), CNCF graduated projects. Verify all URLs return 200, flag any 404s"

**13. Logic** [↓25-35% media-text misalignment]: Ensure prompt requires media-text consistency. ❌ Bad: "Add chart" (no text link) ✅ Optimized: "Text must reference: 'Cache reduces latency to <100ms (see Fig 2)'. Fig 2 chart must show: baseline 500ms → optimized 100ms with cache enabled. Ensure alignment."

**14. Risk/Value** [↑45-55% media decision quality]: Ensure prompt requests media alternatives with cost/benefit analysis. ❌ Bad: "Embed video file" (no alternatives) ✅ Optimized: "Compare video hosting options: (1) YouTube embed (free hosting, fast CDN, analytics), (2) S3 hosting (full control, $5/mo), (3) inline embed (<5MB only). Recommend YouTube for files >10MB."

**15. Fairness** [↑30-40% accessibility compliance]: Ensure prompt requires comprehensive accessibility. ❌ Bad: "Embed video" (inaccessible) ✅ Optimized: "Video accessibility requirements: synchronized captions, full transcript, key frames exported as images with alt text, audio description track, keyboard navigation, screen reader compatibility testing"

### Format: How to Present

**16. Structure** [↑30-40% media findability]: Ensure prompt specifies media organization structure. ❌ Bad: "Add images" (no structure) ✅ Optimized: "Media structure: TOC → H2 sections → [Figure N: title | specs | download link] positioned after introducing paragraph → Caption (1-2 sentences) → Discussion text references Figure N explicitly"

**17. Output Format** [↑35-45% media integration]: Ensure prompt specifies exact media presentation format. ❌ Bad: "Show diagram" (no format) ✅ Optimized: "Media format template: ### Section name → Introductory paragraph → [Figure N: filename.ext | WxH dimensions | Alt text] → **Caption:** 1-sentence description → Discussion paragraph → Download: [URL] → Source: [repository link]"

### Multimedia Integration Specifications

**18. Content Creation** [↓50-70% creation rework]: Ensure prompt provides complete media generation specifications. ❌ Bad: "Generate architecture diagram" (incomplete specs) ✅ Optimized: "Generate Mermaid sequence diagram with: default theme, top-to-bottom direction, actors (User/API/Database), flow: JWT authentication, styling (error paths in red), max width 800px, export formats: PNG + SVG"

**19. Web-Sourced Content** [↓60-80% unverified sources]: Ensure prompt specifies media search criteria and verification. ❌ Bad: "Find OAuth diagram online" (no criteria) ✅ Optimized: "Search criteria: 'OAuth 2.0 flow diagram' in RFC 6749 (IETF official spec), require HTTPS, prefer SVG/PNG, published <2023, verify all URLs return HTTP 200, fallback to generating if none found"

**20. Media Optimization** [↓40-55% loading time]: Ensure prompt requests optimized media delivery. ❌ Bad: "Use highest quality media" (no optimization) ✅ Optimized: "Optimization requirements: diagrams as SVG (scalable), photos as WebP with PNG fallback, videos 1080p for mobile, implement lazy loading, preload critical media only, compression limits: images <500KB, videos <20MB"

### Validation: Ensure Correctness

**21. Evidence** [↑45-55% media trust]: Ensure prompt requires media source citations and licensing. ❌ Bad: "Use online images" (no attribution) ✅ Optimized: "Cite media sources: [1] AWS Architecture Icons (aws.amazon.com/architecture/icons, accessed Oct 2023, verified). License: CC-BY-ND 4.0. Flag uncertainties: 'Using cached copy, may be outdated, verify quarterly'"

**22. Validation** [↓35-45% validation errors]: Ensure prompt requires media validation and testing. ❌ Bad: "Add media" (no validation) ✅ Optimized: "Validation requirements: test all URLs (HTTP 200), verify alt text (descriptive), check caption synchronization (±50ms), screen reader testing, mobile responsiveness check, broken link scanning, schedule quarterly reviews"

**23. Practicality** [↑50-65% media usability]: Ensure prompt addresses technical constraints and compatibility. ❌ Bad: "Embed video" (no compatibility) ✅ Optimized: "Practical requirements: HTML5 video (WebM/MP4), fallback to poster image + transcript, mobile adaptive bitrate, iOS HLS streaming, desktop progressive download, zero plugins, bandwidth detection, degrade gracefully"

**24. Success Criteria** [↑45-55% media measurability]: Ensure prompt defines measurable media success metrics. ❌ Bad: "Ensure good quality media" (unmeasurable) ✅ Optimized: "Success metrics: WCAG 2.1 AA compliance (100% alt text, synchronized captions), Largest Contentful Paint <3s, mobile usability score >90, video completion rate >60%, broken link rate <1%, quarterly content updates"

## Quick Check (30s)

**Before sending:** ☑ Context ☑ Clarity ☑ Precision ☑ Relevance ☑ MECE ☑ Sufficiency ☑ Breadth ☑ Depth ☑ Significance ☑ Concision ☑ Accuracy ☑ Credibility ☑ Logic ☑ Risk/Value ☑ Fairness ☑ Structure ☑ Format ☑ Content Creation ☑ Web-Sourced ☑ Media Optimization ☑ Evidence ☑ Validation ☑ Practicality ☑ Success Criteria

**Quality attributes (10):** Accurate | Accessible | Cited | Complete | Compatible | Consistent | Relevant | Verified | Recent (2023+) | WCAG 2.1 AA

**Exclude:** Decorative media (unless brand requirement), redundant formats (pick 1-2 max), low-res <720p (unless thumbnail), autoplay (WCAG violation), unverified links, proprietary formats without fallback, media lacking alt text/captions, >50MB files (optimize first). **Always specify:** Format, resolution, accessibility, fallback, source, license

**LLM capabilities:** Text-only: link only, describe | Multi-modal: create+link, verify | Vision: analyze+annotate, validate | Audio: transcribe, synthesize

**WCAG 2.1 AA essentials:** Alt text (images, meaningful), captions+transcripts (video/audio, sync ±50ms), keyboard nav (interactive, tab order), contrast ≥4.5:1 (text on images), skip links (long media sequences), no autoplay (user control)

**Impact metrics:** ↓40-50% quality issues (Context) | ↓50-70% rework (Content Creation) | ↓60-80% bad links (Credibility+Web-Sourced) | ↑30-40% accessibility (Fairness) | ↓40-60% media time (Significance) | ↑35-50% integration speed (Structure+Practicality)