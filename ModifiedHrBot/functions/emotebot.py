from highrise import BaseBot, User
import asyncio
from asyncio import Task
import random
from owner import OWNER_USER


emote_list: list[str] = ['sit-idle-cute', 'idle_zombie', 'idle_layingdown2', 'idle_layingdown', 'idle-sleep', 'idle-sad', 'idle-posh', 'idle-loop-tired', 'idle-loop-tapdance', 'idle-loop-sitfloor', 'idle-loop-shy', 'idle-loop-sad', 'idle-loop-happy', 'idle-loop-annoyed', 'idle-loop-aerobics', 'idle-lookup', 'idle-hero', 'idle-floorsleeping2', 'idle-floorsleeping', 'idle-enthusiastic', 'idle-dance-swinging', 'idle-dance-headbobbing', 'idle-angry', 'emote-yes', 'emote-wings', 'emote-wave', 'emote-tired', 'emote-think', 'emote-theatrical', 'emote-tapdance', 'emote-superrun', 'emote-superpunch', 'emote-sumo', 'emote-suckthumb', 'emote-splitsdrop', 'emote-snowball', 'emote-snowangel', 'emote-shy', 'emote-secrethandshake', 'emote-sad', 'emote-ropepull', 'emote-roll', 'emote-rofl', 'emote-robot', 'emote-rainbow', 'emote-proposing', 'emote-peekaboo', 'emote-peace', 'emote-panic', 'emote-no', 'emote-ninjarun', 'emote-nightfever', 'emote-monster_fail', 'emote-model', 'emote-lust', 'emote-levelup', 'emote-laughing2', 'emote-laughing', 'emote-kiss', 'emote-kicking', 'emote-jumpb', 'emote-judochop', 'emote-jetpack', 'emote-hugyourself', 'emote-hot', 'emote-hero', 'emote-hello', 'emote-headball', 'emote-harlemshake', 'emote-happy', 'emote-handstand', 'emote-greedy', 'emote-graceful', 'emote-gordonshuffle', 'emote-ghost-idle', 'emote-gangnam', 'emote-frollicking', 'emote-fainting', 'emote-fail2', 'emote-fail1', 'emote-exasperatedb', 'emote-exasperated', 'emote-elbowbump', 'emote-disco', 'emote-disappear', 'emote-deathdrop', 'emote-death2', 'emote-death', 'emote-dab', 'emote-curtsy', 'emote-confused', 'emote-cold', 'emote-charging', 'emote-bunnyhop', 'emote-bow', 'emote-boo', 'emote-baseball', 'emote-apart', 'emoji-thumbsup', 'emoji-there', 'emoji-sneeze', 'emoji-smirking', 'emoji-sick', 'emoji-scared', 'emoji-punch', 'emoji-pray', 'emoji-poop', 'emoji-naughty', 'emoji-mind-blown', 'emoji-lying', 'emoji-halo', 'emoji-hadoken', 'emoji-give-up', 'emoji-gagging', 'emoji-flex', 'emoji-dizzy', 'emoji-cursing', 'emoji-crying', 'emoji-clapping', 'emoji-celebrate', 'emoji-arrogance', 'emoji-angry', 'dance-voguehands', 'dance-tiktok8', 'dance-tiktok2', 'dance-spiritual', 'dance-smoothwalk', 'dance-singleladies', 'dance-shoppingcart', 'dance-russian', 'dance-robotic', 'dance-pennywise', 'dance-orangejustice', 'dance-metal', 'dance-martial-artist', 'dance-macarena', 'dance-handsup', 'dance-floss', 'dance-duckwalk', 'dance-breakdance', 'dance-blackpink', 'dance-aerobics', 'emote-hyped', 'dance-jinglebell', 'idle-nervous', 'idle-toilet', 'emote-attention', 'emote-astronaut', 'dance-zombie', 'emoji-ghost', 'emote-hearteyes', 'emote-swordfight', 'emote-timejump', 'emote-snake', 'emote-heartfingers', 'emote-heartshape', 'emote-hug', 'emote-lagughing', 'emoji-eyeroll', 'emote-embarrassed', 'emote-float', 'emote-telekinesis', 'dance-sexy', 'emote-puppet', 'idle-fighter', 'dance-pinguin', 'dance-creepypuppet', 'emote-sleigh', 'emote-maniac', 'emote-energyball', 'idle_singing', 'emote-frog', 'emote-superpose', 'emote-cute', 'dance-tiktok9', 'dance-weird', 'dance-tiktok10', 'emote-pose7', 'emote-pose8', 'idle-dance-casual', 'emote-pose1', 'emote-pose3', 'emote-pose5', 'emote-cutey', 'emote-punkguitar', 'emote-zombierun', 'emote-fashionista', 'emote-gravity', 'dance-icecream', 'dance-wrong', 'idle-uwu', 'idle-dance-tiktok4', 'emote-shy2', 'dance-anime', 'dance-kawai', 'idle-wild', 'emote-iceskating', 'emote-pose6', 'emote-celebrationstep', 'emote-creepycute', 'emote-frustrated', 'emote-pose10', 'sit-relaxed', 'sit-open', 'emote-stargaze', 'emote-slap', 'emote-boxer', 'emote-headblowup', 'emote-kawaiigogo', 'emote-repose', 'idle-dance-tiktok7', 'emote-shrink', 'emote-pose9', 'emote-teleporting', 'dance-touch', 'idle-guitar', 'emote-gift', 'dance-employee']

