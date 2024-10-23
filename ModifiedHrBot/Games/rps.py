import random
from highrise import BaseBot, User
import asyncio

class RPS:

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.lock = asyncio.Lock()  # Create a lock to prevent command overlap

    async def handle_command(self, user: User, message: str):
        try:
            if message.lower().startswith("!rps"):
                async with self.lock:  # Ensure one user at a time processes the command
                    choices = ['rock', 'paper', 'scissors']
                    client_chosen = random.choice(choices)
                    option = message[5:].strip().lower()
                    user_name = user.username

                    # Debug: Print user details and message
                    print(f"Handling RPS command for user: {user_name} with message: {message}")

                    text_to_emoji = {"rock": "✊", "paper": "✋", "scissors": "✌️"}

                    if option not in choices:
                        response = f"Invalid command usage:\nExample: !rps <{random.choice(choices)}>\nAvailable Options:\n{', '.join(choices)}"
                        await self.bot.highrise.send_whisper(user.id, response)
                        return

                    # Notify that the user has made a choice
                    await self.bot.highrise.chat(f"@{user_name} has chosen {option.capitalize()} {text_to_emoji[option]}! Let's see how it goes...")

                    # Animation for rock-paper-scissors
                    animation_steps = ["✊...", "✋...", "✌️..."]
                    for step in animation_steps:
                        await self.bot.highrise.chat(step)
                        await asyncio.sleep(1)  # 1-second delay between each step

                    # Determine the result
                    if option == client_chosen:
                        result = f"{user_name}, it's a tie! 🤝"
                    elif (option == "rock" and client_chosen == "scissors") or (option == "paper" and client_chosen == "rock") or (option == "scissors" and client_chosen == "paper"):
                        result = f"Congratulations, {user_name}! You won this round! 🎉"
                    else:
                        result = f"Sorry, {user_name}, you lost this time. 😢"

                    # Debug: Print the chosen options
                    print(f"{user_name} chose {option}, Bot chose {client_chosen}")

                    # Show result with emojis
                    response = f"{result}\nYou: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
                    await self.bot.highrise.chat(response)

                    # Wait for 2 seconds before allowing the next user to play
                    await asyncio.sleep(2)

        except Exception as e:
            # Log the error and notify the user
            print(f"Error in handle_command for user {user.username}: {e}")
            await self.bot.highrise.send_whisper(user.id, "An error occurred while processing your command. Please try again later.")








