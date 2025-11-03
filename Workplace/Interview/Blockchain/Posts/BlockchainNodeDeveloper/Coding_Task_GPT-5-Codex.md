# Blockchain Node Developer — Coding Task (GPT-5 Codex)

This Codex variant mirrors the GPT-5 Coding Task bank and keeps the same tasks, signatures, and grading.

- Baseline (canonical items): See `Coding_Task_GPT-5.md`
- Shared references: See `Shared_References.md`

## alignment and reuse

Re-use all tasks from `Coding_Task_GPT-5.md` to avoid drift. Where helpful, add micro-benchmarks and brief notes on GC/alloc optimizations.

## delta notes (Codex)

- Prefer explicit error handling and edge-case tests (e.g., zero/negative, overflow, cancellation)
- Add “performance hints” for hot paths (re-using timers, pooling buffers, avoiding copies)

## references

- Canonical set: `Shared_References.md`
- Baseline file: `Coding_Task_GPT-5.md`
