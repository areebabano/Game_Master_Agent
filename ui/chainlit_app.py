import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tool.game_master_agent import GameMasterAgent

agent = GameMasterAgent()

@cl.on_message
async def main(message: cl.Message):
    response = await agent.handle_command(message.content)
    await cl.Message(content=response).send()
