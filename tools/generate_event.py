# from agents import function_tool
# import random

# EVENTS = [
#     "A sudden storm forces you to seek shelter.",
#     "You find an ancient artifact glowing with magic.",
#     "A band of goblins ambushes you!",
#     "You discover a hidden path leading to a treasure.",
# ]

# @function_tool
# def generate_event(context: str) -> str:
#     """Generate a random event or description based on context."""
#     event = random.choice(EVENTS)
#     return f"Event for '{context}': {event}"

from agents import function_tool
import random

# Predefined list of possible game events or descriptions
EVENTS = [
    "A sudden storm forces you to seek shelter.",
    "You find an ancient artifact glowing with magic.",
    "A band of goblins ambushes you!",
    "You discover a hidden path leading to a treasure.",
]

@function_tool
def generate_event(context: str) -> str:
    """
    Generate a random game event or description based on the given context.
    The context is a string describing the current game situation or location.
    
    Returns a string describing the event.
    """
    event = random.choice(EVENTS)
    return f"Event for '{context}': {event}"
