# Reverse Engineering Interview Q&A Generator

Generate 25-30 interview Q&As for senior reverse engineering roles (5+ yrs) demonstrating systematic analysis and tool proficiency across binary analysis (x86/x64/ARM), scripting (Python/IDA/Ghidra), and common formats (PE/ELF/Mach-O).

**Output**: 25-30 Q&As across 6 MECE dimensions with scripts, quantified trade-offs, ≥2 tool alternatives, citations  
**Success**: 19/19 validation PASS (see §6)  
**Assumptions**: Foundational assembly, debugger/disassembler knowledge

---

# Requirements

## Question Specs

| Aspect | Requirement |
|--------|-------------|
| **Count** | 25-30 (20% F / 40% I / 40% A) |
| **Length** | 150-300 words (script excluded) |
| **Structure** | Technique → rationale → script → trade-offs → metrics |
| **Citations** | ≥1 (≥2 advanced) |
| **Per Cluster** | Diagram + script + table + metric |

## Coverage (6 Dimensions, 4-6 Q&As/Each)

1. **Static**: Binary structure, function ID, CFG, data flow (IDA Pro, Ghidra, Binary Ninja)
2. **Dynamic**: Debug, trace, instrument, monitor (GDB, x64dbg, Frida, DynamoRIO)
3. **Code Recovery**: Decompile, reconstruct, symbol/type inference (Hex-Rays, RetDec, Ghidra)
4. **Protocol**: Network/file formats, API reversing (Wireshark, 010 Editor, Burp Suite)
5. **Obfuscation**: Packers, VM protectors, anti-debug/tamper (UPX, VMProtect, Themida)
6. **Vulnerability**: Fuzzing, symbolic exec, taint analysis (AFL++, angr, radare2)

## Standards

**Traceability**: Binary → Behavior → Vulnerability → Exploit → Mitigation  
**Quantified**: ✅ "Frida: <5ms hook, +50MB RAM, +30% CPU" ❌ "Slow"  
**Context**: Binary (<1MB|1-10MB|>10MB), Obfuscation (none|packer|VM|custom), Arch (x86|x64|ARM|RISC-V), Protection (none|ASLR|DEP|CFG)  
**Balance**: ≥2 alternatives + table; assumptions/limits; tag `[Industry]`/`[Tool-dep]`/`[Exp]`  
**Precision**: Inline terms; consistent vocab; concrete metrics ("<100 functions" not "small"); minimal jargon

## Artifacts

**Diagram-Code-Metric Mapping**:

| Dimension | Diagram | Script Example | Metric Formula |
|-----------|---------|----------------|----------------|
| Static Analysis | Control Flow Graph | IDA Python disassembly | `Coverage = Analyzed / Total Functions × 100%` |
| Dynamic Analysis | Execution trace | Frida hook script | `Hook Overhead = (Instrumented - Native) / Native × 100%` |
| Code Recovery | AST/Pseudocode | Decompiler optimization | `Accuracy = Correct / Total Constructs × 100%` |
| Protocol Analysis | Message flow | Wireshark dissector | `Field Coverage = Identified / Total Fields × 100%` |
| Obfuscation | Protection layers | Unpacker script | `Success Rate = Unpacked / Total Samples × 100%` |
| Vulnerability Discovery | Attack surface | Fuzzing harness | `Code Coverage = Blocks Hit / Total Blocks × 100%` |

**Format**: Mermaid <120 nodes matching dimension; Scripts 10-30 lines with error handling; Tables with "Use When"; Metrics: formula + vars + target

**Techniques**: Signature matching, string/constant analysis, xref tracing, API hooks, memory dump, shellcode extract, CFG flatten reversal, opaque predicate removal, dead code elimination, taint analysis

## References

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥10 | Terms + relationships |
| **Tools** | ≥5 | URL, update ≤18mo, pricing, adoption |
| **Literature** | ≥6 | Authoritative (Eilam, Eagle, Sikorski, Kaspersky, Dang, Erickson) |
| **Citations** | ≥12 | APA 7th, 60/30/10% EN/ZH/Other (±10%) |

**Quality**: ≥50% last 3yr (≥70% modern tools), ≥3 types (<25% single), peer-reviewed/authoritative, 100% valid links

---

# Process

## 1. Plan

Select 5-6 clusters across 6 dimensions → Allocate 4-6 Q&As/cluster (25-30 total) → Assign 1F/2I/2A per cluster

