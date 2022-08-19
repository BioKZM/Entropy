import disnake
import json
import shutil
import os
from disnake.ext import commands
class GlobalServerCount(commands.Cog):
    def __init__(self, client):
        self.client = client
        



    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        channel = self.client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusuna davet edildim.")
        channel = self.client.get_channel(1009434779508281385)
        await channel.edit(name = f"Mevcut Sunucular : {len(self.client.guilds)}")

        try:
            os.mkdir(f"guilds/{guild.id}")
            os.mkdir(f"guilds/{guild.id}/options")
            os.mkdir(f"guilds/{guild.id}/levels")
            os.mkdir(f"guilds/{guild.id}/files/TTS")

            with open(f"guilds/{guild.id}/options/{guild.id}.json","w") as file:
                data = {
                    "language" : "en",
                    "embedColor" : "0xCC0000"
                }
                json.dump(data,file,indent=4)


            for member in guild.members:
                with open(f"guilds/{guild.id}/levels/{member.id}.json","w") as file:
                    data = {
                        "XP" : 1,
                        "maximumXP" : 1000,
                        "level" : 0,
                        "XPmax" : 1000,
                        "XPmin" : 0,
                        "XPdiv" : 10
                    }
                    json.dump(data,file,indent=4)
        except Exception as err:
            channel = self.client.get_channel(1009425217669582969)
            await channel.send(f"**{guild}** sunucusunun dosyaları oluşturulamadı! Hata kodu : ```{err}```")


    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        try:
            shutil.rmtree(f'guilds/{guild.id}')
        except Exception as err:
            channel = self.client.get_channel(1009425217669582969)
            await channel.send(f"**{guild}** sunucusunun dosyaları silinemedi. Hata kodu : ```{err}```")

        channel = self.client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusundan atıldım.")
        channel = self.client.get_channel(1009434779508281385)
        await channel.edit(name = f"Mevcut Sunucular : {len(self.client.guilds)}")
        
        



def setup(client):
    client.add_cog(GlobalServerCount(client))