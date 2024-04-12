from discord.ext import commands
from discord.ext.commands import command, Context
from .command_tree import CommandTree


class Bot(commands.Bot):
    async def on_ready(self):
        command_tree = CommandTree(self)
        print("Ready!")


@command()
async def close(ctx: Context):
    await ctx.bot.close()
