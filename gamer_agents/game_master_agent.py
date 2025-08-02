# # from agents import Agent, handoff
# # from gamer_agents.narrator_agent import NarratorAgent
# # from gamer_agents.monster_agent import MonsterAgent
# # from gamer_agents.item_agent import ItemAgent

# # GameMasterAgent = Agent(
# #     name="GameMasterAgent",
# #     instructions=(
# #         "You are the game master controlling the fantasy adventure game. "
# #         "Ask the player for their choices and game actions. "
# #         "Always hand off to the correct agent based on game phase:\n"
# #         "- To NarratorAgent for storytelling and events.\n"
# #         "- To MonsterAgent for combat.\n"
# #         "- To ItemAgent for inventory and rewards.\n"
# #         "Never answer directly. Only delegate properly."
# #     ),
# #     handoffs=[
# #         handoff(NarratorAgent, on_handoff=lambda ctx: print("🔄 Handing off to NarratorAgent")),
# #         handoff(MonsterAgent, on_handoff=lambda ctx: print("🔄 Handing off to MonsterAgent")),
# #         handoff(ItemAgent, on_handoff=lambda ctx: print("🔄 Handing off to ItemAgent")),
# #     ]
# # )
# from agents import Agent, handoff
# from gamer_agents.narrator_agent import NarratorAgent
# from gamer_agents.monster_agent import MonsterAgent
# from gamer_agents.item_agent import ItemAgent

# GameMasterAgent = Agent(
#     name="GameMasterAgent",
#     instructions="""
#     You are the game master controlling the fantasy adventure game.
#     Your role is to guide the player by asking for their choices and game actions.
#     You MUST NEVER answer the player's requests directly yourself.
#     Instead, always hand off the conversation to the appropriate specialized agent based on the current game phase:
#     - Hand off to NarratorAgent for storytelling, world events, and narration.
#     - Hand off to MonsterAgent for managing combat sequences and dice rolls.
#     - Hand off to ItemAgent for inventory management, rewards, and item descriptions.
#     Make sure to delegate every player input properly and do not provide any direct responses.
#     """,
#     handoffs=[
#         handoff(NarratorAgent, on_handoff=lambda ctx: print("🔄 Handing off to NarratorAgent")),
#         handoff(MonsterAgent, on_handoff=lambda ctx: print("🔄 Handing off to MonsterAgent")),
#         handoff(ItemAgent, on_handoff=lambda ctx: print("🔄 Handing off to ItemAgent")),
#     ]
# )

# Import necessary classes and functions from the agents library
from agents import Agent, handoff

# Import your custom specialized agents for the fantasy adventure game
from gamer_agents.narrator_agent import NarratorAgent     # Handles storytelling and world narration
from gamer_agents.monster_agent import MonsterAgent       # Handles combat logic and enemy interactions
from gamer_agents.item_agent import ItemAgent             # Handles inventory, items, and rewards

# Define the main agent that controls the overall game flow
GameMasterAgent = Agent(
    name="GameMasterAgent",  # Name of the agent
    instructions="""
    You are the game master controlling the fantasy adventure game.
    Your role is to guide the player by asking for their choices and game actions.
    You MUST NEVER answer the player's requests directly yourself.
    
    Instead, always hand off the conversation to the appropriate specialized agent based on the current game phase:
    - Hand off to NarratorAgent for storytelling, world events, and narration.
    - Hand off to MonsterAgent for managing combat sequences and dice rolls.
    - Hand off to ItemAgent for inventory management, rewards, and item descriptions.
    
    Make sure to delegate every player input properly and do not provide any direct responses.
    """,

    # Define handoffs to specialized agents with optional logging
    handoffs=[
        handoff(NarratorAgent, on_handoff=lambda ctx: print("🔄 Handing off to NarratorAgent")),
        handoff(MonsterAgent, on_handoff=lambda ctx: print("🔄 Handing off to MonsterAgent")),
        handoff(ItemAgent, on_handoff=lambda ctx: print("🔄 Handing off to ItemAgent")),
    ]
)
