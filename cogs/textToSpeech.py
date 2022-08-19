import disnake
import json
from gtts import gTTS
from disnake.ext import commands

class TextToSpeech(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.slash_command(name = "speak")
    async def speak(self,inter):
        pass

    @speak.sub_command(name="en",description = "Make me talk in English")
    async def en(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "en-US"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)


    @speak.sub_command(name="tr",description = "Make me talk in Turkish")
    async def tr(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "tr"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)


    @speak.sub_command(name="ja",description = "Make me talk in Japanese")
    async def ja(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "ja"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)


    @speak.sub_command(name="es",description = "Make me talk in Spanish")
    async def es(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "es"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)

    @speak.sub_command(name="it",description = "Make me talk in Italian")
    async def it(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "it"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)
        

    @speak.sub_command(name="de",description = "Make me talk in German")
    async def de(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "de"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)

    @speak.sub_command(name="ru",description = "Make me talk in Russian")
    async def ru(self,inter,text):
        """
        Parameters
        ----------
        text : Enter the text that you want to say
        """

        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}.json") as file:
            data = json.load(file)
            embedColor = int(data['embedColor'],16)
            lang = data['language']

        with open(f"localization/{lang}.json") as file:
            localization = json.load(file)
        
        language = "ru"
        tts = gTTS(text=text,lang=language,slow=False)
        location = f"guilds/{inter.guild.id}/files/TTS/tts.mp3"
        tts.save(location)
        voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        channel = inter.author.voice.channel
        if voice is None or not voice.is_connected():
            await channel.connect()
            voice = disnake.utils.get(self.client.voice_clients, guild=inter.guild)
        voice.play(disnake.FFmpegOpusAudio(location))

        embed = disnake.Embed(
            title = localization['TEXT_TO_SPEECH_EMBED_TITLE'],
            description = text,
            color = embedColor
        )
        embed.set_author(name = inter.author.display_name, icon_url = inter.author.display_avatar.url)

        await inter.response.send_message(embed=embed)



def setup(client):
    client.add_cog(TextToSpeech(client))