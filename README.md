# AI Chatbot — Groq + Llama-3.3-70b-versatile (FastAPI + Streamlit)

A simple **AI chatbot** with a **FastAPI backend** and a **Streamlit frontend**, using **Groq** as the LLM provider and the **`llama-3.3-70b-versatile`** model.

This repo is structured so the backend API (chat endpoint + agent logic) lives in `app/` and `agents/`, while the UI is in `front/`.

---

## Project Structure

```bash
AI Chatbot/
├── agents/
│   ├── ai_agents.py        # Agent logic / orchestration
│   ├── llm_provider.py     # Groq + model wrapper
│   └── tools.py            # Tools (search, utilities, etc.)
├── app/
│   ├── config.py           # Settings / env loading
│   ├── model.py            # Pydantic models (request/response)
│   └── route.py            # FastAPI routes (e.g., /chat)
├── front/
│   └── app.py              # Streamlit UI
├── .env                    # Local environment variables (not committed)
├── main.py                 # FastAPI entrypoint
├── README.md
└── requirements.txt
```

---

## Requirements

* Python **3.10+**
* A **Groq API key**

---

## Setup

### 1) Create & activate a virtual environment

**Windows (PowerShell)**

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root (same level as `main.py`).

Example:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

**Notes**

* `GROQ_API_KEY` is required.
* `GROQ_MODEL` is optional if your code defaults to `llama-3.3-70b-versatile`.

If your `app/config.py` expects different names, keep the `.env` keys aligned with it.

---

## Run the Backend (FastAPI)

From the project root:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* API: `http://localhost:8000`
* Docs (Swagger): `http://localhost:8000/docs`

---

## Run the Frontend (Streamlit)

Open a second terminal (same venv) and run:

```bash
streamlit run front/app.py
```

Streamlit runs at:

* `http://localhost:8501`

---

## API Overview

### Chat Endpoint

Your FastAPI routes are defined in `app/route.py`, and request/response schemas in `app/model.py`.



## Where Things Live

* **`main.py`**
  FastAPI entrypoint (creates `app`, includes routers).

* **`app/route.py`**
  API endpoints (e.g., `POST /chat`) that call into the agent/LLM.

* **`agents/llm_provider.py`**
  Groq client + model selection (`llama-3.3-70b-versatile`).

* **`agents/ai_agents.py`**
  Agent logic: prompt routing, memory, tool calls, etc.

* **`agents/tools.py`**
  Helper tools (search, calculators, retrieval hooks, etc.).

* **`front/app.py`**
  Streamlit UI: chat input, message rendering, calling the backend.

---




Add a `LICENSE` file (MIT/Apache-2.0/etc.) if you plan to share publicly.
