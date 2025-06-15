
def generate_ideas(theme):
    # Mock response for prototype
    return {"theme": theme, "ideas": [f"{theme} Idea {i}" for i in range(1, 11)]}

def map_idea(idea):
    return {
        "idea": idea,
        "components": [
            {"name": "Frontend", "description": f"Interface for {idea}"},
            {"name": "Backend", "description": f"API handling for {idea}"},
            {"name": "Database", "description": f"Data storage for {idea}"}
        ]
    }
