import os
from la_bot.bot import Bot
from la_bot.command_tree import CommandTree
from discord import Intents

BOT_TOKEN = os.getenv("BOT_TOKEN")

if __name__ == "__main__":
    intents = Intents.default()
    intents.message_content = True

    la_bot = Bot("la_bot/", intents=intents, tree_cls=CommandTree)
    la_bot.run(BOT_TOKEN)
