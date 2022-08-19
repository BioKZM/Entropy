import disnake
import json
from disnake.ext import commands



class ChangeColor(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.slash_command(name = "change")
    async def change(self,inter):
        pass

    @change.sub_command(name = "color",description = "Change Entropy's embedded message colors manual `Example color code : CC0000")
    async def changeColor(self,inter,color):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            language = data['language']

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json","w") as file:
            data['embedColor'] = f"0x{color}"
            embedColor = int(data['embedColor'],16) 
            json.dump(data,file,indent=4)

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        embed = disnake.Embed(
            title = localization['COLOR_CHANGE_EMBED_TITLE'],
            description = f"{localization['COLOR_CHANGE_EMBED_DESCRIPTION']} {color}",
            color = embedColor
        )

        await inter.response.send_message(embed=embed,ephemeral=True)


def setup(client):
    client.add_cog(ChangeColor(client))