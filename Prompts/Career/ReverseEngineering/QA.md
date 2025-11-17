# Reverse Engineering Decision-Critical Q&A Generator

Generate 6-12 decision-critical Q&As for reverse engineering professionals (3+ yrs) enabling informed decisions on analysis strategy, tool selection, and vulnerability discovery—minimal viable knowledge base for time-constrained practitioners.

**Output**: 6-12 Q&As across 4-5 decision-critical dimensions with scripts, quantified trade-offs, ≥2 tool alternatives, citations  
**Success**: 12/12 validation PASS (see §6)  
**Assumptions**: Foundational assembly, debugger/disassembler knowledge  
**Decision Criticality Framework**: Include if blocks decision, creates risk, affects ≥2 stakeholders, actively evolving, or >40h adoption barrier

---

# Requirements

## Question Specs

| Aspect | Requirement |
|--------|-------------|
| **Count** | 6-12 (25% F / 50% I / 25% A) |
| **Length** | 150-250 words (script excluded) |
| **Structure** | Technique → rationale → script → trade-offs → metrics |
| **Citations** | ≥1 (≥2 advanced) |
| **Per Cluster** | Diagram + script + table + metric |

## Coverage (4-5 Decision-Critical Dimensions, 1-3 Q&As/Each)

1. **Static Analysis** (1-3 Q): Function ID, CFG, data flow analysis—blocks analysis strategy (IDA Pro, Ghidra, Binary Ninja)
2. **Dynamic Analysis** (1-3 Q): Instrumentation, tracing, runtime monitoring—blocks runtime understanding (Frida, GDB, x64dbg)
3. **Code Recovery** (1-3 Q): Decompilation accuracy, symbol inference—blocks vulnerability discovery (Hex-Rays, RetDec, Ghidra)
4. **Vulnerability Discovery** (1-3 Q): Fuzzing, symbolic execution, taint analysis—blocks security decisions (AFL++, angr, radare2)
5. **Obfuscation Handling** (1-3 Q): Unpacking, VM protection, anti-debug—blocks analysis feasibility (UPX, VMProtect, Themida)

**Skip**: Protocol Analysis (nice-to-have unless decision-critical to your role)

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

## References (Proportional 60% Reduction)

| Type | Min | Requirements |
|------|-----|--------------|
| **Glossary** | ≥8 | Only terms used in Q&As + relationships |
| **Tools** | ≥3 | Decision-critical only; URL, update ≤18mo, pricing, adoption |
| **Literature** | ≥4 | Canonical references (e.g., Eilam, Eagle, Sikorski, Dang) |
| **Citations** | ≥6 | APA 7th, 60/30/10% EN/ZH/Other (±10%) |

**Quality**: ≥50% last 3yr (≥70% modern tools), ≥3 types (<25% single), peer-reviewed/authoritative, 100% valid links

---

# Process

## 1. Plan

Select 4-5 decision-critical dimensions → Allocate 1-3 Q&As/dimension (target 6-12 total) → Assign 1-2F/2-3I/1-2A across all Q&As

**Check**: 6-12 total; 25/50/25% F/I/A (±5%); 4-5 dimensions; decision-critical only; no overlap

## 2. References

Glossary (≥8 + relations) → Tools (≥3: URL, ≤18mo, pricing, adoption) → Lit (≥4 books + relevance) → Cites (≥6 APA [EN]/[ZH]/[Other])

**Check**: G≥8, T≥3, L≥4, A≥6; 60/30/10% (±10%); ≥50% recent (≥70% modern tools); ≥3 types <25% single; 100% valid URLs

## 3. Write

**Questions**: ≥70% judgment ("How/When/Compare"); avoid recall unless foundational

**Answers**: 150-250 words, ≥1 cite (≥2 adv), technique→rationale→script→trade-offs→metrics, 10-30 line script, ≥2 alternatives + table, assumptions/limits

**Validate**: Count, cites, syntax, traceability, type, quantified

## 4. Artifacts

Per cluster: Diagram (<120 nodes matching dimension) + Script (10-30 lines, errors) + Table (≥2 tools: Tool|Pros|Cons|Use When) + Metric (formula+vars+target)

**Check**: All 4/4; renders; executes; formatted; valid

## 5. Link

Populate sections → Extract `[Ref: ID]` → Verify IDs → Remove orphans → Validate URLs

**Check**: G≥8, T≥3, L≥4, A≥6; 100% resolved; 0 broken; 60/30/10%; no orphans

## 6. Validate (12 Checks - Streamlined)

| # | Check | Target |
|---|-------|--------|
| 1 | Counts | G≥8, T≥3, L≥4, A≥6, Q=6-12 (25/50/25%) |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion (Blocks/Risk/Stakeholders/Evolving/Adoption) |
| 3 | Citations | ≥70% Q&As ≥1; ≥30% ≥2 |
| 4 | Language | 60/30/10% EN/ZH/Other (±10%) |
| 5 | Recency | ≥50% last 3yr (≥70% modern tools) |
| 6 | Diversity | ≥3 types; <25% single |
| 7 | Links | 100% valid |
| 8 | Word count | Sample 5: 150-250 |
| 9 | Quantified Insights | ≥80% have metrics |
| 10 | Traceability | ≥80% technique→script |
| 11 | Artifacts | ≥90% clusters 4/4 |
| 12 | Review | 6/6 criteria (see §7) |

**Failure**: ANY fail → STOP → Document → Fix → Re-validate ALL → 12/12 PASS

