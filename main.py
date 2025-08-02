# import os
# from dotenv import load_dotenv  # Load environment variables from .env file
# import chainlit as cl           # Chainlit framework for chat UI
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled
# from gamer_agents.game_master_agent import GameMasterAgent  # Your main agent coordinating career guidance

# # Load environment variables (like API keys)
# load_dotenv()

# # Disable internal tracing/logging for cleaner output (optional)
# set_tracing_disabled(True)

# # Initialize the OpenAI-compatible async client with Gemini API key and base URL
# external_client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),  # Fetch API key from environment variables
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # Initialize the OpenAI chat model with the async client
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.0-flash",  # Specify model version
#     openai_client=external_client,
# )

# # Configuration for running the agent, including model and client details
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# @cl.on_chat_start
# async def start():
#     await cl.Message(content="🧙‍♂️ Welcome to the Fantasy Adventure! Ready to begin your quest?").send()

# @cl.on_message
# async def handle_message(message: cl.Message):
#     user_input = message.content
#     result = Runner.run_sync(GameMasterAgent, user_input, run_config=config)
#     await cl.Message(content=result.final_output).send()

import os
from dotenv import load_dotenv
import chainlit as cl
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, set_tracing_disabled
from gamer_agents.game_master_agent import GameMasterAgent  # Your main coordinating agent

# Load .env variables (e.g., GEMINI_API_KEY)
load_dotenv()

# Optionally disable internal tracing/logging for cleaner output
set_tracing_disabled(True)

# Initialize async OpenAI client with Gemini API and your API key
external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Create the chat completions model instance using Gemini API
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

# Configure Runner with the model and client
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Chainlit event: When chat starts, send a welcome message
@cl.on_chat_start
async def start():
    await cl.Message(content="🧙‍♂️ Welcome to the Fantasy Adventure! Ready to begin your quest?").send()

# Chainlit event: On user message, pass input to GameMasterAgent and send response
@cl.on_message
async def handle_message(message: cl.Message):
    user_input = message.content
    # Run the synchronous agent runner with the input and config
    result = Runner.run_sync(GameMasterAgent, user_input, run_config=config)
    # Send the agent's final output back to the user
    await cl.Message(content=result.final_output).send()
