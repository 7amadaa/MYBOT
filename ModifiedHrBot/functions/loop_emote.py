from highrise import BaseBot, User
import asyncio
from asyncio import Task


class LoopEmote:
    def __init__(self, bot: BaseBot):
        self.bot = bot
        self.emote_list: list[tuple[int, str, str]] = [
    (0, 'jetpack', 'hcc-jetpack'),
    (1, 'fairyfloat', 'idle-floating'),
    (2, 'fairytwirl', 'emote-looping'),
    (3, 'smooch', 'emote-kissing-bound'),
    (4, 'launch', 'emote-launch'),
    (5, 'float', 'emote-float'),
    (6, 'lust', 'emote-lust'),
    (7, 'creepypuppet', 'dance-creepypuppet'),
    (8, 'repose', 'sit-relaxed'),
    (9, 'enthused', 'idle-enthusiastic'),
    (10, 'anime', 'dance-anime'),
    (11, 'gravity', 'emote-gravity'),
    (12, 'toilet', 'idle-toilet'),
    (13, 'astro', 'emote-astronaut'),
    (14, 'flex', 'emoji-flex'),
    (15, 'timejump', 'emote-timejump'),
    (16, 'penguin', 'dance-pinguin'),
    (17, 'kawaii', 'dance-kawai'),
    (18, 'jinglebell', 'dance-jinglebell'),
    (19, 'skating', 'emote-iceskating'),
    (20, 'teleporting', 'emote-teleporting'),
    (21, 'energyball', 'emote-energyball'),
    (22, 'pushit', 'dance-employee'),
    (23, 'boxer', 'emote-boxer'),
    (24, 'creepycute', 'emote-creepycute'),
    (25, 'headblow', 'emote-headblowup'),
    (26, 'wrong', 'dance-wrong'),
    (27, 'weirdd', 'dance-weird'),
    (28, 'uwu', 'idle-uwu'),
    (29, 'snake', 'emote-snake'),
    (30, 'singing', 'idle_singing'),
    (31, 'model', 'emote-model'),
    (32, 'maniac', 'emote-maniac'),
    (33, 'snow', 'emote-snowangel'),
    (34, 'ride', 'emote-sleigh'),
    (35, 'icecream', 'dance-icecream'),
    (36, 'surprise', 'emote-pose6'),
    (37, 'touch', 'dance-touch'),
    (38, 'swordfight', 'emote-swordfight'),
    (39, 'airguitar', 'idle-guitar'),
    (40, 'zombie', 'emote-zombierun'),
    (41, 'fashion', 'emote-fashionista'),
    (42, 'curtsy', 'emote-curtsy'),
    (43, 'cutee', 'emote-cute'),
    (44, 'telek', 'emote-telekinesis'),
    (45, 'russian', 'dance-russian'),
    (46, 'blackpink', 'dance-blackpink'),
    (47, 'shopping', 'dance-shoppingcart'),
    (48, 'tiktok6', 'dance-tiktok11'),
    (49, 'tiktok5', 'dance-tiktok9'),
    (50, 'tiktok4', 'dance-tiktok8'),
    (51, 'tiktok3', 'idle-dance-tiktok4'),
    (52, 'tiktok2', 'dance-tiktok2'),
    (53, 'tiktok1', 'dance-tiktok10'),
    (54, 'hott', 'emote-hot'),
    (55, 'charge', 'emote-charging'),
    (56, 'greedy', 'emote-greedy'),
    (57, 'confused', 'emote-confused'),
    (58, 'punkguitar', 'emote-punkguitar'),
    (59, 'shy', 'emote-shy2'),
    (60, 'wildd', 'idle-wild'),
    (61, 'nervous', 'idle-nervous'),
    (62, 'hyped', 'emote-hyped'),
    (63, 'fishing', 'fishing-idle'),
    (64, 'frog', 'emote-frog'),
    (65, 'siu', 'emote-celebrationstep'),
    (66, 'snowballfight', 'emote-snowball'),
    (67, 'bow', 'emote-bow'),
    (68, 'thewave', 'emote-wave'),
    (69, 'tiredd', 'emote-tired'),
    (70, 'pennywise', 'dance-pennywise'),
    (71, 'superpose', 'emote-superpose'),  
    (72, 'pose8', 'emote-pose8'),
    (73, 'laugh', 'emote-laughing'),
    (74, 'kiss', 'emote-kiss'),
    (75, 'hellos', 'emote-hello'),
    (76, 'gift', 'emote-gift'),
    (77, 'pose10', 'emote-pose10'),
    (78, 'thumbsup', 'emoji-thumbsup'),
    (79, 'cursing', 'emoji-cursing'),
    (80, 'celebrate', 'emoji-celebrate'),
    (81, 'macarena', 'dance-macarena'),
    (82, 'sitt', 'idle-loop-sitfloor'),
    (83, 'gag', 'emoji-gagging'),          
    (84, 'superpose', 'emote-superpose'),
    (85, 'pose7', 'emote-pose7'),
    (86, 'deny', 'emote-no'),
    (87, 'casual', 'idle-dance-casual'),   
    (88, 'pose1', 'emote-pose1'),
    (89, 'pose3', 'emote-pose3'),
    (90, 'pose5', 'emote-pose5'),
    (91, 'cutey', 'emote-cutey'),
    (92, 'thatsright', 'emote-yes'),
    (93, 'pose9', 'emote-pose9'),
    (94, 'angryy', 'emoji-angry'),   
    (95, 'miningmine', 'mining-mine'),
    (96, 'miningsuccess', 'mining-success'),
    (97, 'fishingpull', 'fishing-pull'),
    (98, 'fishingpullsmall', 'fishing-pull-small'),
    (99, 'fishingcast', 'fishing-cast'),

]
        self.emote_durations = {
            'flex': 2.099351,
            'jetpack': 25.5,
            'toilet': 32.174447,
            'frog': 14.55257,
            'float': 8.995302,
            'enthused': 15.941537,
            'gravity': 8.955966,
            'russian': 10.252905,
            'zombie': 12.922772,
            'punkguitar': 9.365807,
            'airguitar': 13.229398,
            'teleporting': 11.7676,
            'charge': 8.025079,
            'hott': 4.353037,
            'tiktok1': 8.225648,
            'tiktok2': 10.392353,
            'tiktok3': 15.500708,
            'tiktok4': 10.938702,
            'tiktok5': 11.892918,
            'shopping': 4.316035,
            'blackpink': 7.150958,
            'anime': 8.46671,
            'telek': 10.492032,
            'cutee': 3.26032,
            'curtsy': 2.425714,
            'fashion': 5.606485,
            'shy': 4.989278,
            'confused': 8.578827,
            'energyball': 7.575354,
            'gag': 5.500202,
            'icecream': 14.769573,
            'lust': 4.655965,
            'snow': 6.218627,
            'maniac': 4.906886,
            'model': 6.490173,
            'singing': 10.260182,
            'snake': 5.262578,
            'uwu': 24.761968,
            'weirdd': 21.556237,
            'wrong': 12.422389,
            'headblow': 11.667537,
            'creepycute': 7.902453,
            'boxer': 5.555702,
            'pushit': 8,
            'siu': 3.353703,
            'surprise': 5.375124,
            'skating': 7.299156,
            'wildd': 26.422824,
            'kawaii': 10.290789,
            'penguin': 11.58291,
            'timejump': 4.007305,
            'swordfight': 5.914365,
            'astro': 13.791175,
            'nervous': 21.714221,
            'jinglebell': 10.958832,
            'hyped': 7.492423,
            'repose': 29.3,
            'fairyfloat': 26,
            'fairytwirl': 9.0,
            'creepypuppet': 6.416121,
            'ride': 11.333165,
            'fishing': 16,
            'smooch': 6,
            'launch': 9.4,
            'tiktok6': 10.8,
            'sitt': 22.321055,
            'thatsright': 2.565001,
            'thewave': 2.690873,
            'tiredd': 4.61063,
            'snowballfight': 5.230467,
            'snowangel': 6.218627,
            'sad': 5.411073,
            'deny': 2.703034,
            'laugh': 2.69161,
            'kiss': 2.387175,
            'hellos': 2.734844,
            'exasperatedb': 2.722748,
            'bow': 3.344036,
            'thumbsup': 2.702369,
            'cursing': 2.382069,
            'celebrate': 3.412258,
            'angryy': 5.760023,
            'savage': 10.938702,
            'dontstartnow': 10.392353,
            'pennywise': 1.214349,
            'macarena': 12.214141,
            'hearteyes': 4.034386,
            'superpose': 4.530791,
            'pose7': 4.655283,
            'pose8': 4.808806,
            'casual': 9.079756,
            'pose1': 2.825795,
            'pose3': 5.10562,
            'pose5': 4.621532,
            'cutey': 3.26032,
            'pose10': 3.989871,
            'pose9': 4.583117,
            'gift': 5.8,
            'touch': 11.7,
            'miningmine': 3,
            'miningsuccess': 2.5,
            'fishingpull': 1,
            'fishingpullsmall': 1,
            'fishingcast': 1.5,
        
        }  # Mapping emotes to their specific durations (in seconds)


    async def handle_command(self, user: User, message: str) -> None:
        # If the message is "!stopemote", handle that command
        if message.lower() == "stop":
            await self.stopemote(user, message)
            return
        
        # Try to check if the message is a valid emote number or name
        emote_id = ""
        emote_name = ""

        # Check if the message is a number corresponding to a valid emote
        if message.isdigit():
            emote_number = int(message)
            for emote in self.emote_list:
                if emote[0] == emote_number:
                    emote_name = emote[1]
                    emote_id = emote[2]
                    break

        # Check if the message matches any emote name
        else:
            for emote in self.emote_list:
                if emote[1].lower() == message.lower():
                    emote_name = emote[1]
                    emote_id = emote[2]
                    break

        # If a valid emote is found, trigger the emote
        if emote_id != "":
            await self.emote(user, message)
        # Otherwise, ignore the message (allow normal chat without triggering "Invalid emote")


    async def emote(self, user: User, message: str) -> None:
        async def loop_emote(user: User, emote_name_or_number: str) -> None:
            emote_id = ""
            emote_name = ""

            # Check if the input is a number or a name
            if emote_name_or_number.isdigit():
                emote_number = int(emote_name_or_number)  # Input is a number
                for emote in self.emote_list:
                    if emote[0] == emote_number:
                        emote_name = emote[1]
                        emote_id = emote[2]
                        break
            else:
                # Input is a name
                for emote in self.emote_list:
                    if emote[1].lower() == emote_name_or_number.lower():
                        emote_name = emote[1]
                        emote_id = emote[2]
                        break

            if emote_id == "":
                await self.bot.highrise.send_whisper(user.id, "Invalid emote")
                return

            await self.bot.highrise.send_whisper(user.id, f"You are looping [{emote_name}]! Type 'Stop' to stop emoting.")

            # Get the emote duration or use a default value
            sleep_duration = self.emote_durations.get(emote_name.lower(), 10)

            # Keep looping the emote regardless of the user's position
            while True:
                try:
                    await self.bot.highrise.send_emote(emote_id, user.id)
                except:
                    return
                await asyncio.sleep(sleep_duration)  # Wait for the duration of the emote before sending it again

        try:
            emote_name_or_number = message.strip()
        except:
            await self.bot.highrise.chat("Invalid command format. Please use an emote name or number.")
            return
        else:
            taskgroup = self.bot.highrise.tg
            task_list: list[Task] = list(taskgroup._tasks)
            for task in task_list:
                if task.get_name() == user.username:
                    task.cancel()

            taskgroup.create_task(coro=loop_emote(user, emote_name_or_number))
            task_list: list[Task] = list(taskgroup._tasks)
            room_users = (await self.bot.highrise.get_room_users()).content
            user_list = [room_user.username for room_user, pos in room_users]
            for task in task_list:
                if task.get_coro().__name__ == "loop_emote" and task.get_name() not in user_list:
                    task.set_name(user.username)


    async def stopemote(self, user: User, message: str) -> None:
        taskgroup = self.bot.highrise.tg
        task_list: list[Task] = list(taskgroup._tasks)
        for task in task_list:
            if task.get_name() == user.username:
                task.cancel()
                await self.bot.highrise.send_whisper(user.id, "Stopping your emote loop!")
                return
        await self.bot.highrise.send_whisper(user.id, "You're not looping any emotes.")






