import disnake
import json
from disnake.ext import command


class Help(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    @commands.slash_command(name = "help",description = "Show commands and descriptions")
    async def help(self,inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            language = data['language']
            embedColor = data['embedColor']


        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        embed = disnake.Embed(
            title = localization[''],
            description = localization[''],
            color = embedColor
        )
        embed.add_field(name = localization['HELP_EMBED_ADD_FIELD_SOUND_TITLE'],value = localization['HELP_EMBED_ADD_FIELD_SOUND_VALUE'])
        await inter.response.send_message(embed=embed)





def setup(client):
    client.add_cog(Help(client))


