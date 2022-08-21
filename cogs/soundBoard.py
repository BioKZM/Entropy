import disnake
import json
import re
from disnake.ext import commands
from requests import get


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="soundboard")
    async def soundboard(self, inter):
        pass

    @soundboard.sub_command(name="presets",
                            description="Add presets for Soundboard")
    async def prefix(
        self,
        inter,
        slot_1: str = None,
        slot_2: str = None,
        slot_3: str = None,
        slot_4: str = None,
        slot_5: str = None,
        slot_6: str = None,
        slot_7: str = None,
        slot_8: str = None,
        slot_9: str = None,
        slot_10: str = None,
    ):
        """
        Parameters
		----------
		slot_1 : Slot 1
		slot_2 : Slot 2
		slot_3 : Slot 3
		slot_4 : Slot 4
		slot_5 : Slot 5
		slot_6 : Slot 6
		slot_7 : Slot 7
		slot_8 : Slot 8
		slot_9 : Slot 9
		slot_10 : Slot 10
        """
        with open(f"guilds/{inter.guild.id}/options/{inter.author.id}.json") as file:
            data = json.load(file)
            language = data['language']
            embedColor = int(data['embedColor'],16)

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        list = [
            slot_1, slot_2, slot_3, slot_4, slot_5, slot_6, slot_7, slot_8,
            slot_9, slot_10
        ]

        embed = disnake.Embed(
            title=localization['SOUNDBOARD_ADD_SLOT_EMBED_TITLE'],
            description=localization['SOUNDBOARD_ADD_SLOT_EMBED_DESCRIPTION'],
            color=embedColor,
        )
        for slot in list:
            if not slot == None:
                index = list.index(slot)
                data[f"slot_{index+1}"] = slot

        with open(f"guilds/{inter.guild.id}/files/presets/{inter.author.id}.json", "w") as file:
            json.dump(data, file, indent=4)

        for key, value in data.items():
            embed.add_field(name=key, value=value, inline=False)
        await inter.response.send_message(embed=embed)

    @soundboard.sub_command(name="show",
                            description="View your presets")
    async def show(self, inter):
        with open(f"guilds/{inter.guild.id}/options/{inter.author.id}.json") as file:
            data = json.load(file)
            language = data['language']
            embedColor = int(data['embedColor'],16)

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        with open(f"guilds/{inter.guild.id}/files/presets/{inter.author.id}.json") as file:
            presets = json.load(file)

        embed = disnake.Embed(
            title=localization['SOUNDBOARD_PRESETS_EMBED_TITLE'],
            description=['SOUNDBOARD_PRESETS_EMBED_DESCRIPTION'],
            color=embedColor
        )

        for key, value in presets.items():
            embed.add_field(name=key, value=value, inline=False)

        await inter.response.send_message(embed=embed)

    @soundboard.sub_command(
        name="play",
        description="Play sounds from presets or MyInstants links")
    async def play(self, inter, link: str):
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}") as file:
            data = json.load(file)
            language = data['language']
            embedColor = data['embedColor']

        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        # list = [
        #     "slot_1",
        #     "slot_2",
        #     "slot_3",
        #     "slot_4",
        #     "slot_5",
        #     "slot_6",
        #     "slot_7",
        #     "slot_8",
        #     "slot_9",
        #     "slot_10",
        # ]
        try:
            link = int(link)
            if link in range(1, 11):
                sayı = link
                with open(f"guilds/{inter.guild.id}/files/presets/{inter.author.id}.json") as file:
                    data = json.load(file)
                    if not data[f'slot_{sayı}'] == None:
                        link = data[f'slot_{sayı}']
        except:
            pass
        page = get(link)
        list = []
        sayı = 0
        okuma = page.text

        a = re.search('"og:title".* -', okuma).span()
        title = okuma[a[0] + 20:a[1] - 2]
        for i in okuma.split():
            list.append(i)
            if i.startswith('property="og:audio"'):
                sayı = list.index('property="og:audio"')

        newLink = list[sayı + 1]
        scrappedLink = newLink[9:-1]

        channel = inter.author.voice.channel
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients,
                                      guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(scrappedLink))

        embed = disnake.Embed(
            title=localization['SOUNDBOARD_PLAY_EMBED_TITLE'],
            description="\n",
            color=embedColor)
        embed.add_field(name=localization['SOUNDBOARD_PLAY_ADD_FIELD_TITLE'],value=title,inline=False)
        embed.add_field(name=localization['SOUNDBOARD_PLAY_ADD_FIELD_LINK'],value=link,inline=False)
        await inter.response.send_message(embed=embed)


def setup(client):
    client.add_cog(Test(client))
