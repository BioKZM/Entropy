from turtle import position
import disnake
import json
import asyncio
from disnake.ext import commands

class MemberCount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name = "statistics")
    async def statistics(self,inter):
        pass

    @statistics.sub_command(name = "setup", description = "Setup a member statistic panel")
    async def statisticsSetup(self,inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        if lang == "tr":
            with open(f"localization/tr.json") as file:
                localization = json.load(file)

        if lang == "en":
            with open(f"localization/en.json") as file:
                localization = json.load(file)

        overwrites = {
            inter.guild.default_role : disnake.PermissionOverwrite(
                view_channel = True,
                connect = False,
                manage_channels = False,
            )
        }
        category = await inter.guild.create_category_channel(name = localization['SERVER_STATISTICS_CATEGORY_NAME'],overwrites = overwrites)
        voiceChannel = await inter.guild.create_voice_channel(name = f"{localization['SERVER_STATISTICS_MEMBER_COUNT']} {inter.guild.member_count}",category = category)
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json","w") as file:
            data['categoryID'] = category.id
            data['voiceChannelID'] = voiceChannel.id
            json.dump(file,data,indent=4)

        embed = disnake.Embed(
            title = localization["SERVER_STATISTICS_SETUP_EMBED_TITLE"],
            description = localization['SERVER_STATISTICS_SETUP_EMBED_DESCRIPTION'],
            color = embedColor
        )
        await inter.response.send_message(embed=embed,ephemeral=True)

        

    @statistics.sub_command(name = "delete", description = "Delete member statistic panel")
    async def statisticsDelete(self,inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']
            categoryID = data['categoryID']
            voiceChannelID = data['voiceChannelID']


        if lang == "tr":
            with open(f"localization/tr.json") as file:
                localization = json.load(file)

        elif lang == "en":
            with open(f"localization/en.json") as file:
                localization = json.load(file) 

        categoryChannel = inter.guild.get_channel(int(categoryID))
        voiceChannel = inter.guild.get_channel(int(voiceChannelID))
        await categoryChannel.delete()
        await voiceChannel.delete()

        embed = disnake.Embed(
            title = localization['SERVER_STATISTICS_DELETE_EMBED_TITLE'],
            description = localization['SERVER_STATISTICS_DELETE_EMBED_DESCRIPTION'],
            color = embedColor
        )
        await inter.response.send_message(embed=embed,ephemeral=True)
                


def setup(client):
    client.add_cog(MemberCount(client))


