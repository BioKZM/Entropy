import disnake
import json
from disnake.ext import commands

class ChangeSettings(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.slash_command(name = "ayarlar",description = "Entropy'nin ayarlarını değiştir.")
    async def settings(self,inter,kullanıcı:disnake.Member = None):


        class MainView(disnake.ui.View):

            @disnake.ui.button(label = "Dili Değiştir",style = disnake.ButtonStyle.grey)
            async def changeLanguage(self,inter):
                with open(f"files/serverOptions/{inter.guild.id}") as file:
                    data = json.load(file)
                    embedColor = data['embedColor']
            
                languageEmbed = disnake.Embed(
                    title = "Dil Seçimi",
                    description = "Mevcut dillerden herhangi birini seçerek Entropy'nin dilini değiştirebilirsin.",
                    color = embedColor
                )
                
                await inter.response.edit_message(embed=languageEmbed,view=ChangeLanguageView())

            @disnake.ui.button(label = "Gömülü Mesajların Rengini Değiştir", style = disnake.ButtonStyle.grey)
            async def changeEmbedColor(self,inter):
                with open(f"files/serverOptions/{inter.guild.id}") as file:
                    data = json.load(file)
                    embedColor = data['embedColor']

                embedColorEmbed = disnake.Embed(
                    title = "Renk Değişimi",
                    description = "Mevcut renklerden herhangi birini seçerek Entropy'nin gömülü mesajlarının rengini değiştirebilirsin. Daha çeşitli renkler kullanmak için `/changeColor` komutunu kullanabilirsin.",
                    color = embedColor
                )
                await inter.response.edit_message(embed=embedColorEmbed,view=ChangeEmbedColorView())


        class ChangeLanguageView(disnake.ui.View):

            languageOptions = [
                disnake.SelectOption(label = "Türkçe",value = "tr",description = "Entropy'nin dilini Türkçe'ye çevir!"),
                disnake.SelectOption(label = "English",value = "en",description = "Change Entropy's language to English!")
            ]

            @disnake.ui.select(custom_id = "changeLanguage",options = languageOptions)
            async def selectView(self,select:disnake.ui.Select, inter:disnake.Interaction):
                
                if select.values == ["tr"]:
                    embed = disnake.Embed(
                        title = "Başarılı!",
                        description = "Entropy'nin dili başarıyla Türkçe'ye çevrildi.",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                elif select.values == ["en"]:
                    embed = disnake.Embed(
                        title = "Success!",
                        description = "Entropy's language is successfully changed to English.",
                        color = embedColor,
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

        class ChangeEmbedColorView(disnake.ui.View):
            colorOptions = [
                disnake.SelectOption(label = "Kırmızı",value = "kırmızı",emoji = "🟥"),
                disnake.SelectOption(label = "Turuncu",value = "turuncu",emoji = "🟧"),
                disnake.SelectOption(label = "Sarı",value = "sarı",emoji = "🟨"),
                disnake.SelectOption(label = "Yeşil",value = "yeşil",emoji = "🟩"),
                disnake.SelectOption(label = "Mavi",value = "mavi",emoji = "🟦"),
                disnake.SelectOption(label = "Mor",value = "mor",emoji = "🟪"),
                disnake.SelectOption(label = "Kahverengi",value = "kahverengi",emoji = "🟫"),
                disnake.SelectOption(label = "Siyah",value = "siyah",emoji = "⬛"),
                disnake.SelectOption(label = "Beyaz",value = "beyaz",emoji = "⬜")
            ]

            @disnake.ui.select(custom_id = "changeEmbedColor",options = colorOptions)
            async def changeEmbedColorView(self,select:disnake.ui.Select,inter : disnake.Interaction):

                with open(f"files/serverOptions/{inter.guild.id}") as file:
                    data = json.load(file)
                    embedColor = data['embedColor']

                
                if select.values == "kırmızı":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0xFF0000"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)



                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)




                if select.values == "turuncu":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0xFF5F15"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)

                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "sarı":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0xFFFF00"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "yeşil":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0x00b100"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "mavi":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0x0096FF"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "mor":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0xA020F0"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "kahverengi":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0x8B4513"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "siyah":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0x000000"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

                if select.values == "beyaz":
                    with open(f"files/serverOptions/{inter.guild.id}.json","w") as file:
                        data['embedColor'] = "0xFFFFF"
                        embedColor = int(data['embedColor'],16)
                        json.dump(data,file,indent=4)
                    embed = disnake.Embed(
                        title = "Başarılı",
                        description = f"Gömülü mesajların rengi `{select.values}` renge değiştirildi.",
                        color = embedColor
                    )
                    await inter.response.send_message(embed=embed,hidden=True)

        with open(f"files/serverOptions/{inter.guild.id}") as file:
                    data = json.load(file)
                    embedColor = data['embedColor']

        embed = disnake.Embed(
                title = "Ayarlar",
                description = "Entropy'nin ayarlarını değiştirmek için aşağıdaki butonları kullan.",
                color = embedColor
            )

        await inter.response.send_message(embed = embed,view=MainView())


def setup(client):
    client.add_cog(ChangeSettings(client))
