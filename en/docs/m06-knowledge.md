---
title: "M6. Connecting Knowledge"
nav_order: 7
lang: en
---

# Connecting Textbooks — Direct File Upload
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 13:40 | 45 min | 🟢 Hands-on |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- Connect knowledge sources to Copilot Studio by **directly uploading files**
- Experience **before/after answer quality comparison** after adding knowledge sources
- Understand the differences between 4 knowledge connection methods
- How **document structure** affects answer quality

---

## You Can Only Answer What You Know

In M5 you wrote the instructions (job posting).
Now it's time to give the new employee a **textbook**.

| State | Analogy | Agent's Response |
|:-----|:-----|:------------|
| Instructions only | New hire with just a job posting | "I'm unable to give an accurate answer..." |
| Instructions **+ Knowledge** | New hire with job posting + textbook | "According to the document..." (accurate and specific) |

{: .highlight }
> **Good textbooks → good answers.** This is the real-world application of "different ingredients, different answers" from M1.

---

## 4 Knowledge Connection Methods

| Method | Difficulty | Kept Current | Access Control | Recommended |
|:-----|:------|:---------|:---------|:-----|
| **File Upload** ← today's practice | ⭐ Easy | Manual | ❌ | ✅ **Step 1 for beginners** |
| Website URL | ⭐⭐ | Periodic | ❌ | Step 2 |
| SharePoint | ⭐⭐⭐ | Automatic | ✅ | Production stage |
| Dataverse | ⭐⭐⭐ | Real-time | ✅ | Advanced |

{: .tip }
> We start with **file upload** today. It's the easiest and fastest. Switch to SharePoint for production operations.

---

## Practice: File Upload

### 5 Documents to Upload

| File | Content | Format |
|:-------|:-----|:-----|
| FAQ.docx | Frequently asked questions and answers | Q&A structured |
| ContactInfo.docx | Department contacts: names and numbers | Table format |
| BenefitsGuide.docx | Welfare points, health checkups, congratulation/condolence | Narrative |
| ExpenseGuide.docx | Business travel, corporate card, billing procedures | Narrative |
| LeaveGuide.docx | Annual leave, half-day leave, sick leave, special leave | Narrative |

### Step-by-Step

1. **Copilot Studio** → Edit agent → Left menu **"Knowledge"** click
2. Select **"File upload"**
3. **Drag & drop** or select all 5 files
4. Wait until each file status shows **"Ready"** (1–3 minutes)
5. Once Ready is confirmed, **knowledge source activation complete!**

---

## Test: Before vs After

Check how the same question's answer changes before and after uploading files.

| # | Question | Before Upload | After Upload |
|:--|:-----|:---------|:---------|
| 1 | "How many vacation days do I have?" | ❌ "I'm unable to answer" | ✅ Specific answer based on FAQ.docx + citation |
| 2 | "Who handles expense reimbursement?" | ❌ "I'll connect you with the right contact" | ✅ Name and contact from ContactInfo.docx |
| 3 | "Where can I use welfare points?" | ❌ "I can't find the information" | ✅ Detailed answer from BenefitsGuide.docx |
| 4 | "How do I claim business travel expenses?" | ❌ (unable to answer) | ✅ Procedure guide from ExpenseGuide.docx |

{: .important }
> The Before/After difference is **the power of the textbook**. The same agent becomes completely different after adding knowledge.

---

## Best Practices for Writing Documents

For the agent to answer more accurately, **document structure** matters.

| Principle | Description | Example |
|:-----|:-----|:-----|
| **Q&A structure** | Write in question-answer pairs | Q: How many vacation days? A: 15 days. |
| **Clear headings** | Use section titles and subheadings | `## Benefits` → `### Welfare Points` |
| **Use tables** | Structured data in tables | Contacts, phone numbers, etc. |
| **Short sentences** | Under 50 words per sentence | Clarity over long sentences |

{: .tip }
> **Structured documents (Q&A, tables) > Narrative documents** — AI gives more accurate answers from structured information.

---

## Key Takeaways

1. Knowledge = textbook — **good textbook → good answers**
2. File upload is the **easiest and fastest** starting point
3. **Q&A structure + table** format documents are optimal
4. Confirm effectiveness with the Before/After test

---

## FAQ

| Question | Answer |
|:-----|:-----|
| Can I upload PDFs? | Yes. Word, PDF, TXT, and Excel are all supported. |
| If I replace a file later, will it be reflected? | Manual update is needed. Delete the old file and upload the new one. |
| Is there a file size limit? | Yes. Split large files for upload. |
| Is it okay to upload confidential documents? | It's only used within Copilot Studio. M365 security policies apply. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Connecting knowledge sources | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-copilot-studio) |
| File upload knowledge source | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/knowledge-add-file-upload) |
| Knowledge document best practices | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/guidance/building-agents-knowledge) |

---

Next module: [M7. Topics + Variables](m07-topic-variables)
