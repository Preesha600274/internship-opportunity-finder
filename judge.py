import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_judge(role: str, location: str, agent_output: str) -> dict:
    prompt = f"""You are a strict quality evaluator for an AI internship finder.

Evaluate this output for the query: "{role}" internships in "{location}".

=== AGENT OUTPUT ===
{agent_output}

Score each criterion 1-5:

1. RESULT_RELEVANCE: Are results actually internships for the requested role?
2. INFORMATION_COMPLETENESS: Do listings have company, role, location, apply link?
3. FORMATTING_CLARITY: Is output easy to read and well structured?
4. ACTIONABILITY: Can user immediately apply from this output?
5. TIPS_QUALITY: Are the tips specific and useful?

You MUST return ONLY a valid JSON object exactly like this, no extra text, no markdown, no backticks:
{{"scores": {{"result_relevance": {{"score": 4, "reasoning": "your reason here"}}, "information_completeness": {{"score": 3, "reasoning": "your reason here"}}, "formatting_clarity": {{"score": 4, "reasoning": "your reason here"}}, "actionability": {{"score": 3, "reasoning": "your reason here"}}, "tips_quality": {{"score": 4, "reasoning": "your reason here"}}}}, "overall_score": 4, "summary": "your summary here", "top_strength": "best thing about output", "top_improvement": "what to improve"}}"""

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a JSON-only response bot. You never output anything except valid JSON. No markdown, no backticks, no explanation."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1000,
        temperature=0.1
    )

    raw = response.choices[0].message.content.strip()

    # Clean any markdown if present
    if "```" in raw:
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Try to find JSON in the response
        try:
            start = raw.index("{")
            end = raw.rindex("}") + 1
            return json.loads(raw[start:end])
        except:
            return {
                "scores": {},
                "overall_score": "N/A",
                "summary": "Judge could not parse output.",
                "top_strength": "N/A",
                "top_improvement": "N/A"
            }