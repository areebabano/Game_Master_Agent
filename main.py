import os
from dotenv import load_dotenv  # Load environment variables from .env file
import chainlit as cl           # Chainlit framework for chat UI
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled
from gamer_agents.game_master_agent import GameMasterAgent  # Your main agent coordinating career guidance

# Load environment variables (like API keys)
load_dotenv()

# Disable internal tracing/logging for cleaner output (optional)
set_tracing_disabled(True)

# Initialize the OpenAI-compatible async client with Gemini API key and base URL
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  # Fetch API key from environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Initialize the OpenAI chat model with the async client
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Specify model version
    openai_client=external_client,
)

# Configuration for running the agent, including model and client details
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@cl.on_chat_start
async def start():
    await cl.Message(content="🧙‍♂️ Welcome to the Fantasy Adventure! Ready to begin your quest?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    result = Runner.run_sync(GameMasterAgent, user_input, run_config=config)
    await cl.Message(content=result.final_output).send()
