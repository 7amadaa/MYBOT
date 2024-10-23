from highrise import BaseBot, User
import httpx

class AskAi:

    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def handle_command(self, user: User, message: str):
        if message.lower().startswith("!ask"):  # Check if the message starts with !ask
            await self.handle_duck_command(message[4:].strip(), user)  # Extract the query in a case-insensitive way

    async def handle_duck_command(self, query: str, user: User) -> None:
        """Handler for the !ask command"""
        if not query.strip():
            await self.bot.highrise.send_whisper(user.id, "Please provide a search term after the command.")
            return

        answer = await self.get_duck_answer(query)

        if answer:
            for part in self.split_message(answer):
                await self.bot.highrise.send_whisper(user.id, part)  # Send the response as a whisper
        else:
            await self.bot.highrise.send_whisper(user.id, "Sorry, cannot find any results.")

    async def get_duck_answer(self, query: str) -> str:
        """Retrieves and returns an answer from DuckDuckGo based on the provided query."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.duckduckgo.com/",
                params={
                    "q": query,
                    "format": "json",
                    "no_html": 1,
                    "skip_disambig": 1
                },
            )
            
            data = response.json()

            if "AbstractText" in data and data["AbstractText"]:
                return data["AbstractText"]

            if "RelatedTopics" in data and data["RelatedTopics"]:
                return data["RelatedTopics"][0].get("Text", "")
        
        return None

    def split_message(self, message: str) -> list:
        """Splits the message into chunks of 256 characters or less."""
        return [message[i:i + 256] for i in range(0, len(message), 256)]