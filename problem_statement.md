# Problem Statement — Internship Opportunity Finder

## The User
Engineering students in 3rd and 4th year actively looking for internships.

## The Problem
Students waste hours manually searching across LinkedIn, Internshala, 
Naukri etc. Results are often outdated, irrelevant, or missing key 
details like apply links and required skills.

## The Solution
An AI-powered Internship Opportunity Finder agent that:
- Takes a role/skill and location as input
- Searches the web in real time using Tavily Search
- Uses Groq LLaMA to extract and format only real internship listings
- Evaluates its own output quality using an LLM-as-Judge

## Why Agentic?
A single prompt cannot handle this because:
1. It requires real-time web search (external tool use)
2. It requires reasoning to filter fake vs real listings
3. It requires self-evaluation of output quality
These are multi-step, tool-using, reasoning tasks — exactly what 
an agentic approach is designed for.