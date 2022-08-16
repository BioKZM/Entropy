import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = disnake.Localized(key="AVATAR_NAME"), description = disnake.Localized(key = "AVATAR_DESCRIPTION"))
    async def level(self,inter,sayı = commands.Param(name = disnake.Localized(key="MEMBER_NAME"),description = disnake.Localized(key = "MEMBER_DESCRIPTION"))):
        await inter.response.send_message("Test")


def setup(client):
    client.add_cog(Avatar(client))