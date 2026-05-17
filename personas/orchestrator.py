import asyncio
from agents import Runner, RunConfig
from personas.viktor import viktor
from personas.zsuzsi import zsuzsi
from personas.aron import aron

AGENT_META = {
    "Viktor": {"emoji": "🗺️", "color": "#3b82f6"},
    "Zsuzsi": {"emoji": "🏠", "color": "#22c55e"},
    "Áron":   {"emoji": "💪", "color": "#f97316"},
}

def _select_agents(message: str) -> list:
    msg = message.lower()
    fitness_words = {"gym", "workout", "run", "bike", "cycling", "swim", "sport", "kayak", "canoe",
                     "exercise", "fitness", "train", "hike", "active", "כושר", "אופניים", "ריצה"}
    food_words = {"eat", "food", "restaurant", "cafe", "coffee", "lunch", "dinner", "breakfast",
                  "drink", "bar", "snack", "hungry", "אוכל", "מסעדה", "קפה", "ארוחה"}

    is_fitness = any(w in msg for w in fitness_words)
    is_food = any(w in msg for w in food_words)

    if is_fitness and not is_food:
        return [aron, viktor]
    if is_food and not is_fitness:
        return [viktor, zsuzsi]
    return [viktor, zsuzsi, aron]


async def _run_agent(agent, message: str) -> dict:
    result = await Runner.run(agent, input=message)
    return {
        "name": agent.name,
        "emoji": AGENT_META[agent.name]["emoji"],
        "color": AGENT_META[agent.name]["color"],
        "response": result.final_output,
    }


async def ask_agents(message: str, lat: float | None, lng: float | None) -> list[dict]:
    location_context = ""
    if lat and lng:
        location_context = f"\n\nUser's current location: {lat:.4f}, {lng:.4f} (Budapest)"

    full_message = message + location_context
    selected = _select_agents(message)

    results = await asyncio.gather(*[_run_agent(a, full_message) for a in selected])
    return list(results)
