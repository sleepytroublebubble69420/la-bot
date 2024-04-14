import os
import logging
from bot import Bot
from discord import Intents


if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

    intents = Intents.default()
    intents.message_content = True

    la_bot = Bot("la_bot/", intents=intents)
    la_bot.run(BOT_TOKEN, log_handler=handler, log_level=logging.DEBUG)
