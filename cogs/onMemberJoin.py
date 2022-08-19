import disnake
import json
from disnake.ext import commands


class OnMemberJoin(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.Cog.listener()
    async def on_member_join(self,member):
        guild = member.guild
        with open(f"guilds/{guild.id}/levels/{member.id}","w") as file:
            data = {
                    "XP" : 1,
                    "maximumXP" : 1000,
                    "level" : 0,
                    "XPmax" : 1000,
                    "XPmin" : 0,
                    "XPdiv" : 10
                    }
            json.dump(data,file,indent=4)

def setup(client):
    client.add_cog(OnMemberJoin(client))