import disnake
import json
from disnake.ext import commands

def getlang(client,message):
    with open(f"guildOptions/{str(message.guild.id)}.json") as file:
        data = json.load(file)
    return data['lang']

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.lang = (getlang)

    @commands.slash_command(name = "avatar", description = "")
    async def level(self,inter,sayı = commands.Param(
        name = "sayı",
        description = "Lütfen bir sayı gir!"
    )):
        await inter.response.send_message(self.lang)

def setup(client):
    client.add_cog(Avatar(client))