# Mapping emotes to their specific durations (in seconds)
emote_durations = {
    'sit-idle-cute': 17.062613,
    'idle_zombie': 28.754937,
    'idle_layingdown2': 21.546653,
    'idle_layingdown': 24.585168,
    'idle-sleep': 22.620446,
    'idle-sad': 24.377214,
    'idle-posh': 21.851256,
    'idle-loop-tired': 21.959007,
    'idle-loop-tapdance': 6.261593,
    'idle-loop-sitfloor': 22.321055,
    'idle-loop-shy': 16.47449,
    'idle-loop-sad': 6.052999,
    'idle-loop-happy': 18.798322,
    'idle-loop-annoyed': 17.058522,
    'idle-loop-aerobics': 8.507535,
    'idle-lookup': 22.339865,
    'idle-hero': 21.877099,
    'idle-floorsleeping2': 17.253372,
    'idle-floorsleeping': 13.935264,
    'idle-enthusiastic': 15.941537,
    'idle-dance-swinging': 13.198551,
    'idle-dance-headbobbing': 25.367458,
    'idle-angry': 25.427848,
    'emote-yes': 2.565001,
    'emote-wings': 13.134487,
    'emote-wave': 2.690873,
    'emote-tired': 4.61063,
    'emote-think': 3.691104,
    'emote-theatrical': 8.591869,
    'emote-tapdance': 11.057294,
    'emote-superrun': 6.273226,
    'emote-superpunch': 3.751054,
    'emote-sumo': 10.868834,
    'emote-suckthumb': 4.185944,
    'emote-splitsdrop': 4.46931,
    'emote-snowball': 5.230467,
    'emote-snowangel': 6.218627,
    'emote-shy': 4.477567,
    'emote-secrethandshake': 3.879024,
    'emote-sad': 5.411073,
    'emote-ropepull': 8.769656,
    'emote-roll': 3.560517,
    'emote-rofl': 6.314731,
    'emote-robot': 7.607362,
    'emote-rainbow': 2.813373,
    'emote-proposing': 4.27888,
    'emote-peekaboo': 3.629867,
    'emote-peace': 5.755004,
    'emote-panic': 2.850966,
    'emote-no': 2.703034,
    'emote-ninjarun': 4.754721,
    'emote-nightfever': 5.488424,
    'emote-monster_fail': 4.632708,
    'emote-model': 6.490173,
    'emote-lust': 4.655965,
    'emote-levelup': 6.0545,
    'emote-laughing2': 5.056641,
    'emote-laughing': 2.69161,
    'emote-kiss': 2.387175,
    'emote-kicking': 4.867992,
    'emote-jumpb': 3.584234,
    'emote-judochop': 2.427442,
    'emote-jetpack': 16.759457,
    'emote-hugyourself': 4.992751,
    'emote-hot': 4.353037,
    'emote-hero': 4.996096,
    'emote-hello': 2.734844,
    'emote-headball': 10.073119,
    'emote-harlemshake': 13.558597,
    'emote-happy': 3.483462,
    'emote-handstand': 4.015678,
    'emote-greedy': 4.639828,
    'emote-graceful': 3.7498,
    'emote-gordonshuffle': 8.052307,
    'emote-ghost-idle': 19.570492,
    'emote-gangnam': 7.275486,
    'emote-frollicking': 3.700665,
    'emote-fainting': 18.423499,
    'emote-fail2': 6.475972,
    'emote-fail1': 5.617942,
    'emote-exasperatedb': 2.722748,
    'emote-exasperated': 2.367483,
    'emote-elbowbump': 3.799768,
    'emote-disco': 5.366973,
    'emote-disappear': 6.195985,
    'emote-deathdrop': 3.762728,
    'emote-death2': 4.855549,
    'emote-death': 6.615967,
    'emote-dab': 2.717871,
    'emote-curtsy': 2.425714,
    'emote-confused': 8.578827,
    'emote-cold': 3.664348,
    'emote-charging': 8.025079,
    'emote-bunnyhop': 12.380685,
    'emote-bow': 3.344036,
    'emote-boo': 4.501502,
    'emote-baseball': 7.254841,
    'emote-apart': 4.809542,
    'emoji-thumbsup': 2.702369,
    'emoji-there': 2.059095,
    'emoji-sneeze': 2.996694,
    'emoji-smirking': 4.823158,
    'emoji-sick': 5.070367,
    'emoji-scared': 3.008487,
    'emoji-punch': 1.755783,
    'emoji-pray': 4.503179,
    'emoji-poop': 4.795735,
    'emoji-naughty': 4.277602,
    'emoji-mind-blown': 2.397167,
    'emoji-lying': 6.313748,
    'emoji-halo': 5.837754,
    'emoji-hadoken': 2.723709,
    'emoji-give-up': 5.407888,
    'emoji-gagging': 5.500202,
    'emoji-flex': 2.099351,
    'emoji-dizzy': 4.053049,
    'emoji-cursing': 2.382069,
    'emoji-crying': 3.696499,
    'emoji-clapping': 2.161757,
    'emoji-celebrate': 3.412258,
    'emoji-arrogance': 6.869441,
    'emoji-angry': 5.760023,
    'dance-voguehands': 9.150634,
    'dance-tiktok8': 10.938702,
    'dance-tiktok2': 10.392353,
    'dance-spiritual': 15.795092,
    'dance-smoothwalk': 6.690023,
    'dance-singleladies': 21.191372,
    'dance-shoppingcart': 4.316035,
    'dance-russian': 10.252905,
    'dance-robotic': 17.814959,
    'dance-pennywise': 1.214349,
    'dance-orangejustice': 6.475263,
    'dance-metal': 15.076377,
    'dance-martial-artist': 13.284405,
    'dance-macarena': 12.214141,
    'dance-handsup': 22.283413,
    'dance-floss': 21.329661,
    'dance-duckwalk': 11.748784,
    'dance-breakdance': 17.623849,
    'dance-blackpink': 7.150958,
    'dance-aerobics': 8.796402,
    'emote-hyped': 7.492423,
    'dance-jinglebell': 11,
    'idle-nervous': 21.714221,
    'idle-toilet': 32.174447,
    'emote-attention': 4.401206,
    'emote-astronaut': 13.791175,
    'dance-zombie': 12.922772,
    'emoji-ghost': 3.472759,
    'emote-hearteyes': 4.034386,
    'emote-swordfight': 5.914365,
    'emote-timejump': 4.007305,
    'emote-snake': 5.262578,
    'emote-heartfingers': 4.001974,
    'emote-heartshape': 6.232394,
    'emote-hug': 3.503262,
    'emote-lagughing': 1.125537,
    'emoji-eyeroll': 3.020264,
    'emote-embarrassed': 7.414283,
    'emote-float': 8.995302,
    'emote-telekinesis': 10.492032,
    'dance-sexy': 12.30883,
    'emote-puppet': 16.325823,
    'idle-fighter': 17.19123,
    'dance-pinguin': 11.58291,
    'dance-creepypuppet': 6.416121,
    'emote-sleigh': 11.333165,
    'emote-maniac': 4.906886,
    'emote-energyball': 7.575354,
    'idle_singing': 10.260182,
    'emote-frog': 14.55257,
    'emote-superpose': 4.530791,
    'emote-cute': 6.170464,
    'dance-tiktok9': 11.892918,
    'dance-weird': 21.556237,
    'dance-tiktok10': 8.225648,
    'emote-pose7': 4.655283,
    'emote-pose8': 4.808806,
    'idle-dance-casual': 9.079756,
    'emote-pose1': 2.825795,
    'emote-pose3': 5.10562,
    'emote-pose5': 4.621532,
    'emote-cutey': 3.26032,
    'emote-punkguitar': 9.365807,
    'emote-zombierun': 9.182984,
    'emote-fashionista': 5.606485,
    'emote-gravity': 8.955966,
    'dance-icecream': 14.769573,
    'dance-wrong': 12.422389,
    'idle-uwu': 24.761968,
    'idle-dance-tiktok4': 15.500708,
    'emote-shy2': 4.989278,
    'dance-anime': 8.46671,
    'dance-kawai': 10.290789,
    'idle-wild': 26.422824,
    'emote-iceskating': 7.299156,
    'emote-pose6': 5.375124,
    'emote-celebrationstep': 3.353703,
    'emote-creepycute': 7.902453,
    'emote-frustrated': 5.584622,
    'emote-pose10': 3.989871,
    'sit-relaxed': 29.889858,
    'sit-open': 26.025963,
    'emote-stargaze': 1.127464,
    'emote-slap': 2.724945,
    'emote-boxer': 5.555702,
    'emote-headblowup': 11.667537,
    'emote-kawaiigogo': 10,
    'emote-repose': 1.118455,
    'idle-dance-tiktok7': 12.956484,
    'emote-shrink': 8.738784,
    'emote-pose9': 4.583117,
    'emote-teleporting': 11.7676,
    'dance-touch': 11.7,
    'idle-guitar': 13.229398,
    'emote-gift': 5.8,
    'dance-employee': 8,
}

