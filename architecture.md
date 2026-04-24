# Architecture

## System Flow
User Input (Role + Location)
        ↓
Agent 1 — Search Agent (Tavily Search API)
        ↓ Raw Results
Agent 2 — Formatter Agent (Groq LLaMA)
        ↓ Formatted Internships
Agent 3 — Judge Agent (Groq LLaMA)
        ↓ Scores + Evaluation
Streamlit UI — Final Display

## Tech Stack
- Frontend: Streamlit
- LLM: Groq LLaMA 3.1 8B (free)
- Search Tool: Tavily Search API
- Language: Python
- Deployment: Streamlit Cloud
