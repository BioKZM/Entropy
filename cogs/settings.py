from logging import PlaceHolder
from threading import local
import disnake
import json
from disnake.ext import commands

class ChangeSettings(commands.Cog):
    
    def __init__(self,client):
        self.client = client

    

    @commands.slash_command(name = "settings",description = "Change Entropy's settings.")
    async def changeSettings(self,inter):

        with open(f"guildOptions/{inter.guild.id}.json") as file:
            data = json.load(file)
            lang = data['language']

        if lang == "tr":
            with open(f"localization/tr.json") as file:
                localization = json.load(file)
        else:
            with open(f"localization/en.json") as file:
                localization = json.load(file)


        


        # class BackView(disnake.ui.View):
        #     @disnake.ui.button(label = localization['SETTINGS_BACK_BUTTON_LABEL'])
        #     async def backButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
        #         embed = disnake.Embed(
        #             title = localization['SETTINGS_EMBED'],
        #             description = localization['SETTINGS_EMBED_DESCRIPTION']
        #         )
        #         await inter.response.send_message(embed=embed,view=MainView())

        class LanguageView(disnake.ui.View):
            options = [
                disnake.SelectOption(label = "Türkçe", value = "Entropy'nin dilini Türkçe'ye çevir.", emoji = "🇹🇷"),
                disnake.SelectOption(label = "English", value = "Change Entropy's language to English.", emoji = "🇺🇸"),
            ]
        
            @disnake.ui.button(label = localization['SETTINGS_BACK_BUTTON_LABEL'])
            async def backButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                # embed = disnake.Embed(
                #     title = localization['LANGUAGE_EMBED'],
                #     description = localization['LANGUAGE_EMBED_DESCRIPTION']
                # )
                await inter.response.edit_message(view = MainView(timeout=None))

            @disnake.ui.select(options = options)
            async def selectView(self,select:disnake.ui.Select, inter:disnake.Interaction):
                if select.values == ["tr"]:
                    
                    with open(f"guildOptions/{inter.guild.id}.json") as file:
                        data = json.load(file)

                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        data['language'] = "tr"
                        json.dump(data,file,indent=4)

                    with open(f"localization/tr.json") as file:
                        localization = json.load(file)

                    embed = disnake.Embed(
                        title = localization['SETTINGS_SELECT_EMBED_TITLE'],
                        description = localization['SETTINGS_SELECT_EMBED_DESCRIPTION']
                    )
                    await inter.response.send_message(embed=embed,hidden=True)
                
                if select.values == ["en"]:

                    with open(f"guildOptions/{inter.guild.id}.json") as file:
                        data = json.load(file)
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        data['language'] = "en"
                        json.dump(data,file,indent=4)   

                    with open(f"localization/en.json") as file:
                        localization = json.load(file)

                    embed = disnake.Embed(
                        title = localization['SETTINGS_SELECT_EMBED_TITLE'],
                        description = localization['SETTINGS_SELECT_EMBED_DESCRIPTION']
                    )
                
                    await inter.response.send_message(embed=embed,hidden=True)


        # class EmbedColorView(disnake.ui.View):
        #     @disnake.ui.select()


        class MainView(disnake.ui.View):
            @disnake.ui.button(label=localization['SETTINGS_LANGUAGE_BUTTON_LABEL'])
            async def languageButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                await inter.response.edit_message(view = LanguageView())
            # @disnake.ui.button(label=localization['SETTINGS_EMBED_COLOR_BUTTON_LABEL'])
            # async def embedButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
            #     await inter.response.edit_message(view = EmbedColorView())



        embed = disnake.Embed(
            title = localization['SETTINGS_EMBED'],
            description = localization['SETTINGS_EMBED_DESCRIPTION']
        )
        await inter.response.send_message(embed=embed,view=MainView())



def setup(client):
    client.add_cog(ChangeSettings(client))