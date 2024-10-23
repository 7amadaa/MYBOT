import logging
import random
import textwrap
import json
import os
from highrise import BaseBot, User
from owner import OWNER_USER

class HangmanGame:
    SCORES_FILE = 'scores.json'
    USER_DATA_FILE = 'user_data.json'  # Not used anymore but can be removed if not needed

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.reset_game()
        self.load_scores()

    def reset_game(self):
        self.hangman_game = {
            'word': None,
            'guessed': [],
            'attempts': 0,
            'wrong_guesses': [],
            'players': set(),
            'category': None
        }
        self.words = {
    "Fruits": [
        "apple", "banana", "cherry", "grape", "orange", "peach",
        "strawberry", "watermelon", "kiwi", "mango", "pineapple",
        "blueberry", "raspberry", "papaya", "apricot", "coconut",
        "blackberry", "fig", "date", "lemon", "plum",
        "tangerine", "guava", "jackfruit", "currant", "melon",
        "nectarine", "clementine"
    ],
    "Animals": [
        "elephant", "giraffe", "kangaroo", "tiger", "dolphin",
        "penguin", "flamingo", "zebra", "rhino", "hippo",
        "crocodile", "alligator", "chameleon", "octopus", "sparrow",
        "squirrel", "buffalo", "panda", "koala", "ostrich",
        "sloth", "walrus", "dog", "cat", "rabbit", "mouse"
    ],
    "Colors": [
        "red", "blue", "green", "yellow", "purple", "orange",
        "pink", "brown", "black", "white", "gray", "cyan",
        "gold", "silver", "beige", "lavender", "peach"
    ],
    "Countries": [
        "brazil", "canada", "france", "italy", "japan",
        "kenya", "mexico", "spain", "sweden", "thailand",
        "germany", "india", "australia", "netherlands", "norway",
        "portugal", "switzerland", "argentina", "southafrica",
        "greece", "turkey", "china", "russia", "usa"
    ],
    "Objects": [
        "umbrella", "backpack", "pillow", "computer", "notebook",
        "television", "toaster", "microwave", "scissors", "keyboard",
        "phone", "wallet", "bicycle", "flashlight", "camera",
        "table", "chair", "glasses", "mirror", "clock",
        "calculator", "ring", "necklace", "spoon", "fork", "knife"
    ],
    "Foods": [
        "pizza", "hamburger", "sushi", "spaghetti", "taco",
        "sandwich", "salad", "cake", "ice cream", "cookies",
        "pancake", "waffle", "donut", "chocolate", "curry",
        "biryani", "pasta", "quiche", "gelato", "meatball",
        "toast", "rice", "fruit", "vegetable"
    ],
    "Nature": [
        "mountain", "river", "ocean", "forest", "desert",
        "garden", "lake", "island", "beach", "hill",
        "field", "jungle", "tree", "flower", "grass"
    ],
    "Emotions": [
        "happiness", "sadness", "anger", "fear", "surprise",
        "joy", "disgust", "love", "confusion", "excitement",
        "anxiety", "relief", "frustration", "contentment", "curiosity",
        "boredom", "hope", "trust"
    ],
    "Vegetables": [
        "carrot", "broccoli", "spinach", "potato", "tomato", "cucumber",
        "pepper", "onion", "garlic", "lettuce", "cauliflower",
        "eggplant", "zucchini", "radish", "celery", "pumpkin",
        "peas", "corn", "beet", "squash"
    ],
    "Sports": [
        "soccer", "basketball", "baseball", "tennis", "cricket", 
        "hockey", "golf", "swimming", "running", "cycling",
        "volleyball", "badminton", "boxing", "skiing", "surfing",
        "gymnastics", "skating"
    ],
    "Music": [
        "rock", "jazz", "classical", "hip-hop", "reggae", 
        "blues", "pop", "folk", "country", "metal",
        "dance", "swing", "march"
    ],
    "Transportation": [
        "car", "bus", "train", "airplane", "bicycle", "motorcycle", 
        "boat", "subway", "scooter", "taxi", "truck", "van"
    ],
    "Occupations": [
        "doctor", "teacher", "engineer", "artist", "chef", 
        "musician", "scientist", "writer", "nurse", "firefighter",
        "police", "farmer", "driver", "cleaner", "shopkeeper"
    ],
    "Hobbies": [
        "painting", "gardening", "photography", "cooking", 
        "hiking", "fishing", "reading", "writing", "crafting",
        "drawing", "singing", "playing games"
    ],
    "Instruments": [
        "piano", "guitar", "violin", "flute", "trumpet", 
        "drum", "saxophone", "clarinet", "ukulele", "harmonica"
    ],
    "Weather": [
        "sunny", "rainy", "cloudy", "snowy", "windy", 
        "foggy", "stormy", "hot", "cool", "cold",
        "dry", "humid"
    ]
}
        self.max_attempts = 6

    def load_scores(self):
        if os.path.exists(self.SCORES_FILE):
            try:
                with open(self.SCORES_FILE, 'r') as f:
                    try:
                        self.scores = json.load(f)
                        if not isinstance(self.scores, dict):
                            print(f"Invalid format in {self.SCORES_FILE}. Initializing scores.")
                            self.scores = {}
                    except json.JSONDecodeError:
                        print(f"Invalid JSON in {self.SCORES_FILE}. Initializing scores.")
                        self.scores = {}
                        self.save_scores()  # Overwrite with empty dict
            except Exception as e:
                print(f"Error loading scores: {e}")
                self.scores = {}
        else:
            self.scores = {}
            self.save_scores()  # Create the file with empty dict

    def save_scores(self):
        try:
            with open(self.SCORES_FILE, 'w') as f:
                json.dump(self.scores, f, indent=4)
        except Exception as e:
            print(f"Error saving scores: {e}")

    def add_point(self, user: User, points: int = 1):
        user_id = str(user.id)
        username = user.username
        if user_id in self.scores:
            self.scores[user_id]['score'] += points
            self.scores[user_id]['username'] = username  # Update username in case it changed
        else:
            self.scores[user_id] = {'username': username, 'score': points}
        self.save_scores()

    def get_leaderboard(self, top_n: int = 10):
        # Sort users by score in descending order
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1]['score'], reverse=True)
        return sorted_scores[:top_n]

    async def send_message(self, message: str):
        try:
            for chunk in textwrap.wrap(message, 256):
                await self.bot.highrise.chat(chunk)
        except Exception as e:
            print(f"An error occurred while sending a message: {e}")

    async def start_hangman(self, user: User):
        try:
            if self.hangman_game['word'] is None:
                available_categories = [category for category, words in self.words.items() if words]
                if not available_categories:
                    await self.bot.highrise.chat("No words available to start the game.")
                    return

                category = random.choice(available_categories)  # Randomly choose a category
                word = random.choice(self.words[category]).lower()
                self.hangman_game['word'] = word
                self.hangman_game['guessed'] = ['_'] * len(word)
                self.hangman_game['attempts'] = 0
                self.hangman_game['wrong_guesses'] = []
                self.hangman_game['category'] = category

            self.hangman_game['players'].add(user.id)
            message = (
                f"@{user.username} started a new Hangman game!\n"
                f"The word is:\n{' '.join(self.hangman_game['guessed'])}\n"
                f"Use !guess <letter> to guess a letter or !word <your guess> to guess the full word!"
            )
            await self.bot.highrise.chat(message)
        except Exception as e:
            logging.error(f"Error starting the game: {e}")
            await self.bot.highrise.chat(f"An error occurred while starting the game: {e}")

    async def guess_letter(self, user: User, letter: str):
        try:
            if self.hangman_game['word'] is None:
                await self.bot.highrise.chat(f"@{user.username} you need to start a new game with !hangman.")
                return

            if letter in self.hangman_game['guessed'] or letter in self.hangman_game['wrong_guesses']:
                await self.bot.highrise.chat(f"@{user.username} you already guessed '{letter}'. Try a different letter.")
                return

            if letter in self.hangman_game['word']:
                for i, l in enumerate(self.hangman_game['word']):
                    if l == letter:
                        self.hangman_game['guessed'][i] = letter
                self.add_point(user, 1)
                message = (
                    f"✅ Correct guess, @{user.username}! You earned 1 point.\n"
                    f"The word so far:\n{' '.join(self.hangman_game['guessed'])}"
                )
                await self.bot.highrise.chat(message)
            else:
                self.hangman_game['wrong_guesses'].append(letter)
                self.hangman_game['attempts'] += 1
                message = (
                    f"❌ Wrong guess, @{user.username}. Attempts left: {self.max_attempts - self.hangman_game['attempts']}.\n"
                    f"Wrong guesses: {', '.join(self.hangman_game['wrong_guesses'])}"
                )
                await self.bot.highrise.chat(message)

            # Check if the players won or lost
            if '_' not in self.hangman_game['guessed']:
                message = f"🎉 Congratulations to all players, you won! The word was '{self.hangman_game['word']}'."
                await self.bot.highrise.chat(message)
                self.reset_game()  # Reset the game state
            elif self.hangman_game['attempts'] >= self.max_attempts:
                message = f"😞 Sorry, you lost. The word was '{self.hangman_game['word']}'."
                await self.bot.highrise.chat(message)
                self.reset_game()  # Reset the game state
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while processing your guess: {e}")

    async def guess_word(self, user: User, guess: str):
        try:
            if self.hangman_game['word'] is None:
                await self.bot.highrise.chat(f"@{user.username} you need to start a new game with !hangman.")
                return

            guess = guess.lower()
            if guess == self.hangman_game['word']:
                # Calculate points: equal to the number of letters left to guess
                points_awarded = self.hangman_game['guessed'].count('_')
                self.add_point(user, points_awarded)
                message = (
                    f"🎉 @{user.username} guessed the word correctly and earned {points_awarded} points!\n"
                    f"The word was '{self.hangman_game['word']}'. Congratulations!"
                )
                await self.bot.highrise.chat(message)
                self.reset_game()
            else:
                self.hangman_game['attempts'] += 1
                message = (
                    f"😞 @{user.username} guessed the word incorrectly. Attempts left: {self.max_attempts - self.hangman_game['attempts']}."
                )
                await self.bot.highrise.chat(message)

                if self.hangman_game['attempts'] >= self.max_attempts:
                    message = f"😞 Sorry, you lost. The word was '{self.hangman_game['word']}'."
                    await self.bot.highrise.chat(message)
                    self.reset_game()
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while processing your word guess: {e}")

    async def provide_hint(self, user: User):
        try:
            if self.hangman_game['word'] is None:
                await self.bot.highrise.chat(f"@{user.username} you need to start a new game with !hangman.")
                return

            message = f"🔍 @{user.username} the category of the word is: **{self.hangman_game['category']}**"
            await self.bot.highrise.chat(message)
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while providing a hint: {e}")

    async def show_leaderboard(self):
        try:
            leaderboard = self.get_leaderboard()
            if not leaderboard:
                message = "\n🥇 No scores to display yet 🥇"
            else:
                message = "\n🥇__Top 10 Hangman Scorers__🥇\n"  # Removed leading newline
                for idx, (user_id, data) in enumerate(leaderboard, start=1):
                    username = data.get('username', 'Unknown')
                    score = data.get('score', 0)
                    message += f"{idx}. @{username}: {score} points\n"
            await self.bot.highrise.chat(message)
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while displaying the leaderboard: {e}")

    async def clear_scores(self, user: User):
        try:
            privilege_response = await self.bot.highrise.get_room_privilege(user.id)
            if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
                return

            self.scores = {}
            self.save_scores()
            await self.bot.highrise.chat(f"📉 @{user.username} has cleared all hangman scores.")
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while clearing scores: {e}")

    async def handle_command(self, user: User, message: str):
        try:
            if message.lower().startswith("!hangman"):
                await self.start_hangman(user)
            elif message.lower().startswith("!guess"):
                parts = message.split()
                if len(parts) < 2:
                    await self.bot.highrise.chat(f"@{user.username} please provide a letter to guess. Usage: !guess <letter>")
                    return
                letter = parts[1].strip().lower()
                if len(letter) != 1 or not letter.isalpha():
                    await self.bot.highrise.chat(f"@{user.username} please guess a single letter.")
                else:
                    await self.guess_letter(user, letter)
            elif message.lower().startswith("!word"):
                parts = message.split(maxsplit=1)
                if len(parts) < 2:
                    await self.bot.highrise.chat(f"@{user.username} please provide a word to guess. Usage: !word <your guess>")
                    return
                guess = parts[1].strip()
                await self.guess_word(user, guess)
            elif message.lower().startswith("!hint"):
                await self.provide_hint(user)
            elif message.lower().startswith("!hscores"):
                await self.show_leaderboard()
            elif message.lower().startswith("!hclearscores"):
                await self.clear_scores(user)
        except Exception as e:
            await self.bot.highrise.chat(f"An error occurred while handling the command: {e}")







