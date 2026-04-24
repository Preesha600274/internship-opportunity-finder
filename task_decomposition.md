📌 Task Decomposition
Project: Internship Opportunity Finder
1. Overview
The system follows a modular, agent-based architecture where each core file performs a specific responsibility. The workflow ensures that user queries are processed, evaluated, and returned as relevant internship opportunities.
2. Core Components and Responsibilities

🔹 2.1 Orchestrator Agent
File: agent.py
Purpose:
Acts as the central decision-making unit that controls the overall workflow of the system.
Key Responsibilities:
Interpret user input (skills, interests, preferences)
Decompose the request into smaller tasks
Determine the sequence of operations (fetch → filter → rank)
Coordinate with the evaluation module (judge.py)
Aggregate and format the final results
Core Functions:
Task decomposition
Workflow management
Data processing and integration

🔹 2.2 Evaluation and Ranking Agent
File: judge.py
Purpose:
Ensures that the output internships are relevant, high-quality, and properly ranked.
Key Responsibilities:
Evaluate internships based on user requirements
Match user skills with internship criteria
Assign relevance scores to each opportunity
Rank results in descending order of suitability
Filter out irrelevant or low-priority listings
Core Functions:
Scoring mechanism
Skill-based matching
Ranking and filtering logic

🔹 2.3 Backend Controller
File: app.py
Purpose:
Serves as the entry point of the system, handling communication between the user and backend logic.
Key Responsibilities:
Receive user requests through API endpoints
Validate and process input data
Invoke the orchestrator agent (agent.py)
Return structured responses to the user
Manage application routing and execution
Core Functions:
API handling (request/response cycle)
Server-side routing
Integration with backend modules

3. System Workflow
The user submits a query containing preferences such as skills or domain
app.py receives and forwards the request to the system
agent.py analyzes the request and breaks it into manageable tasks
Relevant internship data is processed and refined
judge.py evaluates and ranks the results
The final, sorted list of internships is returned to the user

4. Final Output
A structured list of internship opportunities
Ranked based on relevance and user preferences
Filtered to ensure quality and accuracy