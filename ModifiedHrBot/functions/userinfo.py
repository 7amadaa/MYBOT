from highrise import BaseBot, User
from highrise.webapi import *
from highrise.models_webapi import *



class UserInfo:

    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def handle_command(self, user: User, message: str) -> None:
        # Check if the message starts with the correct command
        if message.lower().startswith("!userinfo"):
            parts = message.split(" ")
            if len(parts) != 2:
                await self.bot.highrise.chat("Incorrect format, please use !userinfo <@username>")
                return

            # Remove the '@' from the username if it exists
            if parts[1].startswith("@"):
                username = parts[1][1:]
            else:
                username = parts[1]

            # Get the user ID from the username
            user_data = await self.bot.webapi.get_users(username=username, limit=1)
            if user_data and user_data.users:
                user_id = user_data.users[0].user_id
            else:
                await self.bot.highrise.chat("User not found, please specify a valid user")
                return

            # Get the user info
            userinfo = await self.bot.webapi.get_user(user_id)
            number_of_followers = userinfo.user.num_followers
            number_of_friends = userinfo.user.num_friends
            number_of_following = userinfo.user.num_following
            joined_at = userinfo.user.joined_at.strftime("%d/%m/%Y %H:%M:%S")

            try:
                last_login = userinfo.user.last_online_in.strftime("%d/%m/%Y %H:%M:%S")
            except Exception:
                last_login = "Last login not available"

            # Get the number of posts and the most liked post
            userposts = await self.bot.webapi.get_posts(author_id=user_id)
            number_of_posts = 0
            most_likes_post = 0
            try:
                while userposts.last_id != "":
                    for post in userposts.posts:
                        if post.num_likes > most_likes_post:
                            most_likes_post = post.num_likes
                        number_of_posts += 1
                    userposts = await self.bot.webapi.get_posts(author_id=user_id, starts_after=userposts.last_id)
            except Exception as e:
                print(e)

            # Send the info to the chat
            await self.bot.highrise.chat(
                f"""User: {username}\nNumber of followers: {number_of_followers}\nNumber of friends: {number_of_friends}\nNumber of following: {number_of_following}\nJoined at: {joined_at}\nLast login: {last_login}\nNumber of posts: {number_of_posts}\nMost likes in a post: {most_likes_post}"""
            )
