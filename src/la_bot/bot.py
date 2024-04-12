from discord.ext import commands
from discord.ext.commands import command, Context


class Bot(commands.Bot):
    async def on_ready(self):
        self.add_command(close)
        print("Ready!")


@command()
async def close(ctx: Context):
    await ctx.bot.close()
