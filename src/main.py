import os
from la_bot import LaBot
from discord import Intents

BOT_TOKEN = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    intents = Intents.default()
    intents.message_content = True

    client = LaBot(intents=intents)
    client.run(BOT_TOKEN)
