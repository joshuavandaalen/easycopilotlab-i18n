---
title: "M13. Complete Your Design Document"
nav_order: 14
lang: en
---

# Complete Your Own Agent Design Document ⭐
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 17:30 | 20 min | 🟢 Finish design doc |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- **Upgrade the design document** from M4 with everything you've learned today
- Confirm that blank spaces have become **concrete plans**
- Gain the **confidence** to say "I can build an agent starting tomorrow"

---

## Morning Seed → Afternoon Flower

When you created the design document in M4, you didn't fully understand agents, instructions, knowledge, or Topics.

**That's changed now.** The words you didn't know this morning are all visible to you now.

{: .highlight }
> Pull out that design document and look at it again. Check how much has changed from the morning to right now.

---

## Design Document Upgrade — 6 Key Points

Check these items and make your design document more concrete.

| Item | Morning (M4) | Now — Upgraded | Related Module |
|:-----|:---------|:--------------|:---------|
| **Agent name** | "○○ Assistant" | Keep or be more specific | M3 |
| **Role/Scope** | Vague description | Reflect 4 elements: role, scope, attitude, principles | M5 |
| **Knowledge sources** | "Company documents" | Specify which files to upload | M6 |
| **FAQ scenarios** | None or 1 | 3 key questions + expected answers | M7 |
| **Deployment channel** | TBD | Specify Teams / @mention / web | M8 |
| **Automation connection** | None | 1–2 lines on which Flows are needed | M9 |

---

## Practice: Complete the Design Document with Copilot

Enter the following prompt to Copilot:

```
Below is a draft design document for the agent I want to build.
Please make it more concrete based on what was learned today:

[Paste the morning design document content here]

Please fill in the following items:
- Instructions: role/scope/attitude/principles
- 3 knowledge files to upload
- 1–2 Flows needed
- Deployment channel
- 3 FAQ scenarios
```

{: .tip }
> You can write it yourself or use Copilot's help. What matters is **making it specific**.

---

## Before vs After Comparison

### Before (M4)

```
Agent name: HR Assistant
Purpose: Answer employee questions
Knowledge sources: Company documents
Deployment: Teams
```

### After (M13)

```
Agent name: HR Assistant
Purpose: Instantly auto-answer all HR questions from onboarding to expense reimbursement

Instructions:
  Role: Friendly assistant on behalf of the HR team
  Scope: Benefits + Vacation policy + Expense reimbursement
  Attitude: Professional tone, lead with key point, within 200 words
  Principles: Unknown questions → connect to HR team

Knowledge sources:
  - FAQ.docx (Q&A format)
  - BenefitsGuide.docx
  - ContactInfo.xlsx

Deployment: Teams + @mention
Flow: RequestByEmail (auto-forward inquiry emails)
FAQ: "How many vacation days?", "How to claim expenses?", "Where to use welfare points?"
```

{: .important }
> With this design document, **you can build the agent starting tomorrow**.

---

## Next Steps: Build from This Design Document

Once your design document is complete, follow this order to build the actual agent.

| Step | Task | Reference Module |
|:-----|:------|:---------|
| 1 | Create agent in Copilot Studio | M3 |
| 2 | Enter instructions (job posting) | M5 |
| 3 | Upload knowledge files | M6 |
| 4 | Set up Topics + STRICT RULES | M7 |
| 5 | Deploy to Teams | M8 |
| 6 | Connect Flow (if needed) | M9 |
| 7 | Set up conversation logging (optional) | M10 |

---

## Key Takeaways

1. The design document from this morning (M4) has become a **completed action plan** with today's learning
2. With this one design document, **you can build an agent starting tomorrow**
3. Describe your idea to Copilot, Copilot designs it, and **you build it**

---

## FAQ

| Question | Answer |
|:-----|:-----|
| Can I actually build based on the design document? | Yes! Follow the steps in M3–M10. The design document is your roadmap. |
| I want to refine the design document more but I'm running out of time | Just get the big picture. Refine it with Copilot tomorrow. |
| What if I get stuck while building? | Use MS Learn docs, Copilot Studio community, and the reference links in this guide. |
| What if our company can't use Copilot Studio? | Ask your admin about licensing. The concepts in the design document are applicable to other tools too. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Copilot Studio official docs | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/) |
| MS Learn learning path | [learn.microsoft.com](https://learn.microsoft.com/training/paths/work-power-virtual-agents/) |
| Copilot Studio community | [community.powerplatform.com](https://community.powerplatform.com/galleries/communitycontent/?v=copilot-studio) |
| Power Automate community | [community.powerplatform.com](https://community.powerplatform.com/galleries/communitycontent/?v=power-automate) |

---

{: .highlight }
> **"The era of non-developers building agents — today you became the first."**

[← Back to Home]({{ site.baseurl }}/en/)
