# from agents import Agent
# from tools.generate_event import generate_event

# ItemAgent = Agent(
#     name="ItemAgent",
#     instructions=(
#         "You manage player inventory and rewards. "
#         "When describing items or effects, ALWAYS call the 'generate_event(context)' tool to get item descriptions and flavor text. "
#         "Do not invent item details yourself. "
#         "Never answer without calling the tool."
#     ),
#     tools=[generate_event]
# )


from agents import Agent
from tools.generate_event import generate_event

ItemAgent = Agent(
    name="ItemAgent",
    instructions="""
    You manage the player's inventory and rewards. 
    Whenever you describe any item or effect, you MUST call the 'generate_event(context)' tool to get 
    accurate and creative item descriptions. 
    You are NOT allowed to make up any item details yourself. 
    ALWAYS call this tool before answering the user. 
    Do NOT respond without calling the tool.
    """,
    tools=[generate_event]
)
