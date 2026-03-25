---
title: "M5. Writing Instructions"
nav_order: 6
lang: en
---

# Writing Instructions (Job Posting) + Debugging
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 11:45 | 25 min | 🟢 Write & test |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- The **4 elements** of instructions (role, scope, attitude, principles)
- Experience the **6 principles** of good instructions
- See the **difference in answers** directly after entering instructions
- The **3-step debugging** diagnostic method for unusual answers

---

## Instructions = Job Posting

A well-written job posting leads to a great employee.
**Well-written instructions lead to a great agent.**

{: .highlight }
> Writing instructions is fundamentally a writing skill. This is **the domain of non-developers**.

---

## The 4 Elements of Instructions

| Element | Key Question | Example |
|:-----|:---------|:-----|
| **Role** | "Who are you?" | "You are an HR assistant" |
| **Scope** | "What do you handle?" | "Benefits, vacation, expense reimbursement" |
| **Attitude** | "How do you speak?" | "Kindly and concisely, using formal tone" |
| **Principles** | "What must you always follow?" | "If you don't know, guide to the right contact" |

---

## 6 Principles of Good Instructions

| # | Principle | ❌ Bad Example | ✅ Good Example |
|:--|:-----|:----------|:----------|
| 1 | **Role should be specific** | "AI assistant" | "Dedicated HR assistant for our company" |
| 2 | **Scope: list only inclusions** | "Don't talk about politics" | "Answer only about benefits, vacation, and expenses" |
| 3 | **Attitude as behavioral guidelines** | "Be friendly" | "All responses in formal tone, lead with the key point" |
| 4 | **Define what to do when unknown** | (omitted) | "Direct to HR team extension 1234" |
| 5 | **Specify language and format** | (unspecified) | "Answer in English, within 200 words" |
| 6 | **Shorter is better** | 1000-word paragraph | 200–500 characters, structured |

{: .warning }
> Omitting Principle 4 causes the agent to **make things up** when it doesn't know (hallucination). Always define "what to do when unknown."

---

## Practice: Write Instructions + Test

### Instructions Template

Paste the text below into the Instructions section of Copilot Studio.

```
## Role
You are our company's dedicated HR/Admin assistant.

## Scope
Answer only questions about benefits, vacation/leave, expense reimbursement, and internal policies.

## Attitude
- Use formal/professional tone
- Lead with the key point, then add details
- Keep responses concise, within 200 words

## Principles
- For topics not in your knowledge: "I'm unable to give an accurate answer.
  Please contact HR (ext. 1234)."
- For personal information (salary, performance reviews): direct to the appropriate contact
```

### 3 Test Questions

After entering the instructions, test with the following 3 questions:

| # | Question | Expected Response |
|:--|:-----|:---------|
| 1 | "How many vacation days do I have?" | ✅ In scope — knowledge-based answer |
| 2 | "What's the weather today?" | 🚫 Out of scope — "This is outside my scope" |
| 3 | "What's my salary?" | 🔒 Principle applied — "Direct to contact" |

{: .tip }
> Change "formal tone" to "casual tone" in the instructions and test again. Changing a single line of text completely transforms the agent.

---

## Engine (Model) Selection

In Copilot Studio, you can choose the AI model the agent uses.

### OpenAI Models

| Model | Characteristics | Notes |
|:-----|:-----|:-----|
| **GPT-4.1** | Suitable for most tasks and fast analysis | ✅ Default |
| GPT-5 Chat | Suitable for most tasks | |
| GPT-5 Auto | Automatically switches between chat and reasoning | Preview |
| GPT-5 Reasoning | Maximum depth and accuracy for the most demanding tasks | Preview |

### Anthropic Models

| Model | Characteristics |
|:-----|:-----|
| **Claude Sonnet 4.5** | General tasks and content creation |
| Claude Sonnet 4.6 | General tasks and content creation |
| Claude Opus 4.6 | Deep reasoning and structured problem solving |

### Which Model to Choose?

| Situation | Recommended Model |
|:-----|:---------|
| General work (default) | GPT-4.1 (default) |
| Priority on content quality | Claude Sonnet 4.5 / 4.6 |
| Complex reasoning and analysis | GPT-5 Reasoning or Claude Opus 4.6 |

{: .note }
> Start with the default (GPT-4.1) and change it when needed.

---

## 3-Step Debugging Diagnostic

When the agent gives an unusual answer, find the cause **in this order**:

| Step | Suspect | Symptom | Solution |
|:-----|:-----|:-----|:-----|
| **STEP 1** | Instructions problem? | Out-of-scope answers, attitude mismatch | Revise role/scope/principles in instructions |
| **STEP 2** | Knowledge problem? | Repeating "I don't know" | Add knowledge sources (M6) |
| **STEP 3** | Engine problem? | Language quality issues, reasoning errors | Switch to a different model and re-test |

{: .important }
> **Order matters:** Suspect instructions → knowledge → engine, in that order.

---

## Key Takeaways

1. Instructions = job posting — **4 elements: role, scope, attitude, principles**
2. Always define "what to do when unknown" (prevents hallucination)
3. When problems occur, debug in order: **instructions → knowledge → engine**

---

## FAQ

| Question | Answer |
|:-----|:-----|
| Do instructions work better written in English? | English instructions work well too, but the agent performs well with instructions in either language. |
| What if the instructions are too long? | 200–500 characters is ideal. Too long actually creates confusion. |
| What about using "don't do X"? | It's possible, but "do this instead" is more effective. |
| What if I don't define the unknown case? | The agent will make things up (hallucination). Always define it. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Instructions writing guide | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/guidance/building-agents-instructions) |
| Agent model selection | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/advanced-generative-answers-overview) |
| Testing and debugging | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/authoring-test-bot) |

---

Next module: [M6. Connecting Knowledge](m06-knowledge)
