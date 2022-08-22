import disnake
import json
from disnake.ext import commands

class Help(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    @commands.slash_command(name = "help",description = "Show commands and descriptions")
    async def help(self,inter,option=None):
        """
        Parameters
        ----------
        option : Select an command to see how it works
        """
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            language = data['language']
            embedColor = int(data['embedColor'],16)

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        optionList = [
            "avatar",
            "level",
            "help",
            "settings",
            "change color",
            "default channel",
            "speak",
            "soundboard"
        ]

        if option == None:
            embed = disnake.Embed(
                title = localization['HELP_EMBED_TITLE'],
                description = localization['HELP_EMBED_DESCRIPTION'],
                color = embedColor
            )
            embed.add_field(name = localization['HELP_EMBED_ADD_FIELD_SOUND_TITLE'],value = localization['HELP_EMBED_ADD_FIELD_SOUND_VALUE'])
        else:
            if option in optionList:
                embed = disnake.Embed(
                    title = localization[''],
                    description = localization[''],
                    color = embedColor
                )
            
        #TODO : Yerelleştirme verileri yazılacak ve tamamı tr.json dosyasına aktarılacak.
        
        await inter.response.send_message(embed=embed)





def setup(client):
    client.add_cog(Help(client))


