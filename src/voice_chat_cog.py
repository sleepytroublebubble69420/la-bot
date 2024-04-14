from discord.ext.commands import Cog, command, Context
from discord import Member, VoiceState


class VoiceChatCog(Cog):
    @Cog.listener()
    async def on_voice_state_update(self, member: Member, ex_voice_state: VoiceState, voice_state: VoiceState):
        if voice_state.channel is not None:
            print(f"{member.name} joined {voice_state.channel.name}")
        else:
            print(f"{member.name} left {ex_voice_state.channel.name}")

    @command(name="mkvc")
    async def create_voice_chat(self, ctx: Context, name):
        await ctx.send("should create voice chat")
        await ctx.guild.create_voice_channel(name)

    @command(name="rnvc")
    async def rename_voice_chat(self, ctx: Context, *, name):
        await ctx.send("should rename voice chat")
        await ctx.guild.create_voice_channel(name)
