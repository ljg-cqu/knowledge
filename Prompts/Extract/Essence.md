# Extract Essence Cards

**Task**: Distill a source text or wiki page into a **minimal, non‑redundant set of essence cards** that capture the decision‑critical core of the content.

**Definition**: An *essence card* is a compact representation of **one core idea** that a reader must retain so that the remaining details of the page can be reconstructed or relearned. Each card states the core idea, why it matters, and how it fits into the topic’s structure.

---

## Principles

### 1. 80/20 Prioritization (Ruthless Selection)
- Extract **1 page‑level essence item** + **3–7 essence cards** per source.
- Prioritize ideas that:
  - **Block a decision** if forgotten
  - **Create material risk** if misunderstood or ignored
  - **Unlock multiple dependent concepts** (foundational principles)
- If in doubt, **exclude**—this file captures only the **top‑level 20%** of ideas.

### 2. MECE Structure (Non‑Overlapping, Complete Top Layer)
- Essence cards must be **mutually exclusive**:
  - No two cards should restate the same core idea in different words.
- Together they should be **collectively exhaustive for the top level**:
  - They cover the **primary purpose and scope** of the page, not every detail.
- Merge overlapping items; **split only** when decisions/risks/uses are clearly distinct.

### 3. Fidelity and Grounding
- Use only information **explicitly stated** or **logically implied** in the source.
- Do **not invent** new concepts, dimensions, or relationships that the source does not support.
- You may **compress and reorganize**, but never contradict or expand beyond the source.

---

## What to Capture

From each source or wiki page, capture:

1. **Page‑Level Essence (1 item)**
   - **Purpose**: Why this page exists; what problem, decision, or competence it supports (1–2 sentences).
   - **Scope**: What is *in* vs *out* of this page.
   - **Central Questions**: 3–5 “If you open this page, you are really asking…” questions.
   - **Organizing Dimensions**: 2–4 axes the topic is structured by (e.g., lifecycle stage, stakeholder role, category, risk type). Use labels derived from the source.
   - **Minimal Glossary**: 3–7 absolutely essential terms needed to understand the essence (term + 1‑line definition).
   - **Wiki Neighborhood** (if implied):
     - **Upstream / Parent topics** (what this depends on)
     - **Sibling topics** (what this sits alongside or is often compared with)
     - **Downstream topics** (what builds on this)
   - **Decision‑Critical Metadata**:
     - **Decision Criticality**: [Blocks / Risk / Roles / Action / Quantified] (choose all that apply)
     - **Primary Stakeholders / Roles**: Who most needs this page.
     - **Time Sensitivity**: [Evergreen / Refresh annually / News‑driven].

2. **Essence Cards (3–7 items)**
   For each core idea:
   - **Label**: Short, reusable heading‑like phrase.
   - **Core Idea**: 1–2 sentences stating the idea in its most compressed form.
   - **Why It Matters**: Which decision, risk, or action this idea directly affects.
   - **Type**: One of [concept / mechanism / pattern / constraint / decision / workflow].
   - **Dimensions**: 1–2 organizing axes from the page‑level dimensions (e.g., lifecycle = Design, role = Architect).
   - **Essential Terms**: 0–3 terms that are indispensable for this card (only if truly necessary).

---

## Rules

**Coverage**:
- Read the **entire source** before extracting.
- First infer the **page‑level essence** (purpose, scope, central questions, dimensions).
- Then identify **3–7 non‑overlapping core ideas** that best represent the page’s decision‑critical content.

**Focus**:
- Do **not** reproduce full explanations, procedures, comparisons, or reflection prompts.
  - Explanations → handled by `Explain.md`
  - Procedures → handled by `How.md`
  - Comparisons → handled by `Compare.md`
  - Reflection → handled by `Reflection.md`
  - Fact recall → handled by `Cloze.md`
  - Why‑chains → handled by `Why.md`
- Here you only capture the **structural spine**: the minimal set of top‑level ideas and how they matter.

**Clarity**:
- Use concise, neutral, wiki‑style language.
- Make each item **self‑contained** so it can be read without the source text.
- Avoid repetition across essence cards; if two cards overlap, merge them or sharpen their distinctions.

---

## Output Format

Output a **Markdown ordered list only**. Use `1.` for every item; Markdown will auto‑number. Output the list only—no extra headings, comments, or explanations.

1. Q: What is the page‑level essence (purpose, scope, and organizing structure) of this source?
   A:
   - **Purpose**: ...
   - **Scope**: ...
   - **Central Questions**:
     - ...
     - ...
   - **Organizing Dimensions**:
     - ...
   - **Minimal Glossary**:
     - Term: ... — ...
   - **Wiki Neighborhood**:
     - **Upstream / Parent**: ...
     - **Siblings**: ...
     - **Downstream**: ...
   - **Decision‑Critical Metadata**:
     - **Decision Criticality**: ...
     - **Primary Stakeholders / Roles**: ...
     - **Time Sensitivity**: ...

1. Q: Essence card – [Label]
   A:
   - **Label**: ...
   - **Core Idea**: ...
   - **Why It Matters**: ...
   - **Type**: ...
   - **Dimensions**: ...
   - **Essential Terms**:
     - ... (optional)

1. Q: Essence card – [Label]
   A:
   - **Label**: ...
   - **Core Idea**: ...
   - **Why It Matters**: ...
   - **Type**: ...
   - **Dimensions**: ...
   - **Essential Terms**:
     - ... (optional)

*(Continue adding essence cards until you have 3–7 in total.)*

---

## Instructions

- Always produce **exactly one** page‑level essence item plus **3–7** essence cards.
- Use `1.` for every list item; rely on Markdown to auto‑number.
- Output **only** the ordered list in the format above—no additional narrative, headings, or commentary.
- Treat this file as the **essential wiki layer**: the minimal, MECE, 80/20 representation that other Extract prompts (Cloze, Explain, How, Decision, etc.) can build on.
