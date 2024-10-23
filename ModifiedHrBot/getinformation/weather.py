from highrise import BaseBot, User
import httpx


class Weather:
    APIKEY: str = "1e6fcc8725dc442aba8140211241009"  # API key for weatherapi.com
 
    def __init__(self, bot: BaseBot):
        self.bot = bot

    async def handle_command(self, user: User, message: str) -> None:
        """Check if the message starts with !w and handle the weather command."""
        if message.lower().startswith("!weather"):
            location = message[8:].strip()  # Slice the message to extract the location
            if not location:
                await self.bot.highrise.chat(f"@{user.username} Please provide a location after the command.")
                return

            response = await self.get_weather_data(location)

            if response is not None:
                # Convert the response to JSON format
                data = response.json()
                if "current" in data:
                    # Extract and display the current temperature
                    await self.bot.highrise.chat(
                        f"The current temperature in {location} is:\n{data['current']['temp_c']} °C\n{data['current']['temp_f']} °F"
                    )
                elif "error" in data:
                    await self.bot.highrise.chat("Please provide a correct location.")
                else:
                    await self.bot.highrise.chat(f"Unrecognized location: {location}")
            else:
                await self.bot.highrise.chat("Failed to retrieve weather data.")

    async def get_weather_data(self, location: str) -> httpx.Response:
        """Retrieves and returns the weather data based on the provided location"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"http://api.weatherapi.com/v1/current.json?key={self.APIKEY}&q={location}")
            return response