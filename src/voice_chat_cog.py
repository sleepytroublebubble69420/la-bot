from discord.ext.commands import Cog, command, Context
from discord import Member, VoiceState


class VoiceChatCog(Cog):
    def __init__(self):
        self.dynamicly_named_channels_id: list = []
        self.dynamic_names: dict = {}

    @Cog.listener()
    async def on_voice_state_update(self, member: Member, ex_voice_state: VoiceState, voice_state: VoiceState):
        channel = voice_state.channel
        channel = ex_voice_state.channel if channel is None else channel

        if channel.id in self.dynamicly_named_channels_id:
            dynamic_name = self.dynamic_names[channel.id]
            member_count = len(channel.members)
            formatted_name = dynamic_name.replace("?", str(member_count))
            await channel.edit(name=formatted_name)

    @command(name="mkvc")
    async def create_voice_chat(self, ctx: Context, name):
        await ctx.send("should create voice chat")
        await ctx.guild.create_voice_channel(name)

    @command(name="rnvc")
    async def rename_voice_chat(self, ctx: Context, *, name):
        await ctx.send("should rename voice chat")
        await ctx.guild.create_voice_channel(name)

    @command(name="vcsetdname")
    async def voice_chat_set_dynamic_name(self, ctx: Context, channel_id: int, dynamic_name=""):
        if channel_id not in self.dynamicly_named_channels_id:
            self.dynamicly_named_channels_id.append(channel_id)
        self.dynamic_names[channel_id] = dynamic_name

        channel = ctx.guild.get_channel(channel_id)
        member_count = len(channel.members)
        formatted_name = dynamic_name.replace("?", str(member_count))
        await channel.edit(name=formatted_name)
