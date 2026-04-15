# Market Research Assistant

A full-stack market research planning application that helps users generate structured research plans from a topic prompt. The project uses a FastAPI backend and a React frontend to support research planning, topic classification, starter source generation, and persistent report history.

## Features

### Backend
- FastAPI API for research plan generation
- Rule-based topic classification:
  - company
  - market
  - comparison
  - general
- Structured research plan generation
- Keyword generation
- Suggested source categories
- Starter source link generation
- Report persistence using a local JSON file
- Retrieve all saved reports
- Retrieve a report by ID
- Delete one report
- Clear all reports

### Frontend
- React UI built with Vite
- Topic input form
- Generate report button
- Display generated research plans
- Saved reports sidebar
- Click to reopen a saved report
- Delete individual reports
- Clear all saved reports
- Selected report highlighting

---

## Tech Stack

### Frontend
- React
- Vite
- CSS

### Backend
- Python
- FastAPI
- Uvicorn
- Pydantic

### Storage
- Local JSON file (`data/reports.json`)

### Tooling
- Git
- GitHub
- npm

---

## Project Structure

```bash
market-research-assistant-api/
├── app/
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── schemas.py
│   ├── services/
│   │   ├── planner.py
│   │   ├── sources.py
│   │   └── storage.py
│   └── main.py
├── data/
│   └── reports.json
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── ...
│   ├── package.json
│   └── ...
├── .gitignore
├── README.md
└── requirements.txt
```
How It Works
1. The user enters a topic in the React frontend.
2. The frontend sends a POST /plan request to the FastAPI backend.
3. The backend:
  - classifies the topic
  - generates a structured research plan
  - builds keyword suggestions
  - recommends starter sources
  - saves the report to local storage
4. The frontend displays the saved report.
5. Users can also:
  - browse saved reports
  - reopen a report
  - delete one report
  - clear all saved reports

Example Topics
- IBM AI strategy
- AWS vs Azure
- cloud security market
- predictive analytics
- NVIDIA market strategy

API Endpoints
Health Check
  - GET /health
Generate and Save Report
  - POST /plan
Request body:
{
  "topic": "IBM AI strategy"
}

Get All Reports
  - GET /reports

Get Report by ID
  - GET /reports/{report_id}

Delete One Report
  - DELETE /reports/{report_id}

Clear All Reports
  - DELETE /reports

Example Response
```
{
  "report_id": "555e9a31-de42-42ae-a559-f6ab75a5c820",
  "topic": "AWS vs Azure",
  "research_type": "comparison",
  "subquestions": [
    "What are the core offerings of each side in AWS vs Azure?",
    "What are the main differences in pricing, features, or positioning in AWS vs Azure?",
    "What types of customers are best served by each option in AWS vs Azure?",
    "What are the strengths and weaknesses of each side in AWS vs Azure?",
    "What trends or market forces affect the comparison in AWS vs Azure?"
  ],
  "report_outline": [
    "Comparison Overview",
    "Core Offerings",
    "Target Customers",
    "Strengths and Weaknesses",
    "Market Implications"
  ],
  "keywords": [
    "AWS",
    "Azure",
    "AWS vs Azure",
    "AWS vs Azure features",
    "AWS vs Azure pricing",
    "AWS vs Azure differences"
  ],
  "next_step": "Next, review both sides using product, pricing, and documentation sources.",
  "suggested_sources": [
    "Official product pages",
    "Pricing pages",
    "Technical documentation",
    "Comparison articles"
  ],
  "starter_sources": [
    {
      "label": "Comparison search",
      "url": "https://www.google.com/search?q=AWS+vs+Azure+comparison"
    },
    {
      "label": "Pricing comparison search",
      "url": "https://www.google.com/search?q=AWS+vs+Azure+pricing"
    }
  ]
}
```

Running the Project Locally

1. Clone the repository
```
git clone https://github.com/tjain010/market-research-assistant-api.git
cd market-research-assistant-api
```
2. Set up the backend

Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```

Install backend dependencies:
```
pip install -r requirements.txt
```

3. Start the FastAPI backend
```
uvicorn app.main:app --reload
```

Backend will run at:

http://127.0.0.1:8000

FastAPI docs will be available at:

http://127.0.0.1:8000/docs

4. Set up the React frontend

Open a new terminal, then run:
```
cd frontend
npm install
npm run dev
```

Frontend will run at:
```
http://localhost:5173
```
Current State
The current version supports:
  - full-stack topic submission
  - backend planning and classification
  - persistent local report storage
  - sidebar-based saved report browsing
  - report deletion and clearing

**Why This Project**

This project was built to demonstrate:
  - backend API development with FastAPI
  - frontend integration with React
  - structured planning workflows
  - topic classification logic
  - local persistence and report history
  - scalable project organization for future AI-assisted research tooling

Planned Improvements
  - add timestamps to saved reports
  - add report search/filtering in the sidebar
  - improve keyword cleanup
  - replace JSON storage with PostgreSQL or MongoDB
  - add real external source retrieval APIs
  - add optional LLM-based summarization
  - add authentication for user-specific report history

**What I Learned**

Through this project, I learned how to:  
  - build and structure a FastAPI backend
  - design request and response schemas with Pydantic
  - separate route logic, planning logic, source generation, and storage
  - connect a React frontend to a backend API
  - manage cross-origin requests with CORS
  - persist and retrieve structured data
  - incrementally grow a project from a simple API into a full-stack app