class DanceBotCommands:

    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def handle_command(self, user: User, message: str) -> None:
        if message.lower() in ["dance", "!dance"]:
            await self.start_emote_bot(user, message)
            
        elif message.lower() in ["stopdance", "!stopdance"]:
            await self.stop_emote_bot(user, message)

    async def start_emote_bot(self, user: User, message: str) -> None:
        privilege_response = await self.bot.highrise.get_room_privilege(user.id)
        if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
            await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
            return

        taskgroup = self.bot.highrise.tg
        task_list: list[Task] = list(taskgroup._tasks)

        # Check if the bot is already emoting
        for task in task_list:
            if task.get_name() == "bot-emote":
                await self.bot.highrise.send_whisper(user.id, "The bot is already emoting.")
                return

        async def bot_emote_loop() -> None:
            while True:
                # Choose a random emote from the list
                emote_name = random.choice(emote_list)

                # Get the emote duration or use a default value
                sleep_duration = emote_durations.get(emote_name.lower(), 10)

                try:
                    await self.bot.highrise.send_emote(emote_name)
                except Exception as e:
                    await self.bot.highrise.send_whisper(user.id, f"Sorry, the bot can't perform the emote: {emote_name}. Error: {str(e)}")
                    return

                # Wait for the duration of the emote before doing the next one
                await asyncio.sleep(sleep_duration)

        # Start the bot's emote loop
        task = taskgroup.create_task(coro=bot_emote_loop())
        task.set_name("bot-emote")

        await self.bot.highrise.send_whisper(user.id, "Bot started emoting! Type 'Stopdance' to stop Bot emote.")

    async def stop_emote_bot(self, user: User, message: str) -> None:
        privilege_response = await self.bot.highrise.get_room_privilege(user.id)
        if not (privilege_response.moderator or user.username.lower() in OWNER_USER):
            await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
            return

        taskgroup = self.bot.highrise.tg
        task_list: list[Task] = list(taskgroup._tasks)

        # Cancel the bot's emote loop if it's running
        for task in task_list:
            if task.get_name() == "bot-emote":
                task.cancel()
                await self.bot.highrise.send_whisper(user.id, "Bot stopped emoting!")
                return

        await self.bot.highrise.send_whisper(user.id, "The bot is not emoting.")
