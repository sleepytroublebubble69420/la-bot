from discord import Client
from discord.app_commands import CommandTree


class LaBot(Client):
    async def on_ready(self):
        command_tree = CommandTree(self)
        command_tree.clear_commands(guild=None)
        await command_tree.sync(guild=None)

        print("Ready!")
