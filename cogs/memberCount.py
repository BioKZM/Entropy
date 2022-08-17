import disnake
import json
from disnake.ext import commands

class MemberCount(commands.Cog):
    def __init__(self, client):
        self.client = client


    async def createCategoryChannel(self,inter,name):
        overwrites = {
            inter.guild.default_role : disnake.PermissionOverwrite(
                view_channel = True,
                connect = False,
                manage_channels = False,
            )
        }

    async def createVoiceChannel(self,inter,name,category,topic=None):
        guild = inter.guild
        await guild.create_voice_channel(name=name,category=category,topic=topic)


    @commands.slash_command(name = "statistics")
    async def statistics(self,inter):
        pass

    @statistics.sub_command(name = "setup", description = "Setup a member statistic panel")
    async def statisticsSetup(self,inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = data['embedColor']
            lang = data['language']

        if lang == "tr":
            with open(f"localization/tr.json") as file:
                localization = json.load(file)
        category = await self.createCategoryChannel(inter,localization['SERVER_STATISTICS_CATEGORY_NAME'])
        await self.createVoiceChannel(inter,f"{localization['SERVER_STATISTICS_MEMBER_COUNT']} {inter.guild.member_count}",category)

    @statistics.sub_command(name = "delete", description = "Delete member statistic panel")
    async def statisticsDelete(self,inter):
        pass


def setup(client):
    client.add_cog(MemberCount(client))


