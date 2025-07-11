import os
from dotenv import load_dotenv
from openai import AsyncOpenAI

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("❌ GEMINI_API_KEY is missing from .env")

# Initialize AsyncOpenAI client with Gemini API key
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",  # Gemini base URL
)

class GameMasterAgent:
    def __init__(self):
        self.state = "You are standing in a dark forest. There is a path to the north."
        self.inventory = []

    async def call_ai_api(self, prompt: str) -> str:
        try:
            response = await client.chat.completions.create(
                model="gemini-2.0-flash",  # Or gemini-2.0-flash if available
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Game Master for a text adventure game."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    },
                ],
                max_tokens=150,
                temperature=0.7,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"⚠️ Gemini API Error: {e}"

    async def handle_command(self, command: str) -> str:
        command = command.strip().lower()

        # Handle greetings
        if command in ["hi", "hello", "hey", "hy"]:
            return (
                "👋 Hello adventurer! Welcome to your journey.\n"
                "You can try commands like:\n"
                "`look`, `go north`, `inventory`, `pick up torch`, `open door`, etc."
            )

        prompt = (
            f"Game State: {self.state}\n"
            f"Inventory: {self.inventory}\n"
            f"Player Command: {command}\n"
            "Respond with the next game description and available actions."
        )
        response = await self.call_ai_api(prompt)
        self.state = response
        return response
