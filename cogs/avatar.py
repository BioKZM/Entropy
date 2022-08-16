import disnake
from disnake.ext import commands

class Avatar(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "avatar", description = "Display an user's avatar.")
    async def avatar(self,inter,member:disnake.Member = None):
        
        if member == None:
            member = inter.author



        class GlobalView(disnake.ui.View):
            @disnake.ui.button(label = "Global Avatar",style = disnake.ButtonStyle.green)
            async def globalAvatar(self, inter:disnake.Interaction, button:disnake.ui.Button):
                embed = disnake.Embed(
                    title = f"{member.name}'s avatar",
                    description = "\n",
                )
                embed.set_image(url=member.avatar.url)
                
                await inter.response.edit_message(embed=embed,view=DisplayView(timeout=None))


        class DisplayView(disnake.ui.View):
            @disnake.ui.button(label = "Display Avatar",style = disnake.ButtonStyle.green)
            async def displayAvatar(self,inter:disnake.Interaction,button:disnake.ui.Button):
                embed = disnake.Embed(
                    title = f"{member.display_name}'s avatar",
                    description = "\n",
                )
                embed.set_image(url=member.display_avatar.url)
                await inter.response.edit_message(embed=embed,view=GlobalView(timeout=None))


        embed = disnake.Embed(
            title = f"{member.display_name}'s avatar",
            description = "\n",
        )
        embed.set_image(url=member.display_avatar.url)

        await inter.response.send_message(embed=embed,view=GlobalView(timeout=None))


def setup(client):
    client.add_cog(Avatar(client))