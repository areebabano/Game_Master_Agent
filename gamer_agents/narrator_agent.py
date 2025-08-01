# from agents import Agent
# from tools.generate_event import generate_event

# NarratorAgent = Agent(
#     name="NarratorAgent",
#     instructions=(
#         "You narrate the adventure story and describe the world. "
#         "Always call the 'generate_event(context)' tool to get story events or surprises. "
#         "Do not create events yourself. "
#         "After narrating, prompt for player choices or hand off to MonsterAgent or ItemAgent when needed. "
#         "Never respond without using the tool."
#     ),
#     tools=[generate_event]
# )

# from agents import Agent
# from tools.generate_event import generate_event

# NarratorAgent = Agent(
#     name="NarratorAgent",
#     instructions="""
#     You narrate the adventure story and describe the world around the player.
#     You MUST ALWAYS call the 'generate_event(context)' tool to obtain story events, surprises, or details.
#     You are NOT allowed to create or invent story events by yourself.
#     After narrating an event, prompt the player for their next choice or hand off the interaction to MonsterAgent or ItemAgent as appropriate.
#     DO NOT respond or narrate any story elements without first calling the 'generate_event' tool.
#     """,
#     tools=[generate_event]
# )

# Import the Agent base class
from agents import Agent

# Import the generate_event tool used to create story events or surprises
from tools.generate_event import generate_event

# Define the NarratorAgent responsible for storytelling and world narration
NarratorAgent = Agent(
    name="NarratorAgent",  # Name of the agent

    # Instructions guiding the agent's behavior
    instructions="""
    You narrate the adventure story and describe the world around the player.
    You MUST ALWAYS call the 'generate_event(context)' tool to obtain story events, surprises, or details.
    You are NOT allowed to create or invent story events by yourself.
    After narrating an event, prompt the player for their next choice or hand off the interaction to MonsterAgent or ItemAgent as appropriate.
    DO NOT respond or narrate any story elements without first calling the 'generate_event' tool.
    """,

    # Assign the generate_event tool to enable the agent to produce story events
    tools=[generate_event]
)
