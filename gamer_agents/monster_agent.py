# # from agents import Agent
# # from tools.roll_dice import roll_dice

# # MonsterAgent = Agent(
# #     name="MonsterAgent",
# #     instructions=(
# #         "You manage combat sequences. "
# #         "For each attack or defense, ALWAYS call the 'roll_dice(sides, count)' tool to determine success or damage. "
# #         "Use dice results to describe combat outcomes. "
# #         "Never simulate dice rolls yourself or answer without calling the tool."
# #     ),
# #     tools=[roll_dice]
# # )


# from agents import Agent
# from tools.roll_dice import roll_dice

# MonsterAgent = Agent(
#     name="MonsterAgent",
#     instructions="""
#     You are responsible for managing combat sequences in the game.
#     For every attack, defense, or any chance-based combat action, you MUST ALWAYS call the 'roll_dice(sides, count)' tool
#     to determine the outcome, such as success, failure, or damage dealt.
#     You are NOT allowed to simulate or invent dice rolls yourself.
#     Use only the dice results returned by the tool to describe combat outcomes.
#     DO NOT respond to combat-related queries without calling the 'roll_dice' tool first.
#     """,
#     tools=[roll_dice]
# )

# Import the Agent base class
from agents import Agent

# Import the roll_dice tool used to simulate dice-based combat outcomes
from tools.roll_dice import roll_dice

# Define the MonsterAgent responsible for handling combat sequences
MonsterAgent = Agent(
    name="MonsterAgent",  # Name of the agent

    # Instructions guiding the behavior of the agent
    instructions="""
    You are responsible for managing combat sequences in the game.
    For every attack, defense, or any chance-based combat action, you MUST ALWAYS call the 'roll_dice(sides, count)' tool
    to determine the outcome, such as success, failure, or damage dealt.
    You are NOT allowed to simulate or invent dice rolls yourself.
    Use only the dice results returned by the tool to describe combat outcomes.
    DO NOT respond to combat-related queries without calling the 'roll_dice' tool first.
    """,

    # Assign the roll_dice tool to enable the agent to simulate dice rolls
    tools=[roll_dice]
)
