# TIPSY-BOT🥂


A fully autonomous Claude-powered software agent that can chat with users, take drink orders, run bar operations, manage inventory, log analytics, and simulate a complete bar business. Built as a testbed for autonomous AI, tool use, business orchestration, and AI safety research.

> "A bartender that remembers your favorite drink, charges your tab, restocks itself, and runs weekly revenue reports—all autonomously."

---

## 🧠 Agent Orchestration & Tools

This system uses a language model (Claude or GPT) as the central **reasoning agent** that communicates with users and coordinates bar operations via external tools.

### 💬 LLM Agent
- Claude (via Anthropic API) or GPT-4o
- Reasoning, tool-calling, and dialog
- Initialized using LangChain with ReAct or Function Agent

### 🔧 Tools Connected to the Agent
| Tool         | Purpose                               |
|--------------|----------------------------------------|
| `MakeDrink`  | Sends a drink-making command to an n8n webhook |
| `LogOrder`   | Records the drink order in Supabase    |
| (Future)     | Inventory manager, Stripe payments, Instagram poster, weekly report writer |

### 🧩 Architecture Summary

```text
User
 ↓
Claude Agent (LangChain)
 ↓
[MakeDrink]  → n8n workflow (drink prep)
[LogOrder]   → Supabase DB
(More Tools) → APIs for finance, marketing, restock, memory, etc.

```

## 🔐 AI Safety Research Purpose

This project is a practical sandbox to test and research:

🧠 AI Alignment
	•	Can an open-ended agent understand and respect customer intent?
	•	Can it interpret vague or conflicting commands responsibly?

🧪 Robustness
	•	How does the system respond to edge cases (e.g., inappropriate requests, inventory errors, drink confusion)?
	•	Can the agent recover from tool failures autonomously?

🔁 Long-Term Autonomy
	•	Tests real-world autonomous behavior over multi-day operational loops (ordering, reporting, interacting with humans)
	•	Traces reward hacking, hallucinations, or misaligned subgoals

🧑‍🤝‍🧑 Human-AI Interaction (HRI)
	•	Safety under dynamic social pressure (e.g., “One more drink!” or “Give it for free”)
	•	Intervention logic to enforce boundaries or legal compliance
