import discord
from discord import Interaction
from discord.app_commands import command


class CommandTree(discord.app_commands.CommandTree):
    def __init__(self, client):
        super().__init__(client)
        self.add_command(ping)
        print("Command Tree initialised")


@command()
async def ping(interaction: Interaction):
    """Respond with a \"pong!\""""
    await interaction.response.send_message("pong!")
