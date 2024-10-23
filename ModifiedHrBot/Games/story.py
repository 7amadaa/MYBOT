import random
from highrise import BaseBot, User



class InteractiveStory:

    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.story_progress = None
        self.story_votes = {}
        self.players = set()

        # Long and detailed story structure
        self.story_scenarios = {
            1: {
                'text': (
                    "You are a renowned explorer, hired by a mysterious organization to find an ancient relic hidden in a long-lost city. "
                    "Your journey begins in a dense jungle, where the air is thick with humidity. Ahead lies a narrow path leading into the unknown. "
                    "Do you follow the path or venture off into the jungle, where you might find hidden treasures or dangers?"
                ),
                'options': {'follow_path': 2, 'venture_off': 3}
            },
            2: {
                'text': (
                    "You follow the path cautiously and soon find yourself at the entrance of an ancient temple. "
                    "The walls are covered in overgrown vines, and strange symbols are etched into the stone. The door is slightly ajar, as if someone—or something—has been here recently. "
                    "Do you enter the temple or investigate the surroundings?"
                ),
                'options': {'enter_temple': 4, 'investigate': 5}
            },
            3: {
                'text': (
                    "You decide to leave the path and venture deep into the jungle. As you push through the thick vegetation, "
                    "you stumble upon a hidden waterfall with a strange glow emanating from behind it. It could be a hidden cave or something else. "
                    "Do you investigate the waterfall or turn back to the path?"
                ),
                'options': {'investigate_waterfall': 6, 'turn_back': 2}
            },
            4: {
                'text': (
                    "You step inside the temple and find a grand hall, its floor littered with ancient relics. "
                    "In the center of the room, a stone pedestal holds a glowing artifact, pulsing with energy. "
                    "But as you approach, you notice strange, shadowy figures lurking in the corners of the room. Do you grab the artifact quickly or retreat and plan your next move?"
                ),
                'options': {'grab_artifact': 7, 'retreat': 8}
            },
            5: {
                'text': (
                    "You explore the surroundings and find a series of hidden traps designed to keep intruders out. "
                    "One of the traps seems to lead to a hidden chamber beneath the temple, and it looks dangerous to disarm it. "
                    "Do you try to disarm the trap to enter the chamber or leave it alone and return to the temple door?"
                ),
                'options': {'disarm_trap': 9, 'return_to_temple': 4}
            },
            6: {
                'text': (
                    "You investigate the waterfall and find a hidden cave behind it. Inside, you see strange symbols carved into the walls, "
                    "and at the back of the cave, there is an ancient scroll placed on an altar. "
                    "Do you take the scroll or leave it behind?"
                ),
                'options': {'take_scroll': 10, 'leave_scroll': 11}
            },
            7: {
                'text': (
                    "You grab the artifact, and instantly, the shadowy figures come to life, revealing themselves as ancient guardians. "
                    "They close in on you, and the room starts to collapse. Do you fight the guardians or try to escape the temple?"
                ),
                'options': {'fight_guardians': 12, 'escape': 13}
            },
            8: {
                'text': (
                    "You decide to retreat, but the shadowy figures begin to stir. The floor beneath you starts to crack. "
                    "You need to make a quick decision. Do you hide in the temple or run outside?"
                ),
                'options': {'hide': 14, 'run_outside': 15}
            },
            9: {
                'text': (
                    "You carefully disarm the trap and reveal a hidden stairway that leads down into a secret chamber. "
                    "Inside, you find ancient texts and relics of a lost civilization. "
                    "However, the air feels thick with danger. Do you explore the chamber further or leave before something happens?"
                ),
                'options': {'explore_further': 16, 'leave': 4}
            },
            10: {
                'text': (
                    "You take the scroll, and the moment you do, the cave begins to shake violently. "
                    "The entrance behind you is blocked by falling rocks, and a new path opens deeper into the cave. "
                    "Do you follow the new path or try to clear the blocked entrance?"
                ),
                'options': {'follow_path': 17, 'clear_entrance': 18}
            },
            11: {
                'text': (
                    "You decide to leave the scroll, sensing its dangerous power. As you turn to leave the cave, you hear footsteps echoing behind you. "
                    "Someone—or something—is following you. Do you hide or confront whatever is behind you?"
                ),
                'options': {'hide': 19, 'confront': 20}
            },
            # Continuing with several more branching scenarios...
            12: {
                'text': "You fight the guardians bravely but are overwhelmed. Your journey ends here.",
                'options': {}
            },
            13: {
                'text': (
                    "You manage to escape the temple just as it collapses behind you. "
                    "Though the artifact is lost, you survive to continue your journey."
                ),
                'options': {}
            },
            14: {
                'text': "You hide in the temple, but the collapse traps you forever beneath the rubble.",
                'options': {}
            },
            15: {
                'text': (
                    "You run outside and barely escape the collapsing temple. "
                    "Though you escaped, you feel a deep sense of loss, as if you missed out on something important inside."
                ),
                'options': {}
            },
            16: {
                'text': (
                    "As you explore the chamber further, you find an ancient artifact of immense power. "
                    "But it comes with a curse—one that may haunt you for the rest of your life."
                ),
                'options': {}
            },
            17: {
                'text': (
                    "You follow the new path deeper into the cave, where you discover an underground city, "
                    "long forgotten by the outside world. Your adventure has only just begun..."
                ),
                'options': {}
            },
            18: {
                'text': "You try to clear the blocked entrance but fail. The cave collapses, trapping you inside.",
                'options': {}
            },
            19: {
                'text': "You hide in the shadows, and the footsteps pass by without noticing you. You escape safely.",
                'options': {}
            },
            20: {
                'text': "You confront the figure, revealing an ancient warrior. A battle ensues, and your fate is sealed.",
                'options': {}
            }
        }

    async def start_story(self, user: User):
        # Allow the user to join an ongoing story
        if self.story_progress is not None:
            self.players.add(user.id)
            await self.bot.highrise.chat(f"@{user.username} has joined the story!")
            await self.display_story_scenario()
        # Start a new story if there is none
        else:
            self.story_progress = 1  # Start at the first scenario
            self.players.add(user.id)
            await self.bot.highrise.chat(f"@{user.username} has started a new story!")
            await self.display_story_scenario()

    async def display_story_scenario(self):
        scenario = self.story_scenarios[self.story_progress]
        await self.send_chunked_message(scenario['text'])

        if scenario['options']:
            options_text = "Choices: " + ", ".join(scenario['options'].keys())
            await self.send_chunked_message(options_text)

    async def send_chunked_message(self, message: str):
        # Split the message into 256-character chunks
        chunk_size = 256
        for i in range(0, len(message), chunk_size):
            await self.bot.highrise.chat(message[i:i + chunk_size])

    async def check_active_players(self):
        # Check for active players in the room and update the player list
        room_users = (await self.bot.highrise.get_room_users()).content

        # Extract the user IDs from the tuples
        active_player_ids = {room_user.id for room_user, _ in room_users}

        # Remove players who are no longer in the room
        self.players = self.players.intersection(active_player_ids)

    async def vote(self, user: User, option: str):
        if self.story_progress is None:
            await self.bot.highrise.chat(f"@{user.username}, start the story first with !story.")
            return

        # Check if the user has joined the story
        if user.id not in self.players:
            await self.bot.highrise.chat(f"@{user.username}, you need to join the story with !story before voting.")
            return

        current_scenario = self.story_scenarios[self.story_progress]
        if option not in current_scenario['options']:
            await self.bot.highrise.chat(f"@{user.username}, that's not a valid choice. Please choose from the available options.")
            return

        self.story_votes[user.id] = option
        await self.bot.highrise.chat(f"@{user.username} voted for '{option}'.")

        # Check active players before counting votes
        await self.check_active_players()

        # Once all remaining active players have voted or after a timeout, move to the next scenario
        if len(self.story_votes) == len(self.players):
            await self.tally_votes()

    async def tally_votes(self):
        vote_counts = {}
        for vote in self.story_votes.values():
            vote_counts[vote] = vote_counts.get(vote, 0) + 1

        winning_option = max(vote_counts, key=vote_counts.get)
        self.story_progress = self.story_scenarios[self.story_progress]['options'][winning_option]
        self.story_votes.clear()

        await self.display_story_scenario()

        # If the next scenario has no options, the story ends
        if not self.story_scenarios[self.story_progress]['options']:
            await self.bot.highrise.chat("The story has ended! Players will need to join again to start a new story.")
            self.story_progress = None  # Reset story progress
            self.players.clear()  # Clear the list of players so they must join again


    async def end_story(self):
        if self.story_progress is None:
            await self.bot.highrise.chat("No story is currently active.")
            return
        
        # End the current story
        await self.bot.highrise.chat("The story has been ended.")
        self.story_progress = None  # Reset story progress
        self.players.clear()  # Clear the list of players so they must join again

    async def handle_command(self, user: User, message: str):
        if message.lower().startswith("!story"):
            await self.start_story(user)
        elif message.lower().startswith("!choose"):
            option = message[8:].strip().lower()
            await self.vote(user, option)
        elif message.lower() == "!endstory":
            await self.end_story()

