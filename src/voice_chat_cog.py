from discord.ext.commands import Cog, command, Context


class VoiceChatCog(Cog):
    @command(name="vc_create")
    async def create_voice_chat(self, ctx: Context, name):
        await ctx.send("should create voice chat")
        await ctx.guild.create_voice_channel(name)
