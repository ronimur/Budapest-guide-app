# Budapest Guide 🇭🇺

A personal AI travel guide for Budapest powered by 3 agents with distinct personalities. Ask anything — where to eat, what to do, where to work out — and get recommendations from 3 different lenses simultaneously.

## Agents

| Agent | Persona | Style |
|---|---|---|
| 🗺️ **Viktor** | Professional tourist guide | Searches in English, high ratings, TripAdvisor top picks |
| 🏠 **Zsuzsi** | Budapest local, 20 years in the city | Searches in Hungarian, hidden gems tourists never find |
| 💪 **Áron** | Fitness-obsessed Budapest local | Gyms with day passes, bike rentals, running routes, active experiences |

## Tech Stack

- **Agents:** [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) with built-in WebSearchTool
- **Model:** `gpt-4o-mini`
- **Server:** FastAPI + uvicorn
- **Frontend:** Single `index.html` — warm editorial design, mobile-first
- **GPS:** Browser Geolocation API → passed to agents for location-aware recommendations

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo "OPENAI_API_KEY=sk-..." > .env

# Run the server
python3 -m uvicorn server:app --host 0.0.0.0 --port 8000
```

Open in browser: `http://localhost:8000`

From phone (same WiFi): `http://<your-machine-ip>:8000`

## Example Queries

- *"Where should I eat near Buda Castle?"*
- *"I want to work out today — gym with a day pass"*
- *"What should I do this evening?"*
- *"Best coffee near me"*
- *"Bike rental near me"*

## Project Structure

```
budapest-guide/
├── personas/
│   ├── viktor.py        # Tourist guide agent
│   ├── zsuzsi.py        # Local Hungarian agent
│   ├── aron.py          # Fitness & activities agent
│   └── orchestrator.py  # Routing logic + parallel execution
├── server.py            # FastAPI server
├── index.html           # Chat UI
└── requirements.txt
```