**Check**: 25-30 total; 20/40/40% F/I/A (±5%); 6 dimensions; no overlap

## 2. References

Glossary (≥10 + relations) → Tools (≥5: URL, ≤18mo, pricing, adoption) → Lit (≥6 books + relevance) → Cites (≥12 APA [EN]/[ZH])

**Check**: G≥10, T≥5, L≥6, A≥12; 60/30/10% (±10%); ≥50% recent (≥70% tools); ≥3 types <25% single; 100% valid URLs

## 3. Write

**Questions**: ≥70% judgment ("How/When/Compare"); avoid recall unless foundational

**Answers**: 150-300 words, ≥1 cite (≥2 adv), technique→rationale→script→trade-offs→metrics, 10-30 line script, ≥2 alternatives + table, assumptions/limits

**Validate per 5**: Count, cites, syntax, traceability, type, quantified

## 4. Artifacts

Per cluster: Diagram (<120 nodes matching dimension) + Script (10-30 lines, errors) + Table (≥2 tools: Tool|Pros|Cons|Use When) + Metric (formula+vars+target)

**Check**: All 4/4; renders; executes; formatted; valid

## 5. Link

Populate sections → Extract `[Ref: ID]` → Verify IDs → Remove orphans → Validate URLs

**Check**: G≥10, T≥5, L≥6, A≥12; 100% resolved; 0 broken; 60/30/10%; no orphans

## 6. Validate (19 Checks)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 (20/40/40%) |
| 2 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 |
| 3 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 4 | Recency | ≥50% last 3yr (≥70% modern tools) |
| 5 | Diversity | ≥3 types; <25% single |
| 6 | Links | 100% valid |
| 7 | Cross-refs | 100% resolved |
| 8 | Word count | Sample 5: 150-300 |
| 9 | Insights | 100% quantified |
| 10 | Per-topic | ≥2 sources + ≥1 tool |
| 11 | Traceability | ≥80% technique→script |
| 12 | Question type | ≥70% judgment |
| 13 | Artifacts | ≥90% clusters 4/4 |
| 14 | Techniques | ≥80% use techniques |
| 15 | Metrics | ≥60% have metrics |
| 16 | Scripts | ≥80% have snippets |
| 17 | Syntax | 100% valid |
| 18 | Formulas | 100% valid |
| 19 | Review | 6/6 criteria (see §7) |

**Failure**: ANY fail → STOP → Document → Fix → Re-validate ALL → 19/19 PASS

## 7. Review (6 Criteria PASS)

1. **Clarity**: Logical, consistent terms, inline defs
2. **Accuracy**: Verifiable facts, valid scripts/diagrams/metrics
3. **Completeness**: 6 dimensions (4-6 Q&As), minimums, 19/19 PASS
4. **Balance**: ≥2 alternatives + table, assumptions/limits, tagged
5. **Practicality**: Actionable, working scripts, measurable
6. **Self-Check**: No redundancy/gaps/orphans

**Submit**: 19/19 + 6/6 PASS

**High-Risk**: Script syntax (validate), URLs (test), xrefs (verify `[Ref: ID]`)

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty |
| [Title] | [Type] | Q1-Q5 | 5 | 1F/2I/2A |
[6 dimensions, 25-30 total, 20/40/40%]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [How/When/Compare question]
**Difficulty**: [F/I/A] | **Dimension**: [Type]  
**Insight**: [Quantified trade-off]

**Answer** (150-300w): [Context → Technique+rationale → Trade-offs → Metrics → Assumptions/Limits] [≥1 cite [Ref: A1]]

**Script** ([Tool]):
```[lang]
# 10-30 lines: errors, logging, tool API
```

**Diagram** (per cluster):
```mermaid
[Type matching dimension, <120 nodes]
```

**Metrics**:
| Metric | Formula | Variables | Target |
| [Name] | [Expr] | [Defs] | [Threshold] |

**Trade-offs** (≥2):
| Approach | Pros | Cons | Use When | Tag |
| [Option] | [Quantified] | [Quantified] | [Context] | [Industry/Tool-dep/Exp] |

---

## References

### Glossary (≥10)
**G1. [Term]** [EN/ZH/Other] – [Definition]. **Related**: [Terms]

### Tools (≥5)
**T1. [Tool]** [Tag] – [Desc]. Updated: [YYYY-MM]. Pricing: [Type]. Adoption: [Metrics]. [URL]

### Literature (≥6)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – Relevance: [Why]

