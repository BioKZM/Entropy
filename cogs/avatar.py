from threading import local
import disnake
import json
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "avatar", description = "Display an user's avatar.")
    async def avatar(self,inter,member:disnake.Member = None):
        
        with open(f"guilds/{inter.guild.id}/optipns/{inter.guild.id}.json") as file:
            data = json.load(file)
            lang = data['language']

        if lang == "tr":
            with open("localization/tr.json") as file:
                localization = json.load(file)

        if member == None:
            member = inter.author



        class GlobalView(disnake.ui.View):
            @disnake.ui.button(label = localization['AVATAR_LABEL_GLOBAL'],style = disnake.ButtonStyle.green)
            async def globalAvatar(self,button:disnake.ui.Button,inter:disnake.Interaction):
                embed = disnake.Embed(
                    title = f"{member} {localization['AVATAR_EMBED_TITLE']}",
                    description = "\n",
                )
                embed.set_image(url=member.avatar.url)
                
                await inter.response.edit_message(embed=embed,view=DisplayView(timeout=None))


        class DisplayView(disnake.ui.View):
            @disnake.ui.button(label = localization['AVATAR_LABEL_DISPLAY'],style = disnake.ButtonStyle.green)
            async def displayAvatar(self,button:disnake.ui.Button,inter:disnake.Interaction):
                embed = disnake.Embed(
                    title = f"{member.display_name}#{member.discriminator} {localization['AVATAR_EMBED_TITLE']}",
                    description = "\n",
                )
                embed.set_image(url=member.display_avatar.url)
                await inter.response.edit_message(embed=embed,view=GlobalView(timeout=None))


        embed = disnake.Embed(
            title = f"{member.display_name}#{member.discriminator} {localization['AVATAR_EMBED_TITLE']}",
            description = "\n",
        )
        embed.set_image(url=member.display_avatar.url)

        await inter.response.send_message(embed=embed,view=GlobalView(timeout=None))


def setup(client):
    client.add_cog(Avatar(client))