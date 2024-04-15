import os
import logging
from voice_chat_cog import VoiceChatCog
from discord.ext.commands import Bot, Context
from discord import Intents


class LaBot(Bot):
    async def on_ready(self):
        await self.add_cog(VoiceChatCog())
        print("Ready!")

        @self.command()
        async def close(ctx: Context):
            await la_bot.close()

        @self.command()
        async def echo(ctx: Context, *, what_to_echo):
            await ctx.send(what_to_echo)


if __name__ == "__main__":
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

    intents = Intents.default()
    intents.message_content = True

    la_bot = LaBot("la_bot/", intents=intents)
    la_bot.run(BOT_TOKEN, log_level=logging.DEBUG)  # , log_handler=handler, log_level=logging.DEBUG)
