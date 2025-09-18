# Wikipedia Search ReAct Agent

A ReAct (Reasoning and Acting) agent that searches Wikipedia iteratively until finding exact answers, built with Google's Agent Development Kit.

## How It Works

The Wikipedia agent uses a **LoopAgent pattern** that searches iteratively and refines queries until finding the exact answer.

**Pattern**: LoopAgent with iterative search and exit condition
```
User Question → LoopAgent → Wikipedia Agent → Search → Evaluate → Continue/Exit
```

## Architecture Diagram

```
👤 User Input                🤖 Agents                      🔧 Tools
┌─────────────┐             ┌──────────────────┐           ┌─────────────────┐
│ 💬 Query:   │────────────▶│ 🔄 LoopAgent     │──────────▶│ 🔍 wikipedia_   │
│ "When did   │             │ (Controller)     │           │    search()     │
│  Gandhi     │             │ • Max 5 loops    │           │                 │
│  die?"      │             │ • Exit control   │           │ 🛑 exit_loop()  │
└─────────────┘             └──────────────────┘           └─────────────────┘
                                      │                             ▲
                                      ▼                             │
                            ┌──────────────────┐                   │
                            │ 🧠 Wikipedia     │───────────────────┘
                            │    Agent (LLM)   │
                            │ • Searches       │
                            │ • Evaluates      │
                            │ • Decides        │
                            └──────────────────┘
                                      │
                                      ▼
                            ⚙️ Process Flow:
                            ┌──────────────────┐
                            │ 1. 🔍 Search     │
                            │ 2. 📊 Evaluate   │
                            │ 3. 🤔 Decide:    │
                            │    ✅ Exit or    │
                            │    🔄 Refine     │
                            └──────────────────┘
                                      │
                                      ▼
                            ┌──────────────────┐
                            │ 📝 Final Answer: │
                            │ "January 30,     │
                            │  1948"           │
                            └──────────────────┘
```

## Component Breakdown

### 🤖 Agents
| Component | Icon | Purpose |
|-----------|------|---------|
| **LoopAgent** | 🔄 | Controls iteration loop (max 5 attempts) |
| **Wikipedia Agent** | 🧠 | LLM that searches and evaluates results |

### 🔧 Tools
| Tool | Icon | Purpose |
|------|------|---------|
| **wikipedia_search()** | 🔍 | Queries Wikipedia API and returns summaries |
| **exit_loop()** | 🛑 | Terminates the loop when answer found |

### ⚙️ Process Flow
| Step | Icon | Action |
|------|------|--------|
| **Search** | 🔍 | Query Wikipedia with current search terms |
| **Evaluate** | 📊 | Assess if result answers the question |
| **Decide** | 🤔 | Either exit with answer or refine query |

## Setup

1. Add your Google Gemini API key to `.env`:
   ```
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

## Usage

### Start the server:
```bash
adk web --port 8000
```

### Example queries:
- "When did Gandhi die?"
- "What is the capital of France?"
- "Who invented the telephone?"

The agent will:
1. Search Wikipedia with your question
2. Evaluate if the result answers your question completely
3. If not satisfied, refine the search query and try again
4. Stop when exact answer is found or max iterations reached

## Files Structure
```
React/
├── wikipedia_agent/
│   ├── agent.py       # LoopAgent + Wikipedia agent
│   ├── tools.py       # Wikipedia search tool
│   └── __init__.py    # Package exports
├── pyproject.toml     # Dependencies
└── README.md         # This file
```

This demonstrates the ReAct pattern for iterative search and refinement until finding precise answers.