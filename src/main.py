import os
from la_bot.client import Client
from discord import Intents

BOT_TOKEN = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    intents = Intents.default()
    intents.message_content = True

    la_bot = Client(intents=intents)
    la_bot.run(BOT_TOKEN)
