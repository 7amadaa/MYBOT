import random
import json
import os
from highrise import BaseBot, User
from owner import OWNER_USER

class TriviaGame:

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.trivia_questions = [ 
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare"},
    {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
    {"question": "What is the boiling point of water?", "answer": "100"},
    {"question": "Which element has the chemical symbol 'O'?", "answer": "oxygen"},
    {"question": "What is the currency of Japan?", "answer": "yen"},
    {"question": "Which fruit is known as the king of fruits?", "answer": "durian"},
    {"question": "What is the chemical symbol for gold?", "answer": "au"},
    {"question": "What is the capital of Italy?", "answer": "rome"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "What is the main ingredient in guacamole?", "answer": "avocado"},
    {"question": "What is the first element on the periodic table?", "answer": "hydrogen"},
    {"question": "What is the largest mammal in the world?", "answer": "bluewhale"},
    {"question": "What is the fastest land animal?", "answer": "cheetah"},
    {"question": "What is the most widely spoken language in the world?", "answer": "mandarin"},
    {"question": "What is the name of the longest river in the world?", "answer": "nile"},
    {"question": "What is the capital of Australia?", "answer": "canberra"},
    {"question": "What is the largest desert in the world?", "answer": "sahara"},
    {"question": "What gas do plants absorb from the atmosphere?", "answer": "carbon"},
    {"question": "What is the hardest natural substance on Earth?", "answer": "diamond"},
    {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
    {"question": "What is the capital of Canada?", "answer": "ottawa"},
    {"question": "Which vitamin is known as the sunshine vitamin?", "answer": "d"},
    {"question": "What is the most spoken language in the world?", "answer": "english"},
    {"question": "What is the name of the fairy in Peter Pan?", "answer": "tinkerbell"},
    {"question": "What is the largest ocean on Earth?", "answer": "pacific"},
    {"question": "What is the main ingredient in hummus?", "answer": "chickpeas"},
    {"question": "What is the capital of Egypt?", "answer": "cairo"},
    {"question": "Which organ is responsible for pumping blood in the human body?", "answer": "heart"},
    {"question": "What is the primary gas found in the air we breathe?", "answer": "nitrogen"},
    {"question": "What is the name of the first man to walk on the moon?", "answer": "neil"},
    {"question": "What is the most common element in the universe?", "answer": "hydrogen"},
    {"question": "What is the capital of Spain?", "answer": "madrid"},
    {"question": "What is the tallest mountain in the world?", "answer": "everest"},
    {"question": "What is the primary color of a lemon?", "answer": "yellow"},
    {"question": "What is the capital of Germany?", "answer": "berlin"},
    {"question": "What is the name of the longest river in South America?", "answer": "amazon"},
    {"question": "What is the chemical symbol for silver?", "answer": "ag"},
    {"question": "What animal is known as the 'Ship of the Desert'?", "answer": "camel"},
    {"question": "Which instrument has 88 keys?", "answer": "piano"},
    {"question": "What is the currency of Russia?", "answer": "ruble"},
    {"question": "Which planet is known for its rings?", "answer": "saturn"},
    {"question": "What is the largest island in the world?", "answer": "greenland"},
    {"question": "What is the name of the first artificial Earth satellite?", "answer": "sputnik"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "japan"},
    {"question": "What is the freezing point of water in Celsius?", "answer": "zero"},
    {"question": "What is the most widely used programming language?", "answer": "python"},
    {"question": "What is the capital of India?", "answer": "delhi"},
    {"question": "What is the chemical formula for water?", "answer": "h2o"},
    {"question": "What is the only mammal capable of true flight?", "answer": "bat"},
    {"question": "What is the name of the fairy tale character who lost her glass slipper?", "answer": "cinderella"},
    {"question": "Which fruit is known for having its seeds on the outside?", "answer": "strawberry"},
    {"question": "What is the capital of Italy?", "answer": "rome"},
    {"question": "What is the main ingredient in tofu?", "answer": "soy"},
    {"question": "What is the capital of Thailand?", "answer": "bangkok"},
    {"question": "Which animal is known as the king of the jungle?", "answer": "lion"},
    {"question": "What is the name of the longest bone in the human body?", "answer": "femur"},
    {"question": "What is the primary ingredient in pesto sauce?", "answer": "basil"},
    {"question": "What is the hardest rock?", "answer": "diamond"},
    {"question": "What is the official currency of China?", "answer": "yuan"},
    {"question": "What is the largest organ in the human body?", "answer": "skin"},
    {"question": "What is the name of the first president of the United States?", "answer": "washington"},
    {"question": "What is the name of the galaxy we live in?", "answer": "milkyway"},
    {"question": "What is the main ingredient in traditional Japanese miso soup?", "answer": "miso"},
    {"question": "Which planet is closest to the sun?", "answer": "mercury"},
    {"question": "What is the capital city of Greece?", "answer": "athens"},
    {"question": "Which gas do humans exhale?", "answer": "carbon"},
    {"question": "What is the name of the largest coral reef system?", "answer": "greatbarrierreef"},
    {"question": "What is the name of the world's largest rainforest?", "answer": "amazon"},
    {"question": "What is the main ingredient in chocolate?", "answer": "cacao"},
    {"question": "Which element is represented by the symbol 'Fe'?", "answer": "iron"},
    {"question": "What is the capital of Portugal?", "answer": "lisbon"},
    {"question": "Which instrument is known as the 'king of instruments'?", "answer": "organ"},
    {"question": "What is the capital of South Korea?", "answer": "seoul"},
    {"question": "What is the first element in the periodic table?", "answer": "hydrogen"},
    {"question": "Which animal is known for its ability to change color?", "answer": "chameleon"},
    {"question": "What is the capital city of Norway?", "answer": "oslo"},
    {"question": "What is the largest species of shark?", "answer": "whale"},
    {"question": "What is the smallest country in the world?", "answer": "vatican"},
    {"question": "What is the capital of New Zealand?", "answer": "wellington"},
    {"question": "Which vitamin is produced when a person is exposed to sunlight?", "answer": "d"},
    {"question": "What is the capital of Hungary?", "answer": "budapest"},
    {"question": "What is the common term for the period of time before a birth?", "answer": "gestation"},
    {"question": "What is the name of the first manmade satellite?", "answer": "sputnik"},
    {"question": "What is the capital city of Sweden?", "answer": "stockholm"},
    {"question": "What is the name of the planet known as the 'Giant Planet'?", "answer": "jupiter"},
    {"question": "What is the primary gas in the Earth's atmosphere?", "answer": "nitrogen"},
    {"question": "Which element has the atomic number 1?", "answer": "hydrogen"},
     {"question": "What is the capital of Brazil?", "answer": "brasilia"},
    {"question": "Which ocean is the largest by area?", "answer": "pacific"},
    {"question": "What is the chemical symbol for potassium?", "answer": "k"},
    {"question": "Which planet is known as the Earth’s twin?", "answer": "venus"},
    {"question": "What is the longest bone in the human body?", "answer": "femur"},
    {"question": "What is the capital of Kenya?", "answer": "nairobi"},
    {"question": "Which animal is known for its black and white stripes?", "answer": "zebra"},
    {"question": "What is the main ingredient in bread?", "answer": "flour"},
    {"question": "What is the highest waterfall in the world?", "answer": "angel"},
    {"question": "Which country is home to the kangaroo?", "answer": "australia"},
    {"question": "What is the most abundant gas in the Earth's atmosphere?", "answer": "nitrogen"},
    {"question": "What is the capital of Thailand?", "answer": "bangkok"},
    {"question": "What is the name of the fairy tale character who leaves a shoe behind?", "answer": "cinderella"},
    {"question": "What mineral is the hardest on the Mohs scale?", "answer": "diamond"},
    {"question": "Which planet is known for its Great Red Spot?", "answer": "jupiter"},
    {"question": "What is the primary ingredient in sushi?", "answer": "rice"},
    {"question": "What is the capital of Finland?", "answer": "helsinki"},
    {"question": "What is the chemical formula for table salt?", "answer": "nacl"},
    {"question": "Which insect is known for producing honey?", "answer": "bee"},
    {"question": "What is the name of the galaxy that contains our solar system?", "answer": "milkyway"},
    {"question": "What is the capital city of Egypt?", "answer": "cairo"},
    {"question": "What is the main ingredient in chocolate?", "answer": "cocoa"},
    {"question": "Which fruit is known for having its seeds on the outside?", "answer": "strawberry"},
    {"question": "What is the capital of Indonesia?", "answer": "jakarta"},
    {"question": "What is the primary ingredient in beer?", "answer": "barley"},
    {"question": "What is the capital city of Vietnam?", "answer": "hanoi"},
    {"question": "What is the largest mammal in the ocean?", "answer": "bluewhale"},
    {"question": "What is the most popular sport in the world?", "answer": "soccer"},
    {"question": "What is the name of the famous clock tower in London?", "answer": "bigben"},
    {"question": "What is the capital of Argentina?", "answer": "buenosaires"},
    {"question": "What is the main ingredient in pesto?", "answer": "basil"},
    {"question": "What is the currency of the United Kingdom?", "answer": "pound"},
    {"question": "What is the name of the largest desert on Earth?", "answer": "antarctica"},
    {"question": "Which animal is known as the king of the jungle?", "answer": "lion"},
    {"question": "What is the capital of Mexico?", "answer": "mexico"},
    {"question": "What is the tallest building in the world?", "answer": "burjkalifa"},
    {"question": "What is the currency of India?", "answer": "rupee"},
    {"question": "What is the capital of Sweden?", "answer": "stockholm"},
    {"question": "Which fruit is known for its high vitamin C content?", "answer": "orange"},
    {"question": "What is the primary ingredient in falafel?", "answer": "chickpeas"},
    {"question": "What is the capital city of Russia?", "answer": "moscow"},
    {"question": "What is the name of the largest land animal?", "answer": "elephant"},
    {"question": "Which country is home to the kangaroo?", "answer": "australia"},
    {"question": "What is the capital of Egypt?", "answer": "cairo"},
    {"question": "What is the tallest animal in the world?", "answer": "giraffe"},
    {"question": "What is the name of the longest wall in the world?", "answer": "greatwall"},
    {"question": "What is the main ingredient in beer?", "answer": "barley"},
    {"question": "Which gas is used in balloons?", "answer": "helium"},
    {"question": "What is the primary ingredient in bread?", "answer": "flour"},
    {"question": "What is the name of the fairy tale character who had a long braid?", "answer": "rapunzel"},
    {"question": "Which planet is known as the Morning Star?", "answer": "venus"},
    {"question": "What is the smallest bone in the human body?", "answer": "stapes"},
    {"question": "What is the largest bird in the world?", "answer": "ostrich"},
    {"question": "What is the name of the first woman in space?", "answer": "tereshkova"},
    {"question": "Which instrument is known for its strings and is played with a bow?", "answer": "violin"},
    {"question": "What is the name of the famous clock tower in London?", "answer": "bigben"},
    {"question": "Which metal is liquid at room temperature?", "answer": "mercury"},
    {"question": "What is the official currency of the United Kingdom?", "answer": "pound"},
    {"question": "What is the largest continent on Earth?", "answer": "asia"},
    {"question": "Which element has the chemical symbol 'Na'?", "answer": "sodium"},
    {"question": "What is the capital of Brazil?", "answer": "brasilia"},
    {"question": "Which vitamin is known as ascorbic acid?", "answer": "c"},
    {"question": "What is the capital of Sweden?", "answer": "stockholm"},
    {"question": "What is the primary ingredient in sushi?", "answer": "rice"},
    {"question": "What is the name of the largest ocean on Earth?", "answer": "pacific"},
    {"question": "What is the chemical formula for table salt?", "answer": "nacl"},
    {"question": "What is the name of the longest river in Europe?", "answer": "volga"},
    {"question": "What is the hardest mineral?", "answer": "diamond"},
    {"question": "What is the capital of Mexico?", "answer": "mexico"},
    {"question": "What is the official language of Brazil?", "answer": "portuguese"},
    {"question": "What is the main ingredient in a traditional Caesar salad?", "answer": "romaine"},
    {"question": "Which city is known as the Big Apple?", "answer": "newyork"},
    {"question": "What is the name of the famous sculpture by Michelangelo?", "answer": "david"},
    {"question": "Which planet has the most moons?", "answer": "saturn"},
    {"question": "What is the currency of South Africa?", "answer": "rand"},
    {"question": "What is the capital of Vietnam?", "answer": "hanoi"},
    {"question": "Which creature is known for its eight legs?", "answer": "octopus"},
    {"question": "What is the name of the process by which plants make their own food?", "answer": "photosynthesis"},
    {"question": "What is the capital city of Malaysia?", "answer": "kuala"},
    {"question": "What is the name of the large body of saltwater that covers most of the Earth?", "answer": "ocean"},
    {"question": "What is the name of the famous desert located in Northern Africa?", "answer": "sahara"},
    {"question": "What is the capital of Indonesia?", "answer": "jakarta"},
    {"question": "What is the official currency of India?", "answer": "rupee"},
    {"question": "Who developed the theory of relativity?", "answer": "einstein"},
    {"question": "What is the capital of Turkey?", "answer": "ankara"},
    {"question": "Which metal is used in batteries?", "answer": "lithium"},
    {"question": "What is the capital of Switzerland?", "answer": "bern"},
    {"question": "What is the process of cell division in somatic cells called?", "answer": "mitosis"},
    {"question": "Who wrote '1984'?", "answer": "orwell"},
    {"question": "What is the capital of Chile?", "answer": "santiago"},
    {"question": "What is the unit of electric current?", "answer": "ampere"},
    {"question": "Which organelle is known as the powerhouse of the cell?", "answer": "mitochondria"},
    {"question": "Which metal has the highest electrical conductivity?", "answer": "silver"},
    {"question": "What is the capital of Belgium?", "answer": "brussels"},
    {"question": "What is the tallest mountain in Africa?", "answer": "kilimanjaro"},
    {"question": "Who is the author of 'Harry Potter'?", "answer": "rowling"},
    {"question": "What is the primary component of natural gas?", "answer": "methane"},
    {"question": "What is the capital of Austria?", "answer": "vienna"},
    {"question": "What is the largest internal organ in the human body?", "answer": "liver"},
    {"question": "What is the capital of Poland?", "answer": "warsaw"},
    {"question": "Who painted the Sistine Chapel ceiling?", "answer": "michelangelo"},
    {"question": "What is the largest moon of Saturn?", "answer": "titan"},
    {"question": "Who is known for the laws of motion?", "answer": "newton"},
    {"question": "Who wrote 'The Odyssey'?", "answer": "homer"},
    {"question": "What is the capital of Nigeria?", "answer": "abuja"},
    {"question": "Who developed the polio vaccine?", "answer": "salk"},
    {"question": "What is the smallest unit of life?", "answer": "cell"},
    {"question": "What is the primary source of energy for the Earth?", "answer": "sun"},
    {"question": "Who painted 'Starry Night'?", "answer": "vangogh"},
    {"question": "What is the capital of Ireland?", "answer": "dublin"},
    {"question": "Who composed the Four Seasons?", "answer": "vivaldi"},
    {"question": "What is the capital of the Philippines?", "answer": "manila"},
    {"question": "What is the term for animals that eat both plants and meat?", "answer": "omnivore"},
    {"question": "What is the main ingredient in tzatziki?", "answer": "yogurt"},
    {"question": "What is the capital of Scotland?", "answer": "edinburgh"},
    {"question": "Who developed the first successful airplane?", "answer": "wright"},
    {"question": "What is the chemical symbol for sodium?", "answer": "na"},
    {"question": "What is the capital of the Netherlands?", "answer": "amsterdam"},
    {"question": "What is the term for a word that is spelled the same forwards and backwards?", "answer": "palindrome"},
    {"question": "What is the capital of Saudi Arabia?", "answer": "riyadh"},
    {"question": "What is the name of the process by which water changes from liquid to gas?", "answer": "evaporation"},
    {"question": "What is the capital of Cuba?", "answer": "havana"},
    {"question": "What is the term for animals that eat only plants?", "answer": "herbivore"},
    {"question": "What is the capital of Israel?", "answer": "jerusalem"},
    {"question": "Who invented the telephone?", "answer": "bell"}
            
        ]
        self.scores = self.load_scores()  # Load scores from file
        self.current_question = None
        self.question_asked = False
        self.used_questions = []  # Track used questions
        self.round_number = 0  # Start round number from 0

    def load_scores(self):
        """Load scores from the JSON file."""
        try:
            if not os.path.exists("triviascores.json"):
                # Create the file with an empty JSON object if it doesn't exist
                with open("triviascores.json", "w") as file:
                    json.dump({}, file)
                return {}

            with open("triviascores.json", "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON. Resetting scores.")
            return {}
        except Exception as e:
            print(f"Error loading scores: {e}")
            return {}

    def save_scores(self):
        """Save scores to the JSON file."""
        try:
            with open("triviascores.json", "w") as file:
                json.dump(self.scores, file, indent=4)  # Use indent for better readability
        except Exception as e:
            print(f"Error saving scores: {e}")

    async def start_trivia(self, user: User):
        try:
            if self.question_asked:
                await self.bot.highrise.chat("A trivia question is already active! Please wait for the current round to finish.")
                return

            if len(self.used_questions) == len(self.trivia_questions):
                await self.bot.highrise.chat("All trivia questions have been used. Resetting questions for a new game!")
                self.used_questions.clear()  # Clear used questions to reset the game
                self.round_number = 0  # Reset round number
                return  # Exit the function after notifying users

            # Select a question that hasn't been used yet
            available_questions = [q for q in self.trivia_questions if q not in self.used_questions]
            if not available_questions:
                await self.bot.highrise.chat("No available questions to ask.")
                return

            self.current_question = random.choice(available_questions)
            self.question_asked = True
            self.used_questions.append(self.current_question)  # Mark the question as used
            self.round_number += 1  # Increment round number
            await self.bot.highrise.chat(f"Round {self.round_number} Trivia Question: {self.current_question['question']}")
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while starting the trivia: " + str(e))

    async def check_answer(self, user: User, message: str):
        try:
            if self.question_asked and message.lower() == self.current_question['answer'].lower():  # Ensure case-insensitive comparison
                # Update scores for the user
                if user.id not in self.scores:
                    self.scores[user.id] = {'username': user.username, 'score': 0}
                self.scores[user.id]['score'] += 1

                self.save_scores()  # Save updated scores to file

                # Send a message to the user with their current score
                await self.bot.highrise.chat(f"Congratulations @{user.username}! You answered correctly and earned a point! 🎉")
                await self.bot.highrise.chat(f"Current score for @{user.username}: {self.scores[user.id]['score']} points")

                self.question_asked = False  # Reset for the next round
                self.current_question = None
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while checking the answer: " + str(e))

    async def skip_question(self):
        try:
            if not self.question_asked:
                await self.bot.highrise.chat("No trivia question is currently active to skip.")
                return

            correct_answer = self.current_question['answer'].capitalize()
            await self.bot.highrise.chat(f"The question was: '{self.current_question['question']}'.\nThe correct answer is: '{correct_answer}'. No points awarded.")
            self.question_asked = False  # Reset for the next round
            self.current_question = None  # Clear the current question
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while skipping the question: " + str(e))

    async def show_top_scores(self):
        """Show the top 10 scores."""
        try:
            top_users = sorted(self.scores.values(), key=lambda x: x['score'], reverse=True)[:10]
            if not top_users:
                await self.bot.highrise.chat("\n🥇 No scores to display yet 🥇")
                return

            message = "🥇__Top 10 Trivia Scorers__🥇\n"  # Remove the leading newline
            for i, user in enumerate(top_users, start=1):
                message += f"{i}. @{user['username']} - {user['score']} points\n"
                if len(message) > 256:  # Check for message length
                    await self.bot.highrise.chat("\n" + message.strip())  # Add a newline before sending
                    message = ""  # Reset message

            if message:
                await self.bot.highrise.chat("\n" + message.strip())  # Add a newline before sending any remaining message
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while displaying top scores: " + str(e))

    async def clear_scores(self, user: User):
        """Clear scores from the file and in memory if the user is authorized."""
        try:
            privilege_response = await self.bot.highrise.get_room_privilege(user.id)
            if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
                await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
                return

            self.scores = {}  # Clear scores in memory
            self.save_scores()  # Clear scores in the file
            await self.bot.highrise.chat(f"📉 @{user.username} has cleared all trivia scores!")  # Custom message
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while clearing scores: " + str(e))

    async def handle_command(self, user: User, message: str):
        try:
            if message.lower() == "!trivia":
                await self.start_trivia(user)
            elif message.lower() == "!skip":
                await self.skip_question()
            elif message.lower() == "!tscores":
                await self.show_top_scores()
            elif message.lower() == "!tclearscores":
                await self.clear_scores(user)
            else:
                await self.check_answer(user, message)
        except Exception as e:
            await self.bot.highrise.chat("An error occurred while processing your command: " + str(e))





