# Game Master Agent - Fantasy Adventure Game

Welcome to the **Game Master Agent**, an AI-powered text-based fantasy adventure game!

## Overview

This project implements a multi-agent system to run an interactive fantasy adventure game. The player experiences a rich narrative, combat sequences, and inventory management through AI agents working together.

### Key Features

- **NarratorAgent:** Narrates the adventure story and generates immersive events.
- **MonsterAgent:** Manages combat by rolling dice to simulate attack and defense outcomes.
- **ItemAgent:** Handles inventory, rewards, and item descriptions using event generation.
- **GameMasterAgent:** Controls the overall game flow and hands off tasks to the appropriate agents.
- **Tools:**  
  - `roll_dice(sides, count)`: Simulates dice rolls for combat.  
  - `generate_event(context)`: Creates story events, surprises, and item descriptions.

## How It Works

1. **User Input:** The player inputs commands or choices.
2. **GameMasterAgent:** Routes requests to the correct agent based on context.
3. **Agents & Tools:** Each agent processes the request, calling tools as needed to generate dynamic responses.
4. **Responses:** The system replies with narrative descriptions, combat results, or item details.

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
pip install -r requirements.txt

javascript
Copy
Edit
4. Set up your `.env` file with API keys if required.
5. Run the application:
chainlit run main.py

shell
Copy
Edit

## Example Interaction

🧙‍♂️ Welcome to the Fantasy Adventure! Ready to begin your quest?

Let's start the adventure.
(NarratorAgent narrates an event.)
I want to attack the goblin.
(MonsterAgent rolls dice and reports combat results.)
What reward did I get?
(ItemAgent describes the reward using generated events.)

yaml
Copy
Edit

## Contribution

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

[MIT License](LICENSE)
