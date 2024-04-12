import os
from discord import Client, Intents, Object, Interaction
from discord.app_commands import CommandTree

BOT_TOKEN = os.getenv("BOT_TOKEN")
DEBUG_GUILD_ID = os.getenv("DEBUG_GUILD_ID")

intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)
command_tree = CommandTree(client)


# @command_tree.command(
#     name="ping",
#     description="sends \"pong\"",
# )
# async def gping(interaction: Interaction):
#     await interaction.response.send_message("pong")


@client.event
async def on_ready():
    # command_tree.clear_commands(guild=Object(id=DEBUG_GUILD_ID))
    print(len(command_tree.get_commands()))
    await command_tree.sync(guild=Object(id=DEBUG_GUILD_ID))
    print("Ready!")


if __name__ == "__main__":
    client.run(BOT_TOKEN)
