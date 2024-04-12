from discord import Object
from discord.ext import commands
from discord.ext.commands import hybrid_command, Context


class Bot(commands.Bot):
    async def on_ready(self):
        self.add_command(close)
        self.add_command(sync_tree)
        print("Ready!")


@hybrid_command()
async def close(ctx: Context):
    await ctx.bot.close()


@hybrid_command()
async def sync_tree(ctx: Context):
    guild_id = ctx.guild.id
    print(f"Trying to sync tree for guild (id = {guild_id})")
    await ctx.bot.tree.sync(guild=Object(id=guild_id))
    print(f"Tree should be synced for guild (id = {guild_id})")
