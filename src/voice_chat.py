from discord.ext.commands import Cog, command, Context


class VoiceChatCog(Cog):
    @command(name="vc create")
    async def create_voice_chat(ctx: Context, name):
        await ctx.send("should create voice chat")
        await ctx.guild.create_voice_channel(name)
