# Dialogue Prompts - Quick Reference

Transform Q&A pairs into natural dialogue formats for effective practice of decision-critical information.

## Quick Start

1. Choose format by style/participants (not complexity)
2. LLM auto-adapts single/multi-round based on content
3. Essential dynamics built-in (80% of cases)
4. Optional: Consult ConversationDynamics.md for advanced patterns

## File Selection Guide

| File | Use When | Output Style |
|------|----------|--------------|
| **ToConversation.md** | 1-on-1, casual learning, mentoring | Friendly, conversational |
| **ToDiscussion.md** | Team meetings, 3+ people | Collaborative, multi-party |
| **ToPresentation.md** | Formal presentations, 1-to-many | Professional, structured |
| **ConversationDynamics.md** | Advanced dynamics or post-check audit | Comprehensive patterns |

**Decision tree**: 1-on-1 casual → ToConversation | 1-on-1 formal → ToPresentation | Group 3+ → ToDiscussion | Need advanced → ConversationDynamics

## Core Files

**ToConversation.md** - 1-on-1 conversational style
- Auto-adapts single Q&A or multi-round (2-5)
- Built-in: confusion handling, interruptions, context rebuilding
- Best for: mentoring, casual learning

**ToDiscussion.md** - Multi-party discussion (3+ speakers)
- Auto-adapts single or multi-phase (2-5)
- Built-in: disagreement handling, participation management, off-topic redirection
- Best for: team meetings, collaborative problem-solving

**ToPresentation.md** - Formal presentation (1-to-many)
- Auto-adapts single or multi-section (2-5)
- Built-in: disruption recovery, audience re-engagement, question handling
- Best for: formal talks, lectures, slide narration

**ConversationDynamics.md** - Comprehensive dynamics reference
- Dual-purpose: supporting reference + post-check audit tool
- Top 10 patterns cover 80% of needs
- Full framework for advanced scenarios

## Key Principles

**Intelligent Complexity Adaptation**: LLM determines single vs. multi-round automatically based on content; you choose style/participants, LLM chooses complexity/rounds

**Self-Contained Formats**: Each core file includes context-specific essential dynamics (80/20 rule); one-file workflow for most cases

**Fidelity**: Preserves all decision-critical content—facts, numbers, technical precision unchanged; transforms style/tone, not substance

**Audio-Only Ready**: All formats include audio adaptation guidance with confirmation markers and explicit structure

## Input/Output

**Input**: Q&A pairs from `Extract/` directory (Cloze, Decision, Creativity, CriticalThinking, Debug, Reflection) or any Q&A format

**Output**: Natural dialogue with automatic complexity adaptation, built-in essential dynamics, audio-ready format

## Best Practices

**Do**:
- Choose format by style/participants
- Trust LLM for complexity adaptation
- Use built-in dynamics (sufficient for 80%)
- Preserve decision-critical content

**Don't**:
- Manually decide complexity/rounds
- Use every dynamic in every dialogue
- Mix multiple formats in one output
- Sacrifice accuracy for naturalness
