import disnake
import json
from disnake.ext import commands,tasks


class MemberCountLoop(commands.Cog):
    def __init__(self,client):
        self.client = client


    @tasks.loop(minutes = 1)
    async def memberCountLoop(self,inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}") as file:
            data = json.load(file)
            language = data['lang']
            voiceChannel = data['voiceChannelID']

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        channel = inter.guild.get_channel(int(voiceChannel))
        memberCount = inter.guild.member_count
        await channel.edit(name = f"{localization['SERVER_STATISTICS_MEMBER_COUNT']} {memberCount}")


def setup(client):
    client.add_cog(MemberCountLoop(client))