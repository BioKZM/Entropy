from pydoc import cli
import disnake
from disnake.ext import commands


class GlobalServerCount(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = self.client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusuna davet edildim.")

def setup(client):
    client.add_cog(GlobalServerCount(client))