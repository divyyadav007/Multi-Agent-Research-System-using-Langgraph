# Multi-Agent Research System using LangGraph

A production-inspired Multi-Agent Research System built with LangGraph, Mistral AI, and Tavily Search that combines human oversight, parallel research execution, and automated fact verification to generate reliable technical research reports.

Unlike traditional single-prompt AI workflows, this system uses a stateful multi-agent architecture where specialized agents collaborate to plan, research, analyze, write, and validate information before producing a final report.

---

## 🚀 Key Features

### Stateful Multi-Agent Architecture

Engineered using LangGraph to move beyond simple linear chains into a flexible cyclic state machine with persistent state tracking.

### Human-in-the-Loop Interruption

Uses graph compilation breakpoints to safely pause execution, allowing users to review, approve, reject, or modify AI-generated research plans before research begins.

### Concurrent Map-Reduce Execution

Leverages LangGraph's Send API to spawn isolated parallel worker states for multiple subtopics, enabling concurrent web research and analysis.

### Dual-Layer Data Refinement

Combines Tavily Search API results with a dedicated Analyst Agent that transforms noisy web content into structured, high-density technical insights.

### Automated Verification Gate

Includes a Fact Checker Agent that evaluates generated reports against source information and automatically requests rewrites when inconsistencies are detected.

### Recursive Self-Correction Loop

Reports failing validation are routed back to the Writer Agent with targeted feedback, creating an iterative quality improvement cycle.

---

## 📐 System Architecture

<img width="2100" height="2026" alt="image" src="https://github.com/user-attachments/assets/da0889fe-a3a9-4263-b409-9159d6bb9368" />

---

## 🔄 Workflow

### 1. Planning Phase

The Planner Agent receives the user's research topic and generates a set of focused research subtopics.

### 2. Human Approval Phase

Execution pauses before research begins. Users can:

* Approve the generated plan
* Reject the plan
* Replace subtopics manually

This ensures research remains aligned with user intent.

### 3. Parallel Research Phase

The graph fans out into multiple concurrent researcher nodes using LangGraph's Send API.

Each researcher:

* Searches the web using Tavily
* Collects relevant information
* Passes findings to an Analyst Agent

### 4. Analysis Phase

The Analyst Agent extracts:

* Key facts
* Important statistics
* Technical insights
* Relevant observations

while filtering noise from raw search results.

### 5. Aggregation Phase

Results from parallel branches are automatically merged using state reducers powered by:

```python
Annotated[list, operator.add]
```

### 6. Report Generation

The Writer Agent synthesizes all collected insights into a structured markdown report.

### 7. Fact Verification

The Fact Checker Agent reviews the generated report against gathered research data.

### 8. Self-Correction Loop

If inconsistencies are detected:

```text
Writer → Fact Checker → Writer
```

The report is revised until approval is granted.

### 9. Final Output

A verified markdown research report is returned to the user.

---

## 🛠️ Tech Stack

### AI Frameworks

* LangGraph
* LangChain

### Language Models

* Mistral AI

### Search & Research

* Tavily Search API

### Programming Language

* Python

### State Management

* LangGraph StateGraph
* MemorySaver Checkpointing

### Environment Management

* UV Package Manager
* Python Virtual Environment
* python-dotenv

---

## 📂 Project Structure

```text
├── agents
│   ├── analyst.py
│   ├── fact_checker.py
│   ├── planner.py
│   ├── researcher.py
│   └── writer.py
│
├── graph
│   └── workflow.py
│
├── main.py
├── state.py
├── pyproject.toml
└── README.md
```

### File Descriptions

| File            | Purpose                                      |
| --------------- | -------------------------------------------- |
| planner.py      | Generates research subtopics                 |
| researcher.py   | Performs web searches                        |
| analyst.py      | Extracts high-value insights                 |
| writer.py       | Creates structured reports                   |
| fact_checker.py | Validates report accuracy                    |
| workflow.py     | Defines graph architecture                   |
| state.py        | Defines graph state schemas                  |
| main.py         | Handles user interaction and graph execution |

---

## 🎯 Skills Demonstrated

This project showcases:

* Multi-Agent Systems
* Agent Orchestration
* LangGraph State Management
* Human-in-the-Loop AI
* Concurrent Processing
* Parallel Graph Execution
* Research Automation
* AI Workflow Engineering
* Prompt Engineering
* LLM Application Development
* State Machines
* Verification Pipelines
* Recursive Agent Loops

---

## ⚡ Engineering Challenges Solved

### Parallel State Aggregation

Managing multiple concurrent research branches while preserving state consistency and merging outputs correctly.

### Human Approval Workflow

Implementing graph interruption points that allow runtime modification of agent-generated plans.

### Hallucination Reduction

Building a dedicated verification layer capable of detecting inconsistencies and triggering targeted report rewrites.

### Stateful Orchestration

Maintaining graph-wide context across multiple execution paths while preserving agent isolation.

---

## 📸 Demo

### Example Research Query

```text
Future of Agentic AI
```

### System Execution

1. Planner generates subtopics
2. User reviews and approves plan
3. Parallel researchers gather data
4. Analysts extract insights
5. Writer drafts report
6. Fact Checker validates output
7. Final verified report generated

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/divyyadav007/Multi-Agent-Research-System-using-Langgraph.git

cd Multi-Agent-Research-System-using-Langgraph
```

### Configure Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Install Dependencies

```bash
uv sync
```

---

## ▶️ Running the Project

```bash
uv run main.py
```

---

## 🧠 Human Intervention Layer

When the Planner Agent generates subtopics, execution pauses and prompts:

```text
Do you approve these subtopics? (Y/N)
```

### If Approved

```text
Y
```

Research proceeds automatically.

### If Rejected

```text
N
```

Users can provide custom subtopics, and the graph updates its internal state dynamically before continuing execution.

---

## 📈 Future Enhancements

* FastAPI Backend
* Docker Containerization
* LangSmith Tracing
* Vector Database Memory
* Source Citation Tracking
* Retry Mechanisms
* Streaming Responses
* Multi-LLM Routing
* Cloud Deployment
* Monitoring & Observability
* Evaluation Framework
* Persistent Database Storage

---

## 💡 Why This Project?

Most AI applications rely on a single-agent architecture where planning, reasoning, research, and writing happen inside one prompt.

This project demonstrates how specialized AI agents can collaborate through a stateful orchestration framework to perform complex research tasks more effectively, transparently, and reliably.

The system combines:

* Agent specialization
* Human oversight
* Parallel execution
* State management
* Automated verification

to create a more robust research workflow.

---

## 👨‍💻 Author

**Divyansh Yadav**

B.Tech – CSE(Artificial Intelligence)

Interested in:

* Generative AI
* AI Engineering
* Multi-Agent Systems
* Agentic Workflows
* LLM Applications
* AI Product Development

GitHub: https://github.com/divyyadav007