## 7. Review (6 Criteria PASS)

1. **Clarity**: Logical, consistent terms, inline defs, decision-critical focus
2. **Accuracy**: Verifiable facts, valid scripts/diagrams/metrics
3. **Completeness**: 4-5 dimensions (1-3 Q&As each), minimums, 12/12 PASS
4. **Balance**: ≥2 alternatives + table, assumptions/limits, tagged, decision-critical only
5. **Practicality**: Actionable, working scripts, measurable, blocks decision or creates risk
6. **Self-Check**: No redundancy/gaps/orphans, decision criticality justified

**Submit**: 12/12 + 6/6 PASS

**High-Risk**: Script syntax (validate), URLs (test), xrefs (verify `[Ref: ID]`)

---

# Output Template

```markdown
## Contents
[TOC: Topic Areas | Q&As | References | Validation]

## Topic Areas
| Cluster | Dimension | Range | Count | Difficulty | Decision Criticality |
| [Title] | [Type] | Q1-Q3 | 1-3 | 1F/2I or 2I/1A | [Blocks/Risk/Stakeholders/Evolving/Adoption] |
[4-5 dimensions, 6-12 total, 25/50/25%]

---

## Topic 1: [Title]
**Overview**: [1-2 sentences]

### Q1: [How/When/Compare question]
**Difficulty**: [F/I/A] | **Dimension**: [Type] | **Decision Criticality**: [Blocks/Risk/Stakeholders/Evolving/Adoption]
**Insight**: [Quantified trade-off]

**Answer** (150-250w): [Context → Technique+rationale → Trade-offs → Metrics → Assumptions/Limits] [≥1 cite [Ref: A1]]

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

### Glossary (≥8)
**G1. [Term]** [EN/ZH/Other] – [Definition]. **Related**: [Terms]

### Tools (≥3)
**T1. [Tool]** [Tag] – [Desc]. Updated: [YYYY-MM]. Pricing: [Type]. Adoption: [Metrics]. [URL]

### Literature (≥4)
**L1. Author(s). (Year). *Title*. Publisher.** [Tag] – Relevance: [Why]

### Citations (≥6, APA 7th, 60/30/10%)
**A1.** Author(s). (Year). *Title*. Source. [EN]

---

## Validation
| # | Check | Target | Result | Status |
| 1 | Counts | G≥8, T≥3, L≥4, A≥6, Q=6-12 | G:X, T:Y | PASS/FAIL |
| 2 | Decision Criticality | 100% satisfy ≥1 criterion | % | PASS/FAIL |
[All 12]

**Overall**: [X/12 - need 12/12] | **Issues**: [Failures] | **Actions**: [Remediation]
```

# Reference Examples

## Glossary (≥8 Decision-Critical Terms)
**G1. Static Analysis** [EN] – Examining code/binary without execution. Reveals structure, logic. Related: Disassembly  
**G2. Dynamic Analysis** [EN] – Observing behavior during execution. Captures runtime state. Related: Debugging  
**G3. Disassembly** [EN] – Converting machine code to assembly. First step in analysis. Related: Static Analysis  
**G4. Decompilation** [EN] – Recovering high-level code from binary. Improves readability. Related: Hex-Rays  
**G5. Control Flow Graph (CFG)** [EN] – Visual representation of execution paths. Reveals branching logic. Related: Basic Block  
**G6. Instrumentation** [EN] – Injecting monitoring code at runtime. Enables dynamic tracing. Related: Frida  
**G7. Obfuscation** [EN] – Deliberate code/data obscuring. Hinders analysis. Related: Packer  
**G8. Packer** [EN] – Compresses/encrypts binary. Runtime unpacking required. Related: UPX

## Tools (≥3 Decision-Critical)
**T1. Ghidra** [EN] – NSA RE framework, decompiler, scripting. 2024-11. Free/OSS. https://ghidra-sre.org  
**T2. Frida** [EN] – Dynamic instrumentation, JS API, cross-platform. 2024-11. Free/OSS. https://frida.re  
**T3. radare2** [EN] – Unix-like RE, CLI, r2pipe, plugins. 2024-11. Free/OSS. https://rada.re

## Literature (≥4 Canonical)
**L1. Eilam, E. (2005). *Reversing*. Wiley.** – Foundation, x86, anti-debug  
**L2. Sikorski, M., & Honig, A. (2012). *Practical Malware Analysis*. No Starch.** – Static/dynamic, behavior  
**L3. Dang, B., et al. (2014). *Practical Reverse Engineering*. Wiley.** – Windows, x64/ARM, kernel  
**L4. Erickson, J. (2008). *Hacking: The Art of Exploitation* (2nd). No Starch.** – Exploitation, shellcode

## Citations (≥6, APA 7th, 60/30/10% EN/ZH/Other; examples illustrate format, not required distribution)
**A1.** Eilam, E. (2005). *Reversing: Secrets of reverse engineering*. Wiley. [EN]  
**A2.** Sikorski, M., & Honig, A. (2012). *Practical malware analysis*. No Starch Press. [EN]  
**A3.** 段钢. (2013). *加密与解密* (4th). 电子工业出版社. [ZH]  
**A4.** Dang, B., et al. (2014). *Practical reverse engineering*. Wiley. [EN]  
**A5.** Erickson, J. (2008). *Hacking: The art of exploitation* (2nd). No Starch Press. [EN]  
**A6.** 看雪学院. (2019). *软件保护及分析技术*. 电子工业出版社. [ZH]
