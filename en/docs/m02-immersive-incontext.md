---
title: "M2. Immersive vs In-context"
nav_order: 3
lang: en
---

# Agent Usage — Immersive vs In-context
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 10:00 | 15 min | 👀 Watch |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- The difference between **immersive** (dedicated channel) and **in-context** (@mention)
- How to decide which mode fits your work
- That a single agent supports both modes

---

## Two Ways to Use an Agent

After building an agent, there are broadly **two ways** to use it.

| | Immersive | In-context |
|:-----|:------|:---------|
| **Analogy** | Dedicated service desk | Colleague at the next desk |
| **Use case** | When you want a focused conversation with the agent | When you need a quick question during other work |
| **Entry point** | Access via dedicated Teams chat | Call with `@agent` in Copilot chat |
| **Advantage** | Focused conversation, dedicated UI | Keep your flow, fast to call |
| **Best for** | New employee onboarding, customer service | Quick lookups during work |

---

## Immersive — Dedicated Desk

Open the agent's dedicated chat in Teams and start a conversation.

**Best suited when:**
- You have several consecutive questions to ask
- You need an in-depth conversation with the agent
- There's a lot of information to cover, like new employee onboarding

---

## In-context — @mention

Call the agent with `@agentname` in Copilot chat.

**Best suited when:**
- You need to quickly check just one thing during other work
- Simple questions like "How many vacation days do I have?"
- You alternate between multiple agents

{: .tip }
> `@HR-helper Tell me where to use welfare points` — the question and answer are done in one line.

---

## Build Once, Use Both Ways

{: .highlight }
> Once you build and deploy an agent, **both immersive and in-context are automatically supported**. No separate configuration needed.

---

## Key Takeaways

1. **Immersive** = Focused conversation at a dedicated desk
2. **In-context** = Quick questions via @mention
3. **Build once, use both** — no extra implementation needed

---

## FAQ

| Question | Answer |
|:-----|:-----|
| Which mode is better? | It depends on the situation. Immersive is better for deep conversations; in-context is convenient for quick lookups. |
| Can I attach files in in-context mode? | Yes, file references are also possible when using @mention. |
| Can I use it on mobile? | Both modes are available in the Teams mobile app. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Agent deployment channels | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels) |
| Using agents in M365 Copilot | [learn.microsoft.com](https://learn.microsoft.com/microsoft-365-copilot/extensibility/) |
| Deploy agent to Teams | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) |

---

Next module: [M3. Agent Builder Practice](m03-agent-builder)
