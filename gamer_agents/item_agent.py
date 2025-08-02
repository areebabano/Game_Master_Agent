# # from agents import Agent
# # from tools.generate_event import generate_event

# # ItemAgent = Agent(
# #     name="ItemAgent",
# #     instructions=(
# #         "You manage player inventory and rewards. "
# #         "When describing items or effects, ALWAYS call the 'generate_event(context)' tool to get item descriptions and flavor text. "
# #         "Do not invent item details yourself. "
# #         "Never answer without calling the tool."
# #     ),
# #     tools=[generate_event]
# # )


# from agents import Agent
# from tools.generate_event import generate_event

# ItemAgent = Agent(
#     name="ItemAgent",
#     instructions="""
#     You manage the player's inventory and rewards. 
#     Whenever you describe any item or effect, you MUST call the 'generate_event(context)' tool to get 
#     accurate and creative item descriptions. 
#     You are NOT allowed to make up any item details yourself. 
#     ALWAYS call this tool before answering the user. 
#     Do NOT respond without calling the tool.
#     """,
#     tools=[generate_event]
# )

# Import the base Agent class from the agents module
from agents import Agent

# Import the generate_event tool which will provide item descriptions and flavor text
from tools.generate_event import generate_event

# Define the ItemAgent responsible for managing inventory and rewards
ItemAgent = Agent(
    name="ItemAgent",  # Name of the agent

    # Instructions provided to the agent describing its responsibilities and behavior
    instructions="""
    You manage the player's inventory and rewards. 
    Whenever you describe any item or effect, you MUST call the 'generate_event(context)' tool to get 
    accurate and creative item descriptions. 
    You are NOT allowed to make up any item details yourself. 
    ALWAYS call this tool before answering the user. 
    Do NOT respond without calling the tool.
    """,

    # Assign the generate_event tool so the agent can use it to fetch item details
    tools=[generate_event]
)
