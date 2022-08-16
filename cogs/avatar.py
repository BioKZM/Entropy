import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "level", description = "Bir kullanıcının seviyesini görüntülemek için kullan")
    async def level(self,inter,sayı = commands.Param(
        name = "sayı",
        description = "Lütfen bir sayı gir!"
    )):


        await inter.response.send_message("Test")


def setup(client):
    client.add_cog(Avatar(client))