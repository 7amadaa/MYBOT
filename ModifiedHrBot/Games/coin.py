import random
from highrise import BaseBot, User
import asyncio

class Coin:

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.lock = asyncio.Lock()  # Create a lock to prevent command overlap

    async def handle_command(self, user: User, message: str):
        if message.lower().startswith("!coin"):
            async with self.lock:  # Ensure one user at a time processes the command
                choices = ['heads', 'tails']
                coin_toss_result = random.choice(choices)
                user_guess = message[6:].strip().lower()
                user_name = user.username  # Updated to use {user.username}

                # Handle invalid guess
                if user_guess not in choices:
                    invalid_responses = [
                        f"Oops, {user_name}! You need to choose either *Heads* or *Tails*. Try again! 😅",
                        f"Hey {user_name}, that's not how this game works! You can only pick *Heads* or *Tails*! 🎲",
                        f"{user_name}, looks like you got a bit confused. The options are *Heads* and *Tails*. Give it another shot! 🤔",
                        f"Invalid guess, {user_name}. You're supposed to pick either *Heads** or *Tails*. Try again! 😄"
                    ]
                    await self.bot.highrise.send_whisper(user.id, random.choice(invalid_responses))
                    return

                # Notify the user that the coin toss is starting
                await self.bot.highrise.chat(f"{user_name} has tossed the coin! 🪙")

                # Simulate a "coin spinning" animation with increasing dots
                spin_phases = ["🌀 Spinning.", "🌀 Spinning..", "🌀 Spinning..."]

                for spin_text in spin_phases:
                    await self.bot.highrise.chat(spin_text)
                    await asyncio.sleep(1)  # 1-second delay between each message

                # Additional delay before showing the result
                await asyncio.sleep(2)

                # Winning responses
                if user_guess == coin_toss_result:
                    win_responses = [
                        f"🎉 Amazing, {user_name}! You nailed it! It's *{coin_toss_result.capitalize()}*! 🪙",
                        f"🌟 Bravo {user_name}! *{coin_toss_result.capitalize()}* it is! Luck's on your side today! 🍀",
                        f"🥳 You called it, {user_name}! *{coin_toss_result.capitalize()}*! Keep that winning streak going!",
                        f"🔥 Unbelievable, {user_name}! You guessed *{coin_toss_result.capitalize()}* right! Keep that energy going! 💪",
                        f"✨ Jackpot, {user_name}! The coin landed on *{coin_toss_result.capitalize()}*! You're on fire! 🔥",
                        f"🌈 What a guess, {user_name}! It's *{coin_toss_result.capitalize()}*! The stars aligned just for you today! ✨",
                        f"🎯 Bullseye, {user_name}! The coin says *{coin_toss_result.capitalize()}*! You're crushing it! 💸"
                    ]
                    result_response = random.choice(win_responses)
                    await self.bot.highrise.chat(result_response)

                # Losing responses
                else:
                    lose_responses = [
                        f"😕 So close, {user_name}, but it's *{coin_toss_result.capitalize()}*. Better luck next time!",
                        f"🙃 Not this time, {user_name}. The coin landed on *{coin_toss_result.capitalize()}*. You'll get it next time!",
                        f"😣 Tough luck, {user_name}. It came up *{coin_toss_result.capitalize()}*. Maybe next toss!",  # Updated emoji
                        f"😢 Oh no, {user_name}! It landed on *{coin_toss_result.capitalize()}*. Don't worry, you can try again!",  # Updated emoji
                        f"😞 Ahh, close call, {user_name}. The coin says *{coin_toss_result.capitalize()}**. Lady luck wasn’t on your side this time!",  # Updated emoji
                        f"😩 Dang, {user_name}! The coin landed on *{coin_toss_result.capitalize()}*. You'll get 'em next time!"  # Updated emoji
                    ]
                    result_response = random.choice(lose_responses)
                    await self.bot.highrise.chat(result_response)

                # Wait for 2 seconds before allowing the next user to play
                await asyncio.sleep(2)


