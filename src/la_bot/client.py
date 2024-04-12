import discord
from .command_tree import CommandTree


class Client(discord.Client):
    async def on_ready(self):
        command_tree = CommandTree(self)
        app_commands = await command_tree.sync(guild=None)
        print("Command tree should be synced")
        print(app_commands)

        print("Ready!")
