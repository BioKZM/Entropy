import disnake
import json
import shutil
import os
from datetime import datetime 
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
        systemChannel = guild.system_channel
        if systemChannel == None:
            list = guild.channels
            systemChannel = list[0] if channel.type == disnake.ChannelType.text else ""

        try:
            os.mkdir(f"guilds/{guild.id}")
            os.mkdir(f"guilds/{guild.id}/options")
            os.mkdir(f"guilds/{guild.id}/levels")
            os.mkdir(f"guilds/{guild.id}/files")
            os.mkdir(f"guilds/{guild.id}/files/TTS")
            os.mkdir(f"guilds/{guild.id}/files/images")
            os.mkdir(f"guilds/{guild.id}/files/presets")


            with open(f"guilds/{guild.id}/options/{guild.id}.json","w") as file:
                data = {
                    "language" : "en",
                    "embedColor" : "0xCC0000",
                    "defaultChannel" : systemChannel.id
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
                with open(f"guilds/{guild.id}/files/presets/{member.id}.json","w") as file:
                    data = {
                        "slot_1": None,
                        "slot_2": None,
                        "slot_3": None,
                        "slot_4": None,
                        "slot_5": None,
                        "slot_6": None,
                        "slot_7": None,
                        "slot_8": None,
                        "slot_9": None,
                        "slot_10": None
                    }
                    json.dump(data,file,indent=4)

        except Exception as err:
            channel = self.client.get_channel(1009425217669582969)
            await channel.send(f"**{guild}** sunucusunun dosyalar?? olu??turulamad??! Hata kodu : ```{err}```")

        with open(f"guilds/{guild.id}/options/{guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            language = data['language']

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        embed = disnake.Embed(
            title = f"{localization['ON_GUILD_JOIN_EMBED_TITLE']}",
            description = f"{localization['ON_GUILD_JOIN_EMBED_DESCRIPTION'].format(systemChannel = systemChannel.mention)}",
            color = embedColor
        )
        embed.set_footer(text="Entropy", icon_url = guild.me.display_avatar.url)
        embed.timestamp = datetime.now()
        await systemChannel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        try:
            shutil.rmtree(f'guilds/{guild.id}')
        except Exception as err:
            channel = self.client.get_channel(1009425217669582969)
            await channel.send(f"**{guild}** sunucusunun dosyalar?? silinemedi. Hata kodu : ```{err}```")

        channel = self.client.get_channel(1009425217669582969)
        await channel.send(f"**{guild}** sunucusundan at??ld??m.")
        channel = self.client.get_channel(1009434779508281385)
        await channel.edit(name = f"Mevcut Sunucular : {len(self.client.guilds)}")
        
        



def setup(client):
    client.add_cog(GlobalServerCount(client))
