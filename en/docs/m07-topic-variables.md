---
title: "M7. Topics + Variables"
nav_order: 8
lang: en
---

# Scripts (Topics) + Sticky Notes (Variables)
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 14:25 | 30 min | 🟡 Copy-paste + verify |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- Understanding the **Topic = script** analogy
- Understanding the **Variable = sticky note** analogy
- Implementing **2 Topics**: FAQ Topic + Contact Topic (copy-paste exercise)
- Adding **STRICT RULES** to instructions to set Topic trigger conditions

---

## Topic = Script

A Topic is a **pre-written script that defines how the agent behaves in a specific situation**.

The generative orchestrator looks at the user's question and **automatically selects and runs the right script** for the situation.

---

## Variable = Sticky Note

A variable is a **sticky note that records information needed during the conversation**.
It can be retrieved later by other Topics or Flows.

```
User: "Who handles expense reimbursement?"
     ↓
Topic: "Run contact lookup script"
     ↓
📝 Sticky note: [Contact: John Smith / Phone: 555-1234]
     ↓
User: "Please submit an inquiry to the contact you found"
     ↓
Flow: Runs using information from the sticky note
```

### Global Variables vs Regular Variables

| Type | Scope | Analogy |
|:-----|:---------|:-----|
| **Global Variable** | Shared across all scripts | Sticky note on your chest |
| Regular Variable | Only within the current script | Sticky note inside the script |

{: .tip }
> We use **only global variables** today. They're easier to work with and needed for the Flow connection in the next module (M9).

---

## Practice ①: Create FAQ Topic

| Item | Content |
|:-----|:-----|
| **Topic Name** | FAQ Topic |
| **Role** | Find answers from FAQ, benefits, expense, and leave documents → save result |
| **Global Variable** | `Global.FAQ_result` |

### Step-by-Step

1. Copilot Studio → Agent → Left menu **"Topics"** click
2. **"+ Add Topic"** → **"New"**
3. Enter topic name: `FAQ Topic`
4. **Copy-paste the instructor-provided configuration text**
5. Set global variable: `Global.FAQ_result`
6. **Save**

---

## Practice ②: Create Contact Topic

| Item | Content |
|:-----|:-----|
| **Topic Name** | Contact Topic |
| **Role** | Search only ContactInfo.docx → return contact |
| **Global Variable** | `Global.Contact_result` |

Create it the same way as above.

---

## Practice ③: Add STRICT RULES

**Add** the following to the instructions you wrote in M5:

```
## STRICT RULES
- Requests to find a contact → call Contact Topic
- All other questions about internal policies/benefits/vacation/expenses → call FAQ Topic
- If Topic can't find the result: "Please contact HR at ext. 1234"
```

{: .warning }
> Without STRICT RULES, the orchestrator may not **correctly select** Topics.

---

## Test

Verify that Topics work correctly with these 3 questions:

| # | Question | Expected Behavior |
|:--|:-----|:---------|
| 1 | "How many vacation days do I have?" | FAQ Topic called → answer |
| 2 | "Who handles expense reimbursement?" | Contact Topic called → contact info |
| 3 | "I'd like to contact the person you found" | Verify sticky note (variable) is used |

---

## Key Takeaways

1. **Topic = script** — scenario-based agent behavior
2. **Variable = sticky note** — memorize info during conversation, use it later
3. **STRICT RULES** — clearly specify when each Topic is called
4. Topics collect and process. **The orchestrator does the talking**

{: .note }
> Even though it's copy-paste, the important thing is **feeling that "notes are being written on a sticky note."**

---

## FAQ

| Question | Answer |
|:-----|:-----|
| How many Topics can I create? | There's no strict limit, but create Topics with clear roles. |
| What if Topics and instructions conflict? | STRICT RULES take priority. Clearly separate the roles of instructions and Topics. |
| Can I name variables anything? | Yes. Just note that `Global.` prefix means it's a global variable. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Topics overview | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/authoring-fundamentals) |
| Variables guide | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables) |
| Global variables | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/authoring-variables-bot) |

---

Next module: [M8. Deployment](m08-deployment)
