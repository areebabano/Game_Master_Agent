# 🎮 **Game Master Agent**
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/Chainlit-UI-purple?logo=chainlit&logoColor=white)](https://docs.chainlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Agent-orange?logo=openai&logoColor=white)](https://platform.openai.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

Welcome to the Game Master Agent — an AI-powered text adventure game master that narrates an immersive story based on your commands!
Built with Python, Chainlit, and powered by the Gemini API for smart AI-driven gameplay.

## 🚀 **Project Overview**
This project is a text-based adventure game where you play by typing commands like go north, look around, or pick up torch.
The Game Master Agent interprets your actions, updates the game world, and responds with vivid descriptions and options — just like a Dungeon Master in tabletop RPGs!

## ⚙️ **Features**
🎲 Interactive text adventure game experience

🤖 AI-powered narration and game logic using Gemini API

💡 State tracking for game world and player inventory

👾 Handles player commands and updates game state dynamically

💬 Built-in Chainlit UI for smooth chat-based gameplay

## 📂 **Project Structure**
plaintext
Copy
Edit
gamer_master_agent/
│
├── tool/
│   └── game_master_agent.py       # Core Game Master AI agent
│
├── ui/
│   └── chainlit_app.py            # Chainlit chat interface
│
├── .env                          # Environment variables (Gemini API key)
├── requirements.txt               # Python dependencies
└── README.md                     # Project documentation

## ⚙️ **Setup & Installation**
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/gamer_master_agent.git
cd gamer_master_agent
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Add your Gemini API key:

Create a .env file in the root directory:

ini
Copy
Edit
GEMINI_API_KEY=your_gemini_api_key_here
Run the Chainlit app:

bash
Copy
Edit
chainlit run ui/chainlit_app.py
Open your browser at http://localhost:8000 and start your adventure!

## 🎮 **How to Play**
Greet the game master by typing: hi or hello

Use commands like:

look — to get a description of your surroundings

go north / go south / go east / go west — to move

inventory — to check your items

pick up <item> — to collect objects

use <item> — to interact with objects

The Game Master will respond with descriptions, options, and story progression.

## 🛠️ **Technologies Used**
Python — Main programming language

Chainlit — For building the interactive chat UI

OpenAI Agents SDK — To build and manage the AI agent logic

Gemini API — AI model powering game narration and decision making

python-dotenv — For managing environment variables securely

## 🤝 **Contributing**
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## 📜 **License**
This project is licensed under the MIT License.

## 🙏 **Acknowledgments**
Inspired by classic text adventure games and powered by modern AI technologies. Thanks to the Chainlit and Gemini API teams for making this possible!
