---
title: "M8. Deployment"
nav_order: 9
lang: en
---

# Publish & Deploy — Teams + Copilot
{: .no_toc }

| Time | Duration | Student Role |
|:-----|:-----|:-----------|
| 15:10 | 20 min | 🟢 Hands-on |

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## What You'll Learn in This Module

- **Publishing** an agent from Copilot Studio
- **Deploying to Teams** and chatting with it directly
- Using the agent via **@mention** in M365 Copilot
- Understanding the concept of **re-publishing**

---

## 4 Deployment Channels

| Channel | Best For | Today's Practice |
|:-----|:---------|:---------|
| **Microsoft Teams** | Internal team use, collaboration tool integration | ✅ Practice |
| SharePoint page | Embed in company portal | Introduction only |
| **M365 Copilot @mention** | Quick use (in-context) | ✅ Practice |
| Website embed | For external customers | Introduction only |

---

## Practice ①: Publish

### Step-by-Step

1. Copilot Studio → Agent editing screen
2. Click **"Publish"** in the top right
3. Publish confirmation dialog → Click **"Publish"**
4. Publishing complete (1–2 minutes)

{: .highlight }
> Publishing = creating the agent's **deployed version**. Without publishing, it's only usable in the test panel.

---

## Practice ②: Deploy to Teams

### Step-by-Step

1. Copilot Studio → Left menu **"Channels"**
2. Click **"Microsoft Teams"**
3. Enable **"Available in Teams"**
4. Save settings
5. Open **Teams app** → Search for the agent by name
6. **Start chatting with the agent!**

---

## Practice ③: Test @mention

1. Open M365 Copilot chat (Teams or browser)
2. Type: `@agentname Tell me where to use welfare points`
3. Confirm the agent responds

{: .tip }
> @mention is the **in-context** method from M2. It's convenient for quick questions during other work.

---

## Sharing After Deployment

To share the agent with colleagues:
- Agent **Settings → Share** → Enter colleague's email
- Or an admin can **deploy to the entire organization**

---

## Re-publishing

{: .important }
> **Deployment is not one-time.** Every time you modify the agent, you must publish again for it to be reflected in Teams.

After adding a Flow in M9 → Click **Publish again**
→ New features immediately reflected in the Teams agent.

---

## Key Takeaways

1. **Publish** = create the deployed version of the agent
2. **Teams deployment** = teammates can use it right away
3. **@mention** = quick questions in Copilot chat
4. **Always re-publish after modifications**

---

## FAQ

| Question | Answer |
|:-----|:-----|
| The agent isn't showing in Teams | It takes 1–3 minutes after publishing. Try searching again. |
| @mention isn't working | Check: is it published? Is the Copilot channel activated? Check admin policy. |
| Can other teammates use it right away? | You can add them in Share settings or deploy to the entire organization. |
| Can I undo deployment? | You can deactivate it from Channels or switch the agent to unpublished state. |

---

## Reference Materials

| Resource | Link |
|:-----|:-----|
| Agent publishing basics | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/publication-fundamentals-publish-channels) |
| Deploy agent to Teams | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/publication-add-bot-to-microsoft-teams) |
| Connect M365 Copilot agent | [learn.microsoft.com](https://learn.microsoft.com/microsoft-365-copilot/extensibility/) |
| Share and collaborate on agents | [learn.microsoft.com](https://learn.microsoft.com/microsoft-copilot-studio/admin-share-bots) |

---

Next module: [M9. Flow + Email Forwarding](m09-flow-card)
