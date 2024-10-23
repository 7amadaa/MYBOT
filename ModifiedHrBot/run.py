from highrise.__main__ import *
import time

bot_file_name = "bot"
bot_class_name = "Mybot"
room_id = "66d2fc7b2e80dd1f6150da76"
bot_token = "cfe5cc11532d49f935f253dc8ef4a0bc87bb4993b3f6a3d250eb50bba95e9271"

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

# ANSI escape code for purple text (magenta)
PURPLE_COLOR = "\033[95m"
RESET_COLOR = "\033[0m"

while True:
    try:
        definitions = [my_bot]
        # Wrap this in a try-except block for KeyboardInterrupt
        try:
            arun(main(definitions))
        except KeyboardInterrupt:
            print(f"{PURPLE_COLOR}Bot is offline{RESET_COLOR}")  # Message in purple when Ctrl + C is pressed
            break  # Exit the while loop
    except Exception as e:
        print(f"An exception occurred: {e}")
        time.sleep(5)
