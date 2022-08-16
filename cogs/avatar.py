import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = Localized(key="ADD_NUM_NAME"), description = "Bir kullanıcının seviyesini görüntülemek için kullan")
    async def level(self,inter,sayı):

        """
        Bir sayıya 5 ekler. {{ADD_NUM}}

        Parameters
        ----------
        sayı : Bir sayı gir {{COOL_NUMBER}}
        """
        await inter.response.send_message("Test")


def setup(client):
    client.add_cog(Avatar(client))