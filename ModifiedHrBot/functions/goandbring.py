from highrise import BaseBot, User, Position
from owner import OWNER_USER

class GoAndBringCommands:
    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def has_permission(self, user: User) -> bool:
        """Check if the user is a moderator."""
        privilege_response = await self.bot.highrise.get_room_privilege(user.id)
        return privilege_response.moderator or user.username.lower() in OWNER_USER

    async def teleport_to_user(self, user: User, target_username: str) -> None:
        # Check user permission before proceeding
        if not await self.has_permission(user):
            await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
            return
        
        try:
            response = await self.bot.highrise.get_room_users()
            for target, position in response.content:
                if target.username.lower() == target_username.lower():
                    new_position = Position(position.x + 1, position.y, position.z, position.facing)
                    await self.bot.highrise.teleport(user.id, new_position)
                    break
        except Exception as e:
            print(f"An error occurred while teleporting to {target_username}: {e}")

    async def teleport_user_to_me(self, user: User, target_username: str) -> None:
        # Check user permission before proceeding
        if not await self.has_permission(user):
            await self.bot.highrise.send_whisper(user.id, "You don't have permission to use this command.")
            return

        try:
            response = await self.bot.highrise.get_room_users()
            my_position = next((pos for usr, pos in response.content if usr.id == user.id), None)
            if my_position is None:
                print("Unable to retrieve your position.")
                return

            for target, _ in response.content:
                if target.username.lower() == target_username.lower():
                    new_position = Position(my_position.x + 1, my_position.y, my_position.z, facing='FrontRight')
                    await self.bot.highrise.teleport(target.id, new_position)
                    break
        except Exception as e:
            print(f"An error occurred while teleporting {target_username} to you: {e}")

    async def handle_command(self, user: User, message: str) -> None:
        # This method will already handle permission checks for the commands
        if message.startswith("!goto"):
            target_username = message.split("@")[-1].strip()
            await self.teleport_to_user(user, target_username)
        
        elif message.startswith("!bring"):
            target_username = message.split("@")[-1].strip()
            await self.teleport_user_to_me(user, target_username)