from pydoc import cli
import disnake
from disnake.ext import commands
client = commands.Bot(command_prefix="!",intents = disnake.Intents.all(), help_command=None)
class GlobalServerCount(commands.Cog):
    def __init__(self, client):
        self.client = client
        



    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusuna davet edildim.")
        channel = client.get_channel(1009434779508281385)
        await channel.edit(name = f"Mevcut Sunucular : {len(self.client.guilds)}")


    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        channel = client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusundan atıldım.")
        channel = client.get_channel(1009434779508281385)
        await channel.edit(name = f"Mevcut Sunucular : {len(self.client.guilds)}")

def setup(client):
    client.add_cog(GlobalServerCount(client))