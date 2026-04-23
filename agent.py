import os
from dotenv import load_dotenv
from tavily import TavilyClient
from groq import Groq

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_internships(role: str, location: str = "remote") -> list:
    query = f"{role} internship {location} 2025 apply"
    results = tavily.search(
        query=query,
        max_results=6,
        search_depth="advanced"
    )
    return results.get("results", [])

def format_internships_with_groq(role: str, raw_results: list) -> str:
    results_text = ""
    for i, r in enumerate(raw_results, 1):
        results_text += f"""
Result {i}:
Title: {r.get('title', 'N/A')}
URL: {r.get('url', 'N/A')}
Content: {r.get('content', 'N/A')[:500]}
---"""

    prompt = f"""You are an internship opportunity finder assistant.
The user is looking for: {role} internships

Here are raw web search results:
{results_text}

Your job:
1. Extract ONLY actual internship opportunities
2. For each internship provide:
   - Company Name
   - Role/Position
   - Location (or Remote)
   - How to Apply (URL)
   - Key Skills Required
3. Skip anything that is NOT a real internship listing
4. Number each internship clearly
5. Add a Quick Tips section at the end with 2-3 tips for {role} internships

Be concise and practical."""

    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500
    )
    return response.choices[0].message.content

def run_agent(role: str, location: str = "remote") -> dict:
    raw_results = search_internships(role, location)

    if not raw_results:
        return {
            "role": role,
            "location": location,
            "formatted_output": "No results found. Try a different role or location.",
            "raw_results": []
        }

    formatted = format_internships_with_groq(role, raw_results)

    return {
        "role": role,
        "location": location,
        "formatted_output": formatted,
        "raw_results": raw_results
    }