import disnake
from disnake.ext import commands

class ChangeDefaultChannel(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "default")
    async def default(self, inter):
        pass

    @default.sub_command(name = "channel",description = "Change default channel for leveling messages.")
    async def changeDefaultChannel(self,inter,channel:disnake.Channel):
        """
        Parameters
        ----------
        channel: Select a text channel.
        """
        pass
    
