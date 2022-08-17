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
            embedColor = int(data['embedColor'],16)

        if lang == "tr":
            with open(f"localization/tr.json") as file:
                localization = json.load(file)
        else:
            with open(f"localization/en.json") as file:
                localization = json.load(file)

        class LanguageView(disnake.ui.View):
            
            options = [
                disnake.SelectOption(label = "Türkçe", value = "tr", emoji = "🇹🇷"),
                disnake.SelectOption(label = "English", value = "en", emoji = "🇺🇸"),
            ]

            @disnake.ui.select(options = options)
            async def selectView(self,select:disnake.ui.Select, inter:disnake.Interaction):
                
                if select.values == ["tr"]:
                    
                    with open(f"guildOptions/{inter.guild.id}.json") as file:
                        data = json.load(file)
                        embedColor = int(data['embedColor'],16)

                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        data['language'] = "tr"
                        json.dump(data,file,indent=4)

                    with open(f"localization/tr.json") as file:
                        localization = json.load(file)

                    embed = disnake.Embed(
                        title = localization['SETTINGS_SELECT_EMBED_TITLE'],
                        description = localization['SETTINGS_SELECT_EMBED_DESCRIPTION'],
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)
                
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
                
                    await inter.response.send_message(embed=embed,ephemeral=True)

            @disnake.ui.button(label = localization['SETTINGS_BACK_BUTTON_LABEL'])
            async def backButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                with open(f"guildOptions/{inter.guild.id}.json") as file:
                    data = json.load(file)
                    embedColor = int(data['embedColor'],16)

                embed = disnake.Embed(
                    title = localization['SETTINGS_EMBED_TITLE'],
                    description = localization['SETTINGS_EMBED_DESCRIPTION'],
                    color = embedColor
                )
                await inter.response.edit_message(view = MainView(timeout=None))

        class EmbedColorView(disnake.ui.View):
            options = [
                disnake.SelectOption(label = localization['COLOR_RED'], value = "red", emoji = "🟥"),
                disnake.SelectOption(label = localization['COLOR_ORANGE'], value = "orange", emoji = "🟧"),
                disnake.SelectOption(label = localization['COLOR_YELLOW'], value = "yellow", emoji = "🟨"),
                disnake.SelectOption(label = localization['COLOR_GREEN'], value = "green", emoji = "🟩"),
                disnake.SelectOption(label = localization['COLOR_BLUE'], value = "blue", emoji = "🟦"),
                disnake.SelectOption(label = localization['COLOR_PURPLE'], value = "purple", emoji = "🟪"),
                disnake.SelectOption(label = localization['COLOR_BROWN'], value = "brown", emoji = "🟫"),
                disnake.SelectOption(label = localization['COLOR_BLACK'], value = "black", emoji = "⬛"),
                disnake.SelectOption(label = localization['COLOR_WHITE'], value = "white", emoji = "⬜"),
            ]
            @disnake.ui.select(options = options)
            async def embedColor(self,select:disnake.ui.Select,inter:disnake.Interaction):
                with open(f"guildOptions/{inter.guild.id}.json") as file:
                    data = json.load(file)
                    embedColor = int(data['embedColor'],16)

                if select.values == ["red"]:
                    data['embedColor'] = "0xFF0000"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)

                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_RED']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["orange"]:
                    data['embedColor'] = "0xFF5F15"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_ORANGE']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["yellow"]:
                    data['embedColor'] = "0xFFFF00"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_YELLOW']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["green"]:
                    data['embedColor'] = "0x00b100"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_GREEN']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["blue"]:
                    data['embedColor'] = "0x0096FF"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_BLUE']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["purple"]:
                    data['embedColor'] = "0xA020F0"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_PURPLE']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["brown"]:
                    data['embedColor'] = "0x8B4513"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_BROWN']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["black"]:
                    data['embedColor'] = "0x000000"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_BLACK']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)

                elif select.values == ["white"]:
                    data['embedColor'] = "0xFFFFFF"
                    embedColor = int(data['embedColor'],16) 
                    with open(f"guildOptions/{inter.guild.id}.json","w") as file:
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = localization['SETTINGS_EMBED_COLOR_CHANGE_TITLE'],
                        description = f"{localization['SETTINGS_EMBED_COLOR_CHANGE_DESCRIPTION']} {localization['COLOR_WHITE']}",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,ephemeral=True)
                
            @disnake.ui.button(label = localization['SETTINGS_BACK_BUTTON_LABEL'])
            async def backButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                with open(f"guildOptions/{inter.guild.id}.json") as file:
                    data = json.load(file)
                    embedColor = int(data['embedColor'],16)

                embed = disnake.Embed(
                    title = localization['SETTINGS_EMBED_TITLE'],
                    description = localization['SETTINGS_EMBED_DESCRIPTION'],
                    color = embedColor
                )
                await inter.response.edit_message(embed=embed,view = MainView(timeout=None))



        class MainView(disnake.ui.View):

            
            @disnake.ui.button(label=localization['SETTINGS_LANGUAGE_BUTTON_LABEL'])
            async def languageButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                with open(f"guildOptions/{inter.guild.id}.json") as file:
                    data = json.load(file)
                    embedColor = int(data['embedColor'],16)

                embed = disnake.Embed(
                    title = localization['SETTINGS_EMBED_TITLE'],
                    description = localization['SETTINGS_EMBED_DESCRIPTION'],
                    color = embedColor
                )
                
                await inter.response.edit_message(embed=embed,view = LanguageView())
            @disnake.ui.button(label=localization['SETTINGS_EMBED_COLOR_BUTTON_LABEL'])
            async def embedButton(self,button:disnake.ui.Button,inter:disnake.Interaction):
                with open(f"guildOptions/{inter.guild.id}.json") as file:
                    data = json.load(file)
                    embedColor = int(data['embedColor'],16)

                embed = disnake.Embed(
                    title = localization['SETTINGS_EMBED_TITLE'],
                    description = localization['SETTINGS_EMBED_DESCRIPTION'],
                    color = embedColor
                )
                await inter.response.edit_message(embed=embed,view = EmbedColorView())



        embed = disnake.Embed(
            title = localization['SETTINGS_EMBED_TITLE'],
            description = localization['SETTINGS_EMBED_DESCRIPTION'],
            color = embedColor
        )
        await inter.response.send_message(embed=embed,view=MainView())



def setup(client):
    client.add_cog(ChangeSettings(client))