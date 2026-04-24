# Task Decomposition & Specs

## Agent 1 — Search Agent
- Input: Role (string), Location (string)
- Tool Used: Tavily Search API
- Process: Searches web for internship listings
- Output: List of 6 raw search results
- Decision Point: If no results found → return error message

## Agent 2 — Formatter Agent
- Input: Role (string), Raw search results (list)
- Tool Used: Groq LLaMA 3.1 8B
- Process: LLM reads raw results, extracts only real internships
- Output: Clean numbered list with company, role, location, apply link
- Decision Point: If result is not real internship → skip it

## Agent 3 — Judge Agent (LLM-as-Judge)
- Input: Role, Location, Formatted output from Agent 2
- Tool Used: Groq LLaMA 3.1 8B (separate LLM call)
- Process: Evaluates output against 5-criteria rubric
- Output: JSON scores (1-5) for each criterion + overall score
- Decision Point: If JSON parse fails → return N/A fallback

## Rubric Criteria
1. Result Relevance
2. Information Completeness
3. Formatting Clarity
4. Actionability
5. Tips Quality

## Flow
User Input → Search Agent → Formatter Agent → Judge Agent → UI