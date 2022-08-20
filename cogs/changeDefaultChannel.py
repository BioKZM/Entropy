import disnake
import json
from datetime import datetime 
from disnake.ext import commands

class ChangeDefaultChannel(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "default")
    async def default(self, inter):
        pass

    @default.sub_command(name = "channel",description = "Change default channel for leveling messages.")
    async def changeDefaultChannel(self,inter,channel:disnake.TextChannel):
        """
        Parameters
        ----------
        channel: Select a text channel.
        """
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            language = data['language']

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json","w") as file:
            data['defaultChannel'] = channel.id
            json.dump(data,file,indent=4)
        
        embed = disnake.Embed(
            title = localization['CHANGE_DEFAULT_CHANNEL_EMBED_TITLE'],
            description = localization['CHANGE_DEFAULT_CHANNEL_EMBED_DESCRIPTION'].format(channel = channel.mention),
            color = embedColor
        )
        embed.set_footer(text = "Entropy", icon_url = inter.client.display_avatar.url)
        embed.timestamp = datetime.now()
        await inter.response.send_message(embed=embed,ephemeral=True)
    
def setup(client):
    client.add_cog(ChangeDefaultChannel(client))
