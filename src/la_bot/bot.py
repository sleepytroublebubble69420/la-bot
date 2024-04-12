from discord.ext import commands
from .command_tree import CommandTree


class Bot(commands.Bot):
    async def on_ready(self):
        command_tree = CommandTree(self)
        print("Ready!")