### Citations (≥12, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation
| # | Check | Target | Result | Status |
| 1 | Counts | G≥10, T≥5, L≥6, A≥12, Q=25-30 | G:X, T:Y | PASS/FAIL |
[All 19]

**Overall**: [X/19 - need 19/19] | **Issues**: [Failures] | **Actions**: [Remediation]
```

# Reference Examples

## Glossary
**G1. Static Analysis** [EN] – Examining code/binary without execution. Reveals structure, logic. Related: Disassembly  
**G2. Dynamic Analysis** [EN] – Observing behavior during execution. Captures runtime state. Related: Debugging  
**G3. Disassembly** [EN] – Converting machine code to assembly. First step in analysis. Related: Static Analysis  
**G4. Decompilation** [EN] – Recovering high-level code from binary. Improves readability. Related: Hex-Rays  
**G5. Control Flow Graph (CFG)** [EN] – Visual representation of execution paths. Reveals branching logic. Related: Basic Block  
**G6. Basic Block** [EN] – Sequence of instructions with single entry/exit. CFG building unit. Related: CFG  
**G7. Instrumentation** [EN] – Injecting monitoring code at runtime. Enables dynamic tracing. Related: Frida  
**G8. Hooking** [EN] – Intercepting function calls/system calls. Modifies behavior. Related: API Hooking  
**G9. Obfuscation** [EN] – Deliberate code/data obscuring. Hinders analysis. Related: Packer  
**G10. Packer** [EN] – Compresses/encrypts binary. Runtime unpacking required. Related: UPX

## Tools
**T1. IDA Pro** [EN] – Disassembler/debugger, Hex-Rays, IDAPython. 2024-10. Commercial ($$$). https://hex-rays.com  
**T2. Ghidra** [EN] – NSA RE framework, decompiler, scripting. 2024-11. Free/OSS. https://ghidra-sre.org  
**T3. Binary Ninja** [EN] – Disassembler, MLIL/HLIL, Python API. 2024-10. Commercial ($$). https://binary.ninja  
**T4. Frida** [EN] – Dynamic instrumentation, JS API, cross-platform. 2024-11. Free/OSS. https://frida.re  
**T5. radare2** [EN] – Unix-like RE, CLI, r2pipe, plugins. 2024-11. Free/OSS. https://rada.re

## Literature
**L1. Eilam, E. (2005). *Reversing*. Wiley.** – Foundation, x86, anti-debug  
**L2. Eagle, C. (2011). *The IDA Pro Book* (2nd). No Starch.** – IDA mastery, IDAPython  
**L3. Sikorski, M., & Honig, A. (2012). *Practical Malware Analysis*. No Starch.** – Static/dynamic, behavior  
**L4. Kaspersky, G. (2003). *The Art of Disassembling*. A-LIST.** – x86 patterns, compiler  
**L5. Dang, B., et al. (2014). *Practical Reverse Engineering*. Wiley.** – Windows, x64/ARM, kernel  
**L6. Erickson, J. (2008). *Hacking: The Art of Exploitation* (2nd). No Starch.** – Exploitation, shellcode

## Citations
**A1.** Eilam, E. (2005). *Reversing: Secrets of reverse engineering*. Wiley. [EN]  
**A2.** Eagle, C. (2011). *The IDA Pro book* (2nd). No Starch Press. [EN]  
**A3.** 段钢. (2013). *加密与解密* (4th). 电子工业出版社. [ZH]  
**A4.** Sikorski, M., & Honig, A. (2012). *Practical malware analysis*. No Starch Press. [EN]  
**A5.** Kaspersky, G. (2003). *The art of disassembling*. A-LIST. [EN]  
**A6.** Dang, B., et al. (2014). *Practical reverse engineering*. Wiley. [EN]  
**A7.** Erickson, J. (2008). *Hacking: The art of exploitation* (2nd). No Starch Press. [EN]  
**A8.** Ligh, M., et al. (2014). *The art of memory forensics*. Wiley. [EN]  
**A9.** 看雪学院. (2019). *软件保护及分析技术*. 电子工业出版社. [ZH]  
**A10.** Ange, A., et al. (2012). *The shellcoder's handbook* (2nd). Wiley. [EN]  
**A11.** Yosifovich, P., et al. (2017). *Windows internals* (7th, Part 1). Microsoft Press. [EN]  
**A12.** Bratus, S., et al. (2011). *Exploit programming*. Syngress. [EN]